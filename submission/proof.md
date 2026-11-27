# Praxis with single-sector search on Boolean-tag extensions

Throughout the proof \(N\) is the protected external variable count and \(N_\star=N+3\) is the number of internally sampled box coordinates. The three internal Boolean coordinates do not change which external witness relation is encrypted. The construction, coefficient placement and probabilities for the amended model follow.

## Amendment C5

In the first disjunct require \(\mathrm{ring\_mode}=0\), \(k\ge1\), and either the original power-of-two \(d_R\) with \(2d_R\mid q-1\), or \(d_R=144\) with \(468\mid q-1\). In the first case keep the original coefficient ring. In the second use
\[
 P(Y)=\frac{(Y^{234}+1)(Y^6+1)}{(Y^{78}+1)(Y^{18}+1)},\qquad
 R=\mathbb Z[Y]/P(Y),\quad R_q=\mathbb F_q[Y]/P(Y).
\]
Each ring is in the power basis of length \(d_R\), and its integer infinity norm is the maximum absolute value of these coefficients.

### Integer ring and its reduction

The roots of \(Y^{234}+1\) have orders \(4d\) with \(d\) a divisor of \(117=9\cdot13\). The primitive 468th roots are exactly the ones left after excluding the orders with \(9\nmid d\) or \(13\nmid d\). The former orders give the roots of \(Y^{78}+1\), and the latter those of \(Y^{18}+1\). Their intersection gives the roots of \(Y^6+1\), because the common orders are \(4d\) with \(d\mid3\). All the roots are simple in characteristic zero. Removing the union therefore gives exactly the stated polynomial quotient, with degree \(234+6-78-18=144\). The quotient is an integer polynomial by monic polynomial division of the numerator by the denominator, whose exact divisibility follows from these root multiplicities. Substituting \(V=Y^6\) shows further that
\[
 P(Y)=P_0(Y^6),\qquad
 P_0(V)=\frac{(V^{39}+1)(V+1)}{(V^{13}+1)(V^3+1)} .
\]
The same root argument for the odd divisors of 39, or the original divisibility and monic division in the subring \(\mathbb Z[Y^6]\), gives an integer polynomial \(P_0\) of degree 24. It has at most 25 coefficient positions. For completeness, let \(\xi\) be any primitive 468th root, and \(f\) its monic irreducible polynomial over \(\mathbb Q\). By the integral factor property of monic integer polynomials, \(f\in\mathbb Z[Y]\). For a prime \(p\nmid468\), suppose \(\xi^p\) has a different monic irreducible polynomial \(h\). Then \(f\) divides \(h(Y^p)\) in \(\mathbb Z[Y]\), using monic division. Modulo \(p\), \(h(Y^p)=h(Y)^p\). The reductions of \(f,h\) therefore share an irreducible factor. Both are distinct factors before reduction of \(Y^{468}-1\), and their product divides it. The common factor would repeat in \(Y^{468}-1\) modulo \(p\), which is impossible since its derivative \(468Y^{467}\) has no common root with it. It follows that \(\xi^p\) is also a root of \(f\). The same argument starts at each primitive root of \(f\). Every \(\xi^u\) with \(\gcd(u,468)=1\) is obtained by iterating primes not dividing 468, by factoring a positive representative \(u\). Thus all primitive roots are roots of \(f\), so \(f=P\). This gives an integral cyclotomic domain and its stated coefficient basis. In \(\mathbb F_q\), the subgroup of order 468 exists by the rule. Its primitive elements give the 144 distinct roots of \(P\), because 468 is prime to the characteristic. The modulus reduction and the power-basis description have the same meaning as in the original branch.

The Module-SIS challenge on the selected ring uses a uniform \(k\)-by-\(\ell\) matrix with entries in \(R_q\) and asks for a nonzero vector of integer coefficients of infinity norm at most \(\beta\) annihilated by the matrix modulo \(q\). The estimate has \(k d_R\) scalar equations and \(\ell d_R\) scalar unknowns, over the same \(q\), under the same scoring convention. Indeed each ring row gives \(d_R\) coefficient equations, and the power basis gives \(\ell d_R\) integer coordinates. The reduction below uses the selected module distribution itself. The scalar counts give the dimensions used by the estimator.

### Ring products and evaluated form coefficients

The degree-144 ring product first embeds the two polynomials of degree below 144 into the ordinary coefficient representation modulo \(Y^{234}+1\). Let \(\omega\) have order 468 in \(\mathbb F_q^*\). The roots of that binomial are \(\omega(\omega^2)^j\) for \(0\le j<234\). Scale input coefficients by \(\omega^i\) and take the ordinary length-234 Fourier transform with generator \(\omega^2\). For length \(L=ab\), index the input by \(i=i_0+ai_1\) and the output by \(j=j_1+bj_0\), with \(0\le i_0,j_0<a\) and \(0\le i_1,j_1<b\). The exponent \(ij\) modulo \(L\) equals \(i_0j_1+i_0bj_0+ai_1j_1\). This gives \(a\) transforms of length \(b\), multiplication by the factors associated with \(i_0j_1\), and \(b\) transforms of length \(a\). Use \(a=18,b=13\), further decompose length eighteen into radices two and three and evaluate the length-thirteen sums directly. Inverting uses the transform at the inverse root, scaling by \(1/234\), and undoing the twist. The finite geometric sum of a nontrivial 234th root vanishes, which proves the inverse formula; the sum for the trivial root is 234. Keep the 144 point products at the primitive roots, insert zeros at the other 90 places, interpolate as above and reduce modulo \(P\). This is the correct product by agreeing at all 144 roots of \(P\). Reduction has at most 90 high terms to eliminate with at most 25 coefficient positions of \(P_0(Y^6)\) per term. This uses 144 pointwise products. One can accumulate the products in the evaluation coordinates, then transform the sum back. The transform and reduction require \(O(d_R\log(2d_R))\) field operations since the radices and number of coefficient positions are bounded absolute constants. In the original branch the radix-two version gives the same bound.

For encryption, postcompose multiplication by the already sampled ring entry \(a\) with the linear functional having the arbitrary coefficient table \(L\) of a selected mask and row. In the original negacyclic branch the coefficient adjoint of multiplication by \(a\) is multiplication by \(a(Y^{-1})\). Indeed multiplication by \(Y\) is a signed permutation with inverse multiplication by \(Y^{-1}\), so transposing each monomial map gives the claimed identity by linearity. For the degree-144 branch use the above ring-product circuit for fixed \(a\), which is linear in its input \(u\). The operations have at most two inputs and are copies, sums, differences or multiplication by a fixed field scalar, including multiplication by the evaluation of \(a\). To evaluate the transpose on \(L\), initialize every wire accumulator to zero and add the given output coefficients to the output wire accumulators. Traverse operations backward. If a forward wire satisfies \(z=c_1x_1+c_2x_2\), add \(c_i\) times its accumulator to the accumulator of \(x_i\) for each input occurrence, with the unary version for a unary operation. Each step substitutes a linear expression into the accumulated output linear functional, so the final input accumulators give exactly the coefficients of \(u\mapsto\langle L,a u\bmod P\rangle\). There is a constant number of operations per original operation. This handles all three multiplier tables of Amendment C6 even though their rows are not geometric progressions. The cost is \(O(k(\ell+1)d_R\log(2d_R))\) for the three masks. In the two ring choices of this first disjunct the protected ledger assigns its fixed unit charge to the \(k(\ell+1)d_R\) matrix coefficients. Ring entries use the stipulated seed-oracle calls; at the same unrolled rank the larger ring reduces the coefficient count without changing row-equation dimensions.

### Irreducible lift with split reduction

The second disjunct has \(\mathrm{ring\_mode}=1,\ k=1,\ d=d_R\ge512,\ 2d\le D,\ d<q\), and \(56d<q-1\). These are the numeric conditions of the second C5 disjunct. The first disjunct has \(\mathrm{ring\_mode}=0\) and one of the two degree choices already proved. The construction uses the following third coefficient ring exactly on the second disjunct.

Write the binary expansion of \(d\) as \(d=\sum_{i=0}^{s-1}m_i\) with distinct powers of two \(m_i\), in increasing order. By \(2d\le D\le2^{28}\), the exponents of these powers are at most 27, so \(s\le28\). The protected order \(q-1\) is divisible by \(2^{28}\), hence by every \(m_i\). Fix a public generator \(\gamma\) of \(\mathbb F_q^*\), and consider
\[
 \bar P(Y)=\prod_{i=0}^{s-1}\left(Y^{m_i}-c_i\right),
 \qquad c_i=\gamma^{(i+1)m_i}.
\]
The \(i\)-th factor has exactly the roots \(\gamma^{i+1}\mu_{m_i}\), where \(\mu_{m_i}\) is the group of \(m_i\)-th roots of unity in \(\mathbb F_q\). These roots are distinct because \(m_i<q\). For two different indices an intersection would give \(\gamma^{i-j}\in\mu_{\max(m_i,m_j)}\): these two subgroups are nested, since their orders are powers of two. This would imply that \((q-1)/\max(m_i,m_j)\) divides the nonzero integer \(i-j\). But that divisor is at least \((q-1)/d>56\) and \(|i-j|\le27\). This contradiction proves that all \(d\) roots are distinct and that \(\bar P\) splits completely in \(\mathbb F_q\).

Lift each nonconstant coefficient below the leading term of \(\bar P\) to an even integer in its residue class modulo \(q\); lift the constant coefficient to a value congruent to 2 modulo 4 in its residue class modulo \(q\); keep the leading coefficient 1. The choices exist and can be fixed by taking the least nonnegative value in the respective congruence class modulo \(2q\) or \(4q\), since \(q\) is odd. This defines an integer monic polynomial \(P\). It is irreducible over \(\mathbb Q\). In fact if it has a nontrivial factorization over \(\mathbb Q\), its monic factors have integer coefficients by the monic integral factor property. Modulo two their product is \(Y^d\) and their degrees do not drop, so both are powers of \(Y\) of positive degree. Both integer constant coefficients are even, making the product divisible by four, contrary to \(P(0)\equiv2\bmod4\). This verifies irreducibility directly.

Use \(R=\mathbb Z[Y]/(P)\) and \(R_q=\mathbb F_q[Y]/(\bar P)\), both in the power basis \(1,Y,\ldots,Y^{d-1}\). Reduction of an integer coefficient vector is componentwise modulo \(q\), and it respects addition and multiplication because the defining polynomial reduces to \(\bar P\). A uniform element of \(R_q\) has exactly \(d\) independent uniform field coefficients. The challenge matrix is uniform in this ring, and its solution criterion is the same nonzero integer power-basis vector with coefficient infinity norm at most \(\beta\) and product zero modulo \(q\). We use the coefficient basis in both the actual reduction and the estimate, with no change of the norm to evaluations at the roots. Each ring row gives exactly \(d\) coefficient equations, so the unrolled dimensions used by M1 are \(kd\) and \(\ell d\). This is the same specified convention for costing the uniform coefficient-ring challenge. The ring construction is deterministic from public constants.

### Arithmetic and transpose on the split branch

The public \(\bar P\) can be formed with \(O(d)\) field operations: multiply the \(s\le28\) binomials in order, using a shift and a scalar multiple at each step for each coefficient of the running polynomial. All intermediate lengths are at most \(d+1\). The \(c_i\) values follow from successive powers of \(\gamma\) and at most 27 squarings for each. This and the coefficient lifts fit the fixed setup bound with \(d\le D\). The public field computations concern \(R_q\), so the integer lifts introduce no subsequent field cost.

To multiply \(a,u\) in coefficient form, form \(f=a u\) of degree at most \(2d-2\) by a power-of-two FFT convolution in the subgroup from C3. This works since \(2d\le D\), and takes \(O(d\log(2d))\) field operations. To reduce it, write its quotient and remainder under \(\bar P\) as \(Q_0,R_0\), with \(\deg Q_0\le d-2\), \(\deg R_0<d\). Use reversed polynomials with fixed lengths: \(F^\star(Y)=Y^{2d-2}f(1/Y)\), \(Q^\star(Y)=Y^{d-2}Q_0(1/Y)\), and \(P^\star(Y)=Y^d\bar P(1/Y)\). The reversal of \(R_0\) in length \(2d-1\) is divisible by \(Y^{d-1}\), so
\[
 Q^\star=F^\star (P^\star)^{-1}\bmod Y^{d-1},
 \qquad P^\star=\prod_i(1-c_iY^{m_i}).
\]
The inverse product can be applied one factor at a time to the truncated vector. Dividing a truncated series \(a'\) by \(1-c_iY^{m_i}\) at this length uses the recurrence \(b_j=a'_j+c_i b_{j-m_i}\), with negative indices zero. It costs \(O(d)\) per factor. Reverse \(Q^\star\) to recover \(Q_0\), compute \(\bar P Q_0\) by the same sequence of binomial shift operations, and subtract it from \(f\), which gives \(R_0\) by division uniqueness. These steps take \(O(sd)=O(d)\) additional field operations. No evaluation coordinate is used as an integer coordinate of the challenge.

The product circuit for fixed ring entry \(a\) is linear in \(u\): convolutions by fixed values, frequency scalings, fixed permutations and copies, additions, and fixed-scalar products in the monic reduction. It has \(O(d\log(2d))\) operations, with at most two inputs to each linear operation. The explicit reverse accumulation proved in the preceding transpose paragraph applies to this circuit, producing the coefficients of \(u\mapsto\langle L,a u\bmod\bar P\rangle\) from the form multiplier table \(L\) in the same time. It works for every multiplier table, including those from the mixed-base Frobenius coordinates, since it assumes no shape of \(L\). Thus formation of the three evaluated masks and decryption's ring products have the same \(O(k(\ell+1)d_R\log(2d_R))\) form-work bound. The benchmark's protected unit charge for them still uses \(k(\ell+1)d_R\) matrix coefficients. In the reduction one can alternatively use naive convolution and monic division in \(O(d^2)\) operations and transpose that linear circuit, giving the same \(O((N_\star+n)D)\) fixed cost used in C7. Indeed \(k d\le n\), \((\ell+1)d\le N_\star+2d\), and \(n,d,N_\star\le D\).

The common packing and distribution argument below applies to this branch as well. It uses monicity, the full coefficient basis and the ring equation under reduction, all established here. The rest of the construction acts on the field coefficient forms \(z\), with the same positions and degrees under Amendment n and C6, and the same three ties. Its rank-three classification, view, packing, entropy bounds and proof of extraction do not depend on how ring products were computed. With the above ring operations its group counts, oracle counts and required complexity bounds remain the same. The original power-of-two ring branch still admits the original asymptotic parameter family.

### Kernel conversion and scope

The coefficients are placed at the slots proved in Amendment n. Each uniform entry has exactly \(d_R\) independent field coefficients in the stated power basis. A form-kernel vector therefore has constant coordinate zero and maps to zero under the nonconstant columns in the selected coefficient ring. Conversely these equations force all form coefficients to vanish. A short integer scalar multiple has integer coordinate 0 equal to zero because its residue vanishes and \(2\beta<q\). Forming the packed vector by Amendment ell preserves every ordinary and tag coordinate once, adds only zeros, and commutes with integral reduction and field scaling. This proves the kernel-to-Module-SIS conversion in the heavy-stack lemma and in Targets. The rank bound and inverse theorem use only the search distribution and the short multiple of a vector with zero constant coordinate. Their hypotheses and conclusions are independent of the choice of monic ring. LIFT is a base-field integer-vector operation, so its correctness and time bounds are also independent of that ring.

The reduction programs the chosen uniform Module-SIS challenge into the nonconstant seed matrix columns and samples the constant entries independently in the same ring. This is exactly the stipulated random oracle distribution. The view, mask, classification, and reduction arguments use the resulting linear form map, its stated kernel, and its coefficient tables. Their proofs in Amendments n, C6, C7 and Targets apply without further ring identities. The same ring algorithms account for preprocessing and kernel tests, with the already stated query and runtime capacities. The ring branch with growing power-of-two degree remains available to the asymptotic corollary, as detailed in Amendment C7. Correctness, extraction and the extractability-error corollary for this exact instance follow from Targets and Amendment Ncmp.

## Amendment I3

The amended (I3) is
\[
\Lambda_1\ge 2\sqrt3 R_{\rm tr}\sqrt N_\star,\qquad
\Lambda_2\ge \sqrt2\,\pi R_{\rm tr}^2 N_\star,\qquad
\Lambda_3\ge \frac{20\,\pi R_{\rm tr}^3 N_\star\sqrt N_\star}{9\sqrt2} .
\]
The rank-two and rank-three geometric lower bounds change. All three inequalities here are checked by the parameter model.

### Which inverse-theorem steps use the change

In `blob:admissibility`, (P3) refers to these inverse conditions, and the bounds in (P1), (P2), (P4) and (P5) have no occurrence of a geometric factor \(\Lambda_d\). The box, saturation, reduction, fiber and height definitions in `blob:lattices` use the same lattice operations. The regularity test uses \(m(\Theta)h(\Theta)\le\Gamma_d/g^d\), and has the same definition. In `blob:trimming` the ellipsoid depends on \(R_{\rm tr}\), \(g\), and the basis through \(\Sigma_\Theta\), with no \(\Lambda_d\). The proof of `lem:prefix` uses only the lattice indices and ceiling count in (a)–(b), and (I1), (I2), (I4) to convert the rank-three ceiling count to the height and regularity in (c). The proof of `lem:trim` applies the exponential moment bound for independent box variables, then the exponential loss inequality in (I2). Thus the prefix and trimming lemmas have the same hypotheses and arguments. We prove `lem:sparse`, `lem:regularize\), and `lem:inverse` under the amended condition below.

### Integer-lattice facts used below

For an integral basis \(B\) with a largest row minor on \(J\), each component of \(y\in\operatorname{span}_{\mathbb R}B\) is \(B_iB_J^{-1}y_J\), with entries of the row \(B_iB_J^{-1}\) bounded by one in absolute value by Cramer's rule and maximality of the minor. The component is therefore at most \(\|y_J\|_1\) in absolute value. When the columns of \(B\) generate a saturated integer lattice, their quotient in the ambient free integer group is torsion-free and finitely generated, hence free. Extending these columns by lifts of a quotient basis gives a unimodular basis of the ambient group. Taking its transpose shows \(B^\top\mathbb Z^I=\mathbb Z^d\).

For the lifting fact, let \(\Delta\) be an integer matrix of rank \(k'>0\) with a nonzero minor \(M\) of order \(k'\) on rows \(I_0\) and columns \(J_0\). Put \(\delta=\det M\). If \(|\delta|<q\) then it is invertible modulo the prime \(q\). Given \(c^\top\Delta=0\bmod q\), write \(I_1\) for the remaining rows and choose an integer vector \(w\equiv\delta^{-1}c_{I_1}\bmod q\). Set \(u_{I_1}=\delta w\) and \(u_{I_0}^\top=-w^\top\Delta_{I_1,J_0}\operatorname{adj}M\). Then \(u^\top\Delta_{J_0}=0\) by the adjugate identity. Those columns span the column space over \(\mathbb Q\), so \(u^\top\Delta=0\). The inside rows also agree with \(c\) modulo \(q\), by uniqueness of the solution for them using \(M\) invertible modulo \(q\). For rank zero take \(u=c\). These facts use no inverse-parameter condition other than the indicated minor bound at the lifting step.

### Prefix estimates

Here are the unchanged parts of the prefix lemma on the amended parameter domain. Let \(\Theta\) be a saturated lattice of rank \(d\), with integral basis matrix \(B\) and a largest minor on \(J\). Order its coordinates with \(J\) first, let \(I_k\) be the first \(k\) coordinates, and let \(\Theta_k=\operatorname{span}_{\mathbb R}(B_{I_k})\cap\mathbb Z^{I_k}\), \(k\ge d\). Let \(h_k,m_k\) be its height and largest fiber density. Its rank is \(d\) because the selected minor remains invertible. If \(Y\) is a basis of \(\Theta_k\), then \(B_{I_k}=Y C\) for an integral nonsingular \(d\)-square matrix \(C\). The fibers of the prefix are thus the level sets of \(B_{I_k}^{\top}r\). The group \(G_k=B_{I_k}^{\top}\mathbb Z^{I_k}=C^\top\mathbb Z^d\), by saturation and the integer-lattice lemma (b), has index \(|\det C|\) in \(\mathbb Z^d\). The \(d\)-row determinants of \(B_{I_k}\) are multiplied from those of \(Y\) by \(\det C\). As their largest absolute value is the original \(h(\Theta)\), this gives \(h_k [\mathbb Z^d:G_k]=h(\Theta)\) and shows that \(J\) is still a largest minor for \(\Theta_k\). At \(k=d\), the column span is all of \(\mathbb R^J\), so \(\Theta_d=\mathbb Z^J\), \(h_d=1\) and \(m_d=g^{-d}\). At the full set of coordinates the saturated lattice is \(\Theta\).

On adding the next row to \(B_{I_k}\), let \(s_k\) be the order of that row as a column in the quotient \(\mathbb Z^d/G_k\). Adjoining it multiplies the size of the subgroup modulo \(G_k\) by \(s_k\), so \(h_{k+1}=s_k h_k\) by the index identity. For a fixed value of \(B_{I_{k+1}}^\top r\), the new coordinate is in at most one residue class modulo \(s_k\); its allowed values in an interval of \(g\) integers number at most \(\lceil g/s_k\rceil\). For each such value the remaining prefix has fiber density at most \(m_k\). Consequently \(m_{k+1}\le m_k\lceil g/s_k\rceil/g\). If \(s_k\ge g\) this also makes the new coordinate constant on the fiber. If \(s_k=1\), the power inequality \(m_{k+1}^b h_{k+1}^{b-1}\le m_k^b h_k^{b-1}\) is immediate. For \(2\le s=s_k<g\), use \(\lceil g/s\rceil/g\le 1/s+1/g\le s^{-1+1/b}\). To verify the second inequality, if \(s\ge2^b\) then \(1/s+1/g<2/s\le s^{-1+1/b}\). Otherwise \(g\ge2^b\) and the concave function \(x^{1/b}-1-x/2^b\) is nonnegative on \([2,2^b]\): it is zero at \(2^b\), and at \(2\) it is at least \((\log 2)/b-2^{1-b}>0\) for \(b\ge7\). The last strict inequality follows from \(\log 2>1/2\) and \(2^{b-2}>b\) for integers \(b\ge7\). This proves the power inequality in all its cases.


### Rank-three height and regularity

This subsection treats the full-rank choice in Amendment I4. On its dense choice the rank-three density premise is impossible by the fiber bound in I4.

Let \(\Theta\) be a rank-three saturated lattice on a set of at most \(N_\star\) coordinates with \(m(\Theta)\ge\mu_{\rm tr}\). Apply the preceding prefix estimates with a largest minor of size three ordered first. At the first rank-three prefix the height is 1 and density \(g^{-3}\). Write \(s_1,\ldots,s_a\) for the nontrivial step orders (at least 2), in the original prefix order. The height and density are bounded by
\[
   h(\Theta)=\prod_{i=1}^a s_i,\qquad
   m(\Theta)\le g^{-3}F,\qquad
   F=\prod_{i=1}^a\frac{\lceil g/s_i\rceil}{g}.
\]
Every factor of \(F\) is at most 1. Empty products are 1.

We prove \(h(\Theta)\le H_3\). Let \(h=h(\Theta)\). Expanding \(\prod_i(1/s_i+1/g)\), the term without \(1/g\) is \(1/h\); since \(1/s_i\le1/2\), all the other terms sum to at most \((1/2+1/g)^a-(1/2)^a\). This difference is 0 if \(a=0\). Otherwise the mean-value inequality bounds it by \(a(1/2+1/g)^{a-1}/g\le (1+2/g)/g\). Indeed the numerator for \(a=1\) is 1, at \(a=2\) it is \(1+2/g\), and for \(a\ge2\) the ratio at successive \(a\) is \((1+1/a)(1/2+1/g)<1\) because \(g\ge128\). Since \(\lceil g/s_i\rceil/g\le1/s_i+1/g\), we have
\[
 m(\Theta)\le g^{-3}\xi_{\rm tr}(1/h+1/g).
\]
This proves \(h\le H_*\) from Amendment H3. The additional integer height bound proved there gives \(h\le H_3\).

Multiplying the same density bound by \(h\) and using \(h\le H_3\) gives \(m(\Theta)h\le g^{-3}\xi_{\rm tr}(1+H_3/g)\le g^{-3}\Gamma_3\) by (I4). This is the required rank-three regularity.

### Trimming estimate

For the trimming lemma, a centered uniform box entry can be added to a uniform independent variable on \([-1/2,1/2]\) to get the continuous uniform variable on \([-g/2,g/2]\). The added variable's moment generating function is at least one by convexity, so the centered box entry has moment generating function bounded by \(\sinh(x)/x\) with \(x=tg/2\) at argument \(t\). Its series is bounded by \(e^{x^2/6}\) because \((2j+1)!\ge6^j j!\) for \(j\ge0\), by induction on \(j\). Let \(Y=B^\top r-\mathbb E[B^\top r]\) and \(\Sigma=(g^2/12)B^\top B\). Independence of the box entries gives \(\mathbb E e^{u^\top Y}\le e^{u^\top\Sigma u/2}\). With \(Z\) an independent standard \(d\)-dimensional Gaussian, the Gaussian moment generating function gives
\[
 \mathbb E e^{(99/200)\|\Sigma^{-1/2}Y\|_2^2}
 =\mathbb E e^{\sqrt{99/100}\,Z^\top\Sigma^{-1/2}Y}
 \le \mathbb E e^{(99/200)\|Z\|_2^2}=10^d .
\]
The inequality conditions on \(Z\); the last equality follows by scaling each normal density in the integral. By Markov's inequality the probability of being outside the trimming ellipsoid is at most \(10^d e^{-99R_{\rm tr}^2/200}\le\varepsilon_{\rm tr}\) by (I2) and \(d\le3\). Trimming any subset removes at most that absolute density. This establishes the trimming conclusion without a norm assumption.


### Projected fiber counts

The claim of `lem:sparse` is as follows. Let \(B\) be a basis of an integral lattice \(\Theta\) on a coordinate set \(I\) with \(|I|\le N_\star\), of rank \(d\in[3]\). Let \(F\ne\varnothing\) be a set of points of the integer box on \(I\cup\{i'\}\), \(i'\notin I\), trimmed by \(\Theta\), and \(\Phi(r)=(B^\top r_I,r_{i'})\). If (a) \(\Phi(F)\) has affine dimension \(d+1\) and lies in a coset of an index-\(q\) subgroup of \(\mathbb{Z}^{d+1}\), then
\(\Pr[F]\le\Lambda_d g^d h(\Theta)m(\Theta)/q\).
If (b) \(F^\perp\) has rank \(d'\) with \(1\le d'<d\), a largest minor on \(J\subseteq I\), and every vector of \(F^\perp\) restricts to a vector in \(\operatorname{span}_{\mathbb R}\Theta\) on \(I\), then
\(\Pr[F]h(F^\perp)\le\Lambda_{d-d'}\,g^{d-d'}h(\Theta)m(\Theta)\).
Here \(F^\perp\) is the lattice of integer vectors normal to the differences in \(F\).

For each possible image \((y,x)\), the probability of \(B^\top r_I=y,r_{i'}=x\) is at most \(m(\Theta)/g\) by independence, so \(\Pr[F]\le|\Phi(F)|m(\Theta)/g\). We count images in \(C=\mathcal{T}_\Theta\times[2,g+1]\).

For (a), put \(s=d+1\), \(\delta=q\), \(J=\varnothing\), and let \(p\) be the identity. Write \(B=(B_1,B_2)\) with \(B_1\) empty, and use \(|\det(B_1)_J|=1\).
For (b), put \(s=d+1-d'\) and let \(Y\) be an integral basis matrix of \(F^\perp\); \(Y_J\) is invertible. The submatrix \(B_J\) has row rank \(d'\) since the columns \(Y_J\) lie in its real column span. The integral kernel of \(B_J\) is saturated in \(\mathbb{Z}^d\), of rank \(d-d'\). It has a basis that extends to an integral basis of \(\mathbb{Z}^d\): the quotient by a saturated subgroup of \(\mathbb{Z}^d\) is finitely generated and torsion-free, hence free, and lifts of a quotient basis give the extension. Using this basis change, write \(B=(B_1,B_2)\) where \((B_2)_J=0\) and \((B_1)_J\) is invertible square. The columns of \(B_2\) number \(s-1\). Trimming is basis independent since the mean and covariance transform by the same invertible change on the image coordinates.

In case (b), the injective map \(a=(a_{[d]},a_{d+1})\mapsto(Ba_{[d]},a_{d+1})\) maps the real annihilator of the differences of \(\Phi(F)\) isomorphically onto the real annihilator of the differences of \(F\), by the restriction assumption. The first annihilator has dimension \(d'\) and its integer points form a saturated lattice with basis matrix \(V\). The real annihilator of differences of \(F\) is spanned by its integer points because those differences are integer vectors, so the restriction premise on integer normals suffices for this isomorphism. Split its rows into \(V_1,V_2,V_3\) of lengths \(d',s-1,1\). The image of its basis is \(Y A\) for an integral nonsingular \(d'\)-square matrix \(A\), as its columns are integral independent normals. At rows \(J\), this gives
\[
(B_1)_J V_1=Y_J A .
\]
Consequently \(V_1\) is invertible and \(|\det(B_1)_J|\,\delta\ge h(F^\perp)\), where \(\delta=|\det V_1|\). Write \(y=(y_1,y_2)\) according to the basis split. Projection \(p:(y,x)\mapsto(y_2,x)\) is injective on any affine translate of the kernel of \(V^\top\), because there the first block of a difference is determined by \(V_1^\top\). It therefore preserves the affine dimension of \(\Phi(F)\), which is \(s\). The projections of differences of image points lie in the kernel of
\[
 (y_2,x)\longmapsto V_2^\top y_2 + x V_3^\top
          \pmod{V_1^\top\mathbb{Z}^{d'}} .
\]
The map is onto because \(V^\top \mathbb{Z}^{d+1}=\mathbb{Z}^{d'}\) by saturation and `lem:lattice-facts` (b), while the \(y_1\) contribution vanishes in the quotient. The kernel has index \(\delta\) in \(\mathbb{Z}^s\). Thus in both cases \(p(\Phi(F))\) has full affine dimension \(s\), cardinality \(|\Phi(F)|\), and lies in \(p(C)\) and in a coset of an index-\(\delta\) lattice.

A full-dimensional finite set \(X\) of \(m\) points in such a coset has \(\operatorname{vol}_s\operatorname{conv}(X)\ge(m-s)\delta/s!\). To see this, start from any \(s+1\) affinely independent points forming a simplex. One can add the points successively while maintaining a triangulation of their hull using all inserted points as vertices. For a point outside the hull, each boundary facet simplex strictly visible to the point gives a new simplex by coning it to the point. Those simplices have disjoint interiors and fill the new region, as rays from the point first hit the old hull in its visible boundary. At least one facet is strictly visible, so at least one full simplex is added. If a point is in the hull, take the unique smallest face of the triangulation containing it. This face has positive dimension since the point is distinct from all earlier vertices. Subdivide that face by coning its boundary faces to the point and make the corresponding subdivision of every full simplex incident to it, by adjoining the complementary simplex vertices. This covers exactly those full simplices and replaces each by at least two, since the point lies in the relative interior of the face. Hence there are at least \(m-s\) full simplices. Each has volume at least \(\delta/s!\), since the determinant of \(s\) independent differences of coset points is a nonzero integer multiple of the determinant \(\delta\) of its lattice. Since \(m\ge s+1\), the region containing \(X\), if convex, has volume at least \(\delta/s!\). In particular, applying both consequences to \(p(C)\) gives
\[
 |\Phi(F)|\le s!\operatorname{vol}_s p(C)/\delta+s
             \le (s+1)!\operatorname{vol}_s p(C)/\delta .
\]

The projection of the ellipsoid \(\mathcal{T}_\Theta\) to the last \(s-1\) coordinates has volume \(v_{s-1}R_{\rm tr}^{s-1}(g/\sqrt{12})^{s-1}\sqrt{\det(B_2^\top B_2)}\), where \(v_j\) is the volume of the Euclidean unit \(j\)-ball. Indeed, write the ellipsoid as the image of a unit ball by \(R_{\rm tr}\Sigma_\Theta^{1/2}\) plus the center. The projected map has a Gram matrix on its range equal to the bottom-right block \(R_{\rm tr}^2(g^2/12)B_2^\top B_2\), which gives the product of its nonzero singular values. The interval in \(p(C)\) has length \(g-1\). In either case \((B_2)_J=0\). By expansion of \(\det(B_2^\top B_2)\) into squared row minors, and because \(|\det(B_1)_J\det(B_2)_{J'}|=|\det B_{J\cup J'}|\le h(\Theta)\) for each \(J'\subseteq I\setminus J\) of size \(s-1\),
\[
 |\det(B_1)_J| \sqrt{\det(B_2^\top B_2)}
 \le h(\Theta)\sqrt{\binom{N_\star}{s-1}} .
\]
Combining with the counting bound and \(\Pr[F]\le |\Phi(F)|m(\Theta)/g\) gives
\[
 \Pr[F]|\det(B_1)_J|\delta
 \le g^{j}h(\Theta)m(\Theta)
      (j+2)!v_j R_{\rm tr}^{j}\sqrt{\binom{N_\star}{j}/12^j},
 \qquad j=s-1 .
\]
Use \(\binom{N_\star}{j}\le N_\star^j/j!\) and \(v_1=2,v_2=\pi,v_3=4\pi/3\). The three upper bounds on the geometric factor are \(2\sqrt3 R_{\rm tr}\sqrt N_\star\), \(\sqrt2\pi R_{\rm tr}^2N_\star\), and \(20\pi R_{\rm tr}^3N_\star^{3/2}/(9\sqrt2)\). They are at most the three allowed \(\Lambda_j\). In case (a), divide by \(q\) to obtain the claim. In (b), replace \(|\det(B_1)_J|\delta\) by \(h(F^\perp)\) on the left to obtain the claim.

### Regularization with the new count

This subsection proves regularization on the full-rank choice. Amendment I4 gives the dense-choice argument.

The claim of `lem:regularize` is that a saturated lattice \(\Theta\) of rank \(d\in[3]\) with \(m(\Theta)\ge\mu_{\rm tr}+(3-d)\varepsilon_{\rm tr}\) is contained in a regular saturated lattice of rank in \([d,3]\) and maximum fiber density at least \(m(\Theta)-(3-d)\varepsilon_{\rm tr}\).

Write \(\mu=\mu_{\rm tr}\) and \(e=\varepsilon_{\rm tr}\) in this paragraph and the next two. Induct downwards on the initial rank. For \(d=3\), `lem:prefix` (c) gives regularity directly. For \(d\le2\), use `lem:prefix` with a largest minor at \(J\) and \(J\) first in the coordinate order. Denote the prefixes by \(\Theta_k\), their heights and max densities by \(h_k,m_k\), and the step order by \(s_k\). The densities are nonincreasing, so each is at least \(\mu+(3-d)e\). Take a densest fiber of \(\Theta_k\) to form \(F_k\). If the preceding \(F_{k-1}^\perp\) strictly contains \(\Theta_{k-1}\), trim this fiber by the regular containing lattice \(\widetilde\Theta_{k-1}\) specified below. Otherwise leave the fiber whole. The density of each \(F_k\) is at least \(m_k-e\) by `lem:trim`. Its normal lattice contains \(\Theta_k\). If this inclusion is strict, saturation gives a rank \(d_k>d\). Its rank is at most three since a fiber of a rank-\(a\) lattice has density at most \(g^{-a}\) by fixing coordinates outside an invertible \(a\)-row minor, and \(g^{-4}<\mu\le m_k-(3-d)e\) by (I5). Its max fiber density is at least \(\Pr[F_k]\ge\mu+(2-d)e\ge\mu+(3-d_k)e\). By induction let \(\widetilde\Theta_k\) be a regular saturated containing lattice of rank at least \(d_k\), with \(m(\widetilde\Theta_k)\ge m(F_k^\perp)-(3-d_k)e\ge m_k-(3-d)e\). This constructs the trimming lattice for the next step, and if \(F_{|I|}^\perp\ne\Theta\) it gives the desired final lattice.

If \(F_{|I|}^\perp=\Theta\), let \(j<|I|\) be the last strict index, or \(j=d-1\) when there is none. For \(j<k<|I|\) the step order \(s_k\) is below \(g\). Otherwise `lem:prefix` (b) would make the new coordinate constant in the fiber of \(\Theta_{k+1}\) containing \(F_{k+1}\); its unit vector would then be in \(F_{k+1}^\perp=\Theta_{k+1}\) and vanish at \(J\), forbidden by `lem:lattice-facts` (a). Iterating the power inequality in `lem:prefix` (b) gives
\[
 \mu(m(\Theta)h(\Theta))^{b-1}
 \le m(\Theta)^b h(\Theta)^{b-1}
 \le m_{j+1}^{b}h_{j+1}^{b-1}.
\]
When \(j=d-1\), \(m_d=g^{-d}, h_d=1\). The bound on \(\Gamma_d^{b-1}\) in (I4) gives \(m_d^{b}h_d^{b-1}\le\mu(\Gamma_d/g^d)^{b-1}\).

When \(j\ge d\), let \(\tilde d\) be the rank of \(\widetilde\Theta_j\). The set \(F_{j+1}\) was trimmed by this lattice. Its normal lattice is exactly \(\Theta_{j+1}\), of rank \(d<\tilde d\), and with largest minor on \(J\) by `lem:prefix` (a). Restrictions to the first \(j\) coordinates lie in the span of \(\Theta_j\) by the definition of the prefix lattice, hence in the span of \(\widetilde\Theta_j\). Apply the proved projected count (b). Since \(\Pr[F_{j+1}]\ge m_{j+1}-e\ge m_{j+1}/A_{\rm inv}\) by (I4) and \(m_{j+1}\ge\mu\), regularity gives
\[
 m_{j+1}h_{j+1}\le A_{\rm inv}\Lambda_{\tilde d-d}\Gamma_{\tilde d}/g^d .
\]
Also \(m_{j+1}\le m_j\le\Pr[F_j]+e\le g^{-d-1}+e\le\mu P_d^{b-1}\) by the rank of \(F_j^\perp\) and (I4). For \(d=1\), (I4) allows \(2e\) in the numerator and therefore implies the same inequality. In all three rank pairs \((d,\tilde d)\in\{(1,2),(1,3),(2,3)\}\), the last growth inequalities of (I4) imply \(A_{\rm inv}\Lambda_{\tilde d-d}\Gamma_{\tilde d}P_d\le\Gamma_d\). Multiplying yields \(m_{j+1}^b h_{j+1}^{b-1}\le\mu(\Gamma_d/g^d)^{b-1}\). Now \(b>1\) and \(\mu>0\) give \(m(\Theta)h(\Theta)\le\Gamma_d/g^d\). This proves regularity and finishes the induction.

The inverse theorem under this (I3) is proved in full in the Amended inverse theorem subsection of Amendment I6. Its full-rank branch uses the results in this section. Its dense branch uses the same projected counts and the dense-choice regularization in I4. In particular, the resulting height and norm conclusions use the same values of the geometric factors that this section proves sufficient.

## Amendment I4

Require either the full-rank choice or the dense choice. The choice controls which inverse proof applies. The published lists and both algorithms have the same definition in the two choices. If both hold, use the full-rank proof.

The full-rank choice requires \(g^2\le2^{40}\cdot2^\lambda\) and the conjunction
\[
\begin{gathered}
 \Gamma_3\ge\xi_{\rm tr}(1+H_3/g),\qquad
 A_{\rm inv}\ge\mu_{\rm tr}/(\mu_{\rm tr}-\varepsilon_{\rm tr}),\\
 P_2^{b-1}\ge(g^{-3}+\varepsilon_{\rm tr})/\mu_{\rm tr},\qquad
 P_1^{b-1}\ge(g^{-2}+2\varepsilon_{\rm tr})/\mu_{\rm tr},\\
 \Gamma_2^{b-1}\ge g^{-2}/\mu_{\rm tr},\qquad
 \Gamma_1^{b-1}\ge g^{-1}/\mu_{\rm tr},\\
 \Gamma_2\ge A_{\rm inv}\Lambda_1\Gamma_3P_2,\qquad
 \Gamma_1\ge A_{\rm inv}\max\{\Lambda_1\Gamma_2,\Lambda_2\Gamma_3\}P_1 .
\end{gathered}
\]
The upper range constraint also gives the original specialization of the search cost to \(O(2^{\lambda/4}N_\star^{1/4})\) in the common efficiency derivation below. The full-rank inverse premises are derived in I3, H2 and I6. This choice permits the original range scale \(g=\Theta(2^{\lambda/2})\).

The dense choice requires \(g^2\le2^{40}\cdot2^{\lambda}\) and the conjunction
\[
\begin{gathered}
g^3\mu_{\rm tr}>(1+1/\sqrt g)^{255},\qquad
\Gamma_2\ge \xi_{\rm tr}\left(1+\frac1g\min\left\{g-1,\frac{\xi_{\rm tr}}{g^2\mu_{\rm tr}-\xi_{\rm tr}/g}\right\}\right),\\
A_{\rm inv}\ge \mu_{\rm tr}/(\mu_{\rm tr}-\varepsilon_{\rm tr}),\qquad
P_1^{\,b-1}\ge (g^{-2}+2\varepsilon_{\rm tr})/\mu_{\rm tr},\\
\Gamma_1^{\,b-1}\ge g^{-1}/\mu_{\rm tr},\qquad
\Gamma_1\ge A_{\rm inv}\Lambda_1\Gamma_2 P_1.
\end{gathered}
\]
Put \(\mu=\mu_{\rm tr}\), \(e=\varepsilon_{\rm tr}\) in this amendment. A rank-\(a\) lattice's box fiber has probability at most \(g^{-a}\): conditional on the coordinates outside an invertible \(a\)-row basis minor, the equations have at most one solution in the remaining coordinates. Hence a lattice of density at least \(\mu>g^{-3}\) cannot have rank three or above. The original rank-three clause of the prefix result is vacuous. We prove the rank-two replacement needed by regularization and the inverse step.

### Prefix estimates

The following gives the dependencies of the prefix and trimming statements explicitly. Let \(\Theta\) be a saturated lattice of rank \(d\), with integral basis matrix \(B\) and a largest minor on \(J\). Order its coordinates with \(J\) first, let \(I_k\) be the first \(k\) coordinates, and let \(\Theta_k=\operatorname{span}_{\mathbb R}(B_{I_k})\cap\mathbb Z^{I_k}\), \(k\ge d\). Let \(h_k,m_k\) be its height and largest fiber density. Its rank is \(d\) because the selected minor remains invertible. If \(Y\) is a basis of \(\Theta_k\), then \(B_{I_k}=Y C\) for an integral nonsingular \(d\)-square matrix \(C\). The fibers of the prefix are thus the level sets of \(B_{I_k}^{\top}r\). The group \(G_k=B_{I_k}^{\top}\mathbb Z^{I_k}=C^\top\mathbb Z^d\), by saturation and the integer-lattice lemma (b), has index \(|\det C|\) in \(\mathbb Z^d\). The \(d\)-row determinants of \(B_{I_k}\) are multiplied from those of \(Y\) by \(\det C\). As their largest absolute value is the original \(h(\Theta)\), this gives \(h_k [\mathbb Z^d:G_k]=h(\Theta)\) and shows that \(J\) is still a largest minor for \(\Theta_k\). At \(k=d\), the column span is all of \(\mathbb R^J\), so \(\Theta_d=\mathbb Z^J\), \(h_d=1\) and \(m_d=g^{-d}\). At the full set of coordinates the saturated lattice is \(\Theta\).

On adding the next row to \(B_{I_k}\), let \(s_k\) be the order of that row as a column in the quotient \(\mathbb Z^d/G_k\). Adjoining it multiplies the size of the subgroup modulo \(G_k\) by \(s_k\), so \(h_{k+1}=s_k h_k\) by the index identity. For a fixed value of \(B_{I_{k+1}}^\top r\), the new coordinate is in at most one residue class modulo \(s_k\); its allowed values in an interval of \(g\) integers number at most \(\lceil g/s_k\rceil\). For each such value the remaining prefix has fiber density at most \(m_k\). Consequently \(m_{k+1}\le m_k\lceil g/s_k\rceil/g\). If \(s_k\ge g\) this also makes the new coordinate constant on the fiber. If \(s_k=1\), the power inequality \(m_{k+1}^b h_{k+1}^{b-1}\le m_k^b h_k^{b-1}\) is immediate. For \(2\le s=s_k<g\), use \(\lceil g/s\rceil/g\le 1/s+1/g\le s^{-1+1/b}\). To verify the second inequality, if \(s\ge2^b\) then \(1/s+1/g<2/s\le s^{-1+1/b}\). Otherwise \(g\ge2^b\) and the concave function \(x^{1/b}-1-x/2^b\) is nonnegative on \([2,2^b]\): it is zero at \(2^b\), and at \(2\) it is at least \((\log 2)/b-2^{1-b}>0\) for \(b\ge7\). The last strict inequality follows from \(\log 2>1/2\) and \(2^{b-2}>b\) for integers \(b\ge7\). This proves the power inequality in all its cases.

For a rank-two saturated lattice with \(m(\Theta)\ge\mu\), use these estimates with its largest minor first. At the first rank-two prefix the height is 1 and density \(g^{-2}\). Write \(s_1,\ldots,s_a\) for the nontrivial step orders (at least 2), in the original prefix order. The height and density are bounded by
\[
   h(\Theta)=\prod_{i=1}^a s_i,\qquad
   m(\Theta)\le g^{-2}F,\qquad
   F=\prod_{i=1}^a\frac{\lceil g/s_i\rceil}{g}.
\]
Every factor of \(F\) is at most 1. Empty products are 1.

First obtain an upper bound on the density from the height. Let \(h=h(\Theta)\). Expanding \(\prod_i(1/s_i+1/g)\), the term without \(1/g\) is \(1/h\); since \(1/s_i\le1/2\), all the other terms sum to at most \((1/2+1/g)^a-(1/2)^a\). This difference is 0 if \(a=0\). Otherwise the mean-value inequality bounds it by \(a(1/2+1/g)^{a-1}/g\le (1+2/g)/g\). Indeed the numerator for \(a=1\) is 1, at \(a=2\) it is \(1+2/g\), and for \(a\ge2\) the ratio at successive \(a\) is \((1+1/a)(1/2+1/g)<1\) because \(g\ge128\). Since \(\lceil g/s_i\rceil/g\le1/s_i+1/g\), we have
\[
 m(\Theta)\le g^{-2}\xi_{\rm tr}(1/h+1/g).
\]


We now show \(h\le g-1\) in the stated density range. Suppose instead that \(h\ge g\). We will show
\[
                        gF \le (1+g^{-1/2})^{255}.
\]
For every step with \(s_i\le\sqrt g\), its factor satisfies
\[
 \frac{\lceil g/s_i\rceil}{g}\le\frac{1+g^{-1/2}}{s_i}.
\]
If there are no orders above \(\sqrt g\), retain a shortest initial list of the orders with product at least \(g\). The list exists since \(h\ge g\), and there are at most 255 retained orders: the preceding product is less than \(g<2^{254}\), and each order is at least 2. Dropping other factors can only increase \(F\). The product on the retained list is at most \((1+g^{-1/2})^{255}/g\).

If there are at least two orders above \(\sqrt g\), the respective factors are each at most \(1/\sqrt g+1/g\). Dropping all others gives \(gF\le(1+g^{-1/2})^2\). In the remaining case let \(s_*\) be the unique order above \(\sqrt g\) and let \(a_*=\lceil g/s_*\rceil\ge1\). The product of all other orders is an integer at least \(g/s_*\) by \(h\ge g\), hence at least \(a_*\). Retain a shortest initial list of those small orders with product at least \(a_*\), empty if \(a_*=1\). As \(a_*\le g\), there are at most 255 retained orders. Their factors have product at most \((1+g^{-1/2})^{255}/a_*\). The large order contributes exactly \(a_*/g\). Dropping other factors gives the claimed bound in this last case too.

If \(h\ge g\), the three cases above give \(gF\le(1+g^{-1/2})^{255}\). But the rank-two density inequality and amended (I4) give \(gF\ge g^3m(\Theta)\ge g^3\mu_{\rm tr}>(1+g^{-1/2})^{255}\). This contradiction proves \(h<g\), hence \(h\le g-1\) by integrality.

The ceiling expansion also gives a second height bound. For \(g\ge128\), \(1+1/\sqrt g>1+2/g\), and hence \((1+1/\sqrt g)^{255}>\xi_{\rm tr}\). The new guard therefore implies \(g^2\mu_{\rm tr}-\xi_{\rm tr}/g>0\). Combining \(m(\Theta)\ge\mu_{\rm tr}\) with \(m(\Theta)\le g^{-2}\xi_{\rm tr}(1/h+1/g)\) and solving for \(h\) gives
\[
 h\le\frac{\xi_{\rm tr}}{g^2\mu_{\rm tr}-\xi_{\rm tr}/g}.
\]
Use the smaller of this bound and \(g-1\) in the same expansion after multiplying by \(h\). The amended lower bound on \(\Gamma_2\) then gives \(m(\Theta)h(\Theta)\le g^{-2}\Gamma_2\), which proves rank-two regularity. The ratio \(\Gamma_2/(g^2\mu_{\rm tr})\) bounds every regular rank-two lattice of density at least \(\mu_{\rm tr}\). Amendment H2 combines this ratio with an independent integral height bound.

### Trimming estimate

For the trimming lemma, a centered uniform box entry can be added to a uniform independent variable on \([-1/2,1/2]\) to get the continuous uniform variable on \([-g/2,g/2]\). The added variable's moment generating function is at least one by convexity, so the centered box entry has moment generating function bounded by \(\sinh(x)/x\) with \(x=tg/2\) at argument \(t\). Its series is bounded by \(e^{x^2/6}\) because \((2j+1)!\ge6^j j!\) for \(j\ge0\), by induction on \(j\). Let \(Y=B^\top r-\mathbb E[B^\top r]\) and \(\Sigma=(g^2/12)B^\top B\). Independence of the box entries gives \(\mathbb E e^{u^\top Y}\le e^{u^\top\Sigma u/2}\). With \(Z\) an independent standard \(d\)-dimensional Gaussian, the Gaussian moment generating function gives
\[
 \mathbb E e^{(99/200)\|\Sigma^{-1/2}Y\|_2^2}
 =\mathbb E e^{\sqrt{99/100}\,Z^\top\Sigma^{-1/2}Y}
 \le \mathbb E e^{(99/200)\|Z\|_2^2}=10^d .
\]
The inequality conditions on \(Z\); the last equality follows by scaling each normal density in the integral. By Markov's inequality the probability of being outside the trimming ellipsoid is at most \(10^d e^{-99R_{\rm tr}^2/200}\le\varepsilon_{\rm tr}\) by (I2) and \(d\le3\). Trimming any subset removes at most that absolute density. This establishes the trimming conclusion without a norm assumption.


### Regularization

A saturated rank-\(d\) lattice with density at least \(\mu+(3-d)e\) has a regular saturated containing lattice of rank in \([d,3]\) and density at least its own minus \((3-d)e\). For \(d=3\) the premise is impossible. For \(d=2\) the lattice is already regular, by the estimate above. It remains to prove the statement for \(d=1\).

Order the coordinates of the rank-one starting lattice \(\Theta\) with its largest minor \(J\) first. Use the prefix lattices and write \(h_k,m_k\) for their heights and maximum densities. By monotonicity of the prefix density, \(m_k\ge m(\Theta)\ge\mu+2e\). In a densest fiber of prefix \(k\), use the whole fiber when \(k=1\) or there is no strict normal-lattice enlargement at \(k-1\). Otherwise trim it by the normal lattice constructed there. Call the resulting set \(F_k\). In either case \(\Pr[F_k]\ge m_k-e>\mu\). Its integer normal lattice \(F_k^\perp\) is saturated and contains \(\Theta_k\), since every prefix equation is constant on the fiber. A strict inclusion increases rank (both lattices are saturated), so the normal lattice then has rank at least two and at most two by the fiber bound. Its density is at least \(\Pr[F_k]\), and it is regular by the rank-two estimate. This makes it a valid trimming lattice for the next prefix. If the inclusion at the full prefix is strict, its normal lattice is the desired regular extension, with loss at most \(e\).

Otherwise let \(j\) be the last strict prefix, or \(j=0\) when none is strict. For \(k>j\) the step to prefix \(k+1\) must have order below \(g\). If not, that coordinate would be constant on \(F_{k+1}\) by the prefix count, so its unit vector would lie in \(F_{k+1}^\perp=\Theta_{k+1}\). It vanishes on the largest minor \(J\) and so cannot lie in that rank-one span. Iterating the prefix power bound gives
\[
 \mu(m(\Theta)h(\Theta))^{b-1}
 \le m(\Theta)^b h(\Theta)^{b-1}
 \le m_{j+1}^b h_{j+1}^{b-1}.
\]
If \(j=0\), then \(m_1=g^{-1}\) and \(h_1=1\), and the lower bound on \(\Gamma_1^{b-1}\) gives \(m_{j+1}^b h_{j+1}^{b-1}\le\mu(\Gamma_1/g)^{b-1}\).

If \(j\ge1\), \(F_{j+1}\) was trimmed by regular \(F_j^\perp\) of rank two, and its own normal lattice is \(\Theta_{j+1}\), of rank one. The largest minor is \(J\), and each vector in \(\Theta_{j+1}\) restricts to the span of \(\Theta_j\), hence to the span of \(F_j^\perp\). The projected count (b) of Amendment I3, applied with difference of ranks one, and the density loss inequality yield
\[
 m_{j+1}h_{j+1}
 \le A_{\rm inv}\,\Pr[F_{j+1}]\,h_{j+1}
 \le A_{\rm inv}\Lambda_1 g\,m(F_j^\perp)h(F_j^\perp)
 \le A_{\rm inv}\Lambda_1\Gamma_2/g .
\]
The first inequality uses \(m_{j+1}\ge\mu\) and \(A_{\rm inv}\ge\mu/(\mu-e)\). Also \(m_{j+1}\le m_j\le\Pr[F_j]+e\le g^{-2}+e\le\mu P_1^{b-1}\), since \(F_j\) lies in a rank-two normal-lattice fiber. Multiplying the two bounds gives \(m_{j+1}^b h_{j+1}^{b-1}\le\mu(\Gamma_1/g)^{b-1}\) by the checked growth condition. Both cases imply \(m(\Theta)h(\Theta)\le\Gamma_1/g\), so the original lattice is regular. This proves the statement in all possible ranks.

The admissibility block uses these conditions through (P3). The lattice and trimming definitions and the actual projected count do not use the removed growth conditions. Their estimates are proved above and in Amendment I3. Amendment I6 proves the resulting inverse theorem. For the heavy-stack consequences, the guessing-probability rank bound and \(g^3\theta>g^3\mu>1\) imply that a heavy stack has rank at most two. A kernel vector is zero at coordinate zero and has guessing probability at least that of the stack, so the amended inverse theorem gives its short multiple. The packing and its norm are verified in Targets. These are the dense-choice arguments. The rank-three bound and full-rank regularization are proved in Amendment I3. In the full-rank choice the protected stack rank bound and (I5) give rank at most three.

## Amendment H2

Write \(A_g=(1+g^{-1/2})^{255}\), \(B_g=(1+g^{-1/2})^{256}\), \(M=g^3\mu_{\rm tr}\), and \(H_*=\Gamma_2/(g^2\mu_{\rm tr})\). Set \(j=\max\{1,\lceil M/A_g\rceil-1\}\) and \(s=\lceil\max\{0,B_g-M\}\rceil\). The amended definition is
\[
 H_2=\min\{H_*,\lceil g/j\rceil-1+sH_*\}.
\]
If \(M\le A_g\), then \(B_g>A_g\) implies \(s\ge1\), so the expression equals \(H_*\). It bounds rank-two heights by regularity. If \(M>A_g\), then \(j\) is the largest integer strictly below \(M/A_g\) and \(M>j A_g\), even at an integral ratio. In this case the following proof supplies the integer height bound on either admissible I4 choice.

For \(M>A_g\), let \(\Theta\) be any saturated regular rank-two lattice of density at least \(\mu_{\rm tr}\) on at most \(N_\star\) coordinates. Regularity gives \(h(\Theta)\le\Gamma_2/(g^2\mu_{\rm tr})\). We prove the second bound by strengthening the integer-order argument of Amendment I4. Order the coordinates with a largest minor first. By the prefix count proved there, take the nontrivial step orders \(s_1,\ldots,s_t\ge2\) in order. The height and density satisfy
\[
 h=\prod_i s_i,\qquad m(\Theta)\le g^{-2}F,\qquad
 F=\prod_i\frac{\lceil g/s_i\rceil}{g}.
\]
Each factor is at most one. A small order \(s_i\le\sqrt g\) gives a factor at most \((1+g^{-1/2})/s_i\). Suppose for contradiction that \(h\ge g/j\).

If all orders are small, retain their shortest initial list with product at least \(g/j\), possibly empty. The preceding product, when the list is nonempty, is less than \(g/j\le g<2^{254}\); as each factor is at least two, there are at most 255 retained orders. Dropping other factors can only increase \(F\). The retained product then gives \(gF\le j A_g\).

If there are at least two orders above \(\sqrt g\), the factors for any two are at most \(g^{-1/2}+g^{-1}\). Dropping other factors gives \(gF\le(1+g^{-1/2})^2\le j A_g\).

In the remaining case, let \(s_*\) be the unique large order and let \(a=\lceil g/s_*\rceil\). The product \(P\) of the other orders is an integer. From \(s_*P\ge g/j\) we get \(jP\ge g/s_*\). The left side is integral, so \(jP\ge a\), or \(P\ge a/j\). Retain the shortest initial list of small orders with product at least \(a/j\), empty if \(a/j\le1\). Its length is at most 255 by the same reasoning, since \(a\le g\). The product of its density factors is at most \(A_g j/a\). Multiplying by the large-order factor \(a/g\) and dropping all remaining factors gives \(gF\le j A_g\).

In every case \(g^3m(\Theta)\le gF\le jA_g<g^3\mu_{\rm tr}\), a contradiction. Thus \(h<g/j\), so the integer height satisfies \(h\le\lceil g/j\rceil-1\), as claimed. If this integer upper bound is zero then no such rank-two lattice exists.

The ordinary box, lattice, trimming and regularity definitions are unchanged. The index identity and prefix density estimates in I3 and I4 use only the basis and the box. The dense-choice rank-two regularity proof uses its stated density guard and \(\Gamma_2\) inequality. It never assumes the former definition of \(H_2\). The trimming calculation in I4 uses only the box moment bound, rank and I2. The two projected counts in I3 use the actual input lattice height, the covariance and the inequalities on \(\Lambda_d\), with no numerical upper-height parameter. The regularization proofs of I3 and I4 use their respective checked growth conditions and the same prefix, trimming and projected estimates. Those proofs therefore already hold on the amended domain. The only inequalities in the checks whose evaluated values change from this definition are the appropriate rank-two minor and short-vector constraints in I5 and I6. Each use of \(H_2\) in the following full inverse proof is on a saturated regular rank-two lattice of density at least \(\mu_{\rm tr}\), which has just been proved to satisfy the new height bound. The rank-one and other density arguments use the original corresponding conditions.

## Amendment H3

Let
\[
 H_*=\frac{\xi_{\rm tr}}{g^3\mu_{\rm tr}-\xi_{\rm tr}/g},\quad
 A_g=(1+1/\sqrt g)^{255},\quad B_g=(1+1/\sqrt g)^{256},\quad M=g^4\mu_{\rm tr},
\]
and set \(j=\max\{1,\lceil M/A_g\rceil-1\}\) and \(s=\lceil\max\{0,B_g-M\}\rceil\). The amended definition is
\[
 H_3=\min\{H_*,\lceil g/j\rceil-1+s H_*\}.
\]
The protected (I2) ensures that the denominator of \(H_*\) is positive. If \(M\le A_g\), then \(B_g>A_g\) gives \(s\ge1\) and the amended expression equals \(H_*\). If \(M>A_g\), then \(j\) is the largest integer strictly below \(M/A_g\), so \(M>jA_g\), including at integral ratios.

Let \(\Theta\) be a saturated rank-three lattice with maximum fiber density \(m(\Theta)\ge\mu_{\rm tr}\). The prefix count in Amendment I3 gives \(h=\prod_i s_i\), \(m(\Theta)\le g^{-3}F\), and \(F=\prod_i \lceil g/s_i\rceil/g\) on the list of nontrivial step orders \(s_i\ge2\). The expansion bound there already gives \(h\le H_*\). We now show \(h<g/j\) whenever \(M>A_g\).

Assume \(h\ge g/j\). An order \(s_i\le\sqrt g\) has \(\lceil g/s_i\rceil/g\le(1+g^{-1/2})/s_i\). If all orders have this property, keep only the shortest initial list of orders with product at least \(g/j\), taking the empty list when \(g/j\le1\). Its length is at most 255 because each order is at least two and the product preceding the last order is less than \(g/j\le g<2^{254}\) by (I1). The discarded factors in \(F\) are at most one. The resulting bound is \(g F\le jA_g\).

If at least two orders exceed \(\sqrt g\), their two factors in \(F\) are at most \(g^{-1/2}+g^{-1}\) each. Keeping just those factors gives \(gF\le(1+g^{-1/2})^2\le jA_g\). In the remaining case let \(s_*\) be the unique order exceeding \(\sqrt g\), \(a=\lceil g/s_*\rceil\), and \(P\) the product of the other orders. The assumption implies \(jP\ge g/s_*\), hence \(jP\ge a\) because \(jP\) is integral. From the other orders retain the shortest initial list of product at least \(a/j\), taking it empty when \(a/j\le1\). Its length is at most 255 by the same preceding-product bound, since \(a\le g\). Its factors have product at most \(A_gj/a\). Multiplying by the \(a/g\) factor for \(s_*\) and discarding the rest gives \(gF\le jA_g\) also in this case.

All three cases contradict \(M\le g^4m(\Theta)\le gF\le jA_g<M\). Hence \(h\le\lceil g/j\rceil-1\) for \(M>A_g\). Combining with the old continuous bound and the nonnegative term \(sH_*\) gives \(h\le H_3\) on the whole amended domain.

For the rank-three regularity argument of the prefix lemma, the same expansion gives \(m(\Theta)h\le g^{-3}\xi_{\rm tr}(1+h/g)\), which is at most \(g^{-3}\Gamma_3\) by the protected (I4) evaluated at the amended \(H_3\). The integer-box and normal-lattice definitions are independent of the height bound. The prefix rank-one and rank-two estimates use just the exact step index and the ceiling inequality. The trimming moment calculation in I3 uses the sampling distribution and the truncation radius, with no dependence on \(H_3\). The sparse projection count uses each lattice's actual height, and the regularization proof uses the proved rank-three regularity and other inequalities of (I4), which still hold. In the proof of the inverse theorem in Amendment I6, the minor cutoff in (I5) now applies with this upper bound on every regular rank-three lattice under consideration. The terminal Minkowski comparison uses its integer floor and the checked inequality in (I6). Thus the short-multiple and extraction proofs apply at this amended height, without changing the lift, the sampler, or the SIS norm.

## Amendment I6

Replace (I6) by the conjunction
\[
 2\beta<q,\quad H_1\le\beta,\quad
 4H_2q\le3\beta^2,\quad 649\lfloor H_3\rfloor q^2\le250\beta^3.
\]
The inverse proof uses amended (I3), both choices of (I4), and amended H2 and H3. The remaining height definition and conditions (I1), (I2), and (I5) retain their meanings.

### Dependence on the inverse conditions

In `blob:admissibility`, (P3) now requires the inverse-theorem conditions with the displayed (I6). The other admissibility conditions are identical, including (P4). The boxes, fibers, densities, saturation, height, and regularity in `blob:lattices` depend on the box, the basis, the field and the \(\Gamma_d\), with no dependence on \(\beta\). The ellipsoid of `blob:trimming` uses only \(g,R_{\mathrm{tr}}\) and the basis. The following lemmas retain their contracts and arguments.

- In `lem:prefix`, the prefix saturation, indices, and fiber count use the integral basis and \(g\). The estimate for a step of index below \(g\) uses (I1), and the full-choice rank-three height and regularity use (I2) and (I4). They involve no short-vector bound.
- In `lem:trim`, the moment-generating-function bound for the independent uniform entries is applied to a linear image of the box and then Markov's inequality is applied with the threshold \(R_{\mathrm{tr}}^2\). The loss condition used is precisely the exponential inequality in (I2).
- In `lem:sparse`, a trimming ellipsoid is projected along the normal constraints and lattice points in the projection are bounded by its volume and the lattice index. The conversion of the volume estimate to the constants uses (I3). The new (I6) is absent from both estimates and their proofs. The sharper geometric constant from the separate (I3) amendment is proved in that section.
- In `lem:regularize`, the downward induction uses the trimming loss, the prefix lattice inequalities, and the projected density–height bound. Promotion can only reach rank three by the inequality \(g^{-4}<\mu_{\mathrm{tr}}\) from (I5). The growth bounds in (I4) suffice for the final prefix. Neither a bound on a short multiple nor (I6) enters the induction.

For sparsity use I3. For regularization use I3 on the full-rank choice and I4 on the dense choice. The prefix estimates, rank-specific bounds and trimming are proved in I3, I4, H2 and H3. On the dense choice any saturated lattice of rank at least three has density at most \(g^{-3}<\mu_{\rm tr}\). Hence every saturated lattice with density above \(\mu_{\rm tr}\) constructed below has rank at most two. The rank-three steps are used only on the full-rank choice.

### Volume of the terminal coordinate body

For \(d=2,3\) let \(a_1,\ldots,a_M\) be the rows of \(BB_J^{-1}\), where \(J\) is a largest \(d\)-row minor. These include all standard unit vectors. Every \(d\)-row determinant has absolute value at most 1, since it is an original minor divided by the chosen largest minor. Define the compact, centrally symmetric body
\[
 K=\{x\in\mathbb R^d:\ |a_i^\top x|\le1\text{ for every }i\}.
\]
It has the origin in its interior since the list is finite. We prove the respective volume lower bounds needed for the amended terminal norm.

#### Planar bound

Let \(C=\operatorname{conv}\{\pm a_i\}\). This is the polar of \(K\), since the inequalities for the vertices give those for every convex combination, and separation gives the converse. Determinant bilinearity implies \(|\det(a,b)|\le1\) for all \(a,b\in C\). Rotate by \(\pi/2\) using \(J\). Then \(|a\cdot Jb|\le1\) for every \(a\in C\) and \(b\in C\), so \(JC\subseteq K\).

Define \(\|x\|_K=\inf\{s>0:x\in sK\}\). This is a norm because \(K\) is bounded, centrally symmetric, convex and contains the origin in its interior. For the triangle inequality, if \(x\in sK\) and \(y\in tK\), then \((x+y)/(s+t)\) is a convex combination of \(x/s\) and \(y/t\); pass to the infimum. The polygon \(K\) has a counterclockwise boundary with finitely many edges. On each edge with initial point \(p\) and directed edge vector \(v\), choose its outward normal \(a\) scaled so that \(a\cdot p=1\). Such scaling is positive since the origin is interior. As \(a\cdot x\le1\) on \(K\), we have \(a\in C\). The counterclockwise orientation gives \(v=tJa\) for \(t>0\). Hence \(\|v\|_K\le t\), and \(\det(p,v)=t(a\cdot p)=t\). Joining the origin to the polygon's vertices divides it into triangles, so \(2\operatorname{vol}_2 K=\sum_{\rm edges}\det(p,v)\ge\sum_{\rm edges}\|v\|_K\).

To lower bound this last sum, choose any \(x\in\partial K\) and traverse the boundary counterclockwise from \(x\) to \(-x\). The continuous function \(y\mapsto\|y-x\|_K\) goes from zero to two, so some intermediate \(y\) satisfies \(\|y-x\|_K=1\). The radial direction of each boundary point is unique since the origin is interior, so \(y\) is not collinear with \(x\). The six boundary points
\[
 x,\ y,\ y-x,\ -x,\ -y,\ x-y
\]
occur in this cyclic order: the direction of \(y-x\) is strictly between those of \(y\) and \(-x\), as a positive sum of these vectors, and the other half is obtained by negation. The successive chord vectors are \(y-x,-x,-y,x-y,x,y\), each of norm one. Split the boundary path at these six points. Splitting an edge does not change its norm-length by homogeneity on that ray, and the triangle inequality shows the length of each of the six resulting arcs is at least the length of its chord. Thus \(\sum_{\rm edges}\|v\|_K\ge6\), and \(\operatorname{vol}_2 K\ge3\). This proof uses only the finite strip description and the normalized determinants.

#### Three-dimensional bound

Maximize \(\det A\) among positive semidefinite symmetric matrices with \(a_i^\top A a_i\le1\) for every \(i\). The domain is compact: the standard unit constraints bound all diagonal entries and positive semidefiniteness bounds each off-diagonal entry by the geometric mean of its two corresponding diagonal entries. A small positive multiple of the identity is feasible, so a maximizing \(A\) is positive definite. Put \(u_i=A^{1/2}a_i\), and call an index active when \(\|u_i\|_2=1\). The identity lies in the cone generated by \(u_i u_i^\top\) at the active indices. To prove this, the cone is closed since every generator has trace 1, so bounded traces bound the coefficients in any sequence of nonnegative combinations. If \(C_0\) is the nearest cone point to \(I\) in the trace inner product and \(S=I-C_0\), the minimizing property gives \(\langle S,X-C_0\rangle\le0\) for every cone point \(X\). Test \(X=0,2C_0\) to see \(\langle S,C_0\rangle=0\). If \(S\ne0\), then \(\operatorname{tr}S=\|S\|_{\rm F}^2>0\) and \(u_i^\top S u_i\le0\) for all active constraints. For small \(t>0\), \(A^{1/2}(I+tS)A^{1/2}\) remains feasible by those inequalities and the strict slack of all inactive constraints. Its determinant increases because \(\det(I+tS)=1+t\operatorname{tr}S+O(t^2)\), a contradiction.

Write \(I=\sum_i w_i u_i u_i^\top\) with positive weights on active indices. At most six are needed. If more than six are present, the symmetric three-by-three matrices have a nonzero linear dependence. Taking traces shows the dependence coefficients have both signs and sum to zero. Subtract the largest nonnegative multiple of that dependence from the weights that keeps them all nonnegative. At least one becomes zero while the representation persists. Repeating gives at most six. Pad the list with zero weights if necessary. Their sum is 3 by traces. Write \(D_{ijk}=\det(a_i,a_j,a_k)\) for ordered indices of this list; determinants involving padded rows can use any existing row. Applying Cauchy–Binet to the matrix with columns \(\sqrt{w_i}u_i\) gives
\[
 1=\det A\cdot S_3,\qquad S_3=\sum_{i<j<k}w_iw_jw_kD_{ijk}^2.
\]
Each \(|D_{ijk}|\le1\). The degree-three elementary symmetric sum of the weights is at most \(5/2\), attained at six equal weights. To justify smoothing, replacing two weights by their average preserves their sum and increases their product. Terms involving exactly one of the two depend only on their sum and terms involving both have nonnegative coefficients. At a maximum with at least three positive weights an unequal pair is strictly improved, since the coefficient of the product is the sum of the other weights and is positive. With fewer positives the sum is zero. This also gives the corresponding maximal sum on any five weights with prescribed sum.

Consider one pivot \(i\) and any four distinct other indices \(a,b,c,d\). The six minors containing \(i\) and a pair among those four satisfy
\[
 D_{iab}D_{icd}-D_{iac}D_{ibd}+D_{iad}D_{ibc}=0 .
\]
Indeed, after an invertible linear map taking the pivot vector to the first coordinate vector, this is the two-by-four determinant identity obtained by expanding the three products of two-by-two minors of the projections on the last two coordinates. Transforming back multiplies all three products by the same nonzero scalar. If the pivot is zero the identity also holds. The absolute values of the three signed products are in \([0,1]\), and the largest is the sum of the other two unless all are zero. Their squared sum is therefore at most 2. For any pair of numbers \(a',b'\) in \([0,1]\), \((a')^2+(b')^2\le1+(a'b')^2\) by expanding \((1-(a')^2)(1-(b')^2)\ge0\). Consequently each six-minor list has sum of squared minors at most \(3+2=5\), and deficit against six unit squares at least 1. Let \(x=\min_i w_i\), so \(0\le x\le1/2\). Each six-minor list has weighted deficit at least \(x^3\) because each triple weight is at least \(x^3\). There are \(6\binom54=30\) lists, and each triple occurs in \(3\binom32=9\) of them (choose its pivot and two additional indices). Thus the overall weighted deficit is at least \((10/3)x^3\), including if \(x=0\). Holding the smallest weight fixed and smoothing the other five gives
\[
 S_3\le f(x)=10\left(\frac{3-x}{5}\right)^3+
              10x\left(\frac{3-x}{5}\right)^2-\frac{10}{3}x^3
 =\frac{54}{25}+\frac{36}{25}x-\frac{42}{25}x^2-\frac{226}{75}x^3.
\]
On the interval \([0,1/2]\), \(f''(x)\le-84/25\). At \(x=1/4\), \(f(x)=5683/2400\), \(f'(x)=7/200\). Integrating the second-derivative bound along the segment from \(1/4\) gives
\[
 f(x)\le \frac{5683}{2400}+\frac7{200}(x-1/4)-\frac{42}{25}(x-1/4)^2
 \le \frac{5683}{2400}+\frac{(7/200)^2}{4(42/25)}
 <\frac{2369}{1000}.
\]
The middle bound maximizes the quadratic on the whole real line. In particular \(a=\sqrt{\det A}\) satisfies \(a^2\ge1000/2369\).

### A section estimate for the three-dimensional body

Set \(K'=A^{-1/2}K\). It contains the unit ball since \(\|u_i\|_2\le1\) for all rows. Choose an active unit vector \(u=u_i\) and let \(\tilde u_j\) be the projection of \(u_j\) to \(u^\perp\). Use oriented orthonormal coordinates in this plane with unit normal \(u\). Then
\[
 |\det_2(\tilde u_j,\tilde u_k)|=|\det_3(u,u_j,u_k)|\le a ,
 \qquad a=\sqrt{\det A},
\]
by the normalized three-row determinants and the transformation \(A^{1/2}\). The central section of \(K'\) in this plane is described by the inequalities \(|\tilde u_j\cdot x|\le1\). Scaling the row vectors by \(1/\sqrt a\) divides each planar determinant by \(a\), and scales the planar body by \(\sqrt a\). That body is a bounded planar strip intersection with interior. The planar proof above used only these properties, central symmetry, and the determinant bound. Consequently
\[
 \operatorname{area}(K'\cap u^\perp)\ge 3/a .
\]

For completeness, for two compact convex planar sets of positive area the square root of area of their Minkowski combination with weights \(1-t,t\) is at least the same combination of the square roots of their areas. To prove it, first normalize both sets to area one. The vertical slice widths \(f,g\) are positive and continuous in the interiors of their respective first-coordinate intervals. Let \(x_f(s),x_g(s)\) for \(0<s<1\) be the inverse functions of their integrals from the left endpoints. Their derivatives are \(1/f(x_f(s))\) and \(1/g(x_g(s))\). At the interpolated first coordinate \((1-t)x_f(s)+t x_g(s)\), the slice of the combination contains the corresponding combination of the two interval slices. Its length is at least \((1-t)f(x_f(s))+t g(x_g(s))\). After changing variables by the strictly increasing interpolated first coordinate, the area is at least the integral over \(0<s<1\) of
\[
 \big((1-t)f+t g\big)\big((1-t)/f+t/g\big)\ge1 ,
\]
where the inequality follows from \(f/g+g/f\ge2\). The change of variables holds first on compact subintervals of \((0,1)\), and their integrals increase to the stated lower bound. For arbitrary positive areas let their square roots be \(r_1,r_2\). Apply the area-one result to the sets scaled by \(1/r_1,1/r_2\), now with normalized weights proportional to \((1-t)r_1,t r_2\), and scale back by their sum. This proves the claim, including the endpoint weights by equality.

Put \(x=\pi a\) and \(R=\sqrt{3/x}\). If \(x\ge3\), the unit ball already gives \(\operatorname{vol}_3 K\ge4x/3\ge4\). Otherwise \(R>1\). The ball slice at height \(z_0=\sqrt{R^2-1}/R\) in direction \(u\) is a disk of radius \(1/R\). The central section has area at least \(\pi R^2\). For each \(0\le z\le z_0\), convexity of \(K'\) includes in its section at height \(z\) the Minkowski combination of these two sections with weights \(1-z/z_0,z/z_0\). The planar result just proved bounds the area below by
\[
 \pi\big(R-z\sqrt{R^2-1}\big)^2 .
\]
For heights \(z_0\le z\le1\) use the ball section; negative heights have the same areas by symmetry. If \(j=\sqrt{R^2-1}\), the volume gain beyond the ball is at least
\[
 2\pi\int_0^{j/R}[(R-jz)^2-(1-z^2)]\,dz
 =\frac{2\pi j^3}{3R}.
\]
Indeed the first two terms after integration, \((R^2-1)j/R\) and \(-Rj(j/R)^2\), cancel, and the cubic term is \((j^2+1)(j/R)^3/3=j^3/(3R)\). Scaling back by \(A^{1/2}\) gives
\[
 \operatorname{vol}_3 K\ge \frac{4x}{3}+\frac{2(3-x)^{3/2}}{3\sqrt3}.
\]
The right hand side is increasing on \(0\le x\le3\), as its derivative is \(4/3-\sqrt{(3-x)/3}\ge1/3\).

It remains to verify the rational lower volume bound used by the rule. Squaring gives
\[
 \frac{1000}{2369}-\left(\frac{6497}{10000}\right)^2
 =\frac{2119679}{236900000000}>0 .
\]
Also \(\pi>6283/2000\). Indeed \(\pi=16\arctan(1/5)-4\arctan(1/239)\) by the tangent addition formula in the first quadrant: the tangent of \(4\arctan(1/5)\) is \(120/119\). Integrating the alternating geometric series for \(1/(1+s^2)\) gives
\[
 \pi>16\left(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}-\frac1{7\cdot5^7}\right)-\frac4{239}
 =\frac{1231847548}{392109375}>\frac{6283}{2000}.
\]
Thus \(x> x_0=2041/1000\) since \((6283/2000)(6497/10000)-x_0=651/20000000\). With \(c=649/250\) and \(r=8/c-4x_0/3=175391/486750>0\), the exact comparison is
\[
 4(3-x_0)^3-27r^2=\frac{2344329476879}{105300250000000}>0 .
\]
Taking the positive root verifies \(4x_0/3+2(3-x_0)^{3/2}/(3\sqrt3)>8/c\). The case \(x\ge3\) also exceeds \(8/c\). This proves the required rank-three volume estimate with coefficient \(649/250\).

We also use the following elementary lattice-volume implication. For a full lattice \(L\) in \(\mathbb{R}^d\) and a centrally symmetric compact convex body \(K'\) with \(\operatorname{vol}K'\ge 2^d\det L\), there is a nonzero lattice point in \(K'\). For strict inequality, translate the pieces of \(K'/2\) lying in distinct translates of a half-open fundamental parallelepiped for \(L\) back into that parallelepiped. The sum of their volumes exceeds \(\det L\), so two pieces overlap. The two corresponding distinct points of \(K'/2\) differ by a nonzero lattice vector, lying in \(K'\) by convexity and symmetry. For equality apply the strict argument to \((1+1/j)K'\) for each positive integer \(j\); these sets lie in \(2K'\), which contains only finitely many lattice points. A nonzero point occurring infinitely often lies in the closed body \(K'\).

### Amended inverse theorem

For prime \(q\), with the remaining hypotheses in `lem:inverse` and the (I6) above, every nonzero \(v\in\mathbb{F}_q^{N_\star+1}\) with \(v_0=0\) and \(\operatorname{gp}(v^\top)>\theta\) has an integer short multiple \(x\) with \(x_0=0\), \(0<\|x\|_\infty\le\beta\), and \(x\bmod q=a v\) for some \(a\in\mathbb{F}_q^*\).

Remove zero coordinates and order the nonzero coordinates as \(v_1,\dots,v_{N_0}\). For a prefix of length \(i\), let \(p_i\) be its maximum modular fiber density for independent box coordinates uniform on \([2,g+1]\cap\mathbb{Z}\). Each fiber of the longer prefix, conditional on the last coordinate, is a fiber of the shorter prefix. Hence \(p_i\ge p_{i+1}\). The single-coordinate map is injective on the box since \(v_1\neq0\) and \(g+1<q\), so
\[
\theta<p_{N_0}\le p_i\le p_1=1/g.
\]
Inductively we construct a saturated regular lattice \(\Theta\) on the first \(i\) coordinates with rank \(d\in\{1,2,3\}\), \(v_{[i]}\in\bar\Theta\), and \(m(\Theta)\ge p_i-3\varepsilon_{\mathrm{tr}}\). This gives \(m(\Theta)>\mu_{\mathrm{tr}}\) and \(h(\Theta)\le H_d\), using regularity when \(d\le2\) and `lem:prefix` (c) when \(d=3\). For \(i=1\) use \(\mathbb{Z}\). Its height is 1, density is \(1/g\) and \(\Gamma_1\ge1\) follows from (I4) and \(\mu_{\mathrm{tr}}<1/g\).

For the extension step we first choose a basis \(B\) with product of the column infinity norms at most \(h(\Theta),2h(\Theta),9h(\Theta)\) in ranks 1, 2, 3, respectively. Choose a row set \(J\) of a largest minor. Restriction identifies \(\Theta\) with the full lattice \(L_J=B_J\mathbb{Z}^d\) of determinant \(h(\Theta)\). Every lifted basis vector has infinity norm bounded by the \(\ell_1\) norm of its \(J\) coordinates by `lem:lattice-facts` (a).

For successive minima we use the upper bound in Minkowski's second theorem, J. W. S. Cassels, *An Introduction to the Geometry of Numbers*, Chapter VIII, Theorem V, p. 218, [publisher record](https://doi.org/10.1007/978-3-642-62035-5). For a convex symmetric body of volume \(V_F\) and a full lattice \(\Lambda\) of determinant \(d(\Lambda)\), the theorem states for its successive minima \(\lambda_1,\ldots,\lambda_d\) that
\[
  (2^d/d!)\,d(\Lambda)\le \lambda_1\cdots\lambda_d V_F\le 2^d d(\Lambda).
\]
Applying it to the \(\ell_1\) unit ball, a union of \(2^d\) orthant simplices of volume \(1/d!\), gives \(\prod_j\lambda_j\le d!\,h(\Theta)\). Choose independent vectors \(u_1,\ldots,u_d\) with \(\|u_j\|_1\le\lambda_j\). These exist by choosing each \(u_j\) outside the span of the earlier ones from the rank-\(\ge j\) span of points of norm at most \(\lambda_j\). Intersect their first \(j\) real spans with \(L_J\) to get a primitive flag of lattices, of ranks \(j\). The successive quotient is free of rank one since the intersections are saturated. In each quotient choose a generator with sign such that \(u_j\) projects to \(m_j\) times that generator with integer \(m_j\ge1\). If \(m_j=1\), use \(u_j\) as a lift of the generator. Otherwise, any lift is \(u_j/m_j+\sum_{l<j}a_l u_l\) with real \(a_l\). Subtract integer multiples of the \(u_l\) to obtain a lift with \(|a_l|\le1/2\). Its norm is at most \(\lambda_j/2+\sum_{l<j}\lambda_l/2\le j\lambda_j/2\). The rank-one lift has norm at most \(\lambda_1\) in either case. These quotient generators form a basis by induction. Thus the product of the \(\ell_1\) norms is at most \(\lambda_1\cdots\lambda_d\) in ranks one and two and \(3\lambda_1\lambda_2\lambda_3/2\) in rank three. Lifting back via \(J\) proves the stated product bounds for \(B\).

Let \(v_{[i]}=Bc'\bmod q\), and \(c=(c',v_{i+1})\) over \(\mathbb{F}_q\). Take a densest modular fiber of \(v_{[i+1]}\) and trim it by \(\Theta\), obtaining \(F\) of density at least \(p_{i+1}-\varepsilon_{\mathrm{tr}}\), by `lem:trim`. Write \(\Phi(r)=(B^\top r_{[i]},r_{i+1})\). The points \(\Phi(F)\) lie in one coset of the subgroup \(c^\top y=0\bmod q\) of index \(q\) in \(\mathbb{Z}^{d+1}\), since the last entry of \(c\) is nonzero. If their affine dimension were \(d+1\), `lem:sparse` (a) and regularity would give
\[
\Pr[F]\le \Lambda_d\, g^d h(\Theta)m(\Theta)/q \le \Lambda_d\Gamma_d/q<\mu_{\mathrm{tr}},
\]
using (I5). This contradicts \(\Pr[F]>\theta-\varepsilon_{\mathrm{tr}}\). Let \(k'\le d\) be the actual dimension and \(\Delta_*\) the integer matrix whose columns are differences of points of \(\Phi(F)\) from any fixed point. Its rank is \(k'\).

For a point in the trimming ellipsoid, the absolute deviation in coordinate \(j\) from the center is at most \(R_{\mathrm{tr}}\sqrt{(\Sigma_\Theta)_{jj}}\), by Cauchy–Schwarz after applying \(\Sigma_\Theta^{-1/2}\). Thus the corresponding row of \(\Delta_*\) has entries bounded by \(2R_{\mathrm{tr}}(g/\sqrt{12})\sqrt{N_\star}\|B e_j\|_\infty=T_{\mathrm{tr}}\|Be_j\|_\infty\). The last row is bounded by \(g-1<T_{\mathrm{tr}}\). In a minor of order \(k'\), products of row norm factors are bounded by \(\prod_{j=1}^d\|Be_j\|_\infty\) since each basis vector is nonzero and integral. Also \(T_{\mathrm{tr}}\ge1\). Expansion by permutations gives the bound
\[
d! T_{\mathrm{tr}}^d \prod_{j=1}^d\|Be_j\|_\infty
\]
on each such minor. This is at most \(H_1T_{\mathrm{tr}}\), \(4H_2T_{\mathrm{tr}}^2\), or \(54H_3T_{\mathrm{tr}}^3\) according to rank, each below \(q\) by (I5). If \(k'=0\), the matrix is zero and the following lift is immediate. Otherwise `lem:lattice-facts` (c) applies to \(c^\top\Delta_*=0\bmod q\) and gives an integral \(u\equiv c\bmod q\) with \(u^\top\Delta_*=0\). Consequently \(u^\top\Phi(r)\) is constant on \(F\), and \((Bu_{[d]},u_{d+1})\) lies in the saturated normal lattice \(F^\perp\), reducing to \(v_{[i+1]}\). In particular \(F^\perp\) has positive rank. A rank-\(s\) lattice fiber has density at most \(g^{-s}\), since fixing the coordinates outside an invertible row minor leaves at most one assignment to the remaining \(s\) coordinates. Since \(\Pr[F]>\theta-\varepsilon_{\mathrm{tr}}>\mu_{\mathrm{tr}}\) and \(g^{-4}<\mu_{\mathrm{tr}}\), its normal lattice has rank at most three. Its maximum fiber density is at least \(\Pr[F]>\mu_{\mathrm{tr}}+2\varepsilon_{\mathrm{tr}}\). Apply `lem:regularize` to \(F^\perp\) to get a regular saturated containing lattice with density at least \(m(F^\perp)-2\varepsilon_{\mathrm{tr}}\ge p_{i+1}-3\varepsilon_{\mathrm{tr}}\). It contains the lift of \(v_{[i+1]}\). This proves the induction.

For the terminal lattice choose \(J\) as above. Let \(z_0\in\mathbb{Z}^d\) with \(Bz_0\equiv v_{[N_0]}\bmod q\). It is nonzero mod \(q\) because \(v_{[N_0]}\ne0\). The preimage \(Z\subseteq\mathbb{Z}^d\) of the line \(\mathbb{F}_q z_0\) has index \(q^{d-1}\), since reduction of \(\mathbb{Z}^d\) is onto and the line has \(q\) elements out of \(q^d\). Hence \(L=B_J Z\) has determinant \(h(\Theta)q^{d-1}\). Consider the body of feasible first coordinates
\[
K_B=\{u\in\mathbb{R}^d:\|B B_J^{-1}u\|_\infty\le1\}.
\]
The rows indexed by \(J\) are the unit rows. Each \(d\)-row determinant has absolute value at most 1 because it is a minor of \(B\) divided by its largest minor, up to sign. The body is symmetric, closed, convex and bounded. In rank one the unit interval lies in it by the largest-minor bound and has length 2. Since \(h(\Theta)\le H_1\le\beta\), \(\operatorname{vol}(\beta K_B)\ge2\det L\). In rank two the planar bound gives
\[
 \operatorname{vol}_2(\beta K_B)\ge3\beta^2\ge4H_2q\ge4h(\Theta)q=4\det L.
\]
In rank three, \(h(\Theta)\le\lfloor H_3\rfloor\) by Amendment H3 and integrality. Hence
\[
 \operatorname{vol}_3(\beta K_B)\ge (8/(649/250))\,\beta^3
 \ge (8/(649/250))\,(649/250)\lfloor H_3\rfloor q^2
 \ge 8\det L .
\]
The volume implication gives a nonzero \(u=B_J z\) in \(L\cap\beta K_B\) in each rank. Put \(x'=Bz\). It is nonzero because its coordinates in \(J\) are \(u\), and its norm is at most \(\beta\) by the definition of \(K_B\). Modulo \(q\), \(x'\) is a multiple of \(v_{[N_0]}\) since \(z\in Z\). If that multiple were zero, each integer entry of \(x'\) would be divisible by \(q\). As \(\|x'\|_\infty\le\beta<q/2\) this would force \(x'=0\). Extend \(x'\) by zeros in the deleted positions, including coordinate 0, to obtain the required short multiple.

## Amendment Ncmp

For the variable \(u\) used by the bound \(E\), set
\[
N_{\mathrm{cmp}}(u)=\frac{u(u+10)}8 .
\]
The remaining formula for \(E\), the values of \(u=2Q+2\) used by the proof, and the two tests in (P5) are as specified in the protected model. The new count applies to the bad events that can pay a \(\theta\) charge. The other pair and entry terms continue to pay for the full collection of possible coincidences.

### Coupling and bad events

Fix the uniform matrix realization \(M\) for the expressions, and fix the adversary's call budget \(Q\). The run up to the first query at the target label has the same law as the run with a uniform string in place of the masked message up to that query without its answer, by the coupling of the protected symbolic-game block. In the latter run the oracle answers and the uniform string can be chosen independently of the valid encryption coins and the search vector. The symbolic simulation with formal equality, including its label images, can therefore be sampled before evaluating the expressions at those coins. An entry introduced on a guessed operand is a new formal variable of its group. The simulation uses at most three new entries per call, for two operands and one result. Received entries are present at initialization. If a result is already formally equal to an entry, the simulation returns that label rather than inserting a new entry.

Evaluate the symbolic simulation at the independent coins and uniformly independent guess-variable values. Within a group a collision means equality of evaluated values for two formally distinct entries. One can couple the evaluated symbolic and random-mask runs until the first such collision. In the real run conditional on the label images, each unused label in any of the three groups, when guessed, has a uniform exponent among the field values not already assigned in its group, and each evaluated result with a new value receives a uniform unused label. Use the same fresh labels in the symbolic and real simulations for new values. Use the uniform guess-variable value for the real guess if it is new in that group, and redraw from the unused field values if it is already assigned. This has the required uniform unused law and disagrees only at a collision. Inductively, before a collision all assigned labels and their expressions agree between the two simulations, and calls and oracle queries agree because the adversary sees the same transcript. The first call on which a collision occurs is common to both runs, even when the answers at that call differ.

The initial collisions are an \(\mathsf{init}\) mark. Suppose a non-initial collision occurs first, before a target-label query has set a mark. If the collision is good in the protected symbolic-game sense, its two entries lie in the target group and their difference has no guess variable. Its later entry cannot be a guessed operand, because that would introduce a new formal variable absent from the earlier entry. It is a result. The real result takes the earlier label, so the monitor sets a good difference mark. Thus a collision that gives a charged first mark must be a bad event. If a target-label query sets a charged first mark before a collision, the queried label has an entry, since otherwise the mark is \(\mathsf{guess}\). This entry has the target value and its expression is bad by the monitor definition. If the first evaluated-symbolic collision instead triggers a redraw of a guessed operand in the real simulation, that collision already contains the fresh guess variable and is bad. It covers any later charged mark even if the real monitor made no mark at the redraw. Hence a charged first mark is covered by the bad collisions after initialization and the bad key-value events in the symbolic simulation.

For a fixed simulation a collision uses the difference expression \(D\) and \(\chi=0\), and a key-value event uses the entry \(D\) and \(\chi=1\). We bound the probability of a bad event over its evaluation. In either source group, if the difference has no guess variable, the source-group coincidence estimate proved in the algebraic view subsection bounds its probability by \(\varepsilon_f\). If the expression contains a guess variable in any group, there is a nonzero formal coefficient of a guess monomial. Such a coefficient is either a nonzero field constant or a formally nonzero expression in one of the source groups, since products of guesses arise only through a pairing of source-group expressions. In the latter case for every fixed \(r\) it is nonzero on some valid encryption coins by the source-group coincidence estimate and \(\varepsilon_f<1\). Thus after clearing the factor \(\varpi\), the event equation is a nonzero polynomial in coins and guess values for each fixed \(r\). Its total degree is at most \(d_f+1\). The terms without guesses have degree at most \(d_f\) by the degree lemma. A term with one guess multiplying a source-group expression adds one degree to the cleared source expression, and terms with two guess variables and no other exponents have degree at most seven after clearing. All independent sampled field coordinates have support size at least \(q-D\). The polynomial root bound gives probability at most \((d_f+1)/(q-D)\le\varepsilon_f\).

The remaining case is a guess-free target-group difference or key-value expression. For any \(r\) at which \(D\) is not identically \(\chi\kappa\), the probability of coincidence over coins is at most \(\varepsilon_f\) by the view lemma. For an \(r\) at which it is identical, the mark stack is nonzero. For a collision this follows since the two entries were formally distinct, and for a key-value expression it follows from the no-formal-key conclusion of the view lemma. The view lemma also places every such \(r\) in a single fiber of the fixed stack, specified by the stack's fixed vectors \(u_c\). Thus the event in this case is bad only for a light stack, and the probability over \(r\) is at most \(\theta\). The combined bound on the bad event is \(\theta+\varepsilon_f\).

### Counting the light-stack charges

Only the last case uses the \(\theta\) summand. At call \(j\) a collision in this case must have a result as its later entry, since an operand entering as a fresh guessed entry has its own new guess variable. Among earlier target-group entries, the received ones number at most two and results of earlier calls at most \(j-1\). All remaining earlier target-group entries are single guessed variables introduced as operands. For a fixed result expression the part involving guess variables can be exactly one of those variables at most once. Thus the result can have guess-free difference with at most one entry of this last type, even if one or both operands of call \(j\) have just been guessed. Indeed if it had guess-free difference with two distinct such entries, their subtraction would be guess-free by linearity, whereas it is the difference of two distinct formal variables. This gives at most \(j+2\) candidate target-group comparisons at call \(j\). The possible guess-free key-value entries in the target group number at most \(Q+2\) since they must be received elements or results; any fresh guessed entry contains its guessed variable. Therefore the total number of events that can incur a \(\theta\) charge is at most
\[
 \sum_{j=1}^Q(j+2)+Q+2
 = \frac{Q(Q+1)}2+3Q+2
 = \frac{u(u+10)}8-1 .
\]
The full count for all other bad events is bounded by the number of pairs plus the number of entries in a table of at most \(L+3Q\) entries, and hence by \(\binom{L+3u}{2}+L+3u\). The pair count may overcount comparisons between different groups, which only increases the bound. Combining the union bounds establishes the amended charged-mark estimate
\[
 \Pr[\text{charged first mark}]
 \le N_{\mathrm{cmp}}(u)(\theta+\varepsilon_f)
       +\left(\binom{L+3u}{2}+L+3u\right)\varepsilon_f .
\]
This argument holds for every realized \(M\), independent of the form packing.

### Generic ledger and scope of the amendment

The generic ledger has the same implication from (P5). In the amended \(E\), all coefficients as a polynomial in \(u\) are nonnegative and its degree is two. Here \(L\ge1\), \(N_{\mathrm{free}}>0\) by (P2), and \(\binom{L+3u}{2}\) expands with nonnegative constant, linear and quadratic coefficients. The new \(N_{\mathrm{cmp}}\) has nonnegative coefficients. For real \(Q\) on \([0,2^\lambda-1]\), the function \(Q\mapsto E(2Q+2)-(Q+1)/2^\lambda\) is convex because its quadratic coefficient is nonnegative. At the first endpoint it is at most zero by the first P5 test. At the second it is \(E(2^{\lambda+1})-1\), at most zero by adding the P5 tests. By convexity it is at most zero throughout. The threshold side conclusion of the generic ledger becomes \(\theta<2^{1-2\lambda}\) for \(\lambda\ge1\). Indeed putting \(U=2^{\lambda+1}\), we have \(N_{\mathrm{cmp}}(U)-N_{\mathrm{cmp}}(2)=U^2/8+5U/4-3>2^{2\lambda-1}\). Every other term in \(E(U)-E(2)\) is nonnegative, so the second P5 bound implies the stated strict threshold limit.

The changed count enters the admissibility block only through the value of \(E\) in P5. The expression, monitor and symbolic-game blocks are independent of the count: they specify the same formal polynomial expressions, oracle label sampling and classifications of marks and events. The view lemma uses degree, coin ranges, algebraic identities of the factors and polynomial root bounds, all independent of this count. The implication \(\varepsilon_f<1\) used by the comparisons follows as before because \(E(2)\ge24\varepsilon_f\) from its fourth term and (P5) remains in force. The factor-one-half lemma concerns the uniform-mask coupling and the two actual failure probabilities, so its argument has no count or bound \(E\) as a premise. The initial and guessed-label bounds use only the distinct received-expression comparisons and the uniform as-yet-unassigned target label respectively. The reduction lemma uses the private polynomial degree, gradient distribution, rank and short-vector properties, with no \(\theta\)-charge count. Its success probability refers to the same run and the same instance. Thus those results in the background list of the bound block apply with the same statements and arguments. The charged-mark and generic-ledger results are proved above, and extraction is derived in Targets.

The extractability-error corollary follows with its original statement from Targets and the factor-one-half lemma. For allowable budgets, in the combined bit experiment with uniform \(b\), put \(f_i=\Pr[\mathsf{Tgt}\wedge\mathsf{Fail}\mid b=i]\). The probability of both a correct bit and extraction failure is at most \(1/2+(f_0+f_1)/4\). The target-query bound in Targets gives \(f_i\le (Q+1)/2^\lambda+s_i\) for each \(i\). Both reductions run in time bounded by \(t_R=t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)\), including fixed description and advice, so each \(s_i\) is bounded by \(\operatorname{Adv}^{\mathrm{MSIS}}(t_R)\) by its defining maximum. Substitution gives extractability error at most \((Q+1)/2^{\lambda+1}+\operatorname{Adv}^{\mathrm{MSIS}}(t_R)\) at the same extractor time. Outside the stated budgets, the trivial probability upper bound 1 yields error \(1/2\) as in the corollary. This accounts for every result in the background list of the bound block.

## Amendment D

The external system \(S\) and its number \(N\) of Boolean unknowns are fixed. Internally extend an assignment with three auxiliary Boolean coordinates \(\mathsf b_1,\mathsf b_2,\mathsf b_3\), all unconstrained except for their Booleanity. Put \(N_\star=N+3\). The extended assignment vector has \(N_\star+1=N+4\) coordinates including the homogeneous coordinate zero. Every witness of the external system has all eight extended tags, and projecting any extended witness onto coordinates zero through \(N\) gives an external witness. The encoding uses no tag as an extra condition on the external system.

Use \(N_\star+1\) distinct Booleanity points \(d_0,\ldots,d_{N_\star}\), a distinct key point \(\rho\), and the same \(n_{\mathsf c}\) cosets of size \(\nu\) for the external constraints. Hence \(D=N+5+\nu n_{\mathsf c}\). Keep the admissible placement and protected field subgroup condition with this \(D\). At \(d_0\) set \(A=0,B=e_0\). At \(d_i\), \(i>0\), set \(A=e_i-e_0,B=e_i\), including the three new Booleanity points. At \(\rho\) set \(A=e_{\mathsf b_1},B=e_{\mathsf b_2}\) so the key corner of a test matrix is \(W_{\mathsf b_1,\mathsf b_2}\). On the constraint cosets keep the protected evaluations, extending those linear forms by zero in the tag entries. The coordinate polynomials are the unique interpolants of degree below \(D\). Store their sparse point-value descriptions rather than a dense coordinate-by-degree table. Define \(Z_0\) to vanish at all \(d_i\) and \(\rho\), \(Z\) at every evaluation point except \(\rho\), \(Z_*=(X-\rho)Z\), and \(L_\rho=Z/Z(\rho)\). Thus \(Z_*=Z_0Z_{\mathcal K}\), where \(Z_{\mathcal K}=\prod_t(X^\nu-\delta_t^\nu)\) is the monic coset vanishing polynomial.

Here is the QAP criterion under this setup. For a symmetric \(W\), \(P_W=A^\top W B\) takes values \(0\) at \(d_0\), \(W_{ii}-W_{0i}\) at \(d_i\) with \(i>0\), and \(W_{\mathsf b_1,\mathsf b_2}\) at \(\rho\). On each constraint coset \(P_W/Z_0\) is the list of terms in that constraint's quadratic test. Let \(R_W\) be the polynomial of degree below \(\nu n_{\mathsf c}\) interpolating these coset values. The sum of \(X^a\) on \(\delta_t\mathcal G\) is zero unless \(\nu\mid a\), in which case it is \(\nu\delta_t^a\). Among degrees below \(\nu n_{\mathsf c}\), the multiples of \(\nu\) give an invertible Vandermonde matrix in the distinct \(\delta_t^\nu\). Consequently all coset sums vanish if and only if \(R_W\) omits all divisible powers. Under the Booleanity and constraint tests, \(P_W-W_{\mathsf b_1,\mathsf b_2} L_\rho-Z_0 R_W\) vanishes at every evaluation point. It is therefore divisible by \(Z_*\), with quotient degree below \(D-1\) from \(\deg P_W\le2D-2\). Equivalently \(P_W-Z_0R_W\) is divisible by \(Z\) with quotient degree below \(D\). Conversely, either such identity with an allowed \(R\) implies the Booleanity values and the coset sum tests by evaluation, and \(R\) is the unique interpolated remainder. In the key identity, evaluation at \(\rho\) gives exactly the specified corner \(W_{\mathsf b_1,\mathsf b_2}\). For a witness vector \(v\), these identities apply to \(vv^\top\), with \(P_v=A_v B_v\) and key corner \(\mathsf b_1\mathsf b_2\).

The new key evaluation still has \(A(\rho)=e_{\mathsf b_1}\), which together with \(A(d_i)=e_i-e_0\) for \(i>0\) spans all form coordinates: the differences span the hyperplane of coordinate sum zero and \(e_{\mathsf b_1}\) has coordinate sum one. The vectors \(B(d_i)=e_i\) are still a basis. These properties, the QAP criterion and the updated \(D\) are the only changes in the generic comparison and coincidence arguments, explicitly used in C7. The point descriptions consist of the nonzero input terms and \(O(D)\) point data. For evaluation of all coordinate polynomials at a scalar off the point set, tabulate the \(D\) Lagrange weights there and accumulate the listed nonzero coordinate entries times their weights. For a witness, accumulate the point values of the two scalar witness polynomials and interpolate only those two polynomials, not the coordinate table. The same subgroup interpolation and vanishing-polynomial algorithms therefore give \(O(|S|+D\log D+\log q)\) setup and the claimed scalar polynomial work with these point sets. The three extra Booleanity evaluations add only a constant number of nonzero coefficients. The score still uses the fixed original nonzero-coefficient charge.

## Amendment ell

Set \(\ell=\lceil N/d_R\rceil+3\). Put ordinary coordinates \(1,\ldots,N\) into the first \(\lceil N/d_R\rceil\) ring columns in the original order, padding with zeros. Put \(\mathsf b_1,\mathsf b_2,\mathsf b_3\) into degree-zero coefficient positions of the three separate last ring columns, with their other coefficients zero. The homogeneous coordinate uses column zero as before. All coordinates are represented once and all introduced extra coefficients are zero. The random matrix has these \(\ell\) nonconstant columns and the independent zeroth column. Use its row as in C5, with one oracle sample per entry and the protected charge \(k(\ell+1)d_R\).

Only the placement map and column count change. It is an injective coordinate padding map, preserves the integer coefficient infinity norm, and commutes with scalar reduction and field scaling. Comparing the coefficient list of the form map gives \(v_0=0\) and \(A\hat v=0\) for an actual form-kernel vector \(v\), where \(A\) is the nonconstant matrix. Thus the short multiple of \(v\) packs to a nonzero solution of the same radius to the precise uniform Module-SIS instance whose unrolled dimensions are \(kd_R,\ell d_R\). For a sample of the seed matrix, its three last entries vary independently and each is a full uniform ring element. For a fixed external witness and any two distinct tag vectors, their seeded form coefficient lists excluding slot zero are independent uniform field vectors: condition on the ordinary columns and all tag columns but one on which the two tag vectors differ. As the retained tag column and the independent column zero vary, their two contributions to those two lists have the invertible scalar matrix with rows \((1,t)\) and \((1,t')\), where \(t\ne t'\). In the split case \(k=1\), all \(d_R=n-1\) nonconstant slots are precisely these uniform coefficients. This proves the distribution used in the correctness estimate. Uniform programming of the nonconstant columns gives the same seed-oracle law and cost per oracle query in the reduction.

## Amendment Bsearch

Use the independent box sampler on \(N_\star=N+3\) coordinates and one extra independent box value \(r_\diamond\), all uniform on \(\{2,\ldots,g+1\}\). Set
\[
 r_0=A_0+r_\diamond-\left\lfloor{\tfrac12\sum_{i=1}^{N_\star}r_i}\right\rfloor,\qquad
 A_0=\left\lceil N_\star(g+1)/2\right\rceil .
\]
Given the box coordinates, the zeroth coordinate is uniform on a translate of \(g\) integers, distinct modulo \(q\). The public center for a Boolean vector \(v\) with \(v_0=1\) is
\[
 c_v=\left\lfloor A_0+\frac{g+3}{2}\bigl(1+\operatorname{wt}(v)-N_\star/2\bigr)\right\rfloor .
\]
If \(X_i=r_i-(g+3)/2\), and \(X_\diamond=r_\diamond-(g+3)/2\), then \(r(v)-c_v=X_\diamond+\sum_i(v_i-1/2)X_i+E\), where the two rounding terms in \(E\) have absolute sum at most \(3/2\). The independent centered sum has variance \((g^2-1)(N_\star+4)/48\). Thus its full RMS is at most \(g\sqrt{(N+7)/48}+3/2\) by the triangle inequality in quadratic mean. Each \(|X_i|\le(g-1)/2\); the deterministic bound including rounding is at most \(B=(N+4)(g+1)\). A centered difference of two tag coordinates or a single centered tag coordinate also lies in this range. This is the definition of \(B_{\rm search}\). The protected check \(2B+1<q\) gives unique valid bounded representatives for all the searches in the amended correctness algorithm.

The guessing probability of a rank-\(d\) stack is still at most \(g^{-d}\). For any prescribed joint fiber, pick a nonsingular \(d\)-column pivot minor of a basis of the row space. If the zeroth column is nonzero, it can be extended to a pivot basis by linear independence of the columns. Fix the remaining nonpivot box coordinates; any solution fixes the pivot box coordinates and the zeroth coordinate uniquely by the invertible linear system. The regular pivot box draws therefore have probability at most \(g^{-(d-1)}\) of meeting their fixed values, and conditional on all box coordinates \(r_0\) has probability at most \(1/g\) of the required value. If the zeroth column is zero, no condition involves \(r_0\), so fixing the other box coordinates directly bounds the pivot solution by \(g^{-d}\). These probabilities hold for every fixed fiber and give the claimed bound. For a kernel vector the zeroth coefficient is zero, so its scalar guessing probability uses precisely the independent box coordinates, now on at most \(N_\star\) positions. The inverse and regularization proofs apply in that dimension with the factors of I3 and \(T_{\rm tr}\) stated next. All heavy-stack and generic ledger arguments therefore use the same guessing-probability implications. The actual arithmetic of the search is supplied in Amendment search_spread.

## Amendment T_tr

Use \(T_{\rm tr}=R_{\rm tr}g\sqrt{(N+3)/3}\). The trimming radius and covariance proof in I3 is used on the independent box of dimension at most \(N_\star\). Each projected feature-row deviation from its center is at most \(R_{\rm tr}(g/\sqrt{12})\sqrt{N_\star}\) times the corresponding basis-vector infinity norm, by the Euclidean Cauchy--Schwarz bound on that row's coefficient norm. Taking differences doubles the bound and gives precisely this new \(T_{\rm tr}\). The minor and prefix-lift argument of I6 uses the checked inequalities in I5 with this value. The projected counting constants in I3 use \(N_\star\) for the same reason. The definitions of regularity, fiber densities and their trimming loss use only the width, coefficient lattice and the radius and have the same arguments. Thus the amended radius supplies the lattice-facts hypothesis and norm proof in the new sampler dimension.

## Amendment C6

Require \(n\ge10\) even, \(n\mid q-1\), split \(\mathrm{ring\_mode}=1\), \(2n\le D\), and \(\Delta\ge n+3\). The split mode of C5 has \(k=1\) and the form placement of Amendment n gives \(n=d_R+1\). Use precisely this one-variable field in the grid of Amendment C7. The additional requirement \(n\ge10\) supplies the two independent coefficient pairs used in the correctness proof. The chunk alignment is supplied by P1.

Take \(F_0=\mathbb F_q\) and \(P_H=H\), so only the basis digit zero occurs. Use the relative modulus \(P_T(T)=T^n-d_*\) with \(d_*\) a public primitive scalar. For a nonzero root \(t\) of this binomial, its multiplicative order \(m\) satisfies \(m/\gcd(m,n)=q-1\). Each prime divisor of \(n\) divides \(q-1\), so the valuation of \(m\) there is the sum of its valuations in \(n\) and \(q-1\). The other valuations are those of \(q-1\). Hence \(m=n(q-1)\). For \(p\mid n\), write \(q=1+a\) with \(p\mid a\). For odd \(p\), in \((1+a)^p-1\) the first term \(pa\) has strictly smaller valuation than every later term, by the binomial coefficient divisibilities and \(p>2\). At \(p=2\) this also holds because \(4\mid a\). Taking a positive power prime to \(p\) preserves the valuation by factoring the difference and reducing the geometric sum modulo \(p\). Iterating gives \(v_p(q^j-1)=v_p(q-1)+v_p(j)\). Thus the Frobenius orbit has size \(n\), and the minimal polynomial of \(t\) is \(P_T\). At \(j=n/2\) we have \(m/2\mid q^j-1\) but \(m\nmid q^j-1\). The ratio \(t^{q^j}/t\) is therefore the nontrivial square root of one, which is \(-1\). This gives the half-turn sign and the even support of \(V\), and the three conjugate projections still have their original field identities.

Since \(q\equiv1\pmod n\), the representative of the \(j\)-th Frobenius image of \(T^s\) for \(0\le s<n\) is the scalar \(d_*^{s(q^j-1)/n}\) times \(T^s\). The coefficient can be computed using the residue of \(q^j\) modulo \(n(q-1)\). The power for \(s=1\) takes \(O(\log q)\) field operations and the remaining table uses successive products in \(O(n)\) operations. The evaluated form multipliers use the same coefficient slots of Amendment n and the same transposed ring evaluation in Amendment C5. The product, weight, mask, view and classification computations use these one-variable representatives as detailed in C7. No auxiliary-variable evaluation is needed.

## Amendment C7

Require \(\mathrm{base\_degree}=\mathrm{base\_left}=\mathrm{base\_right}=\mathrm{scalar\_rel}=1\), \(K_1,K_2\ge1\), and \(2K_1K_2=n\). This is the one-variable grid. Write \(e=A_H=B_H=1\) and \(h=n\) when using field-degree notation. There are \(A_c=3K_1K_2=3n/2\) cells, indexed by a left leg \(a\) with \(0\le a<K_1\) and a right leg \((b,\mathrm X)\), \(0\le b<K_2\), \(\mathrm X\in\{\mathrm E,\mathrm O,\mathrm V\}\). Set \(k_{\mathrm{leg}}=2K_1b+\mathbf1_{\mathrm X=\mathrm O}\) and \(k_c=2a+k_{\mathrm{leg}}\). For E and O the cell weight is the coefficient of \(T^{k_c}\) in \(U=z(w)\sigma^{n/2-1}(z(w))\); for V use \(V=z(w)\sigma^{n/2}(z(w))\). The half-turn fixes \(V\) so only even powers occur there. Euclidean division of the half-exponent by \(K_1\) yields \(a,b\), covering each weight slot exactly once. The key cell is \(a=b=0,\mathrm X=\mathrm E\), with weight the constant coefficient of \(U\).

### Factor masks and publication

Use the original independent scalar coins and centered sampler in the internal dimension. The evaluation coin \(\upsilon\) is uniform nonzero, the scalars \(\pi,s_{\mathrm E},s_{\mathrm O},s_{\mathrm V},\zeta_0,\zeta_1,\zeta'',\eta_1,\eta_2,\eta_3,\Omega_{22},\alpha\) are independent uniform nonzero, \(\Omega_{12}\) and the coordinates \(y_i\) are independent uniform scalars, and \(\tau\) is uniform off the evaluation points. Sample \(\varepsilon\) uniformly from the field excluding \(0,-1\). Let \(F_x(T)\) be the reduced representative of \(\sigma^{n/2+1}(T^x)\), a scalar multiple of \(T^x\) by C6. Write \(z_-,z_\circ,z_+\) for the reduced vectors of linear form coefficients at Frobenius powers \(n/2-1,n/2,n/2+1\), respectively, evaluating at \(\upsilon\) when used as scalars. Set
\[
 \pi_a=\pi(\upsilon^{2a}+\varepsilon F_{2a}(\upsilon)),\qquad
 s_{\rm leg}=s_{\mathrm X}\upsilon^{k_{\rm leg}},\qquad
 \gamma_c=\pi_a s_{\rm leg},\qquad
 \kappa=\gamma_{\rm key}L_\rho(\tau).
\]
Here \(\pi_0=\pi(1+\varepsilon)\ne0\), hence \(\kappa\ne0\) on valid coins. On E/O use the right mask
\[
 \vartheta_{\rm leg}
 =\upsilon^{k_{\rm leg}}(\eta_1 z_\circ+\eta_2 z_+)
   -\varepsilon^{-1}F_{k_{\rm leg}}(\upsilon)(\eta_2 z_-+\eta_3 z_\circ),
\]
and on V use \(\upsilon^{k_{\rm leg}}(\eta_3 z_+-\eta_1 z_-)\). For every input coordinate \(i\) including tags, use the left row \(\pi_a(y_i,A_i(\tau))\) and the right column \((s_{\rm leg}(r_i+A_i(\tau))+\vartheta_{{\rm leg},i},\,s_{\rm leg}(B_i(\tau)-y_i))^\top\). Multiply each left row on the right by the hidden-basis matrix with rows \((1,\Omega_{12})\) and \((0,\Omega_{22})\), and each right column on the left by its inverse. Publish the resulting coordinate arrays in G1 and G2, respectively, the G2 search bases \([s_{\rm leg}]_2\), and the single G1 column \([\zeta'' y_i]_1\). There is one right sector and there are no alpha-scaled source-group inputs. Keep the public target-group element \([\alpha\kappa]_T\), with independent \(\alpha\), and the seed and masked message. This slot preserves the protected overhead count. The decryption algorithm does not require this target-group input.

### Honest cancellation and the three field ties

For a stack form \(W_U,W_V\) by summing cell matrices times \(T^{k_c}\) in their weight families. Put \(\widetilde W_U^+=\sum_{c\in C_U}W_c F_{2a}F_{k_{\rm leg}}\), whose image in the form field is \(\sigma^{n/2+1}(W_U)\). At degree zero in \(\varepsilon\) the three coefficients of the mask contribution, after taking out \(\pi\) and the indicated independent \(\eta\), are
\[
 t_1=W_Uz_\circ-W_Vz_-,\qquad
 t_2=W_Uz_+-\widetilde W_U^+z_-,\qquad
 t_3=W_Vz_+-\widetilde W_U^+z_\circ .
\]
Indeed the negative grade in the right E/O mask contributes degree zero exactly when multiplied by the twisted part of \(\pi_a\); the ordinary products supply the remaining terms. With the honest weights and the form vectors contracted against \(w\), each \(t_i\) vanishes in the field: \(U z_\circ=V z_-\), \(U z_+=\sigma^{n/2+1}(U)z_-\), and \(V z_+=\sigma^{n/2+1}(U)z_\circ\). Their ordinary polynomial degrees are at most \(2n-2\) because conjugating a monomial preserves its slot. Thus monic division by \(P_T=T^n-d_*\) has no remainder and quotient degree at most \(n-2\). Publish the G2 bases with exponents \((\pi\eta_i/\zeta'')P_T(\upsilon)\upsilon^a\), \(0\le a<n-1\), for the three quotients. The positive grades indexed by \(i=1,2,3\) have support lengths \(2n-1,2n-1,2n-2\), since the \(i=3\) positive grade uses only V with exponent at most \(n-2\). The negative grades indexed by \(i=2,3\) each have length \(2n-1\). Publish their ordinary monomial powers under the exponents \(\pi\eta_i\varepsilon^{\pm1}\upsilon^a/\zeta''\), with the respective lengths. This gives \(C_{\rm mask}=13n-9\) slots. The honest values cancel by one G2 MSM using these bases paired with the witness sum of the Y column. All weighted leg products before multiplying by a form are single monomials, so their assembly is linear in the grid size. Polynomial multiplication and the binomial division use \(O(n\log n)\) scalar operations by C3 and \(2n\le D\).

In a formal identity, the Laurent comparison below isolates the same grade-zero polynomials for the actual stack up to multiples of \(P_T\). Their reduction gives all three stated field ties. The right-leg type \(s_{\mathrm X}\) and the ordinary exponent \(k_c\) distinguish every cell in the generic comparison. The proof of the original rank-three classification using these ties follows. The new QAP point at \(\rho\) changes only the corner used by the view and does not change the Booleanity or constraint tests used by that classification.

### Efficiency and asymptotic choices

The complete publication and combination of correction bases, weighted factors and searches are stated in Amendments n1, n2 and the operation-count amendments. With the specified group representation sizes and the exact finite counts they give the amended objectives. No oracle is called more often than one seed query per matrix entry and at most one key query in either algorithm. The eight internal tag variants reuse the same seed and field matrix; only the indicated seven vectors are needed in decryption. Each form evaluation and coefficient-ring adjoint has the same \(O(k(\ell+1)d_R\log(2d_R))\) cost as C5. All mask and field calculations use \(O(n\log n)\) operations per variant, after public field setup. The QAP and weight work is repeated at most a fixed constant number of times and uses \(O(D\log D+|S|)\) operations beyond ring and mask work, as established in n1. The final search is three bounded signed searches as detailed in its amendment.

For the asymptotic cost implication choose powers of two \(K_1,K_2\) of order \(\lambda\) with \(n=2K_1K_2\le N/8\) when \(N\ge\lambda^2\), and use \(k=1,d_R=n-1\) in split mode. Take the subgroup and interval premises supplying \(n\mid q-1\), the powers of two up to the bound in C3, and the supported range and generic ledger choices of I4 and P5. Use \(\Delta=\nu\lfloor D/\nu\rfloor\ge D/2\), so \(\Delta\ge n+3\) for sufficiently large instances, and \(J=\lceil((D-1)+\nu n_{\mathsf c})/\Delta\rceil\le4\), \(J'=1\). For linear-size systems with \(\nu\le2F_{\max}\), \(D=O(N)\) and \(n=\Theta(\lambda^2)\). The three extra coordinates and the three ring entries for tags per row do not change those orders. Then the source arrays contain \(O(\lambda N)\) field elements with bounded group representation degrees. In encryption each requested fixed-base multiple uses \(O(\lambda/\log\lambda)\) group additions by windows of width \(\lfloor\log_2\lambda\rfloor\): precompute all multiples in each of \(O(\lambda/\log\lambda)\) windows and advance the base by the window width. The tables take \(O(\lambda^2/\log\lambda)\) additions and the \(O(\lambda N)\) requested multiplications take \(O(\lambda^2 N/\log\lambda)\) field operations. In decryption the proved counts for a constant number of variants give \(O(\lambda N)\) group additions, \(O(N)\) MSM points and \(O(\lambda)\) pairings and other scalar multiplications. The original cost bounds for these group operations give \(O(\lambda N\log\lambda)\) work outside the searches, including the polynomial and ring operations. The centered search uses \(O(\sqrt{g}\,N^{1/4})\) expected operations by its explicit bound below, which is \(O(2^{\lambda/4}N^{1/4})\) under the admitted growth choices of I4. These are the desired asymptotic costs for the extended internal layout at the original external \(N\).

### Algebraic and reduction interfaces

In `lem:moore`, the field has degree \(n\) and \(z\) plays no role in the statement. To derive the property at the amended degree, if a combination of \(d\) successive Frobenius columns is zero then a polynomial \(\sum_{j=0}^{d-1}a_j X^{q^j}\) vanishes at the entries of \(\sigma^s(h)\). Its roots are closed under \(\mathbb{F}_q\)-linear combinations, and the independent entries give \(q^d\) distinct roots. If any coefficient is nonzero, its degree is at most \(q^{d-1}\), a contradiction. This proof uses only the field and its Frobenius.

Here is the full classification argument for the actual field ties of Amendment C7 with the specified \(z\). Let \(W_c\) be symmetric, pass the Booleanity tests, and satisfy the original three ties, with row space \(\mathcal V\) of dimension \(d\le3\) containing no kernel vector. The zero-dimensional case has zero stack. Let the columns of \(U_*\) over \(\mathbb F_q\) be a basis of \(\mathcal V\), with rows \(u_i^\top\). These rows span \(\mathbb F_q^d\). For \(s\) in \(\mathcal I_*=\{n/2-1,n/2,n/2+1\}\), put \(h_s=U_*^\top\sigma^s(z)\), and put \(h_0=U_*^\top z\). Injectivity of \(z\) on \(\mathcal V\) means the entries of \(h_0\) are independent over \(\mathbb F_q\). In particular \(d\le n\), and the Moore property proved above gives that the three \(h_s\) span over \(\mathbb F_{q^n}\). Write \(W_s\) for \(W_U,W_V,\sigma^{n/2+1}(W_U)\) in the indicated order. Each \(W_s\) has its rows and columns in the extension of \(\mathcal V\), so \(W_s=U_* X_s U_*^\top\) for a unique symmetric \(X_s\). Indeed a left inverse \(L_*\) of \(U_*\) exists, and \(X_s=L_*W_sL_*^\top\); projections back to \(\mathcal V\) act identically on the columns and rows. The ties give \(X_s h_{s'}=X_{s'}h_s\). If \(\sum_s a_sh_s=0\), then \((\sum_s a_sX_s)h_{s'}=0\) for every \(s'\), and spanning gives \(\sum_s a_sX_s=0\). Thus there is a linear map \(X\) with \(X(h_s)=X_s\). The trilinear form \(C(h,u,v)=u^\top X(h)v\) is symmetric in the last two slots and in the first and last slots by the ties, initially on spanning \(h_s\) and then on all vectors by linearity. It is therefore fully symmetric. Each Booleanity test gives \(C(h,u_i,u_i-u_0)=0\) on the spanning \(h_s\), hence on all \(h\). The identities \(X_s=\sigma^s(X_{n-s})\) for \(s=n/2-1,n/2\) follow from the relation between the first and third matrices and because \(W_V\) has even \(T\)-degrees and \(\sigma^{n/2}\) fixes the scalar coefficients, as \(U_*\) and \(L_*\) have field entries fixed by \(\sigma\).

First suppose \(u_0\ne0\). Extend \(l_0=u_0\) to a basis \(l_0,\ldots,l_{d-1}\) chosen from the rows. For each \(\delta\in\{0,1\}^{d-1}\), let \(p_\delta\) satisfy \(l_0^\top p_\delta=1\), \(l_j^\top p_\delta=\delta_j\) for \(j>0\), and set \(w_\delta=U_*p_\delta\). Symmetry lets any repeated positive index in \(C(l_i,l_j,l_k)\) be reduced via the test replacing one occurrence by \(0\). Hence those values depend only on the set of positive indices present. Conversely the cube of the linear functional \(p_\delta\) takes the value \(\prod_{i\in A}\delta_i\) for this set \(A\), and all sets occur since \(d-1\le2\). The matrix of these values indexed by \(A,\delta\) is invertible: indexing \(\delta\) by its support gives the subset-incidence matrix, triangular with diagonal 1 in any inclusion-compatible ordering. Therefore
\[
 X(h)=\sum_\delta c_\delta(h^\top p_\delta)p_\delta p_\delta^\top
\]
for coefficients in the extension field. The squares \(p_\delta p_\delta^\top\) are independent by the same evaluation matrix, now on pairs of basis vectors since \(d-1\le2\). Write \(z_\delta=z(w_\delta)=h_0^\top p_\delta\ne0\). Comparing coefficients of the squares in \(X_s=\sigma^s(X_{n-s})\) gives \(c_\delta\sigma^s(z_\delta)=\sigma^s(c_\delta)z_\delta\) for the two consecutive \(s\). Hence \(c_\delta/z_\delta\) is fixed by \(\sigma\) and belongs to \(\mathbb F_q\), as the fixed points of \(x\mapsto x^q\) are exactly this field. Write it as \(\chi_\delta\). Returning from the matrix restriction gives \(W_s=\sum_\delta\chi_\delta z_\delta\sigma^s(z_\delta)w_\delta w_\delta^\top\). In particular the first two polynomial representatives give the stack \(\sum_\delta\chi_\delta\mathbf H(w_\delta)\).

Let \(f\) be any field-linear test that vanishes on the cells. It vanishes on the \(W_s\). Put \(Q_*=\sum_\delta\chi_\delta f(w_\delta w_\delta^\top)p_\delta p_\delta^\top\), a matrix over \(\mathbb F_q\). The vanishing gives \(h_0^\top Q_* h_s=0\) for all three \(s\), hence \(h_0^\top Q_*=0\). Independence of the entries of \(h_0\) over \(\mathbb F_q\) implies \(Q_*=0\), so independence of the squares implies \(\chi_\delta f(w_\delta w_\delta^\top)=0\) for every \(\delta\). Apply this to all Booleanity tests to deduce that any nonzero coefficient is on a Boolean assignment. If every external constraint test passes, apply the same argument to them to see that each supported assignment is a witness. In any representation by honest stacks of Boolean assignments in \(\mathcal V\), the assignments equal some \(w_\delta\) because their evaluations on the chosen basis fix their \(p_\delta\). Hence the same test argument applies to any such representation.

If \(u_0=0\), take any basis \(l_1,\ldots,l_d\) from the other rows. Booleanity implies \(C(h,l_i,l_i)=0\), so by symmetry every coordinate of the trilinear form with a repeated index vanishes. This gives zero if \(d<3\). For \(d=3\) its only possible value on distinct indices is a shared scalar \(c\). Evaluating \(X_s=\sigma^s(X_{n-s})\) on pairs of different basis vectors gives \(c\, h_s=\sigma^s(c)h_0\) in the basis \(l_1,l_2,l_3\), since \(h_s\) is obtained from \(h_0\) by Frobenius and the basis is over \(\mathbb F_q\). If \(c\ne0\), the first two consecutive vectors \(h_s\) would both be proportional to \(h_0\), impossible by the Moore independence of the three vectors in dimension three. So again \(X=0\), and the stack vanishes. This proves the classification clauses, including that a nonzero usable stack in the stated case has a witness in its row space.

For `lem:heavy`, its rank and inverse-theorem arguments use the sampler and \(v_0=0\), the latter from the kernel identity. For part (c), an integer short multiple \(x\) of \(v\) has \(x_0=0\) because \(v_0=0\) and \(|x_0|<q\). Coordinate packing commutes with reduction and with field scaling. The matrix \(A\) therefore annihilates \(\hat x\bmod q\) by the kernel identity. The representation of \(\hat x\) includes every regular and tag coordinate once by Amendment ell and pads only with zeros, so \(0<\|\hat x\|_\infty=\|x\|_\infty\le\beta\). The MSIS challenge, the infinity norm and the bound being costed are those of the model.

### Degree, view and recovery gradients

Fix the seeded matrix and hence the form coefficients. For source exponents \(a\) in G1 and \(b\) in G2 include their generators. A guess-free target expression is
\[
 \mathsf E=\sum_{a,b}D_{ab}\,a b+D_K\alpha\kappa .
\]
The coefficients are fixed scalars. No source exponent uses \(\alpha\). With \(\varpi=\Omega_{22}\zeta_0\zeta_1\zeta''\varepsilon\) every product clears denominators, since G1 has none and the G2 exponents only use the displayed inverses to the first power. A left scale has degree at most \(n\) and the unscaled G1 factors have degree at most \(D\); the sparse and shifted G1 powers end at degree at most \(D\) including their scale. The other powers have degree at most \(\Delta\le D\) and the Y exponent has degree two. All G1 exponents thus fit \(d_1=D+n+2\). The left and right monomial exponents in a cell sum to \(k_c\le n-1\) and conjugation preserves the left exponent. Therefore \(\gamma_c\) has total degree at most \(n+2\), with the key scale of degree three.

The cleared sparse correction bases have degree at most \(D+n+6\). For non-sparse ones the polynomial part has degree at most \(2D-2\) from P1, and the cell scale and remaining clearing factors give at most \(2D+n+4\). The first and second right coordinates before the masks have degree at most \(D+n+6\) after clearing, by \(k_{\rm leg}\le n-1\), the degree below \(D\) of the QAP polynomials and the linear hidden-basis inverse. A right mask is one leg power of degree at most \(n-1\) times a form of degree at most \(n-1\), with one \(\eta\) and an optional inverse \(\varepsilon\). It has cleared degree at most \(2n+5\), as do the cancellation bases including the one mask scale, \(\pi\) and its grade. Search bases have cleared degree at most \(n+5\). Since \(2n\le D\), all G2 exponents after clearing fit \(d_2=2D+n+6\). The cleared key terms fit \(D+8\). Hence the total degree bound before adding a guessed-operand factor is at most \(d_1+d_2=3D+2n+8\le d_f=3D+2n+2K_1+7\). The extra factor of degree one and each separate bound fit \((q-D)\varepsilon_f\) by its protected formula. The search coordinates enter only linearly, within the same degree bounds.

For any fixed \(r\), the valid scalar coin sets are independent with sizes at least \(q-D\), including the two exclusions on \(\varepsilon\) and the \(D\) exclusions on \(\tau\). The clearing factor is nonzero there. The product-set bound proved in Targets shows that an identity holding on all valid coins is a polynomial identity after clearing, because \(d_f<q-D\) by P5 and \(\varepsilon_f=(d_f+60)/(q-D)\). A nonidentity has coincidence probability at most \(d_f/(q-D)\le\varepsilon_f\). At an identity \(\mathsf E=\chi\kappa\) the coefficient of \(\alpha\) gives \(D_K=0\), since \(\kappa\) is a nonzero polynomial. All stack comparisons henceforth use only the plain factor sector.

Write the two transformed left exponents as \(F_1^{a,i}=\pi_a y_i\) and \(F_2^{a,i}=\pi_a(\Omega_{12}y_i+\Omega_{22}A_i)\). The right exponents are
\[
 H_1^{\mathrm{leg},j}=\ell_{\mathrm{leg},j}
       -(\Omega_{12}/\Omega_{22})s_{\rm leg}(B_j-y_j),\qquad
 H_2^{\mathrm{leg},j}=s_{\rm leg}(B_j-y_j)/\Omega_{22},
\]
where \(\ell_{\mathrm{leg},j}=s_{\rm leg}(r_j+A_j)+\vartheta_{\mathrm{leg},j}\) is independent of the hidden basis. No other G2 input contains a hidden-basis variable. For any G1 input \(a\) denote its evaluation at \(\Omega_{22}=0\) by \(\widetilde a\); for \(F_2^{a,i}\) this is \(\Omega_{12}F_1^{a,i}\). Take the part of the Laurent identity with \(\Omega_{22}^{-1}\) and positive degree in \(\Omega_{12}\). Cancel its common factor \(-\Omega_{12}/\Omega_{22}\). The resulting identity is
\[
 \sum_{a,\mathrm{leg},j}\delta_{a,\mathrm{leg},j}\,\widetilde a\,s_{\rm leg}(B_j-y_j)=0,
\]
where \(\delta_{a,\mathrm{leg},j}\) is the coefficient of the pair with \(H_1^{\mathrm{leg},j}\), subtracting the matched coefficient of \(F_2^{a,i},H_2^{\mathrm{leg},j}\) if its G1 input is \(F_1^{a,i}\). This follows because only a second left coordinate produces a positive \(\Omega_{12}\)-degree when paired with \(H_2\). Differentiate with respect to \(y_{j_0}\) and then set \(y=B(\tau)\). Terms from differentiating \(\widetilde a\) vanish and the result is the zero sum of \(\delta_{a,\mathrm{leg},j_0}\,s_{\rm leg}\widetilde a|_{y=B}\).

The possible left-input types in that last sum are \(1,\zeta_0\tau^v,\zeta_1\tau^v,\zeta''B_i,\pi_a B_i,\Omega_{12}\pi_a B_i\), separated by degrees in \(\zeta_0,\zeta_1,\zeta'',\pi,\Omega_{12}\). In the first four types \(s_{\rm leg}=s_{\mathrm X}\upsilon^{k_{\rm leg}}\) distinguishes the legs in each kind. In a given power list the powers of \(\tau\) are distinct, and the \(B_i\) are independent by their values at the \(d_j\). For the last two types use the constant term in \(\varepsilon\), giving the distinct cell monomials \(\pi s_{\mathrm X}\upsilon^{k_c}\) and the independent \(B_i\). Thus every \(\delta\) vanishes. This matches the \(F_1,H_1\) and \(F_2,H_2\) coefficients and eliminates all first-right pairs with any other left input.

In the multidegree with one \(\pi\) and zero degrees in \(\zeta_0,\zeta_1,\zeta''\) and net hidden-basis degree, the pairs are the matched factor products, first-left pairs with the search bases and generator, the two correction lists with matching inverse scales, and the Y column with cancellation bases. This enumeration follows by checking the degrees of the published exponents: the left first factors have one \(\pi\), the left second also has one hidden-basis degree, and the three other nonconstant left types carry only one of the three scales. The right factor scales and correction types above are their only complementary types. The left-generator pair with any published right exponent of degree one in \(\pi\) has an inverse scale and cannot enter this class. Define \(W_c\) by matched factor coefficients, and \(u_c\) by minus the first-left search-pair coefficients. The class identity is
\[
 \sum_c\gamma_c b_c+\Phi_*=\chi\kappa,\qquad
 b_c=y^\top(W_cr-u_c)+y^\top(W_c-W_c^\top)A(\tau)
              +(P_{W_c}+Z_c h_c+Z_0 R_c)(\tau).
\]
Here the two correction types produce \(Z_c h_c+Z_0R_c\) with allowed \(R_c\), by the residue-preserving monic division proved in n1. The term \(\Phi_*\) collects the masks from the factor products, the Y cancellation products and the first-left generator pairs. It is free of all \(s_{\mathrm X}\). Taking the constant term in \(\varepsilon\) and the coefficients of the distinct \(\pi s_{\mathrm X}\upsilon^{k_c}\) gives \(b_c=0\) except at the key cell, where \(b_c=\chi L_\rho\). The original identity then also gives \(\Phi_*=0\).

For each \(c\), the linear coefficient in \(y\) at \(d_0\) gives \(W_c r=u_c\). The same comparison at \(\rho,d_i\) shows \(W_c-W_c^\top\) vanishes on the spanning vectors in Amendment D, hence \(W_c\) is symmetric. The constant coefficient gives \(\deg Z_c h_c\le2D-2\) since the \(P_{W_c},Z_0R_c,L_\rho\) terms have that bound. Thus \(\deg h_c<D\) for a non-key cell or \(<D-1\) in the key cell. In the key cell evaluate at \(\rho\) where the two vanishing factors are zero to get \((W_c)_{\mathsf b_1,\mathsf b_2}=\chi\). The QAP identities in Amendment D give all Booleanity and constraint tests, with the ordinary or keyed vanishing factor as applicable. In the coefficient of each \(\eta_i\) in \(\Phi_*\) at degree zero in \(\varepsilon\), the mask part is \(\pi y^\top t_i(\upsilon)\). The remaining terms there are the Y pairs with multiples of \(P_T(\upsilon)\); the other grades and generator pairs do not contribute. Comparing the \(y_j\) coefficients and substituting the form generator for \(\upsilon\) therefore gives all three actual ties from the honest cancellation derivation.

If \(r'\) replaces \(r\), the coefficient-matching result shows the difference in the target value is \(\sum_c\gamma_c y^\top W_c(r'-r)\), because no other exponents depend on \(r\). Thus the identity remains valid throughout its prescribed locus. If all stacks are zero, it holds formally at every \(r'\) and the key corner forces \(\chi=0\). If an identity is formal for all \(r\), its equations \(W_c r=u_c\) for every \(r\) force all \(W_c=0\) and again \(\chi=0\). A difference of source expressions pairs with the other source generator to an expression of zero stack. If it vanishes identically at any fixed \(r\), this argument says it is formally zero, so formally different source expressions have the stated coincidence bound. This proves the view clauses with the new corner and one actual sector.

The formal derivative of the target expression with respect to the search coordinates, for a marked identity, is the vector \(\sum_c\gamma_c W_c^\top y\). To compute it use the private evaluation and reverse accumulation of the reduction. At each recovery point project the G1 input polynomials by setting \(\Omega_{12}=\Omega_{22}=0\) and taking the part linear in \(\pi\); these are exactly the first left coordinates. This is a linear projection and therefore respects formal equality of G1 expressions. The derivative of a G2 leaf is nonzero only for a first right coordinate and is \(s_{\rm leg}\) times the corresponding coordinate vector. The matched \(F_1,H_1\) coefficients are precisely the coefficients of the projected product in the derivative. Since unmatched first-right coefficients vanish for a marked identity, this is its full stack gradient. Formally equal targets have zero difference stack and the same gradients; formally equal G2 inputs also have equal derivative records by pairing their difference with a first-left input and applying the zero-stack result. The projected gradients always lie in the marked row space. For a nonzero linear functional on it that vanishes on a given proper subspace, the derivative polynomial after dividing by \(\pi\) is nonzero: take its degree-zero coefficient in \(\varepsilon\) and the distinct monomials \(s_{\mathrm X}\upsilon^{k_c}y_i\). Its degree is at most \(n+2\), establishing the recovery comparison used in Targets. The optional empty alpha sector has identically zero stack and gradients.

The running time with the revised exponent lists has the bound
\[
 t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT},\qquad
 C_R=8I+3L+2C_{\rm post}+C_{\rm set}+C_{\rm desc},
\]
with \(I\) for computing the initial exponents at one point, \(C_{\rm post}\) for processing one tried expression, \(C_{\rm set}\) for fixed transcript initialization, and \(C_{\rm desc}\) for the description. Here \(I,C_{\rm post},C_{\rm set},C_{\rm desc}\) are the costs for the revised exponent lists, and \(C_R=O((N_\star+n)D+\mu)\). We give the dependence on the form indices explicitly.

The per-call bound can be checked by the following implementation in the reduction's unit-operation model. Keep per group a table of assigned exponents indexed both by label and by field value, and a label table status for excluded strings. Both allocated and excluded strings are keys of the same label table, so unused-string sampling excludes both. A label record includes its value at the independent test point and a reference to its first expression node, if any. The reference or zero record is kept on repeated assignments. For an unclassified operand in an addition, scalar product or pairing, keep counters of the remaining exponents and unclassified strings in its group. Draw an integer uniformly below the latter count and compare it to the former count to decide membership. If it is a label, sample a uniformly unused exponent. Insert the relevant forward and reverse entries and update the counts. A rejection only writes its status and updates the unclassified-string count. This gives at most eight operations per unclassified operand: one status lookup, one integer sample and comparison, one exponent sample, two insertions and two counter updates. The conditional laws follow from a uniform injection after the already assigned and excluded labels have been fixed. Record-less labels in answered calls use the common zero expression, at most two further record writes per call.

For a result, allow at most 24 main operations. This includes two lookups of operands and up to three arithmetic operations each at the true and private test points. A result-label lookup, a fresh unused string sample when needed, and the two table insertions use at most four more. Updating both counts uses two. Allow six writes for an expression node (operation tag, operand references, scalar operands if needed, and result reference). The remaining four cover the private-value comparison, recording the first differing target pair, advancing the expression-log index, and checking or recording eligibility for name calls. A name call uses the same routine for negation, and then returns the two labels, with at most two label writes. It is rejected if the input's eligibility flag is absent. Repeated name calls return the already assigned opposite exponent label. An insertion at a known exponent leaves the old reverse entry in place and the private comparison uses its stored record.

For the at most six recovery passes, the forward evaluation at each point takes at most three arithmetic operations per logged gate. The private test point above uses the full exponents. At recovery points, the projected first-left values and the single-sector first-right derivative leaves are prepared before the call loop as described above. Only the right operand of a pairing can contribute a derivative in \(r\), as every G1 value is independent of \(r\). For each of the at most two trial expressions, traverse the resulting straight-line expression log backwards. A sum or scalar multiplication adds the adjoint times the corresponding scalar derivative to the adjoint of each predecessor. A pairing uses the evaluated first operand as its derivative with respect to the second. For a predecessor that is an input leaf, skip it if its derivative is zero in the current sector. Otherwise it is a first right coordinate with derivative equal to one prepared field scalar times the coordinate vector for its index \(j\); directly accumulate the adjoint contribution times this scalar in coordinate \(j\) of the gradient. This is at most three field operations for each of two precursors: a product by the gate derivative, an additional product for a leaf, and an accumulation. A non-leaf involves just the first product and accumulation. The references in the stored log give direct accesses to indexed registers, and each field operation computes its result in its destination register. Neither uses a label-table lookup. Initialize all node adjoint registers to zero before each reverse pass, using one field write per node and pass, then set the starting adjoints for the trial. These updates compute the derivatives by the chain rule in reverse order. Each recovery point therefore costs at most \(3+2(6+1)=17\) operations per call for both expression trials. Initializing the output vectors and the at most two starting adjoints per trial is fixed postprocessing. Including six passes, the call bound is at most \(24+2\cdot 8+2+2+6\cdot17=146\le148\). A fresh key-oracle answer takes one lookup, sample and insertion. A fresh seed-oracle answer replaces its one sample by \(d_R\) coordinate samples. This gives \((d_R+5)Q_H\) when each oracle has at most \(Q_H\) queries.

Only fixed inputs and setup change. Computing the initial exponents at each of at most eight points evaluates \(O(N_\star)\) degree-below-\(D\) QAP polynomials, advances powers through lengths \(O(D+n)\), and forms the \(O(nD)\) scalars in the split QAP group arrays. For the mask vectors, naive transposed ring multiplication takes \(O(nd_R+nN_\star)\) work, bounded by \(O(nD+nN_\star)\) since \(d_R\le n\le D\). Source factor entries take \(O(nN_\star)\) further operations. For postprocessing, apply the full form map to at most three vectors per sector by naive ring multiplication and solve a fixed-width linear system. The same \(O(nD+nN_\star)\) bound covers this before LIFT. Initialization queries and stores the same ring entries and creates the group label records with at most \(O((N_\star+n)D+\mu)\) operations, including masking. The fixed instance QAP polynomials and form indices fit the same size as advice in the protected cost model. Hence \(C_R=O((N_\star+n)D+\mu)\). The lifting step is called at most twice, once per tried expression. This establishes the bound above and the stated \(t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)\) specialization.

This accounts for the background list for the forms and weights block. The generic record and mark bounds depend on the degree, view, sampler and label counts. The degree and view properties needed for the repacked construction are proved above. The extractor sketches only use the coefficient arrays of the left and right factors, independently of the internal representation of the form list.


## Amendment P1

Put \(U_*=(D-1)+\nu n_{\mathsf c}\), the length of the combined polynomial interval. Require \(\Delta\le D\), \(J=\lceil U_*/\Delta\rceil\), \(J'=1\), \(\nu\mid\Delta\), and \(n\le D\). The displayed chunks contain all the merged non-sparse correction coefficients of n1. Their absolute shifts are multiples of \(\nu\), and \((J-1)\Delta<U_*\). In each G2 shifted base the multiplier \(Z_0\) has degree \(N_\star+2=D-\nu n_{\mathsf c}\), so its polynomial part has degree at most \(N_\star+2+U_*-1=2D-2\). The degree proof in C7 includes the scalar factors and validates the original comparison bound. Monic division in the polynomial view gives the same allowed remainders and the same bounded quotient criterion at every cell. All other setup and sampler premises are evaluated with the amended \(D\) and \(B_{\rm search}\) and use their stated bounds.

## Amendment n1

There are
\[
 n_1=(2K_1+1)(N+4)+2\lceil(D-1)/\nu\rceil+\Delta-\Delta/\nu
\]
transmitted G1 elements. Use the single factor sector, field mask bases and Y column of C7. Let \(S_0=\lceil(D-1)/\nu\rceil\) and
\[
 I_0=\{0\le a<D-1:\nu\mid a\},\qquad
 I_0^*=I_0\cup\{a+1:a\in I_0\},\qquad
 I_1=\{0\le a<\Delta:\nu\nmid a\}.
\]
Send \(P_a^0=[\zeta_0\tau^a]_1\) for \(a\in I_0^*\), and \(P_a^1=[\zeta_1\tau^a]_1\) for \(a\in I_1\). There are \(2S_0\) sparse entries because \(\nu\ge2\), and \(\Delta-\Delta/\nu\) non-sparse ones by alignment. Use \(Z_c=Z_*\) in the key cell and \(Z_c=Z\) elsewhere. Send one \(B_c^0=[\gamma_c Z_c(\tau)/\zeta_0]_2\) per cell and \(J\) bases \(B_{c,j}^1=[\gamma_c Z_0(\tau)\tau^{j\Delta}/\zeta_1]_2\), \(0\le j<J\). The factor arrays, search bases and cancellation arrays are those of C7, each once. If the resulting count of G2 slots is odd, append an existing unit generator, computed with one multiplication by one. It is formally the same exponent as the existing generator. Send the seed, the one element \([\alpha\kappa]_T\), and the masked message. There is exactly one fixed-base generator multiplication per transmitted group slot and one more in GT for the key. All scalar exponents use the displayed fixed factors and tabulated powers, with constant work per exponent.

### A single combination at any tag

For the internal witness \(v=(w,\mathsf b_1,\mathsf b_2,\mathsf b_3)\) put \(d_v=\mathsf b_1\mathsf b_2\). The identity of Amendment D gives the exact quotient
\[
 G_v=(A_v B_v-d_v L_\rho)/Z_0
      = Z_{\mathcal K}h_{\rm key}^v+R_v ,
 \qquad \deg h_{\rm key}^v<D-1.
\]
The component of \(G_v\) on the divisible exponents is \(Z_{\mathcal K}h_v^0\), where \(h_v^0\) is the divisible-exponent part of \(h_{\rm key}^v\); \(R_v\) is allowed and \(Z_{\mathcal K}\) belongs to \(\mathbb F_q[X^\nu]\). Exact monic division in the variable \(X^\nu\) gives \(h_v^0\). Let \(T_v=G_v-Z_{\mathcal K}h_v^0\), the non-sparse correction with degree below \(U_*\) and no divisible monomials. One can compute both from \(G_v\) by splitting its coefficient list into the residues, dividing the sparse list and keeping the complementary list. Polynomial products and monic division use \(O(D\log D)\) field operations: after reversal the monic divisor has constant term one, and the update \(u\leftarrow u(2-fu)\) doubles the correct inverse precision because its new residual is \((1-fu)^2\). Multiplication uses boundedly many power-of-two subgroup convolutions at each precision by splitting lengths \(O(D)\) into blocks of at most half the available order. The sum over doubling precisions is \(O(D\log D)\). The compressed division has lengths \(O(D/\nu)\), and evaluating the witness sums of polynomials at the subgroup uses the same allowed point arrays. Thus no separate remainder interpolation is needed.

Evaluate the sparse G1 operands
\[
 H^0=\sum_{a\in I_0}[X^a]h_v^0\,P_a^0,\qquad
 H_{\rm oth}^0=\sum_{a\in I_0}[X^a]h_v^0\,P_{a+1}^0-\rho H^0+d_v P_0^0/Z(\rho).
\]
The second uses at most \(S_0+2\) points including its two fixed operands. Form
\[
 H_j^1=\sum_{\substack{a\in I_1\\ j\Delta+a<U_*}}[X^{j\Delta+a}]T_v\,P_a^1 .
\]
The non-sparse chunks cover precisely the nonzero residue positions below \(U_*\) by P1. Subtract the pairings of \(H^0\) with \(\xi_{\rm key}(v)B_{\rm key}^0\), \(H_{\rm oth}^0\) with \(\sum_{c\ne{\rm key}}\xi_c(v)B_c^0\), and \(H_j^1\) with \(\sum_c\xi_c(v)B_{c,j}^1\) for all \(j\). They subtract the cell-weighted \((Z_*h_v^0+Z_0T_v)(\tau)\) for the key cell and this polynomial plus \(d_vL_\rho\) for other cells, since \(Z(X)(X-\rho)=Z_*\) and \(Z/Z(\rho)=L_\rho\). These are \(P_v-d_v L_\rho\) and \(P_v\), respectively.

For each right leg, form the two weighted left operands by summing \(\xi_c(v)\) times the witness-summed G1 factor of its left leg over the cells at this right leg. Pair them with the two witness-summed right coordinates. In the resulting sum the hidden basis cancels, the two antisymmetric terms \(y(v)A_v-A_v y(v)\) cancel, and the masks are subtracted with the cancellation MSM of C7 paired against the witness-summed Y. The earlier polynomial subtractions remove all \(P_v\) terms except the stated key corner. The first weighted left operand alone is the sum of the left first coordinates; pairing it separately with the search base \(s_{\rm leg}\) at each right leg and summing gives
\[
 \Psi_v=[\psi_v]_T,\qquad \psi_v=y(v)\sum_c\gamma_c\xi_c(v).
\]
The full corrected sum is
\[
 \Lambda_v=[d_v\xi_{\rm key}(v)\kappa+r(v)\psi_v]_T .
\]
To evaluate just \(\Psi_v\) there is no use of the second factor coordinate, QAP correction or cancellation.

### Tag choice and key recovery

For any external witness \(w\), write \(a_i=(w,1,0,i)\), \(b_i=(w,0,1,i)\), \(c_i=(w,0,0,i)\) for \(i=0,1\), with homogeneous coordinate one. Let \(v_*=(w,1,1,0)\). The three possible triples \((a,b,c)\) are
\[
 (a_0,b_0,c_0), \qquad (a_1,b_0,c_1), \qquad (a_0,b_1,c_1).
\]
For each triple \(a+b-c=v_*\) as an equality of integer vectors, and all its tags have \(d_v=0\), whereas \(d_{v_*}=1\). Compute the key weight and \(\Psi_{v_*}\). If the weight is zero, return \(\bot\). If \(\Psi_{v_*}=0\), compute just the full combination \(\Lambda_{v_*}\), divide by its nonzero key weight in GT and recover the key. Otherwise compute the six \(\Psi\) values of the zero-tag variants and choose the first triple with all three nonzero. If none exists return \(\bot\). Compute \(\Lambda\) for the three chosen variants and \(v_*\), reusing all first-coordinate weighted factors already formed.

For the selected triple, start by solving \(r(c)\) using \(\Lambda_c=r(c)\Psi_c\) in additive group notation and the known public center of \(c\). Then solve the two differences \(r(a)-r(c)\) and \(r(b)-r(c)\) from \(\Lambda_a-r(c)\Psi_a\) and \(\Lambda_b-r(c)\Psi_b\) with bases \(\Psi_a,\Psi_b\). Each difference is either a single tag sample or a difference of two tag samples, with a known public centering constant. Add these two recovered increments to \(r(c)\) to obtain \(r(v_*)\). Subtract \(r(v_*)\Psi_{v_*}\) from \(\Lambda_{v_*}\) and multiply by the field inverse of \(\xi_{\rm key}(v_*)\) to obtain \([\kappa]_T\). The last key-oracle call unmasks the message. The search and failure probabilities are proved below. At most seven \(\Psi\) values and four full \(\Lambda\) values are needed, and the triple choice uses only quantities independent of the search sample.

### View of the correction polynomials

Only the sparse quotient bases have inverse scale \(\zeta_0^{-1}\), and only the combined correction bases have inverse scale \(\zeta_1^{-1}\). The key-scalar degree class in C7 therefore collects them in each cell as \(Z_c h_c^0+Z_0 T_c\), with every exponent of \(T_c\) in a nonzero residue class modulo \(\nu\). Monic division of \(T_c\) by \(Z_{\mathcal K}\) preserves those classes in every subtraction step. Its remainder \(R_c\) has degree below \(\nu n_{\mathsf c}\) and is allowed. Multiplying the multiple part by \(Z_0\) gives a multiple of \(Z_*\), hence of \(Z_c\), and it is absorbed into \(h_c\). Thus the arbitrary correction is precisely of the required \(Z_c h_c+Z_0R_c\) form. The constant-term comparison in C7 bounds the quotient degree by the QAP criterion, and the changed corner is \(W_{t_1,t_2}\) from that criterion. Every other Laurent comparison uses the same input types and the same actual field ties, as proved in C7, with the two-sector copies omitted.

## Amendment n2

The exact half-count is
\[
 n_2=\left\lceil\frac{6K_2(N+4)+3K_2+(3n/2)(J+1)+(13n-9)}2\right\rceil .
\]
The first two terms count the single right factor arrays and search bases. There is one sparse list of \(A_c\) bases and \(J\) combined lists of \(A_c\) bases, and the cancellation count is \(13n-9\). The optional generator padding gives \(2n_2\) actual slots. The G1 count is proved in n1. Together with the fixed one GT element, seed and masked message, these give exactly the protected size formula and the one-generator-multiplication count from the published scalars.

## Amendment dec_sum_g1

Compute the witness sums of the two coordinates for each left leg and the Y column on the external \(w\) once with the tag coordinates omitted. In the reference witness-weight convention each uses at most \((N+1)/2\) additions. Each of the at most seven tag variants adds at most three tag entries per array. This gives \((2K_1+1)((N+1)/2+21)\). Reuse these sums for both kinds of combination.

## Amendment dec_sum_g2

For the single right factor sector, compute each of the \(6K_2\) external witness coordinate sums once, using at most \((N+1)/2\) additions each. Only the at most four full combinations need these sums with tags added; each adds at most three entries. Thus the count is \(6K_2((N+1)/2+12)\). The fixed search bases require no analogous coordinate sums.

## Amendment dec_msm_g1

The at most seven first-coordinate weighted left operands and four second-coordinate ones each use a total of \(A_c\) points across the legs. In a full combination the sparse key and non-key MSMs use \(2S_0+2\) points. The combined correction uses \(U_*-(S_0+n_{\mathsf c})\) points below \(U_*\), since there are \(S_0+n_{\mathsf c}\) multiples of \(\nu\) there. Hence the total is at most
\[
 11(3n/2)+4\bigl(D-1+S_0+2+(\nu-1)n_{\mathsf c}\bigr).
\]
All operands appear in n1. They do not require computation of a separate remainder MSM.

## Amendment dec_msm_g2

Each full combination uses \(A_c\) points for the two sparse right operands together, \(J A_c\) for the combined right list, and \(13n-9\) for cancellation. The at most four full combinations therefore use \(4((3n/2)(J+1)+(13n-9))\) points. The \(\Psi\) combinations use the fixed right search bases without new G2 MSMs.

## Amendment dec_pairings

Each of the at most seven \(\Psi\) sums uses \(3K_2\) pairings. Each of at most four \(\Lambda\) sums uses \(6K_2\) factor pairs, \(J\) combined correction pairs, two sparse pairs and one cancellation pair. Thus the total is at most \(21K_2+4(6K_2+J+3)\). Accumulate each signed sum starting with its first term, updating by the indicated group addition or subtraction. This needs at most one fewer accumulation operation per nonempty sum than its pairing count. The remaining bounded number of GT translations, final normalizations and searches are accounted for in search_spread.

## Amendment search_spread

Put
\[
 R_0=g\sqrt{(N+7)/48}+3/2,\qquad R_\Delta=g/\sqrt6+1/2 .
\]
The amended value is
\[
 \left(\frac{20}{37}\left(2\sqrt{R_0}+4\sqrt{R_\Delta}+4000\right)\right)^2 .
\]
For a selected triple the anchor has the RMS bound \(R_0\) by Bsearch. Each subsequent difference is a single centered box draw or the difference of two independent box draws. The variance is at most \(2(g^2-1)/12\), and rounding its public center contributes at most \(1/2\), giving RMS at most \(R_\Delta\). The selection and early-return tests use weights and \(\Psi\) values independent of the search vector. Thus these estimates hold conditional on the chosen case. All three true integers have absolute value at most \(B\) after centering. The final reconstructed centered value \(r(v_*)-c_{v_*}\) also has RMS at most \(R_0\); the amended spread exceeds \(R_0\) as well as the constituent bounds.

The changed pointwise search bound of Proposition 5.7(d) is the fixed-width bound below, and its expectation gives the stated efficiency conclusion for the three searches. For any centered target \(x\) known to have \(|x|\le B\) and \(\mathbb E|x|\le M\), use the sign-class baby and giant search with integer width \(b=\lceil\sqrt M\rceil+1\). Tabulate \(iP\) for \(0\le i<b\), where \(P\ne0\) is the base. The signed intervals centered at \(j(2b-1)\) with radius \(b-1\) partition the integers. Progress outward in the order \(j=0,1,-1,2,-2,\ldots\), testing the sign class of the corresponding residual against the table. Verify the sign and the resulting integer against the bound; \(2B+1<q\) makes the bounded solution unique. A match for the true integer occurs by \(|j|\le |x|/(2b-1)+1\). The baby construction has at most \(b\) counted steps. Its stride follows from the last baby point by a doubling and one addition, and each subsequent giant needs one update. Including a constant for initialization and verification, the total is at most \(b+2|x|/(2b-1)+12\) steps on a true target. This bound includes names and the constant work to derive their signs according to the protected step convention. A run with no valid solution can stop upon exploring all intervals intersecting \([-B,B]\). Since \(2b-1\ge2\sqrt M\), its expected bound on a valid sampled target is at most \(2\sqrt M+14\). A nonzero base is always used for these searches.

The anchor uses \(M=R_0\) and the two subsequent searches use \(M=R_\Delta\), by Cauchy--Schwarz. Before them the already known anchor or public centers are subtracted using one GT multiple per search. Afterward remove the target search term and normalize by the key weight with at most two more GT scalar multiples. On the protected fixed prime, binary multiplication by a scalar modulo \(q\) takes at most \(508\) additions or doublings because \(q<2^{254}\). The five scalar multiples, the elementary translations and sign handling and the three additive overheads of 14 each fit within the 4000 extra step budget. The zero-base case for the target uses only the normalization and fits the same bound. In the protected score, \((37/20)\sqrt{\mathrm{search\_spread}}\) is therefore at least the expected step bound \(2\sqrt{R_0}+4\sqrt{R_\Delta}+4000\), at the same per-step charge of six multiplications. In the asymptotic family the scalar-multiplication overhead is \(O(\log q)\) and the main expected cost is \(O(\sqrt g\,N^{1/4})\). The bounded-answer correctness follows from the unique integers found at each step and the group identities in n1. The generic extraction argument depends only on the sampled search vector and the published group and oracle law, whose conditioned density and rank bounds are proved in Bsearch.

## Amendment n

Use \(n=k d_R+1+(1-\mathrm{ring\_mode})(d_R-1)\). The second ring mode in C5 and C6 requires \(k=1\) and \(\mathrm{ring\_mode}=1\), so for the entire admitted construction \(n=d_R+1\). Put \(v_0\) in slot zero and the \(d_R\) coefficient forms of the matrix product on the witness packing of Amendment ell in slots \(1,\ldots,d_R\). Thus the kernel comparison is \((v_0,A\hat v)=(0,0)\) and every nonconstant ring form is used exactly once. The form polynomials, field identities, generic view and proof of coefficient-adjoint cost ignore where each input was packed once this kernel and the random matrix law are fixed. The output norm and matrix dimensions are exactly those proved in ell and C5. The slot dimensions used in the grid, mask calculation, oracle law and efficiency proof are the actual \(n\), not an additional padded field length.

## Targets

Fix any parameter set satisfying the amended model, the protected system shape, any admissible evaluation points, and the stated group and oracle models. In the chosen modes use the coefficient positions of Amendment n, the base field of Amendment C6 and the grid and masks of Amendment C7, and the single-sector QAP encryption and decryption of Amendment n1. The amended inverse theorem applies by (P3) with Amendments I3, I4, H2, H3 and I6. The charged-mark bound is proved in Amendment Ncmp. Correctness and extraction use the same external witness relation, oracle model, budgets and probability bounds. Internally the projected witness forgets its Boolean tags.

### Correctness with error \(2/q\)

Fix an external witness \(w\), the statement, message and admissible evaluation points. Every tag extension used in n1 is an internal witness. The group identities in that amendment show that a nonzero key weight together with a zero target base gives immediate decryption. If the target base is nonzero, any available triple yields the three unique search integers by Amendment search_spread, hence decrypts. There is an available triple whenever at most one of the six zero-tag bases vanishes, since the three triples have empty common intersection. The algorithm fails exactly if \(\xi_{\rm key}(v_*)=0\), or if \(\Psi_{v_*}\ne0\) and no triple is available, with the first condition taking precedence. We bound these two causes under the new construction.

First consider the target key weight. Write its form value as \(z(v_*)=1+\sum_{i=1}^{n-1}a_i T^i\), with all \(a_i\) independent uniform field coordinates by Amendment ell. Let \(s=n/2-1\) and \(\omega=d_*^{(q-1)/n}\) of order \(n\). The constant coefficient of \(z\cdot\sigma^s(z)\) is
\[
 1+d_*\sum_{i=1}^{n-1}\omega^{s(n-i)}a_i a_{n-i}.
\]
Besides the constant term, a pair can contribute only at total exponent \(n\), since exponents lie between 0 and \(n-1\) and \(T^n=d_*\). For \(i=1,2\), the distinct pairs \((i,n-i)\) have coefficients \(d_*(\omega^{si}+\omega^{-si})\ne0\). Indeed \(2si\equiv-2i\bmod n\); equality \(\omega^{-2i}=-1=\omega^{n/2}\) would imply \(n\mid n/2+2i\), impossible for even \(n\ge10\) and \(i=1,2\). Condition on all variables outside these two pairs and then on \(a_1,a_2\). If either is nonzero, the vanishing equation has probability exactly \(1/q\) over one independent uniform companion coordinate after fixing the other. If both are zero, the conditional probability is at most one. Hence \(\Pr[\xi_{\rm key}(v_*)=0]\le 1/q+1/q^2\).

For the other failure fix all scalar coins except \(y\) and the seed matrix. For a form value \(z\) with constant slot one, \(S(z):=\sum_c\gamma_c \xi_c(z)\) is a polynomial of total degree at most two in its other coefficients, because Frobenius is scalar-linear and the two field products are quadratic. If this polynomial is zero, all bases are zero including the target base and there is no triple failure. Otherwise each of the fixed-tag \(S(z(v))\) values vanishes with probability at most \(2/q\) by the polynomial root bound. For two distinct tag variants their form values are independent by ell. The two values \(y(v),y(v')\) are also independent uniform because the extended assignment vectors have first coordinate one and differ in a tag, so they are linearly independent. All \(y\) coordinates are independent of the seed matrix. Thus for each pair of distinct zero-tag variants the probability that both bases vanish and the target base is nonzero is at most \((3/q)^2\): either \(S\) is identically zero, when that event is empty, or the two independent products each vanish with probability at most \(1/q+2/q\). Union bound over fifteen unordered pairs gives at most \(135/q^2\). Summing both causes of failure gives at most \(1/q+136/q^2\le2/q\), using the protected value \(q>136\). Whenever neither cause prevents decryption, the normalized target element really is \([\kappa]_T\), and the key-oracle xor returns the message. This proves correctness for every required witness and setup.

### Extraction and the reduction

Let \(\mathcal A\) have the budget \(Q<2^\lambda\) of generic group calls and at most \(2^\lambda\) queries to each oracle. Fix one bit \(b\) and messages \(m_0,m_1\), and run the extraction experiment with \(m_b\). The extractor reads the answered generic transcript without any oracle calls. It uses the protected extractor sketches for the plain sector. The empty alpha sector can be represented by zero records. It samples three independent probe vectors for each cell, uses the linear combinations of source-group records and pairings to form sketches, tests the sketches of the result and the difference when there is an old record, and directly checks its ordinary assignment against \(S\), checks the three tag bits, and returns the ordinary witness only. In rank at most three, there are at most four assignments with first coordinate 1 to test: row echelon pivot coordinates determine the vector, pivot 0 must be present, and at most two remaining pivot choices are bits. Output is therefore always \(\bot\) or a witness. A record creation, result, or difference touches \(O(K_1N_\star+n)\) field elements, since a source-group record uses at most \(K_1\) length-\((N_\star+1)\) vectors or \(6A_c\) values, and the pairings compute six such combined sketch vectors. For a pairing, forming the inner products in the G2 record or summing per left leg and combining the G1 vectors uses \(O(K_1N_\star+n)\) operations. A test uses \(O(N_\star)\) for elimination with at most three rows and \(O(N_\star+|S|)\) to generate and check the constant number of candidates. Initialization samples \(6A_c(N_\star+1)\) field values, enters the \(L\) labels as records whose vectors are materialized on first use, and uses \(O(nN+L)\) time. There are at most four tests per result. Thus the extractor uses \(O((Q+1)(nN+|S|)+L)\) time because \(K_1\le n\) and \(N_\star\ge1\).

The reduction on input a uniform \(A\in R_q^{k\times\ell}\) samples the seed, programs the seed oracle at that seed on matrix columns 1 through \(\ell\) using \(A\), and samples the other answers lazily, including the independent column 0. It samples encryption coins as specified, produces the ciphertext for \(m_b\), and simulates all generic labels and names and random oracles by the protected lazy tables. It runs \(\mathcal A\) once. The extraction steps use the answered generic transcript without its output or the random-oracle query transcript, while the lazy tables implement exactly the direct oracle law. Because the programmed entries are jointly independent uniform ring elements for uniform \(A\), all oracle answers including entries at the selected seed have exactly the joint law of the experiment. Private evaluation points are sampled independently of the run.

The reduction keeps records evaluated at its private test point, using the protected rules for guessed operands and for existing records. It tries the first GT result whose label has an existing record of different private value, using the difference expression, and also the target label's record if present. For each tried expression it computes three independent gradient vectors in the plain sector at private recovery points, tests their span for a kernel vector, and applies the unchanged LIFT algorithm if there is such a vector. An output from LIFT is a short multiple of that kernel vector. The coefficient of \(T^0\) in \(z(v)\) is \(v_0\). All \(kd_R\) remaining row coefficients give the equations of \(A\) on the packed input once \(v_0=0\). Thus a nonzero kernel vector has \(v_0=0\) and satisfies \(A\hat v=0\). Its short multiple has \(x_0=0\) since \(2\beta<q\). Reduction and packing commute, and packing preserves all ordinary and tag coordinates by Amendment ell and adds only zeros. This packs the output into a nonzero norm-at-most-\(\beta\) solution to \(A\hat x=0\), exactly for the challenge whose rank, columns, bound, and norm are costed by M1. If no such output is found the reduction returns \(\bot\). Denote its success probability by \(s_b\). The cost is \(t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT}\) with \(Q_H\) the maximum per-oracle query count, \(C_R=O((N_\star+n)D+\mu)\) for the fixed simulation setup and postprocessing, and \(T_{\rm LIFT}\) the time of the lifting step. The reduction-time argument in C7 proves this reduction-time bound on the revised lists, including the original private record and gradient loop costs and the new fixed setup. The inverse conditions and comparison count do not enter those time calculations. LIFT's running-time result applies by \(2\beta<q\) and (P4). In particular the cost is \(t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)\) using \(n,N_\star\le D\).

Here is how the first-mark bounds apply to these algorithms. The degree and view for the new field encoding and the needed gradient formula are derived above. The record invariant uses no inverse premise: setting all guesses to zero commutes with additions and pairings, and before the first mark every reused label comes from formally equal expressions. Formally equal target expressions have identical stacks by the fiber equations applied to their difference for every field search vector. Thus their records also have equal sketches. A good mark's stack is usable with the three field ties of Amendment C7 by the revised view. Its rank is at most three by \(g^{-4}<\mu_{\rm tr}<\theta\) from (I5) and the protected stack rank bound. On the dense choice the stronger guard \(g^{-3}<\mu_{\rm tr}\) gives rank at most two. The full classification applies to every actual tied stack of dimension at most three, including zero-corner marks, because the three ties just derived are the original field identities. A kernel vector in its row space has coordinate 0 equal to zero, and its one-dimensional guessing probability is at least the stack's, by the protected guessing-probability lemma. The amended inverse theorem gives a short multiple, so LIFT succeeds on it.

At a first good difference mark its difference is formally nonzero, so the cleared polynomial is nonzero in the coins at some fixed search vector. This makes it a nonzero joint polynomial in coins and search coordinates. The private test uses independent uniform search coordinates and valid coins; the product-set bound gives failure probability at most \(d_f/(q-D)\). Earlier formal equalities are equalities at every private point by the record invariant, so outside this failure the reduction picks exactly this difference. The degree bound and the uniform valid coin ranges give probability at most \(\varepsilon_f\) for this failure. For a first good key mark the target record already has its expression by the record invariant and persists. Name negatives are target-group results and receive the same private and sketch tests. For a recognized good mark, the coefficient-vanishing and derivative calculation of the algebraic view subsection place each sector gradient in that sector row space. There is no nonzero alpha stack. For any proper subspace of the mark row space choose a linear form zero on the subspace and nonzero on the row space. Its value on one gradient, divided by \(\pi\), is a polynomial of degree at most \(n+2\) which is nonzero by isolating the constant term in \(\varepsilon\) and the distinct monomials \(s_X\upsilon^{k_c}y_i\). The valid values for the independent coin coordinates have sizes at least \(q-D\), by the independent coin support argument. The polynomial root bound, with \(q-D\) in place of \(q\) in its proof, bounds the chance of failing to increase the span while it is proper. Three independent points and rank at most three give failure at most \(3(n+2)/(q-D)\le\varepsilon_f\), by \(n\le D\) and the formula for \(\varepsilon_f\). Thus on a good first mark with a kernel vector, except for the two exceptional events just bounded, the reduction finds a kernel vector in the appropriate span, and produces the MSIS output. The unconditional probability of such a mark is at most \(s_b+2\varepsilon_f\).

For a good first mark with no kernel vector, the classification proved in Amendment C7 gives an extended witness in its row space. Its ordinary projection satisfies the external system. In that sector the linear map from a tuple of probes to \(\sum_c W_cv_c\) has image the row space, as each matrix is symmetric and the sum of its images is the row space of the stack. Uniform independent probe tuples give three independent uniform vectors in this space, even conditional on the run. In dimension \(a\le3\), the chance of failing to span is bounded by \(\sum_{j=0}^{a-1}q^{j-3}<2/q\): equivalently the \(a\) rows of the random \(a\)-by-3 coordinate matrix are independent uniform three-dimensional vectors and the next row falls in the span of \(j\) independent previous rows with probability \(q^{j-3}\). At a difference mark the extractor tests the record difference. If the old entry is a pure guess, a guess-free difference requires the result to contain that same guessed variable with coefficient one. The label has therefore been used in an answered call, possibly the current call, and has a zero record by the test. At a key mark it tests the record of the result that obtained the target label. An initially received record has zero stack and thus is no good mark. These facts from the record invariant show that if the sampled vectors span, the witness is among the assignments tested. So the probability of a good first mark with no kernel vector and with extractor failure is at most \(2/q\).

Let \(u=2Q+2\). Every target query run has a first mark. The protected initial and guessed-mark estimates and the charged-mark estimate of Amendment Ncmp bound their three probabilities by
\[
\left(\binom{L_1}{2}+\binom{L_2}{2}+\binom{L_T}{2}\right)\varepsilon_f,\quad
N_{\rm cmp}(u)(\theta+\varepsilon_f)
+\left(\binom{L+3u}{2}+L+3u\right)\varepsilon_f,\quad
2^\lambda/N_{\rm free},
\]
respectively. These estimates concern the same sampler, oracle and record laws and use only the already checked view and degree properties, budget, and label counts. Together with the two good-mark cases they cover the event of a target key query and no witness. Their sum is at most \(s_b+E(u)\): the good-mark excess is \(2\varepsilon_f+2/q\le (8u+8)\varepsilon_f\), using \(\varepsilon_f\ge1/q\); the remaining terms of \(E\) are nonnegative and its guess term contains \(2^\lambda/N_{\rm free}\). By (P5) and the generic-ledger implication of Amendment Ncmp \(E(2Q+2)\le(Q+1)/2^\lambda\). Hence for each \(b\) the target-query and no-witness probability is at most \((Q+1)/2^\lambda+s_b\), with exactly the stated oracle budgets and one MSIS instance. This proves Theorem 5.9 with its extraction time and soundness as above.
