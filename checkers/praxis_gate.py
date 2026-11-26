"""Organizer-owned gate for the Praxis ciphertext challenge. Standard library only.

Reads one declared input from stdin: {"params": ["<part>", ...]}. The parts, joined, are the
exact text of the submitted params.json (tools/pack.py writes them). The gate parses that
text, evaluates the protected model (checkers/model.json) on it with exact arithmetic
(checkers/praxis_model.py), costs the Module-SIS instance with the pinned estimator
(checkers/msis_estimate.py), and reports:

  passed           every rule in force holds and the two objectives could be computed
  ciphertext_mib   OBJECTIVE 1, SIZE: ciphertext size in MiB, rounded up; -1 when passed is false
  time_mmul        OBJECTIVE 2, TIME: one encryption plus one expected decryption, in millions of field
                   multiplications, rounded up; -1 when passed is false
  enc_mmul, dec_mmul   the two parts of the time, each rounded up, for the reader; not objectives
  tier             "parameters" when the submission changes no rule, "amended" otherwise
  amended, dropped the model entries the submission replaces, adds or drops
  failed           the rules that do not hold (false, undecided, or not evaluable)
  params_sha256    SHA-256 of the text it checked, so a reader can see that the scored
                   text is the submitted params.json

A pass on tier "parameters" means: these parameters satisfy every condition under which the
paper proves its theorems, and the paper's own size formula gives this ciphertext size.
A pass on tier "amended" means only that the AMENDED rules hold for these parameters. Whether
the amended rules are theorems is decided in review, not here.
"""
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import re
import sys
from fractions import Fraction

# Fixed protected path inside the checker sandbox, never a path supplied by the requester.
SNAPSHOT = Path("/snapshot/files")
MAX_PARAMS_BYTES = 15000
MAX_OUTPUT_BYTES = 12000   # the runner refuses a result above 16384 canonical bytes
MAX_AMEND = 24
MAX_EXTRA_PARAMS = 24
RULE_ID = re.compile(r"^[A-Z][A-Za-z0-9_]{0,15}$")
NAME_ID = re.compile(r"^[A-Za-z][A-Za-z0-9_]{0,23}$")
RESERVED = {"pi", "floor", "ceil", "sqrt", "exp", "abs", "min", "max", "is_pow2", "is_int", "msis_log2", "up", "down",
            "and", "or", "not"}


def load_module(root, name):
    spec = importlib.util.spec_from_file_location(name, str(root / "checkers" / f"{name}.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def encode(data, part=4000):
    """Text of params.json -> the list of parts a submission declares."""
    text = data.decode("utf-8")
    return [text[i:i + part] for i in range(0, len(text), part)] or [""]


def decode(parts):
    """The declared parts -> the exact bytes of params.json. Raises ValueError."""
    if not isinstance(parts, list) or not all(isinstance(p, str) for p in parts):
        raise ValueError("params must be a list of strings")
    data = "".join(parts).encode("utf-8")
    if len(data) > MAX_PARAMS_BYTES:
        raise ValueError(f"params.json is larger than {MAX_PARAMS_BYTES} bytes")
    return data


def parse(data):
    """Strict JSON: one object, no repeated key, no NaN or Infinity, no floats."""
    def pairs(items):
        seen = {}
        for key, value in items:
            if key in seen:
                raise ValueError(f"the key {key!r} is repeated; a repeated key can be read two ways")
            seen[key] = value
        return seen

    def constant(name):
        raise ValueError(f"{name} is not a JSON value")

    def no_float(text):
        raise ValueError("write every number as a string of digits, 'a' or 'a/b'; a decimal point is not exact")

    try:
        value = json.loads(data.decode("utf-8"), object_pairs_hook=pairs, parse_constant=constant,
                           parse_float=no_float)
    except RecursionError:
        raise ValueError("params.json is nested too deeply") from None
    except json.JSONDecodeError as exc:
        raise ValueError(f"params.json is not JSON: {exc.msg} at line {exc.lineno}") from None
    if not isinstance(value, dict):
        raise ValueError("params.json is not a JSON object")
    return value


def clip(text, limit):
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[:limit - 3] + "..."


def size(value):
    return len(json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(",", ":")))


def build(model, sub, pm):
    """Apply the submission's amendments to the model. Returns (constants, params, defs, funcs, rules,
    amended, dropped). Raises ValueError with the reason."""
    allowed = {"format", "title", "params", "amend", "drop"}
    extra = sorted(set(sub) - allowed)
    if extra:
        raise ValueError(f"unknown top-level key(s): {', '.join(extra)}")
    if sub.get("format") != "praxis-params/1":
        raise ValueError('format must be "praxis-params/1"')
    if not isinstance(sub.get("title", ""), str) or len(sub.get("title", "")) > 300:
        raise ValueError("title must be a string of at most 300 characters")
    params = sub.get("params")
    if not isinstance(params, dict):
        raise ValueError("params must be an object of name: value")
    amend = sub.get("amend", [])
    drop = sub.get("drop", [])
    if not isinstance(amend, list) or not isinstance(drop, list):
        raise ValueError("amend and drop must be lists")
    if len(amend) > MAX_AMEND or len(drop) > MAX_AMEND:
        raise ValueError(f"at most {MAX_AMEND} amendments and {MAX_AMEND} drops")

    constants = {c["id"]: c["value"] for c in model["constants"]}
    base_params = {p["id"]: p["type"] for p in model["parameters"]}
    defs = {d["id"]: dict(d) for d in model["definitions"]}
    funcs = {f["id"]: dict(f) for f in model["functions"]}
    rules = {r["id"]: dict(r) for r in model["rules"]}
    order = [r["id"] for r in model["rules"]]
    amended, dropped = [], []

    for item in drop:
        if not isinstance(item, str) or item not in rules:
            raise ValueError(f"drop names {item!r}, which is not a rule of the model")
        if rules[item].get("protected"):
            raise ValueError(f"rule {item} is protected and cannot be dropped")
        if item in dropped:
            raise ValueError(f"rule {item} is dropped twice")
        dropped.append(item)
    seen = set()
    for item in amend:
        if not isinstance(item, dict) or set(item) - {"id", "kind", "expr", "args"}:
            raise ValueError("an amendment is an object with id, kind, expr and, for a function, args")
        ident, kind, expr = item.get("id"), item.get("kind"), item.get("expr")
        if not isinstance(ident, str) or kind not in ("rule", "def", "func") or not isinstance(expr, str):
            raise ValueError("an amendment needs a string id, a kind (rule, def or func) and a string expr")
        if ident in seen:
            raise ValueError(f"{ident} is amended twice")
        seen.add(ident)
        if ident in dropped:
            raise ValueError(f"{ident} is both dropped and amended")
        if ident in constants or ident in RESERVED:
            raise ValueError(f"{ident} is a fixed constant or a built-in and cannot be amended")
        if ident in params or ident in base_params:
            raise ValueError(f"{ident} is a parameter; give its value under params")
        pm.parse(expr)  # syntax only; raises ModelError
        if kind == "rule":
            if ident in defs or ident in funcs:
                raise ValueError(f"{ident} is not a rule")
            if ident in rules:
                if rules[ident].get("protected"):
                    raise ValueError(f"rule {ident} is protected and cannot be amended")
            else:
                if not RULE_ID.match(ident):
                    raise ValueError(f"a new rule id must match {RULE_ID.pattern}")
                order.append(ident)
            rules[ident] = {"id": ident, "expr": expr}
        elif kind == "def":
            if ident in rules or ident in funcs:
                raise ValueError(f"{ident} is not a definition")
            if ident in defs and defs[ident].get("protected"):
                raise ValueError(f"definition {ident} is protected and cannot be amended")
            if ident not in defs and not NAME_ID.match(ident):
                raise ValueError(f"a new definition id must match {NAME_ID.pattern}")
            defs[ident] = {"id": ident, "expr": expr}
        else:
            args = item.get("args")
            if (not isinstance(args, list) or not 1 <= len(args) <= 4
                    or not all(isinstance(a, str) and NAME_ID.match(a) for a in args) or len(set(args)) != len(args)):
                raise ValueError(f"function {ident} needs args, a list of 1 to 4 distinct names")
            if ident in rules or ident in defs:
                raise ValueError(f"{ident} is not a function")
            if ident not in funcs and not NAME_ID.match(ident):
                raise ValueError(f"a new function id must match {NAME_ID.pattern}")
            funcs[ident] = {"id": ident, "args": args, "expr": expr}
        amended.append(ident)

    changed = bool(amended or dropped)
    names = set(params)
    for name in names:
        if not isinstance(name, str) or not NAME_ID.match(name):
            raise ValueError(f"parameter name {name!r} is not allowed")
        if name in constants or name in defs or name in funcs or name in rules or name in RESERVED:
            raise ValueError(f"{name} is not a parameter: the model defines it")
    unknown = sorted(names - set(base_params))
    missing = sorted(set(base_params) - names)
    if not changed and (unknown or missing):
        raise ValueError("without amendments, params must give exactly the model's parameters"
                         + (f"; unknown: {', '.join(unknown)}" if unknown else "")
                         + (f"; missing: {', '.join(missing)}" if missing else ""))
    if len(unknown) > MAX_EXTRA_PARAMS:
        raise ValueError(f"at most {MAX_EXTRA_PARAMS} new parameters")
    return constants, base_params, params, defs, funcs, rules, order, amended, dropped


def run(inputs, root=SNAPSHOT):
    out = {"passed": False, "ciphertext_mib": -1, "time_mmul": -1, "enc_mmul": -1, "dec_mmul": -1,
           "time_log2": "", "enc_log2": "", "dec_log2": "",
           "ciphertext_bits": "", "gib": "", "tier": "",
           "amended": [], "dropped": [], "failed": [], "first_failed": "", "rules_checked": 0,
           "msis_log2": "", "msis_block": -1, "g1_elements": "", "g2_elements": "",
           "params_sha256": "", "model_sha256": "", "errors": [], "message": ""}
    try:
        pm = load_module(root, "praxis_model")
        est = load_module(root, "msis_estimate")
        model_bytes = (root / "checkers" / "model.json").read_bytes()
        model = json.loads(model_bytes.decode("utf-8"))
        out["model_sha256"] = hashlib.sha256(model_bytes).hexdigest()
    except Exception as exc:  # the protected bundle itself is broken: never a pass
        out["failed"], out["first_failed"] = ["input"], "input"
        out["errors"] = [clip(f"input: the protected model could not be loaded ({type(exc).__name__})", 300)]
        out["message"] = "organizer error: protected bundle unreadable"
        return out
    try:
        data = decode(inputs["params"])
        out["params_sha256"] = hashlib.sha256(data).hexdigest()
        sub = parse(data)
        constants, base_params, params, defs, funcs, rules, order, amended, dropped = build(model, sub, pm)
    except (ValueError, KeyError, TypeError, pm.ModelError) as exc:
        out["failed"], out["first_failed"] = ["input"], "input"
        out["errors"] = [clip(f"input: {exc}", 300)]
        out["message"] = "the declared input is not a readable parameter file"
        return out
    out["amended"], out["dropped"] = amended[:24], dropped[:24]
    out["tier"] = "amended" if (amended or dropped) else "parameters"

    errors = []
    values = {}
    try:
        for name, text in constants.items():
            values[name] = pm.parse_number(text, name)
        for name, text in params.items():
            v = pm.parse_number(text, name)
            if base_params.get(name) == "int" and v.lo.denominator != 1:
                raise pm.ModelError(f"{name} must be an integer")
            if name in base_params and v.lo <= 0:
                raise pm.ModelError(f"{name} must be positive")
            values[name] = v
    except pm.ModelError as exc:
        out["failed"], out["first_failed"] = ["input"], "input"
        out["errors"] = [clip(f"input: {exc}", 300)]
        out["message"] = "a parameter value is not acceptable"
        return out

    msis = {}

    def msis_log2(n, m, bound, norm):
        n_, m_, b_, norm_ = (x.as_int("an argument of msis_log2") for x in (n, m, bound, norm))
        if norm_ not in (0, 2):
            raise pm.ModelError("msis_log2: norm is 0 (infinity) or 2 (Euclidean)")
        if not (1 <= n_ <= 1 << 16 and n_ < m_ <= 1 << 22 and b_ >= 1):
            raise pm.ModelError("msis_log2: instance out of the supported range")
        q = values["q"].lo.numerator
        try:
            res = est.estimate(n_, q, m_, b_, "oo" if norm_ == 0 else 2)
        except Exception as exc:
            raise pm.ModelError(f"msis_log2: the estimator refused the instance ({clip(exc, 120)})") from None
        cost = res.get("log2_rop")
        if not isinstance(cost, (int, float)) or cost != cost:
            raise pm.ModelError("msis_log2: the estimator returned no cost")
        if cost == float("inf"):
            cost = 100000.0
        milli = math.floor(cost * 1000)
        msis["log2"], msis["block"] = milli, res.get("beta")
        return pm.Iv(Fraction(milli, 1000))

    try:
        functions = {name: (f["args"], pm.parse(f["expr"])) for name, f in funcs.items()}
    except pm.ModelError as exc:
        out["failed"], out["first_failed"] = ["input"], "input"
        out["errors"] = [clip(f"input: {exc}", 300)]
        return out
    ev = pm.Evaluator(values, functions, hooks={"msis_log2": msis_log2})
    busy = set()

    def lazy(name, expr):
        def compute():
            if name in busy:
                raise pm.ModelError(f"definition {name} refers to itself")
            busy.add(name)
            try:
                v = ev.ev(pm.parse(expr))
            finally:
                busy.discard(name)
            if not isinstance(v, pm.Iv):
                raise pm.ModelError(f"definition {name} is not a number")
            return v
        return compute

    for name, d in defs.items():
        values[name] = lazy(name, d["expr"])

    failed = []
    checked = 0
    for rid in order:
        if rid in dropped:
            continue
        checked += 1
        try:
            t = ev.ev(pm.parse(rules[rid]["expr"]))
            if not isinstance(t, pm.Tri):
                raise pm.ModelError("a rule must be a condition")
            if t.v is not True:
                failed.append(rid)
                errors.append(f"{rid}: {'does not hold' if t.v is False else 'could not be decided either way'}")
        except pm.ModelError as exc:
            failed.append(rid)
            errors.append(f"{rid}: {exc}")
        except (RecursionError, MemoryError, OverflowError, ZeroDivisionError) as exc:
            failed.append(rid)
            errors.append(f"{rid}: evaluation failed ({type(exc).__name__})")
    out["rules_checked"] = checked
    score = None
    try:
        bits = ev.lookup("size_bits", None).as_int("size_bits")
        score = {name: ev.lookup(ident, None).as_int(name) for name, ident in model["scores"].items()}
        info = {name: ev.lookup(ident, None).as_int(name) for name, ident in model.get("info", {}).items()}
        n1 = ev.lookup("n1", None).as_int("n1")
        n2 = ev.lookup("n2", None).as_int("n2")
        if bits <= 0 or n1 < 0 or n2 < 0 or min(score.values()) <= 0:
            raise pm.ModelError("the ciphertext size and the costs must be positive")
        out["ciphertext_bits"] = str(bits)
        out["gib"] = f"{bits / 8 / 2 ** 30:.4f}"
        out["g1_elements"], out["g2_elements"] = str(n1), str(2 * n2)
        out["time_log2"] = f"{pm.log2_fraction(ev.lookup('enc_mults', None).hi + ev.lookup('dec_mults', None).hi):.2f}"
        out["enc_log2"] = f"{pm.log2_fraction(ev.lookup('enc_mults', None).hi):.2f}"
        out["dec_log2"] = f"{pm.log2_fraction(ev.lookup('dec_mults', None).hi):.2f}"
    except pm.ModelError as exc:
        failed.append("score")
        errors.append(f"score: {exc}")
        score = None
    except (RecursionError, MemoryError, OverflowError, ZeroDivisionError) as exc:
        failed.append("score")
        errors.append(f"score: evaluation failed ({type(exc).__name__})")
        score = None
    if "log2" in msis:
        out["msis_log2"] = f"{msis['log2'] / 1000:.3f}"
        out["msis_block"] = int(msis["block"]) if isinstance(msis.get("block"), int) else -1
    out["failed"] = failed[:24]
    out["first_failed"] = failed[0] if failed else ""
    out["errors"] = [clip(e, 300) for e in errors[:12]]
    if not failed and score is not None:
        out["passed"] = True
        out.update(info)
        out.update(score)
        out["message"] = ("every rule of the paper's model holds for these parameters"
                          if out["tier"] == "parameters" else
                          "the amended rules hold for these parameters; whether the amendments are theorems is decided in review")
    else:
        out["message"] = clip("rules that do not hold: " + ", ".join(failed), 300)
    while size(out) > MAX_OUTPUT_BYTES and len(out["errors"]) > 1:
        out["errors"].pop()
    return out


if __name__ == "__main__":
    print(json.dumps(run(json.load(sys.stdin)), ensure_ascii=True, sort_keys=True))
