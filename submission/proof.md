# Praxis with a Euclidean coefficient-norm SIS reduction

Throughout the proof $N$ is the protected external variable count and $N_*=N_o+3$ is the number of internally sampled box coordinates. The padding and three tags preserve the external witness relation. The construction, coefficient placement and probabilities for the amended model follow.

## Amendment C5

Put $N_o=N+689$ and $N_*=N_o+3$. Write $d=d_R$, $h_R={\rm ring\_log}$, $p={\rm pack\_digits}$, $p_f={\rm form\_pad}$, $s_0={\rm seed\_degree}$, $A_c=3n/2$, $S_0=\lceil(D-1)/ν\rceil$, and $m=k(ℓ+1)d$. Write $U_d=V_d=33$ and $s_p={\rm short\_columns}$. Require ${\rm ring\_mode}=d=17$, $h_R=0$, and $(q\bmod613)^{36}\equiv1\pmod{613}$. Require $λ=100$, $N=391693$, $ν=2048$, $n_c=1692$, $p=17$, $s_p\in\mathbb Z$, $0\le s_p$, $15s_p\le N_o$, $p_f\in\mathbb Z$, $3\le p_f\le d$, $n=4392$, $s_0=61$, $K_1\ge K_2+1$, $K_2=18$, $J\le24$, and $m\ge55000000$. The scalar arithmetic guard is $W+V\le 3m$, where $W$ and $V$ are the following integers:
\[
 W=d((ℓ+1)(3\lfloor k/2\rfloor+2(k\bmod 2))+2\lfloor k/2\rfloor)
       +2(U_d k+V_d(ℓ+1)),
\]
\[
 \begin{split}
 V={}&2D+N_o+n_c+2099+(2K_1+6K_2+6)(N_o+4)+2K_2\\
    &+(Δ-Δ/ν+2S_0+16)+(J+3)A_c+C_{\rm mask}\\
    &+276624+60(n+J+1)+10000+45962+(N_o+1)+100\\
    &+3653061+J .
 \end{split}
\]

The guard uses the protected value $m$. The prime conductor is $p_0=613$ and a generator of its nonzero residues is $a_0=2$. For primality the remainders at the primes up to $\sqrt{p_0}$, in increasing order, are $1, 1, 3, 4, 8, 2, 1, 5, 15$. For the generator the pairs consisting of a prime divisor $p$ of $p_0-1$ and the residue $a_0^{(p_0-1)/p}\bmod p_0$ are $(2,612), (3,65), (17,586)$. None of the former is zero and none of the latter residues is one. Put $H=\langle a_0^d\rangle$ of size $f=36$ in the cyclic group. For a primitive complex $p_0$-th root $\zeta$, define the period $g_i=\sum_{u\in a_0^iH}\zeta^u$, with indices modulo $d$ and exponents in $\{1,\ldots,p_0-1\}$. The polynomial $1+X+\cdots+X^{p_0-1}$ is irreducible over $\mathbb Q$ by Eisenstein at $p_0$ after substituting $X=1+T$. The checked $q^f\equiv1\bmod p_0$ puts $q\bmod p_0$ in $H$ and gives a primitive $p_0$-th root $\omega$ in $\mathbb F_{q^f}$.

The periods are linearly independent over $\mathbb Q$: a rational linear relation gives a polynomial of degree at most $p_0-1$, with zero constant term, divisible by $1+X+\cdots+X^{p_0-1}$. This polynomial is zero, and the disjoint cosets make every coefficient in the relation zero. The period sum is $-1$. Products of periods are integer combinations of the periods and $1$, because the number of ordered exponent pairs producing a given sum modulo $p_0$ is invariant under multiplication of that sum by an element of $H$. Thus their integer span is an order $R$: a free rank-$d$ unital subring of their rational span. Its actual coefficient basis is
\[
 b_0=1,\ b_j=g_{j-1}\ (1\le j<d).
\]
The transition between this and the period basis is integral with integral inverse, using the relation $1=-\sum_jg_j$. Both transitions use only additions and sign changes. In particular $b_0$ is the ring unit, as needed for tag packing and the independent homogeneous column.

For $\omega$ a primitive $p_0$-th root over the scalar field, the $d$ substitutions $\zeta\mapsto\omega^{a_0^i}$ induce scalar-valued ring maps, since $q\bmod p_0$ belongs to $H$. With period coordinates, the matrix $F$ of their simultaneous evaluation has entry $F_{ij}=\bar g_{i+j}$. Let $s$ be the index of the coset of $-1$, $P_{i,j}=1_{j-i=s\bmod d}$, and $J_d$ be the all-ones matrix. Then
\[
 FF^{\top}=p_0P-fJ_d.
\]
Indeed, $\sum_j\bar g_{i+j}\bar g_{k+j}$ enumerates each $x\in\mathbb F_{p_0}^\times$ once as the first exponent, and sums $\omega^{x(1+a_0^{k-i}h)}$ over $h\in H$ as the second exponent varies. Each inner sum over $x$ is $-1$ unless $1+a_0^{k-i}h=0$, when it is $p_0-1$. There is one such $h$ exactly when $k-i=s$. The row sums of $p_0P-fJ_d$ are $1$. If it annihilates a vector over $\mathbb F_q$, summing the coordinates first gives coordinate sum zero, and $p_0P$ then annihilates that vector, which must be zero since $p_0\ne q$. This proves that evaluation $E$ in the basis $b_j$ is an algebra isomorphism $R/qR\simeq\mathbb F_q^d$. Independently uniform coefficients in this basis therefore yield exactly uniform split tuples, in both directions.

Fix the scalar tables. For $b_a=\sum_{i<d}a^ig_i$ the difference of any two character values is a nonzero polynomial of degree below $d$, because the characters differ on the basis. Thus at most $(d-1)\binom d2<q$ choices cause a coincidence. In residue order take the first $a$ with squarefree characteristic polynomial of multiplication by $b_a$, computed by the period product rule and a derivative gcd. The split isomorphism diagonalizes multiplication, so this test detects exactly the required distinct values. Take the least root $r$ of that split polynomial. The powers of $b_a$ through degree $d-1$ form a basis by the Vandermonde determinant. Express each $g_i$ in this basis and evaluate at $r$ to get one character. Order the others by its cyclic shifts. Precompute these public tables.

### Ring arithmetic and transpose

The period matrix is fixed cyclic convolution after an index reversal. Its inverse is also a cyclic convolution followed by reversal, since the inverse of the invertible convolution commutes with the shift. A transpose reverses the convolution kernel. Thus each of the four maps uses one fixed cyclic convolution and additive basis changes. To compute the cyclic convolution, compute an ordinary product and fold its coefficients modulo $X^d-1$ by additions.

For two ordinary length-seventeen coefficient vectors, let $f$ be the dynamic degree-at-most-sixteen polynomial and $g_0$ the fixed one. Evaluate at the 32 integers $S=\{-15,-14,\ldots,16\}$ and at infinity, meaning the degree-sixteen coefficient on each input. Distinct points stay distinct in this scalar field. Put $Q(X)=\prod_{a\in S}(X-a)$. Public setup tabulates the 32 fixed factors $g_0(a)/Q'(a)$ and the leading coefficient $[X^{16}]g_0$. Thus the dynamic leaf products are
\[
 v_a=f(a)g_0(a)/Q'(a)\quad(a\in S),\qquad
 v_\infty=[X^{16}]f [X^{16}]g_0 .
\]
There are 33 such field multiplications. Recover the ordinary product by
\[
 v_\infty Q(X)+\sum_{a\in S}v_a Q(X)/(X-a).
\]
Both sides have the same degree-thirty-two coefficient and the same 32 finite values. Their difference has degree at most 31 and 32 distinct roots, hence vanishes. Fold by $X^{17}-1$ and perform the additive basis changes already stated.

Use Horner at $|a|\le16$, each step costing at most seven additions including the update. For interpolation let $N_A=\sum_{a\in A}v_a\prod_{b\in A\setminus\{a\}}(X-b)$. Split each non-singleton $A=A_1\sqcup A_2$ evenly. Multiply $N_{A_i}$ successively by the other half's linear factors and add the results. At size $t$ this costs at most $7t^2+t$ additions. The squared sizes over the levels sum to at most $2048$ and the sizes at most $160$. Form $v_\infty Q$ by 32 such linear factors at cost $7\cdot32\cdot33$. The Horner charge is at most $3584$ and final sum, fold and basis changes cost under 100. Thus each map uses under 26000 additions without arbitrary scalar repeated addition.

Each of the four ring maps therefore uses at most 33 multiplications. For a common output factor on one leg, scale its 33 stored leaf factors once; linearity then scales every output while the cost per applied transform stays 33 products.

### Seed-oracle encoding

At each existing seed and entry index, the raw answer is a uniform independent tuple in $\mathbb F_q^{d_R}$ in evaluation-map order, reused on repeated queries. The conceptual ring entry is its inverse under the bijection $E$, hence uniform in the integral coefficient basis. Encryption and decryption consume the tuple directly, so no per-entry forward transform is needed. $W$ charges the transforms of the mask functionals and accumulated columns. Targets programs the same representation from the uniform coefficient challenge.

### Kernel conversion and scope

Amendment n identifies the kernel, and msis_bound and msis_norm prove coefficient-norm packing and lifting. The seed law and actual form map used in C6, C7 and Targets are independent of ring arithmetic.

For the regular right list require $(J-1)∆+N_o+5+2195\le2D-2$.

## Amendment I2

Use $R_{\rm tr}\ge18$ and require
\[
1000\exp(-99 R_{\rm tr}^2 N/(200(N+692)))\leε_{\rm tr}.
\]
The remaining requirements are $ε_{\rm tr}<μ$, $g^5μ>1$, and $μ<μ_{\rm tr}$, where $μ=θ-100ε_{\rm tr}$. The actual covariance trimming radius is $\widehat R=R_{\rm tr}\sqrt{N/(N+692)}$, with $N_*=N_o+3$. I3 proves the upper tail $10^d\exp(-99\widehat R^2/200)$ by Markov's inequality. For counting use the enclosing ellipsoid of radius $R_{\rm tr}\ge\widehat R$, as in I3.

Any projected feature-row deviation from the center is at most $\widehat R(g/\sqrt{12})\sqrt{N_*}$ times that row's coefficient sup norm by Cauchy--Schwarz. A difference doubles this bound, which gives $R_{\rm tr}g\sqrt{N/3}=T_{\rm tr}$ as the factor. The determinant and lifting comparisons in I5 and I6 therefore use the protected definition of $T_{\rm tr}$. The other uses concern the trimming loss and the enclosing ellipsoid.

## Amendment I3

The amended (I3) is
\[
Λ_1\ge 2\sqrt3 R_{\rm tr}\sqrt N_*,\qquad
Λ_2\ge \sqrt2 π R_{\rm tr}^2 N_*,\qquad
Λ_3\ge \frac{20 π R_{\rm tr}^3 N_*\sqrt N_*}{9\sqrt2} .
\]
The rank-two and rank-three geometric lower bounds change. All three inequalities here are checked by the parameter model.

### Which inverse-theorem steps use the change

P3 includes I3. Other admissibility tests are independent of $Λ_i$. The unchanged lattice operations define all prefixes and fibers. The strong regularity bound $mh\leγ_d/g^d$ implies the original one. I2 gives the trimming loss, and mu_tr proves B.18(c) and the actual rank-three rule. The projected counts below feed I3 regularization and I6 inversion.

### Integer-lattice facts used below

For an integral basis $B$ with a largest row minor on $J$, each component of $y\in{\rm span}_{\mathbb R}B$ is $B_iB_J^{-1}y_J$, with entries of the row $B_iB_J^{-1}$ bounded by one in absolute value by Cramer's rule and maximality of the minor. The component is therefore at most $\|y_J\|_1$ in absolute value. When the columns of $B$ generate a saturated integer lattice, their quotient in the ambient free integer group is torsion-free and finitely generated, hence free. Extending these columns by lifts of a quotient basis gives a unimodular basis of the ambient group. Taking its transpose shows $B^\top\mathbb Z^I=\mathbb Z^d$.

For the lifting fact, let $Δ$ be an integer matrix of rank $k'>0$ with a nonzero minor $M$ of order $k'$ on rows $I_0$ and columns $J_0$. Put $δ=\det M$. Assume $δ\ne0\bmod q$, so $M$ is invertible modulo the prime $q$. Given $c^\topΔ=0\bmod q$, write $I_1$ for the remaining rows and choose an integer vector $w\equivδ^{-1}c_{I_1}\bmod q$. Set $u_{I_1}=δ w$ and $u_{I_0}^\top=-w^\topΔ_{I_1,J_0}{\rm adj}M$. Then $u^\topΔ_{J_0}=0$ by the adjugate identity. Those columns span the column space over $\mathbb Q$, so $u^\topΔ=0$. The inside rows also agree with $c$ modulo $q$, by uniqueness of the solution for them using $M$ invertible modulo $q$. For rank zero take $u=c$. These facts use no inverse-parameter condition other than the nonzero modular minor at the lifting step.

### Prefix estimates

Here are the unchanged parts of the prefix lemma on the amended parameter domain. Let $Θ$ be a saturated lattice of rank $d$, with integral basis matrix $B$ and a largest minor on $J$. Order its coordinates with $J$ first, let $I_k$ be the first $k$ coordinates, and let $Θ_k={\rm span}_{\mathbb R}(B_{I_k})\cap\mathbb Z^{I_k}$, $k\ge d$. Let $h_k,m_k$ be its height and largest fiber density. Its rank is $d$ because the selected minor remains invertible. If $Y$ is a basis of $Θ_k$, then $B_{I_k}=Y C$ for an integral nonsingular $d$-square matrix $C$. The fibers of the prefix are thus the level sets of $B_{I_k}^{\top}r$. The group $G_k=B_{I_k}^{\top}\mathbb Z^{I_k}=C^\top\mathbb Z^d$, by saturation and the integer-lattice lemma (b), has index $|\det C|$ in $\mathbb Z^d$. The $d$-row determinants of $B_{I_k}$ are multiplied from those of $Y$ by $\det C$. As their largest absolute value is the original $h(Θ)$, this gives $h_k [\mathbb Z^d:G_k]=h(Θ)$ and shows that $J$ is still a largest minor for $Θ_k$. At $k=d$, the column span is all of $\mathbb R^J$, so $Θ_d=\mathbb Z^J$, $h_d=1$ and $m_d=g^{-d}$. At the full set of coordinates the saturated lattice is $Θ$.

On adding the next row to $B_{I_k}$, let $s_k$ be the order of that row as a column in the quotient $\mathbb Z^d/G_k$. Adjoining it multiplies the size of the subgroup modulo $G_k$ by $s_k$, so $h_{k+1}=s_k h_k$ by the index identity. For a fixed value of $B_{I_{k+1}}^\top r$, the new coordinate is in at most one residue class modulo $s_k$; its allowed values in an interval of $g$ integers number at most $\lceil g/s_k\rceil$. For each such value the remaining prefix has fiber density at most $m_k$. Consequently $m_{k+1}\le m_k\lceil g/s_k\rceil/g$. If $s_k\ge g$ this also makes the new coordinate constant on the fiber. If $s_k=1$, the power inequality $m_{k+1}^b h_{k+1}^{b-1}\le m_k^b h_k^{b-1}$ is immediate. For $2\le s=s_k<g$, use $\lceil g/s\rceil/g\le 1/s+1/g\le s^{-1+1/b}$. To verify the second inequality, if $s\ge2^b$ then $1/s+1/g<2/s\le s^{-1+1/b}$. Otherwise $g\ge2^b$ and the concave function $x^{1/b}-1-x/2^b$ is nonnegative on $[2,2^b]$: it is zero at $2^b$, and at $2$ it is at least $(\log 2)/b-2^{1-b}>0$ for $b\ge7$. The last strict inequality follows from $\log 2>1/2$ and $2^{b-2}>b$ for integers $b\ge7$. This proves the power inequality in all its cases.

Rank-three regularity and the sparse rank-four case are proved in mu_tr.

### Trimming estimate

For the trimming lemma, a centered uniform box entry can be added to a uniform independent variable on $[-1/2,1/2]$ to get the continuous uniform variable on $[-g/2,g/2]$. The added variable's moment generating function is at least one by convexity, so the centered box entry has moment generating function bounded by $\sinh(x)/x$ with $x=tg/2$ at argument $t$. Its series is bounded by $e^{x^2/6}$ because $(2j+1)!\ge6^j j!$ for $j\ge0$, by induction on $j$. Let $Y=B^\top r-\mathbb E[B^\top r]$ and $\Sigma=(g^2/12)B^\top B$. Independence of the box entries gives $\mathbb E e^{u^\top Y}\le e^{u^\top\Sigma u/2}$. With $Z$ an independent standard $d$-dimensional Gaussian, the Gaussian moment generating function gives
\[
 \mathbb E e^{(99/200)\|\Sigma^{-1/2}Y\|_2^2}
 =\mathbb E e^{\sqrt{99/100} Z^\top\Sigma^{-1/2}Y}
 \le \mathbb E e^{(99/200)\|Z\|_2^2}=10^d .
\]
The inequality conditions on $Z$; the last equality follows by scaling each normal density in the integral. By Markov's inequality the probability of being outside the trimming ellipsoid is at most $10^d e^{-99\widehat R^2/200}\leε_{\rm tr}$ by (I2) and $d\le3$. Trimming any subset removes at most that absolute density. This establishes the trimming conclusion without a norm assumption.

### Projected fiber counts

The claim of `lem:sparse` is as follows. Let $B$ be a basis of an integral lattice $Θ$ on $I\subseteq[N_*]$, of rank $d\in[3]$. Take $i'\in[N_*]\setminus I$. Let $F\ne\varnothing$ be a set in the box on $I\cup\{i'\}$ trimmed by $Θ$, and $\Phi(r)=(B^\top r_I,r_{i'})$. If (a) $\Phi(F)$ has affine dimension $d+1$ and lies in a coset of an index-$q$ subgroup of $\mathbb Z^{d+1}$, then
$\Pr[F]\leΛ_d g^d h(Θ)m(Θ)/q$.
If (b) $F^\perp$ has rank $d'$ with $1\le d'<d$, a largest minor on $J\subseteq I$, and every vector of $F^\perp$ restricts to a vector in ${\rm span}_{\mathbb R}Θ$ on $I$, then
$\Pr[F]h(F^\perp)\leΛ_{d-d'} g^{d-d'}h(Θ)m(Θ)$.
Here $F^\perp$ is the lattice of integer vectors normal to the differences in $F$.

For each possible image $(y,x)$, the probability of $B^\top r_I=y,r_{i'}=x$ is at most $m(Θ)/g$ by independence, so $\Pr[F]\le|\Phi(F)|m(Θ)/g$. We count images in $C=\mathcal{T}_Θ\times[2,g+1]$.

For (a), put $s=d+1$, $δ=q$, $J=\varnothing$, and let $p$ be the identity. Write $B=(B_1,B_2)$ with $B_1$ empty, and use $|\det(B_1)_J|=1$.
For (b), put $s=d+1-d'$ and let $Y$ be an integral basis matrix of $F^\perp$; $Y_J$ is invertible. The submatrix $B_J$ has row rank $d'$ since the columns $Y_J$ lie in its real column span. The integral kernel of $B_J$ is saturated in $\mathbb Z^d$, of rank $d-d'$. It has a basis that extends to an integral basis of $\mathbb Z^d$: the quotient by a saturated subgroup of $\mathbb Z^d$ is finitely generated and torsion-free, hence free, and lifts of a quotient basis give the extension. Using this basis change, write $B=(B_1,B_2)$ where $(B_2)_J=0$ and $(B_1)_J$ is invertible square. The columns of $B_2$ number $s-1$. Trimming is basis independent since the mean and covariance transform by the same invertible change on the image coordinates.

In case (b), the injective map $a=(a_{[d]},a_{d+1})\mapsto(Ba_{[d]},a_{d+1})$ maps the real annihilator of the differences of $\Phi(F)$ isomorphically onto the real annihilator of the differences of $F$, by the restriction assumption. The first annihilator has dimension $d'$ and its integer points form a saturated lattice with basis matrix $V$. The real annihilator of differences of $F$ is spanned by its integer points because those differences are integer vectors, so the restriction premise on integer normals suffices for this isomorphism. Split its rows into $V_1,V_2,V_3$ of lengths $d',s-1,1$. The image of its basis is $Y A$ for an integral nonsingular $d'$-square matrix $A$, as its columns are integral independent normals. At rows $J$, this gives
\[
(B_1)_J V_1=Y_J A .
\]
Consequently $V_1$ is invertible and $|\det(B_1)_J| δ\ge h(F^\perp)$, where $δ=|\det V_1|$. Write $y=(y_1,y_2)$ according to the basis split. Projection $p:(y,x)\mapsto(y_2,x)$ is injective on any affine translate of the kernel of $V^\top$, because there the first block of a difference is determined by $V_1^\top$. It therefore preserves the affine dimension of $\Phi(F)$, which is $s$. The projections of differences of image points lie in the kernel of
\[
 (y_2,x)\longmapsto V_2^\top y_2 + x V_3^\top
          \pmod{V_1^\top\mathbb Z^{d'}} .
\]
The map is onto because $V^\top \mathbb Z^{d+1}=\mathbb Z^{d'}$ by saturation and `lem:lattice-facts` (b), while the $y_1$ contribution vanishes in the quotient. The kernel has index $δ$ in $\mathbb Z^s$. Thus in both cases $p(\Phi(F))$ has full affine dimension $s$, cardinality $|\Phi(F)|$, and lies in $p(C)$ and in a coset of an index-$δ$ lattice.

A full-dimensional finite set $X$ of $m$ points in such a coset has ${\rm vol}_s{\rm conv}(X)\ge(m-s)δ/s!$. To see this, start from any $s+1$ affinely independent points forming a simplex. One can add the points successively while maintaining a triangulation of their hull using all inserted points as vertices. For a point outside the hull, each boundary facet simplex strictly visible to the point gives a new simplex by coning it to the point. Those simplices have disjoint interiors and fill the new region, as rays from the point first hit the old hull in its visible boundary. At least one facet is strictly visible, so at least one full simplex is added. If a point is in the hull, take the unique smallest face of the triangulation containing it. This face has positive dimension since the point is distinct from all earlier vertices. Subdivide that face by coning its boundary faces to the point and make the corresponding subdivision of every full simplex incident to it, by adjoining the complementary simplex vertices. This covers exactly those full simplices and replaces each by at least two, since the point lies in the relative interior of the face. Hence there are at least $m-s$ full simplices. Each has volume at least $δ/s!$, since the determinant of $s$ independent differences of coset points is a nonzero integer multiple of the determinant $δ$ of its lattice. Since $m\ge s+1$, the region containing $X$, if convex, has volume at least $δ/s!$. In particular, applying both consequences to $p(C)$ gives
\[
 |\Phi(F)|\le s!{\rm vol}_s p(C)/δ+s
             \le (s+1)!{\rm vol}_s p(C)/δ .
\]

The projection of the ellipsoid $\mathcal{T}_Θ$ to the last $s-1$ coordinates has volume at most $v_{s-1}R_{\rm tr}^{s-1}(g/\sqrt{12})^{s-1}\sqrt{\det(B_2^\top B_2)}$, where $v_j$ is the volume of the Euclidean unit $j$-ball. Indeed, write its enclosing ellipsoid as the image of a unit ball by $R_{\rm tr}\Sigma_Θ^{1/2}$ plus the center. The projected map has a Gram matrix on its range equal to the bottom-right block $R_{\rm tr}^2(g^2/12)B_2^\top B_2$, which gives the product of its nonzero singular values. The interval in $p(C)$ has length $g-1$. In either case $(B_2)_J=0$. By expansion of $\det(B_2^\top B_2)$ into squared row minors, and because $|\det(B_1)_J\det(B_2)_{J'}|=|\det B_{J\cup J'}|\le h(Θ)$ for each $J'\subseteq I\setminus J$ of size $s-1$,
\[
 |\det(B_1)_J| \sqrt{\det(B_2^\top B_2)}
 \le h(Θ)\sqrt{\binom{N_*}{s-1}} .
\]
Combining with the counting bound and $\Pr[F]\le |\Phi(F)|m(Θ)/g$ gives
\[
 \Pr[F]|\det(B_1)_J|δ
 \le g^{j}h(Θ)m(Θ)
      (j+2)!v_j R_{\rm tr}^{j}\sqrt{\binom{N_*}{j}/12^j},
 \ j=s-1 .
\]
Use $\binom{N_*}{j}\le N_*^j/j!$ and $v_1=2,v_2=π,v_3=4π/3$. The three upper bounds on the geometric factor are $2\sqrt3 R_{\rm tr}\sqrt N_*$, $\sqrt2π R_{\rm tr}^2N_*$, and $20π R_{\rm tr}^3N_*^{3/2}/(9\sqrt2)$. They are at most the three allowed $Λ_j$. In case (a), divide by $q$ to obtain the claim. In (b), replace $|\det(B_1)_J|δ$ by $h(F^\perp)$ on the left to obtain the claim.

For a regular rank-four lattice case (b) applies for $d'=1,2,3$. Its feature box lies in the standardized ellipsoid of radius eleven: whitening is orthogonal projection of at most forty centered physical box coordinates of magnitude at most $g/2$, giving squared radius at most 120 in units $g^2/12$. No trimming is needed. The Cauchy--Binet sum has at most forty supported rows. Thus the geometric factors for $j=1,2,3$ are bounded by $(j+2)!v_j 11^j\sqrt{\binom{40}{j}/12^j}$, below $242,22000,1610000$ respectively.

### Regularization with the new count

This subsection proves regularization under the growth conditions in Amendment I4.

The claim of `lem:regularize` is that a saturated lattice $Θ$ on $I\subseteq[N_*]$ of rank $d\in[4]$ with $m(Θ)\geμ+(4-d)ε_{\rm tr}$ is contained in a regular saturated lattice of rank in $[d,4]$ and maximum fiber density at least $m(Θ)-(4-d)ε_{\rm tr}$.

Write $e=ε_{\rm tr}$ in this paragraph and the next two. Induct downwards on rank for all such $I$ simultaneously. Each recursive normal and its regular extension use the same prefix coordinates. An extension is only to the next coordinate of $I$. At rank four use the sparse basis of mu_tr. At rank three use the full-normal rule of mu_tr, with its possible single deletion before a rank-four return. Any recursive return of rank three has passed through this case. Hence all rank-three trimming lattices and all rank-three outputs in the inverse induction are full normals of their untrimmed densest fibers. Use the height bound only for those outputs. For $d\le2$, use `lem:prefix` with a largest minor at $J$ and $J$ first in the coordinate order. Denote the prefixes by $Θ_k$, their heights and max densities by $h_k,m_k$, and the step order by $s_k$. The densities are nonincreasing, so each is at least $μ+(4-d)e$. Take a densest fiber of $Θ_k$ to form $F_k$. If the preceding $F_{k-1}^\perp$ strictly contains $Θ_{k-1}$, trim this fiber if the preceding regular lattice has rank at most three, using the lattice $\widetildeΘ_{k-1}$ specified below. Otherwise leave the fiber whole. The density of each $F_k$ is at least $m_k-e$ by `lem:trim`. Its normal lattice contains $Θ_k$. If this inclusion is strict, saturation gives a rank $d_k>d$. Its rank is at most four since a fiber of a rank-$a$ lattice has density at most $g^{-a}$ by fixing coordinates outside an invertible $a$-row minor, and $g^{-5}<μ\le m_k-(4-d)e$ by (I5). Its max fiber density is at least $\Pr[F_k]\geμ+(3-d)e\geμ+(4-d_k)e$. By induction let $\widetildeΘ_k$ be a regular saturated containing lattice of rank at least $d_k$, with $m(\widetildeΘ_k)\ge m(F_k^\perp)-(4-d_k)e\ge m_k-(4-d)e$. This constructs the trimming lattice for the next step, and if $F_{|I|}^\perp\neΘ$ it gives the desired final lattice.

If $F_{|I|}^\perp=Θ$, let $j<|I|$ be the last strict index, or $j=d-1$ when there is none. For $j<k<|I|$ the step order $s_k$ is below $g$. Otherwise `lem:prefix` (b) would make the new coordinate constant in the fiber of $Θ_{k+1}$ containing $F_{k+1}$; its unit vector would then be in $F_{k+1}^\perp=Θ_{k+1}$ and vanish at $J$, forbidden by `lem:lattice-facts` (a). Iterating the power inequality in `lem:prefix` (b) gives
\[
 μ(m(Θ)h(Θ))^{b-1}
 \le m(Θ)^b h(Θ)^{b-1}
 \le m_{j+1}^{b}h_{j+1}^{b-1}.
\]
When $j=d-1$, $m_d=g^{-d}, h_d=1$. The bound on $γ_d^{b-1}$ in (I4) gives $m_d^{b}h_d^{b-1}\leμ(γ_d/g^d)^{b-1}$.

When $j\ge d$, let $\tilde d$ be the rank of $\widetildeΘ_j$. The set $F_{j+1}$ uses this lattice for trimming in ranks at most three and is whole in rank four. Its normal lattice is exactly $Θ_{j+1}$, of rank $d<\tilde d$, and with largest minor on $J$ by `lem:prefix` (a). Restrictions to the first $j$ coordinates lie in the span of $Θ_j$ by the definition of the prefix lattice, hence in the span of $\widetildeΘ_j$. Apply projected count (b), with the smaller support constants when $\tilde d=4$. Since $\Pr[F_{j+1}]\ge m_{j+1}-e\ge m_{j+1}/A_{\rm inv}$ by (I4) and $m_{j+1}\geμ$, the stronger induction bound gives
\[
 m_{j+1}h_{j+1}\le A_{\rm inv}L_{\tilde d,d}γ_{\tilde d}/g^d .
\]
Also $m_{j+1}\le m_j\le\Pr[F_j]+e\le g^{-d-1}+e\leμ P_d^{b-1}$ by the rank of $F_j^\perp$ and (I4). For $d=1$, (I4) allows $2e$ in the numerator and therefore implies the same inequality. Set $L_{\tilde d,d}=Λ_{\tilde d-d}$ for $\tilde d\le3$. In rank four $Γ_4=2$ and $2L_{4,2}\le44000<Λ_1Γ_3$, $2L_{4,1}\le3220000<Λ_2Γ_3$ by I3 and $Γ_3\ge9$. Thus (I4) gives $A_{\rm inv}L_{\tilde d,d}γ_{\tilde d}P_d\leγ_d$. Multiplying yields $m_{j+1}^b h_{j+1}^{b-1}\leμ(γ_d/g^d)^{b-1}$. Now $b>1$ and $μ>0$ give $m(Θ)h(Θ)\leγ_d/g^d$. This proves regularity and finishes the induction.

B.21 also holds verbatim at $μ_{\rm tr}$. Run the same induction with $μ_{\rm tr}$ replacing $μ$ and rank cap three. The rank-three base is B.18(c). For $d\le2$, every trimmed fiber has mass at least $μ_{\rm tr}+(2-d)e$, exceeding $g^{-4}$, so no normal has rank four. For each strict inclusion the input mass is at least $μ_{\rm tr}+(3-d_k)e$ since $d_k\ge d+1$. The recursion loses at most $(3-d)e$ including the current trimming. The base and last-strict-index inequalities use (I4) at $μ_{\rm tr}$, which follows from (I4) at $μ$ because the density denominators increase and $x/(x-e)$ decreases. These inequalities prove the same stronger regularity, which implies regularity with the original $Γ_d$.

## Amendment I4

Require $g^2\le2^{40}\cdot2^λ$ and $γ_i μ_{\rm tr}\le Γ_i μ$ for $i=1,2$, together with
\[
\begin{gathered}
 Γ_3\ge9ξ_{\rm tr},\qquad
 A_{\rm inv}\geμ/(μ-ε_{\rm tr}),\\
 P_2^{b-1}\ge(g^{-3}+ε_{\rm tr})/μ,\qquad
 P_1^{b-1}\ge(g^{-2}+2ε_{\rm tr})/μ,\\
 γ_2^{b-1}\ge g^{-2}/μ,\qquad
 γ_1^{b-1}\ge g^{-1}/μ,\\
 γ_2\ge A_{\rm inv}Λ_1Γ_3P_2,\qquad
 γ_1\ge A_{\rm inv}\max\{Λ_1γ_2,Λ_2Γ_3\}P_1 .
\end{gathered}
\]
The upper range gives $\sqrt g\le 2^{10}2^{λ/4}$, so the expected $O(\sqrt g N_*^{1/4})$ group work is $O(2^{λ/4}N_*^{1/4})$ for the common efficiency derivation.

I3 uses these inequalities for regularization. The unchanged $H_2\geγ_2/(g^2μ)$ bounds the height by the stronger induction inequality. I5–I6 use these bounds for the minor tests and inverse. Trimming and sparse counting depend on the basis, covariance and fiber density, as shown in I3.

## Amendment mu_tr

Set $μ_{\rm tr}=9ξ_{\rm tr}/(8g^4)$, the cutoff for B.18(c), giving $H_3=8g$. Write $e=ε_{\rm tr}$. For the actual inverse use $μ=θ-100ε_{\rm tr}<μ_{\rm tr}$, inverse parameters $γ_i$ (gamma1_inv, gamma2_inv) for $i=1,2$, and $γ_i=Γ_i$ for $i=3,4$ with $Γ_4=2$. The I4 guards give $H_i=Γ_i/(g^iμ_{\rm tr})\geγ_i/(g^iμ)$ for $i=1,2$. The I3 induction proves $mh\leγ_d/g^d$ and hence original regularity. I2 proves the trimming loss, I3–I4 the sparse count and regularization, and I5–I6 admissibility and inversion. Other lattice and fiber definitions have no cutoff.

B.18(a),(b) are proved in I3. At the actual cutoff, for saturated rank three of mass $m\geμ+e$, start with the full normal of an untrimmed densest fiber $F$. It contains the input and has mass $m$, since $F$ is a fiber for both and other fibers only shrink. If it has rank four it is already sparse and regular. At rank three it equals the input, and the bounds below give the desired regularity and height or promote to rank four after a deletion of mass at most $e$. At the higher cutoff $μ_{\rm tr}>g^{-4}$ the full normal remains rank three, and every suffix order is below $g$ by B.18(b). The all-small height estimate below applies directly, giving $h\le H_3$ and regularity as in B.18(c).

### Large moduli and sparse normal rows

Write $ρ_0=417/1000$. A rank-$d$ box fiber has mass at most $g^{-d}$ by fixing nonpivots. If $d=4$ with mass at least $μ$, or $d=3$ with mass at least $gμ$, each reduced pivot equation succeeds on its independent nonpivots with probability at least $g^4μ\ge417/1000$.

For a cyclic equation $y+\sum a_j x_j=c\pmod s$ with $s\ge7g/2$, fix all inputs but a chosen $x$ at offsets achieving success $ρ_0$. Its successful $(x,y)$ pairs are in a square of side $g$, on a coset of a determinant-$s$ lattice. A shortest primitive direction has maximum norm $m_0\le4\sqrt g$ by pigeonholing the $ρ_0g$ pairs in squares of side $4\sqrt g$. Swap axes for counting so the horizontal component has magnitude $m_0$. Parallel lines are spaced $s/m_0$ in the ordinate $y-\lambda x$, where $|\lambda|\le1$. They number at most $2gm_0/s+1\le 3\sqrt g+1$. At fixed $x$ at most $\lceil gm_0/s\rceil$ chords cross the half-open square. Total horizontal lengths divided by $m_0$, plus the number of chords, bounds the count. For $m_0=3$ or $m_0\ge5$, $\lceil2m_0/7\rceil/m_0\le2/5$ (check 3 and 5 through 8, then use $2/7+1/m_0$). Thus the count is below $(2/5)g+3\sqrt g+1<ρ_0g$.

If $m_0=4$ and $\lambda\ne0$, lines are separated by at least $.85g$, so at most three chords occur. For two chords the overlap of their horizontal domains is at most $.15g/|\lambda|\le.6g$ as $|\lambda|\ge1/4$. For three chords the ordinate range requires $|\lambda|\ge.7$, and the adjacent overlaps total at most $.3g/.7$. In either case the total lengths are at most $1.6g$, giving at most $.4g+3$ points. Thus only a horizontal direction of length four survives. A vertical direction of that length in the original axes is impossible since $s>4$. In the horizontal original axes it means the slope has exact order four. For $m_0\le2$, the direction $(d,e)$ has $d\ne0$ and $da+e=0\pmod s$, so the slope is an integer of magnitude at most two, or $s/2+k/2$ with signed $|k|\le2$.

Translate the boxes to $0,\ldots,g-1$ and shift the target. The disjoint slope classes are ordinary $a=0,\pm1,\pm2$; half-period $a=s/2+k/2$, $|k|\le2$; or exact order four $a=us/4$, $u$ odd and $4\mid s$. These descriptions are modulo $s$ and disjoint at this large $s$. For the half-period inputs write $x=2z+π$. The quotient $z$ is uniform on $0,\ldots,g/2-1$, independently of the uniform bit $π$, and the term is $kz+(s/2)π+(k/2)π$. For an order-four input write $x=4z+π$ with independent uniform quotient and residue modulo four, giving just $(us/4)π$. The other inputs retain their ordinary contributions. These are product laws because $4\mid g$ makes all quotient-remainder pairs equally frequent. Let $S$ sum the ordinary terms and the $kz$ terms. The remaining small displacement $E=\sum (k/2)π$ has $|E|\le N_*$; enlarge the target to length $g+2N_*$ to remove $E$ pointwise, before any conditioning.

Fix the unselected residual inputs. Independent uniform $[-1/2,1/2]$ jitter extends $m$ consecutive uniform integers to a uniform interval of length $m$. For step $b$, its contribution has smoothed width $w=m|b|$ and moves by at most $|b|/2$. The discrete event implies smoothed success in the interval enlarged by total length $\sum |b|$, including modulo $L$. At period $L$ a width $w>0$ folds to density at most $\lceil w/L\rceil/w$ almost everywhere, by counting lifts at each point. Convolution with independent terms averages its translates and keeps this bound. Thus the enlargement costs at most its excess length times the bound for any one of the chosen nonzero terms. The bound is uniform over fixed inputs and translated targets.

If any order-four input occurs, condition on all residual inputs and on all phase residues except one order-four residue. The total phase in units of $s/4$ is uniform modulo four, because its free residue is multiplied by an odd $u$. The removed $E$ can depend on the fixed phase residues and requires no independence claim. Put $p=s/4\ge.85g$. The widened target has width below $2p$, so at most two phases hit. Two hit only when $S\bmod p$ is in the folded overlap of the target and its translate by $p$; this is an interval of width at most $(g+2N_*-p)_+\le.15g+2N_*$. If $S$ has a nonzero term, fix the other residual inputs and smooth this term, of width $g/2,g$ or $2g$ and step at most two. At period $p\ge.85g$ the density bound is at most $2/g$ for each width. Thus the overlap probability is at most $2(.15+(2N_*+2)/g)<.31$. Averaging the uniform phase gives success at most $(1+.31)/4<ρ_0$, a contradiction. Therefore all slopes in this case are multiples of $s/4$ with no residual part.

For the remaining cases, an even density decreasing in circular distance has maximal interval mass at the center. Convolution by a centered interval of half-width $b$ preserves this property: its derivative has sign $f(x+b)-f(x-b)\le0$ for $x,b\in[0,L/2]$ by comparison of circular distances. Thus convolution of the selected uniform widths at period $L$ is even and decreasing there, and centered interval averages decrease with width. The same proof applies on the line.

If there are no half-period slopes, keep period $s$ and the original target. Fix inputs outside a forbidden subset. The subsets are ten unit widths, three double widths, two doubles and one unit, or one double and six units, in units of $g$. The complement is at most nine units, one double and at most five units, or two doubles alone. Smoothing increases the target length by at most ten and the folded density of each selected term is at most $1/g$. The centered masses for ten units and one double with six units are $(1310745917-547199683)/1857945600$ and $(904843-385397)/1290240$, respectively. Their wrapped tails contribute at most $2(2)^{10}/10!$ and $2(1)^7/(2\cdot7!)$, respectively, since the centered support of sum plus target has radius $5.5$ or $4.5$, and $s/g\ge3.5$. The bound on each tail is the orthant simplex volume divided by the product of widths. The two numerators subtract the lower from the upper endpoint values of the cumulative function
\[
 F(x)=\frac{\sum_{S\subseteq[m]}(-1)^{|S|}(x-\sum_{i\in S}w_i)_+^m}{m!\prod_{i=1}^m w_i}
\]
by simplex inclusion-exclusion. For ten units the two endpoint numerators at denominator $10!2^{10}$ are the alternating sums $\sum_{j=0}^{\lfloor n/2\rfloor}(-1)^j\binom{10}j(n-2j)^{10}$ at $n=9,11$. For the double and six units use denominator $2\cdot7!2^7$ and numerator $\sum_{j=0}^{6}(-1)^j\binom6j[(n-2j)_+^7-(n-2j-4)_+^7]$ at $n=7,9$. The two double widths and a unit give $5/12$, from the triangular density $(2-|x|)/4$ and the mean absolute difference $1/3$ of two unit intervals. Their sum plus target has radius three and no contribution from other lifts. Three doubles give no greater interval mass by increasing a width in this centered symmetric circular convolution. Adding $10/g$ to any of these bounds leaves less than $ρ_0$.

If a half-period slope remains, condition on all residual inputs and all but one half-period bit. Averaging the uniform bit makes the two phase targets contribute with weight one half. Their union projects to a target of length $g+2N_*$ at period $s/2$, so the residual must hit it with probability at least $2ρ_0$. Select one double width if present, two full widths if present, one full with two half widths if present, or seven half widths if present. These exhaust the complement of at most six halves or one full and at most one half. At the unit centered target the respective upper bounds are $(1+.3)/2$, $3/4$, $5/6$, and $259723/322560+2/7!$. The first follows by splitting at one full period, since $s/2\ge1.75g$. The next two are the triangular density and the mean overlap loss $1/6$. For the last, scaling all seven halves by two gives endpoints $5/2,9/2$ and their numerator difference at denominator $7!2^7$ is $582283-62837$. The wrap adds the two simplex tails at period $\ge7/4$. These width lists have step sum at most fourteen and folded density at most $2/g$, so adding $(4N_*+28)/g$ to each bound leaves less than $2ρ_0$. The doubled residual has at most six unit coefficients or one doubled and at most one unit coefficient.

These arguments apply for $s=q$ to modular pivot equations. For rational integral-lattice pivot rows, each slope is half-integral since a successful set of size at least $ρ_0 g$ has a pair at distance at most two and their pivot values are integers. Double the equation and reduce it modulo an odd integer larger than ten times the range of all its coefficients and values. Every exact success is then a modular success, and the small signed or resonant residue recovers the original integer or half-integer slope. In both applications the modulus is odd, so there is no nonzero term with zero doubled residual. Including the pivot and clearing denominators, each reduced row is signed unit on at most ten positions, or has one coefficient of magnitude two and at most six of magnitude one, or two of magnitude two and at most one of magnitude one.

For a saturated rank-four integer normal choose a largest minor and normalize on its pivots. The normalized entries have magnitude at most one, so the nonintegral rows of the equation system have squared length at most $10/4$. The suffix parity map into $(\tfrac12\mathbb Z/\mathbb Z)^4$ has image dimension $k$. A fiber must meet one parity class of this map, so its mass is at most $2^{-k}g^{-4}$ since the even boxes give uniform parities and pivots are determined. Thus $k\le1$. The suffix image index above the pivot image is $h=2^k$ by B.18(b). The support has at most 40 coordinates. If $k=0$ the covolume is at most $10^2$, by the product of normalized column norms. If $k=1$ some equation has the smaller norm, giving at most $2\sqrt{10/4}\,10^{3/2}=100$. This gives regularity with $Γ_4=2$.

### Heights of selected rank-three normals

For the full normal of an untrimmed densest fiber, write $h=\prod s_i$ using B.18(b). If all $s_i<g$, the power comparison yields $h\le(g/ρ_0)^{49/48}<5.1g$, using $g<2^{50}$.

If some order is at least $g$, its ceiling factor is $1/g$. The other factors can include at most one nonunit order, which must be two: an order at least three costs at most $1/3+1/g$ and two factors two cost $1/4$, both giving mass below $μ$. Place the large coordinate $y$ first among suffixes. Its order $s$ in the pivot quotient is at least its earlier order, hence $s\ge g$ and $h/s=1$ or 2. Given the other suffix variables, at most one $y$ and one pivot triple are possible.

### Counting all lifts at period at least four box widths

Consider a classified suffix congruence $c_y y+\sum_i c_i x_i=L\pmod s$, with $c_y\ne0$ and no pivot variable. Drop zero coefficients. By reflecting negative coordinates and translating the target we can take all active coefficients positive and all boxes $\{0,\ldots,g-1\}$. Write $W=c_y+\sum_i c_i$, so the total lies in $[0,W(g-1)]$. A lift is an attained integer value in this interval congruent to $L$. With two lifts the bottom value and the distance of the top value from the other end are nonnegative integers $d_1,d_2$ with $d_1+d_2\le(W-4)g$ for $s\ge4g$. With three lifts the corresponding inequality uses $W-8$. Inactive suffix inputs can be fixed or summed out. If $u$ active suffix inputs remain besides $y$, the number of their assignments giving a lift bounds its fiber mass by that number times $g^{-u-4}$, since $y$ and the three pivots are determined. For two or three lifts use the sum of these counts. In particular a total count below $ρ_0g^u$ contradicts the original mass $m\ge ρ_0g^{-4}$.

**All coefficients one.** Here $W=u+1\le10$. With $W\le4$ only one lift fits. At either end the number at distance $d$ is
\[
 C_W(d)=\sum_{j=0}^{\lfloor d/g\rfloor}(-1)^j\binom Wj\binom{d-jg+W-1}{W-1}.
\]
The count is symmetric by reflection and unimodal by repeated convolution of centered integer interval laws. For the latter fact, after one convolution the difference of neighbors is the difference of two values of the preceding law, with the value farther from its center subtracted on the increasing side. This proves each step, including even interval sizes. The elementary upper bound $C_W(d)\le(d+W-1)^{W-1}/(W-1)!$ follows by dropping all upper coordinate bounds in the integer composition count. For $W=5,6$, convexity with $d_1+d_2\le (W-4)g$ bounds the two counts together by $((W-4)g+2W-2)^{W-1}/(W-1)!<.27g^{W-1}$.

For $7\le W\le10$ define
\[
 f_W(t)=\sum_{j=0}^{\lfloor t\rfloor}(-1)^j\binom Wj(t-j)^{W-1}/(W-1)! .
\]
These densities increase to $W/2$ by centered convolution. For $d/g\le W/2$, the exact count satisfies $|C_W(d)/g^{W-1}-f_W(d/g)|<2^{28}/g$. Indeed the per-term absolute difference of products before dividing by $(W-1)!$ is at most $81\cdot6^{W-2}/g$ by telescoping the increments $1/g$ through $(W-1)/g$. The sum of binomial multipliers is at most $2^W$, giving the stated loose error for all four $W$.

With two lifts, call the larger end distance $D$. For each row of the following table, if $D/g$ is below the first endpoint, bound the sum by twice $f_W$ at that endpoint. On every successive interval $(a,b]$, bound the sum by $f_W(b)+f_W(W-4-a)$ by the distance-sum bound. All the arguments are in the increasing range. For $W=10$ the first endpoint is 3, and the others are $4,4.5,4.68,4.74$.
\[
\begin{array}{c|c|c|c}
W & \text{successive endpoints} & \text{upper bound including }2^{29}/g &
  \text{smaller end if larger exceeds final endpoint}\\
7 & 2,2.5 & .280 & .5g\\
8 & 2.8,3.3 & .385 & .7g\\
9 & 3,3.8,4.02 & .416 & .98g\\
10 & 3,4,4.5,4.68,4.74 & .416 & 1.26g
\end{array}
\]
The exact band expressions before adding $2^{29}/g$ are
\[
\begin{array}{c|l}
 7&19/120,\ 10607/46080\\
 8&939007/2734375,\ 17172506189/50400000000\\
 9&477/2240,\ 1335530711/3937500000,\ 980686597916089/2500000000000000\\
10&913/11340,\ 51421/181440,\ 34835159/92897280,\\
 &287975250083722395889/708750000000000000000,\ 
 146824180879347411539/354375000000000000000
\end{array}
\]
For an endpoint $a/b$, insert numerator $\sum_{j=0}^{\lfloor a/b\rfloor}(-1)^j\binom Wj(a-bj)^{W-1}$ over $(W-1)!b^{W-1}$ and add the indicated endpoint terms. Cross-multiplication and $2^{29}/g<1/1000000$ give the stated bounds below $ρ_0$. Thus for two lifts only the last column can occur at the required density, and the smaller end may be discarded.

Three lifts require $W=9,10$. Their extreme distances sum to at most $(W-8)g$. Let $D_*=.98$ for nine and $D_*=1.26$ for ten. If one extreme exceeds $D_*g$, then the middle lift is at distance at most $(W-4-D_*)g$ from the opposite end. The middle contribution is at most $f_W(W-4-D_*)+2^{28}/g$, and the endpoints together contribute at most $(W-8+2(W-1)/g)^{W-1}/(W-1)!$ after division by $g^{W-1}$. Here the two middle-density values are
\[
 f_9(201/50)=\frac{617664595987136070}{1575000000000000000}<393/1000,qquad
 f_{10}(237/50)=\frac{293624599765875790502}{708750000000000000000}<4143/10000 .
\]
For verification, for $(W,n)=(9,201),(10,237)$ the numerator is $\sum_{j=0}^{4}(-1)^j\binom Wj(n-50j)^{W-1}$ and the denominator is $(W-1)!50^{W-1}$. In the endpoint bound replace $2(W-1)/g$ by $10^{-12}$ using $g\ge2^{49}$. The resulting terms are $(1+10^{-12})^8/40320<25/10^6$ and $(2+10^{-12})^9/362880<1412/10^6$, by cross-multiplication. Also $2^{28}/g<1/10^6$. The two sums are below $(393000+25+1)/10^6$ and $(414300+1412+1)/10^6$, respectively, both below $.416$. Otherwise delete both extremes. For these three-lift cases the deleted mass, by convexity, is at most
\[
 g^{-4}\frac{(D_*+(W-1)/g)^{W-1}+(W-8-D_*+(W-1)/g)^{W-1}}{(W-1)!}
 < g^{-4}/40000 .
\]
For nine and ten, upper-bound the bases for the two terms by $(981/1000,21/1000)$ or $(1261/1000,741/1000)$, respectively, since $(W-1)/g<1/1000$. The required integer comparisons are
\[
\begin{split}
 40000(981^8+21^8)&=34309315244745780020416080000
       <40320\cdot1000^8,\\
 40000(1261^9+741^9)&=325168954366438666147792208080000
       <362880\cdot1000^9.
\end{split}
\]
These bounds also cover the one-end deletions for nine and ten. For seven and eight the bounds are $40000\cdot501^6<720\cdot1000^6$ and $40000\cdot701^7<5040\cdot1000^7$, using the single-end terms. Four lifts cannot fit.

**Coefficients two and one.** The classification gives either a single coefficient two and at most six coefficients one, or two coefficients two and at most one coefficient one. In the latter case $W\le4$ unless there is exactly one unit coefficient. For $W=5$ there are two active suffix inputs and $d_1+d_2\le g$. If $y$ is unit, attach disjoint unit squares to the two doubled suffix inputs. If $y$ is doubled, the unit suffix has prescribed parity at each lift, so attach rectangles of width two at that input and one at the doubled input. The rectangles may be based at the tuple for even parity and translated one unit to the left for odd parity, in the unit coordinate, to stay inside the original interval. Reflect at the upper end before attaching rectangles. Their total volume bounds the count by $(d_i+4)^2/8$ in either case, by the orthant weighted simplex formula $R^u/(u!\prod_i c_i)$ after division by the rectangle volume. The two counts together are less than $.126 g^2$.

With exactly one coefficient two and $u\le4$, a lift pair fits only for $u=3,4$ and then $d_1+d_2\le (u-2)g$. If $y$ is unit, attach unit cubes at suffix tuples, with one doubled weight. If $y$ is doubled, the suffix sum has prescribed parity at each lift; attach width two at the first suffix coordinate and width one elsewhere, as above. The two total volumes give the same count bound $((u-2)g+2u+2)^u/(2u!)<.34 g^u$. The factor two is respectively the weight or the rectangle volume.

For one doubled coefficient and $u=5$ we have $W=7$. Both end distances are at most $3g$ and their sum at most $3g$. If $y$ is unit, attach unit cubes and compare their total volume with the normalized sum of independent interval widths $(2,1,1,1,1)$. At end $d_i$ the band is $[d_i/g-1,d_i/g]$ enlarged at its upper endpoint by at most $6/g$ from attachment. Its density is at most one. If both distances are at most $2g$, the two bands cost at most $2F(2)=7/30$ before enlargement. Otherwise the smaller costs at most $F(1)=1/240$ and the larger at most $F(3)-F(2)=23/60$, because centered interval mass increases up to center. Here $F$ is the sum's cumulative distribution. If $y$ is doubled, the same comparison uses the width-two parity rectangles and the law $F_5$ of five unit widths. The band $[d_i/g-2,d_i/g]$ expands by at most $1/g$ at the lower end and $6/g$ at the upper end. Divide the volume by two. If both distances are at most $2g$ the bound is $F_5(2)=27/120$ before enlargement. Otherwise the bounds are $F_5(1)/2=1/240$ and $(F_5(3)-F_5(1))/2=23/60$. For both laws the values follow by simplex inclusion-exclusion, $F(t)=\sum_{S}(-1)^{|S|}(t-\sum_{i\in S}w_i)_+^5/(5!\prod_i w_i)$ for the respective width list. The listed bounds plus $16/g$ are below $ρ_0$. For the last case $W=8$ with one doubled coefficient and six active suffix inputs, there are at most two lifts, with combined distance at most $4g$. Use the same bands as for $W=7$, now with widths $(2,1,1,1,1,1)$ and length one for $y$ unit, or six unit widths and length two with the factor one half for $y$ doubled. Each of the total band bounds incurs less than $20/g$ for rectangles, since the density is at most one and expansion per end at most $9/g$. If both distances are at most $2.75g$, use the sum of the tails at 2.75, below $.404$ before expansion for either width list after the parity factor. If the larger distance is in $(2.75g,3.5g]$, the smaller is at most $1.25g$. The larger band's mass is at most its value at 3.5 by unimodality and symmetry, and the smaller band is bounded by the tail at 1.25. The sum is below $.373$ before expansion. The respective bounds for both distance regimes are $1189877/2949120,549361/1474560$ for widths $(2,1,1,1,1,1)$ and $538301/1474560,732481/1966080$ for six units after the parity factor. Insert $t=11/4,5/4,7/2,5/2,3/2$ as applicable in the width-list inclusion-exclusion with exponent six. For the doubled width the numerator summands use $(t-j)_+^6-(t-j-2)_+^6$ with $(-1)^j\binom5j$ over $2\cdot6!$. For unit widths use $(-1)^j\binom6j(t-j)_+^6$ over $6!$. Thus if the fiber is heavy the larger end distance exceeds $3.5g$ and the smaller is at most $.5g$. The orthant simplex bound on the smaller count is $(.5g+8)^6/(2\cdot6!)$. In the two cases the denominator two again comes from the doubled suffix weight or the parity rectangle volume, respectively. Since $(.5+8/g)^6<(501/1000)^6$, the exact inequality $40000\cdot501^6<2\cdot720\cdot1000^6$ bounds the removed mass by $g^{-4}/40000$.



Thus a classified equation at $s\ge4g$ either has just one lift from the start, or all but one may be deleted at cost at most $g^{-4}/40000\le e$. The initial rank-three mass has the margin $m\ge μ+e$ whenever the regularization rule is invoked, so after deletion it is still at least $μ$.

For $h=s$ with $s\ge7g/2$, apply the slope result. In the pure order-four phase case at most two $y$ values are possible, and if $s\ge4g$ there is at most one, contradicting exact normality. Thus that case has $s<4g$. Otherwise, for $s\ge4g$ the counted sums apply, doubling if a half-period coefficient occurs. The $h=2s$ argument below also gives a doubled equation. Whenever the lift count is applied, one realized lift gives an independent integer normal, with nonzero $y$ coefficient and zero pivots. This contradicts exact rank three if there was no deletion. Otherwise the retained subset has mass at least $μ$ and its full normal has rank at least four by this additional relation and at most four by the pivot density bound. The new normal thus gives the sparse rank-four regularization output with loss at most $e$.

If $h=2s$ with $s\ge7g/2$, quotienting by $y$ imposes a nontrivial parity on the other suffix variables, with probability one half. Some fixed legal parity pattern thus has $y$-success at least $2ρ_0$. In it write all $x_j=2z_j+π_j$ with length-$g/2$ intervals. In the subgroup generated by $y$ the slope is $k_j$ with $2P_j=k_jP_y$ modulo the pivot image. Fix other inputs at offsets attaining success $2ρ_0$. For $1\le i\le\lfloor .66g/2\rfloor$ the successful set intersects its translate by $i$ since twice its cardinality exceeds $g/2+i$. The signed residues $ik_j$ lie in $[-g+1,g-1]$ and their successive differences equal the signed $k_j$, as the difference minus the step has magnitude below $3g<s$. This gives $|k_j|\le3$. Magnitude three gives a progression of length at most $1.5g$ on the fixed-parity $g/2$ inputs. Together with the length-$g$ target its span is below $s$, so it has at most one relevant lift and $g/3+1$ successes, below $2ρ_0g/2$. Thus $|k_j|\le2$. The preceding centered interval bounds at threshold $2ρ_0$ apply to the half and full widths on this pattern, so the residual has at most six unit coefficients or one doubled and at most one unit coefficient. The doubled congruence $2y+\sum k_j x_j$ now holds modulo $s$ on the entire fiber. When $s\ge4g$ the magnitude-two lift count gives an extra normal. Thus any rank-three return has $s<4g$ and $h<8g$.

For a rank-three output also annihilating all public rows over the integers, consider $s\ge7g/2$ in a large-order case. Leave aside the pure order-four phase case just proved. For $h=s$ the ordinary or doubled equation has its small signed coefficients as above. For $h=2s$ use the legal parity pattern argument also for $7g/2\le s<4g$: its signed successive differences still have magnitude below $3g<s$, and the conditional residual bounds still give $|k_j|\le2$ and the same small support patterns. In the pivot quotient, the normalized rows $P_i$ have unit pivot rows and $P_y$ of order $s$. The integer equality $\sum_i H_i P_i=0$ for each public row $H$ gives $H_y+\sum_j a_j H_j=0\pmod s$ in the ordinary cyclic case, or $2H_y+\sum_j k_j H_j=0\pmod s$ after doubling. This is the same coefficient list as its scalar congruence. The absolute value is bounded by $10\cdot2^{43}<s$, so it vanishes as an integer. The weighted exclusion of I5 forces all active positions to be tags.

Thus there are at most three active positions. With unit coefficients the diameter is below $3g<s$. With a double coefficient and two unit coefficients two lifts would have end distances summing to at most $.6g$. The weighted simplex count on the two suffix inputs, using a weight of two or the forced parity if $y$ is doubled, gives at most $(.6g+6)^2/4<.1g^2$ choices in total. With two double coefficients and one unit the distances sum to at most $1.6g$. The corresponding denominator eight in the simplex count is from two doubles, or from one double and the forced parity. The total is below $(1.6g+8)^2/8<.321g^2$. Both counts contradict $mg^4\geρ_0$. With two double terms only, the two tails have total distance at most $.6g$ and at most $.3g+2$ suffix choices. All other subsets with fewer terms fit one lift. One lift supplies the exact additional normal, impossible at rank three. Thus an annihilating rank-three output either has no large order, has only pure order-four phases, or has $s<7g/2$.

These cases exhaust the return: with all orders small the power bound applies. Otherwise moving the large order first leaves $h/s=1$ or $2$. Below $4g$ both heights are below $8g$. At or above $4g$, the pure quarter-phase case has one lift, and the ordinary, half-period and parity-restricted cases use the lift count to return rank four.

Expanding the nonunit prefix factors $1/s_i+1/g$ gives $m\le g^{-3}ξ_{\rm tr}(1/h+1/g)$. The leading term is $1/h$, and the other terms total at most $a(1/2+1/g)^{a-1}/g\le(1+2/g)/g$ for $a$ nonunit factors by the mean value theorem, checking $a=1,2$ and the decreasing ratio. Thus $mh<9ξ_{\rm tr}/g^3\leΓ_3/g^3$.

## Amendment I5

Keep $Λ_iγ_i<μq$ for $1\le i\le3$ and $H_1T_{\rm tr}<q$, $4H_2T_{\rm tr}^2<q$, $54H_3T_{\rm tr}^3<q$. Replace the density test by $g^{-5}<μ$ and require $2400000/q+5/g^5<μ$ and $480000g^4<q$. The latter two tests are the rank-four feature count and minor conditions used in I6. The sampler below excludes rank four for every heavy stack, so the view, extraction and reduction still need only three gradients and three probes. The auxiliary fourth-rank lattice is solely part of the inverse proof. The unchanged comparison counts and final probability bounds are proved in Ncmp and Targets.

### Six public rows and prescribed completions

Put $N_o=N+689$ and $N_*=N_o+3$. Exterior and low weights have the entries
\[
 w(j)=(16j+1,(j+1)^2\bmod P,(j+1)^3\bmod P,(j+1)^4\bmod P,C(j),(j+1)^5\bmod P),
 \quad C(j)=\sum_{a=1}^4 w_a(j).
\]
Use $P=2097257$. Its predecessor factors as $2^3\cdot7\cdot17\cdot2203$. Trial division at primes through 46 gives residues $1,1,3,5,3,6,10,18,18,28,2,20,30,10$ for 2203. Exponentiating 3 gives $3^{P-1}=1\bmod P$, with the complementary powers at primes 2, 7, 17 and 2203 equal to $2097256,360681,1623884,22951$. Each one's difference from one is coprime to $P$ by Euclid's algorithm. Thus for each prime divisor of $P$ the order of 3 is $P-1$, proving primality.

Use low single coordinates $j=0,\ldots,14$. For each $i=4,\ldots,23$, choose a pair at $a_i,a_i+2^{i-4}$ with $0\le a_i<256$, avoiding all earlier indices. At most $2(15+2(i-4))<256$ choices are forbidden. Exterior coordinates are the first $N$ unused indices starting at 256, hence at most $255+N+20$. In particular every used index is below $P-1$, and $16j+1\le 2^{23}+4081$. Equal sums of equally many exterior-type weights with at most five terms on each side give matching first five power sums of $j+1$ modulo $P$. Newton's formula $r e_r=\sum_{i=1}^r(-1)^{i-1}e_{r-i}s_i$, with $e_0=1$, follows by differentiating the product $\prod_j(1+x_jX)$ and multiplying out its logarithmic derivative. It determines the monic polynomial of the multiset, so equality identifies the indices with repetitions.

The completed witness uses 177 high binary pairs. Their respective prescribed differences are $2^i$ in the first direction for $i=24,\ldots,40$ and in each of directions two, three, four and six for $i=0,\ldots,39$. Set their fifth differences equal to the sum of differences in the first four directions plus a positive integer $c_i$. Also use 40 checksum pairs with differences $-2^j$ in direction five only, $0\le j\le39$. Under the linear checksum defect $w_5-\sum_{a=1}^4w_a$, the 217 high pair differences have defects $c_i$ and $-2^j$. Choose the $c_i$ successively in $[1,2^{32}]$ so that no nonempty signed sum of at most five distinct defects vanishes. The powers of two alone satisfy the requirement by dominance of the largest one. At a new choice the forbidden values are signed sums of at most four previous values, and $\sum_{r=0}^4 2^r\binom{216}{r}<2^{32}$. This verifies greedy existence. Add 200 high singleton pads, fixed to one.

A high baseline or singleton has first weight $L+16a+1$ with $L=2^{42}$ and $0\le a<2^{33}$, and each other entry independently in $[0,2^{41})$, with an offset $2^{40}$ on entry five. A high pair consists of the baseline and that baseline plus its prescribed difference. All weights are nonnegative and below $2^{43}$. Choose the 417 baselines or singleton vectors in succession. In addition to assigned positions reserve every future pair difference as a formal term with either sign, used at most once. Whenever a balanced high signed sum with at most five unit multiplicities on each side and at most one coefficient of magnitude two has an unbalanced assigned stage, require its maximum absolute entry above $2^{26}$ if it has at most four multiplicities per side and nonzero otherwise. A stage with aggregate zero contributes either zero or its unit difference, since using both coefficients of magnitude two is excluded. Thus any condition with a last unbalanced stage reduces to a nonconstant multiple of its new baseline plus fixed positions and reserved differences. The bad baselines form at most one integer box of coordinate side at most $2^{27}+1$ (with at most $2^{23}+1$ choices for the first entry on its step-sixteen grid) for up to four multiplicities per side, and at most one point for five. This gives fewer than $2^{160}$ candidates per box using $(2^{23}+1)(2^{27}+1)^5<2^{160}$. Orient a new occurrence positive and put it first. If the new occurrence is a doubled position, or one of the other at most nine positions is doubled, enumerate its location separately. At a stage there are fewer than 1024 choices of a formal position, including reserve symbols (their signs can be treated as signs of their coefficients). For an explicit bound, place all positive positions first, then all negative ones, since summands commute. For any exact positive multiplicity $l$ and negative multiplicity $l$ with $1\le l\le r$, the word with no doubled position is fixed by at most $2\cdot1024^{2l-1}$ choices. With one doubled position it is fixed by at most $2(2l)1024^{2l-2}$ choices, allowing its marked place among the positive and negative occurrences and their known multiplicities. Hence the sum over $l\le4$ is below $2^{72}$ and the sum over $l\le5$ below $2^{92}$. The bad baseline count is below $2^{233}$ in a set of size $2^{238}$. Enumerating endpoint cells of the integer boxes and checking cell corners supplies a choice in polynomial time in the number of pads at this fixed dimension and multiplicity. These weights are public setup constants.

In every vanishing signed relation of total absolute coefficient sum at most ten, equal signed multiplicities follow from the first weight being one modulo sixteen. Their high multiplicities must also agree: each side's residual after subtracting $L$ per high occurrence is nonnegative and below
\[
 5(2^{37}+1)+(2^{41}-2^{24})+2^{40}+5(2^{23}+4081)<L .
\]
The sum of high first-bit increments uses each stage once, with at most one doubled occurrence giving the extra $2^{40}$. For the coefficient pattern with two magnitude-two terms and at most one unit, the unit cannot be present by equality of multiplicities, and equality of two weights is excluded already by the unit-only pair case. In all other patterns there is at most one double. An unbalanced high stage is excluded by the greedy condition, since the low terms have at most four multiplicities per side when a high stage appears, and maximum difference below $4(2^{23}+4081+3(P-1))<2^{26}$. If every high stage balances, its pair gives zero or one signed virtual difference. There are at most five such differences, so a nonempty checksum sum is nonzero, whereas all exterior-type weights have zero defect. With no virtual terms the Newton argument completes the exclusion.

Take the six public rows with these weights on exteriors, their negatives on pads, and zeros on tags. Complete any exterior witness as follows. In the first row subtract the exterior weight sum's residue modulo sixteen using that many low singles starting at zero. This is possible without a negative remainder since every exterior weight is above the total low-single weight 1695. The remaining sum is divisible by sixteen and below $2^{41}$ since all exterior indices lie below $255+N+20$ and their sum is at most $N(N+551)/2$. Choose pair second members for its bits. For directions two, three, four and six encode the exterior sum plus $2^{28}$ less the selected low contributions in that direction. At most 35 low pads are selected and their weights in these directions are below $P$; the result lies in $[0,2^{40})$. In each ordinary direction set the homogeneous entry to the fixed-one weights plus all selected-pair baseline weights, with the $2^{28}$ offset in directions two, three, four and six. All 237 pairs have exactly one selected member, so the baseline sum is independent of the witness. Set the homogeneous checksum defect to the sum of fixed and high baseline defects. After choosing the 177 bits the remaining defect is $-\sum c_i b_i$. The checksum pairs cancel it using its 40-bit encoding, since $177\cdot2^{32}<2^{40}$. All six rows now vanish, and the first two rows supply the two public form slots; the other four are independent sampler shifts. The 15 singles, 237 pairs and 200 fixed pads are precisely 689 internal Boolean coordinates.

### Shifted box sampler

First draw independent length-$g$ boxes $u_i$, $1\le i\le N_*$, and $u_\diamond$ on $\{2,\ldots,g+1\}$. Set $u_0=A_0+u_\diamond-\lfloor\sum_i u_i/2\rfloor$, $A_0=\lceil N_*(g+1)/2\rceil$. Then draw independent uniform scalars $Z_1,\ldots,Z_6\in\mathbb F_q$ and use $r=u+\sum_{ℓ=1}^6 Z_ℓ H^{(ℓ)}$ modulo $q$ in the right factors. On the prescribed honest completion $r^\top v=u^\top v$ modulo $q$. Use that integer for all searches. Write $\mathrm{wt}(v)=\sum_{i=1}^{N_*}v_i$. Its public center is $\lfloor A_0+(g+3)(1+{\rm wt}(v)-N_*/2)/2\rfloor$. Its centered error against the independent centered box sum is at most $3/2$ and its variance bound is $(g^2-1)(N_o+7)/48$, by the sum of squared coefficients (one diamond of coefficient one and $N_*$ coefficients $\pm1/2$). Its deterministic centered magnitude is at most $(N_o+5)(g-1)/4+3/2<B_{\rm search}/2$ for the admitted $N$, using the unchanged $B_{\rm search}=(N+1)(g+1)$. Tag differences remain bounded by $g$ and have the same distributions. The weight and shifts in search_spread now use internal $N_o$ wherever they count box coordinates; the contracted witness sums charge at most 252 retained selected pad bits in addition to the protected external Hamming weight.

### Heavy stacks for the six shifts

The shifted-sampler rank lemma proved in search_spread applies to the six public rows. A stack failing to annihilate any one is light by the $1/q$ bound. For an annihilating stack the fiber law is that of the unshifted boxes with their independent diamond. Rank five or above is light by I5. For a zero-homogeneous rank-four heavy stack, the reduced rows have the sparse coefficient patterns above. The weight evaluation has magnitude below $10\cdot2^{43}<q$ per row. Thus annihilation modulo $q$ is an integer equality and the six-row weight exclusion forces each reduced row to be supported only on tags, impossible at rank four.

If the homogeneous column is nonzero at rank four, the zero-homogeneous rank-three subspace has mass at least $g$ times the stack's mass: conditional on the ordinary boxes, the remaining equation costs probability at most $1/g$ over the diamond. Its reduced rows obey the same support bound at density $gμ$, hence it is the space of the three tags. Fix their values, normalize the last row's zeroth coefficient to one and subtract its tag entries. The remaining equation has conditional probability at least $ρ_0/g$. Condition on the parities $u_i=2x_i+π_i$ of the nontag variables. Then $\lfloor\sum_i u_i/2\rfloor=\sum_i x_i+$ a parity-dependent constant after the fixed tags are absorbed. The diamond fixes the remaining value with probability $1/g$ when it lies in its allowed interval. Thus in some parity class the sum $\sum_i(2v_i-1)x_i$ must fit a length-$g$ interval modulo $q$ with probability at least $ρ_0$, by conditioning away the independent diamond. The $x_i$ are independent intervals of length $g/2$.

For each $α_i=2v_i-1$, fix the other inputs attaining success $ρ_0$ on the length-$g/2$ interval. Two successes have gap one or two, giving a signed integer or half-integer coefficient. The progression plus target spans less than $g^2+g$ in its ordinary part. For an odd doubled coefficient, the two input parities place their progressions near opposite points modulo $q$, so at most one hits. An integer magnitude at least five or an odd doubled magnitude at least five therefore costs at most $g/5+1<ρ_0 g/2$ successes. All signed magnitudes are at most four.

If every coefficient is integral, smoothing 48 nonzero terms assuming there are that many gives mass at most $\sqrt2(g+192)/((g/2)\sqrt{48})<ρ_0$ by the one-dimensional density bound. The other terms are fixed and the remaining diameter is below $q$, so the interval has only one effective lift. If some coefficient is fractional, the whole signed real sum using half-integers spans at most $4N_*g<q/4$. Its integer and odd-half parts map to regions separated by $q/2$ up to this diameter, hence at most one parity class of the numerator can hit. Since $4\mid g$, the parities of all inputs on their length-$g/2$ intervals are independent uniform bits. Exactly half their patterns are legal. On each, after fixing parities the individual nonzero widths after smoothing are at least $g/4$ and the steps are at most eight. Smoothing any 48 terms and fixing the rest gives conditional mass at most $\sqrt2(g+384)/((g/4)\sqrt{48})<2ρ_0$, contradicting success $ρ_0$ after the half factor. Thus at most 47 coefficients are nonzero.

Annihilation of the first public row requires
\[
 2H^{(1)}_0+\sum_i H^{(1)}_i+\sum_iα_i H^{(1)}_i=0\bmod q
\]
with indices outside the tags. The pair baselines cancel in the first two terms, and their increments subtract at most $2^{41}-16$. The fixed pads give at least $200L$ and the fifteen small singles cost at most 1695. The resulting baseline exceeds $200L-2^{41}-1695$. The deviations have magnitude at most $188(L+2^{37}+1)+4(2^{41}-16)$, using at most 47 nonzero deviations of magnitude at most four and the total sum of distinct first-bit increments. The former lower bound is larger. The doubled expression has magnitude below $2^{55}<q$, so this also excludes rank four. Heavy rows therefore annihilate the six public rows and their stack has rank at most three.

## Amendment I6

Write $B_E={\rm beta\_sis}$, $C_3={\rm cov3}$, $C_2={\rm cov2}$, $e=ε_{\rm tr}$. Require $2β<q$, $β\ge B_E$, and
\[
 R_{\rm tr}=18,\quad b=49,\quad 2^{49}\le g<2^{50},\quad
 10^7N_*\le g,\quad H_3=8g,\quad 4\mid g,\quad 40000eg^4\ge1,\quad H_2^{16}<g^{39},\quad
 10000e\leμ,\quad g^4μ\ge417/1000 .
\]
Require $C_3\ge607/10$, $C_2\ge5020000$, $B_E\in\mathbb Z$, $1\le B_E$, $2B_E<q$, $B_E^4<q^3$, $H_1<g^4$, and
\[
 B_Eg^2μ\ge\sqrt{N_*}γ_1,\quad
 200 B_E^2g^2μ\ge231 C_2q,\quad
 70 B_E^3g^3μ\ge99 C_3q^2,\quad
 B_Egμ\ge67000 C_2+1448000000+200 .
\]
The inverse theorem for the actual sampler is proved next. The exact Euclidean bounds and lift appear in msis_bound. The still stronger protected bound on $β$ in P4 supports the same reduction-time and range hypotheses. Neither the admissibility comparison E nor the inverse argument changes the security target.

### Joint inverse on the box coordinates

Write $e=ε_{\rm tr}$. Let a nonzero modular row family on box coordinates have maximum joint fiber probability $p>θ$. Zero columns can be removed. In each active prefix let $p_i$ be the maximum modular fiber mass. Conditioning the new coordinate proves $p_i\ge p_{i+1}$. We construct a regular saturated lattice of rank $d\le4$ containing the prefix row family modulo $q$ and of mass at least $p_i-4e>μ$. At the first nonzero column, the prefix is contained in $\mathbb Z$ of mass $1/g$; $γ_1\ge1$ by I4.

For an extension write each prefix row as $Bc'$ modulo $q$ in the current basis $B$ and append its last entry to obtain a coefficient vector $c$. Choose a densest longer modular fiber, trimming by the old lattice if $d\le3$. Call the resulting set $F$, of mass at least $p_{i+1}-e$. Rank four uses the whole fiber. Its image $\Phi=(B^\top r_I,r_{i+1})$ lies in the common affine equations for all the $c$, at least one of which is nonzero and defines an index-$q$ coset since an appended coefficient is nonzero. If $d\le3$, the projected count (a) of I3 and $Λ_dγ_d<qμ$ exclude affine dimension $d+1$. If $d=4$, normalize the first four features by $B_J^{-\top}$ at a largest pivot minor, of height $h\le2$. Each normalized row has at most ten coefficients of magnitude at most one, so its feature width is at most $10(g-1)<10g$. The extra width is $g$. Normalization divides the index-$q$ coset's covolume by $h$. The simplex count then bounds a full-dimensional image by $5!h\cdot10000g^5/q+5$ points. Each image point has mass at most $g^{-5}$ by the four pivots and the independent new coordinate. The last condition of I5 on the mass therefore excludes full dimension five.

Let $Δ$ have columns formed by differences of image points from a fixed point and rank $k'\le d$. Choose a maximal pivot $B_J$ of determinant magnitude $h$ and normalize by $A^{-1}$ for $A={\rm diag}(B_J^\top,1)$. All entries of $A^{-1}Δ$ have magnitude at most $T_{\rm tr}$ if $d\le3$ by I2, or $10g$ if $d=4$ by the sparse row bound. Every minor of $A^{-1}$ multiplied by $h$ is integral by the complementary-minor identity, obtained by appending complementary standard columns and expanding after multiplication by $A$. Cauchy–Binet gives the same property for minors of $A^{-1}Δ$. A nonzero $k'$-minor times $h$ has magnitude below $q$ by I5, using $h d!T_{\rm tr}^d$ or $2\cdot24(10g)^4$. Since $q\nmid h$ and all $(k'+1)$ minors vanish, this proves rank $k'$ modulo $q$. The rank-zero case needs no minor. Apply the integer lifting fact of I3 to every $c$ to obtain integer annihilators of the image differences reducing to the chosen coefficients. Their pullbacks $(Bu_{[d]},u_{d+1})$ are normals to $F$ and lift all new prefix rows. This normal lattice has rank in $[1,4]$ by $g^{-5}<μ$, and mass at least $p_{i+1}-e>μ+3e$. Regularization in I3 loses at most $3e$ and yields the next invariant. All domains are subsets of the same $N_*$ coordinates.

For the actual sampler a form with zeroth coefficient zero and probability above $θ$ annihilates all six public directions by I5's sampler argument. Its pure-box law is then the one just analyzed. The same applies to each zeroth-zero row of a heavy stack. The terminal normal lattice admits a short multiple of that line by the lattice mass and rank-four intersection estimates and the rank-one to rank-three length bounds in msis_bound. Those estimates use only the just-proved lift, the density and the six public equations, without assuming the conclusion here. Its Euclidean radius $B_E$ is at most $β$, and the infinity norm is bounded by the Euclidean norm. Restore zero coordinates, including coordinate 0. This proves the amended inverse theorem for every line heavy under the actual sampler, as needed by the mark and extraction proofs.

## Amendment Ncmp

For the variable $u$ used by the bound $E$, set
\[
N_{{\rm cmp}}(u)=\frac{u(u+10)}8 .
\]
The remaining formula for $E$, the values of $u=2Q+2$ used by the proof, and the two tests in (P5) are as specified in the protected model. The new count applies to the bad events that can pay a $θ$ charge. The other pair and entry terms continue to pay for the full collection of possible coincidences.

### Coupling and bad events

Fix $M,Q$. By the symbolic-game coupling, replace the masked message by an independent uniform string through the first target query, before its answer. Sample the resulting formal-equality simulation with label images independently of coins and $r$. Receive the initial entries, give each guessed operand a fresh variable of its group and insert each result only if formally new. Each call adds at most three entries.

Assign independent uniform exponents to guesses and evaluate. Couple with the real random-mask run until two formally distinct same-group entries coincide. Share fresh labels for new result values. For a guessed operand reuse its independent exponent unless previously assigned, in which case redraw uniformly among unused exponents. This is uniform on unused exponents as required by the injection law. Before a collision the transcripts agree by induction. Initial collisions have the initial mark. At a later good collision the difference is guess-free in the target group; the new entry cannot be a guessed operand introducing a fresh variable. The result receives the old label and the monitor marks a good difference. A redraw of a guessed operand is already a bad collision with its new variable, even if no mark is recorded then. A charged target query before a collision specifies an existing evaluated target entry with a bad expression (an unassigned entry gives the guess mark). Thus charged first marks are covered by bad noninitial collisions or bad target-value events.

Use difference $D$ and $χ=0$ for a collision, entry $D$ and $χ=1$ for a target query. The source-group view bounds guess-free source differences by $ε_f$. With a guess variable, a nonzero guess-monomial coefficient is a constant or a formally nonzero source expression, since only pairing multiplies source terms. For every fixed $r$ the latter is nonzero on some valid coins by source coincidence and $ε_f<1$. After clearing $ϖ$, the event equation is a nonzero polynomial of degree at most $d_f+1$: one guess adds one degree to a source term, and pure products of two guesses have cleared degree at most eight. The independent field supports of size at least $q-D$ give probability at most $(d_f+1)/(q-D)\le ε_f$.

For a guess-free target event, the view gives probability at most $ε_f$ at each $r$ without a formal identity $D=χ\kappa$. At an identity, formal distinctness (or the exclusion of a formal key) gives a nonzero stack, and all such $r$ lie in its fixed fiber. A bad stack is light, so this part costs at most $θ$.

### Counting the light-stack charges

Only guess-free target events incur $θ$. At call $j$ the later entry of such a collision is the result; a fresh operand introduces its own variable. The earlier entries include at most two received, $j-1$ results, and pure guessed variables. At most one of the latter can have a guess-free difference with the result, since the difference of two distinct guess variables is nonzero. Thus at most $j+2$ comparisons can cost $θ$. Target entries that are guess-free must be received or results, at most $Q+2$. Their total with comparisons is $\sum_{j=1}^Q(j+2)+Q+2=u(u+10)/8-1$.

The full count for all other bad events is bounded by the number of pairs plus the number of entries in a table of at most $L+3Q$ entries, and hence by $\binom{L+3u}{2}+L+3u$. The pair count may overcount comparisons between different groups, which only increases the bound. Combining the union bounds establishes the amended charged-mark estimate
\[
 \Pr[\text{charged first mark}]
 \le N_{{\rm cmp}}(u)(θ+ε_f)
       +(\binom{L+3u}{2}+L+3u)ε_f .
\]
This bound holds for each $M$.

### Generic ledger and scope of the amendment

The generic ledger has the same implication from (P5). In the amended $E$, all coefficients as a polynomial in $u$ are nonnegative and its degree is two. Here $L\ge1$, $N_{{\rm free}}>0$ by (P2), and $\binom{L+3u}{2}$ expands with nonnegative constant, linear and quadratic coefficients. The new $N_{{\rm cmp}}$ has nonnegative coefficients. For real $Q$ on $[0,2^λ-1]$, the function $Q\mapsto E(2Q+2)-(Q+1)/2^λ$ is convex because its quadratic coefficient is nonnegative. At the first endpoint it is at most zero by the first P5 test. At the second it is $E(2^{λ+1})-1$, at most zero by adding the P5 tests. By convexity it is at most zero throughout. The threshold side conclusion of the generic ledger becomes $θ<2^{1-2λ}$ for $λ\ge1$. Indeed putting $U=2^{λ+1}$, we have $N_{{\rm cmp}}(U)-N_{{\rm cmp}}(2)=U^2/8+5U/4-3>2^{2λ-1}$. Every other term in $E(U)-E(2)$ is nonnegative, so the second P5 bound implies the stated strict threshold limit.

The only admissibility use of this count is $E$ in P5, which still implies $ε_f<1$ via $E(2)\ge24ε_f$. Expression degrees, coins, oracle labels, and mark definitions are independent of the count. The factor-one-half lemma compares actual failure probabilities via uniform-mask coupling. The initial and guessed marks use received-expression comparisons and unassigned-label uniformity. The reduction uses degree, gradient distribution, rank and the short-vector guarantee. Their hypotheses and arguments are therefore unaffected. Targets combines these results with the proved charged-mark and generic bounds.

The extractability-error corollary follows with its original statement from Targets and the factor-one-half lemma. For allowable budgets, in the combined bit experiment with uniform $b$, put $f_i=\Pr[\mathsf{Tgt}\wedge\mathsf{Fail}\mid b=i]$. The probability of both a correct bit and extraction failure is at most $1/2+(f_0+f_1)/4$. The target-query bound in Targets gives $f_i\le (Q+1)/2^λ+s_i$ for each $i$. Both reductions run in time bounded by $t_R=t+O(Q+d_R Q_H+μ)+{\rm poly}(D,\log q)$, including fixed description and advice, so each $s_i$ is bounded by ${\rm Adv}^{{\rm MSIS}}(t_R)$ by its defining maximum. Substitution gives extractability error at most $(Q+1)/2^{λ+1}+{\rm Adv}^{{\rm MSIS}}(t_R)$ at the same extractor time. Outside the stated budgets, the trivial probability upper bound 1 yields error $1/2$ as in the corollary. This accounts for every result in the background list of the bound block.

## Amendment D

Keep the external system $S$ on $N$ bits. As in I5 extend it internally by 689 unconstrained Boolean padding bits and three Boolean tags. Its $N_*+1$ positions include the homogeneous coordinate. The prescribed completion gives all eight tag variants of every external witness, and any satisfying internal assignment projects to an external witness.

Use $N_*+1$ distinct Booleanity points $d_0,\ldots,d_{N_*}$, a distinct key point $ρ$, and the same $n_c$ cosets of size $ν$ for the external constraints. Hence $D=N_o+5+ν n_c$. Use the protected subgroup placement in the finite scored algorithm with this $D$. The algebraic identities apply to every admissible set of points. At $d_0$ set $A=0,B=e_0$. At $d_i$, $i>0$, set $A=e_i-e_0,B=e_i$, including all pad and tag Booleanity points. Fix a public primitive eighth root $\omega_8$ in the scalar field, which exists because $8\mid q-1$. Set $c_*=(\omega_8+\omega_8^{-1})^{-1}$; indeed $(\omega_8+\omega_8^{-1})^2=2$ since $\omega_8^2+\omega_8^{-2}=0$. At $ρ$ set $A=c_*(e_{\mathsf b_1}+e_{\mathsf b_2})$ and $B=c_*(e_{\mathsf b_1}+e_{\mathsf b_2}-e_0)$. On the constraint cosets keep the protected evaluations, extending those linear forms by zero in all pad and tag entries. The coordinate polynomials are the unique interpolants of degree below $D$. Store their sparse point-value descriptions rather than a dense coordinate-by-degree table. Define $Z_0$ to vanish at all $d_i$ and $ρ$, $Z$ at every evaluation point except $ρ$, $Z_*=(X-ρ)Z$, and $L_ρ=Z/Z(ρ)$. Thus $Z_*=Z_0Z_{\mathcal K}$, where $Z_{\mathcal K}=\prod_t(X^ν-δ_t^ν)$ is the monic coset vanishing polynomial.

Here is the QAP criterion under this setup. For a symmetric $W$, $P_W=A^\top W B$ takes values $0$ at $d_0$, $W_{ii}-W_{0i}$ at $d_i$ with $i>0$, and $c_*^2(W_{\mathsf b_1,\mathsf b_1}+W_{\mathsf b_2,\mathsf b_2}+2W_{\mathsf b_1,\mathsf b_2}-W_{0,\mathsf b_1}-W_{0,\mathsf b_2})$ at $ρ$. Once the Booleanity tests hold, this last expression equals $W_{\mathsf b_1,\mathsf b_2}$, using symmetry and $2c_*^2=1$. On each constraint coset $P_W/Z_0$ is the list of terms in that constraint's quadratic test. Let $R_W$ be the polynomial of degree below $ν n_c$ interpolating these coset values. The sum of $X^a$ on $δ_t\mathcal G$ is zero unless $ν\mid a$, in which case it is $νδ_t^a$. Among degrees below $ν n_c$, the multiples of $ν$ give an invertible Vandermonde matrix in the distinct $δ_t^ν$. Consequently all coset sums vanish if and only if $R_W$ omits all divisible powers. Under the Booleanity and constraint tests, $P_W-W_{\mathsf b_1,\mathsf b_2} L_ρ-Z_0 R_W$ vanishes at every evaluation point. It is therefore divisible by $Z_*$, with quotient degree below $D-1$ from $\deg P_W\le2D-2$. Equivalently $P_W-Z_0R_W$ is divisible by $Z$ with quotient degree below $D$. Conversely, either such identity with an allowed $R$ implies the Booleanity values and the coset sum tests by evaluation, and $R$ is the unique interpolated remainder. In the key identity, evaluation at $ρ$ gives exactly the specified corner $W_{\mathsf b_1,\mathsf b_2}$. For a witness vector $v$, these identities apply to $vv^\top$, with $P_v=A_v B_v$ and key corner $\mathsf b_1\mathsf b_2$.

The new key evaluation has $A(ρ)=c_*(e_{\mathsf b_1}+e_{\mathsf b_2})$, which together with $A(d_i)=e_i-e_0$ for $i>0$ spans all form coordinates: the differences span the hyperplane of coordinate sum zero and $A(ρ)$ has coordinate sum $2c_*\ne0$. The vectors $B(d_i)=e_i$ are still a basis. These properties, the QAP criterion and the updated $D$ are the only changes in the generic comparison and coincidence arguments, explicitly used in C7. The point descriptions consist of the nonzero input terms and $O(D)$ point data. For evaluation of all coordinate polynomials at a scalar off the point set, tabulate the $D$ Lagrange weights there and accumulate the listed nonzero coordinate entries times their weights. For a witness, accumulate the point values of the two scalar witness polynomials and interpolate only those two polynomials, not the coordinate table. The same subgroup interpolation and vanishing-polynomial algorithms therefore give $O(|S|+D\log D+\log q)$ setup and the claimed scalar polynomial work with these point sets. The extra Booleanity evaluations and the key evaluation add only a constant number of nonzero coefficients. The score still uses the fixed original nonzero-coefficient charge.

## Amendment ell

Set $p=17$, $s_p={\rm short\_columns}$ and $ℓ=\lceil(N_o+2s_p)/p\rceil+3$. Use $s_p$ blocks of fifteen ordinary coordinates, allowed by $15s_p\le N_o$, then blocks of seventeen for the remaining $N_o-15s_p$, padding unused positions with zeros. There are $s_p+\lceil(N_o-15s_p)/17\rceil=\lceil(N_o+2s_p)/17\rceil$ ordinary columns. Put each tag in the constant position of its separate following column and use the independent homogeneous column zero. Every matrix entry is sampled independently uniformly, including those corresponding to zero witness positions.

The placement is injective, preserves coefficient Euclidean norm, and commutes with reduction and field scaling. The first three form slots are $v_0,(H^{(1)})^\top v,(H^{(2)})^\top v$ and the matrix and zero slots follow n. A form-kernel vector has $v_0=0$ and $A\hat v=0$. Thus the short multiple used by the reduction packs to a nonzero solution of the same norm to the uniform Module-SIS problem with dimensions $kd_R,ℓ d_R$. For any fixed tag variant of an external witness, condition on all columns except column zero. Since its homogeneous coordinate is one, the independent uniform column zero adds a uniform coefficient vector to the remaining fixed vector. Consequently each form value is uniform on the affine space where the constant is one and every padding slot is zero. This distribution is sufficient for both the exact key-weight bound and the expected fallback bound.

## Amendment C6

Require $18\le n\le4800$, $n$ even, ${\rm seed\_mode}=1$, $s_0={\rm seed\_degree}$ integral with $2\le s_0\le128$, $2s_0\mid n$, $2n\le D$, and $Δ\ge n+3$. Put $r_H=n/s_0$, an even integer. Require $r_H\mid(q^{s_0}-1)^{28}$. This is the C6 residue test. It ensures that every prime divisor of $r_H$ divides $q^{s_0}-1$. The one-variable field below has degree $n=kd_R+{\rm form\_pad}$, with coefficient positions supplied by Amendment n. The even degree supplies the half-turn and the needed rank of the key-weight quadratic. Set $e=1$, $F_0=\mathbb F_q$, and $Q=q^{s_0}$.

The scored branch fixes $s_0=61$ and $r_H=72$. For fixed tables, test monic $F$ of degree $s_0$ by $X^{q^{s_0}}=X\bmod F$ and $\gcd(F,X^{q^{s_0/l}}-X)=1$ for primes $l\mid s_0$. These force simple factors of degrees dividing $s_0$ and exclude proper divisors. Take the first passing monic polynomial in residue order. Irreducibles exist because proper subfields of $\mathbb F_{q^{s_0}}$ contain at most $s_0 q^{s_0/2}<q^{s_0}$ elements in total.

In $K=\mathbb F_q[X]/(F)$, $Q=q^{s_0}$, take the first passing nonzero representative for $c_H$. Require $c_H^{q^{s_0/l}}\nec_H$ for primes $l\mid s_0$ and $c_H^{(Q-1)/p}\ne1$ for primes $p\mid r_H$. By cyclicity the order tests pass for proportion $\prod_{p\mid r_H}(1-1/p)>1/4$ in this mode. Proper subfields exclude at most $s_0 q^{s_0/2}<(Q-1)/16$. Hence the selection terminates. Define $P_c$ by the conjugate linear factors of $c_H$ and $P_T(T)=P_c(T^{r_H})$. Both selections are public precomputation before Setup, and the proof uses only the tested properties.

Let $t$ be a root of $T^{r_H}-c_H$ in the algebraic closure. If $o$ is the order of $c_H$ and $m$ the order of $t$, then $m/\gcd(m,r_H)=o$. The order tests give $v_p(o)=v_p(Q-1)>0$ at each prime of $r_H$. Thus $m=r_Ho$. For each prime $p\mid r_H$, the binomial expansion gives $v_p(Q^j-1)=v_p(Q-1)+v_p(j)$: raising $1+u$ with $p\mid u$ to $p$ increases $v_p(u)$ by exactly one, since $pu$ is the unique term of lowest valuation. At two this uses $4\mid Q-1$. Raising to an exponent prime to $p$ preserves the valuation by the factorization as $u$ times a geometric sum congruent to that exponent. Iterating proves the identity for every positive $j$. For a positive $j$, the condition $m\mid Q^j-1$ is therefore equivalent to $r_H\mid j$. Thus $t$ has degree $r_H$ over $K$. As it generates $c_H=t^{r_H}$, it also generates $K=\mathbb F_q(c_H)$ over $\mathbb F_q$. Its degree over $\mathbb F_q$ is $s_0r_H=n$. The monic polynomial $P_T(T)=P_c(T^{r_H})$ of degree $n$ vanishes at $t$, proving irreducibility.

At $j=r_H/2$, the same valuations show $m/2\mid Q^j-1$ and $m\nmid Q^j-1$. Consequently $t^{q^{n/2}}=-t$, since $Q^{r_H/2}=q^{n/2}$ and $-1$ is the unique element of order two. Use the monomial basis through degree $n-1$ in the same form slots as above. The reduced $V$ product has even powers only. All three consecutive Frobenius projections have their original field identities and the same coefficient-kernel relation.

For exponent $j$ of Frobenius put $b_j=q^j\bmod r_H(Q-1)$. For each basis monomial $T^a$, its reduced representative is obtained from
\[
 c_H^{\lfloor a b_j/r_H\rfloor}T^{a b_j\bmod r_H}
\]
by expanding the coefficient in the basis $1,c_H,\ldots,c_H^{s_0-1}$ and replacing $c_H$ by $T^{r_H}$. The modulus for $b_j$ suffices because the order of $c_H$ divides $Q-1$. This produces at most $s_0$ powers of degree below $n$, all congruent to $a b_j$ modulo $r_H$. For increasing $a$, the quotient increments by $\lfloor b_j/r_H\rfloor$ or by one more. Compute these two step powers with $O(\log q)$ field operations and tabulate the representatives in $O(n)$ operations using the bounded degree. Evaluate the table in $O(n)$ operations given the evaluation point's powers. The resulting coefficients are used in the same ring transpose circuit and assigned to the same coefficient slots. 

## Amendment C7

Require $\mathrm{base\_degree}=\mathrm{base\_left}=\mathrm{base\_right}=\mathrm{scalar\_rel}=1$, $K_1=122$, $K_2=18$, $2K_1K_2=n$, $\mathrm{mask\_stride}=18$, $q\equiv1\bmod72$ and $C_{\rm mask}=52481$. Put $e=A_H=B_H=1$ and $h=n$. In C6's degree-61 base field write $U_0=T^{72}=c_H$ and let $H$ be the subspace of elements of degree at most 30 in $U_0$. It has dimension 31. Put $\tau_F=σ^{n/2+1}$. For each $0\le j<36$, $\tau_F(T^j)=T^j a_j$ with $a_j\ne0$ by $q\equiv1\bmod72$. The dimension formula for $H\cap(a_j\tau_F|_K)^{-1}H$ gives at least $62-61=1$. Fix its first nonzero echelon vector $r_j$ in the base power basis, using $r_0=1$. Set $R_j=T^j r_j$ and $L_a=T^{72(a\bmod61)+36\lfloor a/61\rfloor}$ for $0\le a<122$. A superscript plus is the reduced representative of $\tau_F$.

For each residue modulo 72 the 61 products $L_a R_j$ in it are a basis because they are the base power basis multiplied by $r_j\ne0$. E/O use the even/odd $j$, respectively, and V reuses the even $j$. Expand $U=zσ^{n/2-1}(z)$ and $V=zσ^{n/2}(z)$ in these product bases to obtain the weights. Each scale has independent right digits and cell products modulo $P_T$. The key basis element is one. To extract weights multiply the component in each residue by $r_j^{-1}$ with three fixed polynomial products of length at most 121. First multiply by its fixed inverse representative. Then reverse the high coefficients and multiply by the precomputed reciprocal of the reversed monic modulus, truncating to 60 to recover the reversed quotient. Subtract the quotient times the fixed modulus. Each fixed product uses at most 121 field multiplications by the integer-node interpolation of C5, using 121 nodes and cached factors. Its transpose uses the same count by reversing the linear circuit, so coordinate extraction and its transpose each cost at most 363 products per residue. The V list uses only the 36 even residues. Both left degrees are at most 4356, both right degrees at most 2195, and the V degree at most 2194. Cache all C7 tables.

### Factor masks and publication

Use the shifted centered sampler of I5 in the internal dimension and the following independent scalar coins. The evaluation coin $υ$ is uniform nonzero, the scalars $π,s_{\mathrm U},s_{\mathrm V},ζ_0,ζ_1,ζ'',η,Ω_{22},α$ are independent uniform nonzero, $Ω_{12}$ and the coordinates $y_i$ are independent uniform scalars, and $τ$ is uniform off the evaluation points. Sample $ε$ uniformly from the field excluding $0,-1$. The three derived scales are $(η_1,η_2,η_3)=η(1,ε^2,ε^4)$. The primitive coins just listed have independent ranges. Use the ordinary and conjugate digits just defined. Write $z_-,z_\circ,z_+$ for the reduced vectors of linear form coefficients at Frobenius powers $n/2-1,n/2,n/2+1$, respectively, evaluating at $υ$ when used as scalars. Set
\[
 π_a=π(L_a(υ)+ε L_a^+(υ)),\qquad
 s_{\rm leg}=s_{\mathrm X}R_{\rm leg}(υ),\qquad
 γ_c=π_a s_{\rm leg},\qquad
 \kappa=γ_{\rm key}L_ρ(τ).
\]
Set $s_{\mathrm X}=s_{\mathrm U}$ on E and O and $s_{\mathrm X}=s_{\mathrm V}$ on V. The right and product bases distinguish each leg and cell separately in each scale. Here $π_0=π(1+ε)\ne0$, hence $\kappa\ne0$ on valid coins. On E/O use the right mask
\[
 \vartheta_{\rm leg}
 =R_{\rm leg}(υ)(η_1 z_\circ+η_2 z_+)
   -ε^{-1}R_{\rm leg}^+(υ)(η_2 z_-+η_3 z_\circ),
\]
and on V use $R_{\rm leg}(υ)(η_3 z_+-η_1 z_-)$. For every input coordinate $i$ including tags, use the left row $π_a(y_i,A_i(τ))$ and the right column $(s_{\rm leg}(r_i+A_i(τ))+\vartheta_{{\rm leg},i}, s_{\rm leg}(B_i(τ)-y_i))^\top$. Multiply each left row on the right by the hidden-basis matrix with rows $(1,Ω_{12})$ and $(0,Ω_{22})$, and each right column on the left by its inverse. Use the resulting raw coordinate exponents for G1 and G2 and the raw Y exponent vector $(ζ'' y_i)_i$. Publish their contractions below and the G2 search bases $[s_{\rm leg}]_2$. There is one right sector and there are no alpha-scaled source-group inputs. Keep the public target-group element $[α\kappa]_T$, with independent $α$, and the seed and masked message. This slot preserves the protected overhead count. The decryption algorithm does not require this target-group input.

### Transmitted coordinates for the prescribed pads

Keep the full internal dimension $N_o+4$ for the sampler, QAP, forms and ring instance. For transmission put $N_{\rm pub}=N+252$. Retain the homogeneous index, the external indices, the fifteen small single pads, the second position of each of the 237 pairs, and the three tag indices. Write $I_{\rm fix}$ for the 200 fixed-one pads, and $A_i,B_i$ for the first and second indices of pair $i$ in this paragraph. Define a linear embedding $\mathcal T$ into the full coordinate space by columns
\[
 b_0=e_0+\sum_{j\in I_{\rm fix}}e_j+\sum_{i=1}^{237}e_{A_i},\qquad
 b_{B_i}=e_{B_i}-e_{A_i},\qquad b_j=e_j
\]
for the remaining retained indices. The rows at the retained indices form an identity, hence the embedding is injective. The prescribed completion for every tag variant is exactly $\mathcal T v'$ for its vector $v'$ of retained coordinates: the fixed pads equal $v'_0=1$ and the first pad of a pair is $1-v'_{B_i}$. The full internal Booleanity constraints, secret draws and uniform matrix columns are retained.

For each of the raw left and right factor coordinate vectors and the raw Y vector, compute its contracted exponents $\mathcal T^\top X$ by sums and differences before multiplying the group generator. Thus each array has $N_{\rm pub}+4$ transmitted entries. The same contraction on the ordinary subspace applies to the common-direction left array of n1. The scalar guards already pay for computing the full raw exponents, and contraction takes additions only. Every transmitted slot still uses one generator multiplication. For an honest completion the contracted coordinate sum is $(v')^\top\mathcal T^\top X=v^\top X$, so all full-witness polynomial identities and search variables below are exact for the transmitted arrays. Decryption initializes each source sum from its retained homogeneous entry. It adds only the chosen nonzero retained coordinates thereafter.

For the generic view expand each transmitted exponent as the indicated fixed signed combination of raw exponents, distributing products in the target expression. The raw symbols in the view proof below describe these polynomials and are not additional delivered labels. All coefficients of the expansion are independent of the coins and of $r$, so every degree bound and coefficient comparison in the proof applies to the resulting expanded expression. A matrix of matched coefficients on the retained coordinates expands to $W_c=\mathcal T W'_c\mathcal T^\top$ and a search vector to $u_c=\mathcal T u'_c$. The rank of the stack is preserved: $\mathcal T^\top$ is onto on input tuples, and applying $\mathcal T$ to each output is injective. Likewise $W_c r=\mathcal T W'_c(\mathcal T^\top r)$ gives the same joint fiber mass. The stack and its fiber are on the full coordinates used by I5 and I6. The full view gives symmetry, all passing tests and the same field ties on this expanded stack. In particular its fiber conditions and row-space recovery use the original sampler. The expansion of an expression is only an analysis of its coefficients; it introduces no oracle call or extra initial label. The number of compared initialized labels is the actual published count. Linear combination of raw entries also initializes each extractor sketch at the corresponding published entry, because the sketch map on each source group is linear. This is fixed initialization; subsequent transcript operations and the external witness test use the same algorithms.

### Honest cancellation with shared scalar degrees

Use the ordinary and conjugate digits above. In each of the sums below use the cells with the indicated right-leg type:
\[
 W_{\mathrm X}=\sum_{c\in C_{\mathrm X}}W_c L_a R_j,\qquad
 W_{\mathrm X}^{+}=\sum_{c\in C_{\mathrm X}}W_c L_a^+R_j,\qquad
 U^{-}=\sum_{c\in C_{\mathrm U}}W_c L_a R_j^+,\qquad
 U^{\pm}=\sum_{c\in C_{\mathrm U}}W_c L_a^+R_j^+.
\]
The multiplication is of polynomial matrix coefficients and the displayed digit polynomials. Modulo $P_T$, $U^{\pm}=σ^{n/2+1}(W_U)$ because Frobenius acts on the coefficients from the scalar field and multiplies in the form field.

Factor $πη$ from the matched left-right mask products. Expanding $π_a/π=L_a(υ)+ε L_a^+(υ)$ and $(η_1,η_2,η_3)/η=(1,ε^2,ε^4)$ yields the following six coefficient polynomials, evaluated at $υ$:
\[
\begin{array}{c|l}
i & M_i \\
0 & W_U z_\circ-W_V z_- \\
1 & W_U^+ z_\circ-W_V^+ z_- - U^- z_- \\
2 & W_U z_+-U^{\pm} z_- \\
3 & W_U^+ z_+-U^- z_\circ \\
4 & W_V z_+-U^{\pm} z_\circ \\
5 & W_V^+ z_+
\end{array}
\]
The paired contributions at degrees 1 and 3 use common lists. The three even degrees contain the separate field ties.

For honest coefficients and a witness, contract each matrix and the form vectors with its witness coordinates as in the matched factor expression. The two weight polynomials are $U=zσ^{n/2-1}(z)$ and $V=zσ^{n/2}(z)$ reduced in the form field, with the latter half-turn invariant. Evaluation of the three even-degree expressions in the form field gives zero by
$U z_\circ=V z_-$, $U z_+=σ^{n/2+1}(U) z_-$ and
$V z_+=σ^{n/2+1}(U) z_\circ$. Each follows by substituting the two products and commuting the factors. Thus the three even-degree polynomials are exactly divisible by $P_T$. These identities for honest masks leave the QAP and key-weight calculations unchanged.

### Six transmitted cancellation lists

The product degrees are at most $4356+2195=6551$, also when either or both legs are conjugated. Thus the even quotients have length at most 6551 and the odd lists at 1 and 3 have length at most $6551+n=10943$. At 5 the V degree discount leaves 10942 slots.

Publish G2 lists with exponents $(πη/ζ'')ε^iυ^a$ for consecutive $a$ starting at zero, multiplied by $P_T(υ)$ only for even $i$. Lengths are $6551,10943,6551,10943,6551,10942$, summing to $C_{\rm mask}=52481$. Take the coefficients of $M_i/P_T$ for even grades and $M_i$ for odd grades. Their signed MSM paired with the witness-summed Y removes the exact mask. The $υ$ degree is at most $3n-3$. In the formal view the even lists affect the three separate ties only by multiples of $P_T$. Monic divisions and digit sums use $O(s_0n)$ operations and the polynomial products $O(n\log n)$ at fixed $s_0$.

### Scored encryption arithmetic

This accounts for all arithmetic of the admitted finite mode. Write $S_{\rm nz}$ for the number of nonzero point coefficients traversed in preparing the QAP exponents, to which the benchmark assigns $2^{30}$. We show at most $S_{\rm nz}+3m$ variable scalar multiplications in that cost convention.

At $υ$, C6 gives 72 blocks of side 61 per non-half-turn map, as Frobenius permutes the 72 relative residues. Pair 60 of the 61 inputs in each block with the C5 identity. Shared input work costs 30 products; each of 61 outputs uses 30 pair products and one unpaired product. In total $144(30+61\cdot31)=276624$ products suffice. The half-turn uses signs. Form the two table values for the scaled forms
\[
 A'=η_3(η_1 z_\circ+η_2 z_+),\qquad
 B'=η_1(η_2 z_-+η_3 z_\circ).
\]
Precompute the three products of the two distinct $η$ scales that occur on the right. Thus evaluating the combined tables still uses at most four products per form coordinate. Their packed coefficient outputs have the same scales. Their difference $C'=A'-B'$ equals $η_2(η_3 z_+-η_1 z_-)$.

Use the invertible evaluation representation of the period coefficient ring from C5. For each of the two independent masks pull the row functional back through $E^{-1}$ using its transpose. After the pointwise products pull each accumulated column functional back through $E$ using its transpose. By C5 the row pullback costs $U_d=33$ products and the column pullback $V_d=33$. The transformation cost is at most $2(U_d k+V_d(ℓ+1))$.

For each evaluation root write the two transformed row-weight sequences as $A^{(1)},A^{(2)}$, and the uniform matrix column as $B$, all of length $k$. For a pair of consecutive indices $u,v$ add
\[
 (A^{(h)}_u+B_v)(A^{(h)}_v+B_u)
 - A^{(h)}_u A^{(h)}_v - B_u B_v
   = A^{(h)}_uB_u+A^{(h)}_vB_v,\ h=1,2.
\]
Compute the sum of the row-only terms separately for the two rows and the sum of the column-only terms once per column, shared across the two outputs. The identity verifies both desired matrix products term by term. Every pair uses two main multiplications and one column correction product. A final unpaired row needs two products per column. The two row corrections take $2\lfloor k/2\rfloor$ products per evaluation root. Hence the total cost of the products and both transforms is bounded by
\[
 W_{{\rm mat}}
 =d((ℓ+1)(3\lfloor k/2\rfloor+2(k\bmod2))+2\lfloor k/2\rfloor)
       +2(U_d k+V_d(ℓ+1))=W .
\]
The two coefficient outputs are $A',B'$, with the first three slots from the fixed table. For every dynamic scalar $x$, use successive finite differences for $16j+1$ and $(j+1)^a\bmod P$, $a=2,3,4,5$, initialized at the first index. The fifth differences are constant before reduction. Update lower differences in increasing order by adding the next higher one and reduce by one subtraction on wraparound. Track $x$ times each residue by the same additions, subtracting $Px$ at each corresponding wrap. Initialize with binary additions for the fixed integers, and skip the prescribed indices in the output. The fifth weight sums the four entries and the remaining pad weights are fixed integers, scaled by binary additions. Tags contribute zero. Thus all six shifts and first-two-row mask terms use only additions beyond the two charged products; $C'=A'-B'$ as above.

Partition the QAP roots into the $N_o+5$ Booleanity and key singleton factors and $n_c$ constraint cosets. Their vanishing factors at $τ$ are respectively $τ-p$ and $τ^ν-a^ν$ for a coset represented by $a$. Compute $τ^{2^j}$ for $1\le j\le11$ by successive squaring. On the list of $b=N_o+5+n_c$ factor values, ordered with singletons first, use prefix and suffix products to get their product and their outer complements. Prefix values through the singleton group and the whole list give $Z_0(τ)$ and $Z_*(τ)$. A first value and an end complement can be copied without multiplying by one. The full prefix uses $b-1$ products, the suffix excluding its unused first product uses $b-2$, and the $b-2$ interior complement products supply the rest. At a coset node of size $2^j$, split it into its two child cosets of size $2^{j-1}$. Each child's vanishing evaluation is the precomputed power $τ^{2^{j-1}}$ minus the corresponding public power of a representative. The two child complements are the outer complement at the parent times the sibling vanishing evaluation. With two multiplications per internal node of a $ν$-leaf tree, this provides all $Z_*(τ)/(τ-p)$ using $2(ν-1)n_c$ products after the outer pass. At $ρ$ the complement is $Z(τ)$. The sum of all products is at most $3b-5+11+2(ν-1)n_c=2D+N_o+n_c+11$, which fits the $2D+N_o+n_c+16$ term. The public QAP coefficients at $p$ are encoded with the fixed multiplier $1/Z_*'(p)$. Multiplying an encoded point coefficient by its cofactor now makes the exact Lagrange contribution with one multiplication. The 692 new Booleanity points use at most 2076 coefficient products. Together with the five entries at the key point these use at most 2081 of the 2083 products reserved in the constant 2099 of the first line of $V$. All these scalars are over $\mathbb F_q$.

The G1 factor computations use at most $(2K_1+2)(N_o+4)$ multiplications apart from the compiled per-leg scales. Compute the one shared expression $A_i+(Ω_{12}/Ω_{22})y_i$ per coordinate. The second left factor has this value multiplied by $Ω_{22}π_a$, computed once per leg. Its expansion is exactly $π_a(Ω_{12}y_i+Ω_{22}A_i)$. The first factor and the Y column use their original single products. In G2 let $U_i=B_i(τ)-y_i$ and $V_i=r_i+A_i(τ)-(Ω_{12}/Ω_{22})U_i$. Compute $V'_{\rm U}=η_3 s_{\rm U} V+A'$ and $V'_{\rm V}=η_2 s_{\rm V} V+C'$. This costs three products per coordinate including the computation of $V$, since each scale is fixed throughout the coordinate vector and $C'=A'-B'$ is formed by subtraction. The first right factor on an E or O leg is $a'V'_{\rm U}+b'B'$ with $a'=R_{\rm leg}(υ)/η_3$ and $b'=-ε^{-1}R_{\rm leg}^+(υ)/η_1$ precomputed. Its expansion in the unprimed quantities is the specified right exponent. Precompute the single shared product $V'_{\rm U}B'$ per input coordinate and one product $a'b'$ per E or O leg. The identity
\[
 a' V'_{\rm U}+b' B'=(V'_{\rm U}+b')(B'+a')-V'_{\rm U}B'-a'b'
\]
takes one remaining product per entry. For a V leg use one product $(R_{\rm leg}(υ)/η_2)V'_{\rm V}$, with its scale precomputed. The second factor on every leg is the original $(s_{\rm leg}/Ω_{22})U$ and uses one product. All these calculations reproduce the original exponents over the given scalar coins; their case distinctions use only the public leg types. Thus the right work per coordinate, including three shared-vector products and the one product shared across E and O legs, is at most $6K_2+4$. The grouped count for both source groups is $(2K_1+6K_2+6)(N_o+4)$, plus the original precomputation of $2K_2$ pair products and the fixed table allowance for the new scales.

### Reused scale factors for the published source exponents

For the sparse list start at $ζ_0$ and advance by $τ^ν$, obtained in eleven squarings including $τ^2$. For each entry multiply by $τ$ for its shifted copy. This uses at most $2S_0-1$ products after the eleven. The non-sparse list starts at $ζ_1τ$ and advances by $τ$ except across excluded multiples of $ν$, where it uses $τ^2$. Including its first product it costs at most $Δ-Δ/ν$. Together the two use at most $Δ-Δ/ν+2S_0+16$ products. The recurrences retain the scale factors, including at $τ=0$, and each slot uses its own fixed-base multiplication.

Precompute the sparse and regular right constants. Each corresponding slot multiplies $γ_c$ by its constant. Search exponents copy the leg scales. Mask slots multiply the powers of $υ$ by the precombined grade constants with the modulus in grades zero, two and four. The generator repeat costs nothing.

For the shared direction data of n1, obtain the three tag Lagrange values from the tag-three coordinate, from $A_1-c_*L_ρ$, and from $A_2-c_*L_ρ$. The key exponent formation already computes $L_ρ$. At $τ$, compute the shared left scale $ζ_0/U(τ)$ using the inverse charged below. The array combines $S_j=A_j^{\rm o}+B_j^{\rm o}$ by an addition and inserts the single homogeneous correction before multiplying by that scale, for $N_o+1$ products. The five fixed quotients of n1 are formed directly using two products for each numerator at most, plus one scale product per entry and one product for each shifted copy; including the shared inverse scale takes at most 21 multiplications. Compute the three linear factors and $U(τ)$ with two products; the two extra right list constants each use multiplication by $U(τ)/ζ_0$. Including one more product for this shared scale, a product for $c_*L_ρ$, and fixed constants or copies, all these extra scalar computations fit the $(N_o+1)+100$ bound. The two new right lists use one product per entry after the common constants are prepared, included in the counted correction slots.

Fixed work uses $276624+4n$ products for Frobenius blocks and weights, $3n$ for powers of $υ$, and fewer than $35n$ for scales. Binary powering of $(τ^ν)^{Δ/ν}$, the regular recurrence and sparse constants cost at most $2J+600$. Horner and the key, grade and common scales use at most $n+35$: four products extend the powers of $ε$, two derive the mask scales and three form the key. The compiled left scales cost at most $n$ and the two short right lists at most $72\cdot31<n$. This fits $276624+54n+12J+700\le276624+60(n+J+1)$. At most ten scale inverses, including $Z_*(τ)$ and $U(τ)$, fit the separate 10000-product guard.

C5 sums the proved scalar charges. The two target exponents share generator multiples two through seven, prepared in six products. Each exponent uses 85 three-bit windows, with three squares and one further product per window. At tariff 67, $6+2\cdot85\cdot4=686$ target products cost $45962$ field products. Thus $W+V\le3m$ gives the required bound $S_{\rm nz}+3m$, besides charged group operations.

### Efficiency and asymptotic choices

The count amendments prove publication and group-operation counts. Each matrix entry uses one seed query, shared by the at most eight tag variants. Each algorithm uses at most one key query. C5 costs $O(k(ℓ+1)d_R\log(2d_R))$ per form application, the masks cost $O(n\log n)$ after setup, and n1 uses $O(D\log D+|S|)$ QAP work. The expected search count is in search_spread.

### Deterministic setup in the scored mode

C5–C7 select fixed public moduli and transform tables before instance setup. A supplied system is scanned and encoded in the D and n1 subgroup layout, costing $O(|S|+D\log D+\log q)$. No field search occurs in this setup and no table is transmitted.

### Parameter selection and Corollary 5.8

At the benchmark security level and shape use these parameters and the protected subgroup placement. For other inputs the original selector and all associated algorithms apply.

For linear-size systems with $N\geλ^2$ the original size, encryption, nonsearch decryption and expected-search scales are $λN$, $λ^2N/\logλ$, $λN\logλ$ and $2^{λ/4}N^{1/4}$. The new branch fixes $(λ,N)$ and its ledgers and $q$-bounded search ranges bound the four costs uniformly. Divide by the positive scales and take maxima with the original constants.

### Algebraic and reduction interfaces

In `lem:moore`, the field has degree $n$ and $z$ plays no role in the statement. To derive the property at the amended degree, if a combination of $d$ successive Frobenius columns is zero then a polynomial $\sum_{j=0}^{d-1}a_j X^{q^j}$ vanishes at the entries of $σ^s(h)$. Its roots are closed under $\mathbb F_q$-linear combinations, and the independent entries give $q^d$ distinct roots. If any coefficient is nonzero, its degree is at most $q^{d-1}$, a contradiction. This proof uses only the field and its Frobenius.

Here is the full classification argument for the actual field ties of Amendment C7 with the specified $z$. Let $W_c$ be symmetric, pass the Booleanity tests, and satisfy the original three ties, with row space $\mathcal V$ of dimension $d\le3$ containing no kernel vector. The zero-dimensional case has zero stack. Let the columns of $U_*$ over $\mathbb F_q$ be a basis of $\mathcal V$, with rows $u_i^\top$. These rows span $\mathbb F_q^d$. For $s$ in $\mathcal I_*=\{n/2-1,n/2,n/2+1\}$, put $h_s=U_*^\topσ^s(z)$, and put $h_0=U_*^\top z$. Injectivity of $z$ on $\mathcal V$ means the entries of $h_0$ are independent over $\mathbb F_q$. In particular $d\le n$, and the Moore property proved above gives that the three $h_s$ span over $\mathbb F_{q^n}$. Write $W_s$ for $W_U,W_V,σ^{n/2+1}(W_U)$ in the indicated order. Each $W_s$ has its rows and columns in the extension of $\mathcal V$, so $W_s=U_* X_s U_*^\top$ for a unique symmetric $X_s$. Indeed a left inverse $L_*$ of $U_*$ exists, and $X_s=L_*W_sL_*^\top$; projections back to $\mathcal V$ act identically on the columns and rows. The ties give $X_s h_{s'}=X_{s'}h_s$. If $\sum_s a_sh_s=0$, then $(\sum_s a_sX_s)h_{s'}=0$ for every $s'$, and spanning gives $\sum_s a_sX_s=0$. Thus there is a linear map $X$ with $X(h_s)=X_s$. The trilinear form $C(h,u,v)=u^\top X(h)v$ is symmetric in the last two slots and in the first and last slots by the ties, initially on spanning $h_s$ and then on all vectors by linearity. It is therefore fully symmetric. Each Booleanity test gives $C(h,u_i,u_i-u_0)=0$ on the spanning $h_s$, hence on all $h$. The identities $X_s=σ^s(X_{n-s})$ for $s=n/2-1,n/2$ follow from the relation between the first and third matrices and because $W_V$ has even $T$-degrees and $σ^{n/2}$ fixes the scalar coefficients, as $U_*$ and $L_*$ have field entries fixed by $σ$.

First suppose $u_0\ne0$. Extend $l_0=u_0$ to a basis $l_0,\ldots,l_{d-1}$ chosen from the rows. For each $δ\in\{0,1\}^{d-1}$, let $p_δ$ satisfy $l_0^\top p_δ=1$, $l_j^\top p_δ=δ_j$ for $j>0$, and set $w_δ=U_*p_δ$. Symmetry lets any repeated positive index in $C(l_i,l_j,l_k)$ be reduced via the test replacing one occurrence by $0$. Hence those values depend only on the set of positive indices present. Conversely the cube of the linear functional $p_δ$ takes the value $\prod_{i\in A}δ_i$ for this set $A$, and all sets occur since $d-1\le2$. The matrix of these values indexed by $A,δ$ is invertible: indexing $δ$ by its support gives the subset-incidence matrix, triangular with diagonal 1 in any inclusion-compatible ordering. Therefore
\[
 X(h)=\sum_δ c_δ(h^\top p_δ)p_δ p_δ^\top
\]
for coefficients in the extension field. The squares $p_δ p_δ^\top$ are independent by the same evaluation matrix, now on pairs of basis vectors since $d-1\le2$. Write $z_δ=z(w_δ)=h_0^\top p_δ\ne0$. Comparing coefficients of the squares in $X_s=σ^s(X_{n-s})$ gives $c_δσ^s(z_δ)=σ^s(c_δ)z_δ$ for the two consecutive $s$. Hence $c_δ/z_δ$ is fixed by $σ$ and belongs to $\mathbb F_q$, as the fixed points of $x\mapsto x^q$ are exactly this field. Write it as $χ_δ$. Returning from the matrix restriction gives $W_s=\sum_δχ_δ z_δσ^s(z_δ)w_δ w_δ^\top$. In particular the first two polynomial representatives give the stack $\sum_δχ_δ\mathbf H(w_δ)$.

Let $f$ be any field-linear test that vanishes on the cells. It vanishes on the $W_s$. Put $Q_*=\sum_δχ_δ f(w_δ w_δ^\top)p_δ p_δ^\top$, a matrix over $\mathbb F_q$. The vanishing gives $h_0^\top Q_* h_s=0$ for all three $s$, hence $h_0^\top Q_*=0$. Independence of the entries of $h_0$ over $\mathbb F_q$ implies $Q_*=0$, so independence of the squares implies $χ_δ f(w_δ w_δ^\top)=0$ for every $δ$. Apply this to all Booleanity tests to deduce that any nonzero coefficient is on a Boolean assignment. If every external constraint test passes, apply the same argument to them to see that each supported assignment is a witness. In any representation by honest stacks of Boolean assignments in $\mathcal V$, the assignments equal some $w_δ$ because their evaluations on the chosen basis fix their $p_δ$. Hence the same test argument applies to any such representation.

If $u_0=0$, take any basis $l_1,\ldots,l_d$ from the other rows. Booleanity implies $C(h,l_i,l_i)=0$, so by symmetry every coordinate of the trilinear form with a repeated index vanishes. This gives zero if $d<3$. For $d=3$ its only possible value on distinct indices is a shared scalar $c$. Evaluating $X_s=σ^s(X_{n-s})$ on pairs of different basis vectors gives $c  h_s=σ^s(c)h_0$ in the basis $l_1,l_2,l_3$, since $h_s$ is obtained from $h_0$ by Frobenius and the basis is over $\mathbb F_q$. If $c\ne0$, the first two consecutive vectors $h_s$ would both be proportional to $h_0$, impossible by the Moore independence of the three vectors in dimension three. So again $X=0$, and the stack vanishes. This proves the classification clauses, including that a nonzero usable stack in the stated case has a witness in its row space.

The rank and inverse clauses of ${\rm lem:heavy}$ are proved in Amendment msis_bound. For the packing clause, write $x\bmod q=a v$, $a\ne0$, for the kernel vector $v$. In either shortness convention $x_0=0$ since $v_0=0$ and $|x_0|<q$. Packing copies each of the $N_*$ coordinates once and inserts zeros. It commutes with reduction, so $A\hat x=aA\hat v=0\bmod q$. For every infinity-short $x$ this gives $0<\|\hat x\|_\infty=\|x\|_\infty\leβ$. For every Euclidean-short $x$ it gives $0<\|\hat x\|_2=\|x\|_2\le B_E$. Only the second problem is costed.

### Degree, view and recovery gradients

Fix the seeded matrix and hence the form coefficients. For source exponents $a$ in G1 and $b$ in G2 include their generators. A guess-free target expression is
\[
 \mathsf E=\sum_{a,b}D_{ab} a b+D_Kα\kappa .
\]
The coefficients are fixed scalars. Source exponents omit $α$. The factor $ϖ=Ω_{22}ζ_0ζ_1ζ''ε$ clears all denominators in every paired product. For degree accounting put $e_*=1$, since C6 admits the bounded seed branch. The degree of $π_a$ is at most $n+e_*$: the ordinary and conjugated left degrees are each at most $n-1$ and the two independent scalar factors are $π,ε$. The QAP factors have degree below $D$, and the hidden-basis matrix supplies at most one further factor. The sparse and shifted G1 powers have degree at most $D$ including scale, and the Y exponent has degree two. The fixed degree bound for G1 is therefore $d_1=D+n+2+e_*$. The degree of $γ_c$ is at most $n+2195+2$ by the right degree. The key scale still has degree three.

Sparse multipliers have degree at most $D+2$, giving cleared degree at most $D+n+2195+8\le2D+n+6$ since $2195<n$ and $2n\le D$. Amendment D uses $N_o+4$ points $d_i$ and one additional point $ρ$, so $Z_0$ has degree $N_o+5$. Thus the regular multiplier $Z_0(τ)τ^{j∆}$ has degree at most $(J-1)∆+N_o+5$. C5 bounds that degree plus $2195$ by $2D-2$. Add the cell scale and the four remaining clearing factors to get at most $2D+n+4$. Raw right factors before masks have cleared degree at most $D+2195+6$. Each right-mask term has degree at most $2n-2$ in $υ$ and scalar factor $ηε^i$ for $0\le i\le4$, so its degree after clearing is at most $2n+8$. A cancellation basis has $υ$-degree at most $3n-3$ and scalar factor $πηε^i/ζ''$ for $0\le i\le5$. Cancelling the denominator with the clearing factor leaves degree at most $3n+8$ in total. Search bases have cleared degree at most $n+5$. Since $2n\le D$, all G2 exponents after clearing fit $d_2=2D+n+6+2e_*K_2$. The cleared key terms fit $D+8$. The product degree before a guessed-operand factor is at most $d_1+d_2=3D+2n+8+e_*(2K_2+1)$. By C5, $K_1\ge K_2+1$. Thus this bound is at most $d_f=3D+2n+2K_1+7$. The extra guess factor of degree one and all listed separate bounds fit $(q-D)ε_f$ by its protected formula. The search coordinates enter only linearly, within the same degree bounds.

For any fixed $r$, the valid scalar coin sets are independent with sizes at least $q-D$, including the two exclusions on $ε$ and the $D$ exclusions on $τ$. The clearing factor is nonzero there. The product-set bound proved in Targets shows that an identity holding on all valid coins is a polynomial identity after clearing, because $d_f<q-D$ by P5 and $ε_f=(d_f+60)/(q-D)$. A nonidentity has coincidence probability at most $d_f/(q-D)\leε_f$. At an identity $\mathsf E=χ\kappa$ the coefficient of $α$ gives $D_K=0$, since $\kappa$ is a nonzero polynomial. All stack comparisons henceforth use only the plain factor sector.

Write the two transformed left exponents as $F_1^{a,i}=π_a y_i$ and $F_2^{a,i}=π_a(Ω_{12}y_i+Ω_{22}A_i)$. The right exponents are
\[
 H_1^{{\rm leg},j}=ℓ_{{\rm leg},j}
       -(Ω_{12}/Ω_{22})s_{\rm leg}(B_j-y_j),\qquad
 H_2^{{\rm leg},j}=s_{\rm leg}(B_j-y_j)/Ω_{22},
\]
where $ℓ_{{\rm leg},j}=s_{\rm leg}(r_j+A_j)+\vartheta_{{\rm leg},j}$ is independent of the hidden basis. No other G2 input contains a hidden-basis variable. For any G1 input $a$ denote its evaluation at $Ω_{22}=0$ by $\widetilde a$; for $F_2^{a,i}$ this is $Ω_{12}F_1^{a,i}$. Take the part of the Laurent identity with $Ω_{22}^{-1}$ and positive degree in $Ω_{12}$. Cancel its common factor $-Ω_{12}/Ω_{22}$. The resulting identity is
\[
 \sum_{a,{\rm leg},j}δ_{a,{\rm leg},j} \widetilde a s_{\rm leg}(B_j-y_j)=0,
\]
where $δ_{a,{\rm leg},j}$ is the coefficient of the pair with $H_1^{{\rm leg},j}$, subtracting the matched coefficient of $F_2^{a,i},H_2^{{\rm leg},j}$ if its G1 input is $F_1^{a,i}$. This follows because only a second left coordinate produces a positive $Ω_{12}$-degree when paired with $H_2$. Substitute $y_i=B_i(τ)+z_i$ with independent indeterminates $z_i$. Then $B_j-y_j=-z_j$, so the coefficient of $z_{j_0}$ is $-\sum_{a,{\rm leg}}δ_{a,{\rm leg},j_0}s_{\rm leg}\widetilde a(B)$ and is zero. Any $z_i$ term of $\widetilde a(B+z)$ contributes degree two, hence cannot enter. The fixed index is $j_0$; no factor $B_{j_0}$ remains.

The left-input types in the sum are $1,ζ_0 p(τ),ζ_1τ^v,ζ''B_i,π_a B_i,Ω_{12}π_a B_i$, separated by degrees in $ζ_0,ζ_1,ζ'',π,Ω_{12}$. The polynomials $p$ include the sparse powers and the new quotient difference polynomials. In the first four types the right basis polynomials distinguish the legs in each scale family. The $ζ_1$ powers are distinct and the $B_i$ are independent by their $d_j$ values. The polynomials in the $ζ_0$ type need not be independent: the identity says for each leg and right coordinate $j_0$ their coefficient-weighted sum is the zero polynomial in $τ$. In this type each $\widetilde a$ is the full first input independent of $y$ and the hidden basis, so its aggregate ordinary pairing with that $H_1^{{\rm leg},j_0}$ vanishes at every coin and every $r$. For the last two types use the constant term in $ε$, giving the independent products $π s_{\mathrm X}L_a(υ)R_{\rm leg}(υ)$. For each coordinate and $j_0$, the relation is linear in $B_i(τ)$; evaluating the polynomial relation at $d_i$ isolates its $i$-th coefficient by Amendment D. Thus the matched factor coefficients agree individually and all unmatched first-right terms cancel identically as sums, which is sufficient both for the class comparison and the derivative. Formal projection onto first-left factors continues to respect formal equality and receives no contribution from the $ζ_0$ type.

In the multidegree with one $π$ and zero degrees in $ζ_0,ζ_1,ζ''$ and net hidden-basis degree, the pairs are the matched factor products, first-left pairs with the search bases and generator, the correction lists in two matching inverse-scale classes, and the Y column with cancellation bases. This enumeration follows by checking the degrees of the published exponents: the left first factors have one $π$, the left second also has one hidden-basis degree, and the three other nonconstant left types carry only one of the three scales. The right factor scales and correction types above are their only complementary types. The left-generator pair with any published right exponent of degree one in $π$ has an inverse scale and cannot enter this class. Define $W_c$ by matched factor coefficients, and $u_c$ by minus the first-left search-pair coefficients. The class identity is
\[
 \sum_cγ_c b_c+\Phi_*=χ\kappa,\qquad
 b_c=y^\top(W_cr-u_c)+y^\top(W_c-W_c^\top)A(τ)
              +(P_{W_c}+Z_c h_c+Z_0 R_c)(τ).
\]
Here the two correction types produce $Z_c h_c+Z_0R_c$ with allowed $R_c$, by the residue-preserving monic division proved in n1. The term $\Phi_*$ collects the masks from the factor products, the Y cancellation products and the first-left generator pairs. It is free of all $s_{\mathrm X}$. Taking the constant term in $ε$ and the coordinates in the independent lists $π s_{\mathrm X}L_a(υ)R_{\rm leg}(υ)$ gives $b_c=0$ except at the key cell, where $b_c=χ L_ρ$. The original identity then also gives $\Phi_*=0$.

For each $c$, the linear coefficient in $y$ at $d_0$ gives $W_c r=u_c$. The same comparison at $ρ,d_i$ shows $W_c-W_c^\top$ vanishes on the spanning vectors in Amendment D, hence $W_c$ is symmetric. The constant coefficient gives $\deg Z_c h_c\le2D-2$ since the $P_{W_c},Z_0R_c,L_ρ$ terms have that bound. Thus $\deg h_c<D$ for a non-key cell or $<D-1$ in the key cell. The QAP identities in Amendment D give all Booleanity and constraint tests, with the ordinary or keyed vanishing factor as applicable. In particular the Booleanity tests follow first by checking the $d_i$, where the key polynomial is zero. In the key cell evaluate then at $ρ$ where the two vanishing factors are zero. The Booleanity equalities reduce $P_{W_c}(ρ)$ to $(W_c)_{\mathsf b_1,\mathsf b_2}$ in the new key evaluation. Therefore $(W_c)_{\mathsf b_1,\mathsf b_2}=χ$. In $Φ_*$ take the part linear in $η$ and compare the separate coefficients of $ε^0,ε^2,ε^4$. The table of matched factors gives $πy^\top M_i(υ)$ at these degrees. Y pairs from the even lists add only multiples of $P_T(υ)$. Odd lists have disjoint $ε$ degrees, and generator terms have degree zero in $η$. The primitive coin independence and degree bound above justify coefficient comparison. Comparing the $y$ coefficients modulo $P_T$ gives all three original field ties, so the full classification through rank three applies.

If $r'$ replaces $r$, the coefficient-matching result shows the difference in the target value is $\sum_cγ_c y^\top W_c(r'-r)$, because no other exponents depend on $r$. Thus the identity remains valid throughout its prescribed locus. If all stacks are zero, it holds formally at every $r'$ and the key corner forces $χ=0$. If an identity is formal for all $r$, its equations $W_c r=u_c$ for every $r$ force all $W_c=0$ and again $χ=0$. A difference of source expressions pairs with the other source generator to an expression of zero stack. If it vanishes identically at any fixed $r$, this argument says it is formally zero, so formally different source expressions have the stated coincidence bound. This proves the view clauses with the new corner and one actual sector.

The formal derivative of the target expression with respect to the search coordinates, for a marked identity, is the vector $\sum_cγ_c W_c^\top y$. To compute it use the private evaluation and reverse accumulation of the reduction. At each recovery point project the G1 input polynomials by setting $Ω_{12}=Ω_{22}=0$ and taking the part linear in $π$; these are exactly the first left coordinates. This is a linear projection and therefore respects formal equality of G1 expressions. The derivative of a first right leaf at retained index $j$ is $s_{\rm leg}b_j$, and the other G2 derivatives vanish. Since the columns $b_j$ are independent, record gradient coordinates in this basis and expand each completed vector once at postprocessing. The matched $F_1,H_1$ coefficients are precisely the coefficients of the projected product in the derivative. Since unmatched first-right coefficients vanish for a marked identity, this is its full stack gradient. Formally equal targets have zero difference stack and the same gradients; formally equal G2 inputs also have equal derivative records by pairing their difference with a first-left input and applying the zero-stack result. The projected gradients always lie in the marked row space. For a nonzero linear functional on it that vanishes on a given proper subspace, the derivative polynomial after dividing by $π$ is nonzero: take its degree-zero coefficient in $ε$ and the independent products $s_{\mathrm X}L_a(υ)R_{\rm leg}(υ)y_i$. Its degree is at most $n+2+R_{\rm leg}$, establishing the recovery comparison used in Targets. The optional empty alpha sector has identically zero stack and gradients.

The running time with the revised exponent lists has the bound
\[
 t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT},\qquad
 C_R=8I+3L+2C_{\rm post}+C_{\rm set}+C_{\rm desc},
\]
Here $I$ is one initial exponent computation, $C_{\rm post}$ one trial's postprocessing, $C_{\rm set}$ transcript initialization, and $C_{\rm desc}$ the description.

Store assignments per group keyed by both label and exponent, marking excluded strings in the same label table. Each record keeps its private test value and first expression reference or zero. For an unclassified operand, one status lookup, integer sample and comparison against the remaining exponent count out of unclassified strings, unused-exponent sample if accepted, two insertions and two counter updates cost at most eight. Rejections only record exclusion and update the denominator count. This is the conditional uniform-injection law. At most two writes attach zero records to record-less operands. For each result budget 24: two lookups, up to six arithmetic operations at the true and test points, lookup and unused-label allocation and two insertions (four), two counter updates, six log writes, four for test comparison, first-difference recording, log advancement and name eligibility. Repeated assignments keep the old record. The name routine rejects ineligible labels, otherwise computes the negation through the same routine, reusing any assigned opposite, and writes at most two labels.

At each of six recovery points the forward log costs at most three arithmetic operations per call. Reverse-propagate each of the at most two trial adjoints from zero-initialized registers. Addition and scalar multiplication propagate their scalar derivatives; pairing propagates its first operand only to the second, since G1 is independent of $r$. At an input leaf with nonzero derivative, accumulate into retained coordinate $j$ the propagated value times the prepared scalar of $b_j$. The other leaves contribute zero. Each predecessor costs at most three operations, including at most two products and one accumulation. Registers are indexed directly, so each point costs at most $3+2(6+1)=17$ per call. Thus $24+2\cdot8+2+2+6\cdot17=146\le148$. The key oracle needs lookup, sample and insertion, and the seed oracle uses $d_R$ coordinate samples instead of one, giving $(d_R+5)Q_H$.

For each of at most eight points, evaluate $O(N_*)$ degree-below-$D$ polynomials, advance $O(D+n)$ powers, and form $O(nD)$ QAP scalars and $O(nN_*)$ factors. Naive ring masks take $O(nd_R+nN_*)$. On a trial expand at most three gradients by the sparse embedding in $O(N_*)$ each, apply the form map and solve its fixed-width system. These and the fixed mask, oracle table, label and advice costs give $C_R=O((N_*+n)D+μ)$, since $d_R,n,N_*\le D$. Each trial uses at most one LIFT. This proves the displayed bound and $t+O(Q+d_RQ_H+μ)+{\rm poly}(D,\log q)$. Extractor sketches use the same coefficient arrays regardless of form packing.

## Amendment P1

Require $Δ\le D$, $J=\lceil((D-1)+νn_c)/Δ\rceil$, $J'=1$, $ν\midΔ$ and $n\le D$. This covers the non-sparse merged interval of n1. Since $(J-1)Δ<U_*=(D-1)+νn_c$ and the shifts preserve residues modulo $ν$, the degree bound for each multiplier $Z_0X^{jΔ}$ is below $2D-1$. The monic division and view proof of n1 handle the actual remainder.

## Amendment n1

There are
\[
 n_1=(2K_1+1)(N_{\rm pub}+4)+2\lceil(D-1)/ν\rceil+Δ-Δ/ν+(N_{\rm pub}+1)+10
\]
transmitted G1 elements. Use the single factor sector, field mask bases and Y column of C7. Let $S_0=\lceil(D-1)/ν\rceil$ and
\[
 I_0=\{0\le a<D-1:ν\mid a\},\qquad
 I_0^*=I_0\cup\{a+1:a\in I_0\},\qquad
 I_1=\{0\le a<Δ:ν\nmid a\}.
\]
Send $P_a^0=[ζ_0τ^a]_1$ for $a\in I_0^*$, and $P_a^1=[ζ_1τ^a]_1$ for $a\in I_1$. There are $2S_0$ sparse entries because $ν\ge2$, and $Δ-Δ/ν$ non-sparse ones by alignment. Use $Z_c=Z_*$ in the key cell and $Z_c=Z$ elsewhere. Send one $B_c^0=[γ_c Z_c(τ)/ζ_0]_2$ per cell and $J$ bases $B_{c,j}^1=[γ_c Z_0(τ)τ^{jΔ}/ζ_1]_2$, $0\le j<J$. The factor arrays, search bases and cancellation arrays are those of C7, each once. Add the tag quotient difference bases below and then apply the same optional existing-generator parity padding, computed as one scalar multiplication by one. Send the seed, the one element $[α\kappa]_T$, and the masked message. There is exactly one fixed-base generator multiplication per transmitted group slot and one more in GT for the key. All scalar exponents use the displayed fixed factors and tabulated powers, with constant work per exponent.

### Reusing right corrections across the four corners

Let $u_i=z(e_i)$ for the first two tag unit vectors. Write $δ_c$ for the product-basis coordinate in cell $c$ of the polar product $u_1σ^j(u_2)+u_2σ^j(u_1)$, with $j=n/2-1$ for U and $j=n/2$ for V. The latter is half-turn invariant, so its exponents are even. For every common base $c_t$ and its corners $a_t,b_t,v^{(t)}$ from the selector below, linearity of $z$ and expansion of its quadratic weights give
\[
 ξ_c(v^{(t)})=ξ_c(a_t)+ξ_c(b_t)-ξ_c(c_t)+δ_c .
\]
Only the public seed and field determine $δ_c$. Send $M_j=\sum_cδ_cB^1_{c,j}$ for $0\le j<J$ and $M'_0=\sum_{c\ne c_{\rm key}}δ_cB^0_c$. For each indicated list compute the ordinary three sums and use first plus second minus third plus the mixed entry for the target. The left operands are as before. Direct normalization uses one ordinary MSM per list, and the key-only entry always uses its own scalar weight.

Convert both tag columns in $66 k$ products; their other form slots are zero. The half-turn $T\mapsto-T$ needs signs only; the two other tag conjugates cost at most $2s_0n$. Use a length-$B=9216$ transform in $\mathbb F_q$, since $B\mid q-1$ and $B>2n-2$. In a radix-three combine, for cube root $ω$ take $s=x_1+x_2,d=x_1-x_2$: the outputs are $x_0+s$ and $x_0-s/2\pm (ω-ω^2)d/2$, using two multiplications. For root $r$ of order $3m$, input $3j+u$ and output $k+mv$ give factor $r^{3jk}r^{uk}r^{umv}$. Thus $T(3m)=3T(m)+2(m-1)+2m$ is an upper bound, counting the nonunit twiddles $r^{uk}$ and the three-point combines. The inverse with reciprocal root has the same count before scaling. For powers of two, $T(2m)=2T(m)+m-1$ with $T(1)=0$: the two half transforms share one twiddle at each index, and the zero-index twiddle is one. Thus $T(m)=(m/2)\log_2m-m+1$, giving $T(512)=1793$ and $T(1024)=4097$. The first radix-three recursion takes $1793\mapsto7425\mapsto28417$ at lengths $512,1536,4608$. The other takes $4097\mapsto16385\mapsto61441$ at lengths $1024,3072,9216$. These are unscaled transform counts; the scaling work is included in the next bound.

Let $H=B/2$. Since $r^H=-1$ at length $B$, the half-turn on coefficients shifts spectra by $H$. Transform both tag values and both non-half-turn conjugates. Compute the U polar by two pointwise multiplications and one inverse with scaling. The V polar is even since the half-turn exchanges its two products. Its spectrum repeats after $H$: compute those $H$ entries using the shifted tag spectra and use a scaled length-$H$ inverse with root $r^2$ to recover the even coefficients. Save the tag spectra for the transposes. The monic form modulus is even, so the U and V reductions cost at most $s_0n$ and $s_0n/2$. With the tag conjugations the cost is $5T(B)+T(H)+9B/2+7s_0n/2$ beyond the tag conversion. Add $A_c$ dot products, $J+1$ scales and $108\cdot363$ products for the two coordinate lists.

For the view condition on the public seed matrix. Expand the new labels into their fixed linear combinations of old right inputs and distribute pairings. The degree, fiber and sketch comparisons apply to the expanded expressions by the same linear initialization as for contracted coordinates. Only the actual published count through n2 enters the initial comparison budget.

### Reusing the cancellation operands

Let $Z$ denote a form value (a length-$n$ coefficient vector, unrelated to the QAP vanishing polynomials in this paragraph). Let $Q_c(Z)=ξ_c(Z)$, and let $B_c(X,Y)=Q_c(X+Y)-Q_c(X)-Q_c(Y)$ be its bilinear polarization. For cell $c=(a,\mathrm{leg})$ define the linear functional $L_c(Z)=π_a\vartheta_{\rm leg}(Z)/ζ''$, where the three forms in $\vartheta$ are the evaluations of the three C6 conjugates of $Z$. Its cancellation MSM exponent is $F(Z)=\sum_c Q_c(Z)L_c(Z)$: C7's quotient bases multiply the quotients at degrees 0, 2 and 4 by $P_T(υ)$ while the other bases evaluate their full coefficients, so their signed sum is precisely the raw mask scalar after dividing out $ζ''$. The three product identities apply to every form value.

For $u_1,u_2$ as above, define the linear functional
\[
 \mathcal L(Z)=\sum_c\big(δ_cL_c(Z)+B_c(Z,u_1)L_c(u_2)+B_c(Z,u_2)L_c(u_1)\big).
\]
Expansion of each quadratic times linear summand shows the mixed finite difference of $F$ at $Z$ is $\mathcal L(Z+(u_1+u_2)/2)$. Indeed its linear part is $\mathcal L(Z)$, and its constant part per cell is $δ_c(L_c(u_1)+L_c(u_2))+Q_c(u_1)L_c(u_2)+Q_c(u_2)L_c(u_1)$, which equals that cell's functional at $(u_1+u_2)/2$ by bilinearity. Publish $[\mathcal L(E_i)]_2$ for the $n$ coefficient basis vectors $E_i$. In an ordinary triple recover the target cancellation operand from the first two ordinary operands minus the baseline operand plus an $n$-point MSM at the shifted baseline form value. Pair with the target's Y sum. Direct normalization uses the original MSM.

Compute $\sum_cδ_c L_c$ in the three conjugate evaluations by three coefficient products per cell. Construct the three dual vectors by transposing the conjugate maps on $(υ^i)_i$. Their products with both tags give $(L_c(u_i))_c$. The resulting dual linear combination gives the first part of $\mathcal L$. The coefficients of each $B_c(Z,u_i)$ are those of $Zσ^s(u_i)+u_iσ^s(Z)$ for its U or V family. First transpose the product-coordinate map on each of the two U/V pairs of lists $(L_c(u_{3-i}))_c$, at most $2\cdot108\cdot363$ products. The resulting V functionals remain even. Apply the two transposed multiplication maps to each list. Use the transpose of $σ^s$ after the second one and sum. Reuse the four fixed conjugates from the quadratic entries.

Reverse the linear circuit by distributing weights at additions and multiplying by the same fixed scalars at multiplication gates. For each U list share one transpose of the reduction and the scaled inverse transform, then multiply by the two cached spectra as in the two multiplication maps. Sum the direct spectra over both tags; for the conjugated path sum the two spectra before the forward transpose and the common conjugation transpose.

Each V functional has only even coefficients. The two polar terms have equal value there because applying the half-turn exchanges them and commutes with the even modulus. Use twice the direct term. Its reduction transpose stays even. The scaled inverse transpose at length $H$ on the even positions, repeated periodically, gives twice the full length-$B$ inverse transpose because $1/H=2/B$. Multiply by the shifted tag spectrum and add these two V spectra to the direct U sum. Thus only two length-$B$ forward transposes are needed. The U and V prefixes, spectral products and forward transposes total $4T(B)+2T(H)+9B+3s_0n$. Two non-half-turn dual evaluations and the remaining U conjugation transpose add at most $3s_0n$; the half-turn dual uses signs. Allow ten products per right leg, one per left digit for its inverse scale, twelve per cell for weighted evaluations and coefficients, and $9n$ for tag evaluations and the dual sum. These fit $20A_c+16n+2000$. The combined compiler cost is $66 k+19s_0n/2+9T(B)+3T(H)+27B/2+21A_c+16n+2001+3\cdot108\cdot363+J=3653061+J$.

For the view take the linear part of the mixed difference in C7's cubic cancellation coefficient vectors before combination with the bases. These functions use the fixed modulus. Their displayed polarization gives exactly the $\mathcal L(E_i)$ exponents after combination. The new labels therefore expand as fixed public linear combinations of existing cancellation types, with the same sketch initialization and their actual count in n2.

### One common left array for the internal tag directions

Let $d'_i,L_i$ be the three tag points and their Lagrange polynomials. The tag coordinate polynomials are $A_i=B_i=L_i+c_*L_ρ$ for $i=1,2$ and $A_3=B_3=L_3$. Put $S_j=A_j^{\rm o}+B_j^{\rm o}$ on ordinary coordinates, and
\[
 U=(X-d'_1)(X-d'_2)(X-ρ),\quad G_j=(S_j+\mathbf1_{j=0}(L_1+L_2+c_*L_ρ))/U .
\]
The values of $S$ at these roots are $-e_0,-e_0,-c_*e_0$, so $G_j$ is polynomial of degree at most $D-4$. Also $U A_i$ has degree at most $D+2$ and vanishes at all QAP points for $i=1,2$. Define
\[
 F_i=-A_i L_{3-i}/Z_*\ (i=1,2),\quad
 F_{ii'}=(2A_i A_{i'}-\mathbf1_{\{i,i'\}=\{1,2\}}L_ρ)/Z_*\ (i<i').
\]
The first numerator vanishes since its factors have disjoint evaluation supports. Of the mixed products only the first two tags overlap at $ρ$, where $2c_*^2=1$. Thus these five quotients are exact and have degree at most $D-2$.

Send the $N_{\rm pub}+1$ ordinary contracted exponent entries of $(ζ_0G_j(τ))_j$ and for each of the five $F$ send $[ζ_0F(τ)]_1,[ζ_0(τ-ρ)F(τ)]_1$. Send $B_c^{(i)}=[γ_cU(τ)A_i(τ)/ζ_0]_2$ for $i=1,2$ in each cell, with the scalar schedule of C7.

For fixed $t$, let $v_0=(w,0,0,t)$ and $v=(w,b_1,b_2,t)$. Set $G_w=\sum_j w_jG_j$ and
\[
 F_v=b_1F_1+b_2F_2+b_1b_2F_{12}+tb_1F_{13}+tb_2F_{23}.
\]
Both variants use the same remainder $R_w$. Expanding the A and B products, the terms linear in each bit after $b_i^2=b_i$ contribute $b_i A_i(S_w+A_i)=b_i(UA_iG_w-A_iL_{3-i})$, with $S_w=\sum_jw_jS_j$ and $w_0=1$. The mixed terms give the remaining quotients, so $P_v-P_{v_0}-d_v L_ρ=U(b_1A_1+b_2A_2)G_w+Z_*F_v$, $d_v=b_1b_2$.

Compute $[ζ_0G_w(τ)]_1$ once. Each present bit requires one weighted MSM of length $A_c$ in the corresponding $B^{(i)}$ list. Add both outputs if both bits are present and pair with the common left operand. Add the fixed sums for $F_v$ and $(τ-ρ)F_v$ to the sparse key and non-key left operands respectively. Their pairs supply $γ_cZ_*F_v$ because $Z_*=(X-ρ)Z$. The separate $d_vP_0^0/Z(ρ)$ on the non-key side restores $d_vL_ρ$ there. Thus the full corrections subtract $P_v-d_vL_ρ$ in the key cell and $P_v$ elsewhere.

The added left inputs are of the existing $ζ_0$ type and have degrees at most $D$. The right inputs of scale $ζ_0^{-1}$ carry $γ_c$ times multiples of $Z_*$, with their degree bounded in C7. Their pairs with $ζ_0$ inputs contribute only multiples of $Z_*$, while old sparse right inputs paired with new left inputs contribute multiples of $Z_c$. C7 absorbs these into $Z_c h_c$ and bounds the degree by its constant comparison. This leaves the other residue classes and the coin laws unchanged.

### A single combination at any tag

At $v_0=(w,0,0,t)$ the key corner is zero. By D the exact quotient $G_{\rm base}=P_{v_0}/Z_0$ is $Z_{\mathcal K}h_{\rm key}^{v_0}+R_w$. Divide its multiples-of-$ν$ part by $Z_{\mathcal K}$ in $X^ν$ to obtain $h^0$. Its complementary part $T_0=G_{\rm base}-Z_{\mathcal K}h^0$ has degree below $U_*$ and only nonzero residues modulo $ν$. For monic division reverse the divisor to constant one and double inverse precision with $u\leftarrow u(2-fu)$, whose error is $(1-fu)^2$. C3 subgroup products use a bounded number of blocks of half the subgroup order per precision, summing to $O(D\log D)$. Interpolate only witness polynomials; the sparse division has length $O(D/ν)$.

Once compute
\[
 H^0=\sum_{a\in I_0}[X^a]h^0 P_a^0,\qquad
 H_{\rm oth}^0=\sum_{a\in I_0}[X^a]h^0 P_{a+1}^0-ρ H^0,\qquad
 H_j^1=\sum_{\substack{a\in I_1\\jΔ+a<U_*}}[X^{jΔ+a}]T_0 P_a^1 .
\]
For each full combination adjust the first operand by the fixed key-tag terms and pair with $ξ_{\rm key}(v)B^0_{\rm key}$. Adjust the second by the shifted fixed tag terms and $d_vP_0^0/Z(ρ)$ before pairing with the weighted non-key $B^0_c$, and pair each $H_j^1$ with the $v$-weighted $B^1_{c,j}$ sum. Also subtract the shared direction pairing when a first or second tag bit is present, as above. The polynomial argument in the preceding subsection shows these subtractions remove exactly the $P_v-d_vL_ρ$ and $P_v$ terms for the key and other cells, respectively.

For each right leg, form the two weighted left operands by summing $ξ_c(v)$ times the witness-summed G1 factor of its left leg over the cells at this right leg. Pair them with the two witness-summed right coordinates. In the resulting sum the hidden basis cancels, the two antisymmetric terms $y(v)A_v-A_v y(v)$ cancel, and the masks are subtracted with the cancellation MSM of C7 paired against the witness-summed Y. The earlier polynomial subtractions remove all $P_v$ terms except the stated key corner. The first weighted left operand alone is the sum of the left first coordinates; pairing it separately with the search base $s_{\rm leg}$ at each right leg and summing gives
\[
 \Psi_v=[\psi_v]_T,\ \psi_v=y(v)\sum_cγ_cξ_c(v).
\]
The full corrected sum is
\[
 Λ_v=[d_vξ_{\rm key}(v)\kappa+r(v)\psi_v]_T .
\]
To evaluate just $\Psi_v$ there is no use of the second factor coordinate, QAP correction or cancellation.

### Finite work of the scalar baseline

For the scored subgroup placement put $M=2^{22}$, $L=2M$, and choose a public scalar $c$ of order $2L$. Then $c\mathcal H_L$ and $\mathcal H_M$ are disjoint. The public system representation can include the fixed interpolation scalars and tables used below. They depend only on the selected points and field and are determined when the system is encoded. They add no group element or field value to the ciphertext.

For each of $F=A_{(w,0,0,0)},B_{(w,0,0,0)}$, partial fractions at the QAP points $p\in\mathcal P\subset\mathcal H_M$ give
\[
 F(X)=\frac{Z_*(X)}{X^M-1}\sum_{j=0}^{M-1}X^j\sum_{p\in\mathcal P}F(p)p^{-1-j}/Z_*'(p).
\]
Indeed $F/Z_*$ has residues $F(p)/Z_*'(p)$ and $(X^M-1)/(X-p)$ supplies the geometric sum. Encode public point coefficients with $1/Z_*'(p)$ and add selected coordinates, then multiply each accumulated entry by $p^{-1}$ for the transform weights. Both arrays need at most $2D$ products. The encryption cofactor computation uses the same encoding.

For each array use one length-$M$ transform for these coefficients and two more for evaluation on the cosets of $\mathcal H_M$ in $c\mathcal H_L$, scaling by the fixed coset powers. This is six transforms and at most $4M$ scalings total. For tag three set to one, add the public tables $F_{\rm tag,3}(x)(x^M-1)/Z_*(x)$ on those shifted points. They can be prepared at setup with the same transforms in $O(D\log D)$ work. Multiply the two evaluated numerators and the fixed quotient factor $Z_*^2/(LZ_0(X^M-1)^2)$ there. All denominators are nonzero on this disjoint domain. One unnormalized length-$L$ inverse and at most $U_*$ scalings by powers of $c^{-1}$ recover the exact quotient coefficients, since its degree is below $U_*<L$. For a transform of length $B$, the butterfly count is $T(B)=B\log_2B/2-(B-1)$ non-unit twiddles, subtracting one unit twiddle per block. At other point placements use direct interpolation and exact division as above.

For the finite matrix evaluation, write the packed witness entries as bits $b_{j,t}$ in the unit-containing period basis of C5. In row $i$, first sum the tuples $E(M_{ij})$ for which $b_{j,t}=1$, separately for each possible $t$. This costs additions only. Multiply each tuple sum componentwise by the fixed tuple $E(b_t)$ and sum the results. Evaluation is a ring isomorphism, so applying $E^{-1}$ once to this total yields the coefficient vector of the ordinary witness product. Convert the three individual tag-column tuples with one inverse each in that row; the homogeneous column is included with its ordinary bit value one at position zero. There are at most $kd^2$ scaling multiplications, plus $4kd^2$ for the inverse matrices. Thus this implementation uses at most $5kd^2=372810$ multiplications at $d=17,k=258$. The other work consists of at most $O(k(ℓ+1)d^2)$ additions, a constant multiple of the finite matrix length for the admitted degree. This gives the previous scalar allowance with the period coefficient ring.

The weights of the at most eight needed form values use three conjugate applications with at most $3s_0 n$ multiplications per variant. The two products for $U,V$ fit length-16384 FFTs. Their monic reductions each take at most $s_0 n$ multiplications, because there are at most $n$ elimination steps with at most $s_0$ lower terms per step. With $s_0\le128$, $n\le4800$, the conjugations and reductions use at most $40s_0n\le24576000$ multiplications. The sixteen products use at most $16(3T(16384)+2\cdot16384)<6$ million more by the nonunit twiddle bound, pointwise products and inverse scalings. All weights with at most $8\cdot108\cdot363$ more products for coordinate conversion fit within 32 million, since here $s_0=61$ and $n=4392$.

For each of at most four full mask combinations, form the six weighted leg polynomials. A cell's products $L R,L^+R,L R^+,L^+R^+$ have respectively at most $31,91,31,91$ terms in their single residue, since a left ordinary digit is a monomial and each conjugate left digit has at most 61 terms. Precompute these products. V uses just the first two. The resulting weighted sums need at most $244 A_c$ multiplications per full combination. Nine length-16384 forward and eight inverse transforms compute the twelve polynomial products after selecting the six weighted legs and three conjugate forms. All polynomial degrees are below $3n\le14400$, so this covers the entire output support. Add or subtract the two pairs of odd-grade coefficient vectors after transforming them back, using only additions. Together the FFTs, pointwise products and the eight inverse scalings take less than 2.1 million multiplications per variant. Exact monic division of the first three outputs takes at most $6ns_0$ more multiplications per variant, by the degree and support bounds of the sparse monic modulus. The complete mask preparation therefore costs below 43 million across four full combinations.

The merged correction divides only in residue zero. The quotient is a reversed convolution with the fixed reciprocal truncated at $S_0=1884$; length 4096 costs $2T(4096)+8192=49154$. Thus the baseline and division cost at most $2D+6T(M)+4M+2L+T(L)+U_*+49154<390000000$. The common direction uses precomputed group arrays. MSM coefficients are copies or signs of weights, quotients and fixed setup scalars. Pad and tag selections and public centers use additions and integer operations. Charge one key-weight inverse, and up to one fallback denominator inverse and two products. Each inverse uses at most 508 products by binary powering, so both branches cost at most 1018. Search group work is in search_spread. The mixed cancellation coefficients cost at most $n$ products for their half shifts. The scalar total is below $390000000+32000000+43000000+372810+1018+n<632000000+m$.

### Tag choice and key recovery

For any external witness, let $w$ be its prescribed padded completion and $t\in\{0,1\}$. Set $a_t=(w,1,0,t)$, $b_t=(w,0,1,t)$, $c_t=(w,0,0,t)$, and $v^{(t)}=(w,1,1,t)$, all with homogeneous coordinate one. The three ordinary corners have zero key corner and $a_t+b_t-c_t=v^{(t)}$ as integer vectors. The target has key corner one.

Return $\bot$ if $ξ_{\rm key}(v^{(0)})=0$. Otherwise if $\Psi_{v^{(0)}}=0$, compute its one full combination and normalize directly with its nonzero key weight. If the primary target base is nonzero and $\Psi_{a_0},\Psi_{b_0},\Psi_{c_0}$ are all nonzero, choose the ordinary triple with $t=0$. Otherwise test $ξ_{\rm key}(v^{(1)})$. If it is zero, take the evaluation-point fallback. With nonzero secondary weight, compute $\Psi_{v^{(1)}}$. If that base is zero, use its direct normalization. If it is nonzero and $\Psi_{a_1},\Psi_{b_1},\Psi_{c_1}$ are all nonzero, select the ordinary triple with $t=1$. Otherwise take the fallback. This uses at most eight plain base tests and four full combinations. All full combinations in the chosen path have common third tag $t$, so they need one baseline. Let $v_*$ denote the selected target in an ordinary branch. Branch selection depends only on the bases and form weights, independently of the search coins.

For the selected triple, use $v_0'=c,v_1'=a,v_2'=b$ and let $c_0,c_1,c_2$ denote the rounded centers of the anchor and differences. Before starting line [full-search], form
\[
 Q_0=Λ_c-c_0\Psi_c,\qquad
 Q_1=Λ_a-(c_0+c_1)\Psi_a,\qquad
 Q_2=Λ_b-(c_0+c_2)\Psi_b .
\]
The line solves $Q_0=t_0\Psi_c$, then solves $Q_1-t_0\Psi_a=t_1\Psi_a$ and $Q_2-t_0\Psi_b=t_2\Psi_b$. The two multiplications by the already recovered $t_0$ use signed binary arithmetic on $|t_0|$, with sign handled by the fixed Frobenius inversion. These are the only group products that translate targets within the search. The output is the three centered logarithms in the record below. The later key computation forms $r(v_*)=c_0+c_1+c_2+t_0+t_1+t_2$, subtracts $r(v_*)\Psi_{v_*}$, and multiplies by the inverse key weight. This gives $[\kappa]_T$. One key-oracle query unmasks the message. At most eight $\Psi$ values and four full $Λ$ values are needed, and the triple choice is independent of the search vector.

### Exact fallback when no ordinary triple is available

This fallback runs only after the nonzero key-weight test has passed and the target base is nonzero, when the selector supplies neither a triple with nonzero target weight nor a direct normalization. The sparse G1 list contains $P_0^0$ and $P_1^0$ because $0\in I_0$ and $1\in I_0^*$. Before entering the unified search line, pair each one with the published key-cell operand $B^0_{\rm key}$. The results are
\[
 E_0=[γ_{\rm key} Z_*(τ)]_T,\qquad
 E_1=[γ_{\rm key} Z_*(τ)τ/c_{\rm q}]_T ,
\]
where $c_{\rm q}=1$ for unscaled powers. The exponent of $E_0$ is nonzero because the key scale is nonzero and $τ$ is outside the QAP points. The public polynomials satisfy $Z_*=(X-ρ)Z$ and $L_ρ=Z/Z(ρ)$. The fallback computes the unique discrete logarithm $j\in\{0,\ldots,q-1\}$ with $jE_0=E_1$, by the following direct-key procedure. At stage $h\ge0$, let $w=2^h$. Tabulate $iE_0$ for $0\le i<w$, starting at the identity. Beginning at $E_1$, check the $w$ giant residuals obtained by successive steps of $-wE_0$. A match at giant index $k$ and baby index $i$ gives $j=kw+i$. Accept only $j<q$. Each stage thus covers all nonnegative integers below $w^2$ that lie in the index range, and distinct accepted indices cannot have equal group value. The first stage with $w^2>j$ is sufficient. For the stride, invert $E_0$ by the fixed Frobenius map of Amendment search_spread once, then double $h$ times per stage. Equality of polynomial-basis target elements suffices for lookups. After finding $j$, compute
\[
 K=\frac{1}{(c_{\rm q}j-ρ)Z(ρ)} E_0
\]
and use its key-oracle value to recover the message. Because $E_0\ne0$, its order is $q$ and $j$ is exactly $τ/c_{\rm q}$ in the field. The denominator is nonzero and $K=[\kappa]_T$, including when $j=0$. The traversal is the evaluation-point mode of line [full-search]. It returns the index as the fourth component, and the arithmetic after the line computes the displayed key group element.

The fallback uses two pairings of operands already present in the ciphertext. It publishes no new value. In the generic security experiment these pairings remain ordinary formal expressions of the same exponents analyzed in C7. The proof of extraction treats every adversarial sequence of calls within the stipulated adversary budget. That quantifier is independent of the cost of the honest evaluation-point traversal.

**One search line and its actual result.** The revised line [full-search] receives the selected mode and the corresponding group operands. On the ordinary mode for the chosen triple, the public centers $c_0,c_1,c_2$ are the rounded centers of the anchor and the two increments. The line returns
\[
 T=(r(c)-c_0,\ r(a)-r(c)-c_1,\ r(b)-r(c)-c_2,\ 0).
\]
On the direct-key mode, the same line instead traverses the evaluation-point logarithm search above and returns $T=(0,0,0,j)$. The index $j$ is the nonnegative solution in $[0,q-1]$ to the displayed group equation, and the other three coordinates are zero. The divisor for key normalization is applied afterward using this fourth returned component. On a bypass branch no logarithm is computed and $T=0$. The line also returns the signed component $t$ of largest magnitude with the smallest index breaking ties. This designated scalar result is an actual recovered logarithm, with $|t|=\|T\|_\infty$. The witness-sampler range $[-B,B]$ is used for the first three coordinates. The separate input-domain range $[0,q-1]$ for the fourth comes from the order of its nonzero base. The RMS and pointwise bounds below cover this entire record, including its fourth component. Reconstruction and group normalization follow the line on either path.

### View of the correction polynomials

The sparse quotient bases and the common-direction right lists are the inputs with inverse scale $ζ_0^{-1}$, and only the combined correction bases have inverse scale $ζ_1^{-1}$. The key-scalar degree class in C7 therefore collects the original and tag-difference terms in each cell as $Z_c h_c^0+Z_0 T_c$, with every exponent of $T_c$ in a nonzero residue class modulo $ν$. Monic division of $T_c$ by $Z_{\mathcal K}$ preserves those classes in every subtraction step. Its remainder $R_c$ has degree below $ν n_c$ and is allowed. Multiplying the multiple part by $Z_0$ gives a multiple of $Z_*$, hence of $Z_c$, and it is absorbed into $h_c$. Thus the arbitrary correction is precisely of the required $Z_c h_c+Z_0R_c$ form. The constant-term comparison in C7 bounds the quotient degree by the QAP criterion, and the changed corner is $W_{t_1,t_2}$ from that criterion. Every other Laurent comparison uses the same input types and the same actual field ties, as proved in C7, with the two-sector copies omitted.

## Amendment n2

The exact half-count is
\[
 n_2=\left\lceil\frac{6K_2(N_{\rm pub}+4)+3K_2+(3n/2)(J+3)+C_{\rm mask}+J+1+n}2\right\rceil .
\]
The first two terms count the single right factor arrays and search bases. There is one sparse list of $A_c$ bases, two common-direction right lists of $A_c$ bases and $J$ combined lists of $A_c$ bases, the cancellation count is $C_{\rm mask}$ and the mixed lists add $J+1$ right corrections and $n$ cancellation entries. The optional generator padding gives $2n_2$ actual slots. The G1 count is proved in n1. Together with the fixed one GT element, seed and masked message, these give exactly the protected size formula and the one-generator-multiplication count from the published scalars.

## Amendment dec_sum_g1

The retained homogeneous entry includes all fixed-pad and first-pair contributions. There are at most 252 further selected pad coordinates: the fifteen small single pads and at most 237 selected second pads. Initialize the sum with the retained homogeneous entry and add each selected other coordinate.

Compute padded witness sums of the two coordinates of each left leg and the Y column once with tags omitted, using at most $(N+1)/2+252$ additions per array in the witness-weight convention. The at most eight variants add at most three tag entries per array. The one common-direction witness sum uses at most $(N+1)/2+252$ additional additions. For each full combination add at most five fixed entries to each of its two sparse operands and add at most one further fixed multiple to the non-key operand. The up to four full variants each need at most ten additions for the fixed entries and one for the non-key term. One further addition can subtract the fixed multiple in forming the shifted baseline sparse operand. The total 45 fits 64; other weighted operands are charged as MSMs. The total bound is $(2K_1+1)((N+1)/2+252+24)+(N+1)/2+252+64$.

## Amendment dec_sum_g2

For the single right factor sector, compute each of the $6K_2$ padded witness coordinate sums once, using at most $(N+1)/2+252$ additions each. Only the at most four full combinations need these sums with tags added; each adds at most three entries. Only the target variant has both tag bits set and needs one addition to combine its two direction MSM results. Each mixed recovery uses three G2 additions, including the cancellation recovery and signed subtractions. Thus the count is $6K_2((N+1)/2+252+12)+1+3(J+2)$. The fixed search bases require no analogous coordinate sums.

## Amendment dec_msm_g1

The at most eight first-coordinate weighted left operands and four second-coordinate ones each use $A_c$ points. The baseline sparse key and non-key MSMs use $S_0$ and at most $S_0+1$ points respectively. Charge one more point for the fixed multiple $P_0^0/Z(ρ)$, computed and reused. The baseline non-sparse correction uses $U_*-(S_0+n_c)$ points. These QAP operands are each computed once and shared, and the common-direction witness sum and fixed-entry adjustments were counted as additions. The bound is therefore
\[
 12(3n/2)+D-1+S_0+2+(ν-1)n_c.
\]

## Amendment dec_msm_g2

For each ordinary triple the regular right lists use $3JA_c$ points, and the non-key sparse list uses $3(A_c-1)$ points. Recover their target-corner sums by the mixed entries, with additions counted in dec_sum_g2. The four key sparse operands use four further points. Direct normalization uses at most $(J+1)A_c$ points for these lists. The three ordinary cancellation MSMs have length $C_{\rm mask}$ each, and the target uses one $n$-point mixed MSM. Direct normalization needs at most one cancellation MSM of length $C_{\rm mask}$. For the common-direction lists the numbers of present bits are zero, one, one and two, so at most $4A_c$ points suffice, also covering direct normalization. The total is bounded by $(3J+7)A_c+3C_{\rm mask}+n+1$. The $\Psi$ sums use fixed search bases.

## Amendment dec_pairings

Each of the at most eight $\Psi$ sums uses $3K_2$ pairings. Each of at most four $Λ$ sums uses $6K_2$ factor pairs, $J$ combined correction pairs, two sparse pairs, at most one common-direction pair and one cancellation pair. Thus the total is at most $24K_2+4(6K_2+J+4)$. Accumulate each signed sum starting with its first term, updating by the indicated group addition or subtraction. This needs at most one fewer accumulation operation per nonempty sum than its pairing count. The remaining bounded number of GT translations, final normalizations and searches are accounted for in search_spread.
The exceptional fallback follows the search-base computations and performs two additional pairings with the already transmitted sparse bases. It uses no full combination. Its pairing count is at most $24K_2+2$, within the same bound.

## Amendment search_spread

### Guessing probability for the shifted sampler

This gives the amended stack definition and replaces Lemma 4.5 in full. On internal coordinates let $W$ be the vertical concatenation of the matrices of any stack. Its rank $d$ is the dimension of its row space. It passes when each matrix is symmetric and passes the internal Booleanity and constraint tests in D. For the actual shifted sampler define $\operatorname{gp}(W)=\max_y\Pr[Wr=y]$; heavy means above $θ$ and light means at most $θ$. Write $r=u+Z$ here with $Z$ the independent uniform vector on the span $\mathcal A$ of the public shift directions. This is indeed uniform, since the map from their independent scalar coefficients to their span is a surjective linear map with equal fiber sizes.

For every stack, $\operatorname{gp}(W)\le g^{-d}$. To prove it, fix any value of $Z$ and any target $y$. Pick $d$ independent pivot columns of $W$. After the nonpivot coordinates of $u$ are fixed, the equation $Wu=y-WZ$ specifies at most one full pivot tuple, since the pivot submatrix is injective. If the zero column vanishes, choose $d$ ordinary pivots and fix the other ordinary coordinates. Their specified tuple has probability at most $g^{-d}$ by independence. If the zero column is nonzero, choose a pivot set containing it by extending it to a column-space basis. Fix the ordinary nonpivots. The specified tuple requires $d-1$ independent ordinary box values, with probability at most $g^{-(d-1)}$. After fixing them, $u_0$ is uniform on $g$ distinct residues through the independent diamond, so its specified value has conditional probability at most $1/g$. Rank zero has probability one. This proves the bound for every fixed shift and averaging gives the same bound for $Wr$.

If the row space is spanned by unit vectors with indices in a set $I\subseteq\{1,\ldots,N_*\}$, a fiber of $W$ is a fiber of $r_I$ because the two linear maps have the same kernel. With $B=\{2,\ldots,g+1\}$ reduced into the field, for $y\in\mathbb F_q^I$ one has
\[
 \Pr[r_I=y]=g^{-|I|}\frac{|\mathcal A_I\cap(y-B^I)|}{|\mathcal A_I|},
\]
where $\mathcal A_I$ is the coordinate projection of the shift space. Thus the original unit-coordinate equality holds exactly if every shift has zero projection on $I$. In that case the probability is $g^{-|I|}$ on the independent box. If the projection is nonzero, one coordinate of its support covers the whole field because a nonzero linear map to the field is surjective. It cannot be contained in the corresponding $g$-point coordinate interval of $y-B^I$. The bound is then strict. In particular a single ordinary unit with nonzero shift coefficient has guessing probability $1/q$, and the tag units retain $1/g$.

For any $v$ in the row space of $W$, one has $v^\top=b^\top W$ for a row of coefficients $b^\top$. A maximizing joint fiber $Wr=y$ lies in the scalar fiber $v^\top r=b^\top y$. Hence $\operatorname{gp}(v^\top)\ge\operatorname{gp}(W)$. If $W$ does not annihilate the shift space, $WZ$ is uniform on its nonzero image, so conditioning on $u$ also gives $\operatorname{gp}(W)\le1/q$. If $W$ annihilates it, its fiber law is exactly that of $u$. I5 applies these two facts and the rank bound to prove that every heavy stack has rank at most three, and I6 uses the row-space marginal bound for the inverse interface. No later step requires equality for shifted unit coordinates.

For the following search analysis $r_i,r_\diamond$ denote the underlying $u_i,u_\diamond$ of I5. Honest completions cancel all six sampler shifts, so their recovered dot products are exactly those of these boxes.

Let $σ^+=g\sqrt{(N_o+7)/48}$, $R_0=σ^++3/2$, and $M_1=g/4+1/2$.
The amended spread is
\[
 \max\left\{ R_0,\ R_T,\ 
   (\frac{20}{37}((1000012/1000000)((165889/100000)\sqrt{σ^+}+(47/18+1/5000000)\sqrt{g/2})+118800))^2\right\},
 \ R_T=g\sqrt{(N_o+23)/48}+14 .
\]
The cost uses the concurrent-anchor bound below and $M_1$ bounds an increment in the first triple. Branch choice is independent of the search vector. The terms $R_0,R_T$ bound the RMS of the recombined centered integer and the search record.

For the ordinary search record, the exactly centered variables have second moments bounded by $(g^2-1)(N_o+7)/48$ for the anchor and $2(g^2-1)/12$ for each increment, since each increment involves at most two independent uniform box samples with opposite coefficients. The square of the Euclidean norm is a sum of squares regardless of their correlations. The vector of rounding errors has Euclidean norm below $2$, since the anchor error is at most $3/2$ and each increment error at most $1/2$. The triangle inequality in square mean bounds the ordinary part of the record by $g\sqrt{(N_o+23)/48}+2$. The fourth component is zero except on the direct-key fallback whose probability is at most $135/q^2$ by Targets. Since $0\le j<q$, its root mean square is at most $\sqrt{135}<12$, even with arbitrary dependence between the branch and $j$. Summing these square-mean bounds gives $(\mathbb E\|T\|_2^2)^{1/2}\le R_T$, which also bounds the RMS of the signed greatest component. The first three coordinates meet the range bound from Bsearch and the stated width of any two box samples, and the evaluation-point coordinate meets its stated range.

### Expected absolute anchor

Before the rounding error of at most $3/2$ in I5, the center removes the mean, leaving the sum of independent symmetric variables
\[
 S=X_\diamond+\sum_{i=1}^{N_o+3}(v_i-1/2)X_i ,
 \ X_i=r_i-(g+3)/2 .
\]
Its standard deviation is $σ_S=\sqrt{(g^2-1)(N_o+7)/48}>0$. Let $Y_i$ be its summands divided by $σ_S$, using one more index for the independent diamond term. Set $v_i'=\mathbb E Y_i^2$ and $v_{\max}=\max_i v_i'$. The ordinary summands have $v_i'=1/(N_o+7)$, the diamond summand has $v_i'=4/(N_o+7)$, and $\sum_i v_i'=1$. Each $|Y_i|^2\le3v_i'$ because the square of the largest deviation of an integer uniform sample of width $g$ is $(g-1)^2/4$ before scaling, and the variance is $(g^2-1)/12$. It follows that $\mathbb E Y_i^4\le3(v_i')^2$.

Write $\phi_i(t)=\mathbb E\cos(tY_i)$, $\psi_i(t)=\exp(-v_i't^2/2)$. For $0\le t\le300$ and $N_o\ge359994$, put $w_i=v_i't^2\le1$. Both $\phi_i(t)$ and $\psi_i(t)$ belong to $[1-w_i/2,1-w_i/2+w_i^2/8]$. For cosine the lower bound follows from $1-\cos x\le x^2/2$, and the upper bound follows from Taylor's theorem to degree three with fourth derivative at most one and the fourth-moment estimate above. For the exponential use Taylor's theorem with its second derivative at most one on the nonnegative half-axis for $\exp(-x)$. Both functions are nonnegative on this interval and at most $1-3w_i/8\le \exp(-w_i/3)$. Symmetry and independence make $\phi=\prod_i\phi_i$ the characteristic function of $S/σ_S$. The product $\psi=\prod_i\psi_i$ is the characteristic function of a standard normal. Telescoping the products, using one difference $|\phi_i-\psi_i|\le w_i^2/8$ and bounding each other factor by its exponential, yields
\[
 |\phi(t)-\psi(t)|
 \le \frac{t^4}{8}\sum_i(v_i')^2
          \exp(-(1-v_{\max})t^2/3)
 \le \frac{t^4}{720000}\exp(-t^2/4).
\]
The last inequality uses $v_{\max}\le1/90000$, $\sum_i(v_i')^2\le v_{\max}$, and $1-v_{\max}\ge3/4$.

For real $x$,
\[
 |x|=\frac2π\int_0^\infty\frac{1-\cos(tx)}{t^2} dt .
\]
Scale by $|x|$ and integrate by parts. The remaining sine integral is $π/2$: with damping $e^{-at}$ its value is $\arctan(1/a)$ by differentiating in $a$ and integrating from infinity. Integration by parts bounds the tail by $2/T$ uniformly in $a\ge0$, justifying $a\downarrow0$. Apply Tonelli and subtract the normal comparison. The low-frequency error is below $1/(180000\sqrtπ)$ by the moment bound and $\int_0^\infty t^2e^{-t^2/4}dt=2\sqrtπ$.

For the scored range $359994\le N_o\le479993$ and $g\ge10^{12}$, the cosine bound can be continued beyond frequency 300. Each of the $N_o+3$ ordinary summands has spacing $1/(2σ_S)$ after normalization, up to sign, with distribution symmetric about zero. The finite geometric sum yields its characteristic function
\[
 \frac{\sin(gu)}{g\sin u},\ u=\frac{t}{4σ_S}.
\]
Here $σ_S/g\le100$ by $N_o+7\le480000$. Also $σ_S\ge g$ since $g\ge2$ and $N_o+7\ge360000$. Thus $300\le t\le10^6$ gives $gu\ge3/4$ and $0<u<1/100$. The function $\sin v/v$ decreases from 1 on $[0,π]$: the derivative numerator $v\cos v-\sin v$ is zero at zero and has derivative $-v\sin v\le0$ there. For $v\geπ$, its absolute value is at most $1/π$. Taylor's bound on $\sin(3/4)/(3/4)$ and the lower bound $\sin u\ge u-u^3/6$ therefore give
\[
 \left|\frac{\sin(gu)}{g\sin u}\right|
 \le \frac{1-(3/4)^2/6+(3/4)^4/120}{1-(1/100)^2/6}<\frac{91}{100}.
\]
Both Taylor bounds follow from the alternating power series on the given fixed intervals. Since $(91/100)^8<1/2$ and $N_o+3\ge320$, the product of the ordinary factors is bounded in absolute value by $2^{-40}$ on this frequency interval. The diamond factor has absolute value at most one and the normal factor is also at most $2^{-40}$ for $t\ge300$. Thus the middle integral contributes less than $2^{-40}$ after its $2/π$ normalization. The tail above $10^6$ contributes at most $4/(π10^6)$.

For the numerical bounds below we use $π>314159/100000$. It follows from $π/4=4\arctan(1/5)-\arctan(1/239)$ by using the alternating series through $-x^7/7$ for the first arctangent and the upper bound $x$ for the second.
 
### Relative searches and fallback work

For a centered box of width $g$, summing the two arithmetic half-progressions bounds its absolute mean by $g/4$. Rounding gives $M_1=g/4+1/2$ for each first-triple increment. The later triples have two-input differences of RMS at most $M_Δ=g/\sqrt6+1/2$. They occur with probability at most $9/q$ by Targets. For absolute mean bound $M$ use babies $iP$ for $0\le i<b=\lceil\sqrt M\rceil+1$ and test residuals about centers $j(2b-1)P$, alternating signs of $j$ in outward order. The radius-$b-1$ signed cells partition the integers. The two progression states advance with one update each and the stride needs one doubling and one addition after the babies. The count is at most $b+2|x|/(2b-1)+12$, including initialization and validation. Bounded representatives are unique since $2B+1<q$. Thus the two later increments contribute below $(9/q)8\sqrt{M_Δ}<1$ expected extra primary steps since $g+1<q$ and $M_Δ$ is above $15^2$ on the admitted shape.

**Proposition 5.7(c).** The source sums, MSMs and pairings are proved in their count amendments, including shared final exponentiation. The auxiliary ledger below has $67(13\cdot508+400+1024)+144(1024+8)=686484$ products. Direct fallback adds fewer than two in expectation, including its scalar denominator. Thus $(1000012/1000000)(4352+1)+(686484+2)/6=89075539177/750000<118800$ primary units cover the fixed work.

**Proposition 5.7(d).** The adaptive traversals below take $O(\sqrt{\|T\|_\infty}+1)$ on their actual log record, with $O(\sqrt g N_o^{1/4})$ expected group work. In direct-key fallback, for width $w=2^h$ two tables and the stride take at most $4w$ operations including setup. The geometric sum through $w^2>j=\|T\|_\infty$ is less than twice the last width, which is at most $2\sqrt{j+1}$. The cap including normalization is $16\sqrt q+600$ products. By Targets its probability is at most $135/q^2$, so $67(135/q^2)(16\sqrt q+600)<1$ expected multiplication beyond its two counted pairings. Its scalar denominator adds below one.

### Concurrent tables for the finite signed logs

For the first triple put $xP=Q$, $A=g/2$, $a=\sqrt A$, and $b=\lfloor a\rfloor$. The single centered tag gives a uniform interval of $g$ integers in $[-A,A]$ with second moment at most $g^2/12+1/4$. Condition only on the independent branch choice.

The baby entries are $iP$, $0\le i\le b+1$. The signed giant centers are $2bi$ and $-(2b+2)j$ for positive $i,j$, with zero used once. The giant entry at center $c$ is $Q-cP$. Visit zero, then alternate the positive and negative centers in outward order. Stop a direction when its next nearest-integer cell misses $[-g,g]$. Prepare the two distinct strides $(2b)P,-(2b+2)P$ using the two setup allowances. Each append uses one update. Alternate one baby and one giant until the baby list is complete and retain both tables during this part. Finish the longer list after the shorter one exhausts; discard the giant table once the baby list is full.

Use the same sign classes and recovery of the signed indices as in the fixed-width traversal. A baby and giant match gives $x=c\pm i$. The retained cells cover $[-g,g]$.

Bound the expected count for the baby and giant matches. For $x\ge0$ select the nearest nonnegative center and for $x<0$ the nearest nonpositive one. Break midpoint ties consistently, so a complete cell has $2m$ integers with residuals $-m,\ldots,m-1$, where $m=b$ or $b+1$. Its giant ordinal $G$, starting at zero, satisfies $G\le |x|/b+2$. Let $I$ be the absolute residual. Put $D_b=b+2$. Before the baby list completes the ordinary hit uses at most $2\max(I,G)+2$ primary entries. If $G\ge D_b$, it uses at most $D_b+G+2$. On a complete cell with $G\le m$, averaging gives
\[
 2\mathbb E\max(I,G)=2G+2\sum_{v=G+1}^m\frac{2(m-v)+1}{2m}=m+G^2/m.
\]
For $G\le m\le D_b$ this is at most $D_b+G^2/D_b$ by monotonicity in the denominator variable. For $m<G<D_b$ use $2G\le D_b+G^2/D_b$, and for $G\ge D_b$ use $G\le G^2/D_b$. Thus the conditional bound is $D_b+G^2/D_b+2$. At most four cells are incomplete, at zero and the interval ends. On each the same bound overestimates the required conditional mean up to an added $2D_b$, by the pointwise counts. The expected addition is at most $2D_b\cdot4(2b+2)/g<17$.

For each $x$, use $D_b\ge a$, $D_b\le a+2$, $b\ge a-1$, $|x|\le a^2$ and $a\ge1000$. Then $G^2/D_b\le x^2/a^3+11$, by expanding $(|x|/b+2)^2/D_b$. The extra quadratic part is at most $a((a/(a-1))^2-1)<4$, the linear part is at most $4a/(a-1)<6$, and the constant part is below one. Combining with the incomplete cells, fixed entries and second moment gives at most $(4/3)a+64$ expected ordinary primary candidates. Here $a\ge2^{24}$ by $g\ge2^{49}$.

### Opposite signs in the retained giant table

At each giant append, probe the earlier giants by the same sign-class name used for baby hits. Store the center and sign. Their centers have span at most $2(B+2b+2)<2^{92}<q$, so signed group points cannot repeat at distinct centers. Opposite signs give $2Q=(c+c')P$, hence the integer midpoint of the two even centers. Check the bound $[-B,B]$ as for an ordinary match. At the identity either sign works. Table lookup needs no field products.

For odd $d\ge1$ and $j\ge1$, pair giant indices $(d+j,j)$ with opposite directions, and interchange them for the second target. The implied targets are $db-j$ and $-d(b+1)-j$. The ordinary residual at each target has magnitude at least $b-j$, by its distance $j$ past or before the midpoint of the adjacent centers. The targets are distinct for the pairs below, since odd differences change a midpoint by at least $2b$ and offsets are less than $b/3$. When $S=(2b-4d-6j-6)_+>0$, both targets are in $(-g/2+1,g/2-1)$ and both progressions remain active until the late baby appears. Indeed $d+j<b/2$ and the traversals retain centers out to $g$. The ordinary hit needs at least $2(b-j)-2$ updates, whereas the pair is ready by $4(d+j)+4$. Thus it saves at least $S$ at each target. On the rectangle $[d-1,d+1)\times[j-1,j)$ the function $(2b-16-4u-6v)_+$ is at most $S$. The rectangles have area two and partition the nonnegative quadrant. Integrating first in $v$ then in $u$ gives $(2b-16)^3/144$. Divide by $g=2a^2$ to obtain at least $(a/36)(1-9/a)^3\ge(1/36-10^{-7})a$ since $a\ge2^{24}$. The increment bound is consequently $(47/36+10^{-7})a+128$.

### Local anchor probability

Set $K=\sum_{i=1}^{N_o+3}(2v_i-1)r_i$, with mean $\mu_K$ and variance $s_K^2=(N_o+3)(g^2-1)/12$. Thus $180<s_K/g<182$ and $1.99σ^+<s_K<2σ^+$ on the admitted shape. The rounded anchor is $X=A_0-c_v+r_\diamond+\lceil K/2\rceil$. Conditional on the diamond, the two $K$ integers corresponding to $X=x$ are within $2|x|+g+3$ of $\mu_K$, below $s_K/2$ when $|x|\le0.47σ^+$. This uses $σ^+/g>80$.

For each integer $k$, $s_K\Pr(K=k)$ equals the Fourier integral of its normalized centered characteristic function with phase $e^{-it(k-\mu_K)/s_K}$ on $[-πs_K,πs_K]$, divided by $2π$. Integer-frequency orthogonality gives this formula. Compare the full-line Gaussian integral. The moment telescope above now has all variances $1/(N_o+3)$ and bounds the difference for $|t|\le300$ by $t^4 e^{-t^2/4}/(8(N_o+3))$, with positive-axis integral of $t^4e^{-t^2/4}$ equal to $12\sqrtπ$. Each uniform factor is $\sin(gu)/(g\sin u)$ with $u=t/(2s_K)$. For $300\le t\le1000$, $gu>4/5$, $u<3/g$, and the sine bounds above with $4/5$ give magnitude below $99/100$. For $1000\le t\leπs_K$, use $\sin u\ge2u/π$ and $s_K/g<182$ to get magnitude below $600/t$. Thus the integral error is below
\[
 π^{-1}(12\sqrtπ/(8(N_o+3))+700(99/100)^{N_o+3}+1000(3/5)^{N_o+3}/(N_o+2)+e^{-45000}/300)<10^{-4}.
\]
Here $(99/100)^{100}<1/2$ follows from Bernoulli on its inverse. The Gaussian on $[-1/2,1/2]$ is at least $(398941/10^6)(2711/3072)$ by the cubic lower bound for $e^{-1/8}$ and the height bound below. Since $398941\cdot2711>350100\cdot3072$, each preimage has probability at least $7/(20s_K)$. Averaging the two over the diamond gives $\Pr(X=x)\ge7/(20σ^+)$ in the indicated central interval.

### Two-phase concurrent traversal for the anchor

Keep the two different giant strides, baby indices from zero through $b+1$, and both lookup types used for increments. Here take $A_*=123/100$, $a=\sqrt{A_*\sigma^+}$ and $b=\lceil a\rceil+1$. Retain cells meeting $[-\lceil B/2\rceil,\lceil B/2\rceil]$, which contains the anchor by the sampler's deterministic bound $(N_o+5)(g-1)/4+3/2$. The center span is below $2B+1<q$ since $2b+2<B$, so the table and answer bounds above apply. Use the cumulative baby schedule
\[
 r_1=21/20,\quad r_2=8/5,\quad t_0=2/5,\quad h_0=r_1t_0,\quad t_1=61/80,
 \qquad
 h(u)=\begin{cases}
 r_1 u&0\le u\le t_0,\\ h_0+r_2(u-t_0)&t_0\le u\le t_1,\\ 1&u\ge t_1 .
 \end{cases}
\]
Use the inverse of $h$ on $[0,t_1]$. Schedule baby $i$ at time $h^{-1}(\min(i/b,1))$ and giant $j$ at time $j/b$. Include both extra baby indices at $t_1$ and prefer babies on ties. Compare the next indices over the rationals.

For the ordinary hit use the nearest center on the sign of $X$, with residual magnitude $I$ and ordinal $J$. Put $x=\min(I/b,1)$, $u=J/b$, $v=\max(u,h^{-1}(x))$, and $H(x,u)=h(v)+v$. The two entries are present by $v$, so the primary count is at most $bH(x,u)+18$, including the extra baby entries. As a function of $x$, $H$ is constant up to $h(u)$ and then equals $x+h^{-1}(x)$, so it is increasing and 2-Lipschitz. For $u\ge t_1$ it equals $1+u$.

Conditional on the other box variables, the diamond gives a uniform interval of $g$ integers. In a full cell the residual is uniform on $-m,\ldots,m-1$ with $m=b$ or $b+1$. Its absolute value is dominated by $mU+1$ for $U$ uniform on $[0,1]$: for $0\le y<m$ its distribution is $(2\lfloor y\rfloor+1)/(2m)\ge\max(0,(y-1)/m)$. Coupling the cumulative probabilities gives $x\le\min(1,U+2/b)$. Thus the full-cell bound is $bf(u)+22$, where
\[
 f(u)=\int_0^1 H(x,u)dx=h(u)(h(u)+u)+\int_{h(u)}^1(x+h^{-1}(x))dx.
\]
On the linear pieces $f'(u)=h(u)(1+h'(u))$. Hence $f$ is continuous, increasing and $13/5$-Lipschitz, below $2$ before $t_1$ and equal to $1+u$ thereafter. There are at most four incomplete cells, at zero and the two interval ends. Their probability is at most $4(2b+2)/g$. Before fill the pointwise count is at most $3b$ and after fill the whole-cell bound holds pointwise. The excess is at most $24b(b+1)/g<3000$, since $a^2/g<121$, $b\le a+2$ and $g>10^{12}$.

The ordinary ordinal satisfies $J\le |X|/b+2$. Thus $bf(J/b)\le bf(|X|/a^2)+26/5$. Also $\mathbb E f(|X|/a^2)\le2+\mathbb E|X|/a^2<3$ from the RMS bound. Changing the exterior $b$ to $a$ costs at most six steps and replacing $X$ by the centered sum $S$ costs less than one since $|S-X|\le3/2$. This totals below 4096. 

Put $Y=S/\sigma_S$ as above and let $G$ be standard normal. The established characteristic-function bound through frequency $10^6$ and the trivial bound beyond it give
\[
 \frac{2}{\pi}\int_0^\infty
    \frac{|\phi_Y(t)-e^{-t^2/2}|}{t^2} dt
 <\frac1{300000}+2^{-40}+\frac2{10^6}<\frac1{150000}.
\]
For every $v\ge0$ the expectations of $(|Y|-v)_+$ and $(|G|-v)_+$ differ by less than $1/150000$: use
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
For exact bounds on these four normal values, use $\varphi(0)=1/\sqrt{2\pi}$. The same Machin identity used above gives $\pi<314160/100000$: use the first arctangent's upper sum through $x^9/9$ at $1/5$ and the second arctangent's lower sum $x-x^3/3$ at $1/239$. With the proved lower bound $314159/100000$, squaring gives
\[
 398941/10^6 < \varphi(0) < 398943/10^6 .
\]
Write $z_i=R_i^2/2$, and set $P_k(z)=\sum_{j=0}^k(-1)^jz^j/j!$ and
$J_k(z)=\sum_{j=0}^k(-1)^jz^j/(j!(2j+1))$. The odd and even sums give lower and upper exponential bounds, including after integration. Thus lower-bound each $\varphi(R_i)$ by $(398941/10^6)P_9(z_i)$, lower-bound $F(R_0)$ by $2R_0(398941/10^6)J_9(z_0)$, and upper-bound $F(R_1)$ by $2R_1(398943/10^6)J_{10}(z_1)$. At $R_0=123/250,R_1=7503/8000$, the respective outward rationals for $F(R_0),F(R_1),\varphi(R_0),\varphi(R_1)$ in units of $10^{-9}$ are
\[
 377279445,\quad651692524,\quad353463962,\quad256982702.
\]
At $z_i=R_i^2/2=A_i/B_i$ with $(A_i,B_i)=(15129,125000),(56295009,128000000)$, take $a_j=\lfloor10^{15}A_i^j/(B_i^j j!d_j)\rfloor$, with $d_j=2j+1$ for $F$ and one for $\varphi$. The signed sum $T=\sum(-1)^ja_j$ encloses $10^{15}$ times the relevant Taylor sum in $[T-5,T+6]$. The table gives $T$ and the outward integer after applying the prefactor and multiplying by $10^{12}$:
\[
\begin{array}{c|r|r}
 &T&\text{integer bound}\\
F(R_0)&961079635112363&377279445579\\
F(R_1)&870877227067145&651692523277\\
\varphi(R_0)&886005606959813&353463962846\\
\varphi(R_1)&644162176367059&256982702802\\
\end{array}
\]
The integer quotients $a_0,\ldots,a_k$, in the same row order:
\[
\begin{array}{c|l}
F(R_0)&1000000000000000,40344000000000,1464874502400,42213497803,993452457,\\
 &19675560,335834,5032,67,0\\
F(R_1)&1000000000000000,146601585937500,19342822499451,2025491753519,173215176965,\\
 &12465958738,773185482,42101509,2042254,89294,3553\\
\varphi(R_0)&1000000000000000,121032000000000,7324372512000,295494484624,8941072115,\\
 &216431168,4365849,75486,1142,15\\
\varphi(R_1)&1000000000000000,439804757812500,96714112497255,14178442274635,1558936592688,\\
 &137125546118,10051411266,631522642,34718332,1696587
\end{array}
\]
The quotient verification inequalities are
$a_j B_i^j j!d_j\le 10^{15}A_i^j<(a_j+1)B_i^j j!d_j$.
Adding even-index entries and subtracting odd-index entries yields the four displayed signed sums.
The last column respectively exceeds, is below, exceeds and exceeds $1000$ times the four earlier thresholds. Inserting them with the corresponding signs in the normal expression gives
\[
 \mathbb E f(|G|/A_*)
 \le\frac{228316975354028917}{151290000000000000}.
\]
Add $(21/5)/(150000A_*)$ for the comparison with $Y$ and multiply by $11090537/10^7>\sqrt{123/100}$, which follows by squaring. This gives the exact upper coefficient
\[
 \frac{2532196058701373803058429}{1512900000000000000000000}<83687/50000.
\]
With the finite errors the anchor takes at most $(83687/50000)\sqrt{\sigma^+}+4096$ expected candidates before the extra lookups.

For the anchor use the same extra lookups. For odd $d\ge1,j\ge1$ consider the two previous targets with $a=\sqrt{(123/100)σ^+}$ and $b=\lceil a\rceil+1$. Put $A'=141/80$, $C'=282/61$, $D'=C'+13/8=3049/488$. If $S_a=(A'b-C'd-D'j-9)_+>0$ then $j<b/3$ and $2(d+j)/b<61/80$. The ordinary baby index is at least $b-j$, reached on the second segment at time $(5/8)(b-j)/b+11/80$ and at least $(13/8)(b-j)+(11/80)b-3$ updates. The giant pair is present at ordinal $2(d+j)$ or earlier. Up to $t_1$, the convex $h(u)+u$ lies below its secant $(141/61)u$, so the pair costs at most $C'(d+j)+6$ updates. Both signs remain active at these ordinals because retained centers extend to $\lceil B/2\rceil$. Hence each of the two distinct targets saves at least $S_a$. They have magnitude below $(61/160)(b^2+b)<0.47σ^+$ by $b\le a+2$ and $a\ge2^{24}$.

Integrating on the same area-two rectangles lowers the constant term by at most $C'+D'$. The local mass bound gives expected saving at least
\[
 (7/(20σ^+))(A'b-9-C'-D')^3/(6C'D') .
\]
Since $9+C'+D'<22$, $b\ge a\ge2^{24}$ and $a^2=(123/100)σ^+$, the coefficient of $a$ is above $(999/1000)(21231456687/1561088000000)>27/2000$, by $2\cdot999\cdot21231456687>27\cdot1561088000000$. Also $a>(11/10)\sqrt{σ^+}$. The anchor costs at most $(165889/100000)\sqrt{σ^+}+4096$ expected primary candidates.

### Adaptive pointwise traversal

Run an auxiliary search alongside each ordinary search. At width $w=2^j$ tabulate $iP$, $0\le i<w$, and test the $2w+1$ residuals starting at $Q+w^2P$, stepping by $-wP$. The two strides use $2j$ doublings and one initial inverse. A table hit at iteration $h$ gives $x=hw+i-w^2$, covering $[-w^2,w^2+w-1]$. Accept only in $[-B,B]$, which is unique modulo $q$. Use exact twelve-coordinate keys and one single-product, sign or lookup action before the first primary step and after every $10^6$ primary candidates. Each auxiliary stage costs $O(w)$ operations. Widths through $w^2\ge|x|$ sum to less than twice the last width, so the interleaved work is $O(\sqrt{|x|}+1)$. The public center translations precede [full-search]. Its two in-line anchor multiples cost $O(\log(|t_0|+1)+1)$ by binary powering, which fits $O(\sqrt{\max_i|t_i|}+1)$. This is the desired bound on the signed largest emitted integer.

Charge six multiplications per primary candidate. Split auxiliary work into individual products, signs or lookups. One action per block costs at most $67/(6\cdot10^6)<12/10^6$ times primary work. The initial auxiliary steps and fixed updates are in the allowance below. The candidate bound is $(165889/100000)\sqrt{σ^+}+(47/18+1/5000000)\sqrt{g/2}+4352+1$, by the proved anchor and increment bounds and the later-triple probability.

**Auxiliary field ledger.** Before instance setup select a nonzero $u$ with $u^{p^6}=-u$ outside $\mathbb F_{p^4}$. The minus eigenspace has dimension one over $\mathbb F_{p^6}$ because the quadratic trace is onto, so it has $p^6>p^4$ elements. No nonzero element there belongs to $\mathbb F_{p^6}$. Thus $u$ has degree 12. In the native pairing coordinates tabulate the matrix with columns $d(1,u,\ldots,u^{11})$, $d=21!$, and its inverse. They convert the scaled power coordinates $\operatorname{coeff}(v)/d$ in either direction at cost 144. Store twelve 32-byte residues. Compute the minimal polynomial $F$ from $u^{12}$. The fixed linear $p^6$ map is inversion on order $q$: with $a=6(4965661367192848881)^2$, $p=q+a$ and $a^4-a^2+1=21888242871839275213430563804664787404649310511694458087810267520700626816493q$. Multiplying by $a^2+1$ gives $p^6≡-1\pmod q$. The map changes odd coefficient signs. Negate source points before signed Miller accumulation and then apply the shared final exponentiation.

Interpolate via C5 at 22 consecutive small integers and infinity. Multiply the 23 node pairs of the two scaled inputs. At finite index $j$ zero-based, use integer weights $d/Q'(a_j)=(-1)^{21-j}\binom{21}j$ by small-integer addition chains. At infinity multiply by $d$ by the factors $1,\ldots,21$. Reconstruction yields the scaled-coefficient product $B$: the common factor $d$ fixes $(1/d)^2$ to $1/d$. Reverse $B=FQ+R$ with $\deg R<12$. The reversed quotient is $(\operatorname{rev}_{22}B)(\operatorname{rev}_{12}F)^{-1}\bmod X^{11}$, where $\operatorname{rev}_j L=X^jL(1/X)$. The C5 interpolation with fixed reciprocal uses 21 products. Subtract $FQ\bmod X^{12}$ using 23 products with the fixed low coefficients of $F$. C5 applies for any length $t$ at $2t-2$ such nodes and infinity. Total: $23+21+23=67$ multiplications.
 
Count thirteen binary multiples of 508 products: three center translations, two terminal operations, six strides and two anchor multiples. Also charge six translation products, six secondary initializations, at most fourteen extra products per traversal and eighteen signs, which are free, all below $400\cdot67$. At most $48K_2+4(J+4)\le1024$ pairing accumulations need one product and one conversion each. The eight other conversions cover the search pairs and outcome. The protected signed step covers the initial primary inverse and each table lookup thereafter uses equality of coordinate vectors. Signs and lookups require no products.

## Amendment n

Use $n=kd_R+{\rm form\_pad}=4392$, $kd_R=258\cdot17=4386$ and form padding six. The coefficients of $T^0,T^1,T^2$ are $v_0,(H^{(1)})^\top v,(H^{(2)})^\top v$. Put the ordered matrix outputs $A\hat v$ in positions 3 through 4388, and zero in positions 4389 through 4391. The kernel is precisely $v_0=0$, both public form values zero, and $A\hat v=0$. On honest variants, the independent column zero supplies the uniform matrix slots and I5 makes the public form slots zero. The constant is one and the last three slots are zero. The field and correctness arguments apply to this affine subspace.

## Amendment msis_bound

Set ${\rm msis\_bound}={\rm beta\_sis}=B_E$. An infinity-short multiple of $v\ne0$ is an integer $x\equiv a v\bmod q$, $a\ne0$, with $0<\|x\|_\infty\leβ$. For the amended Euclidean problem, a short multiple instead means such a congruence with $0<\|x\|_2\le B_E$. Preserve the original infinity theorem as a separate assertion.

For every heavy stack the rank is at most three by I5. Each kernel vector's marginal guessing probability is at least the stack's, as a joint fiber is included in a fiber of the linear combination. A nonzero kernel vector has zeroth coordinate zero, so the inverse theorem of I6 yields an infinity-short multiple. For any kernel vector, every such short multiple packs to an infinity-SIS solution at $β$ by the kernel identity of n and injective coordinate packing of ell.

The costed Euclidean instance has the same rank bound. The proof below gives every heavy-stack kernel direction a Euclidean-short multiple and recovers one deterministically. Every Euclidean-short multiple of a form-kernel vector packs to a solution at $B_E$ by the kernel identity and the isometry in msis_norm.

### Joint fibers

Amendment I6 lifts box-coordinate rows into a regular saturated normal of rank at most four and mass at least $μ$. The sampler itself has heavy-stack rank at most three by I5.

### Mass times Euclidean covolume

For a rank-$d$ lattice $Λ$ with integer basis $B$, write $c(Λ)=\sqrt{\det(B^\top B)}$ for its covolume in its real span. We will prove that each rank-three output of regularization of maximum fiber mass $m\geμ$ satisfies $m c(Λ)\le(362/5)/g^3$. Every regular rank-two output of the regularization procedure of I3 satisfies $m c(Λ)\le C_2/g^2$, provided its input has the required density and its output density is at least $μ$. Use precisely that procedure at each joint-fiber extension.

Choose a largest minor of $B$ on $J$ and order these rows first. Set $h=|\det B_J|$ and $P=BB_J^{-1}$, so each entry of $P$ has absolute value at most one. For a prefix length $j\ge d$, write $G_j=P_{[j]}^\top P_{[j]}\succeq I_d$. The inequality follows because the rows on $J$ are unit axes. Let $Λ_j$ be the saturation of the prefix and $h_j$ its height. Its covolume is $h_j\sqrt{\det G_j}$. Indeed $B_{[j]}=YC$ with $Y$ a basis of $Λ_j$, and $|\det C|=h/h_j$ by the prefix proof of I3. Gram determinants then give the formula. The prefix image $B_{[j]}^\top\mathbb Z^j$ has index $h/h_j$ in $\mathbb Z^d$ by the same proof.

Fix the target of a densest fiber of $B^\top r$. Let $s_i$ be the successive index multipliers after the prefix $j$, so $\prod_i s_i=h/h_j$, including factors one. The prefix before step $i$ has image $G^{\rm int}_{i-1}=B_{[i-1]}^\top\mathbb Z^{i-1}$, and $s_i$ is the order of the next row in the quotient by this image. Call a suffix integer tuple feasible if its projection subtracted from the target leaves a point in the prefix image and in the prefix region described below. If $j=d$, use the exact pivot box of side $g-1$, with $G_j=I_d$ and no trimming. If $j>d$, discard at most $e$ absolute probability using the prefix trimming event of I3. The normalized prefix value lies within $R_{\rm tr} g/\sqrt{12}$ of its mean in the norm $\|G_j^{-1/2}\cdot\|_2$, by changing from the saturated prefix basis to the normalized row matrix $P_{[j]}$. Write $e'=0$ in the first case and $e'=e$ in the second. For each feasible suffix, the conditional probability of the remaining required prefix value is at most $m_j$. All suffix points in the original box have the same probability. Thus if there are $M$ feasible suffix tuples, $m-e'\le m_j M/g^{N_*-j}$.

For each feasible suffix tuple $y$, attach the axis-aligned rectangle centered at $y$ with widths $ℓ_i$ satisfying $1\leℓ_i\le s_i$. The interiors of these rectangles are disjoint. Indeed if two different feasible tuples have last differing index $k$, subtract their two congruences modulo the prefix image and then cancel all terms at indices below $k$ in the larger image $G^{\rm int}_{k-1}$. Their coordinate difference at $k$ is a nonzero multiple of $s_k$. The two intervals at that coordinate have disjoint interiors. Every rectangle has volume $\prod_iℓ_i$. It lies within the product of the enlarged suffix intervals of widths $w_i=g-1+ℓ_i$. The disjointness argument works with width equal to $s_i$; shared boundaries have zero Lebesgue measure.

Write $S_ℓ=\sum_{i:s_i>1}ℓ_i$. Rows of $P$ have entries bounded by one, and their length in the normalized prefix metric is at most $\sqrt d$, because $G_j\succeq I_d$. From a rectangle center to any point in it, the change of the matched prefix value is therefore at most $(S_ℓ+N_*)/2$ in each pivot coordinate if $j=d$, and at most $\sqrt d(S_ℓ+N_*)/2$ in the metric norm otherwise. Here each step of order one uses width one. All attached rectangles thus map under the suffix projection into a fixed translate of $G_j^{1/2}[-w/2,w/2]^d$, where
\[
 w=\begin{cases}
 g+S_ℓ+N_*,&j=d,\\
 2R_{\rm tr}g/\sqrt{12}+\sqrt d(S_ℓ+N_*),&j>d.
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
 \partial_t F-Δ F
   =F(\sum_i c_i v_i^2-\left\|\sum_i c_i v_i u_i\right\|_2^2)\ge0,
\]
because the matrix with columns $\sqrt{c_i}u_i$ has orthonormal rows. On compact positive time intervals the kernel and its derivatives have Gaussian decay times a polynomial: its first logarithmic derivative is $(-s+\mathbb E U)/(2t)$, the second is $-1/(2t)+{\rm Var}(U)/(4t^2)$, with the source $U$ supported where $f_i$ is supported. The tight-frame identity gives the Gaussian decay in $z$, so the integral of the Laplacian vanishes and the integral of $F$ is nondecreasing. Fatou as $t\downarrow0$ bounds the left side. As $t\to\infty$, rescale $z=\sqrt t z'$; the product and Jacobian give the standard Gaussian heat kernel on $\mathbb R^d$ times the right side. The limit is dominated by a constant times $\exp(-\|z'\|_2^2/8)$, using bounded source support and $(v-w)^2\ge v^2/2-w^2$. Continuous cutoffs increasing to one and monotone convergence give the asserted inequality for the unbounded supports.

We need the univariate bound $I(p)=π^{-1}\int_{\mathbb R}|{\rm sinc}(x)|^pdx\le\sqrt{2/p}$ for $p\ge2$. Let $U$ be the uniform density on $[-1/2,1/2]$. Fourier inversion at zero, with frequency $2x$, gives $I(2)=1$, $I(4)=2/3$, and $π^{-1}\int{\rm sinc}(x)^3dx=3/4$. Indeed, $U*U$ is the tent $(1-|t|)_+$; convolving it with $U$ at zero gives $3/4$, and convolving it with itself at zero gives $2/3$. All these Fourier integrals converge absolutely, and inversion follows by first adding Gaussian smoothing and taking its variance to zero, using continuity of the convolutions.

To bound the absolute cubic integral, write $S_-=(2/π)\int_{\{x>0:\sin x<0\}}|\sin x/x|^3dx$. Then $I(3)=3/4+2S_-$. For the first negative interval $[π,2π]$, split it into four equal parts. The integrals of $|\sin x|^3$ on them are $A,B,B,A$, where $A=2/3-5\sqrt2/12<78/1000$ and $B=5\sqrt2/12<590/1000$, from the antiderivative $-\cos x+\cos^3x/3$ on $[0,π]$. Use the left endpoint to bound $x^{-3}$ on each part. On later negative intervals the integrals of $|\sin x|^3$ are $4/3$, and their left endpoints are $(2j+1)π$ for $j\ge1$. The decreasing reciprocal cubes sum to at most $1/27+\int_1^\infty(2t+1)^{-3}dt=1/27+1/36$. It follows that
\[
 S_-\le\frac{2}{π^4}\left\{\frac{78}{1000}(1+(4/7)^3)
           +\frac{590}{1000}((4/5)^3+(2/3)^3)
           +\frac43(1/27+1/36)\right\}.
\]
Substituting $π>314159/100000$ gives $I(3)<777/1000<\exp(-1/4)$; the latter inequality follows from the alternating cubic lower bound. Hölder interpolation gives $I(p)\le\exp(-(p-2)/4)$ for $2\le p\le3$, and $\log(p/2)\le(p-2)/2$ proves $I(p)\le\sqrt{2/p}$ there. Between three and four the scaled endpoint values $I(p)\sqrt p$ are below $34/25$. The concavity gap of $\log p$ above its endpoint chord is at most $1/72$, by the second derivative bound $1/9$ on this unit interval. Hölder thus gives $I(p)\sqrt p\le(34/25)\exp(1/144)<7/5<\sqrt2$.

For $0<x<π$, the difference $(1-x^2/3)\sin x-x\cos x$ has derivative $(x/3)(\sin x-x\cos x)\ge0$, since the parentheses have derivative $x\sin x\ge0$. Integrating $\cot x-1/x\le -x/3$ yields ${\rm sinc}(x)\le\exp(-x^2/6)$. For $x\geπ$, write $\sin^2x=(1-\cos 2x)/2$ and integrate the cosine term by parts to get $\int_π^\infty\sin^2x/x^2 dx\le1/(2π)+1/(4π^2)$. Thus for $p\ge4$,
\[
 I(p)\sqrt p\le\sqrt{6/π}
       +\frac{2\sqrt p}{π}π^{2-p}(\frac1{2π}+\frac1{4π^2})<\sqrt2 .
\]
The tail factor decreases on this interval, and at four the upper bound is below $1407/1000$ by $π>314159/100000$. This completes the bound on all $p\ge2$.

Apply the tight-frame inequality with $f_i(s)=|{\rm sinc}(\sqrt{c_i}s)|^{1/c_i}$. Each integral is at most $π\sqrt2$ by the preceding estimate after rescaling. Fourier inversion with frequency $2z$ bounds the density by $π^{-d}(π\sqrt2)^{\sum_i c_i}=2^{d/2}$. Equivalently, this inversion bound first holds after convolution with a small centered Gaussian by its Fourier integral, and the uniform bound on the smoothed laws passes to the limiting law when integrated against continuous compactly supported tests. The same Gaussian limit justifies the interval convolution inversion at $p=2$, since its transform is integrable and the convolution is continuous. This proves the density inequality, including its determinant factor before normalization.

Take the independent uniform law on the enlarged suffix intervals of widths $w_i$. The union of attached rectangles has volume $M\prod_iℓ_i$, so its probability under this law is $M\prod_iℓ_i/\prod_iw_i$. It is bounded by the probability of the enlarged prefix cube for the projected suffix. As before that probability is the convolution density with the independent uniform on a centered cube of shape $G_j^{1/2}[-w/2,w/2]^d$, multiplied by $w^d\sqrt{\det G_j}$. For a pointwise bound at the translated center, enlarge the cube by an arbitrarily small positive width and move to a nearby center in the full-measure set satisfying the density bound. Then pass to the original width, as the original translated cube is contained in each of these enlarged cubes. The augmented Gram matrix dominates $g^2G_{\rm full}$ since $w_i\ge g$ and $w\ge g$. Thus the cube probability is at most
\[
 2^{d/2}(w/g)^d\sqrt{\det G_j/\det G_{\rm full}} .
\]
Multiplying by the conditional prefix bound and the final covolume gives
\[
 (m-e')c(Λ)
 \ \le\
 2^{d/2}(w/g)^d m_j c(Λ_j)
 \prod_i(w_i/g)\prod_i(s_i/ℓ_i).
\]
All the products are over suffix coordinates. Choosing full widths $ℓ_i=s_i$ incurs no final ratio and satisfies $\prod_i(w_i/g)\le\prod_{s_i>1}(1+s_i/g)$.

For a rank-three regularization output put $j=d=3$. If all suffix orders are below $g$, use $h<5.1g$ from the height proof. At most one order exceeds $\sqrt{5.1g}$. The other nonunit orders have sum at most $52+2\sqrt{5.1g}$: their count is below 52 by the product bound, and $(s-1)/\log s$ is increasing, so sum using its value at $\sqrt{5.1g}$. Cap the large width at $g/3$ and keep all others. The inverse width ratio is at most three, the interval product at most $(4/3)(5000000/4999999)$, and the pivot side ratio at most $4/3+3/10^7$. Since $m_3c(Λ_3)=g^{-3}$, the cube estimate gives $mc(Λ)g^3<27$.

Otherwise use the large coordinate $y$ from the height proof with order $s\ge g$, $h=cs$, $c=1,2$. For $c=2$ condition on a fixed legal parity pattern of the other suffix coordinates. Given the other suffix inputs, at most one $y$ and pivot triple are permitted. Their normalized values require the suffix projection to lie in a translate of the sum of the pivot cube and a segment parallel to $p=P_y^\top$. Smooth each other coordinate by an interval of width one if $c=1$, and two if $c=2$. The resulting independent continuous intervals have width $g$ in either case. This puts the projection in the larger zonotope with cube and segment both of width $w=g+2N_*$.

In the pure order-four phase case, $h=s<4g$. Condition on the residue modulo four of each suffix input except $y$. With uniform residues, at most half the patterns are legal, since the phase is uniform and at most two $y$ values occur. On each legal pattern $y$ is fixed and the remaining projection lies in a pivot cube. Smooth the other inputs by width four, giving independent continuous use of their length-$g$ intervals. Enlarge the cube to side $w=g+4N_*$. Its convolution density bound uses Gram $D_0=w^2 I+g^2\sum_{i\ne y,\ i\notin J}P_i^\top P_i$. Since $D_0/g^2\succeq I$, adding $p p^\top$ with $p=P_y^\top$ changes its determinant by a factor at most $1+\|p\|^2\le4$. The square-root factor is at most two. Therefore $mc(Λ)g^3\le(h/g)(1/2)2^{3/2}\cdot2(1+4N_*/g)^3<12$.

Return to all other large-order outputs. Set $G_0=I+pp^\top$ and $M=(g/w)^2G_0^{-1/2}(\sum_{i\ne y,\ i\notin J}P_i^\top P_i)G_0^{-1/2}$. Normalize the zonotope by $G_0^{-1/2}/w$. It is the image of the centered unit four-cube under $G_0^{-1/2}[I,p]$ with orthonormal rows, so it lies in the unit ball. Its volume is $(1+\sum_i|p_i|)/\sqrt{1+\|p\|_2^2}\le2$ by Cauchy–Schwarz. Before normalization the added volume is the segment length times the area of the cube projection perpendicular to $p$. Indeed along each line the interval extends by that length. The entrance faces cover the projection without overlap except on their boundaries, giving area $\sum |p_i|/\|p\|_2$ if $p\ne0$. The one-dimensional projected length is at most two. For any planar projection the $2$ by $4$ generator matrix $V$ has orthonormal rows, and area equals the sum of absolute two-column determinants by sequential extrusion and additivity of perpendicular widths. The six minors have squared sum one by Cauchy–Binet. Pair the absolute minors from complementary columns as $(a_i,b_i)$, $i=1,2,3$. The signed products satisfy the Plücker relation, obtained by squaring the wedge of the two rows (zero by the repeated rows). Relabel so $a_1b_1+a_2b_2=a_3b_3$, allowing zero products. Put $x_i=(a_i+b_i)/\sqrt2$, $y_i=(a_i-b_i)/\sqrt2$. The relation and squared sum one give $x_1^2+x_2^2+y_3^2=x_3^2+y_1^2+y_2^2=1/2$. Thus the area $\sqrt2\sum x_i\le1+\sqrt2$ by Cauchy–Schwarz, and $4(1+\sqrt2)^2<11657/500$.

For planar area $V_2$, retain the universal bound $1+\sqrt2$ just proved. Also let $u=1+\|p\|_2^2$, and reflect original cube coordinates so the null direction is the nonnegative unit vector $n=(|p_1|,|p_2|,|p_3|,1)/\sqrt u$. Complete orthonormal rows of the projected plane by $n$ and a unit $z$. Complementary minors of the orthogonal matrix (by the inverse-transpose identity) give $V_2=\sum_{i<j}|n_i z_j-n_j z_i|$. At $n_0=(1,1,1,1)/2$, sort $z$: this half-sum of distances is the dot product with $(-3,-1,1,3)/2$, at most $\sqrt5$. The area changes by at most $\sqrt6\|n-n_0\|_2$, by Cauchy–Binet on the squared minors of $(n-n_0,z)$ and Cauchy–Schwarz. If $u>3.9$, set $δ=4-u$. Then $\|(|p|,1)-(1,1,1,1)\|_2\le\sum_i(1-|p_i|)\leδ$. Expanding the squared distance before normalization gives $\|n-n_0\|_2\le δ/(\sqrt2 u^{1/4})$, so $V_2\le\sqrt5+1.25δ$ and $4V_2^2\le20+23δ$.

Let $c_2=11657/500$ if $u\le3.9$, and $c_2=\min(11657/500,20+23δ)$ otherwise. For event probability $P_*$ and decreasing eigenvalues $λ_i$ of $M$, the density estimate in the leading $r$ eigendirections gives $P_*^2\prod_{i\le r}λ_i\le8,c_2,32$ for $r=1,2,3$. A zero product is automatic. The log-majorant list $(8/P_*^2,c_2/8,32/c_2)$ is decreasing for $20\le c_2\le11657/500$. For $P_*>0$ the list bounds log prefix sums, interpreting a zero eigenvalue as log $-\infty$. The sum of positive parts of the logs above any threshold $t$ equals the maximum prefix sum minus its length times $t$. Order these hinges and integrate against the nonnegative second derivative of $\log(1+e^t)$. This gives
\[
  P_*^2\det(I+M)\le9 F(c_2),\qquad F(t)=5+t/8+32/t.
\]
Improve this projected bound for use in the rank-three mass-covolume estimate. Set $t=P_*^2>0$ and $A=8-4t$. The projections of the normalized four-cube of dimensions one and two lie in the side-two box. Convolve each projected interval sum with the uniform law on that box. The density at the center of the translated box is at least $P_*/2^r$, while its Gram has increased by $4I_r$. The cube density bound gives $t(λ_1+4)\le8$ and $t(λ_1+4)(λ_2+4)\le64$. The second product is at least $(\sqrt{λ_1λ_2}+4)^2$. With $B=\min(c_2,(8-4\sqrt t)^2)$, the new upper prefix products are $A/t,B/t,32/t$. Their ratios form a decreasing majorant, since $A\ge\sqrt t(8-4\sqrt t)$ and $B^2\ge256\ge 32A$. The same log-prefix bound therefore gives
\[
 t\det(I+M)\le (8-3t)F_A(B),\qquad F_A(B)=(1+B/A)(1+32/B).
\]
The function $F_A$ increases for $B\ge16$ since $F'_A=1/A-32/B^2\ge0$.

If $u\le3.9$, use just $B\le\min(24,(8-4\sqrt t)^2)$. For $t\le2/3$, replace $B$ by 24: multiplying $77-(8-3t)F_A(24)$ by $3A$ gives $28(1+t)(2-3t)\ge0$. For $t\ge2/3$, replace $B$ by $(8-4x)^2$, $x=\sqrt t\in[4/5,1]$. The difference from 77 times $AB/64$ has ascending polynomial coefficients $(-248,728,-630,28,199,-84,9)$. With $x=(4+z)/5$, its coefficients in the Bernstein basis $\binom6i z^i(1-z)^{6-i}$ are
\[
 (29384/15625,5212/1875,30154/9375,2049/625,381/125,13/5,2).
\]
All are positive, proving a bound of $77$, and $u t\det(I+M)\le 3.9\cdot77<601/2$.

For $3.9<u\le4$, put $δ=4-u$ and replace $B$ by $\min(20+23δ,(8-4\sqrt t)^2)$, using the planar area estimate. At fixed $t$, the product $(4-δ) F_A(B)$ is nonincreasing on $0\leδ\le1/10$. On the branch with $B$ constant this is immediate. On the other branch $20\le B\le22.3$ and $(8-4\sqrt t)^2\ge20$, which implies $A\ge24/5$. The logarithmic derivative
\[
 F'_A(B)/F_A(B)=1/(A+B)+1/(B+32)-1/B
\]
decreases in $A$ and increases in $B$ on this range. The latter assertion follows from $1/B^2-1/(A+B)^2\ge (22.3)^{-2}-(27.1)^{-2}>52^{-2}\ge1/(B+32)^2$. At $A=24/5,B=22.3$, its value times 92 is below one by rational substitution. Thus the positive part of the derivative from $B=20+23δ$ is less than the loss from the prefactor. The maximum is at $δ=0$, with $B=\min(20,(8-4\sqrt t)^2)$.

If this minimum is 20 then $0<t<779/1000$. The function $(8-3t)(1+20/A)$ is convex because its derivative is $-3+160/A^2$ and $A$ decreases. After the constant factor $1+32/20$, the bounds at $0,779/1000$ are respectively $364/5$ and $457983799/6105000$, both below $601/8$. If the minimum is $(8-4x)^2$ instead then $x=\sqrt t\ge22/25$. The difference from $601/8$ times $AB/64$ has ascending coefficients $(-263,743,-2505/4,41/2,1607/8,-84,9)$. With $x=(22+3z)/25$ its Bernstein coefficients are
\[
 (38119436/244140625,797683/1953125,4184677/7812500,346919/625000,12077/25000,67/200,1/8).
\]
Hence $u t\det(I+M)\le4(601/8)=601/2$ on this branch as well.

The determinant formula yields $P_*\sqrt{\det(P^\top P)}\le(w/g)^3\sqrt{u t\det(I+M)}<(1+2/10^7)^3\sqrt{601/2}<17.336$. The mass factor is at most one for $c=1$ and one half for $c=2$ by the legal parity patterns. With $h/c=s<4g$ this gives $mc(Λ)g^3<362/5$. If the lattice annihilates all public rows, $s<7g/2$ outside the pure phase case, so $mc(Λ)g^3<(7/2)17.336<607/10$. The all-small and pure phase bounds stay below both constants.

We will also use a stronger estimate for a rank-three regularization output used as a precursor of high density $m_{\rm old}$ such that $g^4m_{\rm old}\ge .20g^{4/5}$. Its height bound from the product expansion of mu_tr gives $h/g\leξ_{\rm tr}/(g^4m_{\rm old}-ξ_{\rm tr})<10^{-6}$, since $g\ge2^{49}$ and $ξ_{\rm tr}<2$. Use all suffix widths in the cube estimate. The sum of nontrivial orders is at most $h$ (the sum of two integers at least two is at most their product, and iterating proves the claim). Hence $m_{\rm old}c_{\rm old}g^3\le(99/35)(1+10^{-6}+10^{-7})^3/(1-10^{-6})<3$.

### Rank-four predecessors of rank one or two

Suppose the last strict prefix in the I3 construction is followed by a rank-$d$ normal, $d=1,2$, and the selected preceding regular lattice has rank four. It is sparse with height at most two and covolume at most 100. The preceding untrimmed maximum is at most $g^{-4}+3e$. At most one suffix order after the transition can exceed one, and that order is two: any factor of order at least three costs at most $1/3+1/g$, and two factors two cost $1/4$, both taking the mass below $μ$. For the transition itself use its actual image count below, irrespective of its order.

Let $C$ be basis columns of the old sparse lattice and the new unit column, in disjoint blocks, and $G=C^\top C$. It is saturated. The new prefix normal lies in its span, so it has a saturated basis $CV$ with $V$ integer of rank $d$. The five whitened features $G^{-1/2}C^\top r$ are an orthogonal projection of the at most 41 active physical coordinates. Their affine span for this fiber has dimension $a=5-d$. As before the difference lattice has covolume $δ=c(Λ_j)/c_{\rm old}$: extend the integral kernel of $V^\top$ by columns mapping to the $d$ axes and compare full volume $1/\sqrt{\det G}$ with normal projection volume $1/\sqrt{\det(V^\top G V)}$. Each feature point has mass at most $g^{-5}$ by the old four pivots and the independent new coordinate. Thus the number $L_0\ge(m_j-e)g^5>.416g$.

Project the entire physical box onto the direction of the affine span. This contains the projected fiber hull and has volume $g^a$ times the sum of absolute $a$-minors of an orthonormal-row matrix on 41 coordinates. Indeed, adding a segment to a zonotope adds its length times the projected volume perpendicular to that segment, by integration over lines. Applying this increment successively and inducting on the projection dimension gives the sum of the absolute determinants. Cauchy--Binet bounds the sum by $\sqrt{\binom{41}{a}}$. For $a=3$ improve it as follows. For each fixed column $i$, write $d_{ijk}$ for its three-column minors with two other columns. Their array as $j,k$ vary is a decomposable two-vector: rotate the three rows so column $i$ is supported in the first row and expand at that column. For any four other columns, the sum of the absolute six minors is at most $1+\sqrt2$ times their Euclidean norm by the paired-minor argument above, which is homogeneous. Sum over the four-sets, using Cauchy--Schwarz on these norms and observing that each pair appears in $\binom{38}2$ sets. This gives
\[
 \sum_{j<k,\ j,k\ne i}|d_{ijk}|\le (1+\sqrt2)\sqrt{\binom{40}2/6}\left(\sum_{j<k,\ j,k\ne i}|d_{ijk}|^2\right)^{1/2}.
\]
Sum over $i$ and use Cauchy--Schwarz again. Each triple is counted three times and the sum of squared three-minors over triples is one. Thus the volume for $a=3$ is at most $g^3(1+\sqrt2)\sqrt{\binom{41}3/6}$.

The simplex count gives $(m_j-e)c(Λ_j)\le g^{-5}(L_0/(L_0-a))a!c_{\rm old}$ times the corresponding volume. Here $L_0/(L_0-a)<1+10^{-8}$ and $c_{\rm old}\le100$. Full suffix widths have ratio product at most $1+1/g$. The projection of the entire prefix feature range, using orthogonal whitening on at most 41 coordinates, has radius at most $\sqrt{41}g/2$, so in the cube estimate $w/g\le\sqrt{41}+\sqrt d(N_*+2)/g$. The trimming ratios are at most $10000/9999$ by $10000e\leμ$. Multiplying the bounds gives $m c(Λ)<5020000/g^2$ for $d=2$ and $m c(Λ)<7100000/g$ for $d=1$. For example the former product without the smoothing increment and interval ratios is
\[
 (10000/9999)^2\,2\cdot41\cdot 600(1+\sqrt2)\sqrt{\binom{41}3/6}<5010000,
\]
and the two omitted factors multiply to less than $1+10^{-6}$. For the latter product the same computation uses $\sqrt2\sqrt{41}\cdot2400\sqrt{\binom{41}4}$ in place of $2\cdot41\cdot600(1+\sqrt2)\sqrt{\binom{41}3/6}$. Both estimates fit $C_d$.

For rank two use the chosen prefix sequence of the regularization proof of I3. If regularization promoted to rank three or four, use the corresponding terminal bound. Choose $j=d$ if no preceding prefix has a strictly larger normal, and the first prefix after the last strictly larger normal otherwise. Take full widths $ℓ_i=s_i$ on this rank-two extension and write $A_{\rm box}=\prod_i (g-1+s_i)/g$. The suffix steps have order below $g$. As in I3, an order at least $g$ would put a new unit-vector normal vanishing on $J$ into the next selected fiber's normal, contradicting the choice of the last strict prefix. The product of the suffix orders is at most $h\le H_2<g^{39/16}$ by regularity and the guarded sixteenth power. Call an order large if $s_i\ge g^{13/16}$. There are at most two large orders since three would have product at least $g^{39/16}$. Let $a\in\{0,1,2\}$ be the number of large orders. The product of the other nontrivial orders is below $g^{(13/16)(3-a)}$, since each large order is at least $g^{13/16}$. For a real $u>1$, the ratio $(u-1)/\log u$ is increasing, because its derivative has numerator $\log u-1+1/u\ge0$. For each small nontrivial order $s_i$, apply this bound with upper endpoint $g^{13/16}$ to get
\[
 \frac{s_i}{g}
 \le \frac1g+\frac{g^{13/16}-1}{g}\frac{\log s_i}{(13/16)\log g}.
\]
The number of nontrivial orders is below $(39/16)\log_2 g<610$ by (I1). Summing over the small orders thus gives
\[
 \sum_{{\rm small}}\frac{s_i}{g}
 <\frac{610}{g}+(3-a)g^{-3/16}
 <\frac{3-a}{570},
\]
using $g\ge2^{49}$, $580^{16}<2^{147}$, and $610/2^{49}+1/580<1/570$. For zero or one large order, use $S/g<a+(3-a)/570$. The small padding factors have product at most $\exp((3-a)/570)$ and the large factors are at most two each. Using $\exp(x)\le1/(1-x)$ for $0\le x<1$, the total padding factors are below $101/100$ and $201/100$, respectively.

If two large suffix orders occur, they have product at least $g^{26/16}$. Since the regular final lattice has height $h\le H_2<g^{39/16}$, their occurrence forces $h_j<g^{13/16}$. The prefix lattice can then be bounded directly without the preceding rank-three planar count. Apply the rectangle bound to $Λ_j$ itself with its pivot prefix of length two. Its pivot height is one and pivot probability $g^{-2}$. The suffix orders of this nested application have product $h_j$, so their nontrivial sum is at most $h_j$, using that a sum of two or more integers at least two is at most their product. In particular the sum divided by $g$ is below $g^{-3/16}<1/570$. Using their full widths, the product of the enlarged suffix interval ratios is at most $570/569$, and the pivot box ratio is at most $1+1/570+1/1024$. Thus
\[
 m_j c(Λ_j)\le (2/g^2)(570/569)(1+1/570+1/1024)^2<3/g^2.
\]
This uses the actual saturated prefix lattice, so it does not require any additional regularity of that prefix. Its normalized pivots are obtained from a largest minor as before.

In the final suffix with two large orders, $S/g<2+1/570$, and the product $A_{\rm box}$ is below $4(570/569)<402/100$. Its full-width pivot side ratio is below $4$, and the trimmed side ratio is below $14$, using $18/\sqrt3<52/5$, $\sqrt2<99/70$ and $N_*/g\le1/1024$. Hence the general rectangle bound and $m/(m-e')\le1000/999$ give
\[
 m c(Λ)<(1000/999)\cdot2\cdot(402/100)\cdot14^2\cdot3/g^2<5000/g^2<C_2/g^2 .
\]
This proves the two-large case, regardless of the position of the selected prefix.

For zero and one large orders, the trimmed side ratios are below $21/2,12$, respectively: substitute $S/g<a+(3-a)/570$ into $18/\sqrt3+\sqrt2(S/g+N_*/g)$ with the preceding rational bounds. The pivot side ratio is below four. A pivot prefix therefore gives $m c(Λ)<2(201/100)4^2/g^2<C_2/g^2$. It remains to treat $j>d$ in the zero- and one-large cases.

For $j>d$ with preceding rank four use the earlier small-support estimate. Otherwise the preceding rank-three regular containing lattice used to trim $F_j$ in I3 has basis $B_{\rm old}$, covolume $c_{\rm old}$ and mass $m_{\rm old}$. It obeys $m_{\rm old}c_{\rm old}\le(362/5)/g^3$. Let $C={\rm diag}(B_{\rm old},1)$ on the previous prefix plus its new coordinate, and $G=C^\top C$. This is an integer basis of a saturated rank-four lattice, as both summands are saturated. All normals to $F_j$ restrict on the previous coordinates to the span of $B_{\rm old}$ by I3. Thus $C$ carries the real annihilator of differences in the image $C^\top F_j$ isomorphically to the real normal space, and its saturation implies that the image coefficient normals have a saturated basis $V$ in $\mathbb Z^4$ with $CV$ a basis of the integer normal lattice $Λ_j$. Its rank here is two. Hence the affine image space has dimension two.

Whitening the image coordinates by $G^{-1/2}$ maps the difference lattice $\ker V^\top\cap\mathbb Z^4$ to the orthogonal complement of $G^{1/2}V$ with planar covolume
\[
 δ=\sqrt{\det(V^\top G V)}/\sqrt{\det G}=c(Λ_j)/c_{\rm old}.
\]
To see the identity, extend a basis of the kernel lattice with two integer columns $L$ such that $V^\top L=I_2$. They exist by saturation of $V$, which gives $V^\top\mathbb Z^4=\mathbb Z^2$. The full extended basis is unimodular by decomposing an integer vector via $V^\top$. After whitening it has full volume $1/\sqrt{\det G}$. Its last two columns project onto the normal plane as $G^{1/2}V(V^\top G V)^{-1}$, whose area is $1/\sqrt{\det(V^\top G V)}$. Multiplying by the planar covolume gives the full volume and proves the identity.

The whitened trimmed region lies in the ball of radius $g\sqrt{324/12+1/4}$ because the old coordinates are trimmed and the final interval has length $g-1$. Therefore its planar slice has area at most $A=π g^2(324/12+1/4)$. The image point count $M$ satisfies $M\le 2A/δ+2$ by the simplex count in I3. Each image point has mass at most $m_{\rm old}/g$ by independence. Moreover $\Pr[F_j]\ge m_j-e\ge999μ/1000$ by the prefix density premise and the Euclidean guard. The image has affine dimension two, so $M\ge3$. With no large suffix order this suffices for $M/(M-2)\le3$. If there is a large order $s_i$, the prefix probability bound at that step gives $m_{i+1}\le m_i\lceil g/s_i\rceil/g\le 2m_i/s_i$. The prefix masses are nonincreasing, so the earlier $m_j\ge m_i\ge (s_i/2)m_{i+1}\ge(g^{4/5}/2)m$. Each image point has mass at most $m_{\rm old}/g\le g^{-4}$, and the trimmed fiber has mass at least $m_j-e\ge(999/1000)m_j$. Hence
\[
 M\ge (999/2000)g^{4/5} m g^4 \ge (999/2000)ρ_0 g^{4/5} > 2^{36},
\]
using $m\geμ\geρ_0 g^{-4}$ and $g^{4/5}>(147/128)2^{39}$. Thus $M/(M-2)<1001/1000$. Also $m_{\rm old}\ge m_j-3e\ge(.4999999)g^{4/5}m\ge .20g^{4/5}g^{-4}$, since $3e\le3m/1000$ and $g^{4/5}>2^{39}$. The stronger rank-three estimate uses coefficient three there.

The planar count gives $(M-2)δ\le 2A$, so in both remaining cases
\[
 (m_j-e)c(Λ_j)\le M(m_{\rm old}/g)δ c_{\rm old}
 \le 2π(324/12+1/4) (M/(M-2)) g m_{\rm old}c_{\rm old}.
\]
For no large suffix order, one can sharpen the area comparison without assuming that the image contains many points. Set $R_0=g\sqrt{324/12+1/4}$. The section of the trimming ball is a disk of radius at most $R_0$. For $3\le M\le6$ its image polygon has area at most $MR_0^2/2$: orient its vertices around the boundary and use the signed determinant area formula, measuring the vertex vectors from the disk center, so each determinant is at most $R_0^2$. The projected lattice count gives area at least $(M-2)δ/2$. Consequently $Mδ\le M^2 R_0^2/(M-2)\le9R_0^2$. For $M\ge7$ use the disk area bound to get $Mδ\le (14π/5)R_0^2<9R_0^2$. Thus in the no-large case the multiplier in the preceding estimate of $(m_j-e)c(Λ_j)$ can be bounded by $9(324/12+1/4)<246$ in place of $2π(324/12+1/4)M/(M-2)$. For one large order the bound $M/(M-2)<1001/1000$ still gives a multiplier below $172$.

Apply the rectangle estimate to the final suffix. Its factors have already been bounded by $A_{\rm box}<101/100$ and $w/g<21/2$ with no large order, or by $A_{\rm box}<201/100$ and $w/g<12$ with one large order. In both cases $m/(m-e)$ and $m_j/(m_j-e)$ are at most $1000/999$. The general rank-three precursor bound uses $(362/5)/g^3$. The resulting coefficients on its constant are less than
\[
 (1000/999)^2\cdot 2(101/100)(21/2)^2\cdot 246
 \quad\hbox{or}\quad
 (1000/999)^2\cdot 2(201/100)12^2\cdot172 .
\]
The first is below $55000$ and the second below $100000$. The second uses precursor coefficient three, with $300000<5020000$. This proves $mc(Λ)\le C_2/g^2$.

If regularization starts in rank one and returns a rank-two lattice from a recursive call, apply this calculation to the rank-two call and its selected sequence. This proves the needed rank-two mass-covolume estimate.

### Rank-one Euclidean covolume

Let $C_1=67000 C_2+1448000000+200$. For a rank-one regular output of I3 of mass $m\geμ$, choose the pivot prefix $j=1$ or the first prefix after the last strict normal, as for rank two. The suffix orders satisfy $s_i<g$ by the unit-vector argument, and their product is at most $h\le H_1<g^4$. Use widths $s_i$. Call $s_i\ge g^{4/5}$ large and write $L$ for their number, so $L\le4$. The earlier logarithmic bound gives small-order sum divided by $g$ below $1016/g+(5-L)g^{-1/5}<1/150$, since $g<q<2^{254}$ and $g\ge2^{49}$. Hence the padding is below $16e^{1/150}<17$, or $2e^{1/150}<203/100$ for $L\le1$. With $R_{\rm tr}\le20$ and $N_*/g\le1/1024$, the ratio $w/g$ is below six for a pivot prefix, below sixteen for a trimmed prefix and below thirteen for a trimmed prefix with $L\le1$.

For $j=1$, $m_j c(Λ_j)=1/g$, so the rectangle estimate gives $m c(Λ)<200/g$. For preceding rank four use the small-support estimate. Otherwise the preceding strict normal is contained in the regular trimming lattice of rank $r=2$ or $3$, with mass $m_{\rm old}$ and covolume $c_{\rm old}$. Use the earlier diagonal basis $C$ and whitening. The current image normal has one primitive integer column $V$. A basis of $\ker V^\top$ extended by an integer column $L_0$ with $V^\top L_0=1$ is unimodular. The last whitened column has normal projection of length $1/\sqrt{V^\top C^\top C V}$, so the difference lattice has covolume $δ=c(Λ_j)/c_{\rm old}$. The section lies in a ball of radius $g\sqrt{R_{\rm tr}^2/12+1/4}<6g$. Its $M\ge r+1$ image points have mass at most $m_{\rm old}/g$ each, and I3 gives $(M-r)δ\le r!$ times the section volume.

For $r=3$ the ball gives $Mδ<22000g^3$ using $M/(M-3)\le4$, so $(m_j-e)c(Λ_j)\le22000\cdot(362/5)/g$. For $r=2$, the disk and $M/(M-2)\le3$ give $Mδ<680g^2$. If $L\ge2$, the suffix inequalities give $m_j\ge(g^{4/5}/2)^2m$. The previous rank-two mass is at most $g^{-2}$ by its pivots. Thus $M\ge(999/1000)m_j g^3>2^{26}$ since $m\geρ_0 g^{-4}$. Now $M/(M-2)<1001/1000$ and squared radius at most $(324/12+1/4)g^2$ imply $Mδ<172g^2$. The two rank-two bounds give $(m_j-e)c(Λ_j)\le680 C_2/g$ or $172 C_2/g$.

In the rectangle estimate each trimming ratio is at most $1000/999$ and the density factor below $99/70$. The coefficients on $C_2/g$ are at most $(1000/999)^2(99/70)(203/100)13\cdot680$ and $(1000/999)^2(99/70)17\cdot16\cdot172$, both below 67000. The coefficient on $(362/5)/g$ is at most $(1000/999)^2(99/70)17\cdot16\cdot22000<20000000$. Hence $m c(Λ)\le C_1/g$ throughout, without imposing any passing test.

### Euclidean multiples in every heavy stack

Let $\mathcal V$ be the row space of a heavy stack with nonzero kernel vector $v$, with $v_0=0$. The stack fiber is that of any row-space basis. If some $w\in\mathcal V$ has $w_0\ne0$, then conditional on the independent box coordinates $w^\top r$ is uniform on $g$ distinct values through $r_\diamond$ since $g<q$ and $v^\top r$ is fixed. The guessing probability of $v^\top r$ is above $gθ$, so applying joint fibers to it on the box gives a normal lattice of density above $gμ$ since $gθ-3e>gμ$. If all of $\mathcal V$ has zeroth coordinate zero, apply joint fibers to its basis on the box. This gives a normal lattice of density above $μ$ containing $\mathcal V$ modulo $q$. Either lattice has rank at most four and contains the line modulo $q$. By I5 the row space of a heavy stack annihilates all six public directions, so $v$ does too.

At terminal rank three, if the normal annihilates all public rows over the integers then $c(Λ)\le C_3/(g^3μ)$ as just proved. Otherwise restrict a nonzero public row $H$ to the lattice. Column Hermite form at a largest pivot minor bounds the basis entries by $3h$, so the nonzero gcd $a$ of $B^\top H$ is at most $3hN_*2^{43}<q$. The primitive restriction after dividing by $a$ has an integer kernel reducing onto its modular kernel via unimodular completion. It therefore contains the needed line, and is saturated. Its covolume is $c(Λ)\|\mathrm{proj}_{\mathrm{span}Λ}H\|_2/a$ by projecting a lattice vector mapped to $a$ and comparing volumes. In particular it is at most $(362/5)\sqrt{N_*}2^{43}/(g^3μ)<C_2/(g^2μ)$ because $g\ge2^{49}$ and $\sqrt{N_*}<2^{10}$.

If the terminal normal has rank four, its support has at most 40 coordinates, covolume at most 100 and height at most two. By the reduced-row weight exclusion in I5, if all its vectors annihilated all six public rows, its four independent normalized equations would be supported only on the three tags. Choose a public row $H$ with nonzero restriction. Use an integer basis $B$ with the maximal pivot rows in column Hermite form. This bounds pivot entries by $h$ (positive diagonal pivots have product $h$ and reduced off-diagonal entries are smaller than a pivot). All basis entries are at most $4h$ in magnitude by the maximum-minor coefficient bound. Thus the nonzero gcd $a$ of $B^\top H$ has $a<q$. The primitive restriction $(B^\top H)/a$ has an integral kernel basis extending to a unimodular basis by a column mapped to one. This proves that the integer kernel reduces onto the modular kernel, so its ambient lattice contains the needed modular line and is saturated. The volume of the original lattice is the kernel covolume times the perpendicular component of a vector mapped to $a$ under $H$. This component has length $a/\|\mathrm{proj}_{\mathrm{span}Λ}H\|_2$. Thus kernel covolume is at most $100\sqrt{40}2^{43}<2^{53}$ since $400000<2^{20}$. By P5 and $g<2^{50}$, $g^3μ<2^{-49}$, so $C_3/(g^3μ)>(607/10)2^{49}>2^{53}$.

In rank one its primitive generator has norm $c(Λ)\le C_1/(gμ)\le B_E$, and saturation gives a nonzero residue on the line. In ranks two and three the covolume bounds are $C_2/(g^2μ)$ and $C_3/(g^3μ)$. The coefficient preimage of the line of $v$ has index $q^{d-1}$ in rank $d$, since a saturated basis has full rank modulo $q$. Its covolume is multiplied by that index. The shortest-vector inequalities below and the squared or cubic I6 guard give a nonzero vector of norm at most $B_E$. Its residue is nonzero since $2B_E<q$. Appending the zero homogeneous coordinate preserves norm. This proves a short multiple for every kernel vector of every heavy stack. Recovery selects a kernel vector by the form equations on the recovered basis, without constructing the normal lattice.

For the Euclidean lift we use a sharper length bound in ranks two and three. If $L$ has rank two, take a shortest nonzero $u$ of length $λ_1(L)$. It is primitive, so integer coordinate operations extend it to a basis $u,v$. Subtract a nearest integral multiple of $u$ from $v$. Then $|u^\top v|\le\|u\|^2/2$ and $\|v\|\ge\|u\|$, so $c(L)\ge(\sqrt3/2)λ_1(L)^2$.

For rank three, scale so that a shortest nonzero vector $u$ has length one. Project along this primitive vector; the image is a rank-two lattice, since a basis beginning with $u$ projects its other two elements to an independent basis. Take a shortest nonzero projected vector $\bar b$, and complete it with $\bar c$ to a projected basis. Change $\bar c$ by a nearest multiple and a sign to write $\bar c=β\bar b+c_\perp$ with $c_\perp\perp\bar b$, $0\leβ\le1/2$. Let $B=\|\bar b\|^2$ and $C=\|c_\perp\|^2$. Lift to $b,c\in L$ with $u$-coordinates reduced into $[-1/2,1/2]$. Then $c(L)^2=BC$, $B\ge3/4$ by $\|b\|\ge1$, and $C\ge(1-β^2)B\ge3B/4$ by the minimality of $\bar b$.

Suppose $BC<1/2$. Then $B<\sqrt{2/3}$ and $a=\sqrt{1-B}$ lies in $(1/3,1/2]$. Also $C<1/(2B)<B$, so $β\geβ_0=\sqrt{1-C/B}$. For $t\in[β_0,1/2]$ define $p(t)=\sqrt{1-C-Bt^2}$. Its argument is positive: $B(1+a)=(1-a)(1+a)^2=1+a(1-a-a^2)\ge1$, so $C<(1+a)/2$ and $1-C-B/4>(1-a)^2/4$. The $u$-coordinates of $b,c$ have absolute values at least $a,p(β)$, respectively, because both vectors have length at least one. In particular both lower bounds are at most $1/2$. The distance of the difference of the two coordinates from an integer is at most $1-a-p(β)$. For coordinates with the same sign this follows from $|b_u-c_u|\le1/2-\min(a,p(β))$. For opposite signs the absolute difference lies in $[a+p(β),1]$, so subtracting a signed unit gives the bound.

The function $p(t)+(1+a)t$ is concave. At $1/2$ its value is above one by $p(1/2)>(1-a)/2$. At $β_0$ we have $p(β_0)=a$. For $1/3\le a\le1/2$, $4a(1-a)^2\ge1/2$, since this polynomial is decreasing on that interval and equals $1/2$ at its right endpoint. Using $B=1-a^2$ gives
\[
 C<1/(2B)\ \le\ 4aB/(1+a)^2 .
\]
Hence $β_0>(1-a)/(1+a)$, so the other endpoint value is also above one. Concavity proves $p(β)+(1+a)β>1$. Now $c-b$, reduced along $u$, is a nonzero lattice vector with squared length at most $C+B(1-β)^2+(1-a-p(β))^2$. Subtracting one from this expression gives $2(1-a)(1-p(β)-(1+a)β)<0$, a contradiction. Thus $c(L)^2\ge1/2$ at shortest length one. Undoing the scaling gives $λ_1(L)^3\le\sqrt2 c(L)$.

The rational overestimates $2/\sqrt3<231/200$ and $\sqrt2<99/70$ follow by squaring. These are existence bounds; the short-span algorithm below supplies a polynomial-time lift without needing the basis of the lattice used in the existence proof.

### Polynomial-time Euclidean lifting

Discard the zero homogeneous coordinate of $v\ne0$ and order the rest with $v_1\ne0$. Let $L_i=\{x\in\mathbb Z^i:\bar x\in\mathbb F_q v_{[i]}\}$ and let $S_i$ span its vectors of length at most $B_E$. Four independent short vectors would give a nonzero four-row minor divisible by $q^3$: the residues lie on a line, so three rows can be made divisible by $q$ by subtracting multiples of a row with nonzero residue, or all four already are. Its absolute value is at most $B_E^4<q^3$ by Hadamard. Hence $\dim S_i\le3$.

Store a basis of actual short vectors, starting with $1\in L_1$. Every short next-prefix vector projects into $S_i$. Form $U$ from the stored vectors extended by zero and the final unit vector. Choose invertible rows $J$ and write $UU_J^{-1}=A/c$ with integer $A$, $c=|\det U_J|$. These have $O(\log q)$ bits by fixed-size minors. The integer $J$-coordinates $y$ give exactly the allowed vectors $Ay/c$ through the congruences
\[
 A_jy=0\pmod c,\quad (v_1A_j-v_jA_1)y=0\pmod{cq}
\]
for each row $j$, using integer representatives. The first ensures integrality and allows division by $c$ in the second even if $q\mid c$.

Starting from the identity basis for $y$, impose each congruence of modulus $b$ by column gcd operations reducing its row in the current basis to $(h,0,\ldots,0)$, then scale the first column by $b/\gcd(b,h)$ (skip zero rows). Normalize after each update by column gcd operations row by row on columns without pivots, then subtract multiples of pivot columns in row order to put entries left of each pivot in $[0,\text{pivot})$. Already reduced earlier rows are preserved by later columns. Pivot product equals index, at most the product of the processed moduli, so all normalized entries have $O(i\log q)$ bits. At most four gcd reductions and sixteen residue updates per normalization give polynomial bit time, including intermediate entries. Applying $A/c$ gives a basis of $L_{i+1}\cap(S_i\times\mathbb R)$ of rank at most four.

Use the following basis reduction for rational lattices in rank $r\le4$, clearing denominators before reduction and restoring scale afterwards. With Gram–Schmidt vectors $b_i^*$ and coefficients $η_{ij}$, round off $η_{ij}$ by subtracting integer multiples of $b_j$ in descending $j<i$, leaving larger-index coefficients fixed. Swap neighboring columns if
\[
 \|b_{i+1}^*\|^2+η_{i+1,i}^2\|b_i^*\|^2<(3/4)\|b_i^*\|^2,
\]
then fully size reduce again. For the integer basis, the squared prefix volumes $H_j=\det(B_{[j]}^\top B_{[j]})$ are positive integers, with $H_0=1$. Size reduction preserves them, while a swap changes just $H_i$, by the ratio of the new to old squared length after projection off the first $i-1$ columns. The product decreases by a factor below $3/4$ on each swap, so Hadamard gives polynomially many swaps. At size-reduced stages, $\|b_i^*\|^2=H_i/H_{i-1}\le\prod_j H_j$ and $\|b_i\|^2\le r\prod_j H_j$. A swap preserves column norms and the ensuing at most six rational rounding updates therefore have polynomial-size intermediate data. The output satisfies $|η_{ij}|\le1/2$ and $\|b_{i+1}^*\|^2\ge\|b_i^*\|^2/2$. Recover original coordinates by exact rational solves.

For exact closest vector, project the target into the span. Nearest-plane rounding descends from $r$ to $1$, subtracting the nearest multiple in the current Gram–Schmidt coordinate and preserving all later ones. Its distance bound is $\sqrt{\sum_i\|b_i^*\|^2}/2\le\sqrt{2^r-1}\|b_r^*\|/2<2\|b_r^*\|$. A closest vector has last coefficient within two of the target's last normalized coordinate. Try those at most five integers, subtract the candidate multiple of $b_r$, and solve in the reduced prefix after projection. Add the squared orthogonal residual to each squared distance and minimize. The depth is at most four, with exact rational comparisons and rank-zero output zero.

In the prefix lattice $L$ find a new short vector outside the span $W$ of the already stored short vectors. In basis coordinates express $W$ as a kernel of at most four integer rows by clearing denominators. Apply successive column gcd operations to each row restricted to the current kernel columns, retaining the first transformed column as complement whenever the row is nonzero. The remaining columns are its exact integral kernel, and the whole basis stays unimodular. This gives $L\cap W$ and complementary columns, whose projections off $W$ form a rational lattice basis. If its rank is zero, report no new vector. Otherwise reduce the projected basis. If its first vector has length at most $B_E/2$, lift it via the complementary columns and round its $W$ part by nearest plane in the stored short basis. The latter has at most three Gram–Schmidt lengths at most $B_E$, so the resulting squared length is at most $3B_E^2/4+B_E^2/4$.

Otherwise every projected Gram–Schmidt length is greater than $2^{-(r+1)/2}B_E$. Enumerate nonzero projected vectors of length at most $B_E$ by descending coordinates: for fixed later coordinates each new coordinate lies within six of its rational center by this length bound. For each exact norm-qualified projection, lift it and solve closest vector in $L\cap W$ to the negative of its $W$ component. Orthogonality makes the adjusted lift shortest for that projection. Return any within $B_E$, or certify none exists outside $W$. Branching and dimension are bounded, and all projection, basis and distance calculations use polynomial-bit rational arithmetic.

At each prefix start $W=0$ and add each returned vector. With dimension at most three, at most four searches yield a spanning short list. The congruence updates and searches over all prefixes cost polynomial bit time $T_{\rm LIFT}$ in $N_*,\log q$. At the last prefix return a stored vector with coordinate order and the homogeneous zero restored, or $\bot$ for an empty list. The returned nonzero vector has nonzero residue because $B_E<q$, and the congruences put it on the prescribed line.

## Amendment msis_norm

Set ${\rm msis\_norm}=2$ in the concatenated integer coefficient basis of C5. For any kernel vector $v$ and any Euclidean-short multiple $x\equiv a v\bmod q$, $a\ne0$, the bound $2B_E<q$ forces $x_0=0$. Packing copies all other coordinates once, inserts zeros and commutes with reduction. Thus $A\hat x=aA\hat v=0\bmod q$ and $0<\|\hat x\|_2=\|x\|_2\le B_E$, which proves the universal Euclidean packing clause. The original infinity clause remains true at its own norm and radius, as shown in msis_bound. There the heavy-stack selection and lifting prove existence and recovery for the amended reduction. Neither the public seed law, ring matrix, ciphertext nor decryption operation counts use the solution norm. Targets proves extraction and the reduction cost.

## Targets

Fix any admitted parameters, system and evaluation points. Use C6–C7 for the fields and masks, n and n1 for the form and QAP arrays, and I2–I6 with mu_tr for admissibility and inversion. Ncmp proves the charged-mark bound. The statements below use the prescribed oracle budgets and recover only the external witness coordinates.

### Correctness with error $2/q$

Fix an external witness $w$, the statement, message and admissible evaluation points. Every prescribed padding and tag extension used in n1 is an internal witness with $(H^{(1)})^\top v=(H^{(2)})^\top v=0$. If the prescribed weight of $v^{(0)}$ is zero decryption returns $\bot$. Otherwise the chosen target has nonzero weight, whenever the ordinary or direct-normalization branch is selected. The identities of n1 recover the exact key in these branches. They give the settled target value after the three exact integer logarithms and the equality $a_t+b_t-c_t=v^{(t)}$ in the ordinary branch, and directly in the branch where the chosen target base is zero. The evaluation-point branch recovers the exact key on every realization where it is called. Therefore failure is exactly the event of zero prescribed weight, which we bound next.

First consider the key weight for either fixed target. Let $L:F\to\mathbb F_q$ be the coefficient functional at one in the U product basis, nonzero because $L(1)=1$, and let $s=n/2-1$. Then the weight of a form value $x$ is $Q(x)=L(xσ^s(x))$, with $x$ uniform on the affine space with constant slot one and prescribed padding zero. The trace map is nonzero: the polynomial $\sum_{j=0}^{n-1}X^{q^j}$ has degree $q^{n-1}<q^n$ and cannot vanish at all $q^n$ field elements. The pairing $(a,b)\mapsto{\rm Tr}(ab)$ is therefore nondegenerate, since multiplication by a nonzero $a$ is invertible. Thus $L(x)={\rm Tr}(λ x)$ for a unique nonzero $λ$, by equality of the dimensions of the field and its scalar dual.

The polar form $Q(x+y)-Q(x)-Q(y)$ is
\[
 {\rm Tr}\!((σ^{-s}(λ x)+λσ^s(x)) y).
\]
Trace invariance under Frobenius gives this expression. By nondegeneracy, the radical solves $λ x+σ^s(λ)σ^{2s}(x)=0$. If there is one nonzero solution $x_0$, every other solution is $x_0$ times an element fixed by $σ^{2s}$, by dividing the two equations. Since $\gcd(2s,n)=2$, such a ratio is fixed by $σ^2$: use the integer Bezout identity for $2s,n$ and $σ^n=1$. There are at most $q^2$ of these ratios because they are roots of $X^{q^2}-X$. Hence the radical dimension is at most two and the polar rank at least $n-2$. The affine form domain has codimension ${\rm form\_pad}$. Restricting the polar form in either argument to its parallel linear space loses at most ${\rm form\_pad}$ ranks, by the rank of the omitted rows or columns. Therefore its rank is at least $n-2-2{\rm form\_pad}$, at least six in the scored shape and in the growing branch.

For an affine quadratic of rank $d$ over the fixed odd prime field, the proportion of zeros is at most $1/q+q^{-d/2}$. Indeed, use the character sum $q^{-1}\sum_{a\in\mathbb F_q}\exp(2π i a Q/q)$ for its zero indicator. A linear change of variables diagonalizes the quadratic part in odd characteristic, by choosing a vector with a nonzero square coefficient, completing its square to isolate it, and iterating. With $a\ne0$ a one-variable sum for a nonzero square coefficient has magnitude $\sqrt q$, even with a linear term: by completing the square the linear term is a unit-magnitude factor, and the squared magnitude of $\sum_x\exp(2π i c x^2/q)$ is the sum over $x,y$ of $\exp(2π i c(x-y)(x+y)/q)$. The map to $x-y,x+y$ is invertible, and summing first over one new coordinate gives $q$, since only the other coordinate zero has a nonzero inner sum. Every other coordinate has character sum bounded by $q$. After normalization the contribution of all nonzero $a$ to the zero probability is at most $q^{-d/2}$, and the zero character contributes $1/q$. Here $n\ge4000$ and ${\rm form\_pad}=6$ give $d\ge6$, so the key weight vanishes with probability at most $1/q+1/q^3$, and in particular at most $1/q+1/q^2$.

For the search probabilities condition on all scalar coins except $y$ and the seed matrix. Set $S(z)=\sum_cγ_cξ_c(z)$ on the affine form domain, a polynomial of total degree at most two. If it is identically zero, a nonzero prescribed weight always leads to primary direct normalization. Otherwise it vanishes with probability at most $2/q$ by the polynomial root bound. Independently the first factor $y(v)$ in any prescribed base is uniform and vanishes with probability $1/q$, so the base vanishes with probability at most $3/q$. For two distinct tag variants their two form values are jointly uniform on two copies of the domain: after fixing all other columns, the homogeneous column and a differing tag column give a two-by-two evaluation matrix of determinant $1$ or $-1$ in each free coefficient position. Likewise their two $y$ values are independent uniform, by the same determinant on the corresponding two coordinates and independently of the forms. Hence each pair of base-zero events for distinct tags has probability at most $9/q^2$. The event of one specified primary zero-corner base zero and a zero key weight of $v^{(1)}$ has probability at most $6/q^2$, by joint uniformity of their distinct tags and the key-weight bound.

The fallback requires at least one base zero among $a_0,b_0,c_0$, and either a zero secondary target weight or at least one base zero among $a_1,b_1,c_1$. Otherwise the selector gives an ordinary or direct normalization branch. The three events of the first kind paired with the secondary weight contribute at most $18/q^2$ and the nine pairs of base events contribute at most $81/q^2$. Thus fallback probability is at most $99/q^2\le135/q^2$. An ordinary secondary triple also requires a zero among the three primary ordinary bases, so its probability is at most $9/q$. All bounds hold conditional on the fixed scalar coins and therefore also unconditionally, and all selection events are independent of the integer sampler.

### Extraction and the reduction

Let $\mathcal A$ have the budget $Q<2^λ$ of generic group calls and at most $2^λ$ queries to each oracle. Fix one bit $b$ and messages $m_0,m_1$, and run the extraction experiment with $m_b$. The extractor reads the answered generic transcript without any oracle calls. It uses the protected extractor sketches for the plain sector. The empty alpha sector can be represented by zero records. It samples three independent probe vectors for each cell, uses the linear combinations of source-group records and pairings to form sketches, tests the sketches of the result and the difference when there is an old record, checks Booleanity of pads and tags, tests $S$ on coordinates $1,\ldots,N$, and returns those $N$ external witness bits. In rank at most three, there are at most four assignments with first coordinate 1 to test: row echelon pivot coordinates determine the vector, pivot 0 must be present, and at most two remaining pivot choices are bits. Output is therefore always $\bot$ or a witness. A record creation, result, or difference touches $O(K_1N_*+n)$ field elements, since a source-group record uses at most $K_1$ length-$(N_*+1)$ vectors or $6A_c$ values, and the pairings compute six such combined sketch vectors. For a pairing, forming the inner products in the G2 record or summing per left leg and combining the G1 vectors uses $O(K_1N_*+n)$ operations. A test uses $O(N_*)$ for elimination with at most three rows and $O(N_*+|S|)$ to generate and check the constant number of candidates. Initialization samples $6A_c(N_*+1)$ field values, enters the $L$ labels as records whose vectors are materialized on first use, and uses $O(nN+L)$ time. There are at most four tests per result. Thus the extractor uses $O((Q+1)(nN+|S|)+L)$ time because $K_1\le n$ and $N_*\ge1$.

The reduction on input a uniform $A\in R_q^{k\timesℓ}$ samples the seed and programs the raw seed-oracle answers on columns $1,\ldots,ℓ$ as $E(A_{ij})$. It samples every other answer lazily as an independent uniform tuple, including column zero, and returns the same tuple on repeated queries. Thus each programmed conceptual coefficient entry is exactly $A_{ij}$, and the raw tuple law is the same as in encryption by invertibility of $E$. If the challenge is supplied in the coefficient representation, the reduction performs these forward transforms once during its initialization. This costs $O(k(ℓ+1)d_R^2)$ field operations, within $O(nD)$ for the fixed-degree scored branch because $kd_R\le n$, $ℓ+1\le N+4\le D$, and $d_R$ is guarded by C5. This term belongs to $C_R$. It samples encryption coins as specified, produces the ciphertext for $m_b$, and simulates all generic labels and names and random oracles by the protected lazy tables. It runs $\mathcal A$ once. The extraction steps use the answered generic transcript without its output or the random-oracle query transcript, while the lazy tables implement exactly the direct oracle law. Because the programmed entries are jointly independent uniform ring elements for uniform $A$, all oracle answers including entries at the selected seed have exactly the joint law of the experiment. Private evaluation points are sampled independently of the run.

The reduction attempts recovery for the first target result with private value differing from its reused record, using their difference, and for the target-label record if present. For each attempt compute three gradients at independent recovery points, test their span for a kernel vector, and run the selection and LIFT of msis_bound. By n, a kernel vector has $v_0=0$ and $A\hat v=0$. The lift and norm-preserving packing of ell return a nonzero solution with $\|\hat x\|_2\le B_E$, for the precise uniform instance costed by M1. Otherwise return $\bot$. Let $s_b$ be this reduction's success probability. The proved C7 implementation costs $t+148Q+(d_R+5)Q_H+C_R+2T_{\rm LIFT}$ for the maximal per-oracle query count $Q_H$, with $C_R=O((N_*+n)D+μ)$. I6 gives the premises $2B_E<q$ and $B_E^4<q^3$ of the polynomial-time lift. Thus the cost is $t+O(Q+d_RQ_H+μ)+{\rm poly}(D,\log q)$.

Here is how the first-mark bounds apply to these algorithms. The degree and view for the new field encoding and the needed gradient formula are derived above. The record invariant uses no inverse premise: setting all guesses to zero commutes with additions and pairings, and before the first mark every reused label comes from formally equal expressions. Formally equal target expressions have identical stacks by the fiber equations applied to their difference for every field search vector. Thus their records also have equal sketches. A good mark's stack is usable with the three field ties of Amendment C7 by the revised view. Its rank is at most three by the five public shifts and rank proof in I5. The full classification applies to every actual tied stack of dimension at most three, including zero-corner marks, because the three ties just derived are the original field identities. A kernel vector in its row space has coordinate 0 equal to zero, and its one-dimensional guessing probability is at least the stack's, by the replacement rank lemma in search_spread. The selection in Amendment msis_bound gives a short multiple at Euclidean radius $B_E$. The amended LIFT therefore succeeds on that selected kernel vector.

At a first good difference mark its difference is formally nonzero, so the cleared polynomial is nonzero in the coins at some fixed search vector. This makes it a nonzero joint polynomial in coins and search coordinates. The private test uses independent uniform search coordinates and valid coins; the product-set bound gives failure probability at most $d_f/(q-D)$. Earlier formal equalities are equalities at every private point by the record invariant, so outside this failure the reduction picks exactly this difference. The degree bound and the uniform valid coin ranges give probability at most $ε_f$ for this failure. For a first good key mark the target record already has its expression by the record invariant and persists. Name negatives are target-group results and receive the same private and sketch tests. For a recognized good mark, the coefficient-vanishing and derivative calculation of the algebraic view subsection place each sector gradient in that sector row space. There is no nonzero alpha stack. For any proper subspace of the mark row space choose a linear form zero on the subspace and nonzero on the row space. Its value on one gradient, divided by $π$, is a polynomial of degree at most $n+2+R_{\rm leg}$, using the seed-mode bound in the C7 degree ledger. This polynomial is nonzero by isolating the constant term in $ε$ and the independent products $s_X L_a(υ)R_j(υ)y_i$. The valid values for the independent coin coordinates have sizes at least $q-D$, by the independent coin support argument. The polynomial root bound, with $q-D$ in place of $q$ in its proof, bounds the chance of failing to increase the span while it is proper. Three independent points and rank at most three give failure at most $3(n+2+R_{\rm leg})/(q-D)\leε_f$, by $2n\le D$ and $R_{\rm leg}<n$ and the formula for $ε_f$. Thus on a good first mark with a kernel vector, except for the two exceptional events just bounded, the reduction finds a kernel vector in the appropriate span, and produces the MSIS output. The unconditional probability of such a mark is at most $s_b+2ε_f$.

For a good first mark with no kernel vector, the classification proved in Amendment C7 gives an extended witness in its row space. Its ordinary projection satisfies the external system. In that sector the linear map from a tuple of probes to $\sum_c W_cv_c$ has image the row space, as each matrix is symmetric and the sum of its images is the row space of the stack. Uniform independent probe tuples give three independent uniform vectors in this space, even conditional on the run. In dimension $a\le3$, the chance of failing to span is bounded by $\sum_{j=0}^{a-1}q^{j-3}<2/q$: equivalently the $a$ rows of the random $a$-by-3 coordinate matrix are independent uniform three-dimensional vectors and the next row falls in the span of $j$ independent previous rows with probability $q^{j-3}$. At a difference mark the extractor tests the record difference. If the old entry is a pure guess, a guess-free difference requires the result to contain that same guessed variable with coefficient one. The label has therefore been used in an answered call, possibly the current call, and has a zero record by the test. At a key mark it tests the record of the result that obtained the target label. An initially received record has zero stack and thus is no good mark. These facts from the record invariant show that if the sampled vectors span, the witness is among the assignments tested. So the probability of a good first mark with no kernel vector and with extractor failure is at most $2/q$.

Let $u=2Q+2$. Every target query run has a first mark. The protected initial and guessed-mark estimates and the charged-mark estimate of Amendment Ncmp bound their three probabilities by
\[
(\binom{L_1}{2}+\binom{L_2}{2}+\binom{L_T}{2})ε_f,\quad
N_{\rm cmp}(u)(θ+ε_f)
+(\binom{L+3u}{2}+L+3u)ε_f,\quad
2^λ/N_{\rm free},
\]
respectively. These estimates concern the same sampler, oracle and record laws and use only the already checked view and degree properties, budget, and label counts. Together with the two good-mark cases they cover the event of a target key query and no witness. Their sum is at most $s_b+E(u)$: the good-mark excess is $2ε_f+2/q\le (8u+8)ε_f$, using $ε_f\ge1/q$; the remaining terms of $E$ are nonnegative and its guess term contains $2^λ/N_{\rm free}$. By (P5) and the generic-ledger implication of Amendment Ncmp $E(2Q+2)\le(Q+1)/2^λ$. Hence for each $b$ the target-query and no-witness probability is at most $(Q+1)/2^λ+s_b$, with exactly the stated oracle budgets and one MSIS instance. This proves Theorem 5.9 with its extraction time and soundness as above.
