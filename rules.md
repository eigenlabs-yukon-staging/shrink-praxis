# Shrink Praxis

Participants come up with a better witness encryption scheme than Praxis: a smaller ciphertext, less time. "Praxis: Practical Witness Encryption for NP" (D. Tse, N. Vanjani, P. Vesely; Cryptology ePrint Archive 2026/2971, arXiv 2611.28552) encrypts to any NP statement and is proved extractable in the bilinear generic group and random oracle models under Module-SIS. At 100-bit security, for its reference statement (a Groth16 verifier on BN254), its ciphertext is 7.88 GiB. A submission is a parameter set of Praxis, and optionally an amendment of the scheme or of the conditions under which it is proved secure, with its proof. It is scored on two objectives: size, the ciphertext size, and time, the cost of one encryption plus one expected decryption. Lower is better on each, and the result is a Pareto frontier. Everything else is held at Praxis's values.

## Problem and model

### What is fixed

- The statement: the Boolean quadratic system of the paper's Groth16 verifier, with $N = 391693$ Boolean unknowns, 1692 constraints before padding and at most 2047 products per constraint.
- The groups: BN254, of order $q = 21888242871839275222246405745257275088548364400416034343698204186575808495617$. An element of $\mathbb{G}_1$ takes 255 bits and one of $\mathbb{G}_2$ 512 bits; the element of $\mathbb{G}_T$, the seed and the masked message take 3280 bits together.
- The security level: $\lambda = 100$. The security statement is the paper's Theorem 5.9: in the bilinear generic group model with random oracles, for every adversary that makes $Q < 2^\lambda$ group operations and at most $2^\lambda$ queries to each oracle, the probability that it reaches the key while the extractor outputs no witness is at most $(Q+1)/2^\lambda + s_b$, where $s_b$ is the advantage of a reduction against one Module-SIS instance.
- The hardness of that instance: it must cost at least as much as Praxis's own instance under the pinned estimator (below).
- The algorithms and their unit costs: the paper's encryption and decryption algorithms, priced as its Section 6.3 prices them (below).

### The model

The protected file `checkers/model.json` states, as exact arithmetic, everything the paper's theorems ask of a parameter set, and the paper's counts for the ciphertext size and for the work of encryption and decryption. `model.md` is the same model in readable form, with the place in the paper each line comes from. It has:

- **parameters**, the numbers a submission chooses (24 of them): the QAP's coset size and chunking, the Module-SIS shape $d_R$, $k$, the grid $K_1$, $K_2$, the range $g$, the threshold $\theta$, the norm bound $\beta$, and the constants of the inverse theorem (Lemma B.7);
- **definitions**, quantities computed from them, such as $n = (k+1)\,d_R$, the element counts $n_1$ and $n_2$ of Proposition 5.7(a), and the bound $E(u)$ of Definition B.1;
- **rules**, the conditions that must hold (18 of them): the conditions of the construction (C1 to C7), admissibility (P1, P2, P4, P5), the conditions (I1) to (I6) of the inverse theorem, which are (P3), and the hardness rule M1.

Arithmetic is exact. Every value is a rational number or an interval of rationals that provably contains it ($\sqrt{\cdot}$, $\exp$ and $\pi$ are enclosed to about $2^{-320}$). A rule passes only when it holds for every point of the intervals involved. A rule that cannot be decided either way fails.

The hardness rule M1 costs the instance $\mathsf{MSIS}_{k,\ell,\beta}$ over $R_q$, as an SIS instance of rank $k\,d_R$ with $\ell\,d_R$ columns and infinity-norm bound $\beta$, with `checkers/msis_estimate.py`. That file is a port, to the Python standard library, of the lattice attack of the lattice estimator (github.com/malb/lattice-estimator, commit `1d5c3f5c2365ea41c536805626d3f937c4412e55`) with its default cost model for lattice reduction, the one the paper uses. It takes the minimum over the block size and the number of ignored columns, on at most the number of columns the estimator takes by default. M1 requires $\log_2$ of the cost to be at least 103.533, the value the same code gives for Praxis's own instance (block size 242; the paper reports about $2^{103.5}$ at block size 242). The port is the rule: no other estimate counts.

### A submission

A submission is a file `params.json`:

```json
{
  "format": "praxis-params/1",
  "title": "one line",
  "params": {"nu": "2048", "nc": "1694", "J": "11", "...": "..."},
  "amend": [{"id": "I6", "kind": "rule", "expr": "2*beta < q and H1 <= beta and ..."}],
  "drop": []
}
```

Every value under `params` is a string of decimal digits: an integer `"a"` or a rational `"a/b"`. A decimal point is refused, because it is not exact. `amend` and `drop` are optional.

A submission is in one of two tiers, and the gate reports which.

**Tier "parameters".** No `amend` and no `drop`. `params` gives exactly the model's parameters. The gate evaluates every rule. If all hold, the paper's theorems apply to these parameters as they are stated and proved, and the paper's own counts give the size and the time. Nothing is left to judge.

**Tier "amended".** The submission changes the model: `amend` replaces or adds a rule (`"kind": "rule"`), a definition (`"kind": "def"`) or a function (`"kind": "func"`, with `args`), and `drop` removes a rule. New parameters may be added under `params`. The gate evaluates the model as amended. A pass then means only that the amended rules hold for these parameters. Whether the amended rules are theorems is the submitter's burden, in `proof.md`, and is decided in review. The entries marked protected in `model.md` cannot be amended or dropped: the fixed constants, the unit costs, the definitions of the two objectives, and the hardness rule M1.

What an amendment can express: a sharper inverse theorem (other conditions in place of (I1) to (I6), so a smaller $\beta$ and a smaller Module-SIS instance), a sharper generic bound $E$, a reduction to a different SIS instance (the definitions `msis_rank`, `msis_cols`, `msis_bound`, `msis_norm`), or a change to the construction that publishes fewer elements or does less work (the element counts `n1` and `n2`, and the operation counts `dec_sum_g1`, `dec_sum_g2`, `dec_msm_g1`, `dec_msm_g2`, `dec_pairings`, `search_spread`).

### What an amended submission must prove

`proof.md` must contain one section per amended or dropped entry, headed `## Amendment <id>`, and a final section headed `## Targets`. `paper-contract.md` is the protected reference: it lists every statement of the paper, every background block (the construction, the conditions, the bound $E$) with the results that are stated or proved in terms of it, and what each result takes from each prerequisite. `model.md` says, for every model entry, which block states it.

- **O-amend, one per amended or dropped entry.** The section states the entry as amended, in mathematical notation, and it is the same condition or quantity as the expression in `params.json`, with the same constants. For every result of the paper that is stated or proved in terms of the entry's block (the "Background to" list of that block in `paper-contract.md`), the section either gives the result's statement under the amended entry and a complete proof of it, or shows that neither its statement nor its proof uses what changed. A new result is stated in full and proved in full.
- **O-construction, when an element count or an operation count is amended** (`n1`, `n2`, `dec_sum_g1`, `dec_sum_g2`, `dec_msm_g1`, `dec_msm_g2`, `dec_pairings`, `search_spread`). The section specifies the changed construction completely: what encryption publishes and how decryption combines it. It proves correctness (Theorem 5.6 with error $2/q$), proves that a ciphertext consists of $n_1$ elements of $\mathbb{G}_1$, $2n_2$ of $\mathbb{G}_2$, one of $\mathbb{G}_T$, the seed and the masked message, that encryption computes one scalar multiplication of a generator for each of them, and that decryption performs at most the amended numbers of additions, multi-scalar multiplication points and pairings, with a search whose result has root mean square at most the amended spread.
- **O-targets.** The final section derives, for every parameter set that satisfies the amended model, Theorem 5.6 (correctness) and Theorem 5.9 (extraction) as the paper states them, with the same models, the same adversary class and the same bound $(Q+1)/2^\lambda + s_b$, where $s_b$ is the advantage of an explicit reduction against the SIS instance that the amended definitions `msis_rank`, `msis_cols`, `msis_bound` and `msis_norm` describe, with the reduction's running time stated.

Proofs may use the results of the paper that do not depend on an amended entry, by their label and as `paper-contract.md` states them; the background blocks; standard mathematics; and theorems from the literature other than the paper itself, each with its citation, locator and the quoted statement. Full proofs only: every step is written out.

A submission is VALID when the gate passes, the scored text is the submitted `params.json`, and, on tier "amended", every obligation is accepted.

## Score

There are two objectives, both integers, both computed by the protected checker `praxis_gate` from `params.json` and from nothing else. Lower is better on each.

**1. Size, `ciphertext_mib`: the ciphertext size in MiB, rounded up.**

$$\text{size in bits} = 255\, n_1 + 512 \cdot 2 n_2 + 3280, \qquad \texttt{ciphertext\_mib} = \lceil \text{size in bits} / 2^{23} \rceil ,$$

with $n_1 = (2K_1 + 1)(N+1) + \Delta + (\nu - 1)\, n_{\mathsf{c}}/J'$ and $n_2 = 6K_2(N+1) + 3K_2 + \tfrac{3n}{2}(J + J') + 13n - 8$, the counts of Proposition 5.7(a).

**2. Time, `time_mmul`: one encryption plus one expected decryption, in millions of multiplications in the base field, rounded up.**

$$\texttt{time\_mmul} = \lceil (\text{enc} + \text{dec}) / 10^6 \rceil .$$

Encryption computes one fixed-base scalar multiplication for each element of $\mathbb{G}_1$ and $\mathbb{G}_2$: at most 11 and 10 affine additions, of 6 and 15 multiplications, plus one inversion (362 multiplications) shared among 2048 additions. Its work in $\mathbb{F}_q$ is one multiplication for each of the system's about $2^{30}$ nonzero coefficients and three for each of the $m = k(\ell+1)\,d_R$ coefficients of the matrix $M$.

$$\text{enc} = 11\, a_1\, n_1 + 10\, a_2 \cdot 2 n_2 + 2^{30} + 3m, \qquad a_1 = 6 + \tfrac{362}{2048},\quad a_2 = 15 + \tfrac{362}{2048} .$$

Decryption is counted in expectation, with a witness of $\lfloor N/2 \rfloor$ ones:

$$\text{dec} = \underbrace{a_1 (2K_1+1)\tfrac{N+1}{2} + a_2 \cdot 12K_2\, \tfrac{N+1}{2}}_{\text{sums}} + \underbrace{200\,\bigl(3n + 2J\Delta + (\nu-1) n_{\mathsf{c}}\bigr) + 950\,\bigl(3n(J+J') + 26n - 16\bigr)}_{\text{multi-scalar multiplications}} + \underbrace{6400\,(18K_2 + 4J + 2J' + 2)}_{\text{pairings}} + \underbrace{632000000 + m}_{\mathbb{F}_q} + \underbrace{6 \cdot \tfrac{37}{20} \sqrt{g \sqrt{(N+4)/48} + 3/2}}_{\text{search}} .$$

The counts are those of Proposition 5.7(b) to (d), and the unit costs those of Section 6.3. Four numbers are set so that each part reproduces the figure the paper reports for it: 950 multiplications per point of a multi-scalar multiplication in $\mathbb{G}_2$, 6400 per pairing, the factor $37/20$ of the search, and the constant 632000000 of decryption's work in $\mathbb{F}_q$. At the paper's parameters the model gives:

| | this model | the paper |
|---|---|---|
| size | 67,720,351,811 bits = 7.8837 GiB, score 8,073 | 7.88 GiB |
| encryption | $2^{34.22}$ = 20,074 million | about $2^{34.2}$, $2.0 \times 10^{10}$ |
| decryption | $2^{33.00}$ = 8,595 million | about $2^{33.0}$, $8.6 \times 10^{9}$ expected |
| time | $2^{34.74}$, score 28,669 | the sum of the two |

The gate also reports `enc_mmul` and `dec_mmul`, the two parts of the time, so that a reader can see where a change comes from. They are not objectives.

An accepted amendment may replace the counts (`n1`, `n2`, `dec_sum_g1`, `dec_sum_g2`, `dec_msm_g1`, `dec_msm_g2`, `dec_pairings`, `search_spread`); nothing may replace the unit costs or the formulas.

The reviewer does not choose the numbers and does not recompute them. Wording, notation, the length of a proof and the way results are grouped cannot change them.

A submission enters the frontier when no valid submission is at least as good on both objectives and better on one. The starting submission is the paper's own parameter set, with the constants of the inverse theorem that the authors published with their Lean proofs: (8,073, 28,669). A submission that is at least as good as it on both and better on one improves on Praxis outright; one that is better on one and worse on the other is a trade-off, and the frontier shows it as one.

A submission that is not VALID receives no score. It is not scored as the baseline and it is not repaired.

## Tiers on one frontier

There is one track and one frontier. Every entry carries its tier, which the gate reports and anyone can read:

- an entry of tier "parameters" is a parameter set that the paper's own theorems cover. Code decides everything about it;
- an entry of tier "amended" rests on amended rules, accepted by the reviewer and then by a person at promotion.

## What does not count

- A smaller number obtained by changing what is fixed: another statement or a smaller $N$, another curve or group order, another size per group element, other unit costs or faster algorithms for the same operations, a lower security level, a weaker adversary class, a larger bound than $(Q+1)/2^\lambda + s_b$, or a different security notion.
- A security argument that rests on anything the paper's does not: an assumption other than the hardness of the costed SIS instance, another idealized model, a heuristic, or a conjecture.
- A hardness estimate other than rule M1, or an argument that M1's floor is too high.
- On tier "amended": anything short of a full proof. An idea, a plan, a sketch, an outline, a proof that points to the paper's proof of the result it changes, to the reader or to a computation that is not shown, or a step called clear, standard or routine in place of doing it.
- An amendment whose expression in `params.json` is not the condition that `proof.md` proves, constant for constant.
- An amendment justified by citing the paper itself (arXiv 2611.28552, ePrint 2026/2971) or its Lean development (`praxis-lean`) for the amended claim.
- An argument placed where it is not read as a proof: `notes.md`, the title, or the manifest.
- A claim of a machine check, a link, or a transcript. These are context, never evidence.

## Submission and review

Submit only files under `submission/`:

- `params.json`: the parameter set, in the format above.
- `submission.json`: the manifest. It names the claim and declares `params.json` to the protected checker `praxis_gate`. Do not write it by hand: `python3 tools/pack.py` evaluates `params.json` with the protected model, prints what the hosted checker will answer, and writes it.
- `proof.md`: required on tier "amended", absent otherwise.
- `notes.md`, optional: what was changed and why, for a human reader.

No other file and no experiment: `experiments` is `[]`. Limits: 4 files, 262,144 bytes per file. The hosted evaluator accepts a declared input of at most 16,384 bytes, so `params.json` must be shorter than that; write long rationals as short ones that still satisfy the rules.

Review has three stages.

1. **The gate (code).** The protected checker `praxis_gate` rebuilds the declared text, refuses anything that is not one strict JSON object (a repeated key or a decimal point is refused), applies the amendments, and evaluates the model. It passes only when every rule in force holds, and then reports the two objectives, the tier, the amended and dropped entries, and the SHA-256 of the text it checked. Without a pass there is no score.
2. **The review (model).** An LLM reviewer confirms that the SHA-256 the gate reports is the SHA-256 of the submitted `params.json`. On tier "parameters" nothing else is judged. On tier "amended" it then judges every obligation above, reading `proof.md` against `model.md` and `paper-contract.md`. The standard is strict: any gap, any step it cannot confirm, any weakened constant, bound or hypothesis rejects the whole submission.
3. **Promotion (person).** Results are promoted by hand. For tier "parameters" the person confirms the binding with `python3 tools/pack.py --check` and that the tier is "parameters"; there is no mathematics to check. For tier "amended" the person also reads `proof.md` and the reviewer's reasons and opens every cited source.

The hosted evaluator runs in a sandbox with no network. A model reading a proof is not a proof check: on tier "amended" its judgment is an assessment of the submitted text, not a certificate, and the check by a person at promotion is what a record rests on. On tier "parameters" no judgment is involved: the entry rests on the paper's theorems and on the exact evaluation of their conditions.

## What a record means

An entry of tier "parameters" says: Praxis, exactly as the paper specifies and proves it, has this size and this time for the reference statement at 100-bit security, at these parameters, under the cost model above. It inherits what the paper's own claim rests on, and nothing more: the generic group and random oracle models, the estimate of Module-SIS hardness by best known attacks, an honest Groth16 setup, and the correctness of the paper's proofs. An entry of tier "amended" adds the correctness of the amended proofs.
