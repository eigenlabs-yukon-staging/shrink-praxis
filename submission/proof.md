# Praxis with shared sparse quotients and two cancellation lists

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

The product circuit for fixed ring entry \(a\) is linear in \(u\): convolutions by fixed values, frequency scalings, fixed permutations and copies, additions, and fixed-scalar products in the monic reduction. It has \(O(d\log(2d))\) operations, with at most two inputs to each linear operation. The explicit reverse accumulation proved in the preceding transpose paragraph applies to this circuit, producing the coefficients of \(u\mapsto\langle L,a u\bmod\bar P\rangle\) from the form multiplier table \(L\) in the same time. It works for every multiplier table, including those from the mixed-base Frobenius coordinates, since it assumes no shape of \(L\). Thus formation of the three evaluated masks and decryption's ring products have the same \(O(k(\ell+1)d_R\log(2d_R))\) form-work bound. The benchmark's protected unit charge for them still uses \(k(\ell+1)d_R\) matrix coefficients. In the reduction one can alternatively use naive convolution and monic division in \(O(d^2)\) operations and transpose that linear circuit, giving the same \(O((N+n)D)\) fixed cost used in C7. Indeed \(k d\le n\), \((\ell+1)d\le N+2d\), and \(n,d,N\le D\).

The common packing and distribution argument below applies to this branch as well. It uses monicity, the full coefficient basis and the ring equation under reduction, all established here. The rest of the construction acts on the field coefficient forms \(z\), with the same positions and degrees under Amendment n and C6, and the same three ties. Its rank-three classification, view, packing, entropy bounds and proof of extraction do not depend on how ring products were computed. With the above ring operations its group counts, oracle counts and required complexity bounds remain the same. The original power-of-two ring branch still admits the original asymptotic parameter family.

### Kernel conversion and scope

The coefficients are placed at the slots proved in Amendment n. Each uniform entry has exactly \(d_R\) independent field coefficients in the stated power basis. A form-kernel vector therefore has constant coordinate zero and maps to zero under the nonconstant columns in the selected coefficient ring. Conversely these equations force all form coefficients to vanish. A short integer scalar multiple has integer coordinate 0 equal to zero because its residue vanishes and \(2\beta<q\). Forming the packed vector from its other coordinates preserves every coordinate once, adds only zeros, and commutes with integral reduction and field scaling. This proves the kernel-to-Module-SIS conversion in the heavy-stack lemma and in Targets. The rank bound and inverse theorem use only the search distribution and the short multiple of a vector with zero constant coordinate. Their hypotheses and conclusions are independent of the choice of monic ring. LIFT is a base-field integer-vector operation, so its correctness and time bounds are also independent of that ring.

The reduction programs the chosen uniform Module-SIS challenge into the nonconstant seed matrix columns and samples the constant entries independently in the same ring. This is exactly the stipulated random oracle distribution. The view, mask, classification, and reduction arguments use the resulting linear form map, its stated kernel, and its coefficient tables. Their proofs in Amendments n, C6, C7 and Targets apply without further ring identities. The same ring algorithms account for preprocessing and kernel tests, with the already stated query and runtime capacities. The ring branch with growing power-of-two degree remains available to the asymptotic corollary, as detailed in Amendment C7. Correctness, extraction and the extractability-error corollary for this exact instance follow from Targets and Amendment Ncmp.

## Amendment I3

The amended (I3) is
\[
\Lambda_1\ge 2\sqrt3 R_{\rm tr}\sqrt N,\qquad
\Lambda_2\ge \sqrt2\,\pi R_{\rm tr}^2 N,\qquad
\Lambda_3\ge \frac{20\,\pi R_{\rm tr}^3 N\sqrt N}{9\sqrt2} .
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

Let \(\Theta\) be a rank-three saturated lattice on a set of at most \(N\) coordinates with \(m(\Theta)\ge\mu_{\rm tr}\). Apply the preceding prefix estimates with a largest minor of size three ordered first. At the first rank-three prefix the height is 1 and density \(g^{-3}\). Write \(s_1,\ldots,s_a\) for the nontrivial step orders (at least 2), in the original prefix order. The height and density are bounded by
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

The claim of `lem:sparse` is as follows. Let \(B\) be a basis of an integral lattice \(\Theta\) on a coordinate set \(I\) with \(|I|\le N\), of rank \(d\in[3]\). Let \(F\ne\varnothing\) be a set of points of the integer box on \(I\cup\{i'\}\), \(i'\notin I\), trimmed by \(\Theta\), and \(\Phi(r)=(B^\top r_I,r_{i'})\). If (a) \(\Phi(F)\) has affine dimension \(d+1\) and lies in a coset of an index-\(q\) subgroup of \(\mathbb{Z}^{d+1}\), then
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
 \le h(\Theta)\sqrt{\binom{N}{s-1}} .
\]
Combining with the counting bound and \(\Pr[F]\le |\Phi(F)|m(\Theta)/g\) gives
\[
 \Pr[F]|\det(B_1)_J|\delta
 \le g^{j}h(\Theta)m(\Theta)
      (j+2)!v_j R_{\rm tr}^{j}\sqrt{\binom{N}{j}/12^j},
 \qquad j=s-1 .
\]
Use \(\binom{N}{j}\le N^j/j!\) and \(v_1=2,v_2=\pi,v_3=4\pi/3\). The three upper bounds on the geometric factor are \(2\sqrt3 R_{\rm tr}\sqrt N\), \(\sqrt2\pi R_{\rm tr}^2N\), and \(20\pi R_{\rm tr}^3N^{3/2}/(9\sqrt2)\). They are at most the three allowed \(\Lambda_j\). In case (a), divide by \(q\) to obtain the claim. In (b), replace \(|\det(B_1)_J|\delta\) by \(h(F^\perp)\) on the left to obtain the claim.

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
The upper range constraint also gives the original specialization of the search cost to \(O(2^{\lambda/4}N^{1/4})\) in the common efficiency derivation below. The full-rank inverse premises are derived in I3, H2 and I6. This choice permits the original range scale \(g=\Theta(2^{\lambda/2})\).

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

For \(M>A_g\), let \(\Theta\) be any saturated regular rank-two lattice of density at least \(\mu_{\rm tr}\) on at most \(N\) coordinates. Regularity gives \(h(\Theta)\le\Gamma_2/(g^2\mu_{\rm tr})\). We prove the second bound by strengthening the integer-order argument of Amendment I4. Order the coordinates with a largest minor first. By the prefix count proved there, take the nontrivial step orders \(s_1,\ldots,s_t\ge2\) in order. The height and density satisfy
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
 4H_2q\le3\beta^2,\quad 2509\lfloor H_3\rfloor q^2\le1000\beta^3.
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

### A fourth-moment bound for the transformed determinants

Write \(I=\sum_i w_i u_i u_i^\top\) with positive weights on active indices. Their sum is 3 by taking traces. Draw independent unit vectors \(X,Y,Z\) from the active list with probabilities \(w_i/3\), so \(\mathbb E XX^\top=I/3\). Put \(a=\sqrt{\det A}\) and \(D_*=(\det(X,Y,Z))^2\). Every determinant of three transformed rows has absolute value at most \(a\), by the normalized determinant bound before applying \(A^{1/2}\). Thus \(0\le D_*\le a^2\) for every outcome, including repeated rows.

Let \(p=X\cdot Y\), \(r=Y\cdot Z\), and \(s=Z\cdot X\). By expanding the three-dimensional Gram determinant,
\[
 D_*=1-p^2-r^2-s^2+2prs .
\]
Isotropy gives \(\mathbb E p^2=1/3\), \(\mathbb E p^2r^2=1/9\) by conditioning on \(Y\), and \(\mathbb E prs=1/9\) by conditioning on \(X,Y\), because \(\mathbb E[rs\mid X,Y]=p/3\). The same conditioning gives \(\mathbb E[p^3rs]=\mathbb E[p^4]/3\). The cycle permutations have the same expectations. Thus \(\mathbb E D_*=2/9\). To compute its second moment, put \(M=\mathbb E p^4\) and \(T=\mathbb E p^2r^2s^2\). Squaring the displayed Gram formula and substituting the computed expectations gives
\[
 \mathbb E D_*^2=1-2+3M+\frac{6}{9}+\frac49-4M+4T
 =\frac19-M+4T .
\]

On the real vector space of symmetric three-by-three matrices with inner product \(\langle B,C\rangle=\operatorname{tr}(BC)\), define the positive semidefinite operator \(L(B)=\mathbb E[\langle XX^\top,B\rangle XX^\top]\). The trace of an outer product operator of a vector with itself equals its squared norm, so \(\operatorname{tr} L=\mathbb E\|XX^\top\|_{\rm F}^2=1\). The identity matrix is an eigenvector with eigenvalue \(1/3\), and its orthogonal complement has five nonnegative eigenvalues \(\lambda_1,\ldots,\lambda_5\) summing to \(2/3\). The trace of a product of two outer products is the square of their inner product. For three it is the product of their three cyclic inner products, by direct multiplication of the rank-one operators. Applying these identities to independent samples, whose inner products on this matrix space are squared dot products, gives \(M=\operatorname{tr} L^2\) and \(T=\operatorname{tr} L^3\). Therefore
\[
 \mathbb E D_*^2=\frac4{27}+\sum_{i=1}^5 (4\lambda_i^3-\lambda_i^2).
\]
Let \(f(t)=4t^3-t^2\) and \(m=2/15\). For each \(t\ge0\), the exact identity
\[
 f(t)-f(m)-f'(m)(t-m)=(t-m)^2(4t+8m-1)\ge0
\]
holds because \(8m-1=1/15\). Summing cancels the linear term and gives \(\mathbb E D_*^2\ge4/27+5f(m)=8/75\). Since \(D_*^2\le a^2D_*\) pointwise, we conclude
\[
 a^2\ge\frac{8/75}{2/9}=\frac{12}{25}.
\]

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
 \frac{12}{25}-\left(\frac{6928}{10000}\right)^2
 =\frac{11}{390625}>0 .
\]
Also \(\pi>6283/2000\). Indeed \(\pi=16\arctan(1/5)-4\arctan(1/239)\) by the tangent addition formula in the first quadrant: the tangent of \(4\arctan(1/5)\) is \(120/119\). Integrating the alternating geometric series for \(1/(1+s^2)\) gives
\[
 \pi>16\left(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}-\frac1{7\cdot5^7}\right)-\frac4{239}
 =\frac{1231847548}{392109375}>\frac{6283}{2000}.
\]
Thus \(x> x_0=21764/10000\) since \((6283/2000)(6928/10000)-x_0=39/1250000\). With \(c=2509/1000\) and \(r=8/c-4x_0/3=1348531/4704375>0\), the exact comparison is
\[
 4(3-x_0)^3-27r^2=\frac{394261548376699}{24590160156250000}>0 .
\]
Taking the positive root verifies \(4x_0/3+2(3-x_0)^{3/2}/(3\sqrt3)>8/c\). The case \(x\ge3\) also exceeds \(8/c\). This proves the required rank-three volume estimate with coefficient \(2509/1000\).

We also use the following elementary lattice-volume implication. For a full lattice \(L\) in \(\mathbb{R}^d\) and a centrally symmetric compact convex body \(K'\) with \(\operatorname{vol}K'\ge 2^d\det L\), there is a nonzero lattice point in \(K'\). For strict inequality, translate the pieces of \(K'/2\) lying in distinct translates of a half-open fundamental parallelepiped for \(L\) back into that parallelepiped. The sum of their volumes exceeds \(\det L\), so two pieces overlap. The two corresponding distinct points of \(K'/2\) differ by a nonzero lattice vector, lying in \(K'\) by convexity and symmetry. For equality apply the strict argument to \((1+1/j)K'\) for each positive integer \(j\); these sets lie in \(2K'\), which contains only finitely many lattice points. A nonzero point occurring infinitely often lies in the closed body \(K'\).

### Amended inverse theorem

For prime \(q\), with the remaining hypotheses in `lem:inverse` and the (I6) above, every nonzero \(v\in\mathbb{F}_q^{N+1}\) with \(v_0=0\) and \(\operatorname{gp}(v^\top)>\theta\) has an integer short multiple \(x\) with \(x_0=0\), \(0<\|x\|_\infty\le\beta\), and \(x\bmod q=a v\) for some \(a\in\mathbb{F}_q^*\).

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

For a point in the trimming ellipsoid, the absolute deviation in coordinate \(j\) from the center is at most \(R_{\mathrm{tr}}\sqrt{(\Sigma_\Theta)_{jj}}\), by Cauchy–Schwarz after applying \(\Sigma_\Theta^{-1/2}\). Thus the corresponding row of \(\Delta_*\) has entries bounded by \(2R_{\mathrm{tr}}(g/\sqrt{12})\sqrt{N}\|B e_j\|_\infty=T_{\mathrm{tr}}\|Be_j\|_\infty\). The last row is bounded by \(g-1<T_{\mathrm{tr}}\). In a minor of order \(k'\), products of row norm factors are bounded by \(\prod_{j=1}^d\|Be_j\|_\infty\) since each basis vector is nonzero and integral. Also \(T_{\mathrm{tr}}\ge1\). Expansion by permutations gives the bound
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
 \operatorname{vol}_3(\beta K_B)\ge (8/(2509/1000))\,\beta^3
 \ge (8/(2509/1000))\,(2509/1000)\lfloor H_3\rfloor q^2
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


## Amendment C6

### Coefficient positions

Use the row coefficient formulas in the protected forms block, taking the ring from C5, and set \(p=1+(1-\mathrm{ring\_mode})(d_R-1)\) as in Amendment n. Put \(\varphi_0(w)=w_0\), put zeros in slots \(1,\ldots,p-1\), and place the coefficient of \(Y^s\) from the \(i\)-th row product at slot \(p+(i-1)d_R+s\) for \(1\le i\le k,\ 0\le s<d_R\). The \(k d_R\) populated row slots run from \(p\) through \(n-1\) once. The defined form \(z(v)\) is zero precisely when \(v_0=0\) and \(A\hat v=0\) for the nonconstant columns \(A\) of \(M\), because the field basis coefficients are independent and the product terms from the zero column have the factor \(v_0\). The ring and its programmed matrix distribution are exactly those of C5.

The first field disjunct requires \(\mathrm{scalar\_rel}=0\) and the conditions below. The second field disjunct, with \(\mathrm{scalar\_rel}=1\), follows the first field construction. Let \(e=\mathrm{base\_degree}\) and \(h=n/e\). Require \(2\le e\le16\), \(e\mid q-1\), \(2e\mid n\), \(h\mid(q^e-1)^{28}\), \(2n\le D\), \(\Delta\ge h+e+2\), and \(J=1\) or \(\nu\mid\Delta\). The last condition aligns non-sparse quotient chunk shifts with residue classes; if there is one chunk, its shift is zero. The equality \(\mathrm{base\_degree}=\lfloor\mathrm{base\_degree}\rfloor\) explicitly enforces the integer auxiliary degree, and the divisibilities require integer inputs. The basis uses the \(n\) slots specified in Amendment n.

Choose a public primitive \(d_*\in\mathbb F_q^*\). A root of \(H^e-d_*\) is multiplied by \(\omega_0=d_*^{(q-1)/e}\) under \(q\)-Frobenius. Since \(\omega_0\) has order \(e\), the root has orbit length \(e\) and \(F_0=\mathbb F_q[H]/(H^e-d_*)\) is a field. Let \(Q=q^e\) and choose a public primitive \(c_*\) of \(F_0^*\), represented as \(c_*(H)\) with degree below \(e\).

For a root \(t\) of \(T^h-c_*\) in the algebraic closure, its multiplicative order \(m\) satisfies \(m/\gcd(m,h)=Q-1\). The divisibility \(h\mid(Q-1)^{28}\) makes each prime of \(h\) a prime of \(Q-1\). At such a prime the valuation of \(m\) is therefore the sum of the valuations of \(h\) and \(Q-1\). At any other prime it is just the valuation of \(Q-1\). Thus \(m=h(Q-1)\). For a prime \(p\mid h\),
\[
 v_p(Q^j-1)=v_p(Q-1)+v_p(j)\qquad(j\ge1).
\]
For an odd \(p\), expand \((1+a)^p-1\) for \(p\mid a\). Its first term \(pa\) has valuation strictly below that of each later term, by the intervening binomial coefficient divisibilities and \(p>2\). At \(p=2\) the same comparison \(v_2(2a)<v_2(a^2)\) holds because \(4\mid Q-1\). Taking a power prime to \(p\) preserves the valuation by factoring the difference of powers and reducing the geometric sum modulo \(p\). Iterating proves the formula.

Consequently \(m\mid Q^j-1\) exactly when \(h\mid j\). This gives relative Frobenius orbit length \(h\), proving irreducibility and the degree-\(n\) field \(F=F_0[T]/(T^h-c_*)\). At \(j=h/2\) the same valuations give \(m/2\mid Q^j-1\) and \(m\nmid Q^j-1\). Thus the absolute half-turn \(\sigma^{n/2}=(\sigma^e)^{h/2}\) fixes \(F_0\), fixes \(T^2\), and sends \(T\) to \(-T\).

Use the basis \(H^\iota T^s\), \(0\le\iota<e,\ 0\le s<h\), with slot \(es+\iota\). Comparing these coefficients in \(z(v)\) gives the same kernel condition \(v_0=0,\ A\hat v=0\) for the selected C5 ring with its coefficient infinity norm. The products \(U=z(w)\sigma^{n/2-1}(z(w))\), \(V=z(w)\sigma^{n/2}(z(w))\) and \(\sigma^{n/2+1}(U)=z(w)\sigma^{n/2+1}(z(w))\) supply the weights. The half-turn fixes \(V\), so it has only even \(T\)-degrees.

Write \(z_-,z_0,z_+\) for the reduced form vectors at the three indicated successive Frobenius exponents. For any monomial write \(F_{s,\iota}\) for the representative of \(\sigma^{n/2+1}(H^\iota T^s)\). More generally its representative under \(\sigma^j\) has single \(T\)-power \(sq^j\bmod h\) with \(F_0\) coefficient \(\omega_0^{j\iota}H^\iota c_*^{\lfloor sq^j/h\rfloor}\). This follows by powering and reduction modulo the binomial. For each of the three relevant exponents, as \(s\) increases the quotient exponent increments by \(\lfloor q^j/h\rfloor\) or this number plus one. Obtain these powers of \(c_*\) using the public remainder \(q^j\bmod h(Q-1)\), which suffices after reducing the quotient modulo \(Q-1\). The initial field powers take \(O(\log q)\) operations and tabulation takes \(O(n)\). The coefficient widths are bounded by 16, so the tables evaluated at independent \(\upsilon,\upsilon_H\) also take \(O(n)\) field work.

The evaluated form multipliers at all three points are taken in their slots under Amendment n. For each ring row, use the transpose of its coefficient multiplication by the matrix entry to apply the listed linear functional to the ring product, as proved for each ring in C5. This costs \(O(k(\ell+1)d_R\log(2d_R))\) operations for a constant number of multiplier tables. The scoring model uses its protected matrix coefficient charge on the same coefficient dimension \(k(\ell+1)d_R\). All ring dimensions, seed-oracle calls and the kernel equivalence were established above. The following scalar-relative field alternative uses the same coefficient positions and the transposed evaluation with its own basis table.

### One-variable scalar field mode

The second disjunct, with \(\mathrm{seed\_mode}=0\), requires \(\mathrm{scalar\_rel}=1\), \(e=\mathrm{base\_degree}=1\), and \(2\mid n\). It requires \(n=h\mid(q-1)^{28}\), \(2n\le D\), \(\Delta\ge h+e+2\), and \(J=1\) or \(\nu\mid\Delta\). Take \(F_0=\mathbb F_q\) and \(P_H=H\), so only the basis digit zero occurs. The relative modulus is \(P_T(T)=T^n-d_*\) with \(d_*\) a public primitive scalar. For a root \(t\), its multiplicative order \(m\) satisfies \(m/\gcd(m,n)=q-1\). Every prime of \(n\) divides \(q-1\), so the valuation of \(m\) there is the sum of the valuations in \(n\) and \(q-1\). The other valuations are those in \(q-1\). Hence \(m=n(q-1)\). The binomial and geometric-sum argument of the first disjunct gives \(v_p(q^j-1)=v_p(q-1)+v_p(j)\) at every prime \(p\mid n\), with the two-adic identity using \(4\mid q-1\). The scalar Frobenius fixed-point condition for \(t\) is therefore \(n\mid j\), and the orbit gives the monic irreducible polynomial \(P_T\). At \(j=n/2\) we have \(m/2\mid q^j-1\) but \(m\nmid q^j-1\). Thus \(t^{q^{n/2}}/t=-1\), giving the half-turn sign and the even support of \(V\).

For \(0\le s<n\) let \(b_j=q^j\bmod n(q-1)\). The representative of \(\sigma^j(T^s)\) is
\[
 F_{s,0}^{(j)}(T)=d_*^{\lfloor s b_j/n\rfloor}T^{s b_j\bmod n}.
\]
The displayed residue of \(q^j\) suffices because the field order of \(d_*\) divides \(q-1\). For increasing \(s\), the exponent of \(d_*\) increments by \(\lfloor b_j/n\rfloor\) or by one more. Compute the two initial step powers in \(O(\log q)\) field operations and the table in \(O(n)\). The evaluated form multipliers use the same coefficient slots of Amendment n and same transpose evaluation as in the mixed-base disjunct. When \(n\mid q-1\), Frobenius leaves the exponent of each slot unchanged. In the other case C7 uses the exchanged relative positions, for which conjugation preserves the left subgroup of exponents. The three field relations use the same Frobenius projections. The independent auxiliary evaluation coin has degree zero in all these one-variable representatives.


### One-variable modulus from a bounded seed field

The additional disjunct keeps \(e=1\), so \(F_0=\mathbb F_q\) and \(P_H=H\). It requires \(n\le4800\), \(2\le s_0\le32\) integral, \(2s_0\mid n\), and \(r_H=n/s_0\mid(q^{s_0}-1)^{28}\). Here \(s_0=\mathrm{seed\_degree}\), \(Q=q^{s_0}\), and \(r_H\) is even. The same chunk, FFT and evaluation-point conditions hold. In this branch \(\mathrm{seed\_mode}=1\); in both preceding disjuncts it is zero.

Choose \(K=\mathbb F_q[X]/(f(X))\) for a monic irreducible \(f\) of degree \(s_0\). This step can use uniform random monic polynomials of that degree, with a test as follows. Compute \(X^{q^{s_0}}-X\) and \(X^{q^{s_0/p}}-X\) modulo \(f\) for each prime \(p\mid s_0\). The first must be zero and each of the latter must have gcd 1 with \(f\). The roots of \(X^{q^a}-X\) are all elements of \(\mathbb F_{q^a}\) and are simple. Thus the first test says the irreducible factors are distinct and have degrees dividing \(s_0\). Every proper divisor of \(s_0\) divides \(s_0/p\) for some such prime, so the other tests make every factor have degree \(s_0\). This proves the test's equivalence to irreducibility. The field of degree \(s_0\) has at least \(q^{s_0}-s_0q^{s_0/2}\) elements outside its proper subfields, by counting at most \(s_0\) subfields of degrees at most \(s_0/2\). Each orbit of these elements yields a different monic irreducible, so the sampling probability is at least \((1-s_0 q^{-s_0/2})/s_0\). The tests take \(O(\log q)\) field operations because the degrees and the number of tests are bounded.

In \(K^*\) choose \(c_H\) of degree \(s_0\) over \(\mathbb F_q\) with \(c_H^{(Q-1)/p}\ne1\) at every prime \(p\mid r_H\). All these primes divide \(Q-1\). The order condition at each such prime says that the exponent of \(c_H\) as a power of a multiplicative generator is nonzero modulo \(p\). Uniform sampling meets all order conditions with probability \(\prod_{p\mid r_H}(1-1/p)\). There are at most five primes because \(r_H\le2400\) and the product of the six smallest primes exceeds 2400. The product is at least \(2^{-5}\). The fraction of elements of \(K^*\) in proper subfields is at most \(s_0 q^{s_0/2}/(Q-1)<2^{-6}\) for the protected prime and this degree range. Therefore testing both the order condition and full degree succeeds with probability at least \(2^{-6}\). Test full degree by checking \(c_H^{q^{s_0/p}}\ne c_H\) for the primes of \(s_0\). Both tests cost \(O(\log q)\) operations per trial in the scalar field, since the degree of \(K\) and the number of tests are bounded. Its minimal polynomial \(p_c\) is the product of the \(s_0\) linear polynomials from the Frobenius orbit, with coefficients fixed by Frobenius. The public seed constants are independent of the system and encryption coins. Setup is deterministic once they are fixed.

Let \(t\) be a root of \(T^{r_H}-c_H\) in the algebraic closure. If \(o\) is the order of \(c_H\) and \(m\) the order of \(t\), then \(m/\gcd(m,r_H)=o\). The order tests give \(v_p(o)=v_p(Q-1)>0\) at each prime of \(r_H\). Thus \(m=r_Ho\). The prime-by-prime valuation formula above holds for \(Q\), including at two since \(4\mid Q-1\). For a positive \(j\), the condition \(m\mid Q^j-1\) is therefore equivalent to \(r_H\mid j\). Thus \(t\) has degree \(r_H\) over \(K\). As it generates \(c_H=t^{r_H}\), it also generates \(K=\mathbb F_q(c_H)\) over \(\mathbb F_q\). Its degree over \(\mathbb F_q\) is \(s_0r_H=n\). The monic polynomial \(P_T(T)=p_c(T^{r_H})\) of degree \(n\) vanishes at \(t\), proving irreducibility.

At \(j=r_H/2\), the same valuations show \(m/2\mid Q^j-1\) and \(m\nmid Q^j-1\). Consequently \(t^{q^{n/2}}=-t\), since \(Q^{r_H/2}=q^{n/2}\) and \(-1\) is the unique element of order two. Use the monomial basis through degree \(n-1\) in the same form slots as above. The \(V\) weights have even powers only. All three consecutive Frobenius projections have their original field identities and the same coefficient-kernel relation.

For exponent \(j\) of Frobenius put \(b_j=q^j\bmod r_H(Q-1)\). For each basis monomial \(T^a\), its reduced representative is obtained from
\[
 c_H^{\lfloor a b_j/r_H\rfloor}T^{a b_j\bmod r_H}
\]
by expanding the coefficient in the basis \(1,c_H,\ldots,c_H^{s_0-1}\) and replacing \(c_H\) by \(T^{r_H}\). The modulus for \(b_j\) suffices because the order of \(c_H\) divides \(Q-1\). This produces at most \(s_0\) powers of degree below \(n\), all congruent to \(a b_j\) modulo \(r_H\). For increasing \(a\), the quotient increments by \(\lfloor b_j/r_H\rfloor\) or by one more. Compute these two step powers with \(O(\log q)\) field operations and tabulate the representatives in \(O(n)\) operations using the bounded degree. Evaluate the table in \(O(n)\) operations given the evaluation point's powers. The resulting coefficients are used in the same ring transpose circuit and assigned to the same coefficient slots. The auxiliary scalar remains independent and unused here.


## Amendment C7

Put \(A_H=\mathrm{base\_left}\), \(B_H=\mathrm{base\_right}\), and \(u=K_1/A_H\). The explicit floor equalities in the rule require integral \(A_H,B_H\). Together with the stated lower bounds they give positive integers \(A_H,B_H\) with \(A_HB_H=e\), \(K_1\ge A_H\) and \(A_H\mid K_1\), \(K_2\ge1\), and \(2B_HK_1K_2=n\). Thus \(h=2uK_2\). Left legs are \((a,i)\) with \(0\le a<u,\ 0\le i<A_H\). Right legs use blocks \(0\le b<K_2\) with kinds \(\mathrm E_j,\mathrm O_j,\mathrm V_j\) for \(0\le j<B_H\). Write \(\lambda_a\) for the ordinary left \(T\)-exponent, and \(p_X=1\) on O and \(0\) on E or V. On the mixed-base branch, and on the binomial one-variable branch with \(n\mid q-1\), take \(\lambda_a=2a\) and \(k_{\rm leg}=2ub+p_X\). On the binomial one-variable branch with \(n\nmid q-1\) and on the bounded seed branch, take \(\lambda_a=2K_2a\) and \(k_{\rm leg}=2b+p_X\). In both cases put \(k_c=\lambda_a+k_{\rm leg}\) and \(\iota=i+A_Hj\). In the first case the two digits of \((k_c-p_X)/2\) are the quotient and remainder of division by \(u\). In the other case they are the quotient and remainder of division by \(K_2\). Thus every required relative exponent appears once in its weight family under either choice. The weight is the coefficient of \(H^\iota T^{k_c}\) in \(U\) for E/O and in \(V\) for V. Euclidean division enumerates all the base coefficients through \((i,j)\) and all the half-indices through \((a,b)\). The parity kinds therefore cover precisely the required U and V coefficients. The key cell is \(a=i=b=j=0\), kind E. There are \(A_c=3B_HK_1K_2=3n/2\) cells and \(3B_HK_2\) right legs.

### Factor masks and scalar classes

Use the prescribed independent coins, with one nonzero \(s_X\) for each right kind. Independently sample uniform \(\upsilon_H\in\mathbb F_q\) and \(\varepsilon\in\mathbb F_q\setminus\{0,-1\}\). All independent scalar supports have size at least \(q-D\). Put
\[
 \pi_{a,i}=\pi\left(\upsilon^{\lambda_a}\upsilon_H^i+\varepsilon F_{\lambda_a,i}(\upsilon,\upsilon_H)\right),\qquad
 s_{\rm leg}=s_X\upsilon^{k_{\rm leg}},\quad
 \gamma_c=\pi_{a,i}s_{\rm leg},\quad \kappa=\gamma_{\rm key}L_\rho(\tau).
\]
The key factor has \(\pi_{0,0}=\pi(1+\varepsilon)\ne0\) since \(F_{0,0}=1\). On E/O take the right mask at the sampled scalar points to be
\[
 \upsilon^{k_{\rm leg}}\upsilon_H^{A_H j}(\eta_1z_0+\eta_2z_+)
 -\varepsilon^{-1}F_{k_{\rm leg},A_Hj}(\eta_2z_-+\eta_3z_0).
\]
On V take \(\upsilon^{k_{\rm leg}}\upsilon_H^{A_H j}(\eta_3z_+-\eta_1z_-)\). Call this vector \(\vartheta_{\rm leg}\). The clear factors at input coordinate \(v\) are \(\pi_{a,i}(y_v,A_v(\tau))\) and \((s_{\rm leg}(r_v+A_v(\tau))+\vartheta_{{\rm leg},v},s_{\rm leg}(B_v(\tau)-y_v))^\top\). Apply the original hidden-basis transform. Publish the left factors once, the right factors and search bases in both G2 sectors, and the remaining inputs prescribed in Amendment n1.

### Honest cancellation and three actual ties

For a stack let \(W_U,W_V\) be the corresponding matrix sums at ordinary powers \(H^{i+A_Hj}T^{k_c}\). Put \(\widetilde W_U^+=\sum_{c\in C_U}W_c F_{\lambda_a,i}F_{k_{\rm leg},A_Hj}\), whose image in \(F\) is \(\sigma^{n/2+1}(W_U)\) by multiplicativity. At degree zero in \(\varepsilon\) the left scale times right mask gives the following coefficients at the three original \(\eta_a\) after taking out \(\pi\):
\[
 t_1=W_Uz_0-W_Vz_-,\qquad
 t_2=W_Uz_+-\widetilde W_U^+z_-,\qquad
 t_3=W_Vz_+-\widetilde W_U^+z_0 .
\]
Specifically the negative E/O term is multiplied by the \(\varepsilon F_{\lambda_a,i}\) term, producing the raw product of the individually reduced monomials. On a witness replace each \(W_c\) by its weight and contract the forms with \(w\). The resulting \(t_a^w\) vanish in \(F\) by the honest product identities. In the mixed-base branch they have \(T,H\) degree bounds \((2h-2,2e-2)\) for \(a=1\) and \((3h-3-\kappa_T,3e-3)\) for \(a=2,3\), where
\[
 \kappa_T=2u-(q\bmod 2u).
\]
For those mixed-base bounds, the reduced monomial \(\sigma^{n/2+1}(H^iT^x)\) has \(T\)-exponent \(qx\bmod h\). The half-turn only multiplies \(T^x\) by a sign, and reduction of each \(T^h\) introduces a factor in the base field. Since \(q\) is odd, the transformed left exponent for \(x=2a\) is even and at most \(h-2\). On the right \(x=2ub+\mathbf1_O\), where \(b\) indexes a block. With \(2u\mid h\) the transformed exponent has residue either zero or \(q\bmod 2u\) modulo \(2u\), so is at most \(h-\kappa_T\). Thus the two twisted legs and the form have combined raw \(T\)-degree at most \(3h-3-\kappa_T\). Here \(1\le\kappa_T\le2u-1\le h-1\) by oddness and \(2u\mid h\), so the untwisted terms of degree at most \(2h-2\) fit the same bound.

For mode 0, use the polynomials \(P_H=H^e-d_*\), \(P_T=T^h-c_*(H)\). Reduce the coefficients of \(t=t_a^w\) modulo \(P_H\), writing \(t=P_HQ_0+\bar t\). Divide \(\bar t\) by \(P_T\) in \(F_0[T]\), where the remainder is zero, and lift the quotient to \(Q_T\) with \(H\)-degree below \(e\). The exact decomposition is
\[
 t=P_TQ_T+P_HQ_H,\qquad Q_H=Q_0+(\bar t-P_TQ_T)/P_H .
\]
Here the correction quotient is exact coefficientwise and of \(H\)-degree at most \(e-2\), since its numerator has \(H\)-degree at most \(2e-2\). Thus \(Q_H\) has \(H\)-degree at most \(e-2\) for the first tie or \(2e-3\) for the other ties. Its \(T\)-degree is no greater than the numerator bound. The \(T\)-degree of \(Q_T\) is at most \(h-2\) for the first tie or \(2h-3-\kappa_T\) for the other ties. Publish the rectangular power bases for each quotient multiplied by \(P_H\) or \(P_T\) with that tie's scalar \(\pi\eta_a/\zeta''\). This uses \((e-1)(2h-1)+e(h-1)\) slots for the first tie and \((2e-2)(3h-2-\kappa_T)+e(2h-2-\kappa_T)\) for each other one.

In the positive \(\varepsilon\) grades the reduced left, ordinary right and form \(H\)-degrees are at most \(e-1,e-A_H,e-1\), respectively. Their \(H\)-length is \(3e-A_H-1\). The right \(T\)-degrees are at most \(h-2u+1\), with a maximum one smaller on V. Using the even transformed left bound \(h-2\) and the fact that the positive \(\eta_3\) grade occurs only on V, the three \(T\)-lengths are \(3h-2u-1,3h-2u-1,3h-2u-2\). In the negative \(\varepsilon^{-1}\) grades use the ordinary left degrees \(2u-2,A_H-1\) and the degree bounds for the reduced right and the form. This gives \(T\)-length \(2h+2u-\kappa_T-2\) and \(H\)-length \(A_H+2e-2\) for each of the two negative grades. Publish those rectangles with their respective scalars \(\pi\eta_a\varepsilon^{\pm1}/\zeta''\). The total capacity per sector is
\[
\begin{aligned}
 C_{\rm mask}
 &= (e-1)(2h-1)+e(h-1)+2\big((2e-2)(3h-2-\kappa_T)+e(2h-2-\kappa_T)\big)\\
 &\quad +(3e-A_H-1)\big(3(3h-2u-1)-1\big)
       +2(A_H+2e-2)(2h+2u-\kappa_T-2)\\
 &=(54e-5A_H-31)h+(-10e+10A_H-2)u-29e-5A_H+22-(10e+2A_H-8)\kappa_T-5e+5A_H-1 .
\end{aligned}
\]

### Mode 1 cancellation and exact capacity

In mode 1 the extra grid condition is \(A_H=e,\ B_H=1\). In mode 0 the displayed grid rule is unchanged. In both modes \(h=2uK_2\) with \(u=K_1/A_H\), and the same relative parities and digit assignments give exactly one cell for each coefficient of \(U,V\). For mode 1, every right leg has base digit zero. The formulas for \(\pi_a,s_{\rm leg},\gamma_c,\vartheta_{\rm leg}\), the clear factors, hidden basis, and pairings are those just given, using the scalar-relative version of \(F_{s,\iota}\) from C6. Their grade-zero coefficient is the same list \(t_1,t_2,t_3\), so the change is to ordinary polynomial representatives and the rectangles needed to cancel them.

### One-variable capacity in the degree-one auxiliary branch

In the one-variable binomial branch, both auxiliary digits are zero. First suppose \(h=n\mid q-1\). Reducing \(T^{s q^j}\) by \(T^n-d_*\) gives a scalar multiple of \(T^s\) for each slot. Thus a product of the two leg powers always has degree \(k_c=2a+k_{\rm leg}\), whether either or both legs are conjugated. This is at most \(n-1\) on E/O and at most \(n-2\) on V. All forms have degree at most \(n-1\). The three grade-zero polynomials therefore have degree at most \(2n-2\), with exact division by \(T^n-d_*\) on a witness, and each quotient needs at most \(n-1\) powers. Increases in auxiliary degree do not occur because no term depends on the auxiliary indeterminate on this branch. The three positive grades have lengths \(2n-1,2n-1,2n-2\), the last one using only V. Each of the two negative grades has length \(2n-1\). The same scalar masks multiply the indicated monomial powers as in the earlier capacity proof. The full number of slots per sector is
\[
 3(n-1)+2(2n-1)+(2n-2)+2(2n-1)=13n-9 .
\]
These are the exact rectangular list lengths used in this branch, including a slot if the corresponding scalar evaluates to zero. The view proof isolates the same three grade-zero coefficients up to multiples of the relative modulus, since the published grade-zero cancellation bases are all multiples of \(T^n-d_*\) and the other bases have nonzero grades. Thus all three ties still hold on the actual stacks.

For \(n\nmid q-1\) in the one-variable branch the ordinary and conjugated left exponents are multiples of \(2K_2\) and at most \(n-2K_2\). This holds for the conjugate because \(2K_2\mid n\) and the exponent is reduced modulo \(n\). The ordinary right exponent is at most \(2K_2-1\) on E/O and \(2K_2-2\) on V, while the conjugated right exponent is at most \(n-1\). On an honest stack, the first grade-zero identity therefore has degree at most \(2n-2\). The second and third have degrees at most \(3n-2K_2-2\), the maximum of the bounds \(2n-2\) on their untwisted terms and \((n-2K_2)+(n-1)+(n-1)\) on the twisted term. Exact monic division gives a first quotient of length \(n-1\) and the next two of length \(2n-2K_2-1\). The three positive grades still have lengths \(2n-1,2n-1,2n-2\), using the conjugated left bound and the ordinary right one. The two negative grades use the ordinary left and conjugated right bound, so each has length \(3n-2K_2-1\). Their total is
\[
 (n-1)+2(2n-2K_2-1)+2(2n-1)+(2n-2)+2(3n-2K_2-1)
 =17n-8K_2-9 .
\]
The supports have nonnegative lengths since \(2K_2\le n\). Each slot uses the corresponding original scalar mask and the grade-zero bases are multiples of \(T^n-d_*\). Thus the same polynomial view imposes the same three actual identities. Replacing the order of the two relative digits preserves the independent scalar markers and the distinct monomials used to isolate all cells.

Put \(\iota_*=\lceil((q-1)\bmod n)/n\rceil\), which is 0 when \(n\mid q-1\) and 1 otherwise. For \(\mathrm{seed\_mode}=0\), the model and decryption use \(C_{\rm mask}=(1-\mathrm{scalar\_rel})C_0+\mathrm{scalar\_rel}\big(13n-9+\iota_*(4n-8K_2)\big)\), where \(C_0\) is the mixed-base capacity proved above.

For an arbitrary expression the tie coefficient at degree zero in epsilon is still the vector \(t_a\), because the two individually transformed monomials represent the Frobenius image of their ordinary product. The only degree-zero cancellation bases contain \(P_H\) or \(P_T\). The Laurent view proof below therefore imposes the same three field ties on the actual matrices in either mode. Its source types, distinct ordinary monomials, solver and extraction algorithms are unchanged. Its degree bounds use the common limits proved below. In the one-variable branch every altered representative has \(H\)-degree zero, the published mask bases have \(T\)-degree at most \(3h-3\), and the added cell-scale argument uses the selected digit placement. The recovery-point gradient polynomials still use the ordinary cell monomial as their grade-zero coefficient, so their separation and bounds continue to hold. Both modes have the same ring kernel and the three genuine field ties. The rank-three classification, including when the corner is zero, follows from the full argument below and uses no density condition to classify a passing tied stack of dimension at most three.

Since \(e\le16\) is bounded, base polynomial arithmetic has constant width, and the new public base construction and power table fitting take \(O(\log q+n)\) fixed field work. The auxiliary division is trivial in degree one. The relative monic division and coefficient convolution cancel the honest masks exactly for either relative digit placement. No additional MSM, pairing or witness sum is used. The remaining exponent counts, correctness combinations, protected sampler and security proof apply with the chosen capacity at the listed points. The amended asymptotic cost family in the following paragraph still uses mode 0. The size and time estimates under its hypotheses also hold in mode 1 because the same field degrees and counts serve as upper bounds there, and its fixed base arithmetic contributes only the bounded-width work just described.

In the first two field branches, every weighted product of two leg monomials has a single \(T\)-power and a coefficient of bounded \(H\)-degree. Accumulate one contribution per cell before multiplying by the appropriate witness form polynomial for each grade. The ordinary convolutions, coefficient reductions and binomial divisions cost \(O(n\log n)\) field operations. For the convolution, split each length-\(O(n)\) polynomial into a constant number of blocks of length at most \(n\); the products fit the power-of-two subgroup in C3 because \(2n\le D\). The binomial divisions themselves use fixed-width coefficients and block shifts. Evaluate these coefficients on the transmitted bases in one G2 MSM per sector and subtract its pairing against the witness-summed Y column. This cancels the masks exactly.

For every target identity the view below isolates \(t_1,t_2,t_3\) up to the indicated multiples of \(P_H,P_T\). These vanish in the field, imposing all three ties on the actual stack. The cells enumerate the full coefficient lists with no inactive positions. The rank-three classification then uses the same three consecutive Frobenius projections, and any form kernel vector has the equations in the selected C5 ring established in C6.


### Cancellation for the bounded seed modulus

In the added one-variable branch C7 requires \(2K_2\mid r_H\), \(K_2=14\), \(r_H=448\), \(q\bmod 448=321\), and checks the integer
\[
 R_*=n-r_H+\max_{0\le j<2K_2}(qj\bmod r_H).
\]
For the checked residue and right-leg count, the residue list in increasing index is 0, 321, 194, 67, 388, 261, 134, 7, 328, 201, 74, 395, 268, 141, 14, 335, 208, 81, 402, 275, 148, 21, 342, 215, 88, 409, 282, 155. Its maximum is 409, and C7 checks the stated sum. This is an upper bound on the reduced degree of every conjugated right leg. Indeed at Frobenius exponent \(n/2+1\), the half-turn changes only a sign, so the exponent in C6 can use one scalar Frobenius. All powers produced by that formula are no larger than \(n-r_H\) plus their residue modulo \(r_H\). As \(q\) is prime and \(r_H<q\), the residues of \(qj\) are distinct for the \(2K_2\) listed indices. Hence \(2K_2-1\le R_*\le n-1\), using \(r_H\le n\).

Use left exponents \(2K_2 a\) and right exponents \(2b+p_X\). Every ordinary or conjugated left exponent is a multiple of \(2K_2\), since \(2K_2\mid r_H\) and the reduced residue and every higher term have this divisor. Their maximum is at most \(n-2K_2\). Ordinary right exponents are bounded by \(2K_2-1\) on E/O and \(2K_2-2\) on V. This verifies the same cell-scale degree bound as in the exchanged binomial case. The first honest tie has degree at most \(2n-2\). The next two have degree at most \((n-2K_2)+R_*+(n-1)\), which is at least \(2n-2\) by the lower bound on \(R_*\). Dividing by the chosen monic \(P_T\) gives quotient lengths \(n-1\) for the first and \(n-2K_2+R_*\) for each of the next two. The remainders vanish as these are the honest ties. The three positive grades have lengths \(2n-1,2n-1,2n-2\) by the ordinary right and conjugated left bounds. Each negative grade has length \(2n-2K_2+R_*\) by the ordinary left and conjugated right bounds. In total the per-sector list has
\[
 C_{\rm seed}=13n-8K_2+4R_*-5
\]
slots. Each uses the usual independent scale for its \(\eta\) and epsilon grade. The three grade-zero lists evaluate multiples of the monic \(P_T\) and therefore impose all three field ties by the same view proof.

The model selects \(C_{\rm seed}\) in the new branch with the indicator \(\mathrm{seed\_mode}\), and the preceding \(C_{\rm mask}\) otherwise. The maximum relative degrees of the monic polynomial times a published quotient power and of the cross-grade powers are at most \(3n-3\), using \(R_*\le n-1\) and \(K_2\ge1\). Only the variable \(T\) is used in these lists. Thus their degree bounds and recovery gradient separation follow the same exchanged-case inequalities. The ordinary cell exponent \(2K_2 a+2b+p_X\) still occurs at degree zero in epsilon, so the coefficient isolation and row-space implications are unchanged.

In this branch the product of two individually conjugated legs has at most \(s_0^2\) powers, a bounded number. Append the accumulated weighted contributions to their ordinary polynomial positions in \(O(n)\) field work, then multiply these polynomials by the form polynomials using the same blocked convolution as above. For division or reduction by \(p_c(T^{r_H})\), group the terms by the exponent modulo \(r_H\). In each group divide the polynomial in \(T^{r_H}\) by the fixed monic bounded-degree \(p_c\). The group degrees are bounded because the input has degree \(O(n)\) and \(n=s_0r_H\). This is the unique monic division, and it costs \(O(n)\) work. As a result the same \(O(n\log n)\) field work bound covers the sparse branch, including weight construction, and it uses the same charged MSM, cancellation pairing and source counts. The old binomial calculation applies in the two preceding branches.

### Counts and asymptotics

The factor and cancellation arrays have the ranges stated in Amendment n1. The shared QAP lists and split bases in that section prove the amended \(n_1\) and \(n_2\). All listed exponents use one multiplication of their group generator before publication, with one additional GT multiplication for the oracle key. The ciphertext likewise has one GT element, seed and masked message. Group counts and the original asymptotic family are checked explicitly in Amendment n1, including both G2 sectors.

The witness sums use \(2K_1+1\) arrays in G1 and \(12B_HK_2\) arrays across both G2 sectors. Their model counts use the same witness-weight convention. The weighted factor combination in G1 has \(6B_HK_2K_1=2A_c\) points. The revised G1 quotient and pairing counts are proved in Amendments dec_msm_g1 and dec_pairings. The merged correction uses the shared power list and has the total MSM length proved in n1. The additional non-key linear combination in G2 is counted in Amendment dec_msm_g2. The scalar corrections after Comb operate on the same \(G_T\) elements as in the original algorithm. The unchanged centered sampler and search bound give the same `lem:range` and expected search. The argument for the search algorithm depends on \(\Psi,\Lambda'\) and its result only. One can search increasing intervals of radii \(4^j\) with steps of order \(2^j\); the geometric sum is \(O(\sqrt{|t|}+1)\) for the found result \(t\). With \(\mathbb E t^2\le(g\sqrt{(N+4)/48}+3/2)^2\), Jensen's inequality gives the stated expected work.

The number of QAP evaluations and ring products for computing all the forms at \(w\) is unchanged. In the mask calculations the three tabulated multipliers of Amendment C6 apply by the same linear combinations to the matrix coefficients. The altered QAP bases use a constant number of field operations per exponent from the same evaluated polynomials and scalar lists; the explicit original asymptotic work estimate below includes those operations. Both algorithms use the same \(k(\ell+1)\) seed queries and at most one key query.

The transposed ring-block evaluation from Amendment C6 is used for all admitted \(d_R\). Its total field cost is \(O(k(\ell+1)d_R\log(2d_R))\). In the first two branches, the ordinary polynomial convolutions in \(T\) for the form weights and masks have length at most \(2n\le D\). Perform them by power-of-two FFTs using the subgroup for \(D\) allowed by C3. The \(H\) width is constant, and the third branch uses the sparse reduction proved above. This gives \(O(n\log n)\) field operations for these convolutions and their subsequent reductions.

### Asymptotic costs on the admitted choices

Here are the costs with the asymptotic QAP choices \(J'=1\), \(\Delta=\nu\lfloor D/\nu\rfloor\) and \(J=\lceil U_*/\Delta\rceil\le4\), evaluation points in the subgroup from C3, \(N\ge\lambda^2\), and systems of linear size. Take \(K_1,K_2=O(\lambda)\), \(n=O(\lambda^2)\), \(d_R=\Theta(\lambda)\), group representation degrees bounded, and \(\log q=\Theta(\lambda)\), as in the original cost model. Either admissibility choice of I4 can be used. The ciphertext contains \(O(\lambda N)\) field elements, and the field work is \(O(\lambda^2 N/\log\lambda)\) for encryption and \(O(\lambda N\log\lambda)\) for decryption outside the search. The expected field work for the search is \(O(2^{\lambda/4}N^{1/4})\) for both choices.

For the grid and ring placement take \(e,A_H,B_H\) fixed in their permitted ranges, and choose \(u,K_2\) as powers of two each between \(\lambda/(16e)\) and \(\lambda/(8e)\) for sufficiently large \(\lambda\). Put \(K_1=A_Hu\) and \(n=2euK_2\). This is \(\Theta(\lambda^2)\), with \(2n\le N<D\). A power of two \(d_R=\Theta(\lambda)\) divides the product \(uK_2\) for sufficiently large \(\lambda\). For this asymptotic family take \(\mathrm{ring\_mode}=\mathrm{scalar\_rel}=\mathrm{seed\_mode}=0\) and use \(k=n/d_R-1\), under the same ring and QAP subgroup conditions. The relative degree \(h=2uK_2\) is a power of two; C6's prime-power test holds in the original power-of-two subgroup setting whenever \(h\mid q-1\). Here \(\Delta=\nu\lfloor D/\nu\rfloor\ge D/2\) because \(D\ge\nu\), and \(U_*<2D\) gives \(J\le4\). The grid scale chosen above gives \(n\le\lambda^2/32\), so \(\Delta\ge h+e+2\) for sufficiently large \(\lambda\). The full-rank choice retains the original inverse growth inequalities and restricts the range to \(g\le2^{20}\cdot2^{\lambda/2}\). This bound includes the original order of growth with a fixed constant, including the original numerical range at \(\lambda=100\). It never requires the dense lower bound on \(g^3\mu_{\rm tr}\). For example, the inverse conditions admit \(\mu_{\rm tr}=a\,2^{-2\lambda}\) and \(g=\lceil c\,2^{\lambda/2}\rceil\) at compatible fixed constants \(0<a<1\), \(c<4\) with \(ac^4>1\). Then \(g^{-4}<\mu_{\rm tr}\), \(g^4\mu_{\rm tr}>\xi_{\rm tr}\) for all sufficiently large \(\lambda\), and the original third height bound is \(O(g)\). This verifies range compatibility. For example, in a family with \(N\) polynomial in \(\lambda\) and \(q\ge2^{(2+\delta_0)\lambda}\) for fixed \(\delta_0>0\), choose \(\varepsilon_{\rm tr}=\mu_{\rm tr}/1000\), \(R_{\rm tr}=O(\sqrt\lambda)\) large enough for (I2), and \(b=\lfloor\log_2 g\rfloor\). The prescribed lower bounds permit polynomial \(\Lambda_d\), bounded \(P_1,P_2,A_{\rm inv},\Gamma_3\), and polynomial \(\Gamma_1,\Gamma_2\): taking the indicated \((b-1)\)-th roots makes all exponentially growing right-hand sides bounded. Then \(H_1\le {\rm poly}(\lambda)2^{3\lambda/2}\), \(H_2\le{\rm poly}(\lambda)2^\lambda\), and \(H_3=O(g)\). The height products in (I5) are at most \({\rm poly}(\lambda)2^{2\lambda}\), and its \(\Lambda_d\Gamma_d<\mu_{\rm tr}q\) bounds follow from \(\mu_{\rm tr}q\ge a\,2^{\delta_0\lambda}\). A large fixed multiple of \(q^{2/3}g^{1/3}\) for \(\beta\) satisfies (I6) for sufficiently large \(\lambda\), because its growth dominates the rank-one and rank-two requirements, and (P4) follows from \(\beta^4/q^3=O((g^4/q)^{1/3})\). The subgroup and generic ledger conditions are separate premises as in the original corollary. The cost statement is for admitted instances under the displayed growth choices. The growth calculation describes the rates in the inverse inequalities of the cost model. The numerical challenge keeps its fixed prime, security exponent, and original ceilings, including \(g<2^{254}\). The cost assertion is a uniform implication for admitted instances with the stated cost hypotheses.

For the asserted costs, \(D=O(N)\) in the stated coset construction since \(F_{\max}n_{\mathsf c}=O(N)\) and the chosen power-of-two coset size is at most \(2F_{\max}\). Each factor list has \(O(\lambda N)\) entries, and each added cancellation list has \(O(n)\) entries, as derived from its exact lengths. The power, quotient and remainder arrays add \(O(D+n)\). Bounded group representation degrees give the size bound. The ring work is
\[
 O(k(\ell+1)d_R\log(2d_R))=O(\lambda N\log\lambda),
\]
because \(k<n/d_R=O(\lambda)\) and \((\ell+1)d_R\le N+2d_R=O(N)\). Both choices admit this ring growth. The numerical objective uses its protected matrix coefficient charge. On a scalar ring the block operation is a single field product.

For each of the \(O(\lambda N)\) generator multiples, fixed-base batching splits its \(O(\lambda)\) bit scalar into windows of width \(\lfloor\log_2\lambda\rfloor\) for large \(\lambda\). In each window precompute all \(2^w\) multiples of the shifted generator by repeated addition, and advance the generator to the next window by \(w\) doublings. The total preprocessing costs \(O(\lambda 2^w/w+\lambda)=O(\lambda^2/\log\lambda)\) group additions. Each requested multiple then costs at most one addition per window. The model therefore uses \(O(\lambda^2 N/\log\lambda)\) field operations for the group work, which also bounds the stated field preprocessing and polynomial operations. Outside the search, the derived counts give \(O(\lambda)\) pairings, \(O(\lambda N)\) group additions, and \(O(N)\) MSM entries. With the original cost of \(O(\lambda)\) field operations per pairing or variable scalar multiplication, and the field work for the ring and polynomial operations, this fits \(O(\lambda N\log\lambda)\).

In the original search equation the bounded sign-class algorithm still finds the same centered integer. The range lemma gives its squared-moment bound \((g\sqrt{(N+4)/48}+3/2)^2\). The outward interval algorithm described above and Jensen's inequality give \(O(\sqrt g\,N^{1/4})\) expected field work. Both admitted choices imply \(g^2\le2^{40}\cdot2^\lambda\). Hence \(\sqrt g\le 2^{10}2^{\lambda/4}\), with an absolute factor independent of the parameters. This gives the original expected search bound \(O(2^{\lambda/4}N^{1/4})\) on the entire amended domain. The dense choice's lower guard and the amended ledger imply \(1<g^3\mu_{\rm tr}<2^{61-\lambda/2}\), so that choice can occur only for \(\lambda<122\). The full-rank choice permits the original asymptotic parameter scales and the same cost analysis covers every admitted dense finite parameter. Thus no cost conclusion requires evaluating either construction outside its admissible domain.


### Algebraic and reduction interfaces

In `lem:moore`, the field has degree \(n\) and \(z\) plays no role in the statement. To derive the property at the amended degree, if a combination of \(d\) successive Frobenius columns is zero then a polynomial \(\sum_{j=0}^{d-1}a_j X^{q^j}\) vanishes at the entries of \(\sigma^s(h)\). Its roots are closed under \(\mathbb{F}_q\)-linear combinations, and the independent entries give \(q^d\) distinct roots. If any coefficient is nonzero, its degree is at most \(q^{d-1}\), a contradiction. This proof uses only the field and its Frobenius.

Here is the full classification argument for the actual field ties of Amendment C7 with the specified \(z\). Let \(W_c\) be symmetric, pass the Booleanity tests, and satisfy the original three ties, with row space \(\mathcal V\) of dimension \(d\le3\) containing no kernel vector. The zero-dimensional case has zero stack. Let the columns of \(U_*\) over \(\mathbb F_q\) be a basis of \(\mathcal V\), with rows \(u_i^\top\). These rows span \(\mathbb F_q^d\). For \(s\) in \(\mathcal I_*=\{n/2-1,n/2,n/2+1\}\), put \(h_s=U_*^\top\sigma^s(z)\), and put \(h_0=U_*^\top z\). Injectivity of \(z\) on \(\mathcal V\) means the entries of \(h_0\) are independent over \(\mathbb F_q\). In particular \(d\le n\), and the Moore property proved above gives that the three \(h_s\) span over \(\mathbb F_{q^n}\). Write \(W_s\) for \(W_U,W_V,\sigma^{n/2+1}(W_U)\) in the indicated order. Each \(W_s\) has its rows and columns in the extension of \(\mathcal V\), so \(W_s=U_* X_s U_*^\top\) for a unique symmetric \(X_s\). Indeed a left inverse \(L_*\) of \(U_*\) exists, and \(X_s=L_*W_sL_*^\top\); projections back to \(\mathcal V\) act identically on the columns and rows. The ties give \(X_s h_{s'}=X_{s'}h_s\). If \(\sum_s a_sh_s=0\), then \((\sum_s a_sX_s)h_{s'}=0\) for every \(s'\), and spanning gives \(\sum_s a_sX_s=0\). Thus there is a linear map \(X\) with \(X(h_s)=X_s\). The trilinear form \(C(h,u,v)=u^\top X(h)v\) is symmetric in the last two slots and in the first and last slots by the ties, initially on spanning \(h_s\) and then on all vectors by linearity. It is therefore fully symmetric. Each Booleanity test gives \(C(h,u_i,u_i-u_0)=0\) on the spanning \(h_s\), hence on all \(h\). The identities \(X_s=\sigma^s(X_{n-s})\) for \(s=n/2-1,n/2\) follow from the relation between the first and third matrices and because \(W_V\) has even \(T\)-degrees and \(\sigma^{n/2}\) fixes \(H\), as \(U_*\) and \(L_*\) have field entries fixed by \(\sigma\).

First suppose \(u_0\ne0\). Extend \(l_0=u_0\) to a basis \(l_0,\ldots,l_{d-1}\) chosen from the rows. For each \(\delta\in\{0,1\}^{d-1}\), let \(p_\delta\) satisfy \(l_0^\top p_\delta=1\), \(l_j^\top p_\delta=\delta_j\) for \(j>0\), and set \(w_\delta=U_*p_\delta\). Symmetry lets any repeated positive index in \(C(l_i,l_j,l_k)\) be reduced via the test replacing one occurrence by \(0\). Hence those values depend only on the set of positive indices present. Conversely the cube of the linear functional \(p_\delta\) takes the value \(\prod_{i\in A}\delta_i\) for this set \(A\), and all sets occur since \(d-1\le2\). The matrix of these values indexed by \(A,\delta\) is invertible: indexing \(\delta\) by its support gives the subset-incidence matrix, triangular with diagonal 1 in any inclusion-compatible ordering. Therefore
\[
 X(h)=\sum_\delta c_\delta(h^\top p_\delta)p_\delta p_\delta^\top
\]
for coefficients in the extension field. The squares \(p_\delta p_\delta^\top\) are independent by the same evaluation matrix, now on pairs of basis vectors since \(d-1\le2\). Write \(z_\delta=z(w_\delta)=h_0^\top p_\delta\ne0\). Comparing coefficients of the squares in \(X_s=\sigma^s(X_{n-s})\) gives \(c_\delta\sigma^s(z_\delta)=\sigma^s(c_\delta)z_\delta\) for the two consecutive \(s\). Hence \(c_\delta/z_\delta\) is fixed by \(\sigma\) and belongs to \(\mathbb F_q\), as the fixed points of \(x\mapsto x^q\) are exactly this field. Write it as \(\chi_\delta\). Returning from the matrix restriction gives \(W_s=\sum_\delta\chi_\delta z_\delta\sigma^s(z_\delta)w_\delta w_\delta^\top\). In particular the first two polynomial representatives give the stack \(\sum_\delta\chi_\delta\mathbf H(w_\delta)\).

Let \(f\) be any field-linear test that vanishes on the cells. It vanishes on the \(W_s\). Put \(Q_*=\sum_\delta\chi_\delta f(w_\delta w_\delta^\top)p_\delta p_\delta^\top\), a matrix over \(\mathbb F_q\). The vanishing gives \(h_0^\top Q_* h_s=0\) for all three \(s\), hence \(h_0^\top Q_*=0\). Independence of the entries of \(h_0\) over \(\mathbb F_q\) implies \(Q_*=0\), so independence of the squares implies \(\chi_\delta f(w_\delta w_\delta^\top)=0\) for every \(\delta\). Apply this to all Booleanity tests to deduce that any nonzero coefficient is on a Boolean assignment. If every constraint test passes, apply the same argument to them to see that each supported assignment is a witness. In any representation by honest stacks of Boolean assignments in \(\mathcal V\), the assignments equal some \(w_\delta\) because their evaluations on the chosen basis fix their \(p_\delta\). Hence the same test argument applies to any such representation.

If \(u_0=0\), take any basis \(l_1,\ldots,l_d\) from the other rows. Booleanity implies \(C(h,l_i,l_i)=0\), so by symmetry every coordinate of the trilinear form with a repeated index vanishes. This gives zero if \(d<3\). For \(d=3\) its only possible value on distinct indices is a shared scalar \(c\). Evaluating \(X_s=\sigma^s(X_{n-s})\) on pairs of different basis vectors gives \(c\, h_s=\sigma^s(c)h_0\) in the basis \(l_1,l_2,l_3\), since \(h_s\) is obtained from \(h_0\) by Frobenius and the basis is over \(\mathbb F_q\). If \(c\ne0\), the first two consecutive vectors \(h_s\) would both be proportional to \(h_0\), impossible by the Moore independence of the three vectors in dimension three. So again \(X=0\), and the stack vanishes. This proves the classification clauses, including that a nonzero usable stack in the stated case has a witness in its row space.

For `lem:heavy`, its rank and inverse-theorem arguments use the sampler and \(v_0=0\), the latter from the kernel identity. For part (c), an integer short multiple \(x\) of \(v\) has \(x_0=0\) because \(v_0=0\) and \(|x_0|<q\). Coordinate packing commutes with reduction and with field scaling. The matrix \(A\) therefore annihilates \(\hat x\bmod q\) by the kernel identity. The representation of \(\hat x\) includes every coordinate \(1\) through \(N\) once and pads only with zeros, so \(0<\|\hat x\|_\infty=\|x\|_\infty\le\beta\). The MSIS challenge, the infinity norm and the bound being costed are those of the model.

### Degree, view, and the recovery gradients

Fix \(M\), hence the coefficients of the protected \(z\), and treat all scalar coins as indeterminates. Use the two sectors \(\mathsf s\in\{\mathrm{plain},\alpha\}\) with factors \(a_{\rm plain}=1,\ a_\alpha=\alpha\). There is also a possible \(\alpha^2\) part in a target expression. Let \(\mathcal X_1\) and \(\mathcal X_2\) be the two lists of source-group inputs including their generators. Write \(a(\mathbf c,r)\) for the scalar exponent of a label from \(\mathcal X_1\), and likewise for \(b\) from \(\mathcal X_2\). A target expression has value \(\sum_{a,b}D_{ab}a(\mathbf c,r)b(\mathbf c,r)+D_K\alpha\kappa\), with field coefficients \(D_{ab}\) and \(D_K\). Coefficients of a fixed expression do not depend on any of these indeterminates, even when distinguishing two evaluations of the same expression.

For the proof, separate the homogeneous degrees \(j=0,1,2\) in \(\alpha\). Strip the explicit factor of \(\alpha\) from the new G1 copies and from each alpha G2 label. For a pair of underlying plain inputs, in each degree \(j\) sum the coefficients of all pairs that strip to those inputs and that originally contributed degree \(j\). The resulting coefficient representation is an identity in every coin and search coordinate, including at the private evaluation points. In degrees zero and one the pair products after stripping therefore have exactly the same scalar types as in two sectors with alpha carried entirely on G2. In degree one, a pair with the G2 generator may also be present, but it has a G1 input of type \(\zeta\tau^v\) and no search coordinate. In degree two every G1 input before stripping was a new alpha copy of type \(\alpha\zeta\tau^v\). None of the alpha G2 labels has inverse scale \(\zeta^{-1}\). In particular the degree-two part has no terms in the key-scalar multidegree \((\deg_\pi,deg_\zeta,\deg_{\zeta'},\deg_{\zeta''})=(1,0,0,0)\) and has no \(F_1\)-right-factor or \(F_2\)-right-factor coefficients. The optional extra G2 generator slot is identified with the existing plain generator in this representation.

Put \(\varpi=\Omega_{22}\zeta\zeta'\zeta''\varepsilon\). This clears denominators in each term of the value because G1 exponents have none and the published G2 exponents have only the inverses in \(\varpi\), each to the first power. We now check the bound on the cleared degree. A left-leg scalar \(\pi_a\) has total degree at most \(h+e\): the reduced monomial has \(T\)-degree at most \(h-1\), \(H\)-degree at most \(e-1\), and is multiplied by \(\pi,\varepsilon\). The ordinary monomial term is within that bound by \(2u\le h\) and \(A_H\le e\). The G1 factors cost at most \(D\) further degrees. The non-sparse QAP powers have degree at most \(\Delta\). A sparse power or its shifted copy has degree at most \(D\) with its scale and \(D+1\) with alpha, both within \(D+h+e\). The Y column has degree two. Use \(d_1=\max\{D+h+e,\Delta\}+1\).

Every \(k_{\rm leg}<h\) by \(2uK_2=h\), so the leg-scale degree is at most \(h\). For \(e\ge2\) the cell scale has degree at most \(2h+e\le n+2\) since \((e-2)(h-1)\ge0\). In the binomial case \(e=1,n\mid q-1\), each conjugate keeps the slot exponent, so the cell scale has degree at most \(k_c+3\le n+2\). In the exchanged binomial case and in the bounded seed case, each ordinary or conjugated left exponent is at most \(n-2K_2\), and the ordinary right exponent is at most \(2K_2-1\), so the cell scale again has degree at most \(n+2\). The key scale has degree three. The cleared sparse bases have degree at most \(D+n+8\). For a non-sparse base the polynomial part has degree at most \(N+2+(J-1)\Delta\), and the cell scale, alpha copy and four residual clearing factors add at most \(n+7\) total. Thus the bound is \(N+n+9+(J-1)\Delta\le2D+n+5\), using \((J-1)\Delta<U_*=(D-1)+\nu n_{\mathsf c}\) from P1. The right-coordinate QAP part fits \(D+h+6\). The right masks combine a leg monomial and a form, each of \(T\)-degree at most \(h-1\) and \(H\)-degree at most \(e-1\), with an independent scale. Their cleared degree is at most \(2h+2e+3\), and search bases fit \(h+6\).

Cancellation powers including \(P_T\) or \(P_H\) have \(T\)-degree at most \(3h-3\) and \(H\)-degree at most \(3e-3\). Each needs at most eight more degrees from \(\pi\), one mask scale, one grade power, alpha and four residual clearing factors. These therefore fit \(3h+3e+2\le D+n+7\) because \(D\ge2eh\) and \(e,h\ge2\) in the larger auxiliary branches. When \(e=1\), the same inequality is \(3n+5\le D+n+7\), which follows from \(2n\le D\). Every cleared G2 exponent therefore fits \(d_2=2D+n+6\). The cleared key degrees are at most \(D+8,D+7\). The amended P1 gives \(\Delta\le D\), hence \(d_1=D+h+e+1\). Thus
\[
 d_1+d_2\le3D+n+h+e+7.
\]
For \(e,h\ge2\), \(h+e\le eh=n\), so this bound is at most \(3D+2n+7\). For \(e=1\) it is \(3D+2n+8\). Both cases, the separate source and key bounds, and a possible guessed-operand factor of one more degree lie within \((q-D)\varepsilon_f\) by \(K_1\ge1\) and the protected formula (and the same bound \(d_f=3D+2n+2K_1+7\) holds before that extra factor).

For fixed \(r\), the independent valid scalar-coin ranges each have size at least \(q-D\); for \(\varepsilon\) this uses the two excluded values and \(D\ge2\), and for \(\tau\) the excluded \(D\) evaluation points. The clearing factor is nonzero there. By (P5), \(24\varepsilon_f\le E(2)\le 2^{-\lambda}\), so \(d_f<q-D\) because \(\varepsilon_f=(d_f+60)/(q-D)\). The independent-coordinate polynomial root bound, proved in Targets, now has two consequences. If \(D\) has value \(\chi\kappa\) for all valid coins at a fixed \(r\), the cleared polynomial is identically zero in the coin indeterminates. Otherwise the coincidence probability is at most \(d_f/(q-D)\le\varepsilon_f\). In the first case we can compare coefficients before clearing as identities in Laurent polynomials in the nonzero scalar indeterminates.

We next prove the coefficient-vanishing property needed for recovery. With \(\ell_{j,1}^{\rm leg}\) the first entry of the untransformed right factor, its two transformed exponents in sector \(\mathsf s\) are
\[
 a_{\mathsf s}\left(\ell_{j,1}^{\rm leg}
       -\frac{\Omega_{12}}{\Omega_{22}}s_{\rm leg}(B_j(\tau)-y_j)\right),\qquad
 a_{\mathsf s}\frac{s_{\rm leg}(B_j(\tau)-y_j)}{\Omega_{22}}.
\]
The exponent \(\ell_{j,1}^{\rm leg}=s_{\rm leg}(r_j+A_j(\tau))+\vartheta_{{\rm leg},j}\) is independent of the hidden basis. The two left exponents are \(F_1^{k_1,i}=\pi_{k_1}y_i\) and \(F_2^{k_1,i}=\pi_{k_1}(\Omega_{12}y_i+\Omega_{22}A_i(\tau))\). No other G1 exponent involves \(\Omega_{12},\Omega_{22}\), and the other G2 exponents also do not. Let \(\widetilde a\) be the part of the exponent of \(a\in\mathcal X_1\) at \(\Omega_{22}=0\). Its value for \(a=F_2^{k_1,i}\) is \(\Omega_{12}F_1^{k_1,i}\).

Assume the target identity holds at a fixed \(r\). Its right-hand side, including the separate \(D_K\alpha\kappa\) term, is independent of the hidden basis. Take the terms with \(\Omega_{22}^{-1}\) and positive degree in \(\Omega_{12}\). From the first right coordinate every left input contributes \(-\Omega_{12}\widetilde a\) times \(a_{\mathsf s}s_{\rm leg}(B_j-y_j)/\Omega_{22}\). From the second right coordinate only left inputs of type \(F_2\) contribute positive degree in \(\Omega_{12}\); there the contribution is \(+\Omega_{12}F_1^{k_1,i}\) times the same factor. Define \(\delta_{\mathsf s,a,{\rm leg},j}\) to equal \(D_{a,(\mathsf H_{{\rm leg},j,1})^{\mathsf s}}\), minus \(D_{F_2^{k_1,i},(\mathsf H_{{\rm leg},j,2})^{\mathsf s}}\) when \(a=F_1^{k_1,i}\). After cancelling the common nonzero formal factor \(-\Omega_{12}/\Omega_{22}\), the isolated identity reads
\[
 \sum_{\mathsf s,a,{\rm leg},j}
 \delta_{\mathsf s,a,{\rm leg},j}\,
 a_{\mathsf s}\,\widetilde a\, s_{\rm leg}(B_j(\tau)-y_j)=0.
\]
For any fixed \(j_0\), differentiate formally in \(y_{j_0}\) and substitute \(y=B(\tau)\). Terms from differentiating \(\widetilde a\) vanish, leaving
\[
 \sum_{\mathsf s,a,{\rm leg}}
 \delta_{\mathsf s,a,{\rm leg},j_0}\,
 a_{\mathsf s}\,s_{\rm leg}\,\widetilde a\big|_{y=B(\tau)}=0 .
\]

To see that every coefficient in the last sum is zero, its left-input values \(\widetilde a|_{y=B(\tau)}\) fall into the disjoint types
\[
 1,\quad \zeta\tau^v,\quad \zeta'\tau^v,\quad
 \zeta'' B_i(\tau),\quad
 \pi_{k_1}B_i(\tau),\quad
 \Omega_{12}\pi_{k_1}B_i(\tau).
\]
Here \(v\) ranges over the respective published powers. Each type has a distinct multidegree in \(\zeta,\zeta',\zeta'',\pi,\Omega_{12}\). The factors \(1,\alpha,\alpha^2\) separate the three degrees, with coefficients aggregated in each as above. For any of the first four types, \(s_{\rm leg}=s_X\upsilon^{k_{\rm leg}}\) separates legs by \(s_X\) and exponent; within a leg the powers \(\tau^v\) are distinct and the polynomials \(B_i\) are independent by \(B(d_j)=e_j\). In the last two types, isolate the constant term in \(\varepsilon\) of \(\pi_{k_1}s_{\rm leg}\). Up to the distinct \(\Omega_{12}\) factor for the last type it is \(\pi s_X\upsilon^{\lambda_a+k_{\rm leg}}\upsilon_H^{i_*}\), where \(i_*\) is the left base index. The left index \(k_1=(a,i_*)\) and the right leg are determined by the kind \(X\), the ordinary \(T\)-exponent and the \(H\)-exponent \(i_*\), by C7. Again \(B_i\) are independent. Thus all \(\delta_{\mathsf s,a,{\rm leg},j_0}=0\). This gives both conclusions simultaneously: the coefficients pairing \(F_2\) with the second right coordinate equal those pairing the corresponding \(F_1\) with the first, and the coefficient of the first right coordinate paired with any other G1 input is zero.

For the remaining view properties, group the expression into homogeneous classes in \(\pi,\zeta,\zeta',\zeta''\), and the joint degree in \((\Omega_{12},\Omega_{22})\), and separate the three powers of \(\alpha\). The class of \(\chi\kappa-D_K\alpha\kappa\) has degree one in \(\pi\) and zero in the other class coordinates. Among pairs in this class, the left first coordinates pair with the right first coordinates, search bases, and the plain generator. The left second coordinates pair with the right second coordinates. The two QAP power lists pair with bases having the matching inverse scale degree, and the Y column pairs with the cancellation bases. These are all possibilities: the five types of nonzero class coordinates on the G1 side are the linear degree in \(\pi\), degree in \(\pi\) together with positive hidden-basis degree, and degree in exactly one of \(\zeta,\zeta',\zeta''\). G2 exponents of the appropriate complementary degrees are precisely the listed types. Treat a pair of generators as being in the plain sector. In degree two there are no products in this class, as shown above. Any extra degree-one product with the G2 generator from a scaled G1 quotient power has nonzero degree in the quotient scale and is outside the class. In each sector the sum of this class has value \(a_{\mathsf s}\chi_{\mathsf s}\kappa\), with \(\chi_{\rm plain}=\chi\), \(\chi_\alpha=-D_K\).

Define \(W_c\) by the \(F_1,\mathsf H_1\) pairing coefficients in this sector, and \(u_c\) to be the negatives of the \(F_1,\mathsf S\) pairing coefficients. The matched \(F_2,\mathsf H_2\) terms cancel the hidden-basis part. Divide the class identity by \(a_{\mathsf s}\). Using the product of the two untransformed factors, its left side is \(\sum_c\gamma_c b_c+\Phi_*\) with
\[
 b_c=y^\top(W_c r-u_c)
      +y^\top(W_c-W_c^\top)A(\tau)
      +(P_{W_c}+h_cZ_c+Z_0R_c)(\tau).
\]
Here \(h_c,R_c\) are obtained from the two kinds of correction bases published in Amendment n1. A cell's sparse correction already contains \(Z_c\). The non-sparse correction is \(Z_0 T_c\) where the exponents of \(T_c\) are in nonzero residue classes modulo \(\nu\), since each chunk starts at a multiple of \(\nu\). Reduce \(T_c\) modulo \(Z_{\mathcal K}=Z_*/Z_0\), whose exponents are multiples of \(\nu\). By monic division the remainder \(R_c\) is allowed and the difference times \(Z_0\) is a multiple of \(Z_*\), hence of \(Z_c\). Absorb that quotient into \(h_c\). The term \(\Phi_*\) is the sum of the uncancelled masks, the pairs of the Y column with cancellation bases, and the pairs of first left factors with the generator. It is free of the \(3B_H\) independent \(s_X\). Isolating each monomial \(\pi s_X\upsilon^{k_c}\upsilon_H^{i_*}\), with \(i_*\) the cell left base index, at degree zero in \(\varepsilon\) gives \(b_c=0\) except at the key cell, where it gives \(b_c=\chi_{\mathsf s}L_\rho\). In both cases \(b_c\) contains no \(s_X,\pi,\upsilon,\upsilon_H,\varepsilon\), and distinct cells have distinct triples of kind, \(T\)-exponent and \(H\)-exponent. With these identities the original class identity also gives \(\Phi_*=0\).

In each cell the linear coefficient in \(y\) at \(\tau=d_0\), where \(A=0\), gives \(W_c r=u_c\). Then the same coefficient at \(\rho\) and at \(d_j\), where \(A=e_0\) and \(A=e_j-e_0\), implies \(W_c-W_c^\top\) annihilates a spanning set, so \(W_c\) is symmetric. The constant term in \(y\) shows \(\deg(h_c Z_c)\le2D-2\), since \(\deg P_{W_c}\le2D-2\), \(\deg(Z_0 R_c)\le D-1\), and \(\deg L_\rho<D\). Thus \(\deg h_c<D\) for a non-key cell, and \(\deg h_c<D-1\) for a key cell. The constant term in \(y\) for each non-key cell is the non-key QAP criterion of the protected QAP lemma with \(h,R\) equal to \(-h_c,-R_c\). In the key cell evaluate at \(\rho\), where \(Z_c=Z_0=0\), to get \((W_c)_{00}=\chi_{\mathsf s}\); then the constant term is the key QAP criterion. All cells therefore pass, and the plain key corner is \(\chi\). For the three \(\eta_a\) coefficients at degree zero in \(\varepsilon\) in \(\Phi_*=0\), the product masks are \(\pi y^\top t_a(\upsilon,\upsilon_H)\) from Amendment C7. The Y–tie-base contributions for each \(y_j\) are sums of multiples of \(P_T(\upsilon,\upsilon_H)\) and \(P_H(\upsilon_H)\). The cross grades have nonzero \(\varepsilon\)-degree and the generator contribution contains no mask scale. Equating the \(y_j\) coefficients and substituting the two field generators proves the three field ties for the actual usable stack.

The coefficient-vanishing property also implies that the difference in values between \(r'\) and \(r\) is
\(\sum_{\mathsf s}a_{\mathsf s}\sum_c\gamma_c y^\top W_c^{\mathsf s}(r'-r)\), where the sum uses only degrees zero and one. Degree two has no matched \(F_1\) coefficients, and its first-right-coordinate coefficients all vanish by the same Laurent differentiation on the aggregated coefficients. No other input depends on \(r\). It vanishes whenever all \(W_c^{\mathsf s}r'=u_c^{\mathsf s}\), proving the locus statement. With zero stacks the identity holds formally at every \(r'\), and the plain key corner forces \(\chi=0\). An identity holding formally for any \(\chi\) makes \(W_c^{\mathsf s}r\) constant for all \(r\), so all stacks are zero and again \(\chi=0\). For two source expressions that are formally different, pair their difference with the other source generator. This has zero stacks. If it vanished identically at even one \(r\), the just-proved locus statement would make the original source expressions formally equal. Hence it has the coincidence bound at each \(r\), proving the source clause of the view lemma as well.

For recovery, the derivative in \(r_j\) in any sector initially sums over every G1 input paired with the first coordinate of each right factor. By the proved vanishing, only \(F_1\) remains, producing \(a_{\mathsf s}\sum_{c,i}\gamma_c y_i(W_c^{\mathsf s})_{i,j}\). The same coefficient array is used at every private point, so this equation applies there even though the original identity was assumed at the actual search vector. To implement the private gradient with the original per-call loops, put only the first left-factor exponents into the G1 records at the gradient points, setting every other G1 input exponent there to zero. Keep the complete exponent lists, including all alpha copies, at the separate private test point. This projection is well-defined on formally equal G1 expressions: first set \(\Omega_{12}=\Omega_{22}=0\) in the G1 polynomial, then keep its homogeneous degree-one part in \(\pi\). Those operations retain exactly the first left coordinates. The G2 derivative record in each gradient pass still uses only the first right coordinates of that sector and ignores the other sector. In a target operation the derivative recurrence is linear, and for a pairing it multiplies this projected G1 value by the corresponding G2 derivative. There are no alpha G1 first factors, so the two derivative sets are exactly the degree-zero and degree-one matched terms above. For any marked identity they give the complete row-space gradients by coefficient vanishing, even when two placements of alpha had identical underlying pair products. A formally zero G2 difference also has zero gradient-record difference: pair it with any \(F_1\) input. The result is a formally zero target expression, whose stack is zero, and its first-right coefficients for that input are the tested coefficients. Formally equal targets have zero difference stack in every sector, so replacing equal labels in the record recursion preserves the projected gradients. It proves the row-space inclusion and, when the plain mark stack is zero, the vanishing of the plain gradients. This derivation and the degree and view arguments use the original form coefficients only through the degree of \(z\), the location of its mask terms, and the exact mask identity, all established above.

The reductions use the just-proved row-space gradient identity with the same degree and monomial separation. Programming the first \(\ell\) ring columns on the seed leaves the uniform challenge distribution exactly that of the original oracle calls, with the zero column independent and uniform. The private record difference detects a formally nonzero first marked expression except when its cleared polynomial vanishes at the test point. For each recovered sector, the kernel-combination test and LIFT are followed by the packing justified above. Targets gives the success probability and running-time use of these reduction steps.

The running time with the revised exponent lists has the bound
\[
 t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT},\qquad
 C_R=8I+3L+2C_{\rm post}+C_{\rm set}+C_{\rm desc},
\]
with \(I\) for computing the initial exponents at one point, \(C_{\rm post}\) for processing one tried expression, \(C_{\rm set}\) for fixed transcript initialization, and \(C_{\rm desc}\) for the description. Here \(I,C_{\rm post},C_{\rm set},C_{\rm desc}\) are the costs for the revised exponent lists, and \(C_R=O((N+n)D+\mu)\). We give the dependence on the form indices explicitly.

The per-call bound can be checked by the following implementation in the reduction's unit-operation model. Keep per group a table of assigned exponents indexed both by label and by field value, and a label table status for excluded strings. Both allocated and excluded strings are keys of the same label table, so unused-string sampling excludes both. A label record includes its value at the independent test point and a reference to its first expression node, if any. The reference or zero record is kept on repeated assignments. For an unclassified operand in an addition, scalar product or pairing, keep counters of the remaining exponents and unclassified strings in its group. Draw an integer uniformly below the latter count and compare it to the former count to decide membership. If it is a label, sample a uniformly unused exponent. Insert the relevant forward and reverse entries and update the counts. A rejection only writes its status and updates the unclassified-string count. This gives at most eight operations per unclassified operand: one status lookup, one integer sample and comparison, one exponent sample, two insertions and two counter updates. The conditional laws follow from a uniform injection after the already assigned and excluded labels have been fixed. Record-less labels in answered calls use the common zero expression, at most two further record writes per call.

For a result, allow at most 24 main operations. This includes two lookups of operands and up to three arithmetic operations each at the true and private test points. A result-label lookup, a fresh unused string sample when needed, and the two table insertions use at most four more. Updating both counts uses two. Allow six writes for an expression node (operation tag, operand references, scalar operands if needed, and result reference). The remaining four cover the private-value comparison, recording the first differing target pair, advancing the expression-log index, and checking or recording eligibility for name calls. A name call uses the same routine for negation, and then returns the two labels, with at most two label writes. It is rejected if the input's eligibility flag is absent. Repeated name calls return the already assigned opposite exponent label. An insertion at a known exponent leaves the old reverse entry in place and the private comparison uses its stored record.

For the six recovery passes, the forward evaluation at each point takes at most three arithmetic operations per logged gate. The private test point above uses the full exponents. At recovery points, the projected first-left values and the sector-specific first-right derivative leaves are prepared before the call loop as described above. Only the right operand of a pairing can contribute a derivative in \(r\), as every G1 value is independent of \(r\). For each of the at most two trial expressions, traverse the resulting straight-line expression log backwards. A sum or scalar multiplication adds the adjoint times the corresponding scalar derivative to the adjoint of each predecessor. A pairing uses the evaluated first operand as its derivative with respect to the second. For a predecessor that is an input leaf, skip it if its derivative is zero in the current sector. Otherwise it is a first right coordinate with derivative equal to one prepared field scalar times the coordinate vector for its index \(j\); directly accumulate the adjoint contribution times this scalar in coordinate \(j\) of the gradient. This is at most three field operations for each of two precursors: a product by the gate derivative, an additional product for a leaf, and an accumulation. A non-leaf involves just the first product and accumulation. The references in the stored log give direct accesses to indexed registers, and each field operation computes its result in its destination register. Neither uses a label-table lookup. Initialize all node adjoint registers to zero before each reverse pass, using one field write per node and pass, then set the starting adjoints for the trial. These updates compute the derivatives by the chain rule in reverse order. Each recovery point therefore costs at most \(3+2(6+1)=17\) operations per call for both expression trials. Initializing the output vectors and the at most two starting adjoints per trial is fixed postprocessing. Including six passes, the call bound is at most \(24+2\cdot 8+2+2+6\cdot17=146\le148\). A fresh key-oracle answer takes one lookup, sample and insertion. A fresh seed-oracle answer replaces its one sample by \(d_R\) coordinate samples. This gives \((d_R+5)Q_H\) when each oracle has at most \(Q_H\) queries.

Only fixed inputs and setup change. Computing the initial exponents at each of the eight points evaluates \(O(N)\) degree-below-\(D\) QAP polynomials, advances powers through lengths \(O(D+n)\), and forms the \(O(nD)\) scalars in the split QAP group arrays. For the mask vectors, naive transposed ring multiplication takes \(O(nd_R+nN)\) work, bounded by \(O(nD+nN)\) since \(d_R\le n\le D\). Source factor entries take \(O(nN)\) further operations. For postprocessing, apply the full form map to at most three vectors per sector by naive ring multiplication and solve a fixed-width linear system. The same \(O(nD+nN)\) bound covers this before LIFT. Initialization queries and stores the same ring entries and creates the group label records with at most \(O((N+n)D+\mu)\) operations, including masking. The fixed instance QAP polynomials and form indices fit the same size as advice in the protected cost model. Hence \(C_R=O((N+n)D+\mu)\). The lifting step is called at most twice, once per tried expression. This establishes the bound above and the stated \(t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)\) specialization.

This accounts for the background list for the forms and weights block. The generic record and mark bounds depend on the degree, view, sampler and label counts. The degree and view properties needed for the repacked construction are proved above. The extractor sketches only use the coefficient arrays of the left and right factors, independently of the internal representation of the form list.


## Amendment P1

Put \(U_*=(D-1)+\nu n_{\mathsf c}\), the number of absolute positions for the combined non-sparse correction. Require
\[
 \Delta\le D,\qquad J=\lceil U_*/\Delta\rceil,\qquad J'=1,\qquad \nu\mid\Delta,\qquad n\le D .
\]
The quotient correction has degree below \(D-1\) before multiplication by the coset vanishing polynomial of degree \(\nu n_{\mathsf c}\). Every combined term is therefore below \(U_*\), so these chunks contain all of them. Their largest shift satisfies \((J-1)\Delta<U_*\), and divisibility retains the residue classes modulo \(\nu\). The publication multiplies every shifted correction power by \(Z_0\) of degree \(N+2\). Consequently the largest shifted G2 product has unscaled polynomial degree at most \(N+2+U_*-1=2D-2\). The degree ledger in C7 below the field proof accounts for the scalar factors and gives the original polynomial root bound. The evaluation points, sampler and all other admissibility bounds retain their roles. The permitted remainder expression and the quotient degree used in the QAP tests are recovered by the monic division proved below. All security and correctness uses of the chunk and degree conditions thus hold under this version.

## Amendment n1

There are
\[
 n_1=(2K_1+1)(N+1)+4\lceil(D-1)/\nu\rceil+\Delta-\Delta/\nu
\]
transmitted G1 elements. Retain the setup, sampler, field kernels, factor masks and both sector values of C7. The following publication merges the non-sparse quotient and the remainder into one polynomial correction with an aligned exponent list.

### Publication and decryption

Use the same independent nonzero scales \(\zeta_0=\zeta,\ \zeta_1=\zeta'\). Put \(Z_*=(X-\rho)Z(X)=Z_0Z_{\mathcal K}\); \(Z_{\mathcal K}\) is the product of the coset vanishing polynomials \(X^\nu-\delta_t^\nu\) and belongs to \(\mathbb F_q[X^\nu]\). Set \(Z_c=Z_*\) for the key cell and \(Z_c=Z\) otherwise. Set
\[
 I_0=\{0\le a<D-1:\nu\mid a\},\qquad
 I_0^*=I_0\cup\{a+1:a\in I_0\},\qquad
 I_1=\{0\le a<\Delta:\nu\nmid a\}.
\]
Send the factor arrays and common Y column as in C7. Send \(P^0_a=[\zeta_0\tau^a]_1\) and \(P^{0,\alpha}_a=[\alpha\zeta_0\tau^a]_1\) for \(a\in I_0^*\), and \(P^1_a=[\zeta_1\tau^a]_1\) for \(a\in I_1\). The two subsets of \(I_0^*\) are disjoint since \(\nu\ge2\). For every cell send the sparse G2 base \(B^0_c=[\gamma_c Z_c(\tau)/\zeta_0]_2\) once, shared between sectors. For \(0\le j<J\) send both the plain and alpha copies of
\[
 B^1_{c,j}=[\gamma_c Z_0(\tau)\tau^{j\Delta}/\zeta_1]_2 .
\]
Send both sectors of the right factors, search bases and degree-zero and cross-grade cancellation bases, as before. If the total G2 count is odd, publish one repeat of the existing unit generator computed by a scalar multiplication by one. It is formally identical to the generator, so it introduces no extra generic expression. Keep the seed, target group element \([\alpha\kappa]_T\), and the message masked by \(H_{\sf key}([\kappa]_T)\). All listed published slots are scalar multiples of their generators.

For a witness \(w\), \(P_w=A_wB_w\) has the required values at \(d_j,d_0,\rho\), so \(G_w=(P_w-L_\rho)/Z_0\) is an exact monic division. The protected QAP identity gives
\[
 G_w=Z_{\mathcal K}h_{\rm key}+R_w,\qquad
 \deg h_{\rm key}<D-1,\quad \deg R_w<\nu n_{\mathsf c}.
\]
The allowed \(R_w\) contains no powers divisible by \(\nu\). If \(h^0\) is the part of \(h_{\rm key}\) on multiples of \(\nu\), the projection of \(G_w\) onto multiples of \(\nu\) is \(Z_{\mathcal K}h^0\), because multiplication by \(Z_{\mathcal K}\) keeps each residue of an exponent modulo \(\nu\). Recover \(h^0\) by exact monic division of that projection by \(Z_{\mathcal K}\) in the variable \(X^\nu\). The complementary projection \(T_w=G_w-Z_{\mathcal K}h^0\) has no exponent divisible by \(\nu\). Its degree is below \(U_*\). These polynomials can be computed with the same polynomial arithmetic as the original quotient/remainder computation. In particular apply the product to \(A_w,B_w\), subtract \(L_\rho\), and use fast monic division by \(Z_0\). The compressed sparse division is on polynomials of length \(O(D/\nu)\). To see its cost and that of the uncompressed division, reverse the divisor and use the inverse power series to solve for quotient coefficients to the required precision. The reversed monic polynomial has constant term one. Starting with inverse 1, the update \(u\leftarrow u(2-fu)\) doubles the correct precision since \(1-fu(2-fu)=(1-fu)^2\). Products use power-of-two subgroups from C3, splitting any length-\(O(D)\) polynomial into a bounded number of blocks of length at most half the subgroup order. Their total cost over doubling precisions is \(O(D\log D)\), and the point-value computation and evaluation ranges of the setup keep the original asymptotic bound. No extra interpolation of a remainder is required.

Use the same factor, search and cancellation group computations from C7. The group operands for subtracting the polynomial corrections are as follows. In each sector choose the applicable \(P^0\) list, plain or alpha, and form
\[
 H^0=\sum_{a\in I_0} [X^a]h^0\,P_a^0,\qquad
 H_{\rm oth}^0=\sum_{a\in I_0}[X^a]h^0\,P_{a+1}^0-\rho H^0+P_0^0/Z(\rho).
\]
The second expression is an MSM on \(|I_0|+2\) entries, including the existing \(H^0\) and \(P_0^0\). Independently of sector form
\[
 H_j^1=\sum_{\substack{a\in I_1\\j\Delta+a<U_*}}[X^{j\Delta+a}]T_w\,P_a^1
 \quad (0\le j<J),
\]
which can be shared because \(\nu\mid\Delta\). In the plain sector subtract the pairings of \(H^0\) with \(\xi_{\rm key} B^0_{\rm key}\), of \(H_{\rm oth}^0\) with \(\sum_{c\ne {\rm key}}\xi_c B^0_c\), and of \(H_j^1\) with \(\sum_c\xi_c B^1_{c,j}\) for every \(j\). In the alpha sector the sparse G1 operands are the scaled ones while the sparse right operands are shared, and the non-sparse right operands use the scaled copies of \(B^1_{c,j}\). As before, compute each sector's cancellation MSM in G2 and pair it with the shared witness-summed Y.

For the key cell the sparse pair gives its weighted \(Z_*h^0\). For each other cell the sparse pair gives its weighted \(Z_*h^0+L_\rho\), since \(Z(X)(X-\rho)=Z_*\) and \(Z/Z(\rho)=L_\rho\). In every cell the non-sparse pairings give its weighted \(Z_0T_w\). Their sum is \(Z_*h_{\rm key}+Z_0R_w\) in the key cell and \(Z_*h_{\rm key}+Z_0R_w+L_\rho\) elsewhere, under the cell's weight and scale. By the protected identities this is \(P_w-L_\rho\) in the key cell and \(P_w\) in the other cells. In the factors, the antisymmetric part cancels on the two witness inputs, and the mask correction cancels by C7. Thus the combined plain values are
\[
 \Lambda=[\xi_{\rm key}\kappa+r(w)\psi]_T,\qquad
 \Psi=[\psi]_T,\qquad \psi=y(w)\sum_c\gamma_c\xi_c(w).
\]
Every pairing in the second sector has exactly one alpha-scaled operand, giving \(\Lambda^\alpha=\alpha\Lambda\) and \(\Psi^\alpha=\alpha\Psi\). The same centered search and four final scalar multiplications give the original witness correctness of Targets, including the zero base and the event \(\xi_{\rm key}=0\). No sampler or search bound changes.

### Exact counts

The G1 factors and Y give \((2K_1+1)(N+1)\) elements. In the sparse arrays each sector has \(2|I_0|=2\lceil(D-1)/\nu\rceil\) distinct exponents. The complementary list has \(\Delta-\Delta/\nu\) elements. These give the displayed \(n_1\). Write \(A_c=3n/2\). The two right sectors give \(12B_HK_2(N+1)+6B_HK_2\) factor and search slots, plus \(2C_{\rm mask}\) cancellation slots. The shared sparse list has \(A_c\) elements and the non-sparse list has \(2J A_c\). Thus the G2 count including padding is twice the ceiling of half their sum. Every slot is computed by one fixed-base multiplication per generator, including the optional duplicate. The one GT element, seed, and masked message are unchanged. Encryption's scalar work for these lists consists of the same powers and products with the known scales, a constant number per slot.

Witness summation uses the same coordinate and right-leg arrays in both sectors. Weighted left factors use \(2A_c=3n\) G1 MSM points. The sparse computations use \(4|I_0|+4\) points across both sectors. The non-sparse G1 lists used on \(T_w\), counted once, contribute \(U_*-(|I_0|+n_{\mathsf c})\) points: the number of multiples of \(\nu\) strictly below \(U_*\) is \(\lceil U_*/\nu\rceil=|I_0|+n_{\mathsf c}\). Their sum is \(3n+D-1+3|I_0|+4+(\nu-1)n_{\mathsf c}\). The sparse right operands contribute one point per cell including the scaling at the key, shared over both sectors. The non-sparse right MSMs contribute \(2J A_c\), and the two cancellation MSMs contribute \(2C_{\rm mask}\). The pairing count in each sector is \(6B_HK_2\) for factors, \(3B_HK_2\) for search, two for sparse corrections, \(J\) for non-sparse corrections and one for cancellation. Accumulate the four sector target sums starting each with its first term, and use the same three final target additions and four scalar multiplications as in C7, giving the pairing count minus one additions. These counts use the protected witness weight convention and the already derived form and mask costs.

### Polynomial view

When a target identity holds, the degree classes in the independent scales isolate the two published power lists as in C7. The only G2 input having inverse scale \(\zeta_0^{-1}\) is the plain sparse basis at a cell. Every non-sparse correction input has inverse scale \(\zeta_1^{-1}\) and contributes a scalar multiple of \(Z_0(\tau)\tau^{j\Delta+a}\) within that cell for \(a\in I_1\). It has no exponent divisible by \(\nu\) in its polynomial factor after taking out \(Z_0\). Thus after summing the coefficients at each cell the correction is \(Z_c h_c^{\,0}+Z_0 T_c\) with no multiple-of-\(\nu\) monomial in \(T_c\). Divide \(T_c\) by \(Z_{\mathcal K}\). Both quotient and remainder have only nonzero residue classes, since the monic subtraction steps have shifts by multiples of \(\nu\) in all terms of \(Z_{\mathcal K}\). The remainder \(R_c\) has degree below \(\nu n_{\mathsf c}\) and is allowed. The difference \(Z_0(T_c-R_c)\) is a multiple of \(Z_0 Z_{\mathcal K}=Z_*\), hence of \(Z_c\), and is absorbed in \(h_c\). Thus the arbitrary correction has the required form \(Z_c h_c+Z_0R_c\). At a formal identity the constant-term comparison then forces the original degree bound on \(h_c\), as shown in the C7 view derivation. This recovers every original cell test and the key-cell corner. The coefficient matching, field ties, locus, gradients, extraction and probability bounds use the same other scale classes and are proved in C7 and Targets. The degree check in C7 accounts for the combined arrays on their entire admissible range.

## Amendment n2

The exact half-count is
\[
 n_2=6B_HK_2(N+1)+3B_HK_2+
 \left\lceil\frac{(3n/2)(2J+1)}2\right\rceil+C_{\rm mask}.
\]
This is \(\lceil S_2/2\rceil\) from Amendment n1 because the two cancellation lists add \(2C_{\rm mask}\) before rounding. The selected \(C_{\rm mask}\) is proved in C7 for all admitted field modes. The optional generator slot makes the transmitted count even.

## Amendment dec_sum_g2

The G2 sum bound is \(6B_HK_2(N+1)\). There are \(3B_HK_2\) right legs, two coordinates per leg and two sectors. Each sum uses at most \((N+1)/2\) additions in the stated regime. Amendments C7 and n1 specify these sums and their use in decryption.

## Amendment dec_msm_g1

The G1 length bound is \(3n+D-1+3\lceil(D-1)/\nu\rceil+4+(\nu-1)n_{\mathsf c}\). The first term is \(2A_c\) for the two weighted left factors per cell, shared between the sectors. The other terms are the sparse quotient points and combined non-sparse correction points derived in n1.

## Amendment dec_msm_g2

The G2 length bound is \((3n/2)(2J+1)+2C_{\rm mask}\). Amendment n1 proves the shared sparse quotient operands and the two independent cancellation MSMs, each of length \(C_{\rm mask}\). The count includes both sectors and uses the exact applicable capacity from C7.

## Amendment dec_pairings

The pairing bound is \(18B_HK_2+2J+6\). Each of two sectors uses \(6B_HK_2\) factor pairs, \(3B_HK_2\) search pairs, \(J\) non-sparse correction pairs, two sparse quotient pairs and one cancellation pair. The honest-combination proof is in C7 and n1.

## Amendment n

The model uses
\[
 n=k d_R+1+(1-\mathrm{ring\_mode})(d_R-1).
\]
Put \(p=1+(1-\mathrm{ring\_mode})(d_R-1)\). C5 admits only the two values 0 and 1. In mode 0 there are \(p=d_R\) leading slots and \(n=(k+1)d_R\). In mode 1 there is \(p=1\) leading slot and \(n=d_R+1\), since that mode requires \(k=1\). In both cases slot zero is \(v_0\), slots 1 through \(p-1\) are zero, and slots \(p\) through \(n-1\) contain all the original matrix-row coefficients in their original order. The placement and kernel identity are proved at the start of C6. The field coefficients vary according to the actual uniform matrices as proved in Targets. The field dimensions, admissibility and grid use the numeric \(n\), and therefore still contain every coefficient exactly once. Their full proofs and the three actual field ties in C6 and C7 do not assume anything further about the number of zero slots. The ring input dimension, reduction law and power-basis coefficient norm come from C5 and the proved kernel equivalence, so the original heavy-stack, lifting and target conclusions apply. The asymptotic family uses the original ring mode; the actual group counts and the fixed computational bounds proved in C7 hold for either choice.

## Targets

Fix any parameter set satisfying the amended model, the protected system shape, any admissible evaluation points, and the stated group and oracle models. In the chosen modes use the coefficient positions of Amendment n, the base field of Amendment C6 and the grid and masks of Amendment C7, and shared QAP encryption and decryption of Amendment n1. The amended inverse theorem applies by (P3) with Amendments I3, I4, H2, H3 and I6. The charged-mark bound is proved in Amendment Ncmp. The meanings of correctness, extraction, oracle access, adversary budgets and failure events are those of the original two theorems.

### Correctness with error \(2/q\)

Fix a witness \(w\). Conditional on the seed and the entries \(M_{i,j}\) with \(j\ge1\), the \(M_{i,0}\) are independent uniform ring elements because they are answers of the random oracle at distinct inputs. Since \(w_0=1\), adding \(\sum_{j\ge1}M_{i,j}\hat w_j\) to each \(M_{i,0}\) preserves this joint uniform distribution. In the monomial representation of the ring, its \(d_R\) coordinates are therefore independent uniform field elements, across all rows. Hence \(z(w)=1+\sum_{s=p}^{n-1}a_s H^{s\bmod e}T^{\lfloor s/e\rfloor}\), where \(p=1+(1-\mathrm{ring\_mode})(d_R-1)\) and the \(n-p=kd_R\) coefficients \(a_s\) are independent uniform scalars. The omitted slots \(1,\ldots,p-1\) are zeros. The key weight is the \(H^0T^0\) coefficient in the field representative of \(z(w)\sigma^{n/2-1}(z(w))\). It is of total degree at most two in the \(a_s\), since Frobenius is base-field linear, multiplication is bilinear, and taking a basis coefficient is linear. Its value at every \(a_s=0\) is 1, so the polynomial is nonzero.

A nonzero polynomial of total degree \(d_*\) in independent variables sampled uniformly from respective field subsets of size at least \(m\) vanishes with probability at most \(d_*/m\). In the final variable write it as a polynomial of degree \(j_*\) with nonzero leading coefficient of degree at most \(d_*-j_*\) in the earlier variables. By induction the leading coefficient vanishes with probability at most \((d_*-j_*)/m\). Where it is nonzero, at most \(j_*\) values of the final variable are roots, giving conditional probability at most \(j_*/m\). The one-variable bound follows by dividing out a linear factor for each root, and a nonzero constant has no roots. Applying it with \(m=q\) gives \(\Pr[\xi_{\rm key}(w)=0]\le2/q\).

If \(\xi_{\rm key}(w)=0\), the decryption algorithm returns \(\bot\). Otherwise the proved honest combination of the shared QAP construction yields \(\Lambda'=(r(w)-c_w)\Psi^\alpha\), and the unchanged range lemma gives \(|r(w)-c_w|\le B\). If \(\Psi^\alpha\ne0\), it has order \(q\), so \(2B+1<q\) gives a unique matching integer in \([-B,B]\), namely \(r(w)-c_w\). If \(\Psi^\alpha=0\), also \(\Psi=0\) because \(\alpha\ne0\), and the least absolute matching integer is zero. In both cases \(\Lambda-(c_w+t)\Psi=[\xi_{\rm key}(w)\kappa]_T\), hence after dividing by \(\xi_{\rm key}(w)\) the key is \([\kappa]_T\). The final XOR returns the original message. This proves precisely the failure event and the error bound of Theorem 5.6.

### Extraction and the reduction

Let \(\mathcal A\) have the budget \(Q<2^\lambda\) of generic group calls and at most \(2^\lambda\) queries to each oracle. Fix one bit \(b\) and messages \(m_0,m_1\), and run the extraction experiment with \(m_b\). The extractor reads the answered generic transcript without any oracle calls. It uses the two-sector sketches in the protected extractor block. It samples three independent probe vectors for each cell and sector, uses the linear combinations of source-group records and pairings to form sketches, tests the sketches of the result and the difference when there is an old record, and directly checks any candidate assignment against \(S\). In rank at most three, there are at most four assignments with first coordinate 1 to test: row echelon pivot coordinates determine the vector, pivot 0 must be present, and at most two remaining pivot choices are bits. Output is therefore always \(\bot\) or a witness. A record creation, result, or difference touches \(O(K_1N+n)\) field elements, since a source-group record uses at most \(K_1\) length-\((N+1)\) vectors or \(6A_c\) values, and the pairings compute six such combined sketch vectors. For a pairing, forming the inner products in the G2 record or summing per left leg and combining the G1 vectors uses \(O(K_1N+n)\) operations. A test uses \(O(N)\) for elimination with at most three rows and \(O(N+|S|)\) to generate and check the constant number of candidates. Initialization samples \(6A_c(N+1)\) field values, enters the \(L\) labels as records whose vectors are materialized on first use, and uses \(O(nN+L)\) time. There are at most four tests per result. Thus the extractor uses \(O((Q+1)(nN+|S|)+L)\) time because \(K_1\le n\) and \(N\ge1\).

The reduction on input a uniform \(A\in R_q^{k\times\ell}\) samples the seed, programs the seed oracle at that seed on matrix columns 1 through \(\ell\) using \(A\), and samples the other answers lazily, including the independent column 0. It samples encryption coins as specified, produces the ciphertext for \(m_b\), and simulates all generic labels and names and random oracles by the protected lazy tables. It runs \(\mathcal A\) once. The extraction steps use the answered generic transcript without its output or the random-oracle query transcript, while the lazy tables implement exactly the direct oracle law. Because the programmed entries are jointly independent uniform ring elements for uniform \(A\), all oracle answers including entries at the selected seed have exactly the joint law of the experiment. Private evaluation points are sampled independently of the run.

The reduction keeps records evaluated at its private test point, using the protected rules for guessed operands and for existing records. It tries the first GT result whose label has an existing record of different private value, using the difference expression, and also the target label's record if present. For each tried expression it computes three independent gradient vectors in each sector at private recovery points, tests their span for a kernel vector, using the plain sector first, and applies the unchanged LIFT algorithm if there is such a vector. An output from LIFT is a short multiple of that kernel vector. The coefficient of \(H^0T^0\) in \(z(v)\) is \(v_0\). All \(kd_R\) remaining row coefficients give the equations of \(A\) on the packed input once \(v_0=0\). Thus a nonzero kernel vector has \(v_0=0\) and satisfies \(A\hat v=0\). Its short multiple has \(x_0=0\) since \(2\beta<q\). Reduction and packing commute, and packing preserves the other \(N\) coordinates and adds only zeros. This packs the output into a nonzero norm-at-most-\(\beta\) solution to \(A\hat x=0\), exactly for the challenge whose rank, columns, bound, and norm are costed by M1. If no such output is found the reduction returns \(\bot\). Denote its success probability by \(s_b\). The cost is \(t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT}\) with \(Q_H\) the maximum per-oracle query count, \(C_R=O((N+n)D+\mu)\) for the fixed simulation setup and postprocessing, and \(T_{\rm LIFT}\) the time of the lifting step. The original-forms subsection proves this reduction-time bound on the revised lists, including the original private record and gradient loop costs and the new fixed setup. The inverse conditions and comparison count do not enter those time calculations. LIFT's running-time result applies by \(2\beta<q\) and (P4). In particular the cost is \(t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)\) using \(n,N\le D\).

Here is how the first-mark bounds apply to these algorithms. The degree and view for the new field encoding and the needed gradient formula are derived above. The record invariant uses no inverse premise: setting all guesses to zero commutes with additions and pairings, and before the first mark every reused label comes from formally equal expressions. Formally equal target expressions have identical stacks by the fiber equations applied to their difference for every field search vector. Thus their records also have equal sketches. A good mark's stack is usable with the three field ties of Amendment C7 by the revised view. Its rank is at most three by \(g^{-4}<\mu_{\rm tr}<\theta\) from (I5) and the protected stack rank bound. On the dense choice the stronger guard \(g^{-3}<\mu_{\rm tr}\) gives rank at most two. The full classification applies to every actual tied stack of dimension at most three, including zero-corner marks, because the three ties just derived are the original field identities. A kernel vector in its row space has coordinate 0 equal to zero, and its one-dimensional guessing probability is at least the stack's, by the protected guessing-probability lemma. The amended inverse theorem gives a short multiple, so LIFT succeeds on it.

At a first good difference mark its difference is formally nonzero, so the cleared polynomial is nonzero in the coins at some fixed search vector. This makes it a nonzero joint polynomial in coins and search coordinates. The private test uses independent uniform search coordinates and valid coins; the product-set bound gives failure probability at most \(d_f/(q-D)\). Earlier formal equalities are equalities at every private point by the record invariant, so outside this failure the reduction picks exactly this difference. The degree bound and the uniform valid coin ranges give probability at most \(\varepsilon_f\) for this failure. For a first good key mark the target record already has its expression by the record invariant and persists. Name negatives are target-group results and receive the same private and sketch tests. For a recognized good mark, the coefficient-vanishing and derivative calculation of the algebraic view subsection place each sector gradient in that sector row space. If the mark sector is alpha, the plain stack is zero and hence its gradients vanish. For any proper subspace of the mark row space choose a linear form zero on the subspace and nonzero on the row space. Its value on one gradient, divided by \(\alpha_{\mathsf s}\pi\), is a polynomial of degree at most \(n+2\) which is nonzero by isolating the constant term in \(\varepsilon\) and the distinct monomials (with \(i_*\) the left base index of the cell) \(s_X\upsilon^{k_c}\upsilon_H^{i_*}y_i\). The valid values for the independent coin coordinates have sizes at least \(q-D\), by the independent coin support argument. The polynomial root bound, with \(q-D\) in place of \(q\) in its proof, bounds the chance of failing to increase the span while it is proper. Three independent points and rank at most three give failure at most \(3(n+2)/(q-D)\le\varepsilon_f\), by \(n\le D\) and the formula for \(\varepsilon_f\). Thus on a good first mark with a kernel vector, except for the two exceptional events just bounded, the reduction finds a kernel vector in the appropriate span, and produces the MSIS output. The unconditional probability of such a mark is at most \(s_b+2\varepsilon_f\).

For a good first mark with no kernel vector, the classification proved in Amendment C7 gives a witness in its row space. In that sector the linear map from a tuple of probes to \(\sum_c W_cv_c\) has image the row space, as each matrix is symmetric and the sum of its images is the row space of the stack. Uniform independent probe tuples give three independent uniform vectors in this space, even conditional on the run. In dimension \(a\le3\), the chance of failing to span is bounded by \(\sum_{j=0}^{a-1}q^{j-3}<2/q\): equivalently the \(a\) rows of the random \(a\)-by-3 coordinate matrix are independent uniform three-dimensional vectors and the next row falls in the span of \(j\) independent previous rows with probability \(q^{j-3}\). At a difference mark the extractor tests the record difference. If the old entry is a pure guess, a guess-free difference requires the result to contain that same guessed variable with coefficient one. The label has therefore been used in an answered call, possibly the current call, and has a zero record by the test. At a key mark it tests the record of the result that obtained the target label. An initially received record has zero stack and thus is no good mark. These facts from the record invariant show that if the sampled vectors span, the witness is among the assignments tested. So the probability of a good first mark with no kernel vector and with extractor failure is at most \(2/q\).

Let \(u=2Q+2\). Every target query run has a first mark. The protected initial and guessed-mark estimates and the charged-mark estimate of Amendment Ncmp bound their three probabilities by
\[
\left(\binom{L_1}{2}+\binom{L_2}{2}+\binom{L_T}{2}\right)\varepsilon_f,\quad
N_{\rm cmp}(u)(\theta+\varepsilon_f)
+\left(\binom{L+3u}{2}+L+3u\right)\varepsilon_f,\quad
2^\lambda/N_{\rm free},
\]
respectively. These estimates concern the same sampler, oracle and record laws and use only the already checked view and degree properties, budget, and label counts. Together with the two good-mark cases they cover the event of a target key query and no witness. Their sum is at most \(s_b+E(u)\): the good-mark excess is \(2\varepsilon_f+2/q\le (8u+8)\varepsilon_f\), using \(\varepsilon_f\ge1/q\); the remaining terms of \(E\) are nonnegative and its guess term contains \(2^\lambda/N_{\rm free}\). By (P5) and the generic-ledger implication of Amendment Ncmp \(E(2Q+2)\le(Q+1)/2^\lambda\). Hence for each \(b\) the target-query and no-witness probability is at most \((Q+1)/2^\lambda+s_b\), with exactly the stated oracle budgets and one MSIS instance. This proves Theorem 5.9 with its extraction time and soundness as above.
