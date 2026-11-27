# Praxis with degree-23 period packing

Throughout the proof \(N\) is the protected external variable count and \(N_\star=N+3\) is the number of internally sampled box coordinates. The three internal Boolean coordinates do not change which external witness relation is encrypted. The construction, coefficient placement and probabilities for the amended model follow.

## Amendment C5

Write \(d=d_R\), \(h_R=\mathrm{ring\_log}\), \(p=\mathrm{pack\_digits}\), \(p_f=\mathrm{form\_pad}\), \(s_0=\mathrm{seed\_degree}\), \(A_c=3n/2\), \(S_0=\lceil(D-1)/\nu\rceil\), and \(m=k(\ell+1)d\). Write \(U_d=d(\lfloor d/2\rfloor+(d\bmod 2))+\lfloor d/2\rfloor\). Require \(\mathrm{ring\_mode}=d=23\), \(h_R=0\), and \((q\bmod 3359)^{146}\equiv1\bmod 3359\). Require \(\lambda=100\), \(N=391693\), \(\nu=2048\), \(n_{\mathsf c}=1692\), \(p,p_f\in\mathbb{Z}\), \(1\le p\le d\le 4p\), \(1\le p_f\le d\), \(4000\le n\le4800\), \(K_1\ge K_2+1\), \(K_2\le19\), \(J\le24\), and \(m\ge55000000\). The scalar arithmetic guard is \(W+V\le 3m\), where \(W\) and \(V\) are the following integers:
\[
 W=d\big((\ell+1)(3\lfloor k/2\rfloor+2(k\bmod 2))+2\lfloor k/2\rfloor\big)
       +2U_d(k+\ell+1),
\]
\[
 \begin{split}
 V={}&2D+N+n_{\mathsf c}+32+(2K_1+6K_2+11)(N+4)+2K_2\\
    &+(\Delta-\Delta/\nu+2S_0+16)+(J+3)A_c+C_{\rm mask}\\
    &+(3s_0+60)(n+J+1)+10000+189336+(N+1)+100 .
 \end{split}
\]

The guard uses the protected value \(m\) without modification. Write \(p_0=3359\) and \(a_0=11\). These are a prime and a generator of its nonzero residues. For primality it suffices to check the prime divisors up to \(\sqrt{p_0}\): the remainders at those primes, in increasing order, are 1, 2, 4, 6, 4, 5, 10, 15, 1, 24, 11, 29, 38, 5, 22, 20. The prime divisors of \(p_0-1\) and the corresponding residues \(a_0^{(p_0-1)/p}\bmod p_0\) are (2, 3358), (23, 2303), (73, 2451); all are different from one. Let \(H=\langle a_0^d\rangle\) in the residue group, of order \(f=146\). For a primitive complex \(p_0\)-th root \(\zeta\), define the periods
\[
 g_i=\sum_{u\in a_0^iH}\zeta^u,\qquad 0\le i<d.
\]
The index \(i\) in a period is read modulo \(d\), and the exponents are taken between 1 and \(p_0-1\).

The polynomial \(1+X+\cdots+X^{p_0-1}\) is irreducible over the rationals by Eisenstein after \(X=1+T\): it becomes \(((1+T)^{p_0}-1)/T\), whose leading term is monic, whose other coefficients are divisible by \(p_0\), and whose constant term is exactly \(p_0\). Thus \(\mathbb Q(\zeta)\) is a splitting field whose automorphisms are the maps \(\zeta\mapsto\zeta^a\) for \(a\in (\mathbb Z/p_0\mathbb Z)^*\). They act cyclically on the coset periods; multiplication by a residue in \(a_0^i H\) shifts every period index by \(i\). All these sums belong to the integer ring \(\mathbb Z[\zeta]\).

For the protected prime \(q\), the condition \(q^f\equiv1\pmod{p_0}\) says that its residue belongs to \(H\), since \(H\) is the unique subgroup of size \(f\) in the cyclic group. A primitive root \(\omega\) of order \(p_0\) exists in \(\mathbb F_{q^f}\) because \(p_0\mid q^f-1\). The evaluation map from \(\mathbb Z[\zeta]\) reducing coefficients modulo \(q\) and sending \(\zeta\) to \(\omega\) is well-defined: \(1+\omega+\cdots+\omega^{p_0-1}=0\). Write \(\bar g_i\) for the reduced periods. All lie in \(\mathbb F_q\), since Frobenius in the splitting field multiplies every exponent by the residue \(q\in H\), permuting the terms of each period.

The \(d\) row vectors \((\bar g_{i+j})_{j=0}^{d-1}\) are all distinct, even if a pair of individual periods agree. In fact an equal pair of rows \(i\ne k\) would say that
\[
 f_{i,k}(X)=\sum_{u\in a_0^iH}X^u-\sum_{u\in a_0^kH}X^u
\]
vanishes at every \(\omega^a\) with \(1\le a<p_0\). At any such root, choose \(j\) with \(a\in a_0^jH\) and use exactly the shared entry at offset \(j\). The two cosets in the definition are disjoint, so the polynomial is nonzero. Its degree is at most \(p_0-1\), and it has zero constant term. A nonzero polynomial of that degree vanishing at all \(p_0-1\) indicated distinct roots must be a nonzero scalar times their monic product, which is \(1+X+\cdots+X^{p_0-1}\) and has nonzero constant term. This is a contradiction.

Choose the least nonnegative integer \(t\le\binom d2(d-1)\) for which all values \(r_i=\sum_{j=0}^{d-1}t^j\bar g_{i+j}\) differ. The difference for each pair is a nonzero polynomial of degree at most \(d-1\) by the distinct-row result. It has at most \(d-1\) zeros in the scalar field. The union of these root sets leaves at least one allowed \(t\), since the tested integers are distinct modulo the protected prime. Define \(h_i=\sum_{j=0}^{d-1}t^j g_{i+j}\). Their reductions are the \(r_i\), so the \(h_i\) are distinct. Their transitive orbit under the cyclotomic automorphisms has size \(d\). The monic polynomial \(P_R(Y)=\prod_i(Y-h_i)\) has rational coefficients by invariance and integral coefficients because they are algebraic integers. The orbit of each \(h_i\) proves that this is its minimal polynomial. The chosen \(t\) and the polynomial do not depend on which primitive scalar-field root is used: replacing it by a different primitive root rotates the period indices and preserves the set of tested values. They depend only on the fixed public ring and prime, with setup given by constructing the indicated roots, summing the periods, and checking a polynomial number in \(d\) of candidate values. There are no ciphertext coins in this setup.

Define \(R=\mathbb Z[Y]/(P_R)\) and \(R_q=\mathbb F_q[Y]/(P_R)\). The power basis, coefficient infinity norm, and uniform challenge distribution are used for these rings. Let \(E\) evaluate a length-\(d\) power-basis vector at the \(r_i\). It is invertible because a polynomial of degree below \(d\) with \(d\) distinct roots is zero. It is a ring isomorphism from \(R_q\) to \(\mathbb F_q^d\) with componentwise multiplication, since evaluation at each \(r_i\) respects reduction modulo \(P_R\). Sample each seeded entry as an independent uniform tuple in this representation. Under \(E^{-1}\) this gives uniform independent power-basis coefficients. The reduction encodes the actual uniform Module-SIS challenge entries with \(E\) when programming the seed, so it produces the specified oracle distribution. The output solution lies in the integer coefficient ring and uses the power-basis infinity norm counted by the protected estimator.

### Ring arithmetic and transpose

Both evaluation matrices \(E,E^{-1}\) depend only on the public fixed ring and prime. Their entries can be computed from the two Vandermonde maps, by inversion in dimension 23 for the second map, before encryption. For each of the four fixed matrices \(E,E^{-1},E^\top,(E^{-1})^\top\), write its coefficients as \(t_{iu}\). A matrix product with a variable input \(x\) uses the following schedule. Partition the input indices into \(\lfloor d/2\rfloor\) consecutive pairs \(u,v\), with one last index if \(d\) is odd. For a pair and output index \(i\),
\[
 (t_{iu}+x_v)(t_{iv}+x_u)-t_{iu}t_{iv}-x_u x_v=t_{iu}x_u+t_{iv}x_v .
\]
The sum of the fixed terms \(t_{iu}t_{iv}\) is computed once for each output when fixing the matrix. The sum of the input terms \(x_u x_v\) uses one product per pair and is shared across every output. The first term uses one product per pair per output, and the unpaired index costs one product per output. This gives a total of at most \(U_d\) for any of the four matrices. The identity proves the exact linear map regardless of that arithmetic schedule. The inverse interpolation during decryption can still use the direct \(d^2\)-product bound. For fixed \(a\), the linear circuit \(u\mapsto E^{-1}\operatorname{diag}(E(a))E(u)\) gives the ring multiplication and its transpose by reversing these three linear maps and transposing them. Indeed for matrices \(A,B\), the dot product with \(ABu\) pulls back first by \(A^\top\) and then by \(B^\top\); the diagonal is its own transpose. This supplies the scalar kernels and the adjoint form evaluation for all forms used by the scheme. The finite counts for the two independent row functionals are in C7. Since \(d=23\) is fixed, these algorithms cost \(O(k(\ell+1)d\log(2d))\) operations on the admitted branch, and the construction's growing branch retains its original power-of-two ring and algorithms. In setting up the reduction one can alternatively use ordinary multiplication and monic division in \(O(d^2)\) operations. Indeed \(kd\le n\), \((\ell+1)d=(\lceil N/p\rceil+4)d<4N+5d\), and \(n,d,N_\star\le D\), so even this approach costs \(O((N_\star+n)D)\) on the ring dimensions. Packing uses only the monic polynomial and its full coefficient basis. Booleanity, the form field, and the resulting mask ties are independent of the polynomial in this coefficient ring.

### Kernel conversion and scope

The coefficients are placed at the slots proved in Amendment n. Each uniform entry has exactly \(d_R\) independent field coefficients in the stated power basis. A form-kernel vector therefore has constant coordinate zero and maps to zero under the nonconstant columns in the selected coefficient ring. Conversely these equations force all form coefficients to vanish. A short integer scalar multiple has integer coordinate 0 equal to zero because its residue vanishes and \(2\beta<q\). Forming the packed vector by Amendment ell preserves every ordinary and tag coordinate once, adds only zeros, and commutes with integral reduction and field scaling. This proves the kernel-to-Module-SIS conversion in the heavy-stack lemma and in Targets. The rank bound and inverse theorem use only the search distribution and the short multiple of a vector with zero constant coordinate. Their hypotheses and conclusions are independent of the computation method for the protected ring. LIFT is a base-field integer-vector operation, so its correctness and time bounds are also independent of that ring.

The reduction programs the chosen uniform Module-SIS challenge into the nonconstant seed matrix columns and samples the constant entries independently in the same ring. This is exactly the stipulated random oracle distribution. The view, mask, classification, and reduction arguments use the resulting linear form map, its stated kernel, and its coefficient tables. Their proofs in Amendments n, C6, C7 and Targets apply without further ring identities. The same ring algorithms account for preprocessing and kernel tests, with the already stated query and runtime capacities. Correctness, extraction and the extractability-error corollary for this exact instance follow from Targets and Amendment Ncmp.

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
 \operatorname{vol}_3(\beta K_B)\ge (8/(2509/1000))\,\beta^3
 \ge (8/(2509/1000))\,(2509/1000)\lfloor H_3\rfloor q^2
 \ge 8\det L .
\]
The volume implication gives a nonzero \(u=B_J z\) in \(L\cap\beta K_B\) in each rank. Put \(x'=Bz\). It is nonzero because its coordinates in \(J\) are \(u\), and its norm is at most \(\beta\) by the definition of \(K_B\). Modulo \(q\), \(x'\) is a multiple of \(v_{[N_0]}\) since \(z\in Z\). If that multiple were zero, each integer entry of \(x'\) would be divisible by \(q\). As \(\|x'\|_\infty\le\beta<q/2\) this would force \(x'=0\). Extend \(x'\) by zeros in the deleted positions, including coordinate 0, to obtain the required short multiple.

### Extra conditions for the passing-stack lift

Write \(s=\mathrm{stack\_reduction}\) and \(b_{\rm s}=\mathrm{beta\_sis}\). The additional conditions of this amendment allow \(s=0\) or the simultaneous conditions
\[
s=1,\quad b_{\rm s}=\lfloor b_{\rm s}\rfloor,\quad 1\le b_{\rm s}\le\beta,\quad
b_{\rm s}\ge H_1,\quad 3b_{\rm s}^2\ge4qH_2,\quad
3b_{\rm s}^3\ge4q^2\lfloor H_3\rfloor,\quad b_{\rm s}\ge3\lfloor H_3\rfloor^3,\quad b_{\rm s}^2\ge q\lfloor H_3\rfloor^2,\quad 2\lfloor H_3\rfloor^2<q .
\]
The general inverse theorem retains its hypotheses and its radius \(\beta\) from I6. The additional hypotheses apply to the short lift for a heavy passing stack, proved below. Since \(b_{\rm s}\le\beta\), the protected conditions \(2b_{\rm s}<q\) and \(24b_{\rm s}^4<q^3\) for LIFT follow from I6 and P4. The new rule is used only to bound the reduction's actual SIS output.

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

For a fixed simulation a collision uses the difference expression \(D\) and \(\chi=0\), and a key-value event uses the entry \(D\) and \(\chi=1\). We bound the probability of a bad event over its evaluation. In either source group, if the difference has no guess variable, the source-group coincidence estimate proved in the algebraic view subsection bounds its probability by \(\varepsilon_f\). If the expression contains a guess variable in any group, there is a nonzero formal coefficient of a guess monomial. Such a coefficient is either a nonzero field constant or a formally nonzero expression in one of the source groups, since products of guesses arise only through a pairing of source-group expressions. In the latter case for every fixed \(r\) it is nonzero on some valid encryption coins by the source-group coincidence estimate and \(\varepsilon_f<1\). Thus after clearing the factor \(\varpi\), the event equation is a nonzero polynomial in coins and guess values for each fixed \(r\). Its total degree is at most \(d_f+1\). The terms without guesses have degree at most \(d_f\) by the degree lemma. A term with one guess multiplying a source-group expression adds one degree to the cleared source expression, and terms with two guess variables and no other exponents have degree at most eight after clearing. All independent sampled field coordinates have support size at least \(q-D\). The polynomial root bound gives probability at most \((d_f+1)/(q-D)\le\varepsilon_f\).

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

Use \(N_\star+1\) distinct Booleanity points \(d_0,\ldots,d_{N_\star}\), a distinct key point \(\rho\), and the same \(n_{\mathsf c}\) cosets of size \(\nu\) for the external constraints. Hence \(D=N+5+\nu n_{\mathsf c}\). Use the protected subgroup placement in the finite scored algorithm with this \(D\). The algebraic identities apply to every admissible set of points. At \(d_0\) set \(A=0,B=e_0\). At \(d_i\), \(i>0\), set \(A=e_i-e_0,B=e_i\), including the three new Booleanity points. Fix a public primitive eighth root \(\omega_8\) in the scalar field, which exists because \(8\mid q-1\). Set \(c_*=(\omega_8+\omega_8^{-1})^{-1}\); indeed \((\omega_8+\omega_8^{-1})^2=2\) since \(\omega_8^2+\omega_8^{-2}=0\). At \(\rho\) set \(A=c_*(e_{\mathsf b_1}+e_{\mathsf b_2})\) and \(B=c_*(e_{\mathsf b_1}+e_{\mathsf b_2}-e_0)\). On the constraint cosets keep the protected evaluations, extending those linear forms by zero in the tag entries. The coordinate polynomials are the unique interpolants of degree below \(D\). Store their sparse point-value descriptions rather than a dense coordinate-by-degree table. Define \(Z_0\) to vanish at all \(d_i\) and \(\rho\), \(Z\) at every evaluation point except \(\rho\), \(Z_*=(X-\rho)Z\), and \(L_\rho=Z/Z(\rho)\). Thus \(Z_*=Z_0Z_{\mathcal K}\), where \(Z_{\mathcal K}=\prod_t(X^\nu-\delta_t^\nu)\) is the monic coset vanishing polynomial.

Here is the QAP criterion under this setup. For a symmetric \(W\), \(P_W=A^\top W B\) takes values \(0\) at \(d_0\), \(W_{ii}-W_{0i}\) at \(d_i\) with \(i>0\), and \(c_*^2(W_{\mathsf b_1,\mathsf b_1}+W_{\mathsf b_2,\mathsf b_2}+2W_{\mathsf b_1,\mathsf b_2}-W_{0,\mathsf b_1}-W_{0,\mathsf b_2})\) at \(\rho\). Once the Booleanity tests hold, this last expression equals \(W_{\mathsf b_1,\mathsf b_2}\), using symmetry and \(2c_*^2=1\). On each constraint coset \(P_W/Z_0\) is the list of terms in that constraint's quadratic test. Let \(R_W\) be the polynomial of degree below \(\nu n_{\mathsf c}\) interpolating these coset values. The sum of \(X^a\) on \(\delta_t\mathcal G\) is zero unless \(\nu\mid a\), in which case it is \(\nu\delta_t^a\). Among degrees below \(\nu n_{\mathsf c}\), the multiples of \(\nu\) give an invertible Vandermonde matrix in the distinct \(\delta_t^\nu\). Consequently all coset sums vanish if and only if \(R_W\) omits all divisible powers. Under the Booleanity and constraint tests, \(P_W-W_{\mathsf b_1,\mathsf b_2} L_\rho-Z_0 R_W\) vanishes at every evaluation point. It is therefore divisible by \(Z_*\), with quotient degree below \(D-1\) from \(\deg P_W\le2D-2\). Equivalently \(P_W-Z_0R_W\) is divisible by \(Z\) with quotient degree below \(D\). Conversely, either such identity with an allowed \(R\) implies the Booleanity values and the coset sum tests by evaluation, and \(R\) is the unique interpolated remainder. In the key identity, evaluation at \(\rho\) gives exactly the specified corner \(W_{\mathsf b_1,\mathsf b_2}\). For a witness vector \(v\), these identities apply to \(vv^\top\), with \(P_v=A_v B_v\) and key corner \(\mathsf b_1\mathsf b_2\).

The new key evaluation has \(A(\rho)=c_*(e_{\mathsf b_1}+e_{\mathsf b_2})\), which together with \(A(d_i)=e_i-e_0\) for \(i>0\) spans all form coordinates: the differences span the hyperplane of coordinate sum zero and \(A(\rho)\) has coordinate sum \(2c_*\ne0\). The vectors \(B(d_i)=e_i\) are still a basis. These properties, the QAP criterion and the updated \(D\) are the only changes in the generic comparison and coincidence arguments, explicitly used in C7. The point descriptions consist of the nonzero input terms and \(O(D)\) point data. For evaluation of all coordinate polynomials at a scalar off the point set, tabulate the \(D\) Lagrange weights there and accumulate the listed nonzero coordinate entries times their weights. For a witness, accumulate the point values of the two scalar witness polynomials and interpolate only those two polynomials, not the coordinate table. The same subgroup interpolation and vanishing-polynomial algorithms therefore give \(O(|S|+D\log D+\log q)\) setup and the claimed scalar polynomial work with these point sets. The three extra Booleanity evaluations and the key evaluation add only a constant number of nonzero coefficients. The score still uses the fixed original nonzero-coefficient charge.

## Amendment ell

Set \(p=\mathrm{pack\_digits}\) and \(\ell=\lceil N/p\rceil+3\). Divide the ordinary coordinates into successive blocks of \(p\), padding the final block with zeros. Place each block in positions zero through \(p-1\) of its ring column and zero-fill other positions. The range \(1\le p\le d_R\) from C5 provides these distinct positions. Put each of the three tag coordinates in the constant position of its own separate following column. Column zero takes the independent homogeneous entry. All matrix columns have uniform independent entries in the ring.

The placement is injective, preserves coefficient infinity norm, and commutes with reduction and field scaling. The slot-zero form is \(v_0\), and the other forms are exactly the coefficient list of the matrix product of the packed input. A form-kernel vector has \(v_0=0\) and \(A\hat v=0\). Thus the short multiple used by the reduction packs to a nonzero solution of the same norm to the uniform Module-SIS problem with dimensions \(kd_R,\ell d_R\). For any fixed tag variant of an external witness, condition on all columns except column zero. Since its homogeneous coordinate is one, the independent uniform column zero adds a uniform coefficient vector to the remaining fixed vector. Consequently each form value is uniform on the affine space where the constant is one and every padding slot is zero. This distribution is sufficient for both the exact key-weight bound and the expected fallback bound.

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
If \(X_i=r_i-(g+3)/2\), and \(X_\diamond=r_\diamond-(g+3)/2\), then \(r(v)-c_v=X_\diamond+\sum_i(v_i-1/2)X_i+E\), where the two rounding terms in \(E\) have absolute sum at most \(3/2\). The independent centered sum has variance \((g^2-1)(N_\star+4)/48\). Thus its full RMS is at most \(g\sqrt{(N+7)/48}+3/2\) by the triangle inequality in quadratic mean. Each \(|X_i|\le(g-1)/2\); the deterministic bound including rounding is at most \(B=(N+4)(g+1)\). A centered difference of three tag coordinates or a single centered tag coordinate also lies in this range. This is the definition of \(B_{\rm search}\). The protected check \(2B+1<q\) gives unique valid bounded representatives for all the searches in the amended correctness algorithm.

The guessing probability of a rank-\(d\) stack is still at most \(g^{-d}\). For any prescribed joint fiber, pick a nonsingular \(d\)-column pivot minor of a basis of the row space. If the zeroth column is nonzero, it can be extended to a pivot basis by linear independence of the columns. Fix the remaining nonpivot box coordinates; any solution fixes the pivot box coordinates and the zeroth coordinate uniquely by the invertible linear system. The regular pivot box draws therefore have probability at most \(g^{-(d-1)}\) of meeting their fixed values, and conditional on all box coordinates \(r_0\) has probability at most \(1/g\) of the required value. If the zeroth column is zero, no condition involves \(r_0\), so fixing the other box coordinates directly bounds the pivot solution by \(g^{-d}\). These probabilities hold for every fixed fiber and give the claimed bound. For a kernel vector the zeroth coefficient is zero, so its scalar guessing probability uses precisely the independent box coordinates, now on at most \(N_\star\) positions. The inverse and regularization proofs apply in that dimension with the factors of I3 and \(T_{\rm tr}\) stated next. All heavy-stack and generic ledger arguments therefore use the same guessing-probability implications. The actual arithmetic of the search is supplied in Amendment search_spread.

## Amendment T_tr

Use \(T_{\rm tr}=R_{\rm tr}g\sqrt{(N+3)/3}\). The trimming radius and covariance proof in I3 is used on the independent box of dimension at most \(N_\star\). Each projected feature-row deviation from its center is at most \(R_{\rm tr}(g/\sqrt{12})\sqrt{N_\star}\) times the corresponding basis-vector infinity norm, by the Euclidean Cauchy--Schwarz bound on that row's coefficient norm. Taking differences doubles the bound and gives precisely this new \(T_{\rm tr}\). The minor and prefix-lift argument of I6 uses the checked inequalities in I5 with this value. The projected counting constants in I3 use \(N_\star\) for the same reason. The definitions of regularity, fiber densities and their trimming loss use only the width, coefficient lattice and the radius and have the same arguments. Thus the amended radius supplies the lattice-facts hypothesis and norm proof in the new sampler dimension.

## Amendment C6

Require \(18\le n\le4800\), \(n\) even, \(\mathrm{seed\_mode}=1\), \(s_0=\mathrm{seed\_degree}\) integral with \(2\le s_0\le128\), \(2s_0\mid n\), \(2n\le D\), and \(\Delta\ge n+3\). Put \(r_H=n/s_0\), an even integer. Require \(r_H\mid(q^{s_0}-1)^{28}\). This is the modular expression in C6 because reduction before exponentiation and subtraction preserves the resulting residue modulo \(r_H\). It ensures that every prime divisor of \(r_H\) divides \(q^{s_0}-1\). The one-variable field below has degree \(n=kd_R+\mathrm{form\_pad}\), with coefficient positions supplied by Amendment n. The even degree supplies the half-turn and the needed rank of the key-weight quadratic. Set \(e=1\), \(F_0=\mathbb F_q\), \(P_H=H\), and \(Q=q^{s_0}\).

Choose \(K=\mathbb F_q[X]/(f(X))\) for a monic irreducible \(f\) of degree \(s_0\). This step can use uniform random monic polynomials of that degree, with a test as follows. Compute \(X^{q^{s_0}}-X\) and \(X^{q^{s_0/p}}-X\) modulo \(f\) for each prime \(p\mid s_0\). The first must be zero and each of the latter must have gcd 1 with \(f\). The roots of \(X^{q^a}-X\) are all elements of \(\mathbb F_{q^a}\) and are simple. Thus the first test says the irreducible factors are distinct and have degrees dividing \(s_0\). Every proper divisor of \(s_0\) divides \(s_0/p\) for some such prime, so the other tests make every factor have degree \(s_0\). This proves the test's equivalence to irreducibility. The field of degree \(s_0\) has at least \(q^{s_0}-s_0q^{s_0/2}\) elements outside its proper subfields, by counting at most \(s_0\) subfields of degrees at most \(s_0/2\). Each orbit of these elements yields a different monic irreducible, so the sampling probability is at least \((1-s_0 q^{-s_0/2})/s_0\). The tests take \(O(\log q)\) field operations because the degrees and the number of tests are bounded.

In \(K^*\) choose \(c_H\) of degree \(s_0\) over \(\mathbb F_q\) with \(c_H^{(Q-1)/p}\ne1\) at every prime \(p\mid r_H\). All these primes divide \(Q-1\). The order condition at each such prime says that the exponent of \(c_H\) as a power of a multiplicative generator is nonzero modulo \(p\). Uniform sampling meets all order conditions with probability \(\prod_{p\mid r_H}(1-1/p)\). There are at most five primes because \(r_H\le2400\) and the product of the six smallest primes exceeds 2400. The product is at least \(2^{-5}\). The fraction of elements of \(K^*\) in proper subfields is at most \(s_0 q^{s_0/2}/(Q-1)<2^{-6}\) for the protected prime and this degree range. Therefore testing both the order condition and full degree succeeds with probability at least \(2^{-6}\). Test full degree by checking \(c_H^{q^{s_0/p}}\ne c_H\) for the primes of \(s_0\). Both tests cost \(O(\log q)\) operations per trial in the scalar field, since the degree of \(K\) and the number of tests are bounded. Its minimal polynomial \(p_c\) is the product of the \(s_0\) linear polynomials from the Frobenius orbit, with coefficients fixed by Frobenius. The public seed constants are independent of the system and encryption coins. Setup is deterministic once they are fixed.

Let \(t\) be a root of \(T^{r_H}-c_H\) in the algebraic closure. If \(o\) is the order of \(c_H\) and \(m\) the order of \(t\), then \(m/\gcd(m,r_H)=o\). The order tests give \(v_p(o)=v_p(Q-1)>0\) at each prime of \(r_H\). Thus \(m=r_Ho\). For each prime \(p\mid r_H\), the binomial expansion gives \(v_p(Q^j-1)=v_p(Q-1)+v_p(j)\): raising \(1+u\) with \(p\mid u\) to \(p\) increases \(v_p(u)\) by exactly one, since \(pu\) is the unique term of lowest valuation. At two this uses \(4\mid Q-1\). Raising to an exponent prime to \(p\) preserves the valuation by the factorization as \(u\) times a geometric sum congruent to that exponent. Iterating proves the identity for every positive \(j\). For a positive \(j\), the condition \(m\mid Q^j-1\) is therefore equivalent to \(r_H\mid j\). Thus \(t\) has degree \(r_H\) over \(K\). As it generates \(c_H=t^{r_H}\), it also generates \(K=\mathbb F_q(c_H)\) over \(\mathbb F_q\). Its degree over \(\mathbb F_q\) is \(s_0r_H=n\). The monic polynomial \(P_T(T)=p_c(T^{r_H})\) of degree \(n\) vanishes at \(t\), proving irreducibility.

At \(j=r_H/2\), the same valuations show \(m/2\mid Q^j-1\) and \(m\nmid Q^j-1\). Consequently \(t^{q^{n/2}}=-t\), since \(Q^{r_H/2}=q^{n/2}\) and \(-1\) is the unique element of order two. Use the monomial basis through degree \(n-1\) in the same form slots as above. The \(V\) weights have even powers only. All three consecutive Frobenius projections have their original field identities and the same coefficient-kernel relation.

For exponent \(j\) of Frobenius put \(b_j=q^j\bmod r_H(Q-1)\). For each basis monomial \(T^a\), its reduced representative is obtained from
\[
 c_H^{\lfloor a b_j/r_H\rfloor}T^{a b_j\bmod r_H}
\]
by expanding the coefficient in the basis \(1,c_H,\ldots,c_H^{s_0-1}\) and replacing \(c_H\) by \(T^{r_H}\). The modulus for \(b_j\) suffices because the order of \(c_H\) divides \(Q-1\). This produces at most \(s_0\) powers of degree below \(n\), all congruent to \(a b_j\) modulo \(r_H\). For increasing \(a\), the quotient increments by \(\lfloor b_j/r_H\rfloor\) or by one more. Compute these two step powers with \(O(\log q)\) field operations and tabulate the representatives in \(O(n)\) operations using the bounded degree. Evaluate the table in \(O(n)\) operations given the evaluation point's powers. The resulting coefficients are used in the same ring transpose circuit and assigned to the same coefficient slots. 


## Amendment C7

Require \(\mathrm{base\_degree}=\mathrm{base\_left}=\mathrm{base\_right}=\mathrm{scalar\_rel}=1\), \(K_1,K_2\ge1\), and \(2K_1K_2=n\). Require \(a_0=\mathrm{mask\_stride}\) to be a positive integer dividing both \(2K_2\) and \(r_H=n/s_0\). Require \(C_{\rm mask}=17n+2K_2-14-5(a_0-1)\). This is the one-variable grid. Write \(e=A_H=B_H=1\) and \(h=n\) when using field-degree notation. There are \(A_c=3K_1K_2=3n/2\) cells, indexed by a left leg \(a\) with \(0\le a<K_1\) and a right leg \((b,\mathrm X)\), \(0\le b<K_2\), \(\mathrm X\in\{\mathrm E,\mathrm O,\mathrm V\}\). Write \(p_X=\mathbf1_{\mathrm X=\mathrm O}\). Set \(\lambda_a=2K_2a\), \(k_{\mathrm{leg}}=2b+p_X\). Put \(k_c=\lambda_a+k_{\mathrm{leg}}\). For E and O the cell weight is the coefficient of \(T^{k_c}\) in \(U=z(w)\sigma^{n/2-1}(z(w))\); for V use \(V=z(w)\sigma^{n/2}(z(w))\). The half-turn fixes \(V\) so only even powers occur there. For the appropriate parity \(p_X\), divide \((k_c-p_X)/2\) by \(K_2\). Its quotient \(a\) and remainder \(b\) recover the two digits and cover each slot exactly once. The key cell is \(a=b=0,\mathrm X=\mathrm E\), with weight the constant coefficient of \(U\).

### Factor masks and publication

Use the original independent scalar coins and centered sampler in the internal dimension. The evaluation coin \(\upsilon\) is uniform nonzero, the scalars \(\pi,s_{\mathrm E},s_{\mathrm O},s_{\mathrm V},\zeta_0,\zeta_1,\zeta'',\eta_1,\eta_2,\eta_3,\Omega_{22},\alpha\) are independent uniform nonzero, \(\Omega_{12}\) and the coordinates \(y_i\) are independent uniform scalars, and \(\tau\) is uniform off the evaluation points. Sample \(\varepsilon\) uniformly from the field excluding \(0,-1\). Let \(F_x(T)\) be the reduced representative of \(\sigma^{n/2+1}(T^x)\), computed by C6. Write \(z_-,z_\circ,z_+\) for the reduced vectors of linear form coefficients at Frobenius powers \(n/2-1,n/2,n/2+1\), respectively, evaluating at \(\upsilon\) when used as scalars. Set
\[
 \pi_a=\pi(\upsilon^{\lambda_a}+\varepsilon F_{\lambda_a}(\upsilon)),\qquad
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

For a stack form \(W_U,W_V\) by summing cell matrices times \(T^{k_c}\) in their weight families. Put \(\widetilde W_U^+=\sum_{c\in C_U}W_c F_{\lambda_a}F_{k_{\rm leg}}\), whose image in the form field is \(\sigma^{n/2+1}(W_U)\). At degree zero in \(\varepsilon\) the three coefficients of the mask contribution, after taking out \(\pi\) and the indicated independent \(\eta\), are
\[
 t_1=W_Uz_\circ-W_Vz_-,\qquad
 t_2=W_Uz_+-\widetilde W_U^+z_-,\qquad
 t_3=W_Vz_+-\widetilde W_U^+z_\circ .
\]
Indeed the negative grade in the right E/O mask contributes degree zero exactly when multiplied by the twisted part of \(\pi_a\); the ordinary products supply the remaining terms. With the honest weights and the form vectors contracted against \(w\), each \(t_i\) vanishes in the field: \(U z_\circ=V z_-\), \(U z_+=\sigma^{n/2+1}(U)z_-\), and \(V z_+=\sigma^{n/2+1}(U)z_\circ\). The finite supports and group bases for these multiples are specified next.

In a formal identity, the Laurent comparison below isolates the same grade-zero polynomials for the actual stack up to multiples of \(P_T\). Their reduction gives all three stated field ties. The right-leg type \(s_{\mathrm X}\) and the ordinary exponent \(k_c\) distinguish every cell in the generic comparison. The proof of the original rank-three classification using these ties follows. The new QAP point at \(\rho\) changes only the corner used by the view and does not change the Booleanity or constraint tests used by that classification.

### Cancellation for the bounded seed modulus

The ordinary left powers are \(2K_2a\), \(0\le a<K_1\), and the ordinary right powers are \(2b+p_{\mathrm X}\). Their sums give the distinct ordinary grid indices in the corresponding families. Every left exponent is a multiple of \(a_0\). Its conjugated representative has terms in the prescribed residue class modulo \(r_H\) from C6. Since \(a_0\mid r_H\), that residue and every representative exponent are multiples of \(a_0\). With representatives of degree below \(n\), the largest possible such degree is \(n-a_0\). Put \(L_\sigma=n-a_0\), \(R_\sigma=n-1\), and \(Q_\sigma=L_\sigma+R_\sigma\) as bounds for the conjugated left, right and product terms. As \(a_0\le2K_2\le40<n\), \(Q_\sigma\ge n-1\). The degree of the first grade-zero tie polynomial is at most \(2n-2\), and the degrees of the second and third are at most \(Q_\sigma+n-1\). Since each tie vanishes modulo \(P_T\), the quotient supports have lengths \(n-1,Q_\sigma,Q_\sigma\) respectively. Use the basis exponents \((\pi\eta_i/\zeta'')P_T(\upsilon)\upsilon^a\) at consecutive indices starting at zero over each of those support lengths.

The three positive grades use a conjugated left digit, an ordinary right digit of degree at most \(2K_2-1\), and a form of degree at most \(n-1\). Their support lengths are \(L_\sigma+2K_2+n-1,L_\sigma+2K_2+n-1,L_\sigma+2K_2+n-2\), using the even right digit in the V grade. Each negative grade uses an ordinary left digit of degree at most \(n-2K_2\), a conjugated right digit and a form, so its support length is \(2n-2K_2+R_\sigma\). The positive and negative bases have exponents \(\pi\eta_i\varepsilon^{\pm1}\upsilon^a/\zeta''\) over those consecutive support lengths, with the grade fixed and the sign of the correction carried in the scalar coefficients. This follows by multiplying the terms of \(\pi_a\) against those in the right masks: each right inverse-\(\varepsilon\) term combines with the ordinary or twisted term on the left, and only the ordinary-right or V terms combine with the positive-\(\varepsilon\) left term. The published bases evaluate all coefficients of each grade at \(\upsilon\), so the cancellation MSM paired with the witness Y sum removes the entire honest mask. Summing these eight lengths at \(L_\sigma=n-a_0,R_\sigma=n-1,Q_\sigma=2n-a_0-1\) gives exactly \(17n+2K_2-14-5(a_0-1)\), as required by the amended rule. The uniform lengths can cover coefficients that vanish for particular choices or structured exponents; those coefficients are zero in the MSM, and all specified group bases are actually transmitted and counted.

These supports do not change the three ties checked by the view. At grade zero the jointly conjugated ordinary weight polynomial is the required Frobenius image modulo \(P_T\) even when its ordinary degree is larger. Other Laurent comparisons still isolate each ordinary monomial \(T^{k_c}\), whose cell indices are distinct by the original grid. In particular the support bound introduces no new weight family or hidden variable. Every published cancellation exponent has polynomial degree at most \(3n-3\), since \(L_\sigma,R_\sigma\le n-1\), \(2K_2\le n\), and the original left-grid digits and the new finite \(K_2\) guard give the displayed finite grade lengths at most \(3n-2\). Monic reduction can be done in residue classes modulo \(r_H\) by divisions by the bounded-degree seed polynomial. Each class has length at most a fixed multiple of \(s_0\), and the cost of this reduction is \(O(n)\) for \(s_0\le128\). Assembling the weighted digit polynomials uses at most a constant times \(s_0 n\) terms, since all factors for a single product lie in fixed residue classes and their product has at most \(2s_0-1\) terms. The blocked FFT products use \(O(n\log n)\) operations, leaving the claimed asymptotic decryption bound.

### Scored encryption arithmetic

This accounts for all arithmetic of the admitted finite mode. Write \(S_{\rm nz}\) for the number of nonzero point coefficients traversed in preparing the QAP exponents, to which the benchmark assigns \(2^{30}\). We show at most \(S_{\rm nz}+3m\) variable scalar multiplications in that cost convention.

At \(\upsilon\) evaluate the three conjugate-basis tables from C6. In the scored branch each Frobenius representative has at most \(s_0\) monomials. Form the two combined tables for
\[
 A_\eta=\eta_1z_\circ+\eta_2z_+,\qquad B_\eta=\eta_2z_-+\eta_3z_\circ.
\]
The third form used by the masks is \(C_\eta=(\eta_3 A_\eta-\eta_1 B_\eta)/\eta_2\), by direct expansion with the existing nonzero \(\eta_2\).


Use the invertible evaluation representation of the period ring from C5. For each of the two independent masks pull the row functional back through \(E^{-1}\) using its transpose. After the pointwise products pull each accumulated column functional back through \(E\) using its transpose. Each application costs at most \(U_d\) products by C5, including its fixed scalings. Therefore the total transformation cost is at most \(2U_d(k+\ell+1)\).

For each evaluation root write the two transformed row-weight sequences as \(A^{(1)},A^{(2)}\), and the uniform matrix column as \(B\), all of length \(k\). For a pair of consecutive indices \(u,v\) add
\[
 (A^{(h)}_u+B_v)(A^{(h)}_v+B_u)
 - A^{(h)}_u A^{(h)}_v - B_u B_v
   = A^{(h)}_uB_u+A^{(h)}_vB_v,\qquad h=1,2.
\]
Compute the sum of the row-only terms separately for the two rows and the sum of the column-only terms once per column, shared across the two outputs. The identity verifies both desired matrix products term by term. Every pair uses two main multiplications and one column correction product. A final unpaired row needs two products per column. The two row corrections take \(2\lfloor k/2\rfloor\) products per evaluation root. Hence the total cost of the products and both transforms is bounded by
\[
 W_{\mathrm{mat}}
 =d\big((\ell+1)(3\lfloor k/2\rfloor+2(k\bmod2))+2\lfloor k/2\rfloor\big)
       +2U_d(k+\ell+1)=W .
\]
The fields and independent ring entries are unchanged. Only their scalar arithmetic is reorganized. The resulting two form coefficient vectors are exactly \(A_\eta,B_\eta\), with the known slot-zero homogeneous contribution. Form \(C_\eta\) by its linear combination using the two precomputed ratios \(\eta_3/\eta_2,\eta_1/\eta_2\), at two multiplications per input coordinate.

Partition the QAP roots into the \(N+5\) Booleanity and key singleton factors and \(n_{\mathsf c}\) constraint cosets. Their vanishing factors at \(\tau\) are respectively \(\tau-p\) and \(\tau^\nu-a^\nu\) for a coset represented by \(a\). Compute \(\tau^{2^j}\) for \(1\le j\le11\) by successive squaring. On the list of \(b=N+5+n_{\mathsf c}\) factor values, ordered with singletons first, use prefix and suffix products to get their product and their outer complements. Prefix values through the singleton group and the whole list give \(Z_0(\tau)\) and \(Z_*(\tau)\). A first value and an end complement can be copied without multiplying by one. The full prefix uses \(b-1\) products, the suffix excluding its unused first product uses \(b-2\), and the \(b-2\) interior complement products supply the rest. At a coset node of size \(2^j\), split it into its two child cosets of size \(2^{j-1}\). Each child's vanishing evaluation is the precomputed power \(\tau^{2^{j-1}}\) minus the corresponding public power of a representative. The two child complements are the outer complement at the parent times the sibling vanishing evaluation. With two multiplications per internal node of a $\nu$-leaf tree, this provides all \(Z_*(\tau)/(\tau-p)\) using \(2(\nu-1)n_{\mathsf c}\) products after the outer pass. At \(\rho\) the complement is \(Z(\tau)\). The sum of all products is at most \(3b-5+11+2(\nu-1)n_{\mathsf c}=2D+N+n_{\mathsf c}+11\), which fits the \(2D+N+n_{\mathsf c}+16\) term. The public QAP coefficients at \(p\) are encoded with the fixed multiplier \(1/Z_*'(p)\). Multiplying an encoded point coefficient by its cofactor now makes the exact Lagrange contribution with one multiplication. The nine new Booleanity coefficients and the five entries at \(\rho\) are covered by the sixteen-multiplication allowance below. All these scalars are over \(\mathbb F_q\).

The G1 factor computations use at most \((2K_1+3)(N+4)\) multiplications, including the shared hidden-basis scalar \(\Omega_{12}y_i+\Omega_{22}A_i\), the two per-left-scale exponents and the extra Y-column scaling. In G2 put \(U_i=B_i(\tau)-y_i\) and \(V_i=r_i+A_i(\tau)-(\Omega_{12}/\Omega_{22})U_i\). Prepare the three shared vectors \(V_\mathrm E=s_\mathrm E V+A_\eta\), \(V_\mathrm O=s_\mathrm O V+A_\eta\), and \(V_\mathrm V=s_\mathrm V V+C_\eta\). Computing \(V\) and these three vectors costs four multiplications per input coordinate. This and the two for \(C_\eta\) contribute \(6(N+4)\) within the grouped linear term of C5. For a right leg of type E or O its first coordinate is \(a V_{\rm X}+b B_\eta\), where \(a=\upsilon^{k_{\rm leg}}\) and \(b=-\varepsilon^{-1}F_{k_{\rm leg}}(\upsilon)\) are its precomputed scalars. At each input coordinate precompute the products \(V_{\rm E}B_\eta\) and \(V_{\rm O}B_\eta\) once. Store one product \(ab\) per E or O leg. The exact bilinear identity
\[
 a V_{\rm X}+b B_\eta=(V_{\rm X}+b)(B_\eta+a)-V_{\rm X}B_\eta-ab
\]
uses one multiplication per entry after those precomputations. On V use the one product \(\upsilon^{k_{\rm leg}}V_{\rm V}\), and on every leg the second coordinate is the one product \((s_{\rm leg}/\Omega_{22})U\). Thus the right exponent work is at most \((6K_2+2)(N+4)+2K_2\) multiplications after the shared vectors. The ordinary expansion of the identity and of the shared vectors gives exactly the previous mask and hidden-basis exponents. This arithmetic changes no source element or scalar distribution.

### Reused scale factors for the published source exponents

For the sparse powers of Amendment n1, start at the already sampled exponent \(\zeta_0\). Compute \(\tau^\nu\) by eleven squarings, including \(\tau^2\). Advance the sparse base exponent by repeated multiplication by \(\tau^\nu\). For each sparse entry also obtain the shifted entry with one multiplication by \(\tau\). Together these use at most \(2S_0-1\) further products. For the non-sparse list start at \(\zeta_1\tau\). The gap between consecutive allowed exponents is one, except at a skipped multiple of \(\nu\) where it is two. Multiply the current exponent by the already available \(\tau\) or \(\tau^2\) accordingly. At most \(\Delta-\Delta/\nu\) further products therefore produce that list including its initial exponent. The total for both lists is at most \(\Delta-\Delta/\nu+2S_0+16\). This produces the same scalar exponents with the scale factors retained throughout; each transmitted element still takes its own fixed-base generator multiplication. These recurrences also hold at \(\tau=0\).

The key and non-key sparse right constants and the \(J\) regular right constants are prepared once. Each associated right exponent multiplies its \(\gamma_c\) by the corresponding constant, at one multiplication per slot. The search exponents are the precomputed leg scales. The mask power list uses the tabulated powers of \(\upsilon\) multiplied by one constant for each grade and the appropriate monic-modulus factor in degree zero, with one multiplication per slot after combining these constants. The optional generator repeat adds no exponent work.


For the shared direction data of n1, obtain the three tag Lagrange values from the tag-three coordinate, from \(A_1-c_*L_\rho\), and from \(A_2-c_*L_\rho\). The key exponent formation already computes \(L_\rho\). At \(\tau\), compute the shared left scale \(\zeta_0/U(\tau)\) using the inverse charged below. The array combines \(S_j=A_j^{\rm o}+B_j^{\rm o}\) by an addition and inserts the single homogeneous correction before multiplying by that scale, for \(N+1\) products. The five fixed quotients of n1 are formed directly using two products for each numerator at most, plus one scale product per entry and one product for each shifted copy; including the shared inverse scale takes at most 21 multiplications. Compute the three linear factors and \(U(\tau)\) with two products; the two extra right list constants each use multiplication by \(U(\tau)/\zeta_0\). Including one more product for this shared scale, a product for \(c_*L_\rho\), and fixed constants or copies, all these extra scalar computations fit the \((N+1)+100\) bound. The two new right lists use one product per entry after the common constants are prepared, included in the counted correction slots.

The fixed scalar tables use at most \((3s_0+60)(n+J+1)\) multiplications. In particular the three evaluations of the Frobenius tables and the two combined weight arrays use at most \((3s_0+4)n\) multiplications outside the two dense transformations already counted, and the \(\upsilon\) power list uses at most \(3n\). The left, right and cell scale tables use at most \(10(2K_1+3K_2+A_c)<35n\). The sparse and chunk strides and their tables use at most \(2J+600\) further multiplications by successive powering, even including the first strides by binary powers. Preparing the fixed grade and quotient constants, evaluating the scored sparse seed modulus at \(\upsilon\), forming the key exponent and its scalar alpha multiple, and forming any tag self terms uses fewer than \(10(n+J+10)\) operations. The per-n coefficients sum to at most \(3s_0+52\), with at most \(12J+700\) remaining multiplications. This fits \((3s_0+60)(n+J+1)\) since the scored shape has \(n\ge4000\). Invert the bounded list of scale denominators, including \(\varepsilon,\Omega_{22},\zeta_0,\zeta_1,\zeta'',\eta_2\) and, when needed, the common \(Z_*(\tau)\) and the three-root factor \(U(\tau)\) used in n1. At most ten inversions and the additional fixed products are covered by 10,000 multiplications at the protected prime. All other operations for these arrays are additions, subtraction, or selection of entries.

The remaining finite scalar encryption terms sum to at most \(V\) of C5. They include the cofactor products, shared mask forms, left and right factor multiplications, scaled power recurrences, the \((J+3)A_c+C_{\rm mask}\) correction slots, the fixed table and inversion allowances, the bound \((N+1)+100\) for the shared tag directions, and the target exponentiations. Both target-group exponentiations use the same generator. Compute its multiples \(2,\ldots,7\) with six successive products, and share that table. In each exponentiation scan 85 groups of three bits of its canonical 254-bit scalar, padding on the left. For every group use three squarings and at most one table product. Hence the two exponents and table use at most \(6+2(85)(4)=686\) target-field products. At \(276\) base-field multiplications per product, proved in Amendment search_spread, this costs at most \(189336\) multiplications. The matrix bound includes both transforms, so there is no second conversion charge. The guard \(W+V\le3m\) bounds the combined work throughout the admitted domain. Therefore the finite encryption uses at most \(S_{\rm nz}+3m\) field multiplications, and the independently charged fixed-base source-group operations are exactly the ones on the published exponents.

### Efficiency and asymptotic choices

The complete publication and combination of correction bases, weighted factors and searches are stated in Amendments n1, n2 and the operation-count amendments. With the specified group representation sizes and the exact finite counts they give the amended objectives. No oracle is called more often than one seed query per matrix entry and at most one key query in either algorithm. The at most eight tested internal tag variants reuse the same seed and field matrix. Each form evaluation and coefficient-ring adjoint has the same \(O(k(\ell+1)d_R\log(2d_R))\) cost as C5. All mask and field calculations use \(O(n\log n)\) operations per variant, after public field setup. The QAP and weight work is repeated at most a fixed constant number of times and uses \(O(D\log D+|S|)\) operations beyond ring and mask work, as established in n1. The ordinary branch uses three bounded signed searches, and the exact fallback has bounded expected cost as shown in search_spread.

### Parameter selection and Corollary 5.8

Define the amended parameter selector on the public security level, domain, and external system shape. On the protected BN254 domain with security level 100 and the external benchmark shape, use the admitted parameters of this proof, the protected subgroup placement, and the changed algorithms. On every other domain, security level or external shape, take the protected original selector and use its original setup, encryption and decryption at that input. This public dispatch precedes parameter calculation. Only the first branch evaluates any entry amended here. In the second branch the original bounds, norm, sampler, field and ring parameters, point and coefficient placement, group counts and search algorithm all come from the original selector. Thus neither the statement nor the proof of the protected cor:asymptotics on the second branch uses an amended entry. Apply that protected result to the second branch with its unchanged hypotheses and original \(\lambda\).

The statement of Corollary 5.8 for this selector has the same four bounds and scope: for linear-size systems with \(N\ge\lambda^2\) in the designated subgroup placement, size is \(O(\lambda N)\) field elements, encryption costs \(O(\lambda^2N/\log\lambda)\), and decryption costs \(O(\lambda N\log\lambda)\) outside its search with expected \(O(2^{\lambda/4}N^{1/4})\) operations in the search. On the first branch \((\lambda,N)=(100,391693)\) is a single point. The explicit ciphertext count and the finite work proofs bound the costs on this branch uniformly over all admissible parameters, systems of that shape, and placements used in the cost statement. All ciphertext arrays and transform lengths are uniformly bounded by the shape and guards. Every allowable system has at most \(1692(2\cdot2047+1)(391693+1)\) field coefficients in its ordinary form description, so even counting zero coefficients gives a fixed uniform bound on linear form work. All scalar and group operations outside the search use the fixed number of arrays, transforms and coefficients proved here. The elementary coefficient algorithms and the protected group implementation are over fixed finite fields, with finite worst-case costs per listed operation. The ordinary search has a fixed cap \(B_{\mathrm{search}}<q/2\) and the fallback has cap \(q\). Each uses the bounded traversals in Amendment search_spread. Uniform bounds also follow directly from the expected search estimate using \(g^2\le2^{40}2^{100}\). Divide the four uniform costs by the corresponding positive scales at \((100,391693)\) and take the maximum with the original branch's constants. This yields uniform constants for the four bounds throughout \(N\ge\lambda^2\).

The amended branch has no growing-domain conditions. It uses the protected modulus, security parameter, label size, comparison budget, and other protected constants. Targets proves the original correctness and extraction conclusions for every parameter set admitted by the amended rules independently of this dispatch.

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
The coefficients are fixed scalars. No source exponent uses \(\alpha\). The factor \(\varpi=\Omega_{22}\zeta_0\zeta_1\zeta''\varepsilon\) clears all denominators in every paired product. For degree accounting put \(e_*=1\), since C6 admits the bounded seed branch. The degree of \(\pi_a\) is at most \(n+e_*\): the ordinary and conjugated left degrees are each at most \(n-1\) and the two independent scalar factors are \(\pi,\varepsilon\). The QAP factors have degree below \(D\), and the hidden-basis matrix supplies at most one further factor. The sparse and shifted G1 powers have degree at most \(D\) including scale, and the Y exponent has degree two. The fixed degree bound for G1 is therefore \(d_1=D+n+2+e_*\). The degree of \(\gamma_c\) is at most \(n+2+2K_2\), since the right scale has ordinary degree at most \(2K_2-1\) plus its one independent scalar. The key scale still has degree three.

The cleared sparse correction bases, including the new right entries of polynomial degree at most \(D+2\), have degree at most \(D+n+8+2e_*K_2\), which is at most the combined-list bound below since \(D\ge4\). For non-sparse ones the polynomial part has degree at most \(2D-2\) from P1, and the cell scale and remaining clearing factors give at most \(2D+n+4+2e_*K_2\). The first and second right coordinates before the masks have degree at most \(D+n+6+2e_*K_2\) after clearing, by \(k_{\rm leg}\le n-1\), the degree below \(D\) of the QAP polynomials and the linear hidden-basis inverse. Each term of a right mask is a leg power of degree at most \(n-1\) times a form of degree at most \(n-1\), with one \(\eta\) and an optional inverse \(\varepsilon\). It has cleared degree at most \(2n+5\). A cancellation basis has monomial degree at most \(3n-3\) and cleared degree at most \(3n+4\), including its scalar factors and clearing factors. Search bases have cleared degree at most \(n+5\). Since \(2n\le D\), all G2 exponents after clearing fit \(d_2=2D+n+6+2e_*K_2\). The cleared key terms fit \(D+8\). The product degree before a guessed-operand factor is at most \(d_1+d_2=3D+2n+8+e_*(2K_2+1)\). By C5, \(K_1\ge K_2+1\). Thus this bound is at most \(d_f=3D+2n+2K_1+7\). The extra guess factor of degree one and all listed separate bounds fit \((q-D)\varepsilon_f\) by its protected formula. The search coordinates enter only linearly, within the same degree bounds.

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

The left-input types in the sum are \(1,\zeta_0 p(\tau),\zeta_1\tau^v,\zeta''B_i,\pi_a B_i,\Omega_{12}\pi_a B_i\), separated by degrees in \(\zeta_0,\zeta_1,\zeta'',\pi,\Omega_{12}\). The polynomials \(p\) include the sparse powers and the new quotient difference polynomials. In the first four types the monomials \(s_{\rm leg}=s_{\mathrm X}\upsilon^{k_{\rm leg}}\) distinguish the legs in each kind. The \(\zeta_1\) powers are distinct and the \(B_i\) are independent by their \(d_j\) values. The polynomials in the \(\zeta_0\) type need not be independent: the identity says for each leg and right coordinate \(j_0\) their coefficient-weighted sum is the zero polynomial in \(\tau\). In this type each \(\widetilde a\) is the full first input independent of \(y\) and the hidden basis, so its aggregate ordinary pairing with that \(H_1^{\mathrm{leg},j_0}\) vanishes at every coin and every \(r\). For the last two types use the constant term in \(\varepsilon\), giving the distinct cell monomials \(\pi s_{\mathrm X}\upsilon^{k_c}\) and the independent \(B_i\). Thus the matched factor coefficients agree individually and all unmatched first-right terms cancel identically as sums, which is sufficient both for the class comparison and the derivative. Formal projection onto first-left factors continues to respect formal equality and receives no contribution from the \(\zeta_0\) type.

In the multidegree with one \(\pi\) and zero degrees in \(\zeta_0,\zeta_1,\zeta''\) and net hidden-basis degree, the pairs are the matched factor products, first-left pairs with the search bases and generator, the correction lists in two matching inverse-scale classes, and the Y column with cancellation bases. This enumeration follows by checking the degrees of the published exponents: the left first factors have one \(\pi\), the left second also has one hidden-basis degree, and the three other nonconstant left types carry only one of the three scales. The right factor scales and correction types above are their only complementary types. The left-generator pair with any published right exponent of degree one in \(\pi\) has an inverse scale and cannot enter this class. Define \(W_c\) by matched factor coefficients, and \(u_c\) by minus the first-left search-pair coefficients. The class identity is
\[
 \sum_c\gamma_c b_c+\Phi_*=\chi\kappa,\qquad
 b_c=y^\top(W_cr-u_c)+y^\top(W_c-W_c^\top)A(\tau)
              +(P_{W_c}+Z_c h_c+Z_0 R_c)(\tau).
\]
Here the two correction types produce \(Z_c h_c+Z_0R_c\) with allowed \(R_c\), by the residue-preserving monic division proved in n1. The term \(\Phi_*\) collects the masks from the factor products, the Y cancellation products and the first-left generator pairs. It is free of all \(s_{\mathrm X}\). Taking the constant term in \(\varepsilon\) and the coefficients of the distinct \(\pi s_{\mathrm X}\upsilon^{k_c}\) gives \(b_c=0\) except at the key cell, where \(b_c=\chi L_\rho\). The original identity then also gives \(\Phi_*=0\).

For each \(c\), the linear coefficient in \(y\) at \(d_0\) gives \(W_c r=u_c\). The same comparison at \(\rho,d_i\) shows \(W_c-W_c^\top\) vanishes on the spanning vectors in Amendment D, hence \(W_c\) is symmetric. The constant coefficient gives \(\deg Z_c h_c\le2D-2\) since the \(P_{W_c},Z_0R_c,L_\rho\) terms have that bound. Thus \(\deg h_c<D\) for a non-key cell or \(<D-1\) in the key cell. The QAP identities in Amendment D give all Booleanity and constraint tests, with the ordinary or keyed vanishing factor as applicable. In particular the Booleanity tests follow first by checking the \(d_i\), where the key polynomial is zero. In the key cell evaluate then at \(\rho\) where the two vanishing factors are zero. The Booleanity equalities reduce \(P_{W_c}(\rho)\) to \((W_c)_{\mathsf b_1,\mathsf b_2}\) in the new key evaluation. Therefore \((W_c)_{\mathsf b_1,\mathsf b_2}=\chi\). In the coefficient of each \(\eta_i\) in \(\Phi_*\) at degree zero in \(\varepsilon\), the mask part is \(\pi y^\top t_i(\upsilon)\). The remaining terms there are the Y pairs with multiples of \(P_T(\upsilon)\); the other grades and generator pairs do not contribute. Comparing the \(y_j\) coefficients and substituting the form generator for \(\upsilon\) therefore gives all three actual ties from the honest cancellation derivation.

If \(r'\) replaces \(r\), the coefficient-matching result shows the difference in the target value is \(\sum_c\gamma_c y^\top W_c(r'-r)\), because no other exponents depend on \(r\). Thus the identity remains valid throughout its prescribed locus. If all stacks are zero, it holds formally at every \(r'\) and the key corner forces \(\chi=0\). If an identity is formal for all \(r\), its equations \(W_c r=u_c\) for every \(r\) force all \(W_c=0\) and again \(\chi=0\). A difference of source expressions pairs with the other source generator to an expression of zero stack. If it vanishes identically at any fixed \(r\), this argument says it is formally zero, so formally different source expressions have the stated coincidence bound. This proves the view clauses with the new corner and one actual sector.

The formal derivative of the target expression with respect to the search coordinates, for a marked identity, is the vector \(\sum_c\gamma_c W_c^\top y\). To compute it use the private evaluation and reverse accumulation of the reduction. At each recovery point project the G1 input polynomials by setting \(\Omega_{12}=\Omega_{22}=0\) and taking the part linear in \(\pi\); these are exactly the first left coordinates. This is a linear projection and therefore respects formal equality of G1 expressions. The derivative of a G2 leaf is nonzero only for a first right coordinate and is \(s_{\rm leg}\) times the corresponding coordinate vector. The matched \(F_1,H_1\) coefficients are precisely the coefficients of the projected product in the derivative. Since unmatched first-right coefficients vanish for a marked identity, this is its full stack gradient. Formally equal targets have zero difference stack and the same gradients; formally equal G2 inputs also have equal derivative records by pairing their difference with a first-left input and applying the zero-stack result. The projected gradients always lie in the marked row space. For a nonzero linear functional on it that vanishes on a given proper subspace, the derivative polynomial after dividing by \(\pi\) is nonzero: take its degree-zero coefficient in \(\varepsilon\) and the distinct monomials \(s_{\mathrm X}\upsilon^{k_c}y_i\). Its degree is at most \(n+2+2K_2\), establishing the recovery comparison used in Targets. The optional empty alpha sector has identically zero stack and gradients.

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
 n_1=(2K_1+1)(N+4)+2\lceil(D-1)/\nu\rceil+\Delta-\Delta/\nu+(N+1)+10
\]
transmitted G1 elements. Use the single factor sector, field mask bases and Y column of C7. Let \(S_0=\lceil(D-1)/\nu\rceil\) and
\[
 I_0=\{0\le a<D-1:\nu\mid a\},\qquad
 I_0^*=I_0\cup\{a+1:a\in I_0\},\qquad
 I_1=\{0\le a<\Delta:\nu\nmid a\}.
\]
Send \(P_a^0=[\zeta_0\tau^a]_1\) for \(a\in I_0^*\), and \(P_a^1=[\zeta_1\tau^a]_1\) for \(a\in I_1\). There are \(2S_0\) sparse entries because \(\nu\ge2\), and \(\Delta-\Delta/\nu\) non-sparse ones by alignment. Use \(Z_c=Z_*\) in the key cell and \(Z_c=Z\) elsewhere. Send one \(B_c^0=[\gamma_c Z_c(\tau)/\zeta_0]_2\) per cell and \(J\) bases \(B_{c,j}^1=[\gamma_c Z_0(\tau)\tau^{j\Delta}/\zeta_1]_2\), \(0\le j<J\). The factor arrays, search bases and cancellation arrays are those of C7, each once. Add the tag quotient difference bases below and then apply the same optional existing-generator parity padding, computed as one scalar multiplication by one. Send the seed, the one element \([\alpha\kappa]_T\), and the masked message. There is exactly one fixed-base generator multiplication per transmitted group slot and one more in GT for the key. All scalar exponents use the displayed fixed factors and tabulated powers, with constant work per exponent.


### One common left array for the internal tag directions

Write \(d_1',d_2',d_3'\) for the three tag Booleanity points, \(L_1,L_2,L_3\) for their QAP Lagrange polynomials, and \(A_i,B_i\) for the coordinate polynomials of tag \(i\). The new key evaluation gives
\[
 A_i=B_i=L_i+c_*L_\rho \quad(i=1,2),\qquad A_3=B_3=L_3 .
\]
For an ordinary coordinate \(j=0,\ldots,N\) let \(S_j=A_j^{\rm o}+B_j^{\rm o}\). Define the three-root factor and common direction polynomials by
\[
 U=(X-d_1')(X-d_2')(X-\rho),\qquad
 G_j=\frac{S_j+\mathbf1_{j=0}(L_1+L_2+c_*L_\rho)}{U}.
\]
At both tag points in \(U\), the sum of the ordinary A and B vectors is \(-e_0\); at \(\rho\) this sum is \(-c_*e_0\). Thus each \(G_j\) is a polynomial of degree at most \(D-4\). Also \(U A_i\) is a multiple of \(Z_*\) for \(i=1,2\): outside \(U\)'s three roots the Lagrange polynomial \(A_i\) vanishes at every QAP point. It has degree at most \(D+2\).

Define five fixed polynomials
\[
 F_i=-\frac{A_i L_{3-i}}{Z_*}\quad(i=1,2),\qquad
 F_{i,i'}=\frac{2A_i A_{i'}-\mathbf1_{\{i,i'\}=\{1,2\}}L_\rho}{Z_*}\quad(i<i').
\]
Each numerator vanishes at all QAP points: \(A_i\) has nonzero point values only at its own tag point and \(\rho\), and \(L_{3-i}\) only at the other tag point; two distinct tag coordinate polynomials overlap only for tags one and two at \(\rho\), where the product with factor two is \(2c_*^2=1\). The degrees of these quotients are at most \(D-2\). Send the \(N+1\) values \([\zeta_0 G_j(\tau)]_1\), and for each of the five \(F\)'s send \([\zeta_0 F(\tau)]_1\) and \([\zeta_0(\tau-\rho)F(\tau)]_1\). There are \(N+1+10\) left entries. For every cell \(c\), send two right entries
\[
 B^{(i)}_c=[\gamma_c U(\tau)A_i(\tau)/\zeta_0]_2,\qquad i=1,2 .
\]
Their generation uses the scalar evaluations and the schedule in C7.

As before all full combinations use the same third tag \(t\). Let \(v_0=(w,0,0,t)\) and \(v=(w,b_1,b_2,t)\), and let \(d_v=b_1b_2\). They have the same allowed remainder \(R_w\). Put \(G_w=\sum_{j=0}^Nw_jG_j\) and
\[
 F_v=b_1F_1+b_2F_2+b_1b_2F_{1,2}+tb_1F_{1,3}+tb_2F_{2,3}.
\]
For either \(i=1,2\), the part of \(P_v-P_{v_0}\) linear in \(b_i\) excluding mixed terms is \(A_i(S_w+A_i)\), where \(S_w=\sum_jw_jS_j\); this uses \(b_i^2=b_i\). By the definition of \(G_w\) and \(w_0=1\),
\[
 A_i(S_w+A_i)=U A_i G_w-A_i L_{3-i}.
\]
The mixed terms are the three products already handled in the \(F_{i,i'}\), including the subtraction of \(d_vL_\rho\). Hence the exact polynomial identity is
\[
 P_v-P_{v_0}-d_vL_\rho=U(b_1A_1+b_2A_2)G_w+Z_*F_v.
\]
Compute the one ordinary witness sum \([\zeta_0 G_w(\tau)]_1\) once. For each full variant, use the paired weighted right entries \(B^{(i)}_c\) for the present bits. For each present bit do the MSM of length \(A_c\), then when both are present add the two MSM outputs before pairing with the same left witness sum. The polynomial multiplier for cell \(c\) is precisely \(\gamma_c U(b_1A_1+b_2A_2)G_w\). If both bits are zero, this pairing is omitted. For the fixed part add \([\zeta_0F_v(\tau)]_1\) to the sparse key operand and \([\zeta_0(\tau-\rho)F_v(\tau)]_1\) to the sparse non-key operand, using the two sets of fixed left entries. The two resulting sparse pairings incorporate \(\gamma_c Z_*F_v\) for their respective cells because \(Z_*=(X-\rho)Z\). The non-key sparse operand still receives \(d_vP_0^0/Z(\rho)\) separately. Combining these contributions with the baseline sparse and nonsparse operands subtracts \(P_v-d_vL_\rho\) in the key cell and \(P_v\) elsewhere.

In the hidden-basis comparison, the new left inputs are polynomials of the existing \(\zeta_0\) type. The two new right lists are of inverse scale \(\zeta_0^{-1}\), with \(\gamma_c\) and a polynomial multiple of \(Z_*\) and with no other variables. Their pairs with any left input of scale \(\zeta_0\) yield multiples of \(Z_*\), and pairs of old sparse right inputs with new left inputs yield multiples of \(Z_c\). The generic comparison therefore absorbs the entire enlarged class into \(Z_c h_c\), with the same residue restrictions on the other class. The constant-polynomial coefficient bounds the final quotient as in C7. All new left exponents have total degree at most \(D\), and the new right list degree is covered explicitly in C7. The shared third-tag selection changes neither exponents nor coin laws.

### A single combination at any tag

For \(v_0=(w,0,0,t)\) the key corner is zero. By Amendment D, \(G_{\rm base}=P_{v_0}/Z_0\) is exact and equals \(Z_{\mathcal K}h_{\rm key}^{v_0}+R_w\). Compute its sparse part by retaining the multiples of \(\nu\), and divide that part by \(Z_{\mathcal K}\) in the variable \(X^\nu\) to obtain \(h^0\), the sparse part of \(h_{\rm key}^{v_0}\). The complementary part \(T_0=G_{\rm base}-Z_{\mathcal K}h^0\) has degree below \(U_*\) and is formed by deleting sparse coefficients of \(G_{\rm base}\), so every retained exponent is nonzero modulo \(\nu\). Polynomial products and monic divisions here take \(O(D\log D)\) field operations: after reversal a monic divisor has constant term one, and the update \(u\leftarrow u(2-fu)\) doubles the correct inverse precision since its residual equals \((1-fu)^2\). For each precision, products use the C3 power-of-two subgroup and split lengths \(O(D)\) into a bounded number of blocks of length at most half the subgroup order. The sum over the doubling precisions is \(O(D\log D)\). Only the witness polynomials are interpolated and the compressed sparse division has length \(O(D/\nu)\).

Once compute
\[
 H^0=\sum_{a\in I_0}[X^a]h^0\,P_a^0,\qquad
 H_{\rm oth}^0=\sum_{a\in I_0}[X^a]h^0\,P_{a+1}^0-\rho H^0,\qquad
 H_j^1=\sum_{\substack{a\in I_1\\j\Delta+a<U_*}}[X^{j\Delta+a}]T_0\,P_a^1 .
\]
For each full combination adjust the first operand by the fixed key-tag terms and pair with \(\xi_{\rm key}(v)B^0_{\rm key}\). Adjust the second by the shifted fixed tag terms and \(d_vP_0^0/Z(\rho)\) before pairing with the weighted non-key \(B^0_c\), and pair each \(H_j^1\) with the \(v\)-weighted \(B^1_{c,j}\) sum. Also subtract the shared direction pairing when a first or second tag bit is present, as above. The polynomial argument in the preceding subsection shows these subtractions remove exactly the \(P_v-d_vL_\rho\) and \(P_v\) terms for the key and other cells, respectively.

For each right leg, form the two weighted left operands by summing \(\xi_c(v)\) times the witness-summed G1 factor of its left leg over the cells at this right leg. Pair them with the two witness-summed right coordinates. In the resulting sum the hidden basis cancels, the two antisymmetric terms \(y(v)A_v-A_v y(v)\) cancel, and the masks are subtracted with the cancellation MSM of C7 paired against the witness-summed Y. The earlier polynomial subtractions remove all \(P_v\) terms except the stated key corner. The first weighted left operand alone is the sum of the left first coordinates; pairing it separately with the search base \(s_{\rm leg}\) at each right leg and summing gives
\[
 \Psi_v=[\psi_v]_T,\qquad \psi_v=y(v)\sum_c\gamma_c\xi_c(v).
\]
The full corrected sum is
\[
 \Lambda_v=[d_v\xi_{\rm key}(v)\kappa+r(v)\psi_v]_T .
\]
To evaluate just \(\Psi_v\) there is no use of the second factor coordinate, QAP correction or cancellation.

### Finite work of the scalar baseline

For the scored subgroup placement put \(M=2^{22}\), \(L=2M\), and choose a public scalar \(c\) of order \(2L\). Then \(c\mathcal H_L\) and \(\mathcal H_M\) are disjoint. The public system representation can include the fixed interpolation scalars and tables used below. They depend only on the selected points and field and are determined when the system is encoded. They add no group element or field value to the ciphertext.

For the ordinary polynomials \(F=A_{(w,0,0,0)},B_{(w,0,0,0)}\), partial fractions give
\[
 F(X)=\frac{Z_*(X)}{X^M-1}
      \sum_{j=0}^{M-1} X^j\sum_{p\in\mathcal P}\frac{F(p)p^{-1-j}}{Z_*'(p)} .
\]
Indeed the partial fraction identity for \(F/Z_*\) holds by evaluation at all QAP points, and multiplying each term by \(X^M-1\) gives the geometric sum because \(p^M=1\). Encode each public point coefficient with its fixed factor \(1/Z_*'(p)\). After additions selected by the witness bits, multiply the aggregate value for each point by its fixed \(1/p\) to obtain the exact transform input weight from the displayed identity. Both arrays take at most \(2D<8\) million multiplications for this normalization. Encryption uses the same encoding and the cofactor product proved in C7.

For each polynomial use one length-\(M\) transform for the displayed coefficient array and one for its evaluation on each of the two cosets of \(\mathcal H_M\) in \(c\mathcal H_L\). Scale the coefficients by the respective fixed coset powers before the latter transforms. Both arrays take six transforms and at most \(4M\) scalings. When the selected third tag is one, add the two precomputed tag contributions to the respective evaluated numerators. For each of \(F=A,B\), the public tag-three table at shifted point \(x\) has entry \(F_{\rm tag,3}(x)(x^M-1)/Z_*(x)\), where \(F_{\rm tag,3}\) is its QAP coordinate polynomial for that tag. The powers and quotients here depend only on the public points and can be evaluated at setup with the same subgroup transforms in \(O(D\log D)\) work. Because the selected third tag is a bit, this adds no multiplications at decryption. At each shifted point multiply the two evaluated numerators and the fixed factor \(Z_*^2/(LZ_0(X^M-1)^2)\). The factor is defined because the domains are disjoint. Then apply one unnormalized inverse transform of length \(L\), and at most \(U_*\) multiplications by powers of \(c^{-1}\) to recover the actual coefficients of \(G_0\) in the variable \(X\). This works since the quotient is exact and its degree is below \(U_*<L\). It takes below 390 million multiplications, including the small sparse division and the \(2L\) pointwise products. For the transform count, the radix-two butterfly stages have at most \(B\log_2(B)/2-(B-1)\) non-unit twiddles at length \(B\), since each block has a unit first twiddle and the numbers of blocks sum to \(B-1\). The sparse division uses the fixed reversed monic inverse on prefixes of length at most \(1884\), by a convolution at length 4096. For choices of points outside the scoring placement, the unshifted polynomial construction preceding this paragraph uses interpolation and exact division directly.


For the finite matrix evaluation, write the packed witness entries as bits \(b_{j,t}\) in the ordinary power basis. In row \(i\), first sum the tuples \(E(M_{ij})\) for which \(b_{j,t}=1\), separately for each possible \(t\). This costs additions only. Multiply each tuple sum componentwise by the fixed tuple \(E(Y^t)\) and sum the results. Evaluation is a ring isomorphism, so applying \(E^{-1}\) once to this total yields the coefficient vector of the ordinary witness product. Convert the three individual tag-column tuples with one inverse each in that row; the homogeneous column is included with its ordinary bit value one at position zero. There are at most \(kd^2\) scaling multiplications, plus \(4kd^2\) for the inverse matrices. Thus this implementation uses at most \(5kd^2\le 5\cdot4800\cdot 23<5376000\) multiplications, using \(d=23\) and \(kd\le n\le4800\). The other work consists of at most \(O(k(\ell+1)d^2)\) additions, a constant multiple of the finite matrix length for the admitted degree. This gives the previous scalar allowance with the actual period ring.

The weights of the at most eight needed form values use three conjugate applications with at most \(3s_0 n\) multiplications per variant. The two products for \(U,V\) fit length-16384 FFTs. Their monic reductions each take at most \(s_0 n\) multiplications, because there are at most \(n\) elimination steps with at most \(s_0\) lower terms per step. With \(s_0\le128\), \(n\le4800\), the conjugations and reductions use at most \(40s_0n\le24576000\) multiplications. The sixteen products use at most \(16(3T(16384)+2\cdot16384)<6\) million more by the nonunit twiddle bound, pointwise products and inverse scalings. All weights therefore fit within 32 million.

For each of at most four full mask combinations, form the six weighted leg polynomials. The jointly conjugated representatives have at most \(2s_0-1\) terms, and there are at most three additional one-sided conjugated products of support at most \(s_0\) per cell, plus the fixed ordinary products. Use the upper bound \((3n/2)(5s_0+2)\) multiplications per full combination, which suffices also when a cell is used in only a subset of these products. Nine length-16384 forward and eight inverse transforms compute the twelve polynomial products after selecting the six weighted legs and three conjugate forms. All polynomial degrees are below \(3n\le14400\), so this covers the entire output support. Together the FFTs, pointwise products and the eight inverse scalings take less than 2.1 million multiplications per variant. Exact monic division of the first three outputs takes at most \(6ns_0\) more multiplications per variant, by the degree and support bounds of the sparse monic modulus. The complete mask preparation therefore costs below 43 million across four full combinations.

The large QAP scalar preparation, including the required compressed sparse divisions and scalings, costs at most 390 million multiplications by the preceding derivation including the point-wise normalization. Adding the 32-million weight, 43-million mask, 5,376,000 matrix conversion and remaining fixed costs gives fewer than 471 million scalar multiplications. For the remaining counts, throughout the at most four full tag combinations the scalars outside the counted tables are the fixed multiples of the sparse basis, \(d_v\), \(\xi_{\rm key}(v)\), and the key inverse; their computation uses fewer than one thousand further multiplications even using binary exponentiation for the inverse. The protected \(632000000+m\) allowance covers this finite total. The matrix entries themselves were traversed using additions and only the counted coefficient conversions.

### Tag choice and key recovery

For any external witness \(w\) and \(t\in\{0,1\}\), set \(a_t=(w,1,0,t)\), \(b_t=(w,0,1,t)\), \(c_t=(w,0,0,t)\), and \(v^{(t)}=(w,1,1,t)\), all with homogeneous coordinate one. The three ordinary corners have zero key corner and \(a_t+b_t-c_t=v^{(t)}\) as integer vectors. The target has key corner one.

Return \(\bot\) if \(\xi_{\rm key}(v^{(0)})=0\). Otherwise if \(\Psi_{v^{(0)}}=0\), compute its one full combination and normalize directly with its nonzero key weight. If the primary target base is nonzero and \(\Psi_{a_0},\Psi_{b_0},\Psi_{c_0}\) are all nonzero, choose the ordinary triple with \(t=0\). Otherwise test \(\xi_{\rm key}(v^{(1)})\). If it is zero, take the evaluation-point fallback. With nonzero secondary weight, compute \(\Psi_{v^{(1)}}\). If that base is zero, use its direct normalization. If it is nonzero and \(\Psi_{a_1},\Psi_{b_1},\Psi_{c_1}\) are all nonzero, select the ordinary triple with \(t=1\). Otherwise take the fallback. This uses at most eight plain base tests and four full combinations. All full combinations in the chosen path have common third tag \(t\), so they need one baseline. Let \(v_*\) denote the selected target in an ordinary branch. Branch selection depends only on the bases and form weights, independently of the search coins.

For the selected triple, use \(v_0'=c,v_1'=a,v_2'=b\) and let \(c_0,c_1,c_2\) denote the rounded centers of the anchor and differences. Before starting line [full-search], form
\[
 Q_0=\Lambda_c-c_0\Psi_c,\qquad
 Q_1=\Lambda_a-(c_0+c_1)\Psi_a,\qquad
 Q_2=\Lambda_b-(c_0+c_2)\Psi_b .
\]
The line solves \(Q_0=t_0\Psi_c\), then solves \(Q_1-t_0\Psi_a=t_1\Psi_a\) and \(Q_2-t_0\Psi_b=t_2\Psi_b\). The two multiplications by the already recovered \(t_0\) use signed binary arithmetic on \(|t_0|\), with sign handled by the fixed Frobenius inversion. These are the only group products that translate targets within the search. The output is the three centered logarithms in the record below. The later key computation forms \(r(v_*)=c_0+c_1+c_2+t_0+t_1+t_2\), subtracts \(r(v_*)\Psi_{v_*}\), and multiplies by the inverse key weight. This gives \([\kappa]_T\). One key-oracle query unmasks the message. At most eight \(\Psi\) values and four full \(\Lambda\) values are needed, and the triple choice is independent of the search vector.

### Exact fallback when no ordinary triple is available

This fallback runs only after the nonzero key-weight test has passed and the target base is nonzero, when the selector supplies neither a triple with nonzero target weight nor a direct normalization. The sparse G1 list contains \(P_0^0\) and \(P_1^0\) because \(0\in I_0\) and \(1\in I_0^*\). Before entering the unified search line, pair each one with the published key-cell operand \(B^0_{\rm key}\). The results are
\[
 E_0=[\gamma_{\rm key} Z_*(\tau)]_T,\qquad
 E_1=[\gamma_{\rm key} Z_*(\tau)\tau/c_{\rm q}]_T ,
\]
where \(c_{\rm q}=1\) for unscaled powers. The exponent of \(E_0\) is nonzero because the key scale is nonzero and \(\tau\) is outside the QAP points. The public polynomials satisfy \(Z_*=(X-\rho)Z\) and \(L_\rho=Z/Z(\rho)\). The fallback computes the unique discrete logarithm \(j\in\{0,\ldots,q-1\}\) with \(jE_0=E_1\), by the following direct-key procedure. At stage \(h\ge0\), let \(w=2^h\). Tabulate \(iE_0\) for \(0\le i<w\), starting at the identity. Beginning at \(E_1\), check the \(w\) giant residuals obtained by successive steps of \(-wE_0\). A match at giant index \(k\) and baby index \(i\) gives \(j=kw+i\). Accept only \(j<q\). Each stage thus covers all nonnegative integers below \(w^2\) that lie in the index range, and distinct accepted indices cannot have equal group value. The first stage with \(w^2>j\) is sufficient. For the stride, invert \(E_0\) by the fixed Frobenius map of Amendment search_spread once, then double \(h\) times per stage. Equality of polynomial-basis target elements suffices for lookups. After finding \(j\), compute
\[
 K=\frac{1}{(c_{\rm q}j-\rho)Z(\rho)} E_0
\]
and use its key-oracle value to recover the message. Because \(E_0\ne0\), its order is \(q\) and \(j\) is exactly \(\tau/c_{\rm q}\) in the field. The denominator is nonzero and \(K=[\kappa]_T\), including when \(j=0\). The traversal is the evaluation-point mode of line [full-search]. It returns the index as the fourth component, and the arithmetic after the line computes the displayed key group element.

The fallback uses two pairings of operands already present in the ciphertext. It publishes no new value. In the generic security experiment these pairings remain ordinary formal expressions of the same exponents analyzed in C7. The proof of extraction treats every adversarial sequence of calls within the stipulated adversary budget. That quantifier is independent of the cost of the honest evaluation-point traversal.

**One search line and its actual result.** The revised line [full-search] receives the selected mode and the corresponding group operands. On the ordinary mode for the chosen triple, the public centers \(c_0,c_1,c_2\) are the rounded centers of the anchor and the two increments. The line returns
\[
 T=(r(c)-c_0,\ r(a)-r(c)-c_1,\ r(b)-r(c)-c_2,\ 0).
\]
On the direct-key mode, the same line instead traverses the evaluation-point logarithm search above and returns \(T=(0,0,0,j)\). The index \(j\) is the nonnegative solution in \([0,q-1]\) to the displayed group equation, and the other three coordinates are zero. The divisor for key normalization is applied afterward using this fourth returned component. On a bypass branch no logarithm is computed and \(T=0\). The line also returns the signed component \(t\) of largest magnitude with the smallest index breaking ties. This designated scalar result is an actual recovered logarithm, with \(|t|=\|T\|_\infty\). The witness-sampler range \([-B,B]\) is used for the first three coordinates. The separate input-domain range \([0,q-1]\) for the fourth comes from the order of its nonzero base. The RMS and pointwise bounds below cover this entire record, including its fourth component. Reconstruction and group normalization follow the line on either path.

### View of the correction polynomials

The sparse quotient bases and the common-direction right lists are the inputs with inverse scale \(\zeta_0^{-1}\), and only the combined correction bases have inverse scale \(\zeta_1^{-1}\). The key-scalar degree class in C7 therefore collects the original and tag-difference terms in each cell as \(Z_c h_c^0+Z_0 T_c\), with every exponent of \(T_c\) in a nonzero residue class modulo \(\nu\). Monic division of \(T_c\) by \(Z_{\mathcal K}\) preserves those classes in every subtraction step. Its remainder \(R_c\) has degree below \(\nu n_{\mathsf c}\) and is allowed. Multiplying the multiple part by \(Z_0\) gives a multiple of \(Z_*\), hence of \(Z_c\), and it is absorbed into \(h_c\). Thus the arbitrary correction is precisely of the required \(Z_c h_c+Z_0R_c\) form. The constant-term comparison in C7 bounds the quotient degree by the QAP criterion, and the changed corner is \(W_{t_1,t_2}\) from that criterion. Every other Laurent comparison uses the same input types and the same actual field ties, as proved in C7, with the two-sector copies omitted.

## Amendment n2

The exact half-count is
\[
 n_2=\left\lceil\frac{6K_2(N+4)+3K_2+(3n/2)(J+3)+C_{\rm mask}}2\right\rceil .
\]
The first two terms count the single right factor arrays and search bases. There is one sparse list of \(A_c\) bases, two common-direction right lists of \(A_c\) bases and \(J\) combined lists of \(A_c\) bases, and the cancellation count is \(C_{\rm mask}\). The optional generator padding gives \(2n_2\) actual slots. The G1 count is proved in n1. Together with the fixed one GT element, seed and masked message, these give exactly the protected size formula and the one-generator-multiplication count from the published scalars.

## Amendment dec_sum_g1

Compute external witness sums of the two coordinates of each left leg and the Y column once with tags omitted, using at most \((N+1)/2\) additions per array in the witness-weight convention. The at most eight variants add at most three tag entries per array. The one common-direction witness sum uses at most \((N+1)/2\) additional additions. For each full combination add at most five fixed entries to each of its two sparse operands and add at most one further fixed multiple to the non-key operand. Allow 64 additions for these adjustments across the at most four combinations. The total bound is \((2K_1+1)((N+1)/2+24)+(N+1)/2+64\).

## Amendment dec_sum_g2

For the single right factor sector, compute each of the \(6K_2\) external witness coordinate sums once, using at most \((N+1)/2\) additions each. Only the at most four full combinations need these sums with tags added; each adds at most three entries. Only the target variant has both tag bits set and needs one addition to combine its two direction MSM results. Thus the count is \(6K_2((N+1)/2+12)+1\). The fixed search bases require no analogous coordinate sums.

## Amendment dec_msm_g1

The at most eight first-coordinate weighted left operands and four second-coordinate ones each use \(A_c\) points. The baseline sparse key and non-key MSMs use \(S_0\) and at most \(S_0+1\) points respectively. Charge one more point for the fixed multiple \(P_0^0/Z(\rho)\), computed and reused. The baseline non-sparse correction uses \(U_*-(S_0+n_{\mathsf c})\) points. These QAP operands are each computed once and shared, and the common-direction witness sum and fixed-entry adjustments were counted as additions. The bound is therefore
\[
 12(3n/2)+D-1+S_0+2+(\nu-1)n_{\mathsf c}.
\]

## Amendment dec_msm_g2

Each full combination uses \(A_c\) points for the two sparse right operands together, \(J A_c\) for the combined right list and \(C_{\rm mask}\) for cancellation. The four variants at a common third tag have zero, one, one and two present bits, respectively, in the common-direction computation. No variant needs to be used more than once for a full combination. Thus the total count of points in the two common-direction MSM lists across all full variants, including the direct-normalization case with only the target, is at most \(4A_c\). The resulting bound is \(4((3n/2)(J+2)+C_{\rm mask})\). The \(\Psi\) combinations use the fixed right search bases without new G2 MSMs.

## Amendment dec_pairings

Each of the at most eight \(\Psi\) sums uses \(3K_2\) pairings. Each of at most four \(\Lambda\) sums uses \(6K_2\) factor pairs, \(J\) combined correction pairs, two sparse pairs, at most one common-direction pair and one cancellation pair. Thus the total is at most \(24K_2+4(6K_2+J+4)\). Accumulate each signed sum starting with its first term, updating by the indicated group addition or subtraction. This needs at most one fewer accumulation operation per nonempty sum than its pairing count. The remaining bounded number of GT translations, final normalizations and searches are accounted for in search_spread.
The exceptional fallback follows the search-base computations and performs two additional pairings with the already transmitted sparse bases. It uses no full combination. Its pairing count is at most \(24K_2+2\), within the same bound.

## Amendment search_spread

Let \(\sigma^+=g\sqrt{(N+7)/48}\), \(R_0=\sigma^++3/2\), and define
\[
 M_0=\begin{cases}
 (7979/10000)\,g\sqrt{(N+7)/48}+3/2 & 359994\le N\le479993,\quad g\ge10^{12},\\
 (803/1000)\,g\sqrt{(N+7)/48}+3/2 & \text{otherwise when }N\ge359994,\\
 R_0 & N<359994 ,
 \end{cases}
 \qquad M_1=g/4+1/2 .
\]
The amended spread is
\[
 \max\left\{ R_0,\ R_T,\ 
   \left(\frac{20}{37}\big((10001/10000)((83687/50000)\sqrt{\sigma^+}+(8/3)\sqrt{g/2})+402180\big)\right)^2\right\},
 \qquad R_T=g\sqrt{(N+23)/48}+14 .
\]
Here \(M_0\) bounds the expected absolute centered anchor, and \(M_1\) bounds an increment in the first-listed triple. The amended arithmetic cost uses the sharper concurrent-anchor bound proved below. The branch selection is independent of the search vector, so the anchor bound applies on any chosen triple. The two additional quantities \(R_0\) and \(R_T\) cover the RMS of the recombined centered integer and the full search record respectively.

For the ordinary search record, the exactly centered variables have second moments bounded by \((g^2-1)(N+7)/48\) for the anchor and \(2(g^2-1)/12\) for each increment, since each increment involves at most two independent uniform box samples with opposite coefficients. The square of the Euclidean norm is a sum of squares regardless of their correlations. The vector of rounding errors has Euclidean norm below \(2\), since the anchor error is at most \(3/2\) and each increment error at most \(1/2\). The triangle inequality in square mean bounds the ordinary part of the record by \(g\sqrt{(N+23)/48}+2\). The fourth component is zero except on the direct-key fallback whose probability is at most \(135/q^2\) by Targets. Since \(0\le j<q\), its root mean square is at most \(\sqrt{135}<12\), even with arbitrary dependence between the branch and \(j\). Summing these square-mean bounds gives \((\mathbb E\|T\|_2^2)^{1/2}\le R_T\), which also bounds the RMS of the signed greatest component. The first three coordinates meet the range bound from Bsearch and the stated width of any two box samples, and the evaluation-point coordinate meets its stated range.

### Expected absolute anchor

Before the rounding error of at most \(3/2\) in Bsearch, the center removes the mean, leaving the sum of independent symmetric variables
\[
 S=X_\diamond+\sum_{i=1}^{N+3}(v_i-1/2)X_i ,
 \qquad X_i=r_i-(g+3)/2 .
\]
Its standard deviation is \(\sigma_S=\sqrt{(g^2-1)(N+7)/48}>0\). Let \(Y_i\) be its summands divided by \(\sigma_S\), using one more index for the independent diamond term. Set \(v_i'=\mathbb E Y_i^2\) and \(v_{\max}=\max_i v_i'\). The ordinary summands have \(v_i'=1/(N+7)\), the diamond summand has \(v_i'=4/(N+7)\), and \(\sum_i v_i'=1\). Each \(|Y_i|^2\le3v_i'\) because the square of the largest deviation of an integer uniform sample of width \(g\) is \((g-1)^2/4\) before scaling, and the variance is \((g^2-1)/12\). It follows that \(\mathbb E Y_i^4\le3(v_i')^2\).

Write \(\phi_i(t)=\mathbb E\cos(tY_i)\), \(\psi_i(t)=\exp(-v_i't^2/2)\). For \(0\le t\le300\) and \(N\ge359994\), put \(w_i=v_i't^2\le1\). Both \(\phi_i(t)\) and \(\psi_i(t)\) belong to \([1-w_i/2,1-w_i/2+w_i^2/8]\). For cosine the lower bound follows from \(1-\cos x\le x^2/2\), and the upper bound follows from Taylor's theorem to degree three with fourth derivative at most one and the fourth-moment estimate above. For the exponential use Taylor's theorem with its second derivative at most one on the nonnegative half-axis for \(\exp(-x)\). Both functions are nonnegative on this interval and at most \(1-3w_i/8\le \exp(-w_i/3)\). Symmetry and independence make \(\phi=\prod_i\phi_i\) the characteristic function of \(S/\sigma_S\). The product \(\psi=\prod_i\psi_i\) is the characteristic function of a standard normal. Telescoping the products, using one difference \(|\phi_i-\psi_i|\le w_i^2/8\) and bounding each other factor by its exponential, yields
\[
 |\phi(t)-\psi(t)|
 \le \frac{t^4}{8}\sum_i(v_i')^2
          \exp\big(-(1-v_{\max})t^2/3\big)
 \le \frac{t^4}{720000}\exp(-t^2/4).
\]
The last inequality uses \(v_{\max}\le1/90000\), \(\sum_i(v_i')^2\le v_{\max}\), and \(1-v_{\max}\ge3/4\).

For real \(x\),
\[
 |x|=\frac2\pi\int_0^\infty\frac{1-\cos(tx)}{t^2}\,dt .
\]
To verify the constant, scale by \(|x|\) when \(x\ne0\), then integrate by parts to obtain \(\int_0^\infty\sin(t)/t\,dt=\pi/2\). In the integral with a factor \(\exp(-at)\), \(a>0\), differentiating in \(a\) gives \(-1/(1+a^2)\) and the integral tends to zero as \(a\) tends to infinity. It therefore equals \(\arctan(1/a)\). Ordinary integration by parts bounds the damped tail uniformly in \(a\) by \(2/T\) after \(T>0\), since \(\exp(-at)/t\) is positive decreasing. This justifies the limit as \(a\) decreases to zero. The case \(x=0\) is immediate. The integrand of the absolute-value identity is nonnegative, so expectation can be taken inside. The normal absolute moment is \(\sqrt{2/\pi}\) by integrating its density on the two half axes. Its characteristic function \(\exp(-t^2/2)\) follows from differentiating the integral of its density times \(\exp(itx)\), integrating by parts to obtain \(\psi'(t)=-t\psi(t)\), and using \(\psi(0)=1\).

The two characteristic functions have absolute values at most one for every \(t\). Using their sharper bound up to 300, the triangle inequality gives
\[
 \frac{\mathbb E|S|}{\sigma_S}
 \le \sqrt{2/\pi}+
 \frac{2}{720000\pi}\int_0^\infty t^2e^{-t^2/4}\,dt+
 \frac{4}{300\pi}
 < \frac{803}{1000}.
\]
For the inequality the middle integral is \(2\sqrt\pi\) by substituting \(u=t/2\) and integrating by parts, and \(\pi>3.14\) suffices for the final numerical comparison. Adding the rounding error yields \(M_0\), with Cauchy--Schwarz giving the alternate bound at smaller \(N\).

For the scored range \(359994\le N\le479993\) and \(g\ge10^{12}\), the cosine bound can be continued beyond frequency 300. Each of the \(N+3\) ordinary summands has spacing \(1/(2\sigma_S)\) after normalization, up to sign, with distribution symmetric about zero. The finite geometric sum yields its characteristic function
\[
 \frac{\sin(gu)}{g\sin u},\qquad u=\frac{t}{4\sigma_S}.
\]
Here \(\sigma_S/g\le100\) by \(N+7\le480000\). Also \(\sigma_S\ge g\) since \(g\ge2\) and \(N+7\ge360000\). Thus \(300\le t\le10^6\) gives \(gu\ge3/4\) and \(0<u<1/100\). The function \(\sin v/v\) decreases from 1 on \([0,\pi]\): the derivative numerator \(v\cos v-\sin v\) is zero at zero and has derivative \(-v\sin v\le0\) there. For \(v\ge\pi\), its absolute value is at most \(1/\pi\). Taylor's bound on \(\sin(3/4)/(3/4)\) and the lower bound \(\sin u\ge u-u^3/6\) therefore give
\[
 \left|\frac{\sin(gu)}{g\sin u}\right|
 \le \frac{1-(3/4)^2/6+(3/4)^4/120}{1-(1/100)^2/6}<\frac{91}{100}.
\]
Both Taylor bounds follow from the alternating power series on the given fixed intervals. Since \((91/100)^8<1/2\) and \(N+3\ge320\), the product of the ordinary factors is bounded in absolute value by \(2^{-40}\) on this frequency interval. The diamond factor has absolute value at most one and the normal factor is also at most \(2^{-40}\) for \(t\ge300\). Thus the middle integral contributes less than \(2^{-40}\) after its \(2/\pi\) normalization. The tail above \(10^6\) contributes at most \(4/(\pi10^6)\).

The normal first absolute moment is less than \(797886/10^6\). For an exact bound, \(\pi>314159/100000\) follows by the tangent addition formula from \(\pi/4=4\arctan(1/5)-\arctan(1/239)\) and the alternating bounds through the \(-x^7/7\) term for the first arctangent and \(x\) for the second. Indeed the tangent of \(4\arctan(1/5)\) is \(120/119\), and the indicated difference has tangent one and lies between zero and \(\pi/2\). These rational bounds give
\[
 16\left(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}-\frac1{7\cdot5^7}\right)
 -\frac4{239}>\frac{314159}{100000},\qquad
 \frac{314159}{100000}\left(\frac{797886}{10^6}\right)^2>2 .
\]
The low-frequency error is at most \(1/(180000\sqrt\pi)<1/300000\), by the same low-frequency integral used above. Summing the errors gives
\[
 \frac{\mathbb E|S|}{\sigma_S}
 < \frac{797886}{10^6}+\frac1{300000}+2^{-40}+\frac2{10^6}
 < \frac{7979}{10000}.
\]
Adding the rounding allowance again gives the selected \(M_0\).

### Relative searches and fallback work

A centered single box sample has absolute mean at most \(g/4\). For \(g=2m\), the sum of the \(2m\) distances from the midpoint is \(2\sum_{i=1}^m(i-1/2)=m^2\). For \(g=2m+1\), the sum is \(2\sum_{i=1}^m i=m(m+1)\), giving absolute mean \((g^2-1)/(4g)\). Rounding a public center adds at most \(1/2\). Both increments of the first-listed triple are single box samples, so each uses \(M_1\). Any other triple uses increments with RMS at most \(M_\Delta=g/\sqrt6+1/2\) by the second-moment and rounding bounds just proved. Use this as the expected absolute bound on those triples. The probability of needing either later triple is at most \(9/q\), as follows by the union bound over the three zero bases in the first. The increase in expected primary candidates is at most \((9/q)4\sqrt{M_\Delta}\le 36/\sqrt q<1\) since \(g+1<q\) and the protected prime exceeds \(1296\). All ordinary search integers remain within \(B\).

**Amended Proposition 5.7(c).** Decryption uses at most the source-group sums, MSM lengths and pairing counts proved in their respective amendments. In addition it takes at most 1024 target-field accumulator products at the scored shape for the signed pairing sums and at most 400 further target products for fixed combinations, initialization, and search setup. In this bound, shared final exponentiation remains part of the protected pairing charge. Apart from the baby and giant traversals themselves there are at most five scalar multiplications for the ordinary decryption path and two stride multiples per bounded witness logarithm, so at most eleven target-group scalar multiplications. The five are the three center translations, the subtraction of the recovered search term, and the multiplication by the inverse key weight. The branch with zero distinguished target base uses at most one scalar multiplication, and the direct-key recovery branch uses only one scalar multiplication after recovering its evaluation-point index. The admissible upper bounds therefore hold pointwise on all branches outside the single line [full-search]. The arithmetic price for these products, including basis conversions, is proved below.

**Amended Proposition 5.7(d).** Line [full-search] in n1 takes \(O(\sqrt{\|T\|_\infty}+1)\) target-group operations on its actual result \(T\). Equivalently its cost is \(O(\sqrt{|t|}+1)\) for the signed largest emitted logarithm. On the ordinary mode of that line this follows from the three component bounds below. On the direct-key mode it follows from the adaptive evaluation-point search and the equality \(\|T\|_\infty=j\). The same output and pointwise bound therefore cover both traversals. All auxiliary arithmetic during decryption besides these traversals is covered by (c). The expected group work in the line is \(O(\sqrt g\,N^{1/4})\) on an honest ciphertext.

The direct-key mode of the search line has probability at most \(135/q^2\), by Targets. In this mode stage width \(w=2^h\) takes fewer than \(w\) baby updates, fewer than \(w\) giant updates, at most \(h\) doublings and bounded setup. With one inverse of \(E_0\) via the fixed \(p^6\) Frobenius, at most four target operations per unit width including setup suffice. The stage search cost is therefore \(O(w)\), and the sum of widths through the first width with \(w^2>j\) is less than twice that width, while the final width is at most \(2\sqrt{j+1}\). This gives the claimed bound for the fourth component. In particular there are at most \(16\sqrt q+600\) operations of cost at most a target product, including the final scalar multiple outside the line. Its two pairings are included in dec_pairings. Its scalar-field denominator formation and inversion cost less than one multiplication in expectation at the protected prime and fit the protected scalar allowance.

The primary fixed-width traversal gives the expected-cost bound, and the interleaved traversal below supplies the pointwise guarantee of Proposition 5.7(d). For any centered target \(x\) known to have \(|x|\le B\) and \(\mathbb E|x|\le M\), use the sign-class baby and giant search with integer width \(b=\lceil\sqrt M\rceil+1\). Tabulate \(iP\) for \(0\le i<b\), where \(P\ne0\) is the base. The signed intervals centered at \(j(2b-1)\) with radius \(b-1\) partition the integers. Progress outward in the order \(j=0,1,-1,2,-2,\ldots\), testing the sign class of the corresponding residual against the table. Verify the sign and the resulting integer against the bound; \(2B+1<q\) makes the bounded solution unique. A match for the true integer occurs by \(|j|\le |x|/(2b-1)+1\). The baby construction has at most \(b\) counted steps. Its stride follows from the last baby point by a doubling and one addition. Maintain separate accumulators for positive and negative giant indices, so alternating the direction advances the selected accumulator with one update. Including a constant for initialization and verification, the total is at most \(b+2|x|/(2b-1)+12\) steps on a true target. This bound includes names and the constant work to derive their signs according to the protected step convention. A run with no valid solution can stop upon exploring all intervals intersecting \([-B,B]\). Since \(2b-1\ge2\sqrt M\), its expected bound on a valid sampled target is at most \(2\sqrt M+14\). A nonzero base is always used for these searches.

### Concurrent tables for the finite signed logs

The anchor uses the two-phase schedule derived below. Use the following balanced schedule for each increment of the first triple. For either increment of a later triple use the preceding fixed-width primary search with \(M_\Delta\). In the balanced schedule take \(A=g/2\), put \(a=\sqrt A\), \(b=\lceil a\rceil+1\), and \(s=2b-1\). Before entering the search line compute both signed strides \(sP,-sP\) at the already available base \(P\), using the two stride-multiple allowances. Produce the baby entries in order \(0,P,\ldots,(b-1)P\). Produce the giant residuals \(Q-jsP\) for the known centered target group element \(Q\) in the order \(j=0,1,-1,2,-2,\ldots\), maintaining two accumulators. Only one new group value is needed for each entry. While both lists have entries left, alternate one baby entry with one giant entry. If all legal giant entries have been produced first, continue the baby list and query the retained giant table. Once the baby list is complete, continue producing any remaining giant entries without retaining them, and release the already stored giant entries.

Store both lists by the protected sign-class naming operation. On a new entry, query the other list before inserting it into its own list, and recover and test signed indices exactly as in the original fixed-width traversal. All integer tests use the actual legal search range. Each relevant integer belongs to a unique centered interval of length \(s\), so the correct match exists. The baby classes are distinct since \(2b-2<q\). Within the legal giant range, each sign class contains at most two entries. In fact equality with a fixed sign implies equality of giant indices modulo \(q\) as \(sP\ne0\), and equality with the opposite sign gives one linear congruence for the second index. Only indices for intervals meeting the bounded search range are used, so each congruence has at most one legal index. Thus each dictionary action inspects at most two name entries. These table actions and integer index tests add no field multiplication. There is one primary group operation per new group entry, with the original tariff. In particular there is no additional target multiplication for a reverse lookup, which uses the name of the value already generated. The second table requires at most \(O(b)\) entries, since after the baby table is complete no more reverse queries are needed.

Let the true integer be \(x=js+i\), with \(|i|\le b-1\), and let \(J\) be the ordinal number of its giant entry, starting at zero. The first matching baby has ordinal \(I=|i|\). If \(J<b\), the two entries appear within \(2\max(I,J)+2\) primary steps, including their initial entries. If \(J\ge b\), they appear within \(b+J+2\). The group stride updates have already been prepared, and the signs and indices are decided at insertion. The last interval check and the fixed initial bookkeeping add at most twelve steps, as in the single-table search. We may therefore use the two preceding bounds with \(+14\).

Condition on the ordinary triple choice, which is independent of the search coins. For either increment of the first triple, condition also on all search coins but its single tag box variable, without conditioning on the value obtained in the anchor search. Then the actual centered integer is uniform on an interval of \(g\) consecutive integers, since the box variable enters it with coefficient one or minus one and the public center is fixed. An interval that contains an entire giant cell, which has \(2b-1\) integers, gives a uniform residual on that cell. On such a cell and for \(0\le J<b\), the conditional mean without the fixed \(14\) is at most
\[
 2\,\mathbb E[\max(I,J)]
 =2J+\frac{2(b-J-1)(b-J)}{2b-1}
 \le b+\frac{J^2}{b}.
\]
For the equality, \(I=0\) occurs once and every \(I=1,\ldots,b-1\) occurs twice. For the inequality use \(2b(b-J-1)\le(2b-1)(b-J)\). When \(J\ge b\), the bound is \(b+J\) throughout the cell.

Write \(\Phi_b(u)=b+\min(u^2/b,u)\) on \(u\ge0\). By the order of giant indices and \(|i|\le b-1\), \(J\le |x|/(b-\tfrac12)+2\), and \(\Phi_b\) is increasing and 2-Lipschitz. Also \(b-\tfrac12\ge a\), \(0\le b-a\le2\), and \(\Phi_b(u)\le b-a+\Phi_a(u)\). Consequently \(\Phi_b(J)\le a f(x/A)+6\), where \(f(u)=1+\min(u^2,|u|)\). At most two giant cells of the conditional interval are incomplete. On those cells the step count exceeds the bound \(\Phi_b(J)+14\) by at most \(2b\), since the only case needing an averaged residual is \(J<b\). The total error contributed by incomplete cells is at most \(4bs/g<8b^2/g\). For an increment, \(b\le\sqrt{g/2}+2\). The generic ledger of Ncmp gives \(\theta<2^{-199}\). By I5, \(g^{-4}<\mu_{\rm tr}<\theta\), so \(g>2^{199/4}>10^{12}\) and \(b^2/g<1\). The integer and conditional averaging overhead is less than \(14+6+8=28\) steps. These bounds persist after removing the conditioning without requiring independence of the three logs.

For an increment of the first triple, \(A=g/2\) and \(|x|\le A\). The centered uniform box has variance \((g^2-1)/12\), and the deterministic rounding shift has magnitude at most \(1/2\). Thus \(\mathbb E x^2\le g^2/12+1/4\). Since \(f(x/A)=1+x^2/A^2\) on this interval, we obtain \(\mathbb E[a f(x/A)]\le (4/3)\sqrt{g/2}+\sqrt{g/2}/g^2\). The last term is less than one, so each first-triple increment takes at most \((4/3)\sqrt{g/2}+64\) expected primary steps including all integer overhead. The rare later triples use the preceding fixed-width increment bounds.

### Two-phase concurrent traversal for the anchor

Keep the signed baby and giant sequences and queries in the opposite table. Use \(A_*=123/100\), \(a=\sqrt{A_*\sigma^+}\), \(b=\lceil a\rceil+1\), and stride \(s=2b-1\). Prepare both signed strides before the line. On the nonnegative real axis define a cumulative baby schedule \(h\) by
\[
 r_1=21/20,\quad r_2=8/5,\quad t_0=2/5,\quad h_0=r_1t_0,\quad t_1=t_0+(1-h_0)/r_2=61/80,
\]
\[
 h(u)=
 \begin{cases}
 r_1u & 0\le u\le t_0,\\
 h_0+r_2(u-t_0)&t_0\le u\le t_1,\\
 1&u\ge t_1 .
 \end{cases}
\]
Let \(h^{-1}(x)\) be its unique inverse on \([0,t_1]\) for \(x\in[0,1]\). Give the baby entry of ordinal \(i\) time \(h^{-1}(i/b)\) and the giant entry of ordinal \(j\) time \(j/b\), starting at ordinal zero in both tables. At each step compare just the rational times of the next entries, take the earlier and break ties in favor of the baby. The slope and breakpoint constants are fixed rational numbers, so the comparisons use a bounded number of integer operations on indices. Advance and look up that entry in the same sign-class tables as before. This comparison schedule changes neither sequence nor accepted intervals. When a list has ended, use the remaining list. The true legal match therefore still terminates the primary search.

For the true ordinals \(I,J\), set \(x=I/b,u=J/b\) and \(v=\max(u,h^{-1}(x))\). Both entries have arrived by time \(v\). The number of entries through that time is at most \(b(h(v)+v)+2\), by separately counting ordinals not exceeding \(b h(v)\) and \(bv\). With the bounded terminal checks, the primary steps are at most \(b H(x,u)+16\), where \(H(x,u)=h(v)+v\). At fixed \(u\), the function is constant up to \(x=h(u)\) and then equals \(x+h^{-1}(x)\), so it is increasing and 2-Lipschitz in \(x\). For \(u\ge t_1\) it equals \(1+u\) for every \(x\).

Condition on the triple selected independently of the search coins and on all the box variables except the independent diamond variable. The anchor's centered integer \(X\) then lies uniformly in an interval of \(g\) consecutive integers. In every complete giant cell the distribution of \(I\) has one occurrence of zero and two of each \(1,\ldots,b-1\). It is stochastically dominated by \(bU+1\) for \(U\) uniform on \([0,1]\): for \(0\le x<b\) its distribution at level \(x\) is \((2\lfloor x\rfloor+1)/(2b-1)\), at least \(\max(0,(x-1)/b)\); outside that interval the domination is immediate. Equivalently coupling by their cumulative probabilities gives \(I/b\le\min(1,U+1/b)\). Thus the conditional whole-cell expected cost is at most \(b f(u)+18\), where
\[
 f(u)=\int_0^1 H(x,u)\,dx
 =h(u)(h(u)+u)+\int_{h(u)}^1 (x+h^{-1}(x))\,dx.
\]
For \(u<t_1\), differentiation on each of the two linear pieces gives \(f'(u)=h(u)(1+h'(u))\), because the terms with the moving integration endpoint cancel. Therefore \(f\) is continuous, increasing, and \(13/5\)-Lipschitz. Before \(t_1\) it is bounded by \(1+t_1<2\) and thereafter equals \(1+u\).

There are at most two incomplete giant cells in the conditional interval. Their total probability is at most \(2s/g\). When \(u<t_1\), the pointwise cost is at most \((1+t_1)b+16\le3b\), since \(g>10^{12}\) by (I5) and the bound on \(\theta\). After fill the whole-cell bound already holds pointwise. So the expected excess from edge cells is at most \(12b^2/g<1464\), using \(a^2/g=(123/100)\sqrt{(N+7)/48}<121\), \(0\le b-a\le2\) and \(g>10^{12}\) to get \(b^2/g<122\). This comparison holds for every choice of the other box variables.

For each centered \(X\), the signed giant ordering and the radius \(b-1\) give \(J\le |X|/(b-1/2)+2\). Since \(b(b-1/2)\ge a^2\), monotonicity and the Lipschitz bound imply
\[
 b f(J/b)\le b f(|X|/a^2)+26/5 .
\]
Furthermore \(\mathbb E f(|X|/a^2)\le2+\mathbb E|X|/a^2<3\), as \(\mathbb E|X|\le\sigma^++3/2\). Thus replacing the exterior \(b\) by \(a\) costs at most six steps in expectation. Replacing \(X\) by the centered sum \(S\) costs less than one further step, because \(|X-S|\le3/2\) and \((13/5)(3/2)/a<1\). The sum of the explicit comparison errors and edge costs is below 2048.

Put \(Y=S/\sigma_S\) as above and let \(G\) be standard normal. The established characteristic-function bound through frequency \(10^6\) and the trivial bound beyond it give
\[
 \frac{2}{\pi}\int_0^\infty
    \frac{|\phi_Y(t)-e^{-t^2/2}|}{t^2}\,dt
 <\frac1{300000}+2^{-40}+\frac2{10^6}<\frac1{150000}.
\]
In particular, for every \(v\ge0\) the expectations of \((|Y|-v)_+\) and \((|G|-v)_+\) differ by less than \(1/150000\): use
\((|y|-v)_+=(|y-v|+|y+v|)/2-v\) and the absolute-value integral above, in which the average of the shifts multiplies the characteristic function by \(\cos(tv)\). Monotonicity gives \(f(|S|/a^2)\le f(|Y|/A_*)\). To compare this last expectation to the normal one, write \(f(u)=f(0)+\int_0^{t_1}(u-v)_+\,d\mu(v)\), including any atoms at the endpoints. Here \(d\mu\) is the measure of increments of \(f'\). This identity follows by integrating the derivative, which starts at zero. Its derivative grows on the two pieces and jumps upward at \(t_0\) to reach \(1+r_2\) just before \(t_1\), where it drops to one. The total variation of \(\mu\) is \(1+2r_2=21/5\). Therefore
\[
 \left|\mathbb E f(|Y|/A_*)-\mathbb E f(|G|/A_*)\right|
 <\frac{21/5}{150000 A_*}.
\]

It remains to bound the normal expression at the two rational cutoffs \(R_0=A_*t_0=123/250\) and \(R_1=A_*t_1=7503/8000\). Let \(F(v)=\Pr(|G|\le v)\) and \(\varphi\) be the normal density. Direct integration of \(f'\) gives
\[
 f(x/A_*)=
 \begin{cases}
 (7369/8000)+(861/800)(x/A_*)^2,& 0\le x\le R_0,\\
 (39573/40000)-(286/615)x+(20800/15129)x^2,&R_0\le x\le R_1,\\
 1+x/A_*,&x\ge R_1.
 \end{cases}
\]
In computing \(f(0)\), the integral of \(h^{-1}\) equals \(r_1t_0^2/2+(1-h_0)t_0+(1-h_0)^2/(2r_2)\). For the normal integrals use
\(\mathbb E[|G|\mathbf1_{|G|\le v}]=2(\varphi(0)-\varphi(v))\) and
\(\mathbb E[G^2\mathbf1_{|G|\le v}]=F(v)-2v\varphi(v)\), by \(\varphi'=-x\varphi\) and integration by parts. Substituting in the three pieces gives
\[
 \mathbb E f(|G|/A_*)=1
  -\frac{55346489}{75645000}F(R_0)
  +\frac{825539917}{605160000}F(R_1)
  -\frac{341}{1230}\varphi(R_0)-\frac{14}{615}\varphi(R_1).
\]
Use \(398940/10^6<1/\sqrt{2\pi}<398943/10^6\) by the earlier lower bound and \(\pi<314160/100000\). The upper bound on \(\pi\) follows from the same Machin identity, using the alternating sums through the positive ninth-power term for the first arctangent and the negative cubic term as a lower bound for the subtracted arctangent. Squaring the two normalization inequalities with the respective rational bounds on \(\pi\) verifies them.

At both cutoffs \(v\), integrate the alternating exponential series for the folded density. For \(F(v)\) use twice the normalization times the sums
\(\sum_{j=0}^{k}(-1)^j v^{2j+1}/(2^j j!(2j+1))\); for \(\varphi(v)\) use the normalization times
\(\sum_{j=0}^{k}(-1)^j(v^2/2)^j/j!\). The lower and upper sums have \(k=7\) and \(k=6\) respectively, since \(v^2/2<1\). Substituting the two cutoff fractions in these sums gives the following outward rational ends:
\[
 F(R_0)>377278499/10^9,\qquad F(R_1)<325846277/(5\cdot10^8),
\]
\[
 \varphi(R_0)>88365769/(25\cdot10^7),\qquad
 \varphi(R_1)>51396409/(2\cdot10^8).
\]
Use these ends according to coefficient sign in the expression above and \(\sqrt{A_*}<1109054/10^6\) by squaring. The resulting bound for \(\sqrt{A_*}\mathbb E f(|G|/A_*)\) is
\[
 \frac{50643204301966142506511}{30258000000000000000000}
 <\frac{1673713}{10^6}.
\]
Adding \((1109054/10^6)(21/5)/(150000 A_*)\) gives less than \(83687/50000\). Combining this with the finite comparison errors bounds the anchor by \((83687/50000)\sqrt{\sigma^+}+2048\) expected primary steps. All group operations other than the scheduled candidates and their bounded initialization and terminal checks are charged separately below.

### Adaptive pointwise traversal

Each ordinary search runs a second, adaptive search over the same bound. It uses the auxiliary polynomial-basis representation described below and uses exact equality of twelve-coordinate vectors for table keys. At stage \(j\ge0\), set \(w=2^j\) and tabulate \(iP\) for \(0\le i<w\). Use \(j\) doublings to obtain \(wP\) and another \(j\) to obtain \(w^2P\). The stride \(-wP\) comes from negating \(P\) and doubling \(j\) times. The inverse of \(P\) can be extracted once in at most 508 products by using the scalar \(q-1\). It can also be obtained by applying the fixed \(p^6\)-Frobenius matrix, since the BN254 embedding degree is 12, so \(p^6\equiv-1\pmod q\). To handle the pointwise bound uniformly, use this fixed twelve-dimensional linear map, at at most 144 base-field multiplications. Start with the residual \(xP+w^2P\) and test \(2w+1\) residuals, advancing by \(-wP\). A match with baby index \(i\) at giant index \(j'\) gives \(x=j'w+i-w^2\). This covers \([-w^2,w^2+w-1]\), hence certainly every integer of magnitude at most \(w^2\). Accept only an integer in \([-B,B]\); uniqueness follows from \(2B+1<q\). Thus a valid integer is found by the first stage with \(w^2\ge |x|\). With standard constant-operation table access in the search model, the stage costs \(O(w)\). Its finite work consists of group products, table accesses, comparisons and integer index updates. The geometric sum of widths is less than twice the last width, so the total work is \(O(\sqrt{|x|}+1)\). Each group's multiplication can be suspended between products of coordinates. Resume the adaptive search for one elementary operation before the first primary operation and after each block of one million primary operations, stopping when either search returns. An adaptive operation can be a group update, a table operation, or the single Frobenius application. A primary candidate and its associated table actions have bounded cost, so an adaptive search that would finish in \(T\) operations finishes within \(10^6(T+1)\) primary candidates if the primary search has not already finished. Each interleaved search therefore costs \(O(\sqrt{|t_i|}+1)\) for the integer it produces, with an absolute constant independent of \(N,q,g,M\). The three public translations by \(c_0,c_0+c_1,c_0+c_2\) are prepared before entering line [full-search]. The two in-line subtractions of \(t_0\Psi\) use at most \(2\lceil\log_2(|t_0|+1)\rceil\) group products each, and a constant-time target inverse by Frobenius for the appropriate sign. Their cost is \(O(\sqrt{|t_0|}+1)\), using \(\log(x+1)=O(\sqrt{x})\) for \(x\ge1\). Thus the work in this single line, including these translations and all three adaptive traversals, is at most a fixed constant times \(\sqrt{\max_i|t_i|}+1\) in the ordinary mode. Choosing the signed largest component and the later key recombination involve only a fixed number of integer operations.

The anchor uses the two-phase concurrent traversal and both first-triple differences use the balanced concurrent traversal. A later triple uses the same anchor and the fixed-width traversal with \(M_\Delta\) for both differences. Primary baby and giant candidates use the unchanged six-multiplication tariff for the ordinary search operations. For the adaptive search, even charging two arbitrary target-group products at the full 276-multiplication price derived below per scheduled operation, the ratio of adaptive charge to primary charge over a full block is at most \(552/(6\cdot 10^6)<1/10000\). At most three initial adaptive operations and the increment initialization and verification bounds of 14 are accounted for separately in the auxiliary allowance. Apart from that allowance, the expected contribution is at most \((83687/50000)\sqrt{\sigma^+}+(8/3)\sqrt{g/2}+2176+1\), including the rare use of a later ordinary triple. Termination by the adaptive search can only reduce it.

**Base-field multiplication ledger for auxiliary work.** Represent BN254 target elements as elements of the order-\(q\) subgroup of \(\mathbb F_{p^{12}}^\times\), where \(\mathbb F_p\) is the curve base field. Fix any monic irreducible degree-12 polynomial over \(\mathbb F_p\) and its polynomial basis. Pairing outputs can be interpreted in this same field. Precompute the twelve-coordinate vector for each basis power up to degree 22. The polynomial product of two degree-at-most-11 representatives costs at most 144 base-field multiplications. Once the product coefficients of degrees 12 through 22 are known, reduction adds their linear combinations of the fixed twelve-coordinate vectors using at most \(11\cdot12=132\) further base-field multiplications. Thus one target-group addition or doubling costs at most 276 base-field multiplications. This bound applies in any degree-12 polynomial basis, including a basis chosen to match the protected pairing implementation via a fixed linear change of coordinates. If that implementation returns in a different basis, converting one result costs at most 144 base-field multiplications. The protected search can stay in its own basis. Converting the at most three base-and-target pairs entering it and the final output out of the auxiliary basis costs at most eight further such conversions.

For an auxiliary scalar multiple, including a group subtraction when implemented by adding an inverse, reduce the scalar modulo \(q\). The binary algorithm uses at most 508 group multiplications since \(q<2^{254}\). Charge three public center translations before the line, two post-line products for removing the ordinary search term and applying the inverse key weight, six signed-stride setup multiples across the three traversals, and two in-line products by the signed anchor logarithm. This is at most thirteen scalar multiples, each requiring at most 508 group products. The Frobenius sign operations and all remaining constant arithmetic are covered by the allowance of 400 further products. On the fallback path only the fixed evaluation-point inversion in the search and the one normalization after it are needed. For each signed pairing sum, negate source operands by coordinate sign change where needed. Accumulate the corresponding Miller-loop products, then finalize the sum with the protected shared final exponentiation convention. The same polynomial product bound applies to these field products before exponentiation. The pairing bound is \(48K_2+4(J+4)\le48\cdot19+4(24+4)=1024\), including the fallback branches as shown in Amendment dec_pairings. There is at most one accumulator product and basis conversion per pairing, so the allowance of 1024 of each covers them. The zero-target-base path needs only normalization. Allow 400 further group products for combining the terms, handling signs, the three search overheads and other setup. In particular, an inverse for the initial stride in the protected signed search can use the protected sign-class operation. Alternatively, make both initial signed strides by two extra binary scalar multiples. We budget two for each of the three primary searches.

The fallback's expected auxiliary cost is at most \((135/q^2)(16\sqrt q+600)\cdot276\) base-field multiplications in addition to the two pairings already charged, hence less than \(10\cdot276\) for the protected prime. The total above is less than \((13\cdot508+1024+400+10)\cdot276+(1024+7)\cdot144<2400000\) expected base-field multiplications. It therefore fits in 400000 units of six base-field multiplications. The rare choice of a later ordinary triple adds less than one primary candidate in expectation, so its scheduled cost is at most \(10001/10000\) of one unit. Allow two further units for it. The total expected multiplication bound is \(6((10001/10000)((83687/50000)\sqrt{\sigma^+}+(8/3)\sqrt{g/2})+402180)\), covered by the amended spread, since \(400002+(10001/10000)2176<402180\). The ordinary searches retain their bounded-answer correctness, and the fallback introduces no new published operands.


## Amendment n

Use \(n=kd_R+\mathrm{form\_pad}\). Put \(v_0\) in slot zero, put zeros in the following \(\mathrm{form\_pad}-1\) positions, and use the remaining \(kd_R\) positions for the output coefficients of the matrix product, ordered by row and power-basis digit. The finite guard bounds the number of padding positions for each admitted degree. This preserves the exact kernel identity \((v_0,A\hat v)=(0,0)\). The number of padded positions is not a change to the number of input coordinates or to the coefficient norm. The actual Module-SIS dimensions are \(kd_R\) and \(\ell d_R\) with the selected infinity radius, while the exponent calculation uses the field of the full degree \(n\).

## Amendment msis_bound

The radius of the reduction's coefficient infinity norm is
\[
\beta_{\rm use}=(1-s)\beta+s b_{\rm s}.
\]
The uniform coefficient-ring matrix, dimensions and coefficient kernel are the same. Mode zero uses the short lift of I6. In mode one we prove that a deterministically selected nonzero kernel vector of every heavy passing stack admits a short multiple at radius \(b_{\rm s}\).

### Joint fibers

For a nonzero matrix \(A\) of linear forms on independent box coordinates in \(\{1,\ldots,N_\star\}\), suppose the maximum probability of \(Ar_I\) is \(p>\theta\). The prefix construction of I6 extends to this joint fiber and gives a regular saturated lattice of rank at most three containing the row space modulo \(q\), with maximum fiber density at least \(p-3\varepsilon_{\rm tr}\). To see this, remove zero columns. The joint prefix probabilities \(p_i\) are nonincreasing by conditioning on the last coordinate. The first nonzero column gives \(p_1=1/g\) and lattice \(\mathbb Z\). At a subsequent step, express each current prefix row as \(B c_j\) modulo \(q\) in the current basis \(B\). Append the next coefficient to get \(c'_j\). In the trimmed densest joint fiber \(F\) of the longer prefix, these vectors define constant modular forms in \(\Phi(r)=(B^\top r_{[i]},r_{i+1})\). At least one last coefficient is nonzero, so one such form puts \(\Phi(F)\) in an index-\(q\) coset. Since \(\Pr[F]\ge p_{i+1}-\varepsilon_{\rm tr}>\mu_{\rm tr}\) and \(\Lambda_d\Gamma_d<q\mu_{\rm tr}\), the I6 sparse count excludes full affine dimension. The same minors of its difference matrix satisfy the I6 bound because it depends only on the current basis, trimming and the box. The small-minor lift of the protected lattice-facts lemma gives an integer annihilator of those differences for **each** \(c'_j\). Consequently \(F^\perp\) contains integer lifts of all new rows. Its rank is at most three by the density bound and \(g^{-4}<\mu_{\rm tr}\); the regularization lemma enlarges it to a regular saturated lattice losing at most \(2\varepsilon_{\rm tr}\). This proves the claimed induction, including the rank and density. Restoring zero coordinates preserves the claims.

The height bounds \(H_1,H_2,\lfloor H_3\rfloor\) follow from the same density and regularity estimates as in I6. In particular for a single nonzero \(v\) with \(v_0=0\) and \(\operatorname{gp}(v^\top)>g\theta\), its lattice has density greater than \(g\mu_{\rm tr}\) because \(100g\varepsilon_{\rm tr}>3\varepsilon_{\rm tr}\). Since \(g^4\mu_{\rm tr}>1\), this density exceeds \(g^{-3}\), forcing rank at most two by the invertible-minor bound. The terminal argument of I6 in ranks one and two gives a short lift at \(b_{\rm s}\) using the first two norm inequalities of the passing-stack conditions in I6.

### Structure of a heavy passing stack

Let \(\mathcal V\) be the row space. The stack fiber equals a joint fiber of the basis values because the basis rows and all rows span one another. The guessing-probability rank bound and \(g^4\theta>1\) give dimension at most three. Every kernel vector has zeroth coordinate zero. Rank one cannot give a nonzero kernel vector in a nonzero passing stack, because each nonzero symmetric cell would be a nonzero scalar times \(vv^\top\) for a generator \(v\). Its zero zeroth row would force zero diagonal by Booleanity, contradicting \(v\ne0\).

If some \(w\in\mathcal V\) has \(w_0\ne0\), choose any nonzero kernel vector \(v\). Conditional on all the box coordinates, \(v^\top r\) is fixed and \(w^\top r\) has \(g\) distinct equiprobable values through the independent centered-sampler draw \(r_\diamond\). The joint guessing probability is at most \(\operatorname{gp}(v^\top)/g\). Heaviness implies \(\operatorname{gp}(v^\top)>g\theta\) and gives the individual lift just proved.

Suppose instead \(\mathcal V\) vanishes at coordinate zero. If its kernel has dimension at least two, choose an active coordinate \(i\) at which some vector \(w\in\mathcal V\) is nonzero. There is a nonzero kernel vector \(v\) vanishing there by the dimension and a single linear condition. Conditional on all box coordinates except \(i\), the first basis value \(v^\top r\) is fixed and \(w^\top r\) is uniform on \(g\) values. This again gives \(\operatorname{gp}(v^\top)>g\theta\). The active coordinate and selected vector use \(O(N_\star)\) work given a basis of at most three vectors and its kernel.

It remains to consider a one-dimensional kernel in a space with zero zeroth coordinate and dimension two or three. Apply the joint-fiber assertion to a basis of \(\mathcal V\). Its regular lattice \(\Theta\) contains all of \(\mathcal V\) modulo \(q\). Ranks one and two already have the required terminal bounds from I6 at \(b_{\rm s}\). Let \(\Theta\) have rank three. For an integer basis \(B\), choose a largest minor \(B_J\) of absolute determinant \(h\). Normalize the real row matrix to \(P=B B_J^{-1}\). The numerator \(B\operatorname{adj}(B_J)\) has entries of absolute value at most \(h\), by Cramer's rule and maximality. Since \(2h^2<q\), \(B_J\) is invertible modulo \(q\). If two normalized rows are proportional modulo \(q\), their numerator minors of order two are all divisible by \(q\) and of absolute value at most \(2h^2<q\), so the real rows are proportional. A zero modular row is a real zero row by the entry bound. Also any subset of rows of \(B\) of rank at most two modulo \(q\) has rank at most two over the reals, since its order-three minors have absolute value at most \(h<q\). Normalization preserves this rank.

When \(\dim\mathcal V=2\), choose a two-column basis matrix \(U\). A nonzero symmetric cell is \(U C U^\top\) with \(C\) nonzero symmetric: with a left inverse \(L\) take \(C=L W_c L^\top\), using that projection back to \(\mathcal V\) fixes the columns and rows. The cell has zero diagonal by Booleanity, so every coordinate row of \(U\) lies on a projective zero of the binary quadratic with matrix \(C\). A nonzero homogeneous quadratic in two variables has at most two projective roots, by the one-variable root bound on a finite chart and the corresponding degree drop if infinity is a root. The two-dimensional row span forces two distinct lines. A change of basis sends these lines to the coordinate axes, giving a disjoint-support basis \(a,b\) of \(\mathcal V\). Partition the coordinates into the two supports, assigning a coordinate where both vanish to either part. Within a given part, the rows of \(B\) annihilate the coefficient vector of the complementary form in the reduction of \(B\). That coefficient vector is nonzero, so each group has rank at most two modulo \(q\), hence also over the reals. If both row groups have real rank two, each also has modular rank two by the order-two minor bound for the normalized numerator. Choose two rows \(B_i,B_{i'}\) in the group that annihilates the coefficient vector of \(a\), independent modulo \(q\). Form the integer vector \(X_a\) whose coordinate at row \(j\) is \(\det(B_j,B_i,B_{i'})\). This vector is \(B\) multiplied by a fixed integer cofactor column, and is zero in the chosen group since all its rows have real rank two. Its reduction is a nonzero scalar multiple of \(a\): the cofactor column is nonzero modulo \(q\) and spans the modular nullspace of those two rows. The same construction in the other group gives \(X_b\) with residue a nonzero multiple of \(b\). Both have maximum coordinate at most \(h\) by maximality of \(B_J\), and their supports are disjoint.

Let \(h_a=\|X_a\|_\infty\), \(h_b=\|X_b\|_\infty\), both positive. The integer coefficient preimage of the selected kernel line in the basis \(\bar X_a,\bar X_b\) has index \(q\) in \(\mathbb Z^2\). Scaling the two coordinates by \(h_a,h_b\) gives determinant \(q h_a h_b\le qh^2\). The additional checked inequality \(b_{\rm s}^2\ge q\lfloor H_3\rfloor^2\) makes the square of radius \(b_{\rm s}\) have area at least four times this determinant. The lattice-volume implication from I6 gives a nonzero point there. In the original support coordinates it has infinity norm at most \(b_{\rm s}\), since the two supports are disjoint. Its residue is nonzero since \(2b_{\rm s}<q\), and lies on the selected line. This completes the lift in this case.

Otherwise one real row group has rank one and the other rank two, since together they span dimension three. The normalized rows lie in a real plane and a real line.

When \(\dim\mathcal V=3\), the reduction of \(B\) is a basis. The cell matrices span at least two independent matrices. If instead they were all multiples of a single \(W\), the latter would have rank three on the coefficient space because the stack spans dimension three. The field polynomials \(W_U,W_V\) would then be \(aW,bW\) with \(a,b\) not both zero. By the first tie \(aWz_0=bWz_-\). In coefficient coordinates \(W\) has an invertible symmetric matrix. The two consecutive conjugate vectors in those coordinates are independent in the extension field by the Moore argument, since \(z(\mathcal V)\) has dimension two. This forces \(a=b=0\), a contradiction.

Choose two independent symmetric cell matrices in the basis \(\bar B\), by the same left-inverse identity as above. The zero diagonals place each nonzero coordinate signature at a common projective zero of the two independent ternary quadratics. Two such quadratics have at most four common projective zeros or a common line and at most one extra point. To justify this over an algebraic closure, a reducible quadratic is a product of two linear factors, possibly equal. Each line that is not a factor of the other polynomial has at most two common points by the projective root count. With a shared factor, the other linear factors are independent and their simultaneous zeros are one point. The common line is defined over \(\mathbb F_q\), since otherwise its distinct Frobenius conjugate would give a second common factor and make the quadratics proportional. If the first quadratic is irreducible over the closure, it has rank three: completing squares diagonalizes it and ranks one and two factor over the closure. A nonsingular ternary quadratic over that closure can thus be changed into \(XZ-Y^2\) by diagonalizing and scaling its diagonal entries and using odd characteristic. Its projective zeros are \([s^2:st:t^2]\). Substitute these coordinates into the second quadratic. The resulting binary quartic cannot vanish identically since among the six quadratic monomials the only equal substitutions are \(XZ\) and \(Y^2\); the kernel of substitution consists precisely of multiples of the first form. The root count gives at most four projective points.

Normalization by \(B_J^{-1}\) preserves these incidences modulo \(q\). In the four-point case the order-two minor bound gives at most four real directions. In the line-and-point case the rows on the projective line have rank at most two over the reals by the order-three minor bound, and the rows at the extra point have rank at most one by the order-two bound. Hence in the line-and-point case the real rows lie in one real plane and one real line.

### Terminal volume

Let \(K=\{x\in\mathbb R^3:|p_i\cdot x|\le1\ \text{for every normalized row }p_i\}\). It has the three unit-coordinate strips. Every normalized row entry and every three-row determinant has absolute value at most one by maximality of \(B_J\).

Suppose the normalized rows have at most four directions. The three unit axes use three of the directions, and any additional rows on those axes impose no stronger strips because every row entry has absolute value at most one. If the fourth direction is absent, the body is the cube. If a representative \(p=(p_1,p_2,p_3)\) of the fourth direction has at most two nonzero coordinates, choose the row of strongest magnitude on this direction. Its two coefficients are at most one in absolute value. The portion of the corresponding unit square satisfying \(|p_1x_1+p_2x_2|\le1\) has area at least three. Indeed, conditioning on either uniform coordinate, the probability for the other term to belong to an interval of length two centered at the conditioned value decreases with the absolute value of that center, since its density is uniform on a centered interval (or a point mass at zero). This proves monotonicity as the absolute coefficient of the conditioned term increases. By symmetry repeat for the other coefficient, so the minimum is at both coefficients of magnitude one. There two triangles of area \(1/2\) each are removed. The third coordinate contributes a factor two to the volume, giving at least six.

It remains to handle four directions with every \(p_i\ne0\). Here \(\mathcal V\) has dimension three. In the earlier two-dimensional case either a short vector was already found from the two rank-two groups, or the rows lie in a plane and a line. Such a union covering all three unit axes has no direction with all three coordinates nonzero, since its plane is a coordinate plane and its line is the remaining axis. Work in the field basis of \(\mathcal V\) whose three columns are those of \(\bar P\operatorname{diag}(p_1^{-1},p_2^{-1},p_3^{-1})\), with \(P=BB_J^{-1}\) the normalized row matrix and inverse scalars taken modulo \(q\). The fourth row becomes \((1,1,1)\) and the original unit rows remain nonzero multiples of axes. The reductions of the nonzero \(p_i\) are nonzero because their numerators in \(B\operatorname{adj}(B_J)\) have absolute value at most \(h<q\). Every cell coefficient matrix in this basis is symmetric, has diagonal zero, and has its three off-diagonal entries summing to zero by Booleanity at those four row directions. Let \(\mathcal S\) be this two-dimensional space of matrices over \(\mathbb F_q\). The cell matrices span \(\mathcal S\), since they span at least two dimensions as shown above.

Let \(k_0\) be a nonzero coefficient vector of the one-dimensional kernel in this basis, put \(U=k_0^\perp\) over \(\mathbb F_q\), and write \(z_{\mathcal V}=(z(w_1),z(w_2),z(w_3))^\top\) for the field value of the three basis columns. Its entries span two dimensions over \(\mathbb F_q\) by the kernel hypothesis. Put \(s=n/2\) and use \(h_-=\sigma^{s-1}z_{\mathcal V}\), \(h_\circ=\sigma^s z_{\mathcal V}\), and \(h_+=\sigma^{s+1}z_{\mathcal V}\). Each lies in the field extension of \(U\), and the first two form its basis by the consecutive Frobenius independence proved in C7. Let \(X_-,X_\circ,X_+\) be the representations in this coefficient basis of \(W_U,W_V,\sigma^{s+1}(W_U)\). They belong to the extension of \(\mathcal S\). The three ties are \(X_i h_j=X_j h_i\) for each pair. In addition \(X_+=\sigma^{s+1}(X_-)\) and \(X_\circ=\sigma^s(X_\circ)\), the latter because \(W_V\) uses only even powers and the half-turn negates \(T\).

There is a unique extension-linear map \(L_*\) on the extension of \(U\) taking \(h_-\) to \(X_-\) and \(h_\circ\) to \(X_\circ\). It satisfies \(L_*(x)y=L_*(y)x\) by the first tie and bilinearity. It also takes \(h_+\) to \(X_+\). To see this, write \(h_+\) as a linear combination of the first two. The other ties show that \(X_+-L_*(h_+)\) annihilates both first vectors. This difference is symmetric, so its image lies in the orthogonal line of \(U\) and its rank is at most one. A nonzero symmetric rank-one matrix is a scalar multiple of \(vv^\top\) for some nonzero \(v\) and has a nonzero diagonal entry. The difference lies in \(\mathcal S\), which has zero diagonals, so it vanishes.

For every \(i\), the map \(X\mapsto Xh_i\) is injective on the extension of \(\mathcal S\). In fact a matrix there with off-diagonal entries \(x,y,z\) has determinant \(2xyz\). If a nonzero such matrix is singular, one of these entries is zero and the others are nonzero and opposite. Its nullspace is then one of the three \(\mathbb F_q\)-lines given by permuting \((1,1,0)\). A field vector on any of those lines has coefficient rank at most one over \(\mathbb F_q\), unlike \(h_i\).

Suppose the two image planes \(\mathcal S h_-\) and \(\mathcal S h_\circ\), over the form field, are distinct. Their span then has dimension three. For a linear map \(L\colon U\to\mathcal S\) over \(\mathbb F_q\), the identity \(L(x)y=L(y)x\) is equivalent to its check on one basis pair of \(U\). After extending scalars and choosing the pair \(h_-,h_\circ\), this is a linear constraint of rank three on the four map coefficients: the difference \(X_-h_\circ-X_\circ h_-\) ranges over the sum of the two image planes. The solution space over the form field thus has dimension one, and the equations in an \(\mathbb F_q\)-basis have the same rank. Hence \(L_*=\gamma L\) for a map \(L\) defined over \(\mathbb F_q\) and a nonzero field scalar \(\gamma\). If \(L\) has rank one, then \(X_-,X_\circ\) are scalar multiples of the same fixed \(\mathbb F_q\) matrix, and the distinct within-family monomials with degree below n are basis elements. Comparing their coefficients shows that every cell in \(W_U,W_V\) is a multiple of that matrix. This contradicts that the cell matrices span \(\mathcal S\). Thus \(L\) is injective. Its coefficients commute with Frobenius. Using the two Frobenius identities above and \(h_+=\sigma^{s+1}z_{\mathcal V}\), \(h_\circ=\sigma^s z_{\mathcal V}\), gives
\[
 \gamma L(h_+)=\sigma^{s+1}(\gamma)L(z_{\mathcal V}),\qquad
 \gamma L(h_\circ)=\sigma^s(\gamma)L(z_{\mathcal V}).
\]
Indeed \(\sigma^{s+1}h_-=\sigma^s h_\circ=z_{\mathcal V}\). Injectivity makes both \(\sigma^{s+1}z_{\mathcal V}\) and \(\sigma^s z_{\mathcal V}\) proportional to \(z_{\mathcal V}\). Applying \(\sigma\) to the second proportionality and comparing with the first shows \(\sigma z_{\mathcal V}\) proportional to \(z_{\mathcal V}\). The ratios of its entries to any nonzero entry are then fixed by \(\sigma\) and lie in \(\mathbb F_q\), contrary to rank two. Therefore the image planes cannot be distinct.

If they are the same, choose a nonzero vector \(v\) annihilating their common image. By symmetry, \(Xv\) is orthogonal to both \(h_-,h_\circ\) for every \(X\in\mathcal S\), and hence lies on the line of \(k_0\). The map \(X\mapsto Xv\) has domain of dimension two and image of dimension at most one. Some nonzero \(X\) kills \(v\), so by the explicit singular matrices above \(v\) is proportional to a permutation of \((1,1,0)\). For \(v=(1,1,0)\) its image \(\mathcal S v\) is precisely the line of \((1,1,-1)\), since \(Xv=(x,x,y+z)=(x,x,-x)\); permuting coordinates gives the other cases. Thus the kernel coefficient line is generated by a sign vector \(k'\) obtained by permuting \((1,1,-1)\).

Return now to the integer largest-minor normalization. Write \(N_{ji}=(B\operatorname{adj}(B_J))_{ji}\) and \(p_i=N_{j_0i}/\det B_J\) for the chosen fourth row \(j_0\). The integer vector with coordinates
\[
 x_j=\sum_{i=1}^3 N_{ji}k'_i\prod_{t\ne i}N_{j_0t}
\]
reduces to the kernel vector in the rescaled basis multiplied by the nonzero scalar \(\prod_i N_{j_0i}\). This follows by substituting \(P_{ji}=N_{ji}/\det B_J\) and the scaling by \(p_i^{-1}\). In particular it is nonzero modulo \(q\), and its coefficient infinity norm is at most \(3|\det B_J|^3\le3\lfloor H_3\rfloor^3\). The extra checked bound \(b_{\rm s}\ge3\lfloor H_3\rfloor^3\) gives a short multiple of the selected line in this last case, without needing a volume lower bound for these four directions.

In the remaining plane-and-line configuration, the plane must contain two unit axes and the line the third, because their union covers all three independent unit directions. After permuting coordinates, the plane is that of \(e_1,e_2\) and the line that of \(e_3\). Determinants of pairs of in-plane normals are bounded in absolute value by one using \(e_3\) as the third row, and the in-plane rows include \(e_1,e_2\). Its planar strip region therefore has area at least three by I6. The line normals are multiples of \(e_3\) with absolute coefficients at most one and include \(e_3\), so their interval has length two. The full region factors as the planar region times this interval, with volume at least six. The four-direction cases not already settled by a direct short vector have the same lower bound of six.

The line of the selected nonzero kernel vector has preimage of index \(q^2\) in the lattice of integral coefficient vectors of \(B\). The image under \(B_J\) has determinant \(hq^2\). The body \(b_{\rm s}K\) has volume at least \(6b_{\rm s}^3\ge 8 hq^2\) by the passing-stack conditions in I6. The I6 lattice-volume implication gives a nonzero point, lifting exactly as in I6 to a short multiple of that vector. It is nonzero modulo \(q\) because it is nonzero over the integers and has norm below \(q/2\).

### Reduction interface

In mode one, given the recovered row space, use the described active-coordinate choice if its kernel has dimension at least two and its zeroth coordinate vanishes throughout. In all other cases select any nonzero kernel vector when one exists. Use the protected LIFT at \(\beta_{\rm use}\). The lift existence is needed only for a good heavy passing stack, which is the stack supplied by the generic view and mark definition. On other tried expressions, any output remains a short multiple of a tested kernel vector, so packing gives a sound solution. The selection uses \(O(N_\star)\) additional field operations after the kernel computation and no extra oracle calls. It happens after recovery and therefore leaves the private detection and span-recovery probability bounds unchanged. The LIFT running time follows from the passing-stack conditions in I6 and P4. The targets use this actual challenge radius and the original generic, extraction and correctness bounds, including the same reduction-time asymptotic. The general inverse claim and heavy-stack implication at radius \(\beta\) retain their original scopes.

## Targets

Fix any parameter set satisfying the amended model, the protected system shape, any admissible evaluation points, and the stated group and oracle models. In the chosen modes use the coefficient positions of Amendment n, the base field of Amendment C6 and the grid and masks of Amendment C7, and the single-sector QAP encryption and decryption of Amendment n1. The amended inverse theorem applies by (P3) with Amendments I3, I4, H2, H3 and I6. The charged-mark bound is proved in Amendment Ncmp. Correctness and extraction use the same external witness relation, oracle model, budgets and probability bounds. Internally the projected witness forgets its Boolean tags.

### Correctness with error \(2/q\)

Fix an external witness \(w\), the statement, message and admissible evaluation points. Every tag extension used in n1 is a witness of the internal system. If the prescribed weight of \(v^{(0)}\) is zero decryption returns \(\bot\). Otherwise the chosen target has nonzero weight, whenever the ordinary or direct-normalization branch is selected. The identities of n1 recover the exact key in these branches. They give the settled target value after the three exact integer logarithms and the equality \(a_t+b_t-c_t=v^{(t)}\) in the ordinary branch, and directly in the branch where the chosen target base is zero. The evaluation-point branch recovers the exact key on every realization where it is called. Therefore failure is exactly the event of zero prescribed weight, which we bound next.

First consider the key weight for either fixed target. Let \(L:F\to\mathbb F_q\) be the constant-slot coefficient functional in the form basis, nonzero because \(L(1)=1\), and let \(s=n/2-1\). Then the weight of a form value \(x\) is \(Q(x)=L(x\sigma^s(x))\), with \(x\) uniform on the affine space with constant slot one and prescribed padding zero. The trace map is nonzero: the polynomial \(\sum_{j=0}^{n-1}X^{q^j}\) has degree \(q^{n-1}<q^n\) and cannot vanish at all \(q^n\) field elements. The pairing \((a,b)\mapsto\operatorname{Tr}(ab)\) is therefore nondegenerate, since multiplication by a nonzero \(a\) is invertible. Thus \(L(x)=\operatorname{Tr}(\lambda x)\) for a unique nonzero \(\lambda\), by equality of the dimensions of the field and its scalar dual.

The polar form \(Q(x+y)-Q(x)-Q(y)\) is
\[
 \operatorname{Tr}\!\left((\sigma^{-s}(\lambda x)+\lambda\sigma^s(x))\,y\right).
\]
Trace invariance under Frobenius gives this expression. By nondegeneracy, the radical solves \(\lambda x+\sigma^s(\lambda)\sigma^{2s}(x)=0\). If there is one nonzero solution \(x_0\), every other solution is \(x_0\) times an element fixed by \(\sigma^{2s}\), by dividing the two equations. Since \(\gcd(2s,n)=2\), such a ratio is fixed by \(\sigma^2\): use the integer Bezout identity for \(2s,n\) and \(\sigma^n=1\). There are at most \(q^2\) of these ratios because they are roots of \(X^{q^2}-X\). Hence the radical dimension is at most two and the polar rank at least \(n-2\). The affine form domain has codimension \(\mathrm{form\_pad}\). Restricting the polar form in either argument to its parallel linear space loses at most \(\mathrm{form\_pad}\) ranks, by the rank of the omitted rows or columns. Therefore its rank is at least \(n-2-2\mathrm{form\_pad}\), at least six in the scored shape and in the growing branch.

For an affine quadratic of rank \(d\) over the fixed odd prime field, the proportion of zeros is at most \(1/q+q^{-d/2}\). Indeed, use the character sum \(q^{-1}\sum_{a\in\mathbb F_q}\exp(2\pi i a Q/q)\) for its zero indicator. A linear change of variables diagonalizes the quadratic part in odd characteristic, by choosing a vector with a nonzero square coefficient, completing its square to isolate it, and iterating. With \(a\ne0\) a one-variable sum for a nonzero square coefficient has magnitude \(\sqrt q\), even with a linear term: by completing the square the linear term is a unit-magnitude factor, and the squared magnitude of \(\sum_x\exp(2\pi i c x^2/q)\) is the sum over \(x,y\) of \(\exp(2\pi i c(x-y)(x+y)/q)\). The map to \(x-y,x+y\) is invertible, and summing first over one new coordinate gives \(q\), since only the other coordinate zero has a nonzero inner sum. Every other coordinate has character sum bounded by \(q\). After normalization the contribution of all nonzero \(a\) to the zero probability is at most \(q^{-d/2}\), and the zero character contributes \(1/q\). Here \(n\ge4000\) and \(\mathrm{form\_pad}\le23\) give \(d\ge6\), so the key weight vanishes with probability at most \(1/q+1/q^3\), and in particular at most \(1/q+1/q^2\).

For the search probabilities condition on all scalar coins except \(y\) and the seed matrix. Set \(S(z)=\sum_c\gamma_c\xi_c(z)\) on the affine form domain, a polynomial of total degree at most two. If it is identically zero, a nonzero prescribed weight always leads to primary direct normalization. Otherwise it vanishes with probability at most \(2/q\) by the polynomial root bound. Independently the first factor \(y(v)\) in any prescribed base is uniform and vanishes with probability \(1/q\), so the base vanishes with probability at most \(3/q\). For two distinct tag variants their two form values are jointly uniform on two copies of the domain: after fixing all other columns, the homogeneous column and a differing tag column give a two-by-two evaluation matrix of determinant \(1\) or \(-1\) in each free coefficient position. Likewise their two \(y\) values are independent uniform, by the same determinant on the corresponding two coordinates and independently of the forms. Hence each pair of base-zero events for distinct tags has probability at most \(9/q^2\). The event of one specified primary zero-corner base zero and a zero key weight of \(v^{(1)}\) has probability at most \(6/q^2\), by joint uniformity of their distinct tags and the key-weight bound.

The fallback requires at least one base zero among \(a_0,b_0,c_0\), and either a zero secondary target weight or at least one base zero among \(a_1,b_1,c_1\). Otherwise the selector gives an ordinary or direct normalization branch. The three events of the first kind paired with the secondary weight contribute at most \(18/q^2\) and the nine pairs of base events contribute at most \(81/q^2\). Thus fallback probability is at most \(99/q^2\le135/q^2\). An ordinary secondary triple also requires a zero among the three primary ordinary bases, so its probability is at most \(9/q\). All bounds hold conditional on the fixed scalar coins and therefore also unconditionally, and all selection events are independent of the integer sampler.

### Extraction and the reduction

Let \(\mathcal A\) have the budget \(Q<2^\lambda\) of generic group calls and at most \(2^\lambda\) queries to each oracle. Fix one bit \(b\) and messages \(m_0,m_1\), and run the extraction experiment with \(m_b\). The extractor reads the answered generic transcript without any oracle calls. It uses the protected extractor sketches for the plain sector. The empty alpha sector can be represented by zero records. It samples three independent probe vectors for each cell, uses the linear combinations of source-group records and pairings to form sketches, tests the sketches of the result and the difference when there is an old record, and directly checks its ordinary assignment against \(S\), checks the three tag bits, and returns the ordinary witness only. In rank at most three, there are at most four assignments with first coordinate 1 to test: row echelon pivot coordinates determine the vector, pivot 0 must be present, and at most two remaining pivot choices are bits. Output is therefore always \(\bot\) or a witness. A record creation, result, or difference touches \(O(K_1N_\star+n)\) field elements, since a source-group record uses at most \(K_1\) length-\((N_\star+1)\) vectors or \(6A_c\) values, and the pairings compute six such combined sketch vectors. For a pairing, forming the inner products in the G2 record or summing per left leg and combining the G1 vectors uses \(O(K_1N_\star+n)\) operations. A test uses \(O(N_\star)\) for elimination with at most three rows and \(O(N_\star+|S|)\) to generate and check the constant number of candidates. Initialization samples \(6A_c(N_\star+1)\) field values, enters the \(L\) labels as records whose vectors are materialized on first use, and uses \(O(nN+L)\) time. There are at most four tests per result. Thus the extractor uses \(O((Q+1)(nN+|S|)+L)\) time because \(K_1\le n\) and \(N_\star\ge1\).

The reduction on input a uniform \(A\in R_q^{k\times\ell}\) samples the seed, programs the seed oracle at that seed on matrix columns 1 through \(\ell\) using \(A\), and samples the other answers lazily, including the independent column 0. It samples encryption coins as specified, produces the ciphertext for \(m_b\), and simulates all generic labels and names and random oracles by the protected lazy tables. It runs \(\mathcal A\) once. The extraction steps use the answered generic transcript without its output or the random-oracle query transcript, while the lazy tables implement exactly the direct oracle law. Because the programmed entries are jointly independent uniform ring elements for uniform \(A\), all oracle answers including entries at the selected seed have exactly the joint law of the experiment. Private evaluation points are sampled independently of the run.

The reduction keeps records evaluated at its private test point, using the protected rules for guessed operands and for existing records. It tries the first GT result whose label has an existing record of different private value, using the difference expression, and also the target label's record if present. For each tried expression it computes three independent gradient vectors in the plain sector at private recovery points, tests their span for a kernel vector, and applies LIFT with radius \(\beta_{\rm use}\) if there is such a vector, making the selection specified in Amendment msis_bound in mode one. An output from LIFT is a short multiple of that kernel vector. The coefficient of \(T^0\) in \(z(v)\) is \(v_0\). All \(kd_R\) remaining row coefficients give the equations of \(A\) on the packed input once \(v_0=0\). Thus a nonzero kernel vector has \(v_0=0\) and satisfies \(A\hat v=0\). Its short multiple has \(x_0=0\) since \(2\beta<q\). Reduction and packing commute, and packing preserves all ordinary and tag coordinates by Amendment ell and adds only zeros. This packs the output into a nonzero norm-at-most-\(\beta_{\rm use}\) solution to \(A\hat x=0\), exactly for the challenge whose rank, columns, bound, and norm are costed by M1. If no such output is found the reduction returns \(\bot\). Denote its success probability by \(s_b\). The cost is \(t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT}\) with \(Q_H\) the maximum per-oracle query count, \(C_R=O((N_\star+n)D+\mu)\) for the fixed simulation setup and postprocessing, and \(T_{\rm LIFT}\) the time of the lifting step. The reduction-time argument in C7 proves this reduction-time bound on the revised lists, including the original private record and gradient loop costs and the new fixed setup. The inverse conditions and comparison count do not enter those time calculations. LIFT's running-time result applies since \(2\beta_{\rm use}<q\) and \(24\beta_{\rm use}^4<q^3\) by P4 and \(\beta_{\rm use}\le\beta\). In particular the cost is \(t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)\) using \(n,N_\star\le D\).

Here is how the first-mark bounds apply to these algorithms. The degree and view for the new field encoding and the needed gradient formula are derived above. The record invariant uses no inverse premise: setting all guesses to zero commutes with additions and pairings, and before the first mark every reused label comes from formally equal expressions. Formally equal target expressions have identical stacks by the fiber equations applied to their difference for every field search vector. Thus their records also have equal sketches. A good mark's stack is usable with the three field ties of Amendment C7 by the revised view. Its rank is at most three by \(g^{-4}<\mu_{\rm tr}<\theta\) from (I5) and the protected stack rank bound. On the dense choice the stronger guard \(g^{-3}<\mu_{\rm tr}\) gives rank at most two. The full classification applies to every actual tied stack of dimension at most three, including zero-corner marks, because the three ties just derived are the original field identities. A kernel vector in its row space has coordinate 0 equal to zero, and its one-dimensional guessing probability is at least the stack's, by the protected guessing-probability lemma. In mode zero I6 gives a short multiple at radius \(\beta\). In mode one the selection in Amendment msis_bound gives a short multiple at radius \(b_{\rm s}\). Thus LIFT succeeds at the selected challenge radius.

At a first good difference mark its difference is formally nonzero, so the cleared polynomial is nonzero in the coins at some fixed search vector. This makes it a nonzero joint polynomial in coins and search coordinates. The private test uses independent uniform search coordinates and valid coins; the product-set bound gives failure probability at most \(d_f/(q-D)\). Earlier formal equalities are equalities at every private point by the record invariant, so outside this failure the reduction picks exactly this difference. The degree bound and the uniform valid coin ranges give probability at most \(\varepsilon_f\) for this failure. For a first good key mark the target record already has its expression by the record invariant and persists. Name negatives are target-group results and receive the same private and sketch tests. For a recognized good mark, the coefficient-vanishing and derivative calculation of the algebraic view subsection place each sector gradient in that sector row space. There is no nonzero alpha stack. For any proper subspace of the mark row space choose a linear form zero on the subspace and nonzero on the row space. Its value on one gradient, divided by \(\pi\), is a polynomial of degree at most \(n+2+2K_2\), using the seed-mode bound in the C7 degree ledger. This polynomial is nonzero by isolating the constant term in \(\varepsilon\) and the distinct monomials \(s_X\upsilon^{k_c}y_i\). The valid values for the independent coin coordinates have sizes at least \(q-D\), by the independent coin support argument. The polynomial root bound, with \(q-D\) in place of \(q\) in its proof, bounds the chance of failing to increase the span while it is proper. Three independent points and rank at most three give failure at most \(3(n+2+2K_2)/(q-D)\le\varepsilon_f\), by \(2n\le D\) and \(2K_2\le n\) and the formula for \(\varepsilon_f\). Thus on a good first mark with a kernel vector, except for the two exceptional events just bounded, the reduction finds a kernel vector in the appropriate span, and produces the MSIS output. The unconditional probability of such a mark is at most \(s_b+2\varepsilon_f\).

For a good first mark with no kernel vector, the classification proved in Amendment C7 gives an extended witness in its row space. Its ordinary projection satisfies the external system. In that sector the linear map from a tuple of probes to \(\sum_c W_cv_c\) has image the row space, as each matrix is symmetric and the sum of its images is the row space of the stack. Uniform independent probe tuples give three independent uniform vectors in this space, even conditional on the run. In dimension \(a\le3\), the chance of failing to span is bounded by \(\sum_{j=0}^{a-1}q^{j-3}<2/q\): equivalently the \(a\) rows of the random \(a\)-by-3 coordinate matrix are independent uniform three-dimensional vectors and the next row falls in the span of \(j\) independent previous rows with probability \(q^{j-3}\). At a difference mark the extractor tests the record difference. If the old entry is a pure guess, a guess-free difference requires the result to contain that same guessed variable with coefficient one. The label has therefore been used in an answered call, possibly the current call, and has a zero record by the test. At a key mark it tests the record of the result that obtained the target label. An initially received record has zero stack and thus is no good mark. These facts from the record invariant show that if the sampled vectors span, the witness is among the assignments tested. So the probability of a good first mark with no kernel vector and with extractor failure is at most \(2/q\).

Let \(u=2Q+2\). Every target query run has a first mark. The protected initial and guessed-mark estimates and the charged-mark estimate of Amendment Ncmp bound their three probabilities by
\[
\left(\binom{L_1}{2}+\binom{L_2}{2}+\binom{L_T}{2}\right)\varepsilon_f,\quad
N_{\rm cmp}(u)(\theta+\varepsilon_f)
+\left(\binom{L+3u}{2}+L+3u\right)\varepsilon_f,\quad
2^\lambda/N_{\rm free},
\]
respectively. These estimates concern the same sampler, oracle and record laws and use only the already checked view and degree properties, budget, and label counts. Together with the two good-mark cases they cover the event of a target key query and no witness. Their sum is at most \(s_b+E(u)\): the good-mark excess is \(2\varepsilon_f+2/q\le (8u+8)\varepsilon_f\), using \(\varepsilon_f\ge1/q\); the remaining terms of \(E\) are nonnegative and its guess term contains \(2^\lambda/N_{\rm free}\). By (P5) and the generic-ledger implication of Amendment Ncmp \(E(2Q+2)\le(Q+1)/2^\lambda\). Hence for each \(b\) the target-query and no-witness probability is at most \((Q+1)/2^\lambda+s_b\), with exactly the stated oracle budgets and one MSIS instance. This proves Theorem 5.9 with its extraction time and soundness as above.
