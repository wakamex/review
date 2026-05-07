## **REAL BORDERED FLOER HOMOLOGY** 

## ROBERT LIPSHITZ AND PETER OZSVÁTH 

Abstract. Fix a 3-manifold _Y_ with boundary _F ⨿ F_ and an orientation-preserving involution _τ_ : _Y → Y_ exchanging the boundary components, with nonempty fixed set. To an appropriate kind of Heegaard diagram for _Y_ , we describe how to associate a module over the bordered Heegaard Floer algebra _A_ ( _F_ ). These modules satisfy a gluing, or pairing, theorem, and extend Guth-Manolescu’s real Heegaard Floer homology _HFR_[�] . Using these modules, we give a practical algorithm to compute _HFR_[�] ( _Y, τ_ ) for real 3-manifolds ( _Y, τ_ ) with connected fixed set. 

## Contents 

|1.|Introduction|2|
|---|---|---|
|Acknowledgments||4|
|2.|Real bordered Heegaard diagrams|4|
|2.1.|Real bordered 3-manifolds and their Heegaard diagrams|4|
|2.2.|States, domains, and spin_c_-decomposition|8|
|3.|Moduli spaces|11|
|3.1.|Defnitions of the moduli spaces|11|
|3.2.|Expected dimensions|14|
|3.3.|Codimension-1 degenerations|16|
|4.|Real bordered modules|17|
|4.1.|An example|18|
|5.|Real-nice diagrams and the real Auroux-Zarev piece|19|
|5.1.|Real-nice diagrams and their real bordered invariants|19|
|5.2.|Real Auroux-Zarev diagrams|29|
|5.3.|Classical bordered invariants of the Auroux-Zarev diagrams|31|
|5.4.|The real Auroux-Zarev modules|33|
|6.|Pairing theorem|45|
|6.1.|The pairing theorem via nice diagrams|45|
|6.2.|General pairing theorem via time dilation|47|
|7.|Gradings|50|
|7.1.|Review of the unreal case|50|
|7.2.|Grading real bordered modules|51|
|7.3.|Comparison with the unreal gradings|56|
|7.4.|A graded pairing theorem|57|
|8.|Computing �<br>_HFR_ by factoring mapping classes|59|
|8.1.|Computer implementation|60|



RL was supported by NSF grant DMS-2505715, a Simons Foundation travel grant, and the Fernholz Foundation and Princeton University. 

PSO was supported by NSF grants DMS-1708284 and DMS-2104536. 

1 

LIPSHITZ AND OZSVÁTH 

|||||
|---|---|---|---|
|2||LIPSHITZ AND OZSVÁTH||
||9.|Other Applications|62|
||9.1.|The frst diferential in Hendricks’s spectral sequence|62|
||9.2.|A surgery exact triangle|63|
||9.3.|Branched double covers of certain satellites|64|
||9.4.|Genus-1 splittings|70|
||9.5.|Splittings with connected fxed sets and orientable quotients|71|
||10.|Detours|71|
||References||73|



## 1. Introduction 

Many recent applications of low-dimensional Floer theory have relied on invariants incorporating the setting’s symmetries. Notably, these include the internal symmetries of the invariants, particularly the conjugation symmetry on spin _[c]_ -structures considered in Pin(2)equivariant monopole Floer homology [Man16, Lin18] and involutive Heegaard Floer homology [HM17] (with applications, for instance, to the Triangulation Conjecture [Man16] and the structure of the homology cobordism group [DHST23]); and external symmetries of the manifolds, such as the Z _/_ 2-action exchanging the sheets in branched double covers. Combining these symmetries has allowed these invariants to resolve problems that seemed previously inaccessible, such as proving that cables of the figure-8 knot are not slice [DKM[+] 24] or giving exotic surfaces that do not dissolve after a single stabilization [Gut22] (see also [Kan22, LM25, KPT25], among others). 

Li introduced another way of studying Z _/_ 2-symmetries in Seiberg-Witten theory, for a three-manifold equipped with an involution, by composing the involution of the manifold with spin _[c]_ -conjugation to define real monopole Floer homology [Li22]. Inspired by his work, Guth-Manolescu defined real Heegaard Floer homology groups _HFR[◦]_ , equivariant versions of the various variants of Heegaard Floer homology [GM25]. (See [GM25] for a more thorough review of the literature. In particular, 4-dimensional constructions that these Floer theories intend to extend have had particularly striking applications, such as [Miy23].) 

Real Heegaard Floer homology groups are invariants of a 3-manifold _Y_ with an orientationpreserving, smooth involution _τ_ : _Y → Y_ with nonempty (hence 1-dimensional) fixed set. Unlike involutive Heegaard Floer homology, real Heegaard Floer homology is defined via a strict symmetry of a Heegaard diagram, which exchanges the _α_ - and _β_ -curves and reverses the orientation of the Heegaard surface. Although its construction is concrete, in terms of a specific diagram, real Heegaard Floer homology groups remain somewhat mysterious, and have been computed in relatively few cases. The main goal of this paper is to start to ameliorate that, by giving a practical algorithm to compute _HFR_[�] ( _Y, τ_ ), at least when the fixed set of _τ_ is connected. Our strategy is to give an extension of _HFR_[�] to 3-manifolds with boundary, as a variant of bordered Heegaard Floer homology, and then extend the algorithm for computing bordered Heegaard Floer homology from our earlier work (with D. Thurston) [LOT14b]. We have implemented this algorithm, as part of Bohua Zhan’s bordered Floer homology python software package [Zha]. (To date, both real Heegaard Floer homology and bordered Floer homology have only been constructed with F2-coefficients, so all Floer complexes in this paper are over F2.) 

REAL BORDERED FLOER HOMOLOGY 

3 

A real bordered 3-manifold is an arced bordered 3-manifold _Y_ with two boundary components, together with an involution _τ_ : _Y → Y_ exchanging the two boundary components while respecting their parametrizations by a pointed matched circle _Z_ . (See Definition 2.1.) In the interests of brevity, this paper develops only the aspects of the bordered invariants of such ( _Y, τ_ ) needed to compute _HFR_[�] ( _Y, τ_ ). We summarize the structure of our invariants, as developed in this paper, in the following: 

**Theorem 1.1.** _Given a real bordered 3-manifold_ ( _Y, τ_ ) _with boundary −F_ ( _Z_ ) _⨿−F_ ( _Z_ ) _, represented by a real bordered Heegaard diagram_ ( _H, τ_ ) _, there is an associated type D structure_ � _CFDR_ ( _Y, τ_ ) _over the (usual) bordered algebra A_ ( _Z_ ) _. Moreover, for any bordered_ 3 _-manifold Y[′] with boundary −F_ ( _Z[′]_ ) _⨿ F_ ( _Z_ ) _, we have_ 

**==> picture [298 x 17] intentionally omitted <==**

� _where τ is the evident extension of τ , exchanging the two copies of Y[′] . Finally, if Y is closed (or the boundary consists of two copies of S_[2] _), then CFDR_[�] ( _Y, τ_ ) _≃ CFR_[�] ( _Y, τ_ ) _, GuthManolescu’s real Heegaard Floer complex._ 

This is proved below as Theorems 4.3 and 6.5. (We also give a more direct proof of the pairing theorem for nice diagrams, Theorem 6.1.) As some readers may notice, the form of real bordered Floer homology is pleasantly simpler than the form of involutive bordered Floer homology [HL19]; this leads also to a more efficient computer implementation. (A special case of the type _A_ invariant, Proposition 8.2, also makes the computer implementation more efficient.) 

To compute _HFR_[�] ( _Y, τ_ ), we start from a real Heegaard splitting _Y_ = _H ∪_ Σ _τ_ ( _H_ ). There is a particularly attractive real bordered Heegaard diagram for nbd(Σ), coming from the Auroux-Zarev diagram AZ( _Z_ ) [Aur10, Zar10, LOT11] associated to a symmetric pointed matched circle ( _Z, τ_ ), and the associated module _CFDR_[�] (AZ( _Z_ ) _, τ_ ) has a simple description. (See, for instance, Corollary 5.16, which suggests that perhaps analogous constructions would make sense in other Fukaya categories or in purely algebraic settings.) Tensoring this with the bordered invariant _CFA_[�] ( _H_ ) (with appropriate framing), which we computed in earlier work [LOT14b], gives _CFR_[�] ( _Y, τ_ ). 

Although we develop mainly the aspects of real bordered Floer homology needed for this algorithm, the construction has other computational and conceptual applications as well. The existence of real bordered Floer homology implies a surgery exact triangle for � _HFR_ . Identifications between the real bordered modules for real tori and certain borderedsutured invariants imply that if a real 3-manifold ( _Y, τ_ ) admits a separating symmetric torus containing the fixed set, then _HFR_[�] ( _Y, τ_ ) agrees with a familiar sutured Floer homology group. In a similar direction, if ( _Y, τ_ ) admits a separating symmetric surface with orientable quotient, then _HFR_[�] ( _Y, τ_ ) agrees with a real knot Floer homology group. We also obtain a proof of a structural conjecture of Hendricks’s, about the first differential in her spectral sequence to real Heegaard Floer homology [Hen25], at least if the fixed set is connected. Finally, we observe that real bordered Floer homology can be used to compute the real Floer homology of branched covers of even winding number satellites, and illustrate this with the Whitehead pattern and (2 _,_ 1) cabling pattern. This gives, for instance: 

LIPSHITZ AND OZSVÁTH 

4 

**Theorem 1.2.** _Given a knot K ⊂ S_[3] _, let Wh_ ( _K_ ) _denote the (positive or negative) Whitehead double of K. If K is a nontrivial alternating knot, then there is a strict inequality_ 

**==> picture [248 x 17] intentionally omitted <==**

In other words, Hendricks’s spectral sequence is nontrivial in these cases. 

This paper is organized as follows. We describe the kinds of Heegaard diagrams used in the construction, as well as states and domains connecting them, in Section 2. The analysis of the moduli spaces of holomorphic curves is in Section 3, starting with the definition of moduli spaces and then establishing their Fredholm theory (transversality, expected dimensions) and codimension-1 boundary. Section 4 defines the bordered type _D_ structure associated to a real bordered 3-manifold; the gradings for these modules are deferred to Section 7. In Section 5 we study nice real bordered Heegaard diagrams and their invariants in general, and then the Auroux-Zarev diagrams specifically. Section 6 proves the pairing theorem for nice real bordered Heegaard diagrams, Theorem 6.1. 

Applications begin in Section 8, with the algorithm to compute _HFR_[�] . Other applications are in Section 9, to Hendricks’s spectral sequence, a surgery exact triangle, and the real Heegaard Floer homology of certain classes of manifolds, like branched covers of satellite knots. We conclude, in Section 10, with a discussion of results not in this paper—topics we omit for brevity, but which would be part of a thorough development of real bordered Floer theory. 

**Acknowledgments.** We thank Fraser Binns, Gary Guth, Kristen Hendricks, Adam Levine, Semon Rezchikov, and Yonghan Xiao for helpful conversations and corrections. This research was conducted while RL was visiting Princeton University, supported by the Fernholz Foundation, and he is grateful for their support. 

The first author used Anthropic’s Claude chatbot for late-stage proofreading and to help with drawing Figure 8. The second author used xfig. 

## 2. Real bordered Heegaard diagrams 

In Section 2.1, we spell out the class of 3-dimensional cobordisms with real involutions that we will work with, the kinds of bordered Heegaard diagrams we use for them, the gluing operation we consider, and some examples. In Section 2.2, we explain the topological framework for bordered Floer homology of these diagrams, discussing states (generators) and domains connecting them. 

2.1. **Real bordered 3-manifolds and their Heegaard diagrams.** Recall that a _pointed matched circle_ is a tuple _Z_ = ( _Z,_ **a** _, M, z_ ), where _Z_ is a circle, **a** _⊂ Z_ consists of 4 _k_ points, _M_ : **a** _→_ **a** is a fixed point-free involution (the _matching_ ), and _z ∈ Z\_ **a** is a basepoint [LOT18, Definition 3.16]. We require that performing surgery on _Z_ along ( **a** _, M_ ) =[�] 2 _k[S]_[0][results] in a single circle. When considering bordered Heegaard diagrams, the points **a** will be the endpoints of the _α_ -arcs. A _β-pointed matched circle_ consists of exactly the same data as a pointed matched circle, but we think of **a** as the endpoints of the _β_ -arcs [LOT11, Section 3.1]. In particular, given a pointed matched circle _Z_ there is a corresponding _β_ -pointed matched circle _Z[β]_ . 

A pointed matched circle specifies a surface _F_ ( _Z_ ) by thickening _Z_ to _Z ×_ [1 _,_ 2] and attaching 2-dimensional 1-handles to **a** _× {_ 1 _}_ as specified by _M_ . A _β_ -pointed matched circle also specifies a surface, but now the surface is obtained from _Z ×_ [1 _,_ 2] by attaching 

REAL BORDERED FLOER HOMOLOGY 

5 

2-dimensional 1-handles to **a** _× {_ 2 _}_ . So, there is a canonical orientation-reversing diffeomorphism _Kα,β_ : _F_ ( _Z_ ) _→ F_ ( _Z[β]_ ), or equivalently an orientation-preserving diffeomorphism _K α,β_ : _F_ ( _Z_ ) _→−F_ ( _Z[β]_ ). A pointed matched circle _Z_ also specifies a bordered algebra _A_ ( _Z_ ) [LOT18, Chapter 3]. By convention, _A_ ( _Z[β]_ ) is the opposite algebra to _A_ ( _Z_ ) [LOT11, Section 3.2]. 

A _real 3-manifold_ is a closed 3-manifold with an orientation-preserving, smooth involution with nonempty fixed set. We will consider the following extension to 3-manifolds with parameterized boundary: 

**Definition 2.1.** _A_ real bordered 3-manifold _consists of a compact, connected, oriented_ 3 _- manifold Y with boundary; a diffeomorphism_ 

**==> picture [158 x 13] intentionally omitted <==**

_for some pointed matched circle Z; a framed arc γ in Y connecting the two boundary components; and an orientation-preserving, smooth involution τ_ : _Y → Y . These data are required to satisfy:_ 

- _The involution τ commutes with the parametrization of the boundary, in the sense that_ 

(2.2) _τ ◦ ϕL_ = _ϕR._ 

- _The fixed set of τ is nonempty (hence also_ 1 _-dimensional and closed)._ 

- _The involution τ preserves γ, τ_ ( _γ_ ) = _γ, and if we view the framing as a normal vector field ν along γ, then dτ ◦ ν_ = _−ν._ 

It is equivalent, but more natural later, to think of _ϕR_ as a map _F_ ( _−Z[β]_ ) _→ ∂Y_ , from the surface associated to _Z[β]_ with its orientation reversed. Then Formula (2.2) becomes 

**==> picture [284 x 13] intentionally omitted <==**

We will often suppress _ϕL ⨿ ϕR_ and _γ_ , and write a real bordered 3-manifold just as ( _Y, τ_ ). 

_Example_ 2.4 _._ For us, a _real surface_ is a closed, connected, oriented surface Σ together with an orientation-reversing involution _τ_ : Σ _→_ Σ with nonempty fixed set. Real surfaces (Σ _, τ_ ) and (Σ _[′] , τ[′]_ ) are diffeomorphic if there is a diffeomorphism _ψ_ : Σ _→_ Σ _[′]_ so that _τ[′] ◦ ψ_ = _ψ ◦ τ_ . Up to diffeomorphism, a real surface is determined by: 

- The genus _g_ of Σ, 

- The number of components _|C|_ of the fixed set _C_ of _τ_ , and 

- Whether Σ _/τ_ is orientable or nonorientable. 

Further, the only conditions these data must satisfy are that 1 _≤|C| ≤ g_ + 1; if Σ _/τ_ is nonorientable then _|C| ≤ g_ ; and if Σ _/τ_ is orientable, then _|C| ≡ g_ + 1 (mod 2). (See, for example, [Liu20] and the references there.) Figure 1 indicates how to realize any such tuple of data. 

Because we will use it later, note that there is a basis for the homology of Σ so that the action of _τ_ is block-diagonal, with _|C| −_ 1 blocks of the form 

**==> picture [44 x 29] intentionally omitted <==**

LIPSHITZ AND OZSVÁTH 

6 

**==> picture [182 x 87] intentionally omitted <==**

Figure 1. **Real surfaces** . The involution on the surface is given by reflection across the vertical circles in the middle, except that the involution on the thin, shaded cylinders is the free involution with quotient a Möbius band. This surface has _|C|_ = 3, genus 14, and nonorientable quotient; the quotient is orientable if and only if there are no shaded cylinders. 

and the remaining blocks of the forms 

**==> picture [218 x 58] intentionally omitted <==**

(One can trade the former for two copies of the latter, but the former seem a little more natural for orientable quotients.) 

Fix a real surface (Σ _, τ_ ), a point _z_ on the fixed set of _τ_ , a vector _v ∈ Tz_ Σ, and an orientation-preserving diffeomorphism _ϕL_ : _− F_ ( _Z_ ) _→_ Σ for some pointed matched circle _Z_ . Then �[0 _,_ 1] _×_ Σ _, ϕL ⨿ τ ◦ ϕL,_ ( _t, p_ ) _�→_ (1 _− t, τ_ ( _p_ )) _,_ [0 _,_ 1] _× {z},_ [0 _,_ 1] _× v_ �, which we call a _real thick surface_ , is a prototypical real bordered 3-manifold. We call (Σ _, τ_ ) the _central real surface_ of the real thick surface. 

The orientations are, perhaps, a little confusing. The boundary orientation identifies _{_ 0 _}×_ Σ = _−_ Σ, so _ϕL_ is an orientation-preserving map _F_ ( _Z_ ) _→{_ 0 _}×_ Σ. On the other hand, _{_ 1 _} ×_ Σ = Σ, _ϕL_ is an orientation-reversing map from _F_ ( _Z_ ) to Σ, and _τ_ is an orientationreversing map from Σ to Σ, so _τ ◦ ϕL_ is an orientation-preserving map from _F_ ( _Z_ ) to _{_ 1 _}×_ Σ. 

**Definition 2.5.** _A_ real bordered Heegaard diagram _is an α-β-bordered Heegaard diagram H_ = (Σ _,_ _**α** ,_ _**β** ,_ **z** ) _(in the sense of [LOT11, Section 3.3]) together with an orientation-reversing involution τ_ : Σ _→_ Σ _such that_ 

REAL BORDERED FLOER HOMOLOGY 

7 

**==> picture [92 x 92] intentionally omitted <==**

Figure 2. **A real bordered Heegaard diagram.** This diagram (on the left) represents [0 _,_ 1] _× T_[2] with the involution induced by the reflection of _T_[2] with two fixed circles (as indicated on the right). 

- _τ exchanges the two boundary components of_ Σ _,_ 

- _τ_ ( _**α**_ ) = _**β** , and_ 

- _τ_ ( **z** ) = **z** _._ 

In particular, the boundary of a real bordered Heegaard diagram is an _α_ -pointed matched circle _Z_ = _∂LH_ and the _β_ -pointed matched circle _∂RH_ = _−Z[β]_ obtained by reversing the orientation of _Z_ and viewing the points as _β_ -endpoints rather than _α_ -endpoints. Some examples of real bordered Heegaard diagrams are shown in Figures 2, 11 and 12. 

An _α_ - _β_ -bordered Heegaard diagram _H_ specifies an arced bordered 3-manifold _Y_ ( _H_ ) by capping off the boundary components of Σ to obtain Σ, thickening the result to Σ _×_ [1 _,_ 2] and attaching 2-handles along the _α_ -circles in Σ _× {_ 1 _}_ and the _β_ -circles in Σ _× {_ 2 _}_ . The _α_ -arcs (respectively _β_ -arcs) induce a parametrization of the part of the boundary corresponding to Σ _× {_ 1 _}_ (respectively Σ _× {_ 2 _}_ ). (Compare [LOT11, Construction 3.17].) If we start with a real bordered Heegaard diagram, then the corresponding 3-manifold inherits an involution _τ_ induced from the involution _τ_ ( _p, t_ ) = ( _τ_ ( _p_ ) _,_ 3 _− t_ ) on Σ _×_ [1 _,_ 2]. The fixed sets of _τ_ : Σ _→_ Σ and _τ_ : _Y_ ( _H_ ) _→ Y_ ( _H_ ) are identified. 

_Example_ 2.6 _._ Figure 2 shows a real bordered Heegaard diagram for ([0 _,_ 1] _× T_[2] _, τ_ ) where _τ_ is induced from the involution _τ_ : _T_[2] _→ T_[2] as in Example 2.4 given by reflection across two circles (with orientable quotient). 

Figures 11 and 12 both show bordered Heegaard diagrams for [0 _,_ 1] _× T_[2] with connected fixed set and nonorientable quotient, as well as bordered Heegaard diagrams for [0 _,_ 1] _×_ Σ2 with connected fixed set and orientable quotient. Changing the pointed matched circle from the split one to the antipodal one gives Heegaard diagrams for [0 _,_ 1] _×_ Σ2 with connected fixed set and nonorientable quotient. See Section 5.2 for more discussion of these diagrams. 

We do not glue pairs of real bordered 3-manifolds together. Rather, given a real bordered 3-manifold _Y_ = ( _Y, ϕL ⨿ ϕR, γ, τ_ ), where _ϕL_ : _F_ ( _Z_ ) _→ ∂Y_ , and an (ordinary) arced bordered 3-manifold _Y[′]_ = ( _Y[′] , ϕ[′] L[, ϕ][′] R[, γ][′]_[)][with] _[ϕ][′] R_[:] _[−][F]_[(] _[Z]_[)] _[ →][∂Y][′]_[,][we][can][form][a][new][real][bordered] 3-manifold 

� _Y[′] ∪F_ ( _Z_ ) _Y ∪F_ ( _Z_ ) _Y[′] , ϕ[′] L[⨿][ϕ][′] L[, γ][′][ ∪][γ][ ∪][γ][′][,]_[ �] _[τ]_ � _,_ � � where _τ |Y_ = _τ_ and _τ |Y ′_ is the identity map exchanging the two copies of _Y[′]_ . (Note that, on both sides, we are gluing _∂RY[′]_ to _Y_ .) That is, we think of _Y_ as a cobordism _−F_ ( _Z_ ) _⨿ −F_ ( _Z_ ) _→∅_ , and compose with _Y[′] ⨿ Y[′]_ . 

LIPSHITZ AND OZSVÁTH 

8 

Similarly, given a real bordered Heegaard diagram ( _H, τ_ ) = (Σ _,_ _**α** ,_ _**β** ,_ **z** _, τ_ ) and an (ordinary) arced bordered Heegaard diagram _H[′]_ = (Σ _[′] ,_ _**α**[′] ,_ _**β**[′] ,_ **z** _[′]_ ) with _∂LH_ = _Z_ = _−∂RH[′]_ , we can form a new real bordered Heegaard diagram 

( _H[′] ∪Z H ∪Z_ ( _−H[′]_ ) _[β] ,_ � _τ_ ) = �Σ _[′] ∪_ Σ _∪_ ( _−_ Σ _[′]_ ) _,_ _**α**[′] ∪_ _**α** ∪_ _**β**[′] ,_ _**β**[′] ∪_ _**β** ∪_ _**α**[′] ,_ **z** _[′] ∪_ **z** _∪_ **z** _[′] ,_ � _τ_ � _,_ 

where ( _−H[′]_ ) _[β]_ is the _β_ - _β_ -bordered Heegaard diagram obtained by reversing the orientation of Σ and relabeling the _α_ -curves in _H_ as _β_ -curves and the _β_ -circles as _α_ -circles. The map _τ_ � is given by _τ_ on Σ and the (orientation-reversing) identity map Σ _[′] →−_ Σ _[′]_ . 

**Lemma 2.7.** _If_ ( _H, τ_ ) _is a real bordered Heegaard diagram representing a real bordered 3-manifold_ ( _Y_ ( _H_ ) _, τ_ ) _with boundary F_ ( _Z_ ) _⨿ F_ ( _Z_ ) _and H[′] is an arced bordered Heegaard diagram representing an arced bordered 3-manifold Y_ ( _H[′]_ ) _, then_ ( _H[′] ∪Z H ∪Z_ ( _−H[′]_ ) _[β] ,_ � _τ_ ) _represents_ � _Y[′] ∪F_ ( _Z_ ) _Y ∪F_ ( _Z_ ) _Y[′] ,_ � _τ_ � _._ 

_Proof._ This is immediate from the definitions. □ 

2.2. **States, domains, and** spin _[c]_ **-decomposition.** Recall that a _generator_ or _state_ in a bordered Heegaard diagram _H_ = (Σ _,_ _**α** ,_ _**β** , z_ ) (with one boundary component), where _**α**_ = _{α_ 1 _[c][, . . . , α] g[c] −k[, α]_ 1 _[a][, . . . , α]_ 2 _[a] k[}]_[and] _**[β]**_[=] _[ {][β]_[1] _[, . . . , β][g][}]_[,][is][a] _[g]_[-tuple] **[x]**[ =] _[ {][x][i][} ⊂]_ _**[α]**[ ∩]_ _**[β]**_[so][that] one point of **x** lies on each _β_ -circle, one point on each _α_ -circle, and at most one point on each _α_ -arc. In particular, exactly half of the _α_ -arcs are occupied by points in **x** . (In terms of spin _[c]_ -structures, this is the condition that _⟨c_ 1(s) _,_ [ _∂Y_ ] _⟩_ = 0.) We denote the set of states for _H_ by S( _H_ ). 

For _α_ - _β_ -bordered Heegaard diagrams, one can consider states where any number of _α_ -arcs are occupied, but most turn out to be irrelevant for Heegaard Floer homology of closed 3- manifolds. In a real _α_ - _β_ bordered Heegaard diagram ( _H, τ_ ), _**α**_ = _{α_ 1 _[c][, . . . , α] g[c] −k[, α]_ 1 _[a][, . . . , α]_ 2 _[a] k[}]_ and _**β**_ = _{β_ 1 _[c][, . . . , β] g[c] −k[, β]_ 1 _[a][, . . . , β]_ 2 _[a] k[}]_[contain][the][same][number][of][arcs.] If we glue an _α_ - bordered Heegaard diagram _H[′]_ (with connected boundary) to the _α_ -boundary of _H_ , then in a state for _H[′]_ , half of the _α_ -arcs are occupied. Hence, only states for _H_ in which _k α_ -arcs (that is, half of them) and _k β_ -arcs are occupied contribute to the (real) Heegaard Floer homology of the closed diagram. 

So, by a _real generator_ or _real state_ for ( _H, τ_ ) we mean a _g_ -tuple of points **x** = _{xi} ⊂_ _**α** ∩_ _**β**_ so that: 

- Every _α_ -circle and every _β_ -circle contain a point in **x** . 

- Exactly half of the _α_ -arcs and half of the _β_ -arcs contain a point in **x** (and each curve contains at most one point in **x** ). 

- The point **x** is fixed by _τ_ , _τ_ ( **x** ) = **x** . 

Let S _R_ ( _H, τ_ ) denote the set of real states for ( _H, τ_ ). 

Given **x** _,_ **y** _∈_ S( _H_ ) in a real bordered Heegaard diagram ( _H, τ_ ), a _domain_ from **x** to **y** is a linear combination _B_ of components of Σ _\_ ( _**α** ∪_ _**β**_ ) so that 

_∂_ [( _∂B_ ) _∩_ ( _**β** ∪ ∂R_ Σ)] = _−∂_ [( _∂B_ ) _∩_ ( _**α** ∪ ∂L_ Σ)] = **y** _−_ **x** 

and the region containing the arc **z** has coefficient 0 in _B_ . As usual, we denote the set of domains from **x** to **y** by _π_ 2( **x** _,_ **y** ). If _B ∈ π_ 2( **x** _,_ **y** ), then _τ∗_ ( _B_ ) _∈ π_ 2( _τ_ ( **y** ) _, τ_ ( **x** )). (Note that, since _τ_ is orientation-reversing on Σ, the coefficients of _τ∗_ ( _B_ ) are obtained by negating the coefficients of _B_ and applying _τ_ to them.) See Figure 3. 

Given real states **x** _,_ **y** _∈_ S _R_ ( _H, τ_ ), a _real domain_ from **x** to **y** is a domain _B ∈ π_ 2( **x** _,_ **y** ) so that _B_ = _−τ∗_ ( _B_ ). Let _π_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)][denote][the][set][of][real][domains][from] **[x]**[to] **[y]**[.] 

REAL BORDERED FLOER HOMOLOGY 

9 

A domain (or real domain) _B_ is _provincial_ if the coefficients of the regions adjacent to _∂_ Σ are all 0. 

A _real periodic domain_ is an element of _π_ 2 _[R]_[(] **[x]** _[,]_ **[ x]**[)][; the real periodic domains form a subgroup] of _π_ 2( **x** _,_ **x** ) _[∼]_ = _H_ 2( _Y, ∂Y_ ). Similarly, the provincial real periodic domains _π_ 2 _[∂,R]_ form a subgroup of the provincial periodic domains _π_ 2 _[∂]_[(] **[x]** _[,]_ **[ x]**[)] _[ ∼]_[=] _[ H]_[2][(] _[Y]_[ )][.][As][in][the][closed][case][[][GM25][,][Lemma] 3.19], these groups have simple topological interpretations: 

**Lemma 2.8.** _Fix a real bordered Heegaard diagram_ ( _H, τ_ ) _for a real bordered 3-manifold_ ( _Y, ϕL ⨿ ϕR, γ, τ_ ) _. There are canonical isomorphisms_ 

**==> picture [264 x 36] intentionally omitted <==**

_Proof._ Observe that the identification between periodic domains and _H_ 2( _Y, ∂Y_ ) intertwines the action of _τ∗_ on _π_ 2( **x** _,_ **x** ) (from the involution of the Heegaard surface) and the action of _τ∗_ on _H_ 2( _Y, ∂Y_ ) (from the involution of the 3-manifold). By definition, _π_ 2 _[R]_[(] **[x]** _[,]_ **[ x]**[)][ is the kernel] of 1 + _τ∗_ on _π_ 2( **x** _,_ **x** ), and hence the corresponding statement also holds for _H_ 2( _Y, ∂Y_ ). The proof for _π_ 2 _[∂,R]_ is similar. □ 

Following Guth-Manolescu, we will sometimes write 

**==> picture [282 x 15] intentionally omitted <==**

since this is the fixed set for the action of _−τ∗_ ; and similarly for other homology groups. 

Recall that a bordered Heegaard diagram is _admissible_ (respectively _provincially admissible_ ) if every periodic domain (respectively provincial periodic domain) has both positive and negative coefficients. Following Guth-Manolescu [GM25, Section 3.8]: 

**Definition 2.9.** _A real bordered Heegaard diagram_ ( _H, τ_ ) _is_ admissible _(respectively_ provincially admissible _) if H is admissible (respectively provincially admissible) as an ordinary bordered Heegaard diagram._ 

There is a familiar obstruction 

**==> picture [428 x 16] intentionally omitted <==**

to the existence of a domain from **x** to **y** , obtained by connecting **x** to **y** by a 1-chain _b_ in _**β** ∪ ∂R_ Σ and a 1-chain _a_ in _**α** ∪ ∂L_ Σ and considering the difference _b − a_ . As Guth-Manolescu observe [GM25, Section 3.4], in the real case there are two refinements of this construction: 

- (1) We may take _a_ = _τ∗_ ( _b_ ), so _ϵ_ ( **x** _,_ **y** ) lies in the kernel of (1 + _τ∗_ ): _H_ 1( _Y_ ) _/H_ 1( _∂Y_ ) _→ H_ 1( _Y_ ) _/H_ 1( _∂Y_ ). (In fact, they argue that, in the closed case, this lies in a further subgroup.) 

- (2) If _ϵ_ ( **x** _,_ **y** ) = 0, then there is a domain _B ∈ π_ 2( **x** _,_ **y** ). The element _B_ + _τ∗_ ( _B_ ) is a periodic domain ( _τ_ -invariant, not real), so we obtain an element 

**==> picture [104 x 13] intentionally omitted <==**

**==> picture [424 x 33] intentionally omitted <==**

Generalizing the closed case [GM25, Section 3.4], we have: 

**Lemma 2.10.** _The element ζ_ ( **x** _,_ **y** ) _is independent of the choice of B. Moreover, π_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)] _[ ̸]_[=] _∅ if and only if ϵ_ ( **x** _,_ **y** ) = 0 _and ζ_ ( **x** _,_ **y** ) = 0 _._ 

LIPSHITZ AND OZSVÁTH 

10 

**==> picture [74 x 205] intentionally omitted <==**

**==> picture [121 x 205] intentionally omitted <==**

Figure 3. **Domains and the obstruction** _ζ_ **.** Top left: a domain _B ∈ π_ 2( **x** _,_ **y** ). Top right: the domain _τ∗_ ( _B_ ). Bottom left: a state for the space of real periodic domains in this diagram; as an element of _π_ 2( **y** _,_ **y** ), in fact, this domain has a holomorphic representative. Bottom right: the obstruction _ζ_ ( **x** _,_ **y** ) is the periodic domain _B_ + _τ∗_ ( _B_ ). Note that this is not a real periodic domain: it is fixed by _τ∗_ , not _−τ∗_ . 

_Proof._ For the first statement, any other choice of domain can be written as _B_ + _P_ where _P_ is a periodic domain. Then 

**==> picture [260 x 13] intentionally omitted <==**

and hence differs from _B_ + _τ∗_ ( _B_ ) by an element of the image of 1 + _τ∗_ . 

If _π_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)][=] _[∅]_[,][then] _[π]_[2][(] **[x]** _[,]_ **[ y]**[)][=] _[∅]_[,][so] _[ϵ]_[(] **[x]** _[,]_ **[ y]**[)][=][0][and,][by][using][an][element][of] _[π]_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)] to define _ζ_ ( **x** _,_ **y** ), _ζ_ ( **x** _,_ **y** ) = 0. Conversely, suppose _ϵ_ ( **x** _,_ **y** ) = 0 and _ζ_ ( **x** _,_ **y** ) = 0. Write _B_ + _τ∗_ ( _B_ ) = (1 + _τ∗_ )( _P_ ) for some periodic domain _P_ . Then (1 + _τ∗_ )( _B − P_ ) = 0, so _B − P ∈ π_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)][,][as][desired.] □ 

Call states **x** and **y** _real_ spin _[c] -equivalent_ if _π_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)] _[ ̸]_[=] _[ ∅]_[.] 

_Example_ 2.11 _._ Fix a real surface (Σ _, τ_ ) and an orientation-preserving diffeomorphism _ϕL_ : _− F_ ( _Z_ ) _→_ Σ, and consider the real bordered manifold [0 _,_ 1] _×_ Σ from Example 2.4. Fix a real bordered Heegaard diagram ( _H, τ_ ) representing ([0 _,_ 1] _×_ Σ _, τ_ ). We have _H_ 1([0 _,_ 1] _×_ Σ) _/H_ 1( _{_ 0 _,_ 1 _} ×_ Σ) = 0, so the obstruction class _ϵ_ ( **x** _,_ **y** ) vanishes identically and every pair of states can be connected by a domain. (Recall that we are only considering the central spin _[c]_ -structure—the one with _c_ 1(s) = 0.) The long exact sequence for the pair gives 

**==> picture [338 x 13] intentionally omitted <==**

i.e., 

**==> picture [364 x 18] intentionally omitted <==**

REAL BORDERED FLOER HOMOLOGY 

11 

Thus, _H_ 2(Σ _×_ [0 _,_ 1] _,_ Σ _×{_ 0 _,_ 1 _}_ ) = _{_ ( _x, −x_ ) _| x ∈ H_ 1(Σ) _}_ , with the action given by _τ∗_ ( _x, −x_ ) = ( _−τ∗_ ( _x_ ) _, τ∗_ ( _x_ )). So, the space of real periodic domains is 

**==> picture [422 x 35] intentionally omitted <==**

Finally, the obstruction _ζ_ lies in ker(1 _− τ∗_ ) _/_ Im(1 + _τ∗_ ). Again, from Example 2.4, this is (Z _/_ 2Z) _[|][C][|−]_[1] . For example, for the diagrams AZ( _Z_ ) and AZ( _Z_ ) discussed in Section 5.2, _ζ_ lies in a trivial group, hence vanishes identically. For the diagram in Figure 3, _ζ_ ( **x** _,_ **y** ) _∈_ Z _/_ 2Z (and, for the states marked in that diagram, is the nontrivial element). 

## 3. Moduli spaces 

3.1. **Definitions of the moduli spaces.** We briefly recapitulate the definitions of the bordered moduli spaces, but now imposing the symmetry relevant to the real case. The material in this section is a straightforward synthesis of the original bordered moduli spaces [LOT18] and Guth-Manolescu’s real Floer moduli spaces, though we give somewhat complementary details to the ones given in their paper [GM25]. 

Fix a real bordered Heegaard diagram ( _H, τ_ ) = (Σ _,_ _**α** ,_ _**β** ,_ **z** _, τ_ ). There is an induced map 

**==> picture [174 x 13] intentionally omitted <==**

given by 

**==> picture [133 x 13] intentionally omitted <==**

We consider almost complex structures _J_ on Σ _×_ [0 _,_ 1] _×_ R satisfying the usual conditions from bordered Floer theory [LOT18, Definition 5.1] and the additional condition that _τ_ is _J_ -anti-holomorphic, i.e., 

**==> picture [90 x 9] intentionally omitted <==**

We call such almost complex structures _J symmetric almost complex structures_ . 

Write _∂LH_ = _Z_ , so _∂RH_ = _−Z[β]_ . Fix a symmetric almost complex structure _J_ . We consider two kinds of moduli spaces of _J_ -holomorphic maps: 

- Moduli spaces _M[B] R_[(] **[x]** _[,]_ **[ y]**[;] _[ S][▷]_[;] _[ P]_[)][,][where] _[S][▷]_[is][a][given][decorated][Riemann][surface] (see [LOT18, Definition 5.2]) and _P_ is an ordered partition of the _e_ punctures of _S[▷]_ . This is the subspace of the bordered moduli space _M[B]_ ( **x** _,_ **y** ; _S[▷]_ ; _P_ ) [LOT18, Definition 5.5] given by holomorphic maps _u_ : _S →_ Σ _×_ [0 _,_ 1] _×_ R such that there exists an anti-holomorphic involution _η_ : _S → S_ with _τ ◦ u_ = _u ◦ η_ . (Since _u_ is nonconstant on every component of _S_ [LOT18, Condition (M-5)], if _η_ exists, then it is unique.) 

For real curves, punctures necessarily come in pairs, of one puncture mapped to _∂LH_ and one mapped to _∂RH_ . If we are imposing no (other) height constraints, we could view the real moduli space as a subspace of _M[B]_ ( **x** _,_ **y** ; _S[▷]_ ; _P_ ) where _P_ is discrete, or where each part in _P_ has a pair of punctures exchanged by _η_ . We will take the former view, and in general view _P_ as a pair of partitions, one of the punctures mapped to _∂LH_ and the other of punctures mapped to _∂RH_ . (This is similar to the construction of bordered bimodules [LOT15], where we do not impose constraints between punctures on different boundary components.) In particular, for the construction of _CFDR_[�] , we are only interested in the case that _P_ is the discrete partition. (The proof of the structure equation—specifically, Case 3 of Proposition 3.12—involves partitions _P_ where one part has two elements. If we were to construct _CFAR_[�] , more general partitions would be needed.) 

LIPSHITZ AND OZSVÁTH 

12 

- Moduli spaces _M[B] R_[(] **[x]** _[,]_ **[ y]**[;] _[ ⃗ρ]_[)][of][embedded][holomorphic][curves.][These][are][subspaces] of the moduli spaces _M[B]_ ( **x** _,_ **y** ; _⃗_ _**ρ**_ ) [LOT18, Definition 5.68]. Here, _⃗ρ_ = ( _ρ_ 1 _, . . . , ρn_ ) _⃗_ 

- is a sequence of chords in _Z_ and _**ρ**_ = ( _{ρ_ 1 _, τ_ ( _ρ_ 1) _}, . . . , {ρn, τ_ ( _ρn_ ) _}_ ). The subspace _M[B] R_[(] **[x]** _[,]_ **[ y]**[;] _[ ⃗ρ]_[)][consists][of][curves] _[u]_[so][that][the][image][of] _[u]_[is][preserved][by] _[τ]_ (or, equivalently, there is an anti-holomorphic automorphism of the source that _u_ intertwines with _τ_ ). More consistent with viewing _P_ as discrete in the previous point, we can view _M[B] R_[(] **[x]** _[,]_ **[ y]**[;] _[ ⃗ρ]_[)][as][a][subspace][of] _[M][B]_[(] **[x]** _[,]_ **[ y]**[;] _[ ⃗ρ]_[;] _[ ⃗ρ]_[)][from][the][construction][of][bimod-] ules [LOT15, Section 6.3]. (We will not, in fact, make use of either embedding below.) 

Given a decorated surface _S[▷]_ , we can also consider maps _ϕ_ : _S →_ Σ _×_ [0 _,_ 1] _×_ R respecting the decorations, but which are merely smooth, not _J_ -holomorphic. By a _real smooth map_ from _S[▷]_ we mean such a smooth map _ϕ_ together with an orientation-reversing, smooth involution _η_ : _S → S_ so that _ϕ ◦ η_ = _τ ◦ ϕ_ . Call a symmetric almost complex structure _J generic_ if the moduli spaces _M[B] R_[(] **[x]** _[,]_ **[ y]**[;] _[ S][▷]_[;] _[ P]_[)][are][transversely][cut][out][inside][the][space][of][all] real smooth maps respecting the decorations and the partition _P_ , for all choices of decorated Riemann surface _S[▷]_ and all ordered partitions _P_ . 

Of course, we can also talk about real maps of other regularity, and in particular real versions of the weighted Sobolev spaces _Wδ_[1] _[,p]_ used in [LOT18, Section 5.2]. Fix a smooth surface _S_ (with boundary and punctures) and a smooth involution _η_ : _S → S_ . We have a space _B[R]_ , with objects triples ( _j, J, u_ ) of a symmetric almost complex structure _j_ on ( _S, η_ ), a symmetric almost complex structure _J_ on (Σ _×_ [0 _,_ 1] _×_ R _, τ_ ) (as above), and a real _Wδ_[1] _[,p]_[-map] _u_ : _S →_ Σ _×_ [0 _,_ 1] _×_ R. Dropping the equivariance conditions gives a map _B[R] →B_ . Over _B[R]_ , we have a bundle _E[R]_ of (0 _,_ 1)-forms _α_ on _S_ valued in _u[∗] T_ (Σ _×_ [0 _,_ 1] _×_ R), satisfying (3.1) _α_ = _dτ ◦ α ◦ dη._ 

There is a projection from _B[R]_ to the space of (real) almost complex structures on Σ _×_ [0 _,_ 1] _×_ R; let _BJ[R]_[denote][the][fiber][over] _[J]_[(i.e.,][the][space][of][tuples][(] _[S, η, j, u]_[)][).][Similarly,][if][we][hold] _[j]_ and _J_ fixed, we have a subspace we denote _BJ,j[R]_[.][The] _[∂]_[¯][-operator][is][a][section] _[B][→E]_[,][and] its linearization is a bundle map _T B[R] →E[R]_ . More precisely, this linearization is defined canonically when _∂_[¯] ( _u_ ) = 0. At other points in _B[R]_ , it depends on a choice of projection _T E[R] →E[R]_ . We can use _J_ and the standard symplectic form to induce a metric and then such a projection, which gives the formula 

**==> picture [354 x 16] intentionally omitted <==**

[MS04, Proposition 3.1.1], where _∇_ is the Levi-Civita connection, and 

**==> picture [144 x 15] intentionally omitted <==**

The space _E[R]_ is a subspace of the space _E|BR_ where we drop Condition 3.1, and _E|BR_ inherits an involution _α �→ dτ ◦ α ◦ dη_ . Similarly, when _u_ is a real curve, the space _TuBJ,j[R]_ inherits an involution _ξ �→ dτ ◦ ξ ◦ dη_ . Denote both of these involutions by _τ_ . 

**Lemma 3.3.** _For any real map u, the operator Du∂_[¯] : _TuB →E from Equation_ (3.2) _satisfies Du∂_[¯] = _τ ◦ Du∂_[¯] _◦ τ . In particular, Du∂_[¯] _sends T BJ,j[R][to][E][R][.][Moreover,][for][any][real][u][and] symmetric J, this induced map Du∂_[¯] : _TuBJ,j[R][→E] J,j,u[R][is][Fredholm.]_ 

_Proof._ We can check the first statement directly, or observe that this linearization depends only on the Riemannian metrics induced by the symplectic forms and almost complex structures on _S_ and Σ _×_ [0 _,_ 1] _×_ R. Since 

**==> picture [272 x 15] intentionally omitted <==**

REAL BORDERED FLOER HOMOLOGY 

13 

( _ω, J_ ) and ( _−ω, J_ ) induce the same Riemannian metrics, hence the linearization is necessarily _τ_ -equivariant. 

The fact that _Du∂_[¯] sends _TuBJ,j[R]_[to] _[E] J,j,u[R]_[follows:] _[T][u][B] J,j[R]_[and] _[E] J,j,u[R]_[are][the][1][-eigenspaces][of] _τ_ on _TuBJ,j_ and _EJ,j,u_ , respectively, and since _Du∂_[¯] intertwines the operators _τ_ , it respects the _τ_ eigenspaces. 

Finally, to see this induced map is Fredholm, the kernel of _Du∂_[¯] : _TuBJ,j[R][→E] J,j,u[R]_[is][a][sub-] space of the kernel of _Du∂_[¯] : _TuBJ,j →EJ,j,u_ , and since the latter map is Fredholm, the kernel is finite-dimensional. For the cokernel, since _TuBJ,j_ is the sum of the _−_ 1 and 1-eigenspaces of _τ_ , _Du∂_[¯] preserves these eigenspaces, and the cokernel of _Du∂_[¯] is finite-dimensional, the induced map between 1-eigenspaces must also have finite-dimensional cokernel. □ 

**Proposition 3.4.** _For any real bordered Heegaard diagram H, there exist generic symmetric almost complex structures._ 

_Proof._ This is a combination of the arguments in the bordered case [LOT18, Proposition 5.6] and the closed real case [GM25, Proposition 2.2]. As usual, the main step is to prove that for any ( _j, J, u_ ) _∈B[R]_ with _∂_[¯] _J,j_ ( _u_ ) = 0, the linearized map _Du∂_[¯] : _TJ,j,uB[R] →EJ,j,u[R]_[is][surjective.] The proof proceeds one connected component of _S_ at a time. For trivial strips, the statement is clear. So, let _S_ 0 be a connected component which is not a trivial strip. Choose a point ( _p, s_ ) _∈_ Σ _×_ [0 _,_ 1] so that _u[−]_[1] (( _p, s_ ) _×_ R) consists of a single point on _S_ 0, and that point is a regular point for _π_ Σ _◦ u_ and _πD ◦ u_ (cf. [Lip06, Lemma 3.3]). As in the usual proof of transversality for cylindrical Heegaard Floer homology [Lip06, Proposition 3.7], suppose some nontrivial _ζ_ in ( _EJ,j,u[R]_[)] _[∗]_[vanishes][on][the][image][of] _[D][u]_[ ¯] _[∂]_[.][(In][[][Lip06][,][Proposition][3.7],] _ζ_ is denoted _η_ , but we are using _η_ above for the involution on _S_ .) Since we can achieve transversality for the _∂_[¯] -operator via a nonequivariant perturbation, there is either: 

- A vector field _ξ_ along _u_ so that � _S[⟨][ζ, D][u][ξ][⟩̸]_[= 0][or] 

- A perturbation _Ys_ of _J_ so that � _S[⟨][ζ, Y][s][ ◦][du][ ◦][j][⟩̸]_[= 0][or] 

- _•_ A perturbation _Y_ of _j_ so that � _S[⟨][ζ, J][◦][du][ ◦][Y][ ⟩̸]_[= 0][.] 

(As in [Lip06, Proof of Proposition 3.7], we are thinking of _ζ_ as a (0 _,_ 1)-form on _S_ valued in _u[∗] TX_ , so the pairing with the image of _Du∂_[¯] is the integral of the dot product.) Of course, these perturbations are not symmetric. 

Suppose we are in the first case. Replace _ξ_ by _ξ_ + _dτ ◦ ξ ◦ dη_ . Then 

**==> picture [434 x 60] intentionally omitted <==**

This contradicts the fact that _ζ_ annihilates the image of _Du_ . The second case is similar, replacing _Ys_ by _Ys_ + _dτ ◦ Ys ◦ dτ_ , and the third is similar, but replacing _Y_ by _dη ◦ Y ◦ dη_ . The result follows. □ 

For computations, it is typically more convenient to work with a split complex structure, and instead perturb the _α_ - and _β_ -curves. Following Oh [Oh96], Ozsváth-Szabó [OSz04, Proposition 3.9] gave conditions under which such perturbations are sufficient in the closed case (see also [Lip06, Lemma 3.10]). Here is a formulation in the real bordered case: 

LIPSHITZ AND OZSVÁTH 

14 

**Proposition 3.5.** _Fix a real bordered Heegaard diagram H, a real domain B ∈ π_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)] _[,] and a sequence of Reeb chords ⃗ρ. Suppose that, for some split complex structure, every holomorphic representative u_ : _S →_ Σ _×_ [0 _,_ 1] _×_ R _of B has the property that for each component S_ 0 _of S which is not a trivial strip, there is an open subset U of some α-curve in_ Σ _so that_ 

**==> picture [197 x 16] intentionally omitted <==**

_is a diffeomorphism (equivalently, bijection). Then for a small, generic perturbation of_ _**α** , and corresponding perturbation of_ _**β** , the real moduli space M[B] R_[(] **[x]** _[,]_ **[ y]**[;] _[ ⃗ρ]_[)] _[is][transversely][cut] out._ 

_In particular, if S has either a single nontrivial component or two nontrivial components exchanged by η, and there is an arc in_ _**α** so that the coefficient of B on one side is_ 0 _and on the other side is_ 1 _, then this hypothesis holds and, for any generic perturbation of_ _**α** , M[B] R_[(] **[x]** _[,]_ **[ y]**[;] _[ ⃗ρ]_[)] _[is][transversely][cut][out.]_ 

_Proof._ The proof is a simple modification of the unreal case, along the lines of Proposition 3.4, and is left to the reader. □ 

Proposition 3.5 will be used every time we perform explicit computations of moduli spaces, though we may not always mention it. 

3.2. **Expected dimensions.** Recall that there are two versions of the index formula in bordered Heegaard Floer homology: a _source-dependent index formula_ , 

**==> picture [120 x 13] intentionally omitted <==**

[LOT18, Proposition 5.8] that does not assume curves are embedded and rather depends on the topology of the source _S_ , and an _embedded index formula_ 

**==> picture [178 x 13] intentionally omitted <==**

[LOT18, Definition 5.68] for the moduli spaces of embedded curves. Here, _P_ is the partition of the _e∞_ punctures of _S_ induced by the R-coordinate of Σ _×_ [0 _,_ 1] _×_ R, so _|P |_ is the number of _e∞_ punctures minus the number of height constraints. Since we are considering type _D_ structures, _|P |_ agrees with the number of Reeb chords _|⃗ρ|_ . (Having two notations for the same quantity is an artifact of how the properties of these moduli spaces were laid out.) 

Let ind _[R]_ denote the expected dimension of the real moduli spaces. Guth and Manolescu show that, for closed Heegaard diagrams, this expected dimension at a real domain _B ∈ π_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)][is][given][by] 

**==> picture [348 x 25] intentionally omitted <==**

where ind( _B_ ) = _e_ ( _B_ ) + _n_ **x** ( _B_ ) + _n_ **y** ( _B_ ) is the expected dimension of the ordinary Heegaard Floer moduli space and _σ_ ( _**α** ,_ **y** ) is the sum over the points _yi_ in **y** that are fixed by the involution of a local contribution that depends on the cyclic order of _**α**_ , _**β**_ , and the fixed set at _yi_ : 

**==> picture [288 x 71] intentionally omitted <==**

REAL BORDERED FLOER HOMOLOGY 

15 

[GM25, Section 4.2]. The analogous results in the bordered case are: 

**Proposition 3.7.** _The expected dimension of the real moduli space with a fixed source S and the expected dimension for embedded curves are given by_ 

**==> picture [448 x 36] intentionally omitted <==**

_respectively. Here, g is the number of −∞ corners, ⃗ρ is the sequence of α-Reeb chords (as in the notation M[B] R_[(] **[x]** _[,]_ **[ y]**[;] _[ ⃗ρ]_[)] _[from][Section][3.1][),][and][|][P][|]_[ = 2] _[|][⃗ρ][|][is][the][number][of][punctures][of] P not mapped to ±∞._ 

_In particular, the Euler characteristic of a real embedded curve is given by the same formula as in the ordinary case,_ 

**==> picture [356 x 13] intentionally omitted <==**

_Proof._ The computation of the embedded Euler characteristic in our previous paper [LOT18, Proposition 5.69] did not make any assumptions on transversality. So, since real holomorphic curves are special cases of unreal holomorphic curves, the embedded Euler characteristic is given by Formula (3.10). Thus, to prove Proposition 3.7, it suffices to prove Formula (3.8). (Recall that Formula (3.8) is a version of Rasmussen’s index formula [Ras03, Theorem 9.1], but in the real bordered setting.) 

Write _X_ = Σ _×_ [0 _,_ 1] _×_ R and _L_ = ( _**α** × {_ 1 _} ×_ R) _∪_ ( _**β** × {_ 0 _} ×_ R). Fix a real smooth map _u_ : _S →_ Σ _×_ [0 _,_ 1] _×_ R in the homology class _B_ . We have a complex vector bundle _u[∗] TX_ over _S_ , and real subbundle _u[∗] TL_ over _∂S_ . The involution _η_ : _S → S_ is covered by an involution _τ_ : ( _u[∗] TX, u[∗] TL_ ) _→_ ( _u[∗] TX, u[∗] TL_ ); on _u[∗] TX_ this is complex anti-linear. The real index of _Du∂_[¯] is the same as the index of the _∂_[¯] -operator for real sections of ( _u[∗] TX, u[∗] TL_ ). In particular, the only role of _u_ and _B_ is to determine this complex bundle and the real subbundles. So, given a complex 2-dimensional vector bundle _E_ over _S_ , totally real subbundles _F_ over _∂S_ , and involutions _τ_ of these covering _η_ , write ind _[R]_ ( _S, E, F, τ_ ) for the index of the _∂_[¯] -operator on real sections. 

We prove by induction on the complexity of _S_ that 

**==> picture [380 x 16] intentionally omitted <==**

If _S_ consists of a single bigon (and _τ_ is reflection), then this is a special case of GuthManolescu’s computation [GM25, Section 2.3]. If _S_ consists of two components exchanged by _τ_ , then it is clear that the real index is half the ordinary one (and the _σ_ terms vanish). If _S_ is a 2-sphere, _τ_ fixes a circle, and the bundle _E_ over _S_ is trivial, then ind( _S, E, F_ ) = 4 (the 4-dimensional space of constant maps _S_[2] _→_ C[2] ) and ind _[R]_ ( _S, E, F_ ) = 2 (the conjugationinvariant ones, i.e., the constant maps to R[2] ). The same holds if _τ_ is the fixed point-free involution of the 2-sphere, and _E_ is trivial. In particular, Formula (3.11) holds in both of these cases. 

We can reduce any _S_ to a union of surfaces of these four types by cutting along pairs of circles (respectively arcs) exchanged by _τ_ . More precisely, given a pair of disjoint circles _Z, Z[′] ⊂ S_ with _τ_ ( _Z_ ) = _Z[′]_ , fix a trivialization of _E_ over _Z ∪ Z[′]_ . Surgering _S_ along _Z ∪ Z[′]_ gives a surface _S[′]_ . Using the trivializations, _E_ induces a bundle _E[′]_ over _S[′]_ . This operation increases ind( _S, E, F_ ) by 4 and ind _[R]_ ( _S, E, F, τ_ ) by 2: each surgery is equivalent to splicing ( _S, E, F_ ) with a trivial vector bundle over a 2-sphere (see, for instance, the nice explanation in [EGH00, Section 1.8.2]). Similarly, given a pair of disjoint arcs _A, A[′]_ exchanged by _τ_ , 

LIPSHITZ AND OZSVÁTH 

16 

with boundary on _∂S_ , after fixing a trivialization of _E_ along _A_ extending a trivialization of _F_ on _∂A_ , surgering along _A ∪ A[′]_ gives a new surface _S[′]_ and vector bundles _E[′] , F[′]_ and ind _[R]_ ( _S[′] , E[′] , F[′] , τ[′]_ ) = ind _[R]_ ( _S, E, F, τ_ ) + 1 while ind( _S[′] , E[′] , F[′]_ ) = ind( _S, E, F_ ) + 2. (This is splicing with a pair of disks; see, for instance, [ENS02, Section 8.1].) In particular, both sides of Equation (3.11) change in the same way under these operations. Since we can use them to reduce to the base cases considered above, the proposition follows. □ 

3.3. **Codimension-1 degenerations.** The following result about the boundary of the 2- dimensional real moduli spaces is essentially equivalent to the fact that _CFDR_[�] ( _H, τ_ ) satisfies the type _D_ structure relation: 

**Proposition 3.12.** _Fix a real bordered Heegaard diagram_ ( _H, τ_ ) _with ∂LH_ = _Z, and a generic symmetric almost complex structure J. Given_ **x** _,_ **y** _∈_ S _R_ ( _H, τ_ ) _, B ∈ π_ 2( **x** _,_ **y** ) _, and a sequence of Reeb chords ⃗ρ (compatible with B) so that_ ind _[R]_ ( _B, ⃗ρ_ ) = 2 _, the sum of the following numbers is even:_ 

- _(1) The number of real 2-story holomorphic curve ends, i.e., elements of_ 

**==> picture [222 x 45] intentionally omitted <==**

**==> picture [268 x 13] intentionally omitted <==**

**==> picture [258 x 28] intentionally omitted <==**

_where ⃗ρ_ = ( _ρ_ 1 _, . . . , ρn_ ) _._ 

_(3) The number of collisions of levels, i.e., elements of_ 

**==> picture [230 x 26] intentionally omitted <==**

_Here, ρiρi_ +1 _denotes the concatenation of the chords if they are composable, and the two-element set {ρi, ρi_ +1 _} otherwise._ 

_Proof._ This follows from essentially the same arguments as in the unreal case [LOT18, Theorem 5.61], which we recall. 

The first step is to observe that the moduli spaces have compactifications in terms of holomorphic combs [LOT18, Proposition 5.24]. Since the real moduli spaces are subspaces of the usual ones, and this statement does not rely on transversality, the compactness result for the real moduli spaces, via _real holomorphic combs_ , follows from the usual one. 

We then prove several gluing results [LOT18, Section 5.5], for 2-story buildings and certain 1-story combs with curves at _e∞_ . The proofs (which are largely omitted) carry over without change to the real case. In particular, if one starts with a two-story building in which both stories are _τ_ -invariant, the pre-glued approximately holomorphic curves are also _τ_ -invariant, and applying the inverse function theorem to the configuration space of real maps gives real holomorphic curves. Similarly, pre-gluing a symmetric pair of _e∞_ curves on _∂L_ Σ and _∂R_ Σ to a real curve, with the same gluing parameter on the two sides, again gives an approximately holomorphic real curve, and applying the inverse function theorem in the real configuration space gives a real holomorphic curve. 

REAL BORDERED FLOER HOMOLOGY 

17 

The first restrictions on codimension-1 degenerations [LOT18, Proposition 5.43] come from the index formula—the unreal analogue of Formula (3.8). In the real case, the analogous proposition says that the boundary of the index-2 moduli spaces consists of two-story buildings; degenerations at _e∞_ consisting of a join curve at each boundary component; degenerations of some split curves; and nodal curves where some arcs degenerate. (Shuffle curves do not appear because our moduli spaces do not have height constraints between the Reeb chords, or at least not between ones on the same boundary component.) We review the part of that argument that used the index formula; the following discussion assumes the reader is consulting that proof simultaneously. 

Since we are considering an index-2 real moduli space, 

**==> picture [285 x 16] intentionally omitted <==**

As there, since _χ_ ( _S[′]_ ) _≥ χ_ ( _S_ ) and _|P[′] | ≤|P |_ , ind( _B, S[′] , P[′]_ ) _≤_ ind( _B, S, P_ ). If a holomorphic comb has more than one story, the main component of each story has index _≥_ 1. So, there are at most two stories. If there are two stories with index 1 each, then the same argument as in the unreal case implies there are no curves at _e∞_ . Similarly, if ind _[R]_ ( _B, S[′] , P[′]_ ) = 2, then there is no curve at _e∞_ . 

So, suppose we have a single story with ind _[R]_ ( _B, S[′] , P[′]_ ) = 1 and some curves at _e∞_ . Curves at _e∞_ come in pairs; write _T[′]_ = _TL[′][∪][T] R[ ′]_[.][Similarly,] _[ |][P][|−|][P][ ′][|]_[ is even, and the] _[ σ]_[-terms in the] formula are the same for ( _B, S, P_ ) and ( _B, S[′] , P[′]_ ). Thus, either _|P |_ = _|P[′] |_ and _χ_ ( _T[′]_ ) = _m−_ 2 or _|P[′] |_ = _|P | −_ 2 and _χ_ ( _T[′]_ ) = _m_ . The former case is a join curve and the latter is a collision of levels (possibly including a pair of split curves). 

The next step in the unreal case is ruling out boundary degenerations and other nodal degenerations [LOT18, Lemmas 5.47, 5.48, and 5.56]; those arguments are the same in the real case. Combining these restrictions with the gluing results gives the proposition, just as in the unreal case [LOT18, Proof of Theorem 5.61]. □ 

## 4. Real bordered modules 

With the moduli spaces in hand, the definition of the real bordered Floer invariants is the same as the original definition of _CFD_[�] , except with the real states and moduli spaces in place of the usual ones. 

**Definition 4.1.** _Let_ ( _H, τ_ ) _be a provincially admissible real bordered Heegaard diagram, with α-boundary Z and a generic symmetric almost complex structure J. Let CFDR_[�] ( _H, τ_ ) _be the left type D structure over A_ ( _−Z_ ) _defined as follows. As an_ F2 _-vector space, CFDR_[�] ( _H, τ_ ) _has basis_ S _R_ ( _H, τ_ ) _. The left idempotent of a state_ **x** _∈_ S _R_ ( _H, τ_ ) _is the set of α-arcs not containing points on_ **x** _, viewed as a subset of the matched pairs of −Z (which are the same as the matched pairs in Z, i.e., the α-arcs). The differential is defined by_ 

**==> picture [273 x 38] intentionally omitted <==**

_where, if ⃗ρ_ = ( _ρ_ 1 _, . . . , ρn_ ) _, then a_ ( _−⃗ρ_ ) = _a_ ( _−ρ_ 1) _· · · a_ ( _−ρn_ ) _, and −ρi is the chord in −Z corresponding to ρi ⊂ Z (the same subset of the circle, but viewed as having the opposite orientation)._ 

LIPSHITZ AND OZSVÁTH 

18 

**Lemma 4.2.** _The sum defining δ_[1] _is finite, and if H is admissible, then_ ( _CFDR_[�] ( _H, τ_ ) _, δ_[1] ) _is a bounded type D structure (in the sense of [LOT18, Section 2.3])._ 

_Proof._ The proof is the same as in the unreal case [LOT18, Lemma 6.5]. □ 

**Theorem 4.3.** _Definition 4.1 defines a type D structure. That is, δ_[1] _satisfies the type D structure relation._ 

_Proof._ Except that the moduli spaces have a different meaning, Proposition 3.12 is the same as the type _D_ case of the corresponding result in the unreal case [LOT18, Theorem 5.61]. (The unreal case also mentions shuffle curve degenerations, but these only occur when the partition has parts consisting of more than one Reeb chord, and the type _D_ invariant does not consider such partitions.) The results on boundary monotonicity [LOT18, Lemma 6.8 and 6.9] still hold (with the same proofs). The restrictions that collisions of levels must be composable and join curves correspond to valid splittings [LOT18, Lemma 5.77] follow from the embedded index formula (3.9) exactly as in the unreal case: non-composable collisions and invalid splittings drop _|⃗ρ|_ + _ι_ ( _⃗ρ_ ) by more than 1. (These terms are the same as in the unreal index formula, not multiplied by 1 _/_ 2.) So, this follows from exactly the same argument as in the unreal case [LOT18, Proposition 6.7]. □ 

While we do not prove invariance of _CFDR_[�] , we do record that it is independent of the choice of almost complex structure, and hence is an invariant of the real bordered Heegaard diagram: 

**Proposition 4.4.** _Fix a provincially admissible real bordered Heegaard diagram H and generic symmetric almost complex structures J, J[′] . Then the type D structures CFDR_[�] ( _H_ ; _J_ ) _and CFDR_[�] ( _H_ ; _J[′]_ ) _computed with respect to J and J[′] are homotopy equivalent. Proof._ Like the proof of Theorem 4.3, this is a straightforward adaptation of the closed case [LOT18, Section 6.3.1], and is left to the reader. □ 

4.1. **An example.** Consider the bordered Heegaard diagram from Figures 2 and 3, representing [0 _,_ 1] _× T_[2] with involution induced by the reflection on _T_[2] (with two fixed circles). We have _π_ 2( **x** _,_ **x** ) = _π_ 2( **y** _,_ **y** ) = Z, with generator _P_ as shown in Figure 3. Since _ϵ_ ( **x** _,_ **y** ) is the nontrivial element of Z _/_ 2Z (see Example 2.11), the only possible contributions to the differential on _CFDR_[�] ( _H_ ) are real periodic domains. Only domains all of whose coefficients at the boundary are 0 or 1 contribute to the differential on _CFDR_[�] ( _H_ ), because of the form of _A_ ( _T_[2] ). Thus, the only domain to consider is the domain _P_ . By Proposition 3.5, we may compute the contribution of _P_ using a split almost complex structure (and generic perturbation of _**α**_ ). Viewed as an element of _π_ 2( **x** _,_ **x** ), _P_ clearly has no holomorphic representative. Viewed as an element of _π_ 2( **y** _,_ **y** ), a real holomorphic representative of _P_ corresponds to a pair of slits starting at **y** , in some direction along the _α_ -arc and the corresponding direction along the _β_ -arc, and then a degree-1 holomorphic map to [0 _,_ 1] _×_ R[2] from the result. Thus, the result must be a disk. There is exactly one way to achieve that: for the slits to cut out the boundary. The result is an operation _δ_[1] ( **y** ) = _ρ_ 1 _ρ_ 2 _⊗_ **y** (in the usual notation for the torus algebra). To summarize: 

**==> picture [330 x 17] intentionally omitted <==**

REAL BORDERED FLOER HOMOLOGY 

19 

## 5. Real-nice diagrams and the real Auroux-Zarev piece 

In this section, we discuss an extension of Sarkar-Wang’s notion of nice diagrams [SW10] to real bordered Heegaard diagrams. In Section 5.1 we formulate the definition of real nice diagrams and show that holomorphic curve counts in such diagrams are combinatorial. (Substantially more domains contribute than in the unreal case; see Figure 4.) In Section 5.2, we recall two nice diagrams that will be used in our computation of real Floer homology, the Auroux-Zarev diagrams. Their bordered Floer invariants are recalled in Section 5.3, before we compute their real analogues in Section 5.4. 

## 5.1. **Real-nice diagrams and their real bordered invariants.** 

**Definition 5.1.** _A real bordered Heegaard diagram H is_ real-nice _if all the regions in H not containing the basepoint are bigons or rectangles (an edge of which may be on ∂_ Σ _) and for all points x in_ _**α** ∩ C, σ_ ( _x_ ) _has the same value (i.e., either σ_ ( _x_ ) _is always_ 1 _or is always −_ 1 _). If σ_ ( _x_ ) _is identically_ 1 _, call the diagram_ positive real-nice _, and if σ_ ( _x_ ) _is identically −_ 1 _, call it_ negative real-nice _._ 

## **Proposition 5.2.** _If H is negative real-nice, then the differential on CFDR_[�] ( _H_ ) _counts:_ 

- _(1) τ -invariant empty bigons;_ 

- _(2) τ -invariant empty rectangles, which come in two types: rectangles with two_ 90 _[◦]_ **x** _- corners on the fixed set and two_ 90 _[◦]_ **y** _-corners off the fixed set, and rectangles with two_ 270 _[◦]_ **y** _-corners on the fixed set and two_ 90 _[◦]_ **x** _-corners off the fixed set;_ 

- _(3) τ -invariant compact empty hexagons, which are disks with four corners (two in_ **x** _and two in_ **y** _) off the fixed set and two corners (one_ 90 _[◦]_ **x** _-corner and one_ 270 _[◦]_ **y** _-corner) on the fixed set;_ 

- _(4) τ -invariant compact empty octagons, which are disks with two_ 270 _[◦]_ **y** _-corners on the fixed set and four (_ 90 _[◦] )_ **x** _-corners and two (_ 90 _[◦] )_ **y** _-corners off the fixed set;_ 

- _(5) τ -invariant noncompact empty hexagons, which are disks with one fixed_ **x** _-corner (_ 90 _[◦] ), one fixed_ **y** _-corner (_ 270 _[◦] ), and two e∞-punctures;_ 

- _(6) τ -invariant noncompact empty octagons, with two_ **y** _-corners (_ 270 _[◦] ) on the fixed set, two_ **x** _-corners (_ 90 _[◦] ) off the fixed set, and two e∞ Reeb chords;_ 

- _(7) τ -invariant compact annuli so that the fixed set intersects the boundary, which come in four types:_ 

   - _(A1) annuli with one (fixed)_ **x** _-corner and one (fixed)_ **y** _-corner on each boundary component (_ 90 _[◦] and_ 270 _[◦] , respectively) and so that the α-boundary of the inner component is on the same side of the fixed set as the β-boundary of the outer component;_ 

   - _(A2) annuli with one (fixed)_ **x** _-corner and one (fixed)_ **y** _-corner on each boundary component (_ 90 _[◦] and_ 270 _[◦] , respectively) and so that the α-boundary of the inner component is on the same side of the fixed set as the α-boundary of the outer component;_ 

   - _(A3) annuli so that one boundary component has one (fixed)_ **x** _- and one (fixed)_ **y** _- corner (_ 90 _[◦] and_ 270 _[◦] , respectively) and the other boundary component has two fixed_ **y** _-corners (both_ 270 _[◦] ) and two non-fixed_ **x** _corners (both_ 90 _[◦] ); and_ 

   - _(A4) annuli so that each boundary component has two fixed_ **y** _-corners (both_ 270 _[◦] ) and two non-fixed_ **x** _corners (both_ 90 _[◦] );_ 

LIPSHITZ AND OZSVÁTH 

20 

**==> picture [71 x 71] intentionally omitted <==**

**==> picture [36 x 36] intentionally omitted <==**

**==> picture [71 x 71] intentionally omitted <==**

**==> picture [37 x 36] intentionally omitted <==**

**==> picture [368 x 332] intentionally omitted <==**

**==> picture [53 x 53] intentionally omitted <==**

**==> picture [62 x 77] intentionally omitted <==**

Figure 4. **Rigid curves in real-nice diagrams** . All the examples are in the _σ_ = _−_ 1 case. For the _σ_ = 1-case, exchange the _α_ - and _β_ -curves. 

REAL BORDERED FLOER HOMOLOGY 

21 

- _(8) τ -invariant boundary-free annuli, with no fixed corners, one_ 90 _[◦] corner and one_ 270 _[◦] corner (either an_ **x** _- or_ **y** _-corner) on each boundary component, and on which τ acts by reflection across a circle in the interior of the annulus;_ 

- _(9) τ -invariant free annuli, so that the action of τ on the annulus is free (and exchanges the boundary components), and the annulus has one_ 90 _[◦] corner and one_ 270 _[◦] corner (either an_ **x** _- or_ **y** _-corner) on each boundary component;_ 

- _(10) τ -invariant punctured tori, with one boundary component with two fixed_ **y** _-corners and two non-fixed_ **x** _-corners (all_ 270 _[◦] ), and so that the involution on the torus has fixed set an arc and quotient a Möbius band;_ 

- _(11) pairs of empty bigons which are exchanged by τ ;_ 

- _(12) pairs of empty rectangles which are exchanged by τ ; and_ 

- _(13) pairs of empty half-strips which are exchanged by τ ._ 

_If H is positive real-nice, the differential admits an exactly analogous description, except in each case the_ **x** _and_ **y** _corners are exchanged. In all cases, all corners of the domain (or curve) not fixed by the involution are_ 90 _[◦] angles The map from the holomorphic curve to_ Σ _is an immersion, except for boundary-free annuli, free annuli, and tori (Cases (8), (9), and (10)), for which there are two boundary branch points._ 

See Figure 4 for examples of these domains. _Empty_ means that no points of **x** or **y** are in the interior of the domain. Note also that the domains need not be embedded; for example, pairs of rectangles can overlap (cf. Figure 17). 

_Proof._ We will consider the case that all points _x_ on _**α** ∩ C_ have _σ_ ( _x_ ) = _−_ 1. The case that _σ_ ( _x_ ) is identically 1 follows from the observation that reversing the orientation of Σ changes the sign of _σ_ and the directions of holomorphic curves (from **y** to **x** instead of **x** to **y** ), but not the counts of holomorphic curves. 

From Formula (3.8), 

**==> picture [439 x 25] intentionally omitted <==**

Note that _|P |_ = 2 _|⃗ρ|_ : for _|P |_ , both _α_ - and _β_ -Reeb chords count. 

The index is additive over components of _S_ (where 2 _g_ is replaced by the number of _±∞_ corners on the component, and so on). For trivial strips, ind _[R]_ ( _B, S, P_ ) = 0. So, we consider two cases: a pair of components which are exchanged by _τ_ , and a component which is preserved by _τ_ . We first prove that the domain is as in the statement of the proposition without the condition of being empty or the map to Σ being an immersion, and then verify the emptiness and immersion conditions at the end. 

_Case 1._ A pair of non-fixed components. In this case, **x** _∩ C_ = **y** _∩ C_ = _∅_ , and _χ_ ( _S_ ) _≤_ 2 with equality if and only if _S_ consists of two disks. We have 

**==> picture [161 x 25] intentionally omitted <==**

so for each of the two components _S_ 1 and _S_ 2, _gi −χ_ ( _Si_ )+2 _e_ ( _Bi_ )+ _|Pi|_ = 1. This is exactly the index formula in the nonequivariant case, so from the corresponding result for nonequivariant nice diagrams [LOT18, Proposition 8.4], _S_ 1 and _S_ 2 are each a bigon, rectangle, or half-strip. 

Note also that this argument precludes an index-0 pair of non-fixed components. 

_Case 2._ A fixed component. Observe that the component has _|P |_ even, because chords come in pairs, exchanged by the involution; and _χ_ ( _S_ ) _≤_ 1, with equality if and only if _S_ is 

LIPSHITZ AND OZSVÁTH 

22 

a disk. Since the curve has 2 _g_ corners at _±∞_ , we can rewrite Formula (5.3) as 

**==> picture [364 x 13] intentionally omitted <==**

where _nfc_ denotes the number of non-fixed corners—the number of points in **x** not on _C_ plus the number of points in **y** not on _C_ . Moreover, _S_ has at least one fixed _x_ -corner or at least two non-fixed _x_ -corners, so the left side is at least _|P |/_ 2 + _e_ ( _B_ ). So, _e_ ( _B_ ) _≤_ 1, and if _e_ ( _B_ ) _̸_ = 0 then _|P |_ = 0. We take three subcases. 

_Subcase 2a. e_ ( _B_ ) = 1. In this case, _nfc/_ 4 + #( **x** _∩ C_ ) _/_ 2 _− χ_ ( _S_ ) _/_ 2 = 0. Since there is at least one _x_ -corner, we must have _χ_ ( _S_ ) = 1 (so _S_ is a disk) and _nfc/_ 2 + #( _x ∩ C_ ) = 1. Thus, the domain either has two non-fixed corners or one fixed _x_ -corner. The number of _x_ -corners equals the number of _y_ -corners, so we either have a bigon (with one fixed _x_ -corner and one fixed _y_ -corner) or a rectangle of the second type (with two fixed _y_ -corners and two non-fixed _x_ -corners). 

_Subcase 2b. e_ ( _B_ ) = 1 _/_ 2. This does not occur. The condition that _σ_ ( _x_ ) is identically _−_ 1 implies that no elementary region in the diagram is a bigon that is fixed by _τ_ . So, an even number of the elementary regions in _B_ are bigons, and hence the Euler measure of _B_ is an integer. 

_Subcase 2c. e_ ( _B_ ) = 0. In this case, _nfc/_ 4+#( **x** _∩ C_ ) _/_ 2+ _|P |/_ 2 _− χ_ ( _S_ ) _/_ 2 = 1. By counting _x_ -corners, the first two terms contribute at least 1 _/_ 2. So, if _|P | ̸_ = 0, then the left side is at least 3 _/_ 2 _− χ_ ( _S_ ) _/_ 2, so _χ_ ( _S_ ) = 1 ( _S_ is a disk), _|P |_ = 2, and _S_ either has one fixed _x_ -corner (and no non-fixed corners) or two non-fixed _x_ -corners (and no non-fixed _y_ -corners). The first case is a noncompact hexagon, and the second case is a noncompact octagon. 

Finally, if _|P |_ = 0, we could have _χ_ ( _S_ ) = _−_ 1 (a pair of pants or punctured torus), _χ_ ( _S_ ) = 0 (an annulus), or _χ_ ( _S_ ) = 1. (The case _χ_ ( _S_ ) = _−_ 2 does not occur because it would imply there are no _x_ corners.) 

If _χ_ ( _S_ ) = _−_ 1, then Formula (5.4) gives _nfc/_ 4 + #( **x** _∩ C_ ) _/_ 2 + _|P |/_ 2 = 1 _/_ 2. Thus, _|P |_ = 0 and _nfc/_ 4 + #( **x** _∩ C_ ) _/_ 2 = 1 _/_ 2. So, the domain either has 1 fixed _x_ -corner and 1 fixed _y_ -corner, or 2 non-fixed corners. In the latter case, since there is at least one _x_ -corner per boundary component, there are 2 non-fixed _x_ -corners and 2 fixed _y_ -corners. Moreover, in both cases, there are not enough corners for three boundary components, so _S_ must be a punctured torus. Further, since the Euler measure of the domain is 0 and the Euler measure of a torus with one 90 _[◦]_ and one 270 _[◦]_ corner is _−_ 1, in fact the domain has 2 non-fixed _x_ -corners and 2 fixed _y_ -corners, as in Figure 4 (Type (10)). 

If _χ_ ( _S_ ) = 0, then _nfc/_ 4+#( **x** _∩C_ ) _/_ 2+ _|P |/_ 2 = 1. Thus, _|P |_ = 0 and _nfc/_ 2+#( **x** _∩C_ ) = 2. So, the domain either has 2 fixed _x_ -corners, one fixed _x_ -corner and 2 non-fixed corners, or 4 non-fixed corners. If the involution exchanges the two components of the boundary, then there must be two corners on each. We take some cases: 

- If the fixed set of the action on _S_ is empty, then _S_ has two corners on each boundary component, 90 _[◦]_ and one 270 _[◦]_ , and a free, orientation-reversing involution exchanging the boundary components. This is the free annulus (Type (9)). 

- If the fixed set is a circle (in the interior of _S_ ), then _S_ has two corners on each boundary component, one 90 _[◦]_ and one 270 _[◦]_ ; this is the boundary-free annulus, Type (8). 

- If the involution preserves each boundary component, each of the two components of _∂S_ must have two fixed corners, since every orientation-reversing involution of the circle has two fixed points, and an even number of non-fixed corners. So, these are – 

- the type (A1) (A4) annuli. 

REAL BORDERED FLOER HOMOLOGY 

23 

If _e_ ( _B_ ) = 0, _|P |_ = 0 and _χ_ ( _S_ ) = 1, then we are considering a disk with _nfc/_ 4 + #( **x** _∩ C_ ) _/_ 2 = 3 _/_ 2. As in the previous paragraph, the boundary component has two fixed corners. Also, the disk is built entirely of rectangles. The possibilities are: 

- Two fixed _x_ -corners and two non-fixed _y_ -corners; this is a rectangle of the first type. 

- One fixed _x_ -corner, one fixed _y_ -corner, and four non-fixed corners (two of each type). This is a compact hexagon. 

- Two fixed _y_ -corners and six non-fixed corners. This is a compact octagon. 

Note also that the argument in each case precludes an index-0 fixed component. Combining the cases so far, we have proved: 

- The curve consists of either a single, fixed component or a single pair of non-fixed components, and 

- The component(s) have one of the forms from the proposition statement, except perhaps they could be nonempty and the map to Σ might not be an immersion. 

To see that the map to Σ is an immersion except in cases (8), (9), and (10), note that if the (real) map to Σ has branch points, then there is in fact a family of (real) maps by varying the branch points. We will see in Lemma 5.5 that any real disk, or real annulus of types – (A1) (A4), admits a real holomorphic branched cover to the strip, so if the map to Σ has branch points, then the moduli space is not rigid (by varying the branch point in Σ). 

To show that the domain is empty and all non-fixed corners have 90 _[◦]_ angles, we appeal to the embedded index formula. Specifically, by inspection, an empty domain of each of the types we have reduced to has ind _[R]_ ( _B, ⃗ρ_ ) = 1, and a nonempty domain has index strictly larger than this. 

It remains to show that all of these domains admit unique holomorphic representatives. We state and prove this as three separate lemmas, Lemmas 5.5, 5.6, and 5.7. □ 

**Lemma 5.5.** _In a real-nice diagram, for any choice of symmetric almost complex structure, each of the domains in Proposition 5.2 of types (1)–(7) and (11)–(13) has a unique real holomorphic representative._ 

_Proof._ This is familiar except for the annuli; see [GM25, Examples 4.4–4.6]. For example, consider an octagon. We may work with a split almost complex structure when computing the moduli space; we discuss this more in the annulus case below. The source _S_ of a holomorphic representative is obtained from the domain by perhaps making a cut from each of the 270 _[◦]_ corners. Such cuts cannot be made _τ_ -equivariantly, so if the cuts are nontrivial, then _π_ Σ _◦ u ◦ τ_ = _τ ◦ π_ Σ _◦ u_ (because the images of the branch points are different, say). So, there are no cuts: the source _S_ is identified with the domain and _π_ Σ _◦ u_ is the identity map. (If the map to Σ is not an embedding, we mean that if the domain _B_ =[�] _niRi_ , then we take _ni_ copies of _Ri_ and glue these together along shared edges.) We must show there is a unique holomorphic map to [0 _,_ 1] _×_ R respecting the punctures and involution. It is well-known that there is a unique holomorphic map _uD_ to [0 _,_ 1] _×_ R respecting the corners. (Explicitly, identify [0 _,_ 1] _×_ R with the upper half plane, so _−∞_ is identified with 0 and + _∞_ with _∞_ . Identify _S_ with the upper half-plane, so that the _−∞_ punctures are at points _x_ 1 _, x_ 2 _, x_ 3 and the + _∞_ punctures are at points _y_ 1 _, y_ 2 _, y_ 3. Then the map is _z �→_ [( _z − x_ 1)( _z − x_ 2)( _z − x_ 3)] _/_ [( _z − y_ 1)( _z − y_ 2)( _z − y_ 3)].) If this map did not respect the involution, then _τ ◦ uD ◦ τ_ would be another holomorphic map respecting the corners, contradicting uniqueness. (The existence of the map _uD_ for any complex structure on _S_ is 

LIPSHITZ AND OZSVÁTH 

24 

why the maps to Σ in Proposition 5.2 are immersions, in the case of disks; a similar comment applies to annuli, via the argument below.) 

So, in the rest of the proof, we will focus on the four types of annuli in item (7). Note first, because there are no (real) index-0 holomorphic curves in a real-nice diagram, the count is independent of the choice of almost complex structure. Also, by Proposition 3.5, we can achieve transversality by working with a split complex structure and perturbing the _α_ - and _β_ -curves ( _τ_ -equivariantly). 

For all the kinds of annuli under consideration, the holomorphic curve in Σ _×_ [0 _,_ 1] _×_ R can be described as holomorphic maps from the domain in Σ (glued together maximally along shared edges), possibly cut along some _α_ - or _β_ -curves, to [0 _,_ 1] _×_ R. In the real case, the cuts must come in pairs, respecting the Z _/_ 2-action. By considering the local structure at the corners, it follows that for these domains, no cuts are possible. So, we want to show that for some (or all) complex structure on Σ, there is a holomorphic map from the domain shown to [0 _,_ 1] _×_ R, sending the _α_ boundary to _{_ 1 _} ×_ R and the _β_ -boundary to _{_ 0 _} ×_ R. The existence of such a map is independent of how the _α_ - and _β_ -curves continue beyond the portions indicated in Figure 4. 

For type (A1) and (A2) annuli, this is immediate: double branched covers of [0 _,_ 1] _×_ R correspond to involutions on the annulus taking the _α_ -boundary to the _α_ -boundary. Uniformizing the domain by a standard annulus, the real involution shows that, on each component of the boundary, the _α_ -segment subtends an angle of _π_ , and hence such an involution exists (and is unique). (A closely related case, using the same argument, was also described in [GM25, Example 4.7]. See also [OSz04, Lemma 9.3].) 

We reduce the type (A3) and (A4) annuli to this case. As noted above, the count is independent of how the _α_ - and _β_ -curves continue, so consider the (incomplete, but slightly less incomplete) diagrams shown in Figure 5. Starting with the type (A3) annuli (top row in Figure 5), extend the diagram for the annulus by filling the inner boundary component (the one with a 90 _[◦]_ and a 270 _[◦]_ corner) with a bigon, and extending the arcs from the 270 _[◦]_ corner of the annulus on the inner boundary out of the annulus’s outer boundary without crossing the fixed set. This domain decomposes equivariantly in two ways: as an annulus and a bigon, and as a hexagon and a rectangle. Since the pair of bigons both clearly have holomorphic representatives, gluing them gives a 1-dimensional family of annuli, corresponding to a pair of cuts, exchanged by _τ_ , starting from a corner on the inner boundary of the annulus. (The domain does not admit any other real pair of cuts, guaranteeing the moduli space has this form.) The other end of the moduli space is the annulus whose existence we are trying to prove, concatenated with a bigon. This proves annuli of this type exist. 

We handle type (A4) similarly. Extend the domain and some of the curves as shown in Figure 5 (bottom row). The larger domain admits a decomposition as a hexagon, which clearly exists, and a type (A3) annulus, which we just proved exists. Again, there is a unique 1-parameter family of real pairs of cuts leading to this broken curve. At its other edge we see the desired fourth-type annulus glued to a rectangle. This proves the existence of the type (A4) annuli. □ 

**Lemma 5.6.** _In a real-nice diagram, for any choice of generic symmetric almost complex structure or generic perturbation of the α- and β-curves, each of the domains in Proposition 5.2 of types (8) and (9) has an odd number of real holomorphic representatives._ 

REAL BORDERED FLOER HOMOLOGY 

25 

**==> picture [92 x 91] intentionally omitted <==**

**==> picture [91 x 90] intentionally omitted <==**

**==> picture [91 x 90] intentionally omitted <==**

**==> picture [91 x 90] intentionally omitted <==**

**==> picture [431 x 108] intentionally omitted <==**

Figure 5. **Diagrams to prove the existence of annuli.** Top row: the type (A3) annuli from Proposition 5.2; a particular choice of extension of two of the curves in its boundary and a larger domain in the resulting diagram; a decomposition of the result into a pair of type 2 rectangles; the other end of the moduli space, proving the existence of the desired curve. Bottom row: the type (A4) annulus; an extension of four of the curves in its boundary and a domain in the larger diagram; a decomposition of that domain into a type (A3) annulus and a compact hexagon; the other end of the moduli space, where the domain decomposes into a rectangle and the type (A4) annulus, proving the existence of the type (A4) annulus. 

_Proof._ First, consider boundary-free annuli (case (8)). Unlike the annuli considered in Lemma 5.5, there are two possible cuts: along the _α_ -curve from one boundary component and the _β_ -curve (to which it is reflected) from the other. It is easy to see that, because the diagram is nice, an _α_ -cut from one boundary intersects a _β_ -cut from the other (at a point on the fixed set) before exiting the domain; see Figure 6. As the cuts approach this point, the angle subtended by the _α_ -part of one boundary component approaches 2 _π_ , while the _β_ -part of the other boundary component approaches 2 _π_ . Making the other pair of cuts instead, the situation is reversed. Thus, by a familiar argument (see, e.g., [OSz04, Lemma 9.3]), the domain has an odd number of holomorphic representatives. 

The case of free annuli (case (9)) is similar. Now, for each of the two _τ_ -invariant pairs of cuts, either they cross before they exit the domain, or they exit through the opposite boundaries without crossing. (See Figure 7.) Order the two boundary components of the annulus arbitrarily. In either case, one _τ_ -invariant pair limits to a curve where the first boundary component is entirely _α_ -boundary and the second is entirely _β_ -boundary. The second _τ_ -invariant pair limits to a curve where the first boundary component is entirely _β_ -boundary and the second is entirely _α_ -boundary. In either case, there are an odd number 

LIPSHITZ AND OZSVÁTH 

26 

**==> picture [102 x 141] intentionally omitted <==**

**==> picture [102 x 141] intentionally omitted <==**

**==> picture [102 x 141] intentionally omitted <==**

Figure 6. **Boundary-free annulus** . Left: A boundary-free annulus; we have drawn this less symmetrically than in Figure 4, to make it clearer that the symmetry is reflection across the green circle, not some other symmetry. Center: completing the curves locally in a way compatible with a nice diagram. Other ways of completing the diagram come from applying Dehn twists to _α_ - and _β_ -curves, along circles parallel to the fixed set. Right: an equivariant pair of cuts which nearly intersect. For this pair, the inner boundary is mostly _α_ -boundary, while the outer boundary is mostly _β_ -boundary. 

**==> picture [73 x 73] intentionally omitted <==**

**==> picture [73 x 73] intentionally omitted <==**

**==> picture [73 x 74] intentionally omitted <==**

**==> picture [73 x 74] intentionally omitted <==**

Figure 7. **Free annuli.** Left: a domain for a free annulus where the cuts exit without crossing. Right: a domain where the cuts cross before exiting. On the right, we have drawn one pair of maximal cuts thicker, to make it clear that they cross before exiting the domain. 

REAL BORDERED FLOER HOMOLOGY 

27 

of lengths in between where the _α_ portion of the first boundary subtends the same arc as the _α_ portion of the second boundary. □ 

**Lemma 5.7.** _In a real-nice diagram, for any choice of generic symmetric almost complex structure or generic perturbation of the α- and β-curves, each domain D in Proposition 5.2 of type (10) has an odd number of real holomorphic representatives._ 

_Proof._ We will adopt a similar strategy to the types (A3) and (A4) annuli in the proof of Lemma 5.5, after some preparatory work. 

As in the other cases, since there are no index 0 positive domains in the diagram, the count of holomorphic representatives of _D_ is independent of the choice of almost complex structure or perturbation of the _α_ - and _β_ -circles. 

Following an idea of Binns-Guth-Xiao, here is a source of such domains. Start from a closed torus, viewed as R[2] _/_ Z[2] ; this has an orientation-reversing involution given by reflection across the line _y_ = _x_ . Let _**α**_ be the image of two lines of slope _p/q_ , and _**β**_ the image of two lines of slope _q/p_ . (This is a special case of the twisted toroidal grid diagrams for lens spaces in [BGH08].) These lines divide the torus into parallelograms. If there is an embedded 3 _×_ 3 block of parallelograms with two opposite corners on the line _y_ = _x_ , then deleting that block from the torus gives a domain of type (10). See Figure 8. 

We claim that, in fact, all domains of type (10) are of this form. First, since the boundary is connected, the fixed set of the involution is also connected. Next, because the domain under consideration has Euler measure 0, it is tiled by rectangles. Label the four arcs in the boundary _a_ 1 _, b_ 1 _, a_ 2 _, b_ 2, so that the _ai_ lie on _α_ -circles. As the _α_ -curves _α_ 1, _α_ 2 containing _a_ 1, _a_ 2 continue past _b_ 1 into the interior of the domain, they are parallel: there is a rectangle (made of many small rectangles) with one edge on _α_ 1, the opposite edge on _α_ 2, and an edge in between that is the segment _b_ 1. Since the domain is tiled by rectangles, _α_ 1 and _α_ 2 remain parallel—cobounding a rectangle _R_ —until one of them exits the domain—necessarily through the interior of _b_ 2, since the rectangle already has _b_ 1 on its boundary. Eventually, the other _αi_ also exits through the interior of _b_ 2. Moreover, by considering how the rectangle _R_ intersects _b_ 2, it is clear that the four points in ( _α_ 1 _∪ α_ 2) _∩ b_ 2 alternate between points on _α_ 1 and on _α_ 2. See Figure 9. 

By the same argument, there are four points on ( _α_ 1 _∪ α_ 2) _∩ b_ 2, alternating between points on _α_ 1 and on _α_ 2; four points on ( _β_ 1 _∪ β_ 2) _∩ a_ 1, alternating between points on _β_ 1 and on _β_ 2; and four points on ( _β_ 1 _∪ β_ 2) _∩ a_ 1, alternating between points on _β_ 1 and on _β_ 2. It follows that we can glue a rectangle to the boundary of the domain and extend the _α_ - and _β_ -circles to a twisted toroidal grid diagram _G_ for a lens space (as in [BGH08]). 

The fixed set of the involution intersects the boundary of the domain at two opposite corners, and passes diagonally across small rectangles. So, we can extend the fixed set and the involution to the completed grid diagram _G_ , so that the fixed set still passes diagonally across rectangles. Now, choose an identification of the torus with R[2] _/_ Z[2] so that the fixed set maps to the line _y_ = _x_ . Then the _α_ -circles map to circles at some slope _p/q_ , the _β_ -circles map to circles at slope _q/p_ , and the boundary maps to a 3 _×_ 3 sub-rectangle, as claimed. (See Figure 8.) 

View _G_ as a 2-pointed real Heegaard diagram (in the sense of [GM25, Section 3.3]), by placing two basepoints on the fixed set, one in the middle of _D_ and the other in the middle of _G \ D_ . We will use the fact that _∂_[2] = 0 on _HFR[−]_ ( _G_ ) _/_ ( _U_ 1[2] _[, U]_ 2[ 2][)][to][prove][that] _[D][⊂][G]_ has a holomorphic representative. Let _D[′]_ = _G \ D_ be the complement to _D_ . The domain _D[′] ∈ π_ 2( **y** _,_ **x** ) is a rectangle of the first type. Observe that there is an extra symmetry _σ_ of 

LIPSHITZ AND OZSVÁTH 

28 

**==> picture [438 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
y<br>x y x<br>x x<br>y<br>y<br>x<br>x<br>y y<br>y y x<br>x<br>**----- End of picture text -----**<br>


**==> picture [95 x 205] intentionally omitted <==**

**==> picture [320 x 205] intentionally omitted <==**

Figure 8. **Cutting up toroidal domains.** Top: toroidal domains corresponding to four different slopes _p/q_ . Center: extending these domains to twisted grid diagrams. Bottom: the unique alternate equivariant decompositions of these domains. 

**==> picture [121 x 121] intentionally omitted <==**

**==> picture [121 x 121] intentionally omitted <==**

**==> picture [121 x 121] intentionally omitted <==**

Figure 9. **Extending curves in toroidal domains.** Left: the curves _α_ 1 and _α_ 2 are parallel until one exits the domain, through the interior of _b_ 2. Center: the existence of a rectangle _R_ (shaded) determines the order of the points where _α_ 1 and _α_ 2 exit through _b_ 2: the points on _b_ 2 alternate between _α_ 1 and _α_ 2. Right: extending the curves beyond the domain to obtain a grid diagram for a lens space. 

REAL BORDERED FLOER HOMOLOGY 

29 

the diagram, by rotation by _π_ around the basepoints; unlike _τ_ , the symmetry _σ_ is orientationpreserving and takes _α_ -circles to _α_ -circles (but exchanges the two _α_ -circles). The domains _D_ and _D[′]_ are preserved by _σ_ . 

We take two cases, depending on whether _p/q >_ 0 or _p/q <_ 0. For _p/q >_ 0, we consider the concatenation _D[′′]_ = _D ∗ D[′] ∈ π_ 2( **x** _,_ **x** ); for _p/q <_ 0, we consider instead _D[′′]_ = _D[′] ∗ D ∈ π_ 2( **y** _,_ **y** ). We will show that there is a unique second decomposition of _D[′′]_ as a concatenation of index 1 positive domains that are preserved by both _σ_ and _τ_ , and so that those domains are of types we have already shown have holomorphic representatives (i.e., are not tori). Perhaps there are also other decompositions of _D[′′]_ into real index 1 domains that are not _σ_ -equivariant, but those decompositions come in pairs. Any two such decompositions _D_ 1 _∗ D_ 2 _, σ_ ( _D_ 1) _∗ σ_ ( _D_ 2) contribute the same way to _∂_[2] : if _D_ 1 and _D_ 2 are both not tori, then they necessarily contribute, while if they are tori we have not (yet) counted their contribution, but by independence of the count from the almost complex structure, the counts of representatives for _Di_ and _σ_ ( _Di_ ) still agree. In particular, decompositions that are not _σ_ -equivariant contribute an even number of terms to _∂_[2] , and hence it suffices to consider only _σ_ -equivariant decompositions. (Note that the holomorphic curves may not be _σ_ -invariant, just the domains.) 

Consider the case that _p/q >_ 0. Any other _σ_ - and _τ_ -invariant decomposition of _D[′′]_ corresponds to making cuts of equal length in both directions from both _x_ -corners (that is, four cuts along the same number of edges of the grid). These cuts are in the opposite direction from the ones decomposing _D[′′]_ as _D ∗ D[′]_ . The cut starting along _β_ from one _x_ -corner ends when it intersects the cut along _α_ from the other _x_ -corner, and vice versa. These cuts decompose the domain as a concatenation as a free annulus and a boundary-free annulus. See Figure 8. 

Finally, consider the case that _p/q <_ 0. In this case, the four cuts start at the _y_ -corners, and again are of equal length and go in the opposite direction from the decomposition of _D[′′]_ as _D[′] ∗ D_ . In this case, the cuts end when the _β_ -cut from one _y_ -corner intersects the _α_ -cut from the same corner. In this case, these cuts decompose the domain into a pair of type (A2) annuli. Again, see Figure 8. 

We have now shown that, in both cases, decompositions of _D[′′]_ not involving _D_ contribute an odd number of terms to _∂_[2] = 0. Thus, _D_ has an odd number of holomorphic representatives, as desired. □ 

_Remark_ 5.8 _._ For multi-basepointed real Heegaard Floer homology, there is an additional type of toroidal domain in nice diagrams, corresponding to removing a 1 _×_ 1 rather than 3 _×_ 3 sub-grid. See Figure 10. 

_Remark_ 5.9 _._ In the sutured, rather than bordered case, the results in this section have also been obtained by Binns-Guth-Xiao [BGX]. In particular, they pointed out that an earlier version of Proposition 5.2 missed cases (9) and (10). 

5.2. **Real Auroux-Zarev diagrams.** Given a pointed matched circle _Z_ , the _Auroux-Zarev diagram_ AZ( _Z_ ) is obtained from the triangle _T_ = _{_ ( _x, y_ ) _∈_ R[2] _|_ 0 _≤ x ≤ x_ + _y ≤_ 4 _k_ + 1 _}_ as follows. Identify the left boundary _T ∩{x_ = 0 _}_ with _Z_ , so the point 1 _∈_ **a** is identified with (0 _,_ 4 _k_ ). This also identifies _T ∩{x_ + _y_ = 4 _k_ + 1 _}_ with **a** ; identify a neighborhood of ( _i,_ 4 _k_ + 1 _− i_ ) and ( _M_ ( _i_ ) _,_ 4 _k_ + 1 _− M_ ( _i_ )) in _T ∩{x_ + _y_ = 4 _k_ + 1 _}_ , to obtain a surface of genus _k_ with one boundary component. Then identify neighborhoods of (0 _,_ 1 _/_ 2) and (0 _,_ 4 _k_ + 1 _/_ 2), and of (1 _/_ 2 _,_ 0) and (4 _k_ + 1 _/_ 2 _,_ 0) in _∂T_ . The result is a surface with three 

LIPSHITZ AND OZSVÁTH 

30 

**==> picture [120 x 121] intentionally omitted <==**

Figure 10. **Another nice toroidal domain.** Domains of this kind, which require two parallel _α_ -circles, appear in multi-basepointed real Heegaard Floer homology, but not in the single basepoint case. 

boundary components; fill the boundary component intersecting _{x_ + _y_ = 4 _k_ + 1 _}_ with a disk. The _α_ -arcs are the images of the segments [0 _,_ 4 _k_ + 1 _− i_ ] _× {i}_ ; each _α_ -arc consists of two line segments. Similarly, the _β_ -arcs are the images of the segments _{i} ×_ [0 _,_ 4 _k_ + 1 _− i_ ]. The basepoint (or rather, base-arc) **z** is an arc near (0 _,_ 0) connecting the two boundary components. See Figure 11. The diagram AZ( _Z_ ) = _−_ AZ( _−Z_ ) is the result of reversing the orientation on AZ( _−Z_ ). See Figure 12. We recall the bordered invariants of AZ( _Z_ ) and AZ( _Z_ ) in Section 5.3. (See [LOT11] for more on these diagrams.) The diagrams AZ( _Z_ ) and AZ( _Z_ ) represent [0 _,_ 1] _× F_ ( _Z_ ), but with one side below the Heegaard surface ( _α_ -bordered) and the other above ( _β_ -bordered). (The identifications of the boundaries on the two sides differ by a half boundary Dehn twist [LOT11, Proposition 4.4], but because we are interested in computing invariants for closed 3-manifolds, the complications from considering strongly based mapping classes will not play a role in the present paper.) 

**Definition 5.10.** _Fix a pointed matched circle Z_ = ( _Z,_ **a** _, M, z_ ) _. Let w be a point between the_ 2 _k[th] and_ (2 _k_ + 1) _[st] points in_ **a** _, and let τZ_ : _Z → Z denote reflection across {z, w}. We say that_ ( _Z, τZ_ ) _is a_ real pointed matched circle _if M respects τZ, i.e., M ◦ τZ_ = _τZ ◦ M ._ 

See Figure 13. Given a real pointed matched circle _Z_ , the involution _τZ_ induces an _∼_ = isomorphism _τZ,∗_ : _A_ ( _Z_ ) _−→A_ ( _Z_ )[op] . For a real pointed matched circle ( _Z, τZ_ ), the diagrams AZ( _Z_ ) and AZ( _Z_ ) are real bordered Heegaard diagrams, with the involution _τ_ : _T → T_ , _τ_ ( _x, y_ ) = (4 _k_ + 1 _− y,_ 4 _k_ + 1 _− x_ ); see Figures 11 and 12. We have: 

**Lemma 5.11.** _Given a real pointed matched circle Z, the real Heegaard diagrams_ (AZ( _Z_ ) _, τ_ ) _and_ (AZ( _Z_ ) _, τ_ ) _specify real thick surfaces. The central real surface has genus k and one fixed circle, and its quotient is orientable if and only if the matching M in Z preserves {_ 1 _, . . . ,_ 2 _k} (and hence {_ 2 _k_ + 1 _, . . . ,_ 4 _k})._ 

_Proof._ This is immediate from the construction of a real bordered manifold from a real bordered Heegaard diagram. □ 

In particular, if _Z_ is the antipodal pointed matched circle, then _F_ ( _Z_ ) _/τ_ is always nonorientable. If _Z_ is an even-genus split pointed matched circle, then _F_ ( _Z_ ) _/τ_ is orientable; for 

REAL BORDERED FLOER HOMOLOGY 

31 

an odd-genus split pointed matched circle, _F_ ( _Z_ ) _/τ_ is nonorientable (as it must be, by the classification of real involutions of surfaces). 

5.3. **Classical bordered invariants of the Auroux-Zarev diagrams.** It seems helpful to pause at this point and recall the bordered _AA_ and _DD_ invariants of the Auroux-Zarev piece and its mirror. The computations in Section 5.4 of the real invariants of these diagrams do not, in fact, depend on the answers in the unreal case, so the reader may skip this section; but it provides context for the computations below. 

There are canonical isomorphisms 

**==> picture [366 x 60] intentionally omitted <==**

Here, _A_ ( _Z_ ) is the dual type _AA_ bimodule to _A_ ( _Z_ ), whose underlying F2-vector space is HomF2( _A_ ( _Z_ ) _,_ F2). The type _DD_ bimodule _[A]_[(] _[Z]_[)] _bar[A]_[(] _[Z]_[)] has underlying vector space _A_ = HomF2( _A_ ( _Z_ ) _,_ F2) and _δ_[1] : _A →A_ ( _Z_ ) _⊗ A ⊗A_ ( _Z_ ) given by 

**==> picture [468 x 41] intentionally omitted <==**

Here, _d_ is the differential on _A_ induced by (i.e., the transpose of) the differential on _A_ ( _Z_ ), and Chord( _Z_ ) is the set of chords in _Z_ . Note that, if we use the dual basis for _A_ and _ϕ_ = _a_ ( _**ρ**_ ) _[∗]_ , then _d_ ( _ϕ_ ) is the sum of all _a_ ( _**ρ**[′]_ ) _[∗]_ so that _a_ ( _**ρ**_ ) is obtained from _a_ ( _**ρ**[′]_ ) by resolving a crossing, and _ϕ · a_ ( _ξ_ ) is the result of factoring _ξ_ from _**ρ**_ on the right. Our convention for idempotents is that the left idempotent of _a[∗]_ is the complement to the right idempotent for _a_ . As a concrete example, in the genus 1 case, _ρ[∗]_ 12[=] _[ ι]_[1] _[ρ][∗]_ 12 _[ι]_[1][(because] _[ρ]_[12][=] _[ ι]_[0] _[ρ]_[12] _[ι]_[0][)][and] 

**==> picture [315 x 32] intentionally omitted <==**

As another example, _ρ[∗]_ 1[=] _[ ι]_[1] _[ρ][∗]_ 1 _[ι]_[0][(because] _[ρ]_[1][=] _[ ι]_[0] _[ρ]_[1] _[ι]_[1][)][and] 

**==> picture [302 x 32] intentionally omitted <==**

These results also give a description of _CFDD_[�] (AZ( _Z_ )), by tensoring _CFAA_[�] (AZ( _Z_ )) with the type _DD_ identity bimodule on both sides. The underlying vector space of _CFDD_[�] (AZ( _Z_ )) is _A_ ( _Z_ ), and the differential is given by 

**==> picture [469 x 41] intentionally omitted <==**

where _r_ : _Z →−Z_ is the orientation-reversing identity map. Here, we are writing the element � � of _CFDD_[�] (AZ( _Z_ )) corresponding to _a ∈A_ ( _Z_ ) as _a_ ; the left idempotent of _a_ is the image under _r_ of the complement of the right idempotent of _a_ , and the right idempotent of � _a_ is 

LIPSHITZ AND OZSVÁTH 

32 

**==> picture [162 x 285] intentionally omitted <==**

**----- Start of picture text -----**<br>
ρ 3 ρ 23 ρ 123<br>ι 1<br>ρ 2 ρ 12<br>ι 0<br>ρ 1<br>ι 1<br>ι 0<br>ι 0<br>ρ 1 ι 1<br>ρ 12 ρ 2 ι 0<br>ρ 123 ρ 23 ρ 3 ι 1<br>**----- End of picture text -----**<br>


**==> picture [79 x 80] intentionally omitted <==**

**==> picture [79 x 80] intentionally omitted <==**

Figure 11. **Auroux-Zarev pieces.** Horizontal line segments are _α_ -curves, and vertical line segments are _β_ -curves. The left column shows the diagram for the genus 1 pointed matched circle, drawn first so that the action of _A_ ( _Z_ ) on � _CFAA_ (AZ) is apparent, and then as one would draw the diagram to understand � _CFDD_ (AZ). The right side shows the case of the genus 2 split pointed matched circle, drawn in the style of _CFAA_[�] (AZ), with two half-handles omitted to save space. Also, a disk should be attached to the outer boundary of each diagram. The diagonal line (which becomes a circle after attaching the disk) is the fixed set _C_ of the real involution. 

� the image under _r_ of the complement of the left idempotent of _a_ . For example, _ρ_ 12 = _ι_ 0 � _ρ_ 12 _ι_ 0 

REAL BORDERED FLOER HOMOLOGY 

33 

**==> picture [124 x 140] intentionally omitted <==**

**----- Start of picture text -----**<br>
ρ [∗] 123 ρ [∗] 23 ρ [∗] 3<br>ι [∗] 1<br>ρ [∗] 12 ρ [∗] 2<br>ι [∗]<br>0<br>ρ [∗] 1<br>ι [∗] 1<br>ι [∗]<br>0<br>**----- End of picture text -----**<br>


**==> picture [71 x 70] intentionally omitted <==**

**==> picture [71 x 71] intentionally omitted <==**

Figure 12. **Mirror Auroux-Zarev pieces.** In this case, we have drawn both pictures with the _α_ -arcs on the left. Otherwise, conventions are as in Figure 11. 

� and _ρ_ 2 = _ι_ 0 � _ρ_ 2 _ι_ 1, and 

**==> picture [352 x 53] intentionally omitted <==**

5.4. **The real Auroux-Zarev modules.** Fix a real pointed matched circle _Z_ . In the diagram AZ( _Z_ ), all points _x_ on _**α** ∩ C_ have _σ_ ( _x_ ) = _−_ 1; for AZ( _Z_ ), all points _x_ on _**α** ∩ C_ have _σ_ ( _x_ ) = +1. In particular, the diagram AZ( _Z_ ) (respectively AZ( _Z_ )) is negative (respectively positive) real-nice. So, Proposition 5.2 computes _CFDR_[�] (AZ( _Z_ )) and _CFDR_[�] (AZ( _Z_ )). We devote the rest of this section to giving a more explicit description. 

Fix a pointed matched circle _Z_ = ( _Z,_ **a** _, M, z_ ), where _|_ **a** _|_ = 4 _k_ . Cutting _Z_ open at _z_ identifies **a** with _{_ 1 _, . . . ,_ 4 _k}_ . Recall that a _strands diagram_ (generator of _A_ ( _Z_ )) consists of some number _n_ of intervals [ _i, j_ ] with 1 _≤ i < j ≤_ 4 _k_ , the _moving strands_ , and 2 _k −_ 2 _n_ additional points **h** _⊂{_ 1 _, . . . ,_ 4 _k}_ , the _horizontal strands_ , so that _M_ ( **h** ) = **h** , **h** is disjoint from the initial and terminal points of the moving strands, and the initial (respectively terminal) points of the moving strands are themselves disjoint, and disjoint from their images under _M_ . Equivalently, we can think of **h** as a collection of trivial intervals [ _i, i_ ]. We have restricted to the central spin _[c]_ -structure on the surface, as usual. 

Now, fix a real pointed matched circle ( _Z, τZ_ ). The involution _τZ_ acts on the set of strands diagrams. (A moving strand [ _i, j_ ] is sent to [ _τZ_ ( _j_ ) _, τZ_ ( _i_ )].) Call a strands diagram _a symmetric_ if _τZ_ ( _a_ ) = _a_ , and asymmetric otherwise. Similarly, chords [ _i, j_ ] in _Z_ come in two types: _fixed chords_ , with _j_ = _τ_ ( _i_ ), and _non-fixed chords_ . 

Starting with _CFDR_[�] (AZ( _Z_ )), we recall how points in AZ( _Z_ ) correspond to chords. Each _α_ - arc in AZ( _Z_ ) consists of two segments in the triangle (horizontal line segments in Figure 12). 

LIPSHITZ AND OZSVÁTH 

34 

**==> picture [236 x 262] intentionally omitted <==**

**----- Start of picture text -----**<br>
z z z<br>w w w<br>z z z<br>**----- End of picture text -----**<br>


Figure 13. **Real pointed matched circles.** Left and center: genus 2 real pointed matched circles (the split and antipodal pointed matched circles). Right: a genus 2 pointed matched circle which is not real. The dashed semicircles indicate the matchings. As usual, to make drawing easier, we have cut the circles _Z_ open at the basepoints _z_ . 

By going along the boundary in the opposite of the boundary orientation, number these _α_ - segments 1 _, . . . ,_ 4 _k_ . Similarly, each _β_ -arc consists of two _β_ -segments; number the _β_ -segments, too, in the opposite of the boundary orientation. See Figure 14. Identify the intersection point between the _i_[th] beta-segment and the _j_[th] -alpha segment with the strand [ _i, j_ ]. (In the special case _i_ = _j_ , this is a horizontal strand rather than a moving strand.) 

The module _CFDR_[�] (AZ( _Z_ )) is generated by the set of symmetric algebra elements. We will write a state corresponding to a symmetric algebra element _a_ as _a[∗]_ , because the differential is reminiscent of the differential on _CFDD_[�] (AZ( _Z_ )). The left idempotent of _a[∗]_ is the complement of the right idempotent of _a_ . (Compare Section 5.3.) 

Proposition 5.2 specifies which domains contribute to the differential. From the form of the diagram AZ( _Z_ ), there are no bigons, type 2 rectangles, annuli, tori, or bigon pairs. We describe the contributions of each of the remaining classes of domains explicitly: 

- (i) Type 1 Rectangles: These contribute exactly as in the differential on _CFDD_[�] (AZ( _Z_ )), except that the ending chords must both be fixed. Explicitly, if _a_ contains a pair of non-fixed chords [ _i, j_ ] and [ _τ_ ( _j_ ) _, τ_ ( _i_ )] with _i < τ_ ( _j_ ) _≤_ 2 _k_ (and hence 2 _k_ + 1 _≤ j < τ_ ( _i_ )), and there is no chord [ _p, q_ ] in _a_ with _i < p < τ_ ( _j_ ) _< j < q < τ_ ( _i_ ), then _δ_[1] ( _a[∗]_ ) has a term 1 _⊗ b[∗]_ , where _b_ is obtained from _a_ by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _}_ with _{_ [ _i, τ_ ( _i_ )] _,_ [ _j, τ_ ( _j_ )] _}_ . (The condition about [ _p, q_ ] corresponds to the rectangle being empty.) 

REAL BORDERED FLOER HOMOLOGY 

35 

**==> picture [389 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 2 3 4 5 6 7 8<br>1 8<br>2 7<br>3 6<br>4 5<br>5 4<br>6 3<br>7 2<br>8 1<br>1 2 3 4 5 6 7 8<br>AZ AZ<br>**----- End of picture text -----**<br>


Figure 14. **Numbering the segments in** AZ **and** AZ **.** The diagram AZ is shown on the left and the diagram AZ on the right, both drawn with the _α_ - boundary on the left. In both cases, the intersection point corresponding to the chord [2 _,_ 5] is marked. We have not drawn the matching or the corresponding handles, as they are irrelevant to the numbering scheme. Note that the topto-bottom numbering of the points on the _α_ -boundary of AZ is consistent with type _A_ , not type _D_ conventions: for the type _D_ structure, the chord [1 _,_ 2] goes from the point labeled 8 to the point labeled 7. 

- (ii) Rectangle Pairs: These correspond to a pair of terms in _∂_[2] on _CFDD_[�] (AZ( _Z_ )) corresponding to (anti-)resolving a pair of crossings exchanged by _τ_ , between four non-fixed strands. Explicitly, if _a_ contains chords [ _i, j_ ] _,_ [ _i[′] , j[′]_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _,_ [ _τ_ ( _j[′]_ ) _, τ_ ( _i[′]_ )] with _i < i[′] ≤ j < j[′]_ , and there is no chord [ _p, q_ ] in _a_ with _i < p < i[′] ≤ j < q < j[′]_ , then _δ_[1] ( _a[∗]_ ) has a term 1 _⊗ b[∗]_ , where _b_ is obtained by replacing _{_ [ _i, j_ ] _,_ [ _i[′] , j[′]_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _,_ [ _τ_ ( _j[′]_ ) _, τ_ ( _i[′]_ )] _}_ in _a_ with _{_ [ _i, j[′]_ ] _,_ [ _j, i[′]_ ] _,_ [ _τ_ ( _j[′]_ ) _, τ_ ( _i_ )] _,_ [ _τ_ ( _i[′]_ ) _, τ_ ( _j_ )] _}_ . (Again, the condition about [ _p, q_ ] corresponds to the rectangles being empty.) In the case _j_ = _i[′]_ , [ _j, i[′]_ ] and [ _τ_ ( _i[′]_ ) _, τ_ ( _j_ )] are horizontal, so we also add their matched 

- points [ _M_ ( _j_ ) _, M_ ( _i[′]_ )] and [ _M_ ( _τ_ ( _i[′]_ )) _, M_ ( _τ_ ( _j_ ))] to the strand diagram _b_ . This adding of matched points when some strands were horizontal also occurs in cases (iii), (v), (vi), (vii), and (ix), but we will not mention it each time. 

- (iii) Compact Downward-Biting Hexagon: These are similar to the previous case, except that the two crossing are between a fixed strand and a pair of non-fixed strands. Explicitly, if _a_ contains non-fixed chords [ _i, j_ ] and [ _τ_ ( _j_ ) _, τ_ ( _i_ )] and a fixed chord [ _ℓ, τ_ ( _ℓ_ )] with _i < ℓ ≤ j < τ_ ( _ℓ_ ), and no chord [ _p, q_ ] with _i < p < ℓ ≤ j < q < τ_ ( _ℓ_ ), then _δ_[1] ( _a[∗]_ ) has a term 1 _⊗ b[∗]_ , where _b_ is obtained from _a_ by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _,_ [ _ℓ, τ_ ( _ℓ_ )] _}_ with _{_ [ _i, τ_ ( _i_ )] _,_ [ _ℓ, j_ ] _,_ [ _τ_ ( _ℓ_ ) _, τ_ ( _j_ )] _}_ . 

- (iv) Compact Upward-Biting Hexagon: These are similar to the previous case. If _a_ contains non-fixed chords [ _i, j_ ] and [ _τ_ ( _j_ ) _, τ_ ( _i_ )] and a fixed chord [ _ℓ, τ_ ( _ℓ_ )] with _i < ℓ< τ_ ( _j_ ) _< j_ , and no chord [ _p, q_ ] with _i < p < τ_ ( _j_ ) _< j < q < τ_ ( _ℓ_ ), then _δ_[1] ( _a[∗]_ ) has a 

LIPSHITZ AND OZSVÁTH 

36 

   - term 1 _⊗ b[∗]_ , where _b_ is obtained from _a_ by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _,_ [ _ℓ, τ_ ( _ℓ_ )] _}_ with _{_ [ _τ_ ( _j_ ) _, j_ ] _,_ [ _ℓ, τ_ ( _i_ )] _,_ [ _i, τ_ ( _ℓ_ )] _}_ . 

- (v) Octagons: If _a_ contains non-fixed chords [ _i, j_ ] and [ _τ_ ( _j_ ) _, τ_ ( _i_ )] and fixed chords [ _ℓ, τ_ ( _ℓ_ )] and [ _m, τ_ ( _m_ )] with _i < ℓ< m ≤ j < τ_ ( _m_ ), and no chord [ _p, q_ ] with _i < p < m ≤ j < q < τ_ ( _ℓ_ ), then _δ_[1] ( _a[∗]_ ) has a term 1 _⊗ b[∗]_ , where _b_ is obtained from _a_ by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _,_ [ _ℓ, τ_ ( _ℓ_ )] _,_ [ _m, τ_ ( _m_ )] _}_ with _{_ [ _i, τ_ ( _ℓ_ )] _,_ [ _ℓ, τ_ ( _i_ )] _,_ [ _m, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _m_ )] _}_ . 

- (vi) Disjoint Half-Strip Pairs: Suppose _a_ contains non-fixed chords [ _i, j_ ] and [ _τ_ ( _j_ ) _, τ_ ( _i_ )]; _ℓ_ satisfies _i ≤ ℓ< j < τ_ ( _i_ ) and is not equal or matched to a terminal endpoint of any chord in _a_ ; and there is no chord [ _p, q_ ] in _a_ with _p < i ≤ ℓ< q < j_ . Then _δ_[1] ( _a[∗]_ ) has a term _ρ⊗b[∗]_ where _b[∗]_ is obtained from _a_ by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _}_ by _{_ [ _i, ℓ_ ] _,_ [ _τ_ ( _ℓ_ ) _, τ_ ( _i_ )] _}_ and _ρ_ has a single moving strand [ _ℓ, j_ ] and the same left idempotent as _a[∗]_ . 

- (vii) Overlapping Half-Strip Pairs: Suppose _a_ contains two non-fixed chords [ _i, j_ ] and [ _τ_ ( _j_ ) _, τ_ ( _i_ )] exchanged by _τ_ ; _ℓ_ satisfies _i < ℓ ≤ j < τ_ ( _i_ ) and is not equal or matched to a terminal endpoint of any chord in _a_ ; and there is no chord [ _p, q_ ] in _a_ with _i < p < ℓ ≤ j < q_ . Then _δ_[1] ( _a[∗]_ ) has a term _ρ ⊗ b[∗]_ where _b[∗]_ is obtained from _a_ by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _}_ by _{_ [ _ℓ, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _ℓ_ )] _}_ and _ρ_ has a single moving strand [ _τ_ ( _ℓ_ ) _, τ_ ( _j_ )] and the same left idempotent as _a[∗]_ . 

- (viii) Noncompact Hexagon: Suppose _a_ contains a fixed chord [ _i, τ_ ( _i_ )]; _j_ satisfies _i < j ≤_ 2 _k_ and is not equal or matched to the initial endpoint of any chord in _a_ ; and _a_ does not contain a chord [ _p, q_ ] where _i < p < j < τ_ ( _j_ ) _< q_ . Then _δ_[1] ( _a[∗]_ ) has a term _ρ ⊗ b[∗]_ where _b[∗]_ is obtained from _a_ by replacing [ _i, τ_ ( _i_ )] by [ _j, τ_ ( _j_ )] and _ρ_ has a single moving strand [ _τ_ ( _j_ ) _, τ_ ( _i_ )] and the same left idempotent as _a[∗]_ . 

- (ix) Noncompact Octagons: Suppose _a_ contains fixed chords [ _i, τ_ ( _i_ )] and [ _j, τ_ ( _j_ )]; _ℓ_ satisfies _j < ℓ< τ_ ( _j_ ) _< τ_ ( _i_ ) and is not equal or matched to the terminal endpoint of any chord in _a_ ; and no [ _p, q_ ] in _a_ satisfies _p < j_ and _ℓ< q < τ_ ( _i_ ). Then _δ_[1] ( _a[∗]_ ) has a term _ρ ⊗ b[∗]_ where _b[∗]_ is obtained from _a[∗]_ by replacing _{_ [ _i, τ_ ( _i_ )] _,_ [ _j, τ_ ( _j_ )] _}_ by _{_ [ _j, ℓ_ ] _,_ [ _τ_ ( _ℓ_ ) _, τ_ ( _j_ )] _}_ and _ρ_ has a single moving strand [ _ℓ, τ_ ( _i_ )] and the same left idempotent as _a[∗]_ . 

Examples (or schematics) of all of these kinds of differentials are shown in Figure 15; see also Figure 17. 

Next, we describe _CFDR_[�] (AZ( _Z_ )), which we view as a left type _D_ structure over _A_ ( _−Z_ ) (though we could use _τZ_ to view it as a left type _D_ structure over _A_ ( _Z_ )). The underlying F2vector space of _CFDR_[�] (AZ( _Z_ )) is _A_ ( _Z_ ). We will denote the basis element of _CFDR_[�] (AZ( _Z_ )) � corresponding to a strands diagram _a ∈A_ ( _Z_ ) by _a_ . Explicitly, if we draw AZ( _Z_ ) as in Section 5.2, then the chord [ _i, j_ ] corresponds to the point ( _i,_ 4 _k_ + 1 _− j_ ). (See Figure 14.) 

� The left idempotent of _a_ is the complementary idempotent to the left idempotent of _a_ . (Equivalently, because _a_ = _r_ ( _a_ ), this is the image under _r_ of the complementary idempotent to the right idempotent of _a_ ; compare Section 5.3.) 

– The diagram is again nice, and the differential has the following terms. In cases (vi) (ix), the term only appears if the idempotents permit it, i.e., if it does not result in two strands starting on the same matched pair, or ending on the same matched pair. (In the AZ case above, we included this idempotent condition in the individual cases.) 

- (i) Type (1) Rectangles: These contribute exactly as the differential on _A_ ( _Z_ ): given strands [ _i, τ_ ( _i_ )] and [ _j, τ_ ( _j_ )] in _a_ with _i < j < τ_ ( _j_ ) _< τ_ ( _i_ ), and no strand [ _p, q_ ] with 

REAL BORDERED FLOER HOMOLOGY 

37 

**==> picture [450 x 305] intentionally omitted <==**

**----- Start of picture text -----**<br>
w<br>(i) (ii) (iii) (iv) (v)<br>w ⊗ ⊗ ⊗ ⊗<br>(vi) (vii) (viii) (ix)<br>**----- End of picture text -----**<br>


Figure 15. **Differential on** _CFDR_[�] (AZ( _Z_ )) **.** In this schematic, we imagine that part of a real pointed matched circle _Z_ near the midpoint _w_ is shown, and all the points in **a** indicated are matched to points outside this region. The first row shows terms _δ_[1] ( _a[∗]_ ) = 1 _⊗ b[∗]_ coming from provincial domains, with only _a[∗]_ and _b[∗]_ drawn. In cases (ii), (iii), and (v), some non-invariant strands could also be horizontal. The second row shows examples of _c ⊗ b[∗]_ where _c_ is nontrivial (and indicated to the left of the _⊗_ symbol, and with a thicker strand). In cases (vi), (vii) and (ix), some (thin) strands could be horizontal. In (vi), there are cases where the algebra (thick) strand is above or crosses the _w_ -line, in (vii), there are cases where the algebra (thick) strand is below or crosses the _w_ -line, and in (ix) there are cases where the algebra (thick) strand crosses the _w_ -line. 

   - _i < p < j < τ_ ( _j_ ) _< q < τ_ ( _i_ ), _δ_[1] (� _a_ ) has a term 1 _⊗_[�] _b_ where _b_ is obtained from _a_ by replacing _{_ [ _i, τ_ ( _i_ )] _,_ [ _j, τ_ ( _j_ )] _}_ with _{_ [ _i, τ_ ( _j_ )] _,_ [ _j, τ_ ( _i_ )] _}_ . 

- (ii) Rectangle Pairs: These contribute as pairs of differentials on _A_ ( _Z_ ) between quadruples of non-fixed strands exchanged by _τ_ . That is, given four strands [ _i, j_ ], [ _ℓ, m_ ], [ _τ_ ( _j_ ) _, τ_ ( _i_ )], and [ _τ_ ( _m_ ) _, τ_ ( _ℓ_ )] in _a_ with _i < ℓ ≤ m < j < τ_ ( _ℓ_ ), and no strand [ _p, q_ ] with _i < p < ℓ ≤ m < q < j_ , _δ_[1] (� _a_ ) has a term 1 _⊗_[�] _b_ where _b_ is obtained from _a_ by replacing 

   - _{_ [ _i, j_ ] _,_ [ _ℓ, m_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _,_ [ _τ_ ( _m_ ) _, τ_ ( _ℓ_ )] _}_ with _{_ [ _i, m_ ] _,_ [ _ℓ, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _ℓ_ )] _,_ [ _τ_ ( _m_ ) _, τ_ ( _i_ )] _}_ . If _ℓ_ = _m_ , we drop the horizontal strands [ _M_ ( _ℓ_ ) _, M_ ( _m_ )] and [ _M_ ( _τ_ ( _m_ )) _, M_ ( _τ_ ( _ℓ_ ))] 

   - matched to [ _ℓ, m_ ] and [ _τ_ ( _m_ ) _, τ_ ( _ℓ_ )] from _b_ . This also occurs in Cases (iv), (v), (vi), (vii), and (ix) if there are horizontal strands, but we do not mention it again. 

LIPSHITZ AND OZSVÁTH 

38 

- (iii) Compact Downward-Biting Hexagon: These are similar to the previous case, but where we have three strands, with one fixed by _τ_ and the other two exchanged by _τ_ . That is, given strands [ _i, j_ ], [ _τ_ ( _j_ ) _, τ_ ( _i_ )], and [ _m, τ_ ( _m_ )] in _a_ with _i < τ_ ( _j_ ) _< m < τ_ ( _m_ ) _< j < τ_ ( _i_ ), if there is no strand [ _p, q_ ] with _i < p < m < τ_ ( _m_ ) _< q < j_ , then _δ_[1] (� _a_ ) has a term 1 _⊗_[�] _b_ where _b_ is obtained by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _,_ [ _m, τ_ ( _m_ )] _}_ in _a_ with _{_ [ _i, τ_ ( _m_ )] _,_ [ _τ_ ( _j_ ) _, j_ ] _,_ [ _m, τ_ ( _i_ )] _}_ . 

- (iv) Compact Upward-Biting Hexagon: These are similar to the previous case. Given strands [ _i, j_ ], [ _τ_ ( _j_ ) _, τ_ ( _i_ )], and [ _m, τ_ ( _m_ )] in _a_ with _m < i ≤ j < τ_ ( _m_ ), if there is no strand [ _p, q_ ] with _m < p < i ≤ j < q < τ_ ( _m_ ), then _δ_[1] (� _a_ ) has a term 1 _⊗_[�] _b_ where _b_ is obtained from _a_ by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _,_ [ _m, τ_ ( _m_ )] _}_ with _{_ [ _m, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _m_ )] _,_ [ _i, τ_ ( _i_ )] _}_ . 

- (v) Octagons: Given non-fixed strands [ _i, j_ ], [ _τ_ ( _j_ ) _, τ_ ( _i_ )], [ _ℓ, m_ ], [ _τ_ ( _m_ ) _, τ_ ( _ℓ_ )] in _a_ with � 

- _i < τ_ ( _j_ ) _< ℓ< τ_ ( _m_ ), and no strand [ _p, q_ ] with _i < p < ℓ ≤ m < q < j_ , _δ_[1] ( _a_ ) has a term 1 _⊗_[�] _b_ where _b_ is obtained by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _,_ [ _ℓ, m_ ] _,_ [ _τ_ ( _m_ ) _, τ_ ( _ℓ_ )] _}_ in _a_ with _{_ [ _i, m_ ] _,_ [ _τ_ ( _j_ ) _, j_ ] _,_ [ _ℓ, τ_ ( _ℓ_ )] _,_ [ _τ_ ( _m_ ) _, τ_ ( _i_ )] _}_ . 

- (vi) Disjoint Half-Strip Pairs: Given non-fixed strands [ _i, j_ ] and [ _τ_ ( _j_ ) _, τ_ ( _i_ )] in _a_ and an integer _ℓ_ with _i ≤ j < ℓ< τ_ ( _i_ ), and no strand [ _p, q_ ] with _p < i < j < q < ℓ_ , _δ_[1] (� _a_ ) has a term _ρ ⊗_[�] _b_ where _b_ is obtained from _a_ by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _}_ with _{_ [ _i, ℓ_ ] _,_ [ _τ_ ( _ℓ_ ) _, τ_ ( _i_ )] _}_ and _ρ_ has a single moving strand [ _τ_ ( _ℓ_ ) _, τ_ ( _j_ )] and the same � 

- left idempotent as _a_ . 

- (vii) Overlapping Half-Strip Pairs. Given non-fixed strands [ _i, j_ ] and [ _τ_ ( _j_ ) _, τ_ ( _i_ )] in _a_ and an integer _ℓ_ with _ℓ< i ≤ j < τ_ ( _i_ ), and no strand [ _p, q_ ] with _ℓ< p < i ≤ j < q_ , _δ_[1] (� _a_ ) has a term _ρ ⊗_[�] _b_ where _b_ is obtained from _a_ by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _}_ with _{_ [ _ℓ, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _ℓ_ )] _}_ , and _ρ_ has a single moving strand [ _ℓ, i_ ]. 

- (viii) Noncompact Hexagon: Given a fixed strand [ _i, τ_ ( _i_ )] in _a_ , an integer _ℓ> τ_ ( _i_ ), and no strand [ _p, q_ ] in _a_ with _p < i < τ_ ( _i_ ) _< q < ℓ_ , _δ_[1] (� _a_ ) has a term _ρ ⊗_[�] _b_ where _b_ is obtained from _a_ by replacing [ _i, τ_ ( _i_ )] with [ _τ_ ( _ℓ_ ) _, ℓ_ ] and _ρ_ has a single moving strand [ _τ_ ( _ℓ_ ) _, i_ ] � 

- and the same left idempotent as _a_ . 

- (ix) Noncompact Octagons: Given non-fixed strands [ _i, j_ ] and [ _τ_ ( _j_ ) _, τ_ ( _i_ )] in _a_ and an integer _ℓ_ with _i ≤ j < τ_ ( _i_ ) _< ℓ_ , and no strand [ _p, q_ ] in _a_ with _p < i ≤ j < q < ℓ_ , _δ_[1] (� _a_ ) has a term _ρ ⊗_[�] _b_ where _b_ is obtained by replacing _{_ [ _i, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _i_ )] _}_ in _a_ with _{_ [ _i, τ_ ( _i_ )] _,_ [ _τ_ ( _ℓ_ ) _, ℓ_ ] _}_ and _ρ_ has a single moving strand [ _τ_ ( _ℓ_ ) _, τ_ ( _j_ )] and the same left � 

- idempotent as _a_ . 

See Figures 16 and 17. 

_Example_ 5.12 _._ We spell out _CFDR_[�] (AZ( _Z_ )) and _CFDR_[�] (AZ( _Z_ )) if _Z_ is the genus 1 pointed matched circle. The module _CFDR_[�] (AZ( _Z_ )) is generated by two elements, [2 _,_ 3] _[∗]_ and [1 _,_ 4] _[∗]_ , and the differential _δ_[1] ([1 _,_ 4] _[∗]_ ) = [3 _,_ 4] _⊗_ [2 _,_ 3] _[∗]_ . That is, in our usual notation for the torus algebra, _CFDR_[�] (AZ) is generated by _ρ[∗]_ 2[and] _[ρ][∗]_ 123[.][The][right][idempotent][of] _[ρ]_[2][is] _[ι]_[0][and][the] right idempotent of _ρ_ 123 is _ι_ 1 (i.e., _ρ_ 2 _ι_ 0 = _ρ_ 2 and _ρ_ 123 _ι_ 1 = _ρ_ 123), so the left idempotent of _ρ[∗]_ 2[is] _[ι]_[1][and][the][left][idempotent][of] _[ρ][∗]_ 123[is] _[ι]_[0][.][The][differential][is] _[δ]_[1][(] _[ρ][∗]_ 123[) =] _[ ρ]_[3] _[⊗][ρ][∗]_ 2[(which][is] consistent with the idempotents). The differential comes from a noncompact hexagon. 

Similarly, the module _CFDR_[�] (AZ( _Z_ )) is generated by elements [2[�] _,_ 3] and [1[�] _,_ 4]. The differential is given by _δ_[1] ([2[�] _,_ 3]) = [1 _,_ 2] _⊗_ [1[�] _,_ 4]. In the usual notation for the torus algebra, this � is _δ_[1] ( � _ρ_ 2) = _ρ_ 1 _⊗ ρ_ 123. (The differential again comes from a noncompact hexagon.) The left 

REAL BORDERED FLOER HOMOLOGY 

39 

**==> picture [450 x 487] intentionally omitted <==**

**----- Start of picture text -----**<br>
w<br>(i) (ii) (iii) (iv) (v)<br>w ⊗ ⊗ ⊗ ⊗<br>(vi) (vii) (viii) (ix)<br>Figure 16. Differential on CFDR [�] (AZ( Z )) . Conventions are as in Figure 15.<br>1 1 1<br>2 2 2<br>3 3 3<br>4 4 4<br>5 5 5<br>6 6 6<br>7 7 7<br>8 8 8<br>1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8<br>**----- End of picture text -----**<br>


Figure 17. **Domains for terms in the differential on** _CFDR_[�] (AZ( _Z_ )) **.** Left: domains of Type (i) (solid gray), (ii) (crosshatched), and (iii) (dots). Center: Type (iv) (solid gray), (v) (crosshatched), and (vi) (dots). Right: Type (vii) (solid gray), (viii) (crosshatched), and (ix) (dots). To conserve space, these are mostly not the same examples as in Figure 16. 

� idempotent of _ρ_ 2 is _ι_ 1, so the left idempotent of _ρ_ 2 is _ι_ 0. Similarly, the left idempotent of _ρ_ �123 is _ι_ 1 (which is consistent with _δ_[1] ). 

_Example_ 5.13 _._ The complex _CFDR_[�] (AZ( _Z_ )) for _Z_ the split, genus 2 pointed matched circle is shown in Figure 18. Because of the low genus, only terms of types (i), (vi), (vii), and (ix) 

LIPSHITZ AND OZSVÁTH 

40 

– contribute to the differential. (It is immediate that there are no terms of types (ii) (v); to see that there are no terms of type (viii) involves considering the idempotents.) As an � example of the idempotents, the idempotent of the state _{_ [2 _,_ 2] _,_ [4 _,_ 4] _,_ [5 _,_ 5] _,_ [7 _,_ 7] _}_ (which is denoted [[2] _·_[5] _·_[]][in][Figure][18][)][has][the][matched][pairs] _[{]_[1] _[,]_[ 3] _[}]_[and] _[{]_[6] _[,]_[ 8] _[}]_[occupied][(i.e.,][is] � _{_ [1 _,_ 1] _,_ [3 _,_ 3] _,_ [6 _,_ 6] _,_ [8 _,_ 8] _}_ ). The idempotent of the state _{_ [3 _,_ 6] _,_ [4 _,_ 5] _}_ (which is denoted [[3] 6[4] 5[]] in Figure 18) has the matched pairs _{_ 5 _,_ 7 _}_ and _{_ 6 _,_ 8 _}_ occupied. As an example of the differential, 

**==> picture [410 x 112] intentionally omitted <==**

The first two terms are of type (vi), the next three of type (vii), and the last three are of � type (ix). Note that there is, for example, no type (vi) term _{_ [6 _,_ 7] _,_ [1 _,_ 1] _,_ [3 _,_ 3] _}⊗{_ [2 _,_ 4] _,_ [5 _,_ 7] _}_ here because of the idempotents. As another example, 

**==> picture [188 x 18] intentionally omitted <==**

coming from a term of type (i). We could equivalently write 1 as the idempotent corresponding to this state, which is _{_ [5 _,_ 5] _,_ [6 _,_ 6] _,_ [7 _,_ 7] _,_ [8 _,_ 8] _}_ . 

Recall that the strands diagrams in _A_ ( _Z_ ) where two moving strands overlap—the elements whose supports have multiplicity _>_ 1 somewhere—span an acyclic ideal in _A_ ( _Z_ ) [LOT15, Proposition 4.2]. So, the quotient _A[′]_ ( _Z_ ) by this ideal is quasi-isomorphic to _A_ ( _Z_ ), and when performing computations in bordered Floer homology it suffices to work over the smaller algebra _A[′]_ ( _Z_ ). We show that a similar phenomenon occurs for _CFDR_[�] (AZ( _Z_ )). We then observe that, in the case of real pointed matched circles giving surfaces with orientable quotients, this leads to a particularly simple description of _CFDR_[�] (AZ( _Z_ )). 

**Lemma 5.14.** _For any real pointed matched circle Z, the strands diagrams which have multiplicity greater than_ 1 _somewhere span a contractible sub-type-D-structure of CFDR_[�] (AZ( _Z_ )) _. Thus, CFDR_[�] (AZ( _Z_ )) _is homotopy equivalent to its quotient by this sub-type-D-structure._ 

The quotient is, of course, generated by the strands diagrams with multiplicity 0 or 1 everywhere. 

_Proof._ It is immediate from the definition of the differential that these strands diagrams span a sub-type- _D_ -structure. The proof that this substructure is contractible is an adaptation of the corresponding proof for the bordered Floer algebras [LOT15, Theorem 9(2)]. Let _P_ denote this sub-structure. 

Let _A_ +( _Z_ ) be the augmentation ideal, generated by all strands diagrams with at least one moving strand, so _A_ ( _Z_ ) _/A_ +( _Z_ ) = _I_ ( _Z_ ) is a direct sum of copies of F2, one for each idempotent strands diagram. Then _P_ is contractible over _A_ ( _Z_ ) if and only if the induced type _D_ structure _I_ ( _Z_ ) ⊠ _P_ is contractible. That is, when proving that _P_ is contractible, it 

REAL BORDERED FLOER HOMOLOGY 

41 

**==> picture [386 x 374] intentionally omitted <==**

**----- Start of picture text -----**<br>
[5]<br>( [1] 2 [7] 8 [)] �� 1728 26 · �� ( [2] · · [)] � 37 6 · � ( [2] 6 [3] 7 [)]<br>� 67 2 · � 1<br>( [1] 3 [6] 8 [)] � 67 1 · � 3 26 � 15 6 · � ( [2] 7 [3] 6 [)]<br>� 76 · �<br>16 25<br>� 27 · �<br>3 26 4 56<br>� 765 · � � 87 · �<br>( [2] 3 [6] 7 [)] 4 56 ( [1] 8 [4] 5 [)]<br>15 26 � 876 · � 3 6<br>� 486 · � � 5 · �<br>� 56 1 · � � 586 2 · � � 5346 26 · � 1<br>1 6<br>( [2] 4 [5] 7 [)] � 78 2 · � 2 56 � 265 56 · � � 7 · � ( [1] 5 [4] 8 [)]<br>� 87 · �<br>2 5<br>� 6 · �<br>� 154286 26 · � � 2876 56 · � � 48765 56 · �<br>26 15 1 65<br>� 73 · � � 76 · �<br>25 16<br>( [1] 4 [5] 8 [)] � 63 · � ( [3] 6 [4] 5 [)]<br>1 65 4 5<br>� 765 · � � 8 · �<br>1<br>5 2<br>( [3] 4 � [5] 6 8 [)] · � � 2 8765 56 · � � 465 15 · � ( [3] 5 [4] 6 [)]<br>5 2 4 5<br>� 6 · � � 6 · �<br>( [1] · [6] · [)] ( [1] 8 [2] 7 [)]<br>� 28 5 · � ( [1] 7 [2] 8 [)] 1<br>**----- End of picture text -----**<br>


Figure 18. **The complex** _CFDR_[�] (AZ( _Z_ )) **for the split, genus** 2 **pointed matched circle.** For readability, we are using slightly different notation for generators of the algebra: ([1] 8[2] 7[)][,][for][instance,][means][the][pair][of] strands [1 _,_ 8] _,_ [2 _,_ 7], and ([1] 2[6] _·_[)][means][the][single][strand][[1] _[,]_[ 2]][with][left][idem-] potent _{_ 1 _,_ 3 _,_ 6 _,_ 8 _}_ . All the algebra coefficients in the differential are either 1 or have a single moving strand (hence have one dot inside the matrix). Type (i), (vi), (vii), and (ix) terms contribute to the differential. 

suffices to consider only the provincial differential—the terms 1 _⊗_[�] _b_ in the differential—and we will do so for the rest of the argument. We can (and do) regard _P_ with this provincial differential as an ordinary chain complex, by identifying 1 _⊗_[�] _b_ with[�] _b_ . 

There is a filtration on _P_ by the number of horizontal strands; the differential preserves or decreases this filtration. We will show that the homology of the associated graded complex is trivial. Additionally, _P_ decomposes as direct sums over the left and right idempotents, and over the supports of the algebra elements (in _H_ 1( _Z,_ **a** )). (This uses the fact that we are only considering the provincial differential.) So, we fix a choice of left and right idempotents 

LIPSHITZ AND OZSVÁTH 

42 

**==> picture [10 x 6] intentionally omitted <==**

**----- Start of picture text -----**<br>
w<br>**----- End of picture text -----**<br>


Figure 19. **Perturbing the endpoints.** The element of _A_ ( _Z_ ) on the left maps to the element of _A_ (8 _k_ ) on the right, by sending initial endpoints _i_ to 2 _i_ and terminal endpoints _j_ to 2 _j −_ 1. 

**==> picture [364 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
H H H H H H<br>w 0 0 0<br>j<br>i i ℓ m<br>i i τ ( j ) i i<br>j ℓ<br>(H-1) (H-1) (H-1) (H-2) (H-3) (H-4)<br>**----- End of picture text -----**<br>


Figure 20. **The homotopy** _H_ **.** Conventions are as in Figures 15 and 16. 

and a support, and denote by _P_[�] the summand of the associated graded complex with this pair of idempotents and support, and _j_ moving strands. (From the definition of _P_ , _j ≥_ 2.) In _P_[�] , the differential does not resolve crossings on horizontal strands. It follows that the chain complex _P_[�] is independent of the choice of matching. 

Consider a chain complex _Q_ defined like _CFDR_[�] 

_CFDR_ (AZ( _Z_ )), except: 

- If **a** for _Z_ consists of 4 _k_ points _{_ 1 _, . . . ,_ 4 _k}_ , then _Q_ is based on a pointed matched circle with 8 _k_ points _{_ 1 _, . . . ,_ 8 _k}_ , and 

- there is no matching in the definition of _Q_ . 

As in the algebra case [LOT15, Proof of Theorem 9(2)], we can embed _P_[�] in _Q_ . Fix a state � _a ∈ P_[�] . For each moving (non-horizontal) strand _ξ_ = [ _i, j_ ] of _a_ , consider a new strand [2 _i,_ 2 _j −_ 1]. Let _a[′] ∈ C∗_ consist of all the strands _ξ[′]_ , for _ξ_ a strand of _a_ . See Figure 19. Note that the symmetry of _a_ exchanging [ _i, j_ ] and [4 _k_ + 1 _− i,_ 4 _k_ + 1 _− j_ ] induces a symmetry of _a[′]_ exchanging [ _ℓ, m_ ] and [8 _k_ + 1 _− m,_ 8 _k_ + 1 _− ℓ_ ]. In particular, _a[′] ∈ C∗_ . Moreover, because the differential on _P_[�] does not affect the horizontal strands, this induces a chain map _P_[�] _→ Q_ . Of course, all elements in the image have the same support; let _Q_[�] denote the summand with this support. Then _P_[�] _[∼]_ = _Q_[�] , and we will show that _Q_[�] is acyclic. 

REAL BORDERED FLOER HOMOLOGY 

43 

We define a map _H_ : _Q_[�] _→ Q_[�] so that 

**==> picture [282 x 13] intentionally omitted <==**

Consider the first point _i ∈{_ 1 _, . . . ,_ 8 _k}_ so that elements of _Q_[�] have multiplicity 2 above _i_ and 1 below _i_ . Given a state � _a ∈ Q_[�] , let _ξ_ and _ξ[′]_ be the two strands that cross the point _i_ + 1 _/_ 2, so that _ξ_ starts at _i_ and _ξ[′]_ starts at a point below _i_ and ends at a point above _i_ . Observe � that no strand starts or ends between the initial points of _ξ_ and _ξ[′]_ . Define _H_ ( _a_ ) in cases as follows: 

- (H-1) If _ξ_ and _ξ[′]_ cross, define _H_ (� _a_ ) = 0. 

- (H-2) If _ξ_ = [ _i, j_ ] and _ξ[′]_ = [8 _k_ + 1 _− j,_ 8 _k_ + 1 _− i_ ] = [ _τ_ ( _j_ ) _, τ_ ( _i_ )] (so _ξ_ and _ξ[′]_ do not cross, but are exchanged by _τ_ ), let _H_ (� _a_ ) be the result of replacing _{ξ, ξ[′] }_ with _{_ [ _i,_ 8 _k_ + 1 _− i_ ] _,_ [8 _k_ + 1 _− j, j_ ] _}_ (i.e., making them cross). (Note that 8 _k_ + 1 _− j < i_ , from how we chose _ξ_ and _ξ[′]_ .) 

- (H-3) If _ξ_ = [ _i,_ 8 _k_ + 1 _− i_ ] = [ _i, τ_ ( _i_ )] and _ξ[′]_ = [ _j, ℓ_ ], since _ξ_ and _ξ[′]_ do not cross we have � 

- _ℓ<_ 8 _k_ + 1 _− i <_ 8 _k_ + 1 _− j_ . Thus, _a_ also contains _ξ[′′]_ = [ _τ_ ( _ℓ_ ) _, τ_ ( _j_ )]. Let _H_ ( _a_ ) be the result of replacing _{ξ, ξ[′] , ξ[′′] }_ by _{_ [ _j, τ_ ( _j_ )] _,_ [ _i, ℓ_ ] _,_ [ _τ_ ( _ℓ_ ) _, τ_ ( _i_ )] _}_ . That is, we introduce an equivariant pair of crossings. 

- (H-4) Otherwise, _ξ_ = [ _i, j_ ], _ξ[′]_ = [ _ℓ, m_ ], and _a_ also contains the chords [ _τ_ ( _j_ ) _, τ_ ( _i_ )] and � 

- [ _τ_ ( _m_ ) _, τ_ ( _ℓ_ )]. Let _H_ ( _a_ ) be the result of replacing these four chords by the chords _{_ [ _i, m_ ] _,_ [ _ℓ, j_ ] _,_ [ _τ_ ( _j_ ) _, τ_ ( _ℓ_ )] _,_ [ _τ_ ( _m_ ) _, τ_ ( _i_ )] _}_ . 

See Figure 20. 

We verify Equation (5.15) by a case analysis. First, suppose that _H_ (� _a_ ) = 0, as in Case (H1) of the definition of _H_ . There is exactly one term in _d_ ( _a_ ) of type (i)–(iv) that results in _ξ_ and _ξ[′]_ not crossing. Indeed, none of these terms creates a double crossing, because no strands start between the initial points of _ξ_ and _ξ[′]_ ; and type (v) does not contribute, because in that case the bottom two strands do not cross. So, there is exactly one term that contributes to � _H ◦ ∂_ , and ( _H ◦ ∂_ )( _a_ ) = � _a_ . 

Next, suppose that _ξ_ and _ξ[′]_ are as in Case (H-2) of the definition of _H_ . Terms in _∂ ◦ H_ and _H ◦ ∂_ not involving these strands at all cancel in pairs. (This uses the fact that no strands start between the initial points of _ξ_ and _ξ[′]_ , to deduce that none of these terms involve double crossings with _ξ_ or _ξ[′]_ or their images under _H_ .) Applying _H_ and then resolving the new crossing gives the identity map. The remaining terms where we apply this type of _H_ and then a differential are of the following sorts: 

- Performing _H_ and then a type (i) differential (not at the new crossing) cancels with performing a type (iii) differential and then a case (H-3) _H_ . (Note that the type (i) differential leaves the outermost strand unchanged, by the double crossing rule.) 

- Performing _H_ and then a type (iv) differential (not involving the outermost strand) cancel with performing a type (v) differential and then a case (H-3) _H_ . (Type (iv) differentials involving the outermost strand do not occur.) 

Other than the identity, there are no nonzero terms coming from applying a differential and then a type (H-2) _H_ . 

Next, suppose that _ξ_ and _ξ[′]_ are as in Case (H-3) of the definition of _H_ . Applying _H_ and then a type (iv) differential gives the identity map. Other terms in _∂ ◦ H_ (for this case of _H_ ) are: 

LIPSHITZ AND OZSVÁTH 

44 

- A case (H-3) _H_ followed by a type (i) differential. These cancel with applying a type (i) differential and then a case (H-4) _H_ . 

- A case (H-3) _H_ followed by a type (ii) differential. These cancel with applying a type (ii) differential and then a case (H-3) _H_ . 

- A case (H-3) _H_ followed by a type (iv) differential. These cancel with applying a type (iv) differential and then a case (H-3) _H_ . 

- A case (H-3) _H_ followed by a type (v) differential. These cancel with applying a type (v) differential and then a case (H-3) _H_ , where the (H-3) does not use either of the symmetric strands produced by the type (v) differential. 

This also accounts for all the terms in _H ◦∂_ for this case of _H_ , except for type (v) differentials and then case (H-3) using the longer of the two symmetric strands. Those terms canceled terms from case (H-2), above. (There is also the type (iv) differential followed by _H_ on the resulting three strands giving the identity map, from case (H-1).) 

Finally, suppose that _ξ_ and _ξ[′]_ are as in Case (H-4) of the definition of _H_ . Applying _H_ and then a type (ii) differential to the resulting four strands gives the identity map term. Other terms in _∂ ◦ H_ (for this case of _H_ ) are: 

- A case (H-4) _H_ followed by a type (ii) differential using two of these four strands. These cancel with type (ii) differentials followed by case (H-4) _H_ . 

- A case (H-4) _H_ followed by a type (iii) differential. These cancel with type (iii) differentials followed by case (H-4) _H_ . 

- A case (H-4) _H_ followed by a type (v) differential. These cancel with type (v) differentials followed by case (H-4) _H_ . 

The other terms in this case of _H ◦ ∂_ are the identity from a type (ii) differential followed by _H_ ; a type (i) differential followed by a type (H-4) _H_ , which canceled with terms in a type (H3) _H_ followed by a type (i) differential; and a type (iv) differential followed by a type (H-4) _H_ , which canceled with terms in a type (H-3) _H_ followed by a type (iv) differential. 

This completes the verification of Equation (5.15), and hence of the proof of the lemma. □ 

**Corollary 5.16.** _Let Z be a real pointed matched circle so that the real surface_ ( _F_ ( _Z_ ) _, τ_ ) _has F_ ( _Z_ ) _/τ orientable. In particular, Z is the connected sum Z[′]_ #( _−Z[′]_ ) _of a pointed matched circle with its mirror, and there is an embedding A_ ( _Z[′]_ ) _⊗A_ ( _−Z[′]_ ) _�→A_ ( _Z_ ) _. Let r_ : _A_ ( _Z[′]_ ) _→A_ ( _−Z[′]_ ) _be the anti-isomorphism induced by reflection. Then CFDR_[�] (AZ( _Z_ )) _is homotopy equivalent to a type D structure with generators in bijection with multiplicity-1 strands diagrams in A_ ( _Z[′]_ ) _. Moreover, writing_ [ _a ⊗ ra_ ] _for the generator corresponding to a, the left idempotent of_ [ _a ⊗ ra_ ] _is ι[′] ⊗ rι[′] , where ι[′] is the complementary idempotent to the left idempotent of a; and the differential is given by_ 

**==> picture [469 x 29] intentionally omitted <==**

_Proof._ Consider the set of generators � _a_ of _CFDR_[�] (AZ( _Z_ )) so that some strand in _a_ crosses _w_ (or, equivalently, there is a strand [ _i, j_ ] in _a_ with _i ≤_ 2 _k < j_ ). We claim that there are an even number of strands in _a_ crossing _w_ . Indeed, suppose the left idempotent of _a_ has 2 _m_ horizontal strands below _w_ (i.e., _m_ pairs of such strands), and _a_ has _n_ moving strands which cross _w_ . Then the left idempotent of _a_ has 4 _k −_ 2 _m_ horizontal strands above _w_ , so the right idempotent of _a_ has 4 _k −_ 2 _m_ + 2 _n_ horizontal strands above _w_ . Since _a_ is fixed 

REAL BORDERED FLOER HOMOLOGY 

45 

**==> picture [447 x 187] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 7 2 6 ( [2] · [5] · [)] ι 1  ⊗ ι 0<br>� 2 8 · � 1 ρ⊗ 1 ⊗ρ 31<br>[7] 7 2 [6]<br>( [1] 2 8 [)] � 8 · � ( [1] · · [)] ρ 1  ⊗ ρ 3 1 ⊗ρ 3 ι 0  ⊗ ι 1<br>� 3 5 4 6 2 6 · � 1 ρ⊗ 3 ⊗ρ 11<br>� 67 2 · � � 56 2 · � 1 ⊗ρ 2 1 ⊗ρ 1<br>� 67 1 · � � 1 5 4 86 2 6 · � 1 ⊗ρ 2 ρ 1123 ⊗ρ⊗ 11<br>( [1] 3 [6] 8 [)] � 2 6 3 7 1 5 · � � 58 2 · � ( [3] 4 [5] 6 [)] ρ 12  ⊗ ρ 23 1 ρ⊗ 2 ⊗ρ 21 1 ⊗ρ 123 ρ 3  ⊗ ρ 1<br>� 1 6 2 7 2 5 · � � 586 2 · � 1 ρ⊗ 1 ⊗ρ 21 1 ⊗ρ 1<br>2 5 1 6<br>� 3 6 · � 1 ρ⊗ 2 ⊗ρ 11<br>( [2] 3 [6] 7 [)] ( [1] 4 [5] 8 [)] ρ 2  ⊗ ρ 2 ρ 123  ⊗ ρ 123<br>� 56 1 · � ( [2] 4 [5] 7 [)] � 1 5 2 86 2 6 · � 1 ⊗ρ 1 ρ 23  ⊗ ρ 12 ρ 1 ρ 123 ⊗ 1 ⊗ρ⊗ 111<br>**----- End of picture text -----**<br>


Figure 21. **The small model for the complex** _CFDR_[�] (AZ( _Z_ )) **for the split, genus** 2 **pointed matched circle.** Left: Conventions are as in Figure 18. Right: the same model, but in terms of the elements _a ⊗ ra_ and _ρ ⊗_ 1 or 1 _⊗ rρ_ of the statement of Corollary 5.16. 

by _τ_ , 4 _k −_ 2 _m_ + 2 _n_ = 2 _m_ , so _n_ is even, as claimed. Thus, if we quotient by the sub-type- _D_ -structure from Lemma 5.14, we are left with a type _D_ structure generated by symmetric strands diagrams which do not cross _w_ , that is, the set of generators from the statement of the corollary. The differential on the quotient only includes terms which start and end at such generators, which again are exactly the ones in the lemma statement (from rectangle pairs and the two types of half-strip pairs). □ 

_Example_ 5.17 _._ Figure 21 shows the model from Corollary 5.16 for _CFDR_[�] (AZ( _Z_ )) for _Z_ the split genus 2 pointed matched circle (cf. Example 5.13). Figure 22 shows the model from Lemma 5.14 for _CFDR_[�] (AZ( _Z_ )) where _Z_ is the antipodal genus 2 pointed matched circle; note that Corollary 5.16 does not apply in this case, but the answer is still attractively simple. 

## 6. Pairing theorem 

In this section, we give two proofs of the pairing theorem for the tensor product _CFA_[�] ( _H[′]_ )⊠ � _CFDR_ ( _H, τ_ ). First, we give a self-contained proof via nice diagrams, assuming _H[′]_ and _H_ are nice. Then we explain how the time dilation proof of the pairing theorem extends to the real case; to avoid repeating a large amount of verbiage, that argument is meant to be read alongside the proof in the unreal case. 

## 6.1. **The pairing theorem via nice diagrams.** 

**Theorem 6.1.** _Let_ ( _H, τ_ ) _be a real nice bordered Heegaard diagram with boundary_ ( _−Z_ ) _⨿Z[β] , and H[′] a nice arced bordered Heegaard diagram with boundary_ ( _−Z[′]_ ) _⨿Z. Then there is a homotopy equivalence of type D structures_ 

**==> picture [380 x 17] intentionally omitted <==**

LIPSHITZ AND OZSVÁTH 

46 

**==> picture [254 x 191] intentionally omitted <==**

**----- Start of picture text -----**<br>
( [1] · [4] · [)]<br>3 2 6 3<br>� 4 · � � 8 · �<br>( [3] 4 [5] 6 [)] ( [1] 3 [6] 8 [)]<br>2 3 7 2<br>� 4 · � � 8 · �<br>2 4 6 4<br>� 3 · � � 7 · �<br>5 4 1 6 4<br>� 6 · � � 3 7 · �<br>( [2] 4 [5] 7 [)] ( [1] 2 [7] 8 [)]<br>5 4 1 7 4 2<br>� 7 · � � 2 8 · �<br>( [2] · [3] · [)]<br>**----- End of picture text -----**<br>


Figure 22. **The small model for the complex** _CFDR_[�] (AZ( _Z_ )) **for the antipodal, genus** 2 **pointed matched circle.** Conventions are as in Figure 18. 

_Proof._ For definiteness, assume that _H_ is negative real nice. The identification of generators is clear. We first analyze rigid holomorphic curves in _H[′] ∪H ∪_ ( _−H[′]_ ) _[β]_ and show that they appear in the differential on the tensor product _CFDA_[�] ( _H[′]_ ) ⊠ _CFDR_[�] ( _H, τ_ ); then we show that no other terms appear in that differential. 

There are three kinds of rigid holomorphic curves in _H[′] ∪H ∪_ ( _−H[′]_ ) _[β]_ : 

- (1) Holomorphic curves as in Proposition 5.2 where the domain lies entirely in _H[′] ⨿_ ( _−H[′]_ ) _[β]_ (and the components of the curve over _H_ are trivial strips). 

- (2) Holomorphic curves as in Proposition 5.2 (or Figure 4) where the domain lies entirely in _H_ (and the components of the curve over _H[′] ⨿_ ( _−H[′]_ ) _[β]_ are trivial strips). 

- (3) Holomorphic curves as in Proposition 5.2 where the domain intersects all three of _H_ , _H[′]_ , and ( _−H[′]_ ) _[β]_ nontrivially. 

In Case (1), the curve is a bigon pair, rectangle pair, or half-strip pair (since those are the only rigid domains with two connected components). So, the component in _H[′]_ contributes to the operation _δ_ 1[1][on] _CFDA_[�] ( _H[′]_ ), and thus contributes to the differential on the tensor product via the operation 

**==> picture [252 x 30] intentionally omitted <==**

In Case (2), by definition, the domain is one that contributes to the differential on � _CFDR_ ( _H_ ) with coefficient 1. So, this contributes to the differential on the tensor product via the operation 

- (6.3) 

**==> picture [54 x 57] intentionally omitted <==**

_._ 

REAL BORDERED FLOER HOMOLOGY 

47 

In Case (3), we have a holomorphic curve _u_ : _S →_ (Σ _[′] ∪_ Σ _∪_ ( _−_ Σ _[′]_ )) _×_ [0 _,_ 1] _×_ R of one of the types in Proposition 5.2 (Figure 4). Write _∂_ Σ = _Z ⨿ Z[β]_ . Then (perhaps after perturbing the almost complex structure to be generic) the preimages _A_ = ( _π_ Σ _◦ u_ ) _[−]_[1] ( _Z_ ) and _B_ = ( _π_ Σ _◦ u_ ) _[−]_[1] ( _Z[β]_ ) satisfy: 

- _A_ and _B_ are 1-dimensional submanifolds of _S_ (with boundary), 

- _A ∩ B_ = _∅_ , 

- _∂A_ is contained in the part of _∂S_ mapped to the _α_ -curves, and _∂B_ in the part of _∂S_ mapped to the _β_ -curves, 

- _A_ and _B_ are disjoint from the preimage of the fixed set in Σ, and 

- _A ∪ B_ separates _S_ into _SA ∪ S[′] ∪ SB_ , each of which contains at least one _x_ -corner and one _y_ -corner. (This follows from the fact that the _α_ -curves in a bordered Heegaard diagram are homologically linearly independent.) 

In most cases, no such 1-manifolds _A_ and _B_ exist. (For example, for a bigon, any arc _A_ with boundary on the _α_ -boundary of _S_ splits off a component with no _x_ or _y_ -punctures.) Indeed, the only cases in which such _A_ and _B_ exist are compact hexagons, octagons, and rectangle pairs. In each case, there is essentially one way to decompose the curve: as a half-strip in each of _H[′]_ and ( _−H[′]_ ) _[β]_ , and a noncompact hexagon, noncompact octagon, or half-strip pair in _H_ . In particular, the part of the curve in _H[′]_ contributes an operation of the form _δ_ 2[1][(] **[x]** _[′][, ρ]_[) =] **[ y]** _[′]_[ to] _CFDA_[�] ( _H[′]_ ), and the part in _H_ contributes an operation _δ_[1] ( **x** ) = _ρ⊗_ **y** . Taken together, the domain contributes a term 1 _⊗_ ( **y** _[′] ⊗_ **y** ) in _δ_[1] ( **x** _[′] ⊗_ **x** ) on the glued diagram, as 

**==> picture [269 x 61] intentionally omitted <==**

So, we have proved that every term in the differential on _CFDR_[�] ( _H[′] ∪H ∪_ ( _−H[′]_ ) _[β] ,_ � _τ_ ) is also a term in the differential on the tensor product. Conversely, since _H[′]_ is nice, the only nontrivial operations on _CFDA_[�] ( _H[′]_ ) are _δ_ 1[1][and] _[ δ]_ 2[1][, and these come from half-strips with] boundary on _∂LH[′]_ and provincial bigons and rectangles, for _δ_ 1[1][, and the map] _[ δ]_ 2[1][(] **[x]** _[,]_[ 1) = 1] _[⊗]_ **[x]** from the definition of _CFDA_[�] ( _H[′]_ ) as strictly unital and half-strips with boundary on _∂RH[′]_ for _δ_ 2[1][.][In][the][latter][cases,][the][algebra][input][must][come][from][a][rigid][curve][in] _CFDR_[�] ( _H_ ). So, the only terms in the differential on the tensor product are the ones accounted for by Formulas (6.2)–(6.4), above. □ 

6.2. **General pairing theorem via time dilation.** In this section, we observe that the time dilation proof of the pairing theorem also carries over to the real case. In particular, this proves a version of Theorem 6.1 without the requirement that the diagrams be nice: 

**Theorem 6.5.** _Let_ ( _H, τ_ ) _be a real bordered Heegaard diagram with boundary_ ( _−Z_ ) _⨿Z[β] , and H[′] an arced bordered Heegaard diagram with boundary_ ( _−Z[′]_ ) _⨿Z. Then there is a homotopy equivalence of type D structures_ 

_A_ ( _Z[′]_ ) _CFDR_ � ( _H[′] ∪H ∪_ ( _−H[′]_ ) _[β] ,_ � _τ_ ) _≃[A]_[(] _[Z][′]_[)] _CFDA_[ �] ( _H[′]_ ) _A_ ( _Z_ ) ⊠ _[A]_[(] _[Z]_[)] _CFDR_[ �] ( _H, τ_ ) _._ 

**Corollary 6.6.** _Suppose_ ( _Y[′] ∪F_ ( _Z_ ) _Y ∪F_ ( _Z_ ) _Y[′] ,_ � _τ_ ) _is a closed real 3-manifold decomposed_ � _into a real bordered_ 3 _-manifold_ ( _Y, τ_ ) _and a pair of bordered_ 3 _-manifold Y[′] exchanged by τ . Then_ � _CFR_ ( _Y[′] ∪F_ ( _Z_ ) _Y ∪F_ ( _Z_ ) _Y[′] ,_ � _τ_ ) _≃ CFA_[�] ( _Y[′]_ ) _A_ ( _Z_ ) ⊠ _[A]_[(] _[Z]_[)] _CFDR_[ �] ( _Y, τ_ ) _._ 

LIPSHITZ AND OZSVÁTH 

48 

_Proof._ We recall the pairing proof in the unreal case, and note which arguments change in the real case. To minimize confusion, we will prove Corollary 6.6 (where _∂Y[′]_ is connected), rather than the more general Theorem 6.5. 

The proof starts by stretching the neck along _∂H_ [LOT18, Section 9.1]; now we do so while respecting the involution _τ_ (i.e., using the same conformal parameters on the two components of _∂H_ ). Holomorphic curves degenerate to matched holomorphic curves (cf. [LOT18, Definition 9.2]). Since we are now splitting the surface into three components, not two, we obtain matched triples, instead of pairs: holomorphic curves ( _u_ 1 _, u_ 2 _, u_ 3) with _u_ 1 in Σ _[′] ×_ [0 _,_ 1] _×_ R, _u_ 2 a real curve in Σ _×_ [0 _,_ 1] _×_ R, and _u_ 3 = _τ_ ( _u_ 1) in ( _−_ Σ _[′]_ ) _[β] ×_ [0 _,_ 1] _×_ R. The matched expected dimension formula [LOT18, Equation (9.3)] is replaced by 

**==> picture [416 x 35] intentionally omitted <==**

(Really, there are three surfaces _S_ 1 _, S_ 2 _, S_ 3 = _η_ ( _S_ 1) and three domains _B_ 1 _, B_ 2 _, B_ 3 = _−τ∗_ ( _B_ 1), and the formula looks a little more symmetric in these terms. The partition _P_ 2 is essentially two copies of _P_ , as in Proposition 3.7, and _m_ = _|P_ 1 _|_ =[1] 2 _[|][P]_[2] _[|]_[.)][The][moduli][space][of][real] matched triples is transversely cut out by a simple extension of the unreal case [LOT18, Proposition 9.4]. The curves _ui_ are strongly boundary monotone [LOT18, Lemma 9.5]. The count of the matched moduli space agrees with the counts of holomorphic curves in _H[′] ∪H ∪_ ( _−H[′]_ ) for appropriate almost complex structures by an analogous argument to the unreal case [LOT18, Proposition 9.6], but gluing respecting the real involution. As in the unreal case, when stretching the neck, embedded curves converge to embedded curves, and every pair of Reeb chords at the same height are nested or disjoint [LOT18, Lemma 9.8]. (That proof uses the fact that the homology class determines the Euler characteristic for embedded curves which, as noted in the proof of Proposition 3.7, holds without change in the real case.) 

Next, we deform the matching condition ev( _u_ 1) = ev( _u_ 2) = ev( _u_ 3) to ev( _u_ 1) = _T_ ev( _u_ 2) = ev( _u_ 3), to obtain the moduli space of _T_ -matched pairs. Transversality (for generic _T_ , cf. [LOT18, Lemma 4.14]) follows as in the previous paragraph. The next result is a classification of ends of 1-dimensional moduli spaces [LOT18, Proposition 9.17], via the sourcedependent index formula. The claim, that these correspond to 2-story curves or degenerations of a single split or join component, still holds (except that components at _e∞_ come in pairs, exchanged by _τ_ ). Running briefly through that part of the argument, by Formula (3.8) we have 

**==> picture [228 x 15] intentionally omitted <==**

where _m_ 0 is the number of east punctures of _S_ 1 (which is half the number of east punctures of _S_ 2). Moreover, if _T_ denotes the components at _e∞_ between _u_ 1 and _u_ 2, then 

**==> picture [310 x 15] intentionally omitted <==**

(Here _T_ refers only to the components between _S_ 1 and _S_ 2, not those between _S_ 2 and _S_ 3 = _η_ ( _S_ 1), but we are using _m_ 2 to denote the count of _e_ punctures on both sides of _S_ 2 _[′]_[.)][Thus,] with _k_ the number of components of _T_ , an upper bound for the dimension of the space of 

REAL BORDERED FLOER HOMOLOGY 

49 

(real) limit curves for generic _J_ is 

**==> picture [442 x 73] intentionally omitted <==**

This restricts the cases as in the unreal proof. (Note that, because of the symmetry, _m_ 2 is even and the case _m_ 2 = _k_ + 1 is replaced by _m_ 2 = _k_ + 2, corresponding to one new puncture on each side of _u_ 2.) 

The proof that combs in the ends of these moduli spaces with curves at _e∞_ cancel in pairs is the same as in the unreal case [LOT18, Proposition 9.18], but gluing respecting the real involution (as usual). This implies that the _T_ -matched moduli spaces induce a chain complex, as in the unreal case [LOT18, Proposition 9.19]. 

The next step is to consider moduli spaces interpolating between different values of _T_ , the so-called _ψ_ -matched moduli spaces. There is again a classification of ends of the 1- dimensional moduli spaces [LOT18, Lemma 9.21] (this time, with proof omitted); the (omitted) proof adapts to the real case the same way as above (with the same index computations). In particular, different values of _T_ give homotopy equivalent chain complexes, as in the unreal case [LOT18, Proposition 9.22]. 

The next step is to send _T →∞_ . In this limit, _T_ -matched curves converge to (the evident real analogue of) ideal matched holomorphic combs; since the real moduli spaces are subspaces of the unreal ones, and the statement did not use transversality or the index, the unreal case [LOT18, Proposition 9.26] implies the real case. We then introduce simple ideal-matched curves [LOT18, Definition 9.28]; in the real case, these are triples ( _U_ 1 _, U_ 2 _, U_ 3) where _U_ 1 has at most one story, _U_ 3 = _τ_ ( _U_ 1), _U_ 2 is a real comb with perhaps many stories; and either: 

- (1) _U_ 1 and _U_ 3 are trivial while _U_ 2 is a provincial holomorphic curve (no _e∞_ punctures) with one story and real index 1, or 

- (1 _[′]_ ) _U_ 2 is trivial, and _U_ 1 is a provincial holomorphic curve with one story and index 1 (and _U_ 3 = _τ_ ( _U_ 1)), or 

- (2) each story of _U_ 2 has at least one _e_ puncture and real index 1 (with the discrete partition), and _U_ 1 (and hence _U_ 3) has index 1. 

Simple ideal-matched curves have index 1 as real matched curves, by a simple modification of the unreal case [LOT18, Lemma 9.29]. Conversely, we adapt the index computation in the unreal case [LOT18, Lemma 9.30] to show that they are the only ideal matched combs with index 1. With the obvious extension of the notation in that lemma, an upper bound for the dimension of the ideal-matched moduli space is now 

**==> picture [436 x 94] intentionally omitted <==**

LIPSHITZ AND OZSVÁTH 

50 

If ind _[R]_ ( _B_ 1 _, S_ 1; _B_ 2 _, S_ 2) _<_ 1, the sum is negative, so there are no ideal matched combs, and when ind _[R]_ ( _B_ 1 _, S_ 1; _B_ 2 _, S_ 2) = 1 the three other terms must vanish, so ( _U_ 1 _, U_ 2) is a simple ideal-matched curve. 

Finally, we introduce trimmed simple ideal-matched curves [LOT18, Definition 9.31], which again has an evident extension to the real case (with three combs, _w_ 1 _, w_ 2 _, w_ 3 = _τ_ ( _w_ 1) instead of two). The technical lemma relating boundary monotonicity and the algebra in this setting [LOT18, Lemma 9.32] does not use transversality or the expected dimensions, so carries over without change. The spine of a simple ideal-matched curve is a trimmed simple ideal-matched curve: the proof in the unreal case uses the relation between the expected dimensions and the grading in the algebra, in a similar way to ruling out non-composable collisions in the proof of Theorem 4.3. Again, this carries over to the real case because the terms _|⃗ρ|_ and _ι_ ( _⃗ρ_ ) appear the same way in the unreal and real embedded index formulas (because in the real case, each chord appears twice, once on each boundary component of Σ). 

Trimmed curves can again be untrimmed in a combinatorially unique way [LOT18, Lemmas 9.37 and 9.38] (no changes here). As in the unreal case, it is easy to see that there are finitely many trimmed simple ideal-matched curves in a given homology class [LOT18, Lemma 9.39] (again, no changes). Finally, the proof that the counts of the _T_ -matched moduli spaces for _T_ sufficiently large and of the trimmed simple ideal-matched moduli spaces agree is the same as in the unreal case, but where we perform the gluings respecting the involution (as usual). Indeed, the argument is exactly the same as the argument there, focusing on the fiber product of moduli spaces containing ( _w_ 1 _, v_ ) and _w_ 2, with the components ( _w_ 3 = _τ_ ( _w_ 1) _, τ_ ( _v_ )) coming along for the ride. 

With these ingredients in place, the proof of the pairing theorem is formal, and identical to the unreal case [LOT18, Section 9.1]. □ 

## 7. Gradings 

7.1. **Review of the unreal case.** Recall that the bordered algebra _A_ ( _Z_ ) is graded by a noncommutative group. In fact, there are two versions: the _big grading group G[′]_ ( _k_ ) and the _small grading group G_ ( _Z_ ), which are central extensions 

**==> picture [126 x 33] intentionally omitted <==**

Even though _G[′]_ depends only on _k_ , it will be clearer to write it as _G[′]_ ( _Z_ ), thinking of Z[4] _[k][−]_[1] as _H_ 1( _Z \ {z},_ **a** ). We can realize elements of _G[′]_ ( _Z_ ) as certain pairs ( _m_ ; _s_ ) where _s ∈ H_ 1( _Z \ {z},_ **a** ) and _m ∈_[1] 2[Z][[][LOT18][,][Section][3.3].][The][grading][of][an][algebra][element] _[a]_ with support [ _a_ ] is given by 

**==> picture [281 x 14] intentionally omitted <==**

The image of the grading in _H_ 1( _F_ ( _Z_ )) or _H_ 1( _Z \ {z},_ **a** ) is the spin _[c] -component_ of the grading; the element of[1] 2[Z][is][the] _[Maslov][component]_[.] 

The bordered bimodule _CFDA_[�] ( _H_ ), where _∂H_ = _ZL ⨿ZR_ , is graded by a set _S[′]_ ( _H_ ) with a commuting left action by _G[′]_ ( _−ZL_ ) and right action by _G[′]_ ( _ZR_ ), restricting to the same action by Z. Equivalently, _S[′]_ ( _H_ ) has a right action by _G[′]_ ( _−ZL_ )[op] _×_ Z _G[′]_ ( _ZR_ ). The orbits of _S[′]_ ( _H_ ) correspond to spin _[c]_ -structures on _Y_ . Fix a spin _[c]_ -structure on _Y_ represented by a 

REAL BORDERED FLOER HOMOLOGY 

51 

state **x** 0 _∈_ S( _H_ ). Given a domain _B ∈ π_ 2( **x** _,_ **y** ), let 

**==> picture [364 x 14] intentionally omitted <==**

The orbit of _S[′]_ ( _H_ ) corresponding to **x** 0 is given by 

**==> picture [252 x 16] intentionally omitted <==**

a right _G[′]_ ( _−ZL_ )[op] _×_ Z _G[′]_ ( _ZR_ )-set, and the grading of **x** is gr _[′]_ ( **x** ) = _g[′]_ ( _B_ ) for any _B ∈ π_ 2( **x** 0 _,_ **x** ) [LOT15, Section 6.5]. 

To obtain a grading by _G_ ( _Z_ ), we choose _grading refinement data_ , consisting of a basic idempotent _ι_ 0 and for every other basic idempotent _ι_ and element _ψ_ ( _ι_ ) _∈ G[′]_ ( _Z_ ) whose boundary is, in a suitable sense, _ι − ι_ 0 _∈ H_ 0( **a** _/M_ ) [LOT18, Section 3.3.2]. Then, the refined grading of an algebra element _a_ = _ι_ 1 _aι_ 2 is given by 

(7.2) gr( _a_ ) = _ψ_ ( _ι_ 1) gr _[′]_ ( _a_ ) _ψ_ ( _ι_ 2) _[−]_[1] _._ 

With respect to the smaller group, the orbit of the grading set _S_ ( _H_ ) for _CFDA_[�] ( _H_ ) corresponding to the spin _[c]_ structure of **x** 0 is given by 

**==> picture [358 x 15] intentionally omitted <==**

a right _G_ ( _−ZL_ )[op] _×_ Z _G_ ( _ZR_ )-set. Here, we choose the base idempotents _ι_ 0 for _ZL_ and _ZR_ to be the idempotents for the base state **x** 0, and observe that each _g[′]_ ( _P_ ) in fact lies in _G_ ( _Z_ ) _⊂ G[′]_ ( _Z_ ) [LOT15, Lemma 6.29]. The grading of a state **x** with left and right idempotents _ιL_ and _ιR_ is 

(7.4) gr( **x** ) = _ψL_ ( _ιL_ ) gr _[′]_ ( **x** ) _ψR_ ( _ιR_ ) _[−]_[1] _._ 

7.2. **Grading real bordered modules.** Now, let ( _H, τ_ ) be a real bordered Heegaard diagram, with _∂LH_ = _−Z_ , so _CFDR_[�] ( _H, τ_ ) is a left module over _A_ ( _Z_ ). Given a real domain _B ∈ π_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)][,][define] 

**==> picture [358 x 23] intentionally omitted <==**

Fix a real state **x** 0 _∈_ S _R_ ( _H_ ); we define a grading set for the real states that are real spin _[c]_ - equivalent to **x** 0. Specifically, with respect to the big and small grading groups, this grading set is 

**==> picture [349 x 34] intentionally omitted <==**

(7.5) 

which have left actions by _G[′]_ ( _Z_ ) and _G_ ( _Z_ ), respectively. Given a state **x** _∈_ S _R_ ( _H, τ_ ) which is real spin _[c]_ equivalent to **x** 0, with left idempotent _ι_ , choose a real domain _B ∈ π_ 2 _[R]_[(] **[x]**[0] _[,]_ **[ x]**[)] and define 

**==> picture [317 x 32] intentionally omitted <==**

where _ψ_ is some chosen grading refinement data. 

There are several properties to check: 

**Proposition 7.9.** _These definitions have the following properties:_ 

- _(1) For any real domain B ∈ π_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)] _[,][the][tuple][g] R[′]_[(] _[B]_[)] _[lies][in][G][′]_[(] _[Z]_[)] _[.][Thus,][S] R[′]_[(] _[H][,]_ **[ x]**[0][)] _is well-defined and_ gr _[′]_ ( **x** ) _is an element of SR[′]_[(] _[H][,]_ **[ x]**[0][)] _[.]_ 

LIPSHITZ AND OZSVÁTH 

52 

**==> picture [40 x 37] intentionally omitted <==**

**==> picture [55 x 43] intentionally omitted <==**

Figure 23. **A local modification to make** _σ_ **positive.** The diagram near a fixed intersection point before and after the modification are shown. The labels _a_ , _b_ , and _c_ in the left figure indicate the coefficients of a domain before the modification, and the labels in the right figure indicate the corresponding coefficients after the modification. 

- _(2) The elements gR[′]_[(] _[P]_[)] _[in][fact][lie][in][G]_[(] _[Z]_[)] _[ ⊂][G][′]_[(] _[Z]_[)] _[,][so][S][R]_[(] _[H][,]_ **[ x]**[0][)] _[is][well-defined.] (3) If B_ 1 _∈ π_ 2 _[R]_[(] **[w]** _[,]_ **[ x]**[)] _[and][B]_[2] _[∈][π]_ 2 _[R]_[(] **[x]** _[,]_ **[ y]**[)] _[,][and][B]_[1] _[∗][B]_[2] _[∈][π]_[2][(] **[w]** _[,]_ **[ y]**[)] _[is][their][concatenation,] then_ 

**==> picture [150 x 14] intentionally omitted <==**

- _(4) The element_ gr _[′]_ ( **x** ) _is independent of the choice of real domain B._ 

- _(5) The element_ gr( **x** ) _lies in SR_ ( _H,_ **x** 0) _._ 

- _(6) The maps_ gr _[′] and_ gr _define gradings on CFDR_[�] ( _H, τ_ ) _._ 

_Proof._ Recall that _G[′]_ ( _Z_ ) consists of pairs ( _m_ ; _h_ ) where 

**==> picture [206 x 16] intentionally omitted <==**

[LOT18, Definition 3.33]. To verify that _gR[′]_[(] _[B]_[)][lies][in] _[G][′]_[(] _[Z]_[)][,][we][must][check][that][it][satisfies] this congruence. We imitate the proof that _g[′]_ ( _B_ ) has this property [LOT18, Lemma 10.3], and for brevity will assume the reader is following that proof. 

We start with some reductions. First, we may assume that all the points in _**α** ∩_ _**β**_ in the fixed set have _σ_ = 1, as follows. For each fixed point with _σ_ = _−_ 1, let _H[′]_ be the result of performing a small isotopy as in Figure 23, introducing a new pair of bigons and two new non-fixed intersection points, and changing the fixed intersection point to have _σ_ = 1. Any domain in _H_ gives a domain in _H[′]_ with the same corners, as indicated in the figure. The boundary of the domain (and hence _ϵ_ ) is unchanged. If the point under consideration is in both **x** and **y** or in neither **x** nor **y** , then the _σ_ -contribution to the grading is unchanged, and _n_ **x** ( _B_ ) + _n_ **y** ( _B_ ) changes by an even integer. If the point is in one of **x** or **y** , then the _σ_ contribution changes by 1 _/_ 2 and, in the notation from the figure, the new Euler measure and point measures are 

**==> picture [260 x 32] intentionally omitted <==**

So, the change to the grading is an integer plus 1 _/_ 2+( _b_ + _c_ ) _/_ 2. Since this corner is in exactly one of **x** or **y** , _b_ + _c_ is odd, so the overall grading change is an integer. 

REAL BORDERED FLOER HOMOLOGY 

53 

**==> picture [53 x 50] intentionally omitted <==**

Figure 24. **Stabilizing near the fixed set.** A small neighborhood of part of a component of the fixed set is shown, before and after the stabilization. In Guth-Manolescu’s terminology, this is a fixed point stabilization. 

Second, we reduce to the case that an even number of the points in **x** (and **y** ) are fixed by _τ_ . For each component of the fixed set which intersects **x** (and hence **y** ) in an odd number of points, perform a fixed point stabilization as shown in Figure 24 (see also [GM25, Figure 3.5]), with feet adjacent to this component. If the local multiplicity of _B_ at the feet is _a_ , then this decreases the Euler measure by 2 _a_ , increases _n_ **x** + _n_ **y** by 2 _a_ , and does not change any of the other terms in the grading formula. Of course, it also does not change _∂LB_ . So, it suffices to prove the result for the stabilized diagram. Thus, we may assume that **x** and **y** have an even number of points on each component of the fixed set. 

Third, we reduce to the case that none of the points in **x** or **y** is fixed by _τ_ . If **x** contains some points on the fixed set, choose a pair of adjacent points in **x** on a component of the fixed set and perform an isotopy as in Figure 25. In the new diagram, **x** is connected to another state **x** _[′]_ by a rectangle, so that **x** _[′]_ has two fewer points on the fixed set. In particular, the real domain in _B ∈ π_ 2( **x** _,_ **y** ) gives a real domain _B[′] ∈ π_ 2( **x** _[′] ,_ **y** ) with _∂LB_ = _∂LB[′]_ and grading differing by 1. Thus, it suffices to prove the result for _B[′]_ instead of _B_ . Repeat this procedure until the state **x** has no fixed points, and repeat an analogous construction for **y** until **y** has no fixed points. 

So, it suffices to prove the statement when _τ_ : **x** _→_ **x** and _τ_ : **y** _→_ **y** are free. In particular, the _σ_ terms in the definition of _gR[′]_[vanish,][so][we][will][drop][them][from][the][discussion.] 

**==> picture [470 x 51] intentionally omitted <==**

and it suffices to prove the result for _B_[�] instead of _B_ . 

Build the surface _F_ as in the unreal case. The surface _F_ inherits an involution _τF_ which sends _Ri_[(] _[j]_[)] to _τ_ ( _Ri_ )[(] _[m]_[(] _[R][i]_[)] _[−][j]_[)] . That is, _τF_ applies _τ_ from the Heegaard surface and also reverses the indexing of the _Ri_ . It is straightforward to check that _τF_ respects the gluing relations. 

LIPSHITZ AND OZSVÁTH 

54 

**==> picture [61 x 60] intentionally omitted <==**

**==> picture [114 x 134] intentionally omitted <==**

Figure 25. **Third modification near the fixed set.** A small neighborhood of a component of the fixed set is shown, with two fixed components of a state marked. After the isotopy, there is a real rectangle connecting this state to one with two fewer points on the fixed set. 

We have 

**==> picture [184 x 16] intentionally omitted <==**

Here, we view _F/τ_ as a surface-with-corners as follows. Because _τ_ does not fix any points in **x** _∪_ **y** , the fixed set of _τF_ consists entirely of circles. So, the boundary of _F/τ_ is identified with the boundary of _F_ disjoint union some circles; corners are the images of corners in _F_ , with the same local models. 

Define _n±_ as in the unreal case. Because of the symmetry _τ_ , _n_ + and _n−_ are both even; to remember that, write _n±_ = 2 _n[τ] ±_[(so] _[n][τ] ±_[are][counts][of][corners][of] _[F/τ][F]_[).][When][defining][the] _δi_ , consider only the _α_ -boundary of the Heegaard diagram. Then 

**==> picture [240 x 37] intentionally omitted <==**

Also, 

**==> picture [300 x 63] intentionally omitted <==**

(For the second congruence, note that in the real case, for each _α_ -circle there are four points that contribute the same way to _h_ : the two points in **x** and **y** on that _α_ -circle and the points 

REAL BORDERED FLOER HOMOLOGY 

55 

in **x** and **y** on the corresponding _β_ -circle.) Thus, 

**==> picture [428 x 104] intentionally omitted <==**

In the last line, the _h_ sum only counts half-disks with boundary along the _α_ -arcs; the factor of 1 _/_ 2 instead of 1 _/_ 4 is that there are corresponding half-disks with boundary along the _β_ -arcs. 

This last formula is now identical to the formula in the unreal case [LOT18, p. 192]. So, the same case analysis implies that its fractional part agrees with _ϵ_ ( _∂LB_ ), giving Point (1). 

Point (2) is easier. The subgroup _G_ ( _Z_ ) _⊂ G[′]_ ( _Z_ ) consists of pairs ( _m_ ; _h_ ) so that _∂h_ = _−M∗∂_ ( _h_ ), and this condition clearly holds for the boundaries of periodic domains (real or not). 

For Point (3), recall that _g[′]_ ( _B_ ) is additive in the sense that _g[′]_ ( _B_ 1 _∗ B_ 2) = _g[′]_ ( _B_ 1) _g[′]_ ( _B_ 2) [LOT18, Lemma 10.4]. Equivalently, 

**==> picture [456 x 32] intentionally omitted <==**

where _L_ is the linking number [LOT18, Formula 3.32]. Since the linking number satisfies _L_ ( _∂LB_ 1 _, ∂LB_ 2) = _L_ ( _∂RB_ 1 _, ∂RB_ 2), this gives 

**==> picture [449 x 35] intentionally omitted <==**

The _σ_ terms in the definition of _gR[′]_[(] _[B]_[)][are][clearly][additive,][so] _[g] R[′]_[is][also][additive.] Point (4) follows from Point (3), since any other real domain _B[′] ∈ π_ 2 _[R]_[(] **[x]**[0] _[,]_ **[ x]**[)][ can be written] as _B[′]_ = _P ∗ B_ where _P ∈ π_ 2 _[R]_[(] **[x]**[0] _[,]_ **[ x]**[0][)][.] 

Point (5) is straightforward, and is the same as in the unreal case. The projection of _ψ_ ( _ι_ ) _gR[′]_[(] _[B]_[)][has][boundary] _[ι][ −][ι]_[0] _[ −][ι]_[ +] _[ ι]_[0][=][0][(because] _[∂][L][B]_[goes][from] _[ι]_[0][to] _[ι]_[in] _[−][Z][L]_[,][hence] from _ι_ to _ι_ 0 in _ZL_ ). 

Point (6) is again essentially the same as in the unreal case, but using the real index, Formula (3.9), in place of the ordinary index. Suppose a pair ( _B, ⃗ρ_ ) contributes _a_ ( _⃗ρ_ ) _⊗_ **y** to _δ_[1] ( **x** ). Then ind _[R]_ ( _B, ⃗ρ_ ) = 1, so 

**==> picture [246 x 15] intentionally omitted <==**

LIPSHITZ AND OZSVÁTH 

56 

(For the second equality, see [LOT18, Formula (10.21)].) It now follows from Point (3) that gr _[′]_ defines a grading. To see that gr also defines a grading, we have 

**==> picture [352 x 105] intentionally omitted <==**

This concludes the proof. 

7.3. **Comparison with the unreal gradings.** Of course, S _R_ ( _H, τ_ ) _⊂_ S( _H_ ), so the set of real states inherits a grading from the (unreal) grading on S( _H_ ). The Maslov component of this grading is not well-behaved, because the real and unreal indices of holomorphic curves differ (arbitrarily), but the spin _[c]_ components of the grading on S( _H_ ) do behave well. 

Write the boundary of _H_ as ( _−Z_ ) _∪Z[β]_ , and let _Y_ ( _H_ ) be the 3-manifold specified by _H_ . Considering only the spin _[c]_ -components of the gradings, _CFDR_[�] ( _H, τ_ ) is graded by 

**==> picture [137 x 13] intentionally omitted <==**

_∂_ where _∂L_ is the composition _H_ 2( _Y, ∂Y_ ) _[−][τ][∗] → H_ 1( _∂Y_ ) = _H_ 1( _F_ ( _Z_ )) _⨿H_ 1( _F_ ( _Z_ )) _→ H_ 1( _F_ ( _Z_ )) where the second map is projection to the first _H_ 1( _F_ ( _Z_ )) summand. On the other hand, � _CFDD_ ( _H_ ) is graded by 

**==> picture [196 x 16] intentionally omitted <==**

We reformulate the grading on _CFDR_[�] ( _H, τ_ ) to be closer to the grading on _CFDD_[�] ( _H_ ). Inside _H_ 1( _F_ ( _Z_ )) _⊕ H_ 1( _F_ ( _Z_ )) is an anti-diagonal _∇_ = _{_ ( _x, −x_ ) _| x ∈ H_ 1( _F_ ( _Z_ )) _}_ , and 

_H_ 1( _F_ ( _Z_ )) _/∂LH_ 2( _Y, ∂Y_ ) _[−][τ][∗] −→∇∼_ = _/∂H_ 2( _Y, ∂Y_ ) _[−][τ][∗] ._ 

Observe that _∂H_ 2( _Y, ∂Y_ ) _[−][τ][∗] ⊂_ [ _∂H_ 2( _Y, ∂Y_ )] _∩∇_ , so we obtain a map 

**==> picture [424 x 16] intentionally omitted <==**

of grading sets. 

To define a grading on S _R_ ( _H, τ_ ), we choose base states for each real spin _[c]_ -equivalence class. Fixing a real spin _[c]_ -equivalence class and a base state **x** 0 for it, if **x** _∈_ S _R_ ( _H, τ_ ) is another state in the equivalence class, and we also use **x** 0 to define the grading for S( _H_ ), then Formula (7.11) respects the gradings. 

Now, suppose **x** 0 and **y** are spin _[c]_ -equivalent, but not real spin _[c]_ -equivalent. Then using the ordinary grading (and continuing to take only the spin _[c]_ -components), gr( **y** ) _∈_ � _H_ 1( _F_ ( _Z_ )) _⊕ H_ 1( _F_ ( _Z_ ))� _/∂H_ 2( _Y, ∂Y_ ). If ∆= _{_ ( _x, x_ ) _| x ∈ H_ 1( _F_ ( _Z_ )) _}_ is the diagonal, then 

**==> picture [222 x 13] intentionally omitted <==**

By construction, this is exactly _∂ζ_ ( **x** _,_ **y** ). In particular, the spin _[c]_ -components of the ordinary (unreal) grading determines the image of the difference cycle _ζ_ . 

Finally, a few words about how this grading relates to Guth-Manolescu’s in the closed case. Each real spin _[c]_ -equivalence class of states corresponds to a real spin _[c]_ -structure [GM25, 

REAL BORDERED FLOER HOMOLOGY 

57 

Section 3.7] s. The grading we have defined in a given spin _[c]_ -equivalence class is by the Z-set 

**==> picture [208 x 22] intentionally omitted <==**

This is half the divisibility of _c_ 1(s) (where we view s as an ordinary spin _[c]_ -structure). Equivalently, this is a relative grading by Z _/n_ Z where _n_ is half the divisibility of _c_ 1(s), exactly as Guth-Manolescu describe [GM25, Section 4.6]. Tracing through the definitions, our relative grading of states agrees with theirs. 

7.4. **A graded pairing theorem.** As in Theorem 6.1, let ( _H, τ_ ) be a real nice bordered Heegaard diagram with boundary ( _−Z_ ) _⨿Z[β]_ , and _H[′]_ a nice arced bordered Heegaard diagram with boundary ( _−Z[′]_ ) _⨿Z_ . Let ( _Y, τ_ ) and _Y[′]_ be the 3-manifolds represented by ( _H, τ_ ) and _H[′]_ , so _∂Y_ = _−F_ ( _Z_ ) _⨿−F_ ( _Z_ ) and _∂Y[′]_ = _−F_ ( _Z[′]_ ) _⨿ F_ ( _Z_ ). Fix a spin _[c]_ -equivalence class of states for _H[′] ∪H ∪_ ( _−H[′]_ ) _[β]_ , a base state **x** _[′]_ 0 _[∪]_ **[x]**[0] _[∪]_ **[x]** _[′]_ 0[representing][it,][and][grading][refinement] data _ψZ ′_ for _A_ ( _Z[′]_ ) and _ψZ_ for _A_ ( _Z_ ). To keep notation shorter, we will write **x** _[′]_ 0 _[∪]_ **[x]**[0] _[∪]_ **[x]** _[′]_ 0 as **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0[,][and] _[H][′][ ∪H ∪]_[(] _[−H][′]_[)] _[β]_[as] _[H][′][HH][′]_[.][These][data][determine:] 

- Gradings on _A_ ( _Z_ ) and _A_ ( _Z[′]_ ) by _G_ ( _Z_ ) and _G_ ( _Z[′]_ ), via Formulas (7.1) and (7.2). 

- Grading sets for the summands of _CFDR_[�] ( _H, τ_ ) and _CFDA_[�] ( _Z[′]_ ) corresponding to the spin _[c]_ -equivalence class of **x** 0 and **x** _[′]_ 0[,][as][in][Formulas][(][7.6][)][and][(][7.3][).] 

- A grading set for the summand of _CFDR_[�] ( _H[′] HH[′] ,_ � _τ_ ) in the spin _[c]_ -equivalence class of **x** _[′]_[using][the][base][state] **[x]** _[′]_[again][as][in][Formula][(][7.6][).] 0 **[x]**[0] **[x]** _[′]_ 0[,] 0 **[x]**[0] **[x]** _[′]_ 0[,] 

- Gradings of these summands of _CFDR_[�] ( _H, τ_ ), _CFDA_[�] ( _Z[′]_ ), and _CFDR_[�] ( _H[′] HH[′] ,_ � _τ_ ) by these sets, as in Formulas (7.8) and (7.4). 

The last point is a little subtle. To compute the grading of a state **x** _∈_ S _R_ ( _H, τ_ ), say, we choose a domain _B ∈ π_ 2 _[R]_[(] **[x]**[0] _[,]_ **[ x]**[)][,][but][(by][Proposition][7.9][part][(4)][)][the][grading][of] **[x]**[is] independent of that choice. 

As in the pairing theorem for bimodules [LOT15, Section 7.1.1], given states **x** _,_ **y** _∈_ S _R_ ( _H_ ) and **x** _[′] ,_ **y** _[′] ∈_ S( _H[′]_ ) so that _ϵ_ ( **x** _,_ **y** ) = _ϵ_ ( **x** _[′] ,_ **y** _[′]_ ) = 0 and _ζ_ ( **x** _,_ **y** ) = 0, we can compute _ϵ_ ( **x** _[′]_ **xx** _[′] ,_ **y** _[′]_ **yy** _[′]_ ) from the grading data, as follows. It suffices to compute _ϵ_ ( **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0 _[,]_ **[ x]** _[′]_ **[xx]** _[′]_[)][.] The spin _[c]_ -components of the gradings of **x** _[′]_ and **x** are elements of _H_ 1( _F_ ( _Z_ )); denote them [gr( **x** _[′]_ )] and [gr( **x** )]. It follows from the definitions that _ϵ_ ( **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0 _[,]_ **[ x]** _[′]_ **[xx]** _[′]_[)][is][the][image][of] [gr( **x** _[′]_ )] + [gr( **x** )] under the composition 

**==> picture [470 x 38] intentionally omitted <==**

where the first map is induced by inclusion of the left boundary of _Y_ . 

We digress briefly to discuss how to extract _ζ_ from the grading data. So, suppose that _ϵ_ ( **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0 _[,]_ **[ x]** _[′]_ **[xx]** _[′]_[)][=][0][;][for][convenience,][assume][also][that] **[x]**[0][and] **[x]**[occupy][the][same] _[α]_[-arcs.] Then, for _B ∈ π_ 2 _[R]_[(] **[x]**[0] _[,]_ **[ x]**[)][ and] _[ B][′][∈][π]_[2][(] **[x]** _[′]_ 0 _[,]_ **[ x]** _[′]_[)][,][ (] _[∂][R][B][′]_[ +] _[∂][L][B, ∂][L][B]_[ +] _[∂][R][B][′]_[)] _[ ∈][H]_[1][(] _[F]_[(] _[Z]_[)] _[⨿][F]_[(] _[Z]_[))] is in the kernel of the map 

**==> picture [346 x 13] intentionally omitted <==**

where _K_ is the image of the boundary map 

**==> picture [466 x 32] intentionally omitted <==**

LIPSHITZ AND OZSVÁTH 

58 

(as we can change _B[′]_ , _B_ , and _τ_ ( _B[′]_ ) by periodic domains to get a domain in _π_ 2( **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0 _[,]_ **[ x]** _[′]_ **[xx]** _[′]_[)][).] Choose a preimage ( _C, D, E_ ) _∈ H_ 2( _Y[′] , ∂Y[′]_ ) _⊕H_ 2( _Y, ∂Y_ ) _⊕H_ 2( _Y[′] , ∂Y[′]_ ) of ( _∂RB[′]_ + _∂LB, ∂LB_ + _∂RB[′]_ ). Then _ζ_ ( **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0 _[,]_ **[ x]** _[′]_ **[xx]** _[′]_[)][is][represented][by] 

( _C_ + _τ∗_ ( _E_ ) _, D_ + _τ∗_ ( _D_ ) _, E_ + _τ∗_ ( _C_ )) _∈ H_ 2( _Y[′] Y Y[′] , ∂Y[′] Y Y[′]_ ) _[τ][∗] /_ Im(1 + _τ∗_ ) _._ 

It is straightforward to see that this element depends only on the grading data in the tensor product grading set. 

Returning from the digression, if _ζ_ ( **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0 _[,]_ **[ x]** _[′]_ **[xx]** _[′]_[) = 0][,][then][we][can][choose][a][real][domain] connecting **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0[and] **[x]** _[′]_ **[xx]** _[′]_[.][Intersecting][this][domain][with] _[H][′]_[and] _[H]_[gives][domains][that] can be used to define the gradings of **x** _[′]_ and **x** , and hence the grading of **x** _[′] ⊗_ **x** in the tensor product grading set. The result is clearly in the same orbit as the grading of **x** _[′]_ 0 _[⊗]_ **[x]**[0][.][On the] other hand, if (gr( **x** _[′]_ 0[)] _[,]_[ gr(] **[x]**[0][))][and][(gr(] **[x]** _[′]_[)] _[,]_[ gr(] **[x]**[))][are][in][the][same][orbit][of][the][tensor][product] grading set, then we can choose _∂RB[′]_ = _∂LB_ , so **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0[and] **[x]** _[′]_ **[xx]** _[′]_[are][also][connected][by][a] real domain. In conclusion, **x** _[′]_ 0 _[⊗]_ **[x]**[0][and] **[x]** _[′][ ⊗]_ **[x]**[are][in][the][same][orbit][of][the][tensor][product][grading][set] if and only if **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0[and] **[x]** _[′]_ **[xx]** _[′]_[are][in][the][same][orbit][of][the][grading][set][on] _[H][′][ ∪H ∪]_[(] _[−H][′]_[)] _[β]_[.] Now, consider only the orbit corresponding to **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0[.][The grading set on] _[ H][′][∪H∪]_[(] _[−H][′][β]_[)] is 

**==> picture [218 x 23] intentionally omitted <==**

while the grading set on the tensor product is the _G_ ( _Z[′]_ )-orbit of the identity in 

**==> picture [372 x 15] intentionally omitted <==**

Define a map of grading sets sending _h_ to ( _h,_ 1). Then _h · gR[′]_[(] _[P]_[ �][)][maps][to][(] _[h][ ·][ g] R[′]_[(] _[P]_[ �][)] _[,]_[ 1)][,][but] writing _P_[�] = _P[′] PP[′]_ with _P[′] ∈ π_ 2( **x** _[′]_ 0 _[,]_ **[ x]** _[′]_ 0[)][and] _[P][∈][π]_ 2 _[R]_[(] **[x]**[0] _[,]_ **[ x]**[0][)][,][we][have] 

**==> picture [254 x 16] intentionally omitted <==**

where the first equality uses Lemma 7.12 below. In particular, we have a well-defined map of grading sets. 

**Lemma 7.12.** _With notation as above,_ ( _gR[′]_[(] _[P]_[ �][)] _[,]_[ 1) =] _[ g][′]_[(] _[P][ ′]_[)] _[ ·]_[ (1] _[, g] R[′]_[(] _[P]_[))] _[.] Proof._ We have 

**==> picture [442 x 121] intentionally omitted <==**

while 

where the second equality uses the fact that if the spin _[c]_ -components agree, then the Maslov components simply add, and _∂RP[′]_ = _−∂LP_ . □ 

**Theorem 7.13.** _With respect to this isomorphism of grading sets, the homotopy equivalence in Theorem 6.1 respects the gradings._ 

REAL BORDERED FLOER HOMOLOGY 

59 

_Proof._ The proof is essentially the same as the proof of Lemma 7.12. We have already explained in what sense the isomorphism respects the decomposition of the grading group into _G_ ( _Z[′]_ )-orbits. So, consider the orbit containing gr( **x** _[′]_ 0 **[x]**[0] **[x]** _[′]_ 0[)][for][the][glued][diagram,][and] the corresponding orbit containing **x** _[′]_ 0 _[⊗]_ **[x]**[0][for][the][tensor][product.] Given another state **x** _[′]_ **xx** _[′]_ and corresponding state **x** _[′] ⊗_ **x** in this orbit, there are domains _B ∈ π_ 2 _[R]_[(] **[x]**[0] _[,]_ **[ x]**[)][and] _B[′] ∈ π_ 2( **x** _[′]_ 0 _[,]_ **[ x]** _[′]_[)][so][that] _[∂][L][B]_[=] _[ −][∂][R][B][′]_[.][Then] 

**==> picture [394 x 14] intentionally omitted <==**

We have 

**==> picture [390 x 93] intentionally omitted <==**

So, 

**==> picture [372 x 66] intentionally omitted <==**

as desired. 

**==> picture [11 x 9] intentionally omitted <==**

## 8. Computing _HFR_[�] by factoring mapping classes 

We now have all the tools to compute _HFR_[�] ( _Y, τ_ ) as long as _τ_ has connected fixed set. Nagase showed that _Y_ admits a real Heegaard splitting _Y_ = _H ∪_ Σ _H[′]_ , where _τ_ (Σ) = Σ and _τ_ ( _H_ ) = _H[′]_ [Nag79] (see also [GM25, Section 3.1]). Fix a real pointed matched circle _Z_ and a diffeomorphism _ϕ_ : _F_ ( _Z_ ) _→_ Σ intertwining the involutions. (If Σ _/τ_ is nonorientable, we can take _Z_ to be the antipodal pointed matched circle; if Σ _/τ_ is orientable, and hence the genus of Σ is even, we can take _Z_ to be the split pointed matched circle.) From the description of _Y_ (AZ( _Z_ )) (Section 5.2), the diffeomorphism _ϕ_ extends to an identification of _Y_ (AZ( _Z_ )) and a neighborhood of Σ. 

Choose _g_ circles _a_ 1 _, . . . , ag ⊂ F_ ( _Z_ ) so that the handlebody _H_ is determined by compressing _ϕ_ ( _a_ 1) _, . . . , ϕ_ ( _ag_ ). So, _H[′]_ is determined by compressing _τ_ ( _ϕ_ ( _ai_ )) = _ϕ_ ( _τ_ ( _ai_ )), _i_ = 1 _, . . . , g_ . Let _Z[′]_ be the split pointed matched circle with the same genus as _Z_ . Choose a diffeomorphism _ψ_ : _F_ ( _Z_ ) _→ F_ ( _Z[′]_ ) so that _ψ_ ( _a_ 1) _, . . . , ψ_ ( _ag_ ) are the _g_ standard circles on _F_ ( _Z[′]_ ) specifying the 0-framed handlebody _H_ 0 = ( _H_ 0 _, ϕ_ 0 : _F_ ( _Z[′]_ ) _→ ∂H_ 0) of genus _g_ (see Figure 26). 

So, 

**==> picture [373 x 14] intentionally omitted <==**

where _Yψ_ is the mapping cylinder of _ψ_ , and the involution _τ_ is the standard involution on AZ( _Z_ ) and exchanges the two copies of _Yψ_ (respectively _H_ 0). 

LIPSHITZ AND OZSVÁTH 

60 

**==> picture [66 x 59] intentionally omitted <==**

**==> picture [36 x 114] intentionally omitted <==**

**==> picture [42 x 47] intentionally omitted <==**

Figure 26. **The 0-framed handlebody** . Left: the split pointed matched circle _Z[′]_ of genus 2. Center: the associated surface _F_ ( _Z_ ), and two standard circles on it. Right: a bordered Heegaard diagram representing the 0-framed handlebody, in which these two circles bound disks. 

By construction, AZ( _Z_ ) is a real nice bordered Heegaard diagram. Thus, by Corollary 6.6 and the usual pairing theorem for bordered Heegaard Floer homology [LOT15, Theorem 2], 

**==> picture [314 x 39] intentionally omitted <==**

In a previous paper, we gave an algorithm for computing _CFDA_[�] ( _Yψ_ ), by factoring _ψ_ into arcslides, as well as an explicit description of _CFD_[�] ( _−H_ 0) (the latter is easy). Thus, we obtain an algorithm for computing the dimension of _HFR_[�] ( _Y, τ_ ). 

We described in Section 7.4 how to compute the obstruction class _ϵ_ from the grading data for _CFA_[�] ( _H_ 0 _∪ Yψ_ ) and _CFDR_[�] (AZ( _Z_ )), as well as the obstruction class _ζ_ when _ϵ_ vanishes. Together, _ϵ_ and _ζ_ give an affine version of the decomposition of _HFR_[�] ( _Y, τ_ ) into real spin _[c]_ - structures. Finally, in each spin _[c]_ -structure, Theorem 7.13 gives the relative Maslov grading. 

8.1. **Computer implementation.** We have implemented Corollary 5.16’s small model for � _CFDR_ (AZ( _Z_ )), for _Z_ a real pointed matched circle representing a surface with orientable quotient, in Bohua Zhan’s `bfh_python` package [Zha]. This allows one to compute, for instance, _HFR_[�] of branched double covers of knots in _S_[3] . At the time of writing, we have not implemented the gradings, so the code only computes the total dimension of _HFR_[�] . 

As an example interaction, to compute the real Floer homology of the branched double cover of a trefoil, one could run: 

```
fromrealimportrealAZ,selfGluingHB
frompmcimportsplitPMC
```

```
fromarcslideimportArcslide
```

REAL BORDERED FLOER HOMOLOGY 

61 

```
fromarcslideDAimportArcslideDA
hb=selfGluingHB(splitPMC(1))
twists=[ArcslideDA(Arcslide(hb.algebra.pmc,1,0)),
ArcslideDA(Arcslide(hb.algebra.pmc,2,1))]
fortwistintwists:
```

```
hb=twist.tensorD(hb)
hb.simplify()
cx=realAZ(splitPMC(1)).morToD(hb)
cx.simplify()
print("DimensionofHFRis:",len(cx))
```

This prints that the dimension is 3. Indeed, this is a special case of [GM25, Example 6.4], which in turn is a special case of [Hen25, Corollary 1.3] (which was conjectured in [GM25, Remark 6.6]). 

Of course, to use the program, one needs a description of the bordered handlebodies being attached on the two sides. For fibered knots, like the trefoil, these have a particularly convenient description. Let _K_ be a fibered knot with fiber _F_ and monodromy _ϕ_ . Then the branched double cover of _K_ is given by 

H _sg ∪F ∪_ ( _−F_ ) _Yϕ∪_ I _∪F ∪_ ( _−F_ ) [0 _,_ 1] _×_ ( _F ∪_ ( _−F_ )) _∪F ∪_ ( _−F_ ) _Yϕ∪_ I _∪F ∪_ ( _−F_ ) H _sg,_ 

where H _sg_ is the _self-gluing handlebody_ [LOT14b, Section 9.5], that is, [0 _,_ 1] _× F_ . For this to be a decomposition into bordered 3-manifolds, we need parametrizations of the boundaries where the pieces are glued. If we parameterize _F_ by the _linear pointed matched circle_ [LOT14a, Section 5.1], then the Dehn twists coming from branched double covers of braid generators have simple descriptions in terms of arcslides, and in fact `bfh_python` already knows this description. So, implementing _CFD_[�] (H _sg_ ) (which was computed in our earlier paper [LOT14b, Theorem 9.3]) makes it easy to compute _HFR_[�] (Σ( _K_ )) from the monodromy for _K_ . 

From Hendricks’s result [Hen25, Corollary 1.3], if Σ( _K_ ) is an _L_ -space, then we have � _HFR_ (Σ( _K_ ) _, τ_ ) _[∼]_ = _HF_[�] (Σ( _K_ )) _[∼]_ = F[det(] 2 _[K]_[)] . KnotInfo [LMar] lists monodromies for knots through 12 crossings. Of these, there are three fibered, genus 2 knots _K_ for which Σ( _K_ ) is not an _L_ -space, and for these we computed _HFR_[�] (Σ( _K_ ) _, τ_ ): 

|nd for th|ese we co|mputed <br>_HFR_(Σ(|_K_)_, τ_):|
|---|---|---|---|
|_K_|det(_K_)|dim �<br>_HF_(Σ(_K_))|dim �<br>_HFR_(Σ(_K_)_, τ_)|
|10145|3|5|5|
|12_n_121|1|3|3|
|12_n_642|27|29|29|



These computations took a few minutes each on a modern laptop (MacBook Air M1, 16GB RAM). The most time-consuming step is computing and simplifying the morphism complex between type _D_ structures at the end. Indeed, for 12 _n_ 642, the computer produces a complex with 569,433 generators at this stage. 

If we had defined a type _A_ real invariant, tensoring with it instead of taking the morphism complex at this stage would result in a much smaller complex, and hence faster computations. In fact, for the case of AZ( _Z_ ) from Corollary 5.16, this takes little extra work: 

**Proposition 8.2.** _Let Z_ = _Z[′]_ #( _−Z[′]_ ) _be a real pointed matched circle so that F_ ( _Z_ ) _/τ is orientable, as in Corollary 5.16. Define a differential right module CFAR_[�] (AZ( _Z_ ) _, τ_ ) _over the_ 

LIPSHITZ AND OZSVÁTH 

62 

_multiplicity_ 1 _algebra A[′]_ ( _−Z_ ) _as follows. As a chain complex, CFAR_[�] (AZ( _Z_ ) _, τ_ ) _is A[′]_ ( _−Z[′]_ ) _. Define a right action of A[′]_ ( _−Z_ ) _on A[′]_ ( _−Z[′]_ ) _by_ 

**==> picture [339 x 37] intentionally omitted <==**

_Here, r_ : _A[′]_ ( _Z[′]_ ) _→A[′]_ ( _−Z[′]_ ) _denotes vertical mirroring (which is an anti-homomorphism). Then for any bordered_ 3 _-manifold Y with boundary F_ ( _Z_ ) _⨿ F_ ( _Z_ ) _, we have the following pairing theorem:_ 

**==> picture [308 x 17] intentionally omitted <==**

_Proof._ First, we show that _CFAR_[�] (AZ( _Z_ ) _, τ_ ) ⊠ _CFDD_[�] (I _Z_ ) _[∼]_ = _CFDR_[�] (AZ( _Z_ )). Recall that � _CFDD_ (I _Z_ ) is a (left-left) type _DD_ bimodule over _A[′]_ ( _Z_ ) and _A[′]_ ( _−Z_ ), with one generator for each pair of complementary idempotents, and 

**==> picture [250 x 28] intentionally omitted <==**

[LOT14b, Theorem 1]. Here, ~~_r_~~ : _A[′]_ ( _Z_ ) _→A[′]_ ( _−Z_ ) is vertical reflection. 

Write a generator _i ⊗ i[′]_ simply as _i_ . Tensoring this with _CFAR_[�] (AZ( _Z_ ) _, τ_ ) over _A[′]_ ( _−Z_ ), there is one generator _a ⊗ i_ for each generator _a ∈A_ ( _Z[′]_ ), where _i_ is the right idempotent of _a_ , and the differential is 

**==> picture [460 x 63] intentionally omitted <==**

This agrees with the differential from Corollary 5.16. Now, from the pairing theorem, Corollary 6.6, 

**==> picture [306 x 16] intentionally omitted <==**

But we have 

**==> picture [430 x 59] intentionally omitted <==**

as desired. 

Tensoring with this module instead of taking the morphisms to _CFDR_[�] (AZ( _Z_ )), for 12 _n_ 642 the final chain complex has 521 generators (a thousand-fold savings). 

## 9. Other Applications 

9.1. **The first differential in Hendricks’s spectral sequence.** Real Heegaard Floer homology is a version of Z _/_ 2-equivariant Floer theory, and so it is natural to expect that it would relate to nonequivariant Floer homology via a localization theorem. Hendricks showed that this expectation is correct, constructing a spectral sequence 

**==> picture [372 x 28] intentionally omitted <==**

REAL BORDERED FLOER HOMOLOGY 

63 

[Hen25, Theorem 1.2]. She proves that if _Y_ admits a symmetric almost complex structure achieving transversality for the nonequivariant moduli spaces, then the _d_ 1-differential is given by (1 + _ι∗τ∗_ ) _θ_ . Thus: 

**Theorem 9.2.** _Suppose that_ ( _Y, τ_ ) _is a real 3-manifold so that the fixed set of τ is a single circle. Then the d_ 1 _-differential in Hendricks’s spectral sequence_ (9.1) _is_ (1 + _ι∗τ∗_ ) _θ._ 

_Proof._ Decompose _Y_ as in Formula (8.1) and choose nice diagrams for _H_ 0 and _Yψ_ . Gluing these to AZ( _Z_ ) gives a real nice diagram for ( _Y, τ_ ). Since the diagram is, in particular, nice the moduli spaces of holomorphic curves of Maslov index _≤_ 1 are transversely cut out for any choice of almost complex structure on the Heegaard diagram—in particular, for symmetric ones. (There are no positive domains of Maslov index _≤_ 0, and the only ones of Maslov index 1 are empty bigons and rectangles.) This is enough to guarantee that we may compute the Heegaard Floer homology using such an almost complex structure, and hence for Hendricks’s argument [Hen25, Lemma 2.8] to go through. □ 

_Remark_ 9.3 _._ Binns-Guth-Xiao [BGX] have constructed nice diagrams for arbitrary real Heegaard diagrams, giving a proof of Theorem 9.2 without the hypothesis on the fixed set. While our construction of real nice diagrams is independent of theirs, we were aware that they had such a construction before beginning this project. 

## 9.2. **A surgery exact triangle.** 

**Theorem 9.4.** _Let_ ( _Y, τ_ ) _be a real 3-manifold, and_ Σ _a connected, separating surface in Y so that τ_ (Σ) = Σ _. Let K be a framed knot in Y \_ Σ _and K[′]_ = _τ_ ( _K_ ) _. Let_ ( _Y_ 00 _, τ_ 00) _(respectively_ ( _Y_ 11 _, τ_ 11) _) be the result of performing_ 0 _-surgery (respectively_ 1 _-surgery) on both K and K[′] and τ_ 00 _(respectively τ_ 11 _) the involution induced by τ . Then there is an exact triangle_ 

**==> picture [272 x 63] intentionally omitted <==**

_Proof._ Let _T_ 0, _T_ 1, and _T∞_ be the 0-framed, 1-framed, and _∞_ -framed solid tori. There is a short exact sequence 

**==> picture [348 x 16] intentionally omitted <==**

as follows. In our first paper on bordered Floer homology, we constructed a short exact sequence 

0 _→ CFD_[�] ( _T∞_ ) _→ CFD_[�] ( _T−_ 1) _→ CFD_[�] ( _T_ 0) _→_ 0 _._ 

Tensor this with the type _AA_ bimodule of the identity, to obtain the desired sequence. (Recall that tensoring the type _D_ invariant of the 0-framed solid torus with _CFAA_[�] (I) gives the type _A_ invariant of the _∞_ -framed solid torus, as tensoring _CFAA_[�] (I) with the type _D_ invariant of the 0-framed solid torus on both sides gives _S_[3] .) 

Now, decompose 

**==> picture [186 x 13] intentionally omitted <==**

so that _τ_ is the evident involution. Choosing diagrams for _Y[′]_ , [0 _,_ 1] _×_ Σ, and _Ti_ ( _i ∈{_ 0 _,_ 1 _, ∞}_ ), Theorem 6.5 gives 

**==> picture [308 x 17] intentionally omitted <==**

LIPSHITZ AND OZSVÁTH 

64 

□ 

Combining this with the exact sequence (9.5) gives the result. 

9.3. **Branched double covers of certain satellites.** Real bordered Floer homology gives satellite formulas for the real Floer homology of branched double covers, for even winding number patterns. Indeed, if _P ⊂ S_[1] _× D_[2] is a pattern with even winding number, then the branched double cover Σ( _S_[1] _× D_[2] _, P_ ) has boundary _T_[2] _⨿ T_[2] . Given a knot _K ⊂ S_[3] , if _Y_ = _S_[3] _\_ nbd( _K_ ) denotes the exterior of _K_ and _P_ ( _K_ ) denotes the satellite of _K_ with pattern _P_ , then 

**==> picture [206 x 14] intentionally omitted <==**

In particular, by the pairing theorems, 

**==> picture [340 x 39] intentionally omitted <==**

On the other hand, _CFD_[�] ( _Y_ ) is determined by _CFK[−]_ ( _K_ ) [LOT18, Theorem A.11], and � _CFA_ ( _Y_ ) is determined by _CFD_[�] ( _Y_ ), either by tensoring with _CFAA_[�] (I _T_ 2) or Hedden-Levine’s explicit formula [HL16, Theorem 2.2]. Thus, the pairing theorem implies: **Proposition 9.6.** _Let P ⊂ S_[1] _× D_[2] _be a pattern with even winding number, and let K, K[′] ⊂ S_[3] _be knots. If CFK[−]_ ( _K_ ) _≃ CFK[−]_ ( _K[′]_ ) _, then HF_[�] (Σ( _P_ ( _K_ ))) _[∼]_ = _HF_[�] (Σ( _P_ ( _K[′]_ ))) _and HFR_[�] (Σ( _P_ ( _K_ )) _, τ_ ) _[∼]_ = _HFR_[�] (Σ( _P_ ( _K[′]_ )) _, τ_ ) _._ 

As a first example, we consider the case of Whitehead doubling. Figure 27 is a real Heegaard diagram for the Whitehead doubling pattern _P ⊂ S_[1] _× D_[2] ; we will discuss its framing presently. The diagram has 9 regions. The involution preserves _D_ 1, _D_ 2 (the region with the basepoint), _D_ 3, _D_ 4, and _D_ 5, and exchanges _D_ 6 with _D_ 9 and _D_ 7 with _D_ 8. There are 7 real states: _ab_ , _pixj_ , with _i, j ∈{_ 1 _,_ 2 _}_ , and _piy_ , with _i ∈{_ 1 _,_ 2 _}_ . (The Heegaard state **x** = _st_ is _τ_ -invariant, but both _α_ -arcs contain a point in **x** , so _st_ is not a real state.) These are all real spin _[c]_ -equivalent, as we shall see. 

The space of (unreal) periodic domains is generated by 

**==> picture [402 x 11] intentionally omitted <==**

The space of real periodic domains is generated by 

**==> picture [318 x 11] intentionally omitted <==**

The differential is as follows, where we list first the domain and then its contribution: 

**==> picture [361 x 46] intentionally omitted <==**

Cancelling the differential coming from _D_ 4, we find that the type _D_ structure has 5 generators and the following arrows: 

**==> picture [201 x 74] intentionally omitted <==**

65 

## REAL BORDERED FLOER HOMOLOGY 

**==> picture [396 x 219] intentionally omitted <==**

Figure 27. **Branched double cover of the Whitehead doubling pattern.** The thin curve is the fixed set. The boundary is drawn as two intersection points, one between the two _α_ -arcs and the other between the two _β_ -arcs. The numbers 1 _,_ 2 _,_ 3 indicate the chords _ρ_ 1 _, ρ_ 2 _, ρ_ 3 around the boundary components. 

(We have also indicated the idempotents.) 

Implicitly, in drawing Figure 27, we have chosen framings for the boundary components. It is more convenient to frame the boundary as follows: identifying Σ( _P_ ) with the left-handed (2 _,_ 4) torus link, choose the 0-framing of both boundary components. With this choice, gluing in a 0-framed knot complement to each boundary component then gives the branched double cover of the untwisted Whitehead double of the knot. For this framing, if we fill both boundary components at slope _p/q_ , then a presentation matrix for the first homology of the result is � _−p_ 2 _q −p_ 2 _q_ �, so the order of the first homology of this filling is _|p_[2] _−_ 4 _q_[2] _|_ . By contrast, for the diagram in Figure 27, if we identify _H_ 1( _F_ ( _Z_ )) = _H_ 1( _T_[2] ) = Z[2] by sending [ _ρ_ 23] to [1 _,_ 0] _[T]_ and [ _ρ_ 12] to [0 _,_ 1] _[T]_ , then 

**==> picture [364 x 30] intentionally omitted <==**

If we glue a bordered Heegaard diagram for the Dehn twist _τµ_ twice to both sides of the diagram, we obtain a diagram with new periodic domains _P_ 1 _[′][,][ P]_ 2 _[′]_[with][boundaries] 

**==> picture [364 x 30] intentionally omitted <==**

In particular, if we fill both boundary components of this new diagram with _p/q_ -framed solid tori, a presentation matrix for the first homology of the result is 

**==> picture [94 x 58] intentionally omitted <==**

LIPSHITZ AND OZSVÁTH 

66 

**==> picture [439 x 353] intentionally omitted <==**

**----- Start of picture text -----**<br>
• • •<br>• • • • •<br>• • •<br>ρ 2 ρ 2 ρ 3<br>• ◦ • ◦ •<br>ρ 23<br>ρ 1 ρ 1 ρ 1<br>◦ ◦ ◦ ◦ ρ 12<br>ρ 23<br>ρ 123 ρ 123<br>ρ 2 ρ 3 ρ 23 ρ 2 ρ 3<br>• ◦ • ◦ ◦ • ◦ • •<br>ρ 23<br>ρ 1 ρ 1<br>ρ 23<br>◦ ◦ ◦ ◦<br>ρ 123 ρ 123 ρ 123<br>ρ 2 ρ 3 ρ 23<br>• ◦ • ◦ •<br>ρ 3<br>ρ 2 ρ 2 ρ 1<br>• ◦ • ◦ •<br>ρ 2 ,ρ 1<br>ρ 3 ρ 3 ρ 3<br>◦ ◦ ◦ ◦ ρ 3 ,ρ 2<br>ρ 2 ,ρ 1<br>ρ 3 ,ρ 2 ,ρ 1 ρ 3 ,ρ 2 ,ρ 1<br>ρ 2 ρ 1 ρ 2 ,ρ 1 ρ 2 ρ 1<br>• ◦ • ◦ ◦ • ◦ • •<br>ρ 2 ,ρ 1<br>ρ 3 ρ 3<br>ρ 2 ,ρ 1<br>◦ ◦ ◦ ◦<br>ρ 3 ,ρ 2 ,ρ 1 ρ 3 ,ρ 2 ,ρ 1 ρ 3 ,ρ 2 ,ρ 1<br>ρ 2 ρ 1 ρ 2 ,ρ 1<br>• ◦ • ◦ •<br>ρ 1<br>**----- End of picture text -----**<br>


Figure 28. **Staircases.** Top row: staircases with _τ_ = _−_ 2, _τ_ = 2, and _τ_ = 0. Middle row: the corresponding type _D_ structures. Bottom row: the corresponding type _A_ modules. For the type _A_ structures, we have not shown a full set of operations, but just operations that generate the type _A_ structure, under an evident composition operation. Solid dots have idempotent _ι_ 0, and empty dots have idempotent _ι_ 1. 

so the order of the first homology is again _|p_[2] _−_ 4 _q_[2] _|_ . Thus, we have found the desired framing. 

So, to obtain _CFDR_[�] (Σ( _P_ ) _, τ_ ) for the untwisted Whitehead doubling pattern _P_ , we should tensor the type _D_ structure above with _CFDA_[�] ( _τµ_ ) twice. The invariant _CFDA_[�] ( _τµ_ ) was computed in an earlier paper [LOT15, Section 10.2], and an easy computation of the tensor product gives that _CFDR_[�] (Σ( _P_ )) is the following, delightfully simple, type _D_ structure: 

**==> picture [70 x 38] intentionally omitted <==**

To compare the real and unreal invariants of the branched covers, the following lemma will be convenient. To pin down conventions, we use the conventions on the signature _σ_ ( _K_ ) for 

REAL BORDERED FLOER HOMOLOGY 

67 

**==> picture [350 x 69] intentionally omitted <==**

**----- Start of picture text -----**<br>
ρ 2 ρ 3 ρ 2 ρ 1<br>• ◦ • • ◦ •<br>ρ 1 ρ 1 ρ 3 ρ 3<br>• • ◦ ◦ ◦ ◦<br>ρ 123 ρ 123 ρ 3 ,ρ 2 ,ρ 1 ρ 3 ,ρ 2 ,ρ 1<br>ρ 2 ρ 3 ρ 2 ρ 1<br>• • • ◦ • • ◦ •<br>**----- End of picture text -----**<br>


Figure 29. **Bordered invariants for a box.** Left: a 1 _×_ 1 box, as appearing in the knot Floer complex. Center: the corresponding type _D_ structure. Right: the corresponding type _A_ module. Again, we have not drawn all the operations, just a generating set. 

which the right-handed trefoil knot has _σ_ = _−_ 2 and _τ_ = 1; in general, for alternating knots, _σ_ ( _K_ ) = _−_ 2 _τ_ ( _K_ ). We let det( _K_ ) = _|_ ∆( _−_ 1) _|_ . (We apologize that _τ_ is being used both for the involution and the concordance invariant [OSz03], and hope this will not cause confusion.) 

**Lemma 9.7.** _Let K be an alternating knot in S_[3] _. Then the dimension of HF_[�] ( _S_ 1[3][(] _[K]_[))] _[is] given by the formula_ 

**==> picture [26 x 13] intentionally omitted <==**

**==> picture [324 x 51] intentionally omitted <==**

_The dimension of HF_[�] ( _S_ 1[3] _/_ 2[(] _[K]_[))] _[is][given][by]_ 

**==> picture [383 x 51] intentionally omitted <==**

_Proof._ This can be deduced from the knot Floer homology for alternating knots [OS03], combined with surgery formulas for Heegaard Floer homology [OSz08, OSz11]. 

Specifically, the knot Floer homology _HFK_[�] ( _K_ ) of an alternating knot _K_ is determined by its Alexander polynomial ∆ _K_ ( _t_ ) =[�] _i[a][i][T][ i]_[,][and][its][signature] _[σ]_[,][by][the][formula] 

**==> picture [324 x 37] intentionally omitted <==**

The knot Floer complex splits as a direct sum of 1 _×_ 1 boxes (Figure 29) and a staircase (Figure 28) [OS03, Pet13]. 

A staircase is determined by its dimension (which is odd) and its sign. The dimension of the staircase is given by 2 _|τ_ ( _K_ ) _|_ + 1, and the sign is the sign of _τ_ ( _K_ ). 

The surgery formula [OSz08] expresses _HF_[�] ( _S_ +1[3][(] _[K]_[))][as][the][homology][of][a][mapping][cone] of a chain map A _→_ B, which can be described in terms of the knot Floer complex. 

Each box gives rise to a 2-dimensional subspace in _H∗_ (A) which maps trivially to _H∗_ (B). By Equation (9.10), the number of boxes is 

**==> picture [125 x 26] intentionally omitted <==**

LIPSHITZ AND OZSVÁTH 

68 

A straightforward computation shows that when _τ_ = 0, the trivial staircase contributes 1; when _τ >_ 0, the staircase contributes 4 _τ −_ 3; and when _τ <_ 0, the staircase contributes _−_ 4 _τ −_ 1. Equation (9.8) follows. 

For 1 _/_ 2 surgery, we rely on the rational surgery formula [OSz11]. In that case, each box in � _HFK_ contributes 4 to the rank. When _τ_ = 0, the trivial staircase contributes F2; when _τ >_ 0, the staircase contributes F _[−]_ 2[5+8] _[τ]_ ; and when _τ <_ 0, the staircase contributes F _[−]_ 2[8] _[τ][−]_[3] . □ 

_Proof of Theorem 1.2._ As in the previous proof, since _K_ is alternating, its knot Floer complex is the direct sum of a staircase and a collection of 1 _×_ 1 boxes. The type _D_ structures for staircases are shown in Figure 28. The corresponding type _A_ modules are also shown in Figure 28, following the algorithm from Hedden-Levine [HL16, Theorem 2.2]. The type _D_ structure for a 1 _×_ 1 box and the corresponding type _A_ module are shown in Figure 29. Taking the box product with _CFDR_[�] (Σ( _P_ )): 

**==> picture [443 x 67] intentionally omitted <==**

Combining these, 

**==> picture [281 x 37] intentionally omitted <==**

Next, we compute unreal _HF_[�] of the branched double cover. By Montesinos’s trick, the branched double cover of the Whitehead double of any knot _K_ is _S_ 1[3] _/_ 2[(] _[K]_[#] _[r]_[(] _[K]_[))][,][where] _[r]_ denotes the reverse. Since _K_ # _K[r]_ is an alternating knot, Lemma 9.7 implies that 

**==> picture [315 x 51] intentionally omitted <==**

Finally, using det( _K_ ) _≥_ 2 _|τ |_ + 1, it is easy to verify the inequality dim _HFR_[�] (Σ( _P_ ( _K_ )) _, τ_ ) _≤_ dim _HF_[�] (Σ( _P_ ( _K_ ))), with equality holding if and only if (det( _K_ ) _, τ_ ( _K_ )) = (1 _,_ 0). □ 

As a second example, we consider (2 _,_ 1)-cables. A real bordered Heegaard diagram for the branched double cover of the cabling pattern is shown in Figure 30; this is, of course, [0 _,_ 1] _× T_[2] , with boundary parametrizations differing by a Dehn twist, and involution coming from the involution on _T_[2] with quotient a Möbius band. Since this is a genus 1 diagram, it is easy to compute its invariants; its _CFDR_[�] is given by: 

**==> picture [124 x 14] intentionally omitted <==**

To assist with analyzing the framing later, observe that the space of periodic domains is spanned by 

**==> picture [360 x 11] intentionally omitted <==**

REAL BORDERED FLOER HOMOLOGY 

69 

**==> picture [174 x 177] intentionally omitted <==**

**==> picture [132 x 121] intentionally omitted <==**

Figure 30. **A diagram for the** (2 _,_ 1) **-cable.** We have drawn the diagram on a torus and on the rectangle with opposite edges identified. 

The elements of _H_ 1( _F_ ( _ZL_ )) and _H_ 1( _F_ ( _ZR_ )) given by the boundaries of these domains are 

**==> picture [354 x 29] intentionally omitted <==**

(listing multiplicities at _ρ_ 3 _, ρ_ 1, as we did for the Whitehead double). 

The branched double cover of the (2 _,_ 1)-cable pattern is the complement of the (2 _,_ 2) torus link (that is, the Hopf link) in _S_[3] , with each component 0-framed. The order of the first homology of the result of doing _p/q_ surgery to both components of the Hopf link is _|p_[2] _− q_[2] _|_ . We obtain this framing by tensoring the module above with _τλ_ , which transforms the boundaries of the periodic domains into 

**==> picture [364 x 30] intentionally omitted <==**

The corresponding module is 

**==> picture [74 x 14] intentionally omitted <==**

**Theorem 9.11.** _Given a knot K, let P_ ( _K_ ) _be the_ (2 _,_ 1) _-cable of K. Then, for any nontrivial alternating knot K,_ dim _HF_[�] (Σ( _P_ ( _K_ ))) _>_ dim _HFR_[�] (Σ( _P_ ( _K_ )) _, τ_ ) _._ 

_Proof._ This is similar to the proof of Theorem 1.2. Now, a staircase contributes to the dimension of _HFR_[�] as follows: 

**==> picture [289 x 13] intentionally omitted <==**

- 1 if _τ_ ( _K_ ) = 0, and 

**==> picture [339 x 13] intentionally omitted <==**

A box contributes 4 to _HFR_[�] . So, 

**==> picture [293 x 36] intentionally omitted <==**

LIPSHITZ AND OZSVÁTH 

70 

Figure 31. **A Heegaard diagram for a solid torus.** Left: the real Auroux-Zarev diagram for the genus 1 pointed matched circle. Right: a doubly-pointed bordered Heegaard diagram whose invariant is the same as the real bordered invariant of the Auroux-Zarev diagram. The fixed set in the first diagram and the _β_ -circle in the second have the same intersection pattern with the _α_ -arcs, hence represent isotopic circles in the torus. The knot lies on the torus and intersects the meridional disk once, hence is a longitude. 

For the knot Floer homology computation, recall that Σ( _P_ ( _K_ )) is 1-surgery on _K_ # _K[r]_ . So, the dimension of _HF_[�] (Σ( _P_ ( _K_ ))) is given by Lemma 9.7, but with _τ_ ( _K_ ) replaced by 2 _τ_ ( _K_ ) and det( _K_ ) replaced by det( _K_ )[2] . From these formulas, the result is straightforward. □ 

9.4. **Genus-1 splittings.** The next two propositions leverage computations for real thick tori to show that, in very special cases, _HFR_[�] can be identified with more familiar Heegaard Floer homology groups. 

**Proposition 9.12.** _Suppose that_ ( _Y, τ_ ) _is a (closed) real_ 3 _-manifold so that the fixed set K of τ is connected, and there is a separating, genus_ 1 _, τ -invariant surface_ Σ _containing K. Write Y_ = _Y_ 1 _∪_ Σ _Y_ 2 _, so Y_ 2 = _τ_ ( _Y_ 1) _. Let Y[′] be the result of Dehn filling Y_ 1 _with slope K, and let K[′] be the core (longitude) of the new solid torus, with framing induced by_ Σ _. Then_ 

**==> picture [212 x 17] intentionally omitted <==**

_where the sutures_ Γ _consist of two parallel copies of K._ 

_Proof._ This follows from the computation of _CFDR_[�] (AZ( _Z_ )) where _Z_ is the genus 1 pointed matched circle, from Example 5.12. Figure 31 shows a doubly-pointed bordered Heegaard diagram _H_ so that _CFD_[�] ( _H_ ) _[∼]_ = _CFDR_[�] (AZ( _Z_ )). It is clear that _H_ represents some knot in some bordered solid torus; the figure sketches a proof that the solid torus is the one filling _K_ , and that the knot is the longitude. □ 

**Proposition 9.13.** _Suppose that_ ( _Y, τ_ ) _is a (closed) real_ 3 _-manifold so that the fixed set L of τ consists of two circles, and there is a separating, genus_ 1 _, τ -invariant surface_ Σ _containing L. Write Y_ = _Y_ 1 _∪_ Σ _Y_ 2 _. Let Y[′] be the result of Dehn filling Y_ 1 _along the slope specified by L, and let K[′] be the core (longitude) of the new solid torus (with framing induced by_ Σ _). Then_ 

**==> picture [194 x 17] intentionally omitted <==**

REAL BORDERED FLOER HOMOLOGY 

71 

Figure 32. **Heegaard diagram for the solid torus and a knot in it.** Left: the diagram _H_ again, with the two components of the fixed set indicated. Center: the diagram _H_ 1 from the proof of Proposition 9.13. Right: the diagram _H_ 2 from that proof. 

_Proof._ This follows from the computation of _CFDR_[�] ( _H_ ) for the real thick torus _H_ in Section 4.1. Observe that _CFDR_[�] ( _H_ ) _[∼]_ = _CFD_[�] ( _H_ 1) _⊕ CFD_[�] ( _H_ 2) where _H_ 1 is a bordered Heegaard diagram for the solid torus in which the fixed set of _τ_ bounds a disk, and _H_ 2 is the same, but with an extra basepoint; see Figure 32. It is clear that this extra basepoint specifies the longitude of the solid torus. 

It follows from the pairing theorem, Corollary 6.6, that 

**==> picture [324 x 60] intentionally omitted <==**

This proves the result. 

**==> picture [11 x 9] intentionally omitted <==**

## 9.5. **Splittings with connected fixed sets and orientable quotients.** 

**Proposition 9.14.** _Let_ ( _Y, τ_ ) _be a (closed) real_ 3 _-manifold. Suppose that the fixed set K of τ is connected and_ ( _Y, τ_ ) _admits a τ -invariant separating surface_ Σ _containing the fixed set, so that_ Σ _/τ is orientable. Let K[′] and K[′′] be pushoffs of K in_ Σ _, disjoint from K and so that τ_ ( _K[′]_ ) = _K[′′] , and choose a τ -invariant arc A from K[′] to K[′′] . There is an induced real sutured manifold_ ( _Y \_ nbd( _K[′] ∪ K[′′] ∪ A_ ) _,_ Γ _, τ_ ) _, where_ Γ _consists of three sutures: a meridian of K[′] , a meridian of K[′′] , and a suture near A such that_ Γ _is separating. Then_ 

**==> picture [254 x 17] intentionally omitted <==**

_Proof._ By Corollary 5.16 (or its proof), placing an extra basepoint in AZ( _Z_ ) adjacent to the chord [2 _k_ + 1 _,_ 2 _k_ + 2] (the middle of the pointed matched circle) in _∂L_ AZ( _Z_ ), and an extra basepoint adjacent to the corresponding chord in _∂R_ AZ( _Z_ ), does not change the homotopy type of _CFDR_[�] . Deleting a neighborhood of these basepoints and a point on **z** gives a real bordered sutured diagram representing ( _Y \_ nbd( _K[′] ∪ K[′′] ∪ A_ ) _,_ Γ _, τ_ ). See Figure 33. □ 

## 10. Detours 

_Yet all experience is an arch wherethro’ Gleams that untravell’d world whose margin fades For ever and for ever when I move._ —Tennyson, “Ulysses” 

LIPSHITZ AND OZSVÁTH 

72 

**==> picture [224 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
K [′]<br>K K [′′]<br>**----- End of picture text -----**<br>


**==> picture [58 x 199] intentionally omitted <==**

Figure 33. **Adding basepoints to** AZ( _Z_ ) **.** Left: the diagram with the extra basepoints, and the knots _K_ , _K[′]_ , and _K[′′]_ indicated (dashed). Recall that there is a disk glued to the outer boundary of the diagram; _K_ , _K[′]_ , and _K[′′]_ close up in that disk. Right: a schematic of the sutures; in this picture, _K[′] ∪ K[′′] ∪ A_ is solid and the sutures are dashed. 

Our goal in this paper has been to give a usable algorithm to compute _HFR_[�] ( _Y_ ) for branched double covers _Y_ of knots in (closed) 3-manifolds, and we have developed the general theory of real bordered Heegaard Floer homology only as needed for that computation. We conclude by noting results we have not covered, which a researcher interested in further developing real bordered Heegaard Floer homology might (need to) explore. A topic being on this list does not imply there is some unexpected difficulty with it: we have avoided addressing some presumably easy problems to streamline this paper. 

- (1) Prove that every real bordered 3-manifold admits a real bordered Heegaard diagram. Equivalently, prove that for any real bordered 3-manifold ( _Y, τ_ ), there is a connected, separating, _τ_ -invariant surface _F ⊂ Y_ (containing the fixed set). (To deduce the first statement from the second, start with a real bordered Heegaard diagram for a real thick copy of _F_ , and then glue on bordered Heegaard diagrams for the rest of _Y_ .) 

- (2) Define _CFAR_[�] ( _Y, τ_ ) for a real bordered 3-manifold ( _Y, τ_ ), satisfying a pairing theorem with _CFDA_[�] . (Proposition 8.2 will presumably be a special case; in fact, by gluing on a bordered manifold, Proposition 8.2 induces a definition of _CFAR_[�] ( _Y, τ_ ) whenever the fixed set is connected and the manifold admits a connected, separating, _τ_ -invariant surface.) 

- (3) Determine a complete set of real bordered Heegaard moves, and prove that _CFDR_[�] and _CFAR_[�] are invariant under them. 

REAL BORDERED FLOER HOMOLOGY 

73 

- (4) Compute the invariants of enough real thick surfaces to extend the algorithm from Section 8 to compute the real bordered Floer homology of all closed real 3-manifolds, not just ones with connected fixed set. 

The paper also suggests some natural questions: 

- (5) Propositions 9.12 and 9.13 gave interpretations of _HFR_[�] in very special cases in terms of ordinary sutured Floer homology groups. Are there similar interpretations in other cases, or in general? 

- (6) Is there a version of real bordered Floer homology where the fixed sets contain arcs with endpoints on the bordered boundary, instead of just closed 1-manifolds in the interior? 

- (7) What is the natural algebraic or Fukaya-categorical framework for real bordered Heegaard Floer homology? That is, is there a purely algebraic setting in which analogues of the real bordered invariants of thickened surfaces are defined? 

## _How dull it is to pause, to make an end_ 

## References 

- [Aur10] Denis Auroux, _Fukaya categories and bordered Heegaard-Floer homology_ , Proceedings of the International Congress of Mathematicians. Volume II (New Delhi), Hindustan Book Agency, 2010, pp. 917–941. 

- [BGH08] Kenneth L. Baker, J. Elisenda Grigsby, and Matthew Hedden, _Grid diagrams for lens spaces and combinatorial knot Floer homology_ , Int. Math. Res. Not. IMRN (2008), no. 10, Art. ID rnm024, 39. 

- [BGX] Fraser Binns, Gary Guth, and Yonghan Xiao, _Real sutured Heegaard Floer homology_ , In preparation. 

- [DHST23] Irving Dai, Jennifer Hom, Matthew Stoffregen, and Linh Truong, _An infinite-rank summand of the homology cobordism group_ , Duke Math. J. **172** (2023), no. 12, 2365–2432. 

- [DKM[+] 24] Irving Dai, Sungkyung Kang, Abhishek Mallick, JungHwan Park, and Matthew Stoffregen, _The_ (2 _,_ 1) _-cable of the figure-eight knot is not smoothly slice_ , Invent. Math. **238** (2024), no. 2, 371–390. 

- [EGH00] Yakov Eliashberg, Alexander Givental, and Helmut Hofer, _Introduction to symplectic field theory_ , Geom. Funct. Anal. (2000), no. Special Volume, Part II, 560–673, arXiv:math.SG/0010059, GAFA 2000 (Tel Aviv, 1999). 

- [ENS02] John B. Etnyre, Lenhard L. Ng, and Joshua M. Sabloff, _Invariants of Legendrian knots and coherent orientations_ , J. Symplectic Geom. **1** (2002), no. 2, 321–367. 

- [GM25] Gary Guth and Ciprian Manolescu, _Real Heegaard Floer homology_ , 2025, arXiv:2504.09034. [Gut22] Gary Guth, _For exotic surfaces with boundary, one stabilization is not enough_ , 2022, arXiv: 2207.11847. 

- [Hen25] Kristen Hendricks, _A note on real Heegaard Floer homology and localization_ , 2025, arXiv:2508. 03897. 

- [HL16] Matthew Hedden and Adam Simon Levine, _Splicing knot complements and bordered Floer homology_ , J. Reine Angew. Math. **720** (2016), 129–154, arXiv:1210.7055. 

- [HL19] Kristen Hendricks and Robert Lipshitz, _Involutive bordered Floer homology_ , Trans. Amer. Math. Soc. **372** (2019), no. 1, 389–424. 

- [HM17] Kristen Hendricks and Ciprian Manolescu, _Involutive Heegaard Floer homology_ , Duke Math. J. **166** (2017), no. 7, 1211–1299. 

- [Kan22] Sungkyung Kang, _One stabilization is not enough for contractible 4-manifolds_ , 2022, arXiv: 2210.07510. 

- [KPT25] Sungkyung Kang, JungHwan Park, and Masaki Taniguchi, _Exotic diffeomorphisms on a contractible 4-manifold surviving two stabilizations_ , 2025, arXiv:2510.12394. 

- [Li22] Jiakai Li, _Monopole Floer homology and real structures_ , 2022, arXiv:2211.10768. 

LIPSHITZ AND OZSVÁTH 

|74<br>[Lin18]<br>[Lip06]<br>[Liu20]<br>[LM25]<br>[LMar]<br>[LOT11]<br>[LOT14a]<br>[LOT14b]<br>[LOT15]<br>[LOT18]<br>[Man16]<br>[Miy23]<br>[MS04]<br>[Nag79]<br>[Oh96]<br>[OS03]<br>[OSz03]<br>[OSz04]<br>[OSz08]<br>[OSz11]<br>[Pet13]<br>[Ras03]<br>[SW10]<br>[Zar10]<br>[Zha]|LIPSHITZ AND OZSVÁTH<br>Francesco Lin, _A Morse-Bott approach to monopole Floer homology and the triangulation con-_<br>_jecture_, Mem. Amer. Math. Soc. **255** (2018), no. 1221, v+162.<br>Robert Lipshitz, _A cylindrical reformulation of Heegaard Floer homology_, Geom. Topol. **10**<br>(2006), 955–1097, arXiv:math.SG/0502404.<br>C.-C. Melissa Liu, _Moduli of J-holomorphic curves with Lagrangian boundary conditions and_<br>_open Gromov-Witten invariants for an S_1_-equivariant pair_, J. Iran. Math. Soc. **1** (2020), no. 1,<br>5–95.<br>Jianfeng Lin and Anubhav Mukherjee,_Family Bauer-Furuta invariant, exotic surfaces and Smale_<br>_conjecture_, J. Assoc. Math. Res. **3** (2025), no. 2, 237–275.<br>Charles Livingston and Allison H. Moore, _Knotinfo: Table of knot invariants_, URL: `knotinfo.`<br>`org`, Current Month Current Year.<br>Robert Lipshitz, Peter S. Ozsváth, and Dylan P. Thurston,_Heegaard Floer homology as morphism_<br>_spaces_, Quantum Topol. **2** (2011), no. 4, 381–449, arXiv:1005.1248.<br>,_Bordered Floer homology and the spectral sequence of a branched double cover I_, J. Topol.<br>**7** (2014), no. 4, 1155–1199, arXiv:1011.0499.<br>,_Computing_ �<br>_HF by factoring mapping classes_, Geom. Topol.**18**(2014), no. 5, 2547–2681,<br>arXiv:1010.2550.<br>,_Bimodules in bordered Heegaard Floer homology_, Geom. Topol.**19**(2015), no. 2, 525–724,<br>arXiv:1003.0598.<br>, _Bordered Heegaard Floer homology_, Mem. Amer. Math. Soc. **254** (2018), no. 1216,<br>viii+279, arXiv:0810.0687.<br>Ciprian Manolescu,_Pin(2)-equivariant Seiberg-Witten Floer homology and the triangulation con-_<br>_jecture_, J. Amer. Math. Soc. **29** (2016), no. 1, 147–176.<br>Jin Miyazawa, _A gauge theoretic invariant of embedded surfaces in 4-manifolds and exotic P_ 2_-_<br>_knots_, 2023, arXiv:2312.02041.<br>Dusa McDuf and Dietmar Salamon, _J-holomorphic curves and symplectic topology_, American<br>Mathematical Society Colloquium Publications, vol. 52, American Mathematical Society, Prov-<br>idence, RI, 2004.<br>Teruo Nagase, _A generalization of Reidemeister-Singer theorem on Heegaard splittings_, Yoko-<br>hama Math. J. **27** (1979), no. 1, 23–47.<br>Yong-Geun Oh, _Fredholm theory of holomorphic discs under the perturbation of boundary condi-_<br>_tions_, Math. Z. **222** (1996), no. 3, 505–520.<br>Peter Ozsváth and Zoltán Szabó, _Heegaard Floer homology and alternating knots_, Geom. Topol.<br>**7** (2003), 225–254.<br>Peter S. Ozsváth and Zoltán Szabó, _Knot Floer homology and the four-ball genus_, Geom. Topol.<br>**7** (2003), 615–639, arXiv:math.GT/0301149.<br>, _Holomorphic disks and topological invariants for closed three-manifolds_, Ann. of Math.<br>(2) **159** (2004), no. 3, 1027–1158, arXiv:math.SG/0101206.<br>, _Knot Floer homology and integer surgeries_, Algebr. Geom. Topol. **8** (2008), no. 1, 101–<br>153.<br>, _Knot Floer homology and rational surgeries_, Algebr. Geom. Topol. **11** (2011), no. 1,<br>1–68.<br>Ina Petkova, _Cables of thin knots and bordered Heegaard Floer homology_, Quantum Topol. **4**<br>(2013), no. 4, 377–409.<br>Jacob Rasmussen,_Floer homology and knot complements_, Ph.D. thesis, Harvard University, Cam-<br>bridge, MA, 2003, arXiv:math.GT/0306378.<br>Sucharit Sarkar and Jiajun Wang, _An algorithm for computing some Heegaard Floer homologies_,<br>Ann. of Math. (2) **171** (2010), no. 2, 1213–1236, arXiv:math/0607777.<br>Rumen Zarev, _Joining and gluing sutured Floer homology_, 2010, arXiv:1010.3496.<br>Bohua Zhan, _bfh_<br>_python_, `https://github.com/bzhan/bfh_python`.|
|---|---|



REAL BORDERED FLOER HOMOLOGY 

75 

Department of Mathematics, University of Oregon, Eugene, OR 97403 _Email address_ : `lipshitz@uoregon.edu` 

Department of Mathematics, Princeton University, New Jersey, 08544 _Email address_ : `petero@math.princeton.edu` 

