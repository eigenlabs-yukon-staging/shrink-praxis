# Praxis with a Euclidean coefficient-norm SIS reduction

Throughout the proof $N$ is the protected external variable count and $N_\star=N+3$ is the number of internally sampled box coordinates. The three internal Boolean coordinates do not change which external witness relation is encrypted. The construction, coefficient placement and probabilities for the amended model follow.

## Amendment C5

Write $d=d_R$, $h_R=\mathrm{ring\_log}$, $p=\mathrm{pack\_digits}$, $p_f=\mathrm{form\_pad}$, $S_0=\lceil(D-1)/\nu\rceil$, and $m=k(\ell+1)d$. Put $J_Q=\lceil(D-1)/\Delta\rceil$, $J_R=\lceil\nu n_{\mathsf c}/\Delta\rceil$, and $J=J_Q+J_R$.

Require $\mathrm{ring\_mode}=d_R=1$, $h_R=0$, $\lambda=100$, $N=391693$, $\nu=2048$, $n_{\mathsf c}=1692$, $p=p_f=1$, $n=2$, $\mathrm{seed\_degree}=1$, $K_1=1$, $K_2=1$, $20\le J\le250$, and $36000000\le m\le40000000$. Write $z_c=\mathrm{zero\_columns}$ and require $z_c\in\mathbb Z_{\ge0}$. The scalar arithmetic guard is $V\le3m$ for
\[
\begin{split}
 V={}&2D+N+n_{\mathsf c}+32+6(N+4)
       +(\Delta-\Delta/\nu+2S_0+16)+(J+1)\\
    &+70(n+J+1)+10000+189336+100.
\end{split}
\]
Here the initial definitions of $m$, $S_0$ and $J$ are as above; the guard uses the protected $m$. The degree-one ring is $\mathbb Z$ with coefficient basis $(1)$ and scalar reduction $\mathbb F_q$. The oracle uses one independent uniform field sample per entry and caches it for repeated queries. Its full layout includes the ordinary and tag columns, the homogeneous column and the independent unused columns of ell. The challenge reduction programs the used nonconstant columns from its scalar challenge and samples the other columns independently. The active transmitted factors have no matrix multiplication or form-field evaluation, so the only encryption scalar ledger is the explicit one proved in C7 and n1. The oracle and matrix described here are present as auxiliary data of the same experiment even when the sender can leave their entries unsampled until requested. The charged allowance includes the full declared matrix coefficient count.

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
The density lower bound $m(\Theta)\ge\mu_{\rm tr}$ gives $h\le\xi_{\rm tr}/(g^3\mu_{\rm tr}-\xi_{\rm tr}/g)=H_3$ with the protected definition.

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

Require $g^2\le2^{100}\cdot2^\lambda$ and the conjunction
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
The displayed conditions keep the rank-one, rank-two and rank-three growth bounds. The additional upper range constraint gives $\sqrt g\le 2^{25}2^{\lambda/4}$, so the expected $O(\sqrt g\,N_\star^{1/4})$ group work is $O(2^{\lambda/4}N_\star^{1/4})$ for the common efficiency derivation.

The admissibility condition (P3) uses these inequalities together. The prefix and trimming proofs in I3 continue to apply: the upper range condition removes parameter choices and is not used in their estimates. The sparse projection count depends on the basis, covariance and fiber density. The regularization proof in I3 uses the displayed lower bounds on $\Gamma_1,\Gamma_2,\Gamma_3,A_{\rm inv},P_1,P_2$, with the rank-three height bound proved in I3 for the protected H3. The inverse theorem in I6 applies these facts to the modular fibers and gives the stated short-multiple conclusion. For the rank-two height it uses the unchanged definition $H_2=\Gamma_2/(g^2\mu_{\rm tr})$: regularity gives $m(\Theta)h(\Theta)\le\Gamma_2/g^2$, and $m(\Theta)\ge\mu_{\rm tr}$ gives the claimed height upper bound. The inverse theorem at the original infinity radius uses these heights. Amendment msis_bound uses the rank-one passing condition to extract a witness without a Euclidean output.

## Amendment I6

Replace (I6) by the conjunction
\[
 2\beta<q,\quad H_1\le\beta,\quad
 4H_2q\le3\beta^2,\quad 2509\lfloor H_3\rfloor q^2\le1000\beta^3.
\]
The inverse proof uses amended (I3) and (I4) with the protected H3. The height definitions H1 and H2 and conditions (I1), (I2) and (I5) retain their meanings.

### Dependence on the inverse conditions

In `blob:admissibility`, (P3) now requires the inverse-theorem conditions with the displayed (I6). The other admissibility conditions are identical, including (P4). The boxes, fibers, densities, saturation, height, and regularity in `blob:lattices` depend on the box, the basis, the field and the $\Gamma_d$, with no dependence on $\beta$. The ellipsoid of `blob:trimming` uses only $g,R_{\mathrm{tr}}$ and the basis. The following lemmas retain their contracts and arguments.

- In `lem:prefix`, the prefix saturation, indices, and fiber count use the integral basis and $g$. The estimate for a step of index below $g$ uses (I1), and the rank-three height and regularity use (I2) and (I4). They involve no short-vector bound.
- In `lem:trim`, the moment-generating-function bound for the independent uniform entries is applied to a linear image of the box and then Markov's inequality is applied with the threshold $R_{\mathrm{tr}}^2$. The loss condition used is precisely the exponential inequality in (I2).
- In `lem:sparse`, a trimming ellipsoid is projected along the normal constraints and lattice points in the projection are bounded by its volume and the lattice index. The conversion of the volume estimate to the constants uses (I3). The new (I6) is absent from both estimates and their proofs. The sharper geometric constant from the separate (I3) amendment is proved in that section.
- In `lem:regularize`, the downward induction uses the trimming loss, the prefix lattice inequalities, and the projected density–height bound. Promotion can only reach rank three by the inequality $g^{-4}<\mu_{\mathrm{tr}}$ from (I5). The growth bounds in (I4) suffice for the final prefix. Neither a bound on a short multiple nor (I6) enters the induction.

The prefix estimates, trimming, sparse projection, and regularization used below are proved in I3, and the rank-three height bound for protected H3 is proved in I3. A saturated lattice of rank one or two with density at least the threshold has the respective unchanged height bound from regularity, as explained in I4.

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
In rank three, $h(\Theta)\le\lfloor H_3\rfloor$ by I3 and integrality. Hence
\[
 \operatorname{vol}_3(\beta K_B)\ge (8/(2509/1000))\,\beta^3
 \ge (8/(2509/1000))\,(2509/1000)\lfloor H_3\rfloor q^2
 \ge 8\det L .
\]
The volume implication gives a nonzero $u=B_J z$ in $L\cap\beta K_B$ in each rank. Put $x'=Bz$. It is nonzero because its coordinates in $J$ are $u$, and its norm is at most $\beta$ by the definition of $K_B$. Modulo $q$, $x'$ is a multiple of $v_{[N_0]}$ since $z\in Z$. If that multiple were zero, each integer entry of $x'$ would be divisible by $q$. As $\|x'\|_\infty\le\beta<q/2$ this would force $x'=0$. Extend $x'$ by zeros in the deleted positions, including coordinate 0, to obtain the required short multiple.

### Rank-one admissibility

The four inequalities retain the stated infinity-radius conclusion at the original $\beta$. The last two conjuncts in (I6) are $g^2\mu_{\rm tr}>1$ and $\beta_{\rm sis}=8$. In the box used by the inverse theory and in the full search distribution used by the generic game, every rank-$d$ fiber has mass at most $g^{-d}$ by the respective cases of Bsearch. Thus a heavy stack has rank at most one. The fixed $g$ is also in the large-width domain of the search estimate. Indeed, $N_{\rm cmp}(2^{101})-N_{\rm cmp}(2)>2^{199}$, and the other nonconstant terms of $E$ are nondecreasing. By P5, $\theta<2^{-199}$. Since $\mu_{\rm tr}<\theta$ and $g^2\mu_{\rm tr}>1$, it follows that $g>2^{199/2}$. This condition requires no Euclidean inverse theorem. The amended reduction applies only the passing rank-one classification in msis_bound, so its formal SIS radius need not bound short multiples of unusable stacks. The original infinity conclusions and ordinary packing at $\beta$ are independent of this new radius.

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

Set $p=1$ and $\ell=N+z_c+3$ with the nonnegative integer $z_c$ of C5. Place each ordinary coordinate in its own scalar column. The next $z_c$ input coordinates are zero for every input, and all of their corresponding matrix entries are independent uniform field elements just like the other columns. Put the three tag coordinates in three distinct following columns. Column zero takes the independent homogeneous entry. The public ciphertext coefficient vectors retain the ordinary columns, the homogeneous column and the three tag columns only. The omitted input positions are identically zero as functions of all ordinary and tag coordinates, so any linear form on the input and any product of such forms sees exactly the same restriction of the full matrix product.

The placement is injective, preserves coefficient Euclidean norm, and commutes with reduction and field scaling. The slot-zero form is $v_0$, and the following forms contain the matrix coefficient list and prescribed zeros. A form-kernel vector has $v_0=0$ and $A\hat v=0$. Thus any hypothetical short multiple packs to a nonzero solution of the same norm for the full uniform matrix with dimensions $kd_R,\ell d_R$. For any fixed tag variant of an external witness, condition on all columns except column zero. Since its homogeneous coordinate is one, the independent uniform column zero adds a uniform coefficient vector to the remaining fixed vector. Consequently each form value is uniform on the affine space where the constant is one and every padding slot is zero. This describes the auxiliary form distribution only. The actual fallback bound uses the independent scalar coordinates of $y$ in Targets.

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

Require $n=2$, $\mathrm{seed\_mode}=1$, $\mathrm{seed\_degree}=1$, $4\mid q-1$, $2n\le D$, and $\Delta\ge n+3$. Fix $c$ by trying $5$ and then all other nonzero scalars in residue order, accepting when $c^{(q-1)/p}\ne1$ for every prime $p\mid n$. Cyclicity gives a nonempty choice set with full primary order at all those primes. This is fixed public precomputation before Setup. Put $P_T(T)=T^n-c$. If $t$ is any root and $o$ the order of $c$, then $\operatorname{ord}(t)/\gcd(\operatorname{ord}(t),n)=o$. At each prime divisor of $n=2$, the powering tests give $v_p(o)=v_p(q-1)>0$, hence the order equation gives $\operatorname{ord}(t)=no$. For each prime $p\mid n$,
\[
 v_p(q^j-1)=v_p(q-1)+v_p(j)
\]
for positive integers $j$. For an exponent prime to $p$, factor $x^j-1$ into $(x-1)(1+x+\cdots+x^{j-1})$; the latter factor is prime to $p$ for $x=1\bmod p$. For multiplication of the exponent by $p$, expand $(1+u)^p-1$: the linear term $pu$ has strictly lower valuation than every other term, using $v_2(u)\ge2$ at two. This proves the formula by factoring $j$. Since $o\mid q-1$, all other prime factors of $o$ are already present for every $j$. It follows that $no\mid q^j-1$ exactly when $n\mid j$. Thus the $q$-Frobenius orbit of $t$ has length $n$ and $P_T$ is irreducible. At $j=n/2$ the order of $t^{q^j-1}$ is exactly two by the same valuations, so the half-turn sends $t$ to $-t$.

For an integer Frobenius exponent $j$, let $b=q^j\bmod n(q-1)$. The reduced image of $T^a$ is $c^{\lfloor ab/n\rfloor}T^{ab\bmod n}$, since $T^{n(q-1)}=1$. The checked divisibility gives $q^i\equiv1\pmod n$ for every integer $i$. Both conjugations preserve monomial degrees. The monomial scalars are public. Each non-half-turn map uses a permutation and one product per coefficient, while the half-turn uses signs. Evaluating the two monomial tables at $υ$ from its powers uses at most $2n$ products.

## Amendment C7

Require $\mathrm{base\_degree}=\mathrm{base\_left}=\mathrm{base\_right}=\mathrm{scalar\_rel}=1$, $K_1,K_2\ge1$, $2K_1K_2=n$, $\mathrm{mask\_stride}=1$ and $C_{\rm mask}=0$. Under C5 the selector is $n=2$, $K_1=K_2=1$. There is one actual cell with coefficient weight equal to one. The two-dimensional form of C6 and n still specifies the uniform auxiliary problem and the infinity-kernel statement. Evaluation of that form, and extension-field conjugations, do not occur in the ciphertext or decryption. For the actual single-cell object, a stack is one matrix, and the family of intercell equalities is empty. A passing symmetric stack is usable. The classification statement for actual admissible good marks is that a nonzero, passing, symmetric stack of rank at most one is supported on a witness. The proof in msis_bound establishes it directly, and I6 and Bsearch give precisely its rank hypothesis at every good mark. The abstract three-tie classification for the larger grid is a conditional algebra statement, and the present single-cell algorithms and security proof never invoke it.

### Source-group exponents

Sample nonzero independent $\pi,s,\Omega_{22},\zeta_0,\zeta_1$ in the scalar field. Sample $\Omega_{12}$ and each coordinate $y_i$ independently uniformly in the field, and use the protected valid evaluation coin $\tau$ and the centered search vector $r$ of Bsearch. Sample $\alpha$ by its protected independent law. All remaining original coin positions may be sampled and discarded, as the exponents below ignore them. Write $\gamma=\pi s$ and $\kappa=\gamma L_\rho(\tau)$. In particular $\kappa\ne0$ on valid coins, since $L_\rho=Z/Z(\rho)$ and $\tau$ avoids the QAP points. For every input coordinate, including the homogeneous one and all three tags, publish the two group arrays on each side with exponents
\[
 F_1^i=\pi y_i,\qquad F_2^i=\pi(\Omega_{12}y_i+\Omega_{22}A_i(\tau)),
\]
\[
 H_2^i=s(B_i(\tau)-y_i)/\Omega_{22},\qquad
 H_1^i=s(r_i+A_i(\tau))-\Omega_{12}H_2^i .
\]
These are the left factor multiplied by the hidden-basis matrix and the right factor multiplied by its inverse. Publish one G2 search base $[s]_2$. The additional G1 and G2 polynomial lists are exactly those in n1. There is no source-group array for a second cell, a weight or a cancellation. In GT retain the single published $[\alpha\kappa]_T$. The seed and masked message are as in the protected syntax.

A witness sum at any of the prescribed tag extensions gives
\[
 F_1(v)H_1(v)+F_2(v)H_2(v)=\gamma(y(v)r(v)+A_v(\tau)B_v(\tau)).
\]
The terms $\Omega_{12}$ cancel. Expanding the remaining terms gives $y(v)A_v-A_v y(v)=0$, which proves the identity. The search base and the first left sum give $\Psi_v=[\gamma y(v)]_T$. The correction polynomials cancel $A_vB_v$ except for $d_vL_\rho$, giving $\Lambda_v=[d_v\kappa+r(v)\gamma y(v)]_T$ as proved in n1. Thus the correctness and extraction shown in Targets hold for every admitted point placement.

### Scored encryption arithmetic

For a fixed input entry, compute $F_1^i$ with one product, and compute $F_2^i$ with two more using the precomputed $\pi\Omega_{22}$ and the first coordinate times $\Omega_{12}$. Use the precomputed $s/\Omega_{22}$ for one product giving $H_2^i$. Two more products give $s(r_i+A_i)-\Omega_{12}H_2^i$. This is at most six products for each of $N+4$ coordinates. 

Partition the QAP roots into the $N+5$ Booleanity and key singleton factors and $n_{\mathsf c}$ constraint cosets. Their vanishing factors at $\tau$ are respectively $\tau-p$ and $\tau^\nu-a^\nu$ for a coset represented by $a$. Compute $\tau^{2^j}$ for $1\le j\le11$ by successive squaring. On the list of $b=N+5+n_{\mathsf c}$ factor values, ordered with singletons first, use prefix and suffix products to get their product and their outer complements. Prefix values through the singleton group and the whole list give $Z_0(\tau)$ and $Z_*(\tau)$. A first value and an end complement can be copied without multiplying by one. The full prefix uses $b-1$ products, the suffix excluding its unused first product uses $b-2$, and the $b-2$ interior complement products supply the rest. At a coset node of size $2^j$, split it into its two child cosets of size $2^{j-1}$. Each child's vanishing evaluation is the precomputed power $\tau^{2^{j-1}}$ minus the corresponding public power of a representative. The two child complements are the outer complement at the parent times the sibling vanishing evaluation. With two multiplications per internal node of a $\nu$-leaf tree, this provides all $Z_*(\tau)/(\tau-p)$ using $2(\nu-1)n_{\mathsf c}$ products after the outer pass. At $\rho$ the complement is $Z(\tau)$. The sum of all products is at most $3b-5+11+2(\nu-1)n_{\mathsf c}=2D+N+n_{\mathsf c}+11$, which fits the $2D+N+n_{\mathsf c}+16$ term. The public QAP coefficients at $p$ are encoded with the fixed multiplier $1/Z_*'(p)$. Multiplying an encoded point coefficient by its cofactor now makes the exact Lagrange contribution with one multiplication. The nine new Booleanity coefficients and the five entries at $\rho$ are covered by the sixteen further products in the $2D+N+n_{\mathsf c}+32$ guard. All these scalars are over $\mathbb F_q$.

The sparse and non-sparse power recurrences are valid also at $\tau=0$. Compute $\tau^\nu$ by at most eleven squarings, advance at most $S_0-1$ sparse entries using that value, and form a shifted partner for each using one product. The non-sparse entries start with $\zeta_1\tau$ and advance by $\tau$ or $\tau^2$ depending on whether a multiple of $\nu$ was skipped. Their total together is at most $\Delta-\Delta/\nu+2S_0+16$. The one sparse right exponent and $J$ chunk exponents are formed with one product each from the shared $\gamma$ and the coefficient tables.

Compute the common scale factors and the two starting right coefficients using at most twenty products, including the evaluations of $L_\rho$ from its fixed cofactor and the two key exponents. Compute step $h=(\tau^\nu)^{\Delta/\nu}$ with at most 508 products by binary powering since the exponent is at most $D<2^{254}$. Obtain the remaining chunk coefficients in each of the two progressions by multiplying by $h$. Their total with the other table products is at most $528+J$, which is less than $70(n+J+1)$ for $n=2$ and $J\ge20$. At most ten scalar inversions at the protected prime and other fixed scale products fit 10,000 products. The five fixed tag polynomials in n1 are evaluated by their displayed quotient formulas. At the four tag and key points let $u_p=(\tau-p)^{-1}/Z_*^{\prime}(p)$, so $L_p(\tau)=Z_*(\tau)u_p$. Use four of the already-budgeted inversions for the $(\tau-p)$ factors. Multiplication by the derivative factors gives the four $u_p$. The ratio $A_i(\tau)/Z_*(\tau)$ is $u_i+c_*u_\rho$ for $i=1,2$ and $u_3$ otherwise. Evaluate each displayed $F_i$ and $F_{i,i^{\prime}}$ by these ratios and the ordinary $L_p$ values, replacing $L_\rho/Z_*$ by $u_\rho$. This uses at most four derivative products, four products for the $L_p$ values, four products for the two $c_*$ factors in the ratios and unscaled values, and three products per fixed polynomial. Its two published exponents add $\zeta_0$ scaling and the shift in two products per polynomial. The resulting 37 products fit the designated 100. Both GT exponentiations use a common generator: cache its multiples two through seven using six products, then scan 85 three-bit blocks per canonical field scalar using three squares and at most one multiplication per block. The 686 target products cost at most $686\cdot276=189336$ base-field products by search_spread. Hence the full scalar allowance is the sum in C5. Its comparison to $3m$ proves the encryption cost, and every published source element uses exactly one fixed-base multiplication.

### Degree and view of the single cell

Fix the seeded matrix, which now merely provides auxiliary oracle data. A guess-free target expression is $\mathsf E=\sum_{a,b}D_{ab}ab+D_K\alpha\kappa$ over the source-group exponents including their generators. The product $\varpi=\Omega_{22}\zeta_0\zeta_1$ clears all denominators. Left input degrees are at most $D+1$, because QAP factors have degree below $D$ and the two coefficients in the second factor add at most two. Sparse exponents and the ten tag bases have degree at most $D$, including their scalar. The cleared right exponents have degree at most $2D+2$: the chunk polynomial part has degree at most $2D-2$ by P1, $\gamma$ adds two, and clearing its reciprocal scale leaves only two factors of $\varpi$. The sparse right part has degree at most $D+4$, the cleared factor coordinates at most $D+4$, and the cleared search base at most four. The cleared terms with $\kappa$ or $\alpha\kappa$ have degree at most $D+5$. The combined paired degree, even with one extra degree for a guessed operand, is at most $3D+4$. All these bounds fit the protected $d_f=3D+2n+2K_1+7$. For each fixed $r$ every scalar coin domain has at least $q-D$ points and the domains are independent. The clearing factor is nonzero. Successive application of the single-variable root bound gives probability at most $d_f/(q-D)\le\varepsilon_f$ for a nonzero cleared polynomial to vanish: condition on the other variables, use the bound for a nonzero leading coefficient by induction, and then count the roots in the remaining variable. Hence an identity on all valid coins may be treated coefficientwise and vice versa. In an identity to $\chi\kappa$, $\chi\in\{0,1\}$, the coefficient of $\alpha$ kills $D_K$ because $\kappa$ is nonzero and no other term contains $\alpha$.

We identify the terms with an $H_1$ operand first. In the Laurent identity take the part with $\Omega_{22}^{-1}$ and positive $\Omega_{12}$ degree. At $\Omega_{22}=0$ the reduction of $F_2^i$ is $\Omega_{12} F_1^i$. The inverse hidden-basis terms come from the second summand of $H_1$ and from $H_2$ paired with $F_2$. After removing their common factor $-\Omega_{12}/\Omega_{22}$, they give a polynomial identity
\[
 \sum_{a,j}\delta_{a,j}\widetilde a\,s(B_j-y_j)=0.
\]
Here $\widetilde a$ is the left exponent at $\Omega_{22}=0$. For $a=F_1^i$, $\delta_{a,j}$ is the coefficient of $F_1^i H_1^j$ minus that of $F_2^i H_2^j$. For other left inputs it is the coefficient of $aH_1^j$. Replace $y_i$ by $B_i(\tau)+z_i$ with independent $z_i$. The coefficient of $z_j$ gives $\sum_a\delta_{a,j}\widetilde a(B)=0$. Separate the monomials of the scalar variables. Left-generator, $\zeta_0$ polynomial and $\zeta_1$ power terms are separate categories. The generators and distinct $\zeta_1$ powers must have zero coefficients, and any $\zeta_0$ aggregate at this $j$ is the zero polynomial in $\tau$. The latter is independent of $y$ and hidden variables, so its whole $H_1$ contribution vanishes at every $r$. The other two categories are $\pi B_i$ and $\Omega_{12}\pi B_i$. The $B_i$ are independent by their values on the Booleanity points of D, so each of these coefficients is zero. Consequently, only the individually matched pairs contribute any dependence on $r$.

The Laurent coefficient with one $\pi$, one $s$, and zero degrees in the other scalar scales has exactly the matched products, the first-left/search pairs, and the two complementary correction-scale classes. This enumeration follows directly from the source lists in n1 and this section. Pairing with the source generator cannot add this monomial unless the other exponent already has it with no inverse scale, and the only published $\gamma$ exponents all have an inverse scale. The matched products have coefficient matrix $W$. The first-left/search pairs give a linear term $-y^\top u$. By the residue-preserving division in n1 the correction terms have form $Z_*h+Z_0R$, where $R$ has degree below $\nu n_{\mathsf c}$ and nonzero residues modulo $\nu$. Thus an identity to $\chi\kappa$ requires
\[
 y^\top(Wr-u)+y^\top(W-W^\top)A(\tau)+P_W(\tau)+Z_*(\tau)h(\tau)+Z_0(\tau)R(\tau)=\chi L_\rho(\tau).
\]
Compare linear terms in $y$ first at $d_0$, where $A=0$, to get $Wr=u$. The values $A(d_i)$ and $A(\rho)$ span by D, so the other comparisons force $W=W^\top$. The constant part has $\deg h\le D-2$ by degrees of $P_W,Z_0R$ and $L_\rho$. The QAP identities of D give all the passing tests and $W_{\mathsf b_1,\mathsf b_2}=\chi$ in the key corner. These implications use only the selected coefficient. If the identity holds at some $r$, its change when replacing $r$ by $r'$ is exactly $\gamma y^\top W(r'-r)$ by the matched-pair argument, since no other leaf contains $r$. Therefore its identity set is exactly the fiber $Wr'=u$ whenever it is nonempty. For $W=0$ any identity is formal at every $r$, and it forces $\chi=0$ by the corner. A formal identity at all $r$ also has $W=0$ by its fiber equations. The legal support spans affinely: the conditional independent $r_0$ can vary by one with all box coordinates fixed, forcing the zeroth coefficient in any fixed linear constraint to be zero. Then any independent box coordinate can vary by one, forcing each other coefficient to be zero. Source expressions paired against the other source generator have zero matched stack. A formally nonzero source difference is consequently a nonidentity at any fixed $r$, giving the source coincidence bound. This proves the revised view with the unweighted, single passing stack and no intercell ties.

### Transcript sketches and simulation cost

For each of three independent probe vectors $v$, a first G1 factor input $F_1^i$ records the corresponding coordinate vector $e_i$. Other G1 inputs record zero. A first G2 factor $H_1^j$ records the scalar $v_j$, and other G2 inputs record zero. Extend both records linearly, pair by scalar multiplication of the vector, and extend GT records linearly with zero on guesses, source and target generators and $[\alpha\kappa]_T$. On a matched expression these three sketches are $Wv$. The tuple assignment at initialization and induction through group operations give the sketches on every formal expression with guesses set to zero. Formally equal target expressions have zero difference sketch because every formal identity has zero $W$. For source records, the leaf assignments also respect equality: the coefficient of $\pi y_i$ with zero hidden-basis degree specifies the left record, and the coefficient of $s r_j$ specifies the right records, as neither coefficient comes from any other leaf. Thus a consistent first-label table suffices. At a collision the difference of the two calculated sketches is exactly the sketch of the old-and-new expression. At a target key query the extractor has already tested the eligible GT entry from its generic creation. The rank-one argument in Targets then gives the required failure bound. These sketches need only $O(N_\star)$ field operations per generic call and test, inside the protected extractor time allowance.

The auxiliary reduction generates the same oracle law as in msis_cols and has no recovery work. In the protected unit-operation model it runs the adversary once using a table of assigned exponents indexed both by exponent and by label, and a label-status table for excluded strings. For an unclassified operand it compares a uniform integer below the number of unclassified strings to the number of remaining exponents. A positive outcome assigns a uniform unused exponent, while a negative outcome excludes the string. The lookup, two count reads, sample, comparison, optional new exponent sample, and updates to the two tables and counts use at most 20 unit operations per operand. Two operands therefore use at most 40. For a result, at most two operand lookups, one field operation for the group exponent, a label lookup by exponent, optional unused label sample, two table writes, two count updates and status or output records fit another 24 operations. A name call uses the same modular negation and two label operations. The total is within 148 unit operations per generic call. Each seed query uses a lookup, at most $d_R=1$ scalar samples, and at most one insertion, giving $d_R+2$ operations. Each key query uses a lookup, at most one message-space sample, and at most one insertion, giving three operations. Replies are returned with their lookups or inserts in the table-call interface. Each oracle has at most $Q_H$ queries, for a total of $(d_R+5)Q_H$. Initial scalar evaluation and seed table programming take $C_R=O((N_\star+n)D+\mu)$, since $\ell+1\le40000000<11D$ by C5 and evaluating the public QAP data and all input exponent lists is within this bound. This gives time at most $t+148Q+(d_R+5)Q_H+C_R$, with the same generic interface, arbitrary label guesses, oracle domains and no lifting calls.

### Deterministic scored setup

The fixed fields and polynomial placement data are public. Only the scalar field and public subgroup data are used by the active encryption and decryption. Runtime Setup references them without performing field generation or copying the tables. It scans the nonzero system terms and prepares the subgroup point encodings and shifted tables in D and n1, in the stated $O(|S|+D\log D+\log q)$ work. The fixed tables are independent of the input system and encryption coins and add no ciphertext data.

### Parameter selection and Corollary 5.8

Define the amended parameter selector on the public security level, domain, and external system shape. On the protected BN254 domain with security level 100 and the external benchmark shape, use the admitted parameters, the subgroup setup of D on any admissible input, and the changed algorithms. On every other domain, security level or external shape, take the protected original selector and use its original setup, encryption and decryption at that input. This public dispatch precedes parameter calculation. Only the first branch uses the changed entries and algorithms. In the second branch the original bounds, norm, sampler, field and ring parameters, point and coefficient placement, group counts and search algorithm all come from the original selector. Thus neither the statement nor the proof of the protected cor:asymptotics on the second branch uses an amended entry. Apply that protected result to the second branch with its unchanged hypotheses and original $\lambda$.

The statement of Corollary 5.8 for this selector has the same four bounds and scope: for linear-size systems with $N\ge\lambda^2$ in the designated subgroup placement, size is $O(\lambda N)$ field elements, encryption costs $O(\lambda^2N/\log\lambda)$, and decryption costs $O(\lambda N\log\lambda)$ outside its search with expected $O(2^{\lambda/4}N^{1/4})$ operations in the search. On the first branch $(\lambda,N)=(100,391693)$ is a single point. The explicit ciphertext count and the finite work proofs bound the costs on this branch uniformly over all admissible parameters, systems of that shape, and placements used in the cost statement. All ciphertext arrays and transform lengths are uniformly bounded by the shape and guards. Every allowable system has at most $1692(2\cdot2047+1)(391693+1)$ field coefficients in its ordinary form description, so even counting zero coefficients gives a fixed uniform bound on linear form work. All scalar and group operations outside the search use the fixed number of arrays, transforms and coefficients proved here. The elementary coefficient algorithms and the protected group implementation are over fixed finite fields, with finite worst-case costs per listed operation. The ordinary search has a fixed cap $B_{\mathrm{search}}<q/2$ and the fallback has cap $q$. Each uses the bounded traversals in Amendment search_spread. Uniform bounds also follow directly from the expected search estimate using $g^2\le2^{100}2^{100}$. Divide the four uniform costs by the corresponding positive scales at $(100,391693)$ and take the maximum with the original branch's constants. This yields uniform constants for the four bounds throughout $N\ge\lambda^2$.

Targets proves correctness and extraction for every admissible prescribed placement.

## Amendment P1

Require $\Delta\le D$, $J=\lceil(D-1)/\Delta\rceil+\lceil\nu n_{\mathsf c}/\Delta\rceil$, $J'=1$, $\nu\mid\Delta$, and $n\le D$. These are $J_Q$ quotient chunks of length $\Delta$ spanning $[0,D-1)$, and $J_R$ remainder chunks spanning $[0,\nu n_{\mathsf c})$. The quotient right multiplier has degree $D$; the remainder right multiplier has degree $D-\nu n_{\mathsf c}$. A complete allowed interval therefore produces terms of degrees at most $2D-2$ and $D-1$, respectively, when truncated at the supported coefficient lengths. The formal comparison permits every padded position. The ceiling definition gives $(J_Q-1)\Delta<D-1$. This bound on the integer highest quotient shift is at most $D-2$, so its right source polynomial part has degree at most $2D-2$. Likewise the highest remainder shift satisfies $(J_R-1)\Delta<\nu n_{\mathsf c}$, so its right source polynomial part has degree below $D$. The bounds in C7 apply before imposing any honest coefficient restrictions. All shifts are multiples of $\nu$.

## Amendment n1

There are
\[
 n_1=2(N+4)+2\lceil(D-1)/\nu\rceil+\Delta-\Delta/\nu+10
\]
transmitted G1 elements. The first $2(N+4)$ are the two left arrays of C7, for the homogeneous, ordinary and tag coordinates. Let $S_0=\lceil(D-1)/\nu\rceil$ and put
\[
 I_0=\{0\le a<D-1:\nu\mid a\},\qquad
 I_0^*=I_0\cup\{a+1:a\in I_0\},\qquad
 I_1=\{0\le a<\Delta:\nu\nmid a\}.
\]
Send $P_a^0=[\zeta_0\tau^a]_1$ for $a\in I_0^*$ and $P_a^1=[\zeta_1\tau^a]_1$ for $a\in I_1$. The sparse indices are distinct and their cardinality is $2S_0$. The other list has $\Delta-\Delta/\nu$ entries by P1. The final ten elements are the fixed tag-quotient bases specified below.

On the right use the two right factor arrays and one search base from C7. The single sparse correction operand is $B^0=[\gamma Z_*(\tau)/\zeta_0]_2$. The other correction bases are
\[
 B_j^Q=[\gamma Z_*(\tau)\tau^{j\Delta}/\zeta_1]_2\quad(0\le j<J_Q),\qquad
 B_j^R=[\gamma Z_0(\tau)\tau^{j\Delta}/\zeta_1]_2\quad(0\le j<J_R).
\]
Apply the parity rule of n2. The only GT element on the ciphertext is $[\alpha\kappa]_T$, alongside the seed and masked message. Compute each transmitted group element with exactly one fixed-base generator multiplication using its stated scalar. The actual scalar work before the group multiplications is proved in C7.

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

At the single sparse operand add $\sum_i b_iD_i^0$ and the linear combination of the five transmitted unshifted fixed bases giving $[\zeta_0F_v(\tau)]_1$. The shifted bases are included in the exact ciphertext count and need not be used by the routine. The tag correction contributes exactly $\gamma Z_*(\sum_i b_iQ_i^0+F_v)$ through the sparse pairing and $\gamma Z_*\sum_i b_iQ_i^1$ through the ordinary quotient chunks. The fixed tag-direction identity above proves that this is $\gamma(P_v-P_{v_0}-d_v L_\rho)$.

### A single combination at any tag

Put $U_*=(D-1)+\nu n_{\mathsf c}$. For $v_0=(w,0,0,t)$ the key corner is zero. By D, $G_{\rm base}=P_{v_0}/Z_0$ is exactly $Z_{\mathcal K}h+R_w$. Use monic division in each residue modulo $\nu$ because the divisor is in $\mathbb F_q[X^\nu]$. Both quotient and remainder preserve residues. Write $h=h^0+h^1$ for its zero and nonzero-residue parts. The witness condition makes $R_w$ have only nonzero residues. Evaluate the sparse MSM for $h^0$ from the corresponding $P^0$ powers, add the tag terms just described, and pair against $B^0$. Compute separate MSMs into the $P^1$ powers for each quotient and remainder chunk. Add the selected first and second tag-direction operands to the quotient chunks, then pair the quotient and remainder lists against their respective right bases. This evaluates the correction
\[
 \gamma\bigl(Z_* (h+\sum_i b_iQ_i+F_v)+Z_0R_w\bigr)
 =\gamma(P_v-d_v L_\rho).
\]
The two ordinary factor pairings of the witness-summed coordinates give C7's value $\gamma(y(v)r(v)+P_v)$. Subtracting the correction gives $\Lambda_v=[d_v\kappa+r(v)\gamma y(v)]_T$. To compute $\Psi_v=[\gamma y(v)]_T$ use only the first-left witness sum and the published search base, with one pairing.

For the identity view, arbitrary sparse and non-sparse quotient pairings contribute $Z_*h'$ with no further restriction needed on $h'$ before comparing degrees. In the terms multiplied by $Z_0$, all available powers have nonzero residue modulo $\nu$ because $\Delta$ is a multiple of $\nu$. Divide that nonzero-residue polynomial by $Z_{\mathcal K}$, absorb the quotient into $h'$, and keep the remainder of degree below $\nu n_{\mathsf c}$ with nonzero residues. Thus all scale-matched correction terms are exactly of the allowed form used for the view, without requiring choices made by honest decryption. These statements hold for every admissible prescribed placement. For points outside the scored subgroup placement, compute the same polynomials by interpolation and use exact monic division. Products, interpolation and monic division can use block-split power-of-two transforms and doubling-precision division. They require the same published operands and identities.

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

The three QAP scalar costs sum to $388329020+77667419+201334784=667331223$. No field form, weight or mask product is needed. The fallback denominator inversion and group-scalar preparation fit the conservative fixed 1018 operations already allowed for the old direct-normalization and fallback branches. Thus the scalar work outside the separately charged search is at most
\[
 667331223+1018=667332241<632000000+m
\]
since $m\ge36000000$. Bit selections, public centers and arithmetic on exponents of the search use the same search accounting below. The fixed public spectra depend only on the prescribed domain and points, with storage $O(D)$. The additional field arithmetic has the bounds from the selected lists; the generic field and group setup and search are separate.

### Tag choice and key recovery

For any external witness $w$ and $t\in\{0,1\}$, set $a_t=(w,1,0,t)$, $b_t=(w,0,1,t)$, $c_t=(w,0,0,t)$, and $v^{(t)}=(w,1,1,t)$, all with homogeneous coordinate one. The three ordinary corners have zero key corner and $a_t+b_t-c_t=v^{(t)}$ as integer vectors. The target has key corner one.

If the primary target base $\Psi_{v^{(0)}}$ is zero, compute its one full combination, equal to the key $\kappa$ in GT. Otherwise, when the three primary ordinary bases are nonzero, choose the ordinary triple with $t=0$. If a primary ordinary base is zero, test the secondary target and ordinary bases. If the secondary target base is zero, again its full combination is the key. If it is nonzero and the three secondary ordinary bases are nonzero, choose the ordinary triple with $t=1$. Otherwise take the evaluation-point fallback. This uses at most eight base tests and four full combinations. All full combinations on a selected path share the same third tag, so they require one common baseline. Let $v_*$ denote the selected target in an ordinary branch. Branch selection is independent of the search coins.

For the selected triple, use $v_0'=c,v_1'=a,v_2'=b$ and let $c_0,c_1,c_2$ denote the rounded centers of the anchor and differences. Before starting line [full-search], form
\[
 Q_0=\Lambda_c-c_0\Psi_c,\qquad
 Q_1=\Lambda_a-(c_0+c_1)\Psi_a,\qquad
 Q_2=\Lambda_b-(c_0+c_2)\Psi_b .
\]
The line solves $Q_0=t_0\Psi_c$, then solves $Q_1-t_0\Psi_a=t_1\Psi_a$ and $Q_2-t_0\Psi_b=t_2\Psi_b$. The two multiplications by the already recovered $t_0$ use signed binary arithmetic on $|t_0|$, with sign handled by the fixed Frobenius inversion. These are the only group products that translate targets within the search. The output is the three centered logarithms in the record below. The later key computation forms $r(v_*)=c_0+c_1+c_2+t_0+t_1+t_2$, subtracts $r(v_*)\Psi_{v_*}$. This gives $[\kappa]_T$. One key-oracle query unmasks the message. At most eight $\Psi$ values and four full $\Lambda$ values are needed, and the triple choice is independent of the search vector.

### Exact fallback when no ordinary triple is available

This fallback is used when neither ordinary triple or the direct target branch applies. The sparse G1 list contains $P_0^0$ and $P_1^0$ because $0\in I_0$ and $1\in I_0^*$. Before entering the unified search line, pair each one with the published sparse right operand $B^0$. The results are
\[
 E_0=[\gamma Z_*(\tau)]_T,\qquad
 E_1=[\gamma Z_*(\tau)\tau/c_{\rm q}]_T ,
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

## Amendment n2

The total before parity adjustment is $2(N+4)+J+2$. There are $2(N+4)$ right factor entries, one search base, one sparse correction base and $J=J_Q+J_R$ ordinary right correction entries. If this count is odd, add one copy of the G2 generator by fixed-base multiplication by one. The exact even count is $2n_2$ for
\[
 n_2=\left\lceil\frac{2(N+4)+J+2}{2}\right\rceil.
\]
The tag direction does not add right elements. The optional generator duplicate uses the existing group element and exponent; additional published copies of it add no exponents to the formal view. This verifies the complete publication syntax together with n1 and C7.

## Amendment dec_sum_g1

Sum the ordinary witness coordinates in each of the two left arrays at a cost at most $(N+1)/2$ each, including its homogeneous coordinate. At most eight first-factor variants and four second-factor variants need up to three tag additions, for at most 24 per array. The sparse fixed adjustments and tag additions in the four combinations fit 76 further additions by the directly listed additions in n1. More explicitly, at most five fixed sparse terms and two sparse direction terms are added per variant, at most 28 in all, and the shifts and duplicate unused sparse adjustments remain within the same bound. The quotient tag direction adds at most two bits at each of $J_Q$ chunks, each bit in at most two variants, so there are at most $4J_Q$. Thus the count is $2((N+1)/2+24)+76+4\lceil(D-1)/\Delta\rceil$.

## Amendment dec_sum_g2

The two right arrays each use at most $(N+1)/2$ additions to aggregate the ordinary and homogeneous entries. Up to four full variants add at most three tags to each, so $2((N+1)/2+12)$ is sufficient. Both the polynomial correction bases and the search base are already available as individual group elements.

## Amendment dec_msm_g1

The baseline sparse MSM has at most $S_0$ points, within the allowance $2S_0+2$ that also covers the shifted sparse data if prepared. The ordinary quotient and remainder together use at most $D-1-S_0+(\nu-1)n_{\mathsf c}$ points from their nonzero-residue positions. Each of the two direction constructions uses at most $D-1$ sparse and non-sparse points together and may form its optional shifted term with another $S_0+1$ points. The combined bound is
\[
 D-1+S_0+2+(\nu-1)n_{\mathsf c}+2(D+S_0).
\]
There is no weighted left MSM on the factor arrays, since each factor is already one witness sum.

## Amendment dec_msm_g2

The count is zero. Each right operand in an ordinary, direct or fallback pairing is either one of the witness sums of the two right arrays or an individual published base. The former is computed by additions counted above. No right weighting or multi-scalar multiplication is performed.

## Amendment dec_pairings

At most eight $\Psi$ tests use one pairing each. At most four full combinations each use two factor pairings, one sparse correction and $J$ regular correction pairings. Thus the bound is $8+4(J+3)$. The fallback takes two more pairings in place of any full combinations, which stays within that bound. This is also below the conservative 1100-accumulation limit used with the search steps.

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

For an auxiliary scalar multiple, including a group subtraction when implemented by adding an inverse, reduce the scalar modulo $q$. The binary algorithm uses at most 508 group multiplications since $q<2^{254}$. Charge three public center translations before the line, two post-line products for removing the ordinary search term and final key recovery, six signed-stride setup multiples across the three traversals, and two in-line products by the signed anchor logarithm. This is at most thirteen scalar multiples, each requiring at most 508 group products. Besides these scalar multiples and the signed pairing accumulations, the three center translations take three target-field products, the two in-line translations take two, and the final subtraction takes one. Implement a sign on any of these six updates by the fixed $p^6$ Frobenius, using at most 144 products for its linear map, and allow another twelve such maps for the signed initial strides, three bases of the secondary traversals and final hit signs. At the start of each of the three secondary traversals at most two target products are needed to initialize its two sequences, in addition to sign and stride setup. All further secondary steps use the per-operation charge above. The primary traversals initialize the baby at the identity and the giant at the supplied target. In addition to the per-candidate tariff, allow at most fourteen initialization, terminal and verification products per primary traversal as in the signed schedules above. Integer indexing, table comparisons, sign and index recovery, and the final bit and range checks use no target-field products. These explicit extra allowances total at most $6+18+6+3\cdot14=72$ even pricing each fixed linear map as a full target product. The reserve of 400 covers them with room for the already specified fixed sign and initialization operations. On the fallback path only the fixed evaluation-point inversion in the search and the one normalization after it are needed. For each signed pairing sum, negate source operands by coordinate sign change where needed. Accumulate the corresponding Miller-loop products, then finalize the sum with the protected shared final exponentiation convention. The same polynomial product bound applies to these field products before exponentiation. The pairing bound is $8+4(J+3)\le1020$ on the ordinary path and $8+2=10$ on fallback, as shown in Amendment dec_pairings. There is at most one accumulator product and basis conversion per pairing, so the allowance of 1100 of each covers them. The zero-target-base path needs only normalization. In particular, an inverse for the initial stride in the protected signed search can use the protected sign-class operation. Alternatively, make both initial signed strides by two extra binary scalar multiples. We budget two for each of the three primary searches.

The fallback's expected auxiliary cost is at most $(135/q^2)(16\sqrt q+600)\cdot276$ base-field multiplications in addition to the two pairings already charged, hence less than $10\cdot276$ for the protected prime. The total above is less than $(13\cdot508+1100+400+10)\cdot276+(1100+8)\cdot144<2400000$ expected base-field multiplications. It therefore fits in 400000 units of six base-field multiplications. The rare choice of a later ordinary triple adds less than one primary candidate in expectation, so its scheduled cost is at most $10001/10000$ of one unit. Allow two further units for it. The total expected multiplication bound is $6((10001/10000)((4882533/2950000)\sqrt{\sigma^+}+(47/18+1/5000000)\sqrt{g/2})+404500)$, covered by the amended spread, since $400002+(10001/10000)4352<404500$. The ordinary searches retain their bounded-answer correctness, and the fallback introduces no new published operands.


## Amendment n

Use $n=kd_R+\mathrm{form\_pad}$. At $n=2,d_R=1$ the padding guard gives $k=1$ and $\mathrm{form\_pad}=1$. Place $v_0$ in slot zero and the matrix coefficients in slots $1$ through $1$ in row and coefficient order. This order defines the auxiliary form and packing used by the unchanged infinity theorem. The active factors of C7 ignore the form values. The kernel is exactly $v_0=0$ and $A\hat v=0$. For any fixed witness variant, the uniform independent column zero makes the coefficient matrix slots uniform, with homogeneous slot one. The costed coefficient instance and its Euclidean packing are preserved.

## Amendment msis_cols

Set $\mathrm{msis\_cols}=N+3$. This is the dimension of the uniform auxiliary challenge: the $N$ ordinary columns and the three tag columns. Since $d_R=1$, each is one scalar coefficient per row. The $z_c$ additional full-matrix columns have zero witness inputs in every form. The reduction programs the challenge columns in the used positions and samples the independent unused columns and column zero from the same uniform field law. This gives exactly the full matrix distribution across all entries, including seed-oracle queries at padded column indices, with repeated queries cached. The reduced dimension does not constrain what the adversary queries. Its reduction never returns a candidate based on the unused columns or any other columns. For a hypothetical short vector on the ordinary and tag indices, inserting the zeros is the same isometric map already proved in ell. The full-matrix shortness conclusion at the original infinity radius stays on the full matrix. The new count describes only the explicit uniform challenge of Targets.

## Amendment msis_bound

Set $\mathrm{msis\_bound}=\beta_{\rm sis}=8$. No passing heavy stack has a nonzero kernel vector. To prove this, use Bsearch and $g^2\mu_{\rm tr}>1$ to give rank at most one. A good mark is nonzero by the zero-stack clause of the view. Each matrix of a rank-one symmetric stack is $a_c w w^\top$ for some common nonzero spanning vector $w$ and field scalars $a_c$, at least one nonzero. Indeed its rows are multiples of $w^\top$, and symmetry tested against an index where $w$ is nonzero makes its column factor proportional to $w$. In a cell with $a_c\ne0$, the Booleanity tests give $w_i(w_i-w_0)=0$ for every nonconstant coordinate $i$. If $w_0=0$, then all these $w_i$ vanish and $w=0$, a contradiction. Hence $w_0\ne0$. The homogeneous form output is $w_0$, so no nonzero vector on this line is in the kernel. Dividing by $w_0$ gives a Boolean assignment, and all external tests are zero on its square because they are linear in the tested nonzero cell and the cell is a nonzero scalar times that square. Thus every usable heavy case has an ordinary witness in its row space. No assumption about ties, weights or the SIS norm is needed for this implication. The original heavy-stack infinity theorem remains true by the rank bound and the proved infinity inverse in I6: every nonzero kernel vector in any heavy stack has its ordinary infinity-short multiple because a joint fiber is contained in its individual fiber. The new Euclidean radius applies only to the challenge in Targets. The reduction returns failure after its one programmed run and has success probability zero.

## Amendment msis_norm

Use $\mathrm{msis\_norm}=2$ on the $N+3$ scalar coordinates of the uniform auxiliary challenge. The distribution and simulation are described in msis_cols. No Euclidean vector is requested because all usable heavy cases yield a witness; the reduction never returns a candidate. Integer coordinate placement commutes with reduction, and inserting extra zero coordinates preserves the Euclidean norm exactly. The original infinity-radius packing and the old norm statement for the full matrix remain as proved in ell and I6. The new norm specifies only the costed uniform challenge. Neither the seed law nor any correctness or cost formula uses the solution norm.

## Targets

Fix any parameter set satisfying the amended model, the protected system shape, any admissible evaluation points, and the stated group and oracle models. In the chosen modes use the coefficient positions of Amendment n, the scalar field and the singleton factors of Amendment C7, and the QAP encryption and decryption of Amendment n1. The amended inverse theorem applies by (P3) with Amendments I3, I4 and I6 with the protected H3. The charged-mark bound is proved in Amendment Ncmp. Correctness and extraction use the same external witness relation, oracle model, budgets and probability bounds. Internally the projected witness forgets its Boolean tags.

### Correctness with error $2/q$

Fix an external witness, message and admissible evaluation points. All the tag variants in n1 are witnesses for the extended internal constraints. The single-cell group identities give $\Lambda_v=d_v[\kappa]_T+r(v)\Psi_v$, by exact polynomial division and the factor cancellation in C7. A direct target has $d_v=1$ and zero search base, so $\Lambda_v=[\kappa]_T$. The ordinary branch solves three exact integer logarithms using nonzero bases of order $q$ and the bound $2B+1<q$. The identity $a_t+b_t-c_t=v^{(t)}$ in the integer witness inputs gives the exact target $r(v^{(t)})$. Subtracting its search contribution from the full target combination yields the key. In the fallback $E_0$ is nonzero and the exact evaluation-point search gives the same key by its displayed identity. Therefore every branch is correct, in particular with error at most $2/q$. The final random-oracle query is the one made by encryption.

Conditional on all other coins, the search base is zero precisely when the linear form $y(v)$ is zero. Each fixed variant has homogeneous coordinate one, so the form is nonzero and uniform. Any two distinct variants are linearly independent as field vectors: since both homogeneous coordinates are one, a scalar dependence would force equality. Thus the two corresponding linear forms are jointly uniform. A secondary ordinary triple can be selected only if some primary ordinary base is zero, an event of probability at most $3/q$. The fallback requires one zero ordinary base in each triple. By pairwise uniformity and a union bound its probability is at most $9/q^2$. These bounds imply the conservatively charged $9/q$ and $135/q^2$ used in search_spread. All choices are independent of the search coordinates.

### Extraction and the reduction

Let $\mathcal A$ have the budget $Q<2^\lambda$ of generic group calls and at most $2^\lambda$ queries to each oracle. Fix one bit $b$ and messages $m_0,m_1$, and run the extraction experiment with $m_b$. The extractor reads the answered generic transcript without any oracle calls. It uses the protected extractor sketches for the plain sector. The empty alpha sector can be represented by zero records. It samples three independent probe vectors for each cell, uses the linear combinations of source-group records and pairings to form sketches, tests the sketches of the result and the difference when there is an old record, and directly checks its ordinary assignment against $S$, checks the three tag bits, and returns the ordinary witness only. In rank at most three, there are at most four assignments with first coordinate 1 to test: row echelon pivot coordinates determine the vector, pivot 0 must be present, and at most two remaining pivot choices are bits. Output is therefore always $\bot$ or a witness. For the single cell, the three records for a G1 leaf are coordinate vectors or zero and the three G2 records are scalars. Pairing records multiplies each vector by its paired scalar to form the three GT records. Linear group operations add or scale vectors or scalars. Initial records for factor entries can be represented by their unit indices and zero records by a common zero description. Therefore initialization is $O(N_\star+L)$ with the three independently uniform probes. Each later record, difference, or test costs $O(N_\star+|S|)$: perform elimination on at most three vectors and test the at most four projected Boolean assignments when the rank is at most three. This fits the original extractor bound and uses only the answered generic transcript.

The explicit reduction takes $A\in\mathbb F_q^{1\times(N+3)}$ uniform, uses the exact programming of msis_cols to sample the full seed matrix, samples the encryption coins, creates the ciphertext for $m_b$, and simulates the adversary in the protected generic model with the same random oracles. It runs the adversary once and then returns failure, with $s_b=0$. The programmed and independently sampled entries are jointly independent uniform entries. The full seed-oracle table therefore has precisely its original law for every sequence of queries, even at omitted matrix positions, and the adversary sees the same experiment. The reduction has no private recovery input and uses no adversary output. Its time is at most $t+148Q+(d_R+5)Q_H+C_R$ by the earlier simulation bound with no lifting. In the setup cost the matrix storage, sampling and scalar initialization use $O(k(\ell+1))$ operations. The explicit upper guard $m\le40000000$ gives $\ell+1<11D$ at $k=1$; reading, routing and sampling those entries adds $O(nD)$ to $C_R$. As before $C_R=O((N_\star+n)D+\mu)$ in the fixed scored branch. The extractor continues to operate on the answered generic transcript alone, with its independent probes.

Here is the first-mark argument. Setting all guesses to zero commutes with additions and pairings. Before the first mark all repeated labels correspond to formally equal expressions, which have equal stacks by the fiber equations applied to their difference for every $r$. Their sketches therefore agree, giving the extractor's record invariant. At a first good difference mark it tests the old-and-new difference. The extractor tests each eligible received or produced target-group record when its generic record is made. The eventual good key must have such a record, since an operand-only guess cannot be a good guess-free key. The extractor has already tested that record when the key query occurs. These are exactly the stack expressions covered by the view. Each is a passing nonzero rank-one matrix, so msis_bound puts the normalized Boolean witness in its row space. Conditional on the whole generic run, independent uniform probe tuples have uniform image on that row space: the sketch map is multiplication by the symmetric matrix and its image is its row space. The image of each tuple is nonzero with probability $1-1/q$. Three independent probes span the line unless all vanish, an event of probability $q^{-3}$. The normalized row is then one of the extractor's explicitly tested assignments and passes the original system and unit and tag checks. The conditional failure is at most $q^{-3}\le\varepsilon_f$ on the first good mark.

Let $u=2Q+2$. Every target query run has a first mark. The protected initial and guessed-mark estimates and the charged-mark estimate of Amendment Ncmp bound their three probabilities by
\[
\left(\binom{L_1}{2}+\binom{L_2}{2}+\binom{L_T}{2}\right)\varepsilon_f,\quad
N_{\rm cmp}(u)(\theta+\varepsilon_f)
+\left(\binom{L+3u}{2}+L+3u\right)\varepsilon_f,\quad
2^\lambda/N_{\rm free},
\]
respectively. These estimates concern the same sampler, oracle and record laws and use only the already checked view and degree properties, budget, and label counts. Together with the at-most-$q^{-3}$ good-mark extraction failure, these events cover target key query and no witness. The term $(8u+8)\varepsilon_f$ covers that good-mark failure. The total is at most $E(u)=s_b+E(u)$ since the remaining terms of $E$ are nonnegative and its guess term contains $2^\lambda/N_{\rm free}$. By (P5) and the generic-ledger implication of Amendment Ncmp $E(2Q+2)\le(Q+1)/2^\lambda$. Hence for each $b$ the target-query and no-witness probability is at most $(Q+1)/2^\lambda+s_b$, with exactly the stated oracle budgets and one MSIS instance. This proves Theorem 5.9 with its extraction time and soundness as above.
