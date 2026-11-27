# Two-tag Praxis with dense scalar SIS and an exact work ledger

Throughout the proof \(N\) is the protected external variable count and \(N_\star=N+2\) is the number of internally sampled box coordinates. The two internal Boolean coordinates do not change which external witness relation is encrypted. The construction, coefficient placement and probabilities for the amended model follow.

## Amendment C5

Use mode 2 for the finite scoring shape and mode 1 for the asymptotic family. In mode 2 require \(\lambda=100\), \(N=391693\), \(d_R=1\), \(k=4103\), \(\nu=2048\), \(n_{\mathsf c}=1692\), \(J=22\), and \(\Delta=333824\). Use \(R=\mathbb Z[Y]/Y=\mathbb Z\), with coefficient basis \(1\), and \(R_q=\mathbb F_q\). The seed samples one independent uniform scalar per row and column. The nonconstant columns are exactly a dense uniform \(4103\)-by-\(\ell\) scalar SIS matrix. Its output norm is the largest absolute integer coordinate in this same basis, with radius \(\beta_{\rm use}\). No change of basis or structured decomposition is used in this scored instance. Multiplication by a fixed scalar takes one field multiplication and its transpose has the same cost. The more precise weighted mask computation that fits the protected scalar allowance is given in C7.

The asymptotic alternative, mode 1, requires \(\lambda>100\), \(k=1\), \(d=d_R\ge512\), \(2d\le D\), \(d<q\) and \(d^2<q-1\). Its split reduction and integer lift follow below. This alternative supports the growing family in C7. The exact finite encryption and decryption ledgers refer to the unique finite shape admitted by mode 2. The original fixed-price benchmark is a finite count at that shape, while the asymptotic implication uses the demonstrated field and group algorithms in mode 1.

### Irreducible lift with split reduction

On the split branch use the hypotheses of mode 1 above.

Write the binary expansion of \(d\) as \(d=\sum_{i=0}^{s-1}m_i\) with distinct powers of two \(m_i\), in increasing order. The power-of-two subgroup guaranteed by C3 contains a subgroup of order \(m_i\) for every factor since \(m_i\le d\le D/2\). The number of factors satisfies \(s\le1+\log_2 d\le d\). Fix a public generator \(\gamma\) of \(\mathbb F_q^*\), and consider
\[
 \bar P(Y)=\prod_{i=0}^{s-1}\left(Y^{m_i}-c_i\right),
 \qquad c_i=\gamma^{(i+1)m_i}.
\]
The \(i\)-th factor has exactly the roots \(\gamma^{i+1}\mu_{m_i}\), where \(\mu_{m_i}\) is the group of \(m_i\)-th roots of unity in \(\mathbb F_q\). These roots are distinct because \(m_i<q\). For two different indices an intersection would give \(\gamma^{i-j}\in\mu_{\max(m_i,m_j)}\): these two subgroups are nested, since their orders are powers of two. This would imply that \((q-1)/\max(m_i,m_j)\) divides the nonzero integer \(i-j\). But that divisor is at least \((q-1)/d>d\) and \(|i-j|<s\le d\). This contradiction proves that all \(d\) roots are distinct and that \(\bar P\) splits completely in \(\mathbb F_q\).

Lift each nonconstant coefficient below the leading term of \(\bar P\) to an even integer in its residue class modulo \(q\); lift the constant coefficient to a value congruent to 2 modulo 4 in its residue class modulo \(q\); keep the leading coefficient 1. The choices exist and can be fixed by taking the least nonnegative value in the respective congruence class modulo \(2q\) or \(4q\), since \(q\) is odd. This defines an integer monic polynomial \(P\). It is irreducible over \(\mathbb Q\). In fact if it has a nontrivial factorization over \(\mathbb Q\), its monic factors have integer coefficients by the monic integral factor property. Modulo two their product is \(Y^d\) and their degrees do not drop, so both are powers of \(Y\) of positive degree. Both integer constant coefficients are even, making the product divisible by four, contrary to \(P(0)\equiv2\bmod4\). This verifies irreducibility directly.

Use \(R=\mathbb Z[Y]/(P)\) and \(R_q=\mathbb F_q[Y]/(\bar P)\), both in the power basis \(1,Y,\ldots,Y^{d-1}\). Reduction of an integer coefficient vector is componentwise modulo \(q\), and it respects addition and multiplication because the defining polynomial reduces to \(\bar P\). A uniform element of \(R_q\) has exactly \(d\) independent uniform field coefficients. The challenge matrix is uniform in this ring, and its solution criterion is the same nonzero integer power-basis vector with coefficient infinity norm at most \(\beta_{\rm use}\) and product zero modulo \(q\). We use the coefficient basis in both the actual reduction and the estimate, with no change of the norm to evaluations at the roots. Each ring row gives exactly \(d\) coefficient equations, so the unrolled dimensions used by M1 are \(kd\) and \(\ell d\). This is the same specified convention for costing the uniform coefficient-ring challenge. The ring construction is deterministic from public constants.

### Arithmetic and transpose on the split branch

The public \(\bar P\) can be formed with \(O(d\log(2d))\) field operations: multiply the \(s\) binomials in order, using a shift and a scalar multiple at each step for each coefficient of the running polynomial. All intermediate lengths are at most \(d+1\). The \(c_i\) values follow from successive powers of \(\gamma\) and \(O(\log(2d))\) multiplications for each. This and the coefficient lifts fit the fixed setup bound with \(d\le D\). The public field computations concern \(R_q\), so the integer lifts introduce no subsequent field cost.

To multiply \(a,u\) in coefficient form, form \(f=a u\) of degree at most \(2d-2\) by a power-of-two FFT convolution in the subgroup from C3. This works since \(2d\le D\), and takes \(O(d\log(2d))\) field operations. To reduce it, write its quotient and remainder under \(\bar P\) as \(Q_0,R_0\), with \(\deg Q_0\le d-2\), \(\deg R_0<d\). Use reversed polynomials with fixed lengths: \(F^\star(Y)=Y^{2d-2}f(1/Y)\), \(Q^\star(Y)=Y^{d-2}Q_0(1/Y)\), and \(P^\star(Y)=Y^d\bar P(1/Y)\). The reversal of \(R_0\) in length \(2d-1\) is divisible by \(Y^{d-1}\), so
\[
 Q^\star=F^\star (P^\star)^{-1}\bmod Y^{d-1},
 \qquad P^\star=\prod_i(1-c_iY^{m_i}).
\]
The inverse product can be applied one factor at a time to the truncated vector. Dividing a truncated series \(a'\) by \(1-c_iY^{m_i}\) at this length uses the recurrence \(b_j=a'_j+c_i b_{j-m_i}\), with negative indices zero. It costs \(O(d)\) per factor. Reverse \(Q^\star\) to recover \(Q_0\), compute \(\bar P Q_0\) by the same sequence of binomial shift operations, and subtract it from \(f\), which gives \(R_0\) by division uniqueness. These steps take \(O(sd)=O(d\log(2d))\) additional field operations. No evaluation coordinate is used as an integer coordinate of the challenge.

The product circuit for fixed ring entry \(a\) is linear in \(u\): convolutions by fixed values, frequency scalings, fixed permutations and copies, additions, and fixed-scalar products in the monic reduction. It has \(O(d\log(2d))\) operations, with at most two inputs to each linear operation. The explicit reverse accumulation proved in the preceding transpose paragraph applies to this circuit, producing the coefficients of \(u\mapsto\langle L,a u\bmod\bar P\rangle\) from the form multiplier table \(L\) in the same time. It works for every multiplier table, including those from the mixed-base Frobenius coordinates, since it assumes no shape of \(L\). Thus formation of the three evaluated masks and decryption's ring products have the same \(O(k(\ell+1)d_R\log(2d_R))\) form-work bound. This split circuit is used for the asymptotic family. The finite method and all scalar operations at the scored shape are enumerated in C7 and n1. In the reduction one can alternatively use naive convolution and monic division in \(O(d^2)\) operations and transpose that linear circuit, giving the same \(O((N_\star+n)D)\) fixed cost used in C7. Indeed \(kd\le n\) and \((\ell+1)d=(\lceil N/d\rceil+3)d<N+4d\) by the exact column count in Amendment ell. Hence \(k(\ell+1)d^2<n(N+4d)\), which is \(O((N_\star+n)D)\) since \(n,d,N_\star\le D\).

The common packing and distribution argument below applies to this branch as well. It uses monicity, the full coefficient basis and the ring equation under reduction, all established here. The rest of the construction acts on the field coefficient forms \(z\), with the same positions and degrees under Amendment n and C6, and the same three ties. Its rank-three classification, view, packing, entropy bounds and proof of extraction do not depend on how ring products were computed. With the above ring operations its group counts, oracle counts and required complexity bounds remain the same. Amendment C7 uses the split ring for the joint asymptotic parameter family.

### Kernel conversion and scope

The coefficients are placed at the slots proved in Amendment n. Each uniform entry has exactly \(d_R\) independent field coefficients in the stated power basis. A form-kernel vector therefore has constant coordinate zero and maps to zero under the nonconstant columns in the selected coefficient ring. Conversely these equations force all form coefficients to vanish. A short integer scalar multiple has integer coordinate 0 equal to zero because its residue vanishes and \(2\beta<q\). Forming the packed vector by Amendment ell preserves every ordinary and tag coordinate once, adds only zeros, and commutes with integral reduction and field scaling. This proves the kernel-to-Module-SIS conversion in the heavy-stack lemma and in Targets. The rank bound and inverse theorem use only the search distribution and the short multiple of a vector with zero constant coordinate. Their hypotheses and conclusions are independent of the choice of monic ring. LIFT is a base-field integer-vector operation, so its correctness and time bounds are also independent of that ring.

The reduction programs the chosen uniform Module-SIS challenge into the nonconstant seed matrix columns and samples the constant entries independently in the same ring. This is exactly the stipulated random oracle distribution. The view, mask, classification, and reduction arguments use the resulting linear form map, its stated kernel, and its coefficient tables. Their proofs in Amendments n, C6, C7 and Targets apply without further ring identities. The same ring algorithms account for preprocessing and kernel tests, with the already stated query and runtime capacities. The split ring supports the growing power-of-two form degree in the asymptotic corollary of Amendment C7. Correctness, extraction and the extractability-error corollary for this exact instance follow from Targets and Amendment Ncmp.

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
2b_{\rm s}^3\ge3q^2\lfloor H_3\rfloor,\quad b_{\rm s}^2\ge q\lfloor H_3\rfloor^2,\quad 2\lfloor H_3\rfloor^2<q .
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

The external system \(S\) and its number \(N\) of Boolean unknowns are fixed. Internally extend an assignment with two auxiliary Boolean coordinates \(\mathsf b_1,\mathsf b_2\), all unconstrained except for their Booleanity. Put \(N_\star=N+2\). The extended assignment vector has \(N_\star+1=N+3\) coordinates including the homogeneous coordinate zero. Every witness of the external system has all four extended tags, and projecting any extended witness onto coordinates zero through \(N\) gives an external witness. The encoding uses no tag as an extra condition on the external system.

Use \(N_\star+1\) distinct Booleanity points \(d_0,\ldots,d_{N_\star}\), a distinct key point \(\rho\), and the same \(n_{\mathsf c}\) cosets of size \(\nu\) for the external constraints. Hence \(D=N+4+\nu n_{\mathsf c}\). For the finite algorithm use exactly the protected subgroup placement at this \(D\), with cosets first and the other points in bit-reversed order. The algebraic identities below hold for all admissible choices of points. In the growing family use the same subgroup placement with a sufficient power-of-two subgroup. At \(d_0\) set \(A=0,B=e_0\). At an ordinary \(d_i\), \(i>0\), set \(A=e_i-e_0,B=e_i\). At each tag Booleanity point \(d_i\), set \(A=\lambda_i(e_i-e_0)\) and \(B=\lambda_i e_i\) with \(\lambda_i=Z_*^{\prime}(d_i)/Z_*^{\prime}(\rho)\), a nonzero public scalar since the evaluation points are distinct. At \(\rho\) set \(A=e_{\mathsf b_1},B=e_{\mathsf b_2}\) so the key corner of a test matrix is \(W_{\mathsf b_1,\mathsf b_2}\). On the constraint cosets keep the protected evaluations, extending those linear forms by zero in the tag entries. The coordinate polynomials are the unique interpolants of degree below \(D\). Store their sparse point-value descriptions rather than a dense coordinate-by-degree table. Define \(Z_0\) to vanish at all \(d_i\) and \(\rho\), \(Z\) at every evaluation point except \(\rho\), \(Z_*=(X-\rho)Z\), and \(L_\rho=Z/Z(\rho)\). Thus \(Z_*=Z_0Z_{\mathcal K}\), where \(Z_{\mathcal K}=\prod_t(X^\nu-\delta_t^\nu)\) is the monic coset vanishing polynomial.

Here is the QAP criterion under this setup. For a symmetric \(W\), \(P_W=A^\top W B\) takes values \(0\) at \(d_0\), \(W_{ii}-W_{0i}\) at ordinary \(d_i\) with \(i>0\), \(\lambda_i^2(W_{ii}-W_{0i})\) at tag \(d_i\), and \(W_{\mathsf b_1,\mathsf b_2}\) at \(\rho\). On each constraint coset \(P_W/Z_0\) is the list of terms in that constraint's quadratic test. Let \(R_W\) be the polynomial of degree below \(\nu n_{\mathsf c}\) interpolating these coset values. The sum of \(X^a\) on \(\delta_t\mathcal G\) is zero unless \(\nu\mid a\), in which case it is \(\nu\delta_t^a\). Among degrees below \(\nu n_{\mathsf c}\), the multiples of \(\nu\) give an invertible Vandermonde matrix in the distinct \(\delta_t^\nu\). Consequently all coset sums vanish if and only if \(R_W\) omits all divisible powers. Under the Booleanity and constraint tests, \(P_W-W_{\mathsf b_1,\mathsf b_2} L_\rho-Z_0 R_W\) vanishes at every evaluation point. It is therefore divisible by \(Z_*\), with quotient degree below \(D-1\) from \(\deg P_W\le2D-2\). Equivalently \(P_W-Z_0R_W\) is divisible by \(Z\) with quotient degree below \(D\). Conversely, either such identity with an allowed \(R\) implies the Booleanity values and the coset sum tests by evaluation, and \(R\) is the unique interpolated remainder. In the key identity, evaluation at \(\rho\) gives exactly the specified corner \(W_{\mathsf b_1,\mathsf b_2}\). For a witness vector \(v\), these identities apply to \(vv^\top\), with \(P_v=A_v B_v\) and key corner \(\mathsf b_1\mathsf b_2\).

The new key evaluation still has \(A(\rho)=e_{\mathsf b_1}\), which together with the nonzero multiples \(A(d_i)\) of \(e_i-e_0\) for \(i>0\) spans all form coordinates: the differences span the hyperplane of coordinate sum zero and \(e_{\mathsf b_1}\) has coordinate sum one. The vectors \(B(d_i)\) are nonzero multiples of \(e_i\), hence are still a basis. The rescaled Booleanity equations at the tag points are equivalent to the original tests because their factors \(\lambda_i^2\) are nonzero. These properties, the QAP criterion and the updated \(D\) are the only changes in the generic comparison and coincidence arguments, explicitly used in C7. The point descriptions consist of the nonzero input terms and \(O(D)\) point data. For evaluation of all coordinate polynomials at a scalar off the point set, tabulate the \(D\) Lagrange weights there and accumulate the listed nonzero coordinate entries times their weights. For a witness, accumulate the point values of the two scalar witness polynomials and interpolate only those two polynomials, not the coordinate table. The same subgroup interpolation and vanishing-polynomial algorithms therefore give \(O(|S|+D\log D+\log q)\) setup and the claimed scalar polynomial work with these point sets. The two extra Booleanity evaluations add only a constant number of nonzero coefficients. The score still uses the fixed original nonzero-coefficient charge.

## Amendment ell

Set \(\ell=\lceil N/d_R\rceil+2\). Put the ordinary coordinates into the first \(\lceil N/d_R\rceil\) columns in order, padding with zeros. Put the two tag coordinates into the constant coefficients of the two remaining columns, each in its own column with zero other coefficients. Column zero still takes the separate homogeneous coordinate. The matrix entries in every column are independent and uniform in the coefficient ring.

The placement is injective, preserves coefficient infinity norm, and commutes with reduction and field scaling. The slot-zero form is \(v_0\), and the other forms are exactly the coefficient list of the matrix product of the packed input. A form-kernel vector has \(v_0=0\) and \(A\hat v=0\). Thus the short multiple used by the reduction packs to a nonzero solution of the same norm to the uniform Module-SIS problem with dimensions \(kd_R,\ell d_R\). For any fixed tag variant of an external witness, condition on all columns except column zero. Since its homogeneous coordinate is one, the independent uniform column zero adds a uniform coefficient vector to the remaining fixed vector. Consequently the complete form value of each such variant is uniform on the affine constant-slot-one hyperplane. This distribution is sufficient for both the exact key-weight bound and the expected fallback bound.

## Amendment Bsearch

Use the independent box sampler on \(N_\star=N+2\) coordinates and one extra independent box value \(r_\diamond\), all uniform on \(\{2,\ldots,g+1\}\). Set
\[
 r_0=A_0+r_\diamond-\left\lfloor{\tfrac12\sum_{i=1}^{N_\star}r_i}\right\rfloor,\qquad
 A_0=\left\lceil N_\star(g+1)/2\right\rceil .
\]
Given the box coordinates, the zeroth coordinate is uniform on a translate of \(g\) integers, distinct modulo \(q\). The public center for a Boolean vector \(v\) with \(v_0=1\) is
\[
 c_v=\left\lfloor A_0+\frac{g+3}{2}\bigl(1+\operatorname{wt}(v)-N_\star/2\bigr)\right\rfloor .
\]
If \(X_i=r_i-(g+3)/2\), and \(X_\diamond=r_\diamond-(g+3)/2\), then \(r(v)-c_v=X_\diamond+\sum_i(v_i-1/2)X_i+E\), where the two rounding terms in \(E\) have absolute sum at most \(3/2\). The independent centered sum has variance \((g^2-1)(N_\star+4)/48\). Thus its full RMS is at most \(g\sqrt{(N+6)/48}+3/2\) by the triangle inequality in quadratic mean. Each \(|X_i|\le(g-1)/2\); the deterministic bound including rounding is at most \(B=(N+3)(g+1)\). A centered difference of two tag coordinates or a single centered tag coordinate also lies in this range. This is the definition of \(B_{\rm search}\). The protected check \(2B+1<q\) gives unique valid bounded representatives for all the searches in the amended correctness algorithm.

The guessing probability of a rank-\(d\) stack is still at most \(g^{-d}\). For any prescribed joint fiber, pick a nonsingular \(d\)-column pivot minor of a basis of the row space. If the zeroth column is nonzero, it can be extended to a pivot basis by linear independence of the columns. Fix the remaining nonpivot box coordinates; any solution fixes the pivot box coordinates and the zeroth coordinate uniquely by the invertible linear system. The regular pivot box draws therefore have probability at most \(g^{-(d-1)}\) of meeting their fixed values, and conditional on all box coordinates \(r_0\) has probability at most \(1/g\) of the required value. If the zeroth column is zero, no condition involves \(r_0\), so fixing the other box coordinates directly bounds the pivot solution by \(g^{-d}\). These probabilities hold for every fixed fiber and give the claimed bound. For a kernel vector the zeroth coefficient is zero, so its scalar guessing probability uses precisely the independent box coordinates, now on at most \(N_\star\) positions. The inverse and regularization proofs apply in that dimension with the factors of I3 and \(T_{\rm tr}\) stated next. All heavy-stack and generic ledger arguments therefore use the same guessing-probability implications. The actual arithmetic of the search is supplied in Amendment search_spread.

## Amendment T_tr

Use \(T_{\rm tr}=R_{\rm tr}g\sqrt{(N+2)/3}\). The trimming radius and covariance proof in I3 is used on the independent box of dimension at most \(N_\star\). Each projected feature-row deviation from its center is at most \(R_{\rm tr}(g/\sqrt{12})\sqrt{N_\star}\) times the corresponding basis-vector infinity norm, by the Euclidean Cauchy--Schwarz bound on that row's coefficient norm. Taking differences doubles the bound and gives precisely this new \(T_{\rm tr}\). The minor and prefix-lift argument of I6 uses the checked inequalities in I5 with this value. The projected counting constants in I3 use \(N_\star\) for the same reason. The definitions of regularity, fiber densities and their trimming loss use only the width, coefficient lattice and the radius and have the same arguments. Thus the amended radius supplies the lattice-facts hypothesis and norm proof in the new sampler dimension.

## Amendment C6

Require \(n\ge10\) even, the field branch below, one of the two C5 modes, \(2n\le D\), and \(\Delta\ge n+3\). Amendment n gives \(n=kd_R+1\) in both modes. Use precisely this one-variable field in the grid of Amendment C7. The additional requirement \(n\ge10\) supplies the affine quadratic rank used in the correctness proof. The chunk alignment is supplied by P1.

For \(\mathrm{seed\_mode}=0\), require \(n\mid q-1\). Take \(F_0=\mathbb F_q\) and \(P_H=H\), so only the basis digit zero occurs. Use the relative modulus \(P_T(T)=T^n-d_*\) with \(d_*\) a public primitive scalar. For a nonzero root \(t\) of this binomial, its multiplicative order \(m\) satisfies \(m/\gcd(m,n)=q-1\). Each prime divisor of \(n\) divides \(q-1\), so the valuation of \(m\) there is the sum of its valuations in \(n\) and \(q-1\). The other valuations are those of \(q-1\). Hence \(m=n(q-1)\). For \(p\mid n\), write \(q=1+a\) with \(p\mid a\). For odd \(p\), in \((1+a)^p-1\) the first term \(pa\) has strictly smaller valuation than every later term, by the binomial coefficient divisibilities and \(p>2\). At \(p=2\) this also holds because \(4\mid a\). Taking a positive power prime to \(p\) preserves the valuation by factoring the difference and reducing the geometric sum modulo \(p\). Iterating gives \(v_p(q^j-1)=v_p(q-1)+v_p(j)\). Thus the Frobenius orbit has size \(n\), and the minimal polynomial of \(t\) is \(P_T\). At \(j=n/2\) we have \(m/2\mid q^j-1\) but \(m\nmid q^j-1\). The ratio \(t^{q^j}/t\) is therefore the nontrivial square root of one, which is \(-1\). This gives the half-turn sign and the even support of \(V\), and the three conjugate projections still have their original field identities.

Since \(q\equiv1\pmod n\), the representative of the \(j\)-th Frobenius image of \(T^s\) for \(0\le s<n\) is the scalar \(d_*^{s(q^j-1)/n}\) times \(T^s\). The coefficient can be computed using the residue of \(q^j\) modulo \(n(q-1)\). The power for \(s=1\) takes \(O(\log q)\) field operations and the remaining table uses successive products in \(O(n)\) operations. The evaluated form multipliers use the same coefficient slots of Amendment n and the same transposed ring evaluation in Amendment C5. The product, weight, mask, view and classification computations use these one-variable representatives as detailed in C7. No auxiliary-variable evaluation is needed.

### One-variable modulus from a bounded seed field

The seed branch keeps \(e=1\), so \(F_0=\mathbb F_q\) and \(P_H=H\). It requires \(n\le4800\), \(2\le s_0\le32\) integral, \(2s_0\mid n\), and \(r_H=n/s_0\mid(q^{s_0}-1)^{28}\). The gate fixes the degree at 2 and the quotient at 2052 for the submitted seed branch. Here \(s_0=\mathrm{seed\_degree}\), \(Q=q^{s_0}\), and \(r_H\) is even. The same chunk, FFT and evaluation-point conditions hold. In this branch \(\mathrm{seed\_mode}=1\); in the preceding branch it is zero.

Choose \(K=\mathbb F_q[X]/(f(X))\) for a monic irreducible \(f\) of degree \(s_0\). This step can use uniform random monic polynomials of that degree, with a test as follows. Compute \(X^{q^{s_0}}-X\) and \(X^{q^{s_0/p}}-X\) modulo \(f\) for each prime \(p\mid s_0\). The first must be zero and each of the latter must have gcd 1 with \(f\). The roots of \(X^{q^a}-X\) are all elements of \(\mathbb F_{q^a}\) and are simple. Thus the first test says the irreducible factors are distinct and have degrees dividing \(s_0\). Every proper divisor of \(s_0\) divides \(s_0/p\) for some such prime, so the other tests make every factor have degree \(s_0\). This proves the test's equivalence to irreducibility. The field of degree \(s_0\) has at least \(q^{s_0}-s_0q^{s_0/2}\) elements outside its proper subfields, by counting at most \(s_0\) subfields of degrees at most \(s_0/2\). Each orbit of these elements yields a different monic irreducible, so the sampling probability is at least \((1-s_0 q^{-s_0/2})/s_0\). The tests take \(O(\log q)\) field operations because the degrees and the number of tests are bounded.

In \(K^*\) choose \(c_H\) of degree \(s_0\) over \(\mathbb F_q\) with \(c_H^{(Q-1)/p}\ne1\) at every prime \(p\mid r_H\). All these primes divide \(Q-1\). The order condition at each such prime says that the exponent of \(c_H\) as a power of a multiplicative generator is nonzero modulo \(p\). Uniform sampling meets all order conditions with probability \(\prod_{p\mid r_H}(1-1/p)\). There are at most five primes because \(r_H\le2400\) and the product of the six smallest primes exceeds 2400. The product is at least \(2^{-5}\). The fraction of elements of \(K^*\) in proper subfields is at most \(s_0 q^{s_0/2}/(Q-1)<2^{-6}\) for the protected prime and this degree range. Therefore testing both the order condition and full degree succeeds with probability at least \(2^{-6}\). Test full degree by checking \(c_H^{q^{s_0/p}}\ne c_H\) for the primes of \(s_0\). Both tests cost \(O(\log q)\) operations per trial in the scalar field, since the degree of \(K\) and the number of tests are bounded. Its minimal polynomial \(p_c\) is the product of the \(s_0\) linear polynomials from the Frobenius orbit, with coefficients fixed by Frobenius. The public seed constants are independent of the system and encryption coins. Setup is deterministic once they are fixed.

Let \(t\) be a root of \(T^{r_H}-c_H\) in the algebraic closure. If \(o\) is the order of \(c_H\) and \(m\) the order of \(t\), then \(m/\gcd(m,r_H)=o\). The order tests give \(v_p(o)=v_p(Q-1)>0\) at each prime of \(r_H\). Thus \(m=r_Ho\). The prime-by-prime valuation formula above holds for \(Q\), including at two since \(4\mid Q-1\). For a positive \(j\), the condition \(m\mid Q^j-1\) is therefore equivalent to \(r_H\mid j\). Thus \(t\) has degree \(r_H\) over \(K\). As it generates \(c_H=t^{r_H}\), it also generates \(K=\mathbb F_q(c_H)\) over \(\mathbb F_q\). Its degree over \(\mathbb F_q\) is \(s_0r_H=n\). The monic polynomial \(P_T(T)=p_c(T^{r_H})\) of degree \(n\) vanishes at \(t\), proving irreducibility.

At \(j=r_H/2\), the same valuations show \(m/2\mid Q^j-1\) and \(m\nmid Q^j-1\). Consequently \(t^{q^{n/2}}=-t\), since \(Q^{r_H/2}=q^{n/2}\) and \(-1\) is the unique element of order two. Use the monomial basis through degree \(n-1\) in the same form slots as above. The \(V\) weights have even powers only. All three consecutive Frobenius projections have their original field identities and the same coefficient-kernel relation.

For exponent \(j\) of Frobenius put \(b_j=q^j\bmod r_H(Q-1)\). For each basis monomial \(T^a\), its reduced representative is obtained from
\[
 c_H^{\lfloor a b_j/r_H\rfloor}T^{a b_j\bmod r_H}
\]
by expanding the coefficient in the basis \(1,c_H,\ldots,c_H^{s_0-1}\) and replacing \(c_H\) by \(T^{r_H}\). The modulus for \(b_j\) suffices because the order of \(c_H\) divides \(Q-1\). This produces at most \(s_0\) powers of degree below \(n\), all congruent to \(a b_j\) modulo \(r_H\). For increasing \(a\), the quotient increments by \(\lfloor b_j/r_H\rfloor\) or by one more. Compute these two step powers with \(O(\log q)\) field operations and tabulate the representatives in \(O(n)\) operations using the bounded degree. Evaluate the table in \(O(n)\) operations given the evaluation point's powers. The resulting coefficients are used in the same ring transpose circuit and assigned to the same coefficient slots. 


## Amendment C7

Require \(\mathrm{base\_degree}=\mathrm{base\_left}=\mathrm{base\_right}=\mathrm{scalar\_rel}=1\), \(K_1,K_2\ge1\), and \(2K_1K_2=n\). This is the one-variable grid. Write \(e=A_H=B_H=1\) and \(h=n\) when using field-degree notation. There are \(A_c=3K_1K_2=3n/2\) cells, indexed by a left leg \(a\) with \(0\le a<K_1\) and a right leg \((b,\mathrm X)\), \(0\le b<K_2\), \(\mathrm X\in\{\mathrm E,\mathrm O,\mathrm V\}\). Write \(p_X=\mathbf1_{\mathrm X=\mathrm O}\). On the scalar-binomial branch set \(\lambda_a=2a\), \(k_{\mathrm{leg}}=2K_1b+p_X\). On the seed branch set \(\lambda_a=2K_2a\), \(k_{\mathrm{leg}}=2b+p_X\). Put \(k_c=\lambda_a+k_{\mathrm{leg}}\). For E and O the cell weight is the coefficient of \(T^{k_c}\) in \(U=z(w)\sigma^{n/2-1}(z(w))\); for V use \(V=z(w)\sigma^{n/2}(z(w))\). The half-turn fixes \(V\) so only even powers occur there. Euclidean division of the half-exponent by \(K_1\) on the first branch or \(K_2\) on the seed branch recovers the two digits, covering each slot exactly once. The key cell is \(a=b=0,\mathrm X=\mathrm E\), with weight the constant coefficient of \(U\).

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
Indeed the negative grade in the right E/O mask contributes degree zero exactly when multiplied by the twisted part of \(\pi_a\); the ordinary products supply the remaining terms. With the honest weights and the form vectors contracted against \(w\), each \(t_i\) vanishes in the field: \(U z_\circ=V z_-\), \(U z_+=\sigma^{n/2+1}(U)z_-\), and \(V z_+=\sigma^{n/2+1}(U)z_\circ\). On the scalar-binomial branch, their ordinary polynomial degrees are at most \(2n-2\) because conjugating a monomial preserves its slot. Thus monic division by \(P_T=T^n-d_*\) has no remainder and quotient degree at most \(n-2\). Publish the G2 bases with exponents \((\pi\eta_i/\zeta'')P_T(\upsilon)\upsilon^a\), \(0\le a<n-1\), for the three quotients. The positive grades indexed by \(i=1,2,3\) have support lengths \(2n-1,2n-1,2n-2\), since the \(i=3\) positive grade uses only V with exponent at most \(n-2\). The negative grades indexed by \(i=2,3\) each have length \(2n-1\). Publish their ordinary monomial powers under the exponents \(\pi\eta_i\varepsilon^{\pm1}\upsilon^a/\zeta''\), with the respective lengths. This gives \(C_{\rm mask}=13n-9\) slots. The honest values cancel by one G2 MSM using these bases paired with the witness sum of the Y column. All weighted leg products before multiplying by a form are single monomials, so their assembly is linear in the grid size. Polynomial multiplication and the binomial division use \(O(n\log n)\) scalar operations by C3 and \(2n\le D\).

In a formal identity, the Laurent comparison below isolates the same grade-zero polynomials for the actual stack up to multiples of \(P_T\). Their reduction gives all three stated field ties. The right-leg type \(s_{\mathrm X}\) and the ordinary exponent \(k_c\) distinguish every cell in the generic comparison. The proof of the original rank-three classification using these ties follows. The new QAP point at \(\rho\) changes only the corner used by the view and does not change the Booleanity or constraint tests used by that classification.

### Cancellation for the bounded seed modulus

In the added one-variable branch C7 requires \(2K_2\mid r_H\), \(K_2=18\), \(r_H=2052\), \(q\bmod 2052=721\), and checks the integer
\[
 R_*=n-r_H+\max_{0\le j<2K_2}(qj\bmod r_H).
\]
For the checked residue and right-leg count, the residues in increasing index are 0, 721, 1442, 111, 832, 1553, 222, 943, 1664, 333, 1054, 1775, 444, 1165, 1886, 555, 1276, 1997, 666, 1387, 56, 777, 1498, 167, 888, 1609, 278, 999, 1720, 389, 1110, 1831, 500, 1221, 1942, 611. Their maximum is 1997, and C7 checks the stated sum. This is an upper bound on the reduced degree of every conjugated right leg. Indeed at Frobenius exponent \(n/2+1\), the half-turn changes only a sign, so the exponent in C6 can use one scalar Frobenius. All powers produced by that formula are no larger than \(n-r_H\) plus their residue modulo \(r_H\). As \(q\) is prime and \(r_H<q\), the residues of \(qj\) are distinct for the \(2K_2\) listed indices. Hence \(2K_2-1\le R_*\le n-1\), using \(r_H\le n\).

Use left exponents \(2K_2 a\) and right exponents \(2b+p_X\). Every ordinary or conjugated left exponent is a multiple of \(2K_2\), since \(2K_2\mid r_H\) and the reduced residue and every higher term have this divisor. Their maximum is at most \(n-2K_2\). Ordinary right exponents are bounded by \(2K_2-1\) on E/O and \(2K_2-2\) on V. This verifies the same cell-scale degree bound as in the scalar-binomial case. The first honest tie has degree at most \(2n-2\). The next two have degree at most \((n-2K_2)+R_*+(n-1)\), which is at least \(2n-2\) by the lower bound on \(R_*\). Dividing by the chosen monic \(P_T\) gives quotient lengths \(n-1\) for the first and \(n-2K_2+R_*\) for each of the next two. The remainders vanish as these are the honest ties. The three positive grades have lengths \(2n-1,2n-1,2n-2\) by the ordinary right and conjugated left bounds. Each negative grade has length \(2n-2K_2+R_*\) by the ordinary left and conjugated right bounds. In total the per-sector list has
\[
 C_{\rm seed}=13n-8K_2+4R_*-5
\]
slots. Each uses the usual independent scale for its \(\eta\) and epsilon grade. The three grade-zero lists evaluate multiples of the monic \(P_T\) and therefore impose all three field ties by the same view proof.

C7 sets the parameter \(C_{\rm mask}\) to \(C_{\rm seed}\) on the seed branch and to \(13n-9\) otherwise. The maximum relative degrees of the monic polynomial times a published quotient power and of the cross-grade powers are at most \(3n-3\), using \(R_*\le n-1\) and \(K_2\ge1\). Only the variable \(T\) is used in these lists. Thus their degree bounds and recovery gradient separation follow the inequalities in the view proof below. The ordinary cell exponent \(2K_2 a+2b+p_X\) still occurs at degree zero in epsilon, so the coefficient isolation and row-space implications are unchanged.

In this branch the product of two individually conjugated legs has at most \(s_0^2\) powers, a bounded number. Append the accumulated weighted contributions to their ordinary polynomial positions in \(O(n)\) field work, then multiply these polynomials by the form polynomials using the same blocked convolution as on the scalar-binomial branch. For division or reduction by \(p_c(T^{r_H})\), group the terms by the exponent modulo \(r_H\). In each group divide the polynomial in \(T^{r_H}\) by the fixed monic bounded-degree \(p_c\). The group degrees are bounded because the input has degree \(O(n)\) and \(n=s_0r_H\). This is the unique monic division, and it costs \(O(n)\) work. As a result the same \(O(n\log n)\) field work bound covers the sparse branch, including weight construction, and it uses the same charged MSM, cancellation pairing and source counts. The old binomial calculation applies on the scalar-binomial branch.

### Scored encryption arithmetic

This section accounts for the scalar work separately from group operations in the fixed scored branch of C5. The split-ring family below has its stated asymptotic cost, while the finite allowance applies to every admitted scored scalar instance. In this branch \(4104\nmid q-1\), so the scored shape necessarily uses the seed-degree-two field in C6 and the fixed \(K_1,K_2\) from C7. Let \(S_{\rm nz}\) be the number of nonzero coefficients traversed to evaluate the coordinate QAP polynomials. The benchmark's protected system term assigns \(2^{30}\) to this traversal. We prove a bound of \(S_{\rm nz}+3m\) on the variable scalar work in the same counting convention, with \(m=k(\ell+1)\).

The public relative field setup stores each Frobenius table from C6. At the chosen \(\upsilon\), evaluate each of the three basis projection multipliers for the relevant conjugate. In the scored seed branch each table column has at most two monomials. Powers of \(\upsilon\) are formed by successive multiplication through the largest exponent used in the field or mask arrays. The three right mask form combinations are
\[
 A_\eta=\eta_1z_\circ+\eta_2z_+,\qquad
 B_\eta=\eta_2z_-+\eta_3z_\circ,\qquad
 C_\eta=\eta_3z_+-\eta_1z_-.
\]
The first two are dot products with two tables, obtained by combining the three projection-multiplier tables once. Since the coefficient ring has degree one, for each row and column of the public seed matrix these two dot products use exactly one multiplication apiece, then additions. The fixed slot-zero coefficient contributes directly at the homogeneous coordinate. Thus all ordinary and tag entries of \(A_\eta,B_\eta\) use at most \(2m\) matrix-coefficient multiplications. The third set of entries is computed by
\[
 C_\eta=(\eta_3 A_\eta-\eta_1 B_\eta)/\eta_2
\]
with one shared inverse and at most three multiplications per input coordinate. This identity uses the same independent \(\eta\) coins as the polynomial view and gives exactly the same masks. It is an implementation of existing exponents, so it does not alter their distribution or introduce a source element.

Evaluate \(Z_*,Z_0,Z\) at \(\tau\) by multiplying their respective subsets of the \(D\) differences \(\tau-p\), with at most \(3D\) multiplications. Invert the \(D\) differences by one batch inversion with at most \(3D\) multiplications and one scalar inversion. Multiply each inverse by \(Z_*(\tau)\) and by the public \(p\), with two multiplications per point. In the weighted representation of n1, an entry at \(p\) is stored as its original value divided by \(pZ_*^{\prime}(p)\). Multiplying the entry by this point weight gives its exact Lagrange contribution with one multiplication and an accumulation addition. Choosing the normalized tag evaluations in D changes no number of nonzero entries.

For the G1 factor arrays first compute \(\Omega_{12}y_i+\Omega_{22}A_i(\tau)\) for each of the \(N+3\) input coordinates, then multiply each of that result and \(y_i\) by each left scale \(\pi_a\). The Y column uses one further multiplication per coordinate. This portion uses at most \((2K_1+3)(N+3)\) scalar multiplications. For each right leg, calculate its scale, its second-coordinate scale \(s_{\rm leg}/\Omega_{22}\), and its constant mask multipliers before going through the inputs. On E and O the mask combines \(A_\eta,B_\eta\) using two multiplications and on V uses one with \(C_\eta\). The second coordinate \(H_2=s_{\rm leg}(B_i(\tau)-y_i)/\Omega_{22}\) needs one multiplication by its precomputed scale. The first coordinate \(H_1=s_{\rm leg}(r_i+A_i(\tau))+\vartheta_{{\rm leg},i}-\Omega_{12}H_2\) needs at most two more beyond the mask. Both right arrays therefore use at most \(15K_2(N+3)\) scalar multiplications in total.

The remaining ciphertext exponent calculations are the two lists of sparse and regular powers, their right operands, search bases, mask rectangles and one GT entry. The sparse and shifted G1 powers advance by \((\tau/c_{\rm q})^\nu\), with one extra power multiplication per shifted power. The regular list advances by \(\tau/c_{\rm q}\), with one multiplication per position including skipped ones. Including their scale multiplications, these lists use at most \(2(\Delta+2S_0)\). The \(A_c=3n/2\) cell scales \(\gamma_c\) are formed once. The \(J+2\) distinct right correction multiplier constants are prepared from the two vanishing values and the successive chunk powers, then the \((J+1)A_c\) right correction exponents each take one multiplication. The G2 search exponents are the previously computed right leg scales. For cancellation, evaluate the monic seed modulus by Horner evaluation and precompute the scalar for each grade including its possible modulus factor. Each of the \(C_{\rm mask}\) cancellation exponents then multiplies its table power by its fixed grade scalar once. The repeat of the generator, if present, needs no extra exponent calculation. The cell scales, the two combined form tables, the \(\upsilon\) power table and their evaluations, the left and right scale tables, the sparse stride, the \(J+2\) right multiplier constants, and the GT key and alpha scale use at most \(100(n+J+1)\) multiplications together. In detail the three Frobenius evaluations and the two combined tables take at most \(10n\), the power table at most \(3n\), the leg and cell scale tables at most \(10(2K_1+3K_2+A_c)<35n\), the sparse and chunk strides at most \(2J+600\) by bounded-length binary powering for their first values, and the remaining fixed scale products and the GT exponent at most \(10(J+10)\). The \(100(n+J+1)\) allowance exceeds this sum. At most eight scalar inverses, including the batch inverse, \(\varepsilon,\eta_2,\zeta_0,\zeta_1,\zeta'',\Omega_{22}\) and the public shift if needed, fit within 10,000 additional multiplications by binary powering at the protected prime. All fixed field setup data and public ratio denominators for the QAP points are precomputed independent of the encryption coins.

Besides \(S_{\rm nz}+2m\), the resulting upper bound is
\[
 8D+3(N+3)+(2K_1+3)(N+3)+15K_2(N+3)
      +2(\Delta+2S_0)+(J+1)A_c+C_{\rm mask}+100(n+J+1)+10000 .
\]
Under the fixed scored shape in C5 this is less than \(250000000\), whereas \(m=4103(391693+3)=1607128688\) is greater than \(1600000000\). The extra scalar work thus fits inside the unused one matrix multiplication per coefficient in the protected charge. Random scalar and seed-oracle operations and selecting Boolean entries do not require field multiplications. The subsequent group scalar multiplications are the published one per slot charged with the protected fixed-base prices.

### Efficiency and asymptotic choices

The complete publication and combination of correction bases, weighted factors and searches are stated in Amendments n1, n2 and the operation-count amendments. With the specified group representation sizes and the exact finite counts they give the amended objectives. No oracle is called more often than one seed query per matrix entry and at most one key query in either algorithm. The four internal tag variants reuse the same seed and field matrix. Each form evaluation and coefficient-ring adjoint has the same \(O(k(\ell+1)d_R\log(2d_R))\) cost as C5. All mask and field calculations use \(O(n\log n)\) operations per variant, after public field setup. The QAP and weight work is repeated at most a fixed constant number of times and uses \(O(D\log D+|S|)\) operations beyond ring and mask work, as established in n1. The ordinary branch uses three bounded signed searches, and the exact fallback has bounded expected cost as shown in search_spread.

For the asymptotic cost implication take mode 1 as \(\lambda\) grows past 100, and choose powers of two \(K_1,K_2\) of order \(\lambda\) with \(n=2K_1K_2\le N/8\) when \(N\ge\lambda^2\), and use \(k=1,d_R=n-1\) in split mode. Take the subgroup and interval premises supplying \(n\mid q-1\), the powers of two up to the bound in C3, and the supported range and generic ledger choices of I4 and P5. Use \(\Delta=\nu\lfloor D/\nu\rfloor\ge D/2\), so \(\Delta\ge n+3\) for sufficiently large instances, and \(J=\lceil((D-1)+\nu n_{\mathsf c})/\Delta\rceil\le4\), \(J'=1\). For linear-size systems with \(\nu\le2F_{\max}\), \(D=O(N)\) and \(n=\Theta(\lambda^2)\). The two extra coordinates and the two ring entries for tags per row do not change those orders. Then the source arrays contain \(O(\lambda N)\) field elements with bounded group representation degrees. In encryption each requested fixed-base multiple uses \(O(\lambda/\log\lambda)\) group additions by windows of width \(\lfloor\log_2\lambda\rfloor\): precompute all multiples in each of \(O(\lambda/\log\lambda)\) windows and advance the base by the window width. The tables take \(O(\lambda^2/\log\lambda)\) additions and the \(O(\lambda N)\) requested multiplications take \(O(\lambda^2 N/\log\lambda)\) field operations. In decryption the proved counts for a constant number of variants give \(O(\lambda N)\) group additions, \(O(N)\) MSM points and \(O(\lambda)\) pairings and other scalar multiplications. The original cost bounds for these group operations give \(O(\lambda N\log\lambda)\) work outside the searches, including the polynomial and ring operations. The centered search uses \(O(\sqrt{g}\,N^{1/4})\) expected operations by its explicit bound below, which is \(O(2^{\lambda/4}N^{1/4})\) under the admitted growth choices of I4. These are the desired asymptotic costs for the extended internal layout at the original external \(N\).

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

The powers in the two correction lists of n1 have nonzero public scalar factors determined by the public point choice. An arbitrary formal linear or bilinear coefficient absorbs these known factors. This preserves each polynomial span, every support bound and every degree and independence assertion for the power lists. The following calculations use the resulting powers with these nonzero constants absorbed.

Fix the seeded matrix and hence the form coefficients. For source exponents \(a\) in G1 and \(b\) in G2 include their generators. A guess-free target expression is
\[
 \mathsf E=\sum_{a,b}D_{ab}\,a b+D_K\alpha\kappa .
\]
The coefficients are fixed scalars. No source exponent uses \(\alpha\). With \(\varpi=\Omega_{22}\zeta_0\zeta_1\zeta''\varepsilon\) every product clears denominators, since G1 has none and the G2 exponents only use the displayed inverses to the first power. A left scale has degree at most \(n\) and the unscaled G1 factors have degree at most \(D\); the sparse and shifted G1 powers end at degree at most \(D\) including their scale. The other powers have degree at most \(\Delta\le D\) and the Y exponent has degree two. All G1 exponents thus fit \(d_1=D+n+2\). The left and right monomial exponents in a cell sum to \(k_c\le n-1\) and the conjugated left exponent has degree at most \(n-2K_2\) on the seed branch, whose right exponents are at most \(2K_2-1\). Therefore \(\gamma_c\) has total degree at most \(n+2\), with the key scale of degree three.

The cleared sparse correction bases have degree at most \(D+n+6\). For non-sparse ones the polynomial part has degree at most \(2D-2\) from P1, and the cell scale and remaining clearing factors give at most \(2D+n+4\). The first and second right coordinates before the masks have degree at most \(D+n+6\) after clearing, by \(k_{\rm leg}\le n-1\), the degree below \(D\) of the QAP polynomials and the linear hidden-basis inverse. Each term of a right mask is a leg power of degree at most \(n-1\) times a form of degree at most \(n-1\), with one \(\eta\) and an optional inverse \(\varepsilon\). It has cleared degree at most \(2n+5\). A cancellation basis has monomial degree at most \(3n-3\) and cleared degree at most \(3n+4\), including its scalar factors and clearing factors. Search bases have cleared degree at most \(n+5\). Since \(2n\le D\), all G2 exponents after clearing fit \(d_2=2D+n+6\). The cleared key terms fit \(D+8\). Hence the total degree bound before adding a guessed-operand factor is at most \(d_1+d_2=3D+2n+8\le d_f=3D+2n+2K_1+7\). The extra factor of degree one and each separate bound fit \((q-D)\varepsilon_f\) by its protected formula. The search coordinates enter only linearly, within the same degree bounds.

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
 n_1=(2K_1+1)(N+3)+2\lceil(D-1)/\nu\rceil+\Delta-\Delta/\nu
\]
transmitted G1 elements. Use the single factor sector, field mask bases and Y column of C7. Let \(S_0=\lceil(D-1)/\nu\rceil\) and
\[
 I_0=\{0\le a<D-1:\nu\mid a\},\qquad
 I_0^*=I_0\cup\{a+1:a\in I_0\},\qquad
 I_1=\{0\le a<\Delta:\nu\nmid a\}.
\]
Fix the public nonzero scalar \(c_{\rm q}\) described under scalar preparation below, and set it to 1 when that placement is not used. Put \(\bar\tau=\tau/c_{\rm q}\). Send \(P_a^0=[\zeta_0\bar\tau^a]_1\) for \(a\in I_0^*\), and \(P_a^1=[\zeta_1\bar\tau^a]_1\) for \(a\in I_1\). There are \(2S_0\) sparse entries because \(\nu\ge2\), and \(\Delta-\Delta/\nu\) non-sparse ones by alignment. Use \(Z_c=Z_*\) in the key cell and \(Z_c=Z\) elsewhere. Send one \(B_c^0=[\gamma_c Z_c(\tau)/\zeta_0]_2\) per cell and \(J\) bases \(B_{c,j}^1=[\gamma_c Z_0(\tau)\bar\tau^{j\Delta}/\zeta_1]_2\), \(0\le j<J\). The factor arrays, search bases and cancellation arrays are those of C7, each once. If the resulting count of G2 slots is odd, append an existing unit generator, computed with one multiplication by one. It is formally the same exponent as the existing generator. Send the seed, the one element \([\alpha\kappa]_T\), and the masked message. There is exactly one fixed-base generator multiplication per transmitted group slot and one more in GT for the key. All scalar exponents use the displayed fixed factors and tabulated powers, with constant work per exponent.

### A single combination at any tag

For the internal witness \(v=(w,\mathsf b_1,\mathsf b_2)\) put \(d_v=\mathsf b_1\mathsf b_2\). The identity of Amendment D gives the exact quotient
\[
 G_v=(A_v B_v-d_v L_\rho)/Z_0
      = Z_{\mathcal K}h_{\rm key}^v+R_v ,
 \qquad \deg h_{\rm key}^v<D-1.
\]
The component of \(G_v\) on the divisible exponents is \(Z_{\mathcal K}h_v^0\), where \(h_v^0\) is the divisible-exponent part of \(h_{\rm key}^v\); \(R_v\) is allowed and \(Z_{\mathcal K}\) belongs to \(\mathbb F_q[X^\nu]\). Exact monic division in the variable \(X^\nu\) gives \(h_v^0\). Let \(T_v=G_v-Z_{\mathcal K}h_v^0\), the non-sparse correction with degree below \(U_*\) and no divisible monomials. One can compute both from \(G_v\) by splitting its coefficient list into the residues, dividing the sparse list and keeping the complementary list. Polynomial products and monic division use \(O(D\log D)\) field operations: after reversal the monic divisor has constant term one, and the update \(u\leftarrow u(2-fu)\) doubles the correct inverse precision because its new residual is \((1-fu)^2\). Multiplication uses boundedly many power-of-two subgroup convolutions at each precision by splitting lengths \(O(D)\) into blocks of at most half the available order. The sum over doubling precisions is \(O(D\log D)\). The compressed division has lengths \(O(D/\nu)\), and evaluating the witness sums of polynomials at the subgroup uses the same allowed point arrays. Thus no separate remainder interpolation is needed.

Compute the correction polynomials in the public scaled variable \(Y=X/c_{\rm q}\), as detailed below. Put \(\bar h_v(Y)=h_v^0(c_{\rm q}Y)\) and \(\bar T_v(Y)=T_v(c_{\rm q}Y)\). Evaluate the sparse G1 operands
\[
 H^0=\sum_{a\in I_0}[Y^a]\bar h_v\,P_a^0,\qquad
 H_{\rm oth}^0=\sum_{a\in I_0}c_{\rm q}[Y^a]\bar h_v\,P_{a+1}^0-\rho H^0+d_v P_0^0/Z(\rho).
\]
The second uses at most \(S_0+2\) points including its two fixed operands. Form
\[
 H_j^1=\sum_{\substack{a\in I_1\\ j\Delta+a<U_*}}[Y^{j\Delta+a}]\bar T_v\,P_a^1 .
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

### Scalar preparation and finite decryption work

Use the subgroup placement of the protected efficiency statement for the scored instance. Write \(M=2^{22}\), \(L=2M\), and choose a public \(c_{\rm q}\) of order \(2L\). The shifted domain \(c_{\rm q}\mathcal H_L\) is disjoint from \(\mathcal H_M\). All decryption coefficient arrays below are in the variable \(Y=X/c_{\rm q}\). In all other cases where this efficient placement is not used, the algebraic identities still give the same correction polynomials by ordinary interpolation, multiplication and monic division. At the protected placement the public field scalars and convolution tables below are fixed by the system and its evaluation points. Preparing them is part of the fixed description of the QAP, independent of any witness and encryption. In particular, no additional group element or ciphertext field encoding is needed.

Put \(A_\circ=A_{(w,0,0)}\) and \(B_\circ=B_{(w,0,0)}\). They are the baseline witness polynomials. For either \(F=A_\circ,B_\circ\) the partial fraction expression is
\[
 \frac{F(X)}{Z_*(X)}=\sum_{p\in\mathcal P}
        \frac{F(p)}{Z_*'(p)(X-p)}.
\]
Multiplying by \(Z_*\) verifies the equality at every QAP point and both polynomial sides have degree below \(D\). Since \(p^M=1\), this rational sum has denominator \(X^M-1\) and numerator
\[
 C_F(X)=\sum_{j=0}^{M-1}X^j\sum_{p\in\mathcal P}
             \frac{F(p)p^{-1-j}}{Z_*'(p)}.
\]
For each \(F\), compute one length-\(M\) transform on the weights \(F(p)/(pZ_*'(p))\), with zeros outside \(\mathcal P\). The weights are sums of public weighted QAP entries selected by the bits of \(w\), so computing them takes additions. The public tables store the original QAP entries in this invertible weighted representation. Encryption's interpolation coefficients recover the original value by multiplying each public entry by the corresponding evaluation multiplier including \(pZ_*'(p)\), with one multiplication per weighted entry as in the protected cost convention. To get \(C_F\) on the two cosets of \(\mathcal H_M\) that partition \(c_{\rm q}\mathcal H_L\), multiply the input coefficients by the appropriate powers of the coset offset and use one length-\(M\) transform for each coset. Both \(C_F\) arrays therefore use six transforms and at most \(4M\) coefficient scalings.

At the \(L\) shifted points, \(G_\circ=A_\circ B_\circ/Z_0\) is obtained by multiplying the two evaluated numerators and a fixed factor. Also evaluate
\[
 Q_A=\frac{Z_{\mathcal K} A_\circ}{c_{\rm q} Z_*'(\rho)},\qquad
 Q_B=\frac{Z_{\mathcal K} B_\circ}{c_{\rm q} Z_*'(\rho)}
\]
by multiplying each numerator by a fixed factor. The denominators \(X^M-1\) and \(Z_0\) used to define these factors are nonzero at every shifted point. All three polynomials have degree below \(L\). One length-\(L\) inverse transform per array recovers the coefficients of \(G_\circ(c_{\rm q}Y),Q_A(c_{\rm q}Y),Q_B(c_{\rm q}Y)\). Include the inverse-transform scale \(L^{-1}\) in the fixed pointwise factors, so the combined pointwise work is at most \(4L\) multiplications.

For a tag vector \(t\), let \(A_t^\dagger=\sum_i t_i A_{\mathsf b_i}\) and \(B_t^\dagger=\sum_i t_i B_{\mathsf b_i}\) be its public tag parts. Let \([F]_+\) mean the polynomial part of a rational function, so that \(F-[F]_+\) tends to zero at infinity. Store the four fixed polynomials
\[
 K_t(Y)=\left[
       Z_{\mathcal K}(X)(A_t^\dagger(X) B_t^\dagger(X)-d_tL_\rho(X))/Z_*(X)
       \right]_+\Big|_{X=c_{\rm q}Y}
\]
as public coefficient tables of length at most \(U_*\). They can be prepared by fixed polynomial products and division in \(O(D\log D)\) field operations. They depend only on the public evaluation points and tag table. At an internal Booleanity point \(d_{\mathsf b_i}\), the normalized tag entries from D give both \(A_{\mathsf b_i}\) and \(B_{\mathsf b_i}\) the partial fraction term \(1/(Z_*'(\rho)(X-d_{\mathsf b_i}))\) after division by \(Z_*\), while at \(\rho\) only \(A_{\mathsf b_1}\) and \(B_{\mathsf b_2}\) respectively have the term \(1/(Z_*'(\rho)(X-\rho))\). Therefore the following identity holds:
\[
 G_v(c_{\rm q}Y)=G_\circ(c_{\rm q}Y)+K_t(Y)
      +\sum_{i:t_i=1}\left[
            \frac{Q_A(c_{\rm q}Y)+Q_B(c_{\rm q}Y)}{Y-d_{\mathsf b_i}/c_{\rm q}}\right]_+
      +t_1\left[\frac{Q_B(c_{\rm q}Y)}{Y-\rho/c_{\rm q}}\right]_+
      +t_2\left[\frac{Q_A(c_{\rm q}Y)}{Y-\rho/c_{\rm q}}\right]_+ .
\]
Indeed \(G_v-G_\circ=Z_{\mathcal K}(A_\circ B_t^\dagger+A_t^\dagger B_\circ+A_t^\dagger B_t^\dagger-d_tL_\rho)/Z_*\) is a polynomial by D. Taking polynomial parts on its right-hand side is linear and gives the displayed formula. Synthetic division by a linear polynomial \(Y-a\) takes at most one multiplication by \(a\) per input coefficient. All variants use only tags 1 and 2, so the complete algorithm takes at most four such divisions with quotient length at most \(U_*\). The zero-target-base case needs only the target. The no-triple fallback uses none of these divisions.

For each required \(G_v\), its multiple-of-\(\nu\) coefficient list is a convolution of the public \(Z_{\mathcal K}(c_{\rm q}Y)\) in \(Y^\nu\) and its sparse quotient. Compute the quotient by reversing coefficients and multiplying by the fixed inverse series. The shift need not preserve monicity, but the reversed divisor has a nonzero constant coefficient. Start its inverse at the inverse of that constant and truncate the reciprocal to \(S_0\), as in the monic division identity above. The input prefix and that inverse each have at most \(S_0=1884\) coefficients, so this uses at most three transforms of length 4096 and two coefficient scalings of that length per variant. The other coefficients are directly those of \(T_v(c_{\rm q}Y)\). Preparing the sparse shifted operands takes at most \(4S_0\) scalar multiplications by \(c_{\rm q}\) in total. Thus the rounding, sparse division and shifting overhead on top of the large transforms is below one million multiplications.

A radix-two transform of length \(B=2^b\) needs at most \(Bb/2-(B-1)\) nontrivial twiddle multiplications. Each butterfly stage has one unit twiddle per block, and the total number of blocks over the stages is \(B-1\). The inverse variant uses the same count before final scaling. With \(D=3856913\), \(U_*=7322128\), the displayed large QAP array ledger is \(6(M\log_2M/2-M+1)+4M+4L+3(L\log_2L/2-L+1)+4U_*<596000000\). Adding the small sparse division costs at most another million in expectation.

In the finite scalar branch, multiply the seed matrix by the baseline packed witness by summing the columns selected by its Boolean coordinates, including the homogeneous column. This uses field additions since each witness multiplier is zero or one. Add the corresponding tag columns for the other three variants. This is still precisely the same form map. Hence the protected separate charge \(m\) covers the field multiplications of forming those products. No ring convolution or coefficient-basis transform is used at the scored shape.

In all four variants, the three conjugates of a field value require at most \(3s_0 n\) multiplications per variant using the precomputed Frobenius tables. Two convolutions of length 16384 with three transforms and two scalings each give \(U,V\) before reduction. Monic reduction by the seed polynomial in \(T^{r_H}\) costs at most \(s_0 n\) multiplications each, because each cancellation of a leading coefficient uses at most \(s_0\) lower terms and at most \(n\) leading positions require elimination. With \(s_0\le2\) and \(n\le4104\), the four weight calculations use under five million multiplications.

In each of at most four full mask combinations, form the six weighted leg polynomials, one each for ordinary \(U,V\), jointly conjugated \(U\), left-conjugated \(U,V\) and right-conjugated \(U\). Precompute the monomial pair products from C6 as public field data. Since each input representative has at most \(s_0\) terms on a single residue class modulo \(r_H\), a pair of them has at most \(2s_0-1\) terms before monic reduction. The combined expansion cost is at most \((3n/2)(4s_0)\) multiplications. There are twelve pointwise products for the eight mask polynomials of C7. The three grade-zero combinations use six products, the three positive ones use four and the two negative ones use two. All fit length 16384 and use nine forward transforms for the six input weight polynomials and three conjugate forms, followed by eight inverse transforms for their outputs. Include eight output scalings. Sparse monic division of the first three outputs needs at most \(6ns_0\) further multiplications, since each degree is below \(3n\). This bounds the work of the four full mask combinations by eleven million multiplications.

The large QAP transforms and synthetic divisions cost less than 596 million multiplications. The sparse quotient divisions and scalings cost less than one million, and the conjugates, weights and all four mask polynomials use at most five and eleven million respectively as counted above. The remaining scalar operations are the key-weight inverse in the ordinary or direct-normalization path, or the denominator and inverse on the key-only fallback. At most two field multiplications form the latter denominator, and either inverse takes at most 508 field multiplications by binary powering. All scalar centers and search indices use integer arithmetic. The already formed weights and two fixed QAP constants \(c_{\rm q},Z(\rho)^{-1}\) supply the MSM coefficients, with the \(4S_0\) non-key shifts included above and additions or subtractions free in the multiplication count. The tag key-corner bit is the Boolean product of its two tags. Evaluations that occur during group operations are charged in their respective group counts. Oracle calls, checks and the final xor do not perform field multiplications. Thus the total scalar decryption work besides \(m\) is below 614 million and fits the protected \(632000000+m\) allowance. The finite algorithm of D uses this prescribed subgroup placement. The ledger therefore covers every admitted scored parameter set, with no change to the mathematical identities for any admissible point choice. The unscored growing family uses the asymptotic bounds stated in C7.

### Tag choice and key recovery

For any external witness \(w\), let \(a=(w,1,0)\), \(b=(w,0,1)\), \(c=(w,0,0)\), and \(v_*=(w,1,1)\), each with homogeneous coordinate one. Then \(a+b-c=v_*\) over the integers and \(d_a=d_b=d_c=0,\ d_{v_*}=1\). Define the key weight of \(w\) to be the key-cell weight of \(v_*\). If it is zero, return \(\bot\). If \(\Psi_{v_*}=0\), compute the full combination \(\Lambda_{v_*}\), normalize by this nonzero weight, and recover the key. Otherwise obtain \(\Psi_a,\Psi_b,\Psi_c\). If any of these three bases is zero, use the exact fallback below. In all other cases compute \(\Lambda\) for \(a,b,c,v_*\), reusing the first-coordinate operands.

First solve the centered search for \(r(c)\) using \(\Lambda_c=r(c)\Psi_c\) in additive group notation. Next use \(\Lambda_a-r(c)\Psi_a\) and \(\Lambda_b-r(c)\Psi_b\) to recover \(r(a)-r(c)\) and \(r(b)-r(c)\), each a single tag-coordinate draw. These searches use their known public centers. Adding the two increments to \(r(c)\) gives \(r(v_*)\). Subtract \(r(v_*)\Psi_{v_*}\) from \(\Lambda_{v_*}\) and normalize by the key weight to get \([\kappa]_T\). One key-oracle call unmasks the message. At most four \(\Psi\) values and four full \(\Lambda\) values are needed. The choice of branch depends on no search coordinate.

### Exact fallback when a zero-corner base vanishes

This fallback runs only after the nonzero key-weight test has passed and the target base is nonzero, with at least one zero-corner base equal to zero. The sparse G1 list contains \(P_0^0\) and \(P_1^0\) because \(0\in I_0\) and \(1\in I_0^*\). Pair each one with the published key-cell operand \(B^0_{\rm key}\). The results are
\[
 E_0=[\gamma_{\rm key} Z_*(\tau)]_T,\qquad
 E_1=[\gamma_{\rm key} Z_*(\tau)\tau/c_{\rm q}]_T ,
\]
where \(c_{\rm q}=1\) for unscaled powers. The exponent of \(E_0\) is nonzero because the key scale is nonzero and \(\tau\) is outside the QAP points. The public polynomials satisfy \(Z_*=(X-\rho)Z\) and \(L_\rho=Z/Z(\rho)\). The fallback initializes \(Q=0_T\) and scans \(j=0,\ldots,q-1\). If \(Q=E_1\), return the group element
\[
 \frac{1}{(c_{\rm q}j-\rho)Z(\rho)}E_0
\]
and use its key oracle value to recover the message. Otherwise update \(Q\) by adding \(E_0\). There is exactly one match since \(E_0\) generates the prime-order target group. At that match \(c_{\rm q}j=\tau\) in the field, so the denominator is nonzero and the returned element is \([\kappa]_T\). This also works for \(E_1=0\). The displayed key formula is evaluated only at the match. The scan outputs the key element directly. Its loop index is internal to key recovery and never enters the bounded witness search.

The fallback uses two pairings of operands already present in the ciphertext. It publishes no new value. In the generic security experiment these pairings remain ordinary formal expressions of the same exponents analyzed in C7. The scalar search and its arithmetic are a decryption procedure, outside the stipulated adversary call bound when run exhaustively. The proof of extraction continues to treat every adversarial sequence of calls within that bound.

The bounded witness-search output is \(r(v_*)-c_{v_*}\) when using the three ordinary searches, and zero whenever those searches are bypassed, including the fallback. The branch is selected independently of the search vector. Its output therefore has RMS at most \(R_0\) by Amendment Bsearch. Each of the three ordinary intermediate searches also has RMS at most \(R_0\): the anchor obeys the same bound and the two single-coordinate increments have standard deviation at most \(g/\sqrt{12}\) plus the rounding allowance. The amended spread includes \(R_0\). The group scan contributes only its expected finite group steps to the decryption cost.

### View of the correction polynomials

Only the sparse quotient bases have inverse scale \(\zeta_0^{-1}\), and only the combined correction bases have inverse scale \(\zeta_1^{-1}\). The key-scalar degree class in C7 therefore collects them in each cell as \(Z_c h_c^0+Z_0 T_c\), with every exponent of \(T_c\) in a nonzero residue class modulo \(\nu\). Monic division of \(T_c\) by \(Z_{\mathcal K}\) preserves those classes in every subtraction step. Its remainder \(R_c\) has degree below \(\nu n_{\mathsf c}\) and is allowed. Multiplying the multiple part by \(Z_0\) gives a multiple of \(Z_*\), hence of \(Z_c\), and it is absorbed into \(h_c\). Thus the arbitrary correction is precisely of the required \(Z_c h_c+Z_0R_c\) form. The constant-term comparison in C7 bounds the quotient degree by the QAP criterion, and the changed corner is \(W_{t_1,t_2}\) from that criterion. Every other Laurent comparison uses the same input types and the same actual field ties, as proved in C7, with the two-sector copies omitted.

## Amendment n2

The exact half-count is
\[
 n_2=\left\lceil\frac{6K_2(N+3)+3K_2+(3n/2)(J+1)+C_{\rm mask}}2\right\rceil .
\]
The first two terms count the single right factor arrays and search bases. There is one sparse list of \(A_c\) bases and \(J\) combined lists of \(A_c\) bases, and the cancellation count is \(C_{\rm mask}\). The optional generator padding gives \(2n_2\) actual slots. The G1 count is proved in n1. Together with the fixed one GT element, seed and masked message, these give exactly the protected size formula and the one-generator-multiplication count from the published scalars.

## Amendment dec_sum_g1

Compute the witness sums of the two coordinates for each left leg and the Y column on the external \(w\) once with the tag coordinates omitted. In the reference witness-weight convention each uses at most \((N+1)/2\) additions. Each of the at most four tag variants adds at most two tag entries per array. This gives \((2K_1+1)((N+1)/2+8)\). Reuse these sums for both kinds of combination.

## Amendment dec_sum_g2

For the single right factor sector, compute each of the \(6K_2\) external witness coordinate sums once, using at most \((N+1)/2\) additions each. Only the at most four full combinations need these sums with tags added; each adds at most two entries. Thus the count is \(6K_2((N+1)/2+8)\). The fixed search bases require no analogous coordinate sums.

## Amendment dec_msm_g1

The at most four first-coordinate weighted left operands and four second-coordinate ones each use a total of \(A_c\) points across the legs. In a full combination the sparse key and non-key MSMs use \(2S_0+2\) points. The combined correction uses \(U_*-(S_0+n_{\mathsf c})\) points below \(U_*\), since there are \(S_0+n_{\mathsf c}\) multiples of \(\nu\) there. Hence the total is at most
\[
 8(3n/2)+4\bigl(D-1+S_0+2+(\nu-1)n_{\mathsf c}\bigr).
\]
All operands appear in n1. They do not require computation of a separate remainder MSM.

## Amendment dec_msm_g2

Each full combination uses \(A_c\) points for the two sparse right operands together, \(J A_c\) for the combined right list, and \(C_{\rm mask}\) for cancellation. The at most four full combinations therefore use \(4((3n/2)(J+1)+C_{\rm mask})\) points. The \(\Psi\) combinations use the fixed right search bases without new G2 MSMs.

## Amendment dec_pairings

Each of the at most four \(\Psi\) sums uses \(3K_2\) pairings. Each of at most four \(\Lambda\) sums uses \(6K_2\) factor pairs, \(J\) combined correction pairs, two sparse pairs and one cancellation pair. Thus the total is at most \(12K_2+4(6K_2+J+3)\). Accumulate each signed sum starting with its first term, updating by the indicated group addition or subtraction. This needs at most one fewer accumulation operation per nonempty sum than its pairing count. The remaining bounded number of GT translations, final normalizations and searches are accounted for in search_spread.
The exceptional fallback follows the search-base computations and performs two additional pairings with the already transmitted sparse bases. It uses no full combination. Its pairing count is at most \(12K_2+2\), within the same bound.

## Amendment search_spread

Let \(R_0=g\sqrt{(N+6)/48}+3/2\), and define
\[
 M_0=\begin{cases}
 (7979/10000)\,g\sqrt{(N+6)/48}+3/2 & 359994\le N\le479994,\quad g\ge10^{12},\\
 (803/1000)\,g\sqrt{(N+6)/48}+3/2 & \text{otherwise when }N\ge359994,\\
 R_0 & N<359994 ,
 \end{cases}
 \qquad M_1=g/4+1/2 .
\]
The amended spread is
\[
 \max\left\{ R_0,\,
   \left(\frac{20}{37}\big(2\sqrt{M_0}+4\sqrt{M_1}+4010\big)\right)^2\right\}.
\]
At the scored \(g\ge10^{12}\), the checker selects the first case for its fixed external \(N\). The expression also retains the RMS bound \(R_0\). Here \(M_0\) bounds the expected absolute centered anchor, \(M_1\) bounds the centered single-coordinate difference. The triple selection, failure tests and early return are independent of the search vector, so the bounds apply after conditioning on which of these cases is used.

### Expected absolute anchor

Before the rounding error of at most \(3/2\) in Bsearch, the center removes the mean, leaving the sum of independent symmetric variables
\[
 S=X_\diamond+\sum_{i=1}^{N+2}(v_i-1/2)X_i ,
 \qquad X_i=r_i-(g+3)/2 .
\]
Its standard deviation is \(\sigma_S=\sqrt{(g^2-1)(N+6)/48}>0\). Let \(Y_i\) be its summands divided by \(\sigma_S\), using one more index for the independent diamond term. Set \(v_i'=\mathbb E Y_i^2\) and \(v_{\max}=\max_i v_i'\). The ordinary summands have \(v_i'=1/(N+6)\), the diamond summand has \(v_i'=4/(N+6)\), and \(\sum_i v_i'=1\). Each \(|Y_i|^2\le3v_i'\) because the square of the largest deviation of an integer uniform sample of width \(g\) is \((g-1)^2/4\) before scaling, and the variance is \((g^2-1)/12\). It follows that \(\mathbb E Y_i^4\le3(v_i')^2\).

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

For the scored range \(359994\le N\le479994\) and \(g\ge10^{12}\), the cosine bound can be continued beyond frequency 300. Each of the \(N+2\) ordinary summands has spacing \(1/(2\sigma_S)\) after normalization, up to sign, with distribution symmetric about zero. The finite geometric sum yields its characteristic function
\[
 \frac{\sin(gu)}{g\sin u},\qquad u=\frac{t}{4\sigma_S}.
\]
Here \(\sigma_S/g\le100\) by \(N+6\le480000\). Also \(\sigma_S\ge g\) since \(g\ge2\) and \(N+6\ge360000\). Thus \(300\le t\le10^6\) gives \(gu\ge3/4\) and \(0<u<1/100\). The function \(\sin v/v\) decreases from 1 on \([0,\pi]\): the derivative numerator \(v\cos v-\sin v\) is zero at zero and has derivative \(-v\sin v\le0\) there. For \(v\ge\pi\), its absolute value is at most \(1/\pi\). Taylor's bound on \(\sin(3/4)/(3/4)\) and the lower bound \(\sin u\ge u-u^3/6\) therefore give
\[
 \left|\frac{\sin(gu)}{g\sin u}\right|
 \le \frac{1-(3/4)^2/6+(3/4)^4/120}{1-(1/100)^2/6}<\frac{91}{100}.
\]
Both Taylor bounds follow from the alternating power series on the given fixed intervals. Since \((91/100)^8<1/2\) and \(N+2\ge320\), the product of the ordinary factors is bounded in absolute value by \(2^{-40}\) on this frequency interval. The diamond factor has absolute value at most one and the normal factor is also at most \(2^{-40}\) for \(t\ge300\). Thus the middle integral contributes less than \(2^{-40}\) after its \(2/\pi\) normalization. The tail above \(10^6\) contributes at most \(4/(\pi10^6)\).

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

A centered single box sample has absolute mean at most \(g/4\). For \(g=2m\), the sum of the \(2m\) distances from the midpoint is \(2\sum_{i=1}^m(i-1/2)=m^2\). For \(g=2m+1\), the sum is \(2\sum_{i=1}^m i=m(m+1)\), giving absolute mean \((g^2-1)/(4g)\). Rounding a public center adds at most \(1/2\). Both increments in the only triple are single box samples, so each uses \(M_1\). All ordinary search integers remain within the protected \(B\).

The fallback probability is at most \(9/q\), by Targets. Its exhaustive loop uses at most \(q\) GT additions, plus at most 520 steps for the final scalar multiplication and constant setup. Including that setup, it contributes at most \(9+4680/q<10\) expected GT steps because the protected prime exceeds 4680. Its two pairings are included in the pairing bound. Its field operations, including inversion, cost less than one multiplication in expectation at the protected prime and fit in the protected scalar allowance.

The changed pointwise search bound of Proposition 5.7(d) is the fixed-width bound below, and its expectation gives the stated efficiency conclusion for the three searches. For any centered target \(x\) known to have \(|x|\le B\) and \(\mathbb E|x|\le M\), use the sign-class baby and giant search with integer width \(b=\lceil\sqrt M\rceil+1\). Tabulate \(iP\) for \(0\le i<b\), where \(P\ne0\) is the base. The signed intervals centered at \(j(2b-1)\) with radius \(b-1\) partition the integers. Progress outward in the order \(j=0,1,-1,2,-2,\ldots\), testing the sign class of the corresponding residual against the table. Verify the sign and the resulting integer against the bound; \(2B+1<q\) makes the bounded solution unique. A match for the true integer occurs by \(|j|\le |x|/(2b-1)+1\). The baby construction has at most \(b\) counted steps. Its stride follows from the last baby point by a doubling and one addition. Maintain separate accumulators for positive and negative giant indices, so alternating the direction advances one accumulator with one update. Including a constant for initialization and verification, the total is at most \(b+2|x|/(2b-1)+12\) steps on a true target. This bound includes names and the constant work to derive their signs according to the protected step convention. A run with no valid solution can stop upon exploring all intervals intersecting \([-B,B]\). Since \(2b-1\ge2\sqrt M\), its expected bound on a valid sampled target is at most \(2\sqrt M+14\). A nonzero base is always used for these searches.

The anchor uses \(M=M_0\). Each difference uses the width from \(M_1\). For the anchor subtract its public center times its base. For each relative search subtract the sum of the known anchor and the rounded difference center times the relative base. Each translation uses one GT scalar multiple. Afterward remove the target search term and normalize by the key weight with at most two more GT scalar multiples. Binary multiplication by a scalar modulo the protected \(q<2^{254}\) takes at most 508 additions or doublings. The five multiples, elementary translations and sign handling, and three additive overheads of 14 each fit within 4000 extra steps. The zero-target-base case only uses the normalization and fits the same bound. Combining the ordinary search and fallback bounds gives at most \(2\sqrt{M_0}+4\sqrt{M_1}+4010\) expected steps. Thus \((37/20)\sqrt{\mathrm{search\_spread}}\) covers the total charged step bound at the protected price of six multiplications per step. The ordinary searches have the same bounded-answer correctness. The no-triple fallback uses existing operands, so generic extraction probabilities are unchanged. In the asymptotic family the scalar-multiplication overhead is \(O(\log q)\) and the main expected cost is \(O(\sqrt g\,N^{1/4})\).

## Amendment n

Use \(n=kd_R+1\) in both allowed ring modes. Put \(v_0\) in slot zero and then put the \(d_R\) coefficient forms from each matrix row into successive power-basis slots, using every ring row once in row-major order. In the scalar mode those are exactly the \(k\) scalar forms of the dense uniform matrix. In the split mode \(k=1\) and these are the \(d_R\) power-basis coefficients. In both modes the kernel identity is \((v_0,A\hat v)=(0,0)\), and the dimension of the actual Module-SIS instance is \(kd_R\) by \(\ell d_R\) with its infinity norm in this coefficient basis. The scalar tables and field degree used by the three ties, exponent ledger and gradients are those of the actual field \(n\), with no padded field slots. The claimed oracle and arithmetic costs use these same dimensions.

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

With at most four row directions, the unit axes account for three of them; any other rows on those axes give weaker strips by the entry bound. The possible fourth direction supplies a strongest normal \(a\) with \(|a_i|\le1\). Thus \(K\) contains the portion of \([-1,1]^3\) with \(|a\cdot x|\le1\). This portion is minimized when the three \(|a_i|\) equal one. For independent uniform \(X_i\) on \([-1,1]\), the sum of the other terms has an even density nonincreasing on nonnegative inputs, or the point mass at zero. For two nonzero terms the density is a constant times the overlap length of two centered intervals as their centers separate; a single nonzero term gives an even uniform density. Its probability to lie in an interval of length two centered at \(u\) is again even and nonincreasing in \(|u|\), by the same centered-interval comparison or direct integration. The point-mass case has the same property. Conditioning on \(X_i\) proves monotonicity in \(|a_i|\). At three unit coefficients the cube loses two opposite tetrahedra of intercept lengths two and volume \(8/6\) each. The remaining volume is \(16/3\).

In the remaining plane-and-line configuration, the plane must contain two unit axes and the line the third, because their union covers all three independent unit directions. After permuting coordinates, the plane is that of \(e_1,e_2\) and the line that of \(e_3\). Determinants of pairs of in-plane normals are bounded in absolute value by one using \(e_3\) as the third row, and the in-plane rows include \(e_1,e_2\). Its planar strip region therefore has area at least three by I6. The line normals are multiples of \(e_3\) with absolute coefficients at most one and include \(e_3\), so their interval has length two. The full region factors as the planar region times this interval, with volume at least six. Together with the four-direction case this gives a lower bound of \(16/3\).

The line of the selected nonzero kernel vector has preimage of index \(q^2\) in the lattice of integral coefficient vectors of \(B\). The image under \(B_J\) has determinant \(hq^2\). The body \(b_{\rm s}K\) has volume at least \((16/3)b_{\rm s}^3\ge 8 hq^2\) by the passing-stack conditions in I6. The I6 lattice-volume implication gives a nonzero point, lifting exactly as in I6 to a short multiple of that vector. It is nonzero modulo \(q\) because it is nonzero over the integers and has norm below \(q/2\).

### Reduction interface

In mode one, given the recovered row space, use the described active-coordinate choice if its kernel has dimension at least two and its zeroth coordinate vanishes throughout. In all other cases select any nonzero kernel vector when one exists. Use the protected LIFT at \(\beta_{\rm use}\). The lift existence is needed only for a good heavy passing stack, which is the stack supplied by the generic view and mark definition. On other tried expressions, any output remains a short multiple of a tested kernel vector, so packing gives a sound solution. The selection uses \(O(N_\star)\) additional field operations after the kernel computation and no extra oracle calls. It happens after recovery and therefore leaves the private detection and span-recovery probability bounds unchanged. The LIFT running time follows from the passing-stack conditions in I6 and P4. The targets use this actual challenge radius and the original generic, extraction and correctness bounds, including the same reduction-time asymptotic. The general inverse claim and heavy-stack implication at radius \(\beta\) retain their original scopes.

## Targets

Fix any parameter set satisfying the amended model, the protected system shape, any admissible evaluation points, and the stated group and oracle models. In the chosen modes use the coefficient positions of Amendment n, the base field of Amendment C6 and the grid and masks of Amendment C7, and the single-sector QAP encryption and decryption of Amendment n1. The amended inverse theorem applies by (P3) with Amendments I3, I4, H2, H3 and I6. The charged-mark bound is proved in Amendment Ncmp. Correctness and extraction use the same external witness relation, oracle model, budgets and probability bounds. Internally the projected witness forgets its Boolean tags.

### Correctness with error \(2/q\)

Fix an external witness \(w\), the statement, message and admissible evaluation points. Every tag extension used in n1 is an internal witness. The group identities in that amendment show that a nonzero key weight together with a zero target base gives immediate decryption. If the target base is nonzero and all three zero-corner bases are nonzero, the three searches give the unique integers used to recover the key. Otherwise the fallback of n1 recovers the exact key on every valid coin realization after the weight check. Thus decryption fails exactly when \(\xi_{\rm key}(v_*)=0\), the distinguished key weight for the external witness. This gives the failure characterization of Theorem 5.6. We bound that failure and the separate fallback event.

First consider the target key weight. Let \(L:F\to\mathbb F_q\) be the constant-slot coefficient functional in the form basis, nonzero because \(L(1)=1\), and let \(s=n/2-1\). Then the weight of a form value \(x\) is \(Q(x)=L(x\sigma^s(x))\), with \(x\) uniform on the affine hyperplane \(L(x)=1\). The trace map is nonzero: the polynomial \(\sum_{j=0}^{n-1}X^{q^j}\) has degree \(q^{n-1}<q^n\) and cannot vanish at all \(q^n\) field elements. The pairing \((a,b)\mapsto\operatorname{Tr}(ab)\) is therefore nondegenerate, since multiplication by a nonzero \(a\) is invertible. Thus \(L(x)=\operatorname{Tr}(\lambda x)\) for a unique nonzero \(\lambda\), by equality of the dimensions of the field and its scalar dual.

The polar form \(Q(x+y)-Q(x)-Q(y)\) is
\[
 \operatorname{Tr}\!\left((\sigma^{-s}(\lambda x)+\lambda\sigma^s(x))\,y\right).
\]
Trace invariance under Frobenius gives this expression. By nondegeneracy, the radical solves \(\lambda x+\sigma^s(\lambda)\sigma^{2s}(x)=0\). If there is one nonzero solution \(x_0\), every other solution is \(x_0\) times an element fixed by \(\sigma^{2s}\), by dividing the two equations. Since \(\gcd(2s,n)=2\), such a ratio is fixed by \(\sigma^2\): use the integer Bezout identity for \(2s,n\) and \(\sigma^n=1\). There are at most \(q^2\) of these ratios because they are roots of \(X^{q^2}-X\). Hence the radical dimension is at most two and the polar rank at least \(n-2\). Restricting each argument to the hyperplane \(\ker L\) loses at most one rank per restriction, so the affine quadratic on \(L(x)=1\) has quadratic rank at least \(n-4\).

For an affine quadratic of rank \(d\) over the fixed odd prime field, the proportion of zeros is at most \(1/q+q^{-d/2}\). Indeed, use the character sum \(q^{-1}\sum_{a\in\mathbb F_q}\exp(2\pi i a Q/q)\) for its zero indicator. A linear change of variables diagonalizes the quadratic part in odd characteristic, by choosing a vector with a nonzero square coefficient, completing its square to isolate it, and iterating. With \(a\ne0\) a one-variable sum for a nonzero square coefficient has magnitude \(\sqrt q\), even with a linear term: by completing the square the linear term is a unit-magnitude factor, and the squared magnitude of \(\sum_x\exp(2\pi i c x^2/q)\) is the sum over \(x,y\) of \(\exp(2\pi i c(x-y)(x+y)/q)\). The map to \(x-y,x+y\) is invertible, and summing first over one new coordinate gives \(q\), since only the other coordinate zero has a nonzero inner sum. Every other coordinate has character sum bounded by \(q\). After normalization the contribution of all nonzero \(a\) to the zero probability is at most \(q^{-d/2}\), and the zero character contributes \(1/q\). Here \(n\ge10\) gives \(d\ge6\), so the key weight vanishes with probability at most \(1/q+1/q^3\), and in particular at most \(1/q+1/q^2\).

For the fallback probability, condition on all scalar coins except \(y\) and the seed matrix. On the constant-slot-one hyperplane put \(S(z)=\sum_c\gamma_c\xi_c(z)\). It is a polynomial of total degree at most two in the other coordinates because the two products defining the weights are quadratic and Frobenius is scalar-linear. If \(S\) is identically zero, \(\Psi_{v_*}=0\) and no fallback occurs. Otherwise each of \(a,b,c\) has an independent-of-\(y\), uniform form value on that hyperplane by ell. The root bound gives probability at most \(2/q\) that its \(S\) value vanishes. Its \(y\) value is uniform, since its homogeneous coordinate is one and the samples of \(y\) are uniform. Its search base vanishes only if one of these two scalar factors is zero, with probability at most \(3/q\). A union bound over the three bases, followed by averaging over the conditioned coins, gives fallback probability at most \(9/q\). This event affects work only. The key-weight bound above gives probability of decryption failure at most \(1/q+1/q^2\le2/q\). On every other coin realization the algorithm recovers \([\kappa]_T\) and returns the original message with one key-oracle call.

### Extraction and the reduction

Let \(\mathcal A\) have the budget \(Q<2^\lambda\) of generic group calls and at most \(2^\lambda\) queries to each oracle. Fix one bit \(b\) and messages \(m_0,m_1\), and run the extraction experiment with \(m_b\). The extractor reads the answered generic transcript without any oracle calls. It uses the protected extractor sketches for the plain sector. The empty alpha sector can be represented by zero records. It samples three independent probe vectors for each cell, uses the linear combinations of source-group records and pairings to form sketches, tests the sketches of the result and the difference when there is an old record, and directly checks its ordinary assignment against \(S\), checks the two tag bits, and returns the ordinary witness only. In rank at most three, there are at most four assignments with first coordinate 1 to test: row echelon pivot coordinates determine the vector, pivot 0 must be present, and at most two remaining pivot choices are bits. Output is therefore always \(\bot\) or a witness. A record creation, result, or difference touches \(O(K_1N_\star+n)\) field elements, since a source-group record uses at most \(K_1\) length-\((N_\star+1)\) vectors or \(6A_c\) values, and the pairings compute six such combined sketch vectors. For a pairing, forming the inner products in the G2 record or summing per left leg and combining the G1 vectors uses \(O(K_1N_\star+n)\) operations. A test uses \(O(N_\star)\) for elimination with at most three rows and \(O(N_\star+|S|)\) to generate and check the constant number of candidates. Initialization samples \(6A_c(N_\star+1)\) field values, enters the \(L\) labels as records whose vectors are materialized on first use, and uses \(O(nN+L)\) time. There are at most four tests per result. Thus the extractor uses \(O((Q+1)(nN+|S|)+L)\) time because \(K_1\le n\) and \(N_\star\ge1\).

The reduction on input a uniform \(A\in R_q^{k\times\ell}\) samples the seed, programs the seed oracle at that seed on matrix columns 1 through \(\ell\) using \(A\), and samples the other answers lazily, including the independent column 0. It samples encryption coins as specified, produces the ciphertext for \(m_b\), and simulates all generic labels and names and random oracles by the protected lazy tables. It runs \(\mathcal A\) once. The extraction steps use the answered generic transcript without its output or the random-oracle query transcript, while the lazy tables implement exactly the direct oracle law. Because the programmed entries are jointly independent uniform ring elements for uniform \(A\), all oracle answers including entries at the selected seed have exactly the joint law of the experiment. Private evaluation points are sampled independently of the run.

The reduction keeps records evaluated at its private test point, using the protected rules for guessed operands and for existing records. It tries the first GT result whose label has an existing record of different private value, using the difference expression, and also the target label's record if present. For each tried expression it computes three independent gradient vectors in the plain sector at private recovery points, tests their span for a kernel vector, and applies LIFT with radius \(\beta_{\rm use}\) if there is such a vector, making the selection specified in Amendment msis_bound in mode one. An output from LIFT is a short multiple of that kernel vector. The coefficient of \(T^0\) in \(z(v)\) is \(v_0\). All \(kd_R\) remaining row coefficients give the equations of \(A\) on the packed input once \(v_0=0\). Thus a nonzero kernel vector has \(v_0=0\) and satisfies \(A\hat v=0\). Its short multiple has \(x_0=0\) since \(2\beta<q\). Reduction and packing commute, and packing preserves all ordinary and tag coordinates by Amendment ell and adds only zeros. This packs the output into a nonzero norm-at-most-\(\beta_{\rm use}\) solution to \(A\hat x=0\), exactly for the challenge whose rank, columns, bound, and norm are costed by M1. If no such output is found the reduction returns \(\bot\). Denote its success probability by \(s_b\). The cost is \(t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT}\) with \(Q_H\) the maximum per-oracle query count, \(C_R=O((N_\star+n)D+\mu)\) for the fixed simulation setup and postprocessing, and \(T_{\rm LIFT}\) the time of the lifting step. The reduction-time argument in C7 proves this reduction-time bound on the revised lists, including the original private record and gradient loop costs and the new fixed setup. The inverse conditions and comparison count do not enter those time calculations. LIFT's running-time result applies since \(2\beta_{\rm use}<q\) and \(24\beta_{\rm use}^4<q^3\) by P4 and \(\beta_{\rm use}\le\beta\). In particular the cost is \(t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)\) using \(n,N_\star\le D\).

Here is how the first-mark bounds apply to these algorithms. The degree and view for the new field encoding and the needed gradient formula are derived above. The record invariant uses no inverse premise: setting all guesses to zero commutes with additions and pairings, and before the first mark every reused label comes from formally equal expressions. Formally equal target expressions have identical stacks by the fiber equations applied to their difference for every field search vector. Thus their records also have equal sketches. A good mark's stack is usable with the three field ties of Amendment C7 by the revised view. Its rank is at most three by \(g^{-4}<\mu_{\rm tr}<\theta\) from (I5) and the protected stack rank bound. On the dense choice the stronger guard \(g^{-3}<\mu_{\rm tr}\) gives rank at most two. The full classification applies to every actual tied stack of dimension at most three, including zero-corner marks, because the three ties just derived are the original field identities. A kernel vector in its row space has coordinate 0 equal to zero, and its one-dimensional guessing probability is at least the stack's, by the protected guessing-probability lemma. In mode zero I6 gives a short multiple at radius \(\beta\). In mode one the selection in Amendment msis_bound gives a short multiple at radius \(b_{\rm s}\). Thus LIFT succeeds at the selected challenge radius.

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
