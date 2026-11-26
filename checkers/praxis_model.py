"""Exact evaluator for the Praxis cost and admissibility model. Standard library only.

A model is data (checkers/model.json): fixed constants, definitions, functions and rules,
each an arithmetic expression. This module evaluates them for one parameter set.

Arithmetic is exact. Every value is an interval [lo, hi] of rationals (fractions.Fraction);
integers and rationals are points (lo == hi). The only inexact atoms are sqrt, exp and pi,
which return rigorous enclosures. A comparison is TRUE only when it holds for every point of
the intervals involved, FALSE only when it fails for every point, and otherwise UNDECIDED,
which a rule treats as a failure. So a rule that passes here is a true inequality, not a
floating-point accident.

Expression language (Python syntax, parsed with ast, nothing else is accepted):
  integer literals; names; + - * / unary -; ** with an integer exponent; % on integers;
  comparisons < <= > >= == != (chains allowed); and, or, not;
  floor(x) ceil(x) sqrt(x) exp(x) pi min(...) max(...) abs(x) is_pow2(x) is_int(x)
  up(x) down(x)                  the upper and the lower end of the enclosure of x, as exact numbers
  msis_log2(n, m, bound, norm)   norm 0 means the infinity norm, 2 the Euclidean norm
  and calls of functions the model defines.
"""
import ast
from fractions import Fraction
import math

PRECISION_BITS = 320           # sqrt, exp and pi are enclosed to about 2**-320 relative width
MAX_INT_BITS = 400000          # no intermediate integer may exceed this many bits
MAX_EXPONENT = 4096            # |exponent| of ** is at most this
MAX_EXPR_CHARS = 2000
MAX_NODES = 400
# pi to 100 decimals, enclosed between the truncation and the truncation plus one unit
_PI_DIGITS = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
PI_LO = Fraction(int(_PI_DIGITS), 10 ** (len(_PI_DIGITS) - 1))
PI_HI = Fraction(int(_PI_DIGITS) + 1, 10 ** (len(_PI_DIGITS) - 1))


class ModelError(Exception):
    """The expression or the parameter set is not acceptable (never a pass)."""


class Tri:
    """Three-valued truth: True, False or undecided (None)."""
    __slots__ = ("v",)

    def __init__(self, v):
        self.v = v

    def __repr__(self):
        return {True: "TRUE", False: "FALSE", None: "UNDECIDED"}[self.v]


class Iv:
    """A closed interval of rationals."""
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        self.lo = lo if isinstance(lo, Fraction) else Fraction(lo)
        self.hi = self.lo if hi is None else (hi if isinstance(hi, Fraction) else Fraction(hi))
        if self.lo > self.hi:
            raise ModelError("empty interval")
        for x in (self.lo, self.hi):
            if x.numerator.bit_length() > MAX_INT_BITS or x.denominator.bit_length() > MAX_INT_BITS:
                raise ModelError("a number grew beyond the size limit")

    @property
    def exact(self):
        return self.lo == self.hi

    def as_int(self, what):
        if not self.exact or self.lo.denominator != 1:
            raise ModelError(f"{what} must be an exact integer")
        return self.lo.numerator


def _add(a, b):
    return Iv(a.lo + b.lo, a.hi + b.hi)


def _neg(a):
    return Iv(-a.hi, -a.lo)


def _mul(a, b):
    c = (a.lo * b.lo, a.lo * b.hi, a.hi * b.lo, a.hi * b.hi)
    return Iv(min(c), max(c))


def _inv(a):
    if a.lo <= 0 <= a.hi:
        raise ModelError("division by an interval that contains zero")
    return Iv(1 / a.hi, 1 / a.lo)


def _pow(a, e):
    if abs(e) > MAX_EXPONENT:
        raise ModelError("exponent too large")
    if e < 0:
        return _pow(_inv(a), -e)
    if e == 0:
        return Iv(1)
    if a.exact:
        return Iv(a.lo ** e)
    if a.lo >= 0:
        return Iv(a.lo ** e, a.hi ** e)
    if a.hi <= 0:
        lo, hi = a.lo ** e, a.hi ** e
        return Iv(min(lo, hi), max(lo, hi))
    if e % 2:
        return Iv(a.lo ** e, a.hi ** e)
    return Iv(0, max(a.lo ** e, a.hi ** e))


def _round_out(lo, hi):
    """Widen [lo, hi] to dyadic endpoints so that denominators stay bounded."""
    def scale(x):
        bits = PRECISION_BITS + 8
        if x != 0:
            mag = x.numerator.bit_length() - x.denominator.bit_length()
            bits = max(8, bits - mag)
        return bits
    s = max(scale(lo), scale(hi))
    unit = 1 << s
    lo2 = Fraction(math.floor(lo * unit), unit)
    hi2 = Fraction(math.ceil(hi * unit), unit)
    return lo2, hi2


def _sqrt_point(x, up):
    if x < 0:
        raise ModelError("sqrt of a negative number")
    if x == 0:
        return Fraction(0)
    a, b = x.numerator, x.denominator
    # sqrt(a/b) = sqrt(a*b)/b ; scale so that the integer root has PRECISION_BITS bits
    shift = max(0, PRECISION_BITS - (a * b).bit_length() // 2 + 2)
    root = math.isqrt((a * b) << (2 * shift))
    exact = root * root == (a * b) << (2 * shift)
    if up and not exact:
        root += 1
    return Fraction(root, b << shift)


def _sqrt(a):
    return Iv(_sqrt_point(a.lo, False), _sqrt_point(a.hi, True))


def _exp_pos(x):
    """Enclosure (lo, hi) of exp(x) for a rational x >= 0, by the Taylor series with a tail bound."""
    if x > 100000:
        raise ModelError("exp argument too large")
    p = PRECISION_BITS + 64
    one = 1 << p
    a, b = x.numerator, x.denominator
    lo_sum = hi_sum = one
    t_lo = t_hi = one
    k = 0
    limit = 2 * int(x) + 4
    while True:
        k += 1
        t_lo = (t_lo * a) // (b * k)
        t_hi = -((-t_hi * a) // (b * k))
        lo_sum += t_lo
        hi_sum += t_hi
        if k >= limit and t_hi <= 1:
            break
        if k > 2000000:
            raise ModelError("exp did not converge")
    # for k+1 >= 2x the remaining terms are at most t_hi * (1/2 + 1/4 + ...) = t_hi
    hi_sum += t_hi + 1
    return Fraction(lo_sum, one), Fraction(hi_sum, one)


def _exp(a):
    def point(x, up):
        if x >= 0:
            lo, hi = _exp_pos(x)
            return hi if up else lo
        lo, hi = _exp_pos(-x)
        return 1 / lo if up else 1 / hi
    lo, hi = _round_out(point(a.lo, False), point(a.hi, True))
    if lo <= 0:
        lo = point(a.lo, False)
    return Iv(lo, hi)


def _cmp(op, a, b):
    if op == "<":
        return Tri(True) if a.hi < b.lo else Tri(False) if a.lo >= b.hi else Tri(None)
    if op == "<=":
        return Tri(True) if a.hi <= b.lo else Tri(False) if a.lo > b.hi else Tri(None)
    if op == ">":
        return _cmp("<", b, a)
    if op == ">=":
        return _cmp("<=", b, a)
    if op == "==":
        if a.exact and b.exact:
            return Tri(a.lo == b.lo)
        return Tri(False) if a.hi < b.lo or b.hi < a.lo else Tri(None)
    if op == "!=":
        t = _cmp("==", a, b)
        return Tri(None if t.v is None else not t.v)
    raise ModelError("unknown comparison")


_CMP = {ast.Lt: "<", ast.LtE: "<=", ast.Gt: ">", ast.GtE: ">=", ast.Eq: "==", ast.NotEq: "!="}


def parse(expr):
    if not isinstance(expr, str) or not expr.strip():
        raise ModelError("an expression must be a non-empty string")
    if len(expr) > MAX_EXPR_CHARS:
        raise ModelError("expression too long")
    try:
        tree = ast.parse(expr.strip(), mode="eval")
    except (SyntaxError, ValueError, RecursionError, MemoryError):
        raise ModelError("expression is not valid syntax") from None
    count = sum(1 for _ in ast.walk(tree))
    if count > MAX_NODES:
        raise ModelError("expression too large")
    return tree.body


def names_in(expr):
    """Names an expression refers to (variables and called functions)."""
    return sorted({n.id for n in ast.walk(parse(expr)) if isinstance(n, ast.Name)})


class Evaluator:
    def __init__(self, values, functions=None, hooks=None):
        self.values = values            # name -> Iv, or a zero-argument callable that computes it lazily
        self.functions = functions or {}  # name -> (args, parsed expr)
        self.hooks = hooks or {}        # name -> python callable on Iv arguments
        self.depth = 0

    def lookup(self, name, local):
        if local is not None and name in local:
            return local[name]
        if name == "pi":
            return Iv(PI_LO, PI_HI)
        if name not in self.values:
            raise ModelError(f"unknown name {name!r}")
        v = self.values[name]
        if callable(v):
            v = v()
            self.values[name] = v
        return v

    def num(self, node, local=None):
        v = self.ev(node, local)
        if not isinstance(v, Iv):
            raise ModelError("a number was expected")
        return v

    def truth(self, node, local=None):
        v = self.ev(node, local)
        if not isinstance(v, Tri):
            raise ModelError("a condition was expected")
        return v

    def ev(self, node, local=None):
        self.depth += 1
        if self.depth > 200:
            raise ModelError("expression nested too deeply")
        try:
            return self._ev(node, local)
        finally:
            self.depth -= 1

    def _ev(self, node, local):
        if isinstance(node, ast.Constant):
            if type(node.value) is int:
                return Iv(node.value)
            raise ModelError("only integer literals are allowed; write a rational as a/b")
        if isinstance(node, ast.Name):
            return self.lookup(node.id, local)
        if isinstance(node, ast.UnaryOp):
            if isinstance(node.op, ast.USub):
                return _neg(self.num(node.operand, local))
            if isinstance(node.op, ast.UAdd):
                return self.num(node.operand, local)
            if isinstance(node.op, ast.Not):
                t = self.truth(node.operand, local)
                return Tri(None if t.v is None else not t.v)
            raise ModelError("operator not allowed")
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, ast.Pow):
                base = self.num(node.left, local)
                e = self.num(node.right, local).as_int("an exponent")
                return _pow(base, e)
            a, b = self.num(node.left, local), self.num(node.right, local)
            if isinstance(node.op, ast.Add):
                return _add(a, b)
            if isinstance(node.op, ast.Sub):
                return _add(a, _neg(b))
            if isinstance(node.op, ast.Mult):
                return _mul(a, b)
            if isinstance(node.op, ast.Div):
                return _mul(a, _inv(b))
            if isinstance(node.op, ast.Mod):
                x, m = a.as_int("the left side of %"), b.as_int("the right side of %")
                if m <= 0:
                    raise ModelError("% needs a positive modulus")
                return Iv(x % m)
            raise ModelError("operator not allowed")
        if isinstance(node, ast.Compare):
            left = self.num(node.left, local)
            out = Tri(True)
            for op, right_node in zip(node.ops, node.comparators):
                if type(op) not in _CMP:
                    raise ModelError("comparison not allowed")
                right = self.num(right_node, local)
                t = _cmp(_CMP[type(op)], left, right)
                if t.v is False:
                    return Tri(False)
                if t.v is None:
                    out = Tri(None)
                left = right
            return out
        if isinstance(node, ast.BoolOp):
            vals = [self.truth(v, local).v for v in node.values]
            if isinstance(node.op, ast.And):
                return Tri(False if False in vals else None if None in vals else True)
            return Tri(True if True in vals else None if None in vals else False)
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name) or node.keywords:
                raise ModelError("only plain function calls are allowed")
            name = node.func.id
            args = [self.num(a, local) for a in node.args]
            return self.call(name, args)
        raise ModelError(f"syntax not allowed: {type(node).__name__}")

    def call(self, name, args):
        def need(n):
            if len(args) != n:
                raise ModelError(f"{name} takes {n} argument(s)")
        if name == "floor":
            need(1)
            return Iv(math.floor(args[0].lo), math.floor(args[0].hi))
        if name == "ceil":
            need(1)
            return Iv(math.ceil(args[0].lo), math.ceil(args[0].hi))
        if name == "sqrt":
            need(1)
            return _sqrt(args[0])
        if name == "exp":
            need(1)
            return _exp(args[0])
        if name == "abs":
            need(1)
            a = args[0]
            if a.lo >= 0:
                return a
            if a.hi <= 0:
                return _neg(a)
            return Iv(0, max(-a.lo, a.hi))
        if name in ("min", "max"):
            if not args:
                raise ModelError(f"{name} needs arguments")
            f = min if name == "min" else max
            return Iv(f(a.lo for a in args), f(a.hi for a in args))
        if name == "up":
            need(1)
            return Iv(args[0].hi)
        if name == "down":
            need(1)
            return Iv(args[0].lo)
        if name == "is_pow2":
            need(1)
            x = args[0].as_int("the argument of is_pow2")
            return Tri(x >= 1 and x & (x - 1) == 0)
        if name == "is_int":
            need(1)
            if args[0].exact:
                return Tri(args[0].lo.denominator == 1)
            return Tri(None)
        if name in self.hooks:
            return self.hooks[name](*args)
        if name in self.functions:
            params, body = self.functions[name]
            need(len(params))
            return self.ev(body, dict(zip(params, args)))
        raise ModelError(f"unknown function {name!r}")


def parse_number(text, what):
    """A parameter value: an integer, or a rational 'a/b', given as a string of digits."""
    if isinstance(text, bool) or not isinstance(text, (str, int)):
        raise ModelError(f"{what}: a parameter is an integer or a string 'a' or 'a/b'")
    s = str(text).strip()
    if len(s) > 4000:
        raise ModelError(f"{what}: number too long")
    neg = s.startswith("-")
    body = s[1:] if neg else s
    parts = body.split("/")
    if len(parts) not in (1, 2) or not all(p.isascii() and p.isdigit() for p in parts):
        raise ModelError(f"{what}: not an integer or a rational a/b in decimal digits")
    num = int(parts[0])
    den = int(parts[1]) if len(parts) == 2 else 1
    if den == 0:
        raise ModelError(f"{what}: zero denominator")
    v = Fraction(num, den)
    return Iv(-v if neg else v)


def log2_fraction(x):
    """log2 of a positive rational as a float, safe for huge numerators."""
    if x <= 0:
        return float("-inf")
    n, d = x.numerator, x.denominator
    def lg(i):
        b = i.bit_length()
        if b <= 1000:
            return math.log2(i)
        return (b - 1000) + math.log2(i >> (b - 1000))
    return lg(n) - lg(d)
