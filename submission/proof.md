# Praxis with a Euclidean coefficient-norm SIS reduction

Throughout the proof $N$ is the protected external variable count and $N_\star=N+3$ is the number of internally sampled box coordinates. The three internal Boolean coordinates do not change which external witness relation is encrypted. The construction, coefficient placement and probabilities for the amended model follow.

## Amendment C5

Write $d=d_R$, $h_R=\mathrm{ring\_log}$, $p=\mathrm{pack\_digits}$, $p_f=\mathrm{form\_pad}$, $s_0=\mathrm{seed\_degree}$, $A_c=3n/2$, $S_0=\lceil(D-1)/\nu\rceil$, and $m=k(\ell+1)d$. Write $U_d=V_d=121$ and $s_p=\mathrm{short\_columns}$. Require $\mathrm{ring\_mode}=d=61$, $h_R=0$, and $(q\bmod4027)^{66}\equiv1\pmod{4027}$. Require $\lambda=100$, $N=391693$, $\nu=2048$, $n_{\mathsf c}=1692$, $p=17$, $s_p\in\mathbb Z$, $0\le s_p$, $16s_p\le N$, $p_f\in\mathbb Z$, $1\le p_f\le d$, $n=4332$, $s_0=2$, $K_1\ge K_2+1$, $K_2=19$, $J\le24$, and $m\ge55000000$. The scalar arithmetic guard is $W+V\le 3m$, where $W$ and $V$ are the following integers:
\[
 W=d\big((\ell+1)(3\lfloor k/2\rfloor+2(k\bmod 2))+2\lfloor k/2\rfloor\big)
       +2(U_d k+V_d(\ell+1)),
\]
\[
 \begin{split}
 V={}&2D+N+n_{\mathsf c}+32+(2K_1+6K_2+6)(N+4)+2K_2\\
    &+(\Delta-\Delta/\nu+2S_0+16)+(J+3)A_c+C_{\rm mask}\\
    &+12996+60(n+J+1)+10000+189336+(N+1)+100 .
 \end{split}
\]

The guard uses the protected $m$. The conductor $p_0=4027$ is prime by the nonzero remainders 1, 1, 2, 2, 1, 10, 15, 18, 2, 25, 28, 31, 9, 28, 32, 52, 15, 1 at primes through $\sqrt{p_0}$ in order. Since $p_0-1=2\cdot3\cdot11\cdot61$, the residues of $3^{(p_0-1)/p}$ for $p=2,3,11,61$ are $4026,2206,196,13$, so $a_0=3$ generates. Put $H=\langle a_0^d\rangle$ of size $f=66$ and $g_i=\sum_{u\in a_0^iH}\zeta^u$ for a primitive complex $p_0$-th root $\zeta$, with indices modulo $d$. The cyclotomic polynomial $1+X+\cdots+X^{p_0-1}$ is irreducible by Eisenstein after shifting $X$ by one. The checked $q^f\equiv1\bmod p_0$ puts $q\bmod p_0$ in $H$ and gives a primitive root $\omega$ in $\mathbb F_{q^f}$.

The periods are linearly independent over $\mathbb Q$: a rational linear relation gives a polynomial of degree at most $p_0-1$, with zero constant term, divisible by $1+X+\cdots+X^{p_0-1}$. This polynomial is zero, and the disjoint cosets make every coefficient in the relation zero. The period sum is $-1$. Products of periods are integer combinations of the periods and $1$, because the number of ordered exponent pairs producing a given sum modulo $p_0$ is invariant under multiplication of that sum by an element of $H$. Thus their integer span is an order $R$: a free rank-$d$ unital subring of their rational span. Its actual coefficient basis is
\[
 b_0=1,\quad b_j=g_{j-1}\ (1\le j<d).
\]
The transition between this and the period basis is integral with integral inverse, using the relation $1=-\sum_jg_j$. Both transitions use only additions and sign changes. In particular $b_0$ is the ring unit, as needed for tag packing and the independent homogeneous column.

For $\omega$ a primitive $p_0$-th root over the scalar field, the $d$ substitutions $\zeta\mapsto\omega^{a_0^i}$ induce scalar-valued ring maps, since $q\bmod p_0$ belongs to $H$. With period coordinates, the matrix $F$ of their simultaneous evaluation has entry $F_{ij}=\bar g_{i+j}$. Let $s$ be the index of the coset of $-1$, $P_{i,j}=1_{j-i=s\bmod d}$, and $J_d$ be the all-ones matrix. Then
\[
 FF^{\top}=p_0P-fJ_d.
\]
Indeed, $\sum_j\bar g_{i+j}\bar g_{k+j}$ enumerates each $x\in\mathbb F_{p_0}^\times$ once as the first exponent, and sums $\omega^{x(1+a_0^{k-i}h)}$ over $h\in H$ as the second exponent varies. Each inner sum over $x$ is $-1$ unless $1+a_0^{k-i}h=0$, when it is $p_0-1$. There is one such $h$ exactly when $k-i=s$. The row sums of $p_0P-fJ_d$ are $1$. If it annihilates a vector over $\mathbb F_q$, summing the coordinates first gives coordinate sum zero, and $p_0P$ then annihilates that vector, which must be zero since $p_0\ne q$. This proves that evaluation $E$ in the basis $b_j$ is an algebra isomorphism $R/qR\simeq\mathbb F_q^d$. Independently uniform coefficients in this basis therefore yield exactly uniform split tuples, in both directions.

Fix the scalar tables. For $b_a=\sum_{i<d}a^ig_i$ the difference of any two character values is a nonzero polynomial of degree below $d$, because the characters differ on the basis. Thus at most $(d-1)\binom d2<q$ choices cause a coincidence. In residue order take the first $a$ with squarefree characteristic polynomial of multiplication by $b_a$, computed by the period product rule and a derivative gcd. The split isomorphism diagonalizes multiplication, so this test detects exactly the required distinct values. Take the least root $r$ of that split polynomial. The powers of $b_a$ through degree $d-1$ form a basis by the Vandermonde determinant. Express each $g_i$ in this basis and evaluate at $r$ to get one character. Order the others by its cyclic shifts. Precompute these public tables.

### Ring arithmetic and transpose

Period evaluation is cyclic convolution after reversing the input since the matrix entry is $\bar g_{i+j}$. The inverse convolution commutes with the shift, the transpose reverses its kernel, and the unit-basis changes use only signs and additions. Thus each of the four basis maps is one fixed cyclic convolution and these changes. To multiply, first form the ordinary polynomial product and fold modulo $X^d-1$.

Let $f$ be the dynamic polynomial and $g_0$ the fixed polynomial, both of degree at most $d-1$. Put $L=2d-2$, $S=\{2-d,\ldots,d-1\}$, and $P(X)=\prod_{a\in S}(X-a)$. Store $g_0(a)/P'(a)$ at each point and the degree-$(d-1)$ coefficient of $g_0$. Compute
\[
 v_a=f(a)g_0(a)/P'(a),\qquad
 v_\infty=[X^{d-1}]f\,[X^{d-1}]g_0 .
\]
There are $L+1$ products because the normalized fixed factors are stored. Recover as $v_\infty P(X)+\sum_{a\in S}v_a P(X)/(X-a)$. This has the same top coefficient and $L$ values as the ordinary product. Their difference has degree below $L$ and $L$ distinct roots, so it vanishes. All points are distinct in the protected field.

Horner evaluates $f$ at each point. An integer scale of magnitude at most $d-1\le60$ uses signed binary additions and doublings. For reconstruction, split the point set in halves recursively. For each subset $T$, store $\sum_{a\in T}v_a\prod_{b\in T\setminus\{a\}}(X-b)$. Join by multiplying each child's polynomial by the other child's simple linear factors and adding the two results. Multiplication by $X-b$ uses an update per coefficient with an integer scale, shift and addition. Generate $v_\infty P$ by the same simple factors. At a node with $m$ leaves, these factor multiplications use at most $m^2$ coefficient updates. The sum across levels is at most $L\sum_{j<\lceil\log_2 L\rceil}\lceil L/2^j\rceil\le3L^2$. Addition upon joining and the leading term use at most $L^2$ further updates each, and Horner at most $Ld$. Twelve signed additions or doublings per update suffice since $|b|\le60$. The final fold, sum with the leading term and basis changes use fewer than $8d$ additions. This uses fewer than 953,000 additions at $d=61,L=120$ and uses at most $U_d=L+1=2d-1$ field products. A common scalar can be incorporated into the stored leaf factors by charging that scale once. The resulting maps are the exact period-basis representations of the given ring.

### Seed-oracle encoding

In the scored branch, the seed oracle's response type is a vector of $d_R$ scalar-field coordinates, in the order of the $d_R$ evaluation maps defining $E$. At each of the existing seed and entry indices it samples this tuple by independent uniform scalar coordinates and records it as the answer. The conceptual coefficient entry of the matrix is the unique element $E^{-1}$ maps that tuple to. Since $E$ is bijective, these conceptual entries are uniform in $R_q$, mutually independent, and have the same law as directly sampling all their coefficients in the stated integral basis. The raw oracle answers are already $E(M_{ij})$. Encryption and decryption read them in these coordinates. They never convert individual matrix entries to split form, and the transformations charged in $W$ are exactly those on the mask functionals and accumulated columns. This changes the representation of the same seed oracle, with one query per entry and the same independent-answer consistency rule. The reduction programs responses in these coordinates using its coefficient challenge as specified in Targets.

### Kernel conversion and scope

Amendment n places all matrix output coefficients at distinct positions. Vanishing of the forms is equivalent to vanishing of the homogeneous coordinate and of the nonconstant matrix product. The uniform challenge programs precisely those nonconstant columns, while column zero is independently uniform. Coordinate packing and its two norm isometries are proved in msis_bound and msis_norm. The inverse and lifting use integer coefficient vectors and the base field, independent of the multiplication algorithm. The view, mask, classification and reduction proofs in n, C6, C7, Ncmp and Targets use the same linear form map, query counts and seed law.

## Amendment I2

Use $R_{\rm tr}\ge18$ and require
\[
1000\exp\bigl(-99 R_{\rm tr}^2 N/(200(N+3))\bigr)\le\varepsilon_{\rm tr}.
\]
The remaining requirements are $\varepsilon_{\rm tr}<\mu_{\rm tr}$ and $g^3\mu_{\rm tr}>\xi_{\rm tr}/g$ as before. The actual covariance trimming radius is $\widehat R=R_{\rm tr}\sqrt{N/(N+3)}$, with $N_\star=N+3$. The proof in I3 derives the upper tail $10^d\exp(-99\widehat R^2/200)$ by Markov's inequality. This gives the stated loss at each trimmed fiber. For geometric counting use the enclosing ellipsoid of radius $R_{\rm tr}\ge\widehat R$, as in I3.

The difference radius in the protected $T_{\rm tr}$ is still sufficient. Any projected feature-row deviation from the center is at most $\widehat R(g/\sqrt{12})\sqrt{N_\star}$ times that row's coefficient sup norm by Cauchy--Schwarz. A difference doubles this bound, which gives $R_{\rm tr}g\sqrt{N/3}=T_{\rm tr}$ as the factor. The determinant and lifting comparisons in I5 and I6 therefore use the protected definition of $T_{\rm tr}$. All other uses of the ellipsoid are density loss, or upper bounds on its radii or volume. These are supplied by the tail guard or the enclosing ellipsoid, respectively.

## Amendment I3

The amended (I3) is
\[
\Lambda_1\ge 2\sqrt3 R_{\rm tr}\sqrt N_\star,\qquad
\Lambda_2\ge \sqrt2 \pi R_{\rm tr}^2 N_\star,\qquad
\Lambda_3\ge \frac{20 \pi R_{\rm tr}^3 N_\star\sqrt N_\star}{9\sqrt2} .
\]
The rank-two and rank-three geometric lower bounds change. All three inequalities here are checked by the parameter model.

### Which inverse-theorem steps use the change

In `blob:admissibility`, (P3) refers to these inverse conditions, and the bounds in (P1), (P2), (P4) and (P5) have no occurrence of a geometric factor $\Lambda_d$. The box, saturation, reduction, fiber and height definitions in `blob:lattices` use the same lattice operations. The regularity test uses $m(\Theta)h(\Theta)\le\Gamma_d/g^d$, and has the same definition. In `blob:trimming` the ellipsoid depends on $R_{\rm tr}$, $g$, and the basis through $\Sigma_\Theta$, with no $\Lambda_d$. The proof of `lem:prefix` uses only the lattice indices and ceiling count in (a)–(b), and (I1), (I2), (I4) to convert the rank-three ceiling count to the height and regularity in (c). The proof of `lem:trim` applies the exponential moment bound for independent box variables, then the exponential loss inequality in (I2). Thus the prefix and trimming lemmas have the same hypotheses and arguments. We prove `lem:sparse`, `lem:regularize`, and `lem:inverse` under the amended condition below.

### Integer-lattice facts used below

For an integral basis $B$ with a largest row minor on $J$, each component of $y\in{\rm span}_{\mathbb R}B$ is $B_iB_J^{-1}y_J$, with entries of the row $B_iB_J^{-1}$ bounded by one in absolute value by Cramer's rule and maximality of the minor. The component is therefore at most $\|y_J\|_1$ in absolute value. When the columns of $B$ generate a saturated integer lattice, their quotient in the ambient free integer group is torsion-free and finitely generated, hence free. Extending these columns by lifts of a quotient basis gives a unimodular basis of the ambient group. Taking its transpose shows $B^\top\mathbb Z^I=\mathbb Z^d$.

For the lifting fact, let $\Delta$ be an integer matrix of rank $k'>0$ with a nonzero minor $M$ of order $k'$ on rows $I_0$ and columns $J_0$. Put $\delta=\det M$. Assume $\delta\ne0\bmod q$, so $M$ is invertible modulo the prime $q$. Given $c^\top\Delta=0\bmod q$, write $I_1$ for the remaining rows and choose an integer vector $w\equiv\delta^{-1}c_{I_1}\bmod q$. Set $u_{I_1}=\delta w$ and $u_{I_0}^\top=-w^\top\Delta_{I_1,J_0}{\rm adj}M$. Then $u^\top\Delta_{J_0}=0$ by the adjugate identity. Those columns span the column space over $\mathbb Q$, so $u^\top\Delta=0$. The inside rows also agree with $c$ modulo $q$, by uniqueness of the solution for them using $M$ invertible modulo $q$. For rank zero take $u=c$. These facts use no inverse-parameter condition other than the nonzero modular minor at the lifting step.

### Prefix estimates

Here are the unchanged parts of the prefix lemma on the amended parameter domain. Let $\Theta$ be a saturated lattice of rank $d$, with integral basis matrix $B$ and a largest minor on $J$. Order its coordinates with $J$ first, let $I_k$ be the first $k$ coordinates, and let $\Theta_k={\rm span}_{\mathbb R}(B_{I_k})\cap\mathbb Z^{I_k}$, $k\ge d$. Let $h_k,m_k$ be its height and largest fiber density. Its rank is $d$ because the selected minor remains invertible. If $Y$ is a basis of $\Theta_k$, then $B_{I_k}=Y C$ for an integral nonsingular $d$-square matrix $C$. The fibers of the prefix are thus the level sets of $B_{I_k}^{\top}r$. The group $G_k=B_{I_k}^{\top}\mathbb Z^{I_k}=C^\top\mathbb Z^d$, by saturation and the integer-lattice lemma (b), has index $|\det C|$ in $\mathbb Z^d$. The $d$-row determinants of $B_{I_k}$ are multiplied from those of $Y$ by $\det C$. As their largest absolute value is the original $h(\Theta)$, this gives $h_k [\mathbb Z^d:G_k]=h(\Theta)$ and shows that $J$ is still a largest minor for $\Theta_k$. At $k=d$, the column span is all of $\mathbb R^J$, so $\Theta_d=\mathbb Z^J$, $h_d=1$ and $m_d=g^{-d}$. At the full set of coordinates the saturated lattice is $\Theta$.

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
 =\mathbb E e^{\sqrt{99/100} Z^\top\Sigma^{-1/2}Y}
 \le \mathbb E e^{(99/200)\|Z\|_2^2}=10^d .
\]
The inequality conditions on $Z$; the last equality follows by scaling each normal density in the integral. By Markov's inequality the probability of being outside the trimming ellipsoid is at most $10^d e^{-99\widehat R^2/200}\le\varepsilon_{\rm tr}$ by (I2) and $d\le3$. Trimming any subset removes at most that absolute density. This establishes the trimming conclusion without a norm assumption.


### Projected fiber counts

The claim of `lem:sparse` is as follows. Let $B$ be a basis of an integral lattice $\Theta$ on a coordinate set $I$ with $|I|\le N_\star$, of rank $d\in[3]$. Let $F\ne\varnothing$ be a set of points of the integer box on $I\cup\{i'\}$, $i'\notin I$, trimmed by $\Theta$, and $\Phi(r)=(B^\top r_I,r_{i'})$. If (a) $\Phi(F)$ has affine dimension $d+1$ and lies in a coset of an index-$q$ subgroup of $\mathbb{Z}^{d+1}$, then
$\Pr[F]\le\Lambda_d g^d h(\Theta)m(\Theta)/q$.
If (b) $F^\perp$ has rank $d'$ with $1\le d'<d$, a largest minor on $J\subseteq I$, and every vector of $F^\perp$ restricts to a vector in ${\rm span}_{\mathbb R}\Theta$ on $I$, then
$\Pr[F]h(F^\perp)\le\Lambda_{d-d'} g^{d-d'}h(\Theta)m(\Theta)$.
Here $F^\perp$ is the lattice of integer vectors normal to the differences in $F$.

For each possible image $(y,x)$, the probability of $B^\top r_I=y,r_{i'}=x$ is at most $m(\Theta)/g$ by independence, so $\Pr[F]\le|\Phi(F)|m(\Theta)/g$. We count images in $C=\mathcal{T}_\Theta\times[2,g+1]$.

For (a), put $s=d+1$, $\delta=q$, $J=\varnothing$, and let $p$ be the identity. Write $B=(B_1,B_2)$ with $B_1$ empty, and use $|\det(B_1)_J|=1$.
For (b), put $s=d+1-d'$ and let $Y$ be an integral basis matrix of $F^\perp$; $Y_J$ is invertible. The submatrix $B_J$ has row rank $d'$ since the columns $Y_J$ lie in its real column span. The integral kernel of $B_J$ is saturated in $\mathbb{Z}^d$, of rank $d-d'$. It has a basis that extends to an integral basis of $\mathbb{Z}^d$: the quotient by a saturated subgroup of $\mathbb{Z}^d$ is finitely generated and torsion-free, hence free, and lifts of a quotient basis give the extension. Using this basis change, write $B=(B_1,B_2)$ where $(B_2)_J=0$ and $(B_1)_J$ is invertible square. The columns of $B_2$ number $s-1$. Trimming is basis independent since the mean and covariance transform by the same invertible change on the image coordinates.

In case (b), the injective map $a=(a_{[d]},a_{d+1})\mapsto(Ba_{[d]},a_{d+1})$ maps the real annihilator of the differences of $\Phi(F)$ isomorphically onto the real annihilator of the differences of $F$, by the restriction assumption. The first annihilator has dimension $d'$ and its integer points form a saturated lattice with basis matrix $V$. The real annihilator of differences of $F$ is spanned by its integer points because those differences are integer vectors, so the restriction premise on integer normals suffices for this isomorphism. Split its rows into $V_1,V_2,V_3$ of lengths $d',s-1,1$. The image of its basis is $Y A$ for an integral nonsingular $d'$-square matrix $A$, as its columns are integral independent normals. At rows $J$, this gives
\[
(B_1)_J V_1=Y_J A .
\]
Consequently $V_1$ is invertible and $|\det(B_1)_J| \delta\ge h(F^\perp)$, where $\delta=|\det V_1|$. Write $y=(y_1,y_2)$ according to the basis split. Projection $p:(y,x)\mapsto(y_2,x)$ is injective on any affine translate of the kernel of $V^\top$, because there the first block of a difference is determined by $V_1^\top$. It therefore preserves the affine dimension of $\Phi(F)$, which is $s$. The projections of differences of image points lie in the kernel of
\[
 (y_2,x)\longmapsto V_2^\top y_2 + x V_3^\top
          \pmod{V_1^\top\mathbb{Z}^{d'}} .
\]
The map is onto because $V^\top \mathbb{Z}^{d+1}=\mathbb{Z}^{d'}$ by saturation and `lem:lattice-facts` (b), while the $y_1$ contribution vanishes in the quotient. The kernel has index $\delta$ in $\mathbb{Z}^s$. Thus in both cases $p(\Phi(F))$ has full affine dimension $s$, cardinality $|\Phi(F)|$, and lies in $p(C)$ and in a coset of an index-$\delta$ lattice.

A full-dimensional finite set $X$ of $m$ points in such a coset has ${\rm vol}_s{\rm conv}(X)\ge(m-s)\delta/s!$. To see this, start from any $s+1$ affinely independent points forming a simplex. One can add the points successively while maintaining a triangulation of their hull using all inserted points as vertices. For a point outside the hull, each boundary facet simplex strictly visible to the point gives a new simplex by coning it to the point. Those simplices have disjoint interiors and fill the new region, as rays from the point first hit the old hull in its visible boundary. At least one facet is strictly visible, so at least one full simplex is added. If a point is in the hull, take the unique smallest face of the triangulation containing it. This face has positive dimension since the point is distinct from all earlier vertices. Subdivide that face by coning its boundary faces to the point and make the respective subdivision of every full simplex incident to it, by adjoining the complementary simplex vertices. This covers exactly those full simplices and replaces each by at least two, since the point lies in the relative interior of the face. Hence there are at least $m-s$ full simplices. Each has volume at least $\delta/s!$, since the determinant of $s$ independent differences of coset points is a nonzero integer multiple of the determinant $\delta$ of its lattice. Since $m\ge s+1$, the region containing $X$, if convex, has volume at least $\delta/s!$. In particular, applying both consequences to $p(C)$ gives
\[
 |\Phi(F)|\le s!{\rm vol}_s p(C)/\delta+s
             \le (s+1)!{\rm vol}_s p(C)/\delta .
\]

The projection of the ellipsoid $\mathcal{T}_\Theta$ to the last $s-1$ coordinates has volume at most $v_{s-1}R_{\rm tr}^{s-1}(g/\sqrt{12})^{s-1}\sqrt{\det(B_2^\top B_2)}$, where $v_j$ is the volume of the Euclidean unit $j$-ball. Indeed, write its enclosing ellipsoid as the image of a unit ball by $R_{\rm tr}\Sigma_\Theta^{1/2}$ plus the center. The projected map has a Gram matrix on its range equal to the bottom-right block $R_{\rm tr}^2(g^2/12)B_2^\top B_2$, which gives the product of its nonzero singular values. The interval in $p(C)$ has length $g-1$. In either case $(B_2)_J=0$. By expansion of $\det(B_2^\top B_2)$ into squared row minors, and because $|\det(B_1)_J\det(B_2)_{J'}|=|\det B_{J\cup J'}|\le h(\Theta)$ for each $J'\subseteq I\setminus J$ of size $s-1$,
\[
 |\det(B_1)_J| \sqrt{\det(B_2^\top B_2)}
 \le h(\Theta)\sqrt{\binom{N_\star}{s-1}} .
\]
Combining with the counting bound and $\Pr[F]\le |\Phi(F)|m(\Theta)/g$ gives
\[
 \Pr[F]|\det(B_1)_J|\delta
 \le g^{j}h(\Theta)m(\Theta)
      (j+2)!v_j R_{\rm tr}^{j}\sqrt{\binom{N_\star}{j}/12^j},
 \quad j=s-1 .
\]
Use $\binom{N_\star}{j}\le N_\star^j/j!$ and $v_1=2,v_2=\pi,v_3=4\pi/3$. The three upper bounds on the geometric factor are $2\sqrt3 R_{\rm tr}\sqrt N_\star$, $\sqrt2\pi R_{\rm tr}^2N_\star$, and $20\pi R_{\rm tr}^3N_\star^{3/2}/(9\sqrt2)$. They are at most the three allowed $\Lambda_j$. In case (a), divide by $q$ to obtain the claim. In (b), replace $|\det(B_1)_J|\delta$ by $h(F^\perp)$ on the left to obtain the claim.

### Regularization with the new count

This subsection proves regularization under the growth conditions in Amendment I4.

The claim of `lem:regularize` is that a saturated lattice $\Theta$ of rank $d\in[3]$ with $m(\Theta)\ge\mu_{\rm tr}+(3-d)\varepsilon_{\rm tr}$ is contained in a regular saturated lattice of rank in $[d,3]$ and maximum fiber density at least $m(\Theta)-(3-d)\varepsilon_{\rm tr}$.

Write $\mu=\mu_{\rm tr}$ and $e=\varepsilon_{\rm tr}$ in this paragraph and the next two. Induct downwards on the initial rank. For $d=3$, `lem:prefix` (c) gives regularity directly. For $d\le2$, use `lem:prefix` with a largest minor at $J$ and $J$ first in the coordinate order. Denote the prefixes by $\Theta_k$, their heights and max densities by $h_k,m_k$, and the step order by $s_k$. The densities are nonincreasing, so each is at least $\mu+(3-d)e$. Take a densest fiber of $\Theta_k$ to form $F_k$. If the preceding $F_{k-1}^\perp$ strictly contains $\Theta_{k-1}$, trim this fiber by the regular containing lattice $\widetilde\Theta_{k-1}$ specified below. Otherwise leave the fiber whole. The density of each $F_k$ is at least $m_k-e$ by `lem:trim`. Its normal lattice contains $\Theta_k$. If this inclusion is strict, saturation gives a rank $d_k>d$. Its rank is at most three since a fiber of a rank-$a$ lattice has density at most $g^{-a}$ by fixing coordinates outside an invertible $a$-row minor, and $g^{-4}<\mu\le m_k-(3-d)e$ by (I5). Its max fiber density is at least $\Pr[F_k]\ge\mu+(2-d)e\ge\mu+(3-d_k)e$. By induction let $\widetilde\Theta_k$ be a regular saturated containing lattice of rank at least $d_k$, with $m(\widetilde\Theta_k)\ge m(F_k^\perp)-(3-d_k)e\ge m_k-(3-d)e$. This constructs the trimming lattice for the next step, and if $F_{|I|}^\perp\ne\Theta$ it gives the desired final lattice.

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
The displayed conditions keep the rank-one, rank-two and rank-three growth bounds. The additional upper range constraint gives $\sqrt g\le 2^{10}2^{\lambda/4}$, so the expected $O(\sqrt g N_\star^{1/4})$ group work is $O(2^{\lambda/4}N_\star^{1/4})$ for the common efficiency derivation.

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
Condition (I2) ensures that the denominator of $H_*$ is positive. If $M\le A_g$, then $B_g>A_g$ gives $s\ge1$ and the amended expression equals $H_*$. If $M>A_g$, then $j$ is the largest integer strictly below $M/A_g$, so $M>jA_g$, including at integral ratios.

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

In `blob:admissibility`, (P3) now requires the inverse-theorem conditions with the displayed (I6). The other admissibility conditions are identical, including (P4). The boxes, fibers, densities, saturation, height, and regularity in `blob:lattices` depend on the box, the basis, the field and the $\Gamma_d$, with no dependence on $\beta$. The ellipsoid of `blob:trimming` uses only $g,R_{{\rm tr}}$ and the basis. The following lemmas retain their contracts and arguments.

- In `lem:prefix`, the prefix saturation, indices, and fiber count use the integral basis and $g$. The estimate for a step of index below $g$ uses (I1), and the rank-three height and regularity use (I2) and (I4). They involve no short-vector bound.
- In `lem:trim`, the moment-generating-function bound for the independent uniform entries is applied to a linear image of the box and then Markov's inequality is applied with the threshold $R_{{\rm tr}}^2$. The loss condition used is precisely the exponential inequality in (I2).
- In `lem:sparse`, a trimming ellipsoid is projected along the normal constraints and lattice points in the projection are bounded by its volume and the lattice index. The conversion of the volume estimate to the constants uses (I3). The new (I6) is absent from both estimates and their proofs. The sharper geometric constant from the separate (I3) amendment is proved in that section.
- In `lem:regularize`, the downward induction uses the trimming loss, the prefix lattice inequalities, and the projected density–height bound. Promotion can only reach rank three by the inequality $g^{-4}<\mu_{{\rm tr}}$ from (I5). The growth bounds in (I4) suffice for the final prefix. Neither a bound on a short multiple nor (I6) enters the induction.

The prefix estimates, trimming, sparse projection, and regularization used below are proved in I3, and the rank-three height bound is proved in H3. A saturated lattice of rank one or two with density at least the threshold has the respective unchanged height bound from regularity, as explained in I4.

### Volume of the terminal coordinate body

For $d=2,3$ let $a_1,\ldots,a_M$ be the rows of $BB_J^{-1}$, where $J$ is a largest $d$-row minor. These include all standard unit vectors. Every $d$-row determinant has absolute value at most 1, since it is an original minor divided by the chosen largest minor. Define the compact, centrally symmetric body
\[
 K=\{x\in\mathbb R^d:\ |a_i^\top x|\le1\text{ for every }i\}.
\]
It has the origin in its interior since the list is finite. We prove the respective volume lower bounds needed for the amended terminal norm.

#### Planar bound

Let $C={\rm conv}\{\pm a_i\}$. This is the polar of $K$, since the inequalities for the vertices give those for every convex combination, and separation gives the converse. Determinant bilinearity implies $|\det(a,b)|\le1$ for all $a,b\in C$. Rotate by $\pi/2$ using $J$. Then $|a\cdot Jb|\le1$ for every $a\in C$ and $b\in C$, so $JC\subseteq K$.

Define $\|x\|_K=\inf\{s>0:x\in sK\}$. This is a norm because $K$ is bounded, centrally symmetric, convex and contains the origin in its interior. For the triangle inequality, if $x\in sK$ and $y\in tK$, then $(x+y)/(s+t)$ is a convex combination of $x/s$ and $y/t$; pass to the infimum. The polygon $K$ has a counterclockwise boundary with finitely many edges. On each edge with initial point $p$ and directed edge vector $v$, choose its outward normal $a$ scaled so that $a\cdot p=1$. Such scaling is positive since the origin is interior. As $a\cdot x\le1$ on $K$, we have $a\in C$. The counterclockwise orientation gives $v=tJa$ for $t>0$. Hence $\|v\|_K\le t$, and $\det(p,v)=t(a\cdot p)=t$. Joining the origin to the polygon's vertices divides it into triangles, so $2{\rm vol}_2 K=\sum_{\rm edges}\det(p,v)\ge\sum_{\rm edges}\|v\|_K$.

To lower bound this last sum, choose any $x\in\partial K$ and traverse the boundary counterclockwise from $x$ to $-x$. The continuous function $y\mapsto\|y-x\|_K$ goes from zero to two, so some intermediate $y$ satisfies $\|y-x\|_K=1$. The radial direction of each boundary point is unique since the origin is interior, so $y$ is not collinear with $x$. The six boundary points
\[
 x,\ y,\ y-x,\ -x,\ -y,\ x-y
\]
occur in this cyclic order: the direction of $y-x$ is strictly between those of $y$ and $-x$, as a positive sum of these vectors, and the other half is obtained by negation. The successive chord vectors are $y-x,-x,-y,x-y,x,y$, each of norm one. Split the boundary path at these six points. Splitting an edge does not change its norm-length by homogeneity on that ray, and the triangle inequality shows the length of each of the six resulting arcs is at least the length of its chord. Thus $\sum_{\rm edges}\|v\|_K\ge6$, and ${\rm vol}_2 K\ge3$. This proof uses only the finite strip description and the normalized determinants.

#### Three-dimensional bound

Maximize $\det A$ among positive semidefinite symmetric matrices with $a_i^\top A a_i\le1$ for every $i$. The domain is compact: the standard unit constraints bound all diagonal entries and positive semidefiniteness bounds each off-diagonal entry by the geometric mean of its two corresponding diagonal entries. A small positive multiple of the identity is feasible, so a maximizing $A$ is positive definite. Put $u_i=A^{1/2}a_i$, and call an index active when $\|u_i\|_2=1$. The identity lies in the cone generated by $u_i u_i^\top$ at the active indices. To prove this, the cone is closed since every generator has trace 1, so bounded traces bound the coefficients in any sequence of nonnegative combinations. If $C_0$ is the nearest cone point to $I$ in the trace inner product and $S=I-C_0$, the minimizing property gives $\langle S,X-C_0\rangle\le0$ for every cone point $X$. Test $X=0,2C_0$ to see $\langle S,C_0\rangle=0$. If $S\ne0$, then ${\rm tr}S=\|S\|_{\rm F}^2>0$ and $u_i^\top S u_i\le0$ for all active constraints. For small $t>0$, $A^{1/2}(I+tS)A^{1/2}$ remains feasible by those inequalities and the strict slack of all inactive constraints. Its determinant increases because $\det(I+tS)=1+t{\rm tr}S+O(t^2)$, a contradiction.

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

On the real vector space of symmetric three-by-three matrices with inner product $\langle B,C\rangle={\rm tr}(BC)$, define the positive semidefinite operator $L(B)=\mathbb E[\langle XX^\top,B\rangle XX^\top]$. The trace of an outer product operator of a vector with itself equals its squared norm, so ${\rm tr} L=\mathbb E\|XX^\top\|_{\rm F}^2=1$. The identity matrix is an eigenvector with eigenvalue $1/3$, and its orthogonal complement has five nonnegative eigenvalues $\lambda_1,\ldots,\lambda_5$ summing to $2/3$. The trace of a product of two outer products is the square of their inner product. For three it is the product of their three cyclic inner products, by direct multiplication of the rank-one operators. Applying these identities to independent samples, whose inner products on this matrix space are squared dot products, gives $M={\rm tr} L^2$ and $T={\rm tr} L^3$. Therefore
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
 \quad a=\sqrt{\det A},
\]
by the normalized three-row determinants and the transformation $A^{1/2}$. The central section of $K'$ in this plane is described by the inequalities $|\tilde u_j\cdot x|\le1$. Scaling the row vectors by $1/\sqrt a$ divides each planar determinant by $a$, and scales the planar body by $\sqrt a$. That body is a bounded planar strip intersection with interior. The planar proof above used only these properties, central symmetry, and the determinant bound. Consequently
\[
 {\rm area}(K'\cap u^\perp)\ge 3/a .
\]

For completeness, for two compact convex planar sets of positive area the square root of area of their Minkowski combination with weights $1-t,t$ is at least the same combination of the square roots of their areas. To prove it, first normalize both sets to area one. The vertical slice widths $f,g$ are positive and continuous in the interiors of their respective first-coordinate intervals. Let $x_f(s),x_g(s)$ for $0<s<1$ be the inverse functions of their integrals from the left endpoints. Their derivatives are $1/f(x_f(s))$ and $1/g(x_g(s))$. At the interpolated first coordinate $(1-t)x_f(s)+t x_g(s)$, the slice of the combination contains the respective combination of the two interval slices. Its length is at least $(1-t)f(x_f(s))+t g(x_g(s))$. After changing variables by the strictly increasing interpolated first coordinate, the area is at least the integral over $0<s<1$ of
\[
 \big((1-t)f+t g\big)\big((1-t)/f+t/g\big)\ge1 ,
\]
where the inequality follows from $f/g+g/f\ge2$. The change of variables holds first on compact subintervals of $(0,1)$, and their integrals increase to the stated lower bound. For arbitrary positive areas let their square roots be $r_1,r_2$. Apply the area-one result to the sets scaled by $1/r_1,1/r_2$, now with normalized weights proportional to $(1-t)r_1,t r_2$, and scale back by their sum. This proves the claim, including the endpoint weights by equality.

Put $x=\pi a$ and $R=\sqrt{3/x}$. If $x\ge3$, the unit ball already gives ${\rm vol}_3 K\ge4x/3\ge4$. Otherwise $R>1$. The ball slice at height $z_0=\sqrt{R^2-1}/R$ in direction $u$ is a disk of radius $1/R$. The central section has area at least $\pi R^2$. For each $0\le z\le z_0$, convexity of $K'$ includes in its section at height $z$ the Minkowski combination of these two sections with weights $1-z/z_0,z/z_0$. The planar result just proved bounds the area below by
\[
 \pi\big(R-z\sqrt{R^2-1}\big)^2 .
\]
For heights $z_0\le z\le1$ use the ball section; negative heights have the same areas by symmetry. If $j=\sqrt{R^2-1}$, the volume gain beyond the ball is at least
\[
 2\pi\int_0^{j/R}[(R-jz)^2-(1-z^2)] dz
 =\frac{2\pi j^3}{3R}.
\]
Indeed the first two terms after integration, $(R^2-1)j/R$ and $-Rj(j/R)^2$, cancel, and the cubic term is $(j^2+1)(j/R)^3/3=j^3/(3R)$. Scaling back by $A^{1/2}$ gives
\[
 {\rm vol}_3 K\ge \frac{4x}{3}+\frac{2(3-x)^{3/2}}{3\sqrt3}.
\]
The right hand side is increasing on $0\le x\le3$, as its derivative is $4/3-\sqrt{(3-x)/3}\ge1/3$.

It remains to verify the rational lower volume bound used by the rule. Squaring gives
\[
 \frac{12}{25}-(\frac{6928}{10000})^2
 =\frac{11}{390625}>0 .
\]
Also $\pi>6283/2000$. Indeed $\pi=16\arctan(1/5)-4\arctan(1/239)$ by the tangent addition formula in the first quadrant: the tangent of $4\arctan(1/5)$ is $120/119$. Integrating the alternating geometric series for $1/(1+s^2)$ gives
\[
 \pi>16(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}-\frac1{7\cdot5^7})-\frac4{239}
 =\frac{1231847548}{392109375}>\frac{6283}{2000}.
\]
Thus $x> x_0=21764/10000$ since $(6283/2000)(6928/10000)-x_0=39/1250000$. With $c=2509/1000$ and $r=8/c-4x_0/3=1348531/4704375>0$, the exact comparison is
\[
 4(3-x_0)^3-27r^2=\frac{394261548376699}{24590160156250000}>0 .
\]
Taking the positive root verifies $4x_0/3+2(3-x_0)^{3/2}/(3\sqrt3)>8/c$. The case $x\ge3$ also exceeds $8/c$. This proves the required rank-three volume estimate with coefficient $2509/1000$.

We also use the following elementary lattice-volume implication. For a full lattice $L$ in $\mathbb{R}^d$ and a centrally symmetric compact convex body $K'$ with ${\rm vol}K'\ge 2^d\det L$, there is a nonzero lattice point in $K'$. For strict inequality, translate the pieces of $K'/2$ lying in distinct translates of a half-open fundamental parallelepiped for $L$ back into that parallelepiped. The sum of their volumes exceeds $\det L$, so two pieces overlap. The two corresponding distinct points of $K'/2$ differ by a nonzero lattice vector, lying in $K'$ by convexity and symmetry. For equality apply the strict argument to $(1+1/j)K'$ for each positive integer $j$; these sets lie in $2K'$, which contains only finitely many lattice points. A nonzero point occurring infinitely often lies in the closed body $K'$.

### Amended inverse theorem

For prime $q$, with the remaining hypotheses in `lem:inverse` and the (I6) above, every nonzero $v\in\mathbb{F}_q^{N_\star+1}$ with $v_0=0$ and ${\rm gp}(v^\top)>\theta$ has an integer short multiple $x$ with $x_0=0$, $0<\|x\|_\infty\le\beta$, and $x\bmod q=a v$ for some $a\in\mathbb{F}_q^*$.

Remove zero coordinates and order the nonzero coordinates as $v_1,\dots,v_{N_0}$. For a prefix of length $i$, let $p_i$ be its maximum modular fiber density for independent box coordinates uniform on $[2,g+1]\cap\mathbb{Z}$. Each fiber of the longer prefix, conditional on the last coordinate, is a fiber of the shorter prefix. Hence $p_i\ge p_{i+1}$. The single-coordinate map is injective on the box since $v_1\neq0$ and $g+1<q$, so
\[
\theta<p_{N_0}\le p_i\le p_1=1/g.
\]
Inductively we construct a saturated regular lattice $\Theta$ on the first $i$ coordinates with rank $d\in\{1,2,3\}$, $v_{[i]}\in\bar\Theta$, and $m(\Theta)\ge p_i-3\varepsilon_{{\rm tr}}$. This gives $m(\Theta)>\mu_{{\rm tr}}$ and $h(\Theta)\le H_d$, using regularity when $d\le2$ and `lem:prefix` (c) when $d=3$. For $i=1$ use $\mathbb{Z}$. Its height is 1, density is $1/g$ and $\Gamma_1\ge1$ follows from (I4) and $\mu_{{\rm tr}}<1/g$.

For the extension step choose any integral basis $B$ of $\Theta$, with a largest minor on row set $J$. Its determinant in those coordinates has absolute value $h=h(\Theta)$. The proof uses normalized features to bound the modular rank of the difference matrix.

Let $v_{[i]}=Bc'\bmod q$, and $c=(c',v_{i+1})$ over $\mathbb{F}_q$. Take a densest modular fiber of $v_{[i+1]}$ and trim it by $\Theta$, obtaining $F$ of density at least $p_{i+1}-\varepsilon_{{\rm tr}}$, by `lem:trim`. Write $\Phi(r)=(B^\top r_{[i]},r_{i+1})$. The points $\Phi(F)$ lie in one coset of the subgroup $c^\top y=0\bmod q$ of index $q$ in $\mathbb{Z}^{d+1}$, since the last entry of $c$ is nonzero. If their affine dimension were $d+1$, `lem:sparse` (a) and regularity would give
\[
\Pr[F]\le \Lambda_d  g^d h(\Theta)m(\Theta)/q \le \Lambda_d\Gamma_d/q<\mu_{{\rm tr}},
\]
using (I5). This contradicts $\Pr[F]>\theta-\varepsilon_{{\rm tr}}$. Let $k'\le d$ be the actual dimension and $\Delta_*$ the integer matrix whose columns are differences of points of $\Phi(F)$ from any fixed point. Its rank is $k'$.

Put $P=BB_J^{-1}$, with entries bounded by one by the largest-minor argument. The normalized features are $(P^\top r_{[i]},r_{i+1})$. They are obtained from $\Phi$ by $A^{-1}$ where $A={\rm diag}(B_J^\top,1)$ is integral and $|\det A|=h$. The ellipsoid condition is unchanged after the respective covariance change. Each normalized feature's deviation from its center is at most $\widehat R(g/\sqrt{12})\sqrt{N_\star}$, since its row of coefficients has Euclidean norm at most $\sqrt{N_\star}$. Thus every entry of the normalized differences $A^{-1}\Delta_*$ has magnitude at most $2\widehat R(g/\sqrt{12})\sqrt{N_\star}=R_{\rm tr}g\sqrt{N/3}=T_{\rm tr}$, also for the last row since $g-1<T_{\rm tr}$.

For any square minor $M'$ of $A^{-1}$, $h\det M'$ is an integer: take the chosen columns of $A^{-1}$ and append the standard basis columns indexed by the complementary chosen-row set. Expansion in the standard columns gives $\pm\det M'$. Multiplication by $A$ makes the full square matrix integral, proving the divisibility assertion. Cauchy--Binet then shows that $h$ times each $k'$-minor of $A^{-1}\Delta_*$ is integral. A nonzero such minor exists if $k'>0$, and its multiple by $h$ has magnitude at most $h k'!T_{\rm tr}^{k'}\le h d!T_{\rm tr}^d<q$ by (I5), since $h\le H_d$ and $T_{\rm tr}\ge1$. In particular $q\nmid h$. Reducing that minor modulo $q$ through the invertible denominator $h$ shows the normalized difference matrix has rank at least $k'$ over $\mathbb F_q$. As $A$ is invertible there, the integral $\Delta_*$ also has rank $k'$ (larger integer minors vanish). Its nonzero modular maximal minor is enough for the lifting fact of I3, which gives an integral $u\equiv c\bmod q$ with $u^\top\Delta_*=0$. If $k'=0$, take any integral representative of $c$. Consequently $u^\top\Phi(r)$ is constant on $F$, and $(Bu_{[d]},u_{d+1})$ lies in the saturated normal lattice $F^\perp$, reducing to $v_{[i+1]}$. In particular $F^\perp$ has positive rank. A rank-$s$ lattice fiber has density at most $g^{-s}$, since fixing the coordinates outside an invertible row minor leaves at most one assignment to the remaining $s$ coordinates. Since $\Pr[F]>\theta-\varepsilon_{{\rm tr}}>\mu_{{\rm tr}}$ and $g^{-4}<\mu_{{\rm tr}}$, its normal lattice has rank at most three. Its maximum fiber density is at least $\Pr[F]>\mu_{{\rm tr}}+2\varepsilon_{{\rm tr}}$. Apply `lem:regularize` to $F^\perp$ to get a regular saturated containing lattice with density at least $m(F^\perp)-2\varepsilon_{{\rm tr}}\ge p_{i+1}-3\varepsilon_{{\rm tr}}$. It contains the lift of $v_{[i+1]}$. This proves the induction.

For the terminal lattice choose $J$ as above. Let $z_0\in\mathbb{Z}^d$ with $Bz_0\equiv v_{[N_0]}\bmod q$. It is nonzero mod $q$ because $v_{[N_0]}\ne0$. The preimage $Z\subseteq\mathbb{Z}^d$ of the line $\mathbb{F}_q z_0$ has index $q^{d-1}$, since reduction of $\mathbb{Z}^d$ is onto and the line has $q$ elements out of $q^d$. Hence $L=B_J Z$ has determinant $h(\Theta)q^{d-1}$. Consider the body of feasible first coordinates
\[
K_B=\{u\in\mathbb{R}^d:\|B B_J^{-1}u\|_\infty\le1\}.
\]
The rows indexed by $J$ are the unit rows. Each $d$-row determinant has absolute value at most 1 because it is a minor of $B$ divided by its largest minor, up to sign. The body is symmetric, closed, convex and bounded. In rank one the unit interval lies in it by the largest-minor bound and has length 2. Since $h(\Theta)\le H_1\le\beta$, ${\rm vol}(\beta K_B)\ge2\det L$. In rank two the planar bound gives
\[
 {\rm vol}_2(\beta K_B)\ge3\beta^2\ge4H_2q\ge4h(\Theta)q=4\det L.
\]
In rank three, $h(\Theta)\le\lfloor H_3\rfloor$ by Amendment H3 and integrality. Hence
\[
 {\rm vol}_3(\beta K_B)\ge (8/(2509/1000)) \beta^3
 \ge (8/(2509/1000)) (2509/1000)\lfloor H_3\rfloor q^2
 \ge 8\det L .
\]
The volume implication gives a nonzero $u=B_J z$ in $L\cap\beta K_B$ in each rank. Put $x'=Bz$. It is nonzero because its coordinates in $J$ are $u$, and its norm is at most $\beta$ by the definition of $K_B$. Modulo $q$, $x'$ is a multiple of $v_{[N_0]}$ since $z\in Z$. If that multiple were zero, each integer entry of $x'$ would be divisible by $q$. As $\|x'\|_\infty\le\beta<q/2$ this would force $x'=0$. Extend $x'$ by zeros in the deleted positions, including coordinate 0, to obtain the required short multiple.

### Conditions for the range-dependent Euclidean reduction

Write $B_{\rm E}=\mathrm{beta\_sis}$, $N_\star=N+3$, $\mu=\mu_{\rm tr}$, $e=\varepsilon_{\rm tr}$, $C_3=\mathrm{cov3}$, and $C_2=\mathrm{cov2}$. In addition to the four conditions on the original inverse bound, require
\[
R_{\rm tr}=18,\quad g\ge2^{49},\quad1024N_\star\le g,\quad 10^7N_\star\le g,\quad H_3\le g,\quad g^4\mu\ge 147/100,\quad H_2^5<g^{12},\quad 1000e\le\mu,
\]
\[
 C_3\ge 1341/100,\qquad
 C_2\ge100000 C_3.
\]
\[
 B_{\rm E}\in\mathbb Z,\quad1\le B_{\rm E},\quad 2B_{\rm E}<q,\quadB_{\rm E}^4<q^3,
\]
\[
 B_{\rm E}g^2\mu\ge\sqrt{N_\star}\Gamma_1,\qquad
 200 B_{\rm E}^2g^2\mu\ge231 C_2 q,\qquad
 70 B_{\rm E}^3g^3\mu\ge99 C_3 q^2.
\]
The added determinant guard uses the Euclidean Hadamard bound on four short vectors. The original four inverse inequalities still prove the general infinity-radius statement at $\beta$, which satisfies the separately checked (P4). The new guards prove the Euclidean short multiple and deterministic polynomial-time lift used by the reduction in Amendment msis_bound. The degree and form of generic expressions, oracle counts, correctness and witness-extractor span argument use neither radius.

Also require $H_1<g^4$ and $B_{\rm E}g\mu\ge90000 C_2+20000000 C_3+200$. These guards prove the rank-one Euclidean estimate in msis_bound for the unrestricted heavy-stack conclusion.

## Amendment Ncmp

For the variable $u$ used by the bound $E$, set
\[
N_{{\rm cmp}}(u)=\frac{u(u+10)}8 .
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
 \le N_{{\rm cmp}}(u)(\theta+\varepsilon_f)
       +(\binom{L+3u}{2}+L+3u)\varepsilon_f .
\]
This argument holds for every realized $M$, independent of the form packing.

### Generic ledger and scope of the amendment

The generic ledger has the same implication from (P5). In the amended $E$, all coefficients as a polynomial in $u$ are nonnegative and its degree is two. Here $L\ge1$, $N_{{\rm free}}>0$ by (P2), and $\binom{L+3u}{2}$ expands with nonnegative constant, linear and quadratic coefficients. The new $N_{{\rm cmp}}$ has nonnegative coefficients. For real $Q$ on $[0,2^\lambda-1]$, the function $Q\mapsto E(2Q+2)-(Q+1)/2^\lambda$ is convex because its quadratic coefficient is nonnegative. At the first endpoint it is at most zero by the first P5 test. At the second it is $E(2^{\lambda+1})-1$, at most zero by adding the P5 tests. By convexity it is at most zero throughout. The threshold side conclusion of the generic ledger becomes $\theta<2^{1-2\lambda}$ for $\lambda\ge1$. Indeed putting $U=2^{\lambda+1}$, we have $N_{{\rm cmp}}(U)-N_{{\rm cmp}}(2)=U^2/8+5U/4-3>2^{2\lambda-1}$. Every other term in $E(U)-E(2)$ is nonnegative, so the second P5 bound implies the stated strict threshold limit.

The changed count enters the admissibility block only through the value of $E$ in P5. The expression, monitor and symbolic-game blocks are independent of the count: they specify the same formal polynomial expressions, oracle label sampling and classifications of marks and events. The view lemma uses degree, coin ranges, algebraic identities of the factors and polynomial root bounds, all independent of this count. The implication $\varepsilon_f<1$ used by the comparisons follows as before because $E(2)\ge24\varepsilon_f$ from its fourth term and (P5) remains in force. The factor-one-half lemma concerns the uniform-mask coupling and the two actual failure probabilities, so its argument has no count or bound $E$ as a premise. The initial and guessed-label bounds use only the distinct received-expression comparisons and the uniform as-yet-unassigned target label respectively. The reduction lemma uses the private polynomial degree, gradient distribution, rank and short-vector properties, with no $\theta$-charge count. Its success probability refers to the same run and the same instance. Thus those results in the background list of the bound block apply with the same statements and arguments. The charged-mark and generic-ledger results are proved above, and extraction is derived in Targets.

The extractability-error corollary follows with its original statement from Targets and the factor-one-half lemma. For allowable budgets, in the combined bit experiment with uniform $b$, put $f_i=\Pr[\mathsf{Tgt}\wedge\mathsf{Fail}\mid b=i]$. The probability of both a correct bit and extraction failure is at most $1/2+(f_0+f_1)/4$. The target-query bound in Targets gives $f_i\le (Q+1)/2^\lambda+s_i$ for each $i$. Both reductions run in time bounded by $t_R=t+O(Q+d_R Q_H+\mu)+{\rm poly}(D,\log q)$, including fixed description and advice, so each $s_i$ is bounded by ${\rm Adv}^{{\rm MSIS}}(t_R)$ by its defining maximum. Substitution gives extractability error at most $(Q+1)/2^{\lambda+1}+{\rm Adv}^{{\rm MSIS}}(t_R)$ at the same extractor time. Outside the stated budgets, the trivial probability upper bound 1 yields error $1/2$ as in the corollary. This accounts for every result in the background list of the bound block.

## Amendment D

The external system $S$ and its number $N$ of Boolean unknowns are fixed. Internally extend an assignment with three auxiliary Boolean coordinates $\mathsf b_1,\mathsf b_2,\mathsf b_3$, all unconstrained except for their Booleanity. Put $N_\star=N+3$. The extended assignment vector has $N_\star+1=N+4$ coordinates including the homogeneous coordinate zero. Every witness of the external system has all eight extended tags, and projecting any extended witness onto coordinates zero through $N$ gives an external witness. The encoding uses no tag as an extra condition on the external system.

Use $N_\star+1$ distinct Booleanity points $d_0,\ldots,d_{N_\star}$, a distinct key point $\rho$, and the same $n_{\mathsf c}$ cosets of size $\nu$ for the external constraints. Hence $D=N+5+\nu n_{\mathsf c}$. Use the protected subgroup placement in the finite scored algorithm with this $D$. The algebraic identities apply to every admissible set of points. At $d_0$ set $A=0,B=e_0$. At $d_i$, $i>0$, set $A=e_i-e_0,B=e_i$, including the three new Booleanity points. Fix a public primitive eighth root $\omega_8$ in the scalar field, which exists because $8\mid q-1$. Set $c_*=(\omega_8+\omega_8^{-1})^{-1}$; indeed $(\omega_8+\omega_8^{-1})^2=2$ since $\omega_8^2+\omega_8^{-2}=0$. At $\rho$ set $A=c_*(e_{\mathsf b_1}+e_{\mathsf b_2})$ and $B=c_*(e_{\mathsf b_1}+e_{\mathsf b_2}-e_0)$. On the constraint cosets keep the protected evaluations, extending those linear forms by zero in the tag entries. The coordinate polynomials are the unique interpolants of degree below $D$. Store their sparse point-value descriptions rather than a dense coordinate-by-degree table. Define $Z_0$ to vanish at all $d_i$ and $\rho$, $Z$ at every evaluation point except $\rho$, $Z_*=(X-\rho)Z$, and $L_\rho=Z/Z(\rho)$. Thus $Z_*=Z_0Z_{\mathcal K}$, where $Z_{\mathcal K}=\prod_t(X^\nu-\delta_t^\nu)$ is the monic coset vanishing polynomial.

Here is the QAP criterion under this setup. For a symmetric $W$, $P_W=A^\top W B$ takes values $0$ at $d_0$, $W_{ii}-W_{0i}$ at $d_i$ with $i>0$, and $c_*^2(W_{\mathsf b_1,\mathsf b_1}+W_{\mathsf b_2,\mathsf b_2}+2W_{\mathsf b_1,\mathsf b_2}-W_{0,\mathsf b_1}-W_{0,\mathsf b_2})$ at $\rho$. Once the Booleanity tests hold, this last expression equals $W_{\mathsf b_1,\mathsf b_2}$, using symmetry and $2c_*^2=1$. On each constraint coset $P_W/Z_0$ is the list of terms in that constraint's quadratic test. Let $R_W$ be the polynomial of degree below $\nu n_{\mathsf c}$ interpolating these coset values. The sum of $X^a$ on $\delta_t\mathcal G$ is zero unless $\nu\mid a$, in which case it is $\nu\delta_t^a$. Among degrees below $\nu n_{\mathsf c}$, the multiples of $\nu$ give an invertible Vandermonde matrix in the distinct $\delta_t^\nu$. Consequently all coset sums vanish if and only if $R_W$ omits all divisible powers. Under the Booleanity and constraint tests, $P_W-W_{\mathsf b_1,\mathsf b_2} L_\rho-Z_0 R_W$ vanishes at every evaluation point. It is therefore divisible by $Z_*$, with quotient degree below $D-1$ from $\deg P_W\le2D-2$. Equivalently $P_W-Z_0R_W$ is divisible by $Z$ with quotient degree below $D$. Conversely, either such identity with an allowed $R$ implies the Booleanity values and the coset sum tests by evaluation, and $R$ is the unique interpolated remainder. In the key identity, evaluation at $\rho$ gives exactly the specified corner $W_{\mathsf b_1,\mathsf b_2}$. For a witness vector $v$, these identities apply to $vv^\top$, with $P_v=A_v B_v$ and key corner $\mathsf b_1\mathsf b_2$.

The new key evaluation has $A(\rho)=c_*(e_{\mathsf b_1}+e_{\mathsf b_2})$, which together with $A(d_i)=e_i-e_0$ for $i>0$ spans all form coordinates: the differences span the hyperplane of coordinate sum zero and $A(\rho)$ has coordinate sum $2c_*\ne0$. The vectors $B(d_i)=e_i$ are still a basis. These properties, the QAP criterion and the updated $D$ are the only changes in the generic comparison and coincidence arguments, explicitly used in C7. The point descriptions consist of the nonzero input terms and $O(D)$ point data. For evaluation of all coordinate polynomials at a scalar off the point set, tabulate the $D$ Lagrange weights there and accumulate the listed nonzero coordinate entries times their weights. For a witness, accumulate the point values of the two scalar witness polynomials and interpolate only those two polynomials, not the coordinate table. The same subgroup interpolation and vanishing-polynomial algorithms therefore give $O(|S|+D\log D+\log q)$ setup and the claimed scalar polynomial work with these point sets. The three extra Booleanity evaluations and the key evaluation add only a constant number of nonzero coefficients. The score still uses the fixed original nonzero-coefficient charge.

## Amendment ell

Set $p=\mathrm{pack\_digits}=17$, $s_p=\mathrm{short\_columns}$, and $\ell=\lceil(N+s_p)/p\rceil+3$. Pack the first $16s_p$ ordinary coordinates into $s_p$ columns of sixteen positions each, with all positions from the seventeenth through the last equal to zero. Pack the remaining $N-16s_p$ coordinates into blocks of seventeen positions, padding the last block with zeros and leaving every position above seventeen zero. The number of ordinary columns is $s_p+\lceil(N-16s_p)/17\rceil=\lceil(N+s_p)/17\rceil$, by adding the integer $s_p$ within the ceiling. The checked bound $16s_p\le N$ ensures each short column has its sixteen designated input positions. Use the coefficient order and positions of C5, placing each of the three tag coordinates in the constant position of its own separate following column. The independent homogeneous entry uses column zero. All matrix entries, including those in short columns, are sampled independently uniformly as in C5. Only the witness coefficient at the unused digit is fixed to zero.

The placement is injective, preserves coefficient Euclidean norm, and commutes with reduction and field scaling. The slot-zero form is $v_0$, and the other forms are exactly the coefficient list of the matrix product of the packed input. A form-kernel vector has $v_0=0$ and $A\hat v=0$. Thus the short multiple used by the reduction packs to a nonzero solution of the same norm to the uniform Module-SIS problem with dimensions $kd_R,\ell d_R$. For any fixed tag variant of an external witness, condition on all columns except column zero. Since its homogeneous coordinate is one, the independent uniform column zero adds a uniform coefficient vector to the remaining fixed vector. Consequently each form value is uniform on the affine space where the constant is one and every padding slot is zero. This distribution is sufficient for both the exact key-weight bound and the expected fallback bound.

## Amendment Bsearch

Use the independent box sampler on $N_\star=N+3$ coordinates and one extra independent box value $r_\diamond$, all uniform on $\{2,\ldots,g+1\}$. Set
\[
 r_0=A_0+r_\diamond-\lfloor{\tfrac12\sum_{i=1}^{N_\star}r_i}\rfloor,\qquad
 A_0=\lceil N_\star(g+1)/2\rceil .
\]
Given the box coordinates, the zeroth coordinate is uniform on a translate of $g$ integers, distinct modulo $q$. The public center for a Boolean vector $v$ with $v_0=1$ is
\[
 c_v=\lfloor A_0+\frac{g+3}{2}\bigl(1+{\rm wt}(v)-N_\star/2\bigr)\rfloor .
\]
If $X_i=r_i-(g+3)/2$, and $X_\diamond=r_\diamond-(g+3)/2$, then $r(v)-c_v=X_\diamond+\sum_i(v_i-1/2)X_i+E$, where the two rounding terms in $E$ have absolute sum at most $3/2$. The independent centered sum has variance $(g^2-1)(N_\star+4)/48$. Thus its full RMS is at most $g\sqrt{(N+7)/48}+3/2$ by the triangle inequality in quadratic mean. Each $|X_i|\le(g-1)/2$; the deterministic bound including rounding is at most $B=(N+4)(g+1)$. A centered difference of three tag coordinates or a single centered tag coordinate also lies in this range. This is the definition of $B_{\rm search}$. The protected check $2B+1<q$ gives unique valid bounded representatives for all the searches in the amended correctness algorithm.

The guessing probability of a rank-$d$ stack is still at most $g^{-d}$. For any prescribed joint fiber, pick a nonsingular $d$-column pivot minor of a basis of the row space. If the zeroth column is nonzero, it can be extended to a pivot basis by linear independence of the columns. Fix the remaining nonpivot box coordinates; any solution fixes the pivot box coordinates and the zeroth coordinate uniquely by the invertible linear system. The regular pivot box draws therefore have probability at most $g^{-(d-1)}$ of meeting their fixed values, and conditional on all box coordinates $r_0$ has probability at most $1/g$ of the required value. If the zeroth column is zero, no condition involves $r_0$, so fixing the other box coordinates directly bounds the pivot solution by $g^{-d}$. These probabilities hold for every fixed fiber and give the claimed bound. For a kernel vector the zeroth coefficient is zero, so its scalar guessing probability uses precisely the independent box coordinates, now on at most $N_\star$ positions. The inverse and regularization proofs apply in that dimension with the factors of I3 and $T_{\rm tr}$ stated next. All heavy-stack and generic ledger arguments therefore use the same guessing-probability implications. The actual arithmetic of the search is supplied in Amendment search_spread.

## Amendment C6

 Require $n=4332$, $\mathrm{seed\_mode}=1$, $\mathrm{seed\_degree}=2$, $q\equiv1\pmod4$, $q^2\equiv1\pmod3$, $q^2\equiv1\pmod{19}$, $2n\le D$, and $\Delta\ge n+3$. Let $K=\mathbb F_{q^2}$, $Q=q^2$ and $r_H=2166=2\cdot3\cdot19^2$.

 The scored branch fixes $s_0=2$ and $r_H=2166$. In the fixed precomputation, select a monic degree-$s_0$ polynomial $F$ by testing $X^{q^{s_0}}=X\bmod F$ and $\gcd(F,X^q-X)=1$. These tests characterize irreducibility since $s_0$ is prime: the first forces simple factors of degrees dividing $s_0$ and the second excludes degree one. Test $X^{2}+X+2$ first, then enumerate the other monic polynomials in residue order if needed. Irreducibles exist since $q^{s_0}-q$ elements of $\mathbb F_{q^{s_0}}$ have degree $s_0$.

In $K=\mathbb F_q[X]/(F)$, with $Q=q^{s_0}$, select a nonzero $c$ with $c^q\ne c$ and $c^{(Q-1)/l}\ne1$ for all primes $l\mid r_H$. Try $X+4$ first and then enumerate the other representatives. By cyclicity the order tests alone pass for a fraction $\prod_{l\mid r_H}(1-1/l)>1/4$ of $K^*$, and the degree test removes at most $q-1<(Q-1)/16$ elements. Thus selection terminates regardless of the first attempts. Let $P_c(Y)$ be the product of the conjugate linear factors of $c$ and set $P_T(T)=P_c(T^{r_H})$. All data selection is before runtime Setup; the construction below works for every accepted pair.

If $t^{r_H}=c$ then the orders satisfy $m_t/\gcd(m_t,r_H)=o(c)$, where $m_t$ is the order of $t$. The tests force $m_t=r_H o(c)$ prime by prime. For $p\mid r_H$, expanding the binomial shows $v_p(Q^j-1)=v_p(Q-1)+v_p(j)$: prime-to-$p$ powers preserve the valuation and one power by $p$ increases it by one. The even case uses $4\mid Q-1$. Thus $m_t\mid Q^j-1$ exactly when $r_H\mid j$. Every root has degree $r_H$ over $K$, and $t$ generates $K$ over $\mathbb F_q$ through $t^{r_H}=c$. Its minimal polynomial over the base is $P_T(T)=P_c(T^{r_H})$, where $P_c$ is the monic quadratic minimal polynomial of $c$. At $j=r_H/2$ we have $m_t/2\mid Q^j-1$ and $m_t\nmid Q^j-1$. Therefore $t^{q^{n/2}}=-t$ and the half-turn changes signs on exactly the odd monomials.

For Frobenius $\sigma^j$ the representative of $t^b$ is $c^{\lfloor bq^j/r_H\rfloor}T^{bq^j\bmod r_H}$, with its coefficient expanded in $1,c$ and $c$ replaced by $T^{r_H}$. This permutes residue classes and uses a two-by-two fixed block in each class. Compute the tables from the public field by modular exponentiation and reduction, in polynomial time, independently of the system and of encryption coins. The monomial basis has degree range $[0,n-1]$ and exactly the same three consecutive Frobenius identities and homogeneous coefficient as used in C7 and Targets.

## Amendment C7

Require $\mathrm{base\_degree}=\mathrm{base\_left}=\mathrm{base\_right}=\mathrm{scalar\_rel}=1$, $K_1,K_2\ge1$, and $2K_1K_2=n$. Require $a_0=\mathrm{mask\_stride}$ to be a positive integer dividing both $2K_2$ and $r_H=n/s_0$. Require $C_{\rm mask}=17n+2K_2-14-5(a_0-1)$. This is the one-variable grid. Write $e=A_H=B_H=1$ and $h=n$ when using field-degree notation. There are $A_c=3K_1K_2=3n/2$ cells, indexed by a left leg $a$ with $0\le a<K_1$ and a right leg $(b,\mathrm X)$, $0\le b<K_2$, $\mathrm X\in\{\mathrm E,\mathrm O,\mathrm V\}$. Write $p_X=\mathbf1_{\mathrm X=\mathrm O}$. Set $\lambda_a=2K_2a$, $k_{{\rm leg}}=2b+p_X$. Put $k_c=\lambda_a+k_{{\rm leg}}$. For E and O the cell weight is the coefficient of $T^{k_c}$ in $U=z(w)\sigma^{n/2-1}(z(w))$; for V use $V=z(w)\sigma^{n/2}(z(w))$. The half-turn fixes $V$ so only even powers occur there. For the appropriate parity $p_X$, divide $(k_c-p_X)/2$ by $K_2$. Its quotient $a$ and remainder $b$ recover the two digits and cover each slot exactly once. The key cell is $a=b=0,\mathrm X=\mathrm E$, with weight the constant coefficient of $U$.

### Factor masks and publication

Use the centered sampler in the internal dimension and the following independent scalar coins. The evaluation coin $\upsilon$ is uniform nonzero, the scalars $\pi,s_{\mathrm U},s_{\mathrm V},\zeta_0,\zeta_1,\zeta'',\eta_1,\eta_2,\eta_3,\Omega_{22},\alpha$ are independent uniform nonzero, $\Omega_{12}$ and the coordinates $y_i$ are independent uniform scalars, and $\tau$ is uniform off the evaluation points. Sample $\varepsilon$ uniformly from the field excluding $0,-1$. Let $F_x(T)$ be the reduced representative of $\sigma^{n/2+1}(T^x)$, computed by C6. Write $z_-,z_\circ,z_+$ for the reduced vectors of linear form coefficients at Frobenius powers $n/2-1,n/2,n/2+1$, respectively, evaluating at $\upsilon$ when used as scalars. Set
\[
 \pi_a=\pi(\upsilon^{\lambda_a}+\varepsilon F_{\lambda_a}(\upsilon)),\qquad
 s_{\rm leg}=s_{\mathrm X}\upsilon^{k_{\rm leg}},\qquad
 \gamma_c=\pi_a s_{\rm leg},\qquad
 \kappa=\gamma_{\rm key}L_\rho(\tau).
\]
Set $s_{\mathrm X}=s_{\mathrm U}$ on E and O and $s_{\mathrm X}=s_{\mathrm V}$ on V. For U legs the ordinary exponent $2b+p_{\mathrm X}$ determines the class by parity and then $b$. For U cells use quotient and remainder on division by $2K_2$ to also recover $a$. The independent V symbol distinguishes V, where the even remainder uniquely determines $b$. Therefore both families of Laurent-comparison monomials stay pairwise distinct. Here $\pi_0=\pi(1+\varepsilon)\ne0$, hence $\kappa\ne0$ on valid coins. On E/O use the right mask
\[
 \vartheta_{\rm leg}
 =\upsilon^{k_{\rm leg}}(\eta_1 z_\circ+\eta_2 z_+)
   -\varepsilon^{-1}F_{k_{\rm leg}}(\upsilon)(\eta_2 z_-+\eta_3 z_\circ),
\]
and on V use $\upsilon^{k_{\rm leg}}(\eta_3 z_+-\eta_1 z_-)$. For every input coordinate $i$ including tags, use the left row $\pi_a(y_i,A_i(\tau))$ and the right column $(s_{\rm leg}(r_i+A_i(\tau))+\vartheta_{{\rm leg},i}, s_{\rm leg}(B_i(\tau)-y_i))^\top$. Multiply each left row on the right by the hidden-basis matrix with rows $(1,\Omega_{12})$ and $(0,\Omega_{22})$, and each right column on the left by its inverse. Publish the resulting coordinate arrays in G1 and G2, respectively, the G2 search bases $[s_{\rm leg}]_2$, and the single G1 column $[\zeta'' y_i]_1$. There is one right sector and there are no alpha-scaled source-group inputs. Keep the public target-group element $[\alpha\kappa]_T$, with independent $\alpha$, and the seed and masked message. This slot preserves the protected overhead count. The decryption algorithm does not require this target-group input.

### Honest cancellation and the three field ties

For a stack form $W_U,W_V$ by summing cell matrices times $T^{k_c}$ in their weight families. Put $\widetilde W_U^+=\sum_{c\in C_U}W_c F_{\lambda_a}F_{k_{\rm leg}}$, whose image in the form field is $\sigma^{n/2+1}(W_U)$. At degree zero in $\varepsilon$ the three coefficients of the mask contribution, after taking out $\pi$ and the indicated independent $\eta$, are
\[
 t_1=W_Uz_\circ-W_Vz_-,\qquad
 t_2=W_Uz_+-\widetilde W_U^+z_-,\qquad
 t_3=W_Vz_+-\widetilde W_U^+z_\circ .
\]
Indeed the negative grade in the right E/O mask contributes degree zero exactly when multiplied by the twisted part of $\pi_a$; the ordinary products supply the remaining terms. With the honest weights and the form vectors contracted against $w$, each $t_i$ vanishes in the field: $U z_\circ=V z_-$, $U z_+=\sigma^{n/2+1}(U)z_-$, and $V z_+=\sigma^{n/2+1}(U)z_\circ$. The finite supports and group bases for these multiples are specified next.

In a formal identity, the Laurent comparison below isolates the same grade-zero polynomials for the actual stack up to multiples of $P_T$. Their reduction gives all three stated field ties. The right-leg type $s_{\mathrm X}$ and the ordinary exponent $k_c$ distinguish every cell in the generic comparison. The proof of the original rank-three classification using these ties follows. The new QAP point at $\rho$ changes only the corner used by the view and does not change the Booleanity or constraint tests used by that classification.

### Cancellation for the bounded seed modulus

The ordinary left powers are $2K_2a$, $0\le a<K_1$, and the ordinary right powers are $2b+p_{\mathrm X}$. Their sums give the distinct ordinary grid indices in the respective families. Every left exponent is a multiple of $a_0$. Its conjugated representative has terms in the prescribed residue class modulo $r_H$ from C6. Since $a_0\mid r_H$, that residue and every representative exponent are multiples of $a_0$. With representatives of degree below $n$, the largest possible such degree is $n-a_0$. Put $L_\sigma=n-a_0$, $R_\sigma=n-1$, and $Q_\sigma=L_\sigma+R_\sigma$ as bounds for the conjugated left, right and product terms. As $a_0\le2K_2\le40<n$, $Q_\sigma\ge n-1$. The degree of the first grade-zero tie polynomial is at most $2n-2$, and the degrees of the second and third are at most $Q_\sigma+n-1$. Since each tie vanishes modulo $P_T$, the quotient supports have lengths $n-1,Q_\sigma,Q_\sigma$ respectively. Use the basis exponents $(\pi\eta_i/\zeta'')P_T(\upsilon)\upsilon^a$ at consecutive indices starting at zero over each of those support lengths.

The three positive grades use a conjugated left digit, an ordinary right digit of degree at most $2K_2-1$, and a form of degree at most $n-1$. Their support lengths are $L_\sigma+2K_2+n-1,L_\sigma+2K_2+n-1,L_\sigma+2K_2+n-2$, using the even right digit in the V grade. Each negative grade uses an ordinary left digit of degree at most $n-2K_2$, a conjugated right digit and a form, so its support length is $2n-2K_2+R_\sigma$. The positive and negative bases have exponents $\pi\eta_i\varepsilon^{\pm1}\upsilon^a/\zeta''$ over those consecutive support lengths, with the grade fixed and the sign of the correction carried in the scalar coefficients. This follows by multiplying the terms of $\pi_a$ against those in the right masks: each right inverse-$\varepsilon$ term combines with the ordinary or twisted term on the left, and only the ordinary-right or V terms combine with the positive-$\varepsilon$ left term. The published bases evaluate all coefficients of each grade at $\upsilon$, so the cancellation MSM paired with the witness Y sum removes the entire honest mask. Summing these eight lengths at $L_\sigma=n-a_0,R_\sigma=n-1,Q_\sigma=2n-a_0-1$ gives exactly $17n+2K_2-14-5(a_0-1)$, as required by the amended rule. The uniform lengths can cover coefficients that vanish for particular choices or structured exponents; those coefficients are zero in the MSM, and all specified group bases are actually transmitted and counted.

These supports do not change the three ties checked by the view. At grade zero the jointly conjugated ordinary weight polynomial is the required Frobenius image modulo $P_T$ even when its ordinary degree is larger. Other Laurent comparisons still isolate each ordinary monomial $T^{k_c}$, whose cell indices are distinct by the original grid. In particular the support bound introduces no new weight family or hidden variable. Every published cancellation exponent has polynomial degree at most $3n-3$, since $L_\sigma,R_\sigma\le n-1$, $2K_2\le n$, and the original left-grid digits and the new finite $K_2$ guard give the displayed finite grade lengths at most $3n-2$. Monic reduction can be done in residue classes modulo $r_H$ by divisions by the bounded-degree seed polynomial. Each class has length at most a fixed multiple of $s_0$, and the cost of this reduction is $O(n)$ for $s_0\le128$. Assembling the weighted digit polynomials uses at most a constant times $s_0 n$ terms, since all factors for a single product lie in fixed residue classes and their product has at most $2s_0-1$ terms. The blocked FFT products use $O(n\log n)$ operations, leaving the claimed asymptotic decryption bound.

### Scored encryption arithmetic

This accounts for all arithmetic of the admitted finite mode. Write $S_{\rm nz}$ for the number of nonzero point coefficients traversed in preparing the QAP exponents, to which the benchmark assigns $2^{30}$. We show at most $S_{\rm nz}+3m$ variable scalar multiples in that cost convention.

At $\upsilon$ apply two sets of 2166 fixed blocks of side two from C6, with the residue class permutations. For a row $(a_0,a_1)$ on inputs $(x_0,x_1)$ use $(x_0+a_1)(x_1+a_0)-x_0x_1-a_0a_1$. The product $x_0x_1$ is shared and $a_0a_1$ precomputed, so a block uses three products. Both sets cost 12996 products and the half-turn uses signs. Form the two table values for the scaled forms
\[
 A'=\eta_3(\eta_1 z_\circ+\eta_2 z_+),\qquad
 B'=\eta_1(\eta_2 z_-+\eta_3 z_\circ).
\]
Precompute the three products of the two distinct $\eta$ scales that occur on the right. Thus evaluating the combined tables still uses at most four products per form coordinate. Their packed coefficient outputs have the same scales. Their difference $C'=A'-B'$ equals $\eta_2(\eta_3 z_+-\eta_1 z_-)$.

Use the invertible evaluation representation of the period coefficient ring from C5. For each of the two independent masks pull the row functional back through $E^{-1}$ using its transpose. After the pointwise products pull each accumulated column functional back through $E$ using its transpose. By C5 the row pullback costs $U_d=121$ products and the column pullback $V_d=121$. Therefore the total transformation cost is at most $2(U_d k+V_d(\ell+1))$.

For each evaluation root write the two transformed row-weight sequences as $A^{(1)},A^{(2)}$, and the uniform matrix column as $B$, all of length $k$. For a pair of consecutive indices $u,v$ add
\[
 (A^{(h)}_u+B_v)(A^{(h)}_v+B_u)
 - A^{(h)}_u A^{(h)}_v - B_u B_v
   = A^{(h)}_uB_u+A^{(h)}_vB_v,\quad h=1,2.
\]
Compute the sum of the row-only terms separately for the two rows and the sum of the column-only terms once per column, shared across the two outputs. The identity verifies both desired matrix products term by term. Every pair uses two main products and one column correction product. A final unpaired row needs two products per column. The two row corrections take $2\lfloor k/2\rfloor$ products per evaluation root. Hence the total cost of the products and both transforms is bounded by
\[
 W_{{\rm mat}}
 =d\big((\ell+1)(3\lfloor k/2\rfloor+2(k\bmod2))+2\lfloor k/2\rfloor\big)
       +2(U_d k+V_d(\ell+1))=W .
\]
The fields and independent ring entries are unchanged. The resulting two coefficient vectors are exactly $A',B'$, with their scaled slot-zero contributions computed from the same public table. Form $C'$ by subtraction. This uses no product per coordinate beyond the two separately charged matrix products.

Partition the QAP roots into the $N+5$ Booleanity and key singleton factors and $n_{\mathsf c}$ constraint cosets. Their vanishing factors at $\tau$ are respectively $\tau-p$ and $\tau^\nu-a^\nu$ for a coset represented by $a$. Compute $\tau^{2^j}$ for $1\le j\le11$ by successive squaring. On the list of $b=N+5+n_{\mathsf c}$ factor values, ordered with singletons first, use prefix and suffix products to get their product and their outer complements. Prefix values through the singleton group and the whole list give $Z_0(\tau)$ and $Z_*(\tau)$. A first value and an end complement can be copied without multiplying by one. The full prefix uses $b-1$ products, the suffix excluding its unused first product uses $b-2$, and the $b-2$ interior complement products supply the rest. At a coset node of size $2^j$, split it into its two child cosets of size $2^{j-1}$. Each child's vanishing evaluation is the precomputed power $\tau^{2^{j-1}}$ minus the respective public power of a representative. The two child complements are the outer complement at the parent times the sibling vanishing evaluation. With two products per internal node of a $\nu$-leaf tree, this provides all $Z_*(\tau)/(\tau-p)$ using $2(\nu-1)n_{\mathsf c}$ products after the outer pass. At $\rho$ the complement is $Z(\tau)$. The sum of all products is at most $3b-5+11+2(\nu-1)n_{\mathsf c}=2D+N+n_{\mathsf c}+11$, which fits the $2D+N+n_{\mathsf c}+16$ term. The public QAP coefficients at $p$ are encoded with the fixed multiplier $1/Z_*'(p)$. Multiplying an encoded point coefficient by its cofactor now makes the exact Lagrange contribution with one multiplication. The nine new Booleanity coefficients and the five entries at $\rho$ are covered by the sixteen-multiplication allowance below. All these scalars are over $\mathbb F_q$.

The G1 factor computations use at most $(2K_1+2)(N+4)$ products apart from the compiled per-leg scales. Compute the one shared expression $A_i+(\Omega_{12}/\Omega_{22})y_i$ per coordinate. The second left factor has this value multiplied by $\Omega_{22}\pi_a$, computed once per leg. Its expansion is exactly $\pi_a(\Omega_{12}y_i+\Omega_{22}A_i)$. The first factor and the Y column use their original single products. In G2 let $U_i=B_i(\tau)-y_i$ and $V_i=r_i+A_i(\tau)-(\Omega_{12}/\Omega_{22})U_i$. Compute $V'_{\rm U}=\eta_3 s_{\rm U} V+A'$ and $V'_{\rm V}=\eta_2 s_{\rm V} V+C'$. This costs three products per coordinate including the computation of $V$, since each scale is fixed throughout the coordinate vector and $C'=A'-B'$ is formed by subtraction. The first right factor on an E or O leg is $a'V'_{\rm U}+b'B'$ with $a'=\upsilon^{k_{\rm leg}}/\eta_3$ and $b'=-\varepsilon^{-1}F_{k_{\rm leg}}(\upsilon)/\eta_1$ precomputed. Its expansion in the unprimed quantities is the specified right exponent. Precompute the single shared product $V'_{\rm U}B'$ per input coordinate and one product $a'b'$ per E or O leg. The identity
\[
 a' V'_{\rm U}+b' B'=(V'_{\rm U}+b')(B'+a')-V'_{\rm U}B'-a'b'
\]
takes one remaining product per entry. For a V leg use one product $(\upsilon^{k_{\rm leg}}/\eta_2)V'_{\rm V}$, with its scale precomputed. The second factor on every leg is the original $(s_{\rm leg}/\Omega_{22})U$ and uses one product. All these calculations reproduce the original exponents over the given scalar coins; their case distinctions use only the public leg types. Thus the right work per coordinate, including three shared-vector products and the one product shared across E and O legs, is at most $6K_2+4$. The grouped count for both source groups is $(2K_1+6K_2+6)(N+4)$, plus the original precomputation of $2K_2$ pair products and the fixed table allowance for the new scales.

### Reused scale factors for the published source exponents

For the sparse powers of Amendment n1, start at the already sampled exponent $\zeta_0$. Compute $\tau^\nu$ by eleven squarings, including $\tau^2$. Advance the sparse base exponent by repeated multiplication by $\tau^\nu$. For each sparse entry also obtain the shifted entry with one multiplication by $\tau$. Together these use at most $2S_0-1$ further products. For the non-sparse list start at $\zeta_1\tau$. The gap between consecutive allowed exponents is one, except at a skipped multiple of $\nu$ where it is two. Multiply the current exponent by the already available $\tau$ or $\tau^2$ accordingly. At most $\Delta-\Delta/\nu$ further products therefore produce that list including its initial exponent. The total for both lists is at most $\Delta-\Delta/\nu+2S_0+16$. This produces the same scalar exponents with the scale factors retained throughout; each transmitted element still takes its own fixed-base generator multiplication. These recurrences also hold at $\tau=0$.

The key and non-key sparse right constants and the $J$ regular right constants are prepared once. Each associated right exponent multiplies its $\gamma_c$ by the respective constant, at one multiplication per slot. The search exponents are the precomputed leg scales. The mask power list uses the tabulated powers of $\upsilon$ multiplied by one constant for each grade and the appropriate monic-modulus factor in degree zero, with one multiplication per slot after combining these constants. The optional generator repeat adds no exponent work.


For the shared direction data of n1, obtain the three tag Lagrange values from the tag-three coordinate, from $A_1-c_*L_\rho$, and from $A_2-c_*L_\rho$. The key exponent formation already computes $L_\rho$. At $\tau$, compute the shared left scale $\zeta_0/U(\tau)$ using the inverse charged below. The array combines $S_j=A_j^{\rm o}+B_j^{\rm o}$ by an addition and inserts the single homogeneous correction before multiplying by that scale, for $N+1$ products. The five fixed quotients of n1 are formed directly using two products for each numerator at most, plus one scale product per entry and one product for each shifted copy; including the shared inverse scale takes at most 21 products. Compute the three linear factors and $U(\tau)$ with two products; the two extra right list constants each use multiplication by $U(\tau)/\zeta_0$. Including one more product for this shared scale, a product for $c_*L_\rho$, and fixed constants or copies, all these extra scalar computations fit the $(N+1)+100$ bound. The two new right lists use one product per entry after the common constants are prepared, included in the counted correction slots.

The fixed scalar tables cost at most $12996+60(n+J+1)$. The Frobenius blocks and scaled weight arrays use $12996+4n$ products, powers of $\upsilon$ at most $3n$, and left, right and cell scales at most $10(2K_1+3K_2+A_c)<35n$. Form $h=(\tau^\nu)^{\Delta/\nu}$ by binary powering in at most 508 products. Start at $Z_0(\tau)/\zeta_1$, advance $J-1$ times by $h$, and compute the two sparse constants with the cached inverse of $\zeta_0$. This uses at most $J+510\le2J+600$, also at $\tau=0$. Horner evaluation of the form modulus, four products per mask grade, and three products for the key through $L_\rho(\tau)$ and $\gamma_{\rm key}$ use at most $n+35<10(n+J+10)$. The compiled products cost at most $K_1+5K_2+12\le n$ for the two shared right scales, three weight scales, and the per-leg scales counted above. Tag work is counted separately. The total is at most $12996+53n+12J+700\le12996+60(n+J+1)$. Invert at most ten scale denominators, including the common $Z_*(\tau)$ and $U(\tau)$ when needed, within the separate 10,000-product allowance by binary exponentiation. The remaining table operations are additive.

The remaining finite scalar encryption terms sum to at most $V$ of C5. They include the cofactor products, shared mask forms, left and right factor products, scaled power recurrences, the $(J+3)A_c+C_{\rm mask}$ correction slots, the fixed table and inversion allowances, the bound $(N+1)+100$ for the shared tag directions, and the target exponentiations. Both target-group exponentiations use the same generator. Compute its multiples $2,\ldots,7$ with six successive products, and share that table. In each exponentiation scan 85 groups of three bits of its canonical 254-bit scalar, padding on the left. For every group use three squarings and at most one table product. Hence the two exponents and table use at most $6+2(85)(4)=686$ target-field products. At $276$ base-field products per product, proved in Amendment search_spread, this costs at most $189336$ products. The matrix bound includes both transforms, so there is no second conversion charge. The guard $W+V\le3m$ bounds the combined work throughout the admitted domain. Therefore the finite encryption uses at most $S_{\rm nz}+3m$ field products, and the independently charged fixed-base source-group operations are exactly the ones on the published exponents.

### Efficiency and asymptotic choices

The publication and operation counts are proved in n1, n2, and the count amendments. Each matrix entry uses one seed query. The at most eight tag variants share that matrix, and each algorithm uses at most one key query. Form applications cost $O(k(\ell+1)d_R\log(2d_R))$ per variant by C5. The mask calculations take $O(n\log n)$ after field setup, and n1 gives $O(D\log D+|S|)$ additional QAP work. The bounded ordinary and fallback searches have the expected cost proved in search_spread.

### Deterministic setup in the scored mode

The scored mode uses fixed public constants from its scheme description: the normalized interpolation kernels and their transposes in C5, $F,c,P_T$ and the two Frobenius tables in C6, and the designated subgroup roots. Their coefficients are determined by the finite formulas above, so they are read-only tables formed before any instance of Setup. In C6 the fixed tables are computed by reduction and linear algebra from the selected constants; the irreducibility and order checks certify constant data and are outside the runtime algorithm. Setup for a supplied $S$ selects this fixed mode and references its tables without generating a field or sampling any field-defining constant. It scans the nonzero term descriptions and performs the point encodings of D and the shifted table and vanishing-polynomial preparation of n1 with their stated subgroup transforms. Those instance-dependent operations take $O(|S|+D\log D+\log q)$ field work. The extra field tables are public, independent of $S$ and of the seed and all encryption coins. They have no ciphertext charge. The off-branch selector below uses the protected setup.

### Parameter selection and Corollary 5.8

The parameter selector dispatches on the public security level, domain and external shape. At the BN254 benchmark shape with $\lambda=100$, use the admitted parameters and constructions here in the protected subgroup placement. On every other input use the protected selector and its setup, encryption and decryption throughout, so the protected Corollary 5.8 applies with its original hypotheses to that branch.

The four bounds for linear-size systems with $N\ge\lambda^2$ in the designated subgroup placement are size $O(\lambda N)$ in field elements, encryption $O(\lambda^2 N/\log\lambda)$, decryption $O(\lambda N\log\lambda)$ apart from search, and expected search $O(2^{\lambda/4}N^{1/4})$ group operations. The amended branch has the single $(\lambda,N)=(100,391693)$. Its guards, array counts and operation ledgers give finite uniform bounds over the admitted parameters and placements. There are at most $1692(2\cdot2047+1)(391693+1)$ coefficients in the ordinary system description, so the bound holds even when zero coefficients are visited. Both search modes are capped by their proved ranges, which are at most $q$. Divide the four uniform bounds by the corresponding positive scales at this point and take the maxima with the original branch's constants. Targets proves correctness and extraction for every parameter set admitted by the amended rules independently of this dispatch.

### Algebraic and reduction interfaces

In `lem:moore`, the field has degree $n$ and $z$ plays no role in the statement. To derive the property at the amended degree, if a combination of $d$ successive Frobenius columns is zero then a polynomial $\sum_{j=0}^{d-1}a_j X^{q^j}$ vanishes at the entries of $\sigma^s(h)$. Its roots are closed under $\mathbb{F}_q$-linear combinations, and the independent entries give $q^d$ distinct roots. If any coefficient is nonzero, its degree is at most $q^{d-1}$, a contradiction. This proof uses only the field and its Frobenius.

Here is the full classification argument for the actual field ties of Amendment C7 with the specified $z$. Let $W_c$ be symmetric, pass the Booleanity tests, and satisfy the original three ties, with row space $\mathcal V$ of dimension $d\le3$ containing no kernel vector. The zero-dimensional case has zero stack. Let the columns of $U_*$ over $\mathbb F_q$ be a basis of $\mathcal V$, with rows $u_i^\top$. These rows span $\mathbb F_q^d$. For $s$ in $\mathcal I_*=\{n/2-1,n/2,n/2+1\}$, put $h_s=U_*^\top\sigma^s(z)$, and put $h_0=U_*^\top z$. Injectivity of $z$ on $\mathcal V$ means the entries of $h_0$ are independent over $\mathbb F_q$. In particular $d\le n$, and the Moore property proved above gives that the three $h_s$ span over $\mathbb F_{q^n}$. Write $W_s$ for $W_U,W_V,\sigma^{n/2+1}(W_U)$ in the indicated order. Each $W_s$ has its rows and columns in the extension of $\mathcal V$, so $W_s=U_* X_s U_*^\top$ for a unique symmetric $X_s$. Indeed a left inverse $L_*$ of $U_*$ exists, and $X_s=L_*W_sL_*^\top$; projections back to $\mathcal V$ act identically on the columns and rows. The ties give $X_s h_{s'}=X_{s'}h_s$. If $\sum_s a_sh_s=0$, then $(\sum_s a_sX_s)h_{s'}=0$ for every $s'$, and spanning gives $\sum_s a_sX_s=0$. Thus there is a linear map $X$ with $X(h_s)=X_s$. The trilinear form $C(h,u,v)=u^\top X(h)v$ is symmetric in the last two slots and in the first and last slots by the ties, initially on spanning $h_s$ and then on all vectors by linearity. It is therefore fully symmetric. Each Booleanity test gives $C(h,u_i,u_i-u_0)=0$ on the spanning $h_s$, hence on all $h$. The identities $X_s=\sigma^s(X_{n-s})$ for $s=n/2-1,n/2$ follow from the relation between the first and third matrices and because $W_V$ has even $T$-degrees and $\sigma^{n/2}$ fixes the scalar coefficients, as $U_*$ and $L_*$ have field entries fixed by $\sigma$.

First suppose $u_0\ne0$. Extend $l_0=u_0$ to a basis $l_0,\ldots,l_{d-1}$ chosen from the rows. For each $\delta\in\{0,1\}^{d-1}$, let $p_\delta$ satisfy $l_0^\top p_\delta=1$, $l_j^\top p_\delta=\delta_j$ for $j>0$, and set $w_\delta=U_*p_\delta$. Symmetry lets any repeated positive index in $C(l_i,l_j,l_k)$ be reduced via the test replacing one occurrence by $0$. Hence those values depend only on the set of positive indices present. Conversely the cube of the linear functional $p_\delta$ takes the value $\prod_{i\in A}\delta_i$ for this set $A$, and all sets occur since $d-1\le2$. The matrix of these values indexed by $A,\delta$ is invertible: indexing $\delta$ by its support gives the subset-incidence matrix, triangular with diagonal 1 in any inclusion-compatible ordering. Therefore
\[
 X(h)=\sum_\delta c_\delta(h^\top p_\delta)p_\delta p_\delta^\top
\]
for coefficients in the extension field. The squares $p_\delta p_\delta^\top$ are independent by the same evaluation matrix, now on pairs of basis vectors since $d-1\le2$. Write $z_\delta=z(w_\delta)=h_0^\top p_\delta\ne0$. Comparing coefficients of the squares in $X_s=\sigma^s(X_{n-s})$ gives $c_\delta\sigma^s(z_\delta)=\sigma^s(c_\delta)z_\delta$ for the two consecutive $s$. Hence $c_\delta/z_\delta$ is fixed by $\sigma$ and belongs to $\mathbb F_q$, as the fixed points of $x\mapsto x^q$ are exactly this field. Write it as $\chi_\delta$. Returning from the matrix restriction gives $W_s=\sum_\delta\chi_\delta z_\delta\sigma^s(z_\delta)w_\delta w_\delta^\top$. In particular the first two polynomial representatives give the stack $\sum_\delta\chi_\delta\mathbf H(w_\delta)$.

Let $f$ be any field-linear test that vanishes on the cells. It vanishes on the $W_s$. Put $Q_*=\sum_\delta\chi_\delta f(w_\delta w_\delta^\top)p_\delta p_\delta^\top$, a matrix over $\mathbb F_q$. The vanishing gives $h_0^\top Q_* h_s=0$ for all three $s$, hence $h_0^\top Q_*=0$. Independence of the entries of $h_0$ over $\mathbb F_q$ implies $Q_*=0$, so independence of the squares implies $\chi_\delta f(w_\delta w_\delta^\top)=0$ for every $\delta$. Apply this to all Booleanity tests to deduce that any nonzero coefficient is on a Boolean assignment. If every external constraint test passes, apply the same argument to them to see that each supported assignment is a witness. In any representation by honest stacks of Boolean assignments in $\mathcal V$, the assignments equal some $w_\delta$ because their evaluations on the chosen basis fix their $p_\delta$. Hence the same test argument applies to any such representation.

If $u_0=0$, take any basis $l_1,\ldots,l_d$ from the other rows. Booleanity implies $C(h,l_i,l_i)=0$, so by symmetry every coordinate of the trilinear form with a repeated index vanishes. This gives zero if $d<3$. For $d=3$ its only possible value on distinct indices is a shared scalar $c$. Evaluating $X_s=\sigma^s(X_{n-s})$ on pairs of different basis vectors gives $c  h_s=\sigma^s(c)h_0$ in the basis $l_1,l_2,l_3$, since $h_s$ is obtained from $h_0$ by Frobenius and the basis is over $\mathbb F_q$. If $c\ne0$, the first two consecutive vectors $h_s$ would both be proportional to $h_0$, impossible by the Moore independence of the three vectors in dimension three. So again $X=0$, and the stack vanishes. This proves the classification clauses, including that a nonzero usable stack in the stated case has a witness in its row space.

The rank and inverse clauses of $\mathrm{lem:heavy}$ are proved in Amendment msis_bound. For the packing clause, write $x\bmod q=a v$, $a\ne0$, for the kernel vector $v$. In either shortness convention $x_0=0$ since $v_0=0$ and $|x_0|<q$. Packing copies each of the $N_\star$ coordinates once and inserts zeros. It commutes with reduction, so $A\hat x=aA\hat v=0\bmod q$. For every infinity-short $x$ this gives $0<\|\hat x\|_\infty=\|x\|_\infty\le\beta$. For every Euclidean-short $x$ it gives $0<\|\hat x\|_2=\|x\|_2\le B_{\rm E}$. Only the second problem is costed.

### Degree, view and recovery gradients

Fix the seeded matrix and hence the form coefficients. For source exponents $a$ in G1 and $b$ in G2 include their generators. A guess-free target expression is
\[
 \mathsf E=\sum_{a,b}D_{ab} a b+D_K\alpha\kappa .
\]
The coefficients are fixed scalars. No source exponent uses $\alpha$. The factor $\varpi=\Omega_{22}\zeta_0\zeta_1\zeta''\varepsilon$ clears all denominators in every paired product. For degree accounting put $e_*=1$, since C6 admits the bounded seed branch. The degree of $\pi_a$ is at most $n+e_*$: the ordinary and conjugated left degrees are each at most $n-1$ and the two independent scalar factors are $\pi,\varepsilon$. The QAP factors have degree below $D$, and the hidden-basis matrix supplies at most one further factor. The sparse and shifted G1 powers have degree at most $D$ including scale, and the Y exponent has degree two. The fixed degree bound for G1 is therefore $d_1=D+n+2+e_*$. The degree of $\gamma_c$ is at most $n+2+2K_2$, since the right scale has ordinary degree at most $2K_2-1$ plus its one independent scalar. The key scale still has degree three.

The cleared sparse correction bases, including the new right entries of polynomial degree at most $D+2$, have degree at most $D+n+8+2e_*K_2$, which is at most the combined-list bound below since $D\ge4$. For non-sparse ones the polynomial part has degree at most $2D-2$ from P1, and the cell scale and remaining clearing factors give at most $2D+n+4+2e_*K_2$. The first and second right coordinates before the masks have degree at most $D+n+6+2e_*K_2$ after clearing, by $k_{\rm leg}\le n-1$, the degree below $D$ of the QAP polynomials and the linear hidden-basis inverse. Each term of a right mask is a leg power of degree at most $n-1$ times a form of degree at most $n-1$, with one $\eta$ and an optional inverse $\varepsilon$. It has cleared degree at most $2n+5$. A cancellation basis has monomial degree at most $3n-3$ and cleared degree at most $3n+4$, including its scalar factors and clearing factors. Search bases have cleared degree at most $n+5$. Since $2n\le D$, all G2 exponents after clearing fit $d_2=2D+n+6+2e_*K_2$. The cleared key terms fit $D+8$. The product degree before a guessed-operand factor is at most $d_1+d_2=3D+2n+8+e_*(2K_2+1)$. By C5, $K_1\ge K_2+1$. Thus this bound is at most $d_f=3D+2n+2K_1+7$. The extra guess factor of degree one and all listed separate bounds fit $(q-D)\varepsilon_f$ by its protected formula. The search coordinates enter only linearly, within the same degree bounds.

For any fixed $r$, the valid scalar coin sets are independent with sizes at least $q-D$, including the two exclusions on $\varepsilon$ and the $D$ exclusions on $\tau$. The clearing factor is nonzero there. The product-set bound proved in Targets shows that an identity holding on all valid coins is a polynomial identity after clearing, because $d_f<q-D$ by P5 and $\varepsilon_f=(d_f+60)/(q-D)$. A nonidentity has coincidence probability at most $d_f/(q-D)\le\varepsilon_f$. At an identity $\mathsf E=\chi\kappa$ the coefficient of $\alpha$ gives $D_K=0$, since $\kappa$ is a nonzero polynomial. All stack comparisons henceforth use only the plain factor sector.

Write the two transformed left exponents as $F_1^{a,i}=\pi_a y_i$ and $F_2^{a,i}=\pi_a(\Omega_{12}y_i+\Omega_{22}A_i)$. The right exponents are
\[
 H_1^{{\rm leg},j}=\ell_{{\rm leg},j}
       -(\Omega_{12}/\Omega_{22})s_{\rm leg}(B_j-y_j),\qquad
 H_2^{{\rm leg},j}=s_{\rm leg}(B_j-y_j)/\Omega_{22},
\]
where $\ell_{{\rm leg},j}=s_{\rm leg}(r_j+A_j)+\vartheta_{{\rm leg},j}$ is independent of the hidden basis. No other G2 input contains a hidden-basis variable. For any G1 input $a$ denote its evaluation at $\Omega_{22}=0$ by $\widetilde a$; for $F_2^{a,i}$ this is $\Omega_{12}F_1^{a,i}$. Take the part of the Laurent identity with $\Omega_{22}^{-1}$ and positive degree in $\Omega_{12}$. Cancel its common factor $-\Omega_{12}/\Omega_{22}$. The resulting identity is
\[
 \sum_{a,{\rm leg},j}\delta_{a,{\rm leg},j} \widetilde a s_{\rm leg}(B_j-y_j)=0,
\]
where $\delta_{a,{\rm leg},j}$ is the coefficient of the pair with $H_1^{{\rm leg},j}$, subtracting the matched coefficient of $F_2^{a,i},H_2^{{\rm leg},j}$ if its G1 input is $F_1^{a,i}$. This follows because only a second left coordinate produces a positive $\Omega_{12}$-degree when paired with $H_2$. Substitute $y_i=B_i(\tau)+z_i$ with independent indeterminates $z_i$. Then $B_j-y_j=-z_j$, so the coefficient of $z_{j_0}$ is $-\sum_{a,{\rm leg}}\delta_{a,{\rm leg},j_0}s_{\rm leg}\widetilde a(B)$ and is zero. Any $z_i$ term of $\widetilde a(B+z)$ contributes degree two, hence cannot enter. The fixed index is $j_0$; no factor $B_{j_0}$ remains.

The left-input types in the sum are $1,\zeta_0 p(\tau),\zeta_1\tau^v,\zeta''B_i,\pi_a B_i,\Omega_{12}\pi_a B_i$, separated by degrees in $\zeta_0,\zeta_1,\zeta'',\pi,\Omega_{12}$. The polynomials $p$ include the sparse powers and the new quotient difference polynomials. In the first four types the monomials $s_{\rm leg}=s_{\mathrm X}\upsilon^{k_{\rm leg}}$ distinguish the legs in each kind. The $\zeta_1$ powers are distinct and the $B_i$ are independent by their $d_j$ values. The polynomials in the $\zeta_0$ type need not be independent: the identity says for each leg and right coordinate $j_0$ their coefficient-weighted sum is the zero polynomial in $\tau$. In this type each $\widetilde a$ is the full first input independent of $y$ and the hidden basis, so its aggregate ordinary pairing with that $H_1^{{\rm leg},j_0}$ vanishes at every coin and every $r$. For the last two types use the constant term in $\varepsilon$, giving the distinct cell monomials $\pi s_{\mathrm X}\upsilon^{k_c}$. For each of their coefficients and each $j_0$, the relation is linear in $B_i(\tau)$; evaluating the polynomial relation at $d_i$ isolates its $i$-th coefficient by Amendment D. Thus the matched factor coefficients agree individually and all unmatched first-right terms cancel identically as sums, which is sufficient both for the class comparison and the derivative. Formal projection onto first-left factors continues to respect formal equality and receives no contribution from the $\zeta_0$ type.

In the multidegree with one $\pi$ and zero degrees in $\zeta_0,\zeta_1,\zeta''$ and net hidden-basis degree, the pairs are the matched factor products, first-left pairs with the search bases and generator, the correction lists in two matching inverse-scale classes, and the Y column with cancellation bases. This enumeration follows by checking the degrees of the published exponents: the left first factors have one $\pi$, the left second also has one hidden-basis degree, and the three other nonconstant left types carry only one of the three scales. The right factor scales and correction types above are their only complementary types. The left-generator pair with any published right exponent of degree one in $\pi$ has an inverse scale and cannot enter this class. Define $W_c$ by matched factor coefficients, and $u_c$ by minus the first-left search-pair coefficients. The class identity is
\[
 \sum_c\gamma_c b_c+\Phi_*=\chi\kappa,\qquad
 b_c=y^\top(W_cr-u_c)+y^\top(W_c-W_c^\top)A(\tau)
              +(P_{W_c}+Z_c h_c+Z_0 R_c)(\tau).
\]
Here the two correction types produce $Z_c h_c+Z_0R_c$ with allowed $R_c$, by the residue-preserving monic division proved in n1. The term $\Phi_*$ collects the masks from the factor products, the Y cancellation products and the first-left generator pairs. It is free of all $s_{\mathrm X}$. Taking the constant term in $\varepsilon$ and the coefficients of the distinct $\pi s_{\mathrm X}\upsilon^{k_c}$ gives $b_c=0$ except at the key cell, where $b_c=\chi L_\rho$. The original identity then also gives $\Phi_*=0$.

For each $c$, the linear coefficient in $y$ at $d_0$ gives $W_c r=u_c$. The same comparison at $\rho,d_i$ shows $W_c-W_c^\top$ vanishes on the spanning vectors in Amendment D, hence $W_c$ is symmetric. The constant coefficient gives $\deg Z_c h_c\le2D-2$ since the $P_{W_c},Z_0R_c,L_\rho$ terms have that bound. Thus $\deg h_c<D$ for a non-key cell or $<D-1$ in the key cell. The QAP identities in Amendment D give all Booleanity and constraint tests, with the ordinary or keyed vanishing factor as applicable. In particular the Booleanity tests follow first by checking the $d_i$, where the key polynomial is zero. In the key cell evaluate then at $\rho$ where the two vanishing factors are zero. The Booleanity equalities reduce $P_{W_c}(\rho)$ to $(W_c)_{\mathsf b_1,\mathsf b_2}$ in the new key evaluation. Therefore $(W_c)_{\mathsf b_1,\mathsf b_2}=\chi$. In the coefficient of each $\eta_i$ in $\Phi_*$ at degree zero in $\varepsilon$, the mask part is $\pi y^\top t_i(\upsilon)$. The remaining terms there are the Y pairs with multiples of $P_T(\upsilon)$; the other grades and generator pairs do not contribute. Comparing the $y_j$ coefficients and substituting the form generator for $\upsilon$ therefore gives all three actual ties from the honest cancellation derivation.

If $r'$ replaces $r$, the coefficient-matching result shows the difference in the target value is $\sum_c\gamma_c y^\top W_c(r'-r)$, because no other exponents depend on $r$. Thus the identity remains valid throughout its prescribed locus. If all stacks are zero, it holds formally at every $r'$ and the key corner forces $\chi=0$. If an identity is formal for all $r$, its equations $W_c r=u_c$ for every $r$ force all $W_c=0$ and again $\chi=0$. A difference of source expressions pairs with the other source generator to an expression of zero stack. If it vanishes identically at any fixed $r$, this argument says it is formally zero, so formally different source expressions have the stated coincidence bound. This proves the view clauses with the new corner and one actual sector.

The formal derivative of the target expression with respect to the search coordinates, for a marked identity, is the vector $\sum_c\gamma_c W_c^\top y$. To compute it use the private evaluation and reverse accumulation of the reduction. At each recovery point project the G1 input polynomials by setting $\Omega_{12}=\Omega_{22}=0$ and taking the part linear in $\pi$; these are exactly the first left coordinates. This is a linear projection and therefore respects formal equality of G1 expressions. The derivative of a G2 leaf is nonzero only for a first right coordinate and is $s_{\rm leg}$ times the respective coordinate vector. The matched $F_1,H_1$ coefficients are precisely the coefficients of the projected product in the derivative. Since unmatched first-right coefficients vanish for a marked identity, this is its full stack gradient. Formally equal targets have zero difference stack and the same gradients; formally equal G2 inputs also have equal derivative records by pairing their difference with a first-left input and applying the zero-stack result. The projected gradients always lie in the marked row space. For a nonzero linear functional on it that vanishes on a given proper subspace, the derivative polynomial after dividing by $\pi$ is nonzero: take its degree-zero coefficient in $\varepsilon$ and the distinct monomials $s_{\mathrm X}\upsilon^{k_c}y_i$. Its degree is at most $n+2+2K_2$, establishing the recovery comparison used in Targets. The optional empty alpha sector has identically zero stack and gradients.

The running time with the revised exponent lists has the bound
\[
 t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT},\qquad
 C_R=8I+3L+2C_{\rm post}+C_{\rm set}+C_{\rm desc},
\]
with $I$ for computing the initial exponents at one point, $C_{\rm post}$ for processing one tried expression, $C_{\rm set}$ for fixed transcript initialization, and $C_{\rm desc}$ for the description. Here $I,C_{\rm post},C_{\rm set},C_{\rm desc}$ are the costs for the revised exponent lists, and $C_R=O((N_\star+n)D+\mu)$. We give the dependence on the form indices explicitly.

The per-call bound can be checked by the following implementation in the reduction's unit-operation model. Keep per group a table of assigned exponents indexed both by label and by field value, and a label table status for excluded strings. Both allocated and excluded strings are keys of the same label table, so unused-string sampling excludes both. A label record includes its value at the independent test point and a reference to its first expression node, if any. The reference or zero record is kept on repeated assignments. For an unclassified operand in an addition, scalar product or pairing, keep counters of the remaining exponents and unclassified strings in its group. Draw an integer uniformly below the latter count and compare it to the former count to decide membership. If it is a label, sample a uniformly unused exponent. Insert the relevant forward and reverse entries and update the counts. A rejection only writes its status and updates the unclassified-string count. This gives at most eight operations per unclassified operand: one status lookup, one integer sample and comparison, one exponent sample, two insertions and two counter updates. The conditional laws follow from a uniform injection after the already assigned and excluded labels have been fixed. Record-less labels in answered calls use the common zero expression, at most two further record writes per call.

For a result, allow at most 24 main operations. This includes two lookups of operands and up to three arithmetic operations each at the true and private test points. A result-label lookup, a fresh unused string sample when needed, and the two table insertions use at most four more. Updating both counts uses two. Allow six writes for an expression node (operation tag, operand references, scalar operands if needed, and result reference). The remaining four cover the private-value comparison, recording the first differing target pair, advancing the expression-log index, and checking or recording eligibility for name calls. A name call uses the same routine for negation, and then returns the two labels, with at most two label writes. It is rejected if the input's eligibility flag is absent. Repeated name calls return the already assigned opposite exponent label. An insertion at a known exponent leaves the old reverse entry in place and the private comparison uses its stored record.

For the at most six recovery passes, the forward evaluation at each point takes at most three arithmetic operations per logged gate. The private test point above uses the full exponents. At recovery points, the projected first-left values and the single-sector first-right derivative leaves are prepared before the call loop as described above. Only the right operand of a pairing can contribute a derivative in $r$, as every G1 value is independent of $r$. For each of the at most two trial expressions, traverse the resulting straight-line expression log backwards. A sum or scalar multiplication adds the adjoint times the respective scalar derivative to the adjoint of each predecessor. A pairing uses the evaluated first operand as its derivative with respect to the second. For a predecessor that is an input leaf, skip it if its derivative is zero in the current sector. Otherwise it is a first right coordinate with derivative equal to one prepared field scalar times the coordinate vector for its index $j$; directly accumulate the adjoint contribution times this scalar in coordinate $j$ of the gradient. This is at most three field operations for each of two precursors: a product by the gate derivative, an additional product for a leaf, and an accumulation. A non-leaf involves just the first product and accumulation. The references in the stored log give direct accesses to indexed registers, and each field operation computes its result in its destination register. Neither uses a label-table lookup. Initialize all node adjoint registers to zero before each reverse pass, using one field write per node and pass, then set the starting adjoints for the trial. These updates compute the derivatives by the chain rule in reverse order. Each recovery point therefore costs at most $3+2(6+1)=17$ operations per call for both expression trials. Initializing the output vectors and the at most two starting adjoints per trial is fixed postprocessing. Including six passes, the call bound is at most $24+2\cdot 8+2+2+6\cdot17=146\le148$. A fresh key-oracle answer takes one lookup, sample and insertion. A fresh seed-oracle answer replaces its one sample by $d_R$ coordinate samples. This gives $(d_R+5)Q_H$ when each oracle has at most $Q_H$ queries.

Only fixed inputs and setup change. Computing the initial exponents at each of at most eight points evaluates $O(N_\star)$ degree-below-$D$ QAP polynomials, advances powers through lengths $O(D+n)$, and forms the $O(nD)$ scalars in the split QAP group arrays. For the mask vectors, naive transposed ring multiplication takes $O(nd_R+nN_\star)$ work, bounded by $O(nD+nN_\star)$ since $d_R\le n\le D$. Source factor entries take $O(nN_\star)$ further operations. For postprocessing, apply the full form map to at most three vectors per sector by naive ring multiplication and solve a fixed-width linear system. The same $O(nD+nN_\star)$ bound covers this before LIFT. Initialization queries and stores the same ring entries and creates the group label records with at most $O((N_\star+n)D+\mu)$ operations, including masking. The fixed instance QAP polynomials and form indices fit the same size as advice in the protected cost model. Hence $C_R=O((N_\star+n)D+\mu)$. The lifting step is called at most twice, once per tried expression. This establishes the bound above and the stated $t+O(Q+d_R Q_H+\mu)+{\rm poly}(D,\log q)$ specialization.

This accounts for the background list for the forms and weights block. The generic record and mark bounds depend on the degree, view, sampler and label counts. The degree and view properties needed for the repacked construction are proved above. The extractor sketches only use the coefficient arrays of the left and right factors, independently of the internal representation of the form list.


## Amendment P1

Put $U_*=(D-1)+\nu n_{\mathsf c}$, the length of the combined polynomial interval. Require $\Delta\le D$, $J=\lceil U_*/\Delta\rceil$, $J'=1$, $\nu\mid\Delta$, and $n\le D$. The displayed chunks contain all the merged non-sparse correction coefficients of n1. Their absolute shifts are multiples of $\nu$, and $(J-1)\Delta<U_*$. In each G2 shifted base the multiplier $Z_0$ has degree $N_\star+2=D-\nu n_{\mathsf c}$, so its polynomial part has degree at most $N_\star+2+U_*-1=2D-2$. The degree proof in C7 includes the scalar factors and validates the original comparison bound. Monic division in the polynomial view gives the same allowed remainders and the same bounded quotient criterion at every cell. All other setup and sampler premises are evaluated with the amended $D$ and $B_{\rm search}$ and use their stated bounds.

## Amendment n1

There are
\[
 n_1=(2K_1+1)(N+4)+2\lceil(D-1)/\nu\rceil+\Delta-\Delta/\nu+(N+1)+10
\]
transmitted G1 elements. Use the single factor sector, field mask bases and Y column of C7. Let $S_0=\lceil(D-1)/\nu\rceil$ and
\[
 I_0=\{0\le a<D-1:\nu\mid a\},\qquad
 I_0^*=I_0\cup\{a+1:a\in I_0\},\qquad
 I_1=\{0\le a<\Delta:\nu\nmid a\}.
\]
Send $P_a^0=[\zeta_0\tau^a]_1$ for $a\in I_0^*$, and $P_a^1=[\zeta_1\tau^a]_1$ for $a\in I_1$. There are $2S_0$ sparse entries because $\nu\ge2$, and $\Delta-\Delta/\nu$ non-sparse ones by alignment. Use $Z_c=Z_*$ in the key cell and $Z_c=Z$ elsewhere. Send one $B_c^0=[\gamma_c Z_c(\tau)/\zeta_0]_2$ per cell and $J$ bases $B_{c,j}^1=[\gamma_c Z_0(\tau)\tau^{j\Delta}/\zeta_1]_2$, $0\le j<J$. The factor arrays, search bases and cancellation arrays are those of C7, each once. Add the tag quotient difference bases below and then apply the same optional existing-generator parity padding, computed as one scalar multiplication by one. Send the seed, the one element $[\alpha\kappa]_T$, and the masked message. There is exactly one fixed-base generator multiplication per transmitted group slot and one more in GT for the key. All scalar exponents use the displayed fixed factors and tabulated powers, with constant work per exponent.


### One common left array for the internal tag directions

Write $d_1',d_2',d_3'$ for the three tag Booleanity points, $L_1,L_2,L_3$ for their QAP Lagrange polynomials, and $A_i,B_i$ for the coordinate polynomials of tag $i$. The new key evaluation gives
\[
 A_i=B_i=L_i+c_*L_\rho \quad(i=1,2),\quad A_3=B_3=L_3 .
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
Each numerator vanishes at all QAP points: $A_i$ has nonzero point values only at its own tag point and $\rho$, and $L_{3-i}$ only at the other tag point; two distinct tag coordinate polynomials overlap only for tags one and two at $\rho$, where the product with factor two is $2c_*^2=1$. The degrees of these quotients are at most $D-2$. Send the $N+1$ values $[\zeta_0 G_j(\tau)]_1$, and for each of the five $F$'s send $[\zeta_0 F(\tau)]_1$ and $[\zeta_0(\tau-\rho)F(\tau)]_1$. There are $N+1+10$ left entries. For every cell $c$, send two right entries
\[
 B^{(i)}_c=[\gamma_c U(\tau)A_i(\tau)/\zeta_0]_2,\quad i=1,2 .
\]
Their generation uses the scalar evaluations and the schedule in C7.

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
Compute the one ordinary witness sum $[\zeta_0 G_w(\tau)]_1$ once. For each full variant, use the paired weighted right entries $B^{(i)}_c$ for the present bits. For each present bit do the MSM of length $A_c$, then when both are present add the two MSM outputs before pairing with the same left witness sum. The polynomial multiplier for cell $c$ is precisely $\gamma_c U(b_1A_1+b_2A_2)G_w$. If both bits are zero, this pairing is omitted. For the fixed part add $[\zeta_0F_v(\tau)]_1$ to the sparse key operand and $[\zeta_0(\tau-\rho)F_v(\tau)]_1$ to the sparse non-key operand, using the two sets of fixed left entries. The two resulting sparse pairings incorporate $\gamma_c Z_*F_v$ for their respective cells because $Z_*=(X-\rho)Z$. The non-key sparse operand still receives $d_vP_0^0/Z(\rho)$ separately. Combining these contributions with the baseline sparse and nonsparse operands subtracts $P_v-d_vL_\rho$ in the key cell and $P_v$ elsewhere.

In the hidden-basis comparison, the new left inputs are polynomials of the existing $\zeta_0$ type. The two new right lists are of inverse scale $\zeta_0^{-1}$, with $\gamma_c$ and a polynomial multiple of $Z_*$ and with no other variables. Their pairs with any left input of scale $\zeta_0$ yield multiples of $Z_*$, and pairs of old sparse right inputs with new left inputs yield multiples of $Z_c$. The generic comparison therefore absorbs the entire enlarged class into $Z_c h_c$, with the same residue restrictions on the other class. The constant-polynomial coefficient bounds the final quotient as in C7. All new left exponents have total degree at most $D$, and the new right list degree is covered explicitly in C7. The shared third-tag selection changes neither exponents nor coin laws.

### A single combination at any tag

For $v_0=(w,0,0,t)$ the key corner is zero. By Amendment D, $G_{\rm base}=P_{v_0}/Z_0$ is exact and equals $Z_{\mathcal K}h_{\rm key}^{v_0}+R_w$. Compute its sparse part by retaining the multiples of $\nu$, and divide that part by $Z_{\mathcal K}$ in the variable $X^\nu$ to obtain $h^0$, the sparse part of $h_{\rm key}^{v_0}$. The complementary part $T_0=G_{\rm base}-Z_{\mathcal K}h^0$ has degree below $U_*$ and is formed by deleting sparse coefficients of $G_{\rm base}$, so every retained exponent is nonzero modulo $\nu$. Polynomial products and monic divisions here take $O(D\log D)$ field operations: after reversal a monic divisor has constant term one, and the update $u\leftarrow u(2-fu)$ doubles the correct inverse precision since its residual equals $(1-fu)^2$. For each precision, products use the C3 power-of-two subgroup and split lengths $O(D)$ into a bounded number of blocks of length at most half the subgroup order. The sum over the doubling precisions is $O(D\log D)$. Only the witness polynomials are interpolated and the compressed sparse division has length $O(D/\nu)$.

Once compute
\[
 H^0=\sum_{a\in I_0}[X^a]h^0 P_a^0,\qquad
 H_{\rm oth}^0=\sum_{a\in I_0}[X^a]h^0 P_{a+1}^0-\rho H^0,\qquad
 H_j^1=\sum_{\substack{a\in I_1\\j\Delta+a<U_*}}[X^{j\Delta+a}]T_0 P_a^1 .
\]
For each full combination adjust the first operand by the fixed key-tag terms and pair with $\xi_{\rm key}(v)B^0_{\rm key}$. Adjust the second by the shifted fixed tag terms and $d_vP_0^0/Z(\rho)$ before pairing with the weighted non-key $B^0_c$, and pair each $H_j^1$ with the $v$-weighted $B^1_{c,j}$ sum. Also subtract the shared direction pairing when a first or second tag bit is present, as above. The polynomial argument in the preceding subsection shows these subtractions remove exactly the $P_v-d_vL_\rho$ and $P_v$ terms for the key and other cells, respectively.

For each right leg, form the two weighted left operands by summing $\xi_c(v)$ times the witness-summed G1 factor of its left leg over the cells at this right leg. Pair them with the two witness-summed right coordinates. In the resulting sum the hidden basis cancels, the two antisymmetric terms $y(v)A_v-A_v y(v)$ cancel, and the masks are subtracted with the cancellation MSM of C7 paired against the witness-summed Y. The earlier polynomial subtractions remove all $P_v$ terms except the stated key corner. The first weighted left operand alone is the sum of the left first coordinates; pairing it separately with the search base $s_{\rm leg}$ at each right leg and summing gives
\[
 \Psi_v=[\psi_v]_T,\quad \psi_v=y(v)\sum_c\gamma_c\xi_c(v).
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
Indeed the partial fraction identity for $F/Z_*$ holds by evaluation at all QAP points, and multiplying each term by $X^M-1$ gives the geometric sum because $p^M=1$. Encode each public point coefficient with its fixed factor $1/Z_*'(p)$. After additions selected by the witness bits, multiply the aggregate value for each point by its fixed $1/p$ to obtain the exact transform input weight from the displayed identity. Both arrays take at most $2D<8$ million products for this normalization. Encryption uses the same encoding and the cofactor product proved in C7.

For each polynomial use one length-$M$ transform for the displayed coefficient array and one for its evaluation on each of the two cosets of $\mathcal H_M$ in $c\mathcal H_L$. Scale the coefficients by the respective fixed coset powers before the latter transforms. Both arrays take six transforms and at most $4M$ scalings. When the selected third tag is one, add the two precomputed tag contributions to the respective evaluated numerators. For each of $F=A,B$, the public tag-three table at shifted point $x$ has entry $F_{\rm tag,3}(x)(x^M-1)/Z_*(x)$, where $F_{\rm tag,3}$ is its QAP coordinate polynomial for that tag. The powers and quotients here depend only on the public points and can be evaluated at setup with the same subgroup transforms in $O(D\log D)$ work. Because the selected third tag is a bit, this adds no products at decryption. At each shifted point multiply the two evaluated numerators and the fixed factor $Z_*^2/(LZ_0(X^M-1)^2)$. The factor is defined because the domains are disjoint. Then apply one unnormalized inverse transform of length $L$, and at most $U_*$ products by powers of $c^{-1}$ to recover the actual coefficients of $G_0$ in the variable $X$. This works since the quotient is exact and its degree is below $U_*<L$. It takes below 390 million products, including the small sparse division and the $2L$ pointwise products. For the transform count, the radix-two butterfly stages have at most $B\log_2(B)/2-(B-1)$ non-unit twiddles at length $B$, since each block has a unit first twiddle and the numbers of blocks sum to $B-1$. The sparse division uses the fixed reversed monic inverse on prefixes of length at most $1884$, by a convolution at length 4096. For choices of points outside the scoring placement, the unshifted polynomial construction preceding this paragraph uses interpolation and exact division directly.


For the finite matrix evaluation, write the packed witness entries as bits $b_{j,t}$ in the unit-containing period basis of C5. In row $i$, first sum the tuples $E(M_{ij})$ for which $b_{j,t}=1$, separately for each possible $t$. This costs additions only. Multiply each tuple sum componentwise by the fixed tuple $E(b_t)$ and sum the results. Evaluation is a ring isomorphism, so applying $E^{-1}$ once to this total yields the coefficient vector of the ordinary witness product. Convert the three individual tag-column tuples with one inverse each in that row; the homogeneous column is included with its ordinary bit value one at position zero. There are at most $kd^2$ scaling products, plus $4kd^2$ for the inverse matrices. Thus this implementation uses at most $5kd^2=1320955<5376000$ products, since $n=4332=61k+p_f$ with $1\le p_f\le61$. The other work consists of at most $O(k(\ell+1)d^2)$ additions, a constant multiple of the finite matrix length for the admitted degree. This gives the previous scalar allowance with the period coefficient ring.

The weights of the at most eight needed form values use three conjugate applications with at most $3s_0 n$ products per variant. The two products for $U,V$ fit length-16384 FFTs. Their monic reductions each take at most $s_0 n$ products, because there are at most $n$ elimination steps with at most $s_0$ lower terms per step. With $s_0\le128$, $n\le4800$, the conjugations and reductions use at most $40s_0n\le24576000$ products. The sixteen products use at most $16(3T(16384)+2\cdot16384)<6$ million more by the nonunit twiddle bound, pointwise products and inverse scalings. All weights therefore fit within 32 million.

For each of at most four full mask combinations, form the six weighted leg polynomials. The jointly conjugated representatives have at most $2s_0-1$ terms, and there are at most three additional one-sided conjugated products of support at most $s_0$ per cell, plus the fixed ordinary products. Use the upper bound $(3n/2)(5s_0+2)$ products per full combination, which suffices also when a cell is used in only a subset of these products. Nine length-16384 forward and eight inverse transforms compute the twelve polynomial products after selecting the six weighted legs and three conjugate forms. All polynomial degrees are below $3n\le14400$, so this covers the entire output support. Together the FFTs, pointwise products and the eight inverse scalings take less than 2.1 million products per variant. Exact monic division of the first three outputs takes at most $6ns_0$ more products per variant, by the degree and support bounds of the sparse monic modulus. The complete mask preparation therefore costs below 43 million across four full combinations.

The large QAP scalar preparation, including the required compressed sparse divisions and scalings, costs at most 390 million products by the preceding derivation including the point-wise normalization. Adding the 32-million weight, 43-million mask, 5,376,000 matrix conversion and remaining fixed costs gives fewer than 471 million scalar multiples. For the remaining counts, throughout the at most four full tag combinations the scalars outside the counted tables are the fixed multiples of the sparse basis, $d_v$, $\xi_{\rm key}(v)$, and the key inverse; their computation uses fewer than one thousand further products even using binary exponentiation for the inverse. The protected $632000000+m$ allowance covers this finite total. The matrix entries themselves were traversed using additions and only the counted coefficient conversions.

### Tag choice and key recovery

For any external witness $w$ and $t\in\{0,1\}$, set $a_t=(w,1,0,t)$, $b_t=(w,0,1,t)$, $c_t=(w,0,0,t)$, and $v^{(t)}=(w,1,1,t)$, all with homogeneous coordinate one. The three ordinary corners have zero key corner and $a_t+b_t-c_t=v^{(t)}$ as integer vectors. The target has key corner one.

Return $\bot$ if $\xi_{\rm key}(v^{(0)})=0$. Otherwise if $\Psi_{v^{(0)}}=0$, compute its one full combination and normalize directly with its nonzero key weight. If the primary target base is nonzero and $\Psi_{a_0},\Psi_{b_0},\Psi_{c_0}$ are all nonzero, choose the ordinary triple with $t=0$. Otherwise test $\xi_{\rm key}(v^{(1)})$. If it is zero, take the evaluation-point fallback. With nonzero secondary weight, compute $\Psi_{v^{(1)}}$. If that base is zero, use its direct normalization. If it is nonzero and $\Psi_{a_1},\Psi_{b_1},\Psi_{c_1}$ are all nonzero, select the ordinary triple with $t=1$. Otherwise take the fallback. This uses at most eight plain base tests and four full combinations. All full combinations in the chosen path have common third tag $t$, so they need one baseline. Let $v_*$ denote the selected target in an ordinary branch. Branch selection depends only on the bases and form weights, independently of the search coins.

For the selected triple, use $v_0'=c,v_1'=a,v_2'=b$ and let $c_0,c_1,c_2$ denote the rounded centers of the anchor and differences. Before starting line [full-search], form
\[
 Q_0=\Lambda_c-c_0\Psi_c,\qquad
 Q_1=\Lambda_a-(c_0+c_1)\Psi_a,\qquad
 Q_2=\Lambda_b-(c_0+c_2)\Psi_b .
\]
The line solves $Q_0=t_0\Psi_c$, then solves $Q_1-t_0\Psi_a=t_1\Psi_a$ and $Q_2-t_0\Psi_b=t_2\Psi_b$. The two products by the already recovered $t_0$ use signed binary arithmetic on $|t_0|$, with sign handled by the fixed Frobenius inversion. These are the only group products that translate targets within the search. The output is the three centered logarithms in the record below. The later key computation forms $r(v_*)=c_0+c_1+c_2+t_0+t_1+t_2$, subtracts $r(v_*)\Psi_{v_*}$, and multiplies by the inverse key weight. This gives $[\kappa]_T$. One key-oracle query unmasks the message. At most eight $\Psi$ values and four full $\Lambda$ values are needed, and the triple choice is independent of the search vector.

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

**One search line and its actual result.** The revised line [full-search] receives the selected mode and the respective group operands. On the ordinary mode for the chosen triple, the public centers $c_0,c_1,c_2$ are the rounded centers of the anchor and the two increments. The line returns
\[
 T=(r(c)-c_0,\ r(a)-r(c)-c_1,\ r(b)-r(c)-c_2,\ 0).
\]
On the direct-key mode, the same line instead traverses the evaluation-point logarithm search above and returns $T=(0,0,0,j)$. The index $j$ is the nonnegative solution in $[0,q-1]$ to the displayed group equation, and the other three coordinates are zero. The divisor for key normalization is applied afterward using this fourth returned component. On a bypass branch no logarithm is computed and $T=0$. The line also returns the signed component $t$ of largest magnitude with the smallest index breaking ties. This designated scalar result is an actual recovered logarithm, with $|t|=\|T\|_\infty$. The witness-sampler range $[-B,B]$ is used for the first three coordinates. The separate input-domain range $[0,q-1]$ for the fourth comes from the order of its nonzero base. The RMS and pointwise bounds below cover this entire record, including its fourth component. Reconstruction and group normalization follow the line on either path.

### View of the correction polynomials

The sparse quotient bases and the common-direction right lists are the inputs with inverse scale $\zeta_0^{-1}$, and only the combined correction bases have inverse scale $\zeta_1^{-1}$. The key-scalar degree class in C7 therefore collects the original and tag-difference terms in each cell as $Z_c h_c^0+Z_0 T_c$, with every exponent of $T_c$ in a nonzero residue class modulo $\nu$. Monic division of $T_c$ by $Z_{\mathcal K}$ preserves those classes in every subtraction step. Its remainder $R_c$ has degree below $\nu n_{\mathsf c}$ and is allowed. Multiplying the multiple part by $Z_0$ gives a multiple of $Z_*$, hence of $Z_c$, and it is absorbed into $h_c$. Thus the arbitrary correction is precisely of the required $Z_c h_c+Z_0R_c$ form. The constant-term comparison in C7 bounds the quotient degree by the QAP criterion, and the changed corner is $W_{t_1,t_2}$ from that criterion. Every other Laurent comparison uses the same input types and the same actual field ties, as proved in C7, with the two-sector copies omitted.

## Amendment n2

The exact half-count is
\[
 n_2=\lceil\frac{6K_2(N+4)+3K_2+(3n/2)(J+3)+C_{\rm mask}}2\rceil .
\]
The first two terms count the single right factor arrays and search bases. There is one sparse list of $A_c$ bases, two common-direction right lists of $A_c$ bases and $J$ combined lists of $A_c$ bases, and the cancellation count is $C_{\rm mask}$. The optional generator padding gives $2n_2$ actual slots. The G1 count is proved in n1. Together with the fixed one GT element, seed and masked message, these give exactly the protected size formula and the one-generator-multiplication count from the published scalars.

## Amendment dec_sum_g1

Compute external witness sums of the two coordinates of each left leg and the Y column once with tags omitted, using at most $(N+1)/2$ additions per array in the witness-weight convention. The at most eight variants add at most three tag entries per array. The one common-direction witness sum uses at most $(N+1)/2$ additional additions. For each full combination add at most five fixed entries to each of its two sparse operands and add at most one further fixed multiple to the non-key operand. The up to four full variants each need at most ten additions for the fixed entries and one for the non-key term. One further addition can subtract the fixed multiple in forming the shifted baseline sparse operand. The total 45 fits 64; other weighted operands are charged as MSMs. The total bound is $(2K_1+1)((N+1)/2+24)+(N+1)/2+64$.

## Amendment dec_sum_g2

For the single right factor sector, compute each of the $6K_2$ external witness coordinate sums once, using at most $(N+1)/2$ additions each. Only the at most four full combinations need these sums with tags added; each adds at most three entries. Only the target variant has both tag bits set and needs one addition to combine its two direction MSM results. Thus the count is $6K_2((N+1)/2+12)+1$. The fixed search bases require no analogous coordinate sums.

## Amendment dec_msm_g1

The at most eight first-coordinate weighted left operands and four second-coordinate ones each use $A_c$ points. The baseline sparse key and non-key MSMs use $S_0$ and at most $S_0+1$ points respectively. Charge one more point for the fixed multiple $P_0^0/Z(\rho)$, computed and reused. The baseline non-sparse correction uses $U_*-(S_0+n_{\mathsf c})$ points. These QAP operands are each computed once and shared, and the common-direction witness sum and fixed-entry adjustments were counted as additions. The bound is therefore
\[
 12(3n/2)+D-1+S_0+2+(\nu-1)n_{\mathsf c}.
\]

## Amendment dec_msm_g2

Each full combination uses $A_c$ points for the two sparse right operands together, $J A_c$ for the combined right list and $C_{\rm mask}$ for cancellation. The four variants at a common third tag have zero, one, one and two present bits, respectively, in the common-direction computation. No variant needs to be used more than once for a full combination. Thus the total count of points in the two common-direction MSM lists across all full variants, including the direct-normalization case with only the target, is at most $4A_c$. The resulting bound is $4((3n/2)(J+2)+C_{\rm mask})$. The $\Psi$ combinations use the fixed right search bases without new G2 MSMs.

## Amendment dec_pairings

Each of the at most eight $\Psi$ sums uses $3K_2$ pairings. Each of at most four $\Lambda$ sums uses $6K_2$ factor pairs, $J$ combined correction pairs, two sparse pairs, at most one common-direction pair and one cancellation pair. Thus the total is at most $24K_2+4(6K_2+J+4)$. Accumulate each signed sum starting with its first term, updating by the indicated group addition or subtraction. This needs at most one fewer accumulation operation per nonempty sum than its pairing count. The remaining bounded number of GT translations, final normalizations and searches are accounted for in search_spread.
The exceptional fallback follows the search-base computations and performs two additional pairings with the already transmitted sparse bases. It uses no full combination. Its pairing count is at most $24K_2+2$, within the same bound.

## Amendment search_spread

Let $\sigma^+=g\sqrt{(N+7)/48}$, $R_0=\sigma^++3/2$, and define
\[
 M_0=\begin{cases}
 (7979/10000) g\sqrt{(N+7)/48}+3/2 & 359994\le N\le479993,\quad g\ge10^{12},\\
 (803/1000) g\sqrt{(N+7)/48}+3/2 & \text{otherwise when }N\ge359994,\\
 R_0 & N<359994 ,
 \end{cases}
 \quad M_1=g/4+1/2 .
\]
The amended spread is
\[
 \max\{ R_0,\ R_T,\ 
   (\frac{20}{37}\big((10001/10000)((4882533/2950000)\sqrt{\sigma^+}+(47/18+1/5000000)\sqrt{g/2})+404500\big))^2\},
 \quad R_T=g\sqrt{(N+23)/48}+14 .
\]
Here $M_0$ bounds the expected absolute centered anchor, and $M_1$ bounds an increment in the first-listed triple. The amended arithmetic cost uses the sharper concurrent-anchor bound proved below. The branch selection is independent of the search vector, so the anchor bound applies on any chosen triple. The two additional quantities $R_0$ and $R_T$ cover the RMS of the recombined centered integer and the full search record respectively.

For the ordinary search record, the exactly centered variables have second moments bounded by $(g^2-1)(N+7)/48$ for the anchor and $2(g^2-1)/12$ for each increment, since each increment involves at most two independent uniform box samples with opposite coefficients. The square of the Euclidean norm is a sum of squares regardless of their correlations. The vector of rounding errors has Euclidean norm below $2$, since the anchor error is at most $3/2$ and each increment error at most $1/2$. The triangle inequality in square mean bounds the ordinary part of the record by $g\sqrt{(N+23)/48}+2$. The fourth component is zero except on the direct-key fallback whose probability is at most $135/q^2$ by Targets. Since $0\le j<q$, its root mean square is at most $\sqrt{135}<12$, even with arbitrary dependence between the branch and $j$. Summing these square-mean bounds gives $(\mathbb E\|T\|_2^2)^{1/2}\le R_T$, which also bounds the RMS of the signed greatest component. The first three coordinates meet the range bound from Bsearch and the stated width of any two box samples, and the evaluation-point coordinate meets its stated range.

### Expected absolute anchor

Before the rounding error of at most $3/2$ in Bsearch, the center removes the mean, leaving the sum of independent symmetric variables
\[
 S=X_\diamond+\sum_{i=1}^{N+3}(v_i-1/2)X_i ,
 \quad X_i=r_i-(g+3)/2 .
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
 |x|=\frac2\pi\int_0^\infty\frac{1-\cos(tx)}{t^2} dt .
\]
To verify the constant, scale by $|x|$ when $x\ne0$, then integrate by parts to obtain $\int_0^\infty\sin(t)/t dt=\pi/2$. In the integral with a factor $\exp(-at)$, $a>0$, differentiating in $a$ gives $-1/(1+a^2)$ and the integral tends to zero as $a$ tends to infinity. It therefore equals $\arctan(1/a)$. Ordinary integration by parts bounds the damped tail uniformly in $a$ by $2/T$ after $T>0$, since $\exp(-at)/t$ is positive decreasing. This justifies the limit as $a$ decreases to zero. The case $x=0$ is immediate. The integrand of the absolute-value identity is nonnegative, so expectation can be taken inside. The normal absolute moment is $\sqrt{2/\pi}$ by integrating its density on the two half axes. Its characteristic function $\exp(-t^2/2)$ follows from differentiating the integral of its density times $\exp(itx)$, integrating by parts to obtain $\psi'(t)=-t\psi(t)$, and using $\psi(0)=1$.

The two characteristic functions have absolute values at most one for every $t$. Using their sharper bound up to 300, the triangle inequality gives
\[
 \frac{\mathbb E|S|}{\sigma_S}
 \le \sqrt{2/\pi}+
 \frac{2}{720000\pi}\int_0^\infty t^2e^{-t^2/4} dt+
 \frac{4}{300\pi}
 < \frac{803}{1000}.
\]
For the inequality the middle integral is $2\sqrt\pi$ by substituting $u=t/2$ and integrating by parts, and $\pi>3.14$ suffices for the final numerical comparison. Adding the rounding error yields $M_0$, with Cauchy--Schwarz giving the alternate bound at smaller $N$.

For the scored range $359994\le N\le479993$ and $g\ge10^{12}$, the cosine bound can be continued beyond frequency 300. Each of the $N+3$ ordinary summands has spacing $1/(2\sigma_S)$ after normalization, up to sign, with distribution symmetric about zero. The finite geometric sum yields its characteristic function
\[
 \frac{\sin(gu)}{g\sin u},\quad u=\frac{t}{4\sigma_S}.
\]
Here $\sigma_S/g\le100$ by $N+7\le480000$. Also $\sigma_S\ge g$ since $g\ge2$ and $N+7\ge360000$. Thus $300\le t\le10^6$ gives $gu\ge3/4$ and $0<u<1/100$. The function $\sin v/v$ decreases from 1 on $[0,\pi]$: the derivative numerator $v\cos v-\sin v$ is zero at zero and has derivative $-v\sin v\le0$ there. For $v\ge\pi$, its absolute value is at most $1/\pi$. Taylor's bound on $\sin(3/4)/(3/4)$ and the lower bound $\sin u\ge u-u^3/6$ therefore give
\[
 |\frac{\sin(gu)}{g\sin u}|
 \le \frac{1-(3/4)^2/6+(3/4)^4/120}{1-(1/100)^2/6}<\frac{91}{100}.
\]
Both Taylor bounds follow from the alternating power series on the given fixed intervals. Since $(91/100)^8<1/2$ and $N+3\ge320$, the product of the ordinary factors is bounded in absolute value by $2^{-40}$ on this frequency interval. The diamond factor has absolute value at most one and the normal factor is also at most $2^{-40}$ for $t\ge300$. Thus the middle integral contributes less than $2^{-40}$ after its $2/\pi$ normalization. The tail above $10^6$ contributes at most $4/(\pi10^6)$.

The normal first absolute moment is less than $797886/10^6$. For an exact bound, $\pi>314159/100000$ follows by the tangent addition formula from $\pi/4=4\arctan(1/5)-\arctan(1/239)$ and the alternating bounds through the $-x^7/7$ term for the first arctangent and $x$ for the second. Indeed the tangent of $4\arctan(1/5)$ is $120/119$, and the indicated difference has tangent one and lies between zero and $\pi/2$. These rational bounds give
\[
 16(\frac15-\frac1{3\cdot5^3}+\frac1{5\cdot5^5}-\frac1{7\cdot5^7})
 -\frac4{239}>\frac{314159}{100000},\qquad
 \frac{314159}{100000}(\frac{797886}{10^6})^2>2 .
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

**Amended Proposition 5.7(c).** Decryption uses at most the source-group sums, MSM lengths and pairing counts proved in their respective amendments. In addition it takes at most 1024 target-field accumulator products at the scored shape for the signed pairing sums and at most 400 further target products for fixed combinations, initialization, and search setup. In this bound, shared final exponentiation remains part of the protected pairing charge. The ordinary path uses thirteen target-group scalar multiples outside the candidate iterations: three center translations, two in-line anchor translations, two final operations to subtract the search term and apply the inverse key weight, and six initial strides for the three logarithms. The branch with zero distinguished target base uses at most one scalar multiplication, and the direct-key recovery branch uses only one scalar multiplication after recovering its evaluation-point index. The admissible upper bounds therefore hold pointwise on all branches for the stated work outside the candidate iterations. The arithmetic price for these products, including basis conversions, is proved below.

**Amended Proposition 5.7(d).** Line [full-search] in n1 takes $O(\sqrt{\|T\|_\infty}+1)$ target-group operations on its actual result $T$. Equivalently its cost is $O(\sqrt{|t|}+1)$ for the signed largest emitted logarithm. On the ordinary mode of that line this follows from the three component bounds below. On the direct-key mode it follows from the adaptive evaluation-point search and the equality $\|T\|_\infty=j$. The same output and pointwise bound therefore cover both traversals. All auxiliary arithmetic during decryption besides these traversals is covered by (c). The expected group work in the line is $O(\sqrt g N^{1/4})$ on an honest ciphertext.

The direct-key mode of the search line has probability at most $135/q^2$, by Targets. In this mode stage width $w=2^h$ takes fewer than $w$ baby updates, fewer than $w$ giant updates, at most $h$ doublings and bounded setup. With one inverse of $E_0$ via the fixed $p^6$ Frobenius, at most four target operations per unit width including setup suffice. The stage search cost is therefore $O(w)$, and the sum of widths through the first width with $w^2>j$ is less than twice that width, while the final width is at most $2\sqrt{j+1}$. This gives the claimed bound for the fourth component. In particular there are at most $16\sqrt q+600$ operations of cost at most a target product, including the final scalar multiple outside the line. Its two pairings are included in dec_pairings. Its scalar-field denominator formation and inversion cost less than one multiplication in expectation at the protected prime and fit the protected scalar allowance.

The primary fixed-width traversal gives the expected-cost bound, and the interleaved traversal below supplies the pointwise guarantee of Proposition 5.7(d). For any centered target $x$ known to have $|x|\le B$ and $\mathbb E|x|\le M$, use the sign-class baby and giant search with integer width $b=\lceil\sqrt M\rceil+1$. Tabulate $iP$ for $0\le i<b$, where $P\ne0$ is the base. The signed intervals centered at $j(2b-1)$ with radius $b-1$ partition the integers. Progress outward in the order $j=0,1,-1,2,-2,\ldots$, testing the sign class of the respective residual against the table. Verify the sign and the resulting integer against the bound; $2B+1<q$ makes the bounded solution unique. A match for the true integer occurs by $|j|\le |x|/(2b-1)+1$. The baby construction has at most $b$ counted steps. Its stride follows from the last baby point by a doubling and one addition. Maintain separate accumulators for positive and negative giant indices, so alternating the direction advances the selected accumulator with one update. Including a constant for initialization and verification, the total is at most $b+2|x|/(2b-1)+12$ steps on a true target. This bound includes names and the constant work to derive their signs according to the protected step convention. A run with no valid solution can stop upon exploring all intervals intersecting $[-B,B]$. Since $2b-1\ge2\sqrt M$, its expected bound on a valid sampled target is at most $2\sqrt M+14$. A nonzero base is always used for these searches.

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

The paired entries are present by giant ordinal $2(d+j)$, so put $u=2(d+j)/b$. In the positive savings region $u<t_1$, before the baby table fills. Its primary count is at most $b(u+h(u))+6$. On these two segments $h(u)=(8/5)u-\min((11/20)u,11/50)$. Define $A'=141/80$, $C'=26/5$, $R'=13/8$, and
\[
 f_*(v,w)=\left(A'-C'v-R'w+\min((11/10)v,11/50)\right)_+ .
\]
The saved count at each sample is at least $(b f_*((d+j)/b,j/b)-9)_+$. Indeed the support obeys $v\le (A'+11/50)/C'=61/160$, so $u=2v\le t_1$ with strict inequality when the bound is positive. Also $w\le v$ and $f_*(v,w)>0$ imply $w<(A'+11/50)/(C'+R')=61/210<1/3$. In the retained legal range both giant lists are available at these times. The two samples satisfy $|x|\le db+b$. Each adjacent $K$ integer has $|z|\le (5/4)(d/b)+1/100$, since $b^2/\sigma^+<1231/1000$, $2b+g+3<\sigma^+/60$ and $s_K>(99/50)\sigma^+$. Their total probability, including averaging over the diamond, is at least $\ell(d/b)/\sigma^+$ where
\[
 \ell(t)=(199/500)\left(1-\tfrac12((5/4)t+1/100)^2\right)-1/10000 .
\]
Here $s_K<2\sigma^+$, and $\ell$ is positive, below $2/5$, and $1/4$-Lipschitz on $0\le t\le61/160+2/b$.

On an area-two rectangle $[d-1,d+1)\times[j-1,j)$ put $v=(x+y)/b$, $w=y/b$. The discrete saving is at least $(bf_*(v,w)-22)_+$ because the two argument slopes in $x,y$ have magnitude at most $C'$ and $C'+R'$ and $2C'+R'+9<22$. The probability factor is at least $\ell(v-w)-1/(4b)$. Their product is at least $bf_*(v,w)\ell(v-w)-10$, since $f_*\le2$ and $22\ell+f_*/4<10$. This also holds when the discrete saving is zero. Integrating over $0\le w\le v\le61/160$, of area below $1/2$, gives expected savings at least $b^3(I_\ell-5/b)/\sigma^+$.

For the exact integral $I_\ell$, let $A''=A'+11/50$ and let $c_2$ be the quadratic coefficient of $\ell$. The successive $v$ intervals have endpoints $0,1/5,61/210,61/160$. On them set $(F,L)$ to $(A'-(41/10)v,v)$, $(A''-C'v,v)$, and $(A''-C'v,(A''-C'v)/R')$. Integrating $(F-R'w)\ell(v-w)$ over $0\le w\le L$ gives
\[
 F(\ell(v)L-\ell'(v)L^2/2+c_2 L^3/3)
 -R'(\ell(v)L^2/2-\ell'(v)L^3/3+c_2 L^4/4).
\]
The sum of its integrals over those intervals is $I_\ell=3254649870535259/235929600000000000$. Thus the saving is at least $(123/100)a(I_\ell-5/2^{24})>a/59$. Since $a>(11/10)\sqrt{\sigma^+}$, the anchor count is at most $(4882533/2950000)\sqrt{\sigma^+}+4096$ in expectation.

### Adaptive pointwise traversal

Each ordinary search runs a second, adaptive search over the same bound. It uses the auxiliary polynomial-basis representation described below and uses exact equality of twelve-coordinate vectors for table keys. At stage $j\ge0$, set $w=2^j$ and tabulate $iP$ for $0\le i<w$. Use $j$ doublings to obtain $wP$ and another $j$ to obtain $w^2P$. The stride $-wP$ comes from negating $P$ and doubling $j$ times. The inverse of $P$ can be extracted once in at most 508 products by using the scalar $q-1$. It can also be obtained by applying the fixed $p^6$-Frobenius matrix, since the BN254 embedding degree is 12, so $p^6\equiv-1\pmod q$. To handle the pointwise bound uniformly, use this fixed twelve-dimensional linear map, at at most 144 base-field products. Start with the residual $xP+w^2P$ and test $2w+1$ residuals, advancing by $-wP$. A match with baby index $i$ at giant index $j'$ gives $x=j'w+i-w^2$. This covers $[-w^2,w^2+w-1]$, hence certainly every integer of magnitude at most $w^2$. Accept only an integer in $[-B,B]$; uniqueness follows from $2B+1<q$. Thus a valid integer is found by the first stage with $w^2\ge |x|$. With standard constant-operation table access in the search model, the stage costs $O(w)$. Its finite work consists of group products, table accesses, comparisons and integer index updates. The geometric sum of widths is less than twice the last width, so the total work is $O(\sqrt{|x|}+1)$. Each group's multiplication can be suspended between products of coordinates. Resume the adaptive search for one elementary operation before the first primary operation and after each block of one million primary operations, stopping when either search returns. An adaptive operation can be a group update, a table operation, or the single Frobenius application. A primary candidate and its associated table actions have bounded cost, so an adaptive search that would finish in $T$ operations finishes within $10^6(T+1)$ primary candidates if the primary search has not already finished. Each interleaved search therefore costs $O(\sqrt{|t_i|}+1)$ for the integer it produces, with an absolute constant independent of $N,q,g,M$. The three public translations by $c_0,c_0+c_1,c_0+c_2$ are prepared before entering line [full-search]. The two in-line subtractions of $t_0\Psi$ use at most $2\lceil\log_2(|t_0|+1)\rceil$ group products each, and a constant-time target inverse by Frobenius for the appropriate sign. Their cost is $O(\sqrt{|t_0|}+1)$, using $\log(x+1)=O(\sqrt{x})$ for $x\ge1$. Thus the work in this single line, including these translations and all three adaptive traversals, is at most a fixed constant times $\sqrt{\max_i|t_i|}+1$ in the ordinary mode. Choosing the signed largest component and the later key recombination involve only a fixed number of integer operations.

The anchor uses the two-phase concurrent traversal and both first-triple differences use the concurrent traversal with the two distinct strides. A later triple uses the same anchor and the fixed-width traversal with $M_\Delta$ for both differences. Primary baby and giant candidates use the unchanged six-multiplication tariff for the ordinary search operations. For the adaptive search, even charging two arbitrary target-group products at the full 276-multiplication price derived below per scheduled operation, the ratio of adaptive charge to primary charge over a full block is at most $552/(6\cdot 10^6)<1/10000$. At most three initial adaptive operations and the increment initialization and verification bounds of 14 are accounted for separately in the auxiliary allowance. Apart from that allowance, the expected contribution is at most $(4882533/2950000)\sqrt{\sigma^+}+(47/18+1/5000000)\sqrt{g/2}+4352+1$, including the rare use of a later ordinary triple. Termination by the adaptive search can only reduce it.

**Base-field multiplication ledger for auxiliary work.** Use a degree-12 polynomial basis of the target extension of the BN254 base field. Multiplication uses at most 144 coefficient products and reduces the eleven higher coefficients against fixed basis vectors in at most 132 products, for 276 total. Conversion to or from the protected basis uses at most 144 products. At most eight such conversions handle the three base-and-target pairs and output apart from pairing conversions.

A scalar multiplication after reducing the scalar modulo $q<2^{254}$ uses at most 508 group products by binary powering. Budget thirteen such multiples: three center translations, two anchor translations, two final normalization operations and two stride multiples for each of the three traversals. The accompanying updates use six target products. Budget eighteen fixed $p^6$ Frobenius sign maps at 144 products each for those signs, the strides, adaptive bases and hits. The adaptive initializations use at most six further products. There are at most fourteen terminal or initialization products per primary traversal. Thus $6+18+6+3\cdot14=72$ fits within 400 products even pricing each map as a full target product. Signed pairing sums use source sign changes and the protected shared final exponentiation, with at most one accumulator product and basis conversion per pairing. Their count is $48K_2+4(J+4)\le1024$ by the admitted shape. The other scalar operations were charged separately.

The direct-key fallback has expected auxiliary cost at most $(135/q^2)(16\sqrt q+600)276<10\cdot276$, apart from its two pairings already counted. The total auxiliary work is below $(13\cdot508+1024+400+10)276+(1024+8)144<2400000$, hence fits in 400000 primary tariff units. The rare later ordinary triple adds less than one primary candidate in expectation, covered by two extra units including interleaving. Together with the primary and adaptive bounds the expected cost is at most $6((10001/10000)((4882533/2950000)\sqrt{\sigma^+}+(47/18+1/5000000)\sqrt{g/2})+404500)$ since $400002+(10001/10000)4352<404500$. All bounded answers and published operands have the same security and correctness analysis.

## Amendment n

Use $n=kd_R+\mathrm{form\_pad}$. Put $v_0$ in slot zero, put zeros in the following $\mathrm{form\_pad}-1$ positions, and use the remaining $kd_R$ positions for the output coefficients of the matrix product, ordered by row and coefficient position in the basis of C5. The finite guard bounds the number of padding positions for each admitted degree. This preserves the exact kernel identity $(v_0,A\hat v)=(0,0)$. The number of padded positions is not a change to the number of input coordinates or to the coefficient norm. The actual Module-SIS dimensions are $kd_R$ and $\ell d_R$ with the Euclidean coefficient radius of Amendments msis_bound and msis_norm, while the exponent calculation uses the field of the full degree $n$.

## Amendment msis_bound

Set $\mathrm{msis\_bound}=\mathrm{beta\_sis}=B_{\rm E}$. An infinity-short multiple of $v\ne0$ is an integer $x\equiv a v\bmod q$, $a\ne0$, with $0<\|x\|_\infty\le\beta$. For the amended Euclidean problem, a short multiple instead means such a congruence with $0<\|x\|_2\le B_{\rm E}$. Preserve the original infinity theorem as a separate assertion.

Precisely, for every heavy stack, (a) its rank is at most three, (b) every nonzero kernel vector in its row space has an infinity-short multiple, and (c) every infinity-short multiple of any kernel vector packs to an infinity-SIS solution at $\beta$ in the stipulated coefficient ring. For (a), fixing all but pivot coordinates gives ${\rm gp}(W)\le g^{-{\rm rank}W}$, as in Bsearch, and $g^{-4}<\theta$. For (b), a linear combination of stack rows is constant on every joint fiber, so ${\rm gp}(v^\top)\ge{\rm gp}(W)>\theta$. The kernel gives $v_0=0$; apply the proved infinity inverse theorem of I6. For (c), the identity in C7 and coordinate packing in ell give $A\hat x=0\bmod q$ and $0<\|\hat x\|_\infty=\|x\|_\infty\le\beta$.

For the costed Euclidean instance, (a) is identical. Every kernel vector in the row space of any heavy stack has a Euclidean-short multiple. The proof and deterministic lifting procedure follow below. The Euclidean version of (c) is universal: every Euclidean-short multiple of any kernel vector packs to a solution at $B_{\rm E}$, by the same kernel identity and the Euclidean isometry in msis_norm. An infinity-short vector need not be Euclidean-short. No conversion between those two radius predicates is used.

### Joint fibers

For a nonzero matrix $A$ of linear forms on independent box coordinates in $\{1,\ldots,N_\star\}$, suppose the maximum probability of $Ar_I$ is $p>\theta$. The prefix construction of I6 extends to this joint fiber and gives a regular saturated lattice of rank at most three containing the row space modulo $q$, with maximum fiber density at least $p-3\varepsilon_{\rm tr}$. To see this, remove zero columns. The joint prefix probabilities $p_i$ are nonincreasing by conditioning on the last coordinate. The first nonzero column gives $p_1=1/g$ and lattice $\mathbb Z$. At a subsequent step, express each current prefix row as $B c_j$ modulo $q$ in the current basis $B$. Append the next coefficient to get $c'_j$. In the trimmed densest joint fiber $F$ of the longer prefix, these vectors define constant modular forms in $\Phi(r)=(B^\top r_{[i]},r_{i+1})$. At least one last coefficient is nonzero, so one such form puts $\Phi(F)$ in an index-$q$ coset. Since $\Pr[F]\ge p_{i+1}-\varepsilon_{\rm tr}>\mu_{\rm tr}$ and $\Lambda_d\Gamma_d<q\mu_{\rm tr}$, the I6 sparse count excludes full affine dimension. The same minors of its difference matrix satisfy the I6 bound because it depends only on the current basis, trimming and the box. The small-minor lift of the protected lattice-facts lemma gives an integer annihilator of those differences for **each** $c'_j$. Consequently $F^\perp$ contains integer lifts of all new rows. Its rank is at most three by the density bound and $g^{-4}<\mu_{\rm tr}$; the regularization lemma enlarges it to a regular saturated lattice losing at most $2\varepsilon_{\rm tr}$. This proves the claimed induction, including the rank and density. Restoring zero coordinates preserves the claims.

### Mass times Euclidean covolume

For a rank-$d$ lattice $\Lambda$ with integer basis $B$, write $c(\Lambda)=\sqrt{\det(B^\top B)}$ for its covolume in its real span. We will prove that every saturated rank-three normal lattice of maximum fiber mass $m\ge\mu$ satisfies $m c(\Lambda)\leC_3/g^3$. Every regular rank-two output of the regularization procedure of I3 satisfies $m c(\Lambda)\leC_2/g^2$, provided its input has the required density and its output density is at least $\mu$. Use precisely that procedure at each joint-fiber extension.

Choose a largest minor of $B$ on $J$ and order these rows first. Set $h=|\det B_J|$ and $P=BB_J^{-1}$, so each entry of $P$ has absolute value at most one. For a prefix length $j\ge d$, write $G_j=P_{[j]}^\top P_{[j]}\succeq I_d$. The inequality follows because the rows on $J$ are unit axes. Let $\Lambda_j$ be the saturation of the prefix and $h_j$ its height. Its covolume is $h_j\sqrt{\det G_j}$. Indeed $B_{[j]}=YC$ with $Y$ a basis of $\Lambda_j$, and $|\det C|=h/h_j$ by the prefix proof of I3. Gram determinants then give the formula. The prefix image $B_{[j]}^\top\mathbb Z^j$ has index $h/h_j$ in $\mathbb Z^d$ by the same proof.

Fix the target of a densest fiber of $B^\top r$. Let $s_i$ be the successive index multipliers after the prefix $j$, so $\prod_i s_i=h/h_j$, including factors one. The prefix before step $i$ has image $G^{\rm int}_{i-1}=B_{[i-1]}^\top\mathbb Z^{i-1}$, and $s_i$ is the order of the next row in the quotient by this image. Call a suffix integer tuple feasible if its projection subtracted from the target leaves a point in the prefix image and in the prefix region described below. If $j=d$, use the exact pivot box of side $g-1$, with $G_j=I_d$ and no trimming. If $j>d$, discard at most $e$ absolute probability using the prefix trimming event of I3. The normalized prefix value lies within $R_{\rm tr} g/\sqrt{12}$ of its mean in the norm $\|G_j^{-1/2}\cdot\|_2$, by changing from the saturated prefix basis to the normalized row matrix $P_{[j]}$. Write $e'=0$ in the first case and $e'=e$ in the second. For each feasible suffix, the conditional probability of the remaining required prefix value is at most $m_j$. All suffix points in the original box have the same probability. Thus if there are $M$ feasible suffix tuples, $m-e'\le m_j M/g^{N_\star-j}$.

For each feasible suffix tuple $y$, attach the axis-aligned rectangle centered at $y$ with widths $\ell_i$ satisfying $1\le\ell_i\le s_i$. The interiors of these rectangles are disjoint. Indeed if two different feasible tuples have last differing index $k$, subtract their two congruences modulo the prefix image and then cancel all terms at indices below $k$ in the larger image $G^{\rm int}_{k-1}$. Their coordinate difference at $k$ is a nonzero multiple of $s_k$. The two intervals at that coordinate have disjoint interiors. Every rectangle has volume $\prod_i\ell_i$. It lies within the product of the enlarged suffix intervals of widths $w_i=g-1+\ell_i$. The disjointness argument works with width equal to $s_i$; shared boundaries have zero Lebesgue measure.

Write $S_\ell=\sum_{i:s_i>1}\ell_i$. Rows of $P$ have entries bounded by one, and their length in the normalized prefix metric is at most $\sqrt d$, because $G_j\succeq I_d$. From a rectangle center to any point in it, the change of the matched prefix value is therefore at most $(S_\ell+N_\star)/2$ in each pivot coordinate if $j=d$, and at most $\sqrt d(S_\ell+N_\star)/2$ in the metric norm otherwise. Here each step of order one uses width one. All attached rectangles thus map under the suffix projection into a fixed translate of $G_j^{1/2}[-w/2,w/2]^d$, where
\[
 w=\begin{cases}
 g+S_\ell+N_\star,&j=d,\\
 2R_{\rm tr}g/\sqrt{12}+\sqrt d(S_\ell+N_\star),&j>d.
 \end{cases}
\]
The metric ball and its enlargement fit the displayed cube in the second case. In both cases $w\ge g$.

We use the following density inequality. If $A$ has row rank $d$ and $X$ has independent side-one uniform coordinates, then $AX$ has density at most $2^{d/2}/\sqrt{\det(AA^\top)}$. It suffices to prove it for $AA^\top=I_d$ by applying the invertible whitening map. Write the columns of this normalized $A$ as $\sqrt{c_i}u_i$, with $u_i$ unit, $0<c_i\le1$, and discard zero columns. Then $\sum_i c_i u_i u_i^\top=I_d$.

If some $c_i>1/2$, project orthogonally off $u_i$. The other projected columns still sum to the identity as outer products on the orthogonal space. Condition on all other input coordinates and integrate the uniform $i$-th input along $u_i$. Its density there is at most $1/\sqrt{c_i}<\sqrt2$: for a test set, the conditional probability is bounded by this constant times the length of its section at the projected point. Fubini and the lower-dimensional density bound prove the claim in this case by induction, with counting mass one in dimension zero.

If all $c_i\le1/2$, the characteristic function at frequency $2z$ is $\prod_i {\rm sinc}(\sqrt{c_i}u_i^\top z)$ up to phase, where ${\rm sinc}(x)=\sin(x)/x$ with value one at zero. For any nonnegative integrable continuous functions $f_i$, the tight-frame inequality is
\[
 \int_{\mathbb R^d}\prod_i f_i(u_i^\top z)^{c_i} dz
 \ \le\ \prod_i(\int_{\mathbb R} f_i)^{c_i}.
\]
To prove it first take nonzero compactly supported $f_i$, smooth by the one-dimensional heat kernel $f_i(t,s)$, and put $F(t,z)=\prod_i f_i(t,u_i^\top z)^{c_i}$. With $v_i=\partial_s\log f_i(t,u_i^\top z)$, the heat equation and chain rule give
\[
 \partial_t F-\Delta F
   =F(\sum_i c_i v_i^2-\|\sum_i c_i v_i u_i\|_2^2)\ge0,
\]
because the matrix with columns $\sqrt{c_i}u_i$ has orthonormal rows. On compact positive time intervals the kernel and its derivatives have Gaussian decay times a polynomial: its first logarithmic derivative is $(-s+\mathbb E U)/(2t)$, the second is $-1/(2t)+{\rm Var}(U)/(4t^2)$, with the source $U$ supported where $f_i$ is supported. The tight-frame identity gives the Gaussian decay in $z$, so the integral of the Laplacian vanishes and the integral of $F$ is nondecreasing. Fatou as $t\downarrow0$ bounds the left side. As $t\to\infty$, rescale $z=\sqrt t z'$; the product and Jacobian give the standard Gaussian heat kernel on $\mathbb R^d$ times the right side. The limit is dominated by a constant times $\exp(-\|z'\|_2^2/8)$, using bounded source support and $(v-w)^2\ge v^2/2-w^2$. Continuous cutoffs increasing to one and monotone convergence give the asserted inequality for the unbounded supports.

We need the univariate bound $I(p)=\pi^{-1}\int_{\mathbb R}|{\rm sinc}(x)|^pdx\le\sqrt{2/p}$ for $p\ge2$. Let $U$ be the uniform density on $[-1/2,1/2]$. Fourier inversion at zero, with frequency $2x$, gives $I(2)=1$, $I(4)=2/3$, and $\pi^{-1}\int{\rm sinc}(x)^3dx=3/4$. Indeed, $U*U$ is the tent $(1-|t|)_+$; convolving it with $U$ at zero gives $3/4$, and convolving it with itself at zero gives $2/3$. All these Fourier integrals converge absolutely, and inversion follows by first adding Gaussian smoothing and taking its variance to zero, using continuity of the convolutions.

To bound the absolute cubic integral, write $S_-=(2/\pi)\int_{\{x>0:\sin x<0\}}|\sin x/x|^3dx$. Then $I(3)=3/4+2S_-$. For the first negative interval $[\pi,2\pi]$, split it into four equal parts. The integrals of $|\sin x|^3$ on them are $A,B,B,A$, where $A=2/3-5\sqrt2/12<78/1000$ and $B=5\sqrt2/12<590/1000$, from the antiderivative $-\cos x+\cos^3x/3$ on $[0,\pi]$. Use the left endpoint to bound $x^{-3}$ on each part. On later negative intervals the integrals of $|\sin x|^3$ are $4/3$, and their left endpoints are $(2j+1)\pi$ for $j\ge1$. The decreasing reciprocal cubes sum to at most $1/27+\int_1^\infty(2t+1)^{-3}dt=1/27+1/36$. It follows that
\[
 S_-\le\frac{2}{\pi^4}\{\frac{78}{1000}\bigl(1+(4/7)^3\bigr)
           +\frac{590}{1000}\bigl((4/5)^3+(2/3)^3\bigr)
           +\frac43(1/27+1/36)\}.
\]
Substituting $\pi>314159/100000$ gives $I(3)<777/1000<\exp(-1/4)$; the latter inequality follows from the alternating cubic lower bound. Hölder interpolation gives $I(p)\le\exp(-(p-2)/4)$ for $2\le p\le3$, and $\log(p/2)\le(p-2)/2$ proves $I(p)\le\sqrt{2/p}$ there. Between three and four the scaled endpoint values $I(p)\sqrt p$ are below $34/25$. The concavity gap of $\log p$ above its endpoint chord is at most $1/72$, by the second derivative bound $1/9$ on this unit interval. Hölder thus gives $I(p)\sqrt p\le(34/25)\exp(1/144)<7/5<\sqrt2$.

For $0<x<\pi$, the difference $(1-x^2/3)\sin x-x\cos x$ has derivative $(x/3)(\sin x-x\cos x)\ge0$, since the parentheses have derivative $x\sin x\ge0$. Integrating $\cot x-1/x\le -x/3$ yields ${\rm sinc}(x)\le\exp(-x^2/6)$. For $x\ge\pi$, write $\sin^2x=(1-\cos 2x)/2$ and integrate the cosine term by parts to get $\int_\pi^\infty\sin^2x/x^2 dx\le1/(2\pi)+1/(4\pi^2)$. Thus for $p\ge4$,
\[
 I(p)\sqrt p\le\sqrt{6/\pi}
       +\frac{2\sqrt p}{\pi}\pi^{2-p}(\frac1{2\pi}+\frac1{4\pi^2})<\sqrt2 .
\]
The tail factor decreases on this interval, and at four the upper bound is below $1407/1000$ by $\pi>314159/100000$. This completes the bound on all $p\ge2$.

Apply the tight-frame inequality with $f_i(s)=|{\rm sinc}(\sqrt{c_i}s)|^{1/c_i}$. Each integral is at most $\pi\sqrt2$ by the preceding estimate after rescaling. Fourier inversion with frequency $2z$ bounds the density by $\pi^{-d}(\pi\sqrt2)^{\sum_i c_i}=2^{d/2}$. Equivalently, this inversion bound first holds after convolution with a small centered Gaussian by its Fourier integral, and the uniform bound on the smoothed laws passes to the limiting law when integrated against continuous compactly supported tests. The same Gaussian limit justifies the interval convolution inversion at $p=2$, since its transform is integrable and the convolution is continuous. This proves the density inequality, including its determinant factor before normalization.

Take the independent uniform law on the enlarged suffix intervals of widths $w_i$. The union of attached rectangles has volume $M\prod_i\ell_i$, so its probability under this law is $M\prod_i\ell_i/\prod_iw_i$. It is bounded by the probability of the enlarged prefix cube for the projected suffix. As before that probability is the convolution density with the independent uniform on a centered cube of shape $G_j^{1/2}[-w/2,w/2]^d$, multiplied by $w^d\sqrt{\det G_j}$. For a pointwise bound at the translated center, enlarge the cube by an arbitrarily small positive width and move to a nearby center in the full-measure set satisfying the density bound. Then pass to the original width, as the original translated cube is contained in each of these enlarged cubes. The augmented Gram matrix dominates $g^2G_{\rm full}$ since $w_i\ge g$ and $w\ge g$. Thus the cube probability is at most
\[
 2^{d/2}(w/g)^d\sqrt{\det G_j/\det G_{\rm full}} .
\]
Multiplying by the conditional prefix bound and the final covolume gives
\[
 (m-e')c(\Lambda)
 \ \le\
 2^{d/2}(w/g)^d m_j c(\Lambda_j)
 \prod_i(w_i/g)\prod_i(s_i/\ell_i).
\]
All the products are over suffix coordinates. Choosing full widths $\ell_i=s_i$ incurs no final ratio and satisfies $\prod_i(w_i/g)\le\prod_{s_i>1}(1+s_i/g)$.

For rank three take $j=d=3$. The suffix orders are below $g$, since an order at least $g$ would reduce the initial pivot maximum $g^{-3}$ to at most $g^{-4}$ by I3, contradicting $m\ge\mu>g^{-4}$. Their product is at most $H_3\le g$, so at most one order exceeds $\sqrt g$. For the orders in $[2,\sqrt g]$, the monotone ratio $(s-1)/\log s$ bounds their sum by the number of factors plus $(\sqrt g-1)\sum_i\log s_i/\log(\sqrt g)$. There are fewer than 254 factors by (I1) and their log sum is at most $\log g$. Hence $S_{\rm small}/g\le254/g+2/\sqrt g<1/10000000$ for $g\ge2^{49}$. Their enlarged suffix widths contribute at most $\exp(S_{\rm small}/g)\le10000000/9999999$. The exponential bound follows from the geometric series for arguments in $[0,1)$; the monotonicity follows by differentiating the ratio.

Set $L=2$ and $\tau=147/100$. The guards give $H_3\le g$, $g^4\mu\ge\tau$, and $N_\star/g\le10^{-7}$. When every suffix order is at most $g/L$, use the cube smoothing just proved. If there is an order $s>\sqrt g$, choose width $ts$ for that coordinate with $t=1/\max(1,3/L)$ and full widths otherwise. Thus $ts/g\le\min(1/L,1/3)$, and the inverse rectangle-volume ratio is at most $\max(1,3/L)$. The pivot cube side divided by $g$ is at most $(1+ts/g)(1+N_\star/g+10^{-7})$, and the suffix-width contribution is at most $A_{\rm small}(1+ts/g)$ with $A_{\rm small}=10000000/9999999$ as above. With no such order the same bound holds by using full widths everywhere. The cube estimate therefore gives
\[
 m c(\Lambda)g^3\le
 (99/35) A_{\rm small}(1+2\cdot10^{-7})^3
 \max(1,3/L)(1+\min(1/L,1/3))^4 < 1341/100 .
\]
Here $m_3 c(\Lambda_3)=g^{-3}$ for the independent pivot coordinates, and $2^{3/2}<99/35$. The last comparison uses the indicated rational constants.

Otherwise there is an order $s>g/2$. Since it divides the full pivot index $h\le H_3\le g$, we have $h=s$. Fix all nonpivot integer coordinates except this one. For each choice of its integer value $y$, the pivots are determined. They are integral only in one residue class modulo $s$, or in none, because the earlier suffix rows generate no extra index and the large row has order $s$ modulo the pivot image. The number $K$ of choices with all pivots in the box is at most two. Its expectation is $T=g^4m$. Thus $\Pr[K=2]\ge T-1$, since $K\le1+\mathbf1_{K=2}$.

Let $p$ be the normalized large row, and $X$ the projected sum of all other nonpivot coordinates. On $K=2$ the two values are $y_0$ and $y_0+s$ with $0\le y_0\le g-1-s$. For each pivot coordinate with $p_i\ge0$, the endpoint pivot constraints imply that the target minus $X_i$ is at least $s p_i$ and at most $g-1+(g-1-s)p_i$. Reflecting $y$ about $(g-1)/2$ gives the same interval width for a negative $p_i$. Thus $X_i$ lies in a fixed interval of length at most $g-1+(g-1-2s)|p_i|$. Smooth the other nonpivot coordinates by independent uniforms on $[-1/2,1/2]$. This broadens each interval by at most $N_\star$ since every row entry is bounded by one. The resulting independent-coordinate projection belongs, on this event, to a fixed box of widths $g w_i$, where
\[
 w_i=1+10^{-7}-(2s/g-1)|p_i|>0.
\]
This uses $N_\star/g\le10^{-7}$ and $s<g$ from the rank-three density. Hence the probability of the smoothed projection in this box is at least $T-1$.

Let $S$ be the sum of row outer products for the other nonpivot coordinates in the normalized basis. Each smoothed input is uniform on an interval of length $g$. Convolve their projection with an independent uniform box of widths $g w_i$. As in the preceding cube probability argument, the comparison for the translated box follows by arbitrarily small enlargements, using the density bound for a point near its center. The augmented Gram divided by $g^2$ is $S+\mathcal B$, where $\mathcal B=\operatorname{diag}(w_1^2,w_2^2,w_3^2)$. Its density times the box volume gives
\[
 (T-1)\le\Pr[\text{box}]\le
 2^{3/2}\frac{\prod_i w_i}{\sqrt{\det(S+\mathcal B)}}.
\]
The full normalized Gram is $G=S+I+pp^\top$. Put $A=(1+10^{-7})^2I+pp^\top$, so $G\preceq S+A$ and $A\succeq \mathcal B\succ0$. For any $S\succeq0$,
\[
 \frac{\det(S+A)}{\det(S+\mathcal B)}
 =\det\bigl(I+(A-\mathcal B)^{1/2}(S+\mathcal B)^{-1}(A-\mathcal B)^{1/2}\bigr)
 \le\frac{\det A}{\det \mathcal B}.
\]
The identity follows by factoring the positive matrix $S+\mathcal B$ and moving the factors in a determinant of the form $I+UV$. For the inequality, $(S+\mathcal B)^{-1}\preceq \mathcal B^{-1}$ by whitening with $\mathcal B^{1/2}$, and determinant is monotone on positive definite matrices by the same whitening argument. Multiplying by $\sqrt{\det G}$ therefore cancels $\prod_i w_i=\sqrt{\det\mathcal B}$ and gives $(T-1)\sqrt{\det G}\le2^{3/2}\sqrt{\det A}$. Also $h=s$ and $c(\Lambda)=h\sqrt{\det G}$. Since $\sqrt{\det A}\le(1+10^{-7})^3\sqrt{1+\sum_i p_i^2}$, put $t=s/g$, $P=\sum_i p_i^2$, and $a=1+10^{-7}$. The ratio $T/(T-1)$ decreases, so the determinant bound and $h=s$ give
\[
 m c(\Lambda)g^3\le t C\sqrt{1+P},\qquad C=(99/35)a^3\tau/(\tau-1).
\]
If $t\le7501/10000$, this is at most $2C(7501/10000)<13.28<1341/100$.

For the remaining $t$, use each individual interval of the double-choice event as well. Applying the one-dimensional version of the density bound after convolution with its uniform interval gives
\[
 T-1\le \sqrt2\,w_i/\sqrt{S_{ii}+w_i^2}.
\]
Solve for $S_{ii}$ and add the pivot and large-row squared coefficients. With $r=(2t-1)/a$ and $k=a^2(2/(T-1)^2-1)$, this gives $G_{ii}\le f(|p_i|)$ for
\[
 f(x)=1+x^2+k(1-rx)^2 .
\]
Here $1/2\le r\le1$ and $1\le k\le10$, by $\tau\le T\le2$. The determinant of a Gram is at most the product of its diagonal entries, by orthogonalization. Thus $mc(\Lambda)g^3\le tT\sqrt{\prod_i f(|p_i|)}$.

We bound that product at fixed $P$ by concentrating its squared coordinates. Write $f(\sqrt y)=b_0-b_1\sqrt y+b_2y$, where $b_0=1+k$, $b_1=2kr$, $b_2=1+kr^2$. For $0<x\le1$ the sign of the second derivative of $\log f(\sqrt y)$ at $y=x^2$ is the sign of
\[
 b_1b_0-2b_1^2x+5b_1b_2x^2-4b_2^2x^3.
\]
Its derivative is $-2(b_1-2b_2x)(b_1-3b_2x)$, so the minimum on $[0,1]$ occurs at an endpoint or at $b_1/(3b_2)$. The endpoint zero is positive. At the possible interior minimum the value is $b_1 b_0-7b_1^3/(27b_2)>0$ since $b_1^2/(b_0b_2)\le400/121<27/7$. At $x=1$ nonnegativity is equivalent, after dividing by four, to
\[
 kr(3-2r)-1+k^2 r(1-r)^2(1/2-r)\ge0.
\]
The expression is concave in $k$, so check $k=1$ and $k=10$. At one it is $(1-r)(r-1/2)(2-r(1-r))\ge0$. At ten it is at least $9-100/64>0$, since $r(3-2r)\ge1$, $r(1-r)\le1/4$ and $(1-r)(r-1/2)\le1/16$. Convexity extends to zero by continuity. Holding the sum of two squared coordinates fixed, their sum of log factors is convex in either, and is maximized with one at zero or one. Repeating this leaves at most one fractional square. For $1<P\le2$ the resulting absolute-coordinate pattern is $(1,\sqrt{P-1},0)$; for $2\le P\le3$ it is $(1,1,\sqrt{P-2})$.

The following bounds cover $7501/10000<t<1$. Each row is the interval of $t$ ending at $b$ and starting at the preceding endpoint, with $7501/10000$ as the first lower endpoint. It has $r\ge r_0$. The first bound uses $P\le P_0$. Otherwise for $P<2$ the fractional coordinate is at least $x_0$. For $P\ge2$ its lower bound is $x_0$ when $P_0\ge2$, and zero otherwise. All displayed decimals are rationals.

| $b$ | $r_0$ | $P_0$ | $x_0$ | $P\le P_0$ | $P_0<P<2$ | $P\ge\max(2,P_0),\ T\le8/5$ | $P\ge\max(2,P_0),\ T\ge8/5$ |
|---|---|---|---|---|---|---|---|
| $4/5$ | $1/2$ | $5/2$ | $7/10$ | 13.25 | | 11.91 | 9.34 |
| $21/25$ | $599/1000$ | $13/6$ | $2/5$ | 13.23 | | 11.16 | 9.00 |
| $23/25$ | $679/1000$ | $8/5$ | $77/100$ | 13.13 | 12.97 | 13.05 | 10.78 |
| $24/25$ | $839/1000$ | $7/5$ | $63/100$ | 13.16 | 11.47 | 10.52 | 9.63 |
| $1$ | $919/1000$ | $5/4$ | $1/2$ | 13.28 | 12.26 | 10.14 | 9.61 |

For the first column of bounds compare $b^2 C^2(1+P_0)$ to the square of the entry. For the others put $f_J(x)=1+x^2+J(1-r_0x)^2$. It bounds $f$ when $k\le J$. For any fractional coordinate in $[u,1]$, convexity of this quadratic gives its bound as $\max(f_J(u),f_J(1))$. For the second bound column use $J=17/2$, $u=x_0$, and $T\sqrt{f(0)}\le a\sqrt2\tau/(\tau-1)$. The squared bound is
\[
 2(b a\tau/(\tau-1))^2 f_J(1)\max(f_J(x_0),f_J(1)).
\]
For the last two columns use $(T_0,J)=(8/5,17/2)$ and $(2,23/5)$ respectively, since $k=a^2(2/(T-1)^2-1)$. The squared bounds are $(bT_0 f_J(1))^2\max(f_J(u),f_J(1))$ with $u$ as specified above. These rational expressions are below the corresponding squared entries. The table and the first case give the asserted $1341/100$ uniform covolume coefficient. The proof holds for the heavy joint fiber before any passing-stack test.

For rank two use the chosen prefix sequence of the regularization proof of I3. If the final normal lattice is strictly larger, the procedure returns a rank-three lattice, covered above. Otherwise choose $j=d$ if no preceding prefix has a strictly larger normal, and the first prefix after the last strictly larger normal otherwise. Take full widths $\ell_i=s_i$ on this rank-two extension and write $A_{\rm box}=\prod_i (g-1+s_i)/g$. The suffix steps have order below $g$. As in I3, an order at least $g$ would put a new unit-vector normal vanishing on $J$ into the next selected fiber's normal, contradicting the choice of the last strict prefix. The product of the suffix orders is at most $h\le H_2<g^{12/5}$ by regularity and the guarded fifth power. Call an order large if $s_i\ge g^{4/5}$. There are at most two large orders since three would have product at least $g^{12/5}$. Let $a\in\{0,1,2\}$ be the number of large orders. The product of the other nontrivial orders is below $g^{(4/5)(3-a)}$, since each large order is at least $g^{4/5}$. For a real $u>1$, the ratio $(u-1)/\log u$ is increasing, because its derivative has numerator $\log u-1+1/u\ge0$. For each small nontrivial order $s_i$, apply this bound with upper endpoint $g^{4/5}$ to get
\[
 \frac{s_i}{g}
 \le \frac1g+\frac{g^{4/5}-1}{g}\frac{\log s_i}{(4/5)\log g}.
\]
The number of nontrivial orders is below $(12/5)\log_2 g<610$ by (I1). Summing over the small orders thus gives
\[
 \sum_{{\rm small}}\frac{s_i}{g}
 <\frac{610}{g}+(3-a)g^{-1/5}
 <\frac{3-a}{880},
\]
using $g\ge2^{49}$, $890^5<2^{49}$, and $610/2^{49}+1/890<1/880$. For zero or one large order, use $S/g<a+(3-a)/880$. The small padding factors have product at most $\exp((3-a)/880)$ and the large factors are at most two each. Using $\exp(x)\le1/(1-x)$ for $0\le x<1$, the total padding factors are below $101/100$ and $201/100$, respectively.

If two large suffix orders occur, they have product at least $g^{8/5}$. Since the regular final lattice has height $h\le H_2<g^{12/5}$, their occurrence forces $h_j<g^{4/5}$. The prefix lattice can then be bounded directly without the preceding rank-three planar count. Apply the rectangle bound to $\Lambda_j$ itself with its pivot prefix of length two. Its pivot height is one and pivot probability $g^{-2}$. The suffix orders of this nested application have product $h_j$, so their nontrivial sum is at most $h_j$, using that a sum of two or more integers at least two is at most their product. In particular the sum divided by $g$ is below $g^{-1/5}<1/880$. Using their full widths, the product of the enlarged suffix interval ratios is at most $880/879$, and the pivot box ratio is at most $1+1/880+1/1024$. Thus
\[
 m_j c(\Lambda_j)\le (2/g^2)(880/879)(1+1/880+1/1024)^2<3/g^2.
\]
This uses the actual saturated prefix lattice, so it does not require any additional regularity of that prefix. Its normalized pivots are obtained from a largest minor as before.

In the final suffix with two large orders, $S/g<2+1/880$, and the product $A_{\rm box}$ is below $4(880/879)<402/100$. Its full-width pivot side ratio is below $4$, and the trimmed side ratio is below $14$, using $18/\sqrt3<52/5$, $\sqrt2<99/70$ and $N_\star/g\le1/1024$. Hence the general rectangle bound and $m/(m-e')\le1000/999$ give
\[
 m c(\Lambda)<(1000/999)\cdot2\cdot(402/100)\cdot14^2\cdot3/g^2<5000/g^2<C_2/g^2 .
\]
This proves the two-large case, regardless of the position of the selected prefix.

For zero and one large orders, the trimmed side ratios are below $21/2,12$, respectively: substitute $S/g<a+(3-a)/880$ into $18/\sqrt3+\sqrt2(S/g+N_\star/g)$ with the preceding rational bounds. The pivot side ratio is below four. A pivot prefix therefore gives $m c(\Lambda)<2(201/100)4^2/g^2<C_2/g^2$. It remains to treat $j>d$ in the zero- and one-large cases.

When $j>d$ the preceding rank-three regular containing lattice used to trim $F_j$ in I3 has basis $B_{\rm old}$, covolume $c_{\rm old}$ and mass $m_{\rm old}$. It obeys $m_{\rm old}c_{\rm old}\leC_3/g^3$. Let $C={\rm diag}(B_{\rm old},1)$ on the previous prefix plus its new coordinate, and $G=C^\top C$. This is an integer basis of a saturated rank-four lattice, as both summands are saturated. All normals to $F_j$ restrict on the previous coordinates to the span of $B_{\rm old}$ by I3. Thus $C$ carries the real annihilator of differences in the image $C^\top F_j$ isomorphically to the real normal space, and its saturation implies that the image coefficient normals have a saturated basis $V$ in $\mathbb Z^4$ with $CV$ a basis of the integer normal lattice $\Lambda_j$. Its rank here is two. Hence the affine image space has dimension two.

Whitening the image coordinates by $G^{-1/2}$ maps the difference lattice $\ker V^\top\cap\mathbb Z^4$ to the orthogonal complement of $G^{1/2}V$ with planar covolume
\[
 \delta=\sqrt{\det(V^\top G V)}/\sqrt{\det G}=c(\Lambda_j)/c_{\rm old}.
\]
To see the identity, extend a basis of the kernel lattice with two integer columns $L$ such that $V^\top L=I_2$. They exist by saturation of $V$, which gives $V^\top\mathbb Z^4=\mathbb Z^2$. The full extended basis is unimodular by decomposing an integer vector via $V^\top$. After whitening it has full volume $1/\sqrt{\det G}$. Its last two columns project onto the normal plane as $G^{1/2}V(V^\top G V)^{-1}$, whose area is $1/\sqrt{\det(V^\top G V)}$. Multiplying by the planar covolume gives the full volume and proves the identity.

The whitened trimmed region lies in the ball of radius $g\sqrt{324/12+1/4}$ because the old coordinates are trimmed and the final interval has length $g-1$. Therefore its planar slice has area at most $A=\pi g^2(324/12+1/4)$. The image point count $M$ satisfies $M\le 2A/\delta+2$ by the simplex count in I3. Each image point has mass at most $m_{\rm old}/g$ by independence. Moreover $\Pr[F_j]\ge m_j-e\ge999\mu/1000$ by the prefix density premise and the Euclidean guard. The image has affine dimension two, so $M\ge3$. With no large suffix order this suffices for $M/(M-2)\le3$. If there is a large order $s_i$, the prefix probability bound at that step gives $m_{i+1}\le m_i\lceil g/s_i\rceil/g\le 2m_i/s_i$. The prefix masses are nonincreasing, so the earlier $m_j\ge m_i\ge (s_i/2)m_{i+1}\ge(g^{4/5}/2)m$. Each image point has mass at most $m_{\rm old}/g\le g^{-4}$, and the trimmed fiber has mass at least $m_j-e\ge(999/1000)m_j$. Hence
\[
 M\ge (999/2000)g^{4/5} m g^4 > (999/2000)g^{4/5} > 2^{37},
\]
using $m\ge\mu>g^{-4}$ and $g\ge2^{49}$. In particular $M/(M-2)<1001/1000$ if there is any large suffix order.

The planar count gives $(M-2)\delta\le 2A$, so in both remaining cases
\[
 (m_j-e)c(\Lambda_j)\le M(m_{\rm old}/g)\delta c_{\rm old}
 \le 2\pi(324/12+1/4) (M/(M-2)) g m_{\rm old}c_{\rm old}.
\]
For no large suffix order, one can sharpen the area comparison without assuming that the image contains many points. Set $R_0=g\sqrt{324/12+1/4}$. The section of the trimming ball is a disk of radius at most $R_0$. For $3\le M\le6$ its image polygon has area at most $MR_0^2/2$: orient its vertices around the boundary and use the signed determinant area formula, measuring the vertex vectors from the disk center, so each determinant is at most $R_0^2$. The projected lattice count gives area at least $(M-2)\delta/2$. Consequently $M\delta\le M^2 R_0^2/(M-2)\le9R_0^2$. For $M\ge7$ use the disk area bound to get $M\delta\le (14\pi/5)R_0^2<9R_0^2$. Thus in the no-large case the multiplier in the preceding estimate of $(m_j-e)c(\Lambda_j)$ can be bounded by $9(324/12+1/4)<246$ in place of $2\pi(324/12+1/4)M/(M-2)$. For one large order the bound $M/(M-2)<1001/1000$ still gives a multiplier below $172$.

Apply the rectangle estimate to the final suffix. Its factors have already been bounded by $A_{\rm box}<101/100$ and $w/g<21/2$ with no large order, or by $A_{\rm box}<201/100$ and $w/g<12$ with one large order. In both cases $m/(m-e)$ and $m_j/(m_j-e)$ are at most $1000/999$. The resulting constants on $C_3/g^2$ are less than
\[
 (1000/999)^2\cdot 2(101/100)(21/2)^2\cdot 246
 \quad\hbox{or}\quad
 (1000/999)^2\cdot 2(201/100)12^2\cdot172 .
\]
The first is below $55000$ and the second below $100000$, by multiplication of the displayed rationals. This proves $m c(\Lambda)\le C_2/g^2$ by I6.

If regularization starts in rank one and returns a rank-two lattice from a recursive call, apply this calculation to the rank-two call and its selected sequence. This proves the needed rank-two mass-covolume estimate.

### Rank-one Euclidean covolume

Let $C_1=90000 C_2+20000000 C_3+200$. For a rank-one regular output of I3 of mass $m\ge\mu$, choose the pivot prefix $j=1$ or the first prefix after the last strict normal, as for rank two. The suffix orders satisfy $s_i<g$ by the unit-vector argument, and their product is at most $h\le H_1<g^4$. Use widths $s_i$. Call $s_i\ge g^{4/5}$ large and write $L$ for their number, so $L\le4$. For $s>1$, the ratio $(s-1)/\log s$ is increasing, as differentiation gives a derivative of the sign of $\log s-1+1/s\ge0$. Applying it up to $g^{4/5}$ gives small-order sum divided by $g$ below $1016/g+(5-L)g^{-1/5}<1/150$, since $g<q<2^{254}$ and $g\ge2^{49}$. Hence the padding is below $16e^{1/150}<17$, or $2e^{1/150}<203/100$ for $L\le1$. With $R_{\rm tr}\le20$ and $N_\star/g\le1/1024$, the ratio $w/g$ is below six for a pivot prefix, below sixteen for a trimmed prefix and below thirteen for a trimmed prefix with $L\le1$.

For $j=1$, $m_j c(\Lambda_j)=1/g$, so the rectangle estimate gives $m c(\Lambda)<200/g$. Otherwise the preceding strict normal is contained in the regular trimming lattice of rank $r=2$ or $3$, with mass $m_{\rm old}$ and covolume $c_{\rm old}$. Use the rank-two proof’s diagonal basis $C$ and whitening. The current image normal has one primitive integer column $V$. A basis of $\ker V^\top$ extended by an integer column $L_0$ with $V^\top L_0=1$ is unimodular. The last whitened column has normal projection of length $1/\sqrt{V^\top C^\top C V}$, so the difference lattice has covolume $\delta=c(\Lambda_j)/c_{\rm old}$. The section lies in a ball of radius $g\sqrt{R_{\rm tr}^2/12+1/4}<6g$. Its $M\ge r+1$ image points have mass at most $m_{\rm old}/g$ each, and I3 gives $(M-r)\delta\le r!$ times the section volume.

For $r=3$ the ball gives $M\delta<22000g^3$ using $M/(M-3)\le4$, so $(m_j-e)c(\Lambda_j)\le22000 C_3/g$. For $r=2$, the disk and $M/(M-2)\le3$ give $M\delta<680g^2$. If $L\ge2$, the suffix inequalities give $m_j\ge(g^{4/5}/2)^2m$. The previous rank-two mass is at most $g^{-2}$ by its pivots. Thus $M\ge(999/1000)m_j g^3>2^{27}$ since $m>g^{-4}$. Now $M/(M-2)<1001/1000$ and squared radius at most $(400/12+1/4)g^2$ imply $M\delta<213g^2$. The two rank-two bounds give $(m_j-e)c(\Lambda_j)\le680 C_2/g$ or $213 C_2/g$.

In the rectangle estimate each trimming ratio is at most $1000/999$ and the density factor below $99/70$. The coefficients on $C_2/g$ are at most $(1000/999)^2(99/70)(203/100)13\cdot680$ and $(1000/999)^2(99/70)17\cdot16\cdot213$, both below 90000. The coefficient on $C_3/g$ is at most $(1000/999)^2(99/70)17\cdot16\cdot22000<20000000$. Hence $m c(\Lambda)\le C_1/g$ throughout, without imposing any passing test.

### Euclidean multiples in every heavy stack

Let $\mathcal V$ be the row space of a heavy stack with nonzero kernel vector $v$, with $v_0=0$. The stack fiber is that of any row-space basis. If some $w\in\mathcal V$ has $w_0\ne0$, then conditional on the independent box coordinates $w^\top r$ is uniform on $g$ distinct values through $r_\diamond$ since $g<q$ and $v^\top r$ is fixed. The guessing probability of $v^\top r$ is above $g\theta$, so applying joint fibers to it on the box gives a normal lattice of density above $g\mu$ since $g\theta-3e>g\mu$. If all of $\mathcal V$ has zeroth coordinate zero, apply joint fibers to its basis on the box. This gives a normal lattice of density above $\mu$ containing $\mathcal V$ modulo $q$. Either lattice has rank at most three and contains the line of $v$ modulo $q$.

In rank one its primitive generator has norm $c(\Lambda)\le C_1/(g\mu)\le B_{\rm E}$, and saturation gives a nonzero residue on the line. In ranks two and three the covolume bounds are $C_2/(g^2\mu)$ and $C_3/(g^3\mu)$. The coefficient preimage of the line of $v$ has index $q^{d-1}$ in rank $d$, since a saturated basis has full rank modulo $q$. Its covolume is multiplied by that index. The shortest-vector inequalities below and the squared or cubic I6 guard give a nonzero vector of norm at most $B_{\rm E}$. Its residue is nonzero since $2B_{\rm E}<q$. Appending the zero homogeneous coordinate preserves norm. This proves a short multiple for every kernel vector of every heavy stack. Recovery selects a kernel vector by the form equations on the recovered basis, without constructing the normal lattice.

For the Euclidean lift we use a sharper length bound in ranks two and three. If $L$ has rank two, take a shortest nonzero $u$ of length $\lambda_1(L)$. It is primitive, so integer coordinate operations extend it to a basis $u,v$. Subtract a nearest integral multiple of $u$ from $v$. Then $|u^\top v|\le\|u\|^2/2$ and $\|v\|\ge\|u\|$, so $c(L)\ge(\sqrt3/2)\lambda_1(L)^2$.

For rank three, scale so that a shortest nonzero vector $u$ has length one. Project along this primitive vector; the image is a rank-two lattice, since a basis beginning with $u$ projects its other two elements to an independent basis. Take a shortest nonzero projected vector $\bar b$, and complete it with $\bar c$ to a projected basis. Change $\bar c$ by a nearest multiple and a sign to write $\bar c=\beta\bar b+c_\perp$ with $c_\perp\perp\bar b$, $0\le\beta\le1/2$. Let $B=\|\bar b\|^2$ and $C=\|c_\perp\|^2$. Lift to $b,c\in L$ with $u$-coordinates reduced into $[-1/2,1/2]$. Then $c(L)^2=BC$, $B\ge3/4$ by $\|b\|\ge1$, and $C\ge(1-\beta^2)B\ge3B/4$ by the minimality of $\bar b$.

Suppose $BC<1/2$. Then $B<\sqrt{2/3}$ and $a=\sqrt{1-B}$ lies in $(1/3,1/2]$. Also $C<1/(2B)<B$, so $\beta\ge\beta_0=\sqrt{1-C/B}$. For $t\in[\beta_0,1/2]$ define $p(t)=\sqrt{1-C-Bt^2}$. Its argument is positive: $B(1+a)=(1-a)(1+a)^2=1+a(1-a-a^2)\ge1$, so $C<(1+a)/2$ and $1-C-B/4>(1-a)^2/4$. The $u$-coordinates of $b,c$ have absolute values at least $a,p(\beta)$, respectively, because both vectors have length at least one. In particular both lower bounds are at most $1/2$. The distance of the difference of the two coordinates from an integer is at most $1-a-p(\beta)$. For coordinates with the same sign this follows from $|b_u-c_u|\le1/2-\min(a,p(\beta))$. For opposite signs the absolute difference lies in $[a+p(\beta),1]$, so subtracting a signed unit gives the bound.

The function $p(t)+(1+a)t$ is concave. At $1/2$ its value is above one by $p(1/2)>(1-a)/2$. At $\beta_0$ we have $p(\beta_0)=a$. For $1/3\le a\le1/2$, $4a(1-a)^2\ge1/2$, since this polynomial is decreasing on that interval and equals $1/2$ at its right endpoint. Using $B=1-a^2$ gives
\[
 C<1/(2B)\ \le\ 4aB/(1+a)^2 .
\]
Hence $\beta_0>(1-a)/(1+a)$, so the other endpoint value is also above one. Concavity proves $p(\beta)+(1+a)\beta>1$. Now $c-b$, reduced along $u$, is a nonzero lattice vector with squared length at most $C+B(1-\beta)^2+(1-a-p(\beta))^2$. Subtracting one from this expression gives $2(1-a)(1-p(\beta)-(1+a)\beta)<0$, a contradiction. Thus $c(L)^2\ge1/2$ at shortest length one. Undoing the scaling gives $\lambda_1(L)^3\le\sqrt2 c(L)$.

The rational overestimates $2/\sqrt3<231/200$ and $\sqrt2<99/70$ follow by squaring. These are existence bounds; the short-span algorithm below supplies a polynomial-time lift without needing the basis of the lattice used in the existence proof.

### Polynomial-time Euclidean lifting

For input $v\ne0$ with zero zeroth coordinate, discard that coordinate and order the others with $v_1\ne0$. Define $L_i=\{x\in\mathbb Z^i:\bar x\in\mathbb F_q v_{[i]}\}$ and let $S_i$ be the real span of vectors of $L_i$ of length at most $B_{\rm E}$. There cannot be four independent such vectors. They would have a nonzero $4$-by-$4$ minor. Its rows modulo $q$ have rank at most one. If all reduce to zero, the determinant is a multiple of $q^4$. Otherwise subtract from each other row an integer multiple of a row with nonzero residue, making three rows divisible by $q$. The determinant is then divisible by $q^3$, although Hadamard bounds its absolute value by $B_{\rm E}^4<q^3$. Therefore $\dim S_i\le3$.

Maintain an actual list of short vectors spanning $S_i$, initialized in length one with the vector $1$. This belongs to $L_1$ because $v_1\ne0$, and $1\le B_{\rm E}$. Projection of a short vector at the next prefix is short at the preceding prefix. Thus search only in $S_i\times\mathbb R$, of dimension at most four. Let $U$ be the matrix whose columns are the current basis vectors extended by a zero last coordinate, and the final unit vector. Choose an invertible minor on rows $J$. The matrix $C=UU_J^{-1}$ parametrizes possible vectors by their $J$-coordinates $y$. Write $C=A/c$ for $c=|\det U_J|$, with integer entries of $A$. Both $A$ and $c$ have $O(\log q)$-bit entries by fixed-size determinants and the bound $B_{\rm E}<q$ on the columns of $U$. Integer vectors therein must have integer coordinates $y$. Require for each row $j$
\[
 A_j y\equiv0\bmod c,\quad (v_1 A_j-v_j A_1)y\equiv0\bmod cq ,
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
 \|b_{i+1}^*\|_2^2\ge \tfrac12\|b_i^*\|_2^2,\quad |\eta_{ij}|\le\tfrac12.
\]
Track original basis coordinates by exact solving with rational minors, so a reduced-basis expression always has a known lift in that basis.

For a reduced basis of rank at most four we can also solve the exact closest-vector problem in polynomial time. Work in its real span by orthogonally projecting the target $x$, since the perpendicular component adds a constant squared distance. Nearest-plane rounding, from last column to first, subtracts the nearest integer multiple in each last Gram–Schmidt coordinate of the residual. Later subtractions from earlier columns leave the already reduced higher Gram–Schmidt coordinates unchanged. The residual's norm is at most $\tfrac12\sqrt{\sum_i\|b_i^*\|_2^2}$. By the final estimates this is at most $\tfrac12\sqrt{2^r-1} \|b_r^*\|_2<2\|b_r^*\|_2$ for $r\le4$. A closest vector therefore has last basis coefficient within two of the last Gram–Schmidt coordinate of $x$, expressed in units of $b_r^*$. Enumerate all integers in that interval. For each candidate subtract that multiple of $b_r$, project the result to the span of the first $r-1$ columns, and recursively find the closest vector in the lattice of those columns. Its squared distance plus the residual orthogonal squared distance is the exact best value for that last coefficient. The prefix basis is still reduced, so the argument applies at each recursion, with rank zero solved by returning the zero vector. At most five recursive choices per level and fixed depth give polynomial bit time. Coordinate centers, squared distances and nearest integers are evaluated with exact rational arithmetic. At fixed depth their bit lengths remain polynomial by the basis bounds and the rational formulas for projections and centers.

Now compute a basis of $L\cap W$ and extend it to a basis of $L$. In the given basis coordinates of $L$, $W$ is a rational subspace of $\mathbb R^r$, specified by at most $r$ normal rows after clearing denominators in a nullspace basis. Starting from the identity basis on $\mathbb Z^r$, restrict each normal successively to the current kernel columns. For a nonzero row there, extended-gcd unimodular column operations make the row $(h,0,\ldots,0)$ with $h\ne0$. The kernel is exactly the last columns. Retain the first transformed column as a complement, and apply the next restriction only to the kernel columns. Induction gives a unimodular full basis with the final kernel columns spanning all integer points of $W$ in these coordinates. This uses at most four operations of this row-reduction type, each of polynomial bit time by the extended Euclidean algorithm in fixed dimension. Apply the original basis map to get the two sets of columns in $L$.

Project the complementary columns orthogonally off $W$. They form a rational basis of the projected lattice $L'$ because the other columns project to zero and the complements are independent modulo $W$. Each projected lattice point has a lift by the recorded complementary basis coordinates. If $L'$ has rank zero, there is no vector outside $W$. Otherwise reduce its basis by the routine above. If its first vector has norm at most $B_{\rm E}/2$, lift that vector to $L$ and reduce its $W$ component by nearest-plane rounding in the **stored short-vector basis** of $W$. The short-vector basis spans $W$ and consists of actual integer lattice vectors. It need not be the full basis of $L\cap W$ for this rounding step. Every one of its Gram–Schmidt lengths is at most $B_{\rm E}$. After rounding the squared length of the $W$ component is at most $3B_{\rm E}^2/4$; the perpendicular component has squared length at most $B_{\rm E}^2/4$. This returns a short vector outside $W$.

If the first projected reduced basis vector has norm greater than $B_{\rm E}/2$, the final reduction estimates imply that every projected Gram–Schmidt length is greater than $2^{-(r+1)/2}B_{\rm E}$, with $r\le4$. Enumerate every nonzero projected point of length at most $B_{\rm E}$ by descending basis coordinates. Given later integer coordinates, the coefficient of $b_i^*$ is the current coordinate plus a fixed rational shift. Its permitted interval has radius at most $B_{\rm E}/\|b_i^*\|_2<6$ in these units. Enumerating within six of each center and checking the exact squared norm therefore lists every candidate, in a number of branches bounded independently of the input. For each projected point choose a lift $x\in L$. The other lifts are $x+L\cap W$. Use the exact closest-vector routine just proved in $L\cap W$ with target the negative of the $W$ component of $x$. Its output minimizes the total squared length among these lifts by orthogonality. If that minimum is at most $B_{\rm E}^2$, return the lift. If no candidate works, no short vector outside $W$ exists. The orthogonal projections come from rational linear solves in dimension at most four; integer-coordinate conversions and all comparisons have polynomial bit length. This completes the fixed-dimensional search.

Apply this search repeatedly at a prefix, starting with $W=0$ in the located lattice with basis $D_i$. Each success adds an actual short vector and raises the dimension of $W$. When the search certifies there is no short vector outside, the list spans $S_{i+1}$. At most four searches are needed, since its dimension is at most three. Together with the $O(N_\star)$ congruence updates per prefix, the total bit work $T_{\rm LIFT}$ is polynomial in $N_\star,\log q$. At the final prefix return a stored nonzero short vector if the span is nonzero and $\bot$ otherwise. Restore coordinate order and the zero homogeneous coordinate. Its residue is nonzero by the length bound and belongs to the prescribed line by the defining congruences. This is an exact algorithm for the Euclidean lift used in the reduction.

## Amendment msis_norm

Set $\mathrm{msis\_norm}=2$ in the concatenated integer coefficient basis of C5. For any kernel vector $v$ and any Euclidean-short multiple $x\equiv a v\bmod q$, $a\ne0$, the bound $2B_{\rm E}<q$ forces $x_0=0$. Packing copies all other coordinates once, inserts zeros and commutes with reduction. Thus $A\hat x=aA\hat v=0\bmod q$ and $0<\|\hat x\|_2=\|x\|_2\le B_{\rm E}$, which proves the universal Euclidean packing clause. The original infinity clause remains true at its own norm and radius, as shown in msis_bound. There the heavy-stack selection and lifting prove existence and recovery for the amended reduction. Neither the public seed law, ring matrix, ciphertext nor decryption operation counts use the solution norm. Targets proves extraction and the reduction cost.

## Targets

Fix any parameter set satisfying the amended model, the protected system shape, any admissible evaluation points, and the stated group and oracle models. In the chosen modes use the coefficient positions of Amendment n, the base field of Amendment C6 and the grid and masks of Amendment C7, and the single-sector QAP encryption and decryption of Amendment n1. The amended inverse theorem applies by (P3) with Amendments I3, I4, H3 and I6. The charged-mark bound is proved in Amendment Ncmp. Correctness and extraction use the same external witness relation, oracle model, budgets and probability bounds. Internally the projected witness forgets its Boolean tags.

### Correctness with error $2/q$

Fix an external witness $w$, the statement, message and admissible evaluation points. Every tag extension used in n1 is a witness of the internal system. If the prescribed weight of $v^{(0)}$ is zero decryption returns $\bot$. Otherwise the chosen target has nonzero weight, whenever the ordinary or direct-normalization branch is selected. The identities of n1 recover the exact key in these branches. They give the settled target value after the three exact integer logarithms and the equality $a_t+b_t-c_t=v^{(t)}$ in the ordinary branch, and directly in the branch where the chosen target base is zero. The evaluation-point branch recovers the exact key on every realization where it is called. Therefore failure is exactly the event of zero prescribed weight, which we bound next.

First consider the key weight for either fixed target. Let $L:F\to\mathbb F_q$ be the constant-slot coefficient functional in the form basis, nonzero because $L(1)=1$, and let $s=n/2-1$. Then the weight of a form value $x$ is $Q(x)=L(x\sigma^s(x))$, with $x$ uniform on the affine space with constant slot one and prescribed padding zero. The trace map is nonzero: the polynomial $\sum_{j=0}^{n-1}X^{q^j}$ has degree $q^{n-1}<q^n$ and cannot vanish at all $q^n$ field elements. The pairing $(a,b)\mapsto{\rm Tr}(ab)$ is therefore nondegenerate, since multiplication by a nonzero $a$ is invertible. Thus $L(x)={\rm Tr}(\lambda x)$ for a unique nonzero $\lambda$, by equality of the dimensions of the field and its scalar dual.

The polar form $Q(x+y)-Q(x)-Q(y)$ is
\[
 {\rm Tr}\!((\sigma^{-s}(\lambda x)+\lambda\sigma^s(x)) y).
\]
Trace invariance under Frobenius gives this expression. By nondegeneracy, the radical solves $\lambda x+\sigma^s(\lambda)\sigma^{2s}(x)=0$. If there is one nonzero solution $x_0$, every other solution is $x_0$ times an element fixed by $\sigma^{2s}$, by dividing the two equations. Since $\gcd(2s,n)=2$, such a ratio is fixed by $\sigma^2$: use the integer Bezout identity for $2s,n$ and $\sigma^n=1$. There are at most $q^2$ of these ratios because they are roots of $X^{q^2}-X$. Hence the radical dimension is at most two and the polar rank at least $n-2$. The affine form domain has codimension $\mathrm{form\_pad}$. Restricting the polar form in either argument to its parallel linear space loses at most $\mathrm{form\_pad}$ ranks, by the rank of the omitted rows or columns. Therefore its rank is at least $n-2-2\mathrm{form\_pad}$, at least six in the scored shape and in the growing branch.

For an affine quadratic of rank $d$ over the fixed odd prime field, the proportion of zeros is at most $1/q+q^{-d/2}$. Indeed, use the character sum $q^{-1}\sum_{a\in\mathbb F_q}\exp(2\pi i a Q/q)$ for its zero indicator. A linear change of variables diagonalizes the quadratic part in odd characteristic, by choosing a vector with a nonzero square coefficient, completing its square to isolate it, and iterating. With $a\ne0$ a one-variable sum for a nonzero square coefficient has magnitude $\sqrt q$, even with a linear term: by completing the square the linear term is a unit-magnitude factor, and the squared magnitude of $\sum_x\exp(2\pi i c x^2/q)$ is the sum over $x,y$ of $\exp(2\pi i c(x-y)(x+y)/q)$. The map to $x-y,x+y$ is invertible, and summing first over one new coordinate gives $q$, since only the other coordinate zero has a nonzero inner sum. Every other coordinate has character sum bounded by $q$. After normalization the contribution of all nonzero $a$ to the zero probability is at most $q^{-d/2}$, and the zero character contributes $1/q$. Here $n\ge4000$ and $\mathrm{form\_pad}\le19$ give $d\ge6$, so the key weight vanishes with probability at most $1/q+1/q^3$, and in particular at most $1/q+1/q^2$.

For the search probabilities condition on all scalar coins except $y$ and the seed matrix. Set $S(z)=\sum_c\gamma_c\xi_c(z)$ on the affine form domain, a polynomial of total degree at most two. If it is identically zero, a nonzero prescribed weight always leads to primary direct normalization. Otherwise it vanishes with probability at most $2/q$ by the polynomial root bound. Independently the first factor $y(v)$ in any prescribed base is uniform and vanishes with probability $1/q$, so the base vanishes with probability at most $3/q$. For two distinct tag variants their two form values are jointly uniform on two copies of the domain: after fixing all other columns, the homogeneous column and a differing tag column give a two-by-two evaluation matrix of determinant $1$ or $-1$ in each free coefficient position. Likewise their two $y$ values are independent uniform, by the same determinant on the respective two coordinates and independently of the forms. Hence each pair of base-zero events for distinct tags has probability at most $9/q^2$. The event of one specified primary zero-corner base zero and a zero key weight of $v^{(1)}$ has probability at most $6/q^2$, by joint uniformity of their distinct tags and the key-weight bound.

The fallback requires at least one base zero among $a_0,b_0,c_0$, and either a zero secondary target weight or at least one base zero among $a_1,b_1,c_1$. Otherwise the selector gives an ordinary or direct normalization branch. The three events of the first kind paired with the secondary weight contribute at most $18/q^2$ and the nine pairs of base events contribute at most $81/q^2$. Thus fallback probability is at most $99/q^2\le135/q^2$. An ordinary secondary triple also requires a zero among the three primary ordinary bases, so its probability is at most $9/q$. All bounds hold conditional on the fixed scalar coins and therefore also unconditionally, and all selection events are independent of the integer sampler.

### Extraction and the reduction

Let $\mathcal A$ have the budget $Q<2^\lambda$ of generic group calls and at most $2^\lambda$ queries to each oracle. Fix one bit $b$ and messages $m_0,m_1$, and run the extraction experiment with $m_b$. The extractor reads the answered generic transcript without any oracle calls. It uses the protected extractor sketches for the plain sector. The empty alpha sector can be represented by zero records. It samples three independent probe vectors for each cell, uses the linear combinations of source-group records and pairings to form sketches, tests the sketches of the result and the difference when there is an old record, and directly checks its ordinary assignment against $S$, checks the three tag bits, and returns the ordinary witness only. In rank at most three, there are at most four assignments with first coordinate 1 to test: row echelon pivot coordinates determine the vector, pivot 0 must be present, and at most two remaining pivot choices are bits. Output is therefore always $\bot$ or a witness. A record creation, result, or difference touches $O(K_1N_\star+n)$ field elements, since a source-group record uses at most $K_1$ length-$(N_\star+1)$ vectors or $6A_c$ values, and the pairings compute six such combined sketch vectors. For a pairing, forming the inner products in the G2 record or summing per left leg and combining the G1 vectors uses $O(K_1N_\star+n)$ operations. A test uses $O(N_\star)$ for elimination with at most three rows and $O(N_\star+|S|)$ to generate and check the constant number of candidates. Initialization samples $6A_c(N_\star+1)$ field values, enters the $L$ labels as records whose vectors are materialized on first use, and uses $O(nN+L)$ time. There are at most four tests per result. Thus the extractor uses $O((Q+1)(nN+|S|)+L)$ time because $K_1\le n$ and $N_\star\ge1$.

The reduction on input a uniform $A\in R_q^{k\times\ell}$ samples the seed and programs the raw seed-oracle answers on columns $1,\ldots,\ell$ as $E(A_{ij})$. It samples every other answer lazily as an independent uniform tuple, including column zero, and returns the same tuple on repeated queries. Thus each programmed conceptual coefficient entry is exactly $A_{ij}$, and the raw tuple law is the same as in encryption by invertibility of $E$. If the challenge is supplied in the coefficient representation, the reduction performs these forward transforms once during its initialization. This costs $O(k(\ell+1)d_R^2)$ field operations, within $O(nD)$ for the fixed-degree scored branch because $kd_R\le n$, $\ell+1\le N+4\le D$, and $d_R$ is guarded by C5. This term belongs to $C_R$. It samples encryption coins as specified, produces the ciphertext for $m_b$, and simulates all generic labels and names and random oracles by the protected lazy tables. It runs $\mathcal A$ once. The extraction steps use the answered generic transcript without its output or the random-oracle query transcript, while the lazy tables implement exactly the direct oracle law. Because the programmed entries are jointly independent uniform ring elements for uniform $A$, all oracle answers including entries at the selected seed have exactly the joint law of the experiment. Private evaluation points are sampled independently of the run.

The reduction keeps records evaluated at its private test point, using the protected rules for guessed operands and for existing records. It tries the first GT result whose label has an existing record of different private value, using the difference expression, and also the target label's record if present. For each tried expression it computes three independent gradient vectors in the plain sector at private recovery points, tests their span for a kernel vector, and applies Euclidean LIFT with radius $B_{\rm E}$ if there is such a vector, making the selection specified in Amendment msis_bound. An output from LIFT is a short multiple of that kernel vector. The coefficient of $T^0$ in $z(v)$ is $v_0$. All $kd_R$ remaining row coefficients give the equations of $A$ on the packed input once $v_0=0$. Thus a nonzero kernel vector has $v_0=0$ and satisfies $A\hat v=0$. Its short multiple has $x_0=0$ and $\|x\|_2\le B_{\rm E}$ by that lifting algorithm. Reduction and packing commute, and packing preserves all ordinary and tag coordinates by Amendment ell and adds only zeros. This packs the output into a nonzero Euclidean-norm-at-most-$B_{\rm E}$ solution to $A\hat x=0$, exactly for the challenge whose rank, columns, bound, and norm are costed by M1. If no such output is found the reduction returns $\bot$. Denote its success probability by $s_b$. The cost is $t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT}$ with $Q_H$ the maximum per-oracle query count, $C_R=O((N_\star+n)D+\mu)$ for the fixed simulation setup and postprocessing, and $T_{\rm LIFT}$ the time of the lifting step. The reduction-time argument in C7 proves this reduction-time bound on the revised lists, including the original private record and gradient loop costs and the new fixed setup. The inverse conditions and comparison count do not enter those time calculations. The Euclidean lifting-time proof in Amendment msis_bound applies since $2B_{\rm E}<q$ and $B_{\rm E}^4<q^3$ by (I6). In particular the cost is $t+O(Q+d_R Q_H+\mu)+{\rm poly}(D,\log q)$ using $n,N_\star\le D$.

Here is how the first-mark bounds apply to these algorithms. The degree and view for the new field encoding and the needed gradient formula are derived above. The record invariant uses no inverse premise: setting all guesses to zero commutes with additions and pairings, and before the first mark every reused label comes from formally equal expressions. Formally equal target expressions have identical stacks by the fiber equations applied to their difference for every field search vector. Thus their records also have equal sketches. A good mark's stack is usable with the three field ties of Amendment C7 by the revised view. Its rank is at most three by $g^{-4}<\mu_{\rm tr}<\theta$ from (I5) and the protected stack rank bound. The full classification applies to every actual tied stack of dimension at most three, including zero-corner marks, because the three ties just derived are the original field identities. A kernel vector in its row space has coordinate 0 equal to zero, and its one-dimensional guessing probability is at least the stack's, by the protected guessing-probability lemma. The selection in Amendment msis_bound gives a short multiple at Euclidean radius $B_{\rm E}$. The amended LIFT therefore succeeds on that selected kernel vector.

At a first good difference mark its difference is formally nonzero, so the cleared polynomial is nonzero in the coins at some fixed search vector. This makes it a nonzero joint polynomial in coins and search coordinates. The private test uses independent uniform search coordinates and valid coins; the product-set bound gives failure probability at most $d_f/(q-D)$. Earlier formal equalities are equalities at every private point by the record invariant, so outside this failure the reduction picks exactly this difference. The degree bound and the uniform valid coin ranges give probability at most $\varepsilon_f$ for this failure. For a first good key mark the target record already has its expression by the record invariant and persists. Name negatives are target-group results and receive the same private and sketch tests. For a recognized good mark, the coefficient-vanishing and derivative calculation of the algebraic view subsection place each sector gradient in that sector row space. There is no nonzero alpha stack. For any proper subspace of the mark row space choose a linear form zero on the subspace and nonzero on the row space. Its value on one gradient, divided by $\pi$, is a polynomial of degree at most $n+2+2K_2$, using the seed-mode bound in the C7 degree ledger. This polynomial is nonzero by isolating the constant term in $\varepsilon$ and the distinct monomials $s_X\upsilon^{k_c}y_i$. The valid values for the independent coin coordinates have sizes at least $q-D$, by the independent coin support argument. The polynomial root bound, with $q-D$ in place of $q$ in its proof, bounds the chance of failing to increase the span while it is proper. Three independent points and rank at most three give failure at most $3(n+2+2K_2)/(q-D)\le\varepsilon_f$, by $2n\le D$ and $2K_2\le n$ and the formula for $\varepsilon_f$. Thus on a good first mark with a kernel vector, except for the two exceptional events just bounded, the reduction finds a kernel vector in the appropriate span, and produces the MSIS output. The unconditional probability of such a mark is at most $s_b+2\varepsilon_f$.

For a good first mark with no kernel vector, the classification proved in Amendment C7 gives an extended witness in its row space. Its ordinary projection satisfies the external system. In that sector the linear map from a tuple of probes to $\sum_c W_cv_c$ has image the row space, as each matrix is symmetric and the sum of its images is the row space of the stack. Uniform independent probe tuples give three independent uniform vectors in this space, even conditional on the run. In dimension $a\le3$, the chance of failing to span is bounded by $\sum_{j=0}^{a-1}q^{j-3}<2/q$: equivalently the $a$ rows of the random $a$-by-3 coordinate matrix are independent uniform three-dimensional vectors and the next row falls in the span of $j$ independent previous rows with probability $q^{j-3}$. At a difference mark the extractor tests the record difference. If the old entry is a pure guess, a guess-free difference requires the result to contain that same guessed variable with coefficient one. The label has therefore been used in an answered call, possibly the current call, and has a zero record by the test. At a key mark it tests the record of the result that obtained the target label. An initially received record has zero stack and thus is no good mark. These facts from the record invariant show that if the sampled vectors span, the witness is among the assignments tested. So the probability of a good first mark with no kernel vector and with extractor failure is at most $2/q$.

Let $u=2Q+2$. Every target query run has a first mark. The protected initial and guessed-mark estimates and the charged-mark estimate of Amendment Ncmp bound their three probabilities by
\[
(\binom{L_1}{2}+\binom{L_2}{2}+\binom{L_T}{2})\varepsilon_f,\quad
N_{\rm cmp}(u)(\theta+\varepsilon_f)
+(\binom{L+3u}{2}+L+3u)\varepsilon_f,\quad
2^\lambda/N_{\rm free},
\]
respectively. These estimates concern the same sampler, oracle and record laws and use only the already checked view and degree properties, budget, and label counts. Together with the two good-mark cases they cover the event of a target key query and no witness. Their sum is at most $s_b+E(u)$: the good-mark excess is $2\varepsilon_f+2/q\le (8u+8)\varepsilon_f$, using $\varepsilon_f\ge1/q$; the remaining terms of $E$ are nonnegative and its guess term contains $2^\lambda/N_{\rm free}$. By (P5) and the generic-ledger implication of Amendment Ncmp $E(2Q+2)\le(Q+1)/2^\lambda$. Hence for each $b$ the target-query and no-witness probability is at most $(Q+1)/2^\lambda+s_b$, with exactly the stated oracle budgets and one MSIS instance. This proves Theorem 5.9 with its extraction time and soundness as above.
