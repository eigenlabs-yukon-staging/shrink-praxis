# Shrink Praxis

Come up with a better witness encryption scheme than Praxis: a smaller ciphertext, less time.

Praxis (Tse, Vanjani, Vesely; Cryptology ePrint Archive 2026/2971) is the first witness encryption scheme for all of NP that is both proved secure in well-studied models and practical. At 100-bit security, encrypting to a Groth16 verifier on BN254, its ciphertext is **7.88 GiB**, encryption takes about **2.0 × 10^10** field multiplications and decryption about **8.6 × 10^9** on average. This challenge asks for less size, less time, or both, without giving up anything the paper proves.

- **Two objectives**, a Pareto frontier, both lower is better, both computed by code from your parameter file: size, `ciphertext_mib` (the ciphertext in MiB), and time, `time_mmul` (one encryption plus one expected decryption, in millions of field multiplications). The paper's parameters score (8,073, 28,669): 20,074 million to encrypt and 8,595 million to decrypt.
- **A submission** is `submission/params.json`: a parameter set of Praxis. Code checks, with exact arithmetic, every condition under which the paper proves its theorems (18 rules), costs the Module-SIS instance with a pinned lattice estimator, and computes the two objectives with the paper's own counts and unit costs.
- **Two tiers on one frontier.** If you only choose parameters, your entry is covered by the paper's theorems as they stand, and code decides everything (tier "parameters"). You may also change the rules, for example a sharper inverse theorem that allows a smaller Module-SIS instance, and then you must prove your change in `submission/proof.md`; a model reviews the proof and a person checks it before promotion (tier "amended").

Read `rules.md` (what counts), `model.md` (the rules, line by line, with their place in the paper) and `paper-contract.md` (every statement of the paper and what each result takes from the others).

## Where the costs come from

A ciphertext has $n_1 = (2K_1+1)(N+1) + \Delta + (\nu-1)\,n_{\mathsf{c}}/J'$ elements of $\mathbb{G}_1$ (255 bits each) and $2n_2$ of $\mathbb{G}_2$ (512 bits each), with $n_2 = 6K_2(N+1) + 3K_2 + \tfrac{3n}{2}(J+J') + 13n - 8$. So the size is about $(N+1)\,(510\,K_1 + 6144\,K_2)$ bits, and $K_1 K_2 = n/2$ where $n = (k+1)\,d_R$ is the number of forms. The number of forms is set by the Module-SIS instance, whose norm bound $\beta \approx 2^{187.3}$ comes out of the inverse theorem (Lemma B.7). A smaller $n$, a better split of $K_1 K_2$, or a smaller $\beta$ that lets $n$ shrink all make the ciphertext smaller, and encryption with it, since encryption does one scalar multiplication per element.

Decryption is half sums, multi-scalar multiplications and pairings, which follow the same counts, and half a search of about $\tfrac{37}{20}\sqrt{g\sqrt{(N+4)/48}}$ steps. The range $g$ pulls both ways: a larger $g$ lengthens the search but lowers the $\beta$ the inverse theorem needs, which can shrink everything else. The chunk counts $J$, $J'$ trade a little size against a little decryption. `rules.md` has the formulas.

## How to work

```
python3 tools/pack.py --try my-params.json   # evaluate any parameter file, write nothing
python3 tools/pack.py                        # check submission/params.json and write submission/submission.json
python3 tools/pack.py --check                # confirm the manifest declares exactly params.json
```

The gate's answer lists the rules that fail, so a search can be driven from it. Everything is standard-library Python; nothing needs a network.

## Files

| File | What it is |
|---|---|
| `rules.md` | the rules of the challenge |
| `model.md` | the model in readable form: parameters, definitions, rules, and where each comes from |
| `paper-contract.md` | the paper as a dependency graph: every statement, every background block, what each result takes from the others |
| `checkers/model.json` | the model, as the gate evaluates it |
| `checkers/praxis_gate.py`, `checkers/praxis_model.py` | the gate and its exact evaluator |
| `checkers/msis_estimate.py` | the pinned Module-SIS cost estimate |
| `submission/` | the only directory you edit |
| `tools/pack.py` | checks a parameter file and writes the manifest |
