# Working on this challenge

Edit only `submission/`. Read `rules.md` first, then `model.md`. Write `submission/params.json`, then run `python3 tools/pack.py`: it evaluates the parameters with the protected model and writes `submission/submission.json`. Never write the manifest by hand, and declare no experiment. `python3 tools/pack.py --try FILE` evaluates any parameter file without writing anything; use it to search.

There are two objectives, both lower is better, and code computes them from `params.json` alone: size, `ciphertext_mib`, and time, `time_mmul` (one encryption plus one expected decryption). The result is a Pareto frontier: a submission counts when nothing valid is at least as good on both. A submission that beats the paper's parameters on both is the strongest kind. Wording and notation cannot change a score.

- **Tier "parameters":** choose parameters only. No `amend`, no `drop`, no `proof.md`. Every number is a string of digits, `"a"` or `"a/b"`. All 18 rules must hold; the gate lists the ones that fail.
- **Tier "amended":** you may amend or drop rules and definitions in `params.json`, and then `submission/proof.md` must prove each change in full, with one section `## Amendment <id>` per changed entry and a final section `## Targets`. A reviewer model judges it strictly, and a person checks it before promotion. Do not cite the paper or its Lean development for the claim you change.

<!-- llm-verifier:solver-guidance:begin -->
## Preparing a submission

Read the [solver guide](https://github.com/Layr-Labs/llm-verifier/blob/939a35dbb233c062ae514bd9abc62d3168eba1fc/docs/solving.md) and
[solver skill](https://github.com/Layr-Labs/llm-verifier/blob/939a35dbb233c062ae514bd9abc62d3168eba1fc/skills/llm-verifier-solver/SKILL.md)
from the same pinned verifier revision as this challenge.

- Use the challenge's verifier revision for `llm-verifier check --root .`.
- Run the final submission's declared computations through `intake`,
  `prepare-runtime`, and `experiments` without model credentials.
  `test-checkers` runs organizer fixtures, not your candidate's checks.
- Ask a fresh independent subagent to critique the complete final submission,
  protected rules, selected policies and evidence using the guide.
- Fix findings and rerun affected checks and review.
- Report results and omitted steps. Subagent critique is advisory;
  configured-provider review is separate. `simulate` does not judge correctness.
<!-- llm-verifier:solver-guidance:end -->
