# Starting submission: Praxis as published

These are the parameters of Table 4 of the paper, with the constants of the inverse theorem (Lemma B.7) that the authors published with their Lean proofs. The three constants $\Gamma_1$, $\Gamma_2$, $\Gamma_3$ are the authors' exact values rounded up to 80 digits, which keeps every condition true and the file short. Nothing is amended, so there is nothing to judge: every rule of the model holds, and the model gives a size of 8,073 MiB (the paper's 7.88 GiB) and a time of 28,669 million multiplications: 20,074 million to encrypt (about 2^34.2) and 8,595 million to decrypt on average (about 2^33.0).

To submit an improvement, replace `params.json`, run `python3 tools/pack.py` to rewrite `submission.json`, and rewrite this file to say what you changed and why.
