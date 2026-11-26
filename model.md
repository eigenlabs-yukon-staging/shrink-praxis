# The model: what a parameter set of Praxis must satisfy, and what its ciphertext costs

Generated from `checkers/model.json` (SHA-256 `5096220b284278e0c1316588f0bba72e85ea86477f1af3ad0a96faea49fb09f8`). The gate evaluates exactly these expressions, with exact arithmetic.
Paper: Praxis: Practical Witness Encryption for NP (Tse, Vanjani, Vesely), Cryptology ePrint Archive 2026/2971, arXiv 2611.28552v1.

## How to read an expression

Python syntax. Integers; `+ - * /`; `**` with an integer exponent; `%` on integers; comparisons; `and`, `or`, `not`; `floor`, `ceil`, `sqrt`, `exp`, `pi`, `min`, `max`, `abs`, `is_pow2`, `is_int`; `msis_log2(rank, columns, bound, norm)`, the base-2 logarithm of the cost of the lattice attack on that SIS instance by the pinned estimator, rounded down to 1/1000, where `norm` is 0 for the infinity norm and 2 for the Euclidean norm. Every value is a rational or an interval of rationals that contains the true value; a comparison is true only if it holds on the whole interval.

## Fixed constants (protected)

| name | value | what it is |
|---|---|---|
| `q` | `21888242871839275222246405745257275088548364400416034343698204186575808495617` | order of BN254's groups G1, G2, GT (Table 4) |
| `N` | `391693` | Boolean unknowns of the statement: the Groth16 verifier on BN254 as a Boolean quadratic system (Sec. 6.1) |
| `nc_raw` | `1692` | constraints of that system before padding (Sec. 6.1) |
| `Fmax` | `2047` | products per constraint, at most (Table 4) |
| `lam` | `100` | security level in bits |
| `l_lab` | `254` | length of the labels of the generic model (Table 4) |
| `bits_G1` | `255` | bits of one compressed element of G1 (Sec. 6.3) |
| `bits_G2` | `512` | bits of one compressed element of G2 (Sec. 6.3) |
| `overhead_bits` | `3280` | the element of GT, the seed and the masked message: 410 bytes (Sec. 6.3) |
| `inv_mults` | `362` | multiplications of one inversion in the base field: the exponentiation by p - 2, 253 squarings and 109 multiplications (Sec. 6.3) |
| `batch` | `2048` | additions that share one inversion (Sec. 6.3) |
| `enc_adds1` | `11` | affine additions of one fixed-base scalar multiplication in G1, at most (Sec. 6.3) |
| `enc_adds2` | `10` | affine additions of one fixed-base scalar multiplication in G2, at most (Sec. 6.3) |
| `enc_fq` | `1073741824` | encryption's work in F_q that does not depend on the parameters: a multiplication for each of the system's about 2^30.0 nonzero coefficients (Sec. 6.3) |
| `msm1` | `200` | multiplications per point of Pippenger's multi-scalar multiplications in G1 (Sec. 6.3) |
| `msm2` | `950` | multiplications per point of the multi-scalar multiplications in G2; set so that all of them total the paper's 2^31.3 |
| `pair_mults` | `6400` | multiplications per pairing, final exponentiations shared; the paper's 284 pairings take about 2^20.8 (Sec. 6.3) |
| `dec_fq` | `632000000` | decryption's work in F_q apart from the forms; with the forms it is the paper's about 2^29.3 at its parameters (Sec. 6.3) |
| `step_mults` | `6` | multiplications per candidate of the search (Sec. 5.2, Sec. 6.3) |
| `msis_floor` | `103533/1000` | log2 cost of Praxis's own Module-SIS instance under the pinned estimator, rounded down to 1/1000 |

## Parameters (a submission chooses these)

| name | type | what it is | Praxis |
|---|---|---|---|
| `nu` | integer | coset size of the QAP | `2048` |
| `nc` | integer | constraints after padding with 0 = 0 | `1694` |
| `J` | integer | chunks of the quotient powers | `11` |
| `Delta` | integer | length of a chunk of quotient powers | `351001` |
| `Jp` | integer | chunks of the remainder powers (J' in the paper) | `11` |
| `dR` | integer | degree of the ring R_q | `64` |
| `k` | integer | rows of the Module-SIS matrix | `71` |
| `K1` | integer | left legs of the grid of shared factors | `192` |
| `K2` | integer | right legs of each kind | `12` |
| `g` | integer | range of each secret integer | `1736375024658487` |
| `theta` | rational | threshold above which a stack is heavy | `1048575/3369993333…137951281152 (75 chars)` |
| `beta` | integer | norm bound of Module-SIS | `243263909612554812…315305388991 (57 chars)` |
| `b` | integer | inverse theorem: the integer b of (I1) | `50` |
| `eps_tr` | rational | inverse theorem: density one trimming may lose | `1/2037035976334486…706183397376 (93 chars)` |
| `R_tr` | rational | inverse theorem: radius of the trimming ellipsoid | `21` |
| `Lambda1` | rational | inverse theorem: geometric factor, rank 1 | `227642227848876931…000000000000 (82 chars)` |
| `Lambda2` | rational | inverse theorem: geometric factor, rank 2 | `207211108687100453…000000000000 (193 chars)` |
| `Lambda3` | rational | inverse theorem: geometric factor, rank 3 | `226946760695661377…000000000000 (272 chars)` |
| `Gamma1` | rational | inverse theorem: density bound, rank 1 | `328572852988609267…000000000000 (148 chars)` |
| `Gamma2` | rational | inverse theorem: density bound, rank 2 | `141106924167155248…000000000000 (154 chars)` |
| `Gamma3` | rational | inverse theorem: density bound, rank 3 | `773459483762140301…000000000000 (157 chars)` |
| `A_inv` | rational | inverse theorem: loss factor of a trimming | `633824695651204893…433764249499 (61 chars)` |
| `P_1` | rational | inverse theorem: per-step growth, rank 1 (P_1 in Lemma B.7) | `512532115958221845…000000000000 (81 chars)` |
| `P_2` | rational | inverse theorem: per-step growth, rank 2 (P_2 in Lemma B.7) | `626106135216113852…000000000000 (79 chars)` |

## Definitions

| name | expression | what it is | amendable |
|---|---|---|---|
| `D` | `N + 2 + nu*nc` | evaluation points of the QAP (Sec. 4.4) | yes |
| `ell` | `ceil(N/dR)` | columns of the Module-SIS matrix (Sec. 5.1) | yes |
| `n` | `(k+1)*dR` | number of forms (Sec. 5.1) | yes |
| `Deltap` | `nu*nc/Jp` | length of a chunk of remainder powers (Sec. 5.2) | yes |
| `Bsearch` | `(N+1)*(g+1)` | search bound B (Sec. 5.1) | yes |
| `n1` | `(2*K1+1)*(N+1) + Delta + (nu-1)*nc/Jp` | elements of G1 in a ciphertext (Proposition 5.7(a)) | yes |
| `n2` | `6*K2*(N+1) + 3*K2 + (3*n/2)*(J+Jp) + 13*n - 8` | half the elements of G2 in a ciphertext (Proposition 5.7(a)) | yes |
| `L1` | `n1 + 2*K1 + 1` | labels in G1 given to the adversary; reproduces the authors' count 151,468,814 and is at least n1 + 1 | yes |
| `L2` | `2*n2 + 12*K2 + 1` | labels in G2 given to the adversary; reproduces the authors' count 56,828,073 and is at least 2 n2 + 1 | yes |
| `LT` | `2` | labels in GT (Definition B.1) | yes |
| `L` | `L1 + L2 + LT` | all labels given to the adversary (Definition B.1) | yes |
| `eps_f` | `(3*D + 2*n + 2*K1 + 67)/(q - D)` | bound on a coincidence in F_q (Definition B.1) | yes |
| `Nfree` | `2**l_lab - L - 3*2**(lam+1) - 1` | labels never given out (Definition B.1) | yes |
| `mu_tr` | `theta - 100*eps_tr` | density that survives the trimmings (Lemma B.7) | yes |
| `xi_tr` | `(1 + 2/g)**254` | (Lemma B.7) | yes |
| `H3` | `xi_tr/(g**3*mu_tr - xi_tr/g)` | (Lemma B.7) | yes |
| `H1` | `Gamma1/(g*mu_tr)` | (Lemma B.7) | yes |
| `H2` | `Gamma2/(g**2*mu_tr)` | (Lemma B.7) | yes |
| `T_tr` | `R_tr*g*sqrt(N/3)` | (Lemma B.7) | yes |
| `msis_rank` | `k*dR` | rank of the SIS instance the security proof reduces to: MSIS_{k,ell,beta} over R_q, unrolled (Definition 3.3, Lemma B.8(c)) | yes |
| `msis_cols` | `ell*dR` | columns of that instance | yes |
| `msis_bound` | `beta` | its norm bound | yes |
| `msis_norm` | `0` | its norm: 0 for the infinity norm, 2 for the Euclidean norm | yes |
| `matrix_coeffs` | `k*(ell+1)*dR` | coefficients in F_q of the matrix M, 27,818,368 at the paper's parameters (Sec. 5.2); computing the forms costs encryption three multiplications for each (z at three points) and decryption one (Proposition 5.7) | no (protected) |
| `dec_sum_g1` | `(2*K1+1)*(N+1)/2` | additions in G1 of decryption's sums, for a witness with floor(N/2) ones: (N+1)/2 entries in each of 2 K1 + 1 arrays (Sec. 6.3) | yes |
| `dec_sum_g2` | `12*K2*(N+1)/2` | additions in G2 of decryption's sums: (N+1)/2 entries in each of 12 K2 arrays (Sec. 6.3) | yes |
| `dec_msm_g1` | `3*n + 2*J*Delta + (nu-1)*nc` | total length of decryption's multi-scalar multiplications in G1: 2J of length Delta, J' over the allowed remainder powers, and 3n more (Proposition 5.7(c), Sec. 6.3) | yes |
| `dec_msm_g2` | `3*n*(J+Jp) + 26*n - 16` | total length of decryption's multi-scalar multiplications in G2 (Proposition 5.7(c)) | yes |
| `dec_pairings` | `18*K2 + 4*J + 2*Jp + 2` | pairings of decryption (Proposition 5.7(c)) | yes |
| `search_spread` | `g*sqrt((N+4)/48) + 3/2` | bound on the root mean square of the integer the search finds (Lemma 5.5) | yes |
| `search_steps` | `(37/20)*sqrt(search_spread)` | expected baby and giant steps of the search: 37/20 times the square root of the spread, the paper's about 2^29.4 at its parameters (Proposition 5.7(d), Sec. 6.3) | no (protected) |
| `add1` | `6 + inv_mults/batch` | multiplications of one affine addition in G1, with its share of the batched inversion (Sec. 6.3) | no (protected) |
| `add2` | `15 + inv_mults/batch` | multiplications of one affine addition in G2, with its share of the batched inversion (Sec. 6.3) | no (protected) |
| `size_bits` | `bits_G1*n1 + bits_G2*2*n2 + overhead_bits` | ciphertext size in bits (Proposition 5.7(a), Sec. 6.3) | no (protected) |
| `enc_mults` | `enc_adds1*add1*n1 + enc_adds2*add2*2*n2 + enc_fq + 3*matrix_coeffs` | field multiplications of encryption: one fixed-base scalar multiplication for each element of G1 and G2, and the work in F_q (Proposition 5.7(b), Sec. 6.3) | no (protected) |
| `dec_mults` | `add1*dec_sum_g1 + add2*dec_sum_g2 + msm1*dec_msm_g1 + msm2*dec_msm_g2 + pair_mults*dec_pairings + dec_fq + matrix_coeffs + step_mults*search_steps` | expected field multiplications of decryption with a witness of floor(N/2) ones: sums, multi-scalar multiplications, pairings, work in F_q, and the search (Sec. 6.3) | no (protected) |
| `score_mib` | `ceil(size_bits/8/2**20)` | OBJECTIVE 1, SIZE: ciphertext size in MiB, rounded up | no (protected) |
| `score_time` | `ceil(up((enc_mults + dec_mults)/10**6))` | OBJECTIVE 2, TIME: one encryption plus one expected decryption, in millions of field multiplications, rounded up | no (protected) |
| `score_enc` | `ceil(up(enc_mults/10**6))` | reported beside the objectives: encryption alone, in millions of field multiplications | no (protected) |
| `score_dec` | `ceil(up(dec_mults/10**6))` | reported beside the objectives: expected decryption alone, in millions of field multiplications | no (protected) |

## Functions

- `Ncmp(u)` = `u*L + u*(u+1)/2`: comparisons charged in u operations (Definition B.1). Amendable.
- `E(u)` = `(L1*(L1-1)/2 + L2*(L2-1)/2 + LT*(LT-1)/2 + L)*eps_f + Ncmp(u)*(theta + eps_f) + ((L+3*u)*(L+3*u-1)/2 + L + 3*u)*eps_f + (8*u+8)*eps_f + (2*L + 4*u + 2**(lam+2))/Nfree + 4*u/2**126 + 1/2**128`: the bound E of Definition B.1. Amendable.

## Rules

| id | condition | expression | from | stated in | amendable |
|---|---|---|---|---|---|
| **C1** | the coset size divides q - 1 and exceeds F_max | `nu > Fmax and (q - 1) % nu == 0` | Sec. 4.4 | `blob:qap` | yes |
| **C2** | padding only adds constraints; J' divides the number of constraints | `nc >= nc_raw and J >= 1 and Jp >= 1 and nc % Jp == 0` | Sec. 5.2, chunked powers | `blob:enc` | yes |
| **C3** | the evaluation points fit in the subgroup of order 2^ceil(log2 D), which must divide q - 1 (q - 1 is divisible by 2^28 and not by 2^29) | `D < q and D <= 2**28` | Sec. 4.4, Proposition 5.7 | `blob:qap` | yes |
| **C4** | the search bound B = (N+1)(g+1) satisfies 2B + 1 < q | `g >= 1 and 2*Bsearch + 1 < q` | Sec. 5.1, Parameters | `blob:sampler-search` | yes |
| **C5** | d_R is a power of two with q = 1 mod 2 d_R | `k >= 1 and is_pow2(dR) and (q - 1) % (2*dR) == 0` | Sec. 3.3 | `blob:msis` | yes |
| **C6** | the number of forms n = (k+1) d_R is even and divides q - 1 | `n % 2 == 0 and (q - 1) % n == 0` | Sec. 5.1, Forms and weights | `blob:forms-weights` | yes |
| **C7** | the grid has K1 K2 = n/2 legs, so 3n/2 cells | `K1 >= 1 and K2 >= 1 and 2*K1*K2 == n` | Sec. 5.1, Table 4 | `blob:copies-ties` | yes |
| **P1** | D <= J Delta <= D + n and n <= D | `D <= J*Delta and J*Delta <= D + n and n <= D` | Sec. 5.4 (P1) | `blob:admissibility` | yes |
| **P2** | 3(L + 3 2^(lam+1) + 1) <= q | `3*(L + 3*2**(lam+1) + 1) <= q` | Sec. 5.4 (P2) | `blob:admissibility` | yes |
| **I1** | b >= 7 and 2^b <= g < 2^254 | `b >= 7 and 2**b <= g and g < 2**254` | Lemma B.7 (I1) | `blob:inverse-conditions` | yes |
| **I2** | R_tr >= 20, 1000 e^(-99 R_tr^2/200) <= eps_tr < mu_tr, and g^3 mu_tr > xi_tr/g | `R_tr >= 20 and 1000*exp(-99*R_tr**2/200) <= eps_tr and eps_tr < mu_tr and g**3*mu_tr > xi_tr/g` | Lemma B.7 (I2) | `blob:inverse-conditions` | yes |
| **I3** | Lambda1 >= 2 sqrt(3) R_tr sqrt(N), Lambda2 >= 27 sqrt(2) pi R_tr^2 N, Lambda3 >= 144 sqrt(2) pi R_tr^3 N^(3/2) | `Lambda1 >= 2*sqrt(3)*R_tr*sqrt(N) and Lambda2 >= 27*sqrt(2)*pi*R_tr**2*N and Lambda3 >= 144*sqrt(2)*pi*R_tr**3*N*sqrt(N)` | Lemma B.7 (I3) | `blob:inverse-conditions` | yes |
| **I4** | the eight inequalities of (I4) | `Gamma3 >= xi_tr*(1 + H3/g) and A_inv >= mu_tr/(mu_tr - eps_tr) and P_2**(b-1) >= (g**(-3) + eps_tr)/mu_tr and P_1**(b-1) >= (g**(-2) + 2*eps_tr)/mu_tr and Gamma2**(b-1) >= g**(-2)/mu_tr and Gamma1**(b-1) >= g**(-1)/mu_tr and Gamma2 >= A_inv*Lambda1*Gamma3*P_2 and Gamma1 >= A_inv*max(Lambda1*Gamma2, Lambda2*Gamma3)*P_1` | Lemma B.7 (I4) | `blob:inverse-conditions` | yes |
| **I5** | Lambda_d Gamma_d < mu_tr q for d = 1, 2, 3; g^-4 < mu_tr; H1 T_tr < q, 4 H2 T_tr^2 < q, 54 H3 T_tr^3 < q | `Lambda1*Gamma1 < mu_tr*q and Lambda2*Gamma2 < mu_tr*q and Lambda3*Gamma3 < mu_tr*q and g**(-4) < mu_tr and H1*T_tr < q and 4*H2*T_tr**2 < q and 54*H3*T_tr**3 < q` | Lemma B.7 (I5) | `blob:inverse-conditions` | yes |
| **I6** | 2 beta < q, H1 <= beta, 2 H2 q <= beta^2, 6 floor(H3) q^2 <= beta^3 | `2*beta < q and H1 <= beta and 2*H2*q <= beta**2 and 6*floor(H3)*q**2 <= beta**3` | Lemma B.7 (I6) | `blob:inverse-conditions` | yes |
| **P4** | 24 beta^4 < q^3 | `24*beta**4 < q**3` | Sec. 5.4 (P4) | `blob:admissibility` | yes |
| **P5** | E(2) <= 2^-lam and E(2^(lam+1)) - E(2) <= 1 - 2^-lam | `E(2) <= 1/2**lam and E(2**(lam+1)) - E(2) <= 1 - 1/2**lam` | Sec. 5.4 (P5) | `blob:admissibility` | yes |
| **M1** | the Module-SIS instance is at least as hard as Praxis's own, by the pinned lattice estimator | `msis_log2(msis_rank, msis_cols, msis_bound, msis_norm) >= msis_floor` | Sec. 6.2, MSIS | `blob:msis` | no (protected) |

## Which results depend on an entry

The 'stated in' column names the block of `paper-contract.md` that states each rule. Each block's entry there ends with 'Background to:', the results of the paper that are stated or proved in terms of it. An amendment of a model entry must account for every result listed for its block (`rules.md`, O-amend).

Definitions and their blocks: `n1`, `n2` and the operation counts `dec_sum_g1`, `dec_sum_g2`, `dec_msm_g1`, `dec_msm_g2`, `dec_pairings` are Proposition 5.7 (`prop:efficiency`), counted from `blob:enc` and `blob:dec`; `search_spread` is Lemma 5.5 (`lem:range`) with `blob:sampler-search`; `L1`, `L2`, `LT`, `L`, `eps_f`, `Nfree`, `Ncmp`, `E` are `blob:bound-e`; `mu_tr`, `xi_tr`, `H1`, `H2`, `H3`, `T_tr` are `blob:inverse-conditions`; `msis_rank`, `msis_cols`, `msis_bound`, `msis_norm` are `blob:msis` with Lemma B.8(c) (`lem:heavy`) and Lemma B.14 (`lem:reduction`); `D`, `Deltap` are `blob:qap` and `blob:enc`; `ell`, `n` are `blob:forms-weights`; `Bsearch` is `blob:sampler-search`.

## The paper's parameters under this model

All 18 rules hold. Ciphertext: 67,720,351,811 bits = 7.8837 GiB = 8,073 MiB, from 151,468,429 elements of G1 and 56,827,928 of G2. Time: 2^34.74 multiplications = 28,669 million, of which encryption 2^34.22 = 20,074 million and expected decryption 2^33.00 = 8,595 million. Module-SIS: log2 cost 103.533 at block size 242.
