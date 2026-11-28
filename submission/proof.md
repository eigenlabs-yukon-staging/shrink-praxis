# Praxis with a Euclidean coefficient-norm SIS reduction

Throughout the proof $N$ is the protected external variable count and $N_\star=N+3$ is the number of internally sampled box coordinates. The three internal Boolean coordinates do not change which external witness relation is encrypted. The construction, coefficient placement and probabilities for the amended model follow.

## Amendment C5

Write $d=d_R$, $h_R=\mathrm{ring\_log}$, $p=\mathrm{pack\_digits}$, $p_f=\mathrm{form\_pad}$, $A_c=3n/2$, $S_0=\lceil(D-1)/\nu\rceil$, and $m=k(\ell+1)d$. Put $J_Q=\lceil(D-1)/\Delta\rceil$, $J_R=\lceil\nu n_{\mathsf c}/\Delta\rceil$, and $J=J_Q+J_R$.

Require $\mathrm{ring\_mode}=d_R=1$, $h_R=0$, $\lambda=100$, $N=391693$, $\nu=2048$, $n_{\mathsf c}=1692$, $p,p_f\in\mathbb Z$, $1\le p\le d_R\le4p$, $p_f=7$, $n=3434$, $K_1=101$, $K_2=17$, $J\le28$ and $m\ge60000000$. The scalar arithmetic guard is $W+V\le 3m$, where $W$ and $V$ are the following integers:
\[
 W=d\big((\ell+1)(3\lfloor k/2\rfloor+2(k\bmod 2))+2\lfloor k/2\rfloor\big)
\]
\[
 \begin{split}
 V={}&2D+N+n_{\mathsf c}+32+(2K_1+6K_2+9)(N+4)+2K_2\\
    &+(\Delta-\Delta/\nu+2S_0+16)+(J+1)A_c+C_{\rm mask}\\
    &+70(n+J+1)+10000+189336+100+299511264 .
 \end{split}
\]

The degree-one ring is $\mathbb Z$ with unit basis $(1)$ and reduction $\mathbb F_q$. Take evaluation, its inverse and transposes to be identities. Each seed-oracle entry is a uniform independent scalar, reused on repeated queries. The MSIS challenge programs the nonconstant columns by their scalars, and column zero is independent. No split-basis conversions are needed. The two mask products use the scalar row pairs in $W$. The last term of $V$ equals $50ns_0+2000+2u(N+4)$ with $u=6$. The first part accounts for the tower coefficient supports. The second pays the two fixed-row scalar products per input column described in C7. The $u$ rows in Amendment n are deterministic public coefficients outside the uniform SIS instance.

## Amendment I3

The amended (I3) is
\[
\Lambda_1\ge 2\sqrt3 R_{\rm tr}\sqrt N_\star,\qquad
\Lambda_2\ge \sqrt2\,\pi R_{\rm tr}^2 N_\star,\qquad
\Lambda_3\ge \frac{20\,\pi R_{\rm tr}^3 N_\star\sqrt N_\star}{9\sqrt2} .
\]
The rank-two and rank-three geometric lower bounds change. All three inequalities here are checked by the parameter model.

### Which inverse-theorem steps use the change

In `blob:admissibility`, (P3) refers to these inverse conditions, and the bounds in (P1), (P2), (P4) and (P5) have no occurrence of a geometric factor $\Lambda_d$. The box, saturation, reduction, fiber and height definitions in `blob:lattices` use the same lattice operations. The regularity test uses $m(\Theta)h(\Theta)\le\Gamma_d/g^d$, and has the same definition. In `blob:trimming` the ellipsoid depends on $R_{\rm tr}$, $g$, and the basis through $\Sigma_\Theta$, with no $\Lambda_d$. The proof of `lem:prefix` uses only the lattice indices and ceiling count in (a)–(b), and (I1), (I2), (I4) to convert the rank-three ceiling count to the height and regularity in (c). The proof of `lem:trim` applies the exponential moment bound for independent box variables, then the exponential loss inequality in (I2). Thus the prefix and trimming lemmas have the same hypotheses and arguments. We prove `lem:sparse`, `lem:regularize`, and `lem:inverse` under the amended condition below.

### Integer-lattice facts used below

For an integral basis $B$ with a largest row minor on $J$, each component of $y\in\operatorname{span}_{\mathbb R}B$ is $B_iB_J^{-1}y_J$, with entries of the row $B_iB_J^{-1}$ bounded by one in absolute value by Cramer's rule and maximality of the minor. The component is therefore at most $\|y_J\|_1$ in absolute value. When the columns of $B$ generate a saturated integer lattice, their quotient in the ambient free integer group is torsion-free and finitely generated, hence free. Extending these columns by lifts of a quotient basis gives a unimodular basis of the ambient group. Taking its transpose shows $B^\top\mathbb Z^I=\mathbb Z^d$.

For the lifting fact, let $\Delta$ be an integer matrix of rank $k'>0$ with a nonzero minor $M$ of order $k'$ on rows $I_0$ and columns $J_0$. Put $\delta=\det M$. Assume $\delta\ne0\bmod q$, so $M$ is invertible modulo the prime $q$. Given $c^\top\Delta=0\bmod q$, write $I_1$ for the remaining rows and choose an integer vector $w\equiv\delta^{-1}c_{I_1}\bmod q$. Set $u_{I_1}=\delta w$ and $u_{I_0}^\top=-w^\top\Delta_{I_1,J_0}\operatorname{adj}M$. Then $u^\top\Delta_{J_0}=0$ by the adjugate identity. Those columns span the column space over $\mathbb Q$, so $u^\top\Delta=0$. The inside rows also agree with $c$ modulo $q$, by uniqueness of the solution for them using $M$ invertible modulo $q$. For rank zero take $u=c$. These facts use no inverse-parameter condition other than the nonzero modular minor at the lifting step.

### Prefix estimates

Here are the unchanged parts of the prefix lemma on the amended parameter domain. Let $\Theta$ be a saturated lattice of rank $d$, with integral basis matrix $B$ and a largest minor on $J$. Order its coordinates with $J$ first, let $I_k$ be the first $k$ coordinates, and let $\Theta_k=\operatorname{span}_{\mathbb R}(B_{I_k})\cap\mathbb Z^{I_k}$, $k\ge d$. Let $h_k,m_k$ be its height and largest fiber density. Its rank is $d$ because the selected minor remains invertible. If $Y$ is a basis of $\Theta_k$, then $B_{I_k}=Y C$ for an integral nonsingular $d$-square matrix $C$. The fibers of the prefix are thus the level sets of $B_{I_k}^{\top}r$. The group $G_k=B_{I_k}^{\top}\mathbb Z^{I_k}=C^\top\mathbb Z^d$, by saturation and the integer-lattice lemma (b), has index $|\det C|$ in $\mathbb Z^d$. The $d$-row determinants of $B_{I_k}$ are multiplied from those of $Y$ by $\det C$. As their largest absolute value is the original $h(\Theta)$, this gives $h_k [\mathbb Z^d:G_k]=h(\Theta)$ and shows that $J$ is still a largest minor for $\Theta_k$. At $k=d$, the column span is all of $\mathbb R^J$, so $\Theta_d=\mathbb Z^J$, $h_d=1$ and $m_d=g^{-d}$. At the full set of coordinates the saturated lattice is $\Theta$.

On adding the next row to $B_{I_k}$, let $s_k$ be the order of that row as a column in the quotient $\mathbb Z^d/G_k$. Adjoining it multiplies the size of the subgroup modulo $G_k$ by $s_k$, so $h_{k+1}=s_k h_k$ by the index identity. For a fixed value of $B_{I_{k+1}}^\top r$, the new coordinate is in at most one residue class modulo $s_k$; its allowed values in an interval of $g$ integers number at most $\lceil g/s_k\rceil$. For each such value the remaining prefix has fiber density at most $m_k$. Consequently $m_{k+1}\le m_k\lceil g/s_k\rceil/g$. If $s_k\ge g$ this also makes the new coordinate constant on the fiber. If $s_k=1$, the power inequality $m_{k+1}^b h_{k+1}^{b-1}\le m_k^b h_k^{b-1}$ is immediate. For $2\le s=s_k<g$, use $\lceil g/s\rceil/g\le 1/s+1/g\le s^{-1+1/b}$. To verify the second inequality, if $s\ge2^b$ then $1/s+1/g<2/s\le s^{-1+1/b}$. Otherwise $g\ge2^b$ and the concave function $x^{1/b}-1-x/2^b$ is nonnegative on $[2,2^b]$: it is zero at $2^b$, and at $2$ it is at least $(\log 2)/b-2^{1-b}>0$ for $b\ge7$. The last strict inequality follows from $\log 2>1/2$ and $2^{b-2}>b$ for integers $b\ge7$. This proves the power inequality in all its cases.


### Rank-three height and regularity

This subsection uses the rank-three growth and range conditions in Amendment I4.

Let $\Theta$ be a rank-three saturated lattice on a set of at most $N_\star$ coordinates with $m(\Theta)\ge\mu_{\rm tr}$. Apply the preceding prefix estimates with a largest minor of size three ordered first. At the first rank-three prefix the height is 1 and density $g^{-3}$. Write $s_1,\ldots,s_a$ for the nontrivial step orders (at least 2), in the original prefix order. The height and density are bounded by
\[
   h(\Theta)=\prod_{i=1}^a s_i,\qquad
   m(\Theta)\le g^{-3}F,\qquad
   F=\prod_{i=1}^a\frac{\lceil g/s_i\rceil}{g}.
\]
Every factor of $F$ is at most 1. Empty products are 1.

We prove $h(\Theta)\le H_3$. Let $h=h(\Theta)$. Expanding $\prod_i(1/s_i+1/g)$, the term without $1/g$ is $1/h$; since $1/s_i\le1/2$, all the other terms sum to at most $(1/2+1/g)^a-(1/2)^a$. This difference is 0 if $a=0$. Otherwise the mean-value inequality bounds it by $a(1/2+1/g)^{a-1}/g\le (1+2/g)/g$. Indeed the numerator for $a=1$ is 1, at $a=2$ it is $1+2/g$, and for $a\ge2$ the ratio at successive $a$ is $(1+1/a)(1/2+1/g)<1$ because $g\ge128$. Since $\lceil g/s_i\rceil/g\le1/s_i+1/g$, we have
\[
 m(\Theta)\le g^{-3}\xi_{\rm tr}(1/h+1/g).
\]
This proves $h\le H_*$ from Amendment H3. The additional integer height bound proved there gives $h\le H_3$.

Multiplying the same density bound by $h$ and using $h\le H_3$ gives $m(\Theta)h\le g^{-3}\xi_{\rm tr}(1+H_3/g)\le g^{-3}\Gamma_3$ by (I4). This is the required rank-three regularity.

### Trimming estimate

For the trimming lemma, a centered uniform box entry can be added to a uniform independent variable on $[-1/2,1/2]$ to get the continuous uniform variable on $[-g/2,g/2]$. The added variable's moment generating function is at least one by convexity, so the centered box entry has moment generating function bounded by $\sinh(x)/x$ with $x=tg/2$ at argument $t$. Its series is bounded by $e^{x^2/6}$ because $(2j+1)!\ge6^j j!$ for $j\ge0$, by induction on $j$. Let $Y=B^\top r-\mathbb E[B^\top r]$ and $\Sigma=(g^2/12)B^\top B$. Independence of the box entries gives $\mathbb E e^{u^\top Y}\le e^{u^\top\Sigma u/2}$. With $Z$ an independent standard $d$-dimensional Gaussian, the Gaussian moment generating function gives
\[
 \mathbb E e^{(99/200)\|\Sigma^{-1/2}Y\|_2^2}
 =\mathbb E e^{\sqrt{99/100}\,Z^\top\Sigma^{-1/2}Y}
 \le \mathbb E e^{(99/200)\|Z\|_2^2}=10^d .
\]
The inequality conditions on $Z$; the last equality follows by scaling each normal density in the integral. By Markov's inequality the probability of being outside the trimming ellipsoid is at most $10^d e^{-99R_{\rm tr}^2/200}\le\varepsilon_{\rm tr}$ by (I2) and $d\le3$. Trimming any subset removes at most that absolute density. This establishes the trimming conclusion without a norm assumption.


### Projected fiber counts

The claim of `lem:sparse` is as follows. Let $B$ be a basis of an integral lattice $\Theta$ on $I\subseteq[N_\star]$, of rank $d\in[3]$. Take $i'\in[N_\star]\setminus I$. Let $F\ne\varnothing$ be a set in the box on $I\cup\{i'\}$ trimmed by $\Theta$, and $\Phi(r)=(B^\top r_I,r_{i'})$. If (a) $\Phi(F)$ has affine dimension $d+1$ and lies in a coset of an index-$q$ subgroup of $\mathbb{Z}^{d+1}$, then
$\Pr[F]\le\Lambda_d g^d h(\Theta)m(\Theta)/q$.
If (b) $F^\perp$ has rank $d'$ with $1\le d'<d$, a largest minor on $J\subseteq I$, and every vector of $F^\perp$ restricts to a vector in $\operatorname{span}_{\mathbb R}\Theta$ on $I$, then
$\Pr[F]h(F^\perp)\le\Lambda_{d-d'}\,g^{d-d'}h(\Theta)m(\Theta)$.
Here $F^\perp$ is the lattice of integer vectors normal to the differences in $F$.

For each possible image $(y,x)$, the probability of $B^\top r_I=y,r_{i'}=x$ is at most $m(\Theta)/g$ by independence, so $\Pr[F]\le|\Phi(F)|m(\Theta)/g$. We count images in $C=\mathcal{T}_\Theta\times[2,g+1]$.

For (a), put $s=d+1$, $\delta=q$, $J=\varnothing$, and let $p$ be the identity. Write $B=(B_1,B_2)$ with $B_1$ empty, and use $|\det(B_1)_J|=1$.
For (b), put $s=d+1-d'$ and let $Y$ be an integral basis matrix of $F^\perp$; $Y_J$ is invertible. The submatrix $B_J$ has row rank $d'$ since the columns $Y_J$ lie in its real column span. The integral kernel of $B_J$ is saturated in $\mathbb{Z}^d$, of rank $d-d'$. It has a basis that extends to an integral basis of $\mathbb{Z}^d$: the quotient by a saturated subgroup of $\mathbb{Z}^d$ is finitely generated and torsion-free, hence free, and lifts of a quotient basis give the extension. Using this basis change, write $B=(B_1,B_2)$ where $(B_2)_J=0$ and $(B_1)_J$ is invertible square. The columns of $B_2$ number $s-1$. Trimming is basis independent since the mean and covariance transform by the same invertible change on the image coordinates.

In case (b), the injective map $a=(a_{[d]},a_{d+1})\mapsto(Ba_{[d]},a_{d+1})$ maps the real annihilator of the differences of $\Phi(F)$ isomorphically onto the real annihilator of the differences of $F$, by the restriction assumption. The first annihilator has dimension $d'$ and its integer points form a saturated lattice with basis matrix $V$. The real annihilator of differences of $F$ is spanned by its integer points because those differences are integer vectors, so the restriction premise on integer normals suffices for this isomorphism. Split its rows into $V_1,V_2,V_3$ of lengths $d',s-1,1$. The image of its basis is $Y A$ for an integral nonsingular $d'$-square matrix $A$, as its columns are integral independent normals. At rows $J$, this gives
\[
(B_1)_J V_1=Y_J A .
\]
Consequently $V_1$ is invertible and $|\det(B_1)_J|\,\delta\ge h(F^\perp)$, where $\delta=|\det V_1|$. Write $y=(y_1,y_2)$ according to the basis split. Projection $p:(y,x)\mapsto(y_2,x)$ is injective on any affine translate of the kernel of $V^\top$, because there the first block of a difference is determined by $V_1^\top$. It therefore preserves the affine dimension of $\Phi(F)$, which is $s$. The projections of differences of image points lie in the kernel of
\[
 (y_2,x)\longmapsto V_2^\top y_2 + x V_3^\top
          \pmod{V_1^\top\mathbb{Z}^{d'}} .
\]
The map is onto because $V^\top \mathbb{Z}^{d+1}=\mathbb{Z}^{d'}$ by saturation and `lem:lattice-facts` (b), while the $y_1$ contribution vanishes in the quotient. The kernel has index $\delta$ in $\mathbb{Z}^s$. Thus in both cases $p(\Phi(F))$ has full affine dimension $s$, cardinality $|\Phi(F)|$, and lies in $p(C)$ and in a coset of an index-$\delta$ lattice.

A full-dimensional finite set $X$ of $m$ points in such a coset has $\operatorname{vol}_s\operatorname{conv}(X)\ge(m-s)\delta/s!$. To see this, start from any $s+1$ affinely independent points forming a simplex. One can add the points successively while maintaining a triangulation of their hull using all inserted points as vertices. For a point outside the hull, each boundary facet simplex strictly visible to the point gives a new simplex by coning it to the point. Those simplices have disjoint interiors and fill the new region, as rays from the point first hit the old hull in its visible boundary. At least one facet is strictly visible, so at least one full simplex is added. If a point is in the hull, take the unique smallest face of the triangulation containing it. This face has positive dimension since the point is distinct from all earlier vertices. Subdivide that face by coning its boundary faces to the point and make the corresponding subdivision of every full simplex incident to it, by adjoining the complementary simplex vertices. This covers exactly those full simplices and replaces each by at least two, since the point lies in the relative interior of the face. Hence there are at least $m-s$ full simplices. Each has volume at least $\delta/s!$, since the determinant of $s$ independent differences of coset points is a nonzero integer multiple of the determinant $\delta$ of its lattice. Since $m\ge s+1$, the region containing $X$, if convex, has volume at least $\delta/s!$. In particular, applying both consequences to $p(C)$ gives
\[
 |\Phi(F)|\le s!\operatorname{vol}_s p(C)/\delta+s
             \le (s+1)!\operatorname{vol}_s p(C)/\delta .
\]

The projection of the ellipsoid $\mathcal{T}_\Theta$ to the last $s-1$ coordinates has volume $v_{s-1}R_{\rm tr}^{s-1}(g/\sqrt{12})^{s-1}\sqrt{\det(B_2^\top B_2)}$, where $v_j$ is the volume of the Euclidean unit $j$-ball. Indeed, write the ellipsoid as the image of a unit ball by $R_{\rm tr}\Sigma_\Theta^{1/2}$ plus the center. The projected map has a Gram matrix on its range equal to the bottom-right block $R_{\rm tr}^2(g^2/12)B_2^\top B_2$, which gives the product of its nonzero singular values. The interval in $p(C)$ has length $g-1$. In either case $(B_2)_J=0$. By expansion of $\det(B_2^\top B_2)$ into squared row minors, and because $|\det(B_1)_J\det(B_2)_{J'}|=|\det B_{J\cup J'}|\le h(\Theta)$ for each $J'\subseteq I\setminus J$ of size $s-1$,
\[
 |\det(B_1)_J| \sqrt{\det(B_2^\top B_2)}
 \le h(\Theta)\sqrt{\binom{N_\star}{s-1}} .
\]
Combining with the counting bound and $\Pr[F]\le |\Phi(F)|m(\Theta)/g$ gives
\[
 \Pr[F]|\det(B_1)_J|\delta
 \le g^{j}h(\Theta)m(\Theta)
      (j+2)!v_j R_{\rm tr}^{j}\sqrt{\binom{N_\star}{j}/12^j},
 \qquad j=s-1 .
\]
Use $\binom{N_\star}{j}\le N_\star^j/j!$ and $v_1=2,v_2=\pi,v_3=4\pi/3$. The three upper bounds on the geometric factor are $2\sqrt3 R_{\rm tr}\sqrt N_\star$, $\sqrt2\pi R_{\rm tr}^2N_\star$, and $20\pi R_{\rm tr}^3N_\star^{3/2}/(9\sqrt2)$. They are at most the three allowed $\Lambda_j$. In case (a), divide by $q$ to obtain the claim. In (b), replace $|\det(B_1)_J|\delta$ by $h(F^\perp)$ on the left to obtain the claim.

### Regularization with the new count

This subsection proves regularization under the growth conditions in Amendment I4.

The claim of `lem:regularize` is that a saturated lattice $\Theta$ on $I\subseteq[N_\star]$ of rank $d\in[3]$ with $m(\Theta)\ge\mu_{\rm tr}+(3-d)\varepsilon_{\rm tr}$ is contained in a regular saturated lattice of rank in $[d,3]$ and maximum fiber density at least $m(\Theta)-(3-d)\varepsilon_{\rm tr}$.

Write $\mu=\mu_{\rm tr}$ and $e=\varepsilon_{\rm tr}$ in this paragraph and the next two. Induct downwards on rank for all such $I$ simultaneously. Each recursive normal and its regular extension use the same prefix coordinates. An extension is only to the next coordinate of $I$. For $d=3$, `lem:prefix` (c) gives regularity directly. For $d\le2$, use `lem:prefix` with a largest minor at $J$ and $J$ first in the coordinate order. Denote the prefixes by $\Theta_k$, their heights and max densities by $h_k,m_k$, and the step order by $s_k$. The densities are nonincreasing, so each is at least $\mu+(3-d)e$. Take a densest fiber of $\Theta_k$ to form $F_k$. If the preceding $F_{k-1}^\perp$ strictly contains $\Theta_{k-1}$, trim this fiber by the regular containing lattice $\widetilde\Theta_{k-1}$ specified below. Otherwise leave the fiber whole. The density of each $F_k$ is at least $m_k-e$ by `lem:trim`. Its normal lattice contains $\Theta_k$. If this inclusion is strict, saturation gives a rank $d_k>d$. Its rank is at most three since a fiber of a rank-$a$ lattice has density at most $g^{-a}$ by fixing coordinates outside an invertible $a$-row minor, and $g^{-4}<\mu\le m_k-(3-d)e$ by (I5). Its max fiber density is at least $\Pr[F_k]\ge\mu+(2-d)e\ge\mu+(3-d_k)e$. By induction let $\widetilde\Theta_k$ be a regular saturated containing lattice of rank at least $d_k$, with $m(\widetilde\Theta_k)\ge m(F_k^\perp)-(3-d_k)e\ge m_k-(3-d)e$. This constructs the trimming lattice for the next step, and if $F_{|I|}^\perp\ne\Theta$ it gives the desired final lattice.

If $F_{|I|}^\perp=\Theta$, let $j<|I|$ be the last strict index, or $j=d-1$ when there is none. For $j<k<|I|$ the step order $s_k$ is below $g$. Otherwise `lem:prefix` (b) would make the new coordinate constant in the fiber of $\Theta_{k+1}$ containing $F_{k+1}$; its unit vector would then be in $F_{k+1}^\perp=\Theta_{k+1}$ and vanish at $J$, forbidden by `lem:lattice-facts` (a). Iterating the power inequality in `lem:prefix` (b) gives
\[
 \mu(m(\Theta)h(\Theta))^{b-1}
 \le m(\Theta)^b h(\Theta)^{b-1}
 \le m_{j+1}^{b}h_{j+1}^{b-1}.
\]
When $j=d-1$, $m_d=g^{-d}, h_d=1$. The bound on $\Gamma_d^{b-1}$ in (I4) gives $m_d^{b}h_d^{b-1}\le\mu(\Gamma_d/g^d)^{b-1}$.

When $j\ge d$, let $\tilde d$ be the rank of $\widetilde\Theta_j$. The set $F_{j+1}$ was trimmed by this lattice. Its normal lattice is exactly $\Theta_{j+1}$, of rank $d<\tilde d$, and with largest minor on $J$ by `lem:prefix` (a). Restrictions to the first $j$ coordinates lie in the span of $\Theta_j$ by the definition of the prefix lattice, hence in the span of $\widetilde\Theta_j$. Apply the proved projected count (b). Since $\Pr[F_{j+1}]\ge m_{j+1}-e\ge m_{j+1}/A_{\rm inv}$ by (I4) and $m_{j+1}\ge\mu$, regularity gives
\[
 m_{j+1}h_{j+1}\le A_{\rm inv}\Lambda_{\tilde d-d}\Gamma_{\tilde d}/g^d .
\]
Also $m_{j+1}\le m_j\le\Pr[F_j]+e\le g^{-d-1}+e\le\mu P_d^{b-1}$ by the rank of $F_j^\perp$ and (I4). For $d=1$, (I4) allows $2e$ in the numerator and therefore implies the same inequality. In all three rank pairs $(d,\tilde d)\in\{(1,2),(1,3),(2,3)\}$, the last growth inequalities of (I4) imply $A_{\rm inv}\Lambda_{\tilde d-d}\Gamma_{\tilde d}P_d\le\Gamma_d$. Multiplying yields $m_{j+1}^b h_{j+1}^{b-1}\le\mu(\Gamma_d/g^d)^{b-1}$. Now $b>1$ and $\mu>0$ give $m(\Theta)h(\Theta)\le\Gamma_d/g^d$. This proves regularity and finishes the induction.

The inverse theorem under this (I3) is proved in full in the Amended inverse theorem subsection of Amendment I6. It uses the prefix, trimming, projection and regularization estimates in this section. The resulting height and norm conclusions use the geometric factors proved sufficient here.

## Amendment I4

Require $g^2\le2^{40}\cdot2^\lambda$ and the conjunction
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
The displayed conditions keep the rank-one, rank-two and rank-three growth bounds. The additional upper range constraint gives $\sqrt g\le 2^{10}2^{\lambda/4}$, so the expected $O(\sqrt g\,N_\star^{1/4})$ group work is $O(2^{\lambda/4}N_\star^{1/4})$ for the common efficiency derivation.

The admissibility condition (P3) uses these inequalities together. The prefix and trimming proofs in I3 continue to apply: the upper range condition removes parameter choices and is not used in their estimates. The sparse projection count depends on the basis, covariance and fiber density. The regularization proof in I3 uses the displayed lower bounds on $\Gamma_1,\Gamma_2,\Gamma_3,A_{\rm inv},P_1,P_2$, with the rank-three height bound of H3. The inverse theorem in I6 applies these facts to the modular fibers and gives the stated short-multiple conclusion. For the rank-two height it uses the unchanged definition $H_2=\Gamma_2/(g^2\mu_{\rm tr})$: regularity gives $m(\Theta)h(\Theta)\le\Gamma_2/g^2$, and $m(\Theta)\ge\mu_{\rm tr}$ gives the claimed height upper bound. The inverse theorem at the original infinity radius uses these heights. Amendment msis_bound uses the normal lattices to prove the Euclidean output guarantee for the actual challenge of Amendment msis_norm.

## Amendment H3

Let
\[
 H_*=\frac{\xi_{\rm tr}}{g^3\mu_{\rm tr}-\xi_{\rm tr}/g},\quad
 A_g=(1+1/\sqrt g)^{255},\quad B_g=(1+1/\sqrt g)^{256},\quad M=g^4\mu_{\rm tr},
\]
and set $j=\max\{1,\lceil M/A_g\rceil-1\}$ and $s=\lceil\max\{0,B_g-M\}\rceil$. The amended definition is
\[
 H_3=\min\{H_*,\lceil g/j\rceil-1+s H_*\}.
\]
The protected (I2) ensures that the denominator of $H_*$ is positive. If $M\le A_g$, then $B_g>A_g$ gives $s\ge1$ and the amended expression equals $H_*$. If $M>A_g$, then $j$ is the largest integer strictly below $M/A_g$, so $M>jA_g$, including at integral ratios.

Let $\Theta$ be a saturated rank-three lattice with maximum fiber density $m(\Theta)\ge\mu_{\rm tr}$. The prefix count in Amendment I3 gives $h=\prod_i s_i$, $m(\Theta)\le g^{-3}F$, and $F=\prod_i \lceil g/s_i\rceil/g$ on the list of nontrivial step orders $s_i\ge2$. The expansion bound there already gives $h\le H_*$. We now show $h<g/j$ whenever $M>A_g$.

Assume $h\ge g/j$. An order $s_i\le\sqrt g$ has $\lceil g/s_i\rceil/g\le(1+g^{-1/2})/s_i$. If all orders have this property, keep only the shortest initial list of orders with product at least $g/j$, taking the empty list when $g/j\le1$. Its length is at most 255 because each order is at least two and the product preceding the last order is less than $g/j\le g<2^{254}$ by (I1). The discarded factors in $F$ are at most one. The resulting bound is $g F\le jA_g$.

If at least two orders exceed $\sqrt g$, their two factors in $F$ are at most $g^{-1/2}+g^{-1}$ each. Keeping just those factors gives $gF\le(1+g^{-1/2})^2\le jA_g$. In the remaining case let $s_*$ be the unique order exceeding $\sqrt g$, $a=\lceil g/s_*\rceil$, and $P$ the product of the other orders. The assumption implies $jP\ge g/s_*$, hence $jP\ge a$ because $jP$ is integral. From the other orders retain the shortest initial list of product at least $a/j$, taking it empty when $a/j\le1$. Its length is at most 255 by the same preceding-product bound, since $a\le g$. Its factors have product at most $A_gj/a$. Multiplying by the $a/g$ factor for $s_*$ and discarding the rest gives $gF\le jA_g$ also in this case.

All three cases contradict $M\le g^4m(\Theta)\le gF\le jA_g<M$. Hence $h\le\lceil g/j\rceil-1$ for $M>A_g$. Combining with the old continuous bound and the nonnegative term $sH_*$ gives $h\le H_3$ on the whole amended domain.

For the rank-three regularity argument of the prefix lemma, the same expansion gives $m(\Theta)h\le g^{-3}\xi_{\rm tr}(1+h/g)$, which is at most $g^{-3}\Gamma_3$ by the unchanged $\Gamma_3$ inequality in (I4), evaluated at the amended $H_3$. The integer-box and normal-lattice definitions are independent of the height bound. The prefix rank-one and rank-two estimates use just the exact step index and the ceiling inequality. The trimming moment calculation in I3 uses the sampling distribution and the truncation radius, with no dependence on $H_3$. The sparse projection count uses each lattice's actual height, and the regularization proof uses the proved rank-three regularity and other inequalities of (I4), which still hold. In the proof of the inverse theorem in Amendment I6, the minor cutoff in (I5) now applies with this upper bound on every regular rank-three lattice under consideration. The terminal Minkowski comparison uses its integer floor and the checked inequality in (I6). This height controls the retained infinity-radius inverse theorem and the mass-covolume estimate used by Amendment msis_bound. Amendment msis_norm specifies the Euclidean norm of the costed challenge.

## Amendment I6

Replace (I6) by the conjunction
\[
 2\beta<q,\quad H_1\le\beta,\quad
 4H_2q\le3\beta^2,\quad 2509\lfloor H_3\rfloor q^2\le1000\beta^3.
\]
The inverse proof uses amended (I3), (I4) and H3. The height definitions H1 and H2 and conditions (I1), (I2) and (I5) retain their meanings.

### Dependence on the inverse conditions

In `blob:admissibility`, (P3) now requires the inverse-theorem conditions with the displayed (I6). The other admissibility conditions are identical, including (P4). The boxes, fibers, densities, saturation, height, and regularity in `blob:lattices` depend on the box, the basis, the field and the $\Gamma_d$, with no dependence on $\beta$. The ellipsoid of `blob:trimming` uses only $g,R_{\mathrm{tr}}$ and the basis. The following lemmas retain their contracts and arguments.

- In `lem:prefix`, the prefix saturation, indices, and fiber count use the integral basis and $g$. The estimate for a step of index below $g$ uses (I1), and the rank-three height and regularity use (I2) and (I4). They involve no short-vector bound.
- In `lem:trim`, the moment-generating-function bound for the independent uniform entries is applied to a linear image of the box and then Markov's inequality is applied with the threshold $R_{\mathrm{tr}}^2$. The loss condition used is precisely the exponential inequality in (I2).
- In `lem:sparse`, a trimming ellipsoid is projected along the normal constraints and lattice points in the projection are bounded by its volume and the lattice index. The conversion of the volume estimate to the constants uses (I3). The new (I6) is absent from both estimates and their proofs. The sharper geometric constant from the separate (I3) amendment is proved in that section.
- In `lem:regularize`, the downward induction uses the trimming loss, the prefix lattice inequalities, and the projected density–height bound. Promotion can only reach rank three by the inequality $g^{-4}<\mu_{\mathrm{tr}}$ from (I5). The growth bounds in (I4) suffice for the final prefix. Neither a bound on a short multiple nor (I6) enters the induction.

The prefix estimates, trimming, sparse projection, and regularization used below are proved in I3, and the rank-three height bound is proved in H3. A saturated lattice of rank one or two with density at least the threshold has the respective unchanged height bound from regularity, as explained in I4.

### Volume of the terminal coordinate body

For $d=2,3$ let $a_1,\ldots,a_M$ be the rows of $BB_J^{-1}$, where $J$ is a largest $d$-row minor. These include all standard unit vectors. Every $d$-row determinant has absolute value at most 1, since it is an original minor divided by the chosen largest minor. Define the compact, centrally symmetric body
\[
 K=\{x\in\mathbb R^d:\ |a_i^\top x|\le1\text{ for every }i\}.
\]
It has the origin in its interior since the list is finite. We prove the respective volume lower bounds needed for the amended terminal norm.

#### Planar bound

Let $C=\operatorname{conv}\{\pm a_i\}$. This is the polar of $K$, since the inequalities for the vertices give those for every convex combination, and separation gives the converse. Determinant bilinearity implies $|\det(a,b)|\le1$ for all $a,b\in C$. Rotate by $\pi/2$ using $J$. Then $|a\cdot Jb|\le1$ for every $a\in C$ and $b\in C$, so $JC\subseteq K$.

Define $\|x\|_K=\inf\{s>0:x\in sK\}$. This is a norm because $K$ is bounded, centrally symmetric, convex and contains the origin in its interior. For the triangle inequality, if $x\in sK$ and $y\in tK$, then $(x+y)/(s+t)$ is a convex combination of $x/s$ and $y/t$; pass to the infimum. The polygon $K$ has a counterclockwise boundary with finitely many edges. On each edge with initial point $p$ and directed edge vector $v$, choose its outward normal $a$ scaled so that $a\cdot p=1$. Such scaling is positive since the origin is interior. As $a\cdot x\le1$ on $K$, we have $a\in C$. The counterclockwise orientation gives $v=tJa$ for $t>0$. Hence $\|v\|_K\le t$, and $\det(p,v)=t(a\cdot p)=t$. Joining the origin to the polygon's vertices divides it into triangles, so $2\operatorname{vol}_2 K=\sum_{\rm edges}\det(p,v)\ge\sum_{\rm edges}\|v\|_K$.

To lower bound this last sum, choose any $x\in\partial K$ and traverse the boundary counterclockwise from $x$ to $-x$. The continuous function $y\mapsto\|y-x\|_K$ goes from zero to two, so some intermediate $y$ satisfies $\|y-x\|_K=1$. The radial direction of each boundary point is unique since the origin is interior, so $y$ is not collinear with $x$. The six boundary points
\[
 x,\ y,\ y-x,\ -x,\ -y,\ x-y
\]
occur in this cyclic order: the direction of $y-x$ is strictly between those of $y$ and $-x$, as a positive sum of these vectors, and the other half is obtained by negation. The successive chord vectors are $y-x,-x,-y,x-y,x,y$, each of norm one. Split the boundary path at these six points. Splitting an edge does not change its norm-length by homogeneity on that ray, and the triangle inequality shows the length of each of the six resulting arcs is at least the length of its chord. Thus $\sum_{\rm edges}\|v\|_K\ge6$, and $\operatorname{vol}_2 K\ge3$. This proof uses only the finite strip description and the normalized determinants.

#### Three-dimensional bound

Maximize $\det A$ among positive semidefinite symmetric matrices with $a_i^\top A a_i\le1$ for every $i$. The domain is compact: the standard unit constraints bound all diagonal entries and positive semidefiniteness bounds each off-diagonal entry by the geometric mean of its two corresponding diagonal entries. A small positive multiple of the identity is feasible, so a maximizing $A$ is positive definite. Put $u_i=A^{1/2}a_i$, and call an index active when $\|u_i\|_2=1$. The identity lies in the cone generated by $u_i u_i^\top$ at the active indices. To prove this, the cone is closed since every generator has trace 1, so bounded traces bound the coefficients in any sequence of nonnegative combinations. If $C_0$ is the nearest cone point to $I$ in the trace inner product and $S=I-C_0$, the minimizing property gives $\langle S,X-C_0\rangle\le0$ for every cone point $X$. Test $X=0,2C_0$ to see $\langle S,C_0\rangle=0$. If $S\ne0$, then $\operatorname{tr}S=\|S\|_{\rm F}^2>0$ and $u_i^\top S u_i\le0$ for all active constraints. For small $t>0$, $A^{1/2}(I+tS)A^{1/2}$ remains feasible by those inequalities and the strict slack of all inactive constraints. Its determinant increases because $\det(I+tS)=1+t\operatorname{tr}S+O(t^2)$, a contradiction.

### A fourth-moment bound for the transformed determinants

Write $I=\sum_i w_i u_i u_i^\top$ with positive weights on active indices. Their sum is 3 by taking traces. Draw independent unit vectors $X,Y,Z$ from the active list with probabilities $w_i/3$, so $\mathbb E XX^\top=I/3$. Put $a=\sqrt{\det A}$ and $D_*=(\det(X,Y,Z))^2$. Every determinant of three transformed rows has absolute value at most $a$, by the normalized determinant bound before applying $A^{1/2}$. Thus $0\le D_*\le a^2$ for every outcome, including repeated rows.

Let $p=X\cdot Y$, $r=Y\cdot Z$, and $s=Z\cdot X$. By expanding the three-dimensional Gram determinant,
\[
 D_*=1-p^2-r^2-s^2+2prs .
\]
Isotropy gives $\mathbb E p^2=1/3$, $\mathbb E p^2r^2=1/9$ by conditioning on $Y$, and $\mathbb E prs=1/9$ by conditioning on $X,Y$, because $\mathbb E[rs\mid X,Y]=p/3$. The same conditioning gives $\mathbb E[p^3rs]=\mathbb E[p^4]/3$. The cycle permutations have the same expectations. Thus $\mathbb E D_*=2/9$. To compute its second moment, put $M=\mathbb E p^4$ and $T=\mathbb E p^2r^2s^2$. Squaring the displayed Gram formula and substituting the computed expectations gives
\[
 \mathbb E D_*^2=1-2+3M+\frac{6}{9}+\frac49-4M+4T
 =\frac19-M+4T .
\]

On the real vector space of symmetric three-by-three matrices with inner product $\langle B,C\rangle=\operatorname{tr}(BC)$, define the positive semidefinite operator $L(B)=\mathbb E[\langle XX^\top,B\rangle XX^\top]$. The trace of an outer product operator of a vector with itself equals its squared norm, so $\operatorname{tr} L=\mathbb E\|XX^\top\|_{\rm F}^2=1$. The identity matrix is an eigenvector with eigenvalue $1/3$, and its orthogonal complement has five nonnegative eigenvalues $\lambda_1,\ldots,\lambda_5$ summing to $2/3$. The trace of a product of two outer products is the square of their inner product. For three it is the product of their three cyclic inner products, by direct multiplication of the rank-one operators. Applying these identities to independent samples, whose inner products on this matrix space are squared dot products, gives $M=\operatorname{tr} L^2$ and $T=\operatorname{tr} L^3$. Therefore
\[
 \mathbb E D_*^2=\frac4{27}+\sum_{i=1}^5 (4\lambda_i^3-\lambda_i^2).
\]
Let $f(t)=4t^3-t^2$ and $m=2/15$. For each $t\ge0$, the exact identity
\[
 f(t)-f(m)-f'(m)(t-m)=(t-m)^2(4t+8m-1)\ge0
\]
holds because $8m-1=1/15$. Summing cancels the linear term and gives $\mathbb E D_*^2\ge4/27+5f(m)=8/75$. Since $D_*^2\le a^2D_*$ pointwise, we conclude
\[
 a^2\ge\frac{8/75}{2/9}=\frac{12}{25}.
\]

### A section estimate for the three-dimensional body

Set $K'=A^{-1/2}K$. It contains the unit ball since $\|u_i\|_2\le1$ for all rows. Choose an active unit vector $u=u_i$ and let $\tilde u_j$ be the projection of $u_j$ to $u^\perp$. Use oriented orthonormal coordinates in this plane with unit normal $u$. Then
\[
 |\det_2(\tilde u_j,\tilde u_k)|=|\det_3(u,u_j,u_k)|\le a ,
 \qquad a=\sqrt{\det A},
\]
by the normalized three-row determinants and the transformation $A^{1/2}$. The central section of $K'$ in this plane is described by the inequalities $|\tilde u_j\cdot x|\le1$. Scaling the row vectors by $1/\sqrt a$ divides each planar determinant by $a$, and scales the planar body by $\sqrt a$. That body is a bounded planar strip intersection with interior. The planar proof above used only these properties, central symmetry, and the determinant bound. Consequently
\[
 \operatorname{area}(K'\cap u^\perp)\ge 3/a .
\]

For completeness, for two compact convex planar sets of positive area the square root of area of their Minkowski combination with weights $1-t,t$ is at least the same combination of the square roots of their areas. To prove it, first normalize both sets to area one. The vertical slice widths $f,g$ are positive and continuous in the interiors of their respective first-coordinate intervals. Let $x_f(s),x_g(s)$ for $0<s<1$ be the inverse functions of their integrals from the left endpoints. Their derivatives are $1/f(x_f(s))$ and $1/g(x_g(s))$. At the interpolated first coordinate $(1-t)x_f(s)+t x_g(s)$, the slice of the combination contains the corresponding combination of the two interval slices. Its length is at least $(1-t)f(x_f(s))+t g(x_g(s))$. After changing variables by the strictly increasing interpolated first coordinate, the area is at least the integral over $0<s<1$ of
\[
 \big((1-t)f+t g\big)\big((1-t)/f+t/g\big)\ge1 ,
\]
where the inequality follows from $f/g+g/f\ge2$. The change of variables holds first on compact subintervals of $(0,1)$, and their integrals increase to the stated lower bound. For arbitrary positive areas let their square roots be $r_1,r_2$. Apply the area-one result to the sets scaled by $1/r_1,1/r_2$, now with normalized weights proportional to $(1-t)r_1,t r_2$, and scale back by their sum. This proves the claim, including the endpoint weights by equality.

Put $x=\pi a$ and $R=\sqrt{3/x}$. If $x\ge3$, the unit ball already gives $\operatorname{vol}_3 K\ge4x/3\ge4$. Otherwise $R>1$. The ball slice at height $z_0=\sqrt{R^2-1}/R$ in direction $u$ is a disk of radius $1/R$. The central section has area at least $\pi R^2$. For each $0\le z\le z_0$, convexity of $K'$ includes in its section at height $z$ the Minkowski combination of these two sections with weights $1-z/z_0,z/z_0$. The planar result just proved bounds the area below by
\[
 \pi\big(R-z\sqrt{R^2-1}\big)^2 .
\]
For heights $z_0\le z\le1$ use the ball section; negative heights have the same areas by symmetry. If $j=\sqrt{R^2-1}$, the volume gain beyond the ball is at least
\[
 2\pi\int_0^{j/R}[(R-jz)^2-(1-z^2)]\,dz
 =\frac{2\pi j^3}{3R}.
\]
Indeed the first two terms after integration, $(R^2-1)j/R$ and $-Rj(j/R)^2$, cancel, and the cubic term is $(j^2+1)(j/R)^3/3=j^3/(3R)$. Scaling back by $A^{1/2}$ gives
\[
 \operatorname{vol}_3 K\ge \frac{4x}{3}+\frac{2(3-x)^{3/2}}{3\sqrt3}.
\]
The right hand side is increasing on $0\le x\le3$, as its derivative is $4/3-\sqrt{(3-x)/3}\ge1/3$.

It remains to verify the rational lower volume bound used by the rule. Squaring gives
\[
 \frac{12}{25}-\left(\frac{6928}{10000}\right)^2
 =\frac{11}{390625}>0 .
\]
Also $\pi>6283/2000$. Indeed $\pi=16\arctan(1/5)-4\arctan(1/239)$ by the tangent addition formula in the first quadrant: the tangent of $4\arctan(1/5)$ is $120/119$. Integrating the alternating geometric series for $1/(1+s^2)$ gives
\[
 \pi>16\left(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}-\frac1{7\cdot5^7}\right)-\frac4{239}
 =\frac{1231847548}{392109375}>\frac{6283}{2000}.
\]
Thus $x> x_0=21764/10000$ since $(6283/2000)(6928/10000)-x_0=39/1250000$. With $c=2509/1000$ and $r=8/c-4x_0/3=1348531/4704375>0$, the exact comparison is
\[
 4(3-x_0)^3-27r^2=\frac{394261548376699}{24590160156250000}>0 .
\]
Taking the positive root verifies $4x_0/3+2(3-x_0)^{3/2}/(3\sqrt3)>8/c$. The case $x\ge3$ also exceeds $8/c$. This proves the required rank-three volume estimate with coefficient $2509/1000$.

We also use the following elementary lattice-volume implication. For a full lattice $L$ in $\mathbb{R}^d$ and a centrally symmetric compact convex body $K'$ with $\operatorname{vol}K'\ge 2^d\det L$, there is a nonzero lattice point in $K'$. For strict inequality, translate the pieces of $K'/2$ lying in distinct translates of a half-open fundamental parallelepiped for $L$ back into that parallelepiped. The sum of their volumes exceeds $\det L$, so two pieces overlap. The two corresponding distinct points of $K'/2$ differ by a nonzero lattice vector, lying in $K'$ by convexity and symmetry. For equality apply the strict argument to $(1+1/j)K'$ for each positive integer $j$; these sets lie in $2K'$, which contains only finitely many lattice points. A nonzero point occurring infinitely often lies in the closed body $K'$.

### Amended inverse theorem

For prime $q$, with the remaining hypotheses in `lem:inverse` and the (I6) above, every nonzero $v\in\mathbb{F}_q^{N_\star+1}$ with $v_0=0$ and $\operatorname{gp}(v^\top)>\theta$ has an integer short multiple $x$ with $x_0=0$, $0<\|x\|_\infty\le\beta$, and $x\bmod q=a v$ for some $a\in\mathbb{F}_q^*$.

Remove zero coordinates and order the nonzero coordinates as $v_1,\dots,v_{N_0}$. For a prefix of length $i$, let $p_i$ be its maximum modular fiber density for independent box coordinates uniform on $[2,g+1]\cap\mathbb{Z}$. Each fiber of the longer prefix, conditional on the last coordinate, is a fiber of the shorter prefix. Hence $p_i\ge p_{i+1}$. The single-coordinate map is injective on the box since $v_1\neq0$ and $g+1<q$, so
\[
\theta<p_{N_0}\le p_i\le p_1=1/g.
\]
Inductively we construct a saturated regular lattice $\Theta$ on the first $i$ coordinates with rank $d\in\{1,2,3\}$, $v_{[i]}\in\bar\Theta$, and $m(\Theta)\ge p_i-3\varepsilon_{\mathrm{tr}}$. This gives $m(\Theta)>\mu_{\mathrm{tr}}$ and $h(\Theta)\le H_d$, using regularity when $d\le2$ and `lem:prefix` (c) when $d=3$. For $i=1$ use $\mathbb{Z}$. Its height is 1, density is $1/g$ and $\Gamma_1\ge1$ follows from (I4) and $\mu_{\mathrm{tr}}<1/g$.

For the extension step choose any integral basis $B$ of $\Theta$, with a largest minor on row set $J$. Its determinant in those coordinates has absolute value $h=h(\Theta)$. The proof uses normalized features to bound the modular rank of the difference matrix.

Let $v_{[i]}=Bc'\bmod q$, and $c=(c',v_{i+1})$ over $\mathbb{F}_q$. Take a densest modular fiber of $v_{[i+1]}$ and trim it by $\Theta$, obtaining $F$ of density at least $p_{i+1}-\varepsilon_{\mathrm{tr}}$, by `lem:trim`. Write $\Phi(r)=(B^\top r_{[i]},r_{i+1})$. The points $\Phi(F)$ lie in one coset of the subgroup $c^\top y=0\bmod q$ of index $q$ in $\mathbb{Z}^{d+1}$, since the last entry of $c$ is nonzero. If their affine dimension were $d+1$, `lem:sparse` (a) and regularity would give
\[
\Pr[F]\le \Lambda_d\, g^d h(\Theta)m(\Theta)/q \le \Lambda_d\Gamma_d/q<\mu_{\mathrm{tr}},
\]
using (I5). This contradicts $\Pr[F]>\theta-\varepsilon_{\mathrm{tr}}$. Let $k'\le d$ be the actual dimension and $\Delta_*$ the integer matrix whose columns are differences of points of $\Phi(F)$ from any fixed point. Its rank is $k'$.

Put $P=BB_J^{-1}$, with entries bounded by one by the largest-minor argument. The normalized features are $(P^\top r_{[i]},r_{i+1})$. They are obtained from $\Phi$ by $A^{-1}$ where $A=\operatorname{diag}(B_J^\top,1)$ is integral and $|\det A|=h$. The ellipsoid condition is unchanged after the corresponding covariance change. Each normalized feature's deviation from its center is at most $R_{\rm tr}(g/\sqrt{12})\sqrt{N_\star}$, since its row of coefficients has Euclidean norm at most $\sqrt{N_\star}$. Thus every entry of the normalized differences $A^{-1}\Delta_*$ has magnitude at most $T_{\rm tr}$, also for the last row since $g-1<T_{\rm tr}$.

For any square minor $M'$ of $A^{-1}$, $h\det M'$ is an integer: take the chosen columns of $A^{-1}$ and append the standard basis columns indexed by the complementary chosen-row set. Expansion in the standard columns gives $\pm\det M'$. Multiplication by $A$ makes the full square matrix integral, proving the divisibility assertion. Cauchy--Binet then shows that $h$ times each $k'$-minor of $A^{-1}\Delta_*$ is integral. A nonzero such minor exists if $k'>0$, and its multiple by $h$ has magnitude at most $h k'!T_{\rm tr}^{k'}\le h d!T_{\rm tr}^d<q$ by (I5), since $h\le H_d$ and $T_{\rm tr}\ge1$. In particular $q\nmid h$. Reducing that minor modulo $q$ through the invertible denominator $h$ shows the normalized difference matrix has rank at least $k'$ over $\mathbb F_q$. As $A$ is invertible there, the integral $\Delta_*$ also has rank $k'$ (larger integer minors vanish). Its nonzero modular maximal minor is enough for the lifting fact of I3, which gives an integral $u\equiv c\bmod q$ with $u^\top\Delta_*=0$. If $k'=0$, take any integral representative of $c$. Consequently $u^\top\Phi(r)$ is constant on $F$, and $(Bu_{[d]},u_{d+1})$ lies in the saturated normal lattice $F^\perp$, reducing to $v_{[i+1]}$. In particular $F^\perp$ has positive rank. A rank-$s$ lattice fiber has density at most $g^{-s}$, since fixing the coordinates outside an invertible row minor leaves at most one assignment to the remaining $s$ coordinates. Since $\Pr[F]>\theta-\varepsilon_{\mathrm{tr}}>\mu_{\mathrm{tr}}$ and $g^{-4}<\mu_{\mathrm{tr}}$, its normal lattice has rank at most three. Its maximum fiber density is at least $\Pr[F]>\mu_{\mathrm{tr}}+2\varepsilon_{\mathrm{tr}}$. Apply `lem:regularize` to $F^\perp$ to get a regular saturated containing lattice with density at least $m(F^\perp)-2\varepsilon_{\mathrm{tr}}\ge p_{i+1}-3\varepsilon_{\mathrm{tr}}$. It contains the lift of $v_{[i+1]}$. This proves the induction.

For the terminal lattice choose $J$ as above. Let $z_0\in\mathbb{Z}^d$ with $Bz_0\equiv v_{[N_0]}\bmod q$. It is nonzero mod $q$ because $v_{[N_0]}\ne0$. The preimage $Z\subseteq\mathbb{Z}^d$ of the line $\mathbb{F}_q z_0$ has index $q^{d-1}$, since reduction of $\mathbb{Z}^d$ is onto and the line has $q$ elements out of $q^d$. Hence $L=B_J Z$ has determinant $h(\Theta)q^{d-1}$. Consider the body of feasible first coordinates
\[
K_B=\{u\in\mathbb{R}^d:\|B B_J^{-1}u\|_\infty\le1\}.
\]
The rows indexed by $J$ are the unit rows. Each $d$-row determinant has absolute value at most 1 because it is a minor of $B$ divided by its largest minor, up to sign. The body is symmetric, closed, convex and bounded. In rank one the unit interval lies in it by the largest-minor bound and has length 2. Since $h(\Theta)\le H_1\le\beta$, $\operatorname{vol}(\beta K_B)\ge2\det L$. In rank two the planar bound gives
\[
 \operatorname{vol}_2(\beta K_B)\ge3\beta^2\ge4H_2q\ge4h(\Theta)q=4\det L.
\]
In rank three, $h(\Theta)\le\lfloor H_3\rfloor$ by Amendment H3 and integrality. Hence
\[
 \operatorname{vol}_3(\beta K_B)\ge (8/(2509/1000))\,\beta^3
 \ge (8/(2509/1000))\,(2509/1000)\lfloor H_3\rfloor q^2
 \ge 8\det L .
\]
The volume implication gives a nonzero $u=B_J z$ in $L\cap\beta K_B$ in each rank. Put $x'=Bz$. It is nonzero because its coordinates in $J$ are $u$, and its norm is at most $\beta$ by the definition of $K_B$. Modulo $q$, $x'$ is a multiple of $v_{[N_0]}$ since $z\in Z$. If that multiple were zero, each integer entry of $x'$ would be divisible by $q$. As $\|x'\|_\infty\le\beta<q/2$ this would force $x'=0$. Extend $x'$ by zeros in the deleted positions, including coordinate 0, to obtain the required short multiple.

### Conditions for the Euclidean reduction

Write $B_{\rm E}=\mathrm{beta\_sis}$, $N_\star=N+3$, $\mu=\mu_{\rm tr}$, and $e=\varepsilon_{\rm tr}$. In addition to the four inequalities on the original inverse bound, require
\[
 R_{\rm tr}=20,\quad g\ge2^{65},\quad 16777216N_\star\le g,\quad
 16777216H_3\le g,\quad H_2^{10}<g^{19},\quad 1000e\le\mu,\quad g^4\mu\ge10000,
\]
\[
 B_{\rm E}\in\mathbb Z,\quad 1\le B_{\rm E},\quad 2B_{\rm E}<q,\quad
 24B_{\rm E}^4<q^3,
\]
\[
 B_{\rm E}g^2\mu\ge\sqrt{N_\star}\Gamma_1,\qquad
 B_{\rm E}^2g^2\mu\ge(178101/40)q,\qquad
 g^3\mu\ge\alpha_*=751/1000,\quad H_3<4 .
\]
The four inverse inequalities still prove the general infinity-radius statement at $\beta$, which satisfies the separately stipulated (P4). The added guards prove a Euclidean short multiple for every kernel vector in every heavy stack, and polynomial-time Euclidean lifting, in Amendment msis_bound. The degree and form of generic expressions, oracle counts, correctness and witness-extractor span argument use neither radius. The reduction uses the new radius $B_{\rm E}$ after row-space recovery.

Set $C_2=3855$ and $C_3=2828431/1000000$ for the covolume bounds. Also require $H_1<g^4$ and $B_{\rm E}g\mu\ge C_1=480618870=\lceil110000 C_2+20000000 C_3+250\rceil$. This proves the rank-one Euclidean estimate in msis_bound. Amendment n and the dense normal support bound ensure that no rank-three containing lattice in that Euclidean proof can contain a nonzero form-kernel vector. The infinity-radius bounds above remain unchanged for every kernel direction.

## Amendment Ncmp

For the variable $u$ used by the bound $E$, set
\[
N_{\mathrm{cmp}}(u)=\frac{u(u+10)}8 .
\]
The remaining formula for $E$, the values of $u=2Q+2$ used by the proof, and the two tests in (P5) are as specified in the protected model. The new count applies to the bad events that can pay a $\theta$ charge. The other pair and entry terms continue to pay for the full collection of possible coincidences.

### Coupling and bad events

Fix the uniform matrix realization $M$ for the expressions, and fix the adversary's call budget $Q$. The run up to the first query at the target label has the same law as the run with a uniform string in place of the masked message up to that query without its answer, by the coupling of the protected symbolic-game block. In the latter run the oracle answers and the uniform string can be chosen independently of the valid encryption coins and the search vector. The symbolic simulation with formal equality, including its label images, can therefore be sampled before evaluating the expressions at those coins. An entry introduced on a guessed operand is a new formal variable of its group. The simulation uses at most three new entries per call, for two operands and one result. Received entries are present at initialization. If a result is already formally equal to an entry, the simulation returns that label rather than inserting a new entry.

Evaluate the symbolic simulation at the independent coins and uniformly independent guess-variable values. Within a group a collision means equality of evaluated values for two formally distinct entries. One can couple the evaluated symbolic and random-mask runs until the first such collision. In the real run conditional on the label images, each unused label in any of the three groups, when guessed, has a uniform exponent among the field values not already assigned in its group, and each evaluated result with a new value receives a uniform unused label. Use the same fresh labels in the symbolic and real simulations for new values. Use the uniform guess-variable value for the real guess if it is new in that group, and redraw from the unused field values if it is already assigned. This has the required uniform unused law and disagrees only at a collision. Inductively, before a collision all assigned labels and their expressions agree between the two simulations, and calls and oracle queries agree because the adversary sees the same transcript. The first call on which a collision occurs is common to both runs, even when the answers at that call differ.

The initial collisions are an $\mathsf{init}$ mark. Suppose a non-initial collision occurs first, before a target-label query has set a mark. If the collision is good in the protected symbolic-game sense, its two entries lie in the target group and their difference has no guess variable. Its later entry cannot be a guessed operand, because that would introduce a new formal variable absent from the earlier entry. It is a result. The real result takes the earlier label, so the monitor sets a good difference mark. Thus a collision that gives a charged first mark must be a bad event. If a target-label query sets a charged first mark before a collision, the queried label has an entry, since otherwise the mark is $\mathsf{guess}$. This entry has the target value and its expression is bad by the monitor definition. If the first evaluated-symbolic collision instead triggers a redraw of a guessed operand in the real simulation, that collision already contains the fresh guess variable and is bad. It covers any later charged mark even if the real monitor made no mark at the redraw. Hence a charged first mark is covered by the bad collisions after initialization and the bad key-value events in the symbolic simulation.

For a fixed simulation a collision uses the difference expression $D$ and $\chi=0$, and a key-value event uses the entry $D$ and $\chi=1$. We bound the probability of a bad event over its evaluation. In either source group, if the difference has no guess variable, the source-group coincidence estimate proved in the algebraic view subsection bounds its probability by $\varepsilon_f$. If the expression contains a guess variable in any group, there is a nonzero formal coefficient of a guess monomial. Such a coefficient is either a nonzero field constant or a formally nonzero expression in one of the source groups, since products of guesses arise only through a pairing of source-group expressions. In the latter case for every fixed $r$ it is nonzero on some valid encryption coins by the source-group coincidence estimate and $\varepsilon_f<1$. Thus after clearing the factor $\varpi$, the event equation is a nonzero polynomial in coins and guess values for each fixed $r$. Its total degree is at most $d_f+1$. The terms without guesses have degree at most $d_f$ by the degree lemma. A term with one guess multiplying a source-group expression adds one degree to the cleared source expression, and terms with two guess variables and no other exponents have degree at most eight after clearing. All independent sampled field coordinates have support size at least $q-D$. The polynomial root bound gives probability at most $(d_f+1)/(q-D)\le\varepsilon_f$.

The remaining case is a guess-free target-group difference or key-value expression. For any $r$ at which $D$ is not identically $\chi\kappa$, the probability of coincidence over coins is at most $\varepsilon_f$ by the view lemma. For an $r$ at which it is identical, the mark stack is nonzero. For a collision this follows since the two entries were formally distinct, and for a key-value expression it follows from the no-formal-key conclusion of the view lemma. The view lemma also places every such $r$ in a single fiber of the fixed stack, specified by the stack's fixed vectors $u_c$. Thus the event in this case is bad only for a light stack, and the probability over $r$ is at most $\theta$. The combined bound on the bad event is $\theta+\varepsilon_f$.

### Counting the light-stack charges

Only the last case uses the $\theta$ summand. At call $j$ a collision in this case must have a result as its later entry, since an operand entering as a fresh guessed entry has its own new guess variable. Among earlier target-group entries, the received ones number at most two and results of earlier calls at most $j-1$. All remaining earlier target-group entries are single guessed variables introduced as operands. For a fixed result expression the part involving guess variables can be exactly one of those variables at most once. Thus the result can have guess-free difference with at most one entry of this last type, even if one or both operands of call $j$ have just been guessed. Indeed if it had guess-free difference with two distinct such entries, their subtraction would be guess-free by linearity, whereas it is the difference of two distinct formal variables. This gives at most $j+2$ candidate target-group comparisons at call $j$. The possible guess-free key-value entries in the target group number at most $Q+2$ since they must be received elements or results; any fresh guessed entry contains its guessed variable. Therefore the total number of events that can incur a $\theta$ charge is at most
\[
 \sum_{j=1}^Q(j+2)+Q+2
 = \frac{Q(Q+1)}2+3Q+2
 = \frac{u(u+10)}8-1 .
\]
The full count for all other bad events is bounded by the number of pairs plus the number of entries in a table of at most $L+3Q$ entries, and hence by $\binom{L+3u}{2}+L+3u$. The pair count may overcount comparisons between different groups, which only increases the bound. Combining the union bounds establishes the amended charged-mark estimate
\[
 \Pr[\text{charged first mark}]
 \le N_{\mathrm{cmp}}(u)(\theta+\varepsilon_f)
       +\left(\binom{L+3u}{2}+L+3u\right)\varepsilon_f .
\]
This argument holds for every realized $M$, independent of the form packing.

### Generic ledger and scope of the amendment

The generic ledger has the same implication from (P5). In the amended $E$, all coefficients as a polynomial in $u$ are nonnegative and its degree is two. Here $L\ge1$, $N_{\mathrm{free}}>0$ by (P2), and $\binom{L+3u}{2}$ expands with nonnegative constant, linear and quadratic coefficients. The new $N_{\mathrm{cmp}}$ has nonnegative coefficients. For real $Q$ on $[0,2^\lambda-1]$, the function $Q\mapsto E(2Q+2)-(Q+1)/2^\lambda$ is convex because its quadratic coefficient is nonnegative. At the first endpoint it is at most zero by the first P5 test. At the second it is $E(2^{\lambda+1})-1$, at most zero by adding the P5 tests. By convexity it is at most zero throughout. The threshold side conclusion of the generic ledger becomes $\theta<2^{1-2\lambda}$ for $\lambda\ge1$. Indeed putting $U=2^{\lambda+1}$, we have $N_{\mathrm{cmp}}(U)-N_{\mathrm{cmp}}(2)=U^2/8+5U/4-3>2^{2\lambda-1}$. Every other term in $E(U)-E(2)$ is nonnegative, so the second P5 bound implies the stated strict threshold limit.

The changed count enters the admissibility block only through the value of $E$ in P5. The expression, monitor and symbolic-game blocks are independent of the count: they specify the same formal polynomial expressions, oracle label sampling and classifications of marks and events. The view lemma uses degree, coin ranges, algebraic identities of the factors and polynomial root bounds, all independent of this count. The implication $\varepsilon_f<1$ used by the comparisons follows as before because $E(2)\ge24\varepsilon_f$ from its fourth term and (P5) remains in force. The factor-one-half lemma concerns the uniform-mask coupling and the two actual failure probabilities, so its argument has no count or bound $E$ as a premise. The initial and guessed-label bounds use only the distinct received-expression comparisons and the uniform as-yet-unassigned target label respectively. The reduction lemma uses the private polynomial degree, gradient distribution, rank and short-vector properties, with no $\theta$-charge count. Its success probability refers to the same run and the same instance. Thus those results in the background list of the bound block apply with the same statements and arguments. The charged-mark and generic-ledger results are proved above, and extraction is derived in Targets.

The extractability-error corollary follows with its original statement from Targets and the factor-one-half lemma. For allowable budgets, in the combined bit experiment with uniform $b$, put $f_i=\Pr[\mathsf{Tgt}\wedge\mathsf{Fail}\mid b=i]$. The probability of both a correct bit and extraction failure is at most $1/2+(f_0+f_1)/4$. The target-query bound in Targets gives $f_i\le (Q+1)/2^\lambda+s_i$ for each $i$. Both reductions run in time bounded by $t_R=t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)$, including fixed description and advice, so each $s_i$ is bounded by $\operatorname{Adv}^{\mathrm{MSIS}}(t_R)$ by its defining maximum. Substitution gives extractability error at most $(Q+1)/2^{\lambda+1}+\operatorname{Adv}^{\mathrm{MSIS}}(t_R)$ at the same extractor time. Outside the stated budgets, the trivial probability upper bound 1 yields error $1/2$ as in the corollary. This accounts for every result in the background list of the bound block.

## Amendment D

The external system $S$ and its number $N$ of Boolean unknowns are fixed. Internally extend an assignment with three auxiliary Boolean coordinates $\mathsf b_1,\mathsf b_2,\mathsf b_3$, all unconstrained except for their Booleanity. Put $N_\star=N+3$. The extended assignment vector has $N_\star+1=N+4$ coordinates including the homogeneous coordinate zero. Every witness of the external system has all eight extended tags, and projecting any extended witness onto coordinates zero through $N$ gives an external witness. The encoding uses no tag as an extra condition on the external system.

Use $N_\star+1$ distinct Booleanity points $d_0,\ldots,d_{N_\star}$, a distinct key point $\rho$, and the same $n_{\mathsf c}$ cosets of size $\nu$ for the external constraints. Hence $D=N+5+\nu n_{\mathsf c}$. The finite setup selects $n_{\mathsf c}$ distinct order-$\nu$ cosets and $N+5$ unused singleton points inside $\mathcal H_M$ of order $M=2^{22}$, available by C3. There are $M/\nu=2048$ small cosets to choose from and $M-\nu n_{\mathsf c}=729088$ unused singleton positions. Any such arrangement has the same finite counts; there is no larger-block condition. The public constraint and term labels fix which raw point-value records are used in each position. For an externally supplied labelled record, setup can use any arrangement inside the stated subgroup, keep the raw vectors and apply the corresponding $Z_0$ factors. Every constraint sum divides out precisely those factors, so its predicate is unchanged. If the evaluation points are externally prescribed in the field, the same scheme uses them directly with general interpolation instead of the subgroup FFT; the polynomial identities and correction arrays do not require subgroup membership beyond the constraint coset definition.

 At $d_0$ set $A=0,B=e_0$. At $d_i$, $i>0$, set $A=e_i-e_0,B=e_i$, including the three new Booleanity points. Fix a public primitive eighth root $\omega_8$ in the scalar field, which exists because $8\mid q-1$. Set $c_*=(\omega_8+\omega_8^{-1})^{-1}$; indeed $(\omega_8+\omega_8^{-1})^2=2$ since $\omega_8^2+\omega_8^{-2}=0$. At $\rho$ set $A=c_*(e_{\mathsf b_1}+e_{\mathsf b_2})$ and $B=c_*(e_{\mathsf b_1}+e_{\mathsf b_2}-e_0)$. On the constraint cosets keep the protected evaluations, extending those linear forms by zero in the tag entries. The coordinate polynomials are the unique interpolants of degree below $D$. Store their sparse point-value descriptions rather than a dense coordinate-by-degree table. Define $Z_0$ to vanish at all $d_i$ and $\rho$, $Z$ at every evaluation point except $\rho$, $Z_*=(X-\rho)Z$, and $L_\rho=Z/Z(\rho)$. Thus $Z_*=Z_0Z_{\mathcal K}$, where $Z_{\mathcal K}=\prod_t(X^\nu-\delta_t^\nu)$ is the monic coset vanishing polynomial.

Here is the QAP criterion under this setup. For a symmetric $W$, $P_W=A^\top W B$ takes values $0$ at $d_0$, $W_{ii}-W_{0i}$ at $d_i$ with $i>0$, and $c_*^2(W_{\mathsf b_1,\mathsf b_1}+W_{\mathsf b_2,\mathsf b_2}+2W_{\mathsf b_1,\mathsf b_2}-W_{0,\mathsf b_1}-W_{0,\mathsf b_2})$ at $\rho$. Once the Booleanity tests hold, this last expression equals $W_{\mathsf b_1,\mathsf b_2}$, using symmetry and $2c_*^2=1$. On each constraint coset $P_W/Z_0$ is the list of terms in that constraint's quadratic test. Let $R_W$ be the polynomial of degree below $\nu n_{\mathsf c}$ interpolating these coset values. The sum of $X^a$ on $\delta_t\mathcal G$ is zero unless $\nu\mid a$, in which case it is $\nu\delta_t^a$. Among degrees below $\nu n_{\mathsf c}$, the multiples of $\nu$ give an invertible Vandermonde matrix in the distinct $\delta_t^\nu$. Consequently all coset sums vanish if and only if $R_W$ omits all divisible powers. Under the Booleanity and constraint tests, $P_W-W_{\mathsf b_1,\mathsf b_2} L_\rho-Z_0 R_W$ vanishes at every evaluation point. It is therefore divisible by $Z_*$, with quotient degree below $D-1$ from $\deg P_W\le2D-2$. Equivalently $P_W-Z_0R_W$ is divisible by $Z$ with quotient degree below $D$. Conversely, either such identity with an allowed $R$ implies the Booleanity values and the coset sum tests by evaluation, and $R$ is the unique interpolated remainder. In the key identity, evaluation at $\rho$ gives exactly the specified corner $W_{\mathsf b_1,\mathsf b_2}$. For a witness vector $v$, these identities apply to $vv^\top$, with $P_v=A_v B_v$ and key corner $\mathsf b_1\mathsf b_2$.

The new key evaluation has $A(\rho)=c_*(e_{\mathsf b_1}+e_{\mathsf b_2})$, which together with $A(d_i)=e_i-e_0$ for $i>0$ spans all form coordinates: the differences span the hyperplane of coordinate sum zero and $A(\rho)$ has coordinate sum $2c_*\ne0$. The vectors $B(d_i)=e_i$ are still a basis. These properties, the QAP criterion and the updated $D$ are the only changes in the generic comparison and coincidence arguments, explicitly used in C7. The point descriptions consist of the nonzero input terms and $O(D)$ point data. For evaluation of all coordinate polynomials at a scalar off the point set, tabulate the $D$ Lagrange weights there and accumulate the listed nonzero coordinate entries times their weights. For a witness, accumulate the point values of the two scalar witness polynomials and interpolate only those two polynomials, not the coordinate table. The same subgroup interpolation and vanishing-polynomial algorithms therefore give $O(|S|+D\log D+\log q)$ setup and the claimed scalar polynomial work with these point sets. The three extra Booleanity evaluations and the key evaluation add only a constant number of nonzero coefficients. The score still uses the fixed original nonzero-coefficient charge.

## Amendment ell

Set $p=\mathrm{pack\_digits}$ and $\ell=\lceil N/p\rceil+3$. Divide the ordinary coordinates into successive blocks of $p$, padding the final block with zeros. Place each block in positions zero through $p-1$ of its ring column and zero-fill other positions. The range $1\le p\le d_R$ from C5 provides these distinct positions. Put each of the three tag coordinates in the constant position of its own separate following column. Column zero takes the independent homogeneous entry. All matrix columns have uniform independent entries in the ring.

The placement is injective, preserves coefficient Euclidean norm, and commutes with reduction and field scaling. The slot-zero form is $v_0$. The following slots contain the uniform matrix coefficient list and the fixed Vandermonde rows of Amendment n, in that order. A form-kernel vector has $v_0=0$ and $A\hat v=0$, and also lies in the kernel of those fixed rows. Thus the short multiple used by the reduction packs to a nonzero solution of the same norm to the uniform Module-SIS problem with dimensions $kd_R,\ell d_R$. For any fixed tag variant of an external witness, condition on all columns except column zero. Since its homogeneous coordinate is one, the independent uniform column zero adds a uniform coefficient vector to the remaining fixed vector. Consequently each tagged form is uniform on its affine coset with constant slot one and its own prescribed fixed-row values. This distribution is sufficient for both the exact key-weight bound and the expected fallback bound.

## Amendment Bsearch

Use the independent box sampler on $N_\star=N+3$ coordinates and one extra independent box value $r_\diamond$, all uniform on $\{2,\ldots,g+1\}$. Set
\[
 r_0=A_0+r_\diamond-\left\lfloor{\tfrac12\sum_{i=1}^{N_\star}r_i}\right\rfloor,\qquad
 A_0=\left\lceil N_\star(g+1)/2\right\rceil .
\]
Given the box coordinates, the zeroth coordinate is uniform on a translate of $g$ integers, distinct modulo $q$. The public center for a Boolean vector $v$ with $v_0=1$ is
\[
 c_v=\left\lfloor A_0+\frac{g+3}{2}\bigl(1+\operatorname{wt}(v)-N_\star/2\bigr)\right\rfloor .
\]
If $X_i=r_i-(g+3)/2$, and $X_\diamond=r_\diamond-(g+3)/2$, then $r(v)-c_v=X_\diamond+\sum_i(v_i-1/2)X_i+E$, where the two rounding terms in $E$ have absolute sum at most $3/2$. The independent centered sum has variance $(g^2-1)(N_\star+4)/48$. Thus its full RMS is at most $g\sqrt{(N+7)/48}+3/2$ by the triangle inequality in quadratic mean. Each $|X_i|\le(g-1)/2$; the deterministic bound including rounding is at most $B=(N+4)(g+1)$. A centered difference of three tag coordinates or a single centered tag coordinate also lies in this range. This is the definition of $B_{\rm search}$. The protected check $2B+1<q$ gives unique valid bounded representatives for all the searches in the amended correctness algorithm.

The guessing probability of a rank-$d$ stack is still at most $g^{-d}$. For any prescribed joint fiber, pick a nonsingular $d$-column pivot minor of a basis of the row space. If the zeroth column is nonzero, it can be extended to a pivot basis by linear independence of the columns. Fix the remaining nonpivot box coordinates; any solution fixes the pivot box coordinates and the zeroth coordinate uniquely by the invertible linear system. The regular pivot box draws therefore have probability at most $g^{-(d-1)}$ of meeting their fixed values, and conditional on all box coordinates $r_0$ has probability at most $1/g$ of the required value. If the zeroth column is zero, no condition involves $r_0$, so fixing the other box coordinates directly bounds the pivot solution by $g^{-d}$. These probabilities hold for every fixed fiber and give the claimed bound. For a kernel vector the zeroth coefficient is zero, so its scalar guessing probability uses precisely the independent box coordinates, now on at most $N_\star$ positions. The inverse and regularization proofs apply in that dimension with the factors of I3 and $T_{\rm tr}$ stated next. All heavy-stack and generic ledger arguments therefore use the same guessing-probability implications. The actual arithmetic of the search is supplied in Amendment search_spread.

## Amendment T_tr

Use $T_{\rm tr}=R_{\rm tr}g\sqrt{(N+3)/3}$. The trimming radius and covariance proof in I3 is used on the independent box of dimension at most $N_\star$. Each projected feature-row deviation from its center is at most $R_{\rm tr}(g/\sqrt{12})\sqrt{N_\star}$ times the corresponding basis-vector infinity norm, by the Euclidean Cauchy--Schwarz bound on that row's coefficient norm. Taking differences doubles the bound and gives precisely this new $T_{\rm tr}$. The minor and prefix-lift argument of I6 uses the checked inequalities in I5 with this value. The projected counting constants in I3 use $N_\star$ for the same reason. The definitions of regularity, fiber densities and their trimming loss use only the width, coefficient lattice and the radius and have the same arguments. Thus the amended radius supplies the lattice-facts hypothesis and norm proof in the new sampler dimension.


## Amendment C6

Require $n=3434$, $\mathrm{seed\_mode}=1$, $s_0=\mathrm{seed\_degree}=1717$, $n/s_0=r_H=2$, $r_H\mid q-1$, $2n\le D$ and $\Delta\ge n+3$. Put $Q=q^{s_0}$.

For fixed tables, test monic $F$ of degree $s_0$ by $X^{q^{s_0}}=X\bmod F$ and $\gcd(F,X^{q^{s_0/l}}-X)=1$ for primes $l\mid s_0$. These force simple factors of degrees dividing $s_0$ and exclude proper divisors. Take the first passing monic polynomial in residue order. Irreducibles exist because proper subfields of $\mathbb F_{q^{s_0}}$ contain at most $s_0 q^{s_0/2}<q^{s_0}$ elements in total.

In $K=\mathbb F_q[X]/(F)$, $Q=q^{s_0}$, take the first passing nonzero representative for $c_H$. Require $c_H^{q^{s_0/l}}\nec_H$ for primes $l\mid s_0$ and $c_H^{(Q-1)/p}\ne1$ for primes $p\mid r_H$. By cyclicity the order tests pass for proportion $\prod_{p\mid r_H}(1-1/p)>1/4$ in this mode. Proper subfields exclude at most $s_0 q^{s_0/2}<(Q-1)/16$. Hence the selection terminates. Define $P_c$ by the conjugate linear factors of $c_H$ and $P_T(T)=P_c(T^{r_H})$. Both selections are public precomputation before Setup, and the proof uses only the tested properties.

Let $t$ be a root of $T^{r_H}-c_H$ in the algebraic closure. If $o$ is the order of $c_H$ and $m$ the order of $t$, then $m/\gcd(m,r_H)=o$. The order tests give $v_p(o)=v_p(Q-1)>0$ at each prime of $r_H$. Thus $m=r_Ho$. For each prime $p\mid r_H$, the binomial expansion gives $v_p(Q^j-1)=v_p(Q-1)+v_p(j)$: raising $1+u$ with $p\mid u$ to $p$ increases $v_p(u)$ by exactly one, since $pu$ is the unique term of lowest valuation. At two this uses $4\mid Q-1$. Raising to an exponent prime to $p$ preserves the valuation by the factorization as $u$ times a geometric sum congruent to that exponent. Iterating proves the identity for every positive $j$. For a positive $j$, the condition $m\mid Q^j-1$ is therefore equivalent to $r_H\mid j$. Thus $t$ has degree $r_H$ over $K$. As it generates $c_H=t^{r_H}$, it also generates $K=\mathbb F_q(c_H)$ over $\mathbb F_q$. Its degree over $\mathbb F_q$ is $s_0r_H=n$. The monic polynomial $P_T(T)=P_c(T^{r_H})$ of degree $n$ vanishes at $t$, proving irreducibility.

At $j=r_H/2$, the same valuations show $m/2\mid Q^j-1$ and $m\nmid Q^j-1$. Consequently $t^{q^{n/2}}=-t$, since $Q^{r_H/2}=q^{n/2}$ and $-1$ is the unique element of order two. Use the monomial basis through degree $n-1$ in the same form slots as above. The $V$ weights have even powers only. All three consecutive Frobenius projections have their original field identities and the same coefficient-kernel relation.

For each Frobenius exponent $j$, put $b_j=q^j\bmod r_H(Q-1)$. The image of $T^a$ is
\[
 c_H^{\lfloor ab_j/r_H\rfloor}T^{ab_j\bmod r_H}.
\]
Indeed $T^{r_H(Q-1)}=1$ and $T^{r_H}=c_H$. Expand the coefficient in the basis $1,c_H,\ldots,c_H^{s_0-1}$ and replace $c_H$ by $T^{r_H}$. The representative has at most $s_0$ monomials of degree below $n$, all in the residue class $a\bmod r_H$ since $q\equiv1\bmod r_H$. Thus each conjugate map or its transpose uses at most $n s_0$ products, and the half-turn is just a sign on odd powers. C7 uses these representatives as fixed public tables. They have exactly the same field relation as their monomials and preserve the kernel defined by the coefficient placement.

## Amendment C7

Require $\mathrm{base\_degree}=\mathrm{base\_left}=\mathrm{base\_right}=\mathrm{scalar\_rel}=1$, $K_1,K_2\ge1$, and $2K_1K_2=n$. Require $\mathrm{mask\_stride}=1$ and $C_{\rm mask}=58393$. This is the one-variable grid. Write $e=A_H=B_H=1$ and $h=n$ when using field-degree notation. There are $A_c=3K_1K_2=3n/2$ cells, indexed by a left leg $a$ with $0\le a<K_1$ and a right leg $(b,\mathrm X)$, $0\le b<K_2$, $\mathrm X\in\{\mathrm E,\mathrm O,\mathrm V\}$. Write $p_X=\mathbf1_{\mathrm X=\mathrm O}$. Set $\lambda_a=2K_2a$, $k_{\mathrm{leg}}=2b+p_X$. Put $k_c=\lambda_a+k_{\mathrm{leg}}$. For E and O the cell weight is the coefficient of $T^{k_c}$ in $U=z(w)\sigma^{n/2-1}(z(w))$; for V use $V=z(w)\sigma^{n/2}(z(w))$. The half-turn fixes $V$ so only even powers occur there. For the appropriate parity $p_X$, divide $(k_c-p_X)/2$ by $K_2$. Its quotient $a$ and remainder $b$ recover the two digits and cover each slot exactly once. The key cell is $a=b=0,\mathrm X=\mathrm E$, with weight the constant coefficient of $U$.

### Factor masks and publication

Use the original independent scalar coins and centered sampler in the internal dimension. The evaluation coin $\upsilon$ is uniform nonzero, the scalars $\pi,s_{\mathrm U},s_{\mathrm V},\zeta_0,\zeta_1,\zeta'',\eta_1,\eta_2,\eta_3,\Omega_{22},\alpha$ are independent uniform nonzero, $\Omega_{12}$ and the coordinates $y_i$ are independent uniform scalars, and $\tau$ is uniform off the evaluation points. Sample $\varepsilon$ uniformly from the field excluding $0,-1$. Let $F_x(T)$ be the reduced representative of $\sigma^{n/2+1}(T^x)$, computed by C6. Write $z_-,z_\circ,z_+$ for the reduced vectors of linear form coefficients at Frobenius powers $n/2-1,n/2,n/2+1$, respectively, evaluating at $\upsilon$ when used as scalars. Set
\[
 \pi_a=\pi(\upsilon^{\lambda_a}+\varepsilon F_{\lambda_a}(\upsilon)),\qquad
 s_{\rm leg}=s_{\mathrm X}\upsilon^{k_{\rm leg}},\qquad
 \gamma_c=\pi_a s_{\rm leg},\qquad
 \kappa=\gamma_{\rm key}L_\rho(\tau).
\]
Set $s_{\mathrm X}=s_{\mathrm U}$ on E and O, and $s_{\mathrm X}=s_{\mathrm V}$ on V. The U right monomials have distinct even or odd exponents $k_{\rm leg}$, identifying the class and its index. The occupied U cell exponents $k_c$ are all distinct by division by $2K_2$. The V scale is independent, and its even exponents distinguish its own right legs and cells. Thus each use of distinct right or cell monomials in the comparisons below holds with these two scales. Here $\pi_0=\pi(1+\varepsilon)\ne0$, hence $\kappa\ne0$ on valid coins. On E/O use the right mask
\[
 \vartheta_{\rm leg}
 =\upsilon^{k_{\rm leg}}(\eta_1 z_\circ+\eta_2 z_+)
   -\varepsilon^{-1}F_{k_{\rm leg}}(\upsilon)(\eta_2 z_-+\eta_3 z_\circ),
\]
and on V use $\upsilon^{k_{\rm leg}}(\eta_3 z_+-\eta_1 z_-)$. For every input coordinate $i$ including tags, use the left row $\pi_a(y_i,A_i(\tau))$ and the right column $(s_{\rm leg}(r_i+A_i(\tau))+\vartheta_{{\rm leg},i},\,s_{\rm leg}(B_i(\tau)-y_i))^\top$. Multiply each left row on the right by the hidden-basis matrix with rows $(1,\Omega_{12})$ and $(0,\Omega_{22})$, and each right column on the left by its inverse. Publish the resulting coordinate arrays in G1 and G2, respectively, the G2 search bases $[s_{\rm leg}]_2$, and the single G1 column $[\zeta'' y_i]_1$. There is one right sector and there are no alpha-scaled source-group inputs. Keep the public target-group element $[\alpha\kappa]_T$, with independent $\alpha$, and the seed and masked message. This slot preserves the protected overhead count. The decryption algorithm does not require this target-group input.

### Honest cancellation and the three field ties

For a stack form $W_U,W_V$ by summing cell matrices times $T^{k_c}$ in their weight families. Put $\widetilde W_U^+=\sum_{c\in C_U}W_c F_{\lambda_a}F_{k_{\rm leg}}$, whose image in the form field is $\sigma^{n/2+1}(W_U)$. After taking out $\pi$ and the independent $\eta_i$, the actual grade-zero polynomials are
\[
 t_1=W_Uz_\circ-W_Vz_-,\qquad
 t_2=W_Uz_+-\widetilde W_U^+z_-,\qquad
 t_3=W_Vz_+-\widetilde W_U^+z_\circ .
\]
Indeed the negative grade in the right E/O mask contributes degree zero when multiplied by the twisted part of $\pi_a$. The ordinary products supply the remaining terms. With the honest weights and the form vectors contracted against $w$, each $t_i$ vanishes in the field: $U z_\circ=V z_-$, $U z_+=\sigma^{n/2+1}(U)z_-$, and $V z_+=\sigma^{n/2+1}(U)z_\circ$. The finite supports and group bases for these multiples are specified next.

In a formal identity, the Laurent comparison below isolates the same grade-zero polynomials for the actual stack up to multiples of $P_T$. Their reduction gives all three stated field ties. The right-leg type $s_{\mathrm X}$ and the ordinary exponent $k_c$ distinguish every cell in the generic comparison. The proof of the original rank-three classification using these ties follows. The new QAP point at $\rho$ changes only the corner used by the view and does not change the Booleanity or constraint tests used by that classification.


### Cancellation with the even form modulus

The ordinary left exponents are $\lambda_a=2K_2a$. By C6 their images have degree at most $n-r_H$ plus the original exponent residue modulo $r_H$. The left residue cycle has length $r_H/d_0$ for $d_0=\gcd(2K_2,r_H)$ and $K_1\ge r_H/d_0$ at this shape, so the maximum residue is $r_H-d_0$. The right exponents start at zero and their maximum residue is $\min(2K_2-1,r_H-1)$. This gives $L_\sigma=3432$ and $R_\sigma=3433$. The ordinary right degrees are at most $2K_2-1$ on U and $2K_2-2$ on V.

The zero-grade expressions $t_1,t_2,t_3$ have degrees at most $2n-2,L_\sigma+R_\sigma+n-1,L_\sigma+R_\sigma+n-1$, respectively. Both latter bounds are at least $2n-2$. For the honest weights these polynomials are multiples of the degree-$n$ modulus by the field identities already proved. Their quotient lengths are $n-1,L_\sigma+R_\sigma,L_\sigma+R_\sigma$. Publish the bases with exponents $\pi\eta_i P_T(\upsilon)\upsilon^a/\zeta''$ at the corresponding nonnegative consecutive exponents.

The positive grades multiply the conjugated left digit, an ordinary right digit and a form polynomial. Their lengths are $L_\sigma+2K_2-1+n,L_\sigma+2K_2-1+n,L_\sigma+2K_2-2+n$. The last uses the even right degree. Each negative grade multiplies the ordinary left digit, the conjugated right digit and a form. Its length is $2n-2K_2+R_\sigma$. Publish the bases with exponents $\pi\eta_i\varepsilon^{\pm1}\upsilon^a/\zeta''$ at the corresponding consecutive exponents. These products follow directly from the two grades of $\pi_a$ and the ordinary and inverse-$\varepsilon$ terms of the right masks. No additional reduction of a leg product is made.

The eight lengths are $3433,6865,6865,6899,6899,6898,10267,10267$, summing to $58393$. Each coefficient uses its sign in the cancellation MSM. Pairing the result with the witness-summed Y removes the entire mask. These support bounds keep every published cancellation polynomial within degree $3n-3$, including the multiplication by $P_T$ in grade zero. They impose no change to the three actual ties, which the Laurent comparison reads modulo $P_T$, nor to the coefficient of any cell monomial.

### Scored encryption arithmetic

This accounts for all arithmetic of the admitted finite mode. Write $S_{\rm nz}$ for the number of nonzero point coefficients traversed in preparing the QAP exponents, to which the benchmark assigns $2^{30}$. We show at most $S_{\rm nz}+3m$ variable scalar multiplications in that cost convention.

By C6, each of the two selected Frobenius maps sends each basis monomial to a polynomial with at most $s_0$ supported coefficients, and the half-turn applies signs. Evaluating both tables from the powers of $\upsilon$ therefore uses at most $2ns_0$ multiplications. The same support bound applies to the conjugated digit evaluations.

Form the two combined tables for
\[
 A_\eta=\eta_1z_\circ+\eta_2z_+,\qquad B_\eta=\eta_2z_-+\eta_3z_\circ.
\]
The third form used by the masks is $C_\eta=(\eta_3 A_\eta-\eta_1 B_\eta)/\eta_2$, by direct expansion with the existing nonzero $\eta_2$.


The row and accumulated-column maps are identities in the scalar basis. Thus there are no conversion products.

In the scalar representation write the two transformed row-weight sequences as $A^{(1)},A^{(2)}$, and the uniform matrix column as $B$, all of length $k$. For a pair of consecutive indices $u,v$ add
\[
 (A^{(h)}_u+B_v)(A^{(h)}_v+B_u)
 - A^{(h)}_u A^{(h)}_v - B_u B_v
   = A^{(h)}_uB_u+A^{(h)}_vB_v,\qquad h=1,2.
\]
Compute the sum of the row-only terms separately for the two rows and the sum of the column-only terms once per column, shared across the two outputs. The identity verifies both desired matrix products term by term. Every pair uses two main multiplications and one column correction product. A final unpaired row needs two products per column. The two row corrections take $2\lfloor k/2\rfloor$ products per evaluation root. Hence the total cost of the products and both transforms is bounded by
\[
 W_{\mathrm{mat}}
 =d\big((\ell+1)(3\lfloor k/2\rfloor+2(k\bmod2))+2\lfloor k/2\rfloor\big)=W.
\]
The two output products use the same uniform ring entries as the programmed instance. Add the known slot-zero homogeneous contribution. For each input column, add the dot product of its $u$ fixed-row coefficients with the final $u$ entries of each evaluated form-weight vector. This needs at most $2u(N+4)$ further products, as charged in C5. The coefficient basis and Vandermonde powers are fixed public data. The two outputs are now exactly $A_\eta,B_\eta$. Form $C_\eta$ by its linear combination using the two precomputed ratios $\eta_3/\eta_2,\eta_1/\eta_2$, at two multiplications per input coordinate.

Partition the QAP roots into the $N+5$ Booleanity and key singleton factors and $n_{\mathsf c}$ constraint cosets. Their vanishing factors at $\tau$ are respectively $\tau-p$ and $\tau^\nu-a^\nu$ for a coset represented by $a$. Compute $\tau^{2^j}$ for $1\le j\le11$ by successive squaring. On the list of $b=N+5+n_{\mathsf c}$ factor values, ordered with singletons first, use prefix and suffix products to get their product and their outer complements. Prefix values through the singleton group and the whole list give $Z_0(\tau)$ and $Z_*(\tau)$. A first value and an end complement can be copied without multiplying by one. The full prefix uses $b-1$ products, the suffix excluding its unused first product uses $b-2$, and the $b-2$ interior complement products supply the rest. At a coset node of size $2^j$, split it into its two child cosets of size $2^{j-1}$. Each child's vanishing evaluation is the precomputed power $\tau^{2^{j-1}}$ minus the corresponding public power of a representative. The two child complements are the outer complement at the parent times the sibling vanishing evaluation. With two multiplications per internal node of a $\nu$-leaf tree, this provides all $Z_*(\tau)/(\tau-p)$ using $2(\nu-1)n_{\mathsf c}$ products after the outer pass. At $\rho$ the complement is $Z(\tau)$. The sum of all products is at most $3b-5+11+2(\nu-1)n_{\mathsf c}=2D+N+n_{\mathsf c}+11$, which fits the $2D+N+n_{\mathsf c}+16$ term. The public QAP coefficients at $p$ are encoded with the fixed multiplier $1/Z_*'(p)$. Multiplying an encoded point coefficient by its cofactor now makes the exact Lagrange contribution with one multiplication. The nine new Booleanity coefficients and the five entries at $\rho$ are covered by the sixteen-multiplication allowance below. All these scalars are over $\mathbb F_q$.

The G1 factor computations use at most $(2K_1+3)(N+4)$ multiplications, including the shared hidden-basis scalar $\Omega_{12}y_i+\Omega_{22}A_i$, the two per-left-scale exponents and the extra Y-column scaling. In G2 put $U_i=B_i(\tau)-y_i$ and $V_i=r_i+A_i(\tau)-(\Omega_{12}/\Omega_{22})U_i$. Prepare $V_{\rm U}=s_{\rm U}V+A_\eta$ and $V_{\rm V}=s_{\rm V}V+C_\eta$. Computing $V$ and these vectors takes three multiplications per coordinate. With the two for $C_\eta$ this is five per coordinate. Precompute $V_{\rm U}B_\eta$ once per coordinate and the product $ab$ for each E/O leg, where $a=\upsilon^{k_{\rm leg}}$ and $b=-\varepsilon^{-1}F_{k_{\rm leg}}(\upsilon)$. The identity
\[
 aV_{\rm U}+bB_\eta=(V_{\rm U}+b)(B_\eta+a)-V_{\rm U}B_\eta-ab
\]
then gives one product per first U coordinate. The V first coordinate uses $\upsilon^{k_{\rm leg}}V_{\rm V}$, and the second coordinate for each leg uses $(s_{\rm leg}/\Omega_{22})U$. The right products thus cost at most $(6K_2+6)(N+4)+2K_2$, including the five shared products and one shared cross product per coordinate. The left bound is $(2K_1+3)(N+4)$, giving the grouped term of C5.

### Reused scale factors for the published source exponents

For the sparse powers of Amendment n1, start at the already sampled exponent $\zeta_0$. Compute $\tau^\nu$ by eleven squarings, including $\tau^2$. Advance the sparse base exponent by repeated multiplication by $\tau^\nu$. For each sparse entry also obtain the shifted entry with one multiplication by $\tau$. Together these use at most $2S_0-1$ further products. For the non-sparse list start at $\zeta_1\tau$. The gap between consecutive allowed exponents is one, except at a skipped multiple of $\nu$ where it is two. Multiply the current exponent by the already available $\tau$ or $\tau^2$ accordingly. At most $\Delta-\Delta/\nu$ further products therefore produce that list including its initial exponent. The total for both lists is at most $\Delta-\Delta/\nu+2S_0+16$. This produces the same scalar exponents with the scale factors retained throughout; each transmitted element still takes its own fixed-base generator multiplication. These recurrences also hold at $\tau=0$.

The key and non-key sparse right constants and the $J_Q+J_R$ quotient and remainder right constants are prepared once. Each associated right exponent multiplies its $\gamma_c$ by the corresponding constant, at one multiplication per slot. The search exponents are the precomputed leg scales. The mask power list uses the tabulated powers of $\upsilon$ multiplied by one constant for each grade and the appropriate monic-modulus factor in degree zero, with one multiplication per slot after combining these constants. The optional generator repeat adds no exponent work.





For the tag data of n1, obtain $L_1,L_2,L_3,L_\rho$ from the coordinate and key evaluation. The five fixed quotient numerators cost at most two products each. Their scaled first entries take at most two products each and their shifted copies one each. Including the fixed key factor, this fits 100 products. There is no direction-specific transmitted right list, and the other direction data are public system polynomials.

The fixed scalar tables and tower representatives use at most $70(n+J+1)+294810900$ multiplications. In particular the preceding Frobenius-table evaluations and the two combined weight arrays use at most $2n s_0+4n$ multiplications outside the coefficient-ring transformations already counted, and the $\upsilon$ power list uses at most $3n$. The conjugate digit evaluations use at most $s_0$ products each and at most $n s_0$ in total. The left, right and cell scale tables use at most $10(2K_1+3K_2+A_c)<35n$. Reuse the already computed $\tau^\nu$ and obtain $h=(\tau^\nu)^{\Delta/\nu}$ by binary powering. Here $1\le\Delta/\nu\le D<q<2^{254}$, so at most 508 scalar products suffice. Start the two lists with $Z_*(\tau)/\zeta_1$ and $Z_0(\tau)/\zeta_1$ using the cached inverse, and multiply the preceding value by $h$ in the next $J_Q-1$ or $J_R-1$ slots. The two sparse right constants use two more multiplications with the cached inverse of $\zeta_0$. This totals at most $J+510\le2J+600$, including at $\tau=0$ by starting with the specified constants. Evaluate the monic form modulus by Horner's rule with $n$ products. For each of the eight mask grades, multiply its listed scalar factors in the mask exponent formula, keeping the power of $\upsilon$ for the already charged slot product. The grade factor contains at most four scalar factors, including the inverse of $\zeta''$ and the modulus evaluation or signed epsilon scale where applicable. Even allowing four products per grade costs 32. The cofactor at $\rho$ times the public inverse derivative gives $L_\rho(\tau)$ in one product, then multiply by $\gamma_{\rm key}$ and finally by $\alpha$ for two more. The tag constants and shifts are covered by the preceding shared direction count. Thus the modulus, grade and key calculations take at most $n+35<10(n+J+10)$ multiplications. The remaining per-n coefficient is at most 52 besides $3n s_0$, with at most $12J+700$ further multiplications. This fits $70(n+J+1)+294810900$ since $n\ge3072$. Invert the bounded list of scale denominators, including $\varepsilon,\Omega_{22},\zeta_0,\zeta_1,\zeta'',\eta_2$ and the common $Z_*(\tau)$ used in n1. At most ten inversions and the additional fixed products are covered by 10,000 multiplications at the protected prime. All other operations for these arrays are additions, subtraction, or selection of entries.

The remaining finite scalar encryption terms sum to at most $V$ of C5. They include the cofactor products, shared mask forms, left and right factor multiplications, scaled power recurrences, the $(J+1)A_c+C_{\rm mask}$ correction slots, the fixed table and inversion allowances including the tower representatives, the bound $100$ for the fixed tag data, and the target exponentiations. Both target-group exponentiations use the same generator. Compute its multiples $2,\ldots,7$ with six successive products, and share that table. In each exponentiation scan 85 groups of three bits of its canonical 254-bit scalar, padding on the left. For every group use three squarings and at most one table product. Hence the two exponents and table use at most $6+2(85)(4)=686$ target-field products. At $276$ base-field multiplications per product, proved in Amendment search_spread, this costs at most $189336$ multiplications. The matrix bound includes both transforms, so there is no second conversion charge. The guard $W+V\le3m$ bounds the combined work throughout the admitted domain. Therefore the finite encryption uses at most $S_{\rm nz}+3m$ field multiplications, and the independently charged fixed-base source-group operations are exactly the ones on the published exponents.

### Efficiency and asymptotic choices

Amendments n1, n2 and the count amendments specify the exact finite work on every output of the designated setup of D. Each algorithm uses one seed query per matrix entry and at most one key query. All tag variants reuse the matrix. The fixed-degree ring operations cost $O(k(\ell+1)d_R)$, and the form maps and masks cost $O(n^2+n\log n)=O(n\log n)$ for the admitted $n\le4800$. The QAP algorithms take $O(D\log D+|S|)$ as in n1. Amendment search_spread accounts for the search and fallback.

### Deterministic scored setup

The C5 scalar coefficient layout and C6 modulus and Frobenius tables are fixed public data of this scored branch, computed from the displayed constants before instance setup. Runtime Setup references them without performing field generation or copying the tables. It scans the nonzero system terms and prepares the subgroup point encodings and shifted tables in D and n1, in the stated $O(|S|+D\log D+\log q)$ work. The fixed tables are independent of the input system and encryption coins and add no ciphertext data.

### Parameter selection and Corollary 5.8

Define the amended parameter selector on the public security level, domain, and external system shape. On the protected BN254 domain with security level 100 and the external benchmark shape, use the admitted parameters, the subgroup setup of D on any admissible input, and the changed algorithms. On every other domain, security level or external shape, take the protected original selector and use its original setup, encryption and decryption at that input. This public dispatch precedes parameter calculation. Only the first branch evaluates any entry amended here. In the second branch the original bounds, norm, sampler, field and ring parameters, point and coefficient placement, group counts and search algorithm all come from the original selector. Thus neither the statement nor the proof of the protected cor:asymptotics on the second branch uses an amended entry. Apply that protected result to the second branch with its unchanged hypotheses and original $\lambda$.

The statement of Corollary 5.8 for this selector has the same four bounds and scope: for linear-size systems with $N\ge\lambda^2$ in the designated subgroup placement, size is $O(\lambda N)$ field elements, encryption costs $O(\lambda^2N/\log\lambda)$, and decryption costs $O(\lambda N\log\lambda)$ outside its search with expected $O(2^{\lambda/4}N^{1/4})$ operations in the search. On the first branch $(\lambda,N)=(100,391693)$ is a single point. The explicit ciphertext count and the finite work proofs bound the costs on this branch uniformly over all admissible parameters, systems of that shape, and placements used in the cost statement. All ciphertext arrays and transform lengths are uniformly bounded by the shape and guards. Every allowable system has at most $1692(2\cdot2047+1)(391693+1)$ field coefficients in its ordinary form description, so even counting zero coefficients gives a fixed uniform bound on linear form work. All scalar and group operations outside the search use the fixed number of arrays, transforms and coefficients proved here. The elementary coefficient algorithms and the protected group implementation are over fixed finite fields, with finite worst-case costs per listed operation. The ordinary search has a fixed cap $B_{\mathrm{search}}<q/2$ and the fallback has cap $q$. Each uses the bounded traversals in Amendment search_spread. Uniform bounds also follow directly from the expected search estimate using $g^2\le2^{40}2^{100}$. Divide the four uniform costs by the corresponding positive scales at $(100,391693)$ and take the maximum with the original branch's constants. This yields uniform constants for the four bounds throughout $N\ge\lambda^2$.

Targets proves correctness and extraction for every admissible prescribed placement.

### Algebraic and reduction interfaces

For the Moore property, let $A$ be a field automorphism with fixed field $\mathbb F_q$. For any $d$ elements $x_i$ independent over $\mathbb F_q$, the $d$ rows of values $A^j(x_i)$, $0\le j<d$, are independent over the extension. Induct on $d$, with $x_1\ne0$ for $d=1$. If the square matrix had a nonzero kernel on the $i$ index, permute indices and normalize a nonzero coefficient to $c_d=1$. Apply $A$ to the equations for $j=0,\ldots,d-2$ and subtract the equations for $j=1,\ldots,d-1$. This gives a kernel relation with coefficients $A(c_i)-c_i$ on the $d-1$ independent elements $A(x_i)$, $i<d$, across $d-1$ successive powers of $A$. By induction all these differences vanish. The coefficients then belong to the fixed field, contradicting the equation at $j=0$ and the original independence. This gives the needed consecutive statement with $A=\sigma$, whose fixed field is $\mathbb F_q$.

Here is the full classification argument for the actual field ties of Amendment C7 with the specified $z$. Let $W_c$ be symmetric, pass the Booleanity tests, and satisfy the original three ties, with row space $\mathcal V$ of dimension $d\le3$ containing no kernel vector. The zero-dimensional case has zero stack. Let the columns of $U_*$ over $\mathbb F_q$ be a basis of $\mathcal V$, with rows $u_i^\top$. These rows span $\mathbb F_q^d$. For $s$ in $\mathcal I_*=\{n/2-1,n/2,n/2+1\}$, put $h_s=U_*^\top\sigma^s(z)$, and put $h_0=U_*^\top z$. Injectivity of $z$ on $\mathcal V$ means the entries of $h_0$ are independent over $\mathbb F_q$. In particular $d\le n$, and the Moore property proved above gives that the three $h_s$ span over $\mathbb F_{q^n}$. Write $W_s$ for $W_U,W_V,\sigma^{n/2+1}(W_U)$ in the indicated order. Each $W_s$ has its rows and columns in the extension of $\mathcal V$, so $W_s=U_* X_s U_*^\top$ for a unique symmetric $X_s$. Indeed a left inverse $L_*$ of $U_*$ exists, and $X_s=L_*W_sL_*^\top$; projections back to $\mathcal V$ act identically on the columns and rows. The ties give $X_s h_{s'}=X_{s'}h_s$. If $\sum_s a_sh_s=0$, then $(\sum_s a_sX_s)h_{s'}=0$ for every $s'$, and spanning gives $\sum_s a_sX_s=0$. Thus there is a linear map $X$ with $X(h_s)=X_s$. The trilinear form $C(h,u,v)=u^\top X(h)v$ is symmetric in the last two slots and in the first and last slots by the ties, initially on spanning $h_s$ and then on all vectors by linearity. It is therefore fully symmetric. Each Booleanity test gives $C(h,u_i,u_i-u_0)=0$ on the spanning $h_s$, hence on all $h$. The identities $X_s=\sigma^s(X_{n-s})$ for $s=n/2-1,n/2$ follow from the relation between the first and third matrices and because $W_V$ has even $T$-degrees and $\sigma^{n/2}$ fixes the scalar coefficients, as $U_*$ and $L_*$ have field entries fixed by $\sigma$.

First suppose $u_0\ne0$. Extend $l_0=u_0$ to a basis $l_0,\ldots,l_{d-1}$ chosen from the rows. For each $\delta\in\{0,1\}^{d-1}$, let $p_\delta$ satisfy $l_0^\top p_\delta=1$, $l_j^\top p_\delta=\delta_j$ for $j>0$, and set $w_\delta=U_*p_\delta$. Symmetry lets any repeated positive index in $C(l_i,l_j,l_k)$ be reduced via the test replacing one occurrence by $0$. Hence those values depend only on the set of positive indices present. Conversely the cube of the linear functional $p_\delta$ takes the value $\prod_{i\in A}\delta_i$ for this set $A$, and all sets occur since $d-1\le2$. The matrix of these values indexed by $A,\delta$ is invertible: indexing $\delta$ by its support gives the subset-incidence matrix, triangular with diagonal 1 in any inclusion-compatible ordering. Therefore
\[
 X(h)=\sum_\delta c_\delta(h^\top p_\delta)p_\delta p_\delta^\top
\]
for coefficients in the extension field. The squares $p_\delta p_\delta^\top$ are independent by the same evaluation matrix, now on pairs of basis vectors since $d-1\le2$. Write $z_\delta=z(w_\delta)=h_0^\top p_\delta\ne0$. Comparing coefficients of the squares in $X_s=\sigma^s(X_{n-s})$ gives $c_\delta\sigma^s(z_\delta)=\sigma^s(c_\delta)z_\delta$ for the two shifts $n/2-1,n/2$ that differ by one. Hence $c_\delta/z_\delta$ is fixed by $\sigma$, by composing one of the two fixing automorphisms with the inverse of the other. The Frobenius fixed field is $\mathbb F_q$. Write it as $\chi_\delta$. Returning from the matrix restriction gives $W_s=\sum_\delta\chi_\delta z_\delta\sigma^s(z_\delta)w_\delta w_\delta^\top$. In particular the first two polynomial representatives give the stack $\sum_\delta\chi_\delta\mathbf H(w_\delta)$.

Let $f$ be any field-linear test that vanishes on the cells. It vanishes on the $W_s$. Put $Q_*=\sum_\delta\chi_\delta f(w_\delta w_\delta^\top)p_\delta p_\delta^\top$, a matrix over $\mathbb F_q$. The vanishing gives $h_0^\top Q_* h_s=0$ for all three $s$, hence $h_0^\top Q_*=0$. Independence of the entries of $h_0$ over $\mathbb F_q$ implies $Q_*=0$, so independence of the squares implies $\chi_\delta f(w_\delta w_\delta^\top)=0$ for every $\delta$. Apply this to all Booleanity tests to deduce that any nonzero coefficient is on a Boolean assignment. If every external constraint test passes, apply the same argument to them to see that each supported assignment is a witness. In any representation by honest stacks of Boolean assignments in $\mathcal V$, the assignments equal some $w_\delta$ because their evaluations on the chosen basis fix their $p_\delta$. Hence the same test argument applies to any such representation.

If $u_0=0$, take any basis $l_1,\ldots,l_d$ from the other rows. Booleanity implies $C(h,l_i,l_i)=0$, so by symmetry every coordinate of the trilinear form with a repeated index vanishes. This gives zero if $d<3$. For $d=3$ its only possible value on distinct indices is a shared scalar $c$. Evaluating $X_s=\sigma^s(X_{n-s})$ on pairs of different basis vectors gives $c\, h_s=\sigma^s(c)h_0$ in the basis $l_1,l_2,l_3$, since $h_s$ is obtained from $h_0$ by Frobenius and the basis is over $\mathbb F_q$. If $c\ne0$, the first two consecutive vectors $h_s$ would both be proportional to $h_0$, impossible by the Moore independence of the three vectors in dimension three. So again $X=0$, and the stack vanishes. This proves the classification clauses, including that a nonzero usable stack in the stated case has a witness in its row space.

The rank and inverse clauses of $\mathrm{lem:heavy}$ are proved in Amendment msis_bound. For the packing clause, write $x\bmod q=a v$, $a\ne0$, for the kernel vector $v$. In either shortness convention $x_0=0$ since $v_0=0$ and $|x_0|<q$. Packing copies each of the $N_\star$ coordinates once and inserts zeros. It commutes with reduction, so $A\hat x=aA\hat v=0\bmod q$. For every infinity-short $x$ this gives $0<\|\hat x\|_\infty=\|x\|_\infty\le\beta$. For every Euclidean-short $x$ it gives $0<\|\hat x\|_2=\|x\|_2\le B_{\rm E}$. Only the second problem is costed.

### Degree, view and recovery gradients

Fix the seeded matrix and hence the form coefficients. For source exponents $a$ in G1 and $b$ in G2 include their generators. A guess-free target expression is
\[
 \mathsf E=\sum_{a,b}D_{ab}\,a b+D_K\alpha\kappa .
\]
The coefficients are fixed scalars. No source exponent uses $\alpha$. The factor $\varpi=\Omega_{22}\zeta_0\zeta_1\zeta''\varepsilon$ clears all denominators in every paired product. For degree accounting put $e_*=1$, since C6 uses one-variable representatives of degree below the form dimension. The degree of $\pi_a$ is at most $n+e_*$: the ordinary and conjugated left degrees are each at most $n-1$ and the two independent scalar factors are $\pi,\varepsilon$. The QAP factors have degree below $D$, and the hidden-basis matrix supplies at most one further factor. The sparse and shifted G1 powers have degree at most $D$ including scale, and the Y exponent has degree two. The fixed degree bound for G1 is therefore $d_1=D+n+2+e_*$. The degree of $\gamma_c$ is at most $n+2+2K_2$, since the right scale has ordinary degree at most $2K_2-1$ plus its one independent scalar. The key scale still has degree three.

The cleared sparse correction bases, of polynomial degree at most $D$, have degree at most $D+n+8+2e_*K_2$, which is at most the combined-list bound below since $D\ge4$. For the non-sparse list the polynomial part has degree at most $2D-2$ by P1 and the chunk domain. The cell scale and remaining clearing factors give at most $2D+n+4+2e_*K_2$. The first and second right coordinates before the masks have degree at most $D+n+6+2e_*K_2$ after clearing, by $k_{\rm leg}\le n-1$, the degree below $D$ of the QAP polynomials and the linear hidden-basis inverse. The partially reduced right term has smaller degree than its original product. Each original term of a right mask is a leg power of degree at most $n-1$ times a form of degree at most $n-1$, with one $\eta$ and an optional inverse $\varepsilon$. It has cleared degree at most $2n+5$. A cancellation basis has monomial degree at most $3n-3$ and cleared degree at most $3n+4$, including its scalar factors and clearing factors. Search bases have cleared degree at most $n+5$. Since $2n\le D$, all G2 exponents after clearing fit $d_2=2D+n+6+2e_*K_2$. The cleared key terms fit $D+8$. The product degree before a guessed-operand factor is at most $d_1+d_2=3D+2n+8+e_*(2K_2+1)$. By C5, $K_1\ge K_2+1$. Thus this bound is at most $d_f=3D+2n+2K_1+7$. The extra guess factor of degree one and all listed separate bounds fit $(q-D)\varepsilon_f$ by its protected formula. The search coordinates enter only linearly, within the same degree bounds.

For any fixed $r$, the valid scalar coin sets are independent with sizes at least $q-D$, including the two exclusions on $\varepsilon$ and the $D$ exclusions on $\tau$. The clearing factor is nonzero there. The product-set bound proved in Targets shows that an identity holding on all valid coins is a polynomial identity after clearing, because $d_f<q-D$ by P5 and $\varepsilon_f=(d_f+60)/(q-D)$. A nonidentity has coincidence probability at most $d_f/(q-D)\le\varepsilon_f$. At an identity $\mathsf E=\chi\kappa$ the coefficient of $\alpha$ gives $D_K=0$, since $\kappa$ is a nonzero polynomial. All stack comparisons henceforth use only the plain factor sector.

Write the two transformed left exponents as $F_1^{a,i}=\pi_a y_i$ and $F_2^{a,i}=\pi_a(\Omega_{12}y_i+\Omega_{22}A_i)$. The right exponents are
\[
 H_1^{\mathrm{leg},j}=\ell_{\mathrm{leg},j}
       -(\Omega_{12}/\Omega_{22})s_{\rm leg}(B_j-y_j),\qquad
 H_2^{\mathrm{leg},j}=s_{\rm leg}(B_j-y_j)/\Omega_{22},
\]
where $\ell_{\mathrm{leg},j}=s_{\rm leg}(r_j+A_j)+\vartheta_{\mathrm{leg},j}$ is independent of the hidden basis. No other G2 input contains a hidden-basis variable. For any G1 input $a$ denote its evaluation at $\Omega_{22}=0$ by $\widetilde a$; for $F_2^{a,i}$ this is $\Omega_{12}F_1^{a,i}$. Take the part of the Laurent identity with $\Omega_{22}^{-1}$ and positive degree in $\Omega_{12}$. Cancel its common factor $-\Omega_{12}/\Omega_{22}$. The resulting identity is
\[
 \sum_{a,\mathrm{leg},j}\delta_{a,\mathrm{leg},j}\,\widetilde a\,s_{\rm leg}(B_j-y_j)=0,
\]
where $\delta_{a,\mathrm{leg},j}$ is the coefficient of the pair with $H_1^{\mathrm{leg},j}$, subtracting the matched coefficient of $F_2^{a,i},H_2^{\mathrm{leg},j}$ if its G1 input is $F_1^{a,i}$. This follows because only a second left coordinate produces a positive $\Omega_{12}$-degree when paired with $H_2$. Substitute $y_i=B_i(\tau)+z_i$ with independent indeterminates $z_i$. Then $B_j-y_j=-z_j$, so the coefficient of $z_{j_0}$ is $-\sum_{a,\mathrm{leg}}\delta_{a,\mathrm{leg},j_0}s_{\rm leg}\widetilde a(B)$ and is zero. Any $z_i$ term of $\widetilde a(B+z)$ contributes degree two, hence cannot enter. The fixed index is $j_0$; no factor $B_{j_0}$ remains.

The left-input types in the sum are $1,\zeta_0 p(\tau),\zeta_1\tau^v,\zeta''B_i,\pi_a B_i,\Omega_{12}\pi_a B_i$, separated by degrees in $\zeta_0,\zeta_1,\zeta'',\pi,\Omega_{12}$. The polynomials $p$ include the sparse powers and the fixed quotient difference polynomials. In the first four types the monomials $s_{\rm leg}=s_{\mathrm X}\upsilon^{k_{\rm leg}}$ distinguish the legs in each kind. The $\zeta_1$ powers are distinct and the $B_i$ are independent by their $d_j$ values. The polynomials in the $\zeta_0$ type need not be independent: the identity says for each leg and right coordinate $j_0$ their coefficient-weighted sum is the zero polynomial in $\tau$. In this type each $\widetilde a$ is the full first input independent of $y$ and the hidden basis, so its aggregate ordinary pairing with that $H_1^{\mathrm{leg},j_0}$ vanishes at every coin and every $r$. For the last two types use the constant term in $\varepsilon$, giving the distinct cell monomials $\pi s_{\mathrm X}\upsilon^{k_c}$. For each of their coefficients and each $j_0$, the relation is linear in $B_i(\tau)$; evaluating the polynomial relation at $d_i$ isolates its $i$-th coefficient by Amendment D. Thus the matched factor coefficients agree individually and all unmatched first-right terms cancel identically as sums, which is sufficient both for the class comparison and the derivative. Formal projection onto first-left factors continues to respect formal equality and receives no contribution from the $\zeta_0$ type.

In the multidegree with one $\pi$ and zero degrees in $\zeta_0,\zeta_1,\zeta''$ and net hidden-basis degree, the pairs are the matched factor products, first-left pairs with the search bases and generator, the correction lists in two matching inverse-scale classes, and the Y column with cancellation bases. This enumeration follows by checking the degrees of the published exponents: the left first factors have one $\pi$, the left second also has one hidden-basis degree, and the three other nonconstant left types carry only one of the three scales. The right factor scales and correction types above are their only complementary types. The left-generator pair with any published right exponent of degree one in $\pi$ has an inverse scale and cannot enter this class. Define $W_c$ by matched factor coefficients, and $u_c$ by minus the first-left search-pair coefficients. The class identity is
\[
 \sum_c\gamma_c b_c+\Phi_*=\chi\kappa,\qquad
 b_c=y^\top(W_cr-u_c)+y^\top(W_c-W_c^\top)A(\tau)
              +(P_{W_c}+Z_c h_c+Z_0 R_c)(\tau).
\]
Here the two correction types produce $Z_c h_c+Z_0R_c$ with allowed $R_c$, by the residue-preserving monic division proved in n1. The term $\Phi_*$ collects the masks from the factor products, the Y cancellation products and the first-left generator pairs. It is free of all $s_{\mathrm X}$. Taking the constant term in $\varepsilon$ and the coefficients of the distinct $\pi s_{\mathrm X}\upsilon^{k_c}$ gives $b_c=0$ except at the key cell, where $b_c=\chi L_\rho$. The original identity then also gives $\Phi_*=0$.

For each $c$, the linear coefficient in $y$ at $d_0$ gives $W_c r=u_c$. The same comparison at $\rho,d_i$ shows $W_c-W_c^\top$ vanishes on the spanning vectors in Amendment D, hence $W_c$ is symmetric. The constant coefficient gives $\deg Z_c h_c\le2D-2$ since the $P_{W_c},Z_0R_c,L_\rho$ terms have that bound. Thus $\deg h_c<D$ for a non-key cell or $<D-1$ in the key cell. The QAP identities in Amendment D give all Booleanity and constraint tests, with the ordinary or keyed vanishing factor as applicable. In particular the Booleanity tests follow first by checking the $d_i$, where the key polynomial is zero. In the key cell evaluate then at $\rho$ where the two vanishing factors are zero. The Booleanity equalities reduce $P_{W_c}(\rho)$ to $(W_c)_{\mathsf b_1,\mathsf b_2}$ in the new key evaluation. Therefore $(W_c)_{\mathsf b_1,\mathsf b_2}=\chi$. In the coefficient of each $\eta_i$ in $\Phi_*$ at degree zero in $\varepsilon$, the mask part is $\pi y^\top t_i(\upsilon)$. The remaining terms there are the Y pairs with multiples of $P_T(\upsilon)$; the other grades and generator pairs do not contribute. Comparing the $y_j$ coefficients and substituting the form generator for $\upsilon$ therefore gives all three actual ties from the honest cancellation derivation.

If $r'$ replaces $r$, the coefficient-matching result shows the difference in the target value is $\sum_c\gamma_c y^\top W_c(r'-r)$, because no other exponents depend on $r$. Thus the identity remains valid throughout its prescribed locus. If all stacks are zero, it holds formally at every $r'$ and the key corner forces $\chi=0$. If an identity is formal for all $r$, its equations $W_c r=u_c$ for every $r$ force all $W_c=0$ and again $\chi=0$. A difference of source expressions pairs with the other source generator to an expression of zero stack. If it vanishes identically at any fixed $r$, this argument says it is formally zero, so formally different source expressions have the stated coincidence bound. This proves the view clauses with the new corner and one actual sector.

The formal derivative of the target expression with respect to the search coordinates, for a marked identity, is the vector $\sum_c\gamma_c W_c^\top y$. To compute it use the private evaluation and reverse accumulation of the reduction. At each recovery point project the G1 input polynomials by setting $\Omega_{12}=\Omega_{22}=0$ and taking the part linear in $\pi$; these are exactly the first left coordinates. This is a linear projection and therefore respects formal equality of G1 expressions. The derivative of a G2 leaf is nonzero only for a first right coordinate and is $s_{\rm leg}$ times the corresponding coordinate vector. The matched $F_1,H_1$ coefficients are precisely the coefficients of the projected product in the derivative. Since unmatched first-right coefficients vanish for a marked identity, this is its full stack gradient. Formally equal targets have zero difference stack and the same gradients; formally equal G2 inputs also have equal derivative records by pairing their difference with a first-left input and applying the zero-stack result. The projected gradients always lie in the marked row space. For a nonzero linear functional on it that vanishes on a given proper subspace, the derivative polynomial after dividing by $\pi$ is nonzero: take its degree-zero coefficient in $\varepsilon$ and the distinct monomials $s_{\mathrm X}\upsilon^{k_c}y_i$. Its degree is at most $n+2+2K_2$, establishing the recovery comparison used in Targets. The optional empty alpha sector has identically zero stack and gradients.

The running time with the revised exponent lists has the bound
\[
 t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT},\qquad
 C_R=8I+3L+2C_{\rm post}+C_{\rm set}+C_{\rm desc},
\]
with $I$ for computing the initial exponents at one point, $C_{\rm post}$ for processing one tried expression, $C_{\rm set}$ for fixed transcript initialization, and $C_{\rm desc}$ for the description. Here $I,C_{\rm post},C_{\rm set},C_{\rm desc}$ are the costs for the revised exponent lists, and $C_R=O((N_\star+n)D+\mu)$. We give the dependence on the form indices explicitly.

The per-call bound can be checked by the following implementation in the reduction's unit-operation model. Keep per group a table of assigned exponents indexed both by label and by field value, and a label table status for excluded strings. Both allocated and excluded strings are keys of the same label table, so unused-string sampling excludes both. A label record includes its value at the independent test point and a reference to its first expression node, if any. The reference or zero record is kept on repeated assignments. For an unclassified operand in an addition, scalar product or pairing, keep counters of the remaining exponents and unclassified strings in its group. Draw an integer uniformly below the latter count and compare it to the former count to decide membership. If it is a label, sample a uniformly unused exponent. Insert the relevant forward and reverse entries and update the counts. A rejection only writes its status and updates the unclassified-string count. This gives at most eight operations per unclassified operand: one status lookup, one integer sample and comparison, one exponent sample, two insertions and two counter updates. The conditional laws follow from a uniform injection after the already assigned and excluded labels have been fixed. Record-less labels in answered calls use the common zero expression, at most two further record writes per call.

For a result, allow at most 24 main operations. This includes two lookups of operands and up to three arithmetic operations each at the true and private test points. A result-label lookup, a fresh unused string sample when needed, and the two table insertions use at most four more. Updating both counts uses two. Allow six writes for an expression node (operation tag, operand references, scalar operands if needed, and result reference). The remaining four cover the private-value comparison, recording the first differing target pair, advancing the expression-log index, and checking or recording eligibility for name calls. A name call uses the same routine for negation, and then returns the two labels, with at most two label writes. It is rejected if the input's eligibility flag is absent. Repeated name calls return the already assigned opposite exponent label. An insertion at a known exponent leaves the old reverse entry in place and the private comparison uses its stored record.

For the at most six recovery passes, the forward evaluation at each point takes at most three arithmetic operations per logged gate. The private test point above uses the full exponents. At recovery points, the projected first-left values and the single-sector first-right derivative leaves are prepared before the call loop as described above. Only the right operand of a pairing can contribute a derivative in $r$, as every G1 value is independent of $r$. For each of the at most two trial expressions, traverse the resulting straight-line expression log backwards. A sum or scalar multiplication adds the adjoint times the corresponding scalar derivative to the adjoint of each predecessor. A pairing uses the evaluated first operand as its derivative with respect to the second. For a predecessor that is an input leaf, skip it if its derivative is zero in the current sector. Otherwise it is a first right coordinate with derivative equal to one prepared field scalar times the coordinate vector for its index $j$; directly accumulate the adjoint contribution times this scalar in coordinate $j$ of the gradient. This is at most three field operations for each of two precursors: a product by the gate derivative, an additional product for a leaf, and an accumulation. A non-leaf involves just the first product and accumulation. The references in the stored log give direct accesses to indexed registers, and each field operation computes its result in its destination register. Neither uses a label-table lookup. Initialize all node adjoint registers to zero before each reverse pass, using one field write per node and pass, then set the starting adjoints for the trial. These updates compute the derivatives by the chain rule in reverse order. Each recovery point therefore costs at most $3+2(6+1)=17$ operations per call for both expression trials. Initializing the output vectors and the at most two starting adjoints per trial is fixed postprocessing. Including six passes, the call bound is at most $24+2\cdot 8+2+2+6\cdot17=146\le148$. A fresh key-oracle answer takes one lookup, sample and insertion. A fresh seed-oracle answer replaces its one sample by $d_R$ coordinate samples. This gives $(d_R+5)Q_H$ when each oracle has at most $Q_H$ queries.

Only fixed inputs and setup change. The public dense matrices, digit spectra and fixed division data take $O(n^2)$ field elements of description. Applying the dense table maps at each private point takes $O(n^2)$ operations, within $O(nD)$. Computing the initial exponents at each of at most eight points evaluates $O(N_\star)$ degree-below-$D$ QAP polynomials, advances powers through lengths $O(D+n)$, and forms the $O(nD)$ scalars in the split QAP group arrays. For the mask vectors, naive transposed ring multiplication takes $O(nd_R+nN_\star)$ work, bounded by $O(nD+nN_\star)$ since $d_R\le n\le D$. Source factor entries take $O(nN_\star)$ further operations. For postprocessing, apply the full form map to at most three vectors per sector by naive ring multiplication and solve a fixed-width linear system. The same $O(nD+nN_\star)$ bound covers this before LIFT. Initialization queries and stores the same ring entries and creates the group label records with at most $O((N_\star+n)D+\mu)$ operations, including masking. The fixed instance QAP polynomials and form indices fit the same size as advice in the protected cost model. Hence $C_R=O((N_\star+n)D+\mu)$. The lifting step is called at most twice, once per tried expression. This establishes the bound above and the stated $t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)$ specialization.

This accounts for the background list for the forms and weights block. The generic record and mark bounds depend on the degree, view, sampler and label counts. The degree and view properties needed for the repacked construction are proved above. The extractor sketches only use the coefficient arrays of the left and right factors, independently of the internal representation of the form list.


## Amendment P1

Require $\Delta\le D$, $J=\lceil(D-1)/\Delta\rceil+\lceil\nu n_{\mathsf c}/\Delta\rceil$, $J'=1$, $\nu\mid\Delta$, and $n\le D$. These are $J_Q$ quotient chunks of length $\Delta$ spanning $[0,D-1)$, and $J_R$ remainder chunks spanning $[0,\nu n_{\mathsf c})$. The quotient right multiplier has degree $D$; the remainder right multiplier has degree $D-\nu n_{\mathsf c}$. A complete allowed interval therefore produces terms of degrees at most $2D-2$ and $D-1$, respectively, when truncated at the supported coefficient lengths. The formal comparison permits every padded position. The ceiling definition gives $(J_Q-1)\Delta<D-1$. This bound on the integer highest quotient shift is at most $D-2$, so its right source polynomial part has degree at most $2D-2$. Likewise the highest remainder shift satisfies $(J_R-1)\Delta<\nu n_{\mathsf c}$, so its right source polynomial part has degree below $D$. The bounds in C7 apply before imposing any honest coefficient restrictions. All shifts are multiples of $\nu$.

## Amendment n1

There are
\[
 n_1=(2K_1+1)(N+4)+2\lceil(D-1)/\nu\rceil+\Delta-\Delta/\nu+10
\]
transmitted G1 elements. Use the single factor sector, field mask bases and Y column of C7. Let $S_0=\lceil(D-1)/\nu\rceil$ and
\[
 I_0=\{0\le a<D-1:\nu\mid a\},\qquad
 I_0^*=I_0\cup\{a+1:a\in I_0\},\qquad
 I_1=\{0\le a<\Delta:\nu\nmid a\}.
\]
Send $P_a^0=[\zeta_0\tau^a]_1$ for $a\in I_0^*$, and $P_a^1=[\zeta_1\tau^a]_1$ for $a\in I_1$. There are $2S_0$ sparse entries because $\nu\ge2$, and $\Delta-\Delta/\nu$ non-sparse ones since the chunk width is a multiple of the coset size. Use $Z_c=Z_*$ in the key cell and $Z_c=Z$ elsewhere. Send one $B_c^0=[\gamma_c Z_c(\tau)/\zeta_0]_2$ per cell and two families of bases
\[
 B_{c,j}^{Q}=[\gamma_c Z_*(\tau)\tau^{j\Delta}/\zeta_1]_2\quad(0\le j<J_Q),\qquad
 B_{c,j}^{R}=[\gamma_c Z_0(\tau)\tau^{j\Delta}/\zeta_1]_2\quad(0\le j<J_R).
\] The factor arrays, search bases and cancellation arrays are those of C7, each once. Add the tag quotient difference bases below and then apply the same optional existing-generator parity padding, computed as one scalar multiplication by one. Send the seed, the one element $[\alpha\kappa]_T$, and the masked message. There is exactly one fixed-base generator multiplication per transmitted group slot and one more in GT for the key. All scalar exponents use the displayed fixed factors and tabulated powers, with constant work per exponent.


### Common tag direction from the power arrays

Write $d_1',d_2',d_3'$ for the three tag Booleanity points, $L_1,L_2,L_3$ for their QAP Lagrange polynomials, and $A_i,B_i$ for the coordinate polynomials of tag $i$. The new key evaluation gives
\[
 A_i=B_i=L_i+c_*L_\rho \quad(i=1,2),\qquad A_3=B_3=L_3 .
\]
For an ordinary coordinate $j=0,\ldots,N$ let $S_j=A_j^{\rm o}+B_j^{\rm o}$. Define the three-root factor and common direction polynomials by
\[
 U=(X-d_1')(X-d_2')(X-\rho),\qquad
 G_j=\frac{S_j+\mathbf1_{j=0}(L_1+L_2+c_*L_\rho)}{U}.
\]
At both tag points in $U$, the sum of the ordinary A and B vectors is $-e_0$; at $\rho$ this sum is $-c_*e_0$. Thus each $G_j$ is a polynomial of degree at most $D-4$. Also $U A_i$ is a multiple of $Z_*$ for $i=1,2$: outside $U$'s three roots the Lagrange polynomial $A_i$ vanishes at every QAP point. It has degree at most $D+2$.

Define five fixed polynomials
\[
 F_i=-\frac{A_i L_{3-i}}{Z_*}\quad(i=1,2),\qquad
 F_{i,i'}=\frac{2A_i A_{i'}-\mathbf1_{\{i,i'\}=\{1,2\}}L_\rho}{Z_*}\quad(i<i').
\]
Each numerator vanishes at all QAP points: $A_i$ has nonzero point values only at its own tag point and $\rho$, and $L_{3-i}$ only at the other tag point; two distinct tag coordinate polynomials overlap only for tags one and two at $\rho$, where the product with factor two is $2c_*^2=1$. The degrees of these quotients are at most $D-2$. Send $[\zeta_0 F(\tau)]_1$ and $[\zeta_0(\tau-\rho)F(\tau)]_1$ for each of these five fixed polynomials. These are the ten additional left slots. All remaining tag correction operands use the ordinary sparse and non-sparse powers and already counted right bases.

As before all full combinations use the same third tag $t$. Let $v_0=(w,0,0,t)$ and $v=(w,b_1,b_2,t)$, and let $d_v=b_1b_2$. They have the same allowed remainder $R_w$. Put $G_w=\sum_{j=0}^Nw_jG_j$ and
\[
 F_v=b_1F_1+b_2F_2+b_1b_2F_{1,2}+tb_1F_{1,3}+tb_2F_{2,3}.
\]
For either $i=1,2$, the part of $P_v-P_{v_0}$ linear in $b_i$ excluding mixed terms is $A_i(S_w+A_i)$, where $S_w=\sum_jw_jS_j$; this uses $b_i^2=b_i$. By the definition of $G_w$ and $w_0=1$,
\[
 A_i(S_w+A_i)=U A_i G_w-A_i L_{3-i}.
\]
The mixed terms are the three products already handled in the $F_{i,i'}$, including the subtraction of $d_vL_\rho$. Hence the exact polynomial identity is
\[
 P_v-P_{v_0}-d_vL_\rho=U(b_1A_1+b_2A_2)G_w+Z_*F_v.
\]



For $i=1,2$ compute $Q_i=(UA_i/Z_*)G_w$, of degree at most $D-2$. Write $Q_i^0,Q_i^1$ for its parts on powers divisible and not divisible by $\nu$. From the sparse powers and their one-step shifts obtain
\[
 D_i^0=[\zeta_0 Q_i^0(\tau)]_1,\qquad
 D_i^{0,+}=[\zeta_0(\tau-\rho)Q_i^0(\tau)]_1 .
\]
The shifted MSM is followed by subtraction of $\rho D_i^0$. For each quotient chunk form the precomputed witness-direction operand
\[
 D^1_{i,j}=\sum_{\substack{a\in I_1\\j\Delta+a<D-1}}[X^{j\Delta+a}]Q_i^1\,P_a^1 .
\]
It is added to the baseline quotient operand if $b_i=1$. The quotient family of right bases restores $Z_*Q_i^1$ upon summing the chunk pairings. The remainder operands are reused for each variant.

At the sparse operands add $\sum_i b_i D_i^0$ for the key and $\sum_i b_iD_i^{0,+}$ for the other cells, along with the existing fixed entries for $F_v$ and its shift. The non-key operand still receives $d_v P_0^0/Z(\rho)$. Therefore the added sparse terms give $\gamma_c Z_*\sum_i b_i Q_i^0+\gamma_c Z_*F_v$ at each cell. Along with the non-sparse terms and the baseline, these are exactly the required subtractions $P_v-d_vL_\rho$ and $P_v$ in the key and other cells.

### A single combination at any tag

Put $U_*=(D-1)+\nu n_{\mathsf c}$. For $v_0=(w,0,0,t)$ the key corner is zero. By D the exact quotient $G_{\rm base}=P_{v_0}/Z_0$ is $Z_{\mathcal K} h+R_w$. Use ordinary monic division in each residue modulo $\nu$: since $Z_{\mathcal K}$ is in $\mathbb F_q[X^\nu]$, both the quotient and remainder operations preserve each residue. Write $h=h^0+h^1$ for its parts with zero and nonzero residue. The witness condition makes $R_w$ have only nonzero residues. The two sparse left operands are evaluations of $\zeta_0 h^0$ and $\zeta_0(X-\rho)h^0$ with the corresponding powers and the fixed $-\rho$ shift. For each full variant, apply the sparse adjustments above and pair against the weighted key and non-key lists $B_c^0$. Independently compute chunk MSMs of the coefficients of $h^1$ and $R_w$ into the existing non-sparse left powers. Add the selected direction operand $D^1_{i,j}$ to each quotient chunk and pair against the weighted $B^Q_{c,j}$ list. Pair the remainder chunks against the weighted $B^R_{c,j}$ list. Their sum evaluates $Z_* (h^1+\sum_i b_iQ_i^1)+Z_0R_w$, with cell weights and scales. Together with the sparse terms it provides exactly the polynomial subtractions required in each cell.

For formal comparisons, arbitrary polynomials with the available nonzero-residue support multiplied by $Z_*$ may be absorbed into $Z_c h_c$: for a non-key cell use $Z_*=(X-\rho)Z$. For the family multiplied by $Z_0$, divide its nonzero-residue polynomial part by $Z_{\mathcal K}$ and absorb the quotient by the same identity. Its remainder has degree below $\nu n_{\mathsf c}$ and nonzero residues. These facts give the extraction view with the same allowed remainders; the degree of the actual $h_c$ in an identity follows after comparison with $P_{W_c}$ and $L_\rho$ as in C7. They hold at every admissible prescribed point choice. For points outside the finite subgroup one computes the same $G_{\rm base}$ and direction polynomials by general polynomial interpolation and exact division. Products, interpolation and monic divisions can use power-of-two FFTs with block splitting and doubling-precision inversion. There are no additional ciphertext inputs for this implementation.

For each right leg, form the two weighted left operands by summing $\xi_c(v)$ times the witness-summed G1 factor of its left leg over the cells at this right leg. Pair them with the two witness-summed right coordinates. In the resulting sum the hidden basis cancels, the two antisymmetric terms $y(v)A_v-A_v y(v)$ cancel, and the masks are subtracted with the cancellation MSM of C7 paired against the witness-summed Y. The earlier polynomial subtractions remove all $P_v$ terms except the stated key corner. The first weighted left operand alone is the sum of the left first coordinates; pairing it separately with the search base $s_{\rm leg}$ at each right leg and summing gives
\[
 \Psi_v=[\psi_v]_T,\qquad \psi_v=y(v)\sum_c\gamma_c\xi_c(v).
\]
The full corrected sum is
\[
 \Lambda_v=[d_v\xi_{\rm key}(v)\kappa+r(v)\psi_v]_T .
\]
To evaluate just $\Psi_v$ there is no use of the second factor coordinate, QAP correction or cancellation.

### Finite work of the scalar baseline

For the scored subgroup placement put $M=2^{22}$, $L=2M$, and choose a public scalar $c$ of order $2L$. Then $c\mathcal H_L$ and $\mathcal H_M$ are disjoint. The public system representation can include the fixed interpolation scalars and tables used below. They depend only on the selected points and field and are determined when the system is encoded. They add no group element or field value to the ciphertext.

For the ordinary polynomials $F=A_{(w,0,0,0)},B_{(w,0,0,0)}$, partial fractions give
\[
 F(X)=\frac{Z_*(X)}{X^M-1}
      \sum_{j=0}^{M-1} X^j\sum_{p\in\mathcal P}\frac{F(p)p^{-1-j}}{Z_*'(p)} .
\]
Indeed the partial fraction identity for $F/Z_*$ holds by evaluation at all QAP points, and multiplying each term by $X^M-1$ gives the geometric sum because $p^M=1$. Encode each public point coefficient with its fixed factor $1/Z_*'(p)$. After additions selected by the witness bits, multiply the aggregate value for each point by its fixed $1/p$ to obtain the exact transform input weight from the displayed identity. Both arrays take at most $2D<8$ million multiplications for this normalization. Encryption uses the same encoding and the cofactor product proved in C7.

For each polynomial use one length-$M$ transform for the coefficient array and one on each of the two cosets of $\mathcal H_M$ in $c\mathcal H_L$. Coefficient scaling costs at most $4M$ multiplications across both polynomials. Before adding the third tag, compute $G_w(x)$ on $c\mathcal H_M$: multiply the sum of the two numerators by $Z_*(x)/((x^M-1)U(x))$ and add the public correction $(L_1(x)+L_2(x)+c_*L_\rho(x))/U(x)$. Apply an inverse transform to the $M$ values and undo the shift. This takes $T(M)+3M$ products including inverse normalization. Each fixed quadratic $UA_i/Z_*$ has at most three coefficients, and $\deg G_w\le D-4$, so multiplying by both quadratics takes at most $6(D-3)$ products. The complete direction budget is $77\,667\,419$.

When $t=1$, add the precomputed numerator entries for tag three at each shifted point. Their values come from $F_{\rm tag,3}(x)(x^M-1)/Z_*(x)$ for $F=A,B$; no decryption multiplication is needed for adding a bit-selected fixed entry. At each shifted point multiply the two numerators and the fixed factor $Z_*^2/(LZ_0(X^M-1)^2)$. Apply the unnormalized inverse transform of length $L$ and undo the coset shift on the first $U_*$ coefficients. The degree is below $U_*<L$, so the recovered coefficients of $G_{\rm base}$ are exact. With $T(B)=B\log_2(B)/2-(B-1)$ nonunit radix-two twiddles at length $B$, this costs at most $2D+6T(M)+4M+2L+T(L)+U_*=388\,329\,020$, including input normalization.

In each residue modulo $\nu$, reverse the coefficient list of $G_{\rm base}$ at its padded upper degree, and convolve with the precomputed inverse of the reversed monic $Z_{\mathcal K}(X)$ viewed in the variable $X^\nu$. The first at most $S_0=1884$ coefficients, reversed back, give the quotient; this follows by comparing the highest terms in the division identity. Compute the remainder by subtracting the quotient times the fixed monic divisor. Reciprocal and divisor spectra both fit length 4096: the first product has length at most $2\cdot1884-1$ after truncating the reversed dividend, and the second at most $1884+1692$. Each fixed-kernel product needs a forward transform, an inverse transform, at most 4096 pointwise multiplications and at most 4096 inverse scalings. The total division charge is $2\nu(2T(4096)+8192)=201\,334\,784$. Public scalar tables depend on the setup points, have length $O(D)$ for the QAP transforms and add no ciphertext slots.

For the scalar matrix sum the ordinary and homogeneous columns selected by the witness bits, then read the three separate tag columns. Append the corresponding fixed-row sums and tag values from Amendment n. This uses only selection and additions of public coefficients, since the ordinary coordinates are bits. Keep the conservative allowance $5(n-1)$ products used by the displayed ledger. Place the four resulting vectors in the form basis. C6 bounds each of their three Frobenius maps by $n s_0$ products, even charging the half-turn signs in that allowance. The eight variant vectors and their conjugates are assembled by sums.

For each variant compute the two products by ordinary convolutions of length 8192, which covers degrees below $2n$. At length $u$ each product costs at most $3T(u)+2u$ including normalization. Reduce each product by descending degree against $P_T=P_c(T^{r_H})$. There are at most $n$ leading terms to eliminate, each with at most $s_0$ fixed-coefficient products. Thus all weights cost at most
\[
12n s_0+16(3T(u)+2u+n s_0)=167517864 .
\]

For a full combination form $D_{\rm leg}=\sum_a\xi_{a,\rm leg}T^{\lambda_a}$ and $C_{\rm leg}=\sum_a\xi_{a,\rm leg}F_{\lambda_a}$ for each right leg. There are at most $K_1$ left digits per leg and at most $s_0$ monomials per conjugate digit. Their total is at most $7K_1K_2s_0$ products. Four of the six weighted aggregate leg polynomials use shifts and sums. The other two sum at most $2K_2$ products each with fixed conjugated right polynomials. For these sums transform each dynamic operand at length $b=16384$, multiply pointwise by the fixed public right spectrum and add the resulting spectra within each sum. Two inverse transforms recover the aggregate polynomials. Including their normalizations this takes at most $(4K_2+2)T(b)+(4K_2+2)b$. The nine forward transforms, twelve pointwise products and eight inverse transforms for the eight masks then cost at most $17T(b)+20b$. The selected length covers all the product supports below $3n$. The three exact quotient divisions by $P_T$ use at most $2n$ leading eliminations each, at most $s_0$ products per elimination. The full mask work is at most
\[
7K_1K_2s_0+(4K_2+19)T(b)+(4K_2+22)b+6n s_0=66040786 .
\]
The remaining arithmetic uses at most 1018 products for normalization and the fallback, since each inversion takes at most 508 by binary powering. The QAP costs sum to $388329020+77667419+201334784=667331223$. Including four masks the scalar bound is
\[
 667331223+167517864+4\cdot66040786+17165+1018=1099030414 .
\]
This is below $632000000+m$ since $m=k(\ell+1)$ and $\ell=N+3$ by the unit packing. Search and group work are charged separately. Every transform length, fixed spectrum and form table is public and independent of the encryption coins.

### Tag choice and key recovery

For any external witness $w$ and $t\in\{0,1\}$, set $a_t=(w,1,0,t)$, $b_t=(w,0,1,t)$, $c_t=(w,0,0,t)$, and $v^{(t)}=(w,1,1,t)$, all with homogeneous coordinate one. The three ordinary corners have zero key corner and $a_t+b_t-c_t=v^{(t)}$ as integer vectors. The target has key corner one.

Return $\bot$ if $\xi_{\rm key}(v^{(0)})=0$. Otherwise if $\Psi_{v^{(0)}}=0$, compute its one full combination and normalize directly with its nonzero key weight. If the primary target base is nonzero and $\Psi_{a_0},\Psi_{b_0},\Psi_{c_0}$ are all nonzero, choose the ordinary triple with $t=0$. Otherwise test $\xi_{\rm key}(v^{(1)})$. If it is zero, take the evaluation-point fallback. With nonzero secondary weight, compute $\Psi_{v^{(1)}}$. If that base is zero, use its direct normalization. If it is nonzero and $\Psi_{a_1},\Psi_{b_1},\Psi_{c_1}$ are all nonzero, select the ordinary triple with $t=1$. Otherwise take the fallback. This uses at most eight plain base tests and four full combinations. All full combinations in the chosen path have common third tag $t$, so they need one baseline. Let $v_*$ denote the selected target in an ordinary branch. Branch selection depends only on the bases and form weights, independently of the search coins.

For the selected triple, use $v_0'=c,v_1'=a,v_2'=b$ and let $c_0,c_1,c_2$ denote the rounded centers of the anchor and differences. Before starting line [full-search], form
\[
 Q_0=\Lambda_c-c_0\Psi_c,\qquad
 Q_1=\Lambda_a-(c_0+c_1)\Psi_a,\qquad
 Q_2=\Lambda_b-(c_0+c_2)\Psi_b .
\]
The line solves $Q_0=t_0\Psi_c$, then solves $Q_1-t_0\Psi_a=t_1\Psi_a$ and $Q_2-t_0\Psi_b=t_2\Psi_b$. The two multiplications by the already recovered $t_0$ use signed binary arithmetic on $|t_0|$, with sign handled by the fixed Frobenius inversion. These are the only group products that translate targets within the search. The output is the three centered logarithms in the record below. The later key computation forms $r(v_*)=c_0+c_1+c_2+t_0+t_1+t_2$, subtracts $r(v_*)\Psi_{v_*}$, and multiplies by the inverse key weight. This gives $[\kappa]_T$. One key-oracle query unmasks the message. At most eight $\Psi$ values and four full $\Lambda$ values are needed, and the triple choice is independent of the search vector.

### Exact fallback when no ordinary triple is available

This fallback runs only after the nonzero key-weight test has passed and the target base is nonzero, when the selector supplies neither a triple with nonzero target weight nor a direct normalization. The sparse G1 list contains $P_0^0$ and $P_1^0$ because $0\in I_0$ and $1\in I_0^*$. Before entering the unified search line, pair each one with the published key-cell operand $B^0_{\rm key}$. The results are
\[
 E_0=[\gamma_{\rm key} Z_*(\tau)]_T,\qquad
 E_1=[\gamma_{\rm key} Z_*(\tau)\tau/c_{\rm q}]_T ,
\]
where $c_{\rm q}=1$ for unscaled powers. The exponent of $E_0$ is nonzero because the key scale is nonzero and $\tau$ is outside the QAP points. The public polynomials satisfy $Z_*=(X-\rho)Z$ and $L_\rho=Z/Z(\rho)$. The fallback computes the unique discrete logarithm $j\in\{0,\ldots,q-1\}$ with $jE_0=E_1$, by the following direct-key procedure. At stage $h\ge0$, let $w=2^h$. Tabulate $iE_0$ for $0\le i<w$, starting at the identity. Beginning at $E_1$, check the $w$ giant residuals obtained by successive steps of $-wE_0$. A match at giant index $k$ and baby index $i$ gives $j=kw+i$. Accept only $j<q$. Each stage thus covers all nonnegative integers below $w^2$ that lie in the index range, and distinct accepted indices cannot have equal group value. The first stage with $w^2>j$ is sufficient. For the stride, invert $E_0$ by the fixed Frobenius map of Amendment search_spread once, then double $h$ times per stage. Equality of polynomial-basis target elements suffices for lookups. After finding $j$, compute
\[
 K=\frac{1}{(c_{\rm q}j-\rho)Z(\rho)} E_0
\]
and use its key-oracle value to recover the message. Because $E_0\ne0$, its order is $q$ and $j$ is exactly $\tau/c_{\rm q}$ in the field. The denominator is nonzero and $K=[\kappa]_T$, including when $j=0$. The traversal is the evaluation-point mode of line [full-search]. It returns the index as the fourth component, and the arithmetic after the line computes the displayed key group element.

The fallback uses two pairings of operands already present in the ciphertext. It publishes no new value. In the generic security experiment these pairings remain ordinary formal expressions of the same exponents analyzed in C7. The proof of extraction treats every adversarial sequence of calls within the stipulated adversary budget. That quantifier is independent of the cost of the honest evaluation-point traversal.

**One search line and its actual result.** The revised line [full-search] receives the selected mode and the corresponding group operands. On the ordinary mode for the chosen triple, the public centers $c_0,c_1,c_2$ are the rounded centers of the anchor and the two increments. The line returns
\[
 T=(r(c)-c_0,\ r(a)-r(c)-c_1,\ r(b)-r(c)-c_2,\ 0).
\]
On the direct-key mode, the same line instead traverses the evaluation-point logarithm search above and returns $T=(0,0,0,j)$. The index $j$ is the nonnegative solution in $[0,q-1]$ to the displayed group equation, and the other three coordinates are zero. The divisor for key normalization is applied afterward using this fourth returned component. On a bypass branch no logarithm is computed and $T=0$. The line also returns the signed component $t$ of largest magnitude with the smallest index breaking ties. This designated scalar result is an actual recovered logarithm, with $|t|=\|T\|_\infty$. The witness-sampler range $[-B,B]$ is used for the first three coordinates. The separate input-domain range $[0,q-1]$ for the fourth comes from the order of its nonzero base. The RMS and pointwise bounds below cover this entire record, including its fourth component. Reconstruction and group normalization follow the line on either path.

### View of the correction polynomials

The $\eta_2$ tail reduction changes no scalar grade in the generic comparison. In the scale-neutral grade-zero comparison its altered terms reduce to the original field products modulo $P_T$. All negative-grade support is bounded by the new degree calculation in C7. Thus the three ties and the resulting stack classification are exactly the ones proved in C7.

The sparse right class uses inverse scale $\zeta_0^{-1}$ and the two non-sparse families use $\zeta_1^{-1}$. Thus their contributions to the scale-neutral part of the Laurent comparison are exactly the products analyzed above. Every shifted exponent still has nonzero residue modulo $\nu$. Division of the remainder-family polynomial by $Z_{\mathcal K}$ preserves those residues, and the extra quotient-family polynomial joins the cell quotient. The resulting form is $Z_c h_c+Z_0 R_c$ with allowed $R_c$ at every cell.

## Amendment n2

The exact half-count is
\[
 n_2=\left\lceil\frac{6K_2(N+4)+3K_2+(3n/2)(J+1)+C_{\rm mask}}2\right\rceil .
\]
The first two terms count the single right factor arrays and search bases. There is one sparse list of $A_c$ bases and $J_Q+J_R=J$ lists of $A_c$ non-sparse bases, and the cancellation count is $C_{\rm mask}$. The optional generator padding gives $2n_2$ actual slots. The G1 count is proved in n1. Together with the fixed one GT element, seed and masked message, these give exactly the protected size formula and the one-generator-multiplication count from the published scalars.


## Amendment dec_sum_g1

Sum the ordinary witness entries in each of the $2K_1+1$ left arrays at cost at most $(N+1)/2$ each. The at most eight variants add at most three tags per array. The original fixed sparse adjustments need at most 64 additions total. The two new sparse sums have at most four present bits across the four variants, each adding one term in each sparse operand, and two more additions form the two $D_i^{0,+}$. Across the four variants each of the two direction bits can be set in at most two variants, so at most $4J_Q$ additions combine their entries with the baseline chunks. Thus the bound is $(2K_1+1)((N+1)/2+24)+76+4J_Q$.

## Amendment dec_sum_g2

The $6K_2$ ordinary right-coordinate sums each use at most $(N+1)/2$ additions. Only the at most four full variants need right coordinates with tags added, at most three per array. The direction uses the baseline weighted quotient right lists and adds its bit contributions in G1. Hence $6K_2((N+1)/2+12)$ suffices.

## Amendment dec_msm_g1

The at most eight first and four second weighted left factor operands cost $12A_c$ points. Baseline sparse key and non-key MSMs take $S_0$ and $S_0+1$ points and one more fixed multiple; baseline non-sparse ones take $U_*-(S_0+n_{\mathsf c})$. Each direction's first sparse MSM and its non-sparse chunk MSMs together take at most $D-1$ points. Its one-step sparse MSM and fixed multiple cost at most $S_0+1$ more. The baseline non-sparse length counts both non-sparse quotient and remainder coefficients, totaling $(D-1-S_0)+(\nu-1)n_{\mathsf c}$. Thus the full bound is
\[
 12 A_c+D-1+S_0+2+(\nu-1)n_{\mathsf c}+2(D+S_0).
\]

## Amendment dec_msm_g2

Each full variant uses $A_c$ points for the two sparse right operands together, $JA_c$ for the quotient and remainder lists and $C_{\rm mask}$ for cancellation. In total the bound is $4((J+1)A_c+C_{\rm mask})$. The at most eight search-base computations use fixed right bases and no additional G2 MSM.

## Amendment dec_pairings

The at most eight search-base sums use $3K_2$ pairings each. Each of at most four full sums uses $6K_2$ factor pairs, $J$ regular pairs across the quotient and remainder chunks, two sparse pairs and one cancellation pair. This gives $24K_2+4(6K_2+J+3)$. Under $J\le28$ and $K_2=17$ this is at most $408+4(102+28+3)=940$, within the 1100-accumulation ledger of search_spread. The direct fallback uses at most $24K_2+2$ pairings and no full sum.

## Amendment search_spread

Let $\sigma^+=g\sqrt{(N+7)/48}$, $R_0=\sigma^++3/2$, and define
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
   \left(\frac{20}{37}\big((10001/10000)((4882533/2950000)\sqrt{\sigma^+}+(47/18+1/5000000)\sqrt{g/2})+404500\big)\right)^2\right\},
 \qquad R_T=g\sqrt{(N+23)/48}+14 .
\]
Here $M_0$ bounds the expected absolute centered anchor, and $M_1$ bounds an increment in the first-listed triple. The amended arithmetic cost uses the sharper concurrent-anchor bound proved below. The branch selection is independent of the search vector, so the anchor bound applies on any chosen triple. The two additional quantities $R_0$ and $R_T$ cover the RMS of the recombined centered integer and the full search record respectively.

For the ordinary search record, the exactly centered variables have second moments bounded by $(g^2-1)(N+7)/48$ for the anchor and $2(g^2-1)/12$ for each increment, since each increment involves at most two independent uniform box samples with opposite coefficients. The square of the Euclidean norm is a sum of squares regardless of their correlations. The vector of rounding errors has Euclidean norm below $2$, since the anchor error is at most $3/2$ and each increment error at most $1/2$. The triangle inequality in square mean bounds the ordinary part of the record by $g\sqrt{(N+23)/48}+2$. The fourth component is zero except on the direct-key fallback whose probability is at most $135/q^2$ by Targets. Since $0\le j<q$, its root mean square is at most $\sqrt{135}<12$, even with arbitrary dependence between the branch and $j$. Summing these square-mean bounds gives $(\mathbb E\|T\|_2^2)^{1/2}\le R_T$, which also bounds the RMS of the signed greatest component. The first three coordinates meet the range bound from Bsearch and the stated width of any two box samples, and the evaluation-point coordinate meets its stated range.

### Expected absolute anchor

Before the rounding error of at most $3/2$ in Bsearch, the center removes the mean, leaving the sum of independent symmetric variables
\[
 S=X_\diamond+\sum_{i=1}^{N+3}(v_i-1/2)X_i ,
 \qquad X_i=r_i-(g+3)/2 .
\]
Its standard deviation is $\sigma_S=\sqrt{(g^2-1)(N+7)/48}>0$. Let $Y_i$ be its summands divided by $\sigma_S$, using one more index for the independent diamond term. Set $v_i'=\mathbb E Y_i^2$ and $v_{\max}=\max_i v_i'$. The ordinary summands have $v_i'=1/(N+7)$, the diamond summand has $v_i'=4/(N+7)$, and $\sum_i v_i'=1$. Each $|Y_i|^2\le3v_i'$ because the square of the largest deviation of an integer uniform sample of width $g$ is $(g-1)^2/4$ before scaling, and the variance is $(g^2-1)/12$. It follows that $\mathbb E Y_i^4\le3(v_i')^2$.

Write $\phi_i(t)=\mathbb E\cos(tY_i)$, $\psi_i(t)=\exp(-v_i't^2/2)$. For $0\le t\le300$ and $N\ge359994$, put $w_i=v_i't^2\le1$. Both $\phi_i(t)$ and $\psi_i(t)$ belong to $[1-w_i/2,1-w_i/2+w_i^2/8]$. For cosine the lower bound follows from $1-\cos x\le x^2/2$, and the upper bound follows from Taylor's theorem to degree three with fourth derivative at most one and the fourth-moment estimate above. For the exponential use Taylor's theorem with its second derivative at most one on the nonnegative half-axis for $\exp(-x)$. Both functions are nonnegative on this interval and at most $1-3w_i/8\le \exp(-w_i/3)$. Symmetry and independence make $\phi=\prod_i\phi_i$ the characteristic function of $S/\sigma_S$. The product $\psi=\prod_i\psi_i$ is the characteristic function of a standard normal. Telescoping the products, using one difference $|\phi_i-\psi_i|\le w_i^2/8$ and bounding each other factor by its exponential, yields
\[
 |\phi(t)-\psi(t)|
 \le \frac{t^4}{8}\sum_i(v_i')^2
          \exp\big(-(1-v_{\max})t^2/3\big)
 \le \frac{t^4}{720000}\exp(-t^2/4).
\]
The last inequality uses $v_{\max}\le1/90000$, $\sum_i(v_i')^2\le v_{\max}$, and $1-v_{\max}\ge3/4$.

For real $x$,
\[
 |x|=\frac2\pi\int_0^\infty\frac{1-\cos(tx)}{t^2}\,dt .
\]
To verify the constant, scale by $|x|$ when $x\ne0$, then integrate by parts to obtain $\int_0^\infty\sin(t)/t\,dt=\pi/2$. In the integral with a factor $\exp(-at)$, $a>0$, differentiating in $a$ gives $-1/(1+a^2)$ and the integral tends to zero as $a$ tends to infinity. It therefore equals $\arctan(1/a)$. Ordinary integration by parts bounds the damped tail uniformly in $a$ by $2/T$ after $T>0$, since $\exp(-at)/t$ is positive decreasing. This justifies the limit as $a$ decreases to zero. The case $x=0$ is immediate. The integrand of the absolute-value identity is nonnegative, so expectation can be taken inside. The normal absolute moment is $\sqrt{2/\pi}$ by integrating its density on the two half axes. Its characteristic function $\exp(-t^2/2)$ follows from differentiating the integral of its density times $\exp(itx)$, integrating by parts to obtain $\psi'(t)=-t\psi(t)$, and using $\psi(0)=1$.

The two characteristic functions have absolute values at most one for every $t$. Using their sharper bound up to 300, the triangle inequality gives
\[
 \frac{\mathbb E|S|}{\sigma_S}
 \le \sqrt{2/\pi}+
 \frac{2}{720000\pi}\int_0^\infty t^2e^{-t^2/4}\,dt+
 \frac{4}{300\pi}
 < \frac{803}{1000}.
\]
For the inequality the middle integral is $2\sqrt\pi$ by substituting $u=t/2$ and integrating by parts, and $\pi>3.14$ suffices for the final numerical comparison. Adding the rounding error yields $M_0$, with Cauchy--Schwarz giving the alternate bound at smaller $N$.

For the scored range $359994\le N\le479993$ and $g\ge10^{12}$, the cosine bound can be continued beyond frequency 300. Each of the $N+3$ ordinary summands has spacing $1/(2\sigma_S)$ after normalization, up to sign, with distribution symmetric about zero. The finite geometric sum yields its characteristic function
\[
 \frac{\sin(gu)}{g\sin u},\qquad u=\frac{t}{4\sigma_S}.
\]
Here $\sigma_S/g\le100$ by $N+7\le480000$. Also $\sigma_S\ge g$ since $g\ge2$ and $N+7\ge360000$. Thus $300\le t\le10^6$ gives $gu\ge3/4$ and $0<u<1/100$. The function $\sin v/v$ decreases from 1 on $[0,\pi]$: the derivative numerator $v\cos v-\sin v$ is zero at zero and has derivative $-v\sin v\le0$ there. For $v\ge\pi$, its absolute value is at most $1/\pi$. Taylor's bound on $\sin(3/4)/(3/4)$ and the lower bound $\sin u\ge u-u^3/6$ therefore give
\[
 \left|\frac{\sin(gu)}{g\sin u}\right|
 \le \frac{1-(3/4)^2/6+(3/4)^4/120}{1-(1/100)^2/6}<\frac{91}{100}.
\]
Both Taylor bounds follow from the alternating power series on the given fixed intervals. Since $(91/100)^8<1/2$ and $N+3\ge320$, the product of the ordinary factors is bounded in absolute value by $2^{-40}$ on this frequency interval. The diamond factor has absolute value at most one and the normal factor is also at most $2^{-40}$ for $t\ge300$. Thus the middle integral contributes less than $2^{-40}$ after its $2/\pi$ normalization. The tail above $10^6$ contributes at most $4/(\pi10^6)$.

The normal first absolute moment is less than $797886/10^6$. For an exact bound, $\pi>314159/100000$ follows by the tangent addition formula from $\pi/4=4\arctan(1/5)-\arctan(1/239)$ and the alternating bounds through the $-x^7/7$ term for the first arctangent and $x$ for the second. Indeed the tangent of $4\arctan(1/5)$ is $120/119$, and the indicated difference has tangent one and lies between zero and $\pi/2$. These rational bounds give
\[
 16\left(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}-\frac1{7\cdot5^7}\right)
 -\frac4{239}>\frac{314159}{100000},\qquad
 \frac{314159}{100000}\left(\frac{797886}{10^6}\right)^2>2 .
\]
The low-frequency error is at most $1/(180000\sqrt\pi)<1/300000$, by the same low-frequency integral used above. Summing the errors gives
\[
 \frac{\mathbb E|S|}{\sigma_S}
 < \frac{797886}{10^6}+\frac1{300000}+2^{-40}+\frac2{10^6}
 < \frac{7979}{10000}.
\]
Adding the rounding allowance again gives the selected $M_0$.

### Relative searches and fallback work

A centered single box sample has absolute mean at most $g/4$. For $g=2m$, the sum of the $2m$ distances from the midpoint is $2\sum_{i=1}^m(i-1/2)=m^2$. For $g=2m+1$, the sum is $2\sum_{i=1}^m i=m(m+1)$, giving absolute mean $(g^2-1)/(4g)$. Rounding a public center adds at most $1/2$. Both increments of the first-listed triple are single box samples, so each uses $M_1$. Any other triple uses increments with RMS at most $M_\Delta=g/\sqrt6+1/2$ by the second-moment and rounding bounds just proved. Use this as the expected absolute bound on those triples. The probability of needing either later triple is at most $9/q$, as follows by the union bound over the three zero bases in the first. The increase in expected primary candidates is at most $(9/q)4\sqrt{M_\Delta}\le 36/\sqrt q<1$ since $g+1<q$ and the protected prime exceeds $1296$. All ordinary search integers remain within $B$.

**Amended Proposition 5.7(c).** Decryption uses at most the source-group sums, MSM lengths and pairing counts proved in their respective amendments. In addition it takes at most 1100 target-field accumulator products at the scored shape for the signed pairing sums and at most 400 further target products for fixed combinations, initialization, and search setup. In this bound, shared final exponentiation remains part of the protected pairing charge. The ordinary path uses thirteen target-group scalar multiples outside the candidate iterations: three center translations, two in-line anchor translations, two final operations to subtract the search term and apply the inverse key weight, and six initial strides for the three logarithms. The branch with zero distinguished target base uses at most one scalar multiplication, and the direct-key recovery branch uses only one scalar multiplication after recovering its evaluation-point index. The admissible upper bounds therefore hold pointwise on all branches outside the single line [full-search]. The arithmetic price for these products, including basis conversions, is proved below.

**Amended Proposition 5.7(d).** Line [full-search] in n1 takes $O(\sqrt{\|T\|_\infty}+1)$ target-group operations on its actual result $T$. Equivalently its cost is $O(\sqrt{|t|}+1)$ for the signed largest emitted logarithm. On the ordinary mode of that line this follows from the three component bounds below. On the direct-key mode it follows from the adaptive evaluation-point search and the equality $\|T\|_\infty=j$. The same output and pointwise bound therefore cover both traversals. All auxiliary arithmetic during decryption besides these traversals is covered by (c). The expected group work in the line is $O(\sqrt g\,N^{1/4})$ on an honest ciphertext.

The direct-key mode of the search line has probability at most $135/q^2$, by Targets. In this mode stage width $w=2^h$ takes fewer than $w$ baby updates, fewer than $w$ giant updates, at most $h$ doublings and bounded setup. With one inverse of $E_0$ via the fixed $p^6$ Frobenius, at most four target operations per unit width including setup suffice. The stage search cost is therefore $O(w)$, and the sum of widths through the first width with $w^2>j$ is less than twice that width, while the final width is at most $2\sqrt{j+1}$. This gives the claimed bound for the fourth component. In particular there are at most $16\sqrt q+600$ operations of cost at most a target product, including the final scalar multiple outside the line. Its two pairings are included in dec_pairings. Its scalar-field denominator formation and inversion cost less than one multiplication in expectation at the protected prime and fit the protected scalar allowance.

The primary fixed-width traversal gives the expected-cost bound, and the interleaved traversal below supplies the pointwise guarantee of Proposition 5.7(d). For any centered target $x$ known to have $|x|\le B$ and $\mathbb E|x|\le M$, use the sign-class baby and giant search with integer width $b=\lceil\sqrt M\rceil+1$. Tabulate $iP$ for $0\le i<b$, where $P\ne0$ is the base. The signed intervals centered at $j(2b-1)$ with radius $b-1$ partition the integers. Progress outward in the order $j=0,1,-1,2,-2,\ldots$, testing the sign class of the corresponding residual against the table. Verify the sign and the resulting integer against the bound; $2B+1<q$ makes the bounded solution unique. A match for the true integer occurs by $|j|\le |x|/(2b-1)+1$. The baby construction has at most $b$ counted steps. Its stride follows from the last baby point by a doubling and one addition. Maintain separate accumulators for positive and negative giant indices, so alternating the direction advances the selected accumulator with one update. Including a constant for initialization and verification, the total is at most $b+2|x|/(2b-1)+12$ steps on a true target. This bound includes names and the constant work to derive their signs according to the protected step convention. A run with no valid solution can stop upon exploring all intervals intersecting $[-B,B]$. Since $2b-1\ge2\sqrt M$, its expected bound on a valid sampled target is at most $2\sqrt M+14$. A nonzero base is always used for these searches.

### Concurrent tables for the finite signed logs

For the first triple put $xP=Q$, $A=g/2$, $a=\sqrt A$, and $b=\lfloor a\rfloor$. The single centered tag gives a uniform interval of $g$ integers in $[-A,A]$ with second moment at most $g^2/12+1/4$. This is conditional on the first-triple choice, which is independent of the sampler, without conditioning on the recovered anchor.

The baby entries are $iP$, $0\le i\le b+1$. The positive and negative giant centers are $2bi$ and $-(2b+2)j$ for positive $i,j$, with zero used once. The giant entry at center $c$ is $Q-cP$. Visit zero, then alternate the positive and negative centers in outward order. Stop a direction when its next nearest-integer cell misses $[-g,g]$. Prepare the two distinct strides $(2b)P,-(2b+2)P$ using the two setup allowances. Each new entry needs only one group update. Alternate one baby and one giant until the baby list is complete and retain both tables during this part. Finish the longer list after the shorter one exhausts; discard the giant table once the baby list is full.

Use the same sign classes and recovery of the signed indices as in the fixed-width traversal. A baby and giant match gives $x=c\pm i$. Additionally, before discarding the giant table, check each new giant against the stored giants. When two giant values are opposites, at their centers $c,c'$ the equality is $2Q=(c+c')P$, giving the integer $(c+c')/2$ since both centers are even. One can tell whether the signs are opposite from the sign-class names, allowing either sign at the identity. Keep answers only in $[-B,B]$, where $2B+1<q$ ensures uniqueness. The centers span at most $2g+2b+2<2B+1<q$, so a giant sign class has at most two entries. The baby names are distinct. The added lookups use constant work and no field product. Every integer in $[-g,g]$ is within $b+1$ of a center, so the ordinary matches give correctness.

First bound the expected count if giant-to-giant matches are ignored. For $x\ge0$ select the nearest nonnegative center and for $x<0$ the nearest nonpositive one. Break midpoint ties consistently, so a complete cell has $2m$ integers with residuals $-m,\ldots,m-1$, where $m=b$ or $b+1$. Its giant ordinal $G$, starting at zero, satisfies $G\le |x|/b+2$. Let $I$ be the absolute residual. Put $D_b=b+2$. Before the baby list completes the ordinary hit uses at most $2\max(I,G)+2$ primary entries. If $G\ge D_b$, it uses at most $D_b+G+2$. On a complete cell with $G\le m$, averaging gives
\[
 2\mathbb E\max(I,G)=2G+2\sum_{v=G+1}^m\frac{2(m-v)+1}{2m}=m+G^2/m.
\]
For $G\le m\le D_b$ this is at most $D_b+G^2/D_b$ by monotonicity in the denominator variable. For $m<G<D_b$ use $2G\le D_b+G^2/D_b$, and for $G\ge D_b$ use $G\le G^2/D_b$. Thus the conditional bound is $D_b+G^2/D_b+2$. At most four cells are incomplete, at zero and the interval ends. On each the same bound overestimates the required conditional mean up to an added $2D_b$, by the pointwise counts. The expected addition is at most $2D_b\cdot4(2b+2)/g<16$.

For each $x$, use $D_b\ge a$, $D_b\le a+2$, $b\ge a-1$, $|x|\le a^2$ and $a\ge1000$. Then $G^2/D_b\le x^2/a^3+11$, by expanding $(|x|/b+2)^2/D_b$. The extra quadratic part is at most $a((a/(a-1))^2-1)<4$, the linear part is at most $4a/(a-1)<6$, and the constant part is below one. Combining with the incomplete cells, fixed entries and second moment gives at most $(4/3)a+64$ expected ordinary primary candidates. Here $a>2^{24}>1000$ follows from $g^{-4}<\mu_{\rm tr}<\theta<2^{-199}$.

For a positive odd integer $d$ and $j\ge1$, take giant indices $i=d+j$ and $j$ in the positive and negative directions. Their opposite-sign match occurs at $x=db-j$. Interchange the indices for the second sample $x=-d(b+1)-j$. In both cases the two entries appear within $4(d+j)+4$ primary operations. Let
\[
 S(d,j)=\max(0,2b-4d-6j-6).
\]
When this is positive, $d<b/2$, $j<b/3$, and $d+j<b/2$. These samples lie strictly between $-A+1$ and $A-1$, hence in the actual rounded interval. All are distinct, since different positive odd $d$'s move the positive centers by $2b$ and the negative centers by $2b+2$, more than the range of the offsets. The positive sample is at distance at least $b-j$ from every ordinary giant center: it is $j$ to the left of the midpoint of adjacent positive centers, and nonpositive centers are no nearer. The negative sample is $j$ to the left of the corresponding midpoint on the negative side, with nearest distance $b+1-j$. Both giant lists are active through these early indices and until at least $b+1$ babies are made, since the retained cells extend to $g=2a^2$. An ordinary hit requires making baby index at least $b-j$, so it uses at least $2(b-j)-2$ primary operations. Taking the minimum with the new hit thus saves at least $S(d,j)$ operations on each of the two samples. Other inputs cost at most the ordinary count.

For each odd $d\ge1$, $j\ge1$, integrate $\max(0,2b-16-4u-6v)$ over $[d-1,d+1)\times[j-1,j)$. Its value at each point is at most $S(d,j)$, since $d\le u+1$, $j\le v+1$. These rectangles partition the nonnegative quadrant, so the total saving over the two samples per pair is at least $(2b-16)^3/144$, by integrating the affine positive part on its triangle. Dividing by $g=2a^2$ gives at least $(a/36)(1-9/a)^3$, since $b-8\ge a-9$. Bernoulli gives $(1-9/a)^3\ge1-27/a$, and $a>2^{24}$ gives expected savings at least $a(1/36-1/10^7)$. Thus a first-triple increment uses at most $(47/36+1/10^7)\sqrt{g/2}+128$ expected primary steps. The adaptive search below proves the pointwise bound.

### A local bound for anchor probabilities

Let $K=\sum_i(2v_i-1)r_i$ have mean $\mu_K$ and variance $s_K^2=(N+3)(g^2-1)/12$. Its centered summands are independent signed boxes. Thus $180<s_K/g<182$ and $(99/50)\sigma^+<s_K<2\sigma^+$. The anchor is $X=A_0-c_v+r_\diamond+\lceil K/2\rceil$. Given $r_\diamond$, both adjacent $K$ integers producing $X=x$ are within $2|x|+g+3$ of $\mu_K$ by the center formula.

Write $\phi_K$ for the characteristic function of $(K-\mu_K)/s_K$. Integrating each integer frequency over a full period gives
\[
 s_K\Pr(K=k)=\frac{1}{2\pi}\int_{-\pi s_K}^{\pi s_K}
 e^{-it(k-\mu_K)/s_K}\phi_K(t)\,dt .
\]
The normalized Gaussian density is the same integral over the real line with $e^{-t^2/2}$ in place of $\phi_K(t)$, by the Gaussian integral. Up to frequency 300 the same moment telescoping as above gives $|\phi_K(t)-e^{-t^2/2}|\le t^4 e^{-t^2/4}/(8(N+3))$, now with equal summand variances $1/(N+3)$. The integral of $t^4 e^{-t^2/4}$ on the positive axis is $12\sqrt\pi$ by integration by parts. For $300\le t\le1000$, put $u=t/(2s_K)$. Here $gu>4/5$ and $u<3/g$. The sine ratio has magnitude at most $99/100$: $|\sin(gu)/(gu)|<9/10$ by the decreasing sinc on $[4/5,\pi]$ and the bound $1/\pi$ thereafter, and $u/\sin u<11/10$ by Taylor's bound. For $1000\le t\le\pi s_K$, the ratio is at most $600/t$ by $\sin u\ge2u/\pi$ and $\pi s_K/g<600$.

There are $N+3$ factors of the sine ratio in $\phi_K$. Thus the absolute inversion error is at most
\[
 \frac1\pi\left(\frac{12\sqrt\pi}{8(N+3)}+
 700(99/100)^{N+3}+\frac{1000(3/5)^{N+3}}{N+2}+
 \frac{e^{-45000}}{300}\right)<1/10000 .
\]
Consequently each adjacent integer has mass at least $(199/500)(1-z^2/2)/s_K-1/(10000s_K)$ at standard displacement $z$, since $1/\sqrt{2\pi}>199/500$ and $e^{-z^2/2}\ge1-z^2/2$. Apply this conditionally and average over the diamond as below.

### Two-phase concurrent traversal for the anchor

Keep the two different giant strides, baby indices from zero through $b+1$, and the same opposite-sign queries used for increments. Here take $A_*=123/100$, $a=\sqrt{A_*\sigma^+}$ and $b=\lceil a\rceil+1$. Retain cells meeting $[-\lceil B/2\rceil,\lceil B/2\rceil]$, which contains the anchor by the sampler's deterministic bound $(N+5)(g-1)/4+3/2$. The center span is below $2B+1<q$ since $2b+2<B$, so the table and answer bounds above apply. Use the cumulative baby schedule
\[
 r_1=21/20,\quad r_2=8/5,\quad t_0=2/5,\quad h_0=r_1t_0,\quad t_1=61/80,
 \qquad
 h(u)=\begin{cases}
 r_1 u&0\le u\le t_0,\\ h_0+r_2(u-t_0)&t_0\le u\le t_1,\\ 1&u\ge t_1 .
 \end{cases}
\]
Use the inverse of $h$ on $[0,t_1]$. Schedule baby $i$ at time $h^{-1}(\min(i/b,1))$ and giant $j$ at time $j/b$. Include both extra baby indices at $t_1$ and prefer babies on ties. These are rational comparisons of the next indices. As before, retain both tables until the baby list ends.

For the ordinary hit use the nearest center on the sign of $X$, with residual magnitude $I$ and ordinal $J$. Put $x=\min(I/b,1)$, $u=J/b$, $v=\max(u,h^{-1}(x))$, and $H(x,u)=h(v)+v$. The two entries are present by $v$, so the primary count is at most $bH(x,u)+18$, including the extra baby entries. As a function of $x$, $H$ is constant up to $h(u)$ and then equals $x+h^{-1}(x)$, so it is increasing and 2-Lipschitz. For $u\ge t_1$ it equals $1+u$.

Conditional on the other box variables, the diamond gives a uniform interval of $g$ integers. In a full cell the residual is uniform on $-m,\ldots,m-1$ with $m=b$ or $b+1$. Its absolute value is dominated by $mU+1$ for $U$ uniform on $[0,1]$: for $0\le y<m$ its distribution is $(2\lfloor y\rfloor+1)/(2m)\ge\max(0,(y-1)/m)$. Coupling the cumulative probabilities gives $x\le\min(1,U+2/b)$. Thus the full-cell bound is $bf(u)+22$, where
\[
 f(u)=\int_0^1 H(x,u)dx=h(u)(h(u)+u)+\int_{h(u)}^1(x+h^{-1}(x))dx.
\]
On the linear pieces $f'(u)=h(u)(1+h'(u))$. Hence $f$ is continuous, increasing and $13/5$-Lipschitz, below $2$ before $t_1$ and equal to $1+u$ thereafter. There are at most four incomplete cells, at zero and the two interval ends. Their probability is at most $4(2b+2)/g$. Before fill the pointwise count is at most $3b$ and after fill the whole-cell bound holds pointwise. The excess is at most $24b(b+1)/g<3000$, since $a^2/g<121$, $b\le a+2$ and $g>10^{12}$.

The ordinary ordinal satisfies $J\le |X|/b+2$. Thus $bf(J/b)\le bf(|X|/a^2)+26/5$. Also $\mathbb E f(|X|/a^2)\le2+\mathbb E|X|/a^2<3$ from the RMS bound. Changing the exterior $b$ to $a$ costs at most six steps and replacing $X$ by the centered sum $S$ costs less than one since $|S-X|\le3/2$. The complete comparison overhead is below 4096. 

Put $Y=S/\sigma_S$ as above and let $G$ be standard normal. The established characteristic-function bound through frequency $10^6$ and the trivial bound beyond it give
\[
 \frac{2}{\pi}\int_0^\infty
    \frac{|\phi_Y(t)-e^{-t^2/2}|}{t^2} dt
 <\frac1{300000}+2^{-40}+\frac2{10^6}<\frac1{150000}.
\]
In particular, for every $v\ge0$ the expectations of $(|Y|-v)_+$ and $(|G|-v)_+$ differ by less than $1/150000$: use
$(|y|-v)_+=(|y-v|+|y+v|)/2-v$ and the absolute-value integral above, in which the average of the shifts multiplies the characteristic function by $\cos(tv)$. Monotonicity gives $f(|S|/a^2)\le f(|Y|/A_*)$. To compare this last expectation to the normal one, write $f(u)=f(0)+\int_0^{t_1}(u-v)_+ d\mu(v)$, including any atoms at the endpoints. Here $d\mu$ is the measure of increments of $f'$. This identity follows by integrating the derivative, which starts at zero. Its derivative grows on the two pieces and jumps upward at $t_0$ to reach $1+r_2$ just before $t_1$, where it drops to one. The total variation of $\mu$ is $1+2r_2=21/5$. Therefore
\[
 \left|\mathbb E f(|Y|/A_*)-\mathbb E f(|G|/A_*)\right|
 <\frac{21/5}{150000 A_*}.
\]

It remains to bound the normal expression at the two rational cutoffs $R_0=A_*t_0=123/250$ and $R_1=A_*t_1=7503/8000$. Let $F(v)=\Pr(|G|\le v)$ and $\varphi$ be the normal density. Direct integration of $f'$ gives
\[
 f(x/A_*)=
 \begin{cases}
 (7369/8000)+(861/800)(x/A_*)^2,& 0\le x\le R_0,\\
 (39573/40000)-(286/615)x+(20800/15129)x^2,&R_0\le x\le R_1,\\
 1+x/A_*,&x\ge R_1.
 \end{cases}
\]
In computing $f(0)$, the integral of $h^{-1}$ equals $r_1t_0^2/2+(1-h_0)t_0+(1-h_0)^2/(2r_2)$. For the normal integrals use
$\mathbb E[|G|\mathbf1_{|G|\le v}]=2(\varphi(0)-\varphi(v))$ and
$\mathbb E[G^2\mathbf1_{|G|\le v}]=F(v)-2v\varphi(v)$, by $\varphi'=-x\varphi$ and integration by parts. Substituting in the three pieces gives
\[
 \mathbb E f(|G|/A_*)=1
  -\frac{55346489}{75645000}F(R_0)
  +\frac{825539917}{605160000}F(R_1)
  -\frac{341}{1230}\varphi(R_0)-\frac{14}{615}\varphi(R_1).
\]
Use $398940/10^6<1/\sqrt{2\pi}<398943/10^6$ by the earlier lower bound and $\pi<314160/100000$. The upper bound on $\pi$ follows from the same Machin identity, using the alternating sums through the positive ninth-power term for the first arctangent and the negative cubic term as a lower bound for the subtracted arctangent. Squaring the two normalization inequalities with the respective rational bounds on $\pi$ verifies them.

At both cutoffs $v$, integrate the alternating exponential series for the folded density. For $F(v)$ use twice the normalization times the sums
$\sum_{j=0}^{k}(-1)^j v^{2j+1}/(2^j j!(2j+1))$; for $\varphi(v)$ use the normalization times
$\sum_{j=0}^{k}(-1)^j(v^2/2)^j/j!$. The lower and upper sums have $k=7$ and $k=6$ respectively, since $v^2/2<1$. Substituting the two cutoff fractions in these sums gives the following outward rational ends:
\[
 F(R_0)>377278499/10^9,\quad F(R_1)<325846277/(5\cdot10^8),
\]
\[
 \varphi(R_0)>88365769/(25\cdot10^7),\qquad
 \varphi(R_1)>51396409/(2\cdot10^8).
\]
Use these ends according to coefficient sign in the expression above and $\sqrt{A_*}<1109054/10^6$ by squaring. The resulting bound for $\sqrt{A_*}\mathbb E f(|G|/A_*)$ is
\[
 \frac{50643204301966142506511}{30258000000000000000000}
 <\frac{1673713}{10^6}.
\]
Adding $(1109054/10^6)(21/5)/(150000 A_*)$ gives less than $83687/50000$. Including the finite comparison errors, the anchor without the extra giant queries takes at most $(83687/50000)\sqrt{\sigma^+}+4096$ expected primary steps.

The extra giant matches improve the ordinary count. For positive odd $d$ and $j\ge1$, use the distinct samples $db-j$ and $-d(b+1)-j$ from the two opposite-sign pairs described for the increments. Both are at distance at least $b-j$ from every ordinary giant center. For the positive savings region below $j<b/3$, so this required baby ordinal lies on the second segment with time $(5/8)(b-j)/b+11/80$. Any ordinary hit therefore requires at least $(13/8)(b-j)+(11/80)b-3$ primary operations, counting the earlier giants.

The paired entries are present by giant ordinal $2(d+j)$, so put $v=(d+j)/b$, $w=j/b$ and $u=2v$. The $u+h(u)$ cost contributes $2(1+8/5)v=(26/5)v$ before subtracting the early-segment correction. In the positive savings region $u<t_1$, before the baby table fills. Its primary count is at most $b(u+h(u))+6$. On these two segments $h(u)=(8/5)u-\min((11/20)u,11/50)$. Define $A'=141/80$, $C'=26/5$, $R'=13/8$, and
\[
 f_*(v,w)=\left(A'-C'v-R'w+\min((11/10)v,11/50)\right)_+ .
\]
The saved count at each sample is at least $(b f_*((d+j)/b,j/b)-9)_+$. Indeed a positive saving implies $C'v+R'w<A'+11/50$, hence $v<61/160$, so $u=2v\le t_1$ with strict inequality when the bound is positive. Also $w\le v$ and $f_*(v,w)>0$ imply $w<(A'+11/50)/(C'+R')=61/210<1/3$. The rectangles indexed by positive odd $d$ and positive $j$ tile the nonnegative quadrant. For a rectangle intersecting the positive continuous region, its discrete indices obey $d+j<(61/160)b+2$ and $j<(61/210)b+1<b/3$. The absolute values of both signed giant centers are at most $(2b+2)((61/160)b+2)<B/2$, by $b^2<(1231/1000)\sigma^+$, $b>2^{24}$ and $B=(N+4)(g+1)$. In particular both lists retain the paired entries. The positive samples $db-j$ are distinct, since different odd $d$ differ by at least two and all $j$ lie in $(0,b/3)$. The same argument for $d(b+1)+j$ proves distinctness on the negative side. The two signs are disjoint. The two samples satisfy $|x|\le db+b$. Each adjacent $K$ integer has $|z|\le (5/4)(d/b)+1/100$, since $b^2/\sigma^+<1231/1000$, $2b+g+3<\sigma^+/60$ and $s_K>(99/50)\sigma^+$. Their total probability, including averaging over the diamond, is at least $\ell(d/b)/\sigma^+$ where
\[
 \ell(t)=(199/500)\left(1-\tfrac12((5/4)t+1/100)^2\right)-1/10000 .
\]
Here $s_K<2\sigma^+$, and $\ell$ is positive, below $2/5$, and $1/4$-Lipschitz on $0\le t\le61/160+2/b$.

On an area-two rectangle $[d-1,d+1)\times[j-1,j)$ put $v=(x+y)/b$, $w=y/b$. The discrete saving is at least $(bf_*(v,w)-22)_+$ because the two argument slopes in $x,y$ have magnitude at most $C'$ and $C'+R'$ and $2C'+R'+9<22$. The probability factor is at least $\ell(v-w)-1/(4b)$. Their product is at least $bf_*(v,w)\ell(v-w)-10$, since $f_*\le2$ and $22\ell+f_*/4<10$. This also holds when the discrete saving is zero. The variable change has $dx\,dy=b^2\,dv\,dw$. Each rectangle has area two and two distinct signed samples, so those factors cancel. Integrating over $0\le w\le v\le61/160$, of area below $1/2$, gives expected savings at least $b^3(I_\ell-5/b)/\sigma^+$.

For the exact integral $I_\ell$, let $A''=A'+11/50$ and let $c_2$ be the quadratic coefficient of $\ell$. The successive $v$ intervals have endpoints $0,1/5,61/210,61/160$. On them set $(F,L)$ to $(A'-(41/10)v,v)$, $(A''-C'v,v)$, and $(A''-C'v,(A''-C'v)/R')$. Integrating $(F-R'w)\ell(v-w)$ over $0\le w\le L$ gives
\[
 F(\ell(v)L-\ell'(v)L^2/2+c_2 L^3/3)
 -R'(\ell(v)L^2/2-\ell'(v)L^3/3+c_2 L^4/4).
\]
For a polynomial $\sum_i a_i v^i$ use $\sum_i a_i(y^{i+1}-x^{i+1})/(i+1)$ at endpoints $x,y$. With coefficients of $\ell$ equal to $(3978801/10000000,-199/40000,-199/640)$, the three contributions in order are $10515351083/1200000000000$, $11107019592202183/2613824640000000000$, and $3352657411866274343/4282490290173600000000$. Their sum is $I_\ell=3254649870535259/235929360000000000$. As $b\ge a>2^{24}$, the saving is at least $(123/100)a(I_\ell-5/2^{24})$. Its coefficient exceeds $1/59$ by $8507950887291521/463994880000000000000$. Since $a>(11/10)\sqrt{\sigma^+}$, the anchor count is at most $(4882533/2950000)\sqrt{\sigma^+}+4096$ in expectation.

### Adaptive pointwise traversal

Each ordinary search runs a second, adaptive search over the same bound. It uses the auxiliary polynomial-basis representation described below and uses exact equality of twelve-coordinate vectors for table keys. At stage $j\ge0$, set $w=2^j$ and tabulate $iP$ for $0\le i<w$. Use $j$ doublings to obtain $wP$ and another $j$ to obtain $w^2P$. The stride $-wP$ comes from negating $P$ and doubling $j$ times. The inverse of $P$ can be extracted once in at most 508 products by using the scalar $q-1$. It can also be obtained by applying the fixed $p^6$-Frobenius matrix, since the BN254 embedding degree is 12, so $p^6\equiv-1\pmod q$. To handle the pointwise bound uniformly, use this fixed twelve-dimensional linear map, at at most 144 base-field multiplications. Start with the residual $xP+w^2P$ and test $2w+1$ residuals, advancing by $-wP$. A match with baby index $i$ at giant index $j'$ gives $x=j'w+i-w^2$. This covers $[-w^2,w^2+w-1]$, hence certainly every integer of magnitude at most $w^2$. Accept only an integer in $[-B,B]$; uniqueness follows from $2B+1<q$. Thus a valid integer is found by the first stage with $w^2\ge |x|$. With standard constant-operation table access in the search model, the stage costs $O(w)$. Its finite work consists of group products, table accesses, comparisons and integer index updates. The geometric sum of widths is less than twice the last width, so the total work is $O(\sqrt{|x|}+1)$. Each group's multiplication can be suspended between products of coordinates. Resume the adaptive search for one elementary operation before the first primary operation and after each block of one million primary operations, stopping when either search returns. An adaptive operation can be a group update, a table operation, or the single Frobenius application. A primary candidate and its associated table actions have bounded cost, so an adaptive search that would finish in $T$ operations finishes within $10^6(T+1)$ primary candidates if the primary search has not already finished. Each interleaved search therefore costs $O(\sqrt{|t_i|}+1)$ for the integer it produces, with an absolute constant independent of $N,q,g,M$. The three public translations by $c_0,c_0+c_1,c_0+c_2$ are prepared before entering line [full-search]. The two in-line subtractions of $t_0\Psi$ use at most $2\lceil\log_2(|t_0|+1)\rceil$ group products each, and a constant-time target inverse by Frobenius for the appropriate sign. Their cost is $O(\sqrt{|t_0|}+1)$, using $\log(x+1)=O(\sqrt{x})$ for $x\ge1$. Thus the work in this single line, including these translations and all three adaptive traversals, is at most a fixed constant times $\sqrt{\max_i|t_i|}+1$ in the ordinary mode. Choosing the signed largest component and the later key recombination involve only a fixed number of integer operations.

The anchor uses the two-phase concurrent traversal and both first-triple differences use the concurrent traversal with the two distinct strides. A later triple uses the same anchor and the fixed-width traversal with $M_\Delta$ for both differences. Primary baby and giant candidates use the unchanged six-multiplication tariff for the ordinary search operations. For the adaptive search, even charging two arbitrary target-group products at the full 276-multiplication price derived below per scheduled operation, the ratio of adaptive charge to primary charge over a full block is at most $552/(6\cdot 10^6)<1/10000$. At most three initial adaptive operations and the increment initialization and verification bounds of 14 are accounted for separately in the auxiliary allowance. Apart from that allowance, the expected contribution is at most $(4882533/2950000)\sqrt{\sigma^+}+(47/18+1/5000000)\sqrt{g/2}+4352+1$, including the rare use of a later ordinary triple. Termination by the adaptive search can only reduce it.

**Base-field multiplication ledger for auxiliary work.** Represent BN254 target elements as elements of the order-$q$ subgroup of $\mathbb F_{p^{12}}^\times$, where $\mathbb F_p$ is the curve base field. Fix any monic irreducible degree-12 polynomial over $\mathbb F_p$ and its polynomial basis. Pairing outputs can be interpreted in this same field. Precompute the twelve-coordinate vector for each basis power up to degree 22. The polynomial product of two degree-at-most-11 representatives costs at most 144 base-field multiplications. Once the product coefficients of degrees 12 through 22 are known, reduction adds their linear combinations of the fixed twelve-coordinate vectors using at most $11\cdot12=132$ further base-field multiplications. Thus one target-group addition or doubling costs at most 276 base-field multiplications. This bound applies in any degree-12 polynomial basis, including a basis chosen to match the protected pairing implementation via a fixed linear change of coordinates. If that implementation returns in a different basis, converting one result costs at most 144 base-field multiplications. The protected search can stay in its own basis. Converting the at most three base-and-target pairs entering it and the final output out of the auxiliary basis costs at most eight further such conversions.

For an auxiliary scalar multiple, including a group subtraction when implemented by adding an inverse, reduce the scalar modulo $q$. The binary algorithm uses at most 508 group multiplications since $q<2^{254}$. Charge three public center translations before the line, two post-line products for removing the ordinary search term and applying the inverse key weight, six signed-stride setup multiples across the three traversals, and two in-line products by the signed anchor logarithm. This is at most thirteen scalar multiples, each requiring at most 508 group products. Besides these scalar multiples and the signed pairing accumulations, the three center translations take three target-field products, the two in-line translations take two, and the final subtraction takes one. Implement a sign on any of these six updates by the fixed $p^6$ Frobenius, using at most 144 products for its linear map, and allow another twelve such maps for the signed initial strides, three bases of the secondary traversals and final hit signs. At the start of each of the three secondary traversals at most two target products are needed to initialize its two sequences, in addition to sign and stride setup. All further secondary steps use the per-operation charge above. The primary traversals initialize the baby at the identity and the giant at the supplied target. In addition to the per-candidate tariff, allow at most fourteen initialization, terminal and verification products per primary traversal as in the signed schedules above. Integer indexing, table comparisons, sign and index recovery, and the final bit and range checks use no target-field products. These explicit extra allowances total at most $6+18+6+3\cdot14=72$ even pricing each fixed linear map as a full target product. The reserve of 400 covers them with room for the already specified fixed sign and initialization operations. On the fallback path only the fixed evaluation-point inversion in the search and the one normalization after it are needed. For each signed pairing sum, negate source operands by coordinate sign change where needed. Accumulate the corresponding Miller-loop products, then finalize the sum with the protected shared final exponentiation convention. The same polynomial product bound applies to these field products before exponentiation. The pairing bound is $48K_2+4(J+3)\le988$ on the ordinary path and $24K_2+2=410$ on fallback, as shown in Amendment dec_pairings. There is at most one accumulator product and basis conversion per pairing, so the allowance of 1100 of each covers them. The zero-target-base path needs only normalization. In particular, an inverse for the initial stride in the protected signed search can use the protected sign-class operation. Alternatively, make both initial signed strides by two extra binary scalar multiples. We budget two for each of the three primary searches.

The fallback's expected auxiliary cost is at most $(135/q^2)(16\sqrt q+600)\cdot276$ base-field multiplications in addition to the two pairings already charged, hence less than $10\cdot276$ for the protected prime. The total above is less than $(13\cdot508+1100+400+10)\cdot276+(1100+8)\cdot144<2400000$ expected base-field multiplications. It therefore fits in 400000 units of six base-field multiplications. The rare choice of a later ordinary triple adds less than one primary candidate in expectation, so its scheduled cost is at most $10001/10000$ of one unit. Allow two further units for it. The total expected multiplication bound is $6((10001/10000)((4882533/2950000)\sqrt{\sigma^+}+(47/18+1/5000000)\sqrt{g/2})+404500)$, covered by the amended spread, since $400002+(10001/10000)4352<404500$. The ordinary searches retain their bounded-answer correctness, and the fallback introduces no new published operands.


## Amendment n

Use $n=kd_R+\mathrm{form\_pad}$. Here $n=3434$, $d_R=1$, $k=3427$ and $\mathrm{form\_pad}=1+u=7$. Place $v_0$ in slot zero and the $k$ uniform matrix coefficients in slots $1,\ldots,k$. For ordinary and tag coordinates $i=1,\ldots,N_\star$, fix distinct nonzero field elements $a_i=i$ in their public order. Put
\[
 (Vv)_j=\sum_{i=1}^{N_\star} a_i^j v_i,\qquad j=0,\ldots,u-1
\]
in the final $u$ slots, with no homogeneous contribution in these slots. The powers are fixed public coefficients. A form kernel vector satisfies $v_0=0$, $A\widehat v=0$ and $Vv=0$. Any $r\le u$ selected columns of $V$ are independent: the first $r$ rows on those columns have Vandermonde determinant $\prod_{i<j}(a_j-a_i)\ne0$, by the Vandermonde determinant identity. Thus no nonzero kernel vector is supported on at most $u$ box coordinates. This statement holds for every choice of the uniform matrix.

Only the $k$ random rows are programmed from, or counted in, the stipulated scalar SIS instance. Every kernel direction still packs to it as proved in ell and msis_norm. The original rank-three field-tie classification of C7 uses just linearity of the new form map and independence of the images on a subspace containing no form-kernel vector. Both hold for the actual map, so the classification includes every usable stack through rank three. Degree, mask order and field supports depend on $n$ and the actual linear map. The correctness probabilities for the affine form cosets are proved in Targets.

## Amendment msis_bound

Set $\mathrm{msis\_bound}=\mathrm{beta\_sis}=B_{\rm E}$. An infinity-short multiple of $v\ne0$ is an integer $x\equiv a v\bmod q$, $a\ne0$, with $0<\|x\|_\infty\le\beta$. For the amended Euclidean problem, a short multiple instead means such a congruence with $0<\|x\|_2\le B_{\rm E}$. Preserve the original infinity theorem as a separate assertion.

Precisely, for every heavy stack, (a) its rank is at most three, (b) every nonzero kernel vector in its row space has an infinity-short multiple, and (c) every infinity-short multiple of any kernel vector packs to an infinity-SIS solution at $\beta$ in the stipulated coefficient ring. For (a), fixing all but pivot coordinates gives $\operatorname{gp}(W)\le g^{-\operatorname{rank}W}$, as in Bsearch, and $g^{-4}<\theta$. For (b), a linear combination of stack rows is constant on every joint fiber, so $\operatorname{gp}(v^\top)\ge\operatorname{gp}(W)>\theta$. The kernel gives $v_0=0$; apply the proved infinity inverse theorem of I6. For (c), the identity in C7 and coordinate packing in ell give $A\hat x=0\bmod q$ and $0<\|\hat x\|_\infty=\|x\|_\infty\le\beta$.

For the costed Euclidean instance, (a) is identical. Every kernel vector in the row space of any heavy stack has a Euclidean-short multiple. The proof and deterministic lifting procedure follow below. The Euclidean version of (c) is universal: every Euclidean-short multiple of any kernel vector packs to a solution at $B_{\rm E}$, by the same kernel identity and the Euclidean isometry in msis_norm. An infinity-short vector need not be Euclidean-short. No conversion between those two radius predicates is used.

### Joint fibers

For a nonzero matrix $A$ of linear forms on independent box coordinates in $\{1,\ldots,N_\star\}$, suppose the maximum probability of $Ar_I$ is $p>\theta$. The prefix construction of I6 extends to this joint fiber and gives a regular saturated lattice of rank at most three containing the row space modulo $q$, with maximum fiber density at least $p-3\varepsilon_{\rm tr}$. To see this, remove zero columns. The joint prefix probabilities $p_i$ are nonincreasing by conditioning on the last coordinate. The first nonzero column gives $p_1=1/g$ and lattice $\mathbb Z$. At a subsequent step, express each current prefix row as $B c_j$ modulo $q$ in the current basis $B$. Append the next coefficient to get $c'_j$. In the trimmed densest joint fiber $F$ of the longer prefix, these vectors define constant modular forms in $\Phi(r)=(B^\top r_{[i]},r_{i+1})$. At least one last coefficient is nonzero, so one such form puts $\Phi(F)$ in an index-$q$ coset. Since $\Pr[F]\ge p_{i+1}-\varepsilon_{\rm tr}>\mu_{\rm tr}$ and $\Lambda_d\Gamma_d<q\mu_{\rm tr}$, the I6 sparse count excludes full affine dimension. The same minors of its difference matrix satisfy the I6 bound because it depends only on the current basis, trimming and the box. The small-minor lift of the protected lattice-facts lemma gives an integer annihilator of those differences for **each** $c'_j$. Consequently $F^\perp$ contains integer lifts of all new rows. Its rank is at most three by the density bound and $g^{-4}<\mu_{\rm tr}$; the regularization lemma enlarges it to a regular saturated lattice losing at most $2\varepsilon_{\rm tr}$. This proves the claimed induction, including the rank and density. Restoring zero coordinates preserves the claims.

### Mass times Euclidean covolume

For a rank-$d$ lattice $\Lambda$ with integer basis $B$, write $c(\Lambda)=\sqrt{\det(B^\top B)}$ for its covolume in its real span. We will prove that every saturated rank-three normal lattice of maximum fiber mass $m\ge\mu$ satisfies $m c(\Lambda)\le(2828431/1000000)/g^3$. Every regular rank-two output of the regularization procedure of I3 satisfies $m c(\Lambda)\le3855/g^2$, provided its input has the required density and its output density is at least $\mu$. Use precisely that procedure at each joint-fiber extension.

Choose a largest minor of $B$ on $J$ and order these rows first. Set $h=|\det B_J|$ and $P=BB_J^{-1}$, so each entry of $P$ has absolute value at most one. For a prefix length $j\ge d$, write $G_j=P_{[j]}^\top P_{[j]}\succeq I_d$. The inequality follows because the rows on $J$ are unit axes. Let $\Lambda_j$ be the saturation of the prefix and $h_j$ its height. Its covolume is $h_j\sqrt{\det G_j}$. Indeed $B_{[j]}=YC$ with $Y$ a basis of $\Lambda_j$, and $|\det C|=h/h_j$ by the prefix proof of I3. Gram determinants then give the formula. The prefix image $B_{[j]}^\top\mathbb Z^j$ has index $h/h_j$ in $\mathbb Z^d$ by the same proof.

Fix the target of a densest fiber of $B^\top r$. Assume that all nontrivial step orders $s_i$ on the suffix after $j$ are below $g$. Their product is $h/h_j$. Put $S=\sum_i s_i$ over these nontrivial steps. Pad each corresponding box coordinate to width $g_i=s_i\lceil g/s_i\rceil$, keeping its left endpoint $2$. The probability of a subset of the original box is at most its probability under the padded law times $A_{\rm box}=\prod_i g_i/g\le\exp(S/g)$, since every original atom changes by the same reciprocal factor. Write the padded variable as $2+s_i V_i+U_i$, with independent uniforms over the $g_i/s_i$ block indices and residues $0,\ldots,s_i-1$.

Condition on the $V_i$ and the untouched suffix coordinates. There is at most one choice of the $U_i$ giving the fixed target's residue modulo the prefix image. Solve in reverse order of the adjoining steps. At each step the newly adjoined row has order $s_i$ in its quotient, so the residue of its multiplier is unique, and subtracting the selected row multiple reduces the equation to the previous image. This costs a probability factor $h_j/h$ when such a choice exists. After it is fixed, the prefix value is determined, and its probability is at most the maximum prefix fiber mass $m_j$.

For $j>d$ trim the prefix by its own lattice, discarding at most $e$ absolute mass in the original law by I3. The normalized prefix value $P_{[j]}^\top r_{[j]}$ then lies within $R_{\rm tr}g/\sqrt{12}$ of its mean in the norm $\|G_j^{-1/2}\,\cdot\,\|_2$ because the coordinates are an invertible change from the prefix basis. For $j=d$ use the entire exact pivot box of side $g-1$, with $G_j=I_d$ and zero trimming loss. Every suffix row has norm at most $\sqrt d$ in this metric by $G_j\succeq I_d$ and the bound on its entries.

In a padded suffix coordinate replace its residue $U_i$ by $(s_i-1)/2+J_i$, where $J_i$ is independent continuous uniform on $[-s_i/2,s_i/2]$. For other suffix coordinates add independent width-one continuous jitter. The smoothed variables are independent continuous uniforms of widths $g_i$ or $g$, because their consecutive component intervals meet only at endpoints. The displacement in a padded coordinate is at most $s_i-1/2$; each other displacement is at most $1/2$. When $j>d$ the normalized suffix rows have length at most $\sqrt d$ in the $G_j^{-1}$ metric. When $j=d$, $G_j=I_d$ and their maximum coordinates are all at most one. Hence the compatible coarse values put the smoothed suffix in a fixed translated cube of shape $G_j^{1/2}[-w/2,w/2]^d$ for every jitter choice, where
\[
 w=\begin{cases}
 g+2S+N_\star, & j=d,\\
 2R_{\rm tr}g/\sqrt{12}+\sqrt d(2S+N_\star), & j>d .
 \end{cases}
\]
The second cube contains the enlarged prefix metric ball after applying $G_j^{-1/2}$. Both values satisfy $w\ge g$.

We use the following density inequality. If $A$ has row rank $d$ and $X$ has independent side-one uniform coordinates, then $AX$ has density at most $2^{d/2}/\sqrt{\det(AA^\top)}$. It suffices to prove it for $AA^\top=I_d$ by applying the invertible whitening map. Write the columns of this normalized $A$ as $\sqrt{c_i}u_i$, with $u_i$ unit, $0<c_i\le1$, and discard zero columns. Then $\sum_i c_i u_i u_i^\top=I_d$.

If some $c_i>1/2$, project orthogonally off $u_i$. The other projected columns still sum to the identity as outer products on the orthogonal space. Condition on all other input coordinates and integrate the uniform $i$-th input along $u_i$. Its density there is at most $1/\sqrt{c_i}<\sqrt2$: for a test set, the conditional probability is bounded by this constant times the length of its section at the projected point. Fubini and the lower-dimensional density bound prove the claim in this case by induction, with counting mass one in dimension zero.

If all $c_i\le1/2$, the characteristic function at frequency $2z$ is $\prod_i \operatorname{sinc}(\sqrt{c_i}u_i^\top z)$ up to phase, where $\operatorname{sinc}(x)=\sin(x)/x$ with value one at zero. For any nonnegative integrable continuous functions $f_i$, the tight-frame inequality is
\[
 \int_{\mathbb R^d}\prod_i f_i(u_i^\top z)^{c_i}\,dz
 \ \le\ \prod_i\left(\int_{\mathbb R} f_i\right)^{c_i}.
\]
To prove it first take nonzero compactly supported $f_i$, smooth by the one-dimensional heat kernel $f_i(t,s)$, and put $F(t,z)=\prod_i f_i(t,u_i^\top z)^{c_i}$. With $v_i=\partial_s\log f_i(t,u_i^\top z)$, the heat equation and chain rule give
\[
 \partial_t F-\Delta F
   =F\left(\sum_i c_i v_i^2-\left\|\sum_i c_i v_i u_i\right\|_2^2\right)\ge0,
\]
because the matrix with columns $\sqrt{c_i}u_i$ has orthonormal rows. On compact positive time intervals the kernel and its derivatives have Gaussian decay times a polynomial: its first logarithmic derivative is $(-s+\mathbb E U)/(2t)$, the second is $-1/(2t)+\operatorname{Var}(U)/(4t^2)$, with the source $U$ supported where $f_i$ is supported. The tight-frame identity gives the Gaussian decay in $z$, so the integral of the Laplacian vanishes and the integral of $F$ is nondecreasing. Fatou as $t\downarrow0$ bounds the left side. As $t\to\infty$, rescale $z=\sqrt t\,z'$; the product and Jacobian give the standard Gaussian heat kernel on $\mathbb R^d$ times the right side. The limit is dominated by a constant times $\exp(-\|z'\|_2^2/8)$, using bounded source support and $(v-w)^2\ge v^2/2-w^2$. Continuous cutoffs increasing to one and monotone convergence give the asserted inequality for the unbounded supports.

We need the univariate bound $I(p)=\pi^{-1}\int_{\mathbb R}|\operatorname{sinc}(x)|^pdx\le\sqrt{2/p}$ for $p\ge2$. Let $U$ be the uniform density on $[-1/2,1/2]$. Fourier inversion at zero, with frequency $2x$, gives $I(2)=1$, $I(4)=2/3$, and $\pi^{-1}\int\operatorname{sinc}(x)^3dx=3/4$. Indeed, $U*U$ is the tent $(1-|t|)_+$; convolving it with $U$ at zero gives $3/4$, and convolving it with itself at zero gives $2/3$. All these Fourier integrals converge absolutely, and inversion follows by first adding Gaussian smoothing and taking its variance to zero, using continuity of the convolutions.

To bound the absolute cubic integral, write $S_-=(2/\pi)\int_{\{x>0:\sin x<0\}}|\sin x/x|^3dx$. Then $I(3)=3/4+2S_-$. For the first negative interval $[\pi,2\pi]$, split it into four equal parts. The integrals of $|\sin x|^3$ on them are $A,B,B,A$, where $A=2/3-5\sqrt2/12<78/1000$ and $B=5\sqrt2/12<590/1000$, from the antiderivative $-\cos x+\cos^3x/3$ on $[0,\pi]$. Use the left endpoint to bound $x^{-3}$ on each part. On later negative intervals the integrals of $|\sin x|^3$ are $4/3$, and their left endpoints are $(2j+1)\pi$ for $j\ge1$. The decreasing reciprocal cubes sum to at most $1/27+\int_1^\infty(2t+1)^{-3}dt=1/27+1/36$. It follows that
\[
 S_-\le\frac{2}{\pi^4}\left\{\frac{78}{1000}\bigl(1+(4/7)^3\bigr)
           +\frac{590}{1000}\bigl((4/5)^3+(2/3)^3\bigr)
           +\frac43(1/27+1/36)\right\}.
\]
Substituting $\pi>314159/100000$ gives $I(3)<777/1000<\exp(-1/4)$; the latter inequality follows from the alternating cubic lower bound. Hölder interpolation gives $I(p)\le\exp(-(p-2)/4)$ for $2\le p\le3$, and $\log(p/2)\le(p-2)/2$ proves $I(p)\le\sqrt{2/p}$ there. Between three and four the scaled endpoint values $I(p)\sqrt p$ are below $34/25$. The concavity gap of $\log p$ above its endpoint chord is at most $1/72$, by the second derivative bound $1/9$ on this unit interval. Hölder thus gives $I(p)\sqrt p\le(34/25)\exp(1/144)<7/5<\sqrt2$.

For $0<x<\pi$, the difference $(1-x^2/3)\sin x-x\cos x$ has derivative $(x/3)(\sin x-x\cos x)\ge0$, since the parentheses have derivative $x\sin x\ge0$. Integrating $\cot x-1/x\le -x/3$ yields $\operatorname{sinc}(x)\le\exp(-x^2/6)$. For $x\ge\pi$, write $\sin^2x=(1-\cos 2x)/2$ and integrate the cosine term by parts to get $\int_\pi^\infty\sin^2x/x^2\,dx\le1/(2\pi)+1/(4\pi^2)$. Thus for $p\ge4$,
\[
 I(p)\sqrt p\le\sqrt{6/\pi}
       +\frac{2\sqrt p}{\pi}\pi^{2-p}\left(\frac1{2\pi}+\frac1{4\pi^2}\right)<\sqrt2 .
\]
The tail factor decreases on this interval, and at four the upper bound is below $1407/1000$ by $\pi>314159/100000$. This completes the bound on all $p\ge2$.

Apply the tight-frame inequality with $f_i(s)=|\operatorname{sinc}(\sqrt{c_i}s)|^{1/c_i}$. Each integral is at most $\pi\sqrt2$ by the preceding estimate after rescaling. Fourier inversion with frequency $2z$ bounds the density by $\pi^{-d}(\pi\sqrt2)^{\sum_i c_i}=2^{d/2}$. Equivalently, this inversion bound first holds after convolution with a small centered Gaussian by its Fourier integral, and the uniform bound on the smoothed laws passes to the limiting law when integrated against continuous compactly supported tests. The same Gaussian limit justifies the interval convolution inversion at $p=2$, since its transform is integrable and the convolution is continuous. This proves the density inequality, including its determinant factor before normalization.

The probability of the smoothed suffix lying in that translated cube is at most the peak density of its convolution with an independent centered cube of the same shape times $w^d\sqrt{\det G_j}$. Convolution with the constant cube density gives the identity. For each $\delta>0$ enlarge the side by $\delta$, then choose a center arbitrarily close to the required center where the density bound holds, so the enlarged cube contains the original closed cube. Pass to $\delta\downarrow0$ to include boundary values. The linear map from the independent unit-width uniforms to the sum has Gram matrix at least $g^2G_{\rm full}$ in positive semidefinite order, since the added cube supplies $w^2G_j\succeq g^2G_j$ and the suffix widths are at least $g$. The determinant is then at least $g^{2d}\det G_{\rm full}$, by conjugating with the inverse square root of the smaller positive matrix. Hence the probability is at most $2^{d/2}(w/g)^d\sqrt{\det G_j/\det G_{\rm full}}$. The compatible coarse probability is at most this, since compatible choices give membership for every jitter. Multiply by the conditional factor $m_j h_j/h$ and the padding factor $A_{\rm box}$, then by the final covolume, to obtain
\[
 (m-e')c(\Lambda)\le A_{\rm box}\,2^{d/2}(w/g)^d\,m_j c(\Lambda_j),
 \qquad e'=e\text{ if trimmed and }e'=0\text{ otherwise}.
\]

For rank three take $j=d=3$. The step orders are below $g$ since their product is $h\le H_3\le g/16777216$. Also $S\le h$, since the sum of integers at least two is at most their product for two or more, by induction, and the other cases hold directly. The multiplier is bounded by
\[
 \frac{16777216}{16777215}(707107/250000)(1+3/16777216)^3<2828431/1000000 .
\]
Also $\exp(x)\le 1/(1-x)$ for $0\le x<1$ follows term by term, and $N_\star/g\le1/16777216$. The initial product of mass and covolume is $g^{-3}$.

### Support of a dense rank-three normal lattice

Let $B$ be an integer basis of a saturated rank-three lattice on any subset of the independent box coordinates with maximal fiber mass $m\ge\mu$. By I3 and H3 its height has $1\le h\le H_3<4$. With $J$ a largest three-by-three minor, put $P=BB_J^{-1}$. The pivot rows are the identity, and each suffix entry has absolute value at most one and is a multiple of $1/h$ by the determinant formula for $B_J^{-1}$.

Use the padded residue calculation above at the pivot prefix $j=3$. The nonunit orders have product $h$ and sum $S\le h$, so each is below $g$. The factor from compatible residues is $1/h$ and the factor from the fixed values of three pivots is $g^{-3}$. For any one pivot coordinate, the smoothed suffix is consequently restricted to an interval of length at most $g+2S+N_\star<g(1+2^{-23})$ by the same displacement calculation with $G_3=I_3$. More precisely, condition on the coarse padded values and the untouched suffix coordinates. For a compatible choice there is only one residue tuple, and every jitter of the coarse values yields membership in this enlarged interval. Thus its probability under the independent smoothed suffix is an upper bound on the coarse compatibility probability. The initial padding factor is at most $\exp(S/g)\le(1-3/g)^{-1}\le1+2^{-50}$.

Suppose at least 2 entries of this suffix column are nonzero. Retain 2 and condition on the other smoothed variables, which only translates the interval. Each retained signed smoothed variable is uniform on an interval of width at least $g/h$. After centering, the convolution density of any collection of centered uniform intervals is even and decreasing on the nonnegative half-line. This holds by induction: integrating an even decreasing density over a moving symmetric interval gives a function with derivative proportional to the right endpoint density minus the left endpoint density, nonpositive for nonnegative centers. The single uniform density is even decreasing, and the first convolution can also be obtained by its interval lengths. Therefore a centered interval maximizes capture probability, and reducing any summand's width to $g/h$ cannot lower that centered probability. Indeed condition on that summand and average the other summands' interval capture function over its centered uniform interval, an average of an even decreasing function that is nonincreasing in the width.

Scale by $h/g$ so the retained uniforms have width one. The ratio of the mass of the centered interval of length $h(1+2^{-23})$ to $h$ is at most the mass of its concentric interval of length $1+2^{-23}$, since the average density on centered intervals is nonincreasing in length. This cancels the residue factor. The latter interval has mass at most $p_{\rm c}+2^{-23}$, since convolution with probability densities cannot increase the peak of a width-one uniform density above one. Here $p_{\rm c}$ is the centered width-one probability for a sum of 2 independent width-one uniforms. For $r$ such uniforms shifted to $[0,1]$, the CDF at $x$ is
\[
 F_r(x)=\frac1{r!}\sum_{0\le j\le \lfloor x\rfloor}
 (-1)^j\binom rj(x-j)^r .
\]
This follows by inclusion-exclusion on the unit upper bounds of the coordinates in the nonnegative simplex of sum at most $x$. Face events have measure zero and the unconstrained simplex has volume $x^r/r!$ by iterated integration. Symmetry gives $p_{\rm c}=2F_r((r+1)/2)-1$. At $r=2$ this is $3/4$. Combining the factors proves
\[
 m\le g^{-3}(1+2^{-50})(p_{\rm c}+2^{-23})
 <\alpha_*g^{-3}\le\mu,
\]
where the strict comparison is rational substitution. This contradicts density. Each pivot column therefore has at most 2-1 nonzero suffix entries plus its pivot, and their total support is at most $u=3\cdot 2=6$. Every vector in the span has that support restriction. This applies to every rank-three containing lattice of I3 of the indicated mass, including its use as a strict prefix.

For rank two use the chosen prefix sequence of the regularization proof of I3. If the final normal lattice is strictly larger, the procedure returns a rank-three lattice, covered above. Otherwise choose $j=d$ if no preceding prefix has a strictly larger normal, and the first prefix after the last strictly larger normal otherwise. The suffix steps have order below $g$: as in I3 an order at least $g$ places a new coordinate normal vanishing on $J$ into the next selected fiber's normal, contradicting the choice of the last strict prefix.

The product of the remaining orders is at most the height $h\le H_2<g^{19/10}$. Call an order large if at least $g^{2/3}$. Three large orders would have product at least $g^2$, so there are at most two. For their width ratios $x,y\in[0,1]$, setting a missing ratio to zero, one has $xy<g^{-1/10}\le2^{-13/2}<1/90$. Thus $x+y\le1+xy<1+1/90$, and $(1+x)(1+y)<2+2/90$. The number of small nonunit orders is less than $(19/10)\log_2 g<483$, and each contributes less than $g^{-1/3}<2^{-21}$ to $S/g$. By rational substitution,
\[
 S/g<1+1/90+483/2^{21}<1012/1000,
 \qquad A_{\rm box}<(2+2/90)/(1-483/2^{21})<203/100.
\]
The latter estimate uses the large-order product bound and $\prod(1+x_i)\le \exp(\sum x_i)\le1/(1-\sum x_i)$ for the small orders. Thus $\sqrt2(2S+N_\star)/g<287/100$ using $\sqrt2<99/70$ and $N_\star/g\le2^{-24}$. The pivot side ratio is below four. With the pivot prefix the rectangle estimate gives $m c(\Lambda)<(203/100)\cdot2\cdot4^2/g^2$. For a later prefix use the narrowed side below.

When $j>d$ the preceding rank-three regular containing lattice used to trim $F_j$ in I3 has basis $B_{\rm old}$, covolume $c_{\rm old}$ and mass $m_{\rm old}$. It obeys $m_{\rm old}c_{\rm old}\le(2828431/1000000)/g^3$. Let $C=\operatorname{diag}(B_{\rm old},1)$ on the previous prefix plus its new coordinate, and $G=C^\top C$. This is an integer basis of a saturated rank-four lattice, as both summands are saturated. All normals to $F_j$ restrict on the previous coordinates to the span of $B_{\rm old}$ by I3. Thus $C$ carries the real annihilator of differences in the image $C^\top F_j$ isomorphically to the real normal space, and its saturation implies that the image coefficient normals have a saturated basis $V$ in $\mathbb Z^4$ with $CV$ a basis of the integer normal lattice $\Lambda_j$. Its rank here is two. Hence the affine image space has dimension two.

Whitening the image coordinates by $G^{-1/2}$ maps the difference lattice $\ker V^\top\cap\mathbb Z^4$ to the orthogonal complement of $G^{1/2}V$ with planar covolume
\[
 \delta=\sqrt{\det(V^\top G V)}/\sqrt{\det G}=c(\Lambda_j)/c_{\rm old}.
\]
To see the identity, extend a basis of the kernel lattice with two integer columns $L$ such that $V^\top L=I_2$. They exist by saturation of $V$, which gives $V^\top\mathbb Z^4=\mathbb Z^2$. The full extended basis is unimodular by decomposing an integer vector via $V^\top$. After whitening it has full volume $1/\sqrt{\det G}$. Its last two columns project onto the normal plane as $G^{1/2}V(V^\top G V)^{-1}$, whose area is $1/\sqrt{\det(V^\top G V)}$. Multiplying by the planar covolume gives the full volume and proves the identity.

The rank-three predecessor has support at most $u=6$ by the support lemma. In the whitened feature space the map $G^{-1/2}C^\top$ has orthonormal rows since $G=C^\top C$, and only those $u$ old coordinates and one new coordinate can contribute. Subtract their box center, giving length at most $g\sqrt{u+1}/2$ before the map and hence after it. Thus the whitened region lies in a ball of this radius, and its planar slice has area at most $A=\pi g^2(u+1)/4$.

The current rank-two prefix basis and the matrix $P_{[j]}$ have the same column span, spanned also by $CV$. The whitening $G_j^{-1/2}P_{[j]}^\top$ therefore uses an orthonormal pair in the span of the rows of $G^{-1/2}C^\top$. The prefix values in that metric lie within the same radius of their mean by orthogonal projection. The rectangle argument thus allows the narrower side $w=g\sqrt{u+1}+\sqrt2(2S+N_\star)$, which still satisfies $w\ge g$. In particular $w/g\le 27579/5000$, since $\sqrt{u+1}\le 13229/5000$ and the displacement bound is below $287/100$.

The image point count $M$ satisfies $M\le 2A/\delta+2$ by the simplex count in I3. Each image point has mass at most $m_{\rm old}/g$ by independence. Moreover $\Pr[F_j]\ge m_j-e\ge999\mu/1000$ by the prefix density premise and the Euclidean guard. Since $m_{\rm old}\le g^{-3}$ and $g^4\mu\ge10000$, $M\ge9990$. It follows that $M-2\ge999M/1000$, so
\[
 (m_j-e)c(\Lambda_j)
 \le M(m_{\rm old}/g)\delta c_{\rm old}
 \le (2000/999)\pi((u+1)/4)g\, m_{\rm old}c_{\rm old}
 \le(11000/999)g\,m_{\rm old}c_{\rm old},
\]
where the last inequality uses $\pi<22/7$. Combining with the suffix bound and the ratios $m/(m-e),m_j/(m_j-e)\le1000/999$ yields
\[
 m c(\Lambda)\le(1000/999)^2\,((203/100)\cdot2\cdot(27579/5000)^2)\cdot(11000/999)\cdot(2828431/1000000)/g^2
 \le 3855/g^2 .
\]
If regularization starts in rank one and returns a rank-two lattice from a recursive call, apply this calculation to the rank-two call and its selected sequence. This proves the needed rank-two mass-covolume estimate.

### Rank-one Euclidean covolume

Use $C_1=\lceil110000 C_2+20000000 C_3+250\rceil$ from I6. For a rank-one regular output of I3 of mass $m\ge\mu$, choose the pivot prefix $j=1$ or the first prefix after the last strict normal, as for rank two. The suffix orders satisfy $s_i<g$ by the unit-vector argument, and their product is at most $h\le H_1<g^4$. Use widths $s_i$. Call $s_i\ge g^{4/5}$ large and write $L$ for their number, so $L\le4$. For $s>1$, the ratio $(s-1)/\log s$ is increasing, as differentiation gives a derivative of the sign of $\log s-1+1/s\ge0$. Applying it up to $g^{4/5}$ gives small-order sum divided by $g$ below $1016/g+(5-L)g^{-1/5}<1/150$, since $g<q<2^{254}$ and $g\ge2^{49}$. Hence the padding is below $16e^{1/150}<17$, or $2e^{1/150}<203/100$ for $L\le1$. With $R_{\rm tr}\le20$ and $N_\star/g\le1/1024$, the inherited padded smoothing uses $2S+N_\star$, so $w/g$ is below ten for a pivot prefix, below twenty for a trimmed prefix and below fourteen for a trimmed prefix when $L\le1$.

For $j=1$, $m_j c(\Lambda_j)=1/g$, so the rectangle estimate gives $m c(\Lambda)<250/g$. Otherwise the preceding strict normal is contained in the regular trimming lattice of rank $r=2$ or $3$, with mass $m_{\rm old}$ and covolume $c_{\rm old}$. Use the rank-two proof’s diagonal basis $C$ and whitening. The current image normal has one primitive integer column $V$. A basis of $\ker V^\top$ extended by an integer column $L_0$ with $V^\top L_0=1$ is unimodular. The last whitened column has normal projection of length $1/\sqrt{V^\top C^\top C V}$, so the difference lattice has covolume $\delta=c(\Lambda_j)/c_{\rm old}$. The section lies in a ball of radius $g\sqrt{R_{\rm tr}^2/12+1/4}<6g$. Its $M\ge r+1$ image points have mass at most $m_{\rm old}/g$ each, and I3 gives $(M-r)\delta\le r!$ times the section volume.

For $r=3$ the ball gives $M\delta<22000g^3$ using $M/(M-3)\le4$, so $(m_j-e)c(\Lambda_j)\le22000 C_3/g$. For $r=2$, the disk and $M/(M-2)\le3$ give $M\delta<680g^2$. If $L\ge2$, the suffix inequalities give $m_j\ge(g^{4/5}/2)^2m$. The previous rank-two mass is at most $g^{-2}$ by its pivots. Thus $M\ge(999/1000)m_j g^3>2^{27}$ since $m>g^{-4}$. Now $M/(M-2)<1001/1000$ and squared radius at most $(400/12+1/4)g^2$ imply $M\delta<213g^2$. The two rank-two bounds give $(m_j-e)c(\Lambda_j)\le680 C_2/g$ or $213 C_2/g$.

In the rectangle estimate each trimming ratio is at most $1000/999$ and the density factor below $99/70$. The coefficients on $C_2/g$ are at most $(1000/999)^2(99/70)(203/100)14\cdot680$ and $(1000/999)^2(99/70)17\cdot20\cdot213$, both below 110000. The coefficient on $C_3/g$ is at most $(1000/999)^2(99/70)17\cdot20\cdot22000<20000000$. Hence $m c(\Lambda)\le C_1/g$ throughout, without imposing any passing test.

### Euclidean multiples in every heavy stack

Let $\mathcal V$ be the row space of a heavy stack with nonzero kernel vector $v$, with $v_0=0$. The stack fiber is that of any row-space basis. If some $w\in\mathcal V$ has $w_0\ne0$, then conditional on the independent box coordinates $w^\top r$ is uniform on $g$ distinct values through $r_\diamond$ since $g<q$ and $v^\top r$ is fixed. The guessing probability of $v^\top r$ is above $g\theta$, so applying joint fibers to it on the box gives a normal lattice of density above $g\mu$ since $g\theta-3e>g\mu$. If all of $\mathcal V$ has zeroth coordinate zero, apply joint fibers to its basis on the box. This gives a normal lattice of density above $\mu$ containing $\mathcal V$ modulo $q$. Either lattice has rank at most three and contains the line of $v$ modulo $q$. If its rank were three, its support would have at most $u$ coordinates by the support lemma, since the mass is at least $\mu$ in both cases. Every vector in its reduction would have that support restriction, in particular $v$. This contradicts the fixed Vandermonde rows of the actual form kernel. Hence the containing lattice has rank at most two for every kernel direction.

In rank one its primitive generator has norm $c(\Lambda)\le C_1/(g\mu)\le B_{\rm E}$, and saturation gives a nonzero residue on the line. In rank two the covolume bound is $C_2/(g^2\mu)$. The coefficient preimage of the line of $v$ has index $q$, since a saturated basis has full rank modulo $q$. Its covolume is multiplied by that index. The two-dimensional shortest-vector inequality below and the squared I6 guard give a nonzero vector of norm at most $B_{\rm E}$. Its residue is nonzero since $2B_{\rm E}<q$. Appending the zero homogeneous coordinate preserves norm. This proves a short multiple for every kernel vector of every heavy stack. Recovery selects a kernel vector by the form equations on the recovered basis, without constructing the normal lattice.

For the Euclidean lift in rank two take a shortest nonzero $u_1$ of length $\lambda_1(L)$. It is primitive, so it extends to a basis $u_1,v_1$. Subtract a nearest integral multiple of $u_1$ from $v_1$. Then $|u_1^\top v_1|\le\|u_1\|^2/2$ and $\|v_1\|\ge\|u_1\|$, so $c(L)\ge(\sqrt3/2)\lambda_1(L)^2$. The strict numerical bound $2/\sqrt3<231/200$ follows by squaring. Thus I6 proves the required norm bound since its squared guard coefficient is $(231/200)C_2$. These are existence bounds; the short-span algorithm below supplies a polynomial-time lift without needing the basis of the lattice used in the existence proof.

### Polynomial-time Euclidean lifting

For input $v\ne0$ with zero zeroth coordinate, discard that coordinate and order the others with $v_1\ne0$. Define $L_i=\{x\in\mathbb Z^i:\bar x\in\mathbb F_q v_{[i]}\}$ and let $S_i$ be the real span of vectors of $L_i$ of length at most $B_{\rm E}$. There cannot be four independent such vectors. They would have a nonzero $4$-by-$4$ minor. Its rows modulo $q$ have rank at most one. If all reduce to zero, the determinant is a multiple of $q^4$. Otherwise subtract from each other row an integer multiple of a row with nonzero residue, making three rows divisible by $q$. The determinant is then divisible by $q^3$, although Hadamard bounds its absolute value by $B_{\rm E}^4<q^3$. Therefore $\dim S_i\le3$.

Maintain an actual list of short vectors spanning $S_i$, initialized in length one with the vector $1$. This belongs to $L_1$ because $v_1\ne0$, and $1\le B_{\rm E}$. Projection of a short vector at the next prefix is short at the preceding prefix. Thus search only in $S_i\times\mathbb R$, of dimension at most four. Let $U$ be the matrix whose columns are the current basis vectors extended by a zero last coordinate, and the final unit vector. Choose an invertible minor on rows $J$. The matrix $C=UU_J^{-1}$ parametrizes possible vectors by their $J$-coordinates $y$. Write $C=A/c$ for $c=|\det U_J|$, with integer entries of $A$. Both $A$ and $c$ have $O(\log q)$-bit entries by fixed-size determinants and the bound $B_{\rm E}<q$ on the columns of $U$. Integer vectors therein must have integer coordinates $y$. Require for each row $j$
\[
 A_j y\equiv0\bmod c,\qquad (v_1 A_j-v_j A_1)y\equiv0\bmod cq ,
\]
with integer representatives of the $v_j$. These impose exactly integrality and membership in $L_{i+1}$, including if $q\mid c$, because after integrality the second test is equivalent to the congruence on the integral vector.

Compute the lattice of permitted $y$ by processing each congruence in the current basis. Extended-gcd unimodular column operations put its coefficient row in the form $(h,0,\ldots,0)$, with $h$ its gcd. For a modulus $b$, scale the first basis column by $b/\gcd(b,h)$ to impose the congruence. Ignore a zero row. After each update triangularize the basis by successive rows. In each row use extended-gcd operations on the columns not yet assigned pivots, obtaining a positive pivot and zeros in that row to its right. The earlier rows have zeros in those columns and are preserved. Then reduce the entries in each row left of its pivot to residues between zero and that pivot minus one, by subtracting multiples of that column, in row order. Later pivot columns have zeros in the preceding rows, so each preceding reduction stays valid. Its pivots multiply to the index, which is at most the product of the $O(i+1)$ moduli, each at most $cq$. The reduced entries and pivots therefore have bit length $O((i+1)\log q)$. There are at most four gcd reductions and at most sixteen residue updates for each basis normalization. Intermediate integer bit lengths and running time are polynomial because the number of columns is bounded and each gcd or exact quotient acts on polynomial-size integers. Applying $C$ gives an integer basis $D_i$ of $L_{i+1}\cap(S_i\times\mathbb R)$.

We give the fixed-dimensional search for a new short vector explicitly. The input is an integer lattice $L$ of rank $r\le4$, with a given basis of polynomial bit length in a Euclidean coordinate space, and a list of independent short vectors of $L$ spanning $W$. In the prefix application the list has at most three vectors, each of length at most $B_{\rm E}$.

We first describe a rational basis reduction routine used twice below. Multiply a rational basis by a common denominator, run the routine on the integer basis, and divide by the same scalar at the end. Write $b_i^*$ for the Gram–Schmidt vectors, and $\eta_{ij}$ for the coefficient of $b_j^*$ in $b_i$, $j<i$. Fully size-reduce by subtracting nearest integer multiples of $b_j$, with descending $j<i$ for each $i$. Since $b_j$ only has Gram–Schmidt coordinates through $j$, this establishes $|\eta_{ij}|\le1/2$ without undoing a larger-index reduction. If some adjacent pair violates
\[
 \|b_{i+1}^*\|_2^2+\eta_{i+1,i}^2\|b_i^*\|_2^2
 \ \ge\ (3/4)\|b_i^*\|_2^2 ,
\]
swap $b_i,b_{i+1}$ and repeat the full size reduction. All operations are integral unimodular basis changes. For a basis of integers put $H_j=\det(B_{[j]}^\top B_{[j]})$, the squared volume of its first $j$ columns, and $H_0=1$. These are positive integers. Size reduction leaves all $H_j$ unchanged. A swap changes only $H_i$, by the ratio of the left to the unscaled $\|b_i^*\|_2^2$ on the right of the displayed inequality. This follows by projecting the new column $b_{i+1}$ orthogonally off the first $i-1$ columns and comparing its squared length to that of $b_i^*$. Thus every swap shrinks $\prod_j H_j$ by a factor below $3/4$. Its initial logarithm is polynomial by the input bit length and Hadamard, and it stays at least one. At each fully reduced stage $\|b_i^*\|_2^2=H_i/H_{i-1}\le\prod_j H_j$, and size reduction then gives $\|b_i\|_2^2\le r\prod_j H_j$. The next swap preserves these length bounds on the columns. Each subsequent pass computes rational Gram–Schmidt data and at most $r(r-1)/2$ integer updates before the same bound is restored. With $r\le4$ the intermediate bit lengths are polynomial by exact rational operations on these bounded integer coordinate arrays. This proves polynomial bit time and the final estimates
\[
 \|b_{i+1}^*\|_2^2\ge \tfrac12\|b_i^*\|_2^2,\qquad |\eta_{ij}|\le\tfrac12.
\]
Track original basis coordinates by exact solving with rational minors, so a reduced-basis expression always has a known lift in that basis.

For a reduced basis of rank at most four we can also solve the exact closest-vector problem in polynomial time. Work in its real span by orthogonally projecting the target $x$, since the perpendicular component adds a constant squared distance. Nearest-plane rounding, from last column to first, subtracts the nearest integer multiple in each last Gram–Schmidt coordinate of the residual. Later subtractions from earlier columns leave the already reduced higher Gram–Schmidt coordinates unchanged. The residual's norm is at most $\tfrac12\sqrt{\sum_i\|b_i^*\|_2^2}$. By the final estimates this is at most $\tfrac12\sqrt{2^r-1}\,\|b_r^*\|_2<2\|b_r^*\|_2$ for $r\le4$. A closest vector therefore has last basis coefficient within two of the last Gram–Schmidt coordinate of $x$, expressed in units of $b_r^*$. Enumerate all integers in that interval. For each candidate subtract that multiple of $b_r$, project the result to the span of the first $r-1$ columns, and recursively find the closest vector in the lattice of those columns. Its squared distance plus the residual orthogonal squared distance is the exact best value for that last coefficient. The prefix basis is still reduced, so the argument applies at each recursion, with rank zero solved by returning the zero vector. At most five recursive choices per level and fixed depth give polynomial bit time. Coordinate centers, squared distances and nearest integers are evaluated with exact rational arithmetic. At fixed depth their bit lengths remain polynomial by the basis bounds and the rational formulas for projections and centers.

Now compute a basis of $L\cap W$ and extend it to a basis of $L$. In the given basis coordinates of $L$, $W$ is a rational subspace of $\mathbb R^r$, specified by at most $r$ normal rows after clearing denominators in a nullspace basis. Starting from the identity basis on $\mathbb Z^r$, restrict each normal successively to the current kernel columns. For a nonzero row there, extended-gcd unimodular column operations make the row $(h,0,\ldots,0)$ with $h\ne0$. The kernel is exactly the last columns. Retain the first transformed column as a complement, and apply the next restriction only to the kernel columns. Induction gives a unimodular full basis with the final kernel columns spanning all integer points of $W$ in these coordinates. This uses at most four operations of this row-reduction type, each of polynomial bit time by the extended Euclidean algorithm in fixed dimension. Apply the original basis map to get the two sets of columns in $L$.

Project the complementary columns orthogonally off $W$. They form a rational basis of the projected lattice $L'$ because the other columns project to zero and the complements are independent modulo $W$. Each projected lattice point has a lift by the recorded complementary basis coordinates. If $L'$ has rank zero, there is no vector outside $W$. Otherwise reduce its basis by the routine above. If its first vector has norm at most $B_{\rm E}/2$, lift that vector to $L$ and reduce its $W$ component by nearest-plane rounding in the **stored short-vector basis** of $W$. The short-vector basis spans $W$ and consists of actual integer lattice vectors. It need not be the full basis of $L\cap W$ for this rounding step. Every one of its Gram–Schmidt lengths is at most $B_{\rm E}$. After rounding the squared length of the $W$ component is at most $3B_{\rm E}^2/4$; the perpendicular component has squared length at most $B_{\rm E}^2/4$. This returns a short vector outside $W$.

If the first projected reduced basis vector has norm greater than $B_{\rm E}/2$, the final reduction estimates imply that every projected Gram–Schmidt length is greater than $2^{-(r+1)/2}B_{\rm E}$, with $r\le4$. Enumerate every nonzero projected point of length at most $B_{\rm E}$ by descending basis coordinates. Given later integer coordinates, the coefficient of $b_i^*$ is the current coordinate plus a fixed rational shift. Its permitted interval has radius at most $B_{\rm E}/\|b_i^*\|_2<6$ in these units. Enumerating within six of each center and checking the exact squared norm therefore lists every candidate, in a number of branches bounded independently of the input. For each projected point choose a lift $x\in L$. The other lifts are $x+L\cap W$. Use the exact closest-vector routine just proved in $L\cap W$ with target the negative of the $W$ component of $x$. Its output minimizes the total squared length among these lifts by orthogonality. If that minimum is at most $B_{\rm E}^2$, return the lift. If no candidate works, no short vector outside $W$ exists. The orthogonal projections come from rational linear solves in dimension at most four; integer-coordinate conversions and all comparisons have polynomial bit length. This completes the fixed-dimensional search.

Apply this search repeatedly at a prefix, starting with $W=0$ in the located lattice with basis $D_i$. Each success adds an actual short vector and raises the dimension of $W$. When the search certifies there is no short vector outside, the list spans $S_{i+1}$. At most four searches are needed, since its dimension is at most three. Together with the $O(N_\star)$ congruence updates per prefix, the total bit work $T_{\rm LIFT}$ is polynomial in $N_\star,\log q$. At the final prefix return a stored nonzero short vector if the span is nonzero and $\bot$ otherwise. Restore coordinate order and the zero homogeneous coordinate. Its residue is nonzero by the length bound and belongs to the prescribed line by the defining congruences. This is an exact algorithm for the Euclidean lift used in the reduction.

## Amendment msis_norm

Set $\mathrm{msis\_norm}=2$ in the concatenated integer coefficient basis of C5. For any kernel vector $v$ and any Euclidean-short multiple $x\equiv a v\bmod q$, $a\ne0$, the bound $2B_{\rm E}<q$ forces $x_0=0$. Packing copies all other coordinates once, inserts zeros and commutes with reduction. Thus $A\hat x=aA\hat v=0\bmod q$ and $0<\|\hat x\|_2=\|x\|_2\le B_{\rm E}$, which proves the universal Euclidean packing clause. The original infinity clause remains true at its own norm and radius, as shown in msis_bound. There the heavy-stack selection and lifting prove existence and recovery for the amended reduction. Neither the public seed law, ring matrix, ciphertext nor decryption operation counts use the solution norm. Targets proves extraction and the reduction cost.

## Targets

Fix any parameter set satisfying the amended model, the protected system shape, any admissible evaluation points, and the stated group and oracle models. In the chosen modes use the coefficient positions of Amendment n, the base field of Amendment C6 and the grid and masks of Amendment C7, and the single-sector QAP encryption and decryption of Amendment n1. The amended inverse theorem applies by (P3) with Amendments I3, I4, H3 and I6. The charged-mark bound is proved in Amendment Ncmp. Correctness and extraction use the same external witness relation, oracle model, budgets and probability bounds. Internally the projected witness forgets its Boolean tags.

### Correctness with error $2/q$

Fix an external witness $w$, the statement, message and admissible evaluation points. Every tag extension used in n1 is a witness of the internal system. If the prescribed weight of $v^{(0)}$ is zero decryption returns $\bot$. Otherwise the chosen target has nonzero weight, whenever the ordinary or direct-normalization branch is selected. The quotient and remainder identities of n1 recover the exact key in these branches, both for the designated setup and for a prescribed admissible placement. They give the settled target value after the three exact integer logarithms and the equality $a_t+b_t-c_t=v^{(t)}$ in the ordinary branch, and directly in the branch where the chosen target base is zero. The evaluation-point branch recovers the exact key on every realization where it is called. Therefore failure is exactly the event of zero prescribed weight, which we bound next.

First consider the key weight for either fixed target. Let $L:F\to\mathbb F_q$ be the constant-slot coefficient functional in the form basis, nonzero because $L(1)=1$, and let $s=n/2-1$. Then the weight of a form value $x$ is $Q(x)=L(x\sigma^s(x))$, with $x$ uniform on the affine space with constant slot one and the prescribed fixed-row values of that target. The $k$ other slots are uniform by the independent homogeneous matrix column. The trace map is nonzero: the polynomial $\sum_{j=0}^{n-1}X^{q^j}$ has degree $q^{n-1}<q^n$ and cannot vanish at all $q^n$ field elements. The pairing $(a,b)\mapsto\operatorname{Tr}(ab)$ is therefore nondegenerate, since multiplication by a nonzero $a$ is invertible. Thus $L(x)=\operatorname{Tr}(\lambda x)$ for a unique nonzero $\lambda$, by equality of the dimensions of the field and its scalar dual.

The polar form $Q(x+y)-Q(x)-Q(y)$ is
\[
 \operatorname{Tr}\!\left((\sigma^{-s}(\lambda x)+\lambda\sigma^s(x))\,y\right).
\]
Trace invariance under Frobenius gives this expression. By nondegeneracy, the radical solves $\lambda x+\sigma^s(\lambda)\sigma^{2s}(x)=0$. If there is one nonzero solution $x_0$, every other solution is $x_0$ times an element fixed by $\sigma^{2s}$, by dividing the two equations. Since $\gcd(2s,n)=2$, such a ratio is fixed by $\sigma^2$: use the integer Bezout identity for $2s,n$ and $\sigma^n=1$. There are at most $q^2$ of these ratios because they are roots of $X^{q^2}-X$. Hence the radical dimension is at most two and the polar rank at least $n-2$. The affine form domain has codimension $\mathrm{form\_pad}$. Restricting the polar form in either argument to its parallel linear space loses at most $\mathrm{form\_pad}$ ranks, by the rank of the omitted rows or columns. Therefore its rank is at least $n-2-2\mathrm{form\_pad}$, at least six in the scored shape and in the growing branch.

For an affine quadratic of rank $d$ over the fixed odd prime field, the proportion of zeros is at most $1/q+q^{-d/2}$. Indeed, use the character sum $q^{-1}\sum_{a\in\mathbb F_q}\exp(2\pi i a Q/q)$ for its zero indicator. A linear change of variables diagonalizes the quadratic part in odd characteristic, by choosing a vector with a nonzero square coefficient, completing its square to isolate it, and iterating. With $a\ne0$ a one-variable sum for a nonzero square coefficient has magnitude $\sqrt q$, even with a linear term: by completing the square the linear term is a unit-magnitude factor, and the squared magnitude of $\sum_x\exp(2\pi i c x^2/q)$ is the sum over $x,y$ of $\exp(2\pi i c(x-y)(x+y)/q)$. The map to $x-y,x+y$ is invertible, and summing first over one new coordinate gives $q$, since only the other coordinate zero has a nonzero inner sum. Every other coordinate has character sum bounded by $q$. After normalization the contribution of all nonzero $a$ to the zero probability is at most $q^{-d/2}$, and the zero character contributes $1/q$. Here C5, C6 and n give $n=3434$, $\mathrm{form\_pad}=7$ and polar rank $d\ge 3418$, so the key weight vanishes with probability at most $1/q+1/q^3$, and in particular at most $1/q+1/q^2$.

For the search probabilities condition on all scalar coins except $y$ and the seed matrix. Set $S(x)=\sum_c\gamma_c\xi_c(x)$ on the form field. It has the expression
\[
 S(x)=\operatorname{Tr}(\lambda_U x\sigma^s(x)+\lambda_V x\sigma^{n/2}(x)).
\]
Indeed the $U$ weights are the full coefficient list of $x\sigma^s(x)$; the linear functional on this list is nonzero since its coefficient at the constant cell is $\pi(1+\varepsilon)s_{\rm U}\ne0$. Its trace representer $\lambda_U$ is nonzero. The other weights are the even coefficient list of the half-turn invariant product; extend that linear functional to the full form field to obtain $\lambda_V$. Trace invariance shows its polar radical has equation
\[
 \lambda_U\sigma^s(x)+
 (\lambda_V+\sigma^{n/2}(\lambda_V))\sigma^{n/2}(x)
 +\sigma^{-s}(\lambda_U)\sigma^{-s}(x)=0 .
\]
The exponents $s,n/2,-s$ are consecutive modulo $n$. Setting $t=\sigma^s(x)$ gives a nonzero polynomial in $t$ of degree at most $q^2$, since the coefficient of $t$ is $\lambda_U\ne0$. Its root count is at most $q^2$, so the full rank is at least $n-2$. Restriction to the common space of free coefficient positions loses at most $2(u+1)$ ranks as before. Thus $S$ is nonzero on every prescribed affine coset, including different fixed-row values at different tags. Its zero probability on each is at most $2/q$ by the polynomial root bound. The first factor $y(v)$ in any prescribed base is independently uniform and vanishes with probability $1/q$, so the base-zero probability is at most $3/q$.

For two distinct tag variants the form values are jointly uniform on their respective affine cosets, because fixing all other random columns leaves the homogeneous column and a differing tag column with a two-by-two evaluation matrix of determinant $1$ or $-1$ in each free row. Likewise the two $y$ values are independent uniform, by the same determinant and independence of $y$ from the seed. The pair zero-event bound is at most $9/q^2$. A specified primary zero-corner base-zero event and a zero key weight of $v^{(1)}$ have probability at most $6/q^2$ by their distinct tags and the single-weight bound.

The fallback requires at least one base zero among $a_0,b_0,c_0$, and either a zero secondary target weight or at least one base zero among $a_1,b_1,c_1$. Otherwise the selector gives an ordinary or direct normalization branch. The three events of the first kind paired with the secondary weight contribute at most $18/q^2$ and the nine pairs of base events contribute at most $81/q^2$. Thus fallback probability is at most $99/q^2\le135/q^2$. An ordinary secondary triple also requires a zero among the three primary ordinary bases, so its probability is at most $9/q$. All bounds hold conditional on the fixed scalar coins and therefore also unconditionally, and all selection events are independent of the integer sampler.

### Extraction and the reduction

Let $\mathcal A$ have the budget $Q<2^\lambda$ of generic group calls and at most $2^\lambda$ queries to each oracle. Fix one bit $b$ and messages $m_0,m_1$, and run the extraction experiment with $m_b$. The extractor reads the answered generic transcript without any oracle calls. It uses the protected extractor sketches for the plain sector. The empty alpha sector can be represented by zero records. It samples three independent probe vectors for each cell, uses the linear combinations of source-group records and pairings to form sketches, tests the sketches of the result and the difference when there is an old record, and directly checks its ordinary assignment against $S$, checks the three tag bits, and returns the ordinary witness only. In rank at most three, there are at most four assignments with first coordinate 1 to test: row echelon pivot coordinates determine the vector, pivot 0 must be present, and at most two remaining pivot choices are bits. Output is therefore always $\bot$ or a witness. A record creation, result, or difference touches $O(K_1N_\star+n)$ field elements, since a source-group record uses at most $K_1$ length-$(N_\star+1)$ vectors or $6A_c$ values, and the pairings compute six such combined sketch vectors. For a pairing, forming the inner products in the G2 record or summing per left leg and combining the G1 vectors uses $O(K_1N_\star+n)$ operations. A test uses $O(N_\star)$ for elimination with at most three rows and $O(N_\star+|S|)$ to generate and check the constant number of candidates. Initialization samples $6A_c(N_\star+1)$ field values, enters the $L$ labels as records whose vectors are materialized on first use, and uses $O(nN+L)$ time. There are at most four tests per result. Thus the extractor uses $O((Q+1)(nN+|S|)+L)$ time because $K_1\le n$ and $N_\star\ge1$.

The reduction on input a uniform $A\in R_q^{k\times\ell}$ samples the seed and programs the raw seed-oracle answers on columns $1,\ldots,\ell$ as $E(A_{ij})$. It samples every other answer lazily as an independent uniform tuple, including column zero, and returns the same tuple on repeated queries. Thus each programmed conceptual coefficient entry is exactly $A_{ij}$, and the raw tuple law is the same as in encryption by invertibility of $E$. If the challenge is supplied in the coefficient representation, the reduction performs these forward transforms once during its initialization. This costs $O(k(\ell+1)d_R^2)$ field operations, within $O(nD)$ for the fixed-degree scored branch because $kd_R\le n$, $\ell+1\le N+4\le D$, and $d_R$ is guarded by C5. This term belongs to $C_R$. It samples encryption coins as specified, produces the ciphertext for $m_b$, and simulates all generic labels and names and random oracles by the protected lazy tables. It runs $\mathcal A$ once. The extraction steps use the answered generic transcript without its output or the random-oracle query transcript, while the lazy tables implement exactly the direct oracle law. Because the programmed entries are jointly independent uniform ring elements for uniform $A$, all oracle answers including entries at the selected seed have exactly the joint law of the experiment. Private evaluation points are sampled independently of the run.

The reduction keeps records evaluated at its private test point, using the protected rules for guessed operands and for existing records. It tries the first GT result whose label has an existing record of different private value, using the difference expression, and also the target label's record if present. For each tried expression it computes three independent gradient vectors in the plain sector at private recovery points, tests their span for a kernel vector, and applies Euclidean LIFT with radius $B_{\rm E}$ if there is such a vector, making the selection specified in Amendment msis_bound. An output from LIFT is a short multiple of that kernel vector. The coefficient of $T^0$ in $z(v)$ is $v_0$. All $kd_R$ remaining row coefficients give the equations of $A$ on the packed input once $v_0=0$. Thus a nonzero kernel vector has $v_0=0$ and satisfies $A\hat v=0$. Its short multiple has $x_0=0$ and $\|x\|_2\le B_{\rm E}$ by that lifting algorithm. Reduction and packing commute, and packing preserves all ordinary and tag coordinates by Amendment ell and adds only zeros. This packs the output into a nonzero Euclidean-norm-at-most-$B_{\rm E}$ solution to $A\hat x=0$, exactly for the challenge whose rank, columns, bound, and norm are costed by M1. If no such output is found the reduction returns $\bot$. Denote its success probability by $s_b$. The cost is $t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT}$ with $Q_H$ the maximum per-oracle query count, $C_R=O((N_\star+n)D+\mu)$ for the fixed simulation setup and postprocessing, and $T_{\rm LIFT}$ the time of the lifting step. The reduction-time argument in C7 proves this reduction-time bound on the revised lists, including the original private record and gradient loop costs and the new fixed setup. The inverse conditions and comparison count do not enter those time calculations. The Euclidean lifting-time proof in Amendment msis_bound applies since $2B_{\rm E}<q$ and $B_{\rm E}^4<q^3$ by (I6). In particular the cost is $t+O(Q+d_R Q_H+\mu)+\operatorname{poly}(D,\log q)$ using $n,N_\star\le D$.

Here is how the first-mark bounds apply to these algorithms. The degree and view for the new field encoding and the needed gradient formula are derived above. The record invariant uses no inverse premise: setting all guesses to zero commutes with additions and pairings, and before the first mark every reused label comes from formally equal expressions. Formally equal target expressions have identical stacks by the fiber equations applied to their difference for every field search vector. Thus their records also have equal sketches. A good mark's stack is usable with the three field ties of Amendment C7 by the revised view. Its rank is at most three by $g^{-4}<\mu_{\rm tr}<\theta$ from (I5) and the protected stack rank bound. The full classification applies to every actual tied stack of dimension at most three, including zero-corner marks, because the three ties just derived are the original field identities. A kernel vector in its row space has coordinate 0 equal to zero, and its one-dimensional guessing probability is at least the stack's, by the protected guessing-probability lemma. The selection in Amendment msis_bound gives a short multiple at Euclidean radius $B_{\rm E}$. The amended LIFT therefore succeeds on that selected kernel vector.

At a first good difference mark its difference is formally nonzero, so the cleared polynomial is nonzero in the coins at some fixed search vector. This makes it a nonzero joint polynomial in coins and search coordinates. The private test uses independent uniform search coordinates and valid coins; the product-set bound gives failure probability at most $d_f/(q-D)$. Earlier formal equalities are equalities at every private point by the record invariant, so outside this failure the reduction picks exactly this difference. The degree bound and the uniform valid coin ranges give probability at most $\varepsilon_f$ for this failure. For a first good key mark the target record already has its expression by the record invariant and persists. Name negatives are target-group results and receive the same private and sketch tests. For a recognized good mark, the coefficient-vanishing and derivative calculation of the algebraic view subsection place each sector gradient in that sector row space. There is no nonzero alpha stack. For any proper subspace of the mark row space choose a linear form zero on the subspace and nonzero on the row space. Its value on one gradient, divided by $\pi$, is a polynomial of degree at most $n+2+2K_2$, using the seed-mode bound in the C7 degree ledger. This polynomial is nonzero by isolating the constant term in $\varepsilon$ and the distinct monomials $s_X\upsilon^{k_c}y_i$. The valid values for the independent coin coordinates have sizes at least $q-D$, by the independent coin support argument. The polynomial root bound, with $q-D$ in place of $q$ in its proof, bounds the chance of failing to increase the span while it is proper. Three independent points and rank at most three give failure at most $3(n+2+2K_2)/(q-D)\le\varepsilon_f$, by $2n\le D$ and $2K_2\le n$ and the formula for $\varepsilon_f$. Thus on a good first mark with a kernel vector, except for the two exceptional events just bounded, the reduction finds a kernel vector in the appropriate span, and produces the MSIS output. The unconditional probability of such a mark is at most $s_b+2\varepsilon_f$.

For a good first mark with no kernel vector, the classification proved in Amendment C7 gives an extended witness in its row space. Its ordinary projection satisfies the external system. In that sector the linear map from a tuple of probes to $\sum_c W_cv_c$ has image the row space, as each matrix is symmetric and the sum of its images is the row space of the stack. Uniform independent probe tuples give three independent uniform vectors in this space, even conditional on the run. In dimension $a\le3$, the chance of failing to span is bounded by $\sum_{j=0}^{a-1}q^{j-3}<2/q$: equivalently the $a$ rows of the random $a$-by-3 coordinate matrix are independent uniform three-dimensional vectors and the next row falls in the span of $j$ independent previous rows with probability $q^{j-3}$. At a difference mark the extractor tests the record difference. If the old entry is a pure guess, a guess-free difference requires the result to contain that same guessed variable with coefficient one. The label has therefore been used in an answered call, possibly the current call, and has a zero record by the test. At a key mark it tests the record of the result that obtained the target label. An initially received record has zero stack and thus is no good mark. These facts from the record invariant show that if the sampled vectors span, the witness is among the assignments tested. So the probability of a good first mark with no kernel vector and with extractor failure is at most $2/q$.

Let $u=2Q+2$. Every target query run has a first mark. The protected initial and guessed-mark estimates and the charged-mark estimate of Amendment Ncmp bound their three probabilities by
\[
\left(\binom{L_1}{2}+\binom{L_2}{2}+\binom{L_T}{2}\right)\varepsilon_f,\quad
N_{\rm cmp}(u)(\theta+\varepsilon_f)
+\left(\binom{L+3u}{2}+L+3u\right)\varepsilon_f,\quad
2^\lambda/N_{\rm free},
\]
respectively. These estimates concern the same sampler, oracle and record laws and use only the already checked view and degree properties, budget, and label counts. Together with the two good-mark cases they cover the event of a target key query and no witness. Their sum is at most $s_b+E(u)$: the good-mark excess is $2\varepsilon_f+2/q\le (8u+8)\varepsilon_f$, using $\varepsilon_f\ge1/q$; the remaining terms of $E$ are nonnegative and its guess term contains $2^\lambda/N_{\rm free}$. By (P5) and the generic-ledger implication of Amendment Ncmp $E(2Q+2)\le(Q+1)/2^\lambda$. Hence for each $b$ the target-query and no-witness probability is at most $(Q+1)/2^\lambda+s_b$, with exactly the stated oracle budgets and one MSIS instance. This proves Theorem 5.9 with its extraction time and soundness as above.
