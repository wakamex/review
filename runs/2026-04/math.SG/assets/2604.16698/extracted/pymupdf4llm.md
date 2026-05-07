## **Weighted blowups and 3d Poisson desingularizations** 

SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

Abstract. We establish existence of functorial orbifold reductions of singularities for Poisson subvarieties in smooth Poisson threefolds. Namely, we show that with enough weighted blowups, one can reduce the singularities of such Poisson subvarieties to certain simple, explicit, local normal forms: Du Val surface singularities where the Poisson structure is locally Jacobian, and plane curves lying in the vanishing locus of a particular linear Poisson structure. The proof combines Abramovich–Temkin–W�lodarczyk and McQuillan’s recent approach to resolution of singularities for varieties via weighted blowups with some new normal forms for three-dimensional Poisson brackets derived via Poisson cohomology. Along the way, we describe necessary and sufficient conditions for a polyvector field to lift to the weighted blowup of an orbifold along a suborbifold, generalizing criteria of Polishchuk for unweighted blowups of Poisson structures on smooth varieties. 

## Contents 

|1.|Introduction|1|
|---|---|---|
|2.|Weighted blowups of orbifolds|5|
|3.|Blowups of polyvector felds|13|
|4.|Blowups of Poisson structures|16|
|5.|Weighted normal forms of Poisson structures|19|
|6.|Singularity invariants and resolutions|24|
|7.|Weighted resolutions of Poisson subvarieties|30|
|References||39|



## 1. Introduction 

1.1. **Context.** Numerous deep results in algebraic geometry ultimately rely on Hironaka’s desingularization theorem [Hir64], which guarantees that the singularities of any algebraic variety over a field of characteristic zero can be resolved by making sufficiently many blowups along smooth subvarieties. Moreover, it is often useful to know that this can be done in an “embedded” way, e.g. that for a smooth variety X and a singular subvariety Y we can construct a smooth variety X _[′]_ , a smooth subvariety Y _[′] ⊂_ X _[′]_ and a surjective projective morphism of pairs (X _[′] ,_ Y _[′]_ ) _→_ (X _,_ Y) that is an isomorphism away from the singular locus of Y. 

However, in the presence of a symplectic/Poisson structure, the theorem breaks down. For instance, many symplectic singularities in the sense of Beauville [Bea00] admit no Poisson/symplectic resolution; see e.g. [Fu05, Ver00]. The basic problem is that Poisson structures cannot be pulled back along arbitrary maps; in particular, they may develop poles along the exceptional divisor of a blowup. 

1 

2 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

A similar situation occurs for foliations, where it was observed in [MP13, Pan06] (and later [ABdSTW25]) that one can get closer to resolving the singularities if one uses “weighted” blowups that assign different weights to different normal directions to the centre. More recently, Abramovich–Temkin–W�lodarczyk [ATW24] and McQuillan [McQ20] showed that resolution of singularities of varieties (absent further structure) can be done faster and more functorially using weighted blowups as well. The trade-off is that one must work with orbifolds (Deligne–Mumford stacks) rather than varieties. The reason is that weighted projective spaces, when viewed as varieties, have finite quotient singularities. Thus, to prevent weighted blowups from introducing new singularities, we must instead view them as smooth orbifolds, which is good enough for many applications anyhow. 

In this paper, we describe the conditions under which a Poisson structure can be lifted along such a weighted blowup of orbifolds, and use it to give an algorithm to reduce, as much as possible, the singularities of Poisson varieties, in embedding dimension up to three. As we shall see, this approach yields much stronger results than would be possible using ordinary blowups alone. 

1.2. **Results.** We work throughout with orbifolds over an algebraically closed field K of characteristic zero, i.e. smooth separated Deligne–Mumford stacks of finite type over K, or complex analytic orbifolds with K = C. By a _**Poisson triple**_ , we mean an orbifold X equipped with a Poisson structure _σ_ (i.e. a Poisson bracket on _O_ X) and a Poisson subvariety Y _⊂_ X (i.e. the closed substack defined by a coherent sheaf of Poisson ideals). 

Starting from an arbitrary Poisson triple (X _,_ Y _, σ_ ) we try to construct a new triple (X _[′] ,_ Y _[′] , σ[′]_ ) _→_ (X _,_ Y _, σ_ ) giving an embedded resolution (or at least improvement) of the singularities of Y. When dim X _<_ 2, the Poisson structure is zero and Y is smooth, so there is nothing to do. Meanwhile, when dim X = 2, repeatedly applying ordinary blowups to the singular points of Y produces an embedded Poisson resolution (X _[′] ,_ Y _[′] , σ[′]_ ) _→_ (X _,_ Y _, σ_ ); we show that the same is true if we apply the new weighted resolution algorithm of [ATW24], i.e. the latter is compatible with Poisson structures in embedding dimension two. 

However, when dim X = 3, we encounter two types of singularities, illustrated in Figure 1, that can never be blown up without destroying the Poisson structure on the ambient space X: 

- _**Non-nilpotent points**_ , where Y is a curve with planar singularities, contained in the vanishing locus of _σ_ , and the Lie algebra obtained by linearization of the Poisson bracket is not nilpotent. Near such a point, the triple (X _,_ Y _, σ_ ) has a simple normal form: there exists formal coordinates ( _x, y, z_ ) such that 

_σ_ = _x∂x ∧ ∂y_ and Y = _{x_ = _g_ ( _y, z_ ) = 0 _},_ 

for some _g_ ( _y, z_ ). 

- _**Du Val points**_ , where Y is a surface with a Du Val singularity, and _σ_ has an isolated zero, so that _σ_ induces a symplectic structure on the smooth locus of Y in a neighbourhood of _p_ . They also have a simple normal form: 

- _σ_ = _g_ ( _fx∂y ∧ ∂z_ + _fy∂z ∧ ∂x_ + _fz∂x ∧ ∂y_ ) and Y = _{f_ = 0 _},_ where _f_ is a standard equation for a Du Val singularity (recalled in Table 1 in Section 6.3) and _g_ is a function with constant term _g_ ( _p_ ) = 1. Abstractly, 

Weighted blowups and 3d Poisson desingularizations 

3 

**==> picture [125 x 117] intentionally omitted <==**

**(a)** A non-nilpotent point, where Y is a singular curve (red) lying in the vanishing locus of the Poisson structure, which is a vertical plane (purple). The horizontal planes (blue), minus their intersection with the vertical plane, are symplectic leaves. 

**==> picture [144 x 133] intentionally omitted <==**

**(b)** A Du Val point, where Y is a surface (red) with a Du Val singularity, whose smooth locus is a symplectic leaf. The remaining symplectic leaves (blue) are the other level sets of a defining equation of the surface. 

**Figure 1.** Singular Poisson subvarieties Y _⊂_ A[3] that cannot be resolved by weighted blowups. 

these are the three-dimensional Poisson structures given by restricting the versal Poisson deformation of a symplectic surface singularity to a smooth curve in the base of the deformation. 

Note that these conditions involve both the subvariety Y and the Poisson structure. They can be thought of as a sort of nondegeneracy condition on _σ_ along the singular locus of Y. 

Our main result shows that in all other cases, the singularities of Y can be improved by a judicious choice of weighted blowups: 

**Theorem 1.1** (see Theorem 7.10 and Theorem 7.19) **.** _Let_ X _be an orbifold of dimension three equipped with a Poisson structure σ, and let_ Y _⊂_ X _be a Poisson subvariety of pure dimension. Then there exists a sequence of weighted blowups of Poisson triples_ 

(X _[′] ,_ Y _[′] , σ[′]_ ) _→· · · →_ (X _,_ Y _, σ_ ) 

_such that the only singularities of_ Y _[′] are non-nilpotent points (when_ dim Y = 1 _) or Du Val points (when_ dim Y = 2 _)._ 

We remark that the use of weighted blowups here is crucial; with only ordinary blowups, the situation is much less under control. For instance, the Jacobian Poisson structure (Example 4.7) of any function with an isolated singularity of multiplicity two can never be blown up with an ordinary blowup. Thus ordinary blowups will fail to improve many non-Du Val singularities. 

The basic strategy of our proof of Theorem 1.1 is to try, as much as possible, to apply the weighted blowup algorithm of [ATW24]. We find that for “most” singularities, the blowup prescribed by the algorithm is automatically compatible with the Poisson structure, but for some singularities, it is not. We then study the latter cases in detail, and show that unless the singularities are non-nilpotent or Du Val as above, we can find an alternative blowup that still improves the 

## 4 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

singularities. In order to carry out this analysis, we establish several additional intermediate results which may be of independent interest, most notably: 

- Theorem 3.3 gives necessary and sufficient conditions to lift a polyvector field along a weighted blowup of an orbifold. Specialized to the case of bivectors, it gives conditions for the weighted blowup of Poisson structures, generalizing the results of Polishchuk [Pol97, §8], who treated the unweighted case, albeit with a somewhat different exposition. 

- Proposition 6.13, which gives a characterization of Du Val singularities, two-component normal crossings, and Whitney umbrellas as the singular surfaces in A[3] whose singularities are “small” in a certain precise sense. This is closely related to the characterization of Du Val singularities as the canonical singularities of dimension two (see e.g. [Rei80]). 

- Proposition 5.7 and Proposition 5.8, which give normal forms for certain three-dimensional Poisson structures, using Poisson deformation theory via the Poisson cohomology differential graded Lie algebra. Here we make essential use of the calculations of certain key Poisson cohomology groups due to Hoekstra–Zeiser [HZ23] and Pichereau [Pic09]. 

The paper thus involves a mixture of techniques from both resolution of singularities and Poisson geometry, and we include some review of relevant techniques at various points in the paper, most notably in Section 2 and Section 6. 

1.3. **Implications and related questions.** Let us comment briefly on the scope of the result and its connection with related problems. 

1.3.1. _Higher dimension._ While our general results on blowups of polyvectors work in any dimension, many of the methods used to prove Theorem 1.1 are quite specific to dimension three. For instance, we use explicit normal forms for the Poisson bracket. We also rely on the fact that non-nilpotent and Du Val points are isolated, so that they cannot interfere with other singularities. We hope to make progress on the higher-dimensional case in future work, in the spirit of the recent work [ABdSTW25] on foliations. 

1.3.2. _Non-embedded resolutions._ Since curves and symplectic surface singularities admit Poisson resolutions, Theorem 1.1 implies that the singularities of Y itself can be fully resolved by a Poisson morphism Y _[′] →_ Y. The issue is that Y _[′]_ may not be embeddable in a threefold X _[′]_ given by blowing up X, so this does not produce an embedded resolution of the pair (X _,_ Y). 

1.3.3. _Logarithmic resolutions._ For many purposes one wishes to have “logarithmic” resolutions for which the exceptional divisor is simple normal crossings. This is not guaranteed by the methods of [ATW24] on which our Theorem 1.1 is based, but more recent works have modified the algorithm to produce logarithmic resolutions [Que22, W�l23]. We plan to adapt these methods to the Poisson setting in future work. 

1.3.4. _Alterations._ For many purposes in algebraic geometry, such as the study of cohomology, one can get by with a weaker notion of resolution, called an alteration [dJ96], which allows branched covers, not just birational maps. Intriguingly, 

Weighted blowups and 3d Poisson desingularizations 

5 

Du Val points of Poisson triples admit a well known Poisson alteration in a neighbourhood of the singular point, given by a slice of the Grothendieck–Springer alteration for semisimple Lie algebras. It would be interesting to construct global counterparts of this alteration. 

1.3.5. _Semiclassical Hodge theory._ Our work is motivated, in part, by the study of Hodge-theoretic invariants of smooth Poisson varieties and their quantizations by Lindberg and the third author [LP24], following ideas of Kontsevich [Kon08] and Katzarkov–Kontsevich–Pantev [KKP08]. In order to treat singular varieties, or to establish functoriality in the smooth case, one needs some weak form of resolution of singularities for embedded Poisson varieties. While the results of this paper do not completely resolve the singularities, they should still enable the relevant Hodge-theoretic constructions in dimension three, e.g. since the logarithmic de Rham complex of a Du Val singularity is well understood. 

1.4. **Acknowledgements.** Special thanks are due to Maxim Brais, whose numerous insights have informed the third author’s understanding of resolution of singularities. We also thank Dan Abramovich, Ana B˘alibanu, Andr´e Belotto da Silva, Rui Loja Fernandes, Eckhard Meinrenken, Travis Schedler, Michael Temkin and Florian Zeiser for helpful conversations on related topics. Several of these conversations were made possible through workshops hosted by CIRM and BIRS-IASMHangzhou; we thank the institutes and the workshop organizers for the stimulating events. 

S.L. was supported by an Undergraduate Student Research Award from the Natural Sciences and Engineering Research Council of Canada (NSERC). M.M. was supported by a startup fund at The Chinese University of Hong Kong. B.P. was supported by a faculty startup grant at McGill University, a New university researchers startup grant from the Fonds de recherche du Qu´ebec – Nature et technologies (FRQNT), and by NSERC, through Discovery Grant RGPIN-2020-05191. B.Z. was supported by a Tomlinson Fellowship at McGill University. 

## 2. Weighted blowups of orbifolds 

In this section, we review the theory of weighted blowups of orbifolds based on Rees algebras of filtrations, as developed in [LM23, MP13, McQ20, Que22, W�lo23]; see also [Bra25]. Since the terminology, conventions, and notation vary across these references, and each has aspects that are relevant for us, we have adopted a mixture that we present here in a self-contained manner. 

2.1. **Orbifolds.** We work throughout over an algebraically closed field K of characteristic zero. By an _**orbifold**_ we mean a smooth separated Deligne–Mumford stack X of finite type over K or a complex analytic orbifold when K = C. Thus X is ´etale locally isomorphic to the stack quotient of a smooth variety by a finite group. 

We denote by _O_ X the structure sheaf of X and by _T_ X the sheaf of vector fields. A (closed) _**orbifold subscheme**_ is a closed substack Y = V( _J_ ) defined by the vanishing of a coherent sheaf of ideals _J < O_ X. An orbifold subscheme is an _**orbifold subvariety**_ if it is reduced, i.e. _O_ Y = _O_ X _/J_ has no nilpotent elements. 

By an _**orbifold chart**_ on X, we mean an ´etale open _ϕ_ : U _→_ X, together with functions _x_ 1 _, . . . , xn ∈O_ (U) defining an ´etale map U _→_ A _[n]_ . We will often simply say that ( _x_ 1 _, . . . , xn_ ) are orbifold coordinates on X, the et´ale open being left implicit. 

6 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

2.2. **Numerical conventions.** A _**weight sequence**_ (of length _k_ ) is a weakly decreasing sequence 

**w** = ( _w_ 1 _≥ w_ 2 _≥ w_ 3 _≥· · ·_ ) 

of non-negative rational numbers, such that _wj_ = 0 if and only if _j > k_ . We shall abuse notation and identify a weight sequence of length _k_ with the corresponding tuple ( _w_ 1 _, . . . , wk_ ), which contains the same information. 

An _**exponent sequence**_ is a sequence 

**==> picture [110 x 11] intentionally omitted <==**

obtained by taking the termwise reciprocal of a weight sequence **w** , so that _ai_ = 1[its][length][is][the][length][of][the][corresponding][weight][sequence,][or] _wi[∈]_[Q] _[>]_[0] _[ ⊔{∞}]_[;] equivalently the number of entries of **a** that are finite. We identify an exponent sequence of length _k_ with the tuple ( _a_ 1 _, . . . , ak_ ). 

A _**weight sum sequence**_ is a sequence 

**==> picture [112 x 11] intentionally omitted <==**

obtained by taking the partial sums of a weight sequence: _κj_ = _w_ 1 + _· · ·_ + _wj_ . Note that _κ_ 0 = 0 is the empty sum. 

All of these sequences can be viewed as taking values in the _**extended nonnegative rational numbers**_ 

**==> picture [78 x 11] intentionally omitted <==**

_Example_ 2.1 _._ The weight sequence **w** = (3 _,_ 2) = (3 _≥_ 2 _≥_ 0 = 0 = _· · ·_ ) has corresponding exponent sequence ( 3[1] _[,]_[1] 2[)][=][(][1] 3 _[≤]_ 2[1] _[≤∞]_[=] _[∞]_[=] _[· · ·]_[ )][and][corresponding] weight sum sequence _**κ**_ = (0 _,_ 3 _,_ 5 = 5 = _· · ·_ ). ♢ 

2.3. **Weighted orders of monomials.** Suppose that ( _x_ 1 _, . . . , xn_ ) are coordinates on an orbifold X. If _J_ = ( _j_ 1 _, . . . , jn_ ) is a multi-index, we denote by 

_x[J]_ := _x[j]_ 1[1] _[· · ·][ x] n[j][n]_ 

the corresponding monomial. Given a weight sequence **w** , we can think of the quantity 

**==> picture [135 x 12] intentionally omitted <==**

as the “ **w** -weighted order of vanishing of the monomial _x[J]_ ” at the origin. If **a** = **w**[1] is the corresponding exponent sequence, then the tuple ( _x[a]_ 1[1] _[, x][a]_ 2[2] _[, . . . , x] n[a][n]_[)][lists][the] coordinate powers that have weighted order one (with the convention that 0 _· ∞_ = _∞ ∞_[= 1).] 

_Example_ 2.2 _._ Consider the weight sequence **w** = (3 _,_ 2) and corresponding exponent sequence ([1] 3 _[,]_ 2[1][)][from][Example][2.1][.][In][coordinates][(] _[x, y, z]_[)][the][weighted][order][of] the monomial _x[i] y[j] z[k]_ is equal to 3 _i_ + 2 _j_ , and the coordinate powers of order one are given by ( _x_[1] _[/]_[3] _, y_[1] _[/]_[2] _, z[∞]_ ). ♢ 

2.4. **Weighted centres.** The concept of weighted order of a monomial depends on the choice of coordinates and therefore does not globalize well. The filtration on functions defined by weighted order of vanishing is better behaved, so that the correct global notion is the following. 

**Definition 2.3.** Let X be an orbifold. A _**centre**_ on X is a collection Z _•_ = (Z _λ_ ) _λ∈_ Q _≥_ 0 of orbifold subschemes, with defining ideals _I•_ = ( _Iλ_ ) _λ∈_ Q _≥_ 0, such that for every 

Weighted blowups and 3d Poisson desingularizations 

7 

closed point _p ∈_ X, there exist coordinates ( _x_ 1 _, . . . , xn_ ) centred at _p_ and a weight sequence **w** such that 

**==> picture [188 x 13] intentionally omitted <==**

is the ideal generated by monomials of **w** -weighted order at least _λ_ . We say that Z _•_ is defined locally by the _**weighted coordinates**_ ( _x_ **[a]** ) = ( _x[a]_ 1[1] _[, x][a]_ 2[2] _[, . . .]_[) where] **[ a]**[ =] **w**[1] is the corresponding exponent sequence. 

Given a centre Z _•_ with corresponding ideals _I•_ , we denote by 

**==> picture [59 x 24] intentionally omitted <==**

the ideal of elements of order strictly greater than _λ_ . 

**Definition 2.4.** The _**support**_ of a centre Z _•_ is the locus where all functions of positive order vanish: 

**==> picture [142 x 23] intentionally omitted <==**

Thus, in local weighted coordinates ( _x[a]_ 1[1] _[, . . . , x] n[a][n]_[)][the][support][supp][ Z] _[•]_[is][given] by the vanishing of all coordinates whose weight _wi_ = _a_ 1 _i_[is][positive,][or][equiva-] lently whose exponent _ai_ is finite. Hence it is a smooth closed subvariety whose codimension at a point _p_ is the length of the corresponding weight sequence. 

_Example_ 2.5 _._ For the centre Z _•_ defined by the weighted coordinates ( _x_[2] _, y_[3] _, z[∞]_ ) as in Example 2.2, the support supp Z _•_ = V( _x, y_ ) is the _z_ -axis. ♢ _Remark_ 2.6 _._ One can show that the weight sequence **w** (or equivalently the exponent sequence **a** ) at a point _p ∈_ supp Z _•_ in Definition 2.3 is independent of the choice of coordinates, and is constant on connected components of supp Z _•_ ; see, e.g. [Bra25, Remark 1.1.5]. ♢ 

2.5. **Reduced centres.** Note that if Z _•_ is a weighted centre and _λ ∈_ Q _>_ 0 is a nonzero rational, we can rescale the indices of the filtration by a factor of _λ_ to obtain a new centre Z _λ•_ . This freedom is convenient, but it will sometimes also be useful to eliminate it, which we can do by imposing the following condition. 

**Definition 2.7.** A weight sequence is _**reduced**_ if its nonzero entries are coprime integers. A centre Z _•_ is _**reduced**_ if the weight sequence at any point is reduced. 

_Remark_ 2.8 _._ If Z _•_ is reduced, the corresponding filtration _I•_ is completely determined by its values on the integers, i.e. by the ideals _I_ 1 _> I_ 2 _> · · ·_ . ♢ 

For every nonzero weight sequence **w** , there is a unique reduced weight sequence **w** and rational number _λ_ such that 

**==> picture [40 x 8] intentionally omitted <==**

We call _λ_ the _**greatest common divisor**_ of **w** and denote it by gcd **w** . 

Correspondingly, every centre Z _•_ has an underlying reduced centre Z ~~_•_~~[,][obtained] by rescaling the filtration locally by the greatest common divisor of the weight sequence. Thus, if Z _•_ is connected with weight sequence **w** , we have Z ~~_•_~~[=][ Z] gcd( **w** ) _•_[;] in general Z _•_ is the disjoint union of the reductions of its connected components. 

8 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

_Example_ 2.9 _._ The centre Z _•_ with weighted coordinates ( _x_[2] _, y_[3] _, z[∞]_ ) from Example 2.2 and Example 2.5 is not reduced: the entries of the weight sequence **w** = ([1] 2 _[,]_[1] 3 _[,]_[ 0)][are][not][integers,][let][alone][coprime.][However,][we][have] **[w]**[=] 16 _[·]_[ (3] _[,]_[ 2] _[,]_[ 0)] and the weight sequence (3 _,_ 2 _,_ 0) is reduced. Hence gcd **w** =[1] 6[and] **[w]** = (3 _,_ 2 _,_ 0), so that the underlying reduced centre Z _•_[is][defined][by][the][weighted][coordinates] ( _x_[1] _[/]_[3] _, y_[1] _[/]_[2] _, z[∞]_ ) ♢ 

2.6. **Unweighted centres.** A centre Z _•_ is called _**unweighted**_ if all its weights are zero or one; equivalently, it is defined locally be weighted charts of the form ( _x_ 1 _, x_ 2 _, . . . , xj, x[∞] j_ +1 _[, . . . , x] n[∞]_[).][In][this][case,][Z] _[•]_[is][reduced,][and][we][have] 

**==> picture [40 x 14] intentionally omitted <==**

for all _j ∈_ N, so that Z _•_ is completely determined by its support supp Z _•_ . 

Conversely, if Z _<_ X is a smooth closed subvariety defined by an ideal _J < O_ X, then setting _Ij_ := _J[j]_ for _j ≥_ 0 gives a unique unweighted centre whose support is Z. We call this the _**unweighted centre defined by**_ Z. 

2.7. **Cutting centres down to points.** Let Z _•_ be a centre of codimension _k_ , let _p ∈_ supp Z _•_ be a point in the support, and let **a** = ( _a_ 1 _, . . . , ak_ ) be the exponent sequence of Z _•_ at _p_ . Let _b ∈_ Q _>_ 0 be a rational number such that _b ≥ ak_ . Then, as explained in [Bra25, §3.1], one can form a centre supported at _p_ by using the exponent sequence ( _a_ 1 _, . . . , ak_ ) in the normal directions to supp Z _•_ , and assigning exponent _b_ to a system of coordinates on supp Z _•_ . More precisely, the _b_ _**-completion of**_ Z _•_ _**at** p_ from [Bra25, Definition 3.1.10] is the centre Z _•_ [ _p, b_ ] defined by the filtration 

**==> picture [116 x 24] intentionally omitted <==**

Concretely, if ( _x[a]_ 1[1] _[, . . . , x][a] k[k][, x] k[∞]_ +1 _[, . . . , x] n[∞]_[) is a system of weighted coordinates for][ Z] _[•]_ centred at _p_ , then ( _x[a]_ 1[1] _[, . . . , x] k[a][k][, x] k[b]_ +1 _[, . . . , x] n[b]_[)][is][a][system][of][weighted][coordinates] for Z[ _p, b_ ]. 

2.8. **Valuations.** If Z _•_ is a centre, _p ∈_ supp Z _•_ , and _f ∈O_ X _,p_ is a germ of a function at _p_ , then the weighted order of vanishing of _f_ is defined by 

**==> picture [160 x 11] intentionally omitted <==**

It is either a non-negative rational number (if _f_ = 0) or _∞_ (if _f_ = 0). Hence it can be encoded in a valuation 

**==> picture [76 x 11] intentionally omitted <==**

on the local ring _O_ X _,p_ , taking values in the extended non-negative rational numbers _Q_ = Q _≥_ 0 _⊔{∞}_ . 

Concretely, in local weighted coordinates ( _x[a]_ 1[1] _[, x][a]_ 2[2] _[, . . . , x] n[a][n]_[)][centred][at] _[p]_[with] weights **w** = 1 _/_ **a** , every _f ∈O_ X _,p_ has a Taylor expansion _f_ =[�] _cj_ 1 _···jnx[n]_ 1[1] _[· · ·][ x][n] k[k]_[,] and we have 

**==> picture [210 x 12] intentionally omitted <==**

Note that the possible weights of monomials form a discrete set, since they are integer multiples of gcd **w** . Hence if _f_ is nonzero, the infimum is always achieved by some monomial, i.e. it is a minimum. 

Weighted blowups and 3d Poisson desingularizations 

9 

_Example_ 2.10 _._ If Z _•_ is defined by the weighted chart ( _x_[2] _, y_[3] _, z[∞]_ ) of Example 2.2, then 

**==> picture [343 x 43] intentionally omitted <==**

with the minimum being achieved by the monomial _x_[2] _y_[4] _z_[5] . 

In contrast, for the unweighted centre Z _[′] •_[with][the][same][support,][defined][by][the] coordinates ( _x_[1] _, y_[1] _, z[∞]_ ), we have ordZ _′•_ ( _x_[5] ) = 5 and ordZ _′•_ ( _x_[2] _y_[4] _z_[5] ) = 6, so the minimum is instead achieved by _x_[5] . ♢ 

The weighted order of vanishing of a function is constant on connected components of the centre; hence it defines a morphism of sheaves 

**==> picture [79 x 10] intentionally omitted <==**

where _Q_ Z _•_ denote the constant sheaf on supp Z _•_ , viewed as a sheaf on X via pushforward along the inclusion. 

2.9. **Orders of tensors.** Given a centre Z _•_ and a point _p ∈_ Z _•_ , we may define a notion of order for germs of tensors at _p_ , as follows. Concretely, in local weighted coordinates ( _x[a]_ 1[1] _[, . . . , x][a] k[k]_[)][we][set] 

**==> picture [93 x 14] intentionally omitted <==**

and 

**==> picture [107 x 14] intentionally omitted <==**

and extend ordZ _•_ to a valuation on the tensor algebra. 

More intrinsically, if _p ∈_ Z, and _f, g ∈O_ X _,p_ are functions such that _f_ ( _p_ ) = 0, we set 

**==> picture [148 x 11] intentionally omitted <==**

(The normalization _f_ ( _p_ ) = 0 is needed to make this well defined, because d annihilates the constant functions.) The order of an arbitrary tensor _ξ ∈_ ( _T_ X _[∨]_[)] _[⊗][m][ ⊗T]_ X _[⊗][n]_ is then uniquely determined by the requirement that ordZ _•_ be additive with respect to the multiplication in the tensor algebra, and the pairing of _T_ X _[∨]_[with] _[T]_[X][.] More generally, if _F ⊂_ �� _m,n_[(] _[T]_ X _[∨]_[)] _[⊗][m][ ⊗T]_ X _[⊗][n]_ � _p_[is][a][set][of][germs][of][tensors,][we] denote by 

**==> picture [102 x 17] intentionally omitted <==**

the infimum of the orders of all elements of _F_ . 

2.10. **Orders of polyvectors.** We will be primarily interested in the _**polyvectors**_ 

**==> picture [54 x 14] intentionally omitted <==**

In a weighted chart ( _x[a]_ 1[1] _[, . . . , x] n[a][n]_[),][any][polyvector][can][be][written][uniquely][in][the] form 

**==> picture [111 x 22] intentionally omitted <==**

where the sum is over multi-indices _I_ = ( _i_ 1 _< · · · < ij_ ) and _fI ∈O_ X. Hence _ξ_ has order 

**==> picture [178 x 15] intentionally omitted <==**

10 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

Since the weight sequence **w** = ( _w_ 1 _, w_ 2 _, . . ._ ) is decreasing, the minimal possible order of polyvector of degree _j_ is achieved by the monomial _∂x_ 1 _∧· · · ∧ ∂xj_ , which has order _−w_ 1 _−· · · − wj_ = _−κj_ , the _j_ th weight sum. We therefore have the following: 

**Lemma 2.11.** _For a centre_ Z _• with weight sequence_ **w** _, and corresponding weight sum sequence_ _**κ** , the minimal order of a polyvector field of degree j ≥_ 0 _is given by_ 

**==> picture [74 x 13] intentionally omitted <==**

The Schouten bracket 

**==> picture [136 x 13] intentionally omitted <==**

has order zero, in the sense that 

**==> picture [127 x 11] intentionally omitted <==**

for all centres Z _•_ and all polyvectors _ξ, η ∈ X_ X _[•]_[, with equality if] _[ ξ]_[ and] _[ η]_[ are weighted] homogeneous and [ _ξ, η_ ] is nonzero. 

2.11. **Weighted normal bundle.** Let Z _•_ be a centre on X. Its _**weighted normal bundle**_ is the relative spectrum 

**==> picture [104 x 13] intentionally omitted <==**

where gr _[I][•] O_ X =[�] _λ∈_ Q _≥_ 0 _[I][λ][/][I][>λ]_[is][the][associated][graded][with][respect][to][the] filtration. Note that up to re-scaling the index of the gradings, the associated graded with respect to Z _•_ and its underlying reduced centre Z ~~_•_~~[are][the][same,][and] hence we have a canonical isomorphism 

**==> picture [205 x 11] intentionally omitted <==**

of orbifolds over X. 

The weighted normal bundle carries a natural projection NZ _• →_ supp Z _•_ and a “zero section” supp Z _• →_ NZ _•_ , which are dual to the inclusion of, and the projection onto, _O_ supp Z _•_ = _[∼] O_ X _/I>_ 0 _⊂_ gr _[I][•] O_ X. The ideals[�] _µ≥λ[I][µ][/][I][>µ][⊂]_[gr] _[I][•][ O]_[X][for] _λ ∈_ Q _≥_ 0 then define a centre on NZ _•_ supported on the zero section, with the same weights as Z _•_ . 

If ( _x[a]_ 1[1] _[, . . . , x] n[a][n]_[)][are][weighted][coordinates][compatible][with][Z] _[•]_[then][their][images] 

_x_ ˙ _i_ := _xi_ + _I>wi ∈_ gr _[I] w[•] i[O]_[X] 

give a system of weighted coordinates ( ˙ _x[a]_ 1[1] _[, . . . ,][x]_[˙] _[a] n[n]_[)][on][NZ] _[•]_[.] 

2.12. **Leading terms.** Every _f ∈O_ X has a _**leading term**_ 

**==> picture [55 x 11] intentionally omitted <==**

defined as the image of _f_ in the associated graded: 

lt( _f_ ) := _f_ + _I>λ ∈_ gr _[I] λ[•][O]_[X] where _λ_ = ordZ _• f_ 

For instance, the coordinates on the normal bundle above are given by _x_ ˙ _i_ = lt( _xi_ ). 

More generally, the order gives a filtration on the tensor algebra, whose associated graded is identified with the tensor algebra of the weighted normal bundle NZ _•_ . Hence every tensor field _ξ ∈_ ( _T_ X _[∨]_[)] _[⊗][n][ ⊗T]_ X _[⊗][m]_ has a leading term 

**==> picture [106 x 13] intentionally omitted <==**

Weighted blowups and 3d Poisson desingularizations 

11 

given by its projection to the associated graded. Moreover, lt( _ξ_ ) has the same symmetry properties as _ξ_ . For instance, if _ξ_ is totally (skew-)symmetric, then so is lt( _ξ_ ). In particular, the leading term of a polyvector is again a polyvector. 

_Example_ 2.12 (Whitney umbrellas, part 1) _._ In coordinates ( _x, y, z_ ), let _W_ = _x_[2] _− y_[2] _z ∈_ K[ _x, y, z_ ]. This is the polynomial whose vanishing locus is the Whitney umbrella. Let _µ_ = _∂x ∧ ∂y ∧ ∂z_ be the standard covolume and consider the bivector 

**==> picture [220 x 12] intentionally omitted <==**

Here [ _−, −_ ] denotes the Schouten bracket of polyvector fields, so that [ _µ, W_ ] = _ι_ d _W µ_ is the contraction. For an exponent sequence ( _a ≤ b ≤ c_ ), let Z _•_ ( _a, b, c_ ) be the centre defined by the weighted coordinates ( _x[a] , y[b] , z[c]_ ). Then we have 

ordZ _•_ ( _a,b,c_ )( _σ_ ) = ordZ _•_ ( _a,b,c_ )( _W_ ) + ordZ _•_ ( _a,b,c_ )( _∂x ∧ ∂y ∧ ∂z_ ) = ordZ _•_ ( _a,b,c_ )( _W_ ) _− κ_ 3 

where _κ_ 3 = _a_[1][+][1] _b_[+][1] _c_[is][the][third][weight][sum.] For instance, with respect to the unweighted centre Z _•_ := Z _•_ (1 _,_ 1 _,_ 1), we have 

**==> picture [228 x 28] intentionally omitted <==**

With respect to the centre Z _[′] •_[:=][ Z] _[•]_[(1] _[,]_[ 1] _[,][ ∞]_[),][i.e.][the][unweighted] _[z]_[-axis,][we][have] 

**==> picture [258 x 29] intentionally omitted <==**

**==> picture [313 x 46] intentionally omitted <==**

Note that for Z _[′] •_[and][Z] _[′′] •_[,][the][polynomial] _[W]_[and][the][trivector] _[∂][x][∧][∂][y][∧][∂][z]_[are] homogeneous; hence the leading terms have the same expression after replacing the coordinates ( _x, y, z_ ) with the corresponding coordinates ( ˙ _x, y,_ ˙ _z_ ˙) on the normal bundle. ♢ 

2.13. **Euler vector field.** The weighted normal bundle comes equipped with a canonical _**(weighted) Euler vector field**_ 

**==> picture [60 x 12] intentionally omitted <==**

which acts on a homogeneous element _h ∈_ gr _[I] λ[•][O]_[X][by] 

**==> picture [50 x 11] intentionally omitted <==**

Under the isomorphism (2.1), it is related to the corresponding vector field _E ∈_ H[0][�] _T_ NZ ~~_•_~~ � for the reduced weighting Z _•_[by] 

**==> picture [62 x 11] intentionally omitted <==**

Note that _E_ generates the action of Gm on NZ _•_ = _[∼]_ NZ ~~_•_~~[induced][by][the][integer] grading on _O_ NZ _•_[.] 

If ( _x[a]_ 1[1] _[, . . . , x] n[a][n]_[)][is][a][weighted][chart][for][Z] _[•]_[with][corresponding][weights] _[w][i]_[=] _a_ 1 _i_[,] the Euler vector field in these coordinates takes the form 

**==> picture [136 x 11] intentionally omitted <==**

12 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

2.14. **Degeneration to the weighted normal bundle.** Given a centre Z _•_ , the degeneration to the weighted normal bundle DegZ _•_ (X) is a Gm-equivariant family of orbifolds over A[1] , whose generic fibre is X and whose fibre over 0 _∈_ A[1] is the weighted normal bundle NZ _•_ . It can be constructed naturally and functorially as the relative spectrum of the extended Rees algebra, 

**==> picture [148 x 37] intentionally omitted <==**

where _I j_[=] _[ O]_[X][for] _[j][<]_[ 0][and] _[t]_[ is a formal variable corresponding to the coordinate] on A[1] ; see e.g. [LM23, §5.1]. The total space of DegZ _•_ (X), and its Gm-equivariant map to X _×_ A[1] , depend only on the underlying reduced centre Z _•_[.] 

The degeneration to the normal bundle fits into a Gm-equivariant commutative diagram 

**==> picture [170 x 46] intentionally omitted <==**

where X is equipped with the trivial action of Gm. It carries a centre DegZ _•_ (Z _•_ ) whose support is identified with supp(Z _•_ ) _×_ A[1] ; its generic fibre is Z _• ⊂_ X and its fibre over 0 _∈_ A[1] is the induced centre on the normal bundle NZ _•_ . 

In what follows, we will need the expression for these maps in local coordinates, as follows. Let ( _x[a]_ 1[1] _[, . . . , x] n[a][n]_[)][be][a][weighted][chart][for][Z] _[•]_[near][a][point] _[p][ ∈]_[supp][ Z] _[•]_[;] it gives corresponding coordinates ( _x_ 1 _, . . . , xn, t_ ) on X _×_ A[1] , where _t_ is the natural coordinate on A[1] . Then DegZ _•_ (X) carries a unique weighted chart (˜ _x[a]_ 1[1] _[, . . . ,]_[ ˜] _[x] n[a][n][,]_[ ˜] _[t]_[)] such that the map DegZ _•_ (X) _→_ X _×_ A[1] is given by 

**==> picture [239 x 29] intentionally omitted <==**

wewhereobtain _w_ is coordinatesthe reduced _x_ ˜weight _i|t_ ˜=0 whichsequenceare associatedidentified withto **w** =the **a**[1] coordinates[.][Specializing] _x_ ˙ _i_[to] on _[t]_[˜][ = 0] the normal bundle NZ _•_ , via the standard identification of the associated graded of a filtration with the specialization of its Rees algebra. 

The infinitesimal generator of the Gm action on DegZ _•_ (X) is then given by the vector field 

**==> picture [260 x 13] intentionally omitted <==**

which will be useful below. 

**==> picture [215 x 10] intentionally omitted <==**

**==> picture [156 x 11] intentionally omitted <==**

the open suborbifold on which the weighting of DegZ _•_ (X) is trivial. The _**weighted blowup of**_ X _**along**_ Z _•_ is the stack 

**==> picture [122 x 46] intentionally omitted <==**

**==> picture [288 x 12] intentionally omitted <==**

Weighted blowups and 3d Poisson desingularizations 

13 

called the _**blowdown**_ , which is an isomorphism away from Z _•_ . The _**exceptional divisor**_ E := _b[−]_[1] (supp Z _•_ ) is a hypersurface identified with the weighted projective bundle 

**==> picture [136 x 11] intentionally omitted <==**

We have the commutative diagram 

**==> picture [272 x 50] intentionally omitted <==**

where the vertical maps are quotients by free actions of Gm and the horizontal maps are embeddings of open dense suborbifolds. 

As for ordinary blowups, one can construct explicit charts on BlZ _•_ (X) by taking slices to the Gm-action, in which some coordinate is set equal to one; see e.g. [ATW24, §3.4]. However, such charts break the symmetry of the variables, which leads to cumbersome formulae for tensors. Hence, it will be simpler in what follows to use coordinates on DegZ _•_ (X), and remember the Gm-action, i.e. to work with the Gm-invariant map _b ◦ π_ : DegZ _•_ (X) _[◦] →_ X. Then, given weighted coordinates ( _x[a]_ 1[1] _[, . . . , x] n[a][n]_[)][on][X][,][the][blowdown][is][obtained][locally][by][descending][the] Gm-invariant map 

**==> picture [220 x 12] intentionally omitted <==**

to the quotient, recalling that in DegZ _•_ (X) _[◦]_ , the coordinates _x_ ˜ _i_ of positive weight are never all simultaneously equal to zero. The exceptional divisor E is then given by the equation _t_ = 0. 

## 3. Blowups of polyvector fields 

In this section, we give necessary and sufficient conditions for a polyvector field to lift to a weighted blowup. 

3.1. **Quotients by** Gm **.** Since the construction of the blowup involves a quotient by Gm, it will be useful to recall the behaviour of polyvectors under such actions. 

Let X be an orbifold, equipped with an action of the multiplicative group Gm, and let 

**==> picture [48 x 12] intentionally omitted <==**

be the infinitesimal generator of the action. We assume that the action is locally free, i.e. _ν_ is non-vanishing, or equivalently the stabilizers of the action are finite. This means that the quotient [X _/_ Gm] is again an orbifold. Note that the relative tangent bundle of the quotient map _q_ : X _→_ [X _/_ Gm] is generated by _ν_ . Hence we have an exact sequence 

**==> picture [206 x 12] intentionally omitted <==**

whose exterior powers give exact sequences 

**==> picture [308 x 15] intentionally omitted <==**

where the inclusion takes a _j_ -vector _ξ_ on [X _/_ Gm], and sends it to _ν ∧ ξ_[˜] , where _ξ_[˜] is any lift of _ξ_ to a _j_ -vector on X; the result is well-defined because wedging with _ν_ annihilates the tangent spaces of the orbits. 

14 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

Taking Gm-invariants, we obtain the following: 

**Lemma 3.1.** _The exact sequence_ (3.1) _gives an injection_ 

**==> picture [137 x 21] intentionally omitted <==**

_identifying the space of global j-vector fields on_ [X _/_ Gm] _with the space of_ Gm _- invariant_ ( _j_ + 1) _-vector fields on_ X _that are locally of the form ν ∧ η for some j-vector η ∈ X_ X _[j][.]_ 

3.2. **Pushing forward.** Let Z _•_ be a weighted centre on X, and let _b_ : BlZ _•_ (X) _→_ X be the associated blowdown map. A polyvector field _ξ_ on BlZ _•_ (X) can always by pushed forward to X. Namely, the blowdown map _b_ : BlZ _•_ (X) _→_ X is an isomorphism away from a subvariety of X of codimension at least two; hence any tensor on BlZ _•_ (X) can be passed through this isomorphism, and then extended to all of X by normality (Hartogs’ phenomenon). This give a natural injection 

**==> picture [246 x 18] intentionally omitted <==**

compatible with the wedge product and Schouten bracket, i.e. it is a morphism of Gerstenhaber algebras. 

3.3. **Pulling back.** We can also pull back polyvectors along the blowdown map _b_ : BlZ _•_ (X) _→_ X, but this may introduce poles. Namely, over the complement X _\_ Z _•_ , the map _b_ is an isomorphism. Hence if _ξ ∈_ H[0] ( _X_ X _[•]_[)][we][have][a][well-defined] pullback _b[∗] ξ_ which is regular on BlZ _•_ (X) _\_ E but may have a pole on E, where E = _b[−]_[1] (supp Z _•_ ) is the exceptional divisor. 

**Definition 3.2.** We say that a polyvector field _ξ ∈_ H[0] ( _X_ X _[•]_[)] _**[lifts][to][the][blowup]**_ if _b[∗] ξ_ extends to a polyvector field on BlZ _•_ (X), i.e. it has no poles on E, so that we may view it as an element 

**==> picture [86 x 19] intentionally omitted <==**

The following gives necessary and sufficient conditions for a polyvector field to lift to the blowup. 

**Theorem 3.3.** _Let_ X _be an orbifold, let_ Z _• be a regular weighted centre on_ X _and let ξ ∈_ H[0][�] _X_ X _[k]_ � _be a polyvector field of degree k ≥_ 0 _. Then ξ lifts to the blowup_ BlZ _•_ (X) _if and only if the following conditions are satisfied_ 

- (1) ordZ _•_ ( _ξ_ ) _≥−_ gcd **w** _, and_ 

- (2) ordNZ _•_ (lt( _ξ_ ) _∧ E_ ) _≥_ 0 _, where E ∈_ H[0] ( _T_ NZ _•_ ) _is the weighted Euler vector field._ 

_In this case, ξ is tangent to_ Z _λ for all λ. Moreover, b[∗] ξ is tangent to the exceptional divisor if and only if_ ordZ _• ξ ≥_ 0 _._ 

Before proving the theorem we note a convenient reformulation: 

_Remark_ 3.4 _._ Following [LM23, §5.4], we say that a vector field _ϵ ∈T_ X is _**Euler-like**_ if its leading term is the Euler-vector field: lt( _ϵ_ ) = _E_ . Condition (2) in the theorem can then be replaced with the equivalent condition 

- (2 _[′]_ ) ordZ _•_ ( _ϵ ∧ ξ_ ) _≥_ 0 for some Euler-like vector field _ϵ_ . 

Weighted blowups and 3d Poisson desingularizations 

15 

This form is less natural since it depends on the choice of _ϵ_ , but it is more useful in practice since all calculations can be performed in charts on X without explicit mention of the normal bundle. ♢ 

_Proof of Theorem 3.3._ By rescaling the weights, we may assume without loss of generality that the centre is reduced, i.e. gcd **w** = 1. We will use the presentation of BlZ _•_ (X) as the Gm-quotient of DegZ _•_ (X) _[◦]_ . 

Since the problem is ´etale local in X, we can work in a weighted chart ( _x[a]_ 1[1] _[, . . . , x] n[a][n]_[)] with induced coordinates (˜ _x[a]_ 1[1] _[, . . . ,]_[ ˜] _[x] n[a][n][,]_[ ˜] _[t]_[)][on][Deg] Z _•_[(][X][),][so][that][the][G][m][-action][is] generated by _E_[˜] = _t∂_[˜] _t_ ˜ _− w_ ~~1~~ _[x]_[˜][1] _[∂][x]_[˜] 1 _[−· · · −][w]_ ~~_n_~~ _[x]_[˜] _[n][∂][x]_[˜] _n_[and][the][blowdown][map][is][repre-] sented by the Gm-invariant map 

**==> picture [258 x 12] intentionally omitted <==**

Applying Lemma 3.1 with _ν_ = _E_[˜] , we identify the pullback _b[∗] ξ_ of _ξ ∈ X_ X _[k]_[with][the] polyvector 

**==> picture [78 x 17] intentionally omitted <==**

where _ξ_[˜] denotes any lift of _ξ_ along the map (3.3); the result is independent of the choice of _ξ_[˜] . Note, in particular, that we may take 

**==> picture [64 x 14] intentionally omitted <==**

for all _i_ . Moreover, if _f ∈O_ X we have _f_[˜] = _t_[˜][ord(] _[f]_[)] _g_ for a regular function _g_ that is not divisible by _t_ ; its restriction to _t_ = 0 corresponds to the leading term lt( _f_ ). 

Let us write _ξ_ =[�] _ξ[I] ∂xI_ with _ξ[I] ∈O_ X, where the sum is over multi-indices _I_ = ( _i_ 1 _, . . . , ik_ ). Then we have 

**==> picture [314 x 49] intentionally omitted <==**

where the functions _g[I]_ = _t_[˜] _[−]_[ord(] _[ξ][I]_[)][ ˜] _ξ[I]_ are regular and not divisible by _t_ , and _E_ = � _wixi∂xi_ . The conditions (1) and (2) now translate into the condition that the two sums in (3.4) have no poles on the exceptional divisor _t_ = 0, i.e. that _ξ_ lifts to the blowup. 

Note that _b[∗] ξ_ is tangent to the exceptional divisor if and only if _E_[˜] _∧ ξ_[˜] is tangent to the weighted normal bundle, given by the equation _t_[˜] = 0. This, in turn, is equivalent to the first sum in (3.4) being divisible by _t_ , i.e. that ord( _ξ_ ) _≥_ 0. 

Finally for the statement that _ξ_ is tangent to Z _•_ , note that since ord _ξ ≥−_ 1, we have ord( _ι_ d _xiξ_ ) _≥ wi −_ 1. We must show that if _wi >_ 0, then _ι_ d _xiξ ∈IwiX_ X _[k][−]_[1] . Note that the Koszul complex ( _X_ X _[•][,]_[ �] _j[w][j][x][j][∂][x] j[∧−]_[) decomposes as a tensor prod-] uct of the polyvectors on supp Z _•_ (i.e. the zero-weight directions, for which the differential is zero) and the polyvectors in the normal direction (i.e. the positive weight directions, for which the Koszul differential is exact). Hence we may write 

**==> picture [104 x 24] intentionally omitted <==**

for some polyvectors _η_ and _µ_ with ord _η ≥−_ 1 and ord _µ ≥_ 0. Therefore 

**==> picture [190 x 23] intentionally omitted <==**

16 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

We claim that every term on the right-hand side lies in _IwiX_ X _[•]_[.][Indeed,][for][the] term _wixiη_ , this is obvious. Meanwhile, for the terms _wjxj∂xj ∧ ι_ d _xiη_ , we may assume _wj >_ 0. Since the centre is assumed reduced, _wj_ is an integer, and hence _wj ≥_ 1. Since _ι_ d _xiη_ has weighted order at least _wi −_ 1, it lies in _Iwi−_ 1 _X_ X _[•]_[,][so][that] _wjxj∂xj ∧ ι_ d _xiη ∈Iwj_ + _wi−_ 1 _X_ X _[•][⊂I][w] i[X]_ X _[•]_[,][as][desired.][Finally,][since][ord] _[µ][ ≥]_[0,][the] term _ι_ d _xiµ_ has weighted order at least _wi_ and therefore also lies in _IwiX_ X _[•]_[.] □ 

## 4. Blowups of Poisson structures 

4.1. **Poisson structure on orbifolds.** Recall that a _**Poisson structure**_ on an orbifold X is a Poisson bracket on the ´etale structure sheaf 

_{−, −}_ : _O_ X _× O_ X _→O_ X _,_ 

or equivalently a global bivector 

**==> picture [56 x 13] intentionally omitted <==**

such that 

**==> picture [90 x 13] intentionally omitted <==**

4.2. **Poisson structures and weighted centres.** A Poisson structure may interact with a weighted centre in many different ways. 

**Definition 4.1.** Let (X _, σ_ ) be a Poisson orbifold, and let Z _•_ be a centre on X. 

- (1) Z _•_ is _**Poisson**_ if _σ_ is tangent to Z _λ_ for all _λ >_ 0. 

(2) Z _•_ is _**codegenerate**_ if ordZ _•_ ( _σ_ ) _≥−_ gcd **w** and ordZ _•_ (lt( _σ_ ) _∧ E_ ) _≥_ 0. (3) Z _•_ is _**conilpotent**_ if ordZ _•_ ( _σ_ ) _≥_ 0. 

_Remark_ 4.2 _._ If Z _•_ is a Poisson centre, then the Poisson bracket induces a Lie bracket on the sheaf _I>_ 0. Then Z _•_ is conilpotent if and only if the sheaf of Lie algebras _I>_ 0 is topologically nilpotent with respect to the filtration, i.e. lim _n→∞_ (ad _f_ ) _[n]_ = 0 for every _f ∈I>_ 0, where ad _f_ := _{f, −}_ is the adjoint action by the Poisson bracket, and the limit is taken in the adic topology. This is the reason for our choice of terminology. For unweighted centres, conilpotence is equivalent to the stronger condition that the conormal Lie algebra _N_ supp _[∨]_ Z _•_[=] _[ I][>]_[0] _[/][I] >_[2] 0[is abelian; such centres] were called coabelian in [LP24]. The term “codegenerate” is chosen due to its relation, in the unweighted case, with the degeneracy of the conormal Lie algebra introduced by Polishchuk [Pol97, §8]; see Example 4.5 below. ♢ 

Since the condition [ _σ, σ_ ] = 0 for a bivector to be Poisson is closed, it is unaffected by birational transformations, so that Theorem 3.3 immediately gives the following result. For unweighted centres, this recovers results of Polishchuk [Pol97, §8]; see Example 4.5 below. 

**Corollary 4.3.** _Let_ (X _, σ_ ) _be a Poisson orbifold, and let_ Z _• be a weighted centre on_ X _. Then the following statements hold:_ 

- (1) _σ lifts to the blowup_ BlZ _•_ (X) _if and only if_ Z _• is codegenerate._ 

- (2) _In this case,_ Z _• is Poisson, and the lift b[∗] σ is tangent to the exceptional divisor if and only if_ Z _• is conilpotent._ 

Note that the conditions in Definition 4.1 are local, and can therefore be checked in coordinates, as follows. Suppose that Z _•_ is defined by a chart ( _x[a]_ 1[1] _[, . . . , x][a] k[k]_[) with] corresponding weights _wi_ = _a_ 1 _i_[,][and][let] _[{][x][i][, x][j][}]_[=] _[σ]_[(d] _[x][i][∧]_[d] _[x][j]_[)][for] _[i][<][j]_[be][the] Poisson brackets of the coordinate functions. Then we have the following: 

Weighted blowups and 3d Poisson desingularizations 

17 

(1) Z _•_ is Poisson if and only if 

**==> picture [227 x 12] intentionally omitted <==**

for all _i < j_ . 

(2) Z _•_ is codegenerate if and only if 

**==> picture [232 x 12] intentionally omitted <==**

for all _i < j_ , and 

**==> picture [325 x 28] intentionally omitted <==**

(3) _I•_ is conilpotent if and only if 

**==> picture [218 x 12] intentionally omitted <==**

for all _i < j_ . 

Note that by Corollary 4.3, we have the following implications: 

Z _•_ is conilpotent = _⇒_ Z _•_ is codegenerate = _⇒_ Z _•_ is Poisson 

In general, the converses do not hold. However, for centres of codimension two, the codegeneracy condition simplifies: 

**Lemma 4.4.** _Let_ Z _• be a codimension-two centre in_ (X _, σ_ ) _. Then_ Z _• is codegenerate if and only if it is Poisson, and_ ordZ _• σ ≥−_ gcd **w** _._ 

_Proof._ Working in coordinates as above, we must show that if the codimension is two, the conditions (P) and (CD1) imply (CD2). In fact, we claim that a stronger statement is true: we have _wixi{xj, xk} ∈Iwi_ + _wj_ + _wk_ for any triple of distinct indices _i, j, k_ . Indeed, if _wi_ = 0, this is immediate, so assume that _wi_ = 0. Then, since codim Z _•_ = 2, at most one of _wj_ and _wk_ is nonzero. We therefore have max( _wj, wk_ ) = _wj_ + _wk_ . Therefore (P) implies that _{xj, xk} ∈Iwj_ + _wk_ , so that _wixj{xj, xk} ∈Iwi_ + _wj_ + _wk_ , as desired. □ 

4.3. **Examples.** We now give several examples in which the conditions of Corollary 4.3 can be described more explicitly. 

_Example_ 4.5 (Unweighted blowups) _._ For unweighted blowups, Corollary 4.3 recovers a result of Polishchuk [Pol97, §8], as follows; see also [Sch25] for a more differential-geometric approach. 

Suppose that Z _•_ is an unweighted centre supported on a smooth closed subvariety Z that is Poisson for _σ_ . Then the linearization of _σ_ along Z defines a _O_ Z-linear Lie bracket on the conormal sheaf _N_ Z _[∨]_[.][It][is][straightforward][to][check][that][we][have] ordZ( _σ_ ) _≥_ 0 (i.e. Z is conilpotent) if and only if the Lie bracket on _N_ Z _[∨]_[is][abelian.] Meanwhile, ord( _E ∧_ lt( _σ_ )) _≥_ 0 (i.e. Z is codegenerate) if and only if the Lie algebra is degenerate in the sense of _op. cit._ ♢ 

_Example_ 4.6 (Surfaces) _._ Let X = A[2] with coordinates _x, y_ . Then a general Poisson structure on X has the form _σ_ = _f_ ( _x, y_ ) _∂x ∧ ∂y_ where _f ∈O_ (X). Let Z _•_ = Z ~~_•_~~ be a reduced centre supported at a point _p ∈_ X, with weight sequence **w** , so that gcd **w** = 1. We have 

**==> picture [229 x 11] intentionally omitted <==**

18 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

where _κ_ 2 = _w_ 1 + _w_ 2 is the second weight sum. Moreover, _E ∧_ lt( _σ_ ) = 0 for degree reasons. Hence Z _•_ is codegenerate if and only if ordZ _•_ ( _f_ ) _≥ κ_ 2 _−_ 1, and Z _•_ is conilpotent if and only if ordZ _•_ ( _f_ ) _≥ κ_ 2. 

In particular, if Y = V( _f_ ) and Z _•_ is unweighted, we have **w** = (1 _,_ 1) so that _κ_ 2 = 2. Hence the codegeneracy condition reduces to the condition ord _p_ ( _f_ ) _≥_ 1, i.e. _p ∈_ Y, and the conilpotence condition reduces to the condition that ord _p_ ( _f_ ) _≥_ 2, i.e. _p_ is a singular point of Y. ♢ 

_Example_ 4.7 (Jacobian Poisson structures) _._ Recall that if _f_ ( _x, y, z_ ) is a function on A[3] , its _**Jacobian Poisson structure**_ is defined by 

**==> picture [251 x 11] intentionally omitted <==**

Let _E_ be the Euler vector field of a centre Z _•_ for which ordZ _•_ ( _f_ ) _>_ 0. Then ordZ _•_ ( _f_ ) = ordZ _• E_ ( _f_ ), and we have 

**==> picture [113 x 11] intentionally omitted <==**

so that 

ordZ _•_ ( _σ_ ) = ordZ _•_ ( _E ∧ σ_ ) = ordZ _•_ ( _f_ ) _− κ_ 3 _._ 

Thus Z _•_ is conilpotent if and only if it is codegenerate, which in turn is equivalent to the condition ordZ _• f ≥ κ_ 3. ♢ 

_Example_ 4.8 (Whitney umbrellas, part 2) _._ As a special case of the previous example, consider the Jacobian Poisson structure associated to the Whitney umbrella _W_ = _x_[2] _− y_[2] _z_ , which was studied in Example 2.12. The calculations there imply via Example 4.7 that the centre ( _x_[1] _, y_[1] _, z[∞]_ ) corresponding to the _z_ -axis is conilpotent, but neither of the centres ( _x_[1] _, y_[1] _, z_[1] ) nor ( _x_[2] _, y_[3] _, z_[3] ) is even codegenerate. ♢ 

_Example_ 4.9 (The product of a log symplectic surface and a line) _._ Let X = A[3] with coordinates ( _x, y, z_ ). Consider the linear Poisson structure 

**==> picture [60 x 11] intentionally omitted <==**

which is independent of _z_ . We claim that there does not exist any centre of dimension zero that is codegenerate for _σ_ . In particular, there are no conilpotent centres of dimension zero. 

Indeed, suppose that Z _•_ is a Poisson centre of dimension zero. Then Z _•_ is necessarily contained in the vanishing locus of _σ_ , which is the _yz_ -plane W = V( _x_ ). By translation, we may assume without loss of generality that Z _•_ is supported at the origin. 

Let _E_ denote a weighted Euler vector for Z _•_ . We have 

**==> picture [120 x 12] intentionally omitted <==**

and therefore 

**==> picture [178 x 11] intentionally omitted <==**

where we have used that ordZ _•_ ( _E_ ( _z_ )) = ordZ _•_ ( _z_ ). Now note that since d _x_ and d _z_ are linearly independent, the sum of their orders is at most _w_ 1 + _w_ 2 = _κ_ 2. Therefore 

**==> picture [154 x 11] intentionally omitted <==**

where the final inequality follows from the fact that Z _•_ has codimension three. This shows that Z _•_ is not codegenerate, as claimed. ♢ 

Weighted blowups and 3d Poisson desingularizations 

19 

## 5. Weighted normal forms of Poisson structures 

In what follows, we shall need some results on formal normal forms for Poisson structures in weighted charts. If _p ∈_ X is a point in an orbifold, then its formal neighbourhood is described as the completion of the local ring _O_ X _,p_ , which is isomorphic to an algebra of formal power series. Hence we work throughout this section with the latter. 

5.1. **Formal vector fields and automorphisms.** For a fixed integer _n ≥_ 0, let us denote by 

� _O_ := K[[ _x_ 1 _, . . . , xn_ ]] 

the ring of power series in _n_ variables, viewed as a complete local ring with maximal ideal 

**==> picture [78 x 11] intentionally omitted <==**

We denote by 

**==> picture [103 x 14] intentionally omitted <==**

the module of derivations (formal vector fields) and by 

**==> picture [55 x 16] intentionally omitted <==**

the formal polyvectors. 

Note that m _T_[�] is the Lie algebra of formal vector fields “vanishing at the origin”, and 

**==> picture [90 x 19] intentionally omitted <==**

is the group of continuous automorphisms of _O_[�] . Taking the derivative (Jacobian � matrix) at the origin gives a homomorphism from Aut _O_ to GL _n_ (K), fitting into � � a short exact sequence 

**==> picture [254 x 19] intentionally omitted <==**

� where Aut _O_[is][the][subgroup][of][automorphisms][that][are] _**[tangent]**_ � �0[= exp(][m][2][ �] _[T]_[ )] _**to the identity**_ . 

5.2. **Formal centres.** The basic constructions involving centres from Section 2 work equally well for formal powers series. 

**Definition 5.1.** A _**formal centre**_ is a centre Z _•_ on the formal spectrum Spf( _O_[�] ), i.e. a filtration of _O_[�] by ideals, defined by assigning weights to the variables _x_ 1 _, . . . , xn_ . 

Fix now a formal centre Z _•_ defined by formal weighted coordinates ( _x[a]_ 1[1] _[, . . . , x] n[a][n]_[),] and let 

**==> picture [104 x 19] intentionally omitted <==**

denote the subgroup of automorphisms that preserve Z _•_ and act as the identity on � the associated graded (the weighted normal bundle). Equivalently, Aut _O,_ Z _•_ is � � the subgroup obtained be exponentiating the action of the Lie subalgebra of m _T_[�] consisting of vector fields whose weighted order is strictly positive. 

20 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

**Lemma 5.2.** _If an <_ 2 _a_ 1 _(or equivalently_ 2 _wn > w_ 1 _), then every automorphism_ � _tangent to the identity lies in_ Aut _O,_ Z _• , i.e._ � � 

**==> picture [108 x 19] intentionally omitted <==**

_Proof._ We have ordZ _•_ (m) = ordZ _•_ ( _xn_ ) = _wn_ = _a_ 1 _n_[and][ord(] _[T]_[�][ )][=] _[−][κ]_[1][=] _[−][w]_[1][=] _− a_[1] 1[.][Therefore][ord][Z] _[•]_[(][m][2][ �] _[T]_[ ) = 2] _[w][n][ −][w]_[1][=] _a_ 2 _n[−] a_[1] 1 _[>]_[ 0][and][hence][the][Lie][algebra] � � m[2][ �] _T_ of Aut0 _O_ is contained in the Lie algebra of Aut _O,_ Z _•_ . The result follows � � � � by exponentiation. □ 

5.3. **Normal forms from leading terms.** In this subsection we fix a formal centre Z _•_ given by ( _x[a]_ 1[1] _[, x][a]_ 2[2] _[, . . .]_[).][We][will][be][interested][in][the][following:] 

**Definition 5.3.** A _**formal Poisson structure**_ is an element _σ ∈ X_[�][2] such that [ _σ, σ_ ] = 0. Two formal Poisson structures _σ_ and _σ[′]_ are _**equivalent**_ (relative to Z _•_ ) � if there exists an element _ϕ ∈_ Aut _O,_ Z _•_ such that _ϕ · σ_ = _σ[′]_ . � � 

� Note that the action of Aut _O,_ Z _•_ fixes the leading terms, i.e. : � � 

**==> picture [202 x 11] intentionally omitted <==**

Moreover, if we equip _O_[�] with the _grading_ defined by the weighted coordinates ( _x[a]_ 1[1] _[, . . . , x] n[a][n]_[),][rather][than][just][the][filtration,][we][obtain][an][identification] _O_[�] = _[∼]_ gr� _O_[�] , so that the leading term may be viewed as a formal Poisson structure on _O_ that is quasi-homogeneous with respect to the grading. Hence to classify formal Poisson structures up to equivalence, we may fix a quasihomogeneous formal Poisson structure _σ_ 0 _∈ X_[�][2] 

and look at Poisson structures of the form 

**==> picture [50 x 9] intentionally omitted <==**

where _η ∈ X_[�][2] is a bivector of order ordZ _• η >_ ordZ _• σ_ 0. We can then view _η_ as a small perturbation of _σ_ 0, where “small” means “of higher order in the filtration”, and try to simplify _η_ at higher and higher order in the filtration; see, e.g. [DZ05, §2.2]. 

This simplification process can be packaged concisely using the formalism of deformation theory via differential graded Lie algebras, as follows. We will assume some familiarity with this technique; see e.g. [Man22, §5.6 and §6.3] for a recent treatment of the relevant definitions. 

As observed by Lichnerowicz [Lic77], the operation _δ_ := [ _σ_ 0 _, −_ ] defines a differential on _X_[�] _[•]_ , which together with the Schouten bracket and the wedge product, makes _X_ X _[•]_[into][differential][graded][(dg)][Gerstenhaber][algebra.][In][particular,][the] shift _X_ X _[•]_[[1] is a differential graded Lie algebra with respect to the Schouten bracket.] Given a homogeneous formal Poisson structure _σ_ 0 and a formal centre Z _•_ as above, we define a graded subspace 

**==> picture [106 x 14] intentionally omitted <==**

Weighted blowups and 3d Poisson desingularizations 

21 

concentrated in non-negative degrees, by taking 

**==> picture [230 x 20] intentionally omitted <==**

In particular: 

� _•_ g[0] is the set of positive-weight vector fields, so that Aut _O,_ Z _•_ = exp(g[0] ). � � _•_ g[1] is the space of bivector fields _η ∈ X_[�][2] such ordZ _•_ ( _η_ ) _>_ ordZ _•_ ( _σ_ 0). Since the Schouten bracket is homogeneous of order zero, g _[•]_ is preserved by differential and bracket, i.e. the triple (g _[•] , δ,_ [ _−, −_ ]) is a differential graded Lie subalgebra of _X_ X _[•]_[[1].][Note][that][g][is][complete][with][respect][to][the][filtration][induced][by][the] centre. 

An element _η ∈_ g[1] satisfies the Maurer–Cartan equation _δη_ +[1] 2[[] _[η, η]_[] = 0][if][and] only if _σ_ 0 + _η_ is a Poisson structure. Hence the Maurer–Cartan elements of the dg Lie algebra g _[•]_ are in bijection with formal Poisson structures whose leading term is _σ_ 0. Meanwhile, the gauge action of g[0] on Maurer–Cartan elements integrates to the � natural action of Aut _O,_ Z _•_ on Poisson structures. We thus have the following � � **Lemma 5.4.** _The set of gauge equivalence classes of Maurer–Cartan elements of_ � g _[•]_ ( _σ_ 0 _,_ Z _•_ ) _is in canonical bijection with the set of_ Aut _O,_ Z _• -orbits of formal_ � � _Poisson structures whose leading term is σ_ 0 _._ 

We will produce normal forms of formal Poisson structures by identifying subspaces of g _[•]_ = g _[•]_ ( _σ_ 0 _,_ Z _•_ ) that generate all of the gauge equivalence classes. To this end, we will apply the following fundamental result of derived deformation theory from [DR15, §3.2]; see [Man22, Theorem 6.4.4] for a variant in the language of deformation functors. 

**Theorem 5.5** ([DR15, §3.2]) **.** _Let ϕ_ : h _→_ g _be a morphism of complete filtered differential graded Lie algebras, and let_ gr _ϕ_ : gr h _→_ gr g _be the induced map on the associated graded complexes. If_ H[1] (gr _ϕ_ ) : H[1] (gr h) _→_ H[1] (gr g) _is surjective, and_ H[2] (gr _ϕ_ ) : H[2] (gr h) _→_ H[2] (gr g) _is injective, then every Maurer–Cartan element of_ g _is equivalent to one lying in the image of ϕ._ 

_Remark_ 5.6 _._ The version of Theorem 5.5 stated explicitly in [DR15, §3.2] has a stronger hypothesis, namely that _ϕ_ is a filtered quasi-isomorphism, but an inspection of the proof reveals that it uses only the weaker hypotheses stated here. In particular, the surjectivity of H[1] (gr _ϕ_ ) : H[1] (gr h) _→_ H[1] (gr g) is used to justify [DR15, Eq. (3.62), (3.63)], and injectivity of H[2] (gr _ϕ_ ) : H[2] (gr h) _→_ H[2] (gr g) is used in the last step of the proof of [DR15, Claim 3.5]. Note that the grading used in their paper is shifted by _−_ 1 from the one in use here. ♢ 

5.4. **Some normal forms in dimension three.** We now use this formalism to produce some normal forms in dimension _n_ = 3, i.e. for formal Poisson structures on K[[ _x, y, z_ ]]. These results will be used to establish our results on resolution of singularities later in the paper. 

The first normal form concerns Poisson structures with certain specified linearizations; this corresponds to the case in which the centre Z _•_ has all weights equal to one, and the leading term has order _−_ 1. We make use of the calculation of the Poisson cohomology of three-dimensional linear Poisson structures in [HZ23, Theorem 2.1]. 

22 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

**Proposition 5.7.** _Let σ be a formal Poisson structure on_ K[[ _x, y, z_ ]] _and let_ Z _• be the unweighted centre defined by_ ( _x, y, z_ ) _. Let σ_ 0 = lt( _σ_ ) _be the leading term._ 

(1) _If_ 

**==> picture [64 x 11] intentionally omitted <==**

_then either σ_ = _σ_ 0 _, or σ is equivalent to_ 

**==> picture [109 x 25] intentionally omitted <==**

_for some λ ∈_ K _and k >_ 0 _._ 

(2) _If_ 

**==> picture [61 x 11] intentionally omitted <==**

_then there exists a series f ∈_ K[[ _y, z_ ]] _and series_ 

**==> picture [226 x 12] intentionally omitted <==**

_such that σ is equivalent to_ 

**==> picture [178 x 11] intentionally omitted <==**

_Moreover, the equivalences in (1) and (2) can be given by automorphisms tangent to the identity at the origin._ 

_Proof._ **Case one:** Suppose that _σ_ 0 = _x∂x ∧ ∂y_ . This is the product of the _z_ - axis with the zero Poisson structure, whose Poisson cohomology is K[[ _z_ ]] _⟨∂z⟩_ , and the ( _x, y_ )-plane with structure induced by _σ_ 0, whose Poisson cohomology is well known to be given by K _⟨∂y⟩_ , where _⟨−⟩_ denote the exterior algebra with the given generator (see, e.g., [DZ05, Example 2.5.15]). By the K¨unneth formula, the natural map 

(K[[ _z_ ]] _⟨∂y, ∂z⟩ ,_ d = 0) _→_ ( _X_[�] _[•] , δ_ ) 

is a quasi-isomorphism; it evidently respects the Schouten bracket and the grading by the unweighted order. Hence its intersection with g( _σ_ 0 _,_ Z _•_ ) defines a dg Lie subalgebra h _[•]_ := ( _z_[2] K[[ _z_ ]] _⟨∂y, ∂z⟩_ )[1] _<_ g( _σ_ 0 _,_ Z _•_ ), to which we may apply Theorem 5.5. We deduce that every Maurer–Cartan element is gauge equivalent to one of the form _g_ ( _z_ ) _∂z ∧ ∂y_ for some _g ∈ z_[2] K[[ _z_ ]]; put differently, _σ_ is equivalent to _x∂x ∧ ∂y_ + _g_ ( _z_ ) _∂z ∧ ∂y_ . But it is well known (see e.g. [BT77, Corollary 2] or [GGJ04, Theorem 1.1(c)]) that by a formal change of coordinates involving _z_ only, any nonzero one-dimensional vector field _g_ ( _z_ ) _∂z_ vanishing to order at least two at _z[k]_[+1] the origin can be reduced to the normal form 1+ _λz[k][∂][z]_[for][some] _[k][>]_[0][and] _[λ][∈]_[K][,] giving the desired result. 

**Case two:** Suppose _σ_ 0 = _x∂y ∧ ∂z_ . Let u _[j]_ = ( _y, z_ ) _[j]_ K[[ _y, z_ ]] be the ideal of functions vanishing to order _j_ at the origin in _y, z_ , and define subspaces 

**==> picture [174 x 12] intentionally omitted <==**

and 

**==> picture [111 x 13] intentionally omitted <==**

and let h _[j]_ = 0 for _j_ = 1 _,_ 2. We claim that h _[•] ⊂_ g _[•]_ is a dg Lie subalgebra with trivial differential, and that gr h _[•]_ projects isomorphically to the cohomology of gr g _[•]_ in degrees 1 and 2. Indeed, this follows from [HZ23, Theorem 2.1], with the following small modifications: 1) our coordinates differ from those in _op. cit._ by the cyclic permutation ( _x, y, z_ ) _�→_ ( _z, x, y_ ); 2) we use different (but cohomologous) formulae for the 2-cocycles; 3) we work with formal power series instead of smooth 

Weighted blowups and 3d Poisson desingularizations 

23 

� functions; 4) we only consider cocycles that lie in the subspace g _⊂ X[•]_ picked out by the order conditions defining g; and 5) we observe that the isomorphism is compatible with gradings. The calculations giving the proof are the same. 

By Theorem 5.5, we may assume without loss of generality that _σ_ = _σ_ 0 + _η_ where _η ∈_ h[1] , i.e. 

_σ_ = ( _x_ + _g_ ) _∂y ∧ ∂z_ + [ _∂x ∧ ∂y ∧ ∂z, h_ ] 

where _g ∈_ u[2] and _h ∈_ u[3] . Moreover, the integrability condition [ _σ, σ_ ] = 0 is easily seen to be equivalent to the condition that d _g ∧_ d _h_ = 0. It then follows from [MM80, p. 472, Th´eor`eme de factorisation] that there exists a function _f ∈_ K[[ _y, z_ ]] such that _g_ = _A_ ( _f_ ) and _h_ = _B_ ( _f_ ) for some functions _A, B ∈ f_ K[[ _f_ ]], as desired. □ 

Our next result continues our study of the Whitney umbrella from Examples 2.12 and 4.8, and makes use of all three of the weightings we considered there at different stages of the proof. 

**Proposition 5.8** (Whitney umbrellas, part 3) **.** _Let_ Z _• be the centre defined by the weighted coordinates_ ( _x_[2] _, y_[3] _, z_[3] ) _, and let W_ = _x_[2] _− y_[2] _z be the equation for the Whitney umbrella. Let σ be a formal Poisson structure with the following properties_ 

(1) _The leading term_ ltZ _•_ ( _σ_ ) _is equal to the Jacobian structure_ 

**==> picture [270 x 12] intentionally omitted <==**

(2) _The vanishing locus_ V( _σ_ ) _is non-isolated._ 

_Then there exists a continuous automorphism of_ K[[ _x, y, z_ ]] _taking σ to a Poisson structure of the form_ 

**==> picture [112 x 11] intentionally omitted <==**

_for some A ∈_ K[[ _W_ ]] _and some invertible element u ∈_ K[[ _x, y, z_ ]] _[×] ._ 

_Proof._ The weights of the centre ( _x_[2] _, y_[3] _, z_[3] ) are 

**==> picture [106 x 13] intentionally omitted <==**

Note that the linearization of the leading term _σ_ 0 is 2 _x∂y ∧ ∂z_ . It has order _w_ 1 _− w_ 2 _− w_ 3, and since _w_ 1 _> w_ 2 = _w_ 3, all other linear bivectors have strictly lower order. Hence, the linearization of _σ_ itself is also 2 _x∂y ∧ ∂z_ . 

By Proposition 5.7, there is an automorphism tangent to the identity that takes _σ_ to 

_σ[′]_ := (2 _x_ + _A_ ( _f_ )) _∂y ∧∂z_ +[ _∂x ∧∂y ∧∂z, B_ ( _f_ )] = [ _∂x ∧∂y ∧∂z, x_[2] + _B_ ( _f_ )]+ _A_ ( _f_ ) _∂y ∧∂z_ 

for some _f ∈_ K[[ _y, z_ ]] and _A_ ( _f_ ) _, B_ ( _f_ ) _∈ f_ K[[ _f_ ]] with _A_ ( _f_ ) _∈_ ( _y, z_ )[2] and _B_ ( _f_ ) _∈_ ( _y, z_ )[3] . Since _a_ 3 = 3 _<_ 4 = 2 _a_ 1, Lemma 5.2 ensures that this transformation preserves the centre ( _x_[2] _, y_[3] _, z_[3] ). Comparing the leading terms of _σ[′]_ and _σ_ , we see that after a linear change of variables in _y, z_ (which automatically respects the centre), we must have 

lt( _B_ ( _f_ )) = _−y_[2] _z._ 

Since this monomial has a reduced factor, _B_ ( _f_ ) must also; hence we have _B_ ( _f_ ) = _f B_[˜] ( _f_ ) for a unit _B_[˜] _∈_ K[[ _f_ ]] _[×]_ . Thus, by redefining _f_ , we may assume without loss of generality that _B_ ( _f_ ) = _f_ , and 

_σ_ = (2 _x_ + _A_ ( _f_ )) _∂y ∧ ∂z_ + _fy∂z ∧ ∂x_ + _fz∂x ∧ ∂y_ 

The vanishing ideal of _σ_ is then (2 _x_ + _A_ ( _f_ ) _, fy, fz_ ). If _f ∈_ K[[ _y, z_ ]] were reduced, the generators would form a complete intersection, contradicting our assumption 

24 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

that the vanishing locus of _σ_ is non-isolated. Hence _f_ cannot be reduced. Given ˜ ˜ ˜ that its leading term is _−y_[2] _z_ , we must have _f_ = _−y_[2] _z_ for some _y,_ ˜ _z ∈_ K[[ _y, z_ ]] whose leading terms are _y_ and _z_ . Applying the automorphism ( _y, z_ ) _�→_ (˜ _y,_ ˜ _z_ ), we may therefore assume without loss of generality that 

**==> picture [288 x 13] intentionally omitted <==**

where _u_ ( _y, z_ ) is an invertible function corresponding to the Jacobian determinant det _[∂]_[(] _[y,]_[˜] _[z]_[˜][)] _∂_ ( _y,z_ )[.] 

We need to argue that by a change of variables, we can replace the element _A_ ( _y_[2] _z_ ) _∈ y_[2] _z_ K[[ _y_[2] _z_ ]] with an element of _W_ K[[ _W_ ]]. Since the class of invertible functions is preserved by coordinate transformations, we may assume without loss of generality that _u_ = 1, i.e. 

**==> picture [265 x 13] intentionally omitted <==**

To construct the desired transformation, we will use the dg Lie algebra g _[•] < X_[�] _[•]_ [1] associated to the Poisson structure _σ_ 0 = [ _∂x∧∂y ∧∂z, W_ ] and the centre ( _x_[1] _, y_[1] _, z[∞]_ ), with differential 

**==> picture [50 x 11] intentionally omitted <==**

or more precisely a subalgebra g˜ _[•] ⊂_ g _[•]_ , constructed as follows. 

Let _R_ := K[[ _x, y_[2] _z_ ]] _< O_[�] be the subalgebra of elements expressible as power series in _x_ and _y_[2] _z_ , and let r := ( _x, y_[2] _z_ ) be its maximal ideal. We define a graded subspace g˜ _[•] <_ g _[•]_ concentrated in degree zero and one, by the formula 

**==> picture [126 x 13] intentionally omitted <==**

It is straightforward to verify that ˜g _[•]_ is a dg Lie subalgebra of g _[•]_ . Note further that ˜ ˜ for _σ_ of the form (5.2), the bivector _σ − σ_ 0 _∈_ g[1] is a Maurer–Cartan element of g _[•]_ . Hence it is enough to show that every Maurer–Cartan element of ˜g _[•]_ is equivalent to one lying in the subspace h := _W_ K[[ _W_ ]] _∂y ∧ ∂z <_ ˜g[1] , viewed as dg Lie subalgebra h _[•] ⊂_ g _[•]_ concentrated in degree one. For this, note that since h[2] = 0, it suffices by Theorem 5.5 to show that the natural projection h _→_ H[1] (˜g) is surjective. 

To establish this surjectivity, note that the differential on g˜ _[•]_ is determined by its action on monomials as follows: 

**==> picture [279 x 13] intentionally omitted <==**

for every _k, l ≥_ 0. This formula implies, by induction on _k_ , that _x[k]_ ( _y_[2] _z_ ) _[l] ∂y ∧ ∂z_ is cohomologous to a positive multiple of ( _−_ 1) _k_ 2 (( _y_[2] _z_ ) _[l]_[+] _[k]_ 2 _∂y ∧ ∂z_ if _k_ is even, and to zero if _k_ is odd, i.e. the cohomology is topologically spanned by the classes [( _y_[2] _z_ ) _[l] ∂y ∧ ∂z_ ] for _l >_ 0. Since ( _y_[2] _z_ ) _[l]_ = ( _−_ 1) _[l] W[l]_ mod _x_ , this also shows that ( _y_[2] _z_ ) _[l] ∂y ∧ ∂z_ is cohomologous to a multiple of _W[l] ∂y ∧ ∂z_ , and hence h surjects onto H[1] (˜g), as desired. □ 

## 6. Singularity invariants and resolutions 

We now recall the construction of resolution of singularities via weighted blowups as in [ATW24, McQ20]. The only possibly new results are Lemma 6.12 and the results of Section 6.3; the rest is review of previous work by other authors. For further exposition and details we refer the reader also to [Abr25, AQS25, Bra25, Lee20, W�l23, Tem25]. 

Weighted blowups and 3d Poisson desingularizations 

25 

6.1. **Singularity invariants from admissible centres.** The following can be thought of as the condition that an ideal “vanishes to weighted order one” on a centre: 

**Definition 6.1.** Let X be an orbifold, and let _J < O_ X be a coherent sheaf of ideals. A centre Z _•_ is _J_ - _**admissible**_ if ordZ _• J_ = 1. In this case, we may also write that Z _•_ is Y _**-admissible**_ , where Y = V( _J_ ) is the vanishing locus of _J_ . 

The set of _J_ -admissible centres has a partial order, induced by the lexicographic order on the corresponding exponent sequences. The following result is stated and proven in [ATW24]; as explained in [Bra25], it can also be deduced (in a different form) from the results of [BM97]. 

**Theorem 6.2.** _The set of J -admissible centres has a unique maximal element._ 

**Definition 6.3.** The maximal _J_ -admissible centre is call the _**associated centre of** J_ ; we denote it by Z[as] _•_[(] _[J]_[ ).][The] _**[invariant]**_[of] _[J]_[is][the][corresponding][exponent] sequence 

inv( _J_ ) := **a** (Z[as] _•_[(] _[J]_[ ))] 

We also write **a** ( _J_ ) = inv( _J_ ) and denote by **w** ( _J_ ), _**κ**_ ( _J_ ) the corresponding weight and weight sum sequences. 

_Remark_ 6.4 _._ There is also a local version of the invariant and associated centre, defined for the germ of (X _,_ Y) at a point _p ∈_ Y. The local invariant gives an upper semi-continuous function on Y with values in the totally order set of exponent sequences. The global invariant is the maximum of all the local invariants. In particular, if U _⊂_ X is open, then inv(U _,_ Y _∩_ U) _≤_ inv(X _,_ Y), which will be useful below. ♢ 

_Example_ 6.5 _._ The first entry _a_ 1( _J_ ) in the invariant **a** ( _J_ ) = inv( _J_ ) is equal to the maximal unweighted order of vanishing of _J_ at a point of X. In particular, _a_ 1( _J_ ) = 1 if and only if the vanishing locus Y = V( _J_ ) is locally contained in a smooth hypersurface in a neighbourhood of any point _p ∈_ Y. ♢ _Remark_ 6.6 _._ The uniqueness of the maximal admissible centre implies that if _k >_ 0, then the associated centres Z[as] _•_[(] _[J]_[ ) and][ Z] _•_[as][(] _[J][ k]_[) differ be reindexing the weights by] a factor of _k_ , so that inv( _J[k]_ ) = _k ·_ inv( _J_ ). ♢ 

We denote by 

INV := _{_ **a** _|_ **a** = inv(X _,_ Y) for some (X _,_ Y) _} ⊂Q_[N] 

the set of exponent sequence that occur as the invariant of some ideal on some orbifold. Not every exponent sequence lies in INV; see Section 6.2 below. 

Starting from an orbifold X and a subvariety Y _⊂_ X of pure codimension, one can blow up X along the centre Z[as] _•_[(][X] _[,]_[ Y][)][and][take][the][strict][transform][of][Y][to][get] a new pair BlZ _•_ (X _,_ Y). The following result implies that, if one repeats this process recursively, then after finitely many steps one arrives at a pair (X _[′] ,_ Y _[′]_ ) for which Y _[′]_ is smooth. The iterated blowdown (X _[′] ,_ Y _[′]_ ) _→_ (X _,_ Y) then gives a resolution of singularities in the category of orbifolds. 

**Theorem 6.7** ([ATW24]) **.** _The following statements hold_ 

- (1) _The set_ INV _⊂Q_[N] _of invariants is well ordered with respect to the lexicographic ordering on exponent sequences._ 

26 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

- (2) _A subvariety_ Y _⊂_ X _is smooth of pure codimension k if and only if_ 

**==> picture [126 x 25] intentionally omitted <==**

_This is the minimal possible invariant of a codimension-k subvariety._ 

- (3) _More generally, if_ Y _is contained in a smooth subvariety_ W _⊂_ X _of codimension k, then_ 

**==> picture [142 x 25] intentionally omitted <==**

_Conversely, if the first k entries of_ inv(X _,_ Y) _are equal to one, then the germ of_ Y _at any point is contained in the germ of a smooth codimension-k subvariety._ 

- (4) _The invariant decreases upon blowing up the associated centre: if_ Z _•_ = Z[as] _•_[(][X] _[,]_[ Y][)] _[,][then]_ 

**==> picture [118 x 11] intentionally omitted <==**

_where_ BlZ _•_ (X _,_ Y) _is the pair obtained by blowing up_ X _along_ Z _• and taking the strict transform of_ Y _._ 

_Remark_ 6.8 _._ A similar approach to resolution of plane curve singularities using _ordinary_ blowups was described by Abhyankar in [Abh83]. Namely, let ( _a_ 1 _, a_ 2) be the invariant of a plane curve singularity. Then in _op. cit._ it is shown that the pair ( _d, e_ ) = ( _a_ 1 _, a_ 2 _/a_ 1) decreases in the lexicographical order when one performs an ordinary blowup at the singular point. But this is equivalent to saying that the invariant ( _a_ 1 _, a_ 2) itself decreases. 

This fact, combined with Theorem 6.7 part (3), has the following consequence for locally planar curves embedded in higher-dimensional varieties, which will be useful for us below. Suppose that Y _⊂_ X is a curve contained in the support W := supp Z _•_ of a two-dimensional centre Z _•_ , and suppose that Y has a unique singular point _p_ . Then the invariant of Y has the form (1 _, . . . ,_ 1 _, b, c_ ), with length equal to dim X, where ( _b, c_ ) = inv(W _,_ Y). Let Z _•_ [ _p, b_ ] be the _b_ -completion of Z _•_ in the sense of Section 2.7. Then since the reduced centre underlying Z _•_ [ _p, b_ ] _∩_ W is unweighted, the blowup of (X _,_ Y) at _p_ restricts to the ordinary blowup of (W _,_ Y) at _p_ . Hence Abhyankar’s result implies that inv(BlZ _•_ [ _p,b_ ](X _,_ Y)) _<_ inv(X _,_ Y). ♢ 

6.2. **Numerical constraints.** As mentioned above, not every exponent sequence **a** = ( _a_ 1 _≤ a_ 2 _≤· · ·_ ) can arise as the invariant of an ideal, i.e. it need not lie in INV _⊂Q_[N] . According to [Tem25, §2.1], those that do are characterized by the following property: for every _j >_ 0, there exist _n_ 1 _, . . . , nj ∈_ Z _≥_ 0 such that � _ji_ =1 _naii_[=][1][and] _[n][j]_[=][0.][Equivalently,][as][formulated][in][[][Bra25][,][§][3.1]:][for][every] _j ≥_ 0, we have 

**==> picture [236 x 24] intentionally omitted <==**

where _n_ 1 _, . . . , nj_ +1 _∈_ Z _≥_ 0 are such that[�] _[n] aj[j][<]_[ 1][and] _[n][j]_[+1] _[>]_[ 0.] 

These constraints allow us to make predictions about the form of subsequent entries of an invariant from knowledge of a prefix. The following examples of this principle will be useful below. 

Weighted blowups and 3d Poisson desingularizations 

27 

_Example_ 6.9 _._ If **a** _∈_ INV is an invariant, then the first entry _a_ 1 is an integer. (This follows from Example 6.5.) ♢ 

_Example_ 6.10 _._ If **a** _∈_ INV has a sequence of 2s as a prefix, i.e. 

**==> picture [100 x 11] intentionally omitted <==**

then _aj_ +1 must be an integer. Indeed, in this case, the constraint _[n]_ 2[1][+] _[ · · ·]_[ +] _[n]_ 2 _[j][<]_[ 1] implies that at most one of the integers _n_ 1 _, . . . , nj_ is nonzero, and if nonzero it is equal to one. Hence the denominator of (6.1) is either 1 or[1] 2[.][Either way,] _[ a][j]_[+1] _[∈]_[Z][,] as claimed. ♢ 

_Example_ 6.11 _._ If **a** _∈_ INV has a sequence of 2s and 3s as a prefix, i.e. 

**==> picture [140 x 12] intentionally omitted <==**

then _aj_ +1 _≥_ 3 is either an integer, or an integer multiple of[3] 2[,][so][that] _aj_ +1 _∈{_ 3 _,_ 4 _,_ 4 _._ 5 _,_ 5 _,_ 6 _,_ 7 _,_ 7 _._ 5 _,_ 8 _,_ 9 _,_ 10 _,_ 10 _._ 5 _, . . .}._ 

The proof is similar to the previous example, but more involved: now the denominator has the form 1 _−[n]_[where] _[n, m][ ∈]_[Z] _[≥]_[0][,][so][its][only][possible][values][are] 2 _[−][m]_ 3 _[>]_[ 0] 16 _[,]_[1] 3 _[,]_ 2[1] _[,]_[2] 3[or][1.][Therefore] _[a][j]_[+1] _[∈]_[6][Z] _[ ∪]_[3][Z] _[ ∪]_[2][Z] _[ ∪]_ 2[3][Z] _[ ∪]_[Z][ =][ Z] _[ ∪]_[3] 2[Z][,][as][claimed.] ♢ These constraints imply corresponding constraints on the weights **w** and the weight sums _**κ**_ . A useful one for us is the following. 

**Lemma 6.12.** _Let_ **a** _∈_ INV _be an invariant of length two or three with a_ 1 _>_ 1 _. Then the following statements are equivalent:_ 

(1) **a** _<_ (2 _,_ 3 _,_ 6) _._ 

(2) _Either κ_ 3( **a** ) _>_ 1 _or_ **a** = (2 _,_ 2) _._ 

(3) _Either_ **a** _has the form_ (2 _,_ 2 _, n_ ) _with n ≥_ 2 _an integer, or it is equal to one of_ (2 _,_ 2) _,_ (2 _,_ 3 _,_ 3) _,_ (2 _,_ 3 _,_ 4) _,_ (2 _,_ 3 _,_ 4 _._ 5) _or_ (2 _,_ 3 _,_ 5) _._ 

_Proof._ Since the length of **a** is two or three, we have **a** = ( _a ≤ b ≤ c ≤∞≤· · ·_ ), with _b_ finite and _c_ possibly infinite. The implication (3) = _⇒_ (2) is an easy calculation, whose result is summarized in Table 1 below. It therefore suffices to prove that (2) = _⇒_ (1) = _⇒_ (3). 

To see that (1) implies (3), suppose that **a** _<_ (2 _,_ 3 _,_ 6). Then by definition of the lexicographical order, we must have 2 = _a ≤ b ≤_ 3. Moreover by Example 6.10, _b_ is an integer. Hence either _b_ = 2, or _b_ = 3. If _b_ = 2, then _c_ = _n_ is an integer or _c_ = _∞_ , giving **a** = (2 _,_ 2 _, n_ ) or **a** = (2 _,_ 2). If _b_ = 3, then by definition of the lexicographical order, we have _c <_ 6 and hence _c ∈{_ 3 _,_ 4 _,_ 4 _._ 5 _,_ 5 _}_ by Example 6.11. 

Finally, to prove that (2) implies (1), we prove the contrapositive. Suppose that **a** _≥_ (2 _,_ 3 _,_ 6), and note that then **a** = (2 _,_ 2). We claim that _κ_ 3( **a** ) _≤_ 1. There are three cases to consider: either (i) _a ≥_ 3; or (ii) _a_ = 2 and _b >_ 3; or (iii) ( _a, b_ ) = (2 _,_ 3) and _c ≥_ 6. In case (i) we have 

**==> picture [66 x 13] intentionally omitted <==**

In case (ii), we have by Example 6.10 that _b >_ 3 is an integer, and hence _b ≥_ 4. Therefore 

**==> picture [269 x 56] intentionally omitted <==**

Finally, in case (iii), we have 

as desired. 

28 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

6.3. **Surfaces with small weight sums.** Note that if we decrease an exponent sequence **a** in the lexicographical order, the corresponding weight sequence **w** increases, which tends to (but does not always) increase the weight sum _**κ**_ . This suggests that there should be relatively few singularities whose invariants have “large” weights sums, so that they may be amenable to classification. We illustrate this here in the case of two-dimensional hypersurface singularities; see also [Rei80, §4] for a related discussion. 

Note that here, when we refer to the classification of singularities, we mean up to analytic equivalence. In particular, if Y _⊂_ X is a subvariety of an orbifold, then the singularity type at a point _p ∈_ Y can be determined by looking in an orbifold chart, which reduces the problem to the case of subvarieties of affine space. 

**Proposition 6.13.** _Let_ X _be a three-dimensional orbifold, and let_ Y _⊂_ X _be a singular surface. Then the following statements are equivalent._ 

- (1) inv(X _,_ Y) _<_ (2 _,_ 3 _,_ 6) _._ 

- (2) _Either κ_ 3(X _,_ Y) _>_ 1 _or_ inv(X _,_ Y) = (2 _,_ 2) _._ 

- (3) _The only singularities of_ Y _are Du Val singularities, Whitney umbrellas or normal crossings singularities of multiplicity two, given by equations as in Table 1._ 

_In this case, every connected component of the singular locus of_ Y _is smooth of dimension zero or one._ 

_Proof._ The equivalence of the first two statements, and the list of possible invariants **a** in Table 1 is the content of the numerical result Lemma 6.12 above, noting that Y is singular if and only if _a_ 1 _>_ 1, in which case the length is two or three. 

For the rest of the proof, we will make use of some explicit calculations of invariants, which we performed using the method described in [Bra25, §0.4]. In particular, with this method it is straightforward to verify that the singularities listed in (3) have the desired invariant by direct calculation with the standard defining equations in Table 1. Evidently the singular locus of each is either isolated, or a smooth curve. It remains to prove that these are the only singularities with invariant less than (2 _,_ 3 _,_ 6). 

To this end, suppose that the invariant is less than (2 _,_ 3 _,_ 6), and let _f_ be a local defining equation for Y near _p_ . Since _a_ 1 = ord _pf_ , we see that _f_ vanishes to order two, so that its Hessian is nonzero. Hence by the parameterized Morse lemma, there are local coordinates ( _x, y, z_ ) such that _f_ = _x_[2] + _g_ ( _y, z_ ) for some function _g_ ( _y, z_ ). Then ( _a_ 2 _, a_ 3) is the invariant of _g_ , and the singular locus of Y is identified with the singular locus of the curve _{g_ = 0 _}_ in the plane _{x_ = 0 _}_ . 

If **a** = (2 _,_ 2 _, n_ ) with _n_ an integer or **a** = (2 _,_ 2), then _g_ also vanishes to order two, so applying the Morse lemma again we arrange that _f_ = _x_[2] + _y_[2] + _z[n]_ or _x_[2] + _y_[2] , respectively. In the first case, we have an _An−_ 1 singularity, which is isolated, and in the second case the change of variables _x[′]_ = _x_ + _[√] −_ 1 _y_ and _y[′]_ = _x −[√] −_ 1 _y_ gives the normal crossings equation _x[′] y[′]_ = 0. 

Meanwhile, if **a** = (2 _,_ 3 _, c_ ), then _g_ ( _y, z_ ) has order 3. We therefore consider the classification of triple points of plane curves. 

If the singularities are isolated, then _g_ must be equivalent to one of the singularities listed in [AGZV85, §15.2]. Calculating the invariants of those polynomials one finds that only _Dn, E_ 6 _, E_ 7 and _E_ 8 have invariants of the desired form; the remaining ones have invariant (2 _,_ 3 _, c_ ) with _c ≥_ 6. 

Weighted blowups and 3d Poisson desingularizations 

29 

**Table 1.** Surface singularities in A[3] with invariant less than (2 _,_ 3 _,_ 6) 

|Name|Equation|Invariant **a**|Weight sum _κ_3|
|---|---|---|---|
|Normal crossings<br>Whitney umbrella<br>_An, n ≥_1<br>_Dn, n ≥_4<br>_E_6<br>_E_7<br>_E_8|_xy_<br>_x_2 _−y_2_z_<br>_x_2 +_y_2 +_zn_+1<br>_x_2 +_y_2_z_+_zn−_1<br>_x_2 +_y_3 +_z_4<br>_x_2 +_y_3 +_yz_3<br>_x_2 +_y_3 +_z_5|(2_,_2)<br>(2_,_3_,_3)<br>(2_,_2_, n_+ 1)<br>(2_,_3_,_3)<br>(2_,_3_,_4)<br>(2_,_3_,_4_._5)<br>(2_,_3_,_5)|1<br>1 + 1<br>6<br>1 +<br>1<br>_n_+1<br>1 + 1<br>6<br>1 + 1<br>12<br>1 + 1<br>18<br>1 + 1<br>30|



If the singularities are not isolated, then _g_ must have a multiple component, and since _g_ vanishes to order three, the component must have multiplicity at most three. If the multiplicity is two, then _g_ = _u_[2] _v_ for some functions _u, v_ of order one, which can then be used as coordinates. Hence after a change of variables we may assume _u_ = _y_ and _v_ = _z_ , so that _f_ = _x_[2] + _y_[2] _z_ , giving a Whitney umbrella. Meanwhile, the case of a component of multiplicity three cannot occur: in this case, after a change of variables, we have _g_ = _y_[3] , so that _f_ = _x_[2] + _y_[3] , but then the invariant is (2 _,_ 3) = (2 _,_ 3 _, ∞_ ) _>_ (2 _,_ 3 _,_ 6), a contradiction. □ 

_Remark_ 6.14 _._ Proposition 6.13 shows that the Du Val singularities of type _A_ and _E_ are uniquely determined by their invariant (amongst all isolated hypersurface singularities of dimension two). Moreover, these cases, the defining equations in Table 1 are quasi-homogeneous of order one with respect to the exponents defined by the invariant. 

However, for the Du Val singularities of type _D_ , the situation is different. They all have the same invariant, namely (2 _,_ 3 _,_ 3), while the defining equation is quasihomogeneous of order one with respect to the exponent sequence �2 _,_ 2 + _n−_ 2 2 _[, n][ −]_[1] �. The latter is equal to (2 _,_ 3 _,_ 3) when _n_ = 4, but is otherwise strictly smaller in the lexicographical order. ♢ 

Proposition 6.13 characterizes Du Val singularities as the isolated hypersurface singularities of dimension two for which _κ_ 3 _>_ 1, where _κ_ 3 = _κ_ 3(Z[as] _•_[(][X] _[,]_[ Y][))][is][the] weight sum of the associated centre (the one defining the invariant). In fact, this inequality holds for _any_ admissible centre, as a consequence of the fact that Du Val singularities are canonical. Namely, the following is an equivalent rephrasing of [Rei80, Theorem 4.1]; the vector _α_ in _op. cit._ is exactly the data of the exponent sequence of a weighted coordinate system and the expression _α_ ( _g_ ) in _op. cit._ is the valuation ordZ _•_ ( _J_ ) where _J_ is the ideal of Y. For an admissible centre, this valuation is equal to one. 

**Proposition 6.15** ([Rei80, Theorem 4.1]) **.** _Let_ X _be an orbifold of dimension n, and let_ Y _⊂_ X _be a hypersurface with only canonical singularities. Then every_ Y _admissible centre_ Z _• has weight sum κn_ (Z _•_ ) _>_ 1 _._ 

**Corollary 6.16.** _If_ dim X = 3 _and_ Y _⊂_ X _is a surface having only Du Val singularities, then κ_ 3(Z _•_ ) _>_ 1 _for all_ Y _-admissible centres_ Z _•._ 

30 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

## 7. Weighted resolutions of Poisson subvarieties 

7.1. **Poisson subvarieties and triples.** Let (X _, σ_ ) be a Poisson orbifold. By a _**Poisson subvariety**_ , we mean a closed subvariety Y _⊂_ X to which _σ_ is tangent; equivalently the Poisson bracket on _O_ X descends to a bracket on _O_ Y = _O_ X _/J_ , where _J_ is the defining ideal of Y. We allow Y to be singular. 

**Definition 7.1.** A _**Poisson triple**_ is a triple (X _,_ Y _, σ_ ) where X is an orbifold, _σ_ is a Poisson structure on X, and Y _⊂_ X is a closed Poisson subvariety of pure dimension. The _**dimension**_ of a Poisson triple (X _,_ Y _, σ_ ) is the pair (dim X _,_ dim Y). 

We wish to start with a Poisson triple (X _,_ Y _, σ_ ) for which Y is singular, and repeatedly blow it up to improve its singularities without destroying the Poisson structure. It is natural to impose the further condition that the exceptional divisor is Poisson, i.e. that we only blow up conilpotent centres. In fact, in our constructions below in low dimensions, this will turn out to be automatic: allowing codegenerate centres will not enlarge the class of singularities that can be resolved in those cases. 

7.2. **Subvarieties of the vanishing set.** Before proceeding, it will be useful to have a criterion to check that certain centres are conilpotent. 

Namely, a particularly simple sort of Poisson subvariety Y _⊂_ X is one that is contained in the vanishing set of the Poisson structure. Thus _σ ∈J X_ X[2][where] _J < O_ X is the defining ideal of Y. In this case, if Z _•_ is any centre with corresponding weight sum _**κ**_ (Z _•_ ), we have 

ordZ _• σ ≥_ ordZ _• J − κ_ 2(Z _•_ ) _._ 

In particular, we immediately have the following: 

**Lemma 7.2.** _If_ Z _• is_ Y _-admissible and κ_ 2(Z _•_ ) _≤_ 1 _, then_ Z _• is conilpotent with respect to any Poisson structure vanishing on_ Y _._ 

**Corollary 7.3.** _Let a_ 1 _denote the first entry of the singularity invariant of_ (X _,_ Y) _. If a_ 1 _>_ 1 _, then the associated centre_ Z[as] _•_[(][X] _[,]_[ Y][)] _[is][conilpotent][with][respect][to][σ][.]_ 

_Proof._ For the associated centre Z[as] _•_[(][X] _[,]_[ Y][),][the][first][entry] _[a]_[1][is][an][integer;][hence][if] _a_ 1 _>_ 1, we have _κ_ 2 = _a_ 11[+] _a_[1] 2 _[≤] a_ 21 _[≤]_[1.] □ 

By Theorem 6.7, part (3), the condition _a_ 1 = 1 is equivalent to the statement that Y is contained in a smooth hypersurface. Equivalently, the Zariski tangent space of Y at any point _p_ is contained in a hyperplane of T _p_ X. Hence we may rephrase the previous corollary as follows: 

**Corollary 7.4.** _Suppose_ Y _is contained in the vanishing locus of σ and that we have the equality_ T _p_ Y = T _p_ X _of Zariski tangent spaces at some point p ∈_ Y _. Then the associated centre_ Z[as] _•_[(][X] _[,]_[ Y][)] _[is][conilpotent][with][respect][to][σ][.]_ 

7.3. **Curves in surfaces.** Suppose (X _,_ Y _, σ_ ) is a Poisson triple of dimension (2 _,_ 1). Then _σ_ vanishes identically on Y for dimension reasons, and T _p_ Y = T _p_ X at every singular point of Y. By Corollary 7.4, the associated centre Z[as] _•_[(][X] _[,]_[ Y][) is conilpotent] whenever Y is singular. We therefore have the following: 

**Theorem 7.5.** _Let_ (X _,_ Y _, σ_ ) _be a Poisson triple with_ dim X = 2 _and_ dim Y = 1 _. Then the associated centre_ Z[as] _•_[(][X] _[,]_[ Y][)] _[ is conilpotent.][Hence the algorithm of]_[ [][ATW24][]] _produces a sequence of weighted blowups along conilpotent centres_ 

(X _[′] ,_ Y _[′] , σ[′]_ ) _→· · · →_ (X _,_ Y _, σ_ ) 

Weighted blowups and 3d Poisson desingularizations 

31 

## _such that_ Y _[′] is smooth._ 

_Remark_ 7.6 _._ The unweighted centre defined by the singular locus Ysing is also conilpotent; hence ordinary blowup at singular points will also produce a resolution. This approach has the disadvantage that more blowups will typically be required, but it also has the advantage that if X is a variety, X _[′]_ will also be a variety, so no orbifolds are needed. ♢ 

7.4. **Resolution strategy for Poisson threefolds.** In the rest of the paper, we explain how to reduce the singularities of Poisson triples (X _,_ Y _, σ_ ) with dim X = 3. Our strategy is to try, as much as possible, to blow up the associated centre Z[as] _•_[(][X] _[,]_[ Y][)] of the underlying pair, but now there are two important complications. 

The first complication is that there will be a “bad locus” W _⊂_ Y (made precise below), consisting of isolated singularities of Y where _σ_ admits no codegenerate centres. Hence we can never improve the singularities in W using a weighted blowup without destroying the Poisson structure, and we are forced to focus on improving the singularities of the complementary pair (X _\_ W _,_ Y _\_ W). We will therefore set 

## inv(X _,_ Y _, σ_ ) := inv(X _\_ W _,_ Y _\_ W) _≤_ inv(X _,_ Y) 

and try to decrease inv(X _,_ Y _, σ_ ) to the minimal possible value, which corresponds to the case in which Y _\_ W is smooth, i.e. the only singularities of Y are the ones that can’t be improved. 

For instance, we can try to blow up the associated centre of the pair (X _\_ W _,_ Y _\_ W). However, this leads to the second complication: the centre Z[as] _•_[(][X] _[ \]_[ W] _[,]_[ Y] _[ \]_[ W][)][need] not be conilpotent for _σ_ . Therefore, at times, we will need to select a different centre that _is_ conilpotent, and whose blowup still reduces the invariant. 

7.5. **Curves in threefolds.** Let (X _,_ Y _, σ_ ) be a Poisson triple of dimension (3 _,_ 1). Then Y is a curve and _σ_ vanishes identically on Y for degree reasons. In particular, if _p ∈_ Ysing, then the linearization of the Poisson structure gives a Lie algebra h _p_ := (T _[∗] p_[X] _[,]_[ [] _[−][,][ −]_[]).] 

**Definition 7.7.** Let (X _,_ Y _, σ_ ) be a Poisson triple of dimension (3 _,_ 1). A _**nonnilpotent point of**_ (X _,_ Y _, σ_ ) is a point _p ∈_ Ysing such that the Lie algebra h _p_ is not nilpotent. We denote by 

**==> picture [62 x 11] intentionally omitted <==**

## the set of non-nilpotent points. 

The set Y _σ−_ nn will play the role of the “bad locus” W in the strategy outlined in Section 7.4. The rest of the present subsection is devoted to the proof of the following statements, which describe the geometry of non-nilpotent points, and show that these are the only singularities that cannot be eliminated by blowing up. 

**Proposition 7.8.** _If p ∈_ Y _σ−_ nn _, then there exist formal coordinates_ ( _x, y, z_ ) _∈ O_[�] X _,p and an element f ∈_ K[[ _y, z_ ]] _such that_ 

**==> picture [188 x 11] intentionally omitted <==**

_in the formal neighbourhood of p in_ X _._ 

**Corollary 7.9.** _The non-nilpotent locus contains no σ-codegenerate centres; hence non-nilpotent singularities cannot be improved using a weighted blowup._ 

_Proof._ This follows immediately from Proposition 7.8 and Example 4.9. □ 

32 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

**Table 2.** Three-dimensional Lie algebras h with dim[h _,_ h] _≤_ 1 

|dim[h_,_ h]|Nilpotent?|Name|Linear Poisson structure|
|---|---|---|---|
|0<br>1<br>1|yes<br>yes<br>no|abelian<br>Heisenberg<br>split nonabelian|0<br>_x∂y ∧∂z_<br>_x∂x ∧∂y_|



**Theorem 7.10.** _Let_ (X _,_ Y _, σ_ ) _be a Poisson triple of dimension_ (3 _,_ 1) _. Then the there exists a sequence of weighted blowups along conilpotent centres_ 

**==> picture [124 x 11] intentionally omitted <==**

**==> picture [314 x 13] intentionally omitted <==**

Before proving Proposition 7.8 and Theorem 7.10, we need a preparatory lemma. 

**Lemma 7.11.** _Let_ (X _,_ Y _, σ_ ) _be a Poisson triple of dimension_ (3 _,_ 1) _, let p ∈_ Ysing _be a singular point of_ Y _, and let_ h := (T _[∗] p_[X] _[,]_[ [] _[−][,][ −]_[])] _[be][the][conormal][Lie][algebra][at] p. Then_ dim[h _,_ h] _≤_ 1 _, and hence the linearization of σ at p is isomorphic to one of the linear Poisson structures in Table 2._ 

_Proof._ Let _a_ 1 be the first entry of the invariant of (X _,_ Y) at _p_ . If _a_ 1 _>_ 1 then the ideal _J_ defining Y vanishes to order two, and since _σ ∈J X_ X[2][we][deduce][that][the] linearization of _σ_ is zero. Otherwise, _a_ 1 = 1, so that _J_ vanishes to order one. Hence there exist coordinates ( _x, y, z_ ) such that _J_ = ( _x, g_ ( _y, z_ )) for some function _g_ that vanishes to order at least two at the origin, i.e. Y is identified with the curve _g_ = 0 in the _yz_ -plane. Since _σ|_ Y = 0, we have 

**==> picture [63 x 8] intentionally omitted <==**

for some _σ_ 0 _, σ_ 1 _∈ X_ X[2] _,p_[.][Since][d] _[g][|][p]_[=][0,][it][follows][that][[][h] _[,]_[ h][]][is][contained][in][the] linear subspace spanned by d _x|p ∈_ T _[∗] p_[X][,][and][hence][dim[][h] _[,]_[ h][]] _[≤]_[1,][as][claimed.][The] classification in Table 2 now follows immediately from the Bianchi classification of three-dimensional Lie algebras. □ 

_Proof of Proposition 7.8._ According to Table 2, the linearization of _σ_ at a point _p ∈_ Y _σ−_ nn is isomorphic to 

**==> picture [70 x 13] intentionally omitted <==**

By Proposition 5.7, there are formal coordinates ( _x, y, z_ ) such that 

**==> picture [105 x 11] intentionally omitted <==**

for some _g ∈ z_[2] K[[ _z_ ]]. Since _σ|_ Y = 0, we must have Y _⊂_ V( _x, g_ ). If _g_ = 0 then _g_ = _z[j] g_ ˜( _z_ ) for some _j >_ 0 and _g_ ˜ _∈_ K[[ _z_ ]] such that _g_ ˜(0) = 0. Thus Y _⊂_ V( _x, z_ ), which implies that Y is smooth, contradicting the assumption that _p_ is a singular point. We conclude that _g_ = 0 and hence _σ_ = _x∂x ∧ ∂y_ . Then Y lies in the plane _x_ = 0, so that it is given by equations of the form _x_ = _f_ ( _y, z_ ) = 0, as claimed. □ 

**Definition 7.12.** For a Poisson triple (X _,_ Y _, σ_ ) of dimension (3 _,_ 1), we denote by 

inv(X _,_ Y _, σ_ ) := inv(X _\_ Y _σ−_ nn _,_ Y _\_ Y _σ−_ nn) (7.1) 

the invariant of the pair obtained from (X _,_ Y) be removing all non-nilpotent points of (X _,_ Y _, σ_ ). 

Weighted blowups and 3d Poisson desingularizations 

33 

Note that 

**==> picture [232 x 11] intentionally omitted <==**

by Remark 6.4, applied to the open U = X _\_ Y _σ−_ nn. Furthermore, Y _\_ Y _σ−_ nn is smooth if and only if its invariant is (1 _,_ 1) (the minimal possible invariant for a curve in a threefold), i.e. we have the following: 

**==> picture [325 x 11] intentionally omitted <==**

Let Z _⊂_ Y _\_ Y _σ−_ nn be the locus of maximal invariant; note that since the singularities of Y are isolated, Z is a finite set. According to Lemma 7.11, we have a decomposition Z = Zab _⊔_ ZHeis into subsets where the linearization is either abelian, or the Heisenberg algebra, respectively. Define a centre Z _•_ = Z _•_ (X _,_ Y _, σ_ ) supported on Z by assigning weights to each point _p ∈_ Z as follows. The construction treats several cases differently, in order to produce a centre that simultaneously is conilpotent, and reduces the invariant upon blowing up. 

Let _a_ 1 = _a_ 1(X _,_ Y _, σ_ ) be the first entry of inv(X _,_ Y _, σ_ ). 

- If _a_ 1 _>_ 1, set Z _•_ (X _,_ Y _, σ_ ) = Z[as] _•_[(][X] _[ \]_[ Y] _[σ][−]_[nn] _[,]_[ Y] _[ \]_[ Y] _[σ][−]_[nn][).] 

- If _a_ 1 = 1, let Z _•_ = Z _•_ (X _,_ Y _, σ_ ) be the centre defined in the following way: 

   - If _p ∈_ Zab, then Z _•|p_ is the unweighted centre defined by _p_ . 

   - If _p ∈_ ZHeis and V( _σ_ ) has dimension one at _p_ , then by Proposition 5.7 part (2), there exist formal coordinates ( _x, y, z_ ) in which the Poisson structure has the form 

**==> picture [194 x 11] intentionally omitted <==**

with _f ∈_ ( _y, z_ )[2] K[[ _y, z_ ]] and _A, B ∈ f_ K[[ _f_ ]]. There are two possibilities: 

- _∗_ V( _σ_ ) has dimension one; equivalently _B_ ( _f_ ) = 0. Then we take Z _•|p_ := Z[as] _•_[(][X] _[,]_[ Y][)] _[|][p]_[to][be][the][associated][centre.] 

- _∗_ V( _σ_ ) is a smooth surface near _p_ ; equivalently, _B_ ( _f_ ) = 0. Then let _b_ = _a_ 2(X _,_ Y _, σ_ ) and take Z _•|p_ := V( _σ_ )[ _p, b_ ] to be the _b_ - completion of the unweighted centre defined by V( _σ_ ), in the sense of Section 2.7. In coordinates as above, Z _•|p_ is given by (( _x_ + _A_ ( _f_ ))[1] _, y[b] , z[b]_ ). 

Theorem 7.10 now follows immediately by combining the following result with Lemma 7.13 and the well-orderedness of the set of invariants. 

**Proposition 7.14.** _The centre_ Z _•_ = Z _•_ (X _,_ Y _, σ_ ) _is conilpotent, and_ 

**==> picture [250 x 11] intentionally omitted <==**

_Proof._ Let _a_ 1 be the first entry of inv(X _,_ Y _, σ_ ), and let Z _•_ = Z _•_ (X _,_ Y _, σ_ ). We first prove that the invariant decreases as in (7.3). For this, let X _[′]_ = BlZ _•_ (X) with blowdown map _b_ : X _[′] →_ X and let Y _[′]_ be the strict transform of Y. Then since Y _σ−_ nn _∩_ Z _•_ = ∅, the locus Y _σ[′] −_ nn[is][the][disjoint][union][of][the][preimage] _[b][−]_[1][(][Y] _[σ][−]_[nn][)] and the set of non-nilpotent points contained in the exceptional divisor. Hence 

**==> picture [236 x 44] intentionally omitted <==**

34 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

where the inequality in the second line follows from Remark 6.4 applied to the open U = X _[′] \_ Y _σ[′] −_ nn _[⊂]_[X] _[′][ \][ b][−]_[1][(][Y] _[σ][−]_[nn][)][and][the][equality][in][the][third][line][follows][from] the isomorphism X _[′] \ b[−]_[1] (Y _σ−_ nn) = _[∼]_ BlZ _•_ (X _\_ Y _σ−_ nn). It therefore suffices to show that 

**==> picture [264 x 11] intentionally omitted <==**

This is indeed true. Namely, for each point _p ∈_ Z _•_ there are two possibilities. The first is that we blow up the associated centre Z[as] _•[|][p]_[,][in][which][case][Theorem][6.7] applies. The second possibility is that _a_ 1 = 1, and we perform a blowup of a _b_ - completion of a surface W containing the germ of Y at _p_ , in which case Remark 6.8 applies. (This second possibility encompasses both the case of ordinary blowups for _p ∈_ Zab, for which _b_ = 1, and the case _p ∈_ ZHeis with W = V( _σ_ ) a surface.) 

It remains to show that Z _•_ is conilpotent. If _a_ 1 _>_ 1, this follows from Corollary 7.3, so assume that _a_ 1 = 1. At any point _p ∈_ Zab, the unweighted centre is conilpotent by Example 4.5, so it suffices to treat the case in which the linearization is the Heisenberg algebra. 

So, suppose _p ∈_ ZHeis. By Proposition 5.7, we may assume without loss of generality that there exist _f ∈_ K[[ _y, z_ ]] vanishing at the origin, and _A_ ( _f_ ) _, B_ ( _f_ ) _∈ f_ K[[ _f_ ]] such that 

**==> picture [312 x 26] intentionally omitted <==**

If V( _σ_ ) is a curve, then by definition, Z _•|p_ is the associated centre at _p_ . Moreover, _B_ ( _f_ ) must be nonzero. Since _σ_ vanishes on Y, we must have 

**==> picture [144 x 11] intentionally omitted <==**

where _J_ is the ideal defining Y. In particular, d _B_ vanishes identically on Y. Since _B_ ( _f_ ) _|p_ = 0, we conclude that _B_ ( _f_ ) vanishes to order two on Y, i.e. _B_ ( _f_ ) _∈J_[2] . Since _B_ ( _f_ ) is nonzero, we may write _B_ ( _f_ ) = _f[j] B_[˜] ( _f_ ) where _j >_ 0 and _B_[˜] ( _f_ ) is a unit. Hence _f[j] ∈J_ , and since _J_ is radical we must have _f ∈J_ . Therefore _A_ ( _f_ ) _∈J_ and hence _x ∈J_ as well. In particular, ordZ _• B_ ( _f_ ) _≥_ 2ordZ _• J_ = 2 and ordZ _• A_ ( _f_ ) _≥_ ordZ _• J_ = 1. Moreover _x_ gives a maximal contact parameter, and hence after a change of variables involving only _y_ and _z_ , we may assume without loss of generality that Z _|p_ is defined by the coordinates ( _x_[1] _, y[b] , z[c]_ ) with 2 _≤ b ≤ c_ . Then each term in (7.4) has order at least 1 _−_[1] _b[−]_[1] _c[≥]_[0.] 

If V( _σ_ ) is a surface, i.e. _B_ ( _f_ ) = 0, then by definition Z _•|p_ = ( _u_[1] _, v[a]_[2] _, w[a]_[2] ) where _u_ = _x_ + _A_ ( _f_ ) and ( _v, w_ ) = ( _y, z_ ). Hence the Poisson structure (7.4) has the form 

**==> picture [223 x 27] intentionally omitted <==**

Since _A_ ( _f_ ) _∈_ ( _y, z_ )[2] = ( _v, w_ )[2] , we have ordZ _• A_ ( _f_ ) _≥ a_ 22[,][and][we][immediately] obtain ordZ _• σ ≥_ 0. □ 

7.6. **Surfaces in threefolds.** Finally, we treat Poisson triples of dimension (3 _,_ 2). The argument is parallel to the case of dimension (3 _,_ 1) but the details are different. 

**Definition 7.15.** A _**Du Val point**_ of a (3 _,_ 2)-dimensional Poisson triple (X _,_ Y _, σ_ ) is a point at which the surface Y has a Du Val singularity, and the Poisson structure 

Weighted blowups and 3d Poisson desingularizations 

35 

_σ_ has an isolated zero. We denote by 

**==> picture [65 x 11] intentionally omitted <==**

the set of Du Val points. 

Note that the condition depends on both the singularity of the surface and the Poisson structure; for instance if _σ_ is identically zero then there are no Du Val points of the triple (X _,_ Y _, σ_ ), even if the surface Y itself has Du Val singularities. Indeed, it is a sort of nondegeneracy condition: the statement that _p_ is an isolated zero of _σ_ is equivalent to the statement that _σ_ induces a trivialization of the canonical bundle of Y in a neighbourhood of _p_ . 

We begin this section by developing an explicit normal form for the Poisson structure near a Du Val point. The first simplification is provided by the following result of Fraenkel, which is established using a Koszul complex argument: 

**Proposition 7.16** ([Fra13, Proposition 4.1]) **.** _If_ (X _,_ Y _, σ_ ) _is a Poisson triple of dimension_ (3 _,_ 2) _and p is an isolated singular point of_ Y _, then in any system of coordinates_ ( _x, y, z_ ) _centred at p, the germ of σ at p has the form_ 

**==> picture [121 x 11] intentionally omitted <==**

_for some function g ∈O_ X _,p, and some bivector η ∈ X_ X[2] _,p[.]_ 

We now use Pichereau’s work [Pic09] on deformations of Jacobian Poisson structures to show that in the case of Du Val points, the function _f_ in Proposition 7.16 can be put into a normal form, and we can furthermore take _η_ = 0. Note that in part (3) of the following proposition, the centre Z _•_ may differ from the associated centre of the Du Val singularity, in accordance with Remark 6.14. 

**Proposition 7.17.** _Let_ (X _,_ Y _, σ_ ) _be a Poisson triple of dimension_ (3 _,_ 2) _, let p ∈_ Ysing _be a singular point of_ Y _. Then the following are equivalent:_ 

(1) _p is a Du Val point of_ (X _,_ Y _, σ_ ) 

- (2) _There exist formal coordinates_ ( _x, y, z_ ) _∈ O_[�] X _,p and a unit g ∈_ K[[ _x, y, z_ ]] _[×] such that_ 

**==> picture [190 x 11] intentionally omitted <==**

- _where f ∈_ K[ _x, y, z_ ] _is an equation for a Du Val singularity as in Table 1._ 

- (3) _There exists a centre_ Z _• supported at p with weighted coordinates_ ( _x[a] , y[b] , z[c]_ ) _, and a quasi-homogeneous polynomial f ∈_ K[ _x, y, z_ ] _giving an equation for a Du Val singularity as in Table 1, such that_ 

**==> picture [115 x 11] intentionally omitted <==**

_Proof._ The implication (2) = _⇒_ (1) is immediate. We will prove the implications (1) = _⇒_ (3), and (3) = _⇒_ (2). 

To see that (1) implies (3), suppose that _p_ is a Du Val point. Choose coordinates ( _x, y, z_ ) in which Y is given by the vanishing of a polynomial _f_ as in Table 1. Let ( _a ≤ b ≤ c < ∞_ ) be an exponent sequence for which _f_ is quasi-homogeneous of order one (see Remark 6.14), and let Z _•_ be the centre defined ( _x[a] , y[b] , z[c]_ ). 

Since the singularity of Y is isolated, by Proposition 7.16, we have 

**==> picture [117 x 11] intentionally omitted <==**

for some germ of a function _g ∈O_ X _,p_ , and some bivector _η ∈ X_ X[2] _,p_[.][Hence][the] vanishing locus of _σ_ contains the vanishing locus V( _f, g_ ). If _g_ were not a unit in 

36 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

_O_ X _,p_ , then _p_ would lie in V( _f, g_ ), and the latter would have dimension at least one, which would contradict the assumption that _σ_ has an isolated zero. Hence _g_ is a unit, i.e. the constant _λ_ := _g_ ( _p_ ) is nonzero and hence ordZ _• g_ = 0 and ltZ _•_ ( _g_ ) = _λ_ . Since ordZ _•_ lt( _σ_ ) _<_ 0, we can arrange that _λ_ = 1 by rescaling the variables by a suitable constant. 

Since ordZ _• X_ X[2][=] _[−][κ]_[2][(][Z] _[•]_[),][and][since] _[c][<][∞]_[,][we][have] _[κ]_[2][(][Z] _[•]_[)] _[<][κ]_[3][(][Z] _[•]_[).][There-] fore 

**==> picture [242 x 11] intentionally omitted <==**

and we deduce that 

**==> picture [112 x 11] intentionally omitted <==**

as desired. 

Finally, to see that (3) implies (2), assume that ltZ _•_ ( _σ_ ) has the given form and and view _σ_ as a deformation of ltZ _•_ ( _σ_ ) as in Section 5.3. By [Pic09, Proposition 3.6], _σ_ is isomorphic to a Poisson structure of the form _g_ ˜[ _∂x ∧ ∂y ∧ ∂z, f_[˜] ] for some _f_[˜] with lt( _f_[˜] ) = _f_ . Since the class of Du Val singularities is invariant under deformation, we can find a change of variables that takes _f_[˜] to _f_ , and this puts _σ_ in the desired form. □ 

The normal form described in Proposition 7.17 implies that Du Val points can never be eliminated by blowing up, even if we allow the possibility that the exceptional divisor is not Poisson: 

**Corollary 7.18.** _If p is a Du Val point, then there are no σ-codegenerate centres supported at p._ 

_Proof._ From part (2) of Proposition 7.17, we deduce that at a Du Val point _p_ , the Poisson structure is locally Jacobian (up to a nonvanishing factor). Hence by Example 4.7, a Y-admissible centre at _p_ is codegenerate if and only if it has weight sum _κ_ 3 _≤_ 1, but by Corollary 6.16, such centres do not exist. □ 

In the rest of this subsection, we will prove the following result, which shows that by blowing up, we can remove any singularity that is not a Du Val point. 

**Theorem 7.19.** _Let_ (X _,_ Y _, σ_ ) _be a Poisson triple of dimension_ (3 _,_ 2) _. Then there exists a sequence of weighted blowups along conilpotent centres_ 

**==> picture [124 x 11] intentionally omitted <==**

_such that_ Ysing _[′]_[=][Y] _σ[′] −_ DV _[,][i.e.][the][only][singular][points][of]_[Y] _[′][are][Du][Val][points][of] the triple_ (X _[′] ,_ Y _[′] , σ[′]_ ) _._ 

The proof hinges on the following two propositions, which characterize the situations in which the associated centre of the pair (X _,_ Y) is not conilpotent for _σ_ . In the first proposition, we analyze the quasi-homogeneous leading term, and in the second, we use this information to treat the general case. 

**Proposition 7.20.** _Let_ (X _,_ Y _, σ_ ) _be a Poisson triple of dimension_ (3 _,_ 2) _, and let_ Z _•_ = Z[as] _•_[(][X] _[,]_[ Y][)] _[ be the associated centre of the pair]_[ (][X] _[,]_[ Y][)] _[.][If]_[ Z] _[•][is not][ σ][-conilpotent,] then the leading term_ ltZ _•_ ( _σ_ ) _is isomorphic to the Jacobian Poisson structure associated to either a Du Val singularity or a Whitney umbrella._ 

Weighted blowups and 3d Poisson desingularizations 

37 

_Proof._ By degeneration to the normal cone, we may assume without loss of generality that X = A[3] with weighted coordinates ( _x[a] , y[b] , z[c]_ ), that _σ_ = lt( _σ_ ) is quasihomogeneous, and that Y is defined by the vanishing of a quasi-homogeneous polynomial _f_ . Note, however, that since reducedness is not preserved by degeneration, we must now allow the possibility that Y is not reduced. 

Let _f_ 0 be an equation for the reduced hypersurface Y0 := Yred. Recall that a polyvector field is tangent to Y if and only if it is tangent to Y0. Hence _σ_ is tangent to both Y and Y0, which means that the vector fields _η_ := _f[−]_[1] _ι_ d _f σ_ and _η_ 0 := _f_ 0 _[−]_[1] _[ι]_[d] _[f]_ 0 _[σ]_[are][as][well.][Note][that] _[η]_[and] _[η]_[0][,][if][nonzero,][are][homogeneous][of] order ordZ _•_ ( _η_ ) = ordZ _•_ ( _η_ 0) = ordZ _•_ ( _σ_ ) _<_ 0. On the other hand, the associated centre is invariant under formal isomorphism of germs, and hence it is preserved by the flow of any vector field tangent to Y; this implies that the order of _η_ and _η_ 0 is non-negative. We therefore deduce that _η_ = _η_ 0 = 0, and hence 

**==> picture [217 x 12] intentionally omitted <==**

so that _σ_ is a cycle in the Koszul complexes of d _f_ and d _f_ 0. 

Since _f_ 0 is reduced, its critical locus has dimension at most one. Hence the homology of its Koszul complex ( _X_ X _[•][, ι]_[d] _[f]_ 0[)][vanishes][in][degree][two,][so][that] _[σ]_[is] exact. Hence 

**==> picture [267 x 11] intentionally omitted <==**

is the Jacobian Poisson structure of _f_ 0. It remains to show that V( _f_ 0) = Y0 has a Du Val or Whitney umbrella singularity. 

Since _σ_ is nonzero and skew-symmetric, its kernel generically has rank one, and hence (7.6) implies that d _f_ 0 _∧_ d _f_ = 0. Since _f_ 0 is reduced, it follows from [MM80, p. 472, Th´eor`eme de factorisation] that _f_ = _A_ ( _f_ 0) for some _A ∈ f_ 0K[[ _f_ 0]]. By quasihomogeneity, we deduce that _f_ = _f_ 0 _[k]_[for][some] _[k][≥]_[0.][Let][Z][0] _•_[=][Z][as] _•_[(][X] _[,]_[ Y][0][)][be][the] associated centre of Y0. Then Z[0] _•_[is defined by the weighted chart (] _[x][a/k][, y][b/k][, z][c/k]_[),] thanks to Remark 6.6. From (7.7) and the fact that the centre Z _•_ is not conilpotent, we deduce that 

0 _>_ ordZ _•_ ( _σ_ ) = ordZ _•_ ([ _∂x ∧∂y ∧∂z, f_ 0]) = _k_[1][ord][Z][0] _•_[([] _[∂][x][∧][∂][y][ ∧][∂][z][, f]_[0][]) =] _k_[1][(1] _[−][κ]_[3][(][Y][0][))] _[,]_ so that _κ_ 3(Y0) _>_ 1. The result now follows from Proposition 6.13. □ 

We now deform away from the leading term to deduce the following. 

**Proposition 7.21.** _Let p ∈_ Ysing _be a point at which_ Z[as] _•_[(][X] _[,]_[ Y][)] _[is][not][conilpotent.] Then the following dichotomy holds:_ 

_• If_ Y _has an isolated singularity at p, then p is a Du Val point of_ (X _,_ Y _, σ_ ) _._ 

_• Otherwise,_ Y _has a Whitney umbrella singularity at p._ 

_Proof._ Let ( _x[a]_[1] _, y[a]_[2] _, z[a]_[3] ) be coordinates defining the associated centre Z[as] _•_[(][X] _[,]_[ Y][)][at] _p_ . 

Suppose first that Y has an isolated singularity at _p_ . Then by Proposition 7.16, we have _σ_ = _g_ [ _∂x ∧∂y ∧∂z, f_ ]+ _fη_ for some functions _g, f_ and some bivector _η_ . This implies that ordZas _•_[(][X] _[,]_[Y][)][(] _[σ]_[)] _[≥]_[1] _[ −][κ]_[3][.][Since][Z][as] _•_[is][not][conilpotent,][we][must][have] _κ_ 3 _>_ 1, so that the singularity is Du Val by Proposition 6.13, and moreover _g_ (0) _̸_ = 0. Switching to weighted coordinates (˜ _x[a] ,_ ˜ _x[b] ,_ ˜ _x[c]_ ) in which _f_ is quasi-homogeneous as in Remark 6.14, we obtain a centre Z _•_ in which the leading term of _σ_ has the form of Proposition 7.17 part (3), so that _p_ is a Du Val point. 

38 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

Now suppose that _p_ is a non-isolated singularity of Y. Since _σ_ vanishes on Ysing, the point _p_ is also a non-isolated zero of _σ_ ; in particular, _p_ is not a Du Val point of (X _,_ Y _, σ_ ). Therefore by Proposition 7.17, the leading term cannot have a Du Val point either. Hence by Proposition 7.20, the leading term must be the Jacobian Poisson structure of a Whitney umbrella, so that Z[as] _•_[(][X] _[,]_[ Y][) is given by the] weighted coordinates ( _x_[2] _, y_[3] _, z_[3] ). By Proposition 5.8, we may assume without loss of generality that 

**==> picture [194 x 11] intentionally omitted <==**

where _W_ = _x_[2] _− y_[2] _z_ and _u_ is an invertible function. We claim that Y is given locally by _W_ = 0. In fact, we claim something much stronger: the surface _W_ = 0 is the only Poisson surface containing the origin in this formal chart. 

To see this, note first that since the condition of being a Poisson subvariety is invariant under rescaling the bivector by an arbitrary invertible function, we may assume without loss of generality that _u_ = 1, i.e. that 

**==> picture [176 x 11] intentionally omitted <==**

Now note that the vanishing locus of _σ_ is given by the equations 

**==> picture [140 x 11] intentionally omitted <==**

which define a non-reduced scheme supported on the _z_ -axis _x_ = _y_ = 0. Hence the singular locus of Y must be this same axis. Moreover, the surface _z_ = 0 is not tangent to _σ_ . Hence it suffices to show that the only Poisson surface in the complement _z_ = 0 that contains the _z_ -axis is the Whitney umbrella _W_ . 

Furthermore, any Poisson surface must be preserved by the Hamiltonian vector field of _z_ , which has the form 

**==> picture [140 x 11] intentionally omitted <==**

Hence it suffices to show that _W_ = 0 is the only irreducible surface containing the _z_ -axis that is preserved by _ζ_ . 

For this, we may pass to the cover defined by _[√] z_ over the locus _z_ = 0, i.e. work in the larger ring K(( _z_[1] _[/]_[2] ))[[ _x, y_ ]] _⊃_ K[[ _x, y, z_ ]], viewing _ζ_ as a derivation of this larger ring over the base field K(( _z_[1] _[/]_[2] )). There, we may factor _W_ = ( _x_ + _[√] zy_ )( _x −[√] zy_ ), so that the surface _W_ = 0 has two smooth branches _x_ = _±[√] zy_ . 

Since _W ∈_ ( _x, y_ )[2] , the linearization of _ζ_ along the _z_ -axis _x_ = _y_ = 0 is 

**==> picture [84 x 11] intentionally omitted <==**

with eigenvalues _±_ 2 _[√] −z_ . Since the ratio of the eigenvalues is _−_ 1, a theorem of Seidenberg [Sei68] ensures that there are exactly two invariant subvarieties passing through the _z_ -axis. Hence they must be the two branches of the Whitney umbrella, as desired. □ 

We now construct the sequence of blowups that reduces all singularities to Du Val points. The approach is similar to what we did for curves in threefolds above. Namely, let us denote by 

inv(X _,_ Y _, σ_ ) := inv(X _\_ Y _σ−_ DV _,_ Y _\_ Y _σ−_ DV) 

the invariant of the pair formed by the non-Du Val locus. Parallel to the case of dimension (3 _,_ 1), we have that inv(X _,_ Y _, σ_ ) _≤_ inv(X _,_ Y), and this invariant detects when the singularities are Du Val points: 

Weighted blowups and 3d Poisson desingularizations 

39 

**Lemma 7.22.** Ysing = Y _σ−_ DV _if and only if_ inv(X _,_ Y _, σ_ ) = (1) _._ 

We define a centre Z _•_ (X _,_ Y _, σ_ ) on X supported in Y _\_ Y _σ−_ DV, as follows: 

- If inv(X _,_ Y _, σ_ ) _̸_ = (2 _,_ 3 _,_ 3), let Z _•_ (X _,_ Y _, σ_ ) := Z[as] _•_[(][X] _[ \]_[ Y] _[σ][−]_[DV] _[,]_[ Y] _[ \]_[ Y] _[σ][−]_[DV][).] 

- If inv(X _,_ Y _, σ_ ) = (2 _,_ 3 _,_ 3), then by Proposition 6.13, the singular locus of Y _\_ Y _σ−_ DV is a disjoint union Z _⊔_ C where Z is a zero-dimensional set along which Y has Du Val singularities of type _D_ , and C is the union of the onedimensional components of Ysing (along which Y has Whitney umbrella or two-component normal crossings singularities). In this case, we take Z _•_ (X _,_ Y _, σ_ ) to be the disjoint union of the associated centre Z[as] _•_[(][X] _[,]_[ Y][)] _[|]_[Z] along Z and the unweighted centre defined by C. 

Theorem 7.19 now follows immediately from the following result, combined with Lemma 7.22 and the well-orderedness of the set of invariants. 

**Proposition 7.23.** _The centre_ Z _•_ = Z _•_ (X _,_ Y _, σ_ ) _is conilpotent, and_ 

**==> picture [250 x 10] intentionally omitted <==**

_Proof._ To see that the invariant decreases, we argue as in the proof of Proposition 7.14 that it suffices to establish the inequality 

inv(BlZ _•_ (X _\_ Y _σ−_ DV _,_ Y _\_ Y _σ−_ DV)) _<_ inv(X _\_ Y _σ−_ DV _,_ Y _\_ Y _σ−_ DV) _._ 

This inequality does indeed hold: either we blow up the associated centre (which reduces the invariant by Theorem 6.7), or we perform the unweighted blowup of the curve C (which completely resolves the singularities lying over C). 

The conilpotence is immediate from Proposition 7.21, unless inv(X _,_ Y _, σ_ ) = (2 _,_ 3 _,_ 3). In this case, we must also check that the curve C is conilpotent. This is a closed condition, so we can check it at the generic point of C, where the invariant is (2 _,_ 2) and hence the associated centre at the generic point of C is the unweighted centre defined by C. Hence the result follows from Proposition 7.21 again. Alternatively, and more explicitly, we can note that Y generically has normal crossings singularities on C, so near a generic point there are formal coordinates ( _x, y, z_ ) with Y = V( _xy_ ) and C = V( _x, y_ ). Since _σ_ is tangent to Y, it must locally lie in the subalgebra of _X_ X _[•]_[generated][by] _[x∂][x][, y∂][y][, ∂][z]_[all][of][which][have][non-negative] order with respect to the unweighted centre ( _x_[1] _, y_[1] _, z[∞]_ ) defining C. □ 

## References 

- [ABdSTW25] D. Abramovich, A. Belotto da Silva, M. Temkin, and J. W�lodarczyk, _Principalization on logarithmically foliated orbifolds_ , `arXiv:2503.00926 [math.AG]` . 

[Abh83] S. S. Abhyankar, _Desingularization of plane curves_ , Singularities, Part 1 (Arcata, Calif., 1981), Proc. Sympos. Pure Math., vol. 40, Amer. Math. Soc., Providence, RI, 1983, pp. 1–45. 

|[Abh83]|_tion on logarithmically foliated orbifolds_, `arXiv:2503.00926 [math.AG]`.<br>S. S. Abhyankar, _Desingularization of plane curves_, Singularities, Part 1 (Arcata,<br>Calif., 1981), Proc. Sympos. Pure Math., vol. 40, Amer. Math. Soc., Providence,<br>RI, 1983, pp. 1–45.|
|---|---|
|[Abr25]|D. Abramovich, _Resolution of singularities for the dynamical mathematician_,|
||`arXiv:2503.17321 [math.AG]`.|
|[AGZV85]|V. I. Arnol_′_d, S. M. Guse˘ın-Zade, and A. N. Varchenko, _Singularities of diferen-_|
||_tiable maps. Vol. I_, Monographs in Mathematics, vol. 82, Birkh¨auser Boston, Inc.,|
||Boston, MA, 1985. The classifcation of critical points, caustics and wave fronts,|
||Translated from the Russian by Ian Porteous and Mark Reynolds.|
|[AQS25]|D. Abramovich, M. H. Quek, and B. Schober, _Torus actions, weighted blow-ups,_|
||_and desingularization of plane curves_, `arXiv:2507.01232 [math.AG]`.|
|[ATW24]|D. Abramovich, M. Temkin, and J. W�lodarczyk, _Functorial embedded resolution_|
||_via weighted blowings up_, Algebra Number Theory **18** (2024), no. 8, 1557–1587.|
|[Bea00]|A. Beauville, _Symplectic singularities_, Invent. Math. **139** (2000), no. 3, 541–549.|



## 40 SIMON LAPOINTE, MYKOLA MATVIICHUK, BRENT PYM, AND BORIS ZUPANCIC 

|[BM97]|E. Bierstone and P. D. Milman, _Canonical desingularization in characteristic zero_|
|---|---|
||_by blowing up the maximum strata of a local invariant_, Invent. Math. **128** (1997),|
||no. 2, 207–302.|
|[Bra25]|M. J.-L. Brais, _Streamlining resolution of singularities with weighted blow-ups_,|
||`arXiv:2512.01859`.|
|[BT77]|L. Brickman and E. S. Thomas, _Conformal equivalence of analytic fows_, J. Difer-|
||ential Equations **25** (1977), no. 3, 310–324.|
|[dJ96]|A. J. de Jong, _Smoothness, semi-stability and alterations_, Inst. Hautes ´Etudes Sci.|
||Publ. Math. (1996), no. 83, 51–93.|
|[DR15]|V. A. Dolgushev and C. L. Rogers, _A version of the Goldman-Millson theorem for_|
||_fltered L∞-algebras_, J. Algebra **430** (2015), 260–302.|
|[DZ05]|J.-P. Dufour and N. T. Zung, _Poisson structures and their normal forms_, Progress|
||in Mathematics, vol. 242, Birkh¨auser Verlag, Basel, 2005.|
|[Fra13]|A. M. Fraenkel, _Extensions of Poisson structures on singular hypersurfaces_,|
||`arXiv:1310.6083`.|
|[Fu05]|B. Fu, _Poisson resolutions_, J. Reine Angew. Math. **587** (2005), 17–26.|
|[GGJ04]|A. Garijo, A. Gasull, and X. Jarque, _Normal forms for singularities of one dimen-_|
||_sional holomorphic vector felds_, Electron. J. Diferential Equations (2004), No.|
||122, 7.|
|[Hir64]|H. Hironaka, _Resolution of singularities of an algebraic variety over a feld of_|
||_characteristic zero. I, II_, Ann. of Math. (2) 79 (1964), 109–203; ibid. (2) **79** (1964),|
||205–326.|
|[HZ23]|D. Hoekstra and F. Zeiser, _Poisson cohomology of 3D Lie algebras_, J. Geom. Phys.|
||**191** (2023), Paper No. 104862, 38.|
|[KKP08]|L. Katzarkov, M. Kontsevich, and T. Pantev, _Hodge theoretic aspects of mirror_|
||_symmetry_, From Hodge theory to integrability and TQFT tt*-geometry, Proc.|
||Sympos. Pure Math., vol. 78, Amer. Math. Soc., Providence, RI, 2008, pp. 87–|
||174.|
|[Kon08]|M. Kontsevich, _XI Solomon Lefschetz Memorial Lecture series: Hodge structures_|
||_in non-commutative geometry_, Non-commutative geometry in mathematics and|
||physics, Contemp. Math., vol. 462, Amer. Math. Soc., Providence, RI, 2008, pp. 1–|
||21. Notes by Ernesto Lupercio.|
|[Lee20]|J. Lee,<br>_Algorithmic resolution via weighted blowings up_,<br>`arXiv:2008.02169`|
||`[math.AG]`.|
|[Lic77]|A. Lichnerowicz, _Les vari´et´es de Poisson et leurs alg`ebres de Lie associ´ees_, J.|
||Diferential Geometry **12** (1977), no. 2, 253–300.|
|[LM23]|Y. Loizides and E. Meinrenken, _Diferential geometry of weightings_, Adv. Math.|
||**424** (2023), Paper No. 109072, 49.|
|[LP24]|A. Lindberg and B. Pym, _Semiclassical Hodge theory for log Poisson manifolds_,|
||`2408.16685`. 64 pages.|
|[Man22]|M. Manetti, _Lie methods in deformation theory_, Springer Monographs in Mathe-|
||matics, Springer, Singapore, 2022.|
|[McQ20]|M. McQuillan, _Very functorial, very fast, and very easy resolution of singularities_,|
||Geom. Funct. Anal. **30** (2020), no. 3, 858–909.|
|[MM80]|J.-F. Mattei and R. Moussu, _Holonomie et int´egrales premi`eres_, Ann. Sci. ´Ecole|
||Norm. Sup. (4) **13** (1980), no. 4, 469–523.|
|[MP13]|M. McQuillan and D. Panazzolo,_Almost ´etale resolution of foliations_, J. Diferential|
||Geom. **95** (2013), no. 2, 279–319.|
|[Pan06]|D. Panazzolo, _Resolution of singularities of real-analytic vector felds in dimension_|
||_three_, Acta Math. **197** (2006), no. 2, 167–289.|
|[Pic09]|A. Pichereau,_Formal deformations of Poisson structures in low dimensions_,Pacifc|
||J. Math. **239** (2009), no. 1, 105–133.|
|[Pol97]|A. Polishchuk, _Algebraic geometry of Poisson brackets_, J. Math. Sci. (N. Y.) **84**|
||(1997), no. 5, 1413–1444. Algebraic geometry, 7.|
|[Que22]|M. H. Quek, _Logarithmic resolution via weighted toroidal blow-ups_, Algebr. Geom.|
||**9** (2022), no. 3, 311–363.|
|[Rei80]|M. Reid, _Canonical 3-folds_, Journ´ees de g´eom´etrie alg´ebrique d’Angers (Alphen)|
||(A. Beauville, ed.), Sijthof and Noordhof, 1980.|



Weighted blowups and 3d Poisson desingularizations 

41 

- [Sch25] A. Sch¨ußler, _On the real projective blowup of Poisson structures_ , Differential Geom. Appl. **101** (2025), Paper No. 102293, 7. 

- [Sei68] A. Seidenberg, _Reduction of singularities of the differential equation A dy_ = _B dx_ , Amer. J. Math. **90** (1968), 248–269. 

- [Tem25] M. Temkin, _Dream resolution and principalization i: enough derivations_ , `arXiv:2503.18205 [math.AG]` . 

- [Ver00] M. Verbitsky, _Holomorphic symplectic geometry and orbifold singularities_ , Asian J. Math. **4** (2000), no. 3, 553–563. 

- [W�l23] J. W�lodarczyk, _Weighted resolution of singularities. A Rees algebra approach_ , New techniques in resolution of singularities, Oberwolfach Semin., vol. 50, Birkh¨auser/Springer, Cham, 2023, pp. 219–317. 

- [W�lo23] J. W�lodarczyk, _Functorial resolution by torus actions_ , `arXiv:2203.03090` . 

