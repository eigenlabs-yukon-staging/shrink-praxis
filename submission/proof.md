# Praxis with linear weights and rank-two heavy extraction

## Amendment I3

The amended (I3) is
\[
\Lambda_1\ge 2\sqrt3 R_{\rm tr}\sqrt N,\qquad
\Lambda_2\ge \sqrt2\,\pi R_{\rm tr}^2 N,\qquad
\Lambda_3\ge \frac{20\,\pi R_{\rm tr}^3 N\sqrt N}{9\sqrt2} .
\]
The rank-two and rank-three geometric lower bounds change. All three inequalities here are checked by the parameter model.

### Which inverse-theorem steps use the change

In `blob:admissibility`, (P3) refers to these inverse conditions, and the bounds in (P1), (P2), (P4) and (P5) have no occurrence of a geometric factor \(\Lambda_d\). The box, saturation, reduction, fiber and height definitions in `blob:lattices` use the same lattice operations. The regularity test uses \(m(\Theta)h(\Theta)\le\Gamma_d/g^d\), and has the same definition. In `blob:trimming` the ellipsoid depends on \(R_{\rm tr}\), \(g\), and the basis through \(\Sigma_\Theta\), with no \(\Lambda_d\). The proof of `lem:prefix` uses only the lattice indices and ceiling count in (a)–(b), and (I1), (I2), (I4) to convert the rank-three ceiling count to the height and regularity in (c). The proof of `lem:trim` applies the exponential moment bound for independent box variables, then the exponential loss inequality in (I2). Amendment I4 supplies the complete prefix, trimming and regularization derivations for the joint conditions. We prove `lem:sparse`, `lem:regularize\), and `lem:inverse` under the amended condition below.

### Projected fiber counts

The claim of `lem:sparse` is as follows. Let \(B\) be a basis of an integral lattice \(\Theta\) on a coordinate set \(I\) with \(|I|\le N\), of rank \(d\in[3]\). Let \(F\ne\varnothing\) be a set of points of the integer box on \(I\cup\{i'\}\), \(i'\notin I\), trimmed by \(\Theta\), and \(\Phi(r)=(B^\top r_I,r_{i'})\). If (a) \(\Phi(F)\) has affine dimension \(d+1\) and lies in a coset of an index-\(q\) subgroup of \(\mathbb{Z}^{d+1}\), then
\(\Pr[F]\le\Lambda_d g^d h(\Theta)m(\Theta)/q\).
If (b) \(F^\perp\) has rank \(d'\) with \(1\le d'<d\), a largest minor on \(J\subseteq I\), and every vector of \(F^\perp\) restricts to a vector in \(\operatorname{span}_{\mathbb R}\Theta\) on \(I\), then
\(\Pr[F]h(F^\perp)\le\Lambda_{d-d'}\,g^{d-d'}h(\Theta)m(\Theta)\).
Here \(F^\perp\) is the lattice of integer vectors normal to the differences in \(F\).

For each possible image \((y,x)\), the probability of \(B^\top r_I=y,r_{i'}=x\) is at most \(m(\Theta)/g\) by independence, so \(\Pr[F]\le|\Phi(F)|m(\Theta)/g\). We count images in \(C=\mathcal{T}_\Theta\times[2,g+1]\).

For (a), put \(s=d+1\), \(\delta=q\), \(J=\varnothing\), and let \(p\) be the identity. Write \(B=(B_1,B_2)\) with \(B_1\) empty, and use \(|\det(B_1)_J|=1\).
For (b), put \(s=d+1-d'\) and let \(Y\) be an integral basis matrix of \(F^\perp\); \(Y_J\) is invertible. The submatrix \(B_J\) has row rank \(d'\) since the columns \(Y_J\) lie in its real column span. The integral kernel of \(B_J\) is saturated in \(\mathbb{Z}^d\), of rank \(d-d'\). It has a basis that extends to an integral basis of \(\mathbb{Z}^d\): the quotient by a saturated subgroup of \(\mathbb{Z}^d\) is finitely generated and torsion-free, hence free, and lifts of a quotient basis give the extension. Using this basis change, write \(B=(B_1,B_2)\) where \((B_2)_J=0\) and \((B_1)_J\) is invertible square. The columns of \(B_2\) number \(s-1\). Trimming is basis independent since the mean and covariance transform by the same invertible change on the image coordinates.

In case (b), the injective map \(a=(a_{[d]},a_{d+1})\mapsto(Ba_{[d]},a_{d+1})\) maps the real annihilator of the differences of \(\Phi(F)\) isomorphically onto the real annihilator of the differences of \(F\), by the restriction assumption. The first annihilator has dimension \(d'\) and its integer points form a saturated lattice with basis matrix \(V\). Split its rows into \(V_1,V_2,V_3\) of lengths \(d',s-1,1\). The image of its basis is \(Y A\) for an integral nonsingular \(d'\)-square matrix \(A\), as its columns are integral independent normals. At rows \(J\), this gives
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

The regularization conclusion using this projected bound is proved under Amendment I4, and the resulting short-vector conclusion is proved under Amendment I6. They use these projected constants and the combined conditions.

## Amendment I4

The amended condition is the conjunction
\[
\begin{gathered}
g\ge 2^{40},\qquad g^3\mu_{\rm tr}\ge4097/4096,\qquad
\Gamma_2\ge \xi_{\rm tr}(2-1/g),\\
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

For \(g\ge2^{40}\), expand the binomial and bound its coefficients by \(255^j\). This gives
\[
 (1+g^{-1/2})^{255}
 \le \sum_{j=0}^{\infty}(255\cdot 2^{-20})^j
 = (1-255\cdot 2^{-20})^{-1}
 < 4097/4096.
\]
The last inequality is equivalent to \(255\cdot4096<2^{20}-255\). This contradicts \(gF\ge g^3 m(\Theta)\ge g^3\mu_{\rm tr}\ge4097/4096\). Thus \(h<g\) and, because the height is integral, \(h\le g-1\).

Combining \(h\le g-1\) with the ceiling expansion yields \(m(\Theta)h(\Theta)\le g^{-2}\xi_{\rm tr}(2-1/g)\le g^{-2}\Gamma_2\). This is rank-two regularity.

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

The admissibility block uses these conditions through (P3). The lattice and trimming definitions and the actual projected count do not use the removed growth conditions. Their estimates are proved above and in Amendment I3. Amendment I6 proves the resulting inverse theorem. For the heavy-stack consequences, the guessing-probability rank bound and \(g^3\theta>g^3\mu>1\) imply that a heavy stack has rank at most two. A kernel vector is zero at coordinate zero and has guessing probability at least that of the stack, so the amended inverse theorem gives its short multiple. The packing and its norm are verified in Targets. These proofs use no rank-three premise.

## Amendment I6

Replace (I6) by the conjunction
\[
 2\beta<q,\quad H_1\le\beta,\quad
 3H_2q\le2\beta^2,\quad 31\lfloor H_3\rfloor q^2\le 10\beta^3.
\]
The definitions of the three heights and conditions (I1)–(I5) retain their specified meanings.

### Dependence on the inverse conditions

Admissibility uses (I6) through (P3), and keeps the bound (P4) that ensures LIFT works. The box, saturation, regularity and trimming definitions do not take the norm parameter. The full proofs of the prefix, trimming, sparse-count and regularization statements under the joint conditions are in Amendments I3 and I4, and their bounds use the lattice height, projected volumes and trimming loss, without using the norm constraint. The altered terminal geometry enters the inverse theorem below.

### An ellipsoid in the coordinate constraints

Let \(d\) be 2 or 3, and let \(a_i\) be finitely many vectors in \(\mathbb{R}^d\) including all standard unit vectors, with every \(d\)-tuple determinant bounded by 1 in absolute value. Define
\[
K=\{x\in\mathbb{R}^d:\ |a_i^\top x|\le 1\text{ for all }i\}.
\]
For \(d=2\) we prove \(\operatorname{vol}_2 K\ge\pi\sqrt3/2\), and for \(d=3\) we prove \(\operatorname{vol}_3 K\ge(4\pi/3)\sqrt{2/5}\).

Maximize \(\det A\) over symmetric positive semidefinite \(A\) with \(a_i^\top A a_i\le1\). The domain is compact because the coordinate constraints bound the diagonal entries and positive semidefiniteness bounds the off-diagonal entries by the corresponding geometric means. A small positive multiple of the identity is feasible, so a maximizer \(A\) is positive definite. Set \(u_i=A^{1/2}a_i\), and call \(i\) active if \(\|u_i\|_2=1\). The identity matrix belongs to the cone generated by \(u_i u_i^\top\) at the active indices. Indeed, this cone is closed because the trace of each generator is 1, so the coefficients of any convergent sequence of nonnegative combinations are bounded and have a convergent subsequence. Otherwise let \(C\) be the cone point nearest to the identity in the trace inner product and put \(S=I-C\). The minimizing property gives \(\langle S,X-C\rangle\le0\) for any \(X\) in the cone. With \(X=0,2C\) it gives \(\langle S,C\rangle=0\), so \(\operatorname{tr}S=\|S\|_{\rm F}^2>0\) and \(u_i^\top S u_i\le0\) for active \(i\). Then \(A^{1/2}(I+tS)A^{1/2}\) is feasible for all sufficiently small \(t>0\), by the active inequalities and the strict slack of the finitely many other inequalities. Its determinant is larger than \(\det A\) because \(\det(I+tS)=1+t\operatorname{tr}S+O(t^2)\). This contradiction proves the cone claim.

Write \(I=\sum_i w_i u_i u_i^\top\) with \(w_i>0\) on a subset of the active indices. We can take at most \(m=d(d+1)/2\) indices. If there are more, the symmetric matrices of the subset are linearly dependent. Any nonzero dependence \(\sum_i c_i u_i u_i^\top=0\) has \(\sum_i c_i=0\) by traces, so has both signs. Replacing \(w_i\) by \(w_i-tc_i\), with \(t=\min_{c_i>0}w_i/c_i\), preserves the sum and nonnegativity and removes at least one index. Repeat until there are at most \(m\). After padding the weights by zeros to length \(m\), \(\sum_iw_i=d\). The determinant identity after expanding by minors gives
\[
1=\sum_{i_1<\cdots<i_d}\left(\prod_{j=1}^d w_{i_j}\right)
             \det(u_{i_1},\ldots,u_{i_d})^2
 \ \le\ \det A\sum_{i_1<\cdots<i_d}\prod_{j=1}^d w_{i_j}.
\]
Here \(|\det(u_{i_1},\ldots,u_{i_d})|\le\sqrt{\det A}\) by the row determinant hypothesis.

Among nonnegative weights summing to \(d\), the elementary symmetric sum on the right is maximized by equal weights. A maximum exists by compactness and is positive, hence has at least \(d\) positive weights. For any two unequal weights, their replacement by two copies of their average keeps their sum and increases their product. Terms of the symmetric sum involving just one of those positions depend only on their sum, and terms involving both have positive coefficient equal to the degree-\((d-2)\) elementary symmetric sum of the other weights. That coefficient is positive since at least \(d-2\) other weights are positive, with the degree-zero sum equal to 1. Thus any unequal pair contradicts maximality. The maximum is \(\binom{m}{d}(d/m)^d\), equal to \(4/3\) for \(d=2,m=3\) and \(5/2\) for \(d=3,m=6\). The determinant is at least \(3/4\) or \(2/5\), respectively. The ellipsoid \(A^{1/2}\{x:\|x\|_2\le1\}\) lies in \(K\) by Cauchy–Schwarz since \(\|A^{1/2}a_i\|_2\le1\). Multiplying the respective Euclidean ball volumes by \(\sqrt{\det A}\) proves the claimed volume bounds.

We also use the following elementary lattice-volume implication. For a full lattice \(L\) in \(\mathbb{R}^d\) and a centrally symmetric compact convex body \(K'\) with \(\operatorname{vol}K'\ge 2^d\det L\), there is a nonzero lattice point in \(K'\). For strict inequality, translate the pieces of \(K'/2\) lying in distinct translates of a half-open fundamental parallelepiped for \(L\) back into that parallelepiped. The sum of their volumes exceeds \(\det L\), so two pieces overlap. The two corresponding distinct points of \(K'/2\) differ by a nonzero lattice vector, lying in \(K'\) by convexity and symmetry. For equality apply the strict argument to \((1+1/j)K'\) for each positive integer \(j\); these sets lie in \(2K'\), which contains only finitely many lattice points. A nonzero point occurring infinitely often lies in the closed body \(K'\).

### Amended inverse theorem

For prime \(q\), with the remaining hypotheses in `lem:inverse` and the (I6) above, every nonzero \(v\in\mathbb{F}_q^{N+1}\) with \(v_0=0\) and \(\operatorname{gp}(v^\top)>\theta\) has an integer short multiple \(x\) with \(x_0=0\), \(0<\|x\|_\infty\le\beta\), and \(x\bmod q=a v\) for some \(a\in\mathbb{F}_q^*\).

Remove zero coordinates and order the nonzero coordinates as \(v_1,\dots,v_{N_0}\). For a prefix of length \(i\), let \(p_i\) be its maximum modular fiber density for independent box coordinates uniform on \([2,g+1]\cap\mathbb{Z}\). Each fiber of the longer prefix, conditional on the last coordinate, is a fiber of the shorter prefix. Hence \(p_i\ge p_{i+1}\). The single-coordinate map is injective on the box since \(v_1\neq0\) and \(g+1<q\), so
\[
\theta<p_{N_0}\le p_i\le p_1=1/g.
\]
Inductively we construct a saturated regular lattice \(\Theta\) on the first \(i\) coordinates with rank \(d\in\{1,2\}\), \(v_{[i]}\in\bar\Theta\), and \(m(\Theta)\ge p_i-3\varepsilon_{\mathrm{tr}}\). This gives \(m(\Theta)>\mu_{\mathrm{tr}}\) and \(h(\Theta)\le H_d\), using regularity. For \(i=1\) use \(\mathbb{Z}\). Its height is 1, density is \(1/g\) and \(\Gamma_1\ge1\) follows from (I4) and \(\mu_{\mathrm{tr}}<1/g\).

For the extension step we first choose a basis \(B\) with product of the column infinity norms at most \(h(\Theta),2h(\Theta)\) in ranks 1 and 2, respectively. Choose a row set \(J\) of a largest minor. Restriction identifies \(\Theta\) with the full lattice \(L_J=B_J\mathbb{Z}^d\) of determinant \(h(\Theta)\). Every lifted basis vector has infinity norm bounded by the \(\ell_1\) norm of its \(J\) coordinates by `lem:lattice-facts` (a).

For successive minima we use the upper bound in Minkowski's second theorem, J. W. S. Cassels, *An Introduction to the Geometry of Numbers*, Chapter VIII, Theorem V, p. 218, [publisher record](https://doi.org/10.1007/978-3-642-62035-5). For a convex symmetric body of volume \(V_F\) and a full lattice \(\Lambda\) of determinant \(d(\Lambda)\), the theorem states for its successive minima \(\lambda_1,\ldots,\lambda_d\) that
\[
  (2^d/d!)\,d(\Lambda)\le \lambda_1\cdots\lambda_d V_F\le 2^d d(\Lambda).
\]
Applying it to the \(\ell_1\) unit ball, a union of \(2^d\) orthant simplices of volume \(1/d!\), gives \(\prod_j\lambda_j\le d!\,h(\Theta)\). Choose independent vectors \(u_1,\ldots,u_d\) with \(\|u_j\|_1\le\lambda_j\). These exist by choosing each \(u_j\) outside the span of the earlier ones from the rank-\(\ge j\) span of points of norm at most \(\lambda_j\). Intersect their first \(j\) real spans with \(L_J\) to get a primitive flag of lattices, of ranks \(j\). The successive quotient is free of rank one since the intersections are saturated. In each quotient choose a generator with sign such that \(u_j\) projects to \(m_j\) times that generator with integer \(m_j\ge1\). If \(m_j=1\), use \(u_j\) as a lift of the generator. Otherwise, any lift is \(u_j/m_j+\sum_{l<j}a_l u_l\) with real \(a_l\). Subtract integer multiples of the \(u_l\) to obtain a lift with \(|a_l|\le1/2\). Its norm is at most \(\lambda_j/2+\sum_{l<j}\lambda_l/2\le j\lambda_j/2\). The rank-one lift has norm at most \(\lambda_1\) in either case. These quotient generators form a basis by induction. Thus the product of the \(\ell_1\) norms is at most \(\lambda_1\cdots\lambda_d\) in the two possible ranks. Lifting back via \(J\) proves the stated product bounds for \(B\).

Let \(v_{[i]}=Bc'\bmod q\), and \(c=(c',v_{i+1})\) over \(\mathbb{F}_q\). Take a densest modular fiber of \(v_{[i+1]}\) and trim it by \(\Theta\), obtaining \(F\) of density at least \(p_{i+1}-\varepsilon_{\mathrm{tr}}\), by `lem:trim`. Write \(\Phi(r)=(B^\top r_{[i]},r_{i+1})\). The points \(\Phi(F)\) lie in one coset of the subgroup \(c^\top y=0\bmod q\) of index \(q\) in \(\mathbb{Z}^{d+1}\), since the last entry of \(c\) is nonzero. If their affine dimension were \(d+1\), `lem:sparse` (a) and regularity would give
\[
\Pr[F]\le \Lambda_d\, g^d h(\Theta)m(\Theta)/q \le \Lambda_d\Gamma_d/q<\mu_{\mathrm{tr}},
\]
using (I5). This contradicts \(\Pr[F]>\theta-\varepsilon_{\mathrm{tr}}\). Let \(k'\le d\) be the actual dimension and \(\Delta_*\) the integer matrix whose columns are differences of points of \(\Phi(F)\) from any fixed point. Its rank is \(k'\).

For a point in the trimming ellipsoid, the absolute deviation in coordinate \(j\) from the center is at most \(R_{\mathrm{tr}}\sqrt{(\Sigma_\Theta)_{jj}}\), by Cauchy–Schwarz after applying \(\Sigma_\Theta^{-1/2}\). Thus the corresponding row of \(\Delta_*\) has entries bounded by \(2R_{\mathrm{tr}}(g/\sqrt{12})\sqrt{N}\|B e_j\|_\infty=T_{\mathrm{tr}}\|Be_j\|_\infty\). The last row is bounded by \(g-1<T_{\mathrm{tr}}\). In a minor of order \(k'\), products of row norm factors are bounded by \(\prod_{j=1}^d\|Be_j\|_\infty\) since each basis vector is nonzero and integral. Also \(T_{\mathrm{tr}}\ge1\). Expansion by permutations gives the bound
\[
d! T_{\mathrm{tr}}^d \prod_{j=1}^d\|Be_j\|_\infty
\]
on each such minor. This is at most \(H_1T_{\mathrm{tr}}\) or \(4H_2T_{\mathrm{tr}}^2\) according to rank, each below \(q\) by (I5). If \(k'=0\), the matrix is zero and the following lift is immediate. Otherwise `lem:lattice-facts` (c) applies to \(c^\top\Delta_*=0\bmod q\) and gives an integral \(u\equiv c\bmod q\) with \(u^\top\Delta_*=0\). Consequently \(u^\top\Phi(r)\) is constant on \(F\), and \((Bu_{[d]},u_{d+1})\) lies in the saturated normal lattice \(F^\perp\), reducing to \(v_{[i+1]}\). In particular \(F^\perp\) has positive rank. A rank-\(s\) lattice fiber has density at most \(g^{-s}\), since fixing the coordinates outside an invertible row minor leaves at most one assignment to the remaining \(s\) coordinates. Since \(\Pr[F]>\theta-\varepsilon_{\mathrm{tr}}>\mu_{\mathrm{tr}}\) and \(g^{-3}<\mu_{\mathrm{tr}}\), its normal lattice has rank at most two. Its maximum fiber density is at least \(\Pr[F]>\mu_{\mathrm{tr}}+2\varepsilon_{\mathrm{tr}}\). Apply the regularization result of Amendment I4 to \(F^\perp\) to get a regular saturated containing lattice with density at least \(m(F^\perp)-2\varepsilon_{\mathrm{tr}}\ge p_{i+1}-3\varepsilon_{\mathrm{tr}}\). It contains the lift of \(v_{[i+1]}\). This proves the induction.

For the terminal lattice choose \(J\) as above. Let \(z_0\in\mathbb{Z}^d\) with \(Bz_0\equiv v_{[N_0]}\bmod q\). It is nonzero mod \(q\) because \(v_{[N_0]}\ne0\). The preimage \(Z\subseteq\mathbb{Z}^d\) of the line \(\mathbb{F}_q z_0\) has index \(q^{d-1}\), since reduction of \(\mathbb{Z}^d\) is onto and the line has \(q\) elements out of \(q^d\). Hence \(L=B_J Z\) has determinant \(h(\Theta)q^{d-1}\). Consider the body of feasible first coordinates
\[
K_B=\{u\in\mathbb{R}^d:\|B B_J^{-1}u\|_\infty\le1\}.
\]
The rows indexed by \(J\) are the unit rows. Each \(d\)-row determinant has absolute value at most 1 because it is a minor of \(B\) divided by its largest minor, up to sign. The body is symmetric, closed, convex and bounded. In rank one the unit interval lies in it by the largest-minor bound and has length 2. Since \(h(\Theta)\le H_1\le\beta\), \(\operatorname{vol}(\beta K_B)\ge2\det L\). In rank two the ellipsoid result gives
\[
 \operatorname{vol}_2(\beta K_B)\ge(\pi\sqrt3/2)\beta^2
 \ge(\pi\sqrt3/2)(3/2)H_2q\ge 4 h(\Theta)q .
\]
The last inequality uses \(h(\Theta)\le H_2\) and \(3\pi\sqrt3/4>4\), which follows from \(\pi>3.14,\sqrt3>1.73\). The volume implication gives a nonzero \(u=B_J z\) in \(L\cap\beta K_B\) in each rank. Put \(x'=Bz\). It is nonzero because its coordinates in \(J\) are \(u\), and its norm is at most \(\beta\) by the definition of \(K_B\). Modulo \(q\), \(x'\) is a multiple of \(v_{[N_0]}\) since \(z\in Z\). If that multiple were zero, each integer entry of \(x'\) would be divisible by \(q\). As \(\|x'\|_\infty\le\beta<q/2\) this would force \(x'=0\). Extend \(x'\) by zeros in the deleted positions, including coordinate 0, to obtain the required short multiple.

## Amendment C7

The amended grid test is \(K_1\ge1,\ K_2\ge2,\ K_1 K_2=n\). The complete construction uses a single grid with exponent \(e=i+K_1 j\) for \(0\le i<K_1,\ 0\le j<K_2\). Its weight at exponent \(e\) is the linear coefficient \(\xi_e(w)=\varphi_e(w)\) of the original form \(z(w)\). The key cell has \(e=0\) and weight \(w_0\). The group, QAP, matrix and encoded kernel are kept. The change to the grid and its ties is accompanied by the algorithms and proofs below.

### Forms, setup, and sampling

Use the original deterministic QAP setup of the system \(S\), with admissible evaluation points, polynomials \(A_i,B_i,Z,Z_0,L_\rho\), and public field and group parameters. Write \(Z_*=Z(X)(X-\rho)\). Use the original uniform seed, query the seed oracle for every prescribed entry of \(M\), and compute the original \(z=\sum_{e<n}\varphi_e T^e\) over \(\mathbb F_{q^n}=\mathbb F_q[T]/(P)\), \(P=T^n-c_0\). Frobenius \(\sigma\) substitutes \(\omega T\) for \(T\). Draw \(r\) by \(\mathcal D_g\), independent of the other coins. Draw \(y,\tau,\Omega_{12}\) by the protected distributions. Draw independent uniform nonzero \(\Omega_{22},\alpha,\pi,s,\upsilon,\zeta,\zeta',\zeta'',\eta\). Draw \(\varepsilon\) uniformly from \(\mathbb F_q^*\) excluding \(-\omega^{-i}\) for \(0\le i<K_1\). The excluded values are distinct, and all scalar coin coordinates have supports of size at least \(q-D\): for \(\varepsilon\) use \(K_1+1\le n\le D\), since \(K_2\ge2\); for \(\tau\) use the excluded QAP point set of size \(D\).

Set \(\Omega\) to the triangular matrix with rows \((1,\Omega_{12})\) and \((0,\Omega_{22})\). For a left leg \(i\) and right leg \(j\) put
\[
 \pi_i=\pi\upsilon^i(1+\varepsilon\omega^i),\qquad
 s_j=s\upsilon^{K_1j},\qquad
 \gamma_{ij}=\pi_i s_j .
\]
These are nonzero. The key scalar is \(\kappa=\gamma_{00}L_\rho(\tau)\). The right mask is the vector
\[
 \vartheta_j=\eta\,\upsilon^{K_1j}z[\omega\upsilon]
        -\eta\varepsilon^{-1}(\omega\upsilon)^{K_1j}z[\upsilon].
\]
The brackets in \(z[x]\) mean polynomial substitution in the form coefficient vector.

### Transmitted arrays

For witness-coordinate indices \(a,b\in[0,N]\), the G1 array has the two coordinates of \(F^i_a=[\pi_i(y_a,A_a(\tau))\Omega]_1\) on each left leg and the cancellation entries \(Y_a=[\zeta''y_a]_1\). Publish the original quotient powers \(P_l=[\zeta\tau^l]_1\) for \(0\le l<\Delta\) and remainder powers \(P'_l=[\zeta'\tau^l]_1\) for \(0\le l<\Delta'\), \(\nu\nmid l\). The G2 plain array consists of
\[
\begin{aligned}
 H^j_b &= [\Omega^{-1}\big(s_j(r_b+A_b(\tau))+\vartheta_{j,b},
                  s_j(B_b(\tau)-y_b)\big)^\top]_2,\\
 S^j &= [s_j]_2,\\
 Q_{c,l}&=[\gamma_c Z_c(\tau)\tau^{l\Delta}/\zeta]_2 &&(c \text{ a cell},\ 0\le l<J),\\
 Q'_{c,l}&=[\gamma_c Z_0(\tau)\tau^{l\Delta'}/\zeta']_2 &&(c\text{ a cell},\ 0\le l<J'),\\
 C^\pm_b&=[\pi\eta\varepsilon^{\pm1}\upsilon^b/\zeta'']_2 &&(0\le b<2n-1).
\end{aligned}
\]
Here \(Z_c=Z_*\) at the key cell and \(Z_c=Z\) elsewhere. Indices in the last two lines range as shown independently of witness-coordinate indices. Both the plain array and its exponentwise \(\alpha\) copies are sent. Also send \([\alpha\kappa]_T\), the seed and \(m\oplus H_{\sf key}([\kappa]_T)\). Each exponent, including the scaled exponents and the hidden key exponent, is evaluated as a scalar, followed by one multiplication of the appropriate generator.

The number of G1 elements is the protected \((2K_1+1)(N+1)+\Delta+(\nu-1)n_{\mathsf c}/J'\): the first term counts the left factors and \(Y\), and the remainder count uses \(\nu\mid\Delta'\). Per G2 sector there are \(2K_2(N+1)\) right factor elements, \(K_2\) search bases, \(n(J+J')\) chunk bases and \(2(2n-1)=4n-2\) cancellation bases.

### Mask identity and decryption

For a stack of field matrices \(W_c\) write \(W(T)=\sum_c W_c T^{e_c}\) and define
\[
 \begin{aligned}
 t(T)&=W(T)z[\omega T]-W(\omega T)z[T],\\
 t^+(T)&=\left(\sum_{c=(i,j)}\omega^i W_c T^{e_c}\right)z[\omega T],\\
 t^-(T)&=-\left(\sum_{c=(i,j)}\omega^{K_1j}W_c T^{e_c}\right)z[T].
 \end{aligned}
\]
Multiplication with the sampled masks gives exactly
\[
  \sum_{c=(i,j)} \pi_i W_c\vartheta_j
   =\pi\eta\big(t(\upsilon)+\varepsilon t^+(\upsilon)+\varepsilon^{-1}t^-(\upsilon)\big).
\]
Indeed, the product with the first mask term has epsilon degrees zero and one, giving \(W(T)z[\omega T]\) and \(t^+\). The product with the second has degrees minus one and zero, giving \(t^-\) and \(-W(\omega T)z[T]\); the twist factors of degree zero multiply to \(\omega^{i+K_1j}\). All three vector polynomials have degree at most \(2n-2\). The revised tie is the exact polynomial identity \(t(T)=0\). Its reduction modulo \(P\) implies \(W\sigma(z)=\sigma(W)z\).

For a witness \(w\), reconstruct the seed matrix and compute all \(\xi_c=\varphi_{e_c}(w)\). The honest stack is \(W_c=\xi_c ww^\top\). For this stack let \(f=z[T](w)=\sum_c \xi_c T^{e_c}\). Then \(W(T)=f(T)ww^\top\), and \(t(T)=w(f(T)f(\omega T)-f(\omega T)f(T))=0\) as an ordinary polynomial. The two remaining polynomials have direction \(w\); denote their scalar factors by
\[
 x^+(T)=\left(\sum_{c=(i,j)}\omega^i\xi_c T^{e_c}\right)f(\omega T),
 \qquad
 x^-(T)=-\left(\sum_{c=(i,j)}\omega^{K_1j}\xi_c T^{e_c}\right)f(T).
\]
Thus the cancellation group element \(C_w\) in each G2 sector is the MSM of the \(C^\pm_b\) by the coefficients of \(x^\pm\). No epsilon-degree-zero cancellation bases occur. The exact vanishing of \(t(T)\) provides the cancellation of that term on every witness.

Compute \(Y_w=\sum_a w_aY_a\). For each right leg compute \(F_w^j=\sum_i \xi_{ij}\sum_a w_a F^i_a\) using the two coordinates, and \(H_w^j=\sum_b w_b H_b^j\) in each sector. Compute the two QAP quotients \(h_{\rm key},h_{\rm oth}\) and allowed remainder \(R_w\) of \(w\) from the protected QAP identities. Form \(G_l^{\rm key},G_l^{\rm oth}\) in G1 by MSMs of the quotient powers with their coefficients in each \(\Delta\)-chunk. Form \(G'_l\) by MSMs of the remainder powers with the \(l\)-th \(\Delta'\)-chunk, using the allowed exponents there. Each G1 list here is shared across the two sectors. In a G2 sector compute, by weighted sums of the listed bases,
\[
 V_l^{\rm key}=\xi_0 Q_{0,l},\qquad V_l^{\rm oth}=\sum_{c\ne0}\xi_c Q_{c,l},
 \qquad V'_l=\sum_c \xi_c Q'_{c,l}.
\]
In that sector compute
\[
\begin{aligned}
 \Lambda &= \sum_j \big(e(F_{w,1}^j,H_{w,1}^j)+e(F_{w,2}^j,H_{w,2}^j)\big)
 -\sum_l e(G_l^{\rm key},V_l^{\rm key})-\sum_l e(G_l^{\rm oth},V_l^{\rm oth})
 -\sum_l e(G'_l,V'_l)-e(Y_w,C_w),\\
 \Psi &=\sum_j e(F_{w,1}^j,S^j).
\end{aligned}
\]
The quotient sums use \(0\le l<J\); the remainder sum uses \(0\le l<J'\). Apply the same computation to alpha copies to get \((\Lambda^\alpha,\Psi^\alpha)\). For a witness the key weight is 1, so \(\Lambda'=\Lambda^\alpha-[\alpha\kappa]_T-c_w\Psi^\alpha\). Perform the original least-absolute integer search with the same bound \(B\), returning \(\bot\) if no such integer exists. Return the masked message XOR \(H_{\sf key}(\Lambda-(c_w+t)\Psi)\). One may test the key weight and return \(\bot\) at zero as in the protected decryption, although this cannot occur at a witness.

To check the identities, the factor pairings cancel the triangular basis and leave \(\gamma_c(y(w)r(w)+A_w(\tau)B_w(\tau))\) per cell before weighting, plus \(\pi_i y(w)\vartheta_j(w)\). The terms \(y(w)A_w\) from the two coordinates cancel each other. Summing the mask terms with weights gives the pairing of \(Y_w,C_w\) by the mask identity. The quotient and remainder subtractions leave \(\xi_c\gamma_c L_\rho(\tau)\) at the key cell and zero QAP term in each other cell. Thus \(\Lambda=[\kappa+r(w)\psi]_T\) and \(\Psi=[\psi]_T\), where \(\psi=y(w)\sum_c\gamma_c\xi_c\). Each alpha output is scaled by \(\alpha\), since all its G2 elements are exponent-scaled by \(\alpha\). The resulting search equation has the original form and the original centered distribution. Its result either has \(|t|=|r(w)-c_w|\) or \(t=0\) if \(\Psi^\alpha=0\); the protected search-spread bound and sign-class algorithm apply. Targets checks the exact key and correctness in both cases.

### Decryption counts and affected interfaces

For a costed witness, a sum over witness entries starts with entry zero and uses at most \(\lfloor N/2\rfloor\) additions. There are \(2K_1+1\) such arrays in G1 and \(4K_2\) in G2. The weighted coordinates of the left arrays use two length-\(K_1\) MSMs per right leg, totaling \(2n\). There are two sets of \(J\) quotient MSMs of length \(\Delta\), and the remainder MSMs total \((\nu-1)n_{\mathsf c}\) points. In G2, each sector uses at most \(n\) MSM points per quotient chunk across its key and other lists, and at most \(n\) points per remainder chunk. Its cancellation MSM has at most \(4n-2\) points. The two sectors share the G1 lists and use separately scaled G2 arrays. Per sector there are \(2K_2\) factor pairings, \(K_2\) search pairings, \(2J\) quotient pairings, \(J'\) remainder pairings and one cancellation pairing. Accumulating each target-group sum from its first summand uses \(3K_2+2J+J'-1\) additions per sector. The two additions in forming \(\Lambda'\) and one addition in forming the key give \(6K_2+4J+2J'+1\) altogether, one less than the pairing count. The two final GT scalar multiplications by \(c_w\) and \(c_w+t\) are within the original bound of four, since the witness key weight is one. This proves the amended bounds, with each entry stated again in its own section.

Setup, interpolation, the permitted QAP point placement, costed lattice instance and witness tests do not use the grid. Weight computation now reads the original linear forms. The number of oracle queries and the data needed from each of them are unchanged. The scalar algorithms use the protected form and QAP methods, with the displayed mask and cross polynomials. The latter products can be computed with the same polynomial multiplication procedure as the original degree-\(2n-2\) cancellation products; there are only two nonzero ones and no divisions. All exponent lists are filled using the indicated powers. The asymptotic group, field, and setup upper bounds under the original efficiency hypotheses follow by counting these arrays: \(K_1,K_2\le n\), the number of cell terms is \(n\), and the dimensions of the QAP interpolations and the source sums are unchanged. For balanced grids and linear-size parameter families with the original bounds on the grid products and chunk sizes, multiplying the grid product by at most two changes those upper bounds by a constant. Search has expected \(O(\sqrt g\,N^{1/4})\) group work subject to the unchanged range argument. The estimate as a function of \(\lambda\) in the original asymptotic corollary uses its particular choice of \(g\); our security parameters specify the new range.

The honest stack, tie and mask identity are given explicitly above. The new view, rank-two classification, symbolic ledger and extractor for this grid are proved below. They establish the expression, monitor, record, private-recovery and target interfaces for the revised construction. The protected lattice conditions depend on \(n,N,g,\theta,\beta\) and the kernel, with the original form definition, independent of these cell weights. Amendments I3, I4 and I6 prove the lattice claims with their combined hypotheses.

### Degree, view, and the recovery gradients

Fix \(M\), hence the coefficients of the protected \(z\), and treat all scalar coins as indeterminates. Use the two sectors \(\mathsf s\in\{\mathrm{plain},\alpha\}\) with factors \(a_{\rm plain}=1,\ a_\alpha=\alpha\). Let \(\mathcal X_1\) and \(\mathcal X_2\) be the two lists of source-group inputs including their generators. Write \(a(\mathbf c,r)\) for the scalar exponent of a label from \(\mathcal X_1\), and likewise for \(b\) from \(\mathcal X_2\). A target expression has value \(\sum_{a,b}D_{ab}a(\mathbf c,r)b(\mathbf c,r)+D_K\alpha\kappa\), with field coefficients \(D_{ab}\) and \(D_K\). Coefficients of a fixed expression do not depend on any of these indeterminates, even when distinguishing two evaluations of the same expression.

Put \(\varpi=\Omega_{22}\zeta\zeta'\zeta''\varepsilon\). This clears denominators in each term of the value because G1 exponents have none and the published G2 exponents have only the inverses in \(\varpi\), each to the first power. We now check the bound on the cleared degree. A left-leg scalar \(\pi_{k_1}=\pi\upsilon^{k_1}(1+\varepsilon\omega^{k_1})\) has degree at most \(2K_1\). Multiplying it by \(y_i\) or by \(\Omega_{12}y_i+\Omega_{22}A_i(\tau)\) costs at most \(D\) further degrees because \(A_i\) has degree less than \(D\). The G1 quotient powers have degree at most \(\Delta\), the remainder powers degree at most \(\Delta'\le D\), and the cancellation column degree two. Hence every G1 exponent has degree at most \(d_1=\max\{D+2K_1,\Delta\}\).

A cell scalar \(\gamma_c\) has degree at most \(e_c+3\le n+2\), and at the key cell at most three. The cleared quotient bases, including an alpha copy, have degree at most \(D+n+6+(J-1)\Delta\): the polynomial \(Z_c\) has degree \(D-1\) except at the key cell where it has degree \(D\), and clearing the one inverse of \(\zeta\) adds four degrees, with one more for \(\alpha\). The cleared remainder bases have degree at most \(N+n+9+(J'-1)\Delta'\le D+n+7\), using \(\deg Z_0=N+2\) and \((J'-1)\Delta'\le D-N-2\). For a cleared coordinate of a right factor, the QAP part has degree at most \(D+n+6\): it uses a right-leg scalar of degree at most \(n\), a polynomial in \(\tau\) of degree below \(D\) or a degree-one variable, and at most five degrees from \(\varpi\) and one from the sector. The ratio \(\Omega_{12}/\Omega_{22}\) has net degree zero after cancellation. The mask part uses a power of \(\upsilon\) of degree at most \(n-1\), an entry of \(z[x]\) of degree at most \(n-1\) in the evaluation scalar, one \(\eta\), and at most six degrees for clearing and the sector, for a total at most \(2n+5\). A search base needs at most \(n+6\) degrees cleared. The cross bases need at most \(2n+6\) degrees cleared: the powers have degree at most \(2n-2\), with at most one each for \(\pi,\eta,\varepsilon,\alpha\) and four for clearing the inverse of \(\zeta''\). Thus all cleared G2 exponents have degree at most \(d_2=D+n+7+(J-1)\Delta\). The cleared key scalars with and without \(\alpha\) have degrees at most \(D+8\) and \(D+7\). This proves the target-expression bound \(d_f=3D+2n+2K_1+6\), since \(d_1+d_2\le d_f\): if \(d_1=\Delta\), use \(J\Delta\le D+n\), and if \(d_1=D+2K_1\), use \((J-1)\Delta\le D+n-1\). The separate source-expression bounds \(d_1+5,d_2\) also fit \(d_f\). The argument uses no index in the \(z\) polynomial other than its degree bound.

For fixed \(r\), the independent valid scalar-coin ranges each have size at least \(q-D\); for \(\varepsilon\) this uses \(1+K_1\le D\), and for \(\tau\) the excluded \(D\) evaluation points. The clearing factor is nonzero there. By (P5), \(24\varepsilon_f\le E(2)\le 2^{-\lambda}\), so \(d_f<q-D\) because \(\varepsilon_f=(d_f+61)/(q-D)\). The independent-coordinate polynomial root bound, proved in Targets, now has two consequences. If \(D\) has value \(\chi\kappa\) for all valid coins at a fixed \(r\), the cleared polynomial is identically zero in the coin indeterminates. Otherwise the coincidence probability is at most \(d_f/(q-D)\le\varepsilon_f\). In the first case we can compare coefficients before clearing as identities in Laurent polynomials in the nonzero scalar indeterminates.

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
Here \(v\) ranges over the respective published powers. Each type has a distinct multidegree in \(\zeta,\zeta',\zeta'',\pi,\Omega_{12}\). The factor \(a_{\mathsf s}\) separates the two sector degrees in \(\alpha\). For any of the first four types, \(s_j=s\upsilon^{K_1 j}\) separates right legs by their distinct powers; within a leg the powers \(\tau^v\) are distinct and the polynomials \(B_i\) are independent by \(B(d_j)=e_j\). In the last two types, isolate the constant term in \(\varepsilon\) of \(\pi_{k_1}s_{\rm leg}\). Up to the distinct \(\Omega_{12}\) factor for the last type it is \(\pi s\upsilon^{k_1+K_1j}\). This exponent determines \(k_1,j\) uniquely in the prescribed grid. Again \(B_i\) are independent. Thus all \(\delta_{\mathsf s,a,{\rm leg},j_0}=0\). This gives both conclusions simultaneously: the coefficients pairing \(F_2\) with the second right coordinate equal those pairing the corresponding \(F_1\) with the first, and the coefficient of the first right coordinate paired with any other G1 input is zero.

For the remaining view properties, group the expression into homogeneous classes in \(\pi,\zeta,\zeta',\zeta''\), and the joint degree in \((\Omega_{12},\Omega_{22})\), and separate the two powers of \(\alpha\). The class of \(\chi\kappa-D_K\alpha\kappa\) has degree one in \(\pi\) and zero in the other class coordinates. Among pairs in this class, the left first coordinates pair with the right first coordinates, search bases, and the plain generator. The left second coordinates pair with the right second coordinates. The quotient and remainder powers pair with their matching kinds of bases, and the Y column pairs with the cancellation bases. These are all possibilities: the five types of nonzero class coordinates on the G1 side are the linear degree in \(\pi\), degree in \(\pi\) together with positive hidden-basis degree, and degree in exactly one of \(\zeta,\zeta',\zeta''\). G2 exponents of the appropriate complementary degrees are precisely the listed types. Treat a pair of generators as being in the plain sector. In each sector the sum of this class has value \(a_{\mathsf s}\chi_{\mathsf s}\kappa\), with \(\chi_{\rm plain}=\chi\), \(\chi_\alpha=-D_K\).

Define \(W_c\) by the \(F_1,\mathsf H_1\) pairing coefficients in this sector, and \(u_c\) to be the negatives of the \(F_1,\mathsf S\) pairing coefficients. The matched \(F_2,\mathsf H_2\) terms cancel the hidden-basis part. Divide the class identity by \(a_{\mathsf s}\). Using the product of the two untransformed factors, its left side is \(\sum_c\gamma_c b_c+\Phi_*\) with
\[
 b_c=y^\top(W_c r-u_c)
      +y^\top(W_c-W_c^\top)A(\tau)
      +(P_{W_c}+h_cZ_c+Z_0R_c)(\tau).
\]
Here \(h_c\) is assembled from the quotient coefficients, and \(R_c\) from the allowed remainder powers. The latter is allowed because each chunk adds a multiple of \(\Delta'\), which is divisible by \(\nu\), to its exponent. The term \(\Phi_*\) is the sum of the uncancelled masks, the pairs of the Y column with cancellation bases, and the pairs of first left factors with the generator. It is free of \(s\). Isolating each monomial \(\pi s\upsilon^{e_c}\) at degree zero in \(\varepsilon\) gives \(b_c=0\) except at the key cell, where it gives \(b_c=\chi_{\mathsf s}L_\rho\). In both cases \(b_c\) contains no \(s,\pi,\upsilon,\varepsilon\), and distinct cells have distinct exponents \(e_c\). With these identities the original class identity also gives \(\Phi_*=0\).

In each cell the linear coefficient in \(y\) at \(\tau=d_0\), where \(A=0\), gives \(W_c r=u_c\). Then the same coefficient at \(\rho\) and at \(d_j\), where \(A=e_0\) and \(A=e_j-e_0\), implies \(W_c-W_c^\top\) annihilates a spanning set, so \(W_c\) is symmetric. The constant term in \(y\) for each non-key cell is the non-key QAP criterion of the protected QAP lemma with \(h,R\) equal to \(-h_c,-R_c\). In the key cell evaluate at \(\rho\), where \(Z_c=Z_0=0\), to get \((W_c)_{00}=\chi_{\mathsf s}\); then the constant term is the key QAP criterion. All cells therefore pass, and the plain key corner is \(\chi\). Finally, in \(\Phi_*=0\) isolate degree one in \(\eta\) and degree zero in \(\varepsilon\). By the mask identity in Amendment C7 the masks contribute \(\pi\eta\, y^\top t(\upsilon)\). The pairs of \(Y_i\) with cancellation bases have epsilon degree \(+1\) or \(-1\). The pairs with the generator have no \(\eta\). Independence of the \(y_i\) therefore gives \(t(T)=0\), the revised tie.

The coefficient-vanishing property also implies that the difference in values between \(r'\) and \(r\) is
\(\sum_{\mathsf s}a_{\mathsf s}\sum_c\gamma_c y^\top W_c^{\mathsf s}(r'-r)\), since only the first right coordinates depend on \(r\). It vanishes whenever all \(W_c^{\mathsf s}r'=u_c^{\mathsf s}\), proving the locus statement. With zero stacks the identity holds formally at every \(r'\), and the plain key corner forces \(\chi=0\). An identity holding formally for any \(\chi\) makes \(W_c^{\mathsf s}r\) constant for all \(r\), so all stacks are zero and again \(\chi=0\). For two source expressions that are formally different, pair their difference with the other source generator. This has zero stacks. If it vanished identically at even one \(r\), the just-proved locus statement would make the original source expressions formally equal. Hence it has the coincidence bound at each \(r\), proving the source clause of the view lemma as well.

For recovery, the derivative in \(r_j\) in any sector initially sums over every G1 input paired with the first coordinate of each right factor. By the proved vanishing, only \(F_1\) remains, producing \(a_{\mathsf s}\sum_{c,i}\gamma_c y_i(W_c^{\mathsf s})_{i,j}\). The same coefficient array is used at every private point, so this equation applies there even though the original identity was assumed at the actual search vector. It proves the row-space inclusion and, when the plain mark stack is zero, the vanishing of the plain gradients. This derivation and the degree and view arguments use the degree of \(z\), the locations of its mask terms, and the exact mask identity proved in Amendment C7.


### Rank-two tied stacks

Let a nonzero stack have symmetric passing coefficient matrices, the tie \(W\sigma(z)=\sigma(W)z\) and row space \(\mathcal V\) of dimension \(d\le2\). Suppose \(\mathcal V\) contains no nonzero kernel vector of \(z\). We prove that it contains a witness and that the stack is a linear combination over \(\mathbb F_q\) of the new honest stacks of witnesses.

Choose a column basis matrix \(P_*\in\mathbb F_q^{(N+1)\times d}\) of \(\mathcal V\) and denote its rows by \(u_i^\top\). Over \(F=\mathbb F_{q^n}\), put \(h_0=P_*^\top z\) and \(h_1=\sigma(h_0)\). The entries of \(h_0\) are linearly independent over \(\mathbb F_q\), since a nonzero relation would give a kernel vector from the basis columns. For \(d=1\) this gives \(h_0\ne0\). For \(d=2\), if \(h_0,h_1\) were dependent over \(F\), the ratio of their first and second entries in \(h_0\) would be fixed by \(\sigma\). The fixed elements of Frobenius solve \(X^q-X=0\), whose \(q\) roots are exactly \(\mathbb F_q\), contradicting independence. Thus the two vectors span the \(d\)-dimensional \(F\)-space.

Every coefficient of \(W\) has image in \(\mathcal V\) by symmetry, and both \(W,\sigma(W)\) can be written \(P_*\Xi_sP_*^\top\) for \(s=0,1\), with symmetric \(\Xi_s\). To see this, choose a left inverse \(U\) of \(P_*\). Left projection \(P_*U\) fixes these images, and right projection is the transpose by symmetry. Therefore \(\Xi_s=U W_s U^\top\) gives the factorization and is unique; here \(W_0=W,\ W_1=\sigma(W)\). In particular \(\Xi_1=\sigma(\Xi_0)\) since the basis and its left inverse have field coefficients in \(\mathbb F_q\). The tie becomes \(\Xi_0 h_1=\Xi_1 h_0\). There is an \(F\)-linear map \(\Xi(h_s)=\Xi_s\) from \(F^d\) to symmetric matrices: in rank two the inputs are a basis, and in rank one \(h_1=a h_0\) with \(h_0\ne0\), so the tie implies \(\Xi_1=a\Xi_0\). Its trilinear form \(U_*(h;x,x')=x^\top\Xi(h)x'\) is symmetric in \(x,x'\), and in \(h,x'\) on the spanning \(h_0,h_1\) by the tie. By linearity it is totally symmetric. The Booleanity tests for \(W\) and \(\sigma(W)\) imply \(U_*(h;u_j,u_j-u_0)=0\) for every \(h\) and each \(j>0\).

If \(u_0=0\), select a basis of \(F^d\) among the remaining \(u_j\), which span it. Every component of the symmetric tensor in that basis has a repeated index since \(d\le2\), and Booleanity at the repeated index sets it to zero. This gives the zero stack, a contradiction. Therefore \(u_0\ne0\). Set \(l_0=u_0\), and if \(d=2\) complete it by \(l_1=u_j\) from some \(j>0\). When \(d=2\), define the two vectors \(p_\delta\) by \(l_0^\top p_\delta=1,\ l_1^\top p_\delta=\delta\), \(\delta=0,1\); for \(d=1\) use just the normalized \(p_0\). They are an \(\mathbb F_q\)-basis of their space. Further, \(p_\delta p_\delta^\top\) are independent: in rank two evaluating on \((l_1,l_0)\) isolates the coefficient of \(p_1p_1^\top\), then evaluating on \((l_0,l_0)\) isolates the other. This also holds in rank one by the latter evaluation.

In rank two the components of \(U_*\) on \(l_0,l_1\) with one, two or three occurrences of \(l_1\) agree. Replacing two \(l_1\)'s by \(l_1,l_0\) preserves each component by the Booleanity identity and total symmetry. The component with no occurrence may be different. The two cubes \(p_0^{\otimes3},p_1^{\otimes3}\) span exactly this space of tensors, because the first cube evaluates to one only on the all-\(l_0\) tuple and the second evaluates to one on every tuple. In rank one the single cube spans the tensors. Consequently for coefficients \(c_\delta\in F\),
\[
 \Xi(h)=\sum_\delta c_\delta (h^\top p_\delta)p_\delta p_\delta^\top.
\]
Put \(w_\delta=P_*p_\delta\), so \(w_{\delta,0}=1\). The quantities \(h_0^\top p_\delta=z(w_\delta)\) are nonzero by the no-kernel property. Compare the two expressions for \(\Xi_1=\sigma(\Xi_0)\), using independence of the squares, to get \(c_\delta=\sigma(c_\delta)\) and therefore \(c_\delta\in\mathbb F_q\).

For any linear passing test \(L_*\), its value on \(W\) and \(\sigma(W)\) vanishes. The two equations are
\[
 \sum_\delta c_\delta L_*(w_\delta w_\delta^\top)\,(h_s^\top p_\delta)=0,\qquad s=0,1 .
\]
Since \(h_0,h_1\) span, this says \(\sum_\delta c_\delta L_*(w_\delta w_\delta^\top)p_\delta=0\). Independence of the \(p_\delta\) forces each coefficient to be zero. Hence every \(w_\delta\) with \(c_\delta\ne0\) passes all Booleanity and constraint tests and is a witness. Some coefficient is nonzero since the stack is nonzero. By the expression for \(\Xi_0\), each coefficient matrix of \(W(T)\) is the same combination of \(\varphi_e(w_\delta)w_\delta w_\delta^\top\), proving the claim. A representation by such normalized assignments is unique by independence of their squares, so any such representation with all passing tests has the same support property.

Ranks above two do not occur for heavy stacks by Amendment I4. The protected rank-one property of passing matrices is independent of the weights and remains valid. The original classification for the original three families of conjugate products is not used for these ciphertexts. The argument above supplies the classified stacks and witnesses needed by the revised extractor and private reduction, as proved in Targets.

## Amendment n2

The transmitted G2 count per sector is \(n_2=2K_2(N+1)+K_2+n(J+J')+4n-2\). The four kinds of terms are counted in Amendment C7. Both sectors are transmitted. Its encryption, honest combination and security proof supply the construction dependencies of this revised count.

## Amendment dec_sum_g2

The G2 addition bound is \(2K_2(N+1)\). The \(4K_2\) witness sums in Amendment C7 use at most \(4K_2\lfloor N/2\rfloor\) additions. Its correctness proof uses those sums.

## Amendment dec_msm_g1

The G1 MSM length bound is \(2n+2J\Delta+(\nu-1)n_{\mathsf c}\), from the weighted left factors and the three QAP lists counted in Amendment C7. Its honest combination and correctness arguments cover these operations.

## Amendment dec_msm_g2

The G2 MSM length bound is \(2n(J+J')+8n-4\), from the QAP and cancellation lists in the two sectors, as counted and used in Amendment C7.

## Amendment dec_pairings

The pairing bound is \(6K_2+4J+2J'+2\), from the factor, search, QAP and cancellation pairings in both sectors. Amendment C7 derives the two honest sector values from precisely these pairings.

## Amendment Ncmp

For the variable \(u\) used by the bound \(E\), set
\[
N_{\mathrm{cmp}}(u)=\frac{u(u+10)}8 .
\]
The remaining formula for \(E\), the values of \(u=2Q+2\) used by the proof, and the two tests in (P5) are as specified in the protected model. The new count applies to the bad events that can pay a \(\theta\) charge. The other pair and entry terms continue to pay for the full collection of possible coincidences.

### Coupling and bad events

Fix the uniform matrix realization \(M\) for the expressions, and fix the adversary's call budget \(Q\). The run up to the first query at the target label has the same law as the run with a uniform string in place of the masked message up to that query without its answer, by the coupling of the protected symbolic-game block. In the latter run the oracle answers and the uniform string can be chosen independently of the valid encryption coins and the search vector. The symbolic simulation with formal equality, including its label images, can therefore be sampled before evaluating the expressions at those coins. An entry introduced on a guessed operand is a new formal variable of its group. The simulation uses at most three new entries per call, for two operands and one result. Received entries are present at initialization. If a result is already formally equal to an entry, the simulation returns that label rather than inserting a new entry.

Evaluate the symbolic simulation at the independent coins and uniformly independent guess-variable values. Within a group a collision means equality of evaluated values for two formally distinct entries. One can couple the evaluated symbolic and random-mask runs until the first such collision. In the real run conditional on the label images, each unused label in any of the three groups, when guessed, has a uniform exponent among the field values not already assigned in its group, and each evaluated result with a new value receives a uniform unused label. Use the same fresh labels in the symbolic and real simulations for new values. Use the uniform guess-variable value for the real guess if it is new in that group, and redraw from the unused field values if it is already assigned. If \(m\) exponents are assigned, each unused exponent has probability \(1/q+(m/q)/(q-m)=1/(q-m)\) under this coupling. Membership tests for all valid guessed operands, including rejected calls, use the same label images. The two simulations can differ only at a collision. Inductively, before a collision all assigned labels and their expressions agree between the two simulations, and calls and oracle queries agree because the adversary sees the same transcript. The first call on which a collision occurs is common to both runs, even when the answers at that call differ.

The initial collisions are an \(\mathsf{init}\) mark. Suppose a non-initial collision occurs first, before a target-label query has set a mark. If the collision is good in the protected symbolic-game sense, its two entries lie in the target group and their difference has no guess variable. Its later entry cannot be a guessed operand, because that would introduce a new formal variable absent from the earlier entry. It is a result. The real result takes the earlier label, so the monitor sets a good difference mark. Thus a collision that gives a charged first mark must be a bad event. If a target-label query sets a charged first mark before a collision, the queried label has an entry, since otherwise the mark is \(\mathsf{guess}\). This entry has the target value and its expression is bad by the monitor definition. If the first evaluated-symbolic collision instead triggers a redraw of a guessed operand in the real simulation, that collision already contains the fresh guess variable and is bad. It covers any later charged mark even if the real monitor made no mark at the redraw. Hence a charged first mark is covered by the bad collisions after initialization and the bad key-value events in the symbolic simulation.

For a fixed simulation a collision uses the difference expression \(D\) and \(\chi=0\), and a key-value event uses the entry \(D\) and \(\chi=1\). We bound the probability of a bad event over its evaluation. In either source group, if the difference has no guess variable, the source-group coincidence estimate established above bounds its probability by \(\varepsilon_f\). If the expression contains a guess variable in any group, there is a nonzero formal coefficient of a guess monomial. Such a coefficient is either a nonzero field constant or a formally nonzero expression in one of the source groups, since products of guesses arise only through a pairing of source-group expressions. In the latter case for every fixed \(r\) it is nonzero on some valid encryption coins by the source-group coincidence estimate and \(\varepsilon_f<1\). Thus after clearing the factor \(\varpi\), the event equation is a nonzero polynomial in coins and guess values for each fixed \(r\). Its total degree is at most \(d_f+1\). The terms without guesses have degree at most \(d_f\) by the degree lemma. A term with one guess multiplying a source-group expression adds one degree to the cleared source expression, and terms with two guess variables and no other exponents have degree at most seven after clearing. All independent sampled field coordinates have support size at least \(q-D\). The polynomial root bound gives probability at most \((d_f+1)/(q-D)\le\varepsilon_f\).

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

The comparison count enters the admissibility block only through (P5). Interpreting the expression, monitor and symbolic-game records on the revised input lists changes their leaf exponents and stacks. The degree, identity, locus and formal-equality results for those leaves are proved in the view derivation above. The first-mark categories, sample spaces, random-mask coupling and proof of the factor-one-half lemma do not involve the transmitted formulas, beyond requiring a uniform key-oracle mask. The mask is formed by that same rule in Amendment C7. The per-sector label bounds \(L_1,L_2,L_T\) cover the generators and revised lists; any overcount enlarges the initial bound and reduces the lower estimate \(N_{\rm free}\).

For initial labels, condition on the matrix and independently sampled search vector. Two formally different source inputs have coincidence probability at most \(\varepsilon_f\) by the source estimate below. Two formally different GT inputs have zero matrices, so the same bound follows from the zero-stack locus and degree estimates below. A union bound gives \(\sum_s\binom{L_s}{2}\varepsilon_f\). For a target query with no entry before a collision, conditional on the label table, membership decisions and queried strings, the unused target label has a uniform position among still undecided strings when it has no entry. This follows from permuting unused strings in the uniform label injection, which leaves all such observations fixed. The exclusions comprise at most \(L\) initial strings, \(3Q\) strings from generic calls (up to two operands and one result, including rejected operands), \(2^\lambda\) earlier key query strings, and one reserved string. Since \(3Q+2^\lambda+1\le3\cdot2^{\lambda+1}+1\), at least \(N_{\rm free}\) positions remain. Conditioning on prior misses fixes those queried strings and leaves the other positions exchangeable. Summing over at most \(2^\lambda\) key queries gives the \(2^\lambda/N_{\rm free}\) bound. The mask coupling and factor-one-half result depend on this actual label experiment and a uniform random oracle pad. The ciphertext publishes the same mask \(m\oplus H_{\sf key}([\kappa]_T)\), so the coupling equates transcripts through the first query at the target as before, regardless of the source input lists.

This leaves the reduction's private comparisons and good-mark success, proved for the revised ciphertext in Targets. The charged-mark and generic-ledger results are already proved above under this \(N_{\rm cmp}\).

The extractability-error corollary follows with its original statement from Targets and the factor-one-half lemma. For allowable budgets, in the combined bit experiment with uniform \(b\), put \(f_i=\Pr[\mathsf{Tgt}\wedge\mathsf{Fail}\mid b=i]\). The probability of both a correct bit and extraction failure is at most \(1/2+(f_0+f_1)/4\). The target-query bound in Targets gives \(f_i\le (Q+1)/2^\lambda+s_i\) for each \(i\). Both reductions run in time bounded by \(t_R=t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)\), including fixed description and advice, so each \(s_i\) is bounded by \(\operatorname{Adv}^{\mathrm{MSIS}}(t_R)\) by its defining maximum. Substitution gives extractability error at most \((Q+1)/2^{\lambda+1}+\operatorname{Adv}^{\mathrm{MSIS}}(t_R)\) at the same extractor time. Outside the stated budgets, the trivial probability upper bound 1 yields error \(1/2\) as in the corollary. This accounts for every result in the background list of the bound block.

## Targets

Fix any parameter set satisfying the amended model, any system of the protected shape, and any admissible choice of its QAP points. Use the encryption, decryption and linear weights of Amendment C7, with the original form encoding and group and oracle models. The combined inverse conditions and the charged comparison count are justified above. The following proves the same correctness and extraction statements, with the same adversary class and costed Module-SIS instance.

### Polynomial root bound

A nonzero polynomial of total degree \(d_*\) in independent variables sampled uniformly from respective field subsets of size at least \(m\) vanishes with probability at most \(d_*/m\). In the final variable write it as a polynomial of degree \(j_*\) with nonzero leading coefficient of degree at most \(d_*-j_*\) in the earlier variables. By induction the leading coefficient vanishes with probability at most \((d_*-j_*)/m\). Where it is nonzero, at most \(j_*\) values of the final variable are roots, giving conditional probability at most \(j_*/m\). The one-variable bound follows by dividing out a linear factor for each root, and a nonzero constant has no roots.

### Correctness with error \(2/q\)

For every witness, \(\xi_0=w_0=1\) by the prescribed form \(\varphi_0\). The honest equations of Amendment C7 give \(\Lambda'=(r(w)-c_w)\Psi^\alpha\) and \(\Lambda=[\kappa+r(w)\psi]_T,\ \Psi=[\psi]_T\). If \(\Psi^\alpha\ne0\), its order is \(q\), and the protected range bound and \(2B+1<q\) yield the unique matching \(t=r(w)-c_w\). If \(\Psi^\alpha=0\), then \(\Lambda'=0\), the least absolute result is \(0\), and \(\Psi=0\) since \(\alpha\ne0\). In either case the computed key is \([\kappa]_T\). The final XOR returns the original message, so the correctness error is zero and in particular at most \(2/q\). The original failure characterization in terms of a zero key weight holds with an empty failure event on witness inputs.

### Extraction and the reduction

Let \(\mathcal A\) have the budget \(Q<2^\lambda\) of generic group calls and at most \(2^\lambda\) queries to each oracle. Fix one bit \(b\) and messages \(m_0,m_1\), and run the extraction experiment with \(m_b\). The extractor reads only the answered generic transcript, with no oracle calls. It uses the two-sector sketches with one matrix per cell of the amended grid. It samples three independent probe vectors for each cell and sector, uses the linear combinations of source-group records and pairings to form sketches, tests the sketches of the result and the difference when there is an old record, and directly checks any candidate assignment against \(S\). In rank at most three, there are at most four assignments with first coordinate 1 to test: row echelon pivot coordinates determine the vector, pivot 0 must be present, and at most two remaining pivot choices are bits. Output is therefore always \(\bot\) or a witness. A record creation, result, or difference touches \(O(K_1N+n)\) field elements, since a source-group record uses at most \(K_1\) length-\((N+1)\) vectors or \(6n\) values, and the pairings compute six such combined sketch vectors. For a pairing, forming the inner products in the G2 record or summing per left leg and combining the G1 vectors uses \(O(K_1N+n)\) operations. A test uses \(O(N)\) for elimination with at most three rows and \(O(N+|S|)\) to generate and check the constant number of candidates. Initialization samples \(6n(N+1)\) field values, enters the \(L\) labels as records whose vectors are materialized on first use, and uses \(O(nN+L)\) time. There are at most four tests per result. Thus the extractor uses \(O((Q+1)(nN+|S|)+L)\) time because \(K_1\le n\) and \(N\ge1\).

The reduction on input a uniform \(A\in R_q^{k\times\ell}\) samples the seed, programs the seed oracle at that seed on matrix columns 1 through \(\ell\) using \(A\), and samples the other answers lazily, including the independent column 0. It samples encryption coins as specified, produces the ciphertext for \(m_b\), and simulates all generic labels and names and random oracles by the protected lazy tables. It runs \(\mathcal A\) once and uses its answered generic transcript without using its output or random-oracle query transcript. The lazy oracle simulation implements the law of direct oracle access. Because the programmed entries are jointly independent uniform ring elements for uniform \(A\), all oracle answers including entries at the selected seed have exactly the joint law of the experiment. Private evaluation points are sampled independently of the run.

The reduction keeps records evaluated at its private test point, using the protected rules for guessed operands and for existing records. It tries the first GT result whose label has an existing record of different private value, using the difference expression, and also the target label's record if present. For each tried expression it computes three independent gradient vectors in each sector at private recovery points, tests their span for a kernel vector, using the plain sector first, and applies the unchanged LIFT algorithm if there is such a vector. An output from LIFT is a short multiple of that kernel vector. The coefficient of \(T^0\) in \(z(v)\) is \(v_0\). All \(kd_R\) remaining row coefficients give the equations of \(A\) on the packed input once \(v_0=0\). Thus a nonzero kernel vector has \(v_0=0\) and satisfies \(A\hat v=0\). Its short multiple has \(x_0=0\) since \(2\beta<q\). Reduction and packing commute, and packing preserves the other \(N\) coordinates and adds only zeros. This packs the output into a nonzero norm-at-most-\(\beta\) solution to \(A\hat x=0\), exactly for the challenge whose rank, columns, bound, and norm are costed by M1. If no such output is found the reduction returns \(\bot\). Denote its success probability by \(s_b\). The cost is \(t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT}\) with \(Q_H\) the maximum per-oracle query count, \(C_R=O((N+n)D+\mu)\) for the fixed simulation setup and postprocessing, and \(T_{\rm LIFT}\) the time of the lifting step. The exact per-call part of the protected reduction-time accounting applies to these lists. On a call the private monitor uses at most 14 operations for lookups, values, node and result label, and the check of its record. Six recovery passes each use at most 19 operations per call, three for scalar forward evaluation and eight for each of two differences or target records on reverse evaluation. For each, four operations propagate derivatives through the scalar operation and four handle the received operand derivatives. Input exponents and their single-coordinate derivatives for a first right coordinate are initialized before these passes. All other received operands have zero derivative. For two unseen operands the label membership and exponent sampling cost at most \(2\cdot8\) operations, two zero records cost at most two, and handling a name costs at most two. This gives \(14+6\cdot19+2\cdot8+2+2=148\) with the same allowed table operations. The key and seed oracle answers use at most three and \(d_R+2\) operations per query, respectively. Fixed setup fills eight sets of exponent values by evaluating \(O(N)\) polynomials of degree below \(D\), iterating powers up to the chunk capacities and the \(O(n)\) mask degrees, preparing the form data, and creating \(O((N+n)D)\) exponent records. Even if each mask vector is computed by summing all \(n\) forms, using the shared two evaluations \(z[\upsilon],z[\omega\upsilon]\) costs \(O(nN)\); multiplying them by right-leg scalars is \(O(K_2N)\). Description and advice consist of fixed oracle simulation code and the QAP and coefficient data of this size. Postprocessing evaluates the form map on constantly many gradient vectors and solves systems of width at most three, using \(O(nN)\) operations, apart from the two separately counted LIFT calls. Hence \(C_R=O((N+n)D+\mu)\). LIFT's running-time result applies by \(2\beta<q\) and (P4). In particular the cost is \(t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)\) using \(n,N\le D\).

Here is how the first-mark bounds apply to these algorithms. The revised degree and view properties are proved above. To see the record invariant, setting guesses to zero commutes with linear operations and pairings, and before the first mark, reusing a record means equality of formal expressions. Formal equality of target expressions implies equality of stacks since their difference is formally zero and the view equations then give fixed \(W_c r\) for every \(r\). Thus the updated sketches represent the same stacks as the formal entries until the first mark. A good mark has a passing stack satisfying the revised tie. It has rank at most two by the rank bound and \(g^{-3}<\mu_{\rm tr}<\theta\) from Amendment I4. A kernel vector in its row space has coordinate 0 equal to zero, and its one-dimensional guessing probability is at least the stack's, by the protected guessing-probability lemma. The amended inverse theorem gives a short multiple, so LIFT succeeds on it.

At a first good difference mark the record invariant gives its formally nonzero difference. Choose a search vector where the cleared polynomial is nonzero in the coins. This certifies that the joint cleared polynomial in the private coins and the independent uniform search vector is nonzero. Prior record equalities hold at every private point, so this difference is the first detected different private value unless the polynomial vanishes at that point. The degree bound and the uniform valid coin ranges give probability at most \(\varepsilon_f\) for this failure. For a first good key mark the target record already has its expression by the record invariant. The first record persists until the reduction tries it. A name call negative is a GT result and receives the same mark and sketch tests. For a recognized good mark, the gradient identity proved in the revised view places all vectors in its sector row space and puts the plain vectors at zero in the alpha-mark case. For any proper subspace of the mark row space choose a linear form zero on the subspace and nonzero on the row space. Its value on one gradient, divided by \(\alpha_{\mathsf s}\pi\), is a polynomial of degree at most \(n+2\) which is nonzero by the distinct monomials \(s\upsilon^{e_c}y_i\) in the degree-zero part in \(\varepsilon\). The valid values for the independent coin coordinates have sizes at least \(q-D\), by the sampling ranges proved in Amendment C7 and \(K_1+1\le n\le D\). The polynomial root bound, with \(q-D\) in place of \(q\) in its proof, bounds the chance of failing to increase the span while it is proper. Three independent points and rank at most two give failure at most \(3(n+2)/(q-D)\le\varepsilon_f\), by \(n\le D\) and the formula for \(\varepsilon_f\). Thus on a good first mark with a kernel vector, except for the two exceptional events just bounded, the reduction finds a kernel vector in the appropriate span, and produces the MSIS output. The unconditional probability of such a mark is at most \(s_b+2\varepsilon_f\).

For a good first mark with no kernel vector, the rank-two tied-stack result proved above gives a witness in its row space. In that sector the linear map from a tuple of probes to \(\sum_c W_cv_c\) has image the row space, as each matrix is symmetric and the sum of its images is the row space of the stack. Uniform independent probe tuples give three independent uniform vectors in this space, even conditional on the run. In dimension \(a\le2\), the chance of failing to span is bounded by \(\sum_{j=0}^{a-1}q^{j-3}<2/q\): equivalently the \(a\) rows of the random \(a\)-by-3 coordinate matrix are independent uniform three-dimensional vectors and the next row falls in the span of \(j\) independent previous rows with probability \(q^{j-3}\). At a difference mark the extractor tests the record difference. If the previous entry was created as a pure guess, the result must contain that guess with coefficient one for the difference to be guess-free. That label was therefore used in an earlier answered call or in the current call, and its zero record exists by the difference test. At a key mark it tests the record of the result that obtained the target label. An initially received record has zero stack and thus is no good mark. These facts from the record invariant show that if the sampled vectors span, the witness is among the assignments tested. So the probability of a good first mark with no kernel vector and with extractor failure is at most \(2/q\).

Let \(u=2Q+2\). Every target query run has a first mark. The initial, guessed-label and charged-mark estimates proved in Amendment Ncmp bound their three probabilities by
\[
\left(\binom{L_1}{2}+\binom{L_2}{2}+\binom{L_T}{2}\right)\varepsilon_f,\quad
N_{\rm cmp}(u)(\theta+\varepsilon_f)
+\left(\binom{L+3u}{2}+L+3u\right)\varepsilon_f,\quad
2^\lambda/N_{\rm free},
\]
respectively. These estimates concern the same sampler, oracle and record laws and use only the already checked view and degree properties, budget, and label counts. Together with the two good-mark cases they cover the event of a target key query and no witness. Their sum is at most \(s_b+E(u)\): the good-mark excess is \(2\varepsilon_f+2/q\le (8u+8)\varepsilon_f\), using \(\varepsilon_f\ge1/q\); the remaining terms of \(E\) are nonnegative and its guess term contains \(2^\lambda/N_{\rm free}\). By (P5) and the generic-ledger implication of Amendment Ncmp \(E(2Q+2)\le(Q+1)/2^\lambda\). Hence for each \(b\) the target-query and no-witness probability is at most \((Q+1)/2^\lambda+s_b\), with exactly the stated oracle budgets and one MSIS instance. This proves Theorem 5.9 with its extraction time and soundness as above.
