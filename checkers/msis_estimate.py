"""Cost of the lattice attack on a SIS instance. Standard library only.

A port of `SIS.lattice` of the lattice estimator (github.com/malb/lattice-estimator, commit
1d5c3f5c2365ea41c536805626d3f937c4412e55) with its defaults: the cost model MATZOV for lattice
reduction (list decoding, classical) and the geometric series assumption for the shape of a
reduced basis. The functions below follow estimator/sis_lattice.py, estimator/reduction.py,
estimator/simulator.py, estimator/prob.py and estimator/util.py function by function, including
the estimator's own search over the block size and over the number of ignored columns.

Three deliberate differences from calling the estimator directly:

1. Columns. An attacker may ignore columns, and the estimator's search over ignored columns does
   not find the cheap region when the instance has several hundred thousand of them. So the
   instance is costed with m_used = min(m, m_default) columns, where m_default is the number the
   estimator itself takes when m is left unset: 2*ceil(n*log(q)/log(2*bound + 1)) for the
   infinity norm and 2*ceil(n*log2(q)) for the Euclidean norm.
2. The minimum. The estimator searches for a local minimum over the block size and the number of
   ignored columns, and where that search stops moves the answer by up to a few tenths of a bit.
   `estimate` takes the minimum over the whole range instead (every block size; for each, a
   coarse pass over the ignored columns and then a pass with step one), so that
   the answer does not depend on a search path and is never above the estimator's own.
   `estimate_like_estimator` keeps the estimator's search, for comparison.
3. Arithmetic. Costs are kept as base-2 logarithms in double precision, so nothing overflows.

Reference points (this file / the estimator): Dilithium2_MSIS_WkUnf 2^152.16 at block size 427
with estimate_like_estimator (the estimator prints 2^152.2, block size 427, sieve dimension 433);
the instance of the paper, rank 4544 with bound about 2^187.31 over the order of BN254,
2^103.59 at block size 242 with estimate_like_estimator and 2^103.53 with estimate (the paper
reports about 2^103.5 at block size 242).

    estimate(n, q, m, length_bound, norm="oo") -> dict with log2_rop, beta, eta, zeta, d, ...
"""
import math

INF = float("inf")
NN_A = 0.29613500308205365     # MATZOV, "list_decoding-classical": log2(cost) = a*beta + b
NN_B = 20.387885985467914
BETA_SEARCH_MAX = 2 ** 16
SUCCESS = 0.99
_SMALL = ((2, 1.02190), (5, 1.01862), (10, 1.01616), (15, 1.01485), (20, 1.01420), (25, 1.01342),
          (28, 1.01331), (40, 1.01295))


def _delta(beta):
    """Root-Hermite factor of BKZ with block size beta (reduction.ReductionCost._delta)."""
    if beta <= 2:
        return 1.0219
    if beta < 40:
        for i in range(1, len(_SMALL)):
            if _SMALL[i][0] > beta:
                return _SMALL[i - 1][1]
    if beta == 40:
        return _SMALL[-1][1]
    return (beta / (2 * math.pi * math.e) * (math.pi * beta) ** (1.0 / beta)) ** (1.0 / (2 * (beta - 1)))


def delta(beta):
    return _delta(int(round(beta)))


def beta_from_delta(d):
    """Least block size whose root-Hermite factor is at most d (reduction._beta_find_root)."""
    if _delta(40) < d:
        return 40
    if d < _delta(BETA_SEARCH_MAX):
        return INF
    lo, hi = 40.0, float(BETA_SEARCH_MAX)       # _delta is decreasing on [40, oo)
    for _ in range(200):
        mid = (lo + hi) / 2
        if _delta(mid) > d:
            lo = mid
        else:
            hi = mid
    return int(math.ceil(hi - 1e-8))


def d4f(beta):
    """Dimensions for free (reduction.Kyber.d4f)."""
    return max(beta * math.log(4 / 3.0) / math.log(beta / (2 * math.pi * math.e)), 0.0)


def _log2add(a, b):
    if a == -INF:
        return b
    if b == -INF:
        return a
    hi, lo = (a, b) if a >= b else (b, a)
    return hi + math.log2(1 + 2 ** (lo - hi))


_LOG2_C = -math.log2(1.0 - 2 ** (-NN_A))      # C = 1/(1 - 2^-a), the progressive overhead


def log2_reduction(beta, d):
    """log2 of the cost of BKZ-beta in dimension d (reduction.Kyber.__call__ with MATZOV's constants)."""
    if beta < 20:
        raise ValueError("block size below 20 is not costed")
    svp_calls = max(d - beta, 1)
    beta_ = beta - d4f(beta)
    gates = _LOG2_C + math.log2(svp_calls) + _LOG2_C + NN_A * beta_ + NN_B
    return _log2add(3 * math.log2(d), gates)


def short_vectors(beta, d):
    """(log2 rho, log2 cost, log2 N, sieve_dim) of producing many short vectors (reduction.GJ21.short_vectors)."""
    beta_ = beta - math.floor(d4f(beta))
    sieve_dim = beta_
    if beta < d:
        sieve_dim = min(d, math.floor(beta_ + (math.log2(d - beta) + _LOG2_C) / NN_A))
    log2_rho = 0.5 * math.log2(4 / 3.0) + (sieve_dim - 1) * (math.log2(delta(sieve_dim)) - math.log2(delta(beta)))
    log2_n = 0.2075 * sieve_dim
    if log2_n < 1000:
        log2_n = math.log2(math.floor(2 ** log2_n)) if log2_n < 1000 and 2 ** log2_n >= 1 else log2_n
    sieve = _LOG2_C + NN_A * sieve_dim + NN_B
    return log2_rho, _log2add(log2_reduction(beta, d), sieve), log2_n, sieve_dim


def _log2_erf(x_log2):
    """log2(erf(x)) for x = 2**x_log2, in double precision; -inf when it underflows."""
    if x_log2 > 6:
        return 0.0
    x = 2.0 ** x_log2
    # the estimator computes 1 - 2*cdf(-x) in 53 bits, which is 0 once erf(x) < 2^-53
    v = 1.0 - 2.0 * (0.5 * (1.0 + math.erf(-x)))
    return math.log2(v) if v > 0 else -INF


def _log2_amplify(log2_p):
    """log2 of the number of trials to reach success probability 0.99 (prob.amplify)."""
    if log2_p == -INF:
        return INF
    p = 2.0 ** log2_p
    if SUCCESS < p:
        return 0.0
    if log2_p < -2047:                           # the estimator's precision is capped at 2048 bits
        return INF
    if p > 1e-12:
        return math.log2(math.ceil(math.log(1 - SUCCESS) / math.log1p(-p)))
    return math.log2(-math.log(1 - SUCCESS)) - log2_p


def cost_infinity(beta, n, q, m, bound, zeta):
    """One evaluation of the attack with an infinity-norm bound (sis_lattice.SISLattice.cost_infinity)."""
    out = {"log2_rop": INF, "beta": beta, "zeta": zeta}
    d = m
    d_ = d - zeta
    if d_ < beta or beta < 2:
        return out
    log2_q = math.log2(q)
    log2_b = math.log2(bound)
    log_vol = log2_q * n                                   # GSA with d_ - (d_ - n) = n q-vectors
    log2_len0 = (d_ - 1) * math.log2(delta(beta)) + log_vol / d_      # sqrt(r[0])
    log2_rho, log2_cost, log2_n, sieve_dim = short_vectors(beta, d_)
    if d * bound * bound <= q * q:                         # sqrt(d)*bound <= q: one short vector from the sieve
        log2_sigma = log2_rho + log2_len0 - 0.5 * math.log2(d_)
        coords = d_
    else:                                                  # as for Dilithium: a vector of the reduced basis
        coords = max(d_, sieve_dim)
        log2_sigma = log2_len0 - 0.5 * math.log2(coords)
    log2_trial = coords * _log2_erf(log2_b - 0.5 - log2_sigma)
    log2_prob = min(0.0, log2_trial + log2_n)
    rep = _log2_amplify(log2_prob)
    if rep == INF:
        return out
    out.update(log2_rop=log2_cost + rep, log2_red=log2_reduction(beta, d_), eta=sieve_dim, d=d_,
               log2_prob=log2_prob, log2_repeat=rep)
    return out


class _LocalMinimum:
    """The estimator's search for a local minimum (util.local_minimum), step for step."""

    def __init__(self, start, stop, precision=1):
        self.precision = precision
        self.orig = (start, stop)
        start = math.ceil(start / precision)
        stop = math.floor(stop / precision)
        if stop < start:
            raise ValueError("empty search range")
        self.start, self.stop = start, stop - 1
        self.low, self.high = start, stop - 1
        self.direction = -1
        self.last_x = None
        self.next_x = self.stop
        self.best_x, self.best_y = None, None
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        if self.next_x is not None and self.next_x not in self.seen and self.low <= self.next_x <= self.high:
            self.last_x = self.next_x
            self.next_x = None
            return self.last_x * self.precision
        raise StopIteration

    def update(self, res):
        self.seen.add(self.last_x)
        if self.best_x is None:
            self.best_x, self.best_y = self.last_x, res
        if res["log2_rop"] <= self.best_y["log2_rop"]:
            self.best_x, self.best_y = self.last_x, res
            if abs(self.direction) != 1:
                self.direction = -1
                self.next_x = self.last_x - 1
            elif self.direction == -1:
                self.direction = -2
                self.stop = self.last_x
                self.next_x = math.ceil((self.start + self.stop) / 2)
            elif self.direction == 1:
                self.direction = 2
                self.start = self.last_x
                self.next_x = math.floor((self.start + self.stop) / 2)
        else:
            if self.direction == -1:
                self.direction = 1
                self.next_x = self.last_x + 2
            elif self.direction == 1:
                self.next_x = None
            elif self.direction == -2:
                self.start = self.last_x
                self.next_x = math.ceil((self.start + self.stop) / 2)
            elif self.direction == 2:
                self.stop = self.last_x
                self.next_x = math.floor((self.start + self.stop) / 2)
        if self.next_x == self.last_x:
            self.next_x = None

    def neighborhood(self):
        x = self.best_x * self.precision
        return range(max(self.orig[0], x - self.precision), min(self.orig[1], x + self.precision))


def cost_euclidean(n, q, m, bound):
    """The attack with a Euclidean bound (sis_lattice.SISLattice.cost_euclidean)."""
    if bound >= q:
        raise ValueError("SIS trivially easy: the norm bound is at least q")
    log2_q, log2_b = math.log2(q), math.log2(bound)
    log_delta = log2_b ** 2 / (4 * n * log2_q)
    d = min(math.floor(math.sqrt(n * log2_q / log_delta)), m)
    dl = 2 ** ((1.0 / (d - 1)) * (log2_b - (n / d) * log2_q))
    beta = beta_from_delta(dl) if dl >= 1 else INF
    possible = beta <= d
    if not possible:
        beta = d
    ln_q = math.log(q)
    log_a_sq = math.log(n * ln_q)
    log_b_sq = math.log(d) + 2 * (n / d) * ln_q
    if log_a_sq <= log_b_sq:
        ok = math.log(bound) > 0.5 * log_a_sq
    else:
        ok = math.log(bound) > 0.5 * log_b_sq
    out = {"beta": beta, "d": d, "zeta": 0, "eta": beta, "tag": "euclidean", "delta": dl,
           "log2_rop": log2_reduction(beta, d) if (ok and possible and beta >= 20) else INF}
    return out


def cost_zeta(zeta, n, q, m, bound):
    """Best block size for a fixed number of ignored columns (sis_lattice.SISLattice.cost_zeta)."""
    base = cost_euclidean(n, q, m, 2 if bound == 1 else bound)
    try:
        it = _LocalMinimum(40, base["beta"] + 1, precision=2)
    except ValueError:
        return {"log2_rop": INF, "beta": base["beta"], "zeta": zeta}
    for beta in it:
        it.update(cost_infinity(beta, n, q, m, bound, zeta))
    for beta in it.neighborhood():
        it.last_x = it.last_x          # the estimator updates with the stale position; only the cost matters
        res = cost_infinity(beta, n, q, m, bound, zeta)
        if res["log2_rop"] <= it.best_y["log2_rop"]:
            it.best_y = res
    return it.best_y if it.best_y is not None else {"log2_rop": INF, "beta": base["beta"], "zeta": zeta}


def default_m(n, q, bound, norm):
    """The number of columns the estimator takes when m is unset (sis_parameters.SISParameters)."""
    if norm == "oo":
        return 2 * math.ceil(n * math.log(q) / math.log(2 * bound + 1))
    return 2 * math.ceil(n * math.log2(q))


def _instance(n, q, m, length_bound, norm):
    n, q, length_bound = int(n), int(q), int(length_bound)
    norm = "oo" if norm in ("oo", 0, "inf") else 2
    m_default = default_m(n, q, length_bound, norm)
    m_used = m_default if m is None else min(int(m), m_default)
    if n < 1 or m_used <= n or length_bound < 1:
        raise ValueError("instance out of range")
    if norm == "oo" and 2 * length_bound >= q - 1:
        raise ValueError("SIS trivially easy: the norm bound is at least (q-1)/2")
    return n, q, length_bound, norm, m_used, m_default


def estimate_like_estimator(n, q, m, length_bound, norm="oo"):
    """The estimator's own search for a local minimum (sis_lattice.SISLattice.__call__)."""
    n, q, length_bound, norm, m_used, m_default = _instance(n, q, m, length_bound, norm)
    if norm == 2:
        out = cost_euclidean(n, q, m_used, length_bound)
    else:
        it = _LocalMinimum(0, m_used)
        for zeta in it:
            it.update(cost_zeta(zeta, n, q, m_used, length_bound))
        first = cost_zeta(0, n, q, m_used, length_bound)
        out = dict(first if first["log2_rop"] < it.best_y["log2_rop"] else it.best_y)
        out["tag"] = "infinity"
    out.update(m_used=m_used, m_default=m_default)
    return out


def estimate(n, q, m, length_bound, norm="oo"):
    """Cost of the lattice attack on SIS with rank n, modulus q, m columns and the given norm bound.

    norm is "oo" (infinity norm) or 2 (Euclidean norm). Returns a dict; log2_rop is the base-2
    logarithm of the number of operations, float("inf") when the attack does not apply. For the
    infinity norm it is the minimum over the block size (40 up to the block size the Euclidean
    attack needs, plus one) and over the number of ignored columns.
    """
    n, q, length_bound, norm, m_used, m_default = _instance(n, q, m, length_bound, norm)
    if norm == 2:
        out = cost_euclidean(n, q, m_used, length_bound)
        out.update(m_used=m_used, m_default=m_default)
        return out
    top = cost_euclidean(n, q, m_used, 2 if length_bound == 1 else length_bound)["beta"] + 1
    best = {"log2_rop": INF, "beta": top, "zeta": 0}
    for beta in range(40, top + 1):
        if m_used < beta:
            break
        # The cost jumps where the success probability crosses 0.99, and the minimum sits at that
        # edge. A coarse pass over the ignored columns finds the neighbourhood, a pass with step
        # one finds the edge.
        here = {"log2_rop": INF, "beta": beta, "zeta": 0}
        for zeta in range(0, m_used - beta + 1, 32):
            res = cost_infinity(beta, n, q, m_used, length_bound, zeta)
            if res["log2_rop"] < here["log2_rop"]:
                here = res
        if here["log2_rop"] == INF:
            continue
        z0 = here["zeta"]
        for zeta in range(max(0, z0 - 32), min(m_used - beta, z0 + 32) + 1):
            res = cost_infinity(beta, n, q, m_used, length_bound, zeta)
            if res["log2_rop"] < here["log2_rop"]:
                here = res
        if here["log2_rop"] < best["log2_rop"]:
            best = here
    out = dict(best)
    out.update(tag="infinity", m_used=m_used, m_default=m_default)
    return out
