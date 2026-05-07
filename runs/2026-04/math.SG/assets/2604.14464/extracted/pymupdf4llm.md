# **A cord algebra for tori in three-space** 

## **Dissertation** 

zur Erlangung des akademischen Grades Dr. rer. nat. 

eingereicht an der Mathematisch-Naturwissenschaftlich-Technischen Fakult¨at der Universit¨at Augsburg 

von 

## **Mari´an Poppr** 

Augsburg, July 2025 

**==> picture [169 x 98] intentionally omitted <==**

Betreuer: Prof. Dr. Kai Cieliebak, Universit¨at Augsburg Gutachter: Prof. Dr. Tobias Ekholm, Uppsala University 

Tag der m¨undlichen Pr¨ufung: 14.11.2025 

ii 

## **Abstract** 

Given a thin torus _TK,ε_ around a knot _K ⊂_ R[3] , we construct Morse models of cord algebra _Cord_ ( _TK,ε_ ) with Z and loop space coefficients. Using the Multiple time scale dynamics we identify _Cord_ ( _TK,ε_ ; Z) with _Cord_ ( _K_ ; Z). In combination with the work of [CELN16, Pet24] this indirectly relates _Cord_ ( _TK,ε_ ) to 0-th degree Legendrian contact homology _LCH_ 0( _L[∗]_ + _[T][K,ε]_[) of one component of unit conormal] bundle over _TK,ε_ . Our definition of _Cord_ ( _TK,ε_ ) is motivated by _J_ -holomorphic curves with boundary on the Lagrangian submanifold _L[∗]_ + _[T][K,ε][∪]_[R][3][with][arboreal] singularity along the torus _TK,ε_ . 

iii 

## **Acknowledgements** 

First and foremost, I would like to thank my supervisor, Kai Cieliebak, for many inspiring discussions and for encouraging me throughout all these years. Even though I kept calling our meetings “consultations”, which sounded sort of official, it was especially a place where I could share any of my thoughts and always obtain very human advice. 

I am grateful to my wife Zuzka for being with me on this adventure abroad. Without her unceasing support and love, it would not be possible. Also, I thank my parents, Andrea and Roman, for always being here for me. I cannot forget to express my gratitude to my grandparents Jarmila and Emil, brothers Vojta and Vratislav, and to Milada; this is also for you, grandma! 

Next, I am thankful to Urs Frauenfelder for always having time for my questions, sometimes even missing lunch, as the canteen closed. I thank Yuchen Wang for fruitful discussions about dynamical systems. I also want to thank all other members of our symplectic group in Augsburg for all the fun and valuable math inputs. Namely (among others), I thank Shuaipeng Liu, Frederic Wagner, Emilia Konrad, Kevin Ruck, Zhen Gao, Miguel Pereira, Hanna H¨außler, Filip Bro´ci´c, Evgeny Volkov, Airi Takeuchi, Milan Zerbin, Jennifer Gruber, and Lei Zhao. 

I thank Shah Faisal, Francisco Javier Mart´ınez Aguinaga, and Filip Strakoˇs for friendly talks about math. I also thank Jiˇr´ı Zeman and Pavel H´ajek for introducing me to life in Augsburg from a “Czech perspective”. I would like to thank Yukihiro Okamoto for the discussions about various aspects of knot contact homology, it was enjoyable to talk about the topics so closely related to my thesis. I thank Pavel Nov´ak for helping me with the English grammar. I thank my office mate, David Buchberger, for allowing me to expand to other tables and for explaining to me the basics of functional analysis. 

During my studies, I also greatly benefited from the discussions with other people: I thank Roman Golovko, Christian Kuehn, Alberto Abbondandolo, Frank Sottile, and Joa Webber. I also thank Vivek Shende for suggesting to study _J_ - holomorphic curves with the switches along the arboreal singularity _TK_ of the Lagrangian submanifold _L[∗]_ + _[T][K][∪]_[R][3][.][I am grateful to Tobias Ekholm, who agreed] to be a reviewer of my thesis. 

Next, I thank my floorball teammates from Augsburg for keeping me (somehow) fit. And finally, I thank my Czech friends for helping me not to forget the life in my home country. 

iv 

## **Contents** 

|**1**|**Introduction**|**Introduction**|||**1**|
|---|---|---|---|---|---|
||1.1|Algebraic invariants from conormal lifts . . . . . . . . . . . . . . .|||1|
||1.2|Main results . . . . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|2|
|**2**|**Knots and tori**||||**7**|
|**3**|**Space of outward-pointing chords** _MK,ε_||||**10**|
||3.1|A bit of diferential topology .|.|. . . . . . . . . . . . . . . . . . .|10|
||3.2|Defnition of _MK,ε_ . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|13|
||3.3|Topology of _MK,ε_ . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|18|
||3.4|Closer look on the _ε_-diagonal|.|. . . . . . . . . . . . . . . . . . .|33|
||3.5|Energy functions<br>. . . . . . .|.|. . . . . . . . . . . . . . . . . . .|45|
|**4**|**Adiabatic limit with Conley index**||||**57**|
||4.1|Gradient-like vector felds<br>. .|.|. . . . . . . . . . . . . . . . . . .|57|
||4.2|Uniform bounds . . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|60|
||4.3|Conley index<br>. . . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|68|
||4.4|Morse homology . . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|72|
||4.5|Map . . . . . . . . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|74|
|**5**|**Morse fow trees**||||**78**|
||5.1|Trees for knots<br>. . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|78|
||5.2|Trees for tori<br>. . . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|87|
|**6**|**Multiple time scale dynamics**||||**93**|
||6.1|Basic tracking of trajectories .|.|. . . . . . . . . . . . . . . . . . .|93|
||6.2|Fenichel theory . . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|94|
||6.3|Exchange lemma<br>. . . . . . .|.|. . . . . . . . . . . . . . . . . . .|102|
||6.4|Application to Morse fow trees||. . . . . . . . . . . . . . . . . . .|106|
|**7**|**Cord algebras**||||**123**|
||7.1|Topological cord algebra for knots . . . . . . . . . . . . . . . . . .|||123|
||7.2|Morse models for Cord algebras over Z . . . . . . . . . . . . . . .|||124|
||7.3|Morse models for Cord algebras with loop space coefcients . . . .|||125|
|||7.3.1<br>Knot case . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|125|
|||7.3.2<br>Torus case . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|128|
|**8**|**Relation to symplectic geometry**||||**134**|
||8.1|Symplectic set-up . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|134|
||8.2|Moduli spaces . . . . . . . . .|.|. . . . . . . . . . . . . . . . . . .|138|
||8.3|Geometry of switches . . . . .|.|. . . . . . . . . . . . . . . . . . .|140|
||8.4|Broken strings and chain maps|.|. . . . . . . . . . . . . . . . . . .|146|



v 

|**Appendices**<br>**155**|
|---|
|**A Maslov index in** (R2_n, ω_0)<br>**155**|
|A.1 Linear algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 155|
|A.2 Maslov index<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 157|
|**B Maslov index of Reeb chords**<br>**166**|
|B.1 Vector bundles<br>. . . . . . . . . . . . . . . . . . . . . . . . . . . . 166|
|B.2 Basics of symplectic and contact manifolds . . . . . . . . . . . . . 170|
|B.3 On cotangent bundles . . . . . . . . . . . . . . . . . . . . . . . . . 173|
|B.4 Binormal and Hamiltonian chords . . . . . . . . . . . . . . . . . . 175|
|B.5 Binormal and Reeb chords . . . . . . . . . . . . . . . . . . . . . . 179|
|**C Legendrian contact homology**<br>**184**|
|**D Proof of Lemma 45**<br>**188**|
|**List of Symbols**<br>**193**|
|**Bibliography**<br>**194**|



vi 

## **1. Introduction** 

## **1.1 Algebraic invariants from conormal lifts** 

With any submanifold _N ⊂_ R _[n]_ we can associate its unit conormal bundle _L[∗] N_ inside the unit co-sphere bundle _S[∗]_ R _[n]_ . _S[∗]_ R _[n]_ together with the restricted Liouville form _pdq_ becomes a contact manifold and _L[∗] N_ its Legendrian submanifold. In addition, an ambient isotopy of _N_ induces a Legendrian isotopy of its (unit) conormal lift _L[∗] N_ . Hence, for the study of _N_ we can use the toolkit of _J_ - holomorphic curves type invariants associated to _L[∗] N_ such as Legendrian contact homology (LCH). 

Legendrian contact homology was proposed in [EGH00] as the simplest invariant of the general framework of (relative) symplectic field theory. It arises as the homology of a certain differential graded algebra generated by words of Reeb chords, and with the differential counting _J_ -holomorphic curves with punctures asymptotic to Reeb chords. Later, it was proven in [EES05a, EES05b] that Legendrian contact homology is well-defined for Legendrian submanifolds for 1-jet spaces, and hence also of _J_[1] ( _S[n][−]_[1] ) _[∼]_ = _S[∗]_ R _[n]_ . 

In the last decades, _LCH_ ( _L[∗] N_ ) was extensively studied in the case when _N_ is a knot _K ⊂_ R[3] . Namely, L. Ng gave in a series of papers [Ng05a, Ng05b, Ng04] a combinatorial description of _LCH_ ( _L[∗] K_ ) and among others introduced the cord algebra _Cord[top]_ ( _K_ ). The cord algebra _Cord[top]_ ( _K_ ) is a computable invariant of _K_ which is isomorphic to _LCH_ 0( _L[∗] K_ ) and is generated by paths with endpoints on _K_ modulo certain skein relations. In particular, for framed oriented knots, the cord algebra detects the unknot. 

Later, it was verified in [EENS13] that the combinatorial description agrees with the count of _J_ -holomorphic curves from _LCH_ ( _L[∗] K_ ). The argument involved a representation of the knot _K_ in a more suitable form, as a braid along the unknot. This allowed to identify _LCH_ ( _L[∗] K_ ) with a count of certain gradient flow trees in the front projection _J_[0] ( _S_[2] ). 

Next, in [CELN16] a refined version of _LCH_ 0( _L[∗] K_ ) _[∼]_ = _Cord[top]_ ( _K_ ) was shown. Very roughly said, this more direct approach works as follows. We consider certain _J_ -holomorphic curves with one puncture in a Reeb chord and the boundary mapped to two cleanly intersecting Lagrangian submanifolds - the conormal bundle _L[∗] K_ and R[3] . Then _Cord[top]_ ( _K_ ) can be translated from the topological boundary of these _J_ -holomorphic curves. 

The approach of [CELN16] outlines a potential framework for the identification of _LCH_ ( _L[∗] K_ ) with its topological counterpart for more general manifolds than only _K_ . As a consequence, in [ENS17] it was shown that if _p_ is a point in R[3] _\ K_ , then the enhanced Legendrian contact homology _LCH_ 0( _L[∗] K ∪L[∗] p_ ) is a complete knot invariant. We stress that this result uses the “fully noncommutative” version of _LCH_ with loop space coefficients. 

In [Pet24], a Morse-theoretic model of _Cord[M]_ ( _K_ ) with loop space coefficients was constructed. This model counts certain Morse flow trees given by the gradient flow of the standard energy functional on the space _K × K_ . Also, _Cord[M]_ ( _K_ ) is isomorphic to _Cord[top]_ ( _K_ ) (even though the whole proof did not appear in the literature, to experts the isomorphism is known). 

1 

Recently, in [Oka25], Y. Okamoto, using de Rham chains, proposed a topological model of _LCH_ ( _L[∗] N_ ) with R-coefficients. In this case, _LCH_ ( _L[∗] N_ ) is of arbitrary degree and _N ⊂_ R _[n]_ is a closed oriented submanifold of arbitrary codimension. Then the same author studied in [Oka24] the singular and Morse models of _LCH_ ( _L[∗] N_ ) with Z2 coefficients, provided that _N_ has a high codimension. We would like to mention some other works on the knot case. Namely, _LCH_ ( _L[∗] K_ ) can be related to the framework of Ooguri-Vafa large N duality, see for example [EKL20, AENV14, Ekh18]. A different technique is microlocal sheaf theory, which was applied in [She19] to the proof that _L[∗] K_ is a complete knot invariant. A relation between microlocal simple sheaves and augmentations of the DGA underlying _LCH_ ( _L[∗] K_ ) was described in [Gao20]. 

To the end, we mention also the work of J. Asplund [Asp19] which studied _L[∗] N_ using partially wrapped Floer homology in the spirit of wrapped Fukaya categories of Liouville sectors from [GPS18]. 

## **1.2 Main results** 

To any knot _K ⊂_ R[3] we can associate an _ε_ -radius torus _TK,ε_ which arises as the boundary of the _ε_ -tubular neighborhood of _K_ . Since _TK,ε_ is a codimension 1 submanifold, its (unital) conormal lift has two connected components _L[∗] ±[T][K,ε]_[.] Let us take only one component; _L[∗]_ + _[T][K,ε]_[.][It][is][not][hard][to][see][that][there][is][a] canonical Legendrian isotopy _L[∗] K[∼]_ = _L[∗]_ + _[T][K,ε]_[(Lemma 296).][Hence, in particular,] _LCH_ 0( _L[∗] K_ ) _[∼]_ = _LCH_ 0( _L[∗]_ + _[T][K,ε]_[).][As][we][stated][above,][by][[CELN16,][Pet24]][there] is an isomorphism _LCH_ 0( _L[∗] K_ ) _[∼]_ = _Cord[M]_ ( _K_ ). Thus, it is natural to expect that there exists a Morse-theoretic _Cord[M]_ ( _TK,ε_ ) which matches its symplectic counterpart _LCH_ 0( _L[∗]_ + _[T][K,ε]_[).][In][short,][in][this][thesis,][we][are][going][to][study][the] following diagram 

**==> picture [181 x 59] intentionally omitted <==**

The core of the thesis is definition of the Morse model _Cord[M]_ ( _TK,ε_ ) with Z and _loop space coefficients_ and its relation to _Cord[M]_ ( _K_ ). In addition, this indirectly relates _Cord[M]_ ( _TK,ε_ ) to _LCH_ 0( _L[∗]_ + _[T][K,ε]_[).][The][map] _[ϕ][T] K,ε_[will][be][only][outlined][in] Chapter 8. However, leaving first a word about _ϕTK,ε_ will enlight the definition of _Cord[M]_ ( _TK,ε_ ). 

By _L[∗] ±[T][K]_[let][us][denote][two][half’s][of][the][conormal][bundle] _[L][∗][T][K]_[such][that] _L[∗] ±[T][K][⊂][L][∗] ±[T][K]_[.][Next,][similarly][to] _[ϕ][K]_[,][the][map] _[ϕ][T] K,ε_[will][also][use][punctured] _J_ -holomorphic curves with one puncture asymptotic to a Reeb chord and from whose topological boundary one can expect to reconstruct _Cord[M]_ ( _TK,ε_ ). However, now the boundary of the _J_ -holomorphic curves will be mapped to the Lagrangian submanifold _L[∗]_ + _[T][K,ε][∪]_[R][3][ with a simple arboreal singularity along] _[ T][K,ε]_[in] the sense of [Nad17]. This reflects the choice of the single component of _L[∗] TK,ε_ . As a consequence, the boundary of _J_ -holomorphic curves _u_ will satisfy certain jet conditions along the zero section R[3] . Let us denote by _cu_ the oriented path given by one connected component of _∂u ∩_ R[3] . In particular, after a choice of 

2 

appropriate conventions, we conclude that the path _cu_ will be outward-pointing from _TK,ε_ at both of its endpoints. 

Let us return, for now, back to _Cord[M]_ ( _TK,ε_ ). We aim to define _Cord[M]_ ( _TK,ε_ ) by the dynamics of a gradient-like flow of the standard energy functional _Eε_ on _TK,ε × TK,ε_ . However, motivated by _J_ -holomorphic curves we do not consider as an ambient space for the Morse dynamics of _Cord[M]_ ( _TK,ε_ ) the full product _TK,ε × TK,ε_ , but rather only the subspace 

**==> picture [102 x 13] intentionally omitted <==**

which represents the spaces of outward-pointing chords on _TK,ε_ , i.e., the space of oriented line segments on _TK,ε_ that are pointing out from the torus at their endpoints. 

**Theorem 1.** _Let K be generic and ε >_ 0 _be small. Then, outside of a small neighborhood of the diagonal, the space MK,ε is a_ 4 _-dimensional manifold with corners._ 

In addition, we will be able to describe the surprisingly rich topology of _MK,ε_ . In more detail, outside of certain special and diagonal points, _MK,ε_ will look just like a fiber bundle over _K × K_ with fibers diffeomorphic to the square. If we also include the special points, we obtain a broken fibration. We will compute _H_ 1 _[sing]_ of the broken fibration and conclude that the space _MK,ε_ itself remembers nontrivial information about the underlying knot _K_ . 

The topology of _MK,ε_ becomes more dramatic near the diagonal ∆ _full_ , where _MK,ε_ will become singular. As we will see later, this will significantly influence _Cord[M]_ ( _TK,ε_ ) with loop space coefficients. We will show that if _ε >_ 0 is small, then near the diagonal the space _MK,ε_ looks approximately as a stratified fiber bundle over a half-torus with cuspical fibers. 

In order to define _Cord[M]_ ( _TK,ε_ ; Z) we construct a chain complex in degrees 1 _,_ 0 which is generated by critical points of _Eε|MK,ε\_ ∆ _full_ of Morse indices 2 and 1, respectively. Then the differential will be counting certain Morse flow trees _♣[out] XEε[−][out] ⊂ MK,ε \_ ∆ _full_ given by the flow of a gradient-like vector field _XEε_ . Finally, _Cord[M]_ ( _TK,ε_ ; Z) will be 0-th homology of this chain complex. We remark that this version is not using the loop space coefficients, since we are not dealing with the diagonal. 

Similarly, A. Petrak’s [Pet24] cord algebra _Cord[M]_ ( _K_ ; Z) was defined by chains generated by critical points of the energy functional _E_ 0 on _K × K_ . The critical points of indices 1 and 0 were considered, and the differential counted Morse flow trees _♣XE_ 0 . Since there is a bijection between the critical points entering the cord algebras for _K_ and _TK,ε_ , one can guess that the algebras might be isomorphic. In fact, we will prove the following result. 

**Theorem 2.** _For generic K, generic gradient-like vector fields XE_ 0 _, XEε and ε >_ 0 _sufficiently small the cord algebras Cord[M]_ ( _K_ ; Z) _and Cord[M]_ ( _TK,ε_ ; Z) _are isomorphic on the chain level._ 

_Idea of the proof._ Theorem 2 is an adiabatic limit problem with _ε →_ 0. Instead of working with collapsing tori _TK,ε × TK,ε ⊂_ R[3] _×_ R[3] we work rather with configuration spaces given by parametrizations of _K_ and _TK,ε_ , namely with (R _/T_ Z)[2] 

3 

and (R _/T_ Z _× S_[1] )[2] (note that _MK,ε ⊂_ (R _/T_ Z _× S_[1] )[2] also makes sense). Then the main tool for the description of the dynamics of _XEε_ on (R _/T_ Z _× S_[1] )[2] will be multiple time scale dynamics, see for example [Kue15]. In particular, 

**==> picture [230 x 13] intentionally omitted <==**

is a fast-slow flow system with two possible time scales _t, τ_ , related by _τ_ = _t/ε_ . Sending _ε_ to 0 for different times scales, _t, τ,_ we will obtain the slow and the fast subsystem. Ideally, for _ε >_ 0 small, one will be able to recover the dynamics (1 _._ 1) from the interplay between the fast and slow subsystems, provided that (1 _._ 1) is not too singular. Since now we are not dealing with the diagonal and we work with critical points of low degrees, we will be able to avoid the “too singular” behavior of (1 _._ 1). Additionally, the dynamics of the slow subsystem will almost coincide with the dynamics of _XE_ 0 on (R _/T_ Z)[2] _._ 

In order to keep track of the dynamics of the trees _♣[out] XEε[−][out]_ (and _♣XE_ 0 ) it will be not enough to use the standard techniques of Fenichel theory [Fen79] and Exchange Lemmata [Bru99, Sch08]. Indeed, the trees have bifurcations, which depend also on the exterior geometry of _TK,ε_ and _K_ inside R[3] . So we will also need to mix the Fenichel theory and Exchange Lemmata with the perturbations of these bifurcations. 

In the end, we remark that we also prove a weaker version of Theorem 2 using the Conley index, [Con78, Sal85]. In more detail, we show a mod 2 correspondence between the heteroclinic orbits entering _Cord[M]_ ( _K_ ; Z) and _Cord[M]_ ( _TK,ε_ ; Z), where we will additionally be able to capture their homotopy classes (as paths with fixed endpoints). An advantage of the Conley index argument is that it reflects well the compactness argument that we also use in a more involved fashion use also in the multiple time scale dynamics for the trees. 

Now, we turn to the cord algebra with loop space coefficients Z[ _λ[±]_[1] _, µ[±]_[1] ] ( _[∼]_ = Z _π_ 1( _TK_ ) _[∼]_ = _H•_ (Ω _∗TK_ )), where _λ_ corresponds to a longitude and _µ_ to the meridian. Contrary to the knot case, the loop space coefficients in _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) appear much more naturally than in the knot case, because now the ends of the chords are actually living on _TK,ε_ . This becomes even more evident when we approach the diagonal. In the knot case, the chords at the diagonal are replaced by the slightly mysterious algebraic expression 1 _− µ_ . This cannot be seen from the Morse model and has to be justified by the behavior of _J_ -holomorphic curves on _L[∗] K_ . On the other hand, in the _TK,ε_ case, the algebraic expression 1 _− µ_ will be dictated by the cuspidal behavior of _MK,ε_ near the diagonal. 

In order to define _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) we again have to first construct a chain complex _C_ 1 _[M]_[(] _[T][K,ε]_[)] _−→Dε C_ 0 _[M]_[(] _[T][K,ε]_[).][This][will][consist][of][the][following:] 

- _C_ 1 _[M]_[(] _[T][K,ε]_[)][is][precisely][the][same][as][in][the][Z][-coefficient][case][-][the][Z][vector] space generated by _Crit_ 2( _Eε|MK,ε\_ ∆ _full_ ). 

- However, _C_ 0 _[M]_[(] _[T][K,ε]_[)][is][a][bit][more][involved.][By] _[m]_[∆] _ε_[we][denote][the][unique] global minimum of an auxiliary Morse function _h_ ∆ _ε_ on the diagonal ∆ _full_ . Then _C_ 0 _[M]_[(] _[T][K,ε]_[)][is][the][free][unital][noncommutative][Z][-algebra][generated][by] _Crit_ 1( _Eε|MK,ε\_ ∆ _ε_ ) _∪{m_ ∆ _ε}_ and extra generators _λ, µ_ such that _λ_ and _µ_ have inverses and commute together. Note that the Morse index of _m_ ∆ _ε_ is 0 and not 1! 

4 

- Finally, since ∆ _full_ is a Bott-nondegenerate critical manifold of _Eε_ , the differential _Dε_ will count cascade Morse flow trees _♣[c,out] XEε[−][out]_ together with the sign count of _λ, µ_ as the chord-endpoints from the flow trees cross the meridian or the longitude. 

## **Definition 3.** 

_Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) = _C_ 0 _[M]_[(] _[T][K,ε]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] _[/][I][T] K,ε[,] where ITK,ε is the two-sided ideal of C_ 0 _[M]_[(] _[T][K,ε]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] _[generated][by][the][image] of the linear map Dε and m_ ∆ _ε −_ 1 _._ 

Now, we conceptually explain how _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) counts the Morse flow trees near the diagonal. We remark that the following discussion will be only partially proven, but the author believes that the claims are supported by enough evidence. For more details, we refer to Chapter 7. 

For simplicity, let us take _K_ to be the standard unknot _KU_ , which lies in the _xy_ -plane. Let _pε ∈ Crit_ 2( _Eε|MK,ε\_ ∆ _full_ ). Then the crucial claim is the following. 

## **Claim 4.** 

**==> picture [233 x 19] intentionally omitted <==**

_(instead of the expected_ 2 _-dimensional intersection)._ 

In other words, the cuspical singularity of _MK,ε_ is decreasing the expected dimension of the intersection of stable and unstable manifolds by 1. This also depends on two other properties of _−∇Eε_ near the diagonal. First, the eigenvalues of _D∇Eε_ (∆ _full_ ) are so fortunate that by Sternberg’s Linearization Theorem the flow _−∇Eε_ is approaching ∆ _full_ from all directions “uniformly”. The second property is that _−∇Eε_ is strictly outward-pointing from _∂MK,ε_ near ∆ _full_ . This property will be only computed on one example, but is expected to be true. See also the _Mathematica_ model in Figure 1.1. 

**==> picture [258 x 163] intentionally omitted <==**

**----- Start of picture text -----**<br>
ctriv<br>×<br>cpε<br>**----- End of picture text -----**<br>


Figure 1.1: A visualization of _W−∇[u] Eε_[(] _[p][ε]_[)] _[∩][M][K] U[,ε]_[on] _[ T][K] U[,ε]_[.][The][ red][ curves depict] the endpoints of chords emanating from the chord _cε_ under the negative gradient flow constrained to _MKU ,ε_ . Similarly, the blue curves depict the starting points of chords emanating from the chord _cε_ under the negative gradient flow constrained to _MKU ,ε_ . Note also a single pair of red and blue curves that are connected by a trivial chord _ctriv_ ; they represent a trajectory _uε_ from _pε_ to ∆ _ε_ that stays the whole time in _MKU ,ε_ . 

5 

In Figure 1.1, we see the trace of a single trajectory _uε_ emanating from _pε_ that reaches ∆ _full_ . However, since the torus is symmetric along the _xy_ -plane, there is also another trajectory _u_ ˜︁ _ε_ with the trace symmetric to the trace of _uε_ , see Figure 1.2. Since the contribution of these two paths to the loop space coefficients differs by the meridian, we obtain the desired algebraic expression 1 _− µ_ . 

**==> picture [261 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
u [trace]<br>ε<br>u [trace]<br>˜︁ ε<br>cpε<br>**----- End of picture text -----**<br>


Figure 1.2: Traces of _uε_ and _u_ ˜︁ _ε_ . 

The last topic of the thesis is about the map _ϕTK,ε_ from _LCH_ 0( _L[∗]_ + _[T][K,ε]_[)][to] _Cord[M]_ ( _TK,ε,_ Z[ _λ[±]_[1] _, µ[±]_[1] ]) which will be only outlined. In more detail, we analyze the moduli space of _J_ -holomorphic curves with boundary on the Lagrangian submanifold _L[∗]_ + _[T][K,ε][∪]_[R][3][.][We stress the geometric interpretation of the compactness] phenomena of _J_ -holomorphic curves arising from the arboreal singularity. From that we propose a model of 0-th string homology _H_ 0 _[string]_ ( _TK,ε_ ) which is expected to be a middle step between _LCH_ 0( _L[∗]_ + _[T][K,ε]_[)][and] _[Cord][M]_[(] _[T][K,ε][,]_[ Z][[] _[λ][±]_[1] _[, µ][±]_[1][]).][In] short, our string homology _H_ 0 _[string]_ ( _TK,ε_ ) will be defined by a chain complex consisting of relative singular chains of broken strings. 

In the end, we remark that we included in the Appendix also the computation of the interplay between the Morse and Maslov indices of the corresponding Reeb and binormal chords. Such a formula appeared independently in [Oka24]. However, we believe that our approach focuses on a slightly different aspect of the problem and it is meaningful to include it. 

6 

## **2. Knots and tori** 

In the thesis, we would like to associate an algebraic structure with a thin torus _TK ⊂_ R[3] which arises as the boundary of a tubular neighborhood of the knot _K_ . So the aim of this short chapter will be to inspect the map _K ↦→ TK_ between the spaces of embedded knots and tori. For example, a priori it is not clear how many knots are “bounded” by a single torus or even _TK_ . For this, we use classical results from low-dimensional topology. 

**Definition 5.** _Let Q be an boundaryless submanifold of N . Let U ⊂N_ ( _Q, N_ ) _be an open neighborhood of the zero section_ 0 _N_ ( _Q,N_ ) _of the normal bundle N_ ( _Q, N_ ) _. Then a_ _**tubular neighborhood** νQ_ _**of** Q_ _**in** N is a mapping f_ : _U → N satisfying the following:_ 

( _i._ ) _f is an embedding._ 

( _ii._ ) _f |Q_ = _IdQ after the identification of Q with the zero section_ 0 _N_ ( _Q,N_ ) _._ 

( _iii._ ) _f_ ( _U_ ) _is an open neighborhood of Q in N ._ 

_Remark_ 6 _._ Let us consider a Riemannian metric _g_ on _N_ , this induce a _Ng_ ( _Q, N_ ). Then a tubular neighborhood can be constructed as an exponential map that is precomposed with the radial shrinking along each fiber to a sufficiently small neighborhood of 0 _N_ ( _Q,N_ ), for details see [Muk15, Thm 7.1.5]. Also, all tubular neighborhoods are (ambient) isotopic relative to the zero section [Hir97, Thm 5.3]. 

_Remark/Notation_ 7 _._ Now we restrict ourselves to _N_ := _S_[3] . By [Moi52] _S_[3] as a topological 3-manifold admits unique smooth and piecewise-linear structures. 

Now, a _**knot** K_ is a smooth embedding _S_[1] _↪→ S_[3] . Two knots _K_ 1 and _K_ 2 are _**equivalent**_ if there is an orientation–preserving homeomorphism _h_ : _S_[3] _→ S_[3] such that _h ◦ K_ 1 = _K_ 2. 

Analogously, a _**torus** T_ is a smooth embedding _S_[1] _× S_[1] _↪→ S_[3] . Two tori _T_ 1 and _T_ 2 are _**equivalent**_ if there is an orientation–preserving homeomorphism _h_ : _S_[3] _→ S_[3] such that _h ◦ T_ 1 = _T_ 2. 

_Remark_ 8 _._ By Remark 6, knots are completely determined by their tubular neighborhoods. 

Next, let _K_ 1 and _K_ 2 be equivalent knots. Then, by restriction, there is an orientation-preserving homeomorphism between the _**knot complements** S_[3] _\ νK_ 1 and _S_[3] _\ νK_ 2. In particular, it is an orientation-preserving homeomorphism between the boundaries of these complements. Thus, the boundary of a tubular neighborhood of the knot is a knot invariant. 

**Definition 9.** _For any knot K we define two simple curves_ m _,_ L _⊂ ∂_ ( _νK_ ) _. The_ _**meridian m** satisfies_ m _̸∼_ 0 _in π_ 1( _∂νK_ ) _and_ m _∼_ 0 _in π_ 1( _νK_ ) _. And the_ _**longitude**_ L _represents a generator of π_ 1( _νK_ ) _[∼]_ = Z _._ 

The following lemma is an adapted version of the Solid torus theorem from [Rol03]. 

7 

**Lemma 10.** _Let T be a torus in S_[3] _. Let A be one connected component of S_[3] _\ T . Then the closure A is a tubular neighborhood of some knot if and only if the natural inclusion π_ 1( _T_ ) _→ π_ 1( _A_ ) _has a non-trivial kernel. Moreover, if A is a tubular neighborhood of some knot K, then K is unique._ 

_Proof._ Let the inclusion _π_ 1( _T_ ) _→ π_ 1( _A_ ) has a non-trivial kernel. Then by Loop theorem [Pap57] there is a simple non-contractible closed curve in _T_ that bounds a disk _D_ in _A_ . Next, note that _A_ without a bicollared neighborhood _N_ of _D_ bounds (piecewise-linear) _S_[2] given by the union of two discs and the annulus _T \ N_ . Hence, by the polyhedral Schoenflies theorem [Rol03], _A \ N_ is _D_[3] . Finally, canonical gluing of _N_ to _D_[3] is homeomorphic to _S_[1] _× D_[2] , and hence it is a tubular neighborhood of some knot. The opposite implication is trivial. 

It remains to show the uniqueness of _K_ . We need to inspect in how many ways we can embed _S_[1] _×D_[2] into _S_[3] such that the boundary is glued to the boundary of _S_[3] _\ A_ via an orientation–preserving homeomorphism. This is precisely the _knot complement problem_ , see [Tie08], which was solved by Gordon and Luecke in [GL89]. They showed that there is only a trivial gluing (mapping the meridian to the meridian) or _A_ is a tubular neighborhood of the unknot (in this case, we can map the meridian to the meridian plus some number of twists by the longitude). The lemma follows. 

**Lemma 11.** _Any torus T bounds exactly one tubular neighborhood of some knot, unless T bounds a tubular neighborhood of an unknot, in which case it bounds two tubular neighborhoods of two unknots._ 

_Proof._ Let _A_ 1 _, A_ 2 be connected components of _S_[3] _\ T_ . Also, _π_ 1( _T_ ) _[∼]_ = Z _⊕_ Z and _π_ 1( _S_[3] ) _[∼]_ = 0. Hence by Van Kampen’s theorem at least one of inclusions _π_ 1( _T_ ) _→ π_ 1( _A_ 1) and _π_ 1( _T_ ) _→ π_ 1( _A_ 2) has a nontrivial kernel. Then by Lemma 10 the torus _T_ bounds at least one tubular neighborhood of some knot. 

Let _T_ bounds _νK_ . Then _π_ 1( _T_ ) _[∼]_ = _π_ 1( _∂νK_ ) is generated by the meridian m and the longitude L of _K_ . Also, by [Rol03] we know two observations: m is not contractible in _S_[3] _\ νK_ ; and L is contractible in _S_[3] _\ νK_ if and only if _K_ is an unknot. Then Lemma 10 finishes the proof. 

**Corollary 12.** _In S_[3] _there is a bijection between equivalence classes of knots and tori._ 

_Remark_ 13 _._ Let us fix an orientation of _S_[3] . We would like to discuss the choices of **orientations** of knots and tori. 

Let _T ⊂ S_[3] which is not the boundary of a tubular neighborhood of an unknot. Then by Lemma 11 there is a unique _K_ and a _νK_ such that _T_ = _∂_ ( _νK_ ). The open subset _Int_ ( _νK_ ) inherits the orientation of _S_[3] . In particular, _νK_ is oriented, and hence _∂_ ( _νK_ ) is oriented too. This induces an orientation of _T_ . However, such an orientation of _T_ does _not_ determine an orientation of _K_ . 

We note that an orientation of m determines an orientation of _K_ (even if _K_ is an unknot). Indeed, by the definition of m we can take a disk _D ⊂ νK_ such that _∂D_ = m and _K_ ⋔ _D_ at the unique point _x_ . Then 

**==> picture [105 x 13] intentionally omitted <==**

Since _S_[3] is oriented and _D_ inherits the orientation from m, we obtain the orientation of _K_ . 

8 

**Definition 14.** _A_ _**framed knot** K is a knot together with a nowhere-vanishing smooth section of the normal bundle N_ ( _K, S_[3] ) _called a_ _**framing** . Moreover, we enhance K with a base point ∗ on K._ 

_Remark_ 15 _._ Note that the choice of framing defines a (non-oriented) longitude L _⊂ ∂_ ( _νK_ ). An orientation of _K_ induces canonically an orientation of L. There is also a canonically chosen base point _∗_ on L corresponding to the base point on _K ⊂N_ ( _K, S_[3] ). 

_Remark_ 16 _._ Let _p ∈ S_[3] . Then the stereographic projection gives us a diffeomorphism between _S_[3] _\ {p}_ and R[3] . 

_From now on, we will consider knots and tori only in_ R[3] _._ 

**Definition 17.** _Let K be a knot in_ (R[3] _, geuc_ ) _and ε >_ 0 _small. Then we take a tubular neighborhood νK given by an embedding Uε ↪→_ R[3] _;_ ( _q, vq_ ) _↦→ q_ + _vq, where Uε_ := _{_ ( _q, vq_ ) _∈NgEuc_ ( _K,_ R[3] ) _| ∥ vq ∥_[2] _geuc[< ε][}][.] Then the boundary ∂_ ( _νK_ ) _will be denoted as TK._ 

_Remark_ 18 _._ There is a constant _εgood >_ 0 such that _TK_ exists for all _ε ∈_ (0 _, εgood_ ]. Moreover, they are all in the same (ambient) isotopy class, see Remark 6. Later, we would like often to stress out the size of the radius _ε_ , and then we will write _TK,ε_ . 

**Corollary 19.** _Let us consider a torus TK. Then the orientation classes of K are in a bijection with the orientation classes of_ m _⊂ TK. Moreover, the homotopy classes of framings are in bijection with homotopy classes of_ L _⊂ TK._ 

9 

## **3. Space of outward-pointing chords** _M K,ε_ 

Given a thin torus _TK,ε ⊂_ (R[3] _, gEuc_ ), we consider the space of chords - oriented straight lines with endpoints on _TK,ε_ . In fact, we would like to consider a smaller space - _MK,ε_ which consists of those chords that, at their endpoints, point out from the tubular neighborhood _νK_ . 

We emphasize that our primary motivation for studying this space is given by certain _J_ -holomorphic curves. Such _J_ -holomorphic curves have a boundary on the Lagrangian manifold R[3] _∪L[∗]_ + _[T][K,ε]_[with the arboreal singularity along] _[ T][K,ε]_[and] at + _∞_ are asymptotic to Reeb chords of R+ _×L[∗]_ + _[T][K,ε]_[.][It turns out that these] _[ J]_[-] holomorphic curves, when restricted to the zero section R[3] , behave as collections of paths with endpoints on _TK,ε_ , where they have _outward-pointing conditions_ . In other words, one can think nonformally about _J_ -holomorphic curves as a potential chain map from Legendrian contact homology of _L[∗]_ + _[T][K,ε]_[to some Morse-theoretic] algebra of chords on _TK,ε_ (called cord algebra). And the _J_ -holomorphic curves indicate that _MK,ε_ is a good candidate for the ambient space of the cord algebra. For more details, we refer to Chapter 8. On the other hand, the space _MK,ε_ itself is interesting due to its nontrivial topology. For example, from its first homology we will be able to recollect some nontrivial information about the underlying knot. 

The main goal of this chapter is to inspect the manifold structure of _MK,ε_ with special care for the singular behavior near the constant chords, which will later play an important role in the cord algebra. We also study _Eε_ ; the restriction of the standard energy function to _TK,ε × TK,ε_ . 

## **3.1 A bit of differential topology** 

In this section, we present some rather standard properties of manifolds with corners that will be used throughout the subsequent sections. 

**Definition 20.** _A_ _**manifold with corners** M of dimension n is a Hausdorff space such that:_ 

- ( _i._ ) _For every x ∈ M there is a chart_ ( _Ux, φx_ ) _, i. e. an open neighbourhood Ux ⊂ M and φx_ : _Ux →_ R _[j] ×_ [0 _, ∞_ ) _[n][−][j] a homeomorphism onto an open subset of_ R _[j] ×_ [0 _, ∞_ ) _[n][−][j] for some j ∈_ N0 _._ 

- ( _ii._ ) _For any two charts_ ( _Ux, φx_ ) _and_ ( _Uy, φy_ ) _the composition φx ◦ φ[−] y_[1] : _φy_ ( _Ux ∩ Uy_ ) _→ φx_ ( _Ux ∩ Uy_ ) _extends to a smooth map between open sets of_ R _[n] ._ 

**Definition/Lemma 21.** _[Nie81]Let M be a manifold with corners and x ∈ M . We say that j is the_ _**index** ι_ ( _M, x_ ) _**of** x_ _**in** M if there is a chart_ ( _Ux, φx_ ) _on M such that φ_ : _Ux →_ R _[j] ×_ [0 _, ∞_ ) _[n][−][j] and φx_ ( _x_ ) = 0 _._ ( _Ux, φx_ ) _will be called an_ _**index chart for** x. The index is independent of the choice of an index chart._ 

_M is a disjoint union of (boundaryless) manifolds {Mj}j∈{_ 0 _,...,n} such that_ 

**==> picture [147 x 13] intentionally omitted <==**

10 

_A connected component of Mj is called an j_ _**-stratum** , Mn is the interior Int_ ( _M_ ) _of M , and the set M \ Mn is the boundary of M . The closure of each Mj is called a j_ _**-face** . We assume that each face is also a manifold with corners._ 

**Definition 22.** _Let M be a manifold with corners, N be a boundaryless manifold and Q ⊂ N is a submanifold with corners. We say that a smooth map f_ : _M → N is_ _**stratum transverse to** Q if for any two strata M and Q the restriction f |M_ : _M → N is transverse to Q. In more detail, for any x ∈M holds that f_ ( _x_ ) _∈Q/ or_ 

**==> picture [164 x 14] intentionally omitted <==**

**Theorem 23.** _[Nie81] Let M be a manifold with corners, N be a boundaryless manifold and Q ⊂ N be a submanifold with corners. Let f_ : _M → N be a stratum transverse map to Q. Then either f[−]_[1] ( _Q_ ) = _∅, or_ 

- ( _i._ ) _f[−]_[1] ( _Q_ ) _is a submanifold with corners of M , and_ 

- ( _ii._ ) _f[−]_[1] ( _Q_ ) _is stratified by connected components of_ ( _f |M_ ) _[−]_[1] ( _Q_ ) _for all strata M and Q (of M and Q, respectively), and_ 

**==> picture [258 x 14] intentionally omitted <==**

**==> picture [357 x 14] intentionally omitted <==**

_Remark_ 24 _._ The following theorem is a generalization of [Hir97, thm 1.4] from manifolds with boundary to manifolds with corners. 

**Theorem 25.** _[Hir97] Let k ≥_ 1 _. Let M, N be manifolds with corners. Then the set of C[k] embeddings from M to N is open in C[k]_ ( _M, N_ ) _(with strong C[k] topology)._ 

**Theorem 26.** _[Tro78, GM12]Let k ≥_ 1 _. Let M be a manifold with corners, N be a boundaryless manifold, and Q ⊂ N be a submanifold with corners which is_ closed _in N . Then the set_ 

**==> picture [239 x 14] intentionally omitted <==**

_is open (in the strong C[k] topology) in C[k]_ ( _M, N_ ) _._ 

_Non-Example_ 27 _._ [GP10] Typically, we would like to apply Theorem 26 in the following scenario. We have a transverse map, and we would like to extend this map to a smooth homotopy of transverse maps. However, we will see that this might fail if the domain of the map is not compact. 

For this, we choose an auxiliary smooth function _ρ_ : R _→_ R such that 

**==> picture [123 x 37] intentionally omitted <==**

Now we define a family of functions _{ft_ : R _→_ R _}t∈_ R by 

**==> picture [77 x 13] intentionally omitted <==**

Let us put _Q_ = _{_ 0 _}_ . Then _f_ 0 ⋔ _Q_ , but for any _|t| >_ 0 it holds that _ft_ ⋔ _Q_ . 

11 

_Remark_ 28 _._ The following theorem is a generalization of Ehresmann’s Theorem [NP20] for manifolds with boundary to manifolds with corners. See also Thom’s first isotopy Lemma 84, which can be seen as Ehresmann’s Theorem for Whitney stratified spaces. 

**Ehresmann’s Theorem 29.** _[NP20] Let M be a manifold with corners, N be a boundaryless manifold. Let π_ : _M → N be a proper surjection that is a submersion on each stratum of M . Then π defines a locally trivial_ _**fiber bundle** , i.e., for every x ∈ N there is an open neighbourhood Ux in N and a (strata preserving) diffeomorphism ψ_ : _Ux × π[−]_[1] ( _x_ ) _→ π[−]_[1] ( _Ux_ ) _such that π ◦ ψ_ ( _u, v_ ) = _u for every_ ( _u, v_ ) _∈ Ux × π[−]_[1] ( _x_ ) _._ 

_Remark_ 30 _._ Similarly to vector bundles, as discussed in Appendix B.1, also any locally trivial fiber bundle _M → N_ over a contractible space _N_ is trivial. 

In short. We pick a smooth homotopy _F_ : _N ×_ [0 _,_ 1] _→ N_ from the identity to a constant map. Then the pull-back bundle _F[∗] M → N ×_ [0 _,_ 1] possesses a complete Ehresmann’s connection [dH15] ([dH15] also generalizes to the case for manifolds with corners). Then the time 1 flow of the horizontal lift of (0 _, ∂t_ ) gives a global trivialization of the fiber bundle _M_ . 

**Stability Lemma 31.** _Let M be a compact manifold with corners, N be a boundaryless manifold and Q ⊂ N be a submanifold with corners which is closed in N . Assume that there are two maps f, g_ : _M → N such that f is stratum transverse to Q and f_ ( _M_ ) _∩ Q ̸_ = _∅. If g is sufficiently close to f in C[∞] topology, then there is a smooth homotopy F_ : _M ×_ [0 _,_ 1] _→ N such that_ 

**==> picture [181 x 13] intentionally omitted <==**

**==> picture [362 x 14] intentionally omitted <==**

_Moreover, f[−]_[1] ( _Q_ ) _and g[−]_[1] ( _Q_ ) _are isotopic submanifolds with corners of M ._ 

_Proof._ Let _U_ be a small open neighbourhood of _f_ (in strong _C[∞]_ topology) in _C[∞]_ ( _M, N_ ), which consists of stratum transverse maps to _Q_ . Such a neighbourhood exists by Theorem 26. 

Next, by the Strong Whitney embedding theorem [Hir97], there is an embedding _φ_ : _N →_ R _[k]_ for some _k_ . Let us consider the normal bundle _N_ ( _N,_ R _[k]_ ) with the projection _πN_ . Put _Iε_ := ( _−ε,_ 1 + _ε_ ) for some _ε >_ 0. Now we define a smooth homotopy _F_[˜︁] : _M × Iε → N_ by 

**==> picture [225 x 19] intentionally omitted <==**

Since _M_ is compact, we see that if _ε >_ 0 is sufficiently small and _g_ is sufficiently close to _f_ , then each _F_[˜︁] _|M ×{t}_ lies also in _U_ . In particular, _F_ ˜︁ is also stratum transverse to _Q_ . 

Now, by Theorem 23 ( _i._ ), _F_[˜︁] _[−]_[1] ( _Q_ ) is a manifold with corners. We would like to show that _πt_ : _F_[˜︁] _[−]_[1] ( _Q_ ) _→ Iε_ defines a locally trivial fiber bundle. For this, we would like to apply Ehresmann’s Theorem 29. First, _πt_ is smooth. Since _f_ has a non-empty intersection with some stratum of _Q_ , the Simplified Newton’s method [Web99] on _F_ gives us the surjectivity of _πt_ (provided that _ε >_ 0 is sufficiently small and _g_ is sufficiently close to _f_ ). And since _M_ is compact and _Q_ closed, the fibers are compact and _πt_ is proper. 

12 

It remains to show that _πt_ is a submersion on each stratum of _F_[˜︁] _[−]_[1] ( _Q_ ). By Theorem 23 ( _ii._ ) _F_[˜︁] _[−]_[1] ( _Q_ ) is stratified by connected components of _F_[˜︁] _|[−] M×_[1] _Iε_[(] _[Q]_[) for] all strata _M ⊂ M_ and _Q ⊂ Q_ . Let _x_ = ( _m, t_ 0) _∈ F_[˜︁] _|[−] M×_[1] _Iε_[(] _[Q]_[).][We][would][like][to][show][that][there][is][a][tangent] vector _V_ = ( _v, ∂t_ ) _∈ Tx_ ( _F_[˜︁] _|[−] M×_[1] _Iε_[(] _[Q]_[)).][It][holds][that] 

**==> picture [383 x 22] intentionally omitted <==**

Moreover, by the construction of _F_[˜︁] it holds that 

**==> picture [314 x 22] intentionally omitted <==**

Let _{∂zi, ∂zj⊥[}]_[be][a][basis][of] _[T] F_[˜︁] ( _x_ ) _[N]_[such][that] _[{][∂][z][i][}]_[is][a][basis][of] _[T] F_[˜︁] ( _x_ ) _[Q][.]_[Then] _dF_[˜︁] _|M×Iε_ ( _x_ )(0 _, ∂t_ ) = _a[i] ∂zi_ + _b[j] ∂zj⊥[,]_ 

for some _a[i] , b[i] ∈_ R. By relation (3 _._ 1) we see that there exists _v ∈ TmM_ such that 

**==> picture [141 x 19] intentionally omitted <==**

This gives us the desired vector _V_ , and consequently _πt_ is also a submersion on each stratum of _F_[˜︁] _[−]_[1] ( _Q_ ). 

Then Ehresmann’s Theorem 29 gives us a locally trivial fiber bundle. The bundle has a contractible base, so in particular it is a trivial bundle. Since each _F_ ˜︁ _|[−] M_[1] _×{t}_[(] _[Q]_[) is a submanifold of] _[ M]_[,] _[ f][ −]_[1][(] _[Q]_[) and] _[ g][−]_[1][(] _[Q]_[) are isotopic submanifolds] of _M_ . 

**Definition 32.** _Let M be an n-dimensional manifold with corners, x ∈ M with ι_ ( _M, x_ ) := _j < n and v ∈ TxM . Let_ ( _Ux, φx_ : _Ux →_ R _[j] ×_ [0 _, ∞_ ) _[n][−][j]_ ) _be an index chart for x. We consider coordinates_ ( _q_ 1 _, . . . , qn_ ) _on_ R _[n] ×_ R _[n][−][j] . Then we say that the vector v is_ _**outward-pointing at** x if_ 

**==> picture [253 x 19] intentionally omitted <==**

_for every i ∈{j_ + 1 _, . . . , n}. If the signs in_ (3 _._ 2) _are all ≥, we say that the vector v is_ _**inward-pointing at** x. If the signs are all sharp, we say that v is_ _**strictly outward/inward-pointing at** x._ 

_The definitions are independent on the choice of the index chart. Moreover, if v_ = 0 _, then v is both outward-pointing and inward-pointing._ 

## **3.2 Definition of** _MK,ε_ 

We are going to introduce _MK,ε_ ; the space of outward-pointing chords, together with some associated terms. 

**Thom’s Transversality Theorem 33** ([Muk15]) **.** _Let r ∈_ N0 _. Suppose M, N, Q are boundaryless manifolds, where Q is a submanifold of J[r]_ ( _M, N_ ) _. Then the set {f ∈ C[∞]_ ( _M, N_ ) _| j[r]_ ( _f_ ) ⋔ _Q} is a dense subset of C[∞]_ ( _M, N_ ) _(with strong topology) and open if Q is closed._ 

13 

_Remark_ 34 _._ A closed subset Σ of a manifold _N_ is called **stratified** , if it is a disjoint locally finite union of connected submanifolds of _M_ called **strata** . The dimension of Σ is the maximal dimension of its strata. 

The stratified subset Σ is called **Whitney** , if the following holds. Let _Q, M_ are two strata with dim( _Q_ ) _<_ dim( _M_ ). Suppose that there are two sequences of points _xi ∈M_ and _yi ∈Q_ that converge to some _y ∈Q_ . Let the secant lines ~~_x_~~ _i_ ~~_, y_~~ _i_ converge to some limiting line _ℓ_ and the planes _TxiM_ converge to some limiting plane _τ_ . Then the **Whitney conditions** holds, that is _TyQ ⊂ τ_ and _ℓ ⊂ τ_ . The limiting plane _τ_ is called a **generalized tangent space at** _y_ . 

For example, every real analytic set can be (Whitney) stratified [GM12]. 

A map _f_ : _M → N_ is transverse to a (Whitney) stratified subset Σ if it is transverse to each stratum. In addition, Theorem 33 holds also in the case _Q_ = Σ, see [EM02, Thm 2.3.2] and [Tro78]. And if _f_ ⋔ Σ, then _f[−]_[1] (Σ) is a canonically (Whitney) stratified subspace of _M_ of the same codimension as Σ, see [GWdPL76, Thm 1.4]. Also, the transverse intersection of two (Whitney) stratified subspaces is a (Whitney) stratified subspace [GWdPL76]. 

**Lemma 35.** _A generic knot in_ R[3] _has nowhere-vanishing curvature._ 

_Proof._ Let _γ_ : _S_[1] _→_ R[3] be a knot. If _s ∈ S_[1] , then the curvature _κ_ at the point _s_ is defined as _κ_ ( _s_ ) := _||γ_ ̇ ( _s_ ) _×_ ¨ _γ_ ( _s_ ) _||/||γ_ ̇ ( _s_ ) _||_[3] . 

Let us consider coordinates ( _s, a, b, c_ ) on _J_[2] ( _S_[1] _,_ R[3] ) _[∼]_ = _S_[1] _×_ R[3] _×_ R[3] _×_ R[3] . If _s ∈ S_[1] , then _j_[2] _γ_ ( _s_ ) = ( _s, γ_ ( _s_ ) _, γ_ ̇ ( _s_ ) _,_ ¨ _γ_ ( _s_ )) _∈ J_[2] ( _S_[1] _,_ R[3] ). 

Let us put Σ := Σ1 _∪_ Σ2, where 

**==> picture [311 x 19] intentionally omitted <==**

We are going to show that Σ is a codim 2 stratified subset of R[6] . 

From _b × c_ = 0 we see that _b_ and _c_ are linearly dependent. So Σ1 has a structure of real line bundle over R[3] _\ {_ 0 _}_ , which is a 4-dimensional submanifold of R[6] . Moreover, we see that Σ is closed. Alternatively, we can see Σ as an algebraic set _b × c_ = 0. The map _b × c_ has rank 2 on Σ _\ {_ (0 _,_ 0) _}_ , and thus (0 _,_ 0) is the only singular point of Σ. Then the submanifold structure of Σ _\ {_ (0 _,_ 0) _}_ will follow from [BCR98, Prop 3.3.10-11]. 

So Σ[˜︁] := _S_[1] _×_ R[3] _×_ Σ is a codimension 2 stratified subset of _J_[2] ( _S_[1] _,_ R[3] ). By Thom’s Transversality Theorem 33 we have that _j_[2] _γ_ ⋔ Σ[˜︁] for a generic knot. Hence, from the dimension argument, the lemma follows. 

**Lemma 36.** _For a generic knot K in_ R[3] _it holds_ 

- ( _i._ ) _Let_ ( _p, q_ ) _∈ K × K such that p ̸_ = _q. The set of all pairs (points)_ ( _p, q_ ) _such that the tangent line to the knot from p meets the knot again at q is finite. Any such pair_ ( _p, q_ ) _is called p_ _**-special** ._ 

- ( _ii._ ) _Any p-special_ ( _p, q_ ) _pair has the property that tangent line at q does not lie in the osculating plane of p. Recall that the osculating plane of p is the affine plane spanned by the tangent and normal vectors to K at p._ 

- ( _iii._ ) _The subset of those pairs, such that p and q have the same tangent line, is empty._ 

14 

_The analogous statement holds also for q_ _**-special pairs (points)**_ ( _p, q_ ) _**.**_ 

_Proof._ For ( _i._ ) and ( _iii._ ), see the proof of Lemma 7 _._ 10( _b_ ) in [CELN16]. The part ( _ii._ ) is a straightforward application of Thom’s Transversality Theorem 84. 

_Remark_ 37 _._ From now on, we will consider only knots in R[3] that satisfy Lemmata 36 and 35. 

_Remark/Notation_ 38 _._ From now on, until otherwise said, _K_ will be a knot in R[3] with an arc length parametrization _γ_ : R _/T_ Z _→_ R[3] . 

Now, we introduce a function 

**==> picture [213 x 32] intentionally omitted <==**

¨ ¨ ̇ where _n_ ( _s_ ) = _γ_ ( _s_ ) _/||γ_ ( _s_ ) _||_ is the normal vector at _γ_ ( _s_ ) and _b_ ( _s_ ) = _γ_ ( _s_ ) _× n_ ( _s_ ) is the binormal vector at _γ_ ( _s_ ). Later, we will also use the notion of the torsion _τ_ ( _s_ ) := _⟨γ_ ̇ ( _s_ ) _×_ ¨ _γ_ ( _s_ ) _,[...] γ_ ( _s_ ) _⟩/||γ_ ̇ ( _s_ ) _×_ ¨ _γ_ ( _s_ ) _||_[2] . 

Let _ε ∈_ (0 _, εgood_ ]. Recall that _εgood_ was defined in Remark 18 as a radius of a tubular neighbourhood of _K_ . Then the embedded torus _TK,ε_ can be naturally parametrized as 

**==> picture [175 x 32] intentionally omitted <==**

Note that the map Γ _ε_ =0 is also well-defined and its image coincides with _K_ . Let us recall the Fren´et equations 

**==> picture [189 x 14] intentionally omitted <==**

which we use for the auxiliary computations 

**==> picture [319 x 13] intentionally omitted <==**

**==> picture [189 x 13] intentionally omitted <==**

**==> picture [402 x 42] intentionally omitted <==**

_Remark_ 39 _._ Since _TK,ε_ is an embedded surface, the rank of _d_ Γ _ε_ is 2 at each point ( _s, θ_ ). Hence, by relations (3.3), we obtain that 1 _− ε_ cos( _θ_ ) _κ_ ( _s_ ) _>_ 0. This give us an upper bound on _εgood_ : 

**==> picture [173 x 31] intentionally omitted <==**

_Remark_ 40 _._ We are going to show that _v_ ( _s, θ_ ) is outward-pointing normal vector to _TK,ε_ at Γ( _s, θ_ ), as expected. For this, we compute 

**==> picture [446 x 63] intentionally omitted <==**

Note that the vector product is nonzero by the definition of _ε_ from Remark 38 and the bound on _εgood_ from Remark 39. So _v_ ( _s, θ_ ) is normal to _TK,ε_ . Outwardpointing property is immediate from the definition of Γ _ε_ . 

15 

**Definition 41.** _For i_ = 1 _,_ 2 _, we define two families of functions {Fi_[[] _[ε]_[]] _[}][ε][∈]_[[0] _[,ε] good_[]] _which are given by_ 

**==> picture [283 x 34] intentionally omitted <==**

**==> picture [365 x 234] intentionally omitted <==**

**----- Start of picture text -----**<br>
Here ⟨·, ·⟩ is the standard Euclidean metric on R [3] . See also Figure 3.1.<br>v ( s 2 , θ 2)<br>Γ ε ( s 2 , θ 2)  − Γ ε ( s 1 , θ 1)<br>v ( s 1 , θ 1)<br>**----- End of picture text -----**<br>


Figure 3.1: The vectors Γ _ε_ ( _s_ 2 _, θ_ 2) _−_ Γ _ε_ ( _s_ 1 _, θ_ 1) _, v_ ( _s_ 1 _, θ_ 1) and _v_ ( _s_ 2 _, θ_ 2) appearing in the functions _F_ 1[[] _[ε]_[]] and _F_ 2[[] _[ε]_[]] in the case _ε >_ 0. 

**Definition 42.** _Let ε ∈_ [0 _, εgood_ ] _. The set_ 

**==> picture [341 x 43] intentionally omitted <==**

## _is called the_ _**set of outward-pointing chords** ._ 

_Moreover, if ε >_ 0 _, then the set MK,ε|s_ 1= _s_ 2 _is called ε_ _**-diagonal** and denoted by_ ∆ _ε. The set {_ (R _/T_ Z _× S_[1] )[2] _| s_ 1 = _s_ 2 _∧ θ_ 1 = _θ_ 2 _} is called the_ _**full diagonal** and denoted by_ ∆ _full._ 

_Remark/Notation_ 43 _._ Let _r ∈_ R+. An identification of _S_[1] with R _/r_ Z gives _S_[1] a structure of an abelian group. Let _a, b, c ∈ S_[1] . 

Under the expression _a ± b_ we will understand the unique equivalence class [ _a ± b_ ]. 

The linear order on R induce on _S_[1] a ternary relation - **cyclic order** [ _a, b, c_ ], which roughly means “after _a_ , one reaches _b_ before _c_ ”, for details see [nLa25]. This allows us to define intervals on _S_[1] . For example, the open interval ( _a, c_ ) is defined as the set of all _b_ such that [ _a, b, c_ ]. 

Next, _⟨·_[˜︃] _, ·⟩_ will denote the flat metric on _S_[1] , which is defined as the pull-back of the Euclidean metric on R. This will induce the distance function _d_[˜︁] ( _·, ·_ ) on _S_[1] . 

16 

**Definition 44.** _Let TK,ϵ be a torus in_ R[3] _, then for each_ ~~_s_~~ _∈_ R _/T_ Z _we define_ ~~_C_~~ _s,ε as follows. It will be the infinite cylinder in_ R[3] _that is spanned by the lines with directional vector γ_ ̇ ~~(~~ ~~_s_ )~~ _, which are intersecting the circle_ Γ _ε|s_ = _s[.]_ 

**Definition/Lemma 45.** _Let K be a knot in_ R[3] _. Then for each_ ~~_s_~~ _∈_ R _/T_ Z _there is a_ ~~_δ_~~ _s[∈]_[(0] _[, T/]_[2)] _[such][that][for][each][δ]_ 0 _[∈]_[(0] _[, ]_ ~~_[δ]_~~ _s_[]] _[there][is][ε]_ 0 _,s[∈]_[(0] _[, ]_ ~~_[δ]_~~ _s_ ~~[)]~~ _[with][the] following property. If ε ∈_ (0 _, ε_ 0 _,s_[]] _[,][then]_ 

- ( _i._ ) _There exist the unique a ∈_ ~~(~~ ~~_s_~~ _− δ_ 0 _,_ ~~_s_ )~~ _and b ∈_ ~~(~~ ~~_s, s_~~ + _δ_ 0) _such that the circles_ Γ _ε|s_ = _a,_ Γ _ε|s_ = _b are tangent to the infinite cylinder_ ~~_C_~~ _s,ε[at][one][point.] Moreover, it holds that a ∈_ ~~(~~ ~~_s_~~ _− δ_ 0 _,_ ~~_s_~~ _− ε_ ) _and b ∈_ ( ~~_s_~~ + _ε,_ ~~_s_~~ + _δ_ 0) _, and for any s ∈_ [ ~~_s_~~ _− δ_ 0 _, a_ ) _∪_ ( _b,_ ~~_s_~~ + _δk_ ] _the circle_ Γ _|s has an empty intersection with_ ~~_C_~~ _s,ε[.]_ 

_See Figure 3.2 (top)._ 

- ( _ii._ ) _There exist the unique c ∈_ ~~(~~ ~~_s_~~ _−δ_ 0 _,_ ~~_s_ )~~ _and d ∈_ ~~(~~ ~~_s, s_~~ + _δ_ 0) _such that the infinite cylinders Cc,ε, Cd,ε are tangent to the circle_ Γ _ε|s_ = _s[at][one][point.]_ 

   - _Moreover, it holds that c ∈_ ~~(~~ ~~_s_~~ _− δ_ 0 _,_ ~~_s_~~ _− ε_ ) _and d ∈_ ~~(~~ ~~_s_~~ + _ε,_ ~~_s_~~ + _δ_ 0) _, and for any s ∈_ [ ~~_s_~~ _− δ_ 0 _, a_ ) _∪_ ( _b,_ ~~_s_~~ + _δk_ ] _the circle_ Γ _|s_ = _s[has][an][empty][intersection] with C . s,ε_ 

_See Figure 3.2 (bottom)._ 

_Now we define the following terms._ 

_Let δ ∈_ (0 _,_ inf _{_ ~~_δ_~~ _s[|]_ ~~_s_~~ _∈_ R _/T_ Z _}_ ) _. Let us consider a set_ 

**==> picture [209 x 15] intentionally omitted <==**

_or equivalently_ 

**==> picture [67 x 14] intentionally omitted <==**

_where the smooth function Fdist_ : R _/T_ Z _×_ R _/T_ Z _→_ R _/T_ Z _is given by_ ( _s_ 1 _, s_ 2) _↦→ s_ 2 _− s_ 1 _. Such a set will be called a_ _**weak diagonal set** , and elements of the weak diagonal set are called_ _**weak diagonal pairs (points)** ._ 

_Put εdiag_ = inf _{ε_ 0 _,s[|]_ ~~_s_~~ _∈_ R _/T_ Z _∧ δ_ 0 = _δ_ ] _}. Let ε ∈_ (0 _, εdiag_ ) _. The subset of the weak diagonal set_ 

**==> picture [209 x 15] intentionally omitted <==**

_is called an_ _**almost diagonal set** and elements of the almost diagonal set are called_ _**almost diagonal pairs** . Finally, pairs_ ( _s_ 1 _, s_ 2) _with s_ 1 = _s_ 2 _are called_ 0 _**-diagonal** and form the set denoted by_ ∆0 _._ 

_Proof._ Even though the lemma is “evident” from Figure 3.2, the actual proof is a bit technical, since one has to consider all possible local perturbations of the underlying knot _K_ . Thus, we leave the straightforward, but technical, proof to Appendix D. 

**Definition 46.** _Let K be a knot in_ R[3] _and_ ~~_s_~~ 2 _-special pair_ ~~(~~ ~~_s_~~ 1 _,_ ~~_s_~~ 2) _∈_ R _/T_ Z _×_ R _/T_ Z _. Let also δ_ ( _s_ 1 _,s_ 2) _[>]_[ 0] _[.][Then][the][set]_ 

**==> picture [375 x 14] intentionally omitted <==**

_is called the_ _**weakly**_ ~~_s_~~ 2 _**-special set** and its elements as the_ _**weakly**_ ~~_s_~~ 2 _**-special pairs (points)** ._ 

_The analogous statement also holds for_ ~~_s_~~ 1 _-special pairs._ 

17 

**==> picture [275 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
T<br>K,ε<br>Γ ε|s = a<br>•<br>C s,ε<br>T<br>K,ε<br>Cc,ε Γ ε|s = s<br>•<br>**----- End of picture text -----**<br>


Figure 3.2: _Top:_ the intersection (red point) of the cylinder ~~_C_~~ _s,ε_[with][the][circle] Γ _ε|s_ = _a_ . _Bottom:_ the intersection (red point) of the cylinder _Cc,ε_ with the circle Γ _ε|s_ = _s_[.] 

_Remark_ 47 _._ Let _K_ be a generic knot. There is 

**==> picture [243 x 19] intentionally omitted <==**

such that if _δK ∈_ (0 _, δ_ 0), then weak diagonal and weak special sets are disjoint. Let us fix in this Chapter some _δK_ . The complement of the corresponding weak special and weak diagonal sets is called the **standard set** _SK_ . 

## **3.3 Topology of** _MK,ε_ 

In this section, we would like to inspect the manifold structure of _MK,ε \_ ∆ _ε_ provided that _K_ is generic and the radius _ε >_ 0 is small. We aim to write _MK,ε_ as a broken fibration over _K × K_ and describe the fibers. 

**Definition 48.** _Let M be a k-dimensional boundaryless manifold and N be a n- product of copies of_ R _or_ R _/T_ Z _. Let F_ = ( _F_ 1 _, . . . , Fn_ ) : _M → N be a continuous map and let Q_ = _I_ 1 _× · · · × In ⊂ N be a product of intervals. Also let us consider a subset {i_ 1 _, . . . , ij} ⊂{_ 1 _, . . . , n}. Then we put_ 

**==> picture [259 x 19] intentionally omitted <==**

_where πℓ is the canonical projection onto ℓ-th component of N . In particular, Q is the interior Int_ ( _Q_ ) _._ 

_The set_ 

**==> picture [221 x 27] intentionally omitted <==**

_is called the_ _**fake boundary of** F[−]_[1] ( _Q_ ) _. Here recall that_ dim( _M_ ) = _k. Next, the set_ 

**==> picture [257 x 19] intentionally omitted <==**

18 

## _is called the_ _**real boundary of** F[−]_[1] ( _Q_ ) _._ 

_Remark_ 49 _._ In our applications, the manifold _M_ from Definition 48 will be a submanifold of (R _/T_ Z _× S_[1] )[2] or (R _/T_ Z _× S_[1] ) _×_ R _/T_ Z. In particular, _k_ will be 4 or 3. 

We will aim to split the space _MK,ε_ into several pieces, which will be easier to describe. So the notion of the real and the fake boundary will help us to distinguish which strata were made artificially by the splittings. 

**Theorem 50.** _Let us restrict ourselves outside of the weakly diagonal set (i.e., to the set J_ := _{_ ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] _| d_[˜︁] ( _s_ 1 _, s_ 2) _≥ δK}) and put M_[ˆ︂] _K,ε_ := _MK,ε|J . Then there is a ε_ 0 _∈_ (0 _, εgood_ ] _such that for each ε ∈_ [0 _, ε_ 0] _it holds that M_ ˆ︂ _K,ε is a compact_ 4 _-dimensional submanifold with corners. Moreover, all of these M_ ˆ︂ _K,ε are isotopic._ 

_The stratification of each M_[ˆ︂] _K,ε is induced by the stratum transverse intersections of F_[[] _[ε]_[]] = ( _F_ 1[[] _[ε]_[]] _[, F]_ 2[ [] _[ε]_[]] _[, F][dist]_[)] _[and][Q]_[ = [0] _[,][ ∞]_[)] _[ ×]_[ [0] _[,][ ∞]_[)] _[ ×]_[ [] _[δ][K][,][ −][δ][K]_[]] _[.]_ 

_Proof._ If we verify that _F_[[0]] is stratum transverse to _Q_ , then the theorem follows from Stability Lemma 31. 

But first, we would like to do a few auxiliary computations and describe the _T_ matrix (︂ _dF_ 1[[] _[ε]_[]] _[, dF]_ 2[ [] _[ε]_[]] )︂ (at some general point of (R _/T_ Z _× S_ 1)2). We will use the computation also for the study of the diagonal ∆ _ε_ (Definition 42), and hence we do not put _ε_ := 0 immediately. We compute few partial derivatives for _F_ 1[[] _[ε]_[]] 

**==> picture [211 x 77] intentionally omitted <==**

One can show that 

̇ _∂s_ 1 _F_ 1[[] _[ε]_[]] _[−][τ]_[(] _[s]_[1][)] _[∂][θ]_ 1 _[F]_ 1[ [] _[ε]_[]] = _−_ cos( _θ_ 1) _κ_ ( _s_ 1)⟨︂ _γ_ ( _s_ 2) _− γ_ ( _s_ 1) + _ε_ cos( _θ_ 2) _n_ ( _s_ 2) + _ε_ sin( _θ_ 2) _b_ ( _s_ 2) _, γ_ ( _s_ 1)⟩︂ _, ∂s_ 2 _F_ 1[[] _[ε]_[]] _[−][τ]_[(] _[s]_[2][)] _[∂][θ]_ 2 _[F]_ 1[ [] _[ε]_[]] = (1 _− ε_ cos( _θ_ 2) _κ_ ( _s_ 2))⟨︂ cos( _θ_ 1) _n_ ( _s_ 1) + sin( _θ_ 1) _b_ ( _s_ 1) _, γ_ ̇ ( _s_ 2)⟩︂ _._ 

Here we recall that 1 _− ε_ cos( _θ_ 2) _κ_ ( _s_ 2) _̸_ = 0 due to our choice of _ε_ . 

The case of _F_ 2[[] _[ε]_[]] is completely analogous; we only point out that 

**==> picture [220 x 77] intentionally omitted <==**

Let us introduce the notation 

**==> picture [152 x 40] intentionally omitted <==**

19 

⎛ ⎜ ⎜ ⎜ ⎝ 

where _i_ = 1 _,_ 2. Last, we will denote 

**==> picture [99 x 13] intentionally omitted <==**

**==> picture [547 x 221] intentionally omitted <==**

We will denote the elements of the matrix (︂ _dF_ 1[[0]] _[, dF]_ 2[ [0]] )︂ _T_ as _{ai,j}i,j_ . Let us show that _F_[[0]] ⋔ _Q_ 1 _,_ 2. So we need to show that _A_ has rank 2 along the solution set of 

**==> picture [243 x 50] intentionally omitted <==**

Arguing by contradiction, we assume that rank( _A_ ) _<_ 2. 

First, we inspect the cases where the second column is 0. If cos( _θ_ 2) = 0, then by _a_ 3 _,_ 2 and _a_ 4 _,_ 2 the vector _P_ is parallel to _v_ 2. Which is a contradiction by equation (3.7) and the fact that _s_ 1 = _s_ 2. 

If cos( _θ_ 2) = 0, then _v_ 2 = _±b_ ( _s_ 2). Also, by _a_ 4 _,_ 2 and equation (3.7), the vector _P_ is parallel to _γ_ ̇ ( _s_ 2). So by our generic assumptions on _K_ , we have that _P_ is ̇ not parallel to _γ_ ( _s_ 1). Also _s_ 1 = _s_ 2. Thus ( _s_ 1 _, s_ 2) is a _s_ 2-special pair. However, in that case we have assumed that _γ_ ̇ ( _s_ 1) is not lying in the osculating plane of _γ_ ( _s_ 2). But that is a contradiction with _a_ 1 _,_ 2. 

Hence, there exists _t ∈_ R such that _t_ -times the second column of _A_ is the first column. If _t ̸_ = 0, then from the second and fourth row of _A_ and equations (3.6) and (3.7) we obtain that _P_ is parallel to both _γ_ ̇ ( _s_ 1) and _γ_ ̇ ( _s_ 2). But that is not possible for a generic _K_ . 

If _t_ = 0, then the first column is 0, which is analogous to the case when the second column is 0. Hence we obtained contradiction and thus 

**==> picture [59 x 15] intentionally omitted <==**

Moreover, observe that when we assumed that one column of _A_ is zero, then we actually used for the contradiction always only one of the equations (3.6) and (3.7). Hence, in fact, we also showed that 

**==> picture [127 x 13] intentionally omitted <==**

20 

Also, trivially 

**==> picture [47 x 13] intentionally omitted <==**

Now, it remains to inspect the strata that contains the boundary of [ _δK, −δK_ ]. Note that at each point of (R _/T_ Z _× S_[1] )[2] 

**==> picture [106 x 13] intentionally omitted <==**

Let us show that _F_[[0]] ⋔ _Q_ 1 _,_ 2 _,_ 3 _._ Let _x ∈_ ( _F_[[0]] ) _[−]_[1] ( _Q_ 1 _,_ 2 _,_ 3). Note that by the construction of weakly diagonal sets, it holds that _πs_ 1 _,s_ 2( _x_ ) is not a special pair. In particular, _a_ 2 _,_ 1 and _a_ 4 _,_ 2 are non-zero. Hence from the description of _dFdist_ ( _x_ ) it follows that rank( _dF_[[0]] ( _x_ )) = 3, and thus 

**==> picture [65 x 15] intentionally omitted <==**

The cases _F_[[0]] ⋔ _Q_ 1 _,_ 3 and _F_[[0]] ⋔ _Q_ 2 _,_ 3 follow from the same argument as _F_[[0]] ⋔ _Q_ 1 _,_ 2 _,_ 3 did. 

Finally, the case _F_[[0]] ⋔ _Q_ 3 is immediate. 

_Notation_ 51 _._ We recall that in the proof of Theorem 50 we introduced the notation 

**==> picture [152 x 15] intentionally omitted <==**

**==> picture [119 x 13] intentionally omitted <==**

where _i_ = 1 _,_ 2. Last, we denoted 

**==> picture [99 x 13] intentionally omitted <==**

_Remark_ 52 _._ The proofs of the following lemmata - Lemma 53 and Lemma 54 are analogous to the proof of the Theorem 50. 

**Lemma 53.** _Let us restrict ourselves over some weakly special set W_ ( _s_ 1 _,s_ 2) _(i.e. to the set J_ := _{_ ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] _|_ ( _s_ 1 _, s_ 2) _∈ W_ ( _s_ 1 _,s_ 2) _}) and put M_ ˆ︂ _K,ε_ = _MK,ε|J . Then there is a ε_ 0 _∈_ (0 _, εgood_ ] _such that for each ε ∈_ [0 _, ε_ 0] _it holds that M_[ˆ︂] _K,ε is a_ 4 _-dimensional compact submanifold with corners. Moreover, all of these M_[ˆ︂] _K,ε are isotopic._ 

_The stratification of each M_[ˆ︂] _K,ε is induced by the stratum transverse intersections of F_[[] _[ε]_[]] = ( _F_ 1[[] _[ε]_[]] _[, F]_ 2[ [] _[ε]_[]] _[, Id, Id]_[)] _[and]_ 

**==> picture [157 x 14] intentionally omitted <==**

**Lemma 54.** _Let us restrict ourselves over SK (i.e. to the set J_ := _{_ ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] _|_ ( _s_ 1 _, s_ 2) _∈ SK}, where SK was introduced in Remark 47). We put and put M_[ˆ︂] _K,ε_ = _MK,ε|J . Then there is a ε_ 0 _∈_ (0 _, εgood_ ] _such that for each ε ∈_ [0 _, ε_ 0] _it holds that M_[ˆ︂] _K,ε is a_ 4 _-dimensional compact submanifold with corners. Moreover, all of these M_[ˆ︂] _K,ε are isotopic._ 

_The stratification of each M_[ˆ︂] _K,ε is induced by the stratum transverse intersections of F_[[] _[ε]_[]] = ( _F_ 1[[] _[ε]_[]] _[, F]_ 2[ [] _[ε]_[]] _[, F][dist][, Id, . . . , Id]_[)] _[and]_ 

**==> picture [412 x 28] intentionally omitted <==**

21 

_Remark_ 55 _._ In order to understand _MK,ε_ outside of a weakly diagonal set, it will be enough by Lemmata 53 and 54 to study only _MK,_ 0. 

**Lemma 56.** _Let M_[ˆ︂] _K,_ 0 := _MK,_ 0 _|πs−_ 11 _,s_ 2[(] _[S] K_[)] _[.][Then][the][canonical][projection][π][s]_[1] _[,s]_[2][:] _M_ ˆ︂ _K,_ 0 _→ SK defines a locally trivial fiber bundle._ 

_Proof._ Let _F_ ˆ︁ [0] = ( _F_ ˆ︁1[[0]] _[,][F]_[ˆ︁] 2[ [0]][)][denotes][the][restriction][of] _[F]_[ [0]][=][(] _[F]_ 1[ [0]] _[, F]_ 2[ [0]][)][to] _{_ ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] _|_ ( _s_ 1 _, s_ 2) _∈ SK}_ . By Lemma 54 _M_[ˆ︂] _K,_ 0 is a 4- manifold with corners and the stratification is induced by the stratum intersections of _F_ ˆ︁ [0] = ( _F_ ˆ︁1[[0]] _[,][F]_[ˆ︁] 2[ [0]][)][and] _[Q]_[=][[0] _[,][ ∞]_[)] _[×]_[[0] _[,][ ∞]_[).] Our aim is to apply Ehresmann’s Theorem 29 to the projection _πs_ 1 _,s_ 2 : _M_[ˆ︂] _K,_ 0 _→ SK_ . 

_πs_ 1 _,s_ 2 is smooth and surjective. Also, since the fibers are compact, _πs_ 1 _,s_ 2 is proper. We need to show that _πs_ 1 _,s_ 2 is a submersion on each stratum. 

On ( _F_[ˆ︁][[0]] ) _[−]_[1] ( _Q_ ), the projection _πs_ 1 _,s_ 2 is a submersion, since there is locally no condition on _s_ 1 and _s_ 2. 

Let _x_ = ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ ( _F_[ˆ︁][[0]] ) _[−]_[1] ( _Q_ 1). Then 

**==> picture [412 x 73] intentionally omitted <==**

**==> picture [169 x 20] intentionally omitted <==**

Since we are outside of (weakly) special and (weakly) diagonal pairs, _⟨P, v_ 1 _[⊥][⟩̸]_[= 0.] Hence, the rank condition immediately follows from matrix (3.5). 

We treat the remaining two cases similarly. 

_Remark_ 57 _._ We are going to replace Lemma 56 with a stronger result - Lemma 58. However, the proof of Lemma 56 is still conceptually useful, since we would like to describe globally _MK,_ 0 as a broken fibration - Definition 60. 

**Lemma 58.** _Over SK the manifold MK,_ 0 _is diffeomorphic to SK ×_ [ _−π/_ 2 _, π/_ 2] _×_ [ _−π/_ 2 _, π/_ 2] _._ 

_Proof._ Similarly to Lemma 56, let _M_[ˆ︂] _K,_ 0 denotes the restriction of _MK,_ 0 over _SK_ , which is by Lemma 54 a 4-manifold with corners. 

Observe that over _SK_ the projections of _P_ into normal planes at _γ_ ( _s_ 1) and _γ_ ( _s_ 2) are nowhere-vanishing vectors. Hence, for _i_ = 1 _,_ 2, we can make the following changes of smooth orthonormal frames _{n_ ( _si_ ) _, b_ ( _si_ ) _}_ to some _{n[∗] i_[(] _[s]_[1] _[, s]_[2][)] _[, b][∗] i_[(] _[s]_[1] _[, s]_[2][)] _[}]_ which are given by 

**==> picture [330 x 41] intentionally omitted <==**

where _Di_ = _⟨P, n_ ( _si_ ) _⟩_[2] + _⟨P, b_ ( _si_ ) _⟩_[2] _._ The frames _{n[∗] i_[(] _[s]_[1] _[, s]_[2][)] _[, b][∗] i_[(] _[s]_[1] _[, s]_[2][)] _[}]_[are][also] smooth. 

Let _θi[∗][∈][S]_[1][be][angular][coordinates][defined][by][(positively][oriented)][orthonor-] mal frames _{n[∗] i_[(] _[s]_[1] _[, s]_[2][)] _[, b][∗] i_[(] _[s]_[1] _[, s]_[2][)] _[}]_[.][Hence][for][each][(] _[s]_[1] _[, s]_[2][)] _[∈] SK_ the change of frames gives us an automorphims on _S_[1] 

**==> picture [133 x 14] intentionally omitted <==**

22 

Note that _⟨P, ±b[∗] i_[(] _[s]_[1] _[, s]_[2][)] _[⟩]_[= 0.][In other words, for] _[ θ][i]_[=] _[ φ][−] i_ ;([1] _s_ 1 _,s_ 2)[(] _[±][π/]_[2) it holds] that _Fi_[[0]] = 0. We remark that each of _Fi_[[0]] depends, besides _s_ 1 _, s_ 2 _,_ only on one of angular coordinates and that is _θi_ . Moreover, for _θi ∈ φ[−] i_ ;([1] _s_ 1 _,s_ 2)[((] _[−][π/]_[2] _[, π/]_[2))] holds that _Fi_[[0]] _>_ 0. Altogether, there is a (strata preserving) diffeomorphism _M_ ˆ︂ _K,_ 0 _→ SK ×_ [ _−π/_ 2 _, π/_ 2] _×_ [ _−π/_ 2 _, π/_ 2] which is given by 

**==> picture [252 x 13] intentionally omitted <==**

**Lemma 59.** _Let_ ~~(~~ ~~_s_~~ 1 _,_ ~~_s_~~ 2) _be a_ ~~_s_~~ 2 _-special pair. Then over W_ ( _s_ 1 _,s_ 2) _[the]_[4] _[-manifold] MK,_ 0 _is diffeomorphic to NK,_ 0 _×_ [ _−π/_ 2 _, π/_ 2] _, where NK,_ 0 _is a compact_ 3 _-manifold with corners that depends only on_ ( _s_ 1 _, θ_ 2 _, s_ 2) _. In more detail, NK,_ 0 _is stratified by the stratum transverse intersection of F_[[0]] = ( _F_ 2[[0]] _[, Id, Id]_[)] _[and][Q]_[=][[0] _[,][ ∞]_[)] _[ ×] W_ ( _s_ 1 _,s_ 2) _[(here][F]_[ [0]] _[is][the][function][in][variables]_[(] _[s]_ 1 _[, θ]_ 2 _[, s]_ 2[)] _[).]_ 

_The analogous statement holds for_ ~~_s_~~ 1 _-special pairs._ 

_Proof._ Let ~~(~~ ~~_s_~~ 1 _,_ ~~_s_~~ 2) be a ~~_s_~~ 2-special pair. Let _M_[ˆ︂] _K,_ 0 denotes the restriction of _MK,_ 0 over _W_ ( _s_ 1 _,s_ 2)[,][which][is][a][4-manifold][with][corners][by][Lemma][53.] Similarly to Lemma 58 we can write _NK,_ 0 _×_ [ _−π/_ 2 _, π/_ 2] as the image of the embedding of _M_ ˆ︂ _K,_ 0 which is given as 

**==> picture [203 x 14] intentionally omitted <==**

**Definition 60.** _Let M be a manifold with corners and f_ : _M →_ R _be a smooth function._ 

_A point p ∈ M is called a_ _**critical point of** f if df_ ( _p_ ) _|TpQ_ = 0 _, where Q is the stratum containing p. By Crit_ ( _f_ ) _, we will denote the_ _**set of critical points of** f ._ 

_The function f is called_ _**Morse** if:_ 

( _i._ ) _f is proper._ 

- ( _ii._ ) _For each stratum Q, the critical points of f |Q are nondegenerate._ 

- ( _iii._ ) _If p ∈Q is a critical point, then df_ ( _p_ ) _V_ = 0 _, where V is any vector space that satisfies the following property. There is a stratum M, higher then the stratum Q, and a sequence of points pj ∈M converging to p such that_ lim _pj →p Tpj M_ = _V ._ 

_Let I ⊂_ R _be an interval. In addition, if the Morse function f is surjective to I, then the restriction f_ : _f[−]_[1] ( _I_ ) _→ I is called a_ _**broken fibration** ._ 

_Remark_ 61 _._ See also [GM12] for the notion of Morse functions for (Whitney) stratified spaces. There is also a terminology of broken Lefschetz fibrations, for example, in [Lek13]. 

**Lemma 62.** _Let us consider any_ ~~_s_~~ 2 _-special pair_ ~~(~~ ~~_s_~~ 1 _,_ ~~_s_~~ 2) _. And put N_[ˆ︂] _K,_ 0 := _NK,_ 0 _|πs−_ 11[(] _s_ 1 _−δK ,s_ 1+ _δK_ ) _[.][Then the base projection][ π][s]_ 1[:] _N_[ˆ︂] _K,_ 0 _→_ ~~(~~ ~~_s_~~ 1 _−δK,_ ~~_s_~~ 1 + _δK_ ) _is a broken fibration with exactly two critical points. In more detail, the critical points are_ ~~(~~ ~~_s_~~ 1 _,_ ~~_s_~~ 2 _, ±π/_ 2) _, they lie in the real boundary of NK,_ 0 _and are of the Morse index_ 1 _._ 

_The analogous statement also holds for s_ 1 _-special pairs._ 

23 

_Remark_ 63 _._ The geometric picture of Lemma 62 will be described in Remark 67 and Figure 3.5. 

_Proof._ Let us describe _N_[ˆ︂] _K,_ 0 as ( _F_[[0]] ) _[−]_[1] ( _Q_ ), where _F_[[0]] = ( _F_ 2[[0]] _[, Id, Id]_[)][and] _[Q]_[=] [0 _, ∞_ ) _×_ ~~(~~ ~~_s_~~ 1 _− δK,_ ~~_s_~~ 1 + _δK_ ) _×_ [ ~~_s_~~ 2 _− δK,_ ~~_s_~~ 2 + _δK_ ]. Recall that here we see _F_[[0]] only as a function of variables ( _s_ 1 _, s_ 2 _, θ_ 2). Also _F_[[0]] and _Q_ are intersecting stratum transversely, see Theorem 50 or Lemma 53. 

Let us find the critical points. The strategy will be similar to the proof of Lemma 56, only now we look for the points where _πs_ 1 fails to be a fibration. 

So we immediately obtain that there are no critical points on ( _F_[[0]] ) _[−]_[1] ( _Q_ ) or ( _F_[[0]] ) _[−]_[1] ( _Q_ 3). 

Let us consider ( _F_[[0]] ) _[−]_[1] ( _Q_ 1). We pick _p ∈_ ( _F_[[0]] ) _[−]_[1] ( _Q_ 1). Then the matrix ( _dF_ 2[[0]][(] _[p]_[))] _[T]_[is][given][by] 

**==> picture [221 x 42] intentionally omitted <==**

Here we used the computation (3.5). Hence, _p_ is a critical point iff it satisfies 

**==> picture [345 x 69] intentionally omitted <==**

By (3.12) we are outside of the weak diagonal set, and in particular _P_ = 0. Since _{γ_ ̇ ( _s_ 2) _, v_ 2 _, v_ 2 _[⊥][}]_[is][an][orthonormal][basis,][by][(3.10)][and][(3.11)] _[P]_[is][parallel] to _γ_ ̇ ( _s_ 1). So _πs_ 1 _,s_ 2( _p_ ) = ~~(~~ ~~_s_~~ 1 _,_ ~~_s_~~ 2), and in particular _⟨P, γ_ ̇ ( _s_ 2) _⟩̸_ = 0. Hence, by (3.9) cos( _θ_ 2) = 0, and thus _θ_ 2 = _±π/_ 2 and _v_ 2 = _±b_ 2( _s_ 2). 

Let _p_ = ~~(~~ ~~_s_~~ 1 _,_ ~~_s_~~ 2 _, π/_ 2), the other case will be treated analogously. Now, we are going to compute the Morse index of _πs_ 1 at _p_ . Let us consider the implicit equation 

**==> picture [95 x 16] intentionally omitted <==**

Since _F_[[0]] and _Q_ intersect stratum transversely and _p_ is a critical point of _πs_ 1, it holds that _∂s_ 1 _F_ 2[[0]][(] _[p]_[)] _[ ̸]_[= 0.] 

So we can, by the Implicit function theorem, describe the Hessian matrix _H_ ˜︂[ _πs_ 1]( _p_ ). Here the tilde describes that the Hessian matrix is with respect to the flat metric _⟨·_[˜︃] _, ·⟩_ on R _/T_ Z _× S_[1] . Thus, we obtain 

**==> picture [265 x 34] intentionally omitted <==**

In order to compute the sign of the det( _H_[˜︂] [ _πs_ 1]( _p_ )), we can ignore the fraction before _H_[˜︂] [ _πs_ 1]( _p_ ). 

24 

Let us compute 

**==> picture [324 x 103] intentionally omitted <==**

**==> picture [313 x 74] intentionally omitted <==**

**==> picture [160 x 53] intentionally omitted <==**

Hence, 

det( _H_[˜︂] [ _πs_ 1]( _p_ )) = _−κ_ ~~(~~ ~~_s_~~ 2)[2] _⟨P, γ_ ̇ ~~(~~ ~~_s_~~ 2) _⟩_[2] _<_ 0 

due to our generic assumptions on _K_ . Thus the Morse index of _πs_ 1 at _p_ is equal to 1. 

Since the fibers are compact, _πs_ 1 is proper. _πs_ 1 is also surjective. 

It remains to verify that the condition ( _iii._ ) from Definition 60. But _N_[ˆ︂] _K,_ 0 is a codim 0 submanifold of (R _/T_ Z _× S_[1] ) _×_ R _/T_ Z. Hence from the existence of a collar neighbourhood near any critical point _p ∈_ ( _F_[[0]] ) _[−]_[1] ( _Q_ 1) we obtain that for any sequence of points _pj ∈_ ( _F_[[0]] ) _[−]_[1] ( _Q_ ) converging to _p_ it holds 

**==> picture [312 x 22] intentionally omitted <==**

The lemma follows. 

_Remark_ 64 _._ Now, we would like to depict _NK,_ 0. However, the author finds it easier to visualize, instead of _NK,_ 0, rather its certain perturbation: _NK,ε_ . 

**Definition 65.** _Let ε ∈_ [0 _, εgood_ ] _and_ ~~(~~ ~~_s_~~ 1 _,_ ~~_s_~~ 2) _be a_ ~~_s_~~ 2 _-special pair. Then we put NK,ε_ := ( _F_[˜︁][[] _[ε]_[]] ) _[−]_[1] ( _Q_ ) _, where F_ ˜︁ [ _ε_ ] = ( _F_ 2[[0]] + _ε, Id, Id_ ) _and Q_ = [0 _, ∞_ ) _× W_ ( _s_ 1 _,s_ 2) _(note that F_ 2[[0]][+] _[ ε]_[ =] _[ ⟨][P]_[+] _[ εv]_[2] _[, v]_[2] _[⟩][).]_ 

_An analogous statement also holds for_ ~~_s_~~ 1 _-special pairs._ 

_Remark_ 66 _._ Let _ε >_ 0 be small and ~~(~~ ~~_s_~~ 1 _,_ ~~_s_~~ 2) be a ~~_s_~~ 2-special pair. Then by Stability Lemma 31 and Lemma 59 _NK,_ 0 is isotopic to _NK,ε_ . By Stability Lemma 31 one can show that _πs_ 1 : _NK,ε →_ ~~(~~ ~~_s_~~ 1 _−δK,_ ~~_s_~~ 1+ _δK_ ) is also broken fibration with precisely two critical points. The critical points will be the (transversely cut out) solutions of the system 

**==> picture [314 x 15] intentionally omitted <==**

25 

Geometrically, the critical points will correspond to the intersections of the piece of the knot _K|_ ( _s_ 1 _−δK ,s_ 1+ _δK_ )[with][the][lines] 

**==> picture [169 x 13] intentionally omitted <==**

where _s_ 2 _∈_ ~~(~~ ~~_s_~~ 2 _− δK,_ ~~_s_~~ 2 + _δK_ ). 

Also, by the Implicit function theorem applied to (3.13), one can show _πs_ 1 will now have no distinct critical values. 

_Remark_ 67 _._ Let _ε >_ 0 be small and ~~(~~ ~~_s_~~ 1 _,_ ~~_s_~~ 2) be a ~~_s_~~ 2-special pair. We would like to present several visualizations of _NK,ε_ . 

Let us shrink the radius _ε_ of _TK,ε_ to 0 in a neighborhood of _γ_ ~~(~~ ~~_s_~~ 1). Hence on ~~(~~ ~~_s_~~ 1 _− δK,_ ~~_s_~~ 1 + _δK_ ) the torus _TK,ε_ will become _TK,_ 0 = _K_ , see Figure 3.3. So _NK,ε_ represents the set of chords from _TK,_ 0 _|_ ( _s_ 1 _−δK ,s_ 1+ _δK_ )[to] _[T] K,ε[|]_ ( _s_ 2 _−δK ,s_ 2+ _δK_ )[that][are] outward-pointing in their endpoints. 

Next, the first indication that the function _πs_ 1 consists of saddle-type critical points can be seen in Figure 3.4. 

The standard R[3] is not suited for the visualization of the whole _N_ . For _K,ε_ this, will rather use R _/T_ Z _×_ R _/T_ Z _× S_[1] , see Figure 3.5. 

It is worth recalling that all boundary components shown in Figure 3.5 are not the real boundary components of _NK,ε_ . In other words, in Figure 3.5, we also draw fake boundary components, which come from the fact that we restricted the _s_ -coordinates to _W_ ( _s_ 1 _,s_ 2)[.][Fake][boundary][components][(of] _[N] K,ε_[,][or][more][precisely] of _NK,_ 0) will tell us, how _NK,_ 0 _×_ [0 _,_ 1] is glued to the rest of _MK,_ 0. It turns out that _NK,ε_ is homeomorphic to the solid torus _S_[1] _×D_[2] . Moreover, this homeomorphism maps the fake boundary to a thin strip on _S_[1] _× ∂D_[2] that is homotopic to the concatenation of meridian and longitude (given by Seifert framing). See Figure 3.6. 

**==> picture [143 x 133] intentionally omitted <==**

Figure 3.3: A neighborhood of ~~_s_~~ 2-strongly special pair in R[3] . The red points represent the ~~_s_~~ 2-strongly special pair ~~(~~ ~~_s_~~ 2 _,_ ~~_s_~~ 1) _._ The blue curves describe the knot _K_ , where the vertical part is viewed as _TK,_ 0. Around _γ_ ~~(~~ ~~_s_~~ 2) the torus _TK,ε_ is depicted in green. 

26 

**==> picture [159 x 163] intentionally omitted <==**

**==> picture [159 x 168] intentionally omitted <==**

**==> picture [159 x 171] intentionally omitted <==**

Figure 3.4: A visualization in R[3] of fibers _πs[−]_ 1[1][(] _[s]_[1][)] _[⊂][N][K,ε]_[as] _[s]_[1][pass][a][singular] fiber (the middle figure). The blue lines represent the torus _TK,_ 0 of zero radius, which is parametrized by _s_ 1. Next, the orange sets describe the sets of all ends of outward-pointing chords that start in the red points. Orange sets are parametrized by ( _s_ 2 _, θ_ 2)-coordinates. 

27 

**==> picture [175 x 186] intentionally omitted <==**

**----- Start of picture text -----**<br>
s 2<br>s 1 2 π<br>θ 2<br>0<br>**----- End of picture text -----**<br>


Figure 3.5: A visualization of _NK,ε_ in coordinates ( _s_ 1 _, s_ 2 _, θ_ 2). The blue dots represent two critical points of _πs_ 1 (Lemma 62). 

**==> picture [411 x 172] intentionally omitted <==**

**----- Start of picture text -----**<br>
∼<br>=<br>**----- End of picture text -----**<br>


Figure 3.6: The homeomorphism between _NK,ε_ and _S_[1] _× D_[2] . On the left, the red surface describes the fake boundary, and on the right, we see the image of the fake boundary. The image is homotopic to the concatenation of the meridian and the longitude. 

28 

The following result is probably originally due to T. Tsuboi, [Lok18]. 

**Theorem 68.** _If a knot has an empty set of special pairs, then the knot is an unknot._ 

**Corollary 69.** _Let K be generic and ε ≥_ 0 _be small. If H_ 1 _[sing]_ ( _MK,ε|d_ ˜︁( _s_ 1 _,s_ 2) _>δK_ ; Z) _[∼]_ = Z _, then K is an unknot._ 

_Proof._ Let us compute 

**==> picture [397 x 86] intentionally omitted <==**

where the step (1) follows from Theorem 50 and in the step (2) we applied the following two deformations retracts. 

First, we deformation retract each _NK,_ 0 _× {t} ∈ NK,_ 0 _×_ [ _−_ 1 _,_ 1] to the fake boundary of the whole product. To obtain such a deformation retract, we identify each _NK,_ 0 _× {t}[∼]_ = _NK,_ 0 with _S_[1] _× D_[2] by the (orientation preserving) homeomorphism from Remark 67. Then the deformation retraction of the solid torus is straightforward. 

Second, by Lemma 58, the remaining space is diffeomorphic to the product of _SK_ and the square. So the radial shrinking of the square will give us the second deformation retraction. Last, we can potentially slightly extend the space closer to ∆0. 

Hence, we showed that _H_ 1 _[sing]_ counts the special points. Thus, we can apply Theorem 68. 

29 

⎛ ⎜ ⎜ ⎜ ⎝ 

**Conjecture 70.** _Let ε ∈_ (0 _, εdiag_ ) _. Let M_[ˆ︂] _K,ε denotes the restriction of MK,ε to the set {_ ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] _| ε ≤ d_[˜︁] ( _s_ 1 _, s_ 2) _≤ δK}. Then the following holds_ 

- ( _i._ ) _M_ ˆ︂ _K,ε is a_ 4 _-manifold with corners and the projection πs_ 1 : _M_[ˆ︂] _K,ε →_ R _/T_ Z _induce a locally trivial fibration. In more detail, M_[ˆ︂] _K,ε_ = ( _F_[[] _[ε]_[]] ) _[−]_[1] ( _Q_ ) _, where F_[[] _[ε]_[]] = ( _F_ 1[[] _[ε]_[]] _[, F]_ 2[ [] _[ε]_[]] _[, F][ dist]_[)] _[and][Q]_[ =] [0 _, ∞_ ) _×_ [0 _, ∞_ ) _× {_ [ _−δK, −ε_ ] _∪_ [ _ε, δK_ ] _}._ 

- ( _ii._ ) _Let_ ~~_s_~~ 1 _,_ ~~_s_~~ 2 _∈_ R _/T_ Z _be such that_ ~~_s_~~ 1 = ~~_s_~~ 2 _, i.e._ ( ~~_s_~~ 1 _,_ ~~_s_~~ 2) _is a diagonal pair. Then πs[−]_ 1[1] ~~[(]~~ ~~_s_~~ 1) _is a_ 3 _-manifold with corners and the projection πs_ 2 : _πs[−]_ 1[1] ~~[(]~~ ~~_s_~~ 1) _→_ ~~(~~ ~~_s_~~ 2 _− δK,_ ~~_s_~~ 2 _− ε_ ) _∪_ ~~(~~ ~~_s_~~ 2 + _ε,_ ~~_s_~~ 2 + _δK_ ) _induce a broken fibration. In more detail, πs[−]_ 1[1] ~~[(]~~ ~~_s_~~ 1) = ( _F_[˜︁][[] _[ε]_[]] ) _[−]_[1] ( _Q_[˜︁] ) _, where_ 

**==> picture [170 x 19] intentionally omitted <==**

_and_ 

**==> picture [306 x 15] intentionally omitted <==**

_And the only critical points of πs_ 2 _are two critical points in_ ( _F_[˜︁][[] _[ε]_[]] ) _[−]_[1] ( _Q_[˜︁] 1) _, each of them has Morse index equal to_ 1 _._ 

_Remark_ 71 _._ The geometric picture of Conjecture 70 will be described in Figure 3.10. 

_Partial proof._ Recall from the proof of Theorem 50 that the matrix _dF_ 1[[] _[ε]_[]] _[, dF]_ 2[ [] _[ε]_[]] _T_ (︂ )︂ (at some general point of (R _/T_ Z _× S_[1] )[2] ) is given by 

**==> picture [552 x 57] intentionally omitted <==**

We will denote the elements of the matrix by _{ai,j}i,j._ 

_Ad_ ( _i._ ) _:_ 

First, we would like to verify the stratum transversality of _F_[[] _[ε]_[]] and _Q_ and then apply Theorem 23. 

Let us show that _F_[[] _[ε]_[]] ⋔ _Q_ 1. We need to show that 

**==> picture [95 x 16] intentionally omitted <==**

for any _p ∈_ ( _F_[[] _[ε]_[]] ) _[−]_[1] ( _Q_ 1). Assume for contradiction that this is not true. Then by _a_ 3 _,_ 1 and _a_ 4 _,_ 1 we obtain that _v_ 1 = _±v_ 2. However, we also know that _F_ 1[[] _[ε]_[]][(] _[p]_[) = 0] and _F_ 1[[] _[ε]_[]][(] _[p]_[)] _[ >]_[ 0,][which][is][a][contradiction.] Similarly, we can show that _F_[[] _[ε]_[]] ⋔ _Q_ 2. To show that _F_[[] _[ε]_[]] ⋔ _Q_ 3 is immediate, since at each point it holds that the matrix _dF[dist]_ is given by (1 _,_ 0 _,_ 1 _,_ 0). 

Let us show that _F_[[] _[ε]_[]] ⋔ _Q_ 1 _,_ 2. It will be enough to show that for any _p ∈_ ( _F_[[] _[ε]_[]] ) _[−]_[1] ( _Q_ 1 _,_ 2) it holds that at least one of _a_ 2 _,_ 1 and _a_ 4 _,_ 1 is non-zero. Assume 

30 

for contradiction, that _a_ 2 _,_ 1 = _a_ 4 _,_ 1 = 0. We also know that _F_ 1[[] _[ε]_[]][(] _[p]_[) = 0.][Hence, ge-] ometrically the cylinder _Cπs_ 1 ( _p_ ) _,ε_ is tangent to the circle Γ _ε|πs_ 2 ( _p_ ). Then by Lemma 45 ( _i._ ) we obtain that _ε < d_[˜︁] ( _πs_ 1( _p_ ) _, πs_ 2( _p_ )) _< δK_ . Which is a contradiction, since _d_ ˜︁( _πs_ 1( _p_ ) _, πs_ 2( _p_ )) is equal to _ε_ or _δK_ . 

Similarly, we can show that _F_[[] _[ε]_[]] ⋔ _Q_ 2 _,_ 3. To show that _F_[[] _[ε]_[]] ⋔ _Q_ is immediate. It remains to show that _F_[[] _[ε]_[]] ⋔ _Q_ 1 _,_ 2 and _F_[[] _[ε]_[]] ⋔ _Q_ 1 _,_ 2 _,_ 3. Here we _conjecture_ that 

**==> picture [268 x 31] intentionally omitted <==**

at any point _p ∈_ ( _F_[[] _[ε]_[]] ) _[−]_[1] ( _Q_ 1 _,_ 2 _∪Q_ 1 _,_ 2 _,_ 3). See also the discussions in Remark 72 and Example 89. 

Hence, with the assumption (3 _._ 14), we verified that _F_[[] _[ε]_[]] is stratum transverse to _Q_ . In fact, with the assumption (3 _._ 14), we also showed that _πs_ 1 : _M_[ˆ︂] _K,ε →_ R _/T_ Z is a submersion on each stratum. Moreover, _πs_ 1 is proper and surjective. So we can apply Ehresmann’s Theorem 29, which finishes the part ( _i._ ). 

_Ad_ ( _ii._ ) _:_ 

Let us assume (3 _._ 14). 

Then, in fact, we showed already in part ( _i._ ) that also _πs[−]_ 1[1] ~~[(]~~ ~~_s_~~ 1) is a 3-manifold with corners. 

We are going to inspect the critical points of _πs_ 2 : _πs[−]_ 1[1] ~~[(]~~ ~~_s_~~ 1) _→_ ~~(~~ ~~_s_~~ 2 _− δK,_ ~~_s_~~ 2 _− ε_ ) _∪_ ~~(~~ ~~_s_~~ 2 + _ε,_ ~~_s_~~ 2 + _δK_ ). 

Let _p ∈_ ( _F_[˜︁][[] _[ε]_[]] ) _[−]_[1] ( _Q_ 2). Similar to the proof of Lemma 62, _p_ is a critical point of _πs_ 2 iff 

**==> picture [109 x 13] intentionally omitted <==**

By the definition of _p_ it holds that _F_ 2[[] _[ε]_[]] _[|] πs[−]_ 1[1][(] _s_ 1)[(] _[p]_[)][=][0.][Hence][geometrically,][the] cylinder _Cπs_ 2 ( _p_ ) _,ε_ is tangent to the circle Γ _ε_ ~~_|_~~ _s_ 1[.] Then by Lemma 45 ( _ii._ ) (see Figure 3.2 (bottom)) we obtain that _F_ 1[[] _[ε]_[]][(] _[p]_[)] _[<]_[0] _[,]_[which][is][a][contradiction,][since] _F_ 1[[] _[ε]_[]][(] _[p]_[)] _[ <]_[ 0] _[.]_[So][there][is][no][critical][point][on][(] _[F]_[ ˜︁][ [] _[ε]_[]][)] _[−]_[1][(] _[Q]_[2][).] 

Let _p ∈_ ( _F_[˜︁][[] _[ε]_[]] ) _[−]_[1] ( _Q_ 1). Then _p_ is a critical point iff 

**==> picture [109 x 12] intentionally omitted <==**

By the definition of _p_ it holds that _F_ 1[[] _[ε]_[]] _[|] πs[−]_ 1[1][(] _s_ 1)[(] _[p]_[)][=][0.][Hence][geometrically,][the] cylinder ~~_C_~~ _s_ 1 _,ε_[is][tangent][to][the][circle][Γ] _ε[|] πs_ 2 ( _p_ )[.][Then][by][Lemma][45][(] _[i.]_[)][there][are] precisely two such critical points. 

Let _p_ = ( _θ_ 1 _,_ ~~_s_~~ 2 _, θ_ 2) be one of these critical points of _πs_ 2. We would like to compute its Morse index. Let us consider an implicit equation 

**==> picture [128 x 20] intentionally omitted <==**

Since _F_[˜︁][[] _[ε]_[]] ⋔ _Q_ 1, it holds that _∂s_ 2 _F_ 1[[] _[ε]_[]] _[|] πs[−]_ 1[1][(] _s_ 1)[(] _[p]_[)] _[ ̸]_[= 0.] 

So we can, similarly to the proof of Lemma 62, apply the Implicit function theorem and describe the Hessian matrix _H_[˜︂] [ _πs_ 2]( _p_ ) as 

**==> picture [303 x 40] intentionally omitted <==**

31 

In order to compute the sign of the det( _H_[˜︂] [ _πs_ 2]( _p_ )), we can ignore the fraction before _H_[˜︂] [ _πs_ 2]( _p_ ). Hence, we are left with the matrix 

**==> picture [155 x 31] intentionally omitted <==**

Next, since _F_ 1[[] _[ε]_[]] _[|] πs[−]_ 1[1][(] _s_ 1)[(] _[p]_[)][=][0,][we][obtain][that] _[−⟨][P]_[+] _[ εv]_[2] _[, v]_[1] _[⟩]_[=] _[−][ε][⟨][v]_[1] _[, v]_[1] _[⟩]_[=] _−ε <_ 0. Finally, from the geometric picture of Lemma 45 ( _ii._ ), we see that _−ε⟨v_ 1 _, v_ 2 _⟩ >_ 0. 

Hence all together, det( _H_[˜︂] [ _πs_ 2]( _p_ )) _<_ 0. And thus, the Morse index of _πs_ 2 at _p_ is equal to 1. 

Now, it is straightforward that there are no other critical points of _πs_ 2 on ( _F_[˜︁][[] _[ε]_[]] ) _[−]_[1] ( _Q∪Q_ 1 _,_ 2). Consequently, _πs_ 2 : _πs[−]_ 1[1] ~~[(]~~ ~~_s_~~ 1) _→_ ( ~~_s_~~ 2 _−δK,_ ~~_s_~~ 2 _−ε_ ) _∪_ ~~(~~ ~~_s_~~ 2 + _ε,_ ~~_s_~~ 2 + _δK_ ) induce a broken fibration. 

_Remark_ 72 _._ The reason why we did not prove fully the Conjecture 70 is that it is quite difficult to solve 

**==> picture [94 x 16] intentionally omitted <==**

on the set _{_ ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] _| ε ≤ d_[˜︁] ( _s_ 1 _, s_ 2) _≤ δK}_ . Unfortunately, now we cannot shrink _ε →_ 0 and apply the same trick as in Lemma 58. 

Let us aim for a weaker result - to show that close to the diagonal ∆ _ε_ the system _F_ 1[[] _[ε]_[]] = 0 _∧ F_ 2[[] _[ε]_[]] = 0 has exactly 4 real solutions. However, after tangent half-angle substitutions, we will need to find the intersections of two biquadratics. Such a problem is expected to have eight complex solutions and does not have a solution in radicals. Moreover, one can show that the geometric description of _F_ 1[[] _[ε]_[]] = 0 _∧ F_ 2[[] _[ε]_[]] = 0 leads to two biquadratics. In other words, independently of the choice of parametrization, we have to study intersections of two biquadratics. Still, some techniques from Enumerative real algebraic geometry might lead to a proof of the existence of four distinct real solutions. See also Example 89. 

32 

## **3.4 Closer look on the** _ε_ **-diagonal** 

In this section, we inspect the singular behavior of _MK,ε_ near the diagonal ∆ _ε_ . In other words, how, or even whether, the outward-pointing chords can approach the constant chords. This turns out to be a local question about the geometry of _TK,ε_ near points with non-positive Gaussian curvature. After slightly laborious computation, we conclude that for _ε >_ 0 small, _MK,ε_ looks near ∆ _ε_ roughly as a stratified fiber bundle over a half-torus with cuspidal fibers. 

_Remark_ 73 _._ We assume that the reader is familiar with basic notions from the geometry of surfaces, such as the first and the second fundamental forms, principal directions, and Gaussian curvature. For more on this theory, see, for example [CP16]. 

_Convention_ 74 _._ Let _M ⊂_ R[3] be a closed oriented surface. Then there is the unique compact 3-submanifold _M_[˜︂] _⊂_ R[3] such that _∂M_[˜︂] = _M_ . This gives us a canonical outward-pointing normal vector field _N[out]_ on _M_ . Let _p ∈ M_ be such that the principal curvatures _κM_ ( _p_ ) _≥ κm_ ( _p_ ) are not equal. Then we choose the (normalized) principal directions _wM_ ( _p_ ) _, wm_ ( _p_ ) such that 

**==> picture [122 x 16] intentionally omitted <==**

**Lemma 75.** _The Gaussian curvature κG of TK,ε at p_ = ( _s, θ_ ) _is given by_ 

**==> picture [115 x 27] intentionally omitted <==**

_where d_ = (1 _− ε_ cos( _θ_ ) _κ_ ( _s_ )) _._ 

_Also, the principal curvatures κM , κm and the (normalized) principal directions wM , wm are given by_ 

**==> picture [276 x 26] intentionally omitted <==**

_and_ 

**==> picture [177 x 14] intentionally omitted <==**

_Proof._ The strategy of the computation is the following. First, we need to know the first and the second fundamental forms with respect to the basis _{∂s, ∂θ}_ . We denote the first and second fundamental forms as _G_ and _H_ , respectively. Then, we obtain the Gaussian curvature and the mean curvature _κmean_ at _p ∈ TK_ as 

**==> picture [271 x 29] intentionally omitted <==**

Then, the principal curvatures are determined as 

**==> picture [305 x 19] intentionally omitted <==**

From which we finally compute the principal directions as the eigenvectors of _G[−]_[1] _H_ . 

Let us compute _G_ . We recall relations (3 _._ 3), i.e. 

**==> picture [124 x 32] intentionally omitted <==**

33 

Thus, we obtain that 

**==> picture [280 x 31] intentionally omitted <==**

Now, we continue with the computation of _H_ . It holds that 

**==> picture [319 x 58] intentionally omitted <==**

Hence, we compute 

**==> picture [423 x 19] intentionally omitted <==**

**==> picture [180 x 30] intentionally omitted <==**

**==> picture [31 x 13] intentionally omitted <==**

By Remark 40 we know that _v_ are the unital normal vectors to _TK,ε_ and thus the second fundamental form is given as the dot product of the second derivatives from (3.16) with _v_ . Therefore, _H_ is given as 

**==> picture [173 x 31] intentionally omitted <==**

Then _κmean_ ( _p_ ) =[1] _[−]_[2] _[εκ] −_[(] 2 _[s] εd_[)][ cos][(] _[θ]_[)] and the rest of the computation follows. 

_Remark_ 76 _. κG_ is negative for _θ ∈_ ( _−π/_ 2 _, π/_ 2). 

̇ _Remark_ 77 _. wM_ = _−γ_ ( _s_ ) and _wm_ = _v[⊥]_ . And in particular, it holds that _wM × wm_ = _v_ . 

_Notation_ 78 _._ Let _f_ : R[2] _x,y[→]_[R][be][a][smooth][function][and] _[f]_[(] _[x, y]_[) = 0][an][implicit] equation which is locally solved by the function _y_ ( _x_ ). Then, we will use the following notation for the partial and implicit derivatives of _f_ at the point ( _x, y_ ( _x_ )). That is 

**==> picture [184 x 14] intentionally omitted <==**

and 

**==> picture [139 x 26] intentionally omitted <==**

**Definition 79.** _Let wM , wm be two orthogonal vectors in_ R[2] _. Let Q be a quadrant that is spanned by axes ⟨wM ⟩, ⟨wm⟩ and let c_ : [0 _, T_ ] _→ Q be a smooth curve such that c_ (0) = (0 _,_ 0) _and c_ ((0 _, T_ ]) _⊂ Int_ ( _Q_ ) _. c is called wM_ _**-attracted** if there is δ_ ; 0 _< δ < T, such that c_ ((0 _, δ_ ]) _is strictly concave graph over the axis ⟨wM ⟩ (here the positive direction of the functions over ⟨wM ⟩ is given by the half-axis ⟨wm⟩∩ Q)._ 

_Analogously for wm-attracted curves._ 

34 

**Definition/Lemma 80.** _Let M be a closed oriented surface and let p ∈ M such that κG_ ( _p_ ) _<_ 0 _. Let wM , wm be (normalized) principal directions wM , wm of principal curvatures κM > κm (recall Convention 74). We also consider the two planes spanned by the normal vector to M at p together with wM or wm. Then, these planes split a neighbourhood of p in M into four sectors {Qj}j∈{_ 1 _,...,_ 4 _}, see Figure 3.7. Let also cj be the unique curves in Qj given by the intersection of the affine plane TpM and M and defined in a small neighbourhood of p._ 

_Now, we consider Qj for any j. If the curve cj is wM -attracted in TpM for some δ >_ 0 _, then for t ∈_ [0 _, δ_ ] _the chords p, cj_ ( _t_ ) _are outward-pointing in the sense of Definition 42 and there is a smooth curve c_ ˆ︁ _j_ : [0 _, δ_ ] _→ Qj such that_ 

**==> picture [73 x 15] intentionally omitted <==**

**==> picture [152 x 15] intentionally omitted <==**

( _iii._ ) _the chords p,_ ˆ︁ _cj_ ( _t_ ) _are outward-pointing._ 

_See also Figure 3.7._ 

_The analogous statement holds in the wm-attracted case, only then the chords need to be inward-pointing on both ends. We will call such a quadrant Qj_ _**outward** or_ _**inward pointing** ._ 

_Let Q_[˜︂] _j be the quadrants of TpM that naturally correspond to the quadrants Qj; see also Figure 3.7. Then ρ[j] a[, ρ][j] b[be][the][following][functions][on] Q_[˜︂] _j. For j_ = 1 _,_ 3 _, ρ[j] a[is]_[+1] _[and][else][−]_[1] _[.][For][j]_[= 1] _[,]_[ 2] _[,][ρ][j] b[is]_[+1] _[and][else][−]_[1] _[.] If at the point p holds that_ 

**==> picture [438 x 44] intentionally omitted <==**

_then Qj is outward-pointing. If the inequality is opposite, Qj is inward-pointing._ 

**==> picture [412 x 256] intentionally omitted <==**

**----- Start of picture text -----**<br>
Q 4<br>wM<br>c 4<br>Q 1 ˆ︁<br>c 4<br>wm<br>Q 4<br>p<br>Q 2<br>Q 3<br>p<br>Q ˜︂4 ⊂ TpM<br>Figure 3.7: On the left: the splitting of the neighbourhood of p in M onto<br>quadrants Qj using principal directions wM , wm . By our convention, wM × wm is<br>equal to the outward-pointing normal vector. On the right: wM -attracted curve<br>c 4 together with possible c ˆ︁4. Observe also the quadrant Q [˜︂] 4 corresponding to Q 4.<br>**----- End of picture text -----**<br>


35 

_Non-Example_ 81 _._ Let _M_ be a hyperbolic paraboloid. Then still _κG_ ( _p_ ) _<_ 0. However, since _M_ is a ruled surface, the curves _cj_ are neither _wM_ - nor _wm_ - attracted. In particular, there are no curves _c_ ˆ︁ _j_ that satisfy the conditions ( _i._ ) _−_ ( _iii._ ) from Lemma 80. 

_Proof._ Let _cj_ is _wM_ -attracted, then for each _t ∈_ (0 _, δ_ ] chords _p, cj_ ( _t_ ) are outwardpointing. Indeed, _p, cj_ ( _t_ ) lie in _TpM_ , so they are tangent to _M_ at _p_ . At _cj_ ( _t_ ) they are also outward-pointing, since _cj_ is _wM_ -attracted and _κM > κm_ , see Figure 3.8. Now, let us we make a small _C_[0] perturbation _c_ ˜︁ _j_ of _cj_ inside _Q_[˜︁] _j_ such that _cj_ (0) = _c_ ˜︁ _j_ . If the perturbation is small enough then the lift (=: _c_ ˆ︁ _j_ ) of _c_ ˜︁ _j_ to _Qj_ has a property that the chords _p,_ ˆ︁ _cj_ ( _t_ ) are outward-pointing in _c_ ˆ︁ _j_ ( _t_ ). If we perturb _cj_ such that _c_ ˜︁ _j ⊂ Q_[˜︁] _j_ lies in the convex hull given by _cj_ and _⟨wM ⟩∩ Q_[˜︁] _j_ , the the lift _c_ ˆ︁ _j_ satisfies the property ( _iii._ ). In Lemma 82 we will construct a special example of smooth _c_ ˆ︁ _j_ such that the chords _p,_ ˆ︁ _cj_ ( _t_ ) are tangent to _M_ at _c_ ˆ︁ _j_ ( _t_ ). 

**==> picture [164 x 164] intentionally omitted <==**

**----- Start of picture text -----**<br>
Q 4<br>c 4<br>c 4( t )<br>p<br>Q ˜︂4 ⊂ TpM<br>**----- End of picture text -----**<br>


Figure 3.8: In green a chord _p, c_ 4( _t_ ) that is outward-point. 

Now, the inequality (3.17). After rigid transformations of R[3] we can assume that _M_ is locally a graph of a function _f_ : R[2] _x,y[→]_[R][such][that] 

**==> picture [212 x 13] intentionally omitted <==**

**==> picture [134 x 14] intentionally omitted <==**

**==> picture [244 x 15] intentionally omitted <==**

We are going to study the set _f_ ( _x, y_ ) = 0. By the Morse Lemma [Hir97] there is a coordinate change _φ_ : R[2] _x,y[→]_[R][2] _x,y_[, which is defined in a small neighbourhood] ˜︁ ˜︁ of _q_ and satisfy that 

**==> picture [266 x 16] intentionally omitted <==**

Since _q_ is a nondegenerate critical point, _f_ ( _x, y_ ) = 0 is diffeomorphic to a cone, and each of the two smooth components can be written as a graph of _y_ ( _x_ ). In particular, ( _x, y_ ( _x_ )) will lie inside _Q_ 1 and _Q_ 3 or _Q_ 2 and _Q_ 4. Note that we can see immediately the slope _y_ ̇(0) from the Morse Lemma, but for further calculations, 

36 

it will be illustrative to make the following computation 

**==> picture [172 x 133] intentionally omitted <==**

where we used in step (1) implicit differentiation and in step (2) the L _[′]_ Hospital rule. We applied in step (3) implicit differentiation and in step the assumptions on _f_ . We also recall that we used Notation 78 for various differentiating. Hence, as expected, we obtain that 

**==> picture [297 x 34] intentionally omitted <==**

where _ρa_ = sgn( ̇ _y_ (0)). 

In the following, we write for simplicity _f_ ( _x, y_ ( _x_ )) as _f_ . Also, we would like to denote partial derivatives as subscripts, for example, _∂x∂yf_ = _fxy_ . We are interested in the sign of _y_ ¨(0), so we can compute 

**==> picture [481 x 264] intentionally omitted <==**

In equality (1) we used implicit differentiation (and the chain rule), and in (2) we applied implicit differentiation. For (3), we applied the L _[′]_ Hospital rule twice. In (4) we got rid of _O_ -terms; for their closer description, see below. This was possible since _fx, fy, fxy →_ 0 as _x →_ 0, lim _x→_ 0 _fx/fy ∈_ R _\{_ 0 _}_ , and _fyy_[2] _[f] x_[ 2] _[/f] y_[ 2] _[−][f][yy][f][xx][>]_[ 0.] And in (5) we cancelled _fyy_ . 

37 

For completeness, we write the description of the numerator and the denominator in step (3). So the numerator is of the form 

**==> picture [433 x 91] intentionally omitted <==**

and the denominator is equal to 

**==> picture [285 x 53] intentionally omitted <==**

Hence, by relation (3.18) and assumptions on _f_ at _q_ , we obtain 

**==> picture [507 x 200] intentionally omitted <==**

Now, it remains to relate _fxxx, fxxy, fyyx, fyyy_ at _q_ with the directional derivatives _∇wM κM_ , etc. It is not hard to see that at _q_ it holds _fyy_ = _κM_ , _∂x_ = _wM_ , _fyy_ = _κm_ , _∂y_ = _wm_ . However, the quantity _∇wmκM_ ( _q_ ) depends pointwise only on _wM_ ; for _κM_ , we need to know the values in a neighborhood _Uq_ . 

Hence, let us first find the descriptions of _H_ and _G[−]_[1] around _q_ at graphical coordinates ( _x, y_ ). 

Since 

**==> picture [266 x 31] intentionally omitted <==**

we have that 

**==> picture [303 x 32] intentionally omitted <==**

Also at any _r_ = ( _x, y, f_ ( _x, y_ )) we choose a normal vector _Nr_ to the graph of _f_ as 

**==> picture [117 x 32] intentionally omitted <==**

38 

Then 

**==> picture [371 x 94] intentionally omitted <==**

Next, 

and hence 

**==> picture [213 x 26] intentionally omitted <==**

We can also compute that 

**==> picture [311 x 52] intentionally omitted <==**

and similarly 

**==> picture [132 x 25] intentionally omitted <==**

Now we compute 

**==> picture [344 x 153] intentionally omitted <==**

where in (1) we used the assumption that _fxx >_ 0 _> fyy_ . 

We obtain similarly that _∇wmκM_ ( _q_ ) = _fxxy, ∇wM κm_ ( _q_ ) = _fyyx, ∇wmκm_ ( _q_ ) = _fyyy_ . This concludes the lemma. 

**Lemma 82.** _Assume that the quadrant Qj ⊂ M from Lemma 80 is outwardpointing. Then the curve c_ ˆ︁ _j_ ( _t_ ) _can be chosen such that the chords p,_ ˆ︁ _cj_ ( _t_ ) _are tangent to M at c_ ˆ︁ _j_ ( _t_ ) _. Moreover, the curves cj and c_ ˆ︁ _j have a common tangent line at p._ 

_The analogous statement holds for the inward-pointing case._ 

_Proof._ We will prove the outward-pointing case. As in the proof of Lemma 80, let us consider _M_ locally as a graph of _f_ ( _x, y_ ). 

Now we define two functions _F_ 1 _,p, F_ 2 _,p_ : _M →_ R which are similar to the functions from Definition 41. More precisely, at _r_ = ( _x, y, f_ ( _x, y_ )) we put 

**==> picture [328 x 13] intentionally omitted <==**

39 

Recall that _p_ = (0 _,_ 0 _,_ 0) and _Nr_ = ( _fx_[2][+] _[f] y_[ 2][+1)] _[−]_[1] _[/]_[2][(] _[−][f][x][,][ −][f][y][,]_[ 1)] _[T]_[.][Note that now,] unlike in Definition 41, _F_ 1 _,p_ and _F_ 2 _,p_ have fixed variables in the “start-point.” Hence, in graphical coordinates 

**==> picture [247 x 30] intentionally omitted <==**

As in the proof of Lemma 80, we can write around _q_ = (0 _,_ 0) _y_ as the unique function of _x_ constrained to _F_ 1 _,p_ = 0 _∧ πx,y_ ( _Qj_ ). Such a function gives us _{qt_[1] _[}]_ and in particular 

**==> picture [121 x 35] intentionally omitted <==**

Now, in _πx,y_ ( _Qj_ ), we would like to write similarly _y_ as the locally unique function of _x_ constrained to _F_ 2 _,p_ = 0. Also along the set _{y_ = 0 _} ∩ πx,y_ ( _Qj_ ) it holds that _F_ 1 _,p ≤_ 0. Then, by the Intermediate value theorem and _wM_ -attraction of _cj_ , _y_ ( _x_ ) will contribute by a family of chords that are not only outward pointing in ( _x, y_ ( _x_ )), but also in _p_ . For this, it will be sufficient to show that at _p_ the functions _F_ 1 _,p_ and _F_ 2 _,p_ have the same value, the same Jacobi matrix, and, up to a multiple of _−_ 1, the same Hessian matrix. Note that this will, in particular, also imply that the curves _cj_ and _c_ ˆ︁ _j_ have a common tangent line at _p_ . 

First, by the choice of _f_ , it holds clearly that _F_ 1 _,p_ ( _q_ ) = 0 = _F_ 2 _,p_ ( _q_ ). Then, let us compute 

**==> picture [301 x 64] intentionally omitted <==**

Hence both Jacobi matrices vanish. Let us continue with 

**==> picture [277 x 15] intentionally omitted <==**

**==> picture [381 x 136] intentionally omitted <==**

where _{gi}i_ =1 _,...,_ 6 are some functions that are bounded in a small neighborhood of _q_ . Note that the blue terms are the only nonzero contributions to the Hessian matrix of _F_ 2 _,p_ at _q_ . In particular, _H_ [ _F_ 1 _,p_ ]( _q_ ) = _−H_ [ _F_ 2 _,p_ ]( _q_ ), and the lemma follows. 

**Lemma 83.** _Let M and p be as in Lemma 80. For i_ = 1 _,_ 2 _let Fi,p be the functions from (3.21). Then there is a small collar neighborhood Up[◦][of][p][in][M][such][that]_ 

**==> picture [93 x 13] intentionally omitted <==**

**==> picture [188 x 14] intentionally omitted <==**

40 

_Proof._ We consider the graphical coordinates ( _x, y, f_ ( _x, y_ )) as in Lemma 80. Then for each quadrant _Qj_ we can find the locally unique solution ( _x, y_ ( _x_ )) of _Fi,p_ ( _x, y_ ( _x_ )) = 0. We know that _∂xF_ ̇ _i,p_ ( _q_ ) = 0, where _q_ = (0 _,_ 0). Then one can show that the implicit derivative ( _∂xFi,p_ )( _q_ ) _̸_ = 0, since _κG_ ( _p_ ) _̸_ = 0. So on a small neighborhood of _q_ it holds that _∂xFi,p_ ( _q_ ) is strictly increasing or decreasing along ( _x, y_ ( _x_ )). 

**Thom’s first isotopy Lemma 84.** _[GM12, Mat12] Let Z be a Whitney stratified subset of a smooth manifold M and π_ : _M → N be a smooth map onto a smooth manifold N . Assume that π|Z is a proper surjection and π is a submersion on each stratum of Z. Then π|Z defines a locally trivial_ _**stratified fiber bundle** , i.e., for every x ∈ N there is an open neighborhood Ux in N and a strata preserving homeomorphism ψ_ : _Ux × π|Z[−]_[1][(] _[x]_[)] _[→][π][|][−] Z_[1][(] _[U][x]_[)] _[which][is][smooth][on][each][stratum] and π|Z ◦ ψ_ ( _u, v_ ) = _u for every_ ( _u, v_ ) _∈ Ux × π|Z[−]_[1][(] _[x]_[)] _[.]_ 

**Lemma 85.** _Let_ ( _M, g_ ) _be an oriented surface in_ (R[3] _, gEuc_ ) _with induced metric and p ∈ M with κG_ ( _p_ ) _<_ 0 _. Let us consider a neighborhood Up of p in M and the diagonal_ ∆ _Up ⊂ Up × Up. Next,_ ~~_ν_~~ _δ_ ~~(~~ ∆ _Up_ ) _⊂ M × M be a δ-radius closed tubular neighborhood induced by the normal bundle Ng×g_ (∆ _Up, Up × Up_ ) _. By M[out][−][out] we denote the set of outward-pointing chords_ ~~_ν_~~ _δ_ ~~(~~ ∆ _Up_ ) _⊂ M × M . Assume that each quadrant Qj of p is either outward- or inward-pointing. If Up and δ >_ 0 _are sufficiently small, then M[out][−][out] is_ codim 0 _Whitney stratified subset of_ ~~_ν_~~ _δ_ (∆ _Up_ ) _and_ 

_M[out][−][out] −−→πN_ ∆ _Up_ 

_is a locally trivial stratified fiber bundle. Here the projection πN is determined by the bundle projection in identification of_ ~~_ν_~~ _δ_ ~~(~~ ∆ _Up_ ) _with a disk subbundle of Ng×g_ (∆ _Up, Up × Up_ ) _._ 

_In particular, any generalized tangent space of πN[−]_[1][((] _[p, p]_[))] _[at]_[(] _[p, p]_[)] _[lies][in][the] span of wM_ ( _p_ ) _×−wM_ ( _p_ ) _and wm_ ( _p_ ) _×−wm_ ( _p_ ) _(for the definition of the generalized tangent space see Remark 34)._ 

_Proof._ For _i_ = 1 _,_ 2 let us consider functions _Fi_ ( _·, ·_ ) := _Fi,·_ ( _·_ ) : ~~_ν_~~ _δ_ ~~(~~ ∆ _Up_ ) _\_ ∆ _Up →_ R and put _F_ = ( _F_ 1 _, F_ 2). If _Up_ together with _ε >_ 0 are small, then by Lemma 83 _F_ is stratum transverse to [0 _, ∞_ )[2] . Hence, if there is at least one outward-pointing quadrant, then _F[−]_[1] ([0 _, ∞_ )[2] ) is a 4-manifold with corners. Then _M[out][−][out]_ = _F[−]_[1] ([0 _, ∞_ )[2] ) _∪_ ∆ _Up_ , so we can consider on _M[out][−][out]_ a stratification given by the canonical stratifications of the 4-manifold with corners _F[−]_[1] ([0 _, ∞_ )[2] ) and ∆ _Up_ . We would like to show that this stratification is Whitney. 

Let us canonically extend _F_ 1 and _F_ 2 to ∆ _Up_ . Then we claim that ∆ _Up_ is a Bott nondegenerate manifold (Definition 90) for the functions _F_ 1 and _F_ 2. Moreover, we claim that in both cases the metric Hessian has eigenvectors _wM × −wM_ and _wm × −wm_ with the eigenvalues equal to _κM_ and _κm_ , respectively. For this, one has to consider for each ( _p,_ ˜︁ _p_ ˜︁) _∈_ ∆ _Up_ the graphical coordinates ( _x_ 1 _, y_ 1 _, f_ ( _x_ 1 _, y_ 1) _, x_ 2 _, y_ 2 _, f_ ( _x_ 2 _, y_ 2)) centered at ( _p,_ ˜︁ _p_ ˜︁), see coordinates in Lemma 80. Then the rest follows from a straightforward computation as in Lemma 82; we will leave the computation to the reader. 

Now, similarly to the proof of Lemma 80, we can apply the Morse-Bott Lemma [BH04, Hir97] to each of _F_ 1 and _F_ 2 and conclude the Whitney conditions along the stratum ∆ _Up_ . 

41 

Then the lemma follows from Thom’s first isotopy Lemma 84. In particular, to show that _πN_ is a submersion on each strata, one has to use Lemma 83. 

**Lemma 86.** _For each_ ( _s, θ_ ) _∈_ R _/T_ Z _×_ ( _−π/_ 2 _, π/_ 2) _we consider {Qj}j∈{_ 1 _,...,_ 4 _} - quadrants on a O_ ( _ε_ ) _-small neighbourhood of_ Γ( _s, θ_ ) = _p ∈ TK,ε, which were defined in Lemma 80._ 

_There is a positive constant Cs such that for each sufficiently small ε >_ 0 _the following holds_ 

- _If θ ∈_ [ _ε_[1] _[/]_[2] _Cs, π/_ 2 _− ε_[1] _[/]_[2] _Cs_ ] _, then Q_ 1 _, Q_ 2 _are outward-pointing and Q_ 3 _, Q_ 4 _are inward-pointing._ 

- _If θ ∈_ [ _−π/_ 2+ _ε_[1] _[/]_[2] _Cs, −ε_[1] _[/]_[2] _Cs_ ] _, then Q_ 1 _, Q_ 2 _are inward-pointing and Q_ 3 _, Q_ 4 _are outward-pointing._ 

**==> picture [337 x 223] intentionally omitted <==**

**----- Start of picture text -----**<br>
See also Figure 3.9.<br>T<br>K,ε<br>wm<br>p<br>wM<br>**----- End of picture text -----**<br>


Figure 3.9: Local description of chords emanating from _p_ = Γ _ε_ ( _s, θ_ ) for _θ ∈_ [ _ε_[1] _[/]_[2] _Cs, π/_ 2 _− ε_[1] _[/]_[2] _Cs_ ]. Blue regions describe the possible endpoints for _“out-out”_ chords. Red regions describe the possible endpoints for _“in-in”_ chords. Grey lines are integral curves of principal directions from _p_ . 

_Proof._ The lemma follows from Lemmata 75 and 80. Observe that at ( _s, θ_ ) it holds: 

**==> picture [215 x 157] intentionally omitted <==**

42 

Hence, on the _Qj_ quadrant inequality (3.17) becomes equivalent to 

_ρ[j] b_ (︂ _−_ 2 _ρ[j] a[d]_[1] _[/]_[2][(̇] _[κ]_[(] _[s]_[) cos(] _[θ]_[)+] _[τ]_[(] _[s]_[)] _[κ]_[(] _[s]_[) sin(] _[θ]_[))] _[−]_[(1] _[/ε]_[1] _[/]_[2][)6] _[κ]_[3] _[/]_[2][(] _[s]_[) sin(] _[θ]_[)] _[|]_[ cos(] _[θ]_[)] _[|]_[1] _[/]_[2][)︂] _<_ 0 _._ Which can be rewritten as 

**==> picture [298 x 15] intentionally omitted <==**

for some bounded function _A_ ( _s, θ_ ). And the lemma follows. 

_Remark_ 87 _._ The diagonal ∆ _ε_ is diffeomorphic to _S_[1] _×_ [0 _,_ 1], where _S_[1] _× {_ 0 _,_ 1 _}_ correspond to points of _TK,ε_ with _κG_ = 0. In particular, ∆ _ε_ ⊊ ∆ _full_ . 

**Corollary 88.** _Put CK_ := 2 sup _{Cs_ 1 _| s_ 1 _∈_ R _/T_ Z _}. In a small closed tubular neighborhood of_ 

∆ _[cusp] ε_ := ∆ _ε\_ {︂( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _| θ_ 1 _∈_ ( _kπ/_ 2 _−ε_[1] _[/]_[2] _CK, kπ/_ 2+ _ε_[1] _[/]_[2] _CK_ ) _, k ∈_ Z}︂ (3.23) _it holds that MK,ε has a structure of a locally trivial stratified fibration. The fibers are identified with the union of two cuspidal regions. More precisely, the map identifying each fiber πN[−]_[1][(] _[p]_[)] _[with]_ 

**==> picture [193 x 19] intentionally omitted <==**

_is a stratum preserving homeomorphism, which is a diffeomorphism outside of p._ 

_Proof._ The corollary follows from the combination of Lemmata 86, 85 and 82. 

_Example_ 89 _._ In a simplified case, we are going to illustrate the behavior of _MK,ε_ ̇ near the diagonal. We will consider _K_ with _τ_ = _κ_ = 0 (note that this will, in particular, also simplify inequality (3 _._ 22) to _ρ[j] b_[sin(] _[θ]_[)] _[|]_[ cos(] _[θ]_[)] _[|]_[1] _[/]_[2] _[>]_[ 0).] 

Let _TK,ε_ be a standard torus parameterized by 

**==> picture [291 x 19] intentionally omitted <==**

Let _M_[ˆ︂] _K,ε_ denotes the restriction of _MK,ε_ to the set _{_ ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] _| d_[˜︁] ( _s_ 1 _, s_ 2) _≤ δK}_ and _πs_ 1 : _M_[ˆ︂] _K,ε →_ R _/T_ Z be the canonical projection. We would like to inspect the fiber _πs[−]_ 1[1][(3] _[π/]_[2).] 

To enlight Conjecture 70 and Remark 72 we can explicitly compute the solutions of _F_ 1[[] _[ε]_[]] = 0 _∧ F_ 2[[] _[ε]_[]] = 0 in ( _θ_ 1 _, s_ 2 _, θ_ 2)-coordinates. If we ignore the trivial solutions coming from ∆ _ε_ , we obtain four (piecewise smooth) curves _{cj}j∈{_ 1 _,...,_ 4 _}_ : 

**==> picture [291 x 48] intentionally omitted <==**

The curves _c_ 1 and _c_ 2 intersect (touch) at the point ( _π,_ 3 _π/_ 2 _, π_ ), and their union is homeomorphic to a cone and consists of two smooth curves. See Figure 3.10. 

43 

**==> picture [321 x 340] intentionally omitted <==**

**----- Start of picture text -----**<br>
θ 1 •<br>2 π<br>•<br>θ 2<br>s 2<br>0<br>**----- End of picture text -----**<br>


Figure 3.10: A visualisation of fiber _πs[−]_ 1[1][(3] _[π/]_[2)][in][(] _[θ]_[1] _[, s]_[2] _[, θ]_[2][)-coordinates.][The] red line corresponds to points on ∆ _ε_ , the blue curves denote _c_ 1 and _c_ 2, and the green lines represent _c_ 3 and _c_ 4. Two blue dots represent critical points of _πs_ 2 (Conjecture 70 ( _ii._ )). Note that the singular behavior of ∆ _ε_ causes lower quality of the visualization in a neighborhood of ∆ _ε_ . But still, we can see the cuspidal fibration from Conjecture 88. 

44 

## **3.5 Energy functions** 

We are going to study _E_ 0 _, Eε_ ; the restrictions of the standard energy function _E_ : R[3] _×_ R[3] _→_ R to _K × K_ and _TK,ε × TK,ε_ ( _MK,ε_ ), respectively. In particular, we show that for generic _K_ and _ε >_ 0 the functions _E_ 0 _, Eε_ are Morse-Bott, and we also relate their critical points. In the end of the section we inspect how the cuspical geometry of _MK,ε_ restricts the number of potential _−∇Eε_ -trajectories in _MK,ε_ that can reach the minimum ∆ _ε_ before flowing out of _MK,ε_ . This will also depend on the non-resonance of eigenvalues of _−D∇Eε_ (∆ _ε_ ) and the behavior of _−∇Eε_ along _∂MK,ε_ . 

**Definition 90.** _Let_ ( _M, g_ ) _be a closed oriented Riemanninan manifold. A smooth function f_ : _M →_ R _is called_ _**Morse-Bott** , if the set of critical points Crit_ ( _f_ ) _is a disjoint union of connected submanifolds {Qj}j of M with the following property: the Hessian H[g]_ [ _f_ ] _, when restricted fiberwise to the normal bundle of Qj in M_ (:= _N[g]_ ( _Qj, M_ )) _, defines a nondegenerate bilinear form. The Qj will be called_ _**Bott-nondegenerate (critical) submanifold** ._ 

_In addition, if N±[g]_[(] _[Q] j[, M]_[)] _[denotes][the][splinting][of][N][ g]_[(] _[Q] j[, M]_[)] _[onto][positive] and negative eigenspaces of H[g]_ [ _f_ ] _, then we define the_ _**Morse index of** Qj as_ 

**==> picture [151 x 13] intentionally omitted <==**

_Critk_ ( _f_ ) _will denote the subset of Crit_ ( _f_ ) _that consists of Bott-nondegenerate critical submanifolds of the Morse index k._ 

**Definition 91.** _Let f be a Morse-Bott function on the Riemannian manifold_ ( _M, g_ ) _. Then the (negative)_ _**gradient flow** is the flow of −∇[g] f and will be denoted by ϕ[t] f[or][·][f][.]_ 

**Definition 92.** _Let f_ : _M →_ R _be a Morse-Bott function and Q ⊂ Crit_ ( _f_ ) _. Then we define the_ _**unstable manifold** Wf_ ( _Qj_ ) _as_ 

**==> picture [195 x 18] intentionally omitted <==**

_and the_ _**stable manifold** Wf_ ( _Q_ ) _as_ 

**==> picture [195 x 18] intentionally omitted <==**

_Remark_ 93 _._ [AB95, Prop 3.2] _Wf[u]_[(] _[Q]_[)][is][the][image][of][an][injective][immersion][of] _N−[g]_[(] _[Q, M]_[)][into] _[M]_[and][the][map] _[x][ ↦→]_[lim] _t→−∞[ϕ][t] f_[(] _[x]_[)][gives][to] _[W] f[ u]_[(] _[Q]_[),][in][a][neigh-] borhood of _Q_ , a structure of locally trivial fiber bundle over _Q_ . The analogous statement also holds for _Wf[s]_[(] _[Q]_[).] 

**Definition 94.** _On K we define_ 

**==> picture [276 x 42] intentionally omitted <==**

_where γ_ : R _/T_ Z _→_ R[3] _is an arc length parametrization of K and ⟨·, ·⟩ is the induced metric on K from_ (R[3] _, gEuc_ ) _._ 

45 

_Remark_ 95 _._ We can compute 

**==> picture [106 x 31] intentionally omitted <==**

Hence, the critical points of _E_ 0 are the solutions of 

**==> picture [137 x 13] intentionally omitted <==**

which are the binormal chords on _K_ and points from ∆0. Next, we can compute 

**==> picture [158 x 50] intentionally omitted <==**

We also point out that, by the construction, _γ_ is an isometry between the flat metric on R _/T_ Z and _⟨·, ·⟩_ on _K_ . 

**Lemma 96.** _For a generic K in_ R[3] _the function E_ 0 _is Morse outside of the Bott nondegenerate manifold_ ∆0 _._ 

_Proof._ For any _K_ the Bott-nondegenaracy of ∆0 is immediate from Remark 95, see also [CELN16, Lemma 7.10]. 

Let 

**==> picture [129 x 31] intentionally omitted <==**

be a section with zeros as critical points of _E_ 0. Recall from Remark 444 that along the zero section, _p ∈_ s _[−]_[1] (0), we have the canonical splitting of _T_ ( _p,_ 0) _T[∗]_ ( _K × K_ ). In particular, we consider the vertical linearized map 

**==> picture [263 x 36] intentionally omitted <==**

By the Rank-nullity theorem, we obtain that _d[v]_ s( _p_ ) is a Fredholm map with the index zero. In particular, _d[v]_ s( _p_ ) ⋔ 0 iff _d[v]_ s( _p_ ) is injective. And by the construction of _d[v]_ s( _p_ ), this is equivalent to _p_ being a nondegenerate critical point of _E_ 0. 

Now, let us consider a section 

**==> picture [251 x 36] intentionally omitted <==**

where _C[k]_ ( _S_[1] _,_ R[3] ) is a Banach space with _C[k]_ topology and _k_ is big enough. We note that _γ_ is here just an arbitrary element of _C[k]_ ( _S_[1] _,_ R[3] ) and that _E_ 0 is here understood as ( _γ × γ_ ) _[∗] E_ , where _E_ is the standard energy function on (R[3] _×_ R[3] _, gEuc_ ). 

We are going to show the surjectivity of the linearised map _dS_ ( _γ, s_ 1 _, s_ 2) : _C[k]_ ( _S_[1] _,_ R[3] ) _×_ R[2] _→_ R[2] at the zero section. 

46 

We compute that 

**==> picture [384 x 31] intentionally omitted <==**

ˆ ˆ ˆ ˆ We choose _γi, i_ = 1 _,_ 2 _,_ as follows. We put _γ_ 1( _s_ 2) _− γ_ 1( _s_ 1) = _γ_[̇] 1( _s_ 1) = _γ_ ( _s_ 2) _− γ_ ( _s_ 1) ˆ ̇ ˆ ˆ ˆ and _γ_[̇] 1( _s_ 2) = _γ_ ( _s_ 2). And analogously, _γ_ 2( _s_ 2) _− γ_ 2( _s_ 1) = _γ_[̇] 2( _s_ 2) = _γ_ ( _s_ 2) _− γ_ ( _s_ 1) and _γ_ ˆ[̇] 2( _s_ 1) = _γ_ ̇ ( _s_ 1). 

Hence, we obtain that 

and 

**==> picture [238 x 90] intentionally omitted <==**

Since _||γ_ ( _s_ 2) _− γ_ ( _s_ 1) _||_[2] = 0, we obtain the surjectivity of _dS_ along the zero section. Now, by the Implicit function theorem, see for example [Cie18], _S[−]_[1] (0) is a Banach manifold. Let us consider the projection _π_ 1 : _S[−]_[1] (0) _→ C[k]_ ( _S_[1] _,_ R[3] ), which is, for _k_ big enough, smooth. By Sard-Smale theorem, [Cie18], the set of regular values (= _Creg_ ) of _π_ 1 is residual in _C[k]_ ( _S_[1] _,_ R[3] ). By [Hir97, Cor 1.6, Thm 2.13], _C[k]_ -embeddings (= _Cembedd_ ) are dense and open in _C[k]_ ( _S_[1] _,_ R[3] ). Hence, for each _γ_ from the generic subset _Creg ∩ Cembedd_ of _C[∞]_ ( _S_[1] _,_ R[3] ) the corresponding section s ⋔ 0. And, in particular, _E_ 0 is Morse-Bott. 

_From now on, we will work with knots that are generic in the spirit of Lemma 96_ 

**Definition 97.** _Let K be a knot in_ R[3] _and ε ∈_ (0 _, εgood_ ] _. Then we define_ 

**==> picture [311 x 44] intentionally omitted <==**

_Also, by Eε[out][−][out] we will denote the restriction of Eε to MK,ε._ 

_Remark_ 98 _._ We would like to describe _−∇Eε_ . 

We recall our notation that _⟨·, ·⟩_ is the standard metric in R[3] or R[3] _×_ R[3] and _⟨·_ ˜︃ _, ·⟩_ is the standard metric in the coordinate charts ( _s_ 1 _, s_ 2) or ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2), see Notation 43. Hence, the gradients with respect to those metrics will be denoted as _∇_ and[˜︂] _∇_ , respectively, and so on. 

Let us consider the map 

**==> picture [272 x 14] intentionally omitted <==**

which is not, unlike in the knot case, an isometry. First, we compute 

**==> picture [220 x 65] intentionally omitted <==**

47 

where we used, as in Theorem 50, the fact that 

**==> picture [204 x 13] intentionally omitted <==**

And hence 

**==> picture [309 x 71] intentionally omitted <==**

where _di_ = (1 _− ε_ cos( _θi_ ) _κ_ ( _si_ )). 

Next, let us consider the pull-back metric _g_ = **Γ** _[∗] ε[⟨·][,][ ·⟩]_[.] _[g]_[is][a][product][metric] on the product of tori (R _/T_ Z _× S_[1] ) _×_ (R _/T_ Z _× S_[1] ) and recall that by (3.15) it holds 

**==> picture [317 x 50] intentionally omitted <==**

Hence the inverse metric _g[−]_[1] is given by the matrix 

**==> picture [369 x 69] intentionally omitted <==**

Next, by the definition 

**==> picture [413 x 41] intentionally omitted <==**

Thus 

**==> picture [379 x 57] intentionally omitted <==**

**Lemma 99.** _Let us restrict E_ 0 _and Eε outside of the diagonals_ ∆0 _and_ ∆ _full, respectively. We denote these restrictions by E_[ˆ︁] 0 _and E_[ˆ︁] _ε. Then it holds that if E_[ˆ︁] 0 _is Morse and ε >_ 0 _is sufficiently small, then E_[ˆ︁] _ε is also Morse._ 

_In addition, there is a bijection between Critk_ ( _E_[ˆ︁] 0) _and Critk_ +1( _E_[ˆ︁] _ε[out][−][out]_ ) _, for any k ∈_ N0 _. More precisely, the sets Crit_ ( _E_[ˆ︁] 0) _and Crit_ ( _E_[ˆ︁] _ε_ ) _∩ Int_ ( _MK,ε_ ) _are in a bijection and_ 

**==> picture [139 x 13] intentionally omitted <==**

_where p_ 0 _and pε are the corresponding critical points from Crit_ ( _E_[ˆ︁] 0) _and Crit_ ( _E_[ˆ︁] _ε_ ) _∩ Int_ ( _MK,ε_ ) _, respectively._ 

48 

_Proof._ From Remark 95 we know that the critical points of _E_[ˆ︁] 0 are the binormal chords on _K_ , i.e. the solutions of 

**==> picture [73 x 13] intentionally omitted <==**

Since our ambient space is R[3] with the flat metric, we can relate the energy functionals from Definitions 436 and 97, _**E**_[ˆ︂] _ε_ and _E_[ˆ︁] _ε_ , respectively. In particular, by Remark 439, the critical points _pε_ of _E_[ˆ︁] _ε_ represent the binormal chords of _TK,ε_ , that is 

**==> picture [94 x 13] intentionally omitted <==**

Alternatively, we can see this directly from relations (3.24). Altogether, at _pε_ it holds that _v_ 1 = _±v_ 2 and each _pε_ is uniquely determined as the solution of 

**==> picture [277 x 14] intentionally omitted <==**

So, for each _pε ∈ Crit_ ( _E_[ˆ︁] _ε_ ) there is a _p_ 0 _∈ Crit_ ( _E_[ˆ︁] 0) such that _πs_ 1 _,s_ 2( _pε_ ) = _p_ 0. Now, we would like to compare the signs of the Hessian matrices of these _p_ 0 and 

_pε_ . 

But first, let us make the following auxiliary computations 

**==> picture [251 x 13] intentionally omitted <==**

**==> picture [121 x 13] intentionally omitted <==**

**==> picture [251 x 14] intentionally omitted <==**

̇ _∂θ_ 2 _⟨P_ + _εv_ 2 _, γ_ ( _s_ 1) _⟩_ = _ε⟨v_ 2 _[⊥][,][γ]_[̇][(] _[s]_[1][)] _[⟩]_ 

and 

**==> picture [355 x 71] intentionally omitted <==**

**==> picture [351 x 110] intentionally omitted <==**

**==> picture [396 x 52] intentionally omitted <==**

**==> picture [327 x 36] intentionally omitted <==**

**==> picture [127 x 15] intentionally omitted <==**

49 

Hence, by Remark 95 _∂si∂sj E_ 0( _p_ 0) = _∂si∂sj Eε_ ( _pε_ ) + _O_ ( _ε_ ). And also all other second derivatives of _Eε_ are of type _O_ ( _ε_ ). 

This motivates us to the following comparison of the Hessian matrices of _E_[ˆ︁] 0 and _E_[ˆ︁] _ε_ . 

Because _K_ is generic, by Lemma 96 _E_[ˆ︁] 0 is Morse. Since nondegenerate critical points are isolated, we can assume that critical points of _E_[ˆ︁] 0 lie outside of the weakly special and weakly diagonal points. Let us pick any _pε ∈ Crit_ ( _E_[ˆ︁] _ε_ ) and put _p_ 0 := _πs_ 1 _,s_ 2( _pε_ ). 

Recall that at the critical points, the signs of the Hessian matrix do not depend on the pull-back metric and can be described in coordinates just as second derivatives. 

Now we write the Hessian matrix _H_[˜︂] [ _E_ 0]( _p_ 0) as 4 _×_ 4 matrix, where the even rows and columns are filled with zeros and we implicitly considered the standard metric _⟨·_ ˜︃ _, ·⟩_ on coordinates ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2). Hence _H_[˜︂] [ _Eε_ ]( _pε_ ) can be seen as _ε_ - perturbation of elements of _H_[˜︂] [ _E_ 0]( _p_ 0). By Kato’s selection theorem, this gives us a _ε_ -perturbation of the eigenvalues of matrices. 

By our assumptions on _p_ 0, _H_[˜︂] [ _E_ 0]( _p_ 0) has two eigenvalues _λ_ 0;1 _, λ_ 0;2 such that 

**==> picture [111 x 13] intentionally omitted <==**

for some _δ ≥_ 0. Then _H_[˜︂] [ _Eε_ ]( _pε_ ) has 4 eigenvalues _λε_ ;1 _, λε_ ;2 _, λε_ ;3 _, λε_ ;4 such that 

**==> picture [95 x 65] intentionally omitted <==**

Hence, if 0 _< ε ≪ δ_ , the eigenvalues _λε_ ;1 _, λε_ ;2 have the same signs as _λε_ ;1 _, λε_ ;2, respectively. 

Now we aim to inspect the sign of det (︂˜︂ _H_ [ _Eε_ ]( _pε_ ))︂. We can compute 

**==> picture [351 x 40] intentionally omitted <==**

Since _pε_ is a binormal chord, from (3.28) we have that _P || vi_ . Moreover, since _pε ∈/_ ∆ _full_ , we conclude that for _ε >_ 0 sufficiently small it holds det (︂˜︂ _H_ [ _Eε_ ]( _pε_ ))︂ = 0. In particular, we showed that if _ε >_ 0 is small and _E_[ˆ︁] 0 is Morse, then _E_[ˆ︁] _ε_ is Morse too. 

At the critical point _pε ∈/_ ∆ _full_ , we can deduce from _P_ being parallel to _vi_ even more. It holds that 

**==> picture [317 x 16] intentionally omitted <==**

where _Di_ = _⟨P, n_ ( _si_ ) _⟩_[2] + _⟨P, b_ ( _si_ ) _⟩_[2] _._ For the geometric picture, see the proof of Lemma 58. Note that since _pε_ does not project onto any diagonal or special point, _Di >_ 0. So for each _p_ 0 _∈ Crit_ ( _E_[ˆ︁] 0) there are four possible _pε_ with _πs_ 1 _,s_ 2( _pε_ ) = _p_ 0. Then it holds 

**==> picture [501 x 38] intentionally omitted <==**

**==> picture [31 x 13] intentionally omitted <==**

50 

Hence for only one of the four critical points _pε_ , that project to _p_ 0, it holds that 

**==> picture [269 x 13] intentionally omitted <==**

Let _pε_ be the critical point satisfying (3.32). Since _p_ 0 is outside of weakly special and weakly diagonal points, for _ε >_ 0 sufficiently small it holds that _pε ∈ Int_ ( _MK,ε_ ). Moreover, for _ε >_ 0 sufficiently small the sign of det (︂˜︂ _H_ [ _Eε_ ]( _pε_ )) is _opposite_ to the sign of the product _λ_ 0;1 _λ_ 0;2. Hence we obtain that _IndE_ 0( _p_ 0) = _IndEε_ ( _pε_ ) _−_ 1. 

_Remark_ 100 _._ Later, we will see Lemma 99 also as a consequence of Multiple-time scale dynamics. 

**Lemma 101.** ∆ _full is a Bott nondegenerate critical manifold of Eε. Moreover, if p ∈_ ∆ _full, then the nonzero eigenvalues of H_ [ _Eε_ ]( _p_ ) _are both equal to_ 2 _(we took H_ [ _Eε_ ]( _p_ ) _with respect to the induced metric g_ = **Γ** _[∗] ε[⟨·][,][ ·⟩][).]_ 

_Proof._ Let _p ∈_ ∆ _full_ . By the proof of Lemma 99 we quickly obtain that _H_[˜︂] [ _Eε_ ]( _p_ ) is given by 

**==> picture [276 x 57] intentionally omitted <==**

Hence, by Remark 98 we can compute that 

**==> picture [370 x 200] intentionally omitted <==**

Observe that the matrix _H_ [ _Eε_ ]( _p_ ) has a 2-dimensional kernel spanned by _∂s_ 1 + _∂s_ 2 and _∂θ_ 1 + _∂θ_ 2. Moreover _H_ [ _Eε_ ]( _p_ ) is positive definite in directions _∂s_ 1 _− ∂s_ 2 and _∂θ_ 1 _− ∂θ_ 2 with the same positive eigenvalues equal to 2. Note also that the 0- eigenspace is orthogonal to the 2-eigenspace with respect to the metric _g_ . This finishes the Bott nondegeneracy of ∆ _full_ . 

**Lemma 102.** _Let xε ∈ MK,ε such that yε_ := _πs_ 1 _,s_ 2( _xε_ ) _∈ SK (see Remark 47 for the notion of the standard set SK). Provided that ε >_ 0 _is sufficiently small, it holds that_ 

51 

- ( _i._ ) _If F_ 1[[] _[ε]_[]][(] _[x][ε]_[) = 0] _[and][F]_ 2[ [] _[ε]_[]][(] _[x][ε]_[)] _[ >]_[ 0] _[,][then][−∇][E][ε]_[(] _[x][ε]_[)] _[is][strictly][inward-pointing] into M . K,ε_ 

- ( _ii._ ) _If F_ 1[[] _[ε]_[]][(] _[x][ε]_[)] _[ >]_[ 0] _[ and][ F]_ 2[ [] _[ε]_[]][(] _[x][ε]_[) = 0] _[,][then][ −∇][E][ε]_[(] _[x][ε]_[)] _[ is strictly outward-pointing] from MK,ε._ 

- ( _iii._ ) _If F_ 1[[] _[ε]_[]][(] _[x][ε]_[) =] _[ F]_ 1[ [] _[ε]_[]][(] _[x][ε]_[) = 0] _[,][then][there][is][δ][>]_[ 0] _[such][that]_ 

**==> picture [140 x 13] intentionally omitted <==**

**==> picture [101 x 13] intentionally omitted <==**

_See also Figure 3.11._ 

**==> picture [213 x 217] intentionally omitted <==**

Figure 3.11: The square diffeomorphic to _MK,ε|πs−_ 11 _,s_ 2[(] _[y] ε_[)][, where the horizontal sides] correspond to _F_ 1[[] _[ε]_[]] = 0 and the vertical sides correspond to _F_ 2[[] _[ε]_[]] = 0. Moreover, the arrows describe the behavior of the gradient flow of _−∇Eε|πs−_ 11 _,s_ 2[(] _[y] ε_[)][on][the] boundary _∂MK,ε|πs−_ 11 _,s_ 2[(] _[y] ε_[)][.] 

_Proof._ We are going to prove only the case ( _i._ ), since the other cases are analogous. 

Let us consider a smooth family of functions 

**==> picture [349 x 22] intentionally omitted <==**

such that 

**==> picture [348 x 43] intentionally omitted <==**

Let _{M_[ˆ︂] _K,ε}ε∈_ [0 _,ε_ 0] be the compact manifolds of outward-pointing chords over _SK_ from Lemma 54. By Lemma 54 all of these _M_[ˆ︂] _K,ε_ are isotopic submanifolds of (R _/T_ Z)[2] . 

52 

Let _ε ∈_ (0 _, ε_ 0] and _xε ∈ M_[ˆ︂] _K,ε_ be such that _F_ 1[[] _[ε]_[]][(] _[x][ε]_[)][=][0][and] _[F]_ 2[ [] _[ε]_[]][(] _[x][ε]_[)] _[>]_[0.][By] _x_ 0 _∈ M_[ˆ︂] _K,_ 0 we denote the isotopic point to _xε_ . In particular, _F_ 1[[0]][(] _[x]_[0][)][=][0][and] _F_ 2[[0]][(] _[x]_[0][)] _[ >]_[ 0.] Note that 

**==> picture [113 x 14] intentionally omitted <==**

since we consider points over _SK_ , and moreover _F_ 1[[0]][(] _[x]_[0][)][=] _[⟨][P, v][⟩]_[=][0.][Hence][if] _ε >_ 0 is sufficiently small, then also 

**==> picture [53 x 13] intentionally omitted <==**

by the smoothness of the family (3 _._ 33) _._ Moreover, _xε_ and _x_ 0 are isotopic. So if _ε >_ 0 is sufficiently small, then also 

**==> picture [56 x 13] intentionally omitted <==**

Finally, since _ε >_ 0, it holds that 

**==> picture [138 x 21] intentionally omitted <==**

which finishes the case ( _i._ ). 

**Conjecture 103.** _Let xε ∈ MK,ε \_ ∆ _ε such that πs_ 1 _,s_ 2( _xε_ ) _is an almost diagonal pair for ε >_ 0 _small (recall Definition 45 for almost diagonal pairs). If_ 

**==> picture [137 x 16] intentionally omitted <==**

_then −∇Eε_ ( _xε_ ) _is strictly outward-pointing from MK,ε. I.e. −∇Eε_ ( _xε_ ) = 0 _and there is δ >_ 0 _such that xε ·Eε_ (0 _, δ_ ] _∩ MK,ε_ = _∅ and xε ·Eε_ [ _−δ,_ 0) _⊂ Int_ ( _MK,ε_ ) _. See also Example 104._ 

_Example_ 104 _._ We are going to describe Conjecture 103 for the outward-pointing chords on a closed oriented surface _M ⊂_ R[3] in a neighborhood of a point _p ∈ M_ with the negative Gaussian curvature. 

Assume that _M_ is locally given as a graph _{_ ( _x, y, x_[2] _− y_[2] _− x_[2] _y_ ) _}_ , where _p_ := (0 _,_ 0 _,_ 0). So ( _x, y_ ) gives us the graphical coordinates of _M_ . We can assume that the vector (0 _,_ 0 _,_ 1) _[T]_ at _p_ is an outward-pointing normal vector, see Convention 74. 

Let us split a neighborhood _Up_ of _p_ into quadrants _Qi_ as in Lemma 80. Then the quadrants _Q_ 1 _, Q_ 2 are outward-pointing and _Q_ 3 _, Q_ 4 are inward-pointing. Hence by Lemma 85 the space of outward-pointing chords _M[out][−][out] ⊂ Up × Up πN_ has near ( _p, p_ ) a structure of a stratified fiber bundle _M[out][−][out] −−→ Up × Up_ . Here, the outward-pointing conditions are given by functions _F_ 1 _, F_ 2 of coordinates ( _x_ 1 _, y_ 1 _, x_ 2 _, y_ 2). 

By _E_ we will understand the restriction of the standard energy function from (R[3] _×_ R[3] _, gEuc_ ) to _Up × Up_ . 

Let us consider the set 

**==> picture [257 x 15] intentionally omitted <==**

53 

i.e., the set of outward-pointing chords starting at _p_ . Recall that _Lp_ is not the fiber _πN[−]_[1][(] _[p, p]_[),][but] _[M][ out][−][out]_[can][be][covered][by][the][sets] _[{][L][q][|][ q][∈][U]_[˜︁] _[p][}]_[for][some] _U_ ˜︁ _p ⊃ Up_ . 

We would like to inspect the behavior of _−∇E_ and _−∇E|Lp_ on _Lp_ . Let us parametrize the set _{F_ 1 = 0 _} ∩ Lp_ by 

**==> picture [157 x 25] intentionally omitted <==**

and the set _{F_ 2 = 0 _} ∩ Lp_ by 

**==> picture [100 x 26] intentionally omitted <==**

To understand _−∇E_ along the boundary of _Lp_ in some neighborhood of _p_ , we use the same condition as in Lemma 102. Using _Mathematica_ we compute that 

**==> picture [187 x 46] intentionally omitted <==**

along _{F_ 1 = 0 _} \ {_ (0 _,_ 0 _,_ 0 _,_ 0) _}_ . And also 

**==> picture [199 x 20] intentionally omitted <==**

along _{F_ 2 = 0 _} \ {_ (0 _,_ 0 _,_ 0 _,_ 0) _}_ . 

Hence, if _V_[˜︁] _p[◦]_[is][some][small][collar][neighborhood][of] _[p]_[,][then] _[−∇][E]_[is][strictly] outward-pointing from _M[out][−][out]_ along the set _Lp ∩ V_[˜︁] _p[◦][∩{][F]_[1][=] _[ F]_[2][= 0] _[}][.]_ 

It is interesting to consider also the semi-fixed case, i.e., _−∇E|Lp_ . We then obtain that 

**==> picture [197 x 47] intentionally omitted <==**

along _{F_ 1 = 0 _} \ {_ (0 _,_ 0 _,_ 0 _,_ 0) _}_ . And also 

**==> picture [219 x 22] intentionally omitted <==**

along _{F_ 2 = 0 _} \ {_ (0 _,_ 0 _,_ 0 _,_ 0) _}_ . So now, the negative gradient is strictly outwardpointing only from the boundary corresponding to _F_ 2 = 0. To the last, note that the dot product condition for _Fi_ gave twice as big value and with the opposite sign when restricted to ( _xi, yi_ ), then when restricted to ( _xj, yj_ ) for _j_ = _i_ . 

_Remark_ 105 _._ We expect that over any weakly ~~_s_~~ 2-special set the following holds. There is a point _xε ∈ MK,ε_ such that _F_ 1[[] _[ε]_[]][(] _[x][ε]_[)] _[ >]_[ 0] _[∨][F]_ 2[ [] _[ε]_[]][(] _[x][ε]_[) = 0 and] _[ −∇][E][ε]_[(] _[x][ε]_[) is] now inward-pointing into _MK,ε_ In other words, the relative direction of _−∇Eε_ ( _xε_ ) is opposite to the direction in Lemma 102 ( _i._ ). For geometric intuition, the reader might find it convenient to see Figure 3.4. We expect the analogous phenomena also for weakly ~~_s_~~ 1-special sets. 

54 

**Definition 106.** _Let X be a C_[1] _vector field on the Riemannian manifold_ ( _M, g_ ) _that vanishes at a point p. Let x ∈ M \p. We say that ℓp ∈ TpM is an_ _**asymptotic limit vector of** x iff there is a partial flow line u_ : [0 _, ∞_ ) _→ M of X such that_ 

( _i._ ) _u_ (0) = _x._ 

**==> picture [111 x 13] intentionally omitted <==**

**==> picture [125 x 19] intentionally omitted <==**

_Remark_ 107 _._ [Sch93, Lemma B.5] Let _f_ be a Morse function on ( _M, g_ ). Then for the gradient flow _ϕ[t] f_[it holds that every point] _[ x][ ∈][M][ \][ Crit]_[(] _[f]_[) has an asymptotic] limit vector. 

**Sternberg’s Linearization Theorem 108.** _[Nel70] Let n ≥_ 2 _and X be a smooth vector field on_ R _[n] that vanishes at_ 0 _. Let χ_ 1 _, . . . , χn be (complex) eigenvalues of DX_ (0) _that satisfy the following non-resonant assumption:_ 

**==> picture [396 x 24] intentionally omitted <==**

**==> picture [74 x 31] intentionally omitted <==**

_Then there is a local smooth diffeomorphism around_ 0 _conjugating X with its linear part on T_ 0R _[n] ._ 

**Lemma 109.** _Let p ∈_ ∆ _full and ℓp be a unit vector of Tp_ (R _/T_ Z _× S_[1] )[2] _. Let νδ_ (∆ _full_ ) _be a δ-radius tubular neighborhood of_ ∆ _full for some δ >_ 0 _. If δ >_ 0 _is small, then for the flow ϕ[t] Eε[on]_[(][R] _[/T]_[Z] _[ ×][ S]_[1][)][2] _[it][holds][that][the][set]_ 

**==> picture [277 x 13] intentionally omitted <==**

_is flow invariant and diffeomorphic to an open interval._ 

_Proof._ By Lemma 101 ∆ _full_ is a Bott nondegenerate critical manifold for _Eε_ . Let _W_ ˆ︂ _E[s] ε_[(∆] _[full]_[)][be][the][restriction][of] _[W][ s] Eε_[(∆] _[full]_[)][to] _[ν][δ]_[(∆] _[full]_[).][By][Remark][93][the][flow] endpoint map _πEε_ : _W_[ˆ︂] _E[s] ε_[(∆] _[full]_[)] _[ →]_[∆] _[full]_[induce][a][locally][trivial][fiber][bundle.] Let _p ∈_ ∆ _full_ . We consider the fiber _F_ = _πE[−] ε_[1][(] _[p]_[)][and][the][flow][of] _[−∇][E][ε][|][F]_[.] In particular, _F_ is flow invariant. By Lemma 101 the spectrum of _−D∇Eε|F_ ( _p_ ) consists of two eigenvalues equal to 2. Hence if _δ >_ 0 is small, then by Sternberg’s Linearization Theorem 108 _−∇Eε|F_ is conjugated by a smooth diffeomorphism with _−D∇Eε|F_ (restricted to some small neighborhood _U_ 0 of 0 in _TpF_ ). 

Now, by the spectrum of _−D∇Eε|F_ (0) the following holds for the flow of _−D∇Eε|F_ . If _ℓ_ 0 _∈ T_ 0( _TpF_ ) is a unit vector, then the set of _x ∈ U_ 0, with the asymptotic limit vector _ℓ_ 0, is diffeomorphic to an open interval. 

Since the flows are conjugated by a smooth diffeomorphism, the lemma follows. 

**Conjecture 110.** _For every δ >_ 0 _small there is a subset_ ∆ _ε,δ ⊂_ ∆ _[cusp] ε which is O_ ( _δ_ ) _-close and diffeomorphic to_ ∆ _[cusp] ε and the following holds._ 

55 

**==> picture [412 x 227] intentionally omitted <==**

**----- Start of picture text -----**<br>
πE [−] ε [1][(] [p] [)] πE [−] ε [1][(] [p] [)]<br>M<br>K,ε<br>p p<br>A<br>p<br>Figure 3.12: On the left: the fiber πE [−] ε [1][(] [p] [)] [of] [the] [fibration] W [ˆ︂] E [s] ε [(∆] [full] [)] −−→πEε ∆ full<br>inside  νδ (∆ full ). The gradient flow trajectories of  −∇Eε  are in grey. On the right:<br>the restriction of the gradient flow trajectories from  πE [−] ε [1][(] [p] [) to] [ π] E [−] ε [1][(] [p] [)] [∩] [M][K,ε] [.] [The]<br>set Ap is depicted in red.<br>**----- End of picture text -----**<br>


_If p ∈_ ∆ _ε,δ, then the set_ 

**==> picture [292 x 31] intentionally omitted <==**

_is flow invariant and diffeomorphic to a disjoint union of two open intervals. See also Figure 3.12._ 

_Partial proof._ Inside the tubular neighborhood _νδ_ (∆ _full_ ) we have two (stratified) fiber bundles _W_[ˆ︂] _E[s] ε_[(∆] _[full]_[)] _−−→πEε_ ∆ _full_ and _M_[ˆ︂] _K,ε −−→πN_ ∆ _[cusp] ε_ given by Remark 93, Lemma 85 and Corrollary 88. Recall that _πEε_ is the flow end-point map and _πN_ is induced from the normal bundle _N_ **Γ** _∗⟨·,·⟩_ (∆ _[cusp] ε ,_ (R _/T_ Z _× S_[1] )[2] ). Now, let us assume that _p ∈_ ∆ _[cusp] ε_ is such that 

**==> picture [259 x 16] intentionally omitted <==**

So, if _δ >_ 0 is small, then by Conjecture 103 and Corollary 88 the set _Ap_ consists of points with one of two possible asymptotic limit vectors at _p_ . Hence, by Lemma 109, it holds that _Ap_ is diffeomorphic to a disjoint union of two open intervals. 

It remains to show that the relation (3.34) can be satisfied by a sufficiently large subset ∆ _ε,δ ⊂_ ∆ _[cusp] ε_ . By Lemma 85 we see that any generalized tangent space of _πN[−]_[1][(] _[p]_[)][at] _[p]_[is][contained][at] _[T][p]_[(] _[π] E[−] ε_[1][(] _[p]_[)).][Finally,][as][we][shrink] _[δ]_[-radius][of] _νδ_ (∆ _full_ ), ∆ _ε,δ_ can be arbitrarily large as a subset of ∆ _[cusp] ε_ . 

56 

## **4. Adiabatic limit with Conley index** 

From Section 3.5 we know the correspondence between the critical points _Crit_ ( _E_ 0) and _Crit_ ( _Eε|MK,ε_ ) and their degree shift. Hence, it is natural to ask about the correspondence between the trajectories on _K × K_ and _MK,ε_ , at least for _ε >_ 0 small. However, as we shrink _TK,ε_ to _K_ , the gradient _∇Eε_ explodes. Hence, due to the singular behavior, we would like to apply an Adiabatic limit argument as in [FW22a, FW22b], see also [Web99]. In order to avoid a lot of analysis, we would like to perform instead of two Implicit function theorems rather a certain Conley index argument. As a consequence, such a correspondence will not identify the particular trajectories, but rather only certain equivalence classes of trajectories. However, we will be able to close each equivalence class of trajectories to an arbitrarily thin strip (isolating neighborhood), and in particular know reasonably well the “shape” of the trajectories. In addition, these thin strips and a certain argument by contradiction will be used to trap the trajectories and obtain the adiabatic compactness. 

We remark that in our argument, we want the trajectories on _K × K_ to generically avoid special and diagonal points. For this, we restrict the adiabatic limit only for trajectories between critical points in low degrees that moreover do not belong to diagonals. 

To the end, we note that in the literature, some Conley index arguments were used for the singular dynamical systems, see for example [GKM[+] 99]. However, to the author's knowledge, only in the task of the existence of orbits. This is probably due to the fact that our dynamics is given by gradient(-like) vector fields instead of some general dynamical system. 

## **4.1 Gradient-like vector fields** 

We are going to introduce gradient-like vector fields and discuss some of their perturbation techniques. 

**Definition 111.** _Let f be a Morse-Bott function on closed oriented Riemannian manifold_ ( _M, g_ ) _. A (smooth) vector field Xf is called_ _**gradient-like** adapted to f if it holds that_ 

( _i._ ) _df_ ( _x_ ) _Xf |x <_ 0 _for every x ∈/ Crit_ ( _f_ ) _._ 

( _ii._ ) _−∇[g] f_ = _Xf in some open neighborhood of Crit_ ( _f_ ) _._ 

_The flow of Xf will be denoted as ϕ[t] Xf[or][·][X] f[.][The][stable/unstable][manifolds][of] Q ⊂ Crit_ ( _f_ ) _will be denoted as WX[s/u] f_[(] _[Q]_[)] _[.][Moreover,]_ 

**==> picture [189 x 16] intentionally omitted <==**

_where Qi, Qj ⊂ Crit_ ( _f_ ) _. In addition, we put_ 

**==> picture [165 x 14] intentionally omitted <==**

57 

_where the quotient is given by the free action of_ R _, which shifts the time on the flow lines._ 

_Remark_ 112 _._ Due to the condition ( _i._ ) in Definition 111, we can see any gradientlike vector field as a negative gradient vector field with respect to some different metric. In more detail, let _Xf_ be a gradient-like vector field adapted to a MorseBott function _f_ on ( _M, g_ ). Then there is a Riemannian metric _g_ ˆ︁ on _M_ such that _Xf_ = _−∇_[ˆ︁] _[g] f_ . 

To see this, one has to find a suitable metric locally in nice charts and then use the partition unity argument. Around _Crit_ ( _f_ ), we already have a good metric. Outside of _Crit_ ( _f_ ) we can always take local coordinates ( _x_ 0 _, . . . , xn_ ) such that _f_ is a constant in coordinates ( _x_ 1 _, . . . , xn_ ). Then, we define point-wise a matrix _A_ by columns which consist of bases vectors _∂x_ 1 _, . . . , ∂xn_ and _−Xf /_ ~~√~~ _|df_ ( _X_ ) _|_ . Finally, ( _AA[T]_ ) _[−]_[1] will define point-wise the desired local metric. 

**Definition 113.** _[Hur12]Let f_ : _M →_ R _be a Morse-Bott function and Xf be a gradient-like vector field. Then the vector field Xf is called_ _**Morse-Bott-Smale** if for any two Qi,j ∈ Crit_ ( _f_ ) _it holds that_ 

**==> picture [257 x 15] intentionally omitted <==**

_for all q ∈ Qi. Specially, if f is Morse and Xf satisfy_ (4 _._ 1) _, then Xf is called_ _**Morse-Smale** ._ 

_Remark_ 114 _._ Let _Xf_ be a Morse-Smale vector field adapted to a Morse function _f_ on ( _M, g_ ) and _p, q ∈ Crit_ ( _f_ ). Then by Remark 93 and Theorem 23 _WXf_ ( _p, q_ ) is an (embedded) submanifold of _M_ and dim( _WXf_ ( _p, q_ )) = _Indf_ ( _p_ ) _− Indf_ ( _q_ ). 

Note that if moreover _WXf_ ( _p, q_ ) = _∅_ , then _WXf_ ( _p, q_ ) consists of at least one gradient flow line, and thus dim( _Wf_ ( _p, q_ )) _>_ 0 . Hence, there are no gradient flow lines between the critical points of the same Morse index. 

_Remark_ 115 _._ Let _f_ be a Morse function on the _n_ -dimensional manifold _M_ and _q_ 0 _, q_ 1 _, qn−_ 1 _, qn_ be its critical points with Morse indices equal to the subscripts. Assume that _Xf_ is a Morse-Smale vector field adapted to _f_ . Then the manifolds _WXf_ ( _q_ 1 _, q_ 0) _, WXf_ ( _qn−_ 1 _, qn_ ) both contain up to 2 (unparametrized) gradient-like flow lines. 

_Remark_ 116 _._ If two stable and unstable manifolds intersect transversely at some point _x ∈ M_ , then they intersect transversely along the whole flow line containing _x_ . 

**Lemma 117.** _[Sma61]Let f be a Morse-Bott function on closed oriented Riemannian manifold_ ( _M, g_ ) _. Let Xf be a gradient-like vector field adapted to f . Let Q ∈ Crit_ ( _f_ ) _such that f_ ( _Q_ ) _̸_ = max( _f_ ) _and UQ be an open neighborhood of Q such that UQ ∩ Crit_ ( _f_ ) = _Q. If δ >_ 0 _is small, then WX[s] f_[(] _[Q]_[)] _[ ∩][U][Q][∩][f][ −]_[1][(︂] ( _f_ ( _Q_ ) + _δ, f_ ( _Q_ ) + 2 _δ_ ))︂ = _∅ and there is a vector field Y such that_ 

**==> picture [343 x 19] intentionally omitted <==**

**==> picture [284 x 14] intentionally omitted <==**

58 

( _iii._ ) _For any Qj ∈ Crit_ ( _f_ ) _it holds that_ 

**==> picture [134 x 16] intentionally omitted <==**

**Kupka-Smale Theorem 118.** _[Sma61] Let Xf be a gradient-like vector field adapted to the Morse-Bott function f on the closed oriented Riemannian manifold_ ( _M, g_ ) _. Let ym be the minimum value of f . Assume that Crit_ ( _f_ ) _\f[−]_[1] ( _ym_ ) _consists of_ 0 _-dimensional critical manifolds. Then there exists a Morse-Bott-Smale vector field Yf that is C_[1] _close to Xf ._ 

_Proof._ Recall that (nontrivial) gradient-like flow lines flow “downhill” with respect to the level sets of the Morse function. Hence, we can partially order _Crit_ ( _f_ ) by the heights of critical values (from the highest to the lowest). We aim to inductively apply Lemma 117. For this, we will reorder the critical manifolds with the same critical values by different choices of small _δ >_ 0, so that the perturbations from Lemma 117 will be made in different heights. The points of _Crit_ ( _f_ ) with maximal height can be reordered arbitrarily, since for them we do not need to call Lemma 117. So the set _Crit_ ( _f_ ) is now ordered and ready for inductive application of Lemma 117. 

To the end, we point out that since only the higher-dimensional critical manifolds lie in _f[−]_[1] ( _ym_ ), the Morse-Bott-Smale transversality at the unstable manifolds of these critical manifolds is automatic. 

_Remark_ 119 _._ Presented Lemma 117 and Kupka-Smale Theorem 118 slightly extend the work [Sma61] which was done for Morse-Smale flows adapted to Morse functions with distinct critical values. For another proof, see also [PdM82, Pei67]. 

**Lemma 120.** _[Pet24]Let XE_ 0 _be a gradient-like vector field. Next, let p_ 0 _∈ Crit_ 1( _E_ 0) _and x ∈_ (R _/T_ Z)[2] _be a special point. Let Ux be an open neighborhood of x. Then there is a vector field Y such that_ 

**==> picture [189 x 13] intentionally omitted <==**

**==> picture [311 x 15] intentionally omitted <==**

**==> picture [378 x 16] intentionally omitted <==**

**==> picture [249 x 17] intentionally omitted <==**

_Proof._ Note that in Lemma 117, we made a local perturbation of the flow that globally deforms the stable and unstable manifolds. However, here we demand the property ( _iv._ ), so now the perturbation technique will be a bit different than the perturbation in Lemma 117. 

First, we make a local compact perturbation of the 1-dimensional manifold _WX[u] E_ 0[(] _[p]_[0][)][such][that][the][transversality][with] _[x]_[is][achieved.][This][can][be][done][by] Relative Thom’s transversality Theorem, see [Pet24, thm A.4]. Then we find a new vector field _Y_ such that the perturbed 1-manifold is an integral of _Y_ , see [Pet24, lem 2.19]. If the perturbation was small enough, then _Y_ is also a gradient-like vector field adapted to _E_ 0. 

In this chapter, we will consider the following **generic approximations** of _−∇E_ 0 and _−∇Eε_ . 

59 

**Corollary 121.** _There is a C_[1] _small vector field Y on_ (R _/T_ Z)[2] _such that the vector field_ 

_XE_ 0 := _−∇E_ 0 + _Y_ 

_is Morse-Bott-Smale and for every p_ 0 _∈ Crit_ ( _E_ 0) _it holds that WX[u] E_ 0[(] _[p]_[0][)] _[is][trans-] verse to all special points._ 

_Let ε ∈_ (0 _, εgood_ ] _and Y_ 0 _be a canonical lift of Y to_ (R _/T_ Z) _× S_[1] )[2] _, i.e._ ( _πs_ 1 _,s_ 2) _∗Y_ 0 = _Y and_ ( _πθ_ 1 _,θ_ 2) _∗Y_ 0 = 0 _. Then there is a C_[1] _O_ ( _ε_[2] ) _-small vector field Zε on_ (R _/T_ Z _× S_[1] )[2] _such that the vector field_ 

**==> picture [125 x 12] intentionally omitted <==**

_is Morse-Bott-Smale and XEε and −∇Eε_ + _Y_ 0 _agree outside of a O_ ( _ε_[2] ) _-small neighborhood of Crit_ ( _Eε_ ) _._ 

_Proof._ Recall that by Lemma 36 there is only a finite number of special points. Moreover, these points are clearly not critical points of _E_ 0 (or inside ∆0). In order to obtain _XE_ 0, we would like to inductively apply to _−∇E_ 0 the finite number of perturbations from the Kupka-Smale theorem 118 and Lemma 120. 

We consider the ordered set of _Crit_ ( _E_ 0) from the Kupka-Smale Theorem 118 and augment the set with the special points. The special points will be ordered using their values in _E_ 0. The resulting set _S_ is now partially ordered. In particular, if for a special point _x_ and a critical point _p_ 0 _∈ Crit_ ( _E_ 0) holds that _E_ 0( _x_ ) = _E_ ( _p_ 0) _̸_ = max( _E_ 0), then we chose a convention _x < p_ 0. This is due to the fact that the perturbation for _p_ 0 will be made at the level ( _f_ ( _p_ 0) + _δ, f_ ( _p_ 0) + 2 _δ_ ) and not in ( _f_ ( _p_ 0) _− δ, f_ ( _p_ 0) + _δ_ ) for some _δ >_ 0. If _E_ 0( _x_ ) = _E_ ( _p_ 0) = max( _E_ 0), then we reorder by _x < p_ 0. The special points with the same values of _E_ 0 can be reordered among themselves arbitrarily. So the set _S_ is now ordered. 

Let us consider a step of the induction, where we want to perform a small local perturbation around a special point _x_ . By taking a sufficiently small neighborhood _Ux_ , we can achieve that this perturbation deforms (locally) only the unique 1-dimensional unstable manifold that intersects the special point, and that this perturbation is not made in the same levels as the perturbations for the critical points. In particular, the perturbed unstable manifold will have no intersection with any special or critical point on the same _E_ 0-level as _x_ . Since the gradient-like flows flow downhill, the induction will produce the desired _XE_ 0. 

Now, the perturbation of _−∇Eε_ + _Y_ 0 is an immediate consequence of the Kupka-Smale Theorem 118. 

**Definition 122.** _Let XE_ 0 _be a gradient-like vector field and p_ 0 _, q_ 0 _∈ Crit_ ( _E_ 0) _. A gradient-like flow line u of the flow ϕ[t] XE_ 0 _[is][called][a]_[0] _**[-solution][from]**[p]_[0] _**[to]**[q]_[0] _if u ⊂ WXE_ 0 ( _p_ 0 _, q_ 0) _._ 

_Let ε ∈_ (0 _, εgood_ ] _, XEε be a gradient-like vector field and pε, qε ∈ Crit_ ( _Eε_ ) _. A gradient-like flow line uε of the flow ϕ[t] XEε[is][called][an][ε]_ _**[-solution][from]**[p][ε]_ _**[to]**[q][ε] if uε ⊂ WXEε_ ( _pε, qε_ ) _._ 

## **4.2 Uniform bounds** 

In this section, we provide uniform bounds for the _ε_ -trajectories that will be needed for the adiabatic compactness. 

60 

**Theorem 123.** _There is a ε_ 0 _∈_ (0 _, εgood_ ] _and positive constants {cj}j_ =1 _,...,_ 8 _such that for every ε ∈_ (0 _, ε_ 0] _the following holds._ 

_Let pε ∈ Cr_ 2( _Eε_ ) _and qε ∈ Cr_ 1( _Eε_ ) _such that pε, qε ∈ MK,ε \_ ∆ _ε. Let XEε be a generic approximation of −∇Eε (see Corollary 121). Let uε_ ( _t_ ) _be an ε-solution from pε to qε which is described in coordinates as_ 

**==> picture [163 x 13] intentionally omitted <==**

_Then there are bounds_ 

**==> picture [240 x 13] intentionally omitted <==**

_for t ∈_ R _._ 

_Moreover, let us assume that uε avoids weakly special and weakly diagonal points, i.e., πs_ 1 _,s_ 2 _◦ uε ⊂ SK. Then uε ⊂ MK,ε. And, in addition, there are bounds_ 

**==> picture [240 x 15] intentionally omitted <==**

_for t ∈_ R _._ 

_Remark_ 124 _._ We are going to show Theorem 123 only for _−∇Eε_ . Then, provided that _ε >_ 0 is sufficiently small, Theorem 123 will also hold for any generic approximation of _−∇Eε_ which is given by Corollary 121. 

_Remark_ 125 _._ The proof of Theorem 123 will be the aim of the rest of this section. But first we would like to enlight the main idea of the proof. We would like to construct certain more and more delicate “Lyapunov-like traps” for _uε_ . Unlike for the standard level sets of a Lyapunov function, in our case, a general flow line could potentially escape from the trap (and even flow back). However, due to the global geometry of _TK,ε × TK,ε_ , we will see that _uε_ will not be able to escape. 

_Remark_ 126 _._ Let _ε ∈_ (0 _, εgood_ ]. With the help of (3.27), we are going to describe in coordinates the first two derivatives of the components of _uε_ . 

The first derivatives are immediately given by 

**==> picture [333 x 70] intentionally omitted <==**

since _uε_ is an integral of _−∇Eε_ . Recall that _di_ = 1 _− ε_ cos( _θi_ ) _κ_ ( _si_ ) _._ 

The second derivatives will be described with the help of certain (bounded) functions _{fk,ε_ : (R _/T_ Z _× S_[1] )[2] _→_ R _}k_ =1 _,...,_ 4. We point out that since we are in coordinates, we are computing the derivatives of _u_ ̇ _ε_ with respect to the flat 

61 

connection (not _∇[g]_ ). 

**==> picture [406 x 212] intentionally omitted <==**

analogously also 

**==> picture [264 x 13] intentionally omitted <==**

Moreover, 

**==> picture [411 x 230] intentionally omitted <==**

And also analogously, we have that 

**==> picture [315 x 21] intentionally omitted <==**

˜︂ where _−⟨_[˜︂] _∇⟨P, v_ 2 _[⊥][⟩][,][ ∇][E][ε][⟩]_[also splits in the terms] _[ O]_[(] _[ε]_[)+] _[O]_[(1)+] _[O]_[(1] _[/ε]_[).][Specially,] _O_ (1 _/ε_ ) terms consists of 

**==> picture [74 x 27] intentionally omitted <==**

**Lemma 127.** _There is ε_ 0 _such that c_ 1 _and c_ 2 _exist._ 

62 

_Proof._ This follows from equations (4.2) and (4.3). For _i_ = 1 _,_ 2, let us consider a family of functions _{hi,ε_ := ( _πsi_ ) _∗_ ( _−∇Eε_ ) : (R _/T_ Z _× S_[1] )[2] _→_ R _}ε∈_ (0 _,εgood_ ]. 

Note that each _hi,ε_ is a smooth function on a compact set, and hence bounded. Also lim _ε→_ 0 _d[−] i_[1] = 1. In particular, the smooth family _{hi,ε}ε∈_ (0 _,εgood_ ] smoothly extends to _ε_ = 0. By the compactness of the domain (R _/T_ Z _× S_[1] )[2] and smoothness of the family, it will be enough to verify the uniform bounds for _|hi,_ 0 _|_ . Then there will be _ε_ 0 _>_ 0 small such that the uniform bounds hold also for each _|hi,ε|_ with _ε ∈_ [0 _, ε_ 0]. And in particular, we will obtain the uniform bounds for _|s_ ̇ _i|_ . Since the uniform bound for _|hi,_ 0 _|_ is straightforward, the lemma follows. 

**Lemma 128.** _There is ε_ 0 _such that c_ 3 _and c_ 4 _exist._ 

_Proof._ Let us see the relations (4.6) and (4.7). Our aim is to bound the functions _{_ be _fi,ε_ that _}i_ =1 _f,_ 2 _i,ε_ analogously to the proof of Lemma 127.( _uε_ ( _t_ )) contains a term _θ_[̇] _i_ ( _t_ ) which mightOnly potential difficulty mightblow up as _ε →_ 0. However, this term is paired with the scalar _ε_ , so that the (potential) blowing up is canceled. 

**Lemma 129.** _For i_ = 1 _,_ 2 _, we define a function Gi on the set {x_ = ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] _| πs_ 1 _,s_ 2( _x_ ) _∈ SK} by_ 

**==> picture [88 x 15] intentionally omitted <==**

_Then there is a ε_ 0 _>_ 0 _and δ_[ˆ︁] _>_ 0 _such that for every ε ∈_ [0 _, ε_ 0) _it holds that_ 

**==> picture [137 x 15] intentionally omitted <==**

**==> picture [233 x 15] intentionally omitted <==**

_Proof._ Since we are outside of the special and diagonal points, we can find a bound _δ_[ˆ︁] _>_ 0 for the compact set _{G_ 1 = _G_ 2 = 0 _}_ . Hence, we can also find a bound _δ_[ˆ︁] _>_ 0 for a small open neighborhood _U_ of the set _{G_ 1 = _G_ 2 = 0 _}_ . Finally, we can find _ε_ 0 _>_ 0 small such that _U ⊃{|G_ 1 _| ≤ ε_[1] 0 _[/]_[2] _∧|G_ 2 _| ≤ ε_[1] 0 _[/]_[2] _[}]_[,][see][the] diffeomorphism from Lemma 58. So the lemma follows. 

_Remark_ 130 _._ By the diffeomorphism from Lemma 58 the set _{G_ 1 = _G_ 2 = 0 _}_ is described as a 4-sheet graph over _SK_ with the sheets given by 

**==> picture [185 x 14] intentionally omitted <==**

It is natural to inspect what happens to the sheets _{G_ 1 = _G_ 2 = 0 _}_ , if we extend the domain of _G_ 1 _, G_ 2 also over weakly special and weakly diagonal points. We will be denote such a extension by _G_ 1 _, G_ 2. Over a special point, two sheets of _{G_ 1 = _G_ 1 = 0 _}_ get connected by a circle _S_[1] and over diagonal points they get all connected by the torus, i.e., the diagonal ∆ _full_ . We will study these sets later in Section 6.4. 

_Remark/Notation_ 131 _._ Let us introduce the following non-negative constants 

**==> picture [351 x 17] intentionally omitted <==**

The constants are real numbers by the compactness of R _/T_ Z. Note also that _d[−] i_[1] _<_ 2 provided that _ε <_ min _{εgood,_ 1 _}._ 

63 

**Definition 132.** _Let ε >_ 0 _. Then we define a GK,ε_ _**-strip** as the set_ 

**==> picture [225 x 19] intentionally omitted <==**

_where_ 

**==> picture [279 x 52] intentionally omitted <==**

**Theorem 133.** _There is a ε_ 0 _>_ 0 _such that for each ε ∈_ (0 _, ε_ 0) _the GK,ε-strip has the following properties:_ 

- ( _i._ ) _The GK,ε-strip is a submanifold with corners of Int_ ( _MK,ε_ ) _._ 

- ( _ii._ ) _πs_ 1 _,s_ 2 _induces on GK,ε-strip a structure of a locally trivial fiber bundle with fibers diffeomorphic to the square._ 

- ( _iii._ ) _−∇Eε is strictly outward pointing on {|G_ 1 _| < εcG ∧|G_ 2 _|_ = _εcG}, strictly inward pointing on {|G_ 2 _| < εcG ∧|G_ 1 _|_ = _εcG}. If x ∈{|G_ 2 _| < εcG ∧ |G_ 1 _|_ = _εcG}, then there is δ >_ 0 _such that {xε ·Eε_ [ _−δ, δ_ ] _} ∩ GK,ε-strip_ = _xε and −∇Eε_ ( _xε_ ) = 0 _. (The analogous statement holds also for a generic approximation XEε of −∇Eε.)_ 

- ( _iv._ ) _As ε →_ 0 _, the width of GK,ε-strip (in θ_ 1 _, θ_ 2 _directions and with respect to ⟨·_ ˜︃ _, ·⟩ metric) converge to_ 0 _._ 

- ( _v._ ) _The GK,ε-strip contains in its interior all critical points (except_ ∆ _ε) of Eε on MK,ε._ 

_Proof._ Ad ( _i._ ): Let us show that the map ( _G_ 1 _, G_ 2) : _{x ∈_ (R _/T_ Z _× S_[2] )[2] _| πs_ 1 _,s_ 2 _∈ SK} →_ R[2] is stratum transverse to [ _−εcG, εcG_ ][2] for _ε ∈_ (0 _, ε_ 0), where _ε_ 0 _>_ 0 is small. Hence, let us describe the matrix _B_ := ( _dG_ 1 _, dG_ 2) _[T]_ at any point _x ∈ −_ ( _G_ 1 _, G_ 2) _[−]_[1] ([ _εcG, εcG_ ][2] ): 

**==> picture [417 x 57] intentionally omitted <==**

Let _ε_ 0 _>_ 0 be small. Then, by Lemma 129 we can bound _|⟨P, vi⟩|_ from bellow by _δ_ . Thus we have that rank( _B_ ) = 2. So we obtain the stratum transversality and by Theorem 23 ( _G_ 1 _, G_ 2) _[−]_[1] ([ _−εcG, εcG_ ][2] ) is a submanifold of (R _/T_ Z _× S_[2] )[2] . In addition, if _ε_ 0 _>_ 0 is small enough, we obtain by Lemma 129 that the _GK,ε_ -strip is in fact a submanifold of _Int_ ( _MK,ε_ ). 

Ad ( _ii._ ): Recall from above that at _x ∈ GK,ε_ -strip _∂θiGi_ = _±⟨P, vi⟩̸_ = 0. So the fiber bundle structure immediately follows from Ehresmann’s Theorem 29. The structure of each fiber follows from the diffeomorphism from Lemma 58. 

˜︂ Ad ( _iii._ ): Let us compute the quantity _⟨∇_[˜︂] _Gi, −∇Eε⟩_ along _{MK,ε ∩|Gi|_ = _εcG}_ . Observe that there is a term of the form _±_[1] _ε[⟨][P, v][i][⟩⟨][P, v] i[⊥][⟩][.]_[ Now, the constant] _cG_ was chosen such that this term is always leading, and hence its sign determines the behavior of the flow of _−∇Eε_ along the boundary of the _GK,ε_ -strip. And the 

64 

˜︂ part ( _iii._ ) for _−∇Eε_ follows. For the case of _XEε_ observe that _⟨∇_[˜︂] _Gi, −∇Eε⟩_ is _O_ (1) along the compact set _{MK,ε ∩|Gi|_ = _εcG}_ . 

Ad ( _iv._ ): It is clear that if _εa, εb ∈_ [0 _, ε_ 0) and _εa > εb_ , then _{|Gi| ≤ εb} ⊂ {|Gi| ≤ εa}._ 

Ad ( _v._ ): This immediately follows from (3.28), provided that _δK_ is sufficiently small, i.e., weakly special and weakly diagonal sets are chosen sufficiently small. 

**Lemma 134.** _Let uε be a ε-solution from pε to qε (pε, qε ∈ MK,ε) such that πs_ 1 _,s_ 2 _◦ uε ⊂ SK. Then uε ⊂ GK,ε-strip._ 

_Proof._ Until now, we were studying the space of “ _out-out_ ” chords - _MK,ε_ . This space turned out to be a submanifold of (R _/T_ Z _× S_[1] )[2] , which has a nice topology outside of weakly special and weakly diagonal pairs, see Theorem 50 and Lemma 58. Also, the behavior of _−∇Eε_ was described in Lemma 102. 

However, one can consider _MK,ε_ as one part of the splitting of the whole space (R _/T_ Z _× S_[1] )[2] . We can naturally split (R _/T_ Z _× S_[1] )[2] (or more precisely (R _/T_ Z _×S_[1] )[2] _\_ ∆ _full_ ) in four sets of chords that are classified by the conditions on their endpoints _{F_ 1[[] _[ε]_[]] ≶ 0 _, F_ 2[[] _[ε]_[]] ≶ 0 _}_ , i.e., the sets of “ _out-out, in-out, out-in, inin_ ” chords. It is not hard to construct for them analogous statements as Theorem 50, Lemma 58, and Lemma 102. That is, all of them have a manifold structure, outside of weakly special and weakly diagonal pairs, they are diffeomorphic to the product of _SK_ and the square. In addition, the behavior of _−∇Eε_ on the lower strata of these manifolds is induced from the knowledge of the behavior of _−∇Eε_ on the lower strata of _MK,ε_ . 

Next, we construct a trap for the global dynamics of _uε_ . Here, recall that _uε_ can be not only a flow line corresponding to _−∇Eε_ , but also to a generic approximation _XEε_ . Assume that _uε_ flows out at some point from _out-out_ manifold ( _MK,ε_ ), then at that point _uε_ will enter the _out-in_ manifold. But from the _out-in_ manifold, nothing can escape outside of weakly special and weakly diagonal pairs. So also _uε_ can not escape from the _out-in_ manifold, and hence could not flow to _qε_ . Contradiction. Thus _uε ⊂ MK,ε_ . See Figure 4.1 on the left. 

In fact, we can improve the localization of _uε_ . From Theorem 133 we know that _uε_ starts and ends at the _GK,ε_ -strip, and we also know the description of _−∇Eε_ along the boundary of the _GK,ε_ -strip. 

Now, we will use a similar argument as above. Let us assume that _uε_ escapes at some point from the _GK,ε_ -strip. Then _uε_ will flow through the set (manifold) _{|G_ 2 _| ≥ εcG ∩|G_ 1 _| ≤ εcG ∩ MK,ε}_ . But from this manifold _uε_ can flow only into _out-in_ manifold, and hence will never get to _qε_ , contradiction. See also Figure 4.1 on the right. 

**Lemma 135.** _There is ε_ 0 _such that c_ 5 _and c_ 6 _exist._ 

_Proof._ Observe that the only potential problematic terms in equations (4.4) and (4.5) are of the form _±⟨P, vi[⊥][⟩]_[.][However,][by][the][assumptions][on] _[u][ε]_[and][Lemma] 134 we know that _uε_ cannot leave the _GK,ε_ -strip, which gives us the desired bounds on those problematic terms. More precisely, 

**==> picture [117 x 18] intentionally omitted <==**

provided that _ε <_ min _{εgood,_ 1 _}._ 

65 

**==> picture [345 x 281] intentionally omitted <==**

Figure 4.1: Cartoon pictures of the discussed spaces restricted to fibers _πs[−]_ 1[1] _,s_ 2[((] _[s]_[1] _[, s]_[2][)).][On][the][left:][In][blue][is][the] _[out-out]_[manifold][(] _[M][K,ε]_[)][and][in][red] is the _out-in_ manifold. Black arrows describe _−∇Eε_ at the boundaries. On the right: In green is the set _{|G_ 2 _| ≤ εcG ∩|G_ 1 _| ≤ εcG ∩ MK,ε}_ ( _GK,ε_ -strip). In deep purple is the set _{|G_ 2 _| ≥ εcG ∩|G_ 1 _| ≤ εcG ∩ MK,ε}_ 

66 

**Lemma 136.** _Let ε >_ 0 _. For i_ = 1 _,_ 2 _we define a function Hi on the set {x_ = ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] _| πs_ 1 _,s_ 2( _x_ ) _∈ SK} by_ 

**==> picture [161 x 20] intentionally omitted <==**

_Then there is a ε_ 0 _>_ 0 _and c_ ˆ︁ _H >_ 0 _such that for every ε ∈_ (0 _, ε_ 0) _and every x ∈ Int_ ( _GK,ε-strip_ ) _holds that_ 

**==> picture [227 x 31] intentionally omitted <==**

_Proof._ See (4.7) for the splitting of _Hi_ ( _x_ ) in the terms _O_ ( _ε_ ) + _O_ (1) + _O_ (1 _/ε_ ). Then the lemma follows from the compactness of (R _/T_ Z _× S_[1] ) and the fact that _x ∈ GK,ε_ -strip (so the terms _⟨P, vi[⊥][⟩][/ε]_[will][not][blow][up).] 

**Definition 137.** _Let ε >_ 0 _be small. Then we define a HK,ε_ _**-strip** as the set of x ∈ Int_ ( _GK,ε-strip_ ) _such that it is satisfied that_ 

**==> picture [75 x 13] intentionally omitted <==**

_where i_ = 1 _,_ 2 _, and cH_ = ( _c_ ˆ︁ _H_ + 1) _/δ_[ˆ︁] _(recall Lemma 129 for the definition of δ_[ˆ︁] _)._ 

**Theorem 138.** _There is a ε_ 0 _>_ 0 _such that for each ε ∈_ (0 _, ε_ 0) _the HK,ε-strip has the following properties:_ 

- ( _i._ ) _The HK,ε-strip is a submanifold with corners of Int_ ( _GK,ε-strip_ ) _._ 

- ( _ii._ ) _−∇Eε is strictly outward pointing on {|H_ 1 _| < εcH ∧|H_ 2 _|_ = _εcH}, strictly inward pointing on {|H_ 2 _| < εcH ∧|H_ 1 _|_ = _εcH} and never tangent to the corners. If x ∈{|H_ 2 _| < εcH ∧|H_ 1 _|_ = _εcH}, then there is δ >_ 0 _such that {xε ·Eε_ [ _−δ, δ_ ] _} ∩ HK,ε-strip_ = _xε and −∇Eε_ ( _xε_ ) = 0 _. (The analogous statement holds also for a generic approximation XEε of −∇Eε.)_ 

- ( _iii._ ) _The HK,ε-strip contains in its interior all critical points (except_ ∆ _ε) of Eε on MK,ε._ 

_Proof._ Ad ( _i._ ): Let _x ∈ Int_ ( _GK,ε_ -strip). By (4.7), we see that the following terms are the only terms of _∂θiHi_ ( _x_ ) that can potentially blow up: 

However, we have that 

and 

**==> picture [111 x 121] intentionally omitted <==**

So the case ( _i._ ) follows from Theorem 50. 

Ad ( _ii._ ): This case is obtained from Lemma 136 and the definition of the boundary of the _HK,ε_ -strip. 

Ad ( _iii._ ): This case is analogous to the Theorem 4.7 ( _v._ ). 

67 

**Lemma 139.** _Let uε be a ε-solution from pε to qε (pε, qε ∈ MK,ε) such that πs_ 1 _,s_ 2 _◦ uε ⊂ SK. Then uε ⊂ HK,ε-strip._ 

_Proof._ The lemma is based on a similar trick as in Lemma 134. Let us assume that _uε_ leaves at some point _x_ the _HK,ε_ -strip. This can be done in two ways. 

First, if _x ∈ ∂_ ( _HK,ε_ -strip). Then _uε_ will flow through the set (manifold) _{|H_ 2 _| ≥ εcH ∩|G_ 1 _| ≤ εcH ∩ GK,ε_ -strip _}_ . From _{|H_ 2 _| ≥ εcH ∩|G_ 1 _| ≤ εcH ∩ GK,ε_ -strip _} uε_ cannot flow directly back to the _HK,ε_ -strip. So the _uε_ can only flow out from the _GK,ε_ -strip. But this is not possible by Lemma 134. Second, let _x_ be on the boundary of the _GK,ε_ -strip. But again, this could not happen by Lemma 134. Contradiction. 

**Lemma 140.** _There is ε_ 0 _such that c_ 6 _and c_ 8 _exist._ 

_Proof._ Let us consider the equations (4.7) and (4.9). The functions _{fi,ε}i_ =3 _,_ 4 are straightforward to bound. The bounds for the remaining terms follow from Definition 137 and Lemma 139. 

## **4.3 Conley index** 

We are going to recollect basic notions of Conley index theory and give an explicit construction of a regular index pair that will be used later. 

**Definition 141.** _Let φ_ = _{φ[t] }t∈_ R _be a flow on locally compact metric space M . For a compact subset N ⊂ M we put_ 

**==> picture [232 x 14] intentionally omitted <==**

_N is called an_ _**isolating neighborhood** if I_ ( _N, φ_ ) _⊂ Int_ ( _N_ ) _._ 

_A (compact) subset S ⊂ M is called_ _**isolated invariant set** if S_ = _I_ ( _N, φ_ ) _for some isolating neighborhood N ._ 

**Definition 142.** _An_ _**index pair**_ ( _N, L_ ) _for an isolated invariant set S is a pair of compact sets L ⊂ N ⊂ M such that_ 

- ( _i._ ) _S_ = _I_ ( _N \ L, φ_ ) _⊂ Int_ ( _N \ L_ ) _._ 

- ( _ii._ ) _L is an_ _**exit set** for N . That is; for all x ∈ N , if φ[t]_ ( _x_ ) _∈/ N for some t >_ 0 _, then there is τ ∈_ [0 _, t_ ] _with φ[τ]_ ( _x_ ) _∈ L._ 

- ( _iii._ ) _L is_ _**positively invariant** in N . That is; if x ∈ L and t >_ 0 _such that φ_ ([0 _, t_ ] _, x_ ) _⊂ N , then φ_ ([0 _, t_ ] _, x_ ) _⊂ L._ 

_The_ _**Conley index** associated to an isolated invariant set S is defined to be the pointed homotopy type_ ( _N/L,_ [ _L_ ]) _._ 

**Theorem 143.** _[Con78, Sal85] Let S be an isolated invariant set, then:_ 

- ( _i._ ) _S admits an index pair._ 

- ( _ii._ ) _The Conley index is invariant under the choice of the index pair._ 

68 

- ( _iii._ ) _The Conley index is invariant under continuation: Let {φλ}λ∈_ [0 _,_ 1] _be a homotopy of flows on M such that N is an isolating neighborhood for each φλ, λ ∈_ [0 _,_ 1] _. Then the Conley indices of I_ ( _N, φ_[0] ) _and I_ ( _N, φ_[1] ) _are the same._ 

**Definition 144.** _An index pair_ ( _N, L_ ) _is called_ _**regular** if the inclusion L ↪→ N is a cofibration, i.e. whenever we are given a topological space M , continuous maps f_ : _N → M and H_ : _L ×_ [0 _,_ 1] _→ M such that f_ ( _x_ ) = _H_ ( _x,_ 0) _for all x ∈ L, then there exists a continuous map F_ : _N ×_ [0 _,_ 1] _→ M extending H such that F_ ( _x,_ 0) = _f_ ( _x_ ) _for all x ∈ X._ 

_Remark_ 145 _._ For a regular index pair ( _N, L_ ) it holds that _H∗[sing]_ ( _N, L_ ; Z2) _[∼]_ = _H∗[sing]_ ( _N/L,_ [ _L_ ]; Z2). Also, the canonical inclusion of a subcomplex of a CWcomplex is a cofibration. 

**Lemma 146.** _[Sal85]An index pair_ ( _N, L_ ) _is regular if it holds that_ 

**==> picture [99 x 13] intentionally omitted <==**

_for every x ∈ L and every ε >_ 0 _._ 

**Lemma 147.** _[Sal85] Let_ ( _N, L_ ) _be an index pair for an isolated invariant set S, then there is a continuous Lyapunov function h_ : _N →_ [0 _,_ 1] _such that_ 

- ( _i._ ) _h_ ( _x_ ) = 1 _, iff φ_ ([0 _, ∞_ ) _, x_ ) _⊂ N and the omega limit of x is in S._ 

- ( _ii._ ) _h_ ( _x_ ) = 0 _, iff x ∈ L._ 

( _iii._ ) _If t >_ 0 _,_ 0 _< h_ ( _x_ ) _<_ 1 _, φ_ ([0 _, t_ ] _, x_ ) _⊂ N , then h_ ( _φ[t]_ ( _x_ )) _< h_ ( _x_ ) _._ 

_Moreover, we obtain the following. Let ε ∈_ (0 _,_ 1) _. If we replace L by Lε_ = _{x ∈ N | h_ ( _x_ ) _≤ ε}, then_ ( _N, Lε_ ) _is a regular index pair for S._ 

_Example_ 148 _._ Let _XE_ 0 be a gradient-like vector field adapted to _E_ 0. Let _p_ 0 _∈ Crit_ 1( _E_ 0) _\_ ∆0, _q_ 0 _∈ Crit_ 0( _E_ 0) _\_ ∆0 and _u_ be a 0-solution from _p_ 0 to _q_ 0. We would like to construct a smooth regular index pair ( _N, L_ ) for the invariant set _{p_ 0 _, q_ 0 _, u}._ 

Since _IndE_ 0( _q_ 0) = 0, _q_ 0 is a local minimum. Let _δ >_ 0 and _Uq_ 0 be a open neighborhood of _q_ 0. We put _Nq_ 0 := _Uq_ 0 _∩ E_ 0 _[−]_[1][[] _[E]_[(] _[q]_[0][)] _[, E]_[(] _[q]_[0][)][+] _[δ]_[]][which][is][an] embedded 2-disc, provided that _δ >_ 0 and _Uq_ 0 are sufficiently small. Then ( _Nq_ 0 _, ∅_ ) is a (regular) index pair for _q_ 0. 

From the index reasons, _p_ 0 has 1-dimensional stable and unstable manifolds; _WX[s] E_ 0[(] _[p]_[0][)] _[, W] X[ u] E_ 0[(] _[p]_[0][)] _[.]_[Let] _[δ][>]_[0][be][small.] Then _WX[s] E_ 0[(] _[p]_[0][)][⋔] _[∂E]_ 0 _[−]_[1][([] _[E]_[0][(] _[p]_[0][)] _[−] δ, E_ 0( _p_ 0)+ _δ_ ]) at two points _A, B_ . Next, there are two small closed neighborhoods _DA, DB_ of points _A, B_ in _∂E_ 0 _[−]_[1][([] _[E]_[0][(] _[p]_[0][)] _[ −][δ, E]_[0][(] _[p]_[0][) +] _[ δ]_[]),][respectively.][Now][we] put 

**==> picture [365 x 19] intentionally omitted <==**

and 

**==> picture [155 x 14] intentionally omitted <==**

69 

See also Figure 4.2. By the construction, if _δ >_ 0, _DA, DB_ are small enough, then _Np_ 0 is a (smooth) 2-manifold with corners and ( _Np_ 0 _, Lp_ 0) is an index pair of _p_ 0. Also note that _Lp_ 0 has two connected components. However, the index pair is not necessarily regular. We also remark that by Hartman-Grobman Theorem [PT93] there is a homeomorphism conjugating _XE_ 0 with _DXE_ 0( _p_ 0) around _p_ 0. Which describes the dynamics on _Np_ 0. We will leave ( _Np_ 0 _, Lp_ 0) for now and construct an index pair for _{p_ 0 _, q_ 0 _, u}_ . 

**==> picture [9 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
A<br>**----- End of picture text -----**<br>


**==> picture [138 x 130] intentionally omitted <==**

**----- Start of picture text -----**<br>
p 0<br>B<br>**----- End of picture text -----**<br>


Figure 4.2: The neighbourhood _Up_ 0 of the critical point _p_ 0. In purple, there are neighbourhoods _DA, DB_ of points _A, B_ , respectively. 

Let _C_ be the unique point in _u ∩ ∂Nq_ 0. Let _A_ 1 _,q_ 0 _∈ ∂Nq_ 0 _\ C_ . If _A_ 1 _,q_ 0 is sufficiently close to _C_ , then the set 

**==> picture [175 x 19] intentionally omitted <==**

consists of the unique point (=: _A_ 1 _,p_ 0) and we can assume that _A_ 1 _,p_ 0 _∈ DA_ . This follows from the continuous dependence of the vector fields on the initial conditions (Remark 208) and the Hartman-Grobman Theorem. Similarly, we can take another _A_ 2 _,q_ 0 _∈ Nq_ 0 close to _C_ such that the _A_ 2 _,p_ 0 is on the same connected component of _Lp_ 0 as _A_ 1 _,p_ 0. We can choose _A_ 2 _,q_ 0 such that the arc _A, A_ 2 _,p_ 0 inside _DA_ is shorter then _A, A_ 1 _,p_ 0. 

This gives us a rectangular tube _A_ 1 _,q_ 0 _, A_ 1 _,p_ 0 _, A_ 2 _,p_ 0 _, A_ 2 _,q_ 0 which is from _DA_ to _∂Nq_ 0 smoothly foliated by the flow lines. Here we recall that because _A_ 1 _,p_ 0 _, A_ 2 _,p_ 0 are close to _C_ , the tube contains no critical point of _E_ 0. 

Then we can consider a smooth section _ℓA_ of this foliation from _A_ 2 _,p_ 0 to _A_ 1 _,q_ 0 that is transverse to the leaves. In another words, _ℓA_ ⋔ _XE_ 0. See Figure 4.3 left. 

Now we construct analogously a tube from _DB_ to _∂Nq_ 0 and a section _ℓB_ . Then we obtain a hull around _{p_ 0 _, q_ 0 _, u}_ connecting _Np_ 0 and _Nq_ 0 with _ℓA_ and _ℓB_ , which give us almost _N_ . We only need to deform the remaining two components of the hull, which are not transverse to _XE_ 0. This can be done by the same trick as above, and hence we obtain a regular index pair ( _N, L_ ). See Figure 4.3. Observe that by the construction, _N_ is a smooth manifold with corners and _L_ is contractible. 

70 

**==> picture [414 x 344] intentionally omitted <==**

**----- Start of picture text -----**<br>
∂−U<br>p 0 p 0<br>A 2 ,p 0<br>A 1 ,p 0<br>u<br>u<br>C<br>A 1 ,q 0<br>A 2 ,q 0<br>q 0 q 0<br>**----- End of picture text -----**<br>


Figure 4.3: _On the left:_ In green the rectangular tube _A_ 1 _,q_ 0 _, A_ 1 _,p_ 0 _, A_ 2 _,p_ 0 _, A_ 2 _,q_ 0 connecting _Np_ 0 and _Nq_ 0. In blue the section _ℓA_ . _On the right:_ The regular index pair ( _N, L_ ) for _{p_ 0 _, q_ 0 _, u}_ . Here in red is the exit set _L_ . 

71 

## **4.4 Morse homology** 

Using the Conley index theory, we define a Morse homology for manifolds with corners and introduce the Morse Homology Theorem 158. 

_Assumption_ 149 _._ In this section, we will assume the following. ( _M, g_ ) will be a compact Riemannian _n_ -manifold with corners. Next, _f_ : _M →_ R will be a Morse function such that _Crit_ ( _f_ ) _∩ ∂M_ = _∅_ . 

**Definition 150.** _A gradient-like vector field Xf (adapted to f ) is said to be_ _**regular on** ∂M if Xf is not tangent to any_ ( _n −_ 1) _-face of M . Then ∂−M will denote the closure of the set of all x ∈ ∂M such that Xf is strictly outwardpointing at x._ 

_Remark_ 151 _._ Let _Xf_ be a gradient-like vector field which is regular on _∂M_ . Then _∂−M_ is a manifold with corners with stratification canonically induced from _M_ . 

**Definition 152.** _Let Xf be a gradient-like vector field on M , then we put_ 

**==> picture [139 x 26] intentionally omitted <==**

_(In particular, Crit_ ( _f_ ) _⊂SXf .)_ 

**Lemma 153.** _Let Xf be a gradient-like vector field which is regular on ∂M . Then_ ( _M, ∂−M_ ) _is a regular index pair for the isolated invariant set SXf . And in particular, SXf is compact._ 

_Proof._ By the assumption of _Xf_ on _∂M_ it holds that _SXf_ = _I_ ( _M, ϕXf_ ). Since _M_ is compact, _SXf_ is compact too. _∂−M_ is a positively invariant exit set of _M_ , so ( _M, ∂−M_ ) is an index pair for _SXf_ . Then by Lemma 146, the index pair ( _M, ∂−M_ ) is regular. 

**Lemma 154.** _Let Xf be a gradient-like vector field which is regular on ∂M . If a gradient-like vector field Yf is sufficiently C_[0] _-close to Xf , then Yf is also regular on ∂M with the same ∂−M . And in particular,_ ( _M, ∂−M_ ) _is an regular index pair for SYf ._ 

_Proof._ The lemma immediately follows from the compactness of _M_ and the fact that the assumption for _Xf_ on _∂M_ is open. 

**Definition 155.** _Let Xf be a Morse-Smale vector field which is regular on ∂−M . Then we define a_ _**Morse chain complex** as the following graded abelian groups C∗_ ( _Xf_ ) _together with a differential ∂∗[m]_[:] _[ C][∗]_[(] _[X][f]_[)] _[ →][C][∗−]_[1][(] _[X][f]_[)] _[.]_ 

_For i ∈_ N0 _, we generate Ci_ ( _Xf_ ) _by the critical points as_ 

**==> picture [141 x 13] intentionally omitted <==**

_Next for p ∈ Criti_ ( _f_ ) _we put_ 

**==> picture [296 x 26] intentionally omitted <==**

_where_ #2 _MXf_ ( _p, q_ ) _means modulo_ 2 _count of elements of MXf_ ( _p, q_ ) _. Then we extend ∂[m] by_ Z2 _-linearity on the whole Ci_ ( _Xf_ ) _._ 

_Then the_ _**Morse homology** is defined by_ 

**==> picture [129 x 30] intentionally omitted <==**

72 

_Remark_ 156 _._ Let _Xf_ be a Morse-Smale vector field, _p ∈ Crit∗_ ( _f_ ) and _q ∈ Crit∗−_ 1( _f_ ). By Remark 114, there are no flow lines between the critical points of the same index, so the set 

**==> picture [283 x 14] intentionally omitted <==**

is closed. Since _M_ is compact, _WXf_ ( _p, q_ ) _∪{p, q}_ is compact too. It follows that _MYf_ ( _p, q_ ) is a finite set, hence the sum in (4 _._ 10) is finite too. 

**Lemma 157.** _[Sal90, RV14]Let Xf be a Morse-Smale vector field which is regular on ∂M . Then_ 

**==> picture [242 x 13] intentionally omitted <==**

_Sketch proof._ We present two different ways how to show (4 _._ 12). Both of them strongly depend on the isolating property of _SXf_ . 

_First approach:_ 

Let _p ∈ Criti_ ( _f_ ) and _q ∈ Criti−_ 2( _f_ ). Let us consider any sequence of gradientlike trajectories of _WXf_ ( _p, q_ ). Then the sequence converges subsequentially in Floer-Gromov _Cloc_[1][sense [FN20] to a broken gradient-like flow line from] _[ p]_[ to] _[ q]_[ that] passes through a single element of _Criti−_ 1( _f_ ). This induces the compactification _MXf_ ( _p, q_ ) of _MXf_ ( _p, q_ ) in the Floer-Gromov topology, see [FN20]. 

Hence, _MXf_ ( _p, q_ ) has a structure of a compact 1-dimensional manifold with boundary. In particular, _MXf_ ( _p, q_ ) is diffeomorphic to a union of circles and closed intervals, which has an even number of boundary points. 

Since 

**==> picture [215 x 31] intentionally omitted <==**

the relation (4 _._ 12) follows. 

_Second approach:_ 

Let _r ∈ Critj_ ( _f_ ). Then by Hartman-Grobman Theorem [PT93] we can quickly find a regular index pair ( _Nr, Lr_ ) for _r_ , see also Example 148. In particular, _Hj[sing]_ ( _Nr, Lr_ ; Z2) _[∼]_ = Z2 which gives an identification 

**==> picture [187 x 27] intentionally omitted <==**

Let _p ∈ Criti_ ( _f_ ) and _q ∈ Criti−_ 1( _f_ ). Next, let _SXf_ ( _p, q_ ) be the isolated invariant set from (4 _._ 11) and ( _N_ 2 _, N_ 0) be some regular index pair for _SXf_ ( _p, q_ ). Then we define _N_ 1 := _N_ 1 _∪_ ( _N_ 2 _∩ Ma_ ), where _Ma_ = _{x ∈ M | f_ ( _x_ ) _≤ a}_ for some _a ∈_ ( _f_ ( _q_ ) _, f_ ( _p_ )). Now we introduce an isomorphism 

**==> picture [241 x 16] intentionally omitted <==**

as the composition 

**==> picture [409 x 16] intentionally omitted <==**

where the first and the third map are isomorphisms induced by the homotopy independence of the Conley index. The map _∂_ is given by the LES for the triple ( _N_ 0 _, N_ 1 _, N_ 2) _._ 

73 

In fact, using a certain deformation argument for _Xf_ outside of _SXf_ ( _p, q_ ), one can choose a nice _N_ 2 _, N_ 0 and show that ∆ _i_ ( _p, q_ ) actually counts the gradient-like trajectories from _p_ to _q_ . 

Now, we would like to inspect the global properties of the map ∆ _∗_ . Let us define 

**==> picture [252 x 17] intentionally omitted <==**

which are compact isolated invariant subsets of _SXf_ . Then by [Con78] there is a filtration 

**==> picture [322 x 13] intentionally omitted <==**

such that each ( _Mi, Mj−_ 1) is a regular index pair for _SX[i,j] f_[.] 

Hence, we obtain a commutative diagram 

**==> picture [396 x 63] intentionally omitted <==**

and in particular also relation (4 _._ 12) _._ 

**Morse Homology Theorem 158.** _[Sal90, RV14]Let Xf be a Morse-Smale vector field which is regular on ∂M . Then_ 

**==> picture [187 x 15] intentionally omitted <==**

_Sketch proof._ The theorem follows from the standard argument which combines LESs of the triples from filtration (4 _._ 13). 

## **4.5 Map** 

In this section, we finally combine the uniform bounds together with Conley index theory and show the correspondence between the 0-solutions and the _ε_ -solutions. 

**Definition 159.** _Let pε, qε ∈ Crit_ ( _Eε_ ) _and XEε be a gradient-like vector field. Then_ 

**==> picture [81 x 17] intentionally omitted <==**

_will denote the restriction of the space of (unparametrized) trajectories from MXEε_ ( _pε, qε_ ) _to the trajectories that lie completely in MK,ε._ 

**Theorem 160.** _Let p_ 0 _∈ Cr_ 1( _E_ 0) _\_ ∆0 _, q_ 0 _∈ Cr_ 0( _E_ 0) _\_ ∆0 _and pε, qε be their unique corresponding critical points of Eε in MK,ε. Let XE_ 0 _and XEε be generic approximations of −∇E_ 0 _and −∇Eε, respectively (see Corollary 121). Then for ε >_ 0 _sufficiently small, there is a multivalued function_ 

**==> picture [193 x 15] intentionally omitted <==**

_with the following properties:_ 

**==> picture [324 x 15] intentionally omitted <==**

74 

- ( _ii._ ) _All elements in_ Φ _[ε] p_ 0 _,q_ 0[(] _[u]_[)] _[are][homotopic][through][curves][in][M][K,ε][with][fixed] endpoints pε, qε._ 

- ( _iii._ ) _For each two different u,_ ˆ︁ _u ∈MXE_ 0 ( _p_ 0 _, q_ 0) _it holds that_ Φ _[ε] p_ 0 _,q_ 0[(] _[u]_[)] _[∩]_[Φ] _[ε] p_ 0 _,q_ 0[(] _[u]_[ˆ︁][) =] _∅ (as elements in the set MXEε_ ( _pε, qε_ ) _) ._ 

- ( _iv._ ) Φ _[ε] p_ 0 _,q_ 0 _[is][surjective.]_ 

_Moreover,_ 

**==> picture [288 x 16] intentionally omitted <==**

_Proof._ Follows from Lemmata 162 and 163. 

_Remark_ 161 _._ The count over Z2 in Theorem 160 ( _i._ ) is due to the fact that we considered for simplicity the Morse homology over Z2. However, one can expect that the count will also work over Z, see [Sal90, RV14] for the Morse homology over Z. Later, using the techniques of Multiple-time scale dynamics in Chapter 6, we will show that Φ _[ε] p_ 0 _,q_ 0[is][in][fact][a][bijection.] 

**Lemma 162.** _If ε >_ 0 _is sufficiently small, then there is a multivalued function_ Φ _[ε][M][X][→M][X][which][is]_[mod][2] _[injective,][i.e.]_[Φ] _[ε] p_ 0 _,q_ 0[:] _E_ 0[(] _[p]_[0] _[, q]_[0][)] _Eε_[(] _[p][ε][, q][ε]_[)] _p_ 0 _,q_ 0 _satisfies properties_ ( _i._ ) _−_ ( _iii._ ) _from Theorem 160._ 

_Proof._ Let _u ∈MXE_ 0 ( _p_ 0 _, q_ 0). The strategy is the following. First, we will find a compact submanifold with corners _N ⊂_ (R _/T_ Z)[2] such that ( _N, ∂−N_ ) is a regular index pair for _{p_ 0 _, q_ 0 _, u}._ Then, we construct a lift of _N_ to _Nε ⊂ MK,ε_ , where in particular _pε, qε ∈ Nε_ . Next, due to the genericity assumptions of _XE_ 0 we will be able to apply Morse homology Theorem 158 to _XE_ 0 _|Nε_ . Hence, we obtain that 

**==> picture [231 x 15] intentionally omitted <==**

where the last equality follows from the fact that the constructed 4-manifold _Nε_ is contractible and _∂−Nε_ is contractible too. Then, we focus on how the relative Morse homology was computed. Since _pε, qε_ will be the only critical points of _Eε_ inside _Nε_ , it means that by the homology reasons 

**==> picture [120 x 13] intentionally omitted <==**

In other words, for _u_ we find 1 mod 2 of elements in _MXEε_ ( _pε, qε_ ). This gives us the assignment _u ↦→_ Φ _[ε] p_ 0 _,q_ 0[(] _[u]_[)][and][also][the][property][(] _[i.]_[).][Then][(] _[ii.]_[)][is][clear][from] the contractibility of _Nε_ . Since ( _N, ∂−N_ ) is a regular index pair for _{p_ 0 _, q_ 0 _, u}_ , there could not be any other element of _MXE_ 0 ( _p_ 0 _, q_ 0) inside _N_ other than _u_ (recall that in _MXE_ 0 ( _p_ 0 _, q_ 0) we modded out the reparametrizations). Then, from the canonical choice of the lift _Nε_ , the case ( _iii._ ) will follow. 

So it remains to do few things: to construct _N_ , to show that _Nε_ and _XEε|Nε_ satisfy the assumptions of Morse homology Theorem 158, to verify the contractibility of _Nε, ∂−Nε_ and the case ( _iii._ ). 

_Construction of N :_ 

For the construction of the regular index pair ( _N, ∂−N_ ), we consider precisely the index pair ( _N, L_ ) from Example 148. We remark that due to the generic assumptions on _XE_ 0, the submanifold _N_ lies inside the standard set _SK_ . _Assumptions of Morse homology Theorem 158:_ 

75 

We define _Nε_ as the subset of the _GK,ε_ -strip (Definition 132) that projects under _πs_ 1 _,s_ 2 to _N_ . Since _N ⊂ SK_ and _N_ is contractible, by Theorem 133 we obtain that _Nε −−−→πs_ 1 _,s_ 2 _N_ is a trivial fiber bundle with fibers diffeomorphic to the square [ _−_ 1 _,_ 1][2] . In particular, _Nε_ is a manifold with corners. 

Let us inspect _XEε_ along the 3-faces of _Nε_ . They are of two kinds. Elements of the first group are given by the equations _Gi_ = _εcG_ ; here the behavior of _XEε_ is already known from Theorem 133. The second group consists of 3-faces arising from the boundary sides of _N_ . So let us focus on this group. 

By the definition, the compact boundary of _N_ can be finitely covered by the regular 0-sets of some smooth locally supported functions _fj_ ( _s_ 1 _, s_ 2). Then the intersections of these level sets give us corners of _N_ . In particular, by the construction of _N_ , it holds that 

**==> picture [78 x 21] intentionally omitted <==**

along the level sets of _fj_ . Here, recall that _⟨·_[˜︃] _, ·⟩_ is our notation for the standard metrics on coordinate charts ( _s_ 1 _, s_ 2) or ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2). 

Moreover, the functions _fj_ give us canonically the covering of the remaining boundary sides of _Nε_ by the regular 0-sets of the functions _fj ◦ πs_ 1 _,s_ 2( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2). We need to verify that the relations 

**==> picture [276 x 21] intentionally omitted <==**

and 

**==> picture [309 x 21] intentionally omitted <==**

hold along the corresponding points of the level sets of _fj_ and _fj ◦ πs_ 1 _,s_ 2. First, observe that clearly[˜︂] _∇fj_ and[˜︂] _∇_ ( _fj ◦ πs_ 1 _,s_ 2) depend only on variables _s_ 1 _, s_ 2, and _∇_ ˜︂ _fj_ = ( _πs_ 1 _,s_ 2) _∗∇_[˜︂] ( _fj ◦ πs_ 1 _,s_ 2). Also, by Remarks 95 and 98 and Corrollary 121 the _si_ -components of _∇E_ 0 and _∇Eε_ differ only by _O_ ( _ε_ )-terms. 

Since _∂N_ is compact, we can bound each _|⟨∇_[˜︂] _fj, XE_ 0 _⟩|_ from bellow by some constant _c_ 0 _>_ 0. Moreover, since (R _/T_ Z _× S_[1] )[2] is also compact, it holds that 

**==> picture [149 x 13] intentionally omitted <==**

provided that _ε >_ 0 is sufficiently small. And the relations (4.15) and (4.16) hold. Hence, the assumptions of Morse homology Theorem 158 are satisfied. 

_Contractibility:_ 

By the above, it holds that 

**==> picture [355 x 14] intentionally omitted <==**

In particular, _∂−Nε_ is contractible, which is also the case for _Nε_ . _The case_ ( _iii._ ) _:_ Now, this is immediate from the construction of _N_ and _Nε_ . 

**Lemma 163.** _If ε >_ 0 _is sufficiently small,_ Φ _[ε] p_ 0 _,q_ 0 _[satisfies][property]_[(] _[iv.]_[)] _[from] Theorem 160. In addition, the equality of moduli spaces_ (4 _._ 14) _holds._ 

76 

_Proof._ By contradiction. Let us assume that there is a sequence _{uεn}_ of _εn_ - solutions with _εn →_ 0 that are not images of the multivalued maps Φ _[ε] p[n]_ 0 _,q_ 0[.][Which] is by the proof Lemma 162 equivalent to the assumption that _uεn_ are not in any of the sets _Nεn_ . 

On the other hand, recall the uniform bounds from Theorem 123 on _uεn_ . Hence, by [FN20, Thm 4.7], the _πs_ 1 _,s_ 2( _uεn_ ) converge in Floer-Gromov _Cloc_[1][sense] to some broken flow line from _p_ 0 to _q_ 0. But since _XE_ 0 is Morse-Bott-Smale, by the index reason, the limit is in fact a 0-solution. We will denote it by _u_ . Hence, for _n ≫_ 0 it holds that _πs_ 1 _,s_ 2( _uεn_ ) _⊂ N_ . Recall also that _u_ is the only 0-solution inside _N_ . 

Now, since _πs_ 1 _,s_ 2( _uεn_ ) _⊂ N_ , in particular _uεn_ avoids special and diagonal points. Hence, we can apply Lemma 134 and thus, each _uεn ⊂ GK,εn_ -strip. But, by the construction, _Nεn_ = _πs[−]_ 1[1] _,s_ 2[(] _[N]_[)] _[ ∩][G][K,ε] n_[-strip.][Hence,][for] _[n][ ≫]_[0,] _[u][ε] n[⊂][N][ε] n_[.] Contradiction. 

Since _GK,εn_ -strip _⊂ MK,ε_ , we in fact also showed (4 _._ 14). 

_Remark_ 164 _._ Note that in the proof of Lemma 163 for the Floer-Gromov convergence of _πs_ 1 _,s_ 2( _uεn_ ) we needed in fact only the uniform bounds for derivatives of _si_ -coordinates. 

On the other hand, the use of the uniform bounds for derivatives of _θi_ - coordinates inside the strips tells us interesting information about the geometry of the trajectories _uεn_ in _MK,ε_ . They Floer-Gromov _Cloc_[1][converge to the algebraic] ODE, which turns out to be the slow trajectory between p0 and q0, see Lemma 246. This can be seen as an indication for the use of the Multiple-time scale dynamics to study our problem, see Chapter 6. 

77 

## **5. Morse flow trees** 

In this chapter, we introduce certain Morse flow trees that will be counted later in cord algebras for knots and tori. In [Ng05b], the notion of Morse flow trees for knots was outlined. Later, in [Pet24], the Morse flow trees were used in more detail for the Morse model of Cord algebra for knots with loop space coefficients. See also [Oka24] for Morse chains with a coproduct that were motivated by the language of [Abo13]. 

For further purposes, it will be useful for us to have various models of Morse flow trees and describe the translations between them. In more detail, motivated by [Mes16], we define trees as preimages of certain evaluation maps. This will allow us later to control the trees under the deformations in the adiabatic limit problem. Next, in the configuration space (R _/T_ Z)[2] , we also use an iterative construction of trees under the forward-flow, see [Pet24]. This will be suitable for achieving the transversality conditions. However, for tori we use in the configuration space (R _/T_ Z _× S_[1] )[2] an iterative construction of trees under the backward-flow. This is slightly technical, but it will allow us to track the trees better and keep the dimension of tracked trajectories constant. 

## **5.1 Trees for knots** 

_Remark/Notation_ 165 _._ We would like to introduce few notions from graph theory. For more about graphs, see, for example [MJN00]. 

A **rooted tree** _T_ is a connected acyclic graph, where one vertex has been designated the **root** . _V_ ( _T_ ) _, E_ ( _T_ ) will denote the sets of all vertices/edges of _T_ , respectively. 

**Inner vertices** are the vertices of _T_ that have the valence higher than 1. We will assume that the _valence of interior vertices is equal to_ 3 _and the valence of the root is equal to_ 1. The set of interior vertices will be denoted by _Vint_ ( _T_ ). A **leaf** is any vertex of _T_ that is not an inner vertex or the root. The set of leaves will be denoted by _Vleaf_ ( _T_ ). Let _m_ = _|Vleaf_ ( _T_ ) _|_ . 

The paths from the root induce the canonical orientation of _T_ . 

We consider the tree _T_ with an **ordering** that is an assignment of each leaf to the unique number from _{_ 1 _, . . . , m}_ . Let _T_ 1 and _T_ 2 be two rooted trees with orderings. We say that _T_ 1 and _T_ 2 are **isomorphic** if there is a graph isomorphism from _T_ 1 to _T_ 2 that preserves leaves together with their ordering. An equivalence class of isomorphic rooted trees is called an **ordered tree** and will be still denoted by _T_ . The set of all ordered trees (with _m_ leaves) will be denoted by _♣_ ( _♣m_ ). 

An edge _e_ is called **interior** if the endpoints of _e_ are interior vertices. The set of all interior edges will be denoted by _Eint_ ( _T_ ). Using the orientation on _T_ , we will say that one of the endpoints of any edge _e_ is the **incoming vertex** _ve[in]_ and the other is the **outcoming vertex** _ve[out]_[.] 

For any vertex _v ∈ Vint_ ( _T_ ) the orientation on _T_ induces the unique **incoming edge** _ev_ such that _v_ belongs to _ev_ . Moreover, using the ordering on _T_ , we will distinguish the two remaining edges with endpoint at _v_ - the **lower edge** _e[L] v_[and] the **upper edge** _e[U] v_[.][The convention is that the unique path from the root to the] leaf, which goes through _e[U] v_[,][will][end][in][the][leaf][with][a][higher][number][than][the] 

78 

path through _e[L] v_[.][By] _[e][r]_[we][will][denote][the][unique][edge][that][contains][the][root.] _Remark_ 166 _._ Let _T ∈♣_ . A **flag** in _T_ is a pair ( _v, e_ ), where _v ∈ Vint_ ( _T_ ) and _e ∈ E_ ( _T_ ). We can naturally collect flags in two ways: by the common edges and by the common interior vertices. This will motivate us for the reordering functions in Definitions 186 and 203. See also [CV23]. 

_Remark/Notation_ 167 _._ We will be using three notions for **chords on** _K_ . If _γ_ : R _/T_ Z _→_ R[3] is an arc reparametrization of _K_ , then any chord can be seen as a pair ( _s_ 1 _, s_ 2) _∈_ (R _/T_ Z)[2] or a vector _P_ = _γ_ ( _s_ 2) _− γ_ ( _s_ 1). Moreover, the chord can also be seen as a smooth map _cs_ 1 _,s_ 2 : [0 _,_ 1] _→_ R[3] defined by 

**==> picture [167 x 13] intentionally omitted <==**

**Definition 168.** _[Ng05b] Let p_ 0 _∈ Crit_ 1( _E_ 0) _\_ ∆0 _and q_ 0[1] _[, . . . , q]_ 0 _[m][∈][Crit]_[0][(] _[E]_[0][)] _[\]_[∆][0] _[.] Let T ∈♣m. Let XE_ 0 _be a gradient-like vector field adapted to E_ 0 _. A_ _**Morse flow tree from** p_ 0 _**to** q_ 0[1] _[, . . . , q]_ 0 _[m]_ _**[modeled][on]**[T]_ _**[(in][the][configuration][space]**_ (R _/T_ Z)[2] _**)** is an ordered tree T together with the following assignment:_ 

- ( _i._ ) _If m_ = 1 _then the unique edge corresponds to a standard flow line of ϕ[t] XE_ 0 _with t ∈_ R _._ 

   - _If m >_ 1 _, then the interior edges correspond to positive finite length partial flow lines of ϕ[t] XE_ 0 _[.][Then][the][other][edges][correspond][to][partial][flow][lines][of] ϕ[t] XE_ 0 _[parametrized][by][t][ ∈]_[[0] _[,][ ∞]_[)] _[or][t][ ∈]_[(] _[−∞][,]_[ 0]] _[.]_ 

- ( _ii._ ) _The root corresponds to p_ 0 _._ 

- ( _iii._ ) _i-th leaf is identified with q[i]_ 

      - 0 _[.]_ 

- ( _iv._ ) _The tree is allowed to bifurcate at the points where the flow lines consist of nontrivial chords intersecting K by their interior._ 

_Let_ ( _s_ 1 _, s_ 2) _be such a chord and s_ 3 _corresponds to the intersection of cs_ 1 _,s_ 2 _|_ (0 _,_ 1) _with K. Then we jump to the chords_ ( _s_ 1 _, s_ 3) _,_ ( _s_ 3 _, s_ 2) _and continue to flow with ϕ[t] XE_ 0 _[.][Now,][the][triple][{]_[(] _[s]_[1] _[, s]_[2][)] _[,]_[ (] _[s]_[1] _[, s]_[3][)] _[,]_[ (] _[s]_[3] _[, s]_[2][)] _[}][is][assigned][to][the][cor-] responding interior vertex v of the tree T . The partial flow-line starting from_ ( _s_ 1 _, s_ 3) _will correspond to the edge_ e _[L] v[and][the][partial][flow-line][starting] from_ ( _s_ 3 _, s_ 2) _will correspond to the edge_ e _[U] v[.][See][also][Figure][5.1.]_ 

_The_ _**set of all Morse flow trees from** p_ 0 _**to** q_ 0[1] _[, . . . , q]_ 0 _[m]_ _**[modeled][on]**[T] is denoted by_ 

_♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, . . . , q]_ 0 _[m]_[)] _[.]_ 

_The set of all Morse flow trees for all choices of m, T , p_ 0 _∈ Crit_ 1( _E_ 0) _\_ ∆0 _and q_ 0[1] _[, . . . , q]_ 0 _[m][∈][Crit]_[0][(] _[E]_[0][)] _[ \]_[ ∆][0] _[will][be][denoted][by][♣][X] E_ 0 _[.] If m_ = 1 _, we mod out the natural_ R _-action, then_ 

**==> picture [164 x 16] intentionally omitted <==**

_Remark_ 169 _._ If in Definition 168 we demand that at least one edge corresponds to a constant or a broken (partial) flow line of _ϕ[t] XE_ 0[,][then][the][resulted][tree][will] be called **broken Morse flow tree** . 

We stress that even for the broken Morse flow trees we do not allow that _q_ 0 _[i][∈]_[∆][0][for][some] _[i][ ∈{]_[1] _[, . . . , m][}][.]_ 

79 

**==> picture [405 x 223] intentionally omitted <==**

**----- Start of picture text -----**<br>
ev<br>v<br>e [L] v e [U] v<br>**----- End of picture text -----**<br>


Figure 5.1: On the left: a bifurcation of a Morse flow tree in the vertex _v_ . _ev_ is the incoming edge and _e[L] v[,][ e][U] v_[are][the][lower][and][upper][edges,][respectively.][Recall] that the orientation of the edges agrees with the flow of _XE_ 0. On the right: the realization of the bifurcation of the tree on the knot _K_ in R[3] . 

**Lemma 170.** _Let p_ 0 _∈ Crit_ 1( _E_ 0) _\_ ∆0 _and q_ 0[1] _[, . . . , q]_ 0 _[m][∈][Crit]_[0][(] _[E]_[0][)] _[ \]_[ ∆][0] _[.][Let] T ∈♣m. If K is a generic knot and XE_ 0 _is a generic perturbation of −∇E_ 0 _, then ♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, . . . , q]_ 0 _[m]_[)] _[ is a zero dimensional compact manifold.][In addition,] there are no broken Morse flow trees, and for m ≫_ 0 _the set ♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, . . . , q]_ 0 _[m]_[)] _is empty._ 

_Remark_ 171 _._ Lemma 170 was done in [Pet24, lem 2.23] with a small mistake. First, we are going to show Lemma 170 heuristically and later present (hopefully) a correct argument. 

_Heuristic proof._ Let _m_ = 1. Since ∆0 is the global minimum of _E_ 0, we can restrict the flow _ϕ[t] XE_ 0[to][(][R] _[/T]_[Z][)][2][without][a][small][open][neighborhood][of][∆][0][such][that] _XE_ 0 is outward-pointing from the boundary. Then the case _m_ = 1 is precisely Remark 156. For _m >_ 1 we obtain _♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, . . . , q]_ 0 _[m]_[)][as][an][intersection][of] certain transversality conditions; let us compute 

**==> picture [401 x 138] intentionally omitted <==**

where the terms in (1) are obtained as follows. The first two summands are coming from the dimensions of the unstable and stable manifolds, respectively. 

80 

The third summand is the contribution of interior edges. They contribute by the spaces of positive finite length trajectories. Now only the terms corresponding to constraints remain. The first group of these terms is realized by the transversality conditions between the stable and unstable manifolds, and the space of finitelength trajectories. The terms in the last group are determined by the fact that the condition for a chord to intersect the knot in its interior is of codim 1. 

The ambient space is compact and by the dimension reasons there will be generically no nontrivial subsequential convergence phenomena (see [Mes16, thm 4.22]), and hence _♣XE_ 0 ( _T_ ; _p_ 0 _,_ ; _q_ 0[1] _[, . . . , q]_ 0 _[m]_[)][is][subsequentially][compact.] 

In more detail, the phenomenon of broken trees will be of too high codimension, so it will be avoidable for trees that satisfy certain generic conditions. To achieve the transversality, it will be more suitable for us to impose the perturbations of _−∇E_ 0 geometrically in the configuration space, which we will do later. 

To see that there are no trees with too many bifurcations, one has to estimate how much any branch is shorter after a bifurcation. 

**Definition 172.** _Let us introduce the evaluation map_ 

ev _**R**_ : [0 _,_ 1] _×_ (R _/T_ Z)[2] _×_ (R _/T_ Z)[2] _×_ (R _/T_ Z)[2] _→_ (R _/T_ Z)[3] _×_ R[3] 

_as_ 

**==> picture [255 x 103] intentionally omitted <==**

_where the coordinates_ ( _s_ 1 _, s_ 2 _, y_ 1 _, y_ 3 _, z_ 2 _, z_ 3) _are induced by the single arc length parametrization γ_ : R _/T_ Z _→ K. By Remark 43,_ ev _**R** is a well-defined smooth map. See Figure 5.2._ 

_Next,_ evˆ︃ _**R** will denote the restriction of_ ev _**R** to_ (0 _,_ 1) _×_ ((R _/T_ Z)[2] _\_ ∆0)[3] _. Then the subset R ⊂_ (R _/T_ Z)[2] _is defined as_ 

**==> picture [114 x 19] intentionally omitted <==**

_and called the_ _**space of chords meeting** K_ _**in their interior** . We also define two other sets_ 

**==> picture [271 x 19] intentionally omitted <==**

_Remark_ 173 _._ Due to the choice of coordinates, we can canonically see all _R, R[L] , R[U]_ as subsets of the single (R _/T_ Z)[2] . In particular, it is reasonable to admit that we chose more coordinates in Definition 172 than we needed. However, the presented definition of ev _**R**_ will be better for various notions of trees _♣XE_ 0 . 

81 

**==> picture [179 x 152] intentionally omitted <==**

**----- Start of picture text -----**<br>
cz 3 ,z 2<br>cs 1 ,s 2<br>cy 1 ,y 3<br>**----- End of picture text -----**<br>


Figure 5.2: Geometrically, we can see a zero of ev _**R**_ (or evˆ︃ _**R**_ ) as a coincidence of _cs_ 1 _,s_ 2 with the union of _cy_ 1 _,y_ 3 and _cz_ 3 _,z_ 2. The coincidence is depicted as the dashed chord. 

_Remark_ 174 _._ For further discussions, it will be useful to have described the differential _d_ ev _**R**_ at a point _x_ = ( _ℓ, s_ 1 _, s_ 2 _, y_ 1 _, y_ 3 _, z_ 2 _, z_ 3) 

**==> picture [390 x 56] intentionally omitted <==**

Note that the last row of the matrix is in fact a 3 _×_ 7 matrix. 

The following lemma is a small extension of [CELN16, lem 7.10] 

**Lemma 175.** _For a generic K the set_ evˆ︃ _**R** −_ 1(0) _is a_ 1 _-dimensional submanifold−_ 1 _and the maps πs_ 1 _,s_ 2 _, πy_ 1 _,y_ 3 _, πz_ 2 _,z_ 3 _are immersions, when restricted to_ evˆ︃ _**R**_ (0) _._ 

_Moreover, the closure R is a compact immersed_ 1 _-dimensional submanifold of_ (R _/T_ Z)[2] _\_ ∆0 _with finitely many transverse self-intersections and boundary such that:_ 

- ( _i._ ) _The self-intersections consist of pairs_ ( _s_ 1 _, s_ 2) _∈R such that cs_ 1 _,s_ 2 _|_ (0 _,_ 1) _intersects K twice. We will denote the set of these pairs by_ ♢ _R._ 

- ( _ii._ ) _The boundary of R are the special pairs (at special pairs R is not selfintersecting)._ 

**Lemma 176.** _Let K be generic. Then the closures R[L] , R[U] are compact immersed_ 1 _-dimensional submanifolds of_ (R _/T_ Z)[2] _with boundaries given by transverse intersections with_ ∆0 _together with y_ 1 _- and z_ 2 _-special points, respectively. Along_ ∆0 _, each of R[L] , R[U] has no self-intersections._ 

_If we canonically represent R[L] , R[U] as submanifolds of the single_ (R _/T_ Z)[2] _, then they are symmetric along the axis_ ∆0 _. See Figure 5.3._ 

_Moreover, there are well-defined maps_ 

**==> picture [351 x 47] intentionally omitted <==**

**==> picture [161 x 16] intentionally omitted <==**

82 

(R _/T_ Z)[2] 

_T_ 0 _T_ Figure 5.3: A visualization of _R, R[L] , R[U]_ in the single configuration space (R _/T_ Z)[2] _._ Black dots represents special pairs. The groups of full and dashed curves correspond to two different connected components of ev _[−]_ _**R**_[1][(0).] 

_Proof._ The lemma is a consequence of Lemma 175 (i.e. [CELN16, lem 7.10]). We remark that in the proof of Lemma 175, a small neighborhood of _∂R_ in _R_ was explicitly constructed as a _single_ regular curve emanating from each special pair. This will in fact imply the transvesrality of _R[L] , R[U]_ with respect to ∆0. 

**Lemma 177.** _Let K be generic. If x ∈_ evˆ︃ _**R** −_ 1(0) _, then rank_ ( _d_ ev _**R**_ ( _x_ )) = 6 _. Moreover, let v ∈ Tπs_ 1 _,s_ 1 ( _x_ )(R _/T_ Z)[2] _. Then v_ ⋔ _R, iff the vectors_ 

**==> picture [166 x 13] intentionally omitted <==**

_are linearly independent._ 

_Proof._ The lemma can be seen as a corollary of the proof of Lemma 175 (i.e. [CELN16, lem 7.10]), where one had used twice Thom’s Transversality Theorem 33. 

In more detail. The condition “four vectors from R[3] lie in a plane” is of codim 2. Hence, from the matrix _d_ ev _**R**_ ( _x_ ) (Remark 174), we see that the condition “rank( _d_ ev _**R**_ ( _x_ )) _<_ 6, where _x ∈_ evˆ︃ _**R** −_ 1(0)” is of codim 3 + 3 + 2 = 8. Thus, it is avoidable for generic knots. 

In the second statement, one obtains analogously that for a generic knot the ̇ vectors _γ_ ( _y_ 3) _, ℓγ_ ( _s_ 2) _−ℓγ_ ( _s_ 1) are linearly independent. Indeed, the condition “two vectors from R[3] are linearly dependent” is of codim 2. Finally, since _Tx_ (ev _[−]_ _**R**_[1][(0)) =] ker( _d_ ev _**R**_ ( _x_ )), (ev _**R**_ ) _∗v_ could not lie in the _span_ of _γ_ ̇ ( _y_ 3) _, ℓγ_ ( _s_ 2) _− ℓγ_ ( _s_ 1). So the second statement follows. 

**Lemma 178.** _For a generic knot K it holds that_ 

**==> picture [277 x 15] intentionally omitted <==**

_Proof._ By Lemma 96 we know that for a generic _K_ the set _Crit_ ( _E_ 0) _\_ ∆0 consists of a finite number of nondegenerate critical points. In particular, _Crit_ ( _E_ 0) _\_ ∆0 

83 

is stable under perturbations of _K_ (in the sense of Stability Lemma 31 for the perturbations of the map ( _γ × γ_ ) _[∗] E_ ). Hence, for a generic knot, we can assume that any two binormal chords are not parallel. In particular, if _x ∈_ evˆ︃ _**R** −_ 1(0), then at most one point of _πs_ 1 _,s_ 2( _x_ ) _, πy_ 1 _,y_ 3( _x_ ) _, πz_ 2 _,z_ 3( _x_ ) lies in _Crit_ ( _E_ 0). Then the lemma follows from perturbations of _K_ as in [Pet24, lem 2.17]. 

**Lemma 179.** _Let K be a generic knot and XE_ 0 _be a gradient-like vector field. Then there is a gradient-like vector field YE_ 0 _such that YE_ 0 _is tangent to R at only a finite number of the points and XE_ 0 _and YE_ 0 _are C_[1] _close._ 

_Proof._ By Lemma 175 we know that _R_ is a compact immersed 1-manifold with boundary and a finite number of transverse self-intersections of the covering degree 2. Hence there is a finite covering _{Ri}i_ =1 _,...,k_ of _R_ by compact connected 1-manifolds _Ri_ embedded in (R _/T_ Z)[2] . Moreover, there are open subsets _Ui ⊂_ (R _/T_ Z)[2] such that _Ri ⊂ Ui_ and _∂Ui_ ⋔ _R_ . 

Let us put _Y_ 0 := _XE_ 0. By an induction in _i_ we would like to construct perturbed vector fields _Yi_ such that _Yi_ ⋔ _R_ along _Ri_ and _Yi_ = _Yi−_ 1 on (R _/T_ Z)[2] _\Ui_ (see below). Then we put _YE_ 0 := _Yk_ . If for each _i_ the perturbation is sufficiently small in _C[∞]_ topology (relative to the perturbations at the steps 1 _, . . . , i−_ 1), then by Stability Lemma 31 the vector field _YE_ 0 has the desired tangency properties and is _C_[1] close to _XE_ 0. Moreover, by Lemma 178 _YE_ 0 is gradient-like. Let us discuss the _i_ -th perturbation. For simplicity of the notation, we assume that _Ri_ does not contain any self-intersection of _R_ . Let _Ri[ext]_ be a small open extension of _Ri_ inside _R_ (if _Ri ∩ ∂R_ = _∅_ , then we consider, instead of _R_ , any small auxiliary extension of _R_ beyond the boundary _∂R_ ). Now, we can assume that a small tubular neighborhood _ν_ ( _Ri[ext]_[)][induces][a][chart] _[φ]_[:] _[ν]_[(] _[R] i[ext]_[)] _[→]_[R] _[x,y]_ such that 

**==> picture [366 x 14] intentionally omitted <==**

Let _Y_[˜︁] _i−_ 1 := _φ∗Yi−_ 1 _φ[−]_[1] . Then by Relative Thom’s transversality Theorem [Pet24, thm A.4] there is a _C_[1] small function _ρ_ : [ _−_ 2 _,_ 2] _×{_ 0 _} →_ R such that _dy_ ( _Y_[˜︁] _i−_ 1)+ _ρ_ ⋔ 0 along [ _−_ 2 _,_ 2] _×{_ 0 _}_ and _ρ_ ( _{±_ 2 _}×{_ 0 _}_ ) = 0 _._ Now we can extend _ρ_ to the whole _U i_ as _σ_ ( _y_ ) _ρ_ ( _x_ ), where _σ_ ( _y_ ) is a small bump function which is supported on [ _−_ 1 _,_ 1]. Then _σρ∂y_ determines the desired perturbation of _Yi−_ 1. 

_Proof of Lemma 170_ . Lemma 175 and Corrollary 176 give us a recipe, how to use the _forward flow ϕ[t] XE_ 0[and][iteratively][construct][in][the][configuration][space] (R _/T_ Z)[2] all trees of _♣XE_ 0 . 

That is the following. We consider _p_ 0 _∈ Crit_ 1( _E_ 0) _\_ ∆0 and _x ∈ WX[u] E_ 0[(] _[p]_[0][)] that is close to _p_ 0. Then we continue flowing with _ϕ[t] XE_ 0[(] _[x]_[) until we hit] _R_ , ideally in _R \_ ♢ _R_ . Then we can bifurcate and jump with the maps _φ[L/U]_ . After that, we continue by flowing and repeat. 

Hence, what we need to achieve is that each potential intersection of the (partial) flow trajectory with _R_ is transverse and avoid _∂R,_ ♢ _R_ . Moreover, we need to avoid _Crit_ ( _E_ 0) besides the root and the leaves. About ∆0 and _∂R_ , we do not need to worry. Indeed, we are not counting trees with leaves in ∆0, and ∆0 is the global minimum of _E_ 0. So, we can take a small regular index pair ( _N, ∅_ ) for ∆0 and study the flow only on (R _/T_ Z)[2] _\ Int_ ( _N_ ) _._ In particular, any bifurcation 

84 

will shrink the chords at least by some positive constant. Since the gradient-like vector field flows downhill, the number of potential bifurcations is bounded from above. 

By Lemma 179, we can assume that there is only a _finite_ number of problematic points along the whole _R_ . Now, a similar _finite_ inductive argument as in Corollary 121 will result in a desired perturbed gradient-like vector field. We remark that the local perturbations around the intersections with _R_ are described in [Pet24, lem 2.20], see also Lemma 120. 

_Remark_ 180 _._ Since by Lemma 175 _∂R_ corresponds to the special points, we achieved in Lemma 170 that the trees _♣XE_ 0 (when realized in (R _/T_ Z)[2] ) all lie in a standard set _SK_ . Here we implicitly assumed that the constant _δK >_ 0 for _SK_ is sufficiently small, see Remark 47. 

_Set-up_ 181 _._ Let us fix _m ∈_ N _, T ∈♣m, p_ 0 _∈ Crit_ 1( _E_ 0) _\_ ∆0 and _q_ 0[1] _[, . . . , q]_ 0 _[m][∈] Crit_ 0( _E_ 0) _\_ ∆0 and a gradient-like vector field _XE_ 0. 

The following exposition is motivated by [Mes16], see also [Abo11, Maz25]. _Remark_ 182 _._ Recall that _m_ = _|Vleaf_ ( _T_ ) _|_ = _|Vint_ ( _T_ ) _|_ + 1 = _|Eint_ ( _T_ ) _|_ + 2. **Definition 183.** _We define a map_ 

**==> picture [239 x 34] intentionally omitted <==**

_(Here_ R+ = (0 _, ∞_ ) _.) The domain_ (R _/T_ Z)[2] _×_ R+ _will be called as the_ _**space of positive finite length trajectories** ._ 

_d Remark_ 184 _._ Since _dt[|][t]_[=] _[t]_[0] _[ϕ] X[t] E_ 0[(] _[s]_[1] _[, s]_[2][)][=] _[X][E]_ 0[(] _[ϕ] X[t]_[0] _E_ 0[(] _[s]_[1] _[, s]_[2][)),][the][map] _[i][time]_[has] full rank, when restricted outside of _Crit_ ( _E_ 0) _×_ R+. In fact, because _XE_ 0 is a gradient-like vector field, the map _itime_ is an embedding when restricted outside of _Crit_ ( _E_ 0) _×_ R+. 

**Definition 185.** _The map_ 

**==> picture [405 x 69] intentionally omitted <==**

_is induced by itime and canonical inclusions on the remaining terms. (We assume that Eint_ ( _T_ ) _and Vint_ ( _T_ ) _are arbitrarily ordered.)_ 

**Definition 186.** _The_ _**reordering map** ρT_ : 

**==> picture [457 x 51] intentionally omitted <==**

_will be defined by permuting the coordinates as follows. Here letters “a” or “b” represent, in fact, pairs of coordinates._ 

85 

_To each pair of a-coordinates or b-coordinates, we would like to assign a flag. If two pairs of a-coordinates and b-coordinates will have assigned the same flag, then they will be canonically identified under ρT . For this, we will use the notions from Remarks 165 and 166._ 

- _To each of a_[0] _, a_[1] _, . . . , a[m] we assign the unique edge_ e _such that the root or the i-th leaf belongs to_ e ( _i ∈{_ 1 _, . . . , m}_ ) _. The assigned vertex will be the unique interior vertex that belongs to_ e _._ 

- _To each a[in/out]_ e _we assign the edge_ e _and the vertex v_ e _[in/out] ._ 

- _To each of bv, b[L] v[, b][U] v[we][assign][the][vertex][v][and][the][edges]_[e] _[v][,]_[ e] _[L] v[,]_[ e] _[U] v[,][respec-] tively._ 

**Definition 187.** _Let XE_ 0 _be a gradient-like vector field. Then we define the evaluation map_ Ev _T_ ; _p_ 0; _q_ 01 _[,...,q]_ 0 _[m]_[:] 

**==> picture [466 x 79] intentionally omitted <==**

**Corollary 188.** _For K generic, there is a canonical bijection_ 

**==> picture [258 x 18] intentionally omitted <==**

_In particular, if XE_ 0 _is a generic gradient-like vector field from Lemma 170 (which was constructed by certain perturbations in the configuration space_ (R _/T_ Z)[2] _), then_ 

**==> picture [251 x 15] intentionally omitted <==**

_Proof._ The bijection follows from the construction of Ev _T_ ; _p_ 0; _q_ 01 _[,...,q]_ 0 _[m]_[.] Here we remark that Ev _T_ ; _p_ 0; _q_ 01 _[,...,q]_ 0 _[m]_ does not count trees with edges of constant paths. Indeed, for interior edges it is clear, and for the remaining edges it follows from _R ∩ Crit_ ( _E_ 0) = _∅_ . Also for every _v ∈ Vint_ ( _T_ ) it holds that (Ev _T_ ; _p_ 0; _q_ 01 _[,...,q]_ 0 _[m]_[)] _[−]_[1][(0)] _[ ∩] πℓ[−] v_[1][(] _[{]_[0] _[,]_[ 1] _[}]_[)][=] _[∅]_[.][This][follows][from][the][fact][that] _[p]_[0] _[, q]_ 0[1] _[, . . . , q]_ 0 _[m][∈][Crit]_[(] _[E]_[0][)] _[ \]_[ ∆][0][,] see also Remark 180. 

The transversality (5.1) then follows from Lemma 177, see also Remark 174 for the description of _d_ ev _**R**_ . 

We finish the section with a small discussion about the evaluation map ev _**R**_ . _Remark_ 189 _._ It is easy to see that _πs_ 1 _,s_ 2(ev _[−]_ _**R**_[1][(0))][=][(][R] _[/T]_[Z][)][2] _[,]_[which][is][too][big] _−_ 1 space. We have also introduced the restriction evˆ︃ _**R**_ , where _πs_ 1 _,s_ 2(ev ˆ︃ _**R**_ (0)) = _R_ . By Lemma 175 _R_ has a nice geometric picture, and moreover allows us to describe all bifurcations of _♣XE_ 0 . However, for further work, it will be a bit inconvenient that the domain of evˆ︃ _**R**_ , and in particular also _R_ , are both non-compact. Luckily, we have seen in Remark 180 that in fact all bifurcations of evˆ︃ _**R**_ have to appear outside of a small neighborhood of _∂R._ So it will be enough to consider only certain restrictions of _R_ . This motivates the following definition. 

86 

**Definition 190.** evˆ︃ˆ︃ _**R** will denote the restriction of_ ev _**R** to_ [0 _,_ 1] _×_ ((R _/T_ Z)[2] _\ νδR_ (∆0))[3] _, where νδR_ (∆0) _is a δR-radius (open) tubular neighborhood of_ ∆0 _for some δR >_ 0 _small. Then the canonical projections πs_ 1 _,s_ 2 _, πy_ 1 _,y_ 3 _, πz_ 2 _,z_ 3 _on_ ev[ˆ︃] ˆ︃ _**R** −_ 1(0) _will define the sets R_[ˆ︂] ˆ︂ _, R_[ˆ︃] ˆ︃ _[L] , R_[ˆ︃] ˆ︃ _[U] , respectively._ 

_Remark_ 191 _._ If _δR >_ 0 is small and _K_ generic, then by Lemma 175 and Lemma 176 the following holds. _R_ ˆ︂ˆ︂ is a compact immersed 1-dimensional submanifold of (R _/T_ Z)[2] with boundary. Moreover, outside of small neighborhoods of special points _R_ and _R_[ˆ︂] ˆ︂ coincide and _d_[˜︁] _Haus_ ( _R, R_[ˆ︂] ˆ︂) _→_ 0 as _δR →_ 0. 

## **5.2 Trees for tori** 

We would like to define Morse flow trees on _TK,ε × TK,ε_ (on _MK,ε_ ) in a similar flavor as was done in the knot case. 

_Remark/Notation_ 192 _._ Similarly to the knot case, we will be using three notions for **chords on** _TK,ε_ . If Γ _ε_ : (R _/T_ Z _× S_[1] ) _→_ R[3] is the parametrization of _TK,ε_ from Remark 38, then any chord can be seen as a quadruple ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] or a as vector Γ _ε_ ( _s_ 2 _, θ_ 2) _−_ Γ _ε_ ( _s_ 1 _, θ_ 1). Moreover, the chord can also be seen as a smooth map _c[ε] s_ 1 _,θ_ 1 _,s_ 2 _,θ_ 2[: [0] _[,]_[ 1]] _[ →]_[R][3][defined][by] 

**==> picture [353 x 19] intentionally omitted <==**

Here recall that in Remark 38 we introduced _v_ ( _si, θi_ ) = cos( _θi_ ) _n_ ( _si_ )+sin( _θi_ ) _b_ ( _si_ ). 

**Definition 193.** _Let ε ∈_ (0 _, εgood_ ] _. Let pε ∈ Crit_ 2( _Eε|MK,ε\_ ∆ _ε_ ) _and qε_[1] _[, . . . , q] ε[m][∈] Crit_ 1( _Eε|MK,ε\_ ∆ _ε_ ) _such that pε, qε_[1] _[, . . . , q] ε[m] ∈ MK,ε. Let T ∈♣m. Let XEε be a gradient-like vector field adapted to Eε. A_ _**Morse flow tree from** pε_ _**to** qε_[1] _[, . . . , q] ε[m]_ _**[modeled][on]**[T]_ _**[(in][the][configuration][space]**_[(][R] _[/T]_[Z] _[ ×][ S]_[1][)][2] _**[)]**[is][an] ordered tree T together with the following assignment:_ 

- ( _i._ ) _If m_ = 1 _then the unique edge corresponds to a standard flow line ϕ[t] XE_ 0 _[with] t ∈_ R _._ 

_If m >_ 1 _, then the interior edges correspond to positive finite length partial flow lines of ϕ[t] XEε[.][The][other][edges][correspond][to][partial][flow][lines][of][ϕ][t] XEε parametrized by t ∈_ [0 _, ∞_ ) _or t ∈_ ( _−∞,_ 0] _._ 

- ( _ii._ ) _The root corresponds to pε._ 

- ( _iii._ ) _i-th leaf is identified with qε[i]_ 

   - _ε[.]_ 

- ( _iv._ ) _The tree is allowed to bifurcate at the points where the flow lines consist of nontrivial chords intersecting TK,ε by their interior._ 

_Let_ ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _be such a chord and_ ( _s_ 3 _, θ_ 2) _corresponds to the intersection of c[ε] s_ 1 _,θ_ 1 _,s_ 2 _,θ_ 2 _[|]_[(0] _[,]_[1)] _[with][T][K,ε][.][Then,][we][jump][to][the][chords]_[(] _[s]_[1] _[, θ]_[1] _[, s]_[3] _[, θ]_[3][)] _[and]_ ( _s_ 3 _, θ_ 3 _, s_ 2 _, θ_ 2) _and continue to flow with ϕ[t] XEε[.][Now,][the][triple]_ 

**==> picture [220 x 13] intentionally omitted <==**

87 

_is assigned to the corresponding interior vertex v of the tree T . The partial flow-line starting from_ ( _s_ 1 _, θ_ 1 _, s_ 3 _, θ_ 3) _corresponds to the edge_ e _[L] v[and][the] partial flow-line starting from_ ( _s_ 3 _, θ_ 3 _, s_ 2 _, θ_ 2) _corresponds to the edge_ e _[U] v[.]_ 

_The_ _**set of all Morse flow trees from** pε_ _**to** qε_[1] _[, . . . , q] ε[m]_ _**modeled on** T is denoted by_ 

_♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, . . . , q] ε[m]_[)] _[.]_ 

_The set of all Morse flow trees for all choices of m, T , pε ∈ Crit_ 2( _Eε|MK,ε\_ ∆ _ε_ ) _and qε_[1] _[, . . . , q] ε[m][∈][Crit]_[1][(] _[E][ε][|][M] K,ε[\]_[∆] _ε_[)] _[will][be][denoted][by][♣][X] Eε[.] If m_ = 1 _, we mod out the natural_ R _-action, then_ 

**==> picture [163 x 16] intentionally omitted <==**

_Remark_ 194 _._ If in Definition 193 we demand that at least one edge corresponds to a constant or broken (partial) flow line of _ϕXEε_ , then the resulted tree will be called **broken Morse flow tree** . 

Again, as in Remark 169, we stress out that even for the broken Morse flow trees we are not allowing that _qε[i][∈]_[∆] _[full]_[for][some] _[i][ ∈{]_[1] _[, . . . , m][}][.]_ 

**Definition 195.** _We put_ 

**==> picture [129 x 16] intentionally omitted <==**

_I. e. ♣[out] XEε[−][out] consists of Morse flow trees of ♣XEε that lie completely in MK,ε._ 

**Lemma 196.** _Let ε ∈_ (0 _, εgood_ ] _. Let pε ∈ Crit_ 2( _Eε|MK,ε\_ ∆ _ε_ ) _and qε_[1] _[, . . . , q] ε[m] ∈ Crit_ 1( _Eε|MK,ε\_ ∆ _ε_ ) _such that pε, qε_[1] _[, . . . , q] ε[m][∈][M][K,ε][.][If][K][is][a][generic][knot,][ε][>]_[0] _is small, XEε is a generic perturbation of −∇Eε, then ♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, . . . , q] ε[m]_[)] _[ is a] zero dimensional compact manifold. In addition, there are no broken Morse flow trees, ♣XEε_ = _♣[out] XEε[−][out] and for m ≫_ 0 _the set ♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, . . . , q] ε[m]_[)] _[is][empty.]_ 

_Remark_ 197 _._ Now, we are going to show a heuristic proof of the dimension count for _♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, . . . , q] ε[m]_[).][The][precise][proof][of][Lemma][170][will][be][the][aim][of] Chapter 6, where we will compare _♣XEε_ with _♣XE_ 0 using the Multiple time scale dynamics together with the compactness argument motivated by Chapter 4. 

_Heuristic proof._ For _m_ = 1, the argument is the same as in Lemma 170. For _m >_ 1 we obtain _♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, . . . , q] ε[m]_[)][as][an][intersection][of][certain][transversality] conditions; let us compute 

**==> picture [397 x 138] intentionally omitted <==**

The step (1 _._ ) is similar to that in Lemma 170 except that now, the constraint for a chord to intersect _T_ with its interior is of codim 0. _K,ε_ 

88 

**Definition 198.** _Let ε ∈_ [0 _, εgood_ ] _(i.e. ε can be even_ 0 _). Let us introduce the evaluation map_ 

ev _ε_ : [0 _,_ 1] _×_ (R _/T_ Z _×S_[1] )[2] _×_ (R _/T_ Z _×S_[1] )[2] _×_ (R _/T_ Z _×S_[1] )[2] _→_ ( _S_[1] )[3] _×_ (R _/T_ Z)[3] _×_ R[3] 

_as_ 

**==> picture [444 x 186] intentionally omitted <==**

_where the coordinates_ (( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _,_ ( _y_ 1 _, α_ 1 _, y_ 3 _, α_ 3) _,_ ( _z_ 2 _, β_ 2 _, z_ 3 _, β_ 3)) _are induced by a single parametrization_ Γ _ε_ : R _/T_ Z _× S_[1] _→ TK,ε. Also, by Remark 43_ ev _ε is a well-defined smooth map._ 

_Next,_ ev[ˆ︃] ˆ︃ _ε will denote the restriction of_ ev _ε to_ 

**==> picture [229 x 21] intentionally omitted <==**

_for some δR >_ 0 _small. Then the subset R_[ˆ︃] ˆ︃ _ε ⊂_ (R _/T_ Z _× S_[1] )[2] _is defined as_ 

**==> picture [135 x 21] intentionally omitted <==**

_We also define two sets_ 

**==> picture [263 x 23] intentionally omitted <==**

_See also Figure 5.4._ 

_Remark_ 199 _._ Note that the family _{_ ev _ε}ε∈_ [0 _,εgood_ ] is smooth. Moreover 

**==> picture [250 x 55] intentionally omitted <==**

and 

**==> picture [87 x 14] intentionally omitted <==**

**Lemma 200.** _For a generic knot and δR >_ 0 _sufficiently small, there is a ε_ 0 _>_ 0 _−_ 1 _such that {_ ev[ˆ︃] ˆ︃ _ε_ (0) _}ε∈_ [0 _,ε_ 0] _is a smooth family of isotopic_ 4 _-dimensional compact submanifolds with boundary._ 

89 

**==> picture [325 x 155] intentionally omitted <==**

Figure 5.4: _On the left:_ for _ε >_ 0 we can see geometrically a zero of ev[ˆ︃] ˆ︃ _ε_ as a coincidence of _c[ε] s_ 1 _,θ_ 1 _,s_ 2 _,θ_ 2[with][the][union][of] _[c][ε] y_ 1 _,α_ 1 _,y_ 3 _,α_ 3[and] _[c][ε] z_ 3 _,β_ 3 _,z_ 2 _,β_ 2[.][Two][possible] coincidences are depicted as the dashed chords with three marked points. Note that we are not imposing any outward-pointing condition. _On the right:_ an example of a not allowed coincidence, since we are not counting intersections that are close in knot coordinates. 

_Proof._ Our aim is to apply the Stability Lemma 31. Hence, we need to verify that for a generic knot the map ev[ˆ︃] ˆ︃0 is stratum transverse to 0. If we restrict ev[ˆ︃] ˆ︃0 to _Int_ ( _Dom_ (ev[ˆ︃] ˆ︃0)), then the transversality is straightforward by relation (5 _._ 2) and Lemma 177. By Lemmata 175 and 176, provided that _δ >_ 0 is sufficiently small, it holds 

**==> picture [113 x 14] intentionally omitted <==**

**==> picture [330 x 42] intentionally omitted <==**

In particular, ev[ˆ︃] ˆ︃0 _−_ 1(0) _∩ πℓ−_ 1[(] _[{]_[0] _[,]_[ 1] _[}]_[)][=] _[∅]_[.][Which][implies][the][transversality][for] the remaining cases. 

**Lemma 201.** _For a generic knot and δR, ε >_ 0 _sufficiently small it holds that_ 

**==> picture [281 x 19] intentionally omitted <==**

_Proof._ By Lemma 178 we know that for generic _K_ it holds that _Crit_ ( _E_ 0) _∩R_[ˆ︂] ˆ︂ = _∅_ . Hence by Lemma 99 (the relations (3 _._ 28)) we obtain that _Crit_ ( _Eε_ ) _∩ R_[ˆ︃] ˆ︃0 = _∅_ . Since _Eε_ is Morse-Bott, the critical submanifolds are isolated. So the isotopy from Lemma 200 finishes the proof, provided that _ε >_ 0 is sufficiently small. Other cases are analogous. 

**Lemma 202.** _For a generic knot and δR, ε >_ 0 _sufficiently small it holds that each bifurcation of ♣XEε appears at R_[ˆ︃] ˆ︃ _ε._ 

_Proof._ Note that there is a _δK >_ 0 small such that for any _ε >_ 0 sufficiently small 

**==> picture [239 x 19] intentionally omitted <==**

90 

is a regular index pair of ∆ _full_ under the flow _ϕXEε_ . Also, similarly to the knot case, bifurcations are shortening the chords, so the forward-flow _ϕXEε_ flows along _♣XEε_ downhill. Hence, since elements of _♣XEε_ have no leaves in ∆ _full_ , for any _ε >_ 0 sufficiently small _πs_ 1 _,s_ 2( _♣XEε_ ) avoids a _δK_ -neighborhood of any special point. Now, we take _δR >_ 0 such that _δR ≪ δK_ which determines _R_[ˆ︃] ˆ︃ _ε_ with the desired property. 

**Definition 203.** _Let ε ∈_ (0 _, εgood_ ] _. Let pε ∈ Crit_ 2( _Eε|MK,ε\_ ∆ _ε_ ) _and qε_[1] _[, . . . , q] ε[m][∈] Crit_ 1( _Eε|MK,ε\_ ∆ _ε_ ) _such that pε, qε_[1] _[, . . . , q] ε[m] ∈ MK,ε. Let T ∈♣m. Let XEε be a gradient-like vector field adapted to Eε._ 

_Then we define the evaluation map_ Ev _[ε] T_ ; _pε_ ; _qε_[1] _,...,qε[m]_[:] 

**==> picture [393 x 64] intentionally omitted <==**

_as_ 

**==> picture [206 x 27] intentionally omitted <==**

_where the definitions of the reordering function ρT and ican are analogous to Definitions 185 and 186._ 

**Corollary 204.** _For K generic, δR, ε >_ 0 _sufficiently small there is a canonical bijection_ 

**==> picture [257 x 17] intentionally omitted <==**

_Proof._ Similarly as in Corollary 188, the bijection follows from the construction of Ev _T_ ; _pε_ ; _qε_ 1 _,...,qεm_[.][Here][we][remark][that][Ev] _[T]_[ ;] _[p][ε]_[;] _[q] ε_[1] _[,...,q] ε[m]_[also][does][not][count][trees] with edges of constant paths. Indeed, for interior edges it is clear, and for the remaining edges it follows from Lemmata 201 and 202. Also by Lemma 202, for every _v ∈ Vint_ ( _T_ ) it holds that (Ev _T_ ; _pε_ ; _qε_ 1 _,...,qεm_[)] _[−]_[1][(0)] _[ ∩][π] ℓ[−] v_[1][(] _[{]_[0] _[,]_[ 1] _[}]_[) =] _[ ∅]_[.] 

_Remark_ 205 _._ Recall that in the knot case we also used an iterative construction of _♣XE_ 0 under the _forward-flow ϕ[t] XE_ 0[.][I. e.,][roughly speaking,][we track] _[ W] X[ u] E_ 0[(] _[p]_[0][)] for some _p_ 0 _∈ Crit_ 1( _E_ 0). When we hit _R_ , we bifurcate and continue flowing along the new branches and repeat. 

However, for the torus case, this method is not very convenient. If we start naively to flow along some trajectory from _pε ∈ Crit_ 2( _Eε_ ), then we realize that suddenly after the first bifurcation we have to follow two 1-dimensional families of trajectories and so on. Hence, it might look that the dimensions of the tracked trajectories are exploding after each bifurcation. Fortunately, this all will get corrected once we reach the leaves. Contrary to the knot case, now the constraints to reach the stable manifolds at leaves are of codim 1, which will reduce the dimension of the tracked trajectories. 

In order to avoid these temporary explosions of the dimension of tracked trajectories, we will be considering in the torus case an iterative construction under the _backward-flow ϕ[−] X[t] Eε_[.][I.][e.,][roughly][speaking,][we][start][to][track][two][3-] dimensional stable manifolds of two leaves. When they hit _R_[ˆ︃] ˆ︃ _[L] ε_[and] _R_[ˆ︃] ˆ︃ _[U] ε_[, then they] 

91 

induce a subset _Rε ⊂ R_[ˆ︃] ˆ︃ _ε_ . Our wish will be that _Rε_ is a 2-dimensional manifold, which is transverse to the flow _ϕ[−] X[t] Eε[.]_[ Then we will follow] _[ ϕ] X_[(] _[−∞] Eε[,]_[0]] ( _Rε_ ), which will be only 3-dimensional manifold. Altogether, we started tracking two 3-dimensional stable manifolds and continue to track one 3-dimensional flow invariant manifold. This induces the recursion under the backward-flow. We will use this method in Chapter 6. 

We finish the chapter with one auxiliary lemma. 

_−_ 1 **Lemma 206.** _Let_ ( _ℓ,_ ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _,_ ( _y_ 1 _, α_ 1 _, y_ 3 _, α_ 3) _,_ ( _z_ 2 _, β_ 2 _, z_ 3 _, β_ 3)) _∈_ ev[ˆ︃] ˆ︃ _ε_ (0) _, then the vector γ_ ( _s_ 2) _− γ_ ( _s_ 1) _can be represented in two ways as_ 

_or_ 

**==> picture [214 x 76] intentionally omitted <==**

_Proof._ The lemma immediately follows from the geometric picture of ev[ˆ︃] ˆ︃ _ε−_ 1(0). 

92 

## **6. Multiple time scale dynamics** 

In this chapter, we will see the dynamics of _−∇Eε_ as a fast-slow system on the configuration space (R _/T_ Z _× S_[1] )[2] which in different time scales approaches the fast or slow subsystem as _ε →_ 0. If we ignore the singularities at special and diagonal points, the slow subsystem will look like _−∇E_ 0 dynamics on 4 sheets of (R _/T_ Z)[2] embedded into (R _/T_ Z _× S_[1] )[2] . In addition, the fast system looks like the flow in _θ_ -directions between the 4 sheets, which are now normally hyperbolic critical manifolds (again, the situation is a bit more complicated once also the special and diagonal points get involved). For _ε >_ 0 small, we will be able to recover the dynamics of the fast-slow system from the combination of the fast and slow subsystems. The Fenichel theory and Exchange Lemmata will be the techniques that we will be using for this task. 

In addition, one of the sheets, where the slow dynamics is contained, lies in _MK,ε._ Hence, we will be able to construct the bijective correspondence between the _−∇E_ 0-heteroclinic orbits on (R _/T_ Z)[2] and the _−∇Eε_ -heteroclinic orbits _MK,ε_ , provided that the rest points have low Morse indices and do not lie on diagonals. In fact, we will be able to show the bijective correspondence also for the Morse flow trees. For the surjectivity, we will adapt the compactness from Chapter 4, where we did the adiabatic limit with the Conley index. Later, in Chapter 7, the correspondence of trees will allow us to relate various cord algebras. 

We remark that in Morse theory, the Multiple-time scale dynamics naturally appeared in the following places and was used for the bijective correspondence of (broken) heteroclinic orbits. It was used in [SX14] for Lagrangian multipliers and in [BH13] for the cascades between Bott-critical manifolds. 

In Sections 6.1-6.3 we recollect the notions of Fenichel theory and Exchange Lemmata. Then, finally, in Section 6.4 we apply the theory to our setup. 

## **6.1 Basic tracking of trajectories** 

**Gronwall’s inequality 207.** _[HSD04] Let u ∈ C_[0] ([0 _, T_ ] _,_ R _≥_ 0) _. Assume that C, L are non-negative constants such that_ 

**==> picture [117 x 26] intentionally omitted <==**

_for all t ∈_ [0 _, T_ ] _. Then, for each such t holds that_ 

**==> picture [64 x 15] intentionally omitted <==**

_Remark_ 208 _._ [HSD04] A useful consequence of Gronwall’s inequality 207 is that the flow of _C_[1] vector field depends continuously on initial conditions. 

**Lemma 209.** _[Wig94, lem 3.2.7]Let f and f[pert] be two C_[1] _vector fields on_ R _[n] . Let us consider an open bounded set U ⊂_ R _[n] and ε >_ 0 _. Assume that f and f[pert] are C_[0] _ε-close on U , i. e._ 

**==> picture [272 x 23] intentionally omitted <==**

93 

_We fix T >_ 0 _and denote by ϕ[t] and ϕ[t] pert[the][flows][generated][by][f][and][f][ pert][,] respectively. Then for each x ∈ U and |t| ≤ T holds_ 

**==> picture [161 x 16] intentionally omitted <==**

_provided that ϕ[t]_ ( _x_ ) _and ϕ[t] pert_[(] _[x]_[)] _[remain][in][the][compact][set] U . Here L is the Lipschitz constant of f ._ 

_Proof._ We compute 

**==> picture [414 x 167] intentionally omitted <==**

_. ._ where in the step (1 ) we used the assumption (6.1), in (2 ) we used the Lipschitz continuity of _f_ , and finally in (3 _._ ) we applied Gronwall’s inequality 207. 

_Remark_ 210 _._ Alternatively, one can use an Implicit function theorem argument and show a smooth dependence of _ϕ[t]_ ( _x_ ) on the initial data. Here, one has to consider the vector fields from a bounded open subset of the space of bounded vector fields with the uniform _C[k]_ -norm. See [Eld13, appx A]. 

## **6.2 Fenichel theory** 

_From now on in this chapter, we will consider that k is a natural number bigger than_ 3 _._ 

**Definition 211.** _Let_ 

**==> picture [228 x 13] intentionally omitted <==**

_be a general autonomous ODE on_ R _[n] given by a C[k] function F_ : R _[n] →_ R _[n] . Then ϕ[t] will denote the flow induced by (6.2). Let M be a connected compact C[k] -manifold in_ R _[n] with corners (M is potentially of_ codim _>_ 0 _). M is called:_ 

- _**Overflowing** if ϕ[t]_ ( _p_ ) _∈ M for every p ∈ M and t ≤_ 0 _, and in addition the vector field of (6.2) is strictly outward-pointing from ∂M (recall the terminology for vectors on the boundary in Definition 32)._ 

- _**Inflowing** if ϕ[t]_ ( _p_ ) _∈ M for every p ∈ M and t ≥_ 0 _, and in addition the vector field of (6.2) is strictly inward-pointing from ∂M ._ 

- _**Invariant** if ϕ[t]_ ( _p_ ) _∈ M for every p ∈ M and t ∈_ R _._ 

94 

- _**Locally invariant** if for every p ∈ M[◦] there exists some open interval Ip such that_ 0 _∈ Ip and ϕ[t]_ ( _p_ ) _∈ M for t ∈ Ip._ 

_Remark_ 212 _._ [FM71] We would like to inspect the stability of the _overflowing_ manifold _M_ under a perturbation of _f_ . For this, we will first introduce the rate of growth of normal vectors under the linearised dynamics in backward time. And then we will impose a function measuring the flattening of orbits relative to _M_ by relating the normal and tangential directions in backward time. 

More precisely, let _N_ := _N_ ( _M,_ R _[n]_ ) be the normal bundle of _M_ . Let _p ∈ M_ . Then for any _v_ 0 _∈ TpM_ and _w_ 0 _∈Np_ we put 

**==> picture [225 x 14] intentionally omitted <==**

Now, we consider any Riemannian metric on R _[n]_ and define the following **generalized Lyapunov-type numbers** as 

**==> picture [273 x 30] intentionally omitted <==**

and, if _ν_ ( _p_ ) _<_ 1, 

**==> picture [438 x 25] intentionally omitted <==**

_Remark_ 213 _._ [FM71, Wig94] _ν_ and _σ_ are independent of choices of the Riemannian metric on R _[n]_ and _N_ . Moreover, _ν_ and _σ_ are constant along orbits. 

Also, for the computation (especially at equilibrium points), there are useful relations 

**==> picture [201 x 52] intentionally omitted <==**

**Theorem 214.** _[FM71, Wig94, Fen79] Let M be an overflowing manifold for the system (6.2). Assume that ν_ ( _p_ ) _<_ 1 _and σ_ ( _p_ ) _<_ 1 _/k for each p ∈ M ._ 

_Let the C[k] -vector field f[ε] be C_[1] _O_ ( _ε_ ) _-close to f , where_ 0 _< ε ≪_ 1 _. Then there is an overflowing C[k] -manifold Mε for f[ε] which is diffeomorphic to M . In addition, M and M[ε] are O_ ( _ε_ ) _-close in Hausdorff distance._ 

_Sketch proof._ The proof is based on the original idea of Hadamard from 1901 of the graph transform, see [Has17]. First, we consider the disc bundle _Dδ_ over _M_ consisting of normal vectors of norm _≤ δ_ . This gives us local coordinates R[dim] _[ M] ×_ R _[n][−]_[dim] _[ M]_ that identify locally _M_ with R[dim] _[ M] × {_ 0 _}_ . For simplicity, we assume the coordinates are global. In particular, any section _v ∈Dδ_ can be seen as a graph (=: graph( _v_ )) over R[dim] _[ M]_ . 

Let _Sδ_ be the space of sections in _Dδ_ with Lipschitz constant _δ_ . Then we define a graph transform _G_ on _Sδ_ by 

**==> picture [135 x 14] intentionally omitted <==**

for some fixed _T >_ 1. If we ignore what overflows from the bundle _Dδ_ and _δ, ε_ are sufficiently small, then _G_ is well-defined. Next, the generalized Lyapunovtype numbers _ν, σ_ imply that _ϕ[T]_ is contracting _δ_ of _Dδ_ . However, if _δ_ and 

95 

_ε_ are sufficiently small, then _G_ is also a contraction. Hence, by the Banach contraction mapping theorem, _G_ has a unique fixed point _v_ . In particular, graph( _v_ ) _⊆ ϕ[T] ε_[(graph(] _[v]_[)).] Then an inductive argument, starting from small _t >_ 0, shows that graph( _v_ ) _⊆ ϕ[t] ε_[(graph(] _[v]_[))][for][all] _[t][ ≥]_[0.] 

In the end, we remarked that we worked in a slightly simplified setting. In order to show the regularity of _M[ε]_ , we should not have started with _Dδ ⊂ N_ ( _M,_ R _[n]_ ). We should have rather considered _Dδ_ inside a so-called transversal bundle. That is a certain _C[k]_ dim _M_ -bundle in _T_ R _[n] |M_ that is close to _N_ ( _M,_ R _[n]_ ) (which is only _C[k][−]_[1] ). For more details on the regularity of _M[ε]_ , see [Wig94]. 

_Remark_ 215 _._ Reversing time brings a straightforward extension of Theorem 214 to inflowing manifolds and, in particular, to boundary-less invariant manifolds. 

In the case of invariant manifolds with boundaries, the situation is a bit more delicate. By the definition, the vector field _f_ is also defined on a small neighborhood _U_ of _M_ . Now, we deform the vector field _f_ by adding certain small bump functions supported in _U \ M_ . The purpose of this modification is that we will obtain a compact set _M_[˜︂] _⊃ M_ , where _M_[˜︂] is inflowing or overflowing. The downside is that for the perturbation _f[ε]_ , the manifold _M[ε]_ will be only locally invariant due to the potential leaving of the flow through the boundary. Luckily, in our applications, we will be able to recover a lot of the structure of the dynamics restricted to _M[ε]_ . For more details on this construction, see [Fen79, Wig88]. _Remark_ 216 _._ [FM71, Wig94] Continuing the discussion from Remark 213, we introduce new **generalized Lyapunov-type numbers** . Assume we have a ( _C[k]_ ) splitting 

**==> picture [139 x 13] intentionally omitted <==**

where we assume that _N[u] ⊕ TM_ and _N[s] ⊕ TM_ are invariant under _Dϕ[t]_ from the system (6.2) for _t ≤_ 0. Let us pick a Riemannian metric on R _[n]_ . Now, we put 

**==> picture [217 x 107] intentionally omitted <==**

These numbers are also independent of the Riemannian metric and constant along orbits. 

**Unstable manifold Theorem 217.** _[FM71, Wig94] Let M be an overflowing C[k] -manifold for the system (6.2) such that supp∈M max{ν[u]_ ( _p_ ) _, ν[s]_ ( _p_ ) _, σ[u]_ ( _p_ ) _} <_ 1 _. Then there is an overflowing C[k] -manifold W[u] tangent to N[u] along M ._ 

_W[u] persists under perturbation by C[k] -vector field f[ε] C_[1] _O_ ( _ε_ ) _-close to f . In more detail, there is an overflowing C[k] -manifold Wε[u][diffeomorphic][to][W][ u][and] O_ ( _ε_ ) _-close in Hausdorff distance._ 

_Sketch proof._ For the existence, we study the graph transform on sections of _N[u] ⊕N[s] →N[u]_ given by the linearised flow. Hence, the Banach contraction mapping theorem gives us the existence of _W[u]_ in a small neighborhood _U_ of _M_ . 

96 

For the persistence, we do not need to compute generalized Lyapunov-type numbers for _W[u]_ . But we would rather use the fact that in _U_ the manifolds _W[u]_ and _N[u]_ are close (in the coordinates induced by the splitting of _T_ R _[n] |M_ ). Hence, if _U_ is sufficiently small, then we obtain the appropriate bounds for the Banach contraction mapping theorem and thus _Wε[u]_[.] 

**Definition 218.** _Let M be a compact invariant manifold without boundary. The splitting T_ R _[n] |M_ = _N[u] ⊕ TM ⊕N[s] is called_ _**normally hyperbolic** , if_ 

**==> picture [217 x 14] intentionally omitted <==**

_Then M is called a_ _**normally hyperbolic manifold** . We will denote by ℓu the dimension of fibers of N[u] and by ℓs the dimension of fibers of N[s] ._ 

_Remark_ 219 _._ [FM71] The Unstable Manifold Theorem 217 extends also to normally hyperbolic invariant manifolds. In this case, we obtain the existence of overflowing _W[u]_ and inflowing _W[s]_ . Moreover, not only _W[u]_ and _W[s]_ persist under perturbation of _f_ , but also _M_ persists. In this case _Wε[u][∩][W] ε[ s]_[=] _[ M][ε]_[,] _[W][ u] ε_[is][over-] flowing, _Wε[s]_[is][inflowing][and] _[M][ε]_[is][invariant.][We][will][call] _[W] ε[ s]_[and] _[W] ε[ u]_[the] **[local] stable and unstable manifolds** of _Mε_ , and denote them rather as _Wε[s,loc]_ ( _Mε_ ) and _Wε[u,loc]_ ( _Mε_ ), respectively. The unions of the images of _Wε[s/u,loc]_ ( _Mε_ ) under the flow for all times give us **global stable and unstable manifolds** of _Mε_ . 

_Example_ 220 _._ Let _F_ be a Morse function on a closed Riemannian manifold ( _M, g_ ) _._ Let _XF_ be a gradient like-vector field adapted to _F_ and _p_ 0 _∈ Crit_ ( _F_ ). Then, with respect to _XF_ , the point _p_ 0 is a normally hyperbolic invariant manifold with the unique local unstable manifold _WX[u,loc] F_[(] _[p]_[0][)][(the][uniqueness][is][with][respect][to] the fixed radius of the corresponding disk in _N[u]_ ). 

Hence, if _Y[ε]_ is a _C[k] O_ ( _ε_ )-perturbation of _XF_ , then the unique perturbations of _pε_ and _WY[u,loc][ε]_[(] _[p][ε]_[)][are] _[C][k][O]_[(] _[ε]_[)-close][to] _[p]_[0][and] _[W][ u,loc] XF_[(] _[p]_[0][),][respectively.] 

Let us moreover assume that the perturbation _Y[ε]_ of _XF_ is _C[k]_ smooth in _ε ∈_ [ _−ε_ 0 _, ε_ 0], where _ε_ 0 _>_ 0 is small. We can then study perturbations _Y[ε] × {_ 0 _}_ of _XF × {_ 0 _}_ on _M ×_ [ _−ε_ 0 _, ε_ 0]. By [Fen79, pg 90], the graph transform argument can still be applied in this case. Hence, _pε_ and _WY[u,loc][ε]_[(] _[p][ε]_[)][will][vary][in] _[C][k]_[families] parametrized by _ε_ . We remark that since all of these manifolds can be seen as _ε_ -parametrized graphs over _p_ 0 and a disc in _N[u]_ , they are in fact isotopic submanifolds of _M_ . We will also use this trick (of augmenting the vector field) in Theorem 225 for the fast-slow systems. 

Let _W_[˜︂] _X[u] F_[(] _[p]_[0][)][be][a][(compact)][codim 0][overflowing][submanifold][of][the][global] unstable manifold _WX[u] F_[(] _[p]_[0][).][In][particular,] _[W] X[ u,loc] F_[(] _[p]_[0][)] _[ ⊂] W_[˜︂] _X[u] F_[(] _[p]_[0][).][Hence][we][can] encode every point _y_ 0 _∈ W_[˜︂] _X[u] F_[(] _[p]_[0][)] _[ \][ W] X[ u,loc] F_[(] _[p]_[0][)][as] _[ϕ][T] XF_[(] _[x]_[0][)][for][some] _[T][>]_[0][and] _x_ 0 _∈ ∂_ ( _WX[u,loc] F_[(] _[p]_[0][)).][Recall][that][by][Remark][210][the][flow][depends][smoothly][on] the initial data ( _x_ 0 _, XF_ ), because _M_ is compact. So the _C[k]_ smooth perturbation _Y[ε]_ , will perturb _W_[˜︂] _X[u] F_[(] _[p]_[0][)][also] _[C][k]_[smoothly][by][a] _[C][k]_[family][of] _[C][k]_[maps.][Since] embeddings are open by Theorem 25, we will in fact obtain isotopic overflowing _C[k]_ submanifolds of _M_ . 

To the end, we remark that the smooth family of _WY[u,loc][ε]_[(] _[p][ε]_[)][can][also][be][ob-] tained by Perron’s method, see [PT93, Apx 1, 4]. 

97 

**Definition 221.** _[Kue15]A_ _**Fast-slow system** is a system of ordinary differential equations of the form_ 

**==> picture [263 x 32] intentionally omitted <==**

_where f_ 1 _∈ C[k]_ (R _[m] ×_ R _[n] ×_ R _,_ R _[n]_ ) _, f_ 2 _∈ C[k]_ (R _[m] ×_ R _[n] ×_ R _,_ R _[m]_ ) _, and_ 0 _< ε ≪_ 1 _. Here, θ are called the_ _**fast variables** and s are called the_ _**slow variables** . We can equivalently put τ_ = _t/ε and obtain_ 

**==> picture [262 x 31] intentionally omitted <==**

_We will refer to t as the_ _**slow time** and to τ as the_ _**fast time** . The_ _**fast-slow flow** will be denoted (equivalently) as ·f-s t or ·f-s τ ._ 

**Definition 222.** _[Kue15] The_ _**slow flow** is the solution of the_ _**slow subsystem** , which is the differential-algebraic equation_ 

**==> picture [73 x 31] intentionally omitted <==**

_and will be denoted as ·slowt._ 

_The_ _**fast flow** is the solution of the_ _**fast subsystem** , which is given by_ 

**==> picture [76 x 29] intentionally omitted <==**

_and will be denoted as ·fastτ ._ 

**Definition 223.** _[Kue15] The_ _**critical set** C_ 0 _is defined by_ 

**==> picture [211 x 12] intentionally omitted <==**

_A subset S_ 0 _⊂ C_ 0 _is called_ _**normally hyperbolic** (for the fast flow) if for each p ∈ S_ 0 _the_ ( _n × n_ ) _-matrix Dθf_ 1( _p,_ 0) _has no eigenvalue with zero real part. We will assume that S_ 0 _is a smooth compact m-dimensional manifold (possibly with corners)._ 

_Points in C_ 0 _, which do not lie in any normally hyperbolic manifold, are called_ _**singularities** ._ 

_Remark_ 224 _._ Note that the equilibrium points of the fast flow are in bijection with the points of _C_ 0. 

**Theorem 225.** _[Fen79, Jon95, Fen77] Let S_ 0 _be a normally hyperbolic manifold for the fast flow and let W_ 0 _[s/u,loc]_ ( _S_ 0) _be its local stable and unstable manifolds. If ε_ 0 _>_ 0 _is sufficiently small, then there are families {Sε}ε∈_ [0 _,ε_ 0] _and {Wε[s,loc]_ ( _Sε_ ) _}ε∈_ [0 _,ε_ 0] _, {Wε[u,loc]_ ( _Sε_ ) _}ε∈_ [0 _,ε_ 0] _such that:_ 

> ( _i._ ) _Families consists of C[k] manifolds (with corners) and are C[k][−]_[1] _in ε (the manifolds in each family are isotopic submanifolds of_ R _[m]_[+] _[n] )._ 

98 

( _ii._ ) _Wε[s,loc]_ ( _Sε_ ) _∩ Wε[u,loc]_ ( _Sε_ ) = _Sε._ 

- ( _iii._ ) _If ε >_ 0 _, then Sε, Wε[s,loc]_ ( _Sε_ ) _, Wε[u,loc]_ ( _Sε_ ) _are locally invariant for the fast-slow flow._ 

_Sketch proof._ We augment the system (6 _._ 13) by _ε[′]_ = 0 for _|ε|_ small and would like to apply Theorems 214 and 217. The variable _ε_ is not too much of a problem due to the behavior of the vector field in the _ε_ direction. However, slow variables contribute with center-like directions that we need to deal with. For this, we perturb the augmented system by bump functions as discussed in Remark 215. 

_Remark_ 226 _._ Due to normal hyperbolicity, we can use the implicit function theorem to write _S_ 0 locally as a graph over the slow variable. We will assume that _S_ 0 can be globally written as a graph _{_ ( _s, h_ 0( _s_ )) _| s ∈ K}_ , where _K ⊂_ R _[m]_ is a compact, contractible (smooth) manifold with corners. 

Then by Theorem 225 the _Sε_ can be written as graphs of functions _hε_ ( _s_ ), which are _C[k]_ in _s_ and _C[k][−]_[1] in _ε_ . 

On _Sε_ , the fast-slow flow is given as 

**==> picture [101 x 13] intentionally omitted <==**

and hence in the slow time as 

**==> picture [93 x 13] intentionally omitted <==**

Observe that as _ε →_ 0, the limit of the flow exists and is given by 

**==> picture [93 x 13] intentionally omitted <==**

In particular, this family of flows on _Sε_ is _C[k][−]_[1] in _ε_ . Hence, the study of the fast-slow flow on _Sε_ is a regular perturbation problem in the sense of [Kue15, Def 5.1.4]. 

_Remark_ 227 _._ On the first sight, the results from Theorem 225 look a bit weak, since the perturbed manifolds are only locally invariant. But in Remark 226 we already described the dynamics on _Sε_ . However, we still do not understand well the dynamics on the perturbations of stable and unstable manifolds. For this, we introduce a certain flow invariant fibration on _Wε[s/u,loc]_ ( _Sε_ ). Which, in particular, will show us that _Wε[s/u,loc]_ ( _Sε_ ) are decaying to _Sε_ exponentially and hence, the notation is justified. 

**Theorem 228.** _[Jon95, Fen79] Let S_ 0 _be a normally hyperbolic manifold for the fast flow. Let ε_ 0 _>_ 0 _be small. Let {Sε}ε∈_ [0 _,ε_ 0] _be parametrized by vε ∈ Sε, where the parametrization is C[k] in v and C[k][−]_[1] _in ε. Then for each vε ∈ Sε there exists a C[k] manifold W[s,loc]_ ( _vε_ ) _(with corners) such that:_ 

**==> picture [143 x 14] intentionally omitted <==**

- ( _ii._ ) _Wε[s,loc]_ ( _vε_ ) _is C[k] in v and C[k][−]_[1] _in ε._ 

- ( _iii._ ) _If ε_ = 0 _, then W_ 0 _[s,loc]_ ( _v_ 0) _is a local stable manifold of v_ 0 _∈ S_ 0 _for the fast flow._ 

99 

- ( _iv._ ) _If ε >_ 0 _, then Wε[s,loc]_ ( _vε_ ) _is_ _**positively invariant** . I.e. if vε ·f-s_ [0 _, τ_ ] _∈ Wε[s,loc]_ ( _Sε_ ) _, then_ 

**==> picture [342 x 19] intentionally omitted <==**

**==> picture [407 x 63] intentionally omitted <==**

_Analogous statement holds for the unstable case, only then in_ ( _iv._ ) _and_ ( _v._ ) _we consider τ ≤_ 0 _._ 

_Sketch proof._ The theorem can be proven similarly to Theorem 225 by a graph transform argument applied to the augmented fast-slow system, which is deformed by bump functions in a neighborhood of _∂S_ 0. However, to obtain a result about the unperturbed system, we need to impose the constraints in ( _iv._ )-( _v._ ) to be sure that we do not leave the locally invariant manifolds _Wε[s/u,loc]_ ( _Sε_ ). 

_Remark_ 229 _._ Let _D_ be a subset of _Sε_ . Based on the construction of fibrations from Theorem 228, we introduce 

**==> picture [289 x 24] intentionally omitted <==**

**Definition/Theorem 230.** _[Fen79, JT09] Let us consider the C[k] fast-slow system (6.4) with m-dimensional normally hyperbolic manifold S_ 0 _⊂_ R _[m]_[+] _[n] . Let U_ 0 _be an open (contractible) subset of S_ 0 _. Then there are_ _**Fenichel coordinates** . That is a C[k][−]_[1] _coordinate change_ Φ _[fen] of a neighbourhood of U_ 0 _×{_ 0 _} ⊂_ R _[m]_[+] _[n] ×_ [0 _, ε_ 0) _such that (6.4) takes the_ _**Fenichel normal form** ._ 

**==> picture [287 x 54] intentionally omitted <==**

_where_ 

- _(i.) (6.5) is C[k][−]_[2] _._ 

- _(ii.) A and B are matrices of the form ℓu × ℓu and ℓs × ℓs, respectively (recall that ℓs_ + _ℓu_ = _n). The real parts of the eigenvalues of A are in_ ( _α, ∞_ ) _, and of B are in_ ( _−∞, −β_ ) _, for some α, β >_ 0 _. Also_ ( _a, b_ ) _→ H_ ( _a, b, x, ε_ ) _ab is bilinear._ 

- _(iii.) For each ε ∈_ [0 _, ε_ 0) _, it holds in these coordinates that Uε_ = _{a_ = 0 _, b_ = 0 _}, Wε[u,loc]_ ( _Uε_ ) = _{b_ = 0 _}, and Wε[s,loc]_ ( _Uε_ ) = _{a_ = 0 _}. (Here, we were considering x ∈ Ufen ⊂_ R _[m] , for some Ufen diffeomorphic to the original U_ 0 _⊂ S_ 0 _.) In particular, along Wε[u,loc]_ ( _Uε_ ) _we have that_ ( _x_ ( _τ_ ) _, a_ ( _τ_ ) _,_ 0) _is a solution iff_ ( _x_ ( _τ_ ) _,_ 0 _,_ 0) _is a solution. Analogously for Wε[s,loc]_ ( _Uε_ ) _._ 

100 

- _(iv.) If Wε[u,loc]_ ( _Uε_ ) _−→πa Uε and Wε[s,loc]_ ( _Uε_ ) _−→πb Uε are fibrations induced by the canonical projections πa, πb, then the flow of_ (6 _._ 5) _is a fiber invariant, i.e., the flow maps fibers into fibers. Moreover, let p ∈ Uε and pu be a lift to the fiber πa[−]_[1][(] _[p]_[)] _[,][then][the][distance][of][images][of][p][and][p][u][exponentially] decreases under the backward flow. Analogously, for the fibers πb, only with the forward flow._ 

_This is provided that ∥a∥≤ δ, ∥b∥≤ δ and ε_ 0 _, δ >_ 0 _are sufficiently small._ 

_By Bδ,Ufen we will denote the set {_ ( _a, b, x_ ) _∈_ R _[ℓ][u] ×_ R _[ℓ][s] ×_ R _[m] | ∥a∥≤ δ, ∥b∥≤ δ, x ∈ Ufen}. We also put_ Φ _[fen] ε_ := Φ _[fen] |ε fixed._ 

_Sketch proof._ First, the coordinate change. Since _U_ 0 is contractible, we have a normally hyperbolic splitting of trivial bundles _T_ R _[m]_[+] _[n] |U_ 0 = _N[u] ⊕N[s] ⊕ TU_ 0, which gives locally _C[k][−]_[1] coordinates ( _a, b, x_ ) in R _[ℓ][u] ×_ R _[ℓ][s] ×_ R _[m]_ . By Fenichel’s theory (Theorem 225), we can, for each _ε ≥_ 0 sufficiently small, write _Wε[s/u,loc]_ ( _Uε_ ) in these coordinates locally as graphs of some auxiliary functions 

**==> picture [331 x 15] intentionally omitted <==**

such that these functions are _C[k][−]_[1] with a domain on _{x ∈ Ufen ⊂ R[m] , ∥a∥ < δ, ∥b∥ < δ, ∥ε∥ < ε_ 0 _}_ . 

Then we change coordinates by straightening _Wε[u,loc]_ ( _Uε_ ). This introduce new variables ( _a_ 1 _, b_ 1 _, x_ 1) = ( _a, b − h[u]_ ( _a, x, ε_ ) _, x_ ). The Jacobi matrix of the coordinate transformation has a full rank at _a_ = _b_ = 0 _, ε_ = 0, so the transformation is invertible on _{x ∈ Ufen, ∥a∥ < δ, ∥b∥ < δ, ∥ε∥ < ε_ 0 _}_ with _δ, ε_ 0 _>_ 0 sufficiently small. 

Now the argument is similar for the straightening of _Wε[s,loc]_ ( _Uε_ ). Then it remains to straighten the flow invariant fibers of _Wε[s,loc]_ ( _Uε_ ) and _W[s]_ ( _Uε_ ), which were defined in Theorem 228. This involves changing the _x_ -coordinate by the images of the affine maps given by basepoint maps of the fibrations. Again, the rank argument shows that the transformation is invertible on a neighborhood of _a_ = _b_ = 0 _, ε_ = 0. 

The Fenichel normal form follows from looking at invariant sets _a_ = 0 or _b_ = 0 together with the property that projections along fibers intertwine with the flow. In particular, the obtained map _H_ is _C[k][−]_[2] , [Fen77]. 

The signature of eigenvalues of matrices _A_ and _B_ follows from the normal hyperbolicity of _S_ 0 and Taylor expansion estimates; see [Kue15, Prop 4.1.1]. 

**Definition 231.** _[Szm91] Let_ p0 _be a hyperbolic equilibrium of the slow flow on a normally hyperbolic manifold for the fast flow. Then we put_ 

**==> picture [162 x 27] intentionally omitted <==**

_and call the set as the_ _**singular unstable manifold of**_ p0 _. The restriction of W[u][to][the][local][stable][manifolds][for][the][fast][and][slow][flows][is][called][the] sing_[(][p][0][)] _**local singular unstable manifold of**_ p0 _and denoted by Wsing[u,loc]_[(][p][0][)] _[.][We][will] also often use the term_ 

**==> picture [168 x 32] intentionally omitted <==**

101 

_where W_[˜︂] _slow[u]_[(][p][0][)] _[is][a][(compact)]_[codim 0] _[overflowing][submanifold][of][W] slow[ u]_[(][p][0][)] _[.] Analogously, we also define the terms in the stable case._ 

**Corollary 232.** _[Fen79, Szm91] Let S_ 0 _be a normally hyperbolic manifold for the fast flow. Assume also that p_ 0 _∈ S_ 0 _is a normally hyperbolic equilibrium for the slow flow. Then for ε >_ 0 _sufficiently small, there are families of normally hyperbolic equilibria_ p _ε and their local stable and unstable manifolds. Dimensions of the local stable (unstable) manifolds are equal to the sum of stable (unstable) directions in fast and slow flows. The families are C[k][−]_[1] _in ε and describe isotopic C[k] manifolds._ 

_Proof._ Let us consider a Fenichel coordinates around p0. By Remark 226 and the discussion in Example 220, the following holds. The submanifold _Wslow[u,loc]_[(][p][0][)] _[⊂] Ufen_ extends to a smooth family of _W[u,loc]_ (p _ε_ ) _⊂ Ufen_ . Here _W[u,loc]_ (p _ε_ ) are the local unstable manifold for the (slow time) fast-slow flow restricted to _Ufen_ . 

Hence, we can smoothly extend _Wsing[u,loc]_[(][p][0][) to] _[ W] f[ u,loc]_ - _s_[(][p] _[ε]_[) by taking the unstable] fibers over the perturbed _Wslow[u,loc]_[(][p][0][).][Note][that][by][the][flow][invariance][of][fibers] and the exponential decay of solutions in _Wε[u,loc]_ ( _Uε_ ) to _Uε_ (Theorem 230 ( _iv._ )) we obtain that in our case _Wf[u,loc]_ - _s_[(][p] _[ε]_[)][are][not][only][locally][invariant][but][actually] overflowing. 

_Remark_ 233 _._ By the discussion in Example 220 there is also the following extension of Corrollary 232: _W_ ˜︂ _sing[u]_[(][p][0][)] _[⊂][S]_[0][extends][smoothly][to][isotopic] _W_[˜︂] _f[u]_ - _s_[(][p] _[ε]_[),] where _W_[˜︂] _f[u]_ - _s_[(][p] _[ε]_[) which are (compact) codim 0 overflowing submanifolds of] _[ W] f[ u]_ - _s_[(][p] _[ε]_[).] 

## **6.3 Exchange lemma** 

_Remark_ 234 _._ Let us consider the set _U_ 0 from Definition 230. Assume that _U_ 0 is rectifiable. Then we can, after a _C[k][−]_[1] coordinate change, write the Fenichel normal form of (6.4) as 

**==> picture [303 x 54] intentionally omitted <==**

for ( _a, b, x_ ) _∈ Bδ,Ufen ⊂_ R _[ℓ][u] ×_ R _[ℓ][s] ×_ R _[m]_ and _ε ∈_ [0 _, ε_ 0]. Indeed, first we rectify the slow flow along _U_ 0. The Flow box theorem, for instance, can accomplish this. And then we make coordinate changes, as in the proof of Theorem 230. 

By _ϕ[τ] red,ε_[we will denote the] **[ reduced flow]**[ of (6] _[.]_[6) to] _[ U][fen]_[(parametrized with] the fast time). 

_Remark_ 235 _._ By Theorem 230 we know how to track the trajectories _uε_ ( _τ_ ) = ( _x_ ( _τ_ ) _, a_ ( _τ_ ) _, b_ ( _τ_ )) of the system (6 _._ 6) that start in the stable or the unstable manifold, i.e. in the set _{a_ = 0 _}_ or _{b_ = 0 _}_ . 

In this section, we will be interested in tracking _uε_ when _a_ (0) and _b_ (0) are nonzero. First observation will be that the norm of _a_ is exponentially decreasing in the forward time and the norm of _b_ is exponentially decreasing in the backward time. This follows from eigenvalue estimates from Theorem 230 ( _ii._ ), for more details see [JT09, cor 1]. We also remark that these are only _C_[0] estimates for _uε_ . 

102 

In order to have more information about the track of _uε_ or even some flow invariant manifolds, we will present so-called Exchange lemmata which are based on the technique of **Silnikov boundary value problems** [Shi67]. That is a quest to find solutions of (6 _._ 6) on a time interval [0 _, T_ ] with boundary value problems 

**==> picture [284 x 15] intentionally omitted <==**

or 

**==> picture [287 x 14] intentionally omitted <==**

We can heuristically see the existence of the solution to the Silnikov BVP as in Figure 6.1, see also [Hsu15]. The Exchange lemmata, derived from the solutions of two Silnikov BVPs (6 _._ 7), (6 _._ 8), give us two different perspectives on how the tracked invariant manifolds can be parametrized. To the Silnikov BVP (6 _._ 8) will correspond Exchange lemmata 237 and 239 and to BVP (6 _._ 7) corresponds Exchange Lemma 240. 

**==> picture [160 x 161] intentionally omitted <==**

**----- Start of picture text -----**<br>
b [0]<br>0 a [1]<br>**----- End of picture text -----**<br>


Figure 6.1: Trajectories of the system _a[′]_ = _a, b[′]_ = _−b, x[′]_ = 0 in the rectangle _{_ ( _a, b_ ) _∈_ [0 _, a_[1] ] _×_ [0 _, b_[0] ] _}_ can be parametrized by _T ≥_ 0, where _b_ (0) = _b_[0] and _a_ ( _T_ ) = _a_[1] . A solution can stay inside the rectangle for an arbitrarily long time _T_ if it is sufficiently close to the axes. 

_Remark/Notation_ 236 _._ By _**M**_ we will denote a _C[k][−]_[2] submanifold of _Bδ,Ufen ×_ [0 _, ε_ 0], such that _ε_ -level sets are isotopic _C[k][−]_[2] submanifolds. We will denote the _ε_ -levels by _Mε_ . _Mε[∗]_[will][characterize][the][evolution][of] _[M][ε]_[under][the][flow][of][(6] _[.]_[6).] 

The following is a simplified version of Schecter’s formulation of the Exchange Lemma. 

( _ℓu_ + 1) **-Exchange Lemma 237.** _[Sch08] Let us consider the C[k][−]_[2] _system_ (6 _._ 6) _and the_ ( _ℓu_ +1) _-dimensional manifold_ _**M** (from Remark 236). Assume that inside Bδ,Ufen the manifold M_ 0 _intersects {a_ = 0 _} transversally at some point_ ( _b_[0] _,_ 0 _,_ 0) _. Let_ ~~_x_~~ _>_ 0 _such that_ 

**==> picture [205 x 15] intentionally omitted <==**

_(u_ 0 _is parametrized by the slow time) and D be a small neighborhood of_ (0 _,_ ~~_x_ )~~ _in ax_ 1 _-space. Then for ε_ 0 _>_ 0 _sufficiently small there exist C[k][−]_[3] _functions_ 

**==> picture [119 x 34] intentionally omitted <==**

103 

_such that_ 

( _i._ )[˜︁] _b_ ( _a, x_ 1 _,_ 0) = 0 _._ 

( _ii._ ) _x_ ˜︁( _a, x_ 1 _,_ 0) = _x_ ˜︁(0 _, x_ 1 _, ε_ ) = 0 _._ 

( _iii._ ) _As ε →_ 0 _, the functions_ ([˜︁] _b,_ ˜︁ _x_ ) _→_ 0 _exponentially (in uniform norm), along all derivatives up to order k −_ 3 _with respect to all variables._ 

( _iv._ ) _For ε ∈_ (0 _, ε_ 0] _, the set_ 

**==> picture [348 x 17] intentionally omitted <==**

_is contained in Mε[∗][.][See][also][Figure][6.2.]_ 

**==> picture [417 x 150] intentionally omitted <==**

**----- Start of picture text -----**<br>
b<br>M 0 Mε<br>M [∗]<br>M [∗] x ε<br>0<br>x<br>D<br>a<br>**----- End of picture text -----**<br>


Figure 6.2: ( _ℓu_ +1)-Exchange Lemma for _m_ = _ℓs_ = _ℓu_ = 1. _On the left:_ evolution of _M_ 0 under fast flow. _On the right: C[k][−]_[3] -inclination of _Mε_ under the fast-slow flow. 

_Remark/Notation_ 238 _._ [Sch08]Let us consider (6 _._ 6) and the ( _ℓu_ + _σ_ +1)-dimensional manifold _**M**_ (from Remark 236), where 0 _≤ σ ≤ m −_ 1. 

Let us assume that 

- ( _i._ ) Inside _Bδ,Ufen_ the manifold _M_ 0 intersects _{a_ = 0 _}_ transversally in a manifold _N_ 0 (of dimension _σ_ ). 

( _ii._ ) _N_ 0 projects to a _σ_ -dimensional submanifold _P_ 0 of _Ufen_ . 

( _iii._ ) The vector (1 _,_ 0 _, . . . ,_ 0) _[T]_ is not tangent to _P_ 0. 

Note that for _ε_ 0 _>_ 0 small we can (uniquely) define _Nε, Pε_ that satisfy ( _i._ ) _−_ ( _iii._ ) with indices 0 replaced by _ε ∈_ [0 _, ε_ 0]. 

Hence, similarly to Theorem 230 and Remark 234 we can introduce ( _ε_ dependent) _C[k][−]_[1] coordinates ( _a, b, u, v, w_ ) _∈_ R _[ℓ][u] ×_ R _[ℓ][s] ×_ R _×_ R _[σ] ×_ R _[m][−]_[1] _[−][σ]_ , which locally take _Pε_ to the _v_ -space and such that the system (6.6) takes a form 

104 

**==> picture [284 x 88] intentionally omitted <==**

for ( _a, b, u, v, w, ε_ ) _∈ Bδ,Ufen_ and _ε ∈_ [0 _, ε_ 0]. 

The following is another simplified version of Schecter’s formulation of the Exchange Lemma. 

( _ℓu_ + _σ_ + 1) **-Exchange Lemma 239.** _[Sch08] Let us consider the C[k][−]_[1] _system_ (6 _._ 9) _and the_ ( _ℓu_ + _σ_ +1) _-dimensional manifold_ _**M** (from Remark 238). Let_ ~~_u_~~ _>_ 0 _such that_ 

**==> picture [158 x 13] intentionally omitted <==**

_and D be a small neighborhood of_ (0 _,_ ~~_u,_~~ 0) _in auv-space. Then for ε_ 0 _>_ 0 _sufficiently small there exist C[k][−]_[3] _functions_ 

**==> picture [133 x 35] intentionally omitted <==**

_such that_ 

**==> picture [103 x 15] intentionally omitted <==**

( _ii._ ) _w_ ˜︁( _a, u, v,_ 0) = _w_ ˜︁(0 _, u, v, ε_ ) = 0 _._ 

( _iii._ ) _As ε →_ 0 _the functions_ ([˜︁] _b, w_ ˜︁) _→_ 0 _exponentially, along all derivatives up to order k −_ 3 _with respect to all variables._ 

( _iv._ ) _For ε ∈_ (0 _, ε_ 0] _, the set_ 

**==> picture [363 x 42] intentionally omitted <==**

The following is Brunovsk´y’s formulation of the Exchange Lemma. 

( _ℓu_ + _σ_ + 1) **-Exchange Lemma 240.** _[Bru99] Let us consider the C[k][−]_[1] _system_ 

(6 _._ 9) _and the_ ( _ℓu_ + _σ_ + 1) _-dimensional manifold_ _**M** (from Remark 238). Let t >_ 0 _and let Vp be a small neighborhood of_ 0 _in the v-space such that_ 

**==> picture [193 x 14] intentionally omitted <==**

_Let t ∈_ (0 _, t_ ) _and let δ_ 0 _>_ 0 _be small. Then for ε >_ 0 _sufficiently small there is a C[k][−]_[3] _function_ 

**==> picture [220 x 19] intentionally omitted <==**

_such that_ 

**==> picture [175 x 16] intentionally omitted <==**

105 

_for some_ ( _a_[0] _, b_[0] _,_ 0 _, v_[0] _,_ 0) _∈ Mε and τ ∈_ [ _t/ε, t/ε_ ] _if and only if_ 

**==> picture [260 x 15] intentionally omitted <==**

_where x ∈ ϕ[τ] red,ε_[(0] _[, v]_[0] _[,]_[ 0)] _[.]_ 

_Moreover, as ε →_ 0 _the functions s_ ˜︁ _[ε]_ ( _a, x_ ) _→_ (0 _, x_ ) _exponentially, along all derivatives up to order k −_ 3 _with respect to all variables._ 

_To the end, we recall that by our choice of coordinates we have the simplifications_ 

**==> picture [177 x 18] intentionally omitted <==**

_and_ 

**==> picture [135 x 15] intentionally omitted <==**

_Remark_ 241 _._ [Bru99, Rem 4.2, Rem 4.5] By (6 _._ 10) the set _{a} × Graph_ ( _s_ ˜︁ _[ε]_ ) describe only points of those trajectories through _Mε_ over _VP_ (=: _Mε|VP_ ) that do not leave the set _{∥a∥≤ δ_ 0 _}_ . 

Let _u_ ˆ︁ _ε_ : [0 _, τ_ ] _→_ R _[m]_[+] _[n]_ be such a (fast time) trajectory, then in addition 

- _πx_ ( _u_ ˆ︁ _ε_ ) and _ϕ_[[0] _red,ε[,τ]_[]] (︂ _πx_ ( _u_ ˆ︁(0)))︂ are _O_ ( _e[−]_[1] _[/ε]_ ) close (recall also that along _Ufen_ the 1 _/ε_ -multiple of the reduced vector field converges to the slow vector field as _ε →_ 0). 

**==> picture [101 x 14] intentionally omitted <==**

Hence, only the points of _Mε|VP_ with exponentially small _∥a_[0] _∥_ matter. 

_Remark_ 242 _._ From Brunovsk´y’s Exchange Lemma 240 we know that the sets _{a} × Graph_ ( _s_ ˜︁ _[ε]_ ) exponentially converge to the _auv_ -space as _ε →_ 0. So for _ε >_ 0 small the _canonical_ orthogonal projection of _{a} × Graph_ ( _s_ ˜︁ _[ε]_ ) onto _auv_ -space is injective. 

Let us pick some _δ_ 1 _>_ 0 small and _Vp_ as in Brunovsk´y’s Exchange Lemma 240. Hence the set _Graph_ ([˜︁] _b[ε] , w_ ˜︁ _[ε]_ ) from Schecter’s Exchange Lemma 239 can be seen as the set of those points of 

**==> picture [137 x 16] intentionally omitted <==**

that projects orthogonally to _D_ provided that _D_ and _ε >_ 0 are small (here ~~_u_~~ + _δ_ 1 is a slow time). 

_Remark_ 243 _._ We stated the Exchange lemmata in the form of “inclination theorems.” In the literature, another popular version of the Exchange lemma is to track manifolds close to “jumps” of trajectories combining the fast and slow flows; see, for example, [Sch08, JT09, Jon95]. 

## **6.4 Application to Morse flow trees** 

In this section, we relate the flows of _−∇E_ 0 and _−∇Eε_ with the multiple time scale dynamics and show the desired correspondence between the Morse flow trees. Since the proofs of the correspondence are a bit technical, we kindly recommend that the reader looks at Remark 252, where the key steps and ideas of the proofs are outlined. At the end of the section, we briefly discuss some orientation conventions. 

106 

_Example_ 244 _._ The negative gradient vector fields _−∇Eε_ determine a fast-slow system 

**==> picture [349 x 85] intentionally omitted <==**

where ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈_ (R _/T_ Z _× S_[1] )[2] . Recall that _di_ = 1 _− ε_ cos( _θi_ ) _κ_ ( _si_ ), see also Notation 51. 

Then the slow subsystem is given by 

**==> picture [250 x 69] intentionally omitted <==**

and the fast subsystem is given by 

**==> picture [243 x 68] intentionally omitted <==**

Note that the critical set _C_ 0 is given by the set _{G_ 1 = 0 _∧ G_ 2 = 0 _}_ which was described in Remark 130. Also, 

**==> picture [110 x 14] intentionally omitted <==**

Hence, outside of special and diagonal points, _C_ 0 has a structure of normally hyperbolic 2-dimenisonal trivial fiber bundle over ( _s_ 1 _, s_ 2). The typical fiber is given by 4 points. Over a special point, it holds that _C_ 0 is diffeomorphic to the disjoint union of two circles. At the diagonal, _C_ 0 is diffeomorphic to _S_[1] _× S_[1] . 

By _S_ 0 _[out][−][out]_ we will denote a subset of _C_ 0 consisting of normally hyperbolic points such that _⟨P, v_ 1 _⟩ >_ 0 and _⟨P, v_ 2 _⟩ >_ 0. We moreover impose the condition that _πs_ 1 _,s_ 2( _S_ 0 _[out][−][out]_ ) = _SK_ , where the standard set _SK_ was introduced in Remark 47. In particular, _S_ 0 _[out][−][out]_ is diffeomorphic to _SK_ , and hence it is a compact manifold with corners. 

If _x ∈ S[out][−][out]_ , then the linearized fast subsystem has at _x_ a positive eigenvalue _⟨P, v_ 1 _⟩_ with eigenvector _∂θ_ 1 _|x_ and a negative eigenvalue _−⟨P, v_ 1 _⟩_ with eigenvector _∂θ_ 2 _|x_ . 

_Remark_ 245 _._ The special points impose singularities, so-called turning points. For the study of the dynamics around turning points, see, for example, the Exchange lemma in [Sch08]. To the author, it is not known whether anywhere in literature, there exists a study of Multiple-time scale dynamics for singularities of the type of diagonal points, i.e., when all eigenvalues vanish. 

For our purposes, we will be, after careful analysis, able to show that the desired Morse flow trees will generically avoid these singularities. 

107 

**Lemma 246.** _The projection πs_ 1 _,s_ 2 _, when restricted to S_ 0 _[out][−][out] , is a diffeomorphism onto its image. πs_ 1 _,s_ 2 _canonically identifies the slow flow (6.12) on S_ 0 _[out][−][out] with the −∇E_ 0 _flow outside of weakly diagonal and weakly special points._ 

_Proof._ As in Remark 226, we can, due to the normal hyperbolicity, describe _S_ 0 _[out][−][out]_ as a graph over the slow variables. More explicitly, the smooth lift to fast variables is uniquely given as in Lemma 58 by 

**==> picture [214 x 16] intentionally omitted <==**

where _Di_ = _⟨P, n_ ( _si_ ) _⟩_[2] + _⟨P, b_ ( _si_ ) _⟩_[2] _._ Then from Example 244 we know that the _._ differential equations for the slow flow (6 12) are fortunately only in slow variables. In addition, they coincide with the differential equations for the flow _ϕE_ 0. 

_Notation_ 247 _._ The lift from Lemma 246 will be denoted by _i[out-out]_ . 

**Definition 248.** _We say that the gradient-like vector fields XE_ 0 _and XEε are K_ _**approximations** of −∇E_ 0 _and −∇Eε if there is a vector field Y on_ (R _/T_ Z)[2] _such that_ 

**==> picture [219 x 12] intentionally omitted <==**

_where Y_ 0 _is given by equations_ ( _πs_ 1 _,s_ 2) _∗Y_ 0 = _Y and_ ( _πθ_ 1 _,θ_ 2) _∗Y_ 0 = 0 _._ 

_Remark_ 249 _._ Note that unlike the approximations of _−∇Eε_ in Chapter 4 now the _K_ -approximations are perturbing _−∇Eε_ only in _s_ 1 and _s_ 2 variables. 

_Remark_ 250 _._ For _K_ -approximations of _−∇E_ 0 and _−∇Eε_ it holds that _S_ 0 _[out][−][out]_ still consists of normally hyperbolic points and the analogy to Lemma 246 is still true. Indeed, the algebraic equations from the slow subsystem are unchanged, and the differential equations from the slow subsystem are still dependent only on variables _s_ 1 and _s_ 2. 

_Remark_ 251 _._ Let _XE_ 0 and _XEε_ be _K_ -approximations of _−∇E_ 0 and _−∇Eε_ . Let _p_ 0 _∈ Cr_ ( _E_ 0) _\_ ∆0 and _pε_ be the unique corresponding elements from in _Cr_ ( _Eε_ ) _∩ MK,ε_ . Recall that the correspondence is given by Lemma 99, see also equations _. ._ (3 28) 

By p0 and p _ε_ we denote the unique realizations of _p_ 0 and _pε_ as the equilibria of the slow flow on _S_ 0 _[out][−][out]_ and fast-slow flow, respectively. Then p0 = p _ε_ . 

_Remark_ 252 _._ In danger of future repetitiveness, let us make a _road map of further theorems and the key steps of their proofs._ In Theorem 253, Lemmata 256 and 257 we are going to show a bijective correspondence Ψ _[ε]_ between the trees on (R _/T_ Z)[2] and (R _/T_ Z _× S_[1] )[2] with _m_ = 0 _,_ 1 _,_ 2 interior vertices, provided that _ε >_ 0 is small. Then we claim that the cases _m_ = 0 _,_ 1 _,_ 2 capture all phenomena that will be necessary for the proof of any case with _m >_ 2. Recall also that so far we defined the trees only for _Crit_ with low indices and outside of the diagonals, see Chapter 5. So, let us briefly discuss the proofs. 

_m_ = 0 : 

By generic a choice of _XE_ 0 and index reasons we will be able to lift all trees (orbits) on (R _/T_ Z)[2] to corresponding orbits of the slow flow on the normally hyperbolic critical submanifold _S[out][−][out] ⊂_ (R _/T_ Z _×S_[1] )[2] . These orbits of the slow flow can be realized as transverse intersections of singular stable and unstable manifolds. With the help of Fenichel theory and the Stability Lemma 31, we 

108 

perturb compact parts of these singular manifolds. This will construct desired fast-slow orbits and, in particular, give us the definition and injectivity of Ψ _[ε]_ . Then, we continue with a slightly laborious discussion of the local uniqueness of these fast-slow orbits. Such a discussion will be beneficial also in the cases _m_ = 1 _,_ 2. Finally, the surjectivity will be similar to the Theorem 160. 

_m_ = 1 : 

Now, the single interior vertex is present. Since the bifurcations depend also on the embeddings of _K_ and _TK,ε_ into R[3] , it will not be enough to perturb only the singular stable and unstable manifolds. Hence, we will also be perturbing the evaluation maps from Definition 198. For the surjectivity, we use Lemma 200 to show that the projections of the bifurcations of trees on the torus converge to the bifurcations of the trees on the knot. 

_m_ = 2 : 

Now, an interior edge appears. Such an edge corresponds to the space of finite-length trajectories. This space is neither a stable, nor an unstable manifold; hence, the Fenichel theory itself will not be sufficient. So we will represent the tree under the backward flow (see Remark 205) and overcome the interior edge with the Exchange Lemma. 

**Theorem 253.** _Let p_ 0 _∈ Cr_ 1( _E_ 0) _\_ ∆0 _, q_ 0 _∈ Cr_ 0( _E_ 0) _\_ ∆0 _and pε, qε are their unique corresponding critical points of Eε in MK,ε. If ε >_ 0 _is sufficiently small and XE_ 0 _and XEε are generic K-approximations of −∇E_ 0 _and −∇Eε, then there is a map_ 

**==> picture [191 x 15] intentionally omitted <==**

_which is a bijection. In addition,_ 

**==> picture [165 x 17] intentionally omitted <==**

_Proof._ Let _XE_ 0 be generically approximating _−∇E_ 0 in the sense of Corollary 121, i.e. _XE_ 0 is Morse-Bott-Smale and _WX[u]_ 0[(] _[p]_[0][)][is][transverse][to][all][special][points.] 

_Definition of_ Ψ _[ε] p_ 0 _,q_ 0 _[:]_ 

Let _u ∈MXE_ 0 ( _p_ 0 _, q_ 0). By the choice of _XE_ 0 it holds that _u ∈ SK_ , which was defined by _δK >_ 0 sufficiently small. Hence, by Remark 250, there is a small contractible open neighborhood _U_ of _{p_ 0 _∪ u ∪ q_ 0 _} ⊂ K × K_ which can be canonically lifted as a subset _U_ 0 _⊂ S_ 0 _[out][−][out]_ . In particular, we lifted _u_ to _u_ 0 which is an (transverse) intersection of _Wslow[u]_[(][p][0][)][and] _[W] slow[ s]_[(][q][0][)][in] _[U]_[0][.] Now, we are going to construct certain _W_[˜︂] _slow[u]_[(][p][0][)] _[,] W_[˜︂] _slow[s]_[(][q][0][)] _[⊂][U]_[0][,][i.e.][by] Definition 231 compact overflowing/inflowing codim 0 submanifolds of _Wslow[u]_[(][p][0][)] and _Wslow[s]_[(][q][0][),][respectively.] 

We pick an auxiliary slow-time parametrization of _u_ 0. Then _W_[˜︂] _slow[u]_[(][p][0][)][con-] sists of a small local unstable manifold of p0 together with _u_ 0(( _−∞,_ 1]). Next, _W_ ˜︂ _slow[s]_[(][q][0][)][consists][of][a][small][local][stable][manifold][of][q][0][together][with][a][small] neighborhood of _u_ 0([ _−_ 1 _, ∞_ )). Finally, we slightly cut the obtained set (as in Example 148), such that _W_[˜︂] _slow[s]_[(][q][0][) is really inflowing invariant.][Note that] _W_[˜︂] _slow[u]_[(][p][0][)] is overflowing automatically. 

Now we extend _W_[˜︂] _slow[u]_[(][p][0][)][and] _W_[˜︂] _slow[s]_[(][q][0][)][to] _W_[˜︂] _sing[u]_[(][p][0][)][and] _W_[˜︂] _sing[s]_[(][q][0][)][such][that] _W_ ˜︂ _sing[u]_[(][p][0][)] _[,] W_[˜︂] _sing[s]_[(][q][0][)] _[ ⊂]_[(Φ] 0 _[fen]_ ) _[−]_[1] ( _Bδ,Ufen_ ) for some Fenichel coordinates around _U_ 0 with small _δ >_ 0. 

109 

Last, we consider an auxiliary smooth compact 4-disk _D_ in a neighborhood of _u_ 0(0) _∈_ (R _/T_ Z _× S_[1] )[2] . We can choose the disk _D_ small enough such that 

- _u_ 0 ⋔ _∂D_ in exactly two points. 

**==> picture [198 x 46] intentionally omitted <==**

- _πs_ 1 _,s_ 2( _D_ ) _∩ u_ ˆ︁ = _∅_ , where _u_ ˆ︁ _∈MXE_ 0 ( _p_ 0 _, q_ 0) such that _u_ = _u_ ˆ︁ (we recall that _MXE_ 0 ( _p_ 0 _, q_ 0) is a finite set). 

**==> picture [374 x 101] intentionally omitted <==**

Figure 6.3: The intersection of _W_[˜︂] _slow[u]_[(][p][0][)][and] _W_[˜︂] _slow[s]_[(][q][0][)][with] _[D]_[0][:=] _[ D][ ∩][U]_[0][.] 

Then, if _ε_ 0 _>_ 0 is sufficiently small, the Fenichel theory (Corollary 232 and Remark 233) gives us a _C[k]_ -isotopy: 

**==> picture [308 x 19] intentionally omitted <==**

from the canonical inclusion to 

**==> picture [299 x 19] intentionally omitted <==**

On the product of 3 tori (R _/T_ Z _× S_[1] )[6] we consider coordinates 

**==> picture [226 x 13] intentionally omitted <==**

Then we consider the diagonal ∆ _⊂_ (R _/T_ Z _× S_[1] )[6] which is given by 8 equations 

**==> picture [148 x 13] intentionally omitted <==**

We stress that _u_ 0 _⊂ S_ 0 _[out][−][out]_ , which is a normally hyperbolic set. So, by the construction, it holds that _h_[[0]] is stratum transverse to the diagonal ∆and _c_ 0 = _πr_ 1 _,ρ_ 1 _,r_ 2 _,ρ_ 2 (︂( _h_[[0]] ) _[−]_[1] (∆))︂ defines a compact curve _c_ 0 with boundary which is embedded in (R _/T_ Z _×S_[1] )[2] _._ Hence, if _ε_ 0 _>_ 0 is sufficiently small, Stability Lemma 31 and Theorem 25 determine the embedded curves _cε_ = _πr_ 1 _,ρ_ 1 _,r_ 2 _,ρ_ 2 (︂( _h_[[0]] ) _[−]_[1] (∆))︂ _⊂_ (R _/T_ Z _× S_[1] )[2] for each _ε ∈_ [0 _, ε_ 0]. 

In particular, the curves are isotopic, and thus each _cε_ is _C[k] O_ ( _ε_ )-close to _c_ 0. Also, for _ε >_ 0, _cε_ describes the unique (transverse) intersection of _W_[˜︂] _f[u]_ - _s_[(][p] _[ε]_[)][and] _W_ ˜︂ _f[s]_ - _s_[(][q] _[ε]_[)][inside] _[D]_[.][Since] _W_[˜︂] _f[u]_ - _s_[(][p] _[ε]_[)][and] _W_[˜︂] _f[s]_ - _s_[(][q] _[ε]_[)][are][locally][invariant,] _[c][ε]_[is][not] only a curve, but also a (partial) flow trajectory. By continuing flowing along _Wf[u]_ - _s_[(][p] _[ε]_[)][and] _[W][ s] f_ - _s_[(][q] _[ε]_[),][we][extend][to] _[c][ε]_[to][a][heteroclinic][orbit] _[u][ε]_[from][p] _[ε]_[to][q] _[ε]_[.] In addition, _uε_ is transversely cut out. 

110 

Hence, now we put Ψ _[ε] p_ 0 _,q_ 0[(] _[u]_[) :=] _[ u][ε]_[which][determines][a][well][defined][map.] 

_Injectivity of_ Ψ _[ε] p_ 0 _,q_ 0 _[:]_ 

If we consider two distinct _u,_ ˆ︁ _u ∈MXE_ 0 ( _p_ 0 _, q_ 0), then by Stability Lemma 31 Ψ _[ε]_[and][Ψ] _[ε]_[remain][distinct,][provided][that] _[ε >]_[ 0][is][small.] _p_ 0 _,q_ 0[(] _[u]_[)] _p_ 0 _,q_ 0[(] _[u]_[ˆ︁][)] 

_Closeness of u_ 0 _and_ Ψ _[ε] p_ 0 _,q_ 0[(] _[u]_[)] _[(i.e.][u][ε][):]_ We are going to show that for every _δ_ 0 _>_ 0 there is a _ε_ 0 _>_ 0 such that for every _ε ∈_ (0 _, ε_ 0) it holds that 

**==> picture [91 x 13] intentionally omitted <==**

It will be enough to describe the bound for the distance of _ϕ_[[0] _slow[,][∞]_[)][(] _[c]_[0][)][from] _ϕ_[[0] _f_ - _[,] s[∞]_[)][(] _[c][ε]_[),][since][the][bound][in][the][backward][time][can][be][done][analogously.][From] the above, we know that _c_ 0 and _cε_ are _O_ ( _ε_ ) close. Moreover, _c_ 0 _⊂ U_ 0 and _cε ⊂ Uε_ . 

Hence, by Gronwall estimates in Fenichel coordinates, we see that after a finite time _T >_ 0 _ϕ[T] slow_[(] _[c]_[0][)][and] _[ϕ][T] f_ - _s_[(] _[c][ε]_[)][are][still] _[O]_[(] _[ε]_[)-close][(here][recall][that][Feinchel] coordinates depend smoothly on _ε_ ). 

We also know by Remark 233 (and proof of Corollary 232) that _W_[˜︂] _slow[s]_[(][q][0][) and] _W_ ˜︂ _[s]_ (q _ε_ ) (defined by the perturbed slow flow) are isotopic. Hence we can take a small 4-dimensional ball _Bδ_ 0(q0) with the following property. If _ε >_ 0 is small, then by Stability Lemma 31 the intersections _Bδ_ 0(q0) ⋔ _W_[˜︂] _slow[s]_[(][q][0][)][and] _[B][δ]_ 0[(][q][0][)][ ⋔] _W_ ˜︂ _[s]_ (q _ε_ ) are both inflowing manifolds (with respect to given flows). The inflowing property of the intersection follows from eigenvalue estimates as in [JT09, prop 2]. Alternatively, one can use instead of _Bδ_ 0(q0) some _O_ ( _δ_ ) neighborhood of q0 which 

is coming from the graph transform construction of the local stable manifolds. But _c_ 0 _⊂ W_[˜︂] _slow[s]_[(][q][0][)][and] _[c][ε][⊂] W_[˜︂] _[s]_ (q _ε_ ). So once _ϕ[T] slow_[(] _[c]_[0][)][and] _[ϕ]_[[0] _f_ - _[,] s[∞]_[)][(] _[c][ε]_[)][enter] _Bδ_ 0(q0), they got trapped. Thus, we showed that 

**==> picture [163 x 17] intentionally omitted <==**

_Local uniqueness of_ Ψ _[ε] p_ 0 _,q_ 0[(] _[u]_[)] _[(i.e.][u][ε][):]_ 

In particular, we are going to show that there is a closed neighborhood _Vu_ 0 of _u_ 0 with the following property: If _ε >_ 0 is sufficiently small, then _uε_ is the unique element of _MXEε_ ( _pε, qε_ ) that lies (entirely) in _Vu_ 0. 

Pick _x_ 0 _∈ Int_ ( _c_ 0) and _δ_ 1 _>_ 0 small such that _Bδ_ 1( _x_ 0) _⊂ Int_ ( _D_ ). Then we put 

**==> picture [167 x 16] intentionally omitted <==**

where the balls _Bδ_ 1( _x_ 0) and _Bδ_ 1(q0) are “glued” by a thin tube _Tδ_[q] 1[0] _/_ 2[which is just] a tubular neighborhood _νδ_ 1 _/_ 2( _ϕ_[[0] _slow[,][∞]_[)][(] _[x]_[0][)).] 

We can always assume that _δ_ 0 _≪ δ_ 1. Now, note that if _δ_ 1 _>_ 0 is sufficiently small, then _∂Vu_[q] 0[0] _[∩] W_[˜︂] _sing[s]_[(][q][0][) =] _[ ∅][.]_[ Indeed,] _W_[˜︂] _slow[s]_[(][q][0][) is overflowing, so] _[ ϕ]_[[0] _slow[,][∞]_[)][(] _[x]_[0][)] _[ ⊂] Int_ ( _W_[˜︂] _sing[s]_[(][q][0][)).][Since,] _W_[˜︂] _sing[s]_[(][q][0][)][and] _W_[˜︂] _f[s]_ - _s_[(][q] _[ε]_[)][are][isotopic][and][compact,] 

**==> picture [106 x 17] intentionally omitted <==**

provided that _ε >_ 0 is sufficiently small. Note a crucial observation 

111 

- (□) If _y_ 0 _∈ Bδ_ 1( _x_ 0) _\ W_[˜︂] _f[s]_ - _s_[(][q] _[ε]_[)][and][lim] _[t][→∞][ϕ][t] f_ - _s_[(] _[y]_[0][)][=][q] _[ε]_[,][then] _[ϕ]_[[0] _f_ - _[,] s[∞]_[)][(] _[y]_[0][)][does] not lie entirely in _Vu_[q] 0[0][.] 

Indeed, the trajectory from _y_ 0 will enter _W_[˜︂] _f[s]_ - _s_[(][q] _[ε]_[)] _[ \]_[ q] _[ε]_[at][some][point.][This][can] be done only through _∂W_[˜︂] _f[s]_ - _s_[(][q] _[ε]_[).][But] _[∂] W_[˜︂] _f[s]_ - _s_[(][q] _[ε]_[)][does][not][lie][in] _[V] u_[q] 0[0][.] Now, we analogously construct _Vu_[p] 0[0][(with][the][same][constant] _[δ]_[1] _[>]_[ 0).][Finally,] we put 

**==> picture [89 x 15] intentionally omitted <==**

We can assume that _δ_ 1 _>_ 0 is so small that _Vu_ 0 _\ Bδ_ 1( _x_ 0) is a disconnected set. In particular, any heteroclinic orbit form p _ε_ to q _ε_ , that stays in _Vu_ 0, needs to go through _Bδ_ 1( _x_ 0). 

Now we would like to traverse _Vu_ 0 with a certain set _Ku_ 0 that will have nice properties with respect to slow and fast-slow flows. By the continuity of the flow, there is a 1-ball _B_[ˆ︁] _δ_ 1( _x_ 0) _⊂ U_ 0 that is transverse to the slow flow and 

**==> picture [235 x 16] intentionally omitted <==**

is disconnected, provided that _δ_ 1 _>_ 0 is small. We put 

**==> picture [249 x 16] intentionally omitted <==**

see also Figure 6.4. Moreover, if _ε >_ 0 is sufficiently small, then the following holds. By the same computation as in (4 _._ 16), the fast-slow flow is transverse to _K_ 0 “in the same direction” as the slow is transverse to _B_[ˆ︁] _δ_ 1( _x_ 0). 

- _W_ ˜︂ _f[u]_ - _s_[(][p] _[ε]_[)] _W_ ˜︂ _f[s]_ - _s_[(][q] _[ε]_[)] 

- p _ε uε_ q _ε_ 

- _Vu_ 0 _Ku_ 0 

- Figure 6.4: A visualization of the splitting of _Vu_ 0 by _Ku_ 0. Note that _∂W_[˜︂] _f[u]_ - _s_[(][p] _[ε]_[) and] _∂W_[˜︂] _f[u]_ - _s_[(][p] _[ε]_[)][will][have][now][non-empty][intersections][with] _[V][u]_ 0[.][But][the][intersections] will be on the different connected components of the splitting of _Vu_ 0 by _Ku_ 0. Hence, the following holds 

- • If _y_ 0 _∈ Bδ_ 1( _x_ 0) _\_ (︂˜︂ _Wf[s]_ - _s_[(][q] _[ε]_[)] _[ ∩] W_[˜︂] _f[u]_ - _s_[(][p] _[ε]_[)] )︂ and _y_ 0 is contained in some heteroclinic orbit _u_ ˆ︁ _ε_ from p _ε_ to q _ε_ , then _u_ ˆ︁ _ε_ does not lie entirely in _Vu_ 0. 

Finally, since _W_[˜︂] _f[s]_ - _s_[(][q] _[ε]_[)][and] _W_[˜︂] _f[u]_ - _s_[(][p] _[ε]_[)][contribute][by][the][unique][heteroclinic] orbit - _uε_ , the set _Vu_ 0 has the desired property. 

We will also introduce a notation - _Nu[ε]_ 0[which will be a subset of the] _[ G][K,ε]_[-strip] that projects by _πs_ 1 _,s_ 2 to _πs_ 1 _,s_ 2( _Vu_ 0). 

_The surjectivity of the map_ Ψ _[ε] p_ 0 _,q_ 0 _[:]_ 

112 

This follows from a similar argument as the proof of Lemma 163; for the sake of completeness, we will still present the proof. 

By contradiction. Let us assume that there is a sequence _{u_ ˆ︁ _εn}_ of _εn_ -solutions with _εn →_ 0 that are not images of Ψ _[ε] p[n]_ 0 _,q_ 0[.][Which][is][by][the][above][equivalent][to] assume that _u_ ˆ︁ _εn_ are not in any of the sets _Vu_ 0. 

On the other hand, recall the uniform bounds from Theorem 123 on _u_ ˆ︁ _εn_ . Hence, by [FN20, Thm 4.7], the _πs_ 1 _,s_ 2( _u_ ˆ︁ _εn_ ) converge in Floer-Gromov _Cloc_[1][sense] to some broken flow line from _p_ 0 to _q_ 0. But since _XE_ 0 is Morse-Bott-Smale, by the index reason, the limit is in fact a 0-solution. We will denote it by _u_ . Hence, for _n ≫_ 0 it holds that _πs_ 1 _,s_ 2( _uεn_ ) _⊂ πs_ 1 _,s_ 2( _Vu_ 0). Recall also that _u_ is the only 0-solution inside _πs_ 1 _,s_ 2( _Vu_ 0). 

Now, since _πs_ 1 _,s_ 2( _u_ ˆ︁ _εn_ ) _⊂ πs_ 1 _,s_ 2( _Vu_ 0), in particular _u_ ˆ︁ _εn_ avoids special and diagonal points. Hence we can apply Lemma 134 and thus each _u_ ˆ︁ _εn ⊂ Nu[ε]_ 0 _[n]_[.][But,][for] _n ≫_ 0, _Nu[ε]_ 0 _[n][⊂][V][u]_ 0[.][Also,][by][the][construction] _[V][u]_ 0[consists][the][unique] _[ε][n]_[-solution] - _uεn_ . So _u_ ˆ︁ _εn_ = _uεn_ . Contradiction. 

**Theorem 254.** _Let m >_ 1 _and T ∈♣m. Let p_ 0 _∈ Cr_ 1( _E_ 0) _\_ ∆0 _, q_ 0[1] _[, . . . , q]_ 0 _[m][∈] Cr_ 0( _E_ 0) _\_ ∆0 _and pε, qε_[1] _[, . . . , q] ε[m][are][their][unique][corresponding][critical][points][of] Eε in MK,ε. If ε >_ 0 _is sufficiently small and XE_ 0 _and XEε are generic K- approximations of −∇E_ 0 _and −∇Eε, then there is a map_ 

**==> picture [323 x 17] intentionally omitted <==**

_which is a bijection. In addition,_ 

**==> picture [267 x 17] intentionally omitted <==**

_Remark_ 255 _._ We are going to show the proof of Theorem 254 for _m_ = 2 _,_ 3. Then we will claim that we captured all crucial phenomena, and the remaining cases of _m_ are analogous. 

**Lemma 256.** _If m_ = 2 _, then Theorem 254 holds._ 

_Proof._ Let us consider a generic _XE_ 0 as in the proof of Lemma 170, see also Remark 189. I.e. if _u ∈♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, q]_ 0[2][),][then] 

**==> picture [96 x 18] intentionally omitted <==**

provided that the constant _δK >_ 0 (which defines _SK_ ) is small. 

_Definition of_ Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2] _[:]_ Let _u ∈♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, q]_ 0[2][).][By][the][above,][we][can][consider][a][small][neigh-] borhood of _{p_ 0 _∪ u ∪ q_ 0[1] _[∪][q]_ 0[2] _[}]_[in] _[S][K]_[that][consists][of][three][(disjoint)][contractible] components. By Remark 250, we can lift, with _i[out-out]_ , diffeomorphically this neighborhood to some _U_ 0 _∪ U_ 0[1] _[∪][U]_ 0[ 2] _[⊂][S]_ 0 _[out][−][out]_ . Also, _{p_ 0 _∪ u ∪ q_ 0[1] _[∪][q]_ 0[2] _[}]_[is][lifted] to _{_ p0 _∪ u_ 0 _∪_ q[1] 0 _[∪]_[q][2] 0 _[}]_[,][where] _[u]_[0][,][the][lift][of] _[u]_[,][is][locally][invariant][under][the][slow] flow. 

Similar to the proof of Theorem 253, we consider certain manifolds 

**==> picture [284 x 17] intentionally omitted <==**

113 

To do this, we take _W_[˜︂] _slow[u]_[(][p][0][) as an overflowing codim 0 submanifold of] _[ W] slow[ u]_[(][p][0][)] that is inside _U_ 0 and contains _{_ p0 _∪_ ( _u_ 0 _∩ U_ 0) _}_ . And analogously we construct _W_ ˜︂ _slow[s]_[(][q][1] 0[)][and] _W_[˜︂] _slow[s]_[(][q][2] 0[).][We][require][that][the manifolds][from][(6] _[.]_[14)][lie][in][the][set] (Φ0 _[fen]_ ) _[−]_[1] ( _Bδ,Ufen_ ) for some Fenichel coordinates around _U_ 0 _∪ U_ 0[1] _[∪][U]_ 0[ 2][with][small] _δ >_ 0. This fully determines (6 _._ 14). 

Now, we would like to construct certain homotopy of the maps that resemble the evaluation maps from Chapter 5. 

First, we consider a product of three flat tori (R _/T_ Z _× S_[1] )[6] with coordinates (( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _,_ ( _y_ 1 _, α_ 1 _, y_ 3 _, α_ 3) _,_ ( _z_ 2 _, β_ 2 _, z_ 3 _, β_ 3)). And in these coordinates, we will view _W_[˜︂] _sing[u]_[(][p][0][)] _[ ×] W_[˜︂] _sing[s]_[(][q] 0[1][)] _[ ×] W_[˜︂] _sing[s]_[(][q] 0[2][)][as][an][8-dimensional][submanifold.] In particular, we can locally write 

**==> picture [320 x 19] intentionally omitted <==**

where ( _s_ 1( _r_ ) _, s_ 2( _r_ )) is a local parametrization of 1-dimensional _WX[u] E_ 0[(] _[p]_[0][).][Then] _θ_ 1( _s_ 1( _r_ ) _, s_ 2( _r_ )) is a function which is determined by the lift _i[out-out]_ . Analogously, we have the local descriptions 

**==> picture [293 x 19] intentionally omitted <==**

and 

**==> picture [292 x 19] intentionally omitted <==**

Let _x_ be the unique point of _u_ ⋔ _R_ . Now, by _Dx_ we will denote a silly auxiliary 12-dimensional ball 

**==> picture [335 x 19] intentionally omitted <==**

If _δ_ 1 _>_ 0 is sufficiently small, then the following holds 

**==> picture [251 x 45] intentionally omitted <==**

**==> picture [397 x 28] intentionally omitted <==**

**==> picture [232 x 16] intentionally omitted <==**

consists of a single point (the representative of _u_ from the bijection in Corollary 188). Recall also that _♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, q]_ 0[2][)][is][a][finite][set.] 

See also Figure 6.5. 

We take one more time the product of three flat tori (R _/T_ Z _× S_[1] )[6] but now with “bold” coordinates (( _**s**_ 1 _,_ _**θ**_ 1 _,_ _**s**_ 2 _,_ _**θ**_ 2) _,_ ( _**y**_ 1 _,_ _**α**_ 1 _,_ _**y**_ 3 _,_ _**α**_ 3) _,_ ( _**z**_ 2 _,_ _**β**_ 2 _,_ _**z**_ 3 _,_ _**β**_ 3)). Then we canonically embed _Dx_ into this product (R _/T_ Z _× S_[1] )[6] . We will denote the image of the embedding still by _Dx_ . 

Now, as in Theorem 253, if _ε_ 0 _>_ 0 is sufficiently small, the Fenichel theory (Corollary 232 and Remark 233) gives us a _C[k]_ -isotopy _H_ 1: 

**==> picture [390 x 36] intentionally omitted <==**

114 

**==> picture [249 x 212] intentionally omitted <==**

**----- Start of picture text -----**<br>
(R /T Z) [2]<br>**----- End of picture text -----**<br>


Figure 6.5: A neighborhood of the bifurcation of _u_ depicted in the single configuration space (R _/T_ Z)[2] . In more detail, after the canonical identification the curves _R, R[L] , R[U]_ and the three projections _πs_ 1 _,s_ 2( _Dx_ ) _, πy_ 1 _,y_ 3( _Dx_ ) _, πz_ 3 _,z_ 2( _Dx_ ) are visualized in the same space. 

from the canonical inclusion to _h_[[] 1 _[ε]_[0][]] : 

**==> picture [382 x 40] intentionally omitted <==**

We remark, that the convention of the coordinates on (R _/T_ Z _× S_[1] )[6] _×_ [0 _,_ 1] _×_ (R _/T_ Z _× S_[1] )[6] is the following. On the first factor of (R _/T_ Z _× S_[1] )[6] _×_ [0 _,_ 1] _×_ (R _/T_ Z _× S_[1] )[6] we have the “bold” coordinates. So by _π_ non-bold we understand the canonical projection onto the remaining coordinates. 

Next, we define a smooth homotopy 

_H_ 2 : (R _/T_ Z _×S_[1] )[6] _×_ [0 _,_ 1] _×_ (R _/T_ Z _×S_[1] )[6] _→_ (R _/T_ Z _×S_[1] )[6] _×_ ( _S_[1] )[3] _×_ (R _/T_ Z)[3] _×_ R[3] by 

**==> picture [150 x 19] intentionally omitted <==**

for every _ε ∈_ [0 _, ε_ ]. Here, the maps ev _ε_ were introduced in Definition 198. The map evauxil is just given as a difference of each “bold” coordinate with the corresponding “non-bold” coordinate. I.e. for example _**s**_ 1 _− s_ 1. Note that the coordinate _ℓ ∈_ [0 _,_ 1] does not have a “bold” coordinate equivalent, and hence does not appear in evauxil. 

Finally, we define a _C[k]_ homotopy _H_ : 

**==> picture [387 x 36] intentionally omitted <==**

as the horizontal composition _H_ 2 _◦ H_ 1, i.e. 

**==> picture [82 x 15] intentionally omitted <==**

115 

It is crucial to observe that 

(∆) _h_[[0]] ⋔ 0 and ( _h_[[0]] ) _[−]_[1] (0) consists of a single point, where in addition 

**==> picture [178 x 19] intentionally omitted <==**

Now, we would like to enlight (∆). Let x 0 := ( _h_[[0]] ) _[−]_[1] (0). First, note that _h_[[0]] 1 is just an inclusion that adjusts the domain, where we would like to count the zeros of _h_[[0]] . By the descriptions (6 _._ 15) _,_ (6 _._ 16) _,_ (6 _._ 17) we see that at x 0 the coordinates _α_ 1 _, θ_ 2 _, β_ 3 are uniquely determined by _θ_ 1( _s_ 1( _r_ ) _, s_ 2( _r_ )) _, β_ 2( _z_ 2 _, z_ 3) _, α_ 1( _y_ 1 _, y_ 3), respectively. Hence, by the definition of _Dx_ and relation (5.2) we obtain that x 0 is a single point and _πs_ 1 _,θ_ 1 _,s_ 2 _,θ_ 2( x 0) = _i[out-out]_ ( _x_ ) _._ In addition, by Lemma 177 it follows that ev0 _◦ π_ non-bold ⋔ 0. Finally, from the definition of _Dx_ , we immediately get that evauxil ⋔ 0. 

Hence, if _ε_ 0 _>_ 0 is small, Stability Lemma 31 determines a _C[k]_ -family of points 

**==> picture [177 x 21] intentionally omitted <==**

which by Corollary 204 uniquely determines a family of trees 

**==> picture [163 x 15] intentionally omitted <==**

We will also use a notation 

**==> picture [101 x 13] intentionally omitted <==**

Finally, we put Ψ _[ε] T_ ; _p_ 0; _q_ 0[1][;] _[q]_ 0[2][(] _[u]_[) :=] _[ u][ε]_[which][determines][a][well][defined][map.] 

_Injectivity of_ Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2] _[:]_ 

It is a straightforward consequence of the Stability Lemma 31 and Corollary 204. 

_Closeness of u_ 0 _and_ Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2][(] _[u]_[)] _[(i.e.][u][ε][):]_ We would like to show that for every _δ_ 0 _>_ 0 there is a _ε_ 0 _>_ 0 such that for every _ε ∈_ (0 _, ε_ 0) it holds that 

**==> picture [91 x 13] intentionally omitted <==**

For this, we have to compare the distance of each edge of _uε_ from _u_ 0. 

For example, we have to compare the distance of _ϕ_[(] _f[−∞]_ - _s[,]_[0]] ( _xε_ ) from _ϕ_[(] _slow[−∞][,]_[0]] ( _x_ 0). By Stability Lemma 31 we know that _x_ 0 and _xε_ are _O_ ( _ε_ ) close. But since _x_ 0 _∈ U_ 0 and _xε ∈ W[u]_ ( _Uε_ ), it follows that also _x_ 0 and _πa_ ( _xε_ ) are _O_ ( _ε_ ) close (here _πa_ is the base projection from Fenichel fibration - Theorems 228 and 230). So by the same argument as in Theorem 253 we can bound the distance of _ϕ_[(] _f[−∞]_ - _s[,]_[0]] ( _πa_ ( _xε_ )) from _ϕ_[(] _slow[−∞][,]_[0]] ( _x_ 0). Moreover the distance of _xε_ and _πa_ ( _xε_ ) exponentially decay in backward-time by Theorems 228 which imply the bound for the distance of _ϕ_[(] _f[−∞]_ - _s[,]_[0]] ( _xε_ ) from _ϕ_[(] _slow[−∞][,]_[0]] ( _x_ 0). 

_Local uniqueness of_ Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2][(] _[u]_[)] _[(i.e.][u][ε][):]_ 

116 

In particular, we are going to show that there is a closed neighborhood _Vu_ 0 of _u_ 0 with the following property: If _ε >_ 0 is sufficiently small, then _uε_ is the unique element of _♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, q] ε_[2][)][that][lies][(entirely)][in] _[V][u]_ 0[.] In fact, this is an easier version of the local uniqueness from the proof of Theorem 253. We just construct _Vu_ 0 _⊂_ (R _/T_ Z _× S_[1] )[2] as the union of small neighborhoods _Vu_[p] 0[0] _[, V] u_ q0[1] 0 _, Vu_ q0[2] 0 which are around the connected components of _u_ 0. Then the local uniqueness will follow from Stability Lemma 31, definition of _Dx_ together with the observation (□) from the proof of Theorem 253. 

_Trap for trees:_ 

In particular, using a similar technique as was in Lemma 134, we are going to construct a subset _Nu[ε]_ 0 _[⊂][V][u]_ 0[with][the][following][property:][if] _[ε][>]_[0][is][small][and] _u_ ˆ︁ _ε ∈♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, q] ε_[2][)][such][that] _[π][s]_ 1 _[,s]_ 2[(] _[u]_[ˆ︁] _[ε]_[)] _[ ⊂][π][s]_ 1 _[,s]_ 2[(] _[N] u[ ε]_ 0[),][then] _[u]_[ˆ︁] _[ε][⊂][N] u[ ε]_ 0[.] We define _Nu[ε]_ 0[as][the][union][of][the][following][three][sets.] 

_Nu[ε,]_ 0[p][0] = {︂( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈ MK,ε |_ ( _s_ 1 _, s_ 2) _∈ πs_ 1 _,s_ 2( _Vu_[p] 0[0][)] _[ ∧|⟨][P, v]_ 1 _[⊥][⟩|][ < ε]_[1] _[/]_[2] _[ ∧|⟨][P, v]_ 2 _[⊥][⟩|][ < ε]_[1] _[/]_[3][}︂] _, Nu[ε,]_ 0[q] 0[1] = {︂( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈ MK,ε |_ ( _s_ 1 _, s_ 2) _∈ πs_ 1 _,s_ 2( _Vu_[q] 00[1][)] _[ ∧|⟨][P, v]_ 1 _[⊥][⟩|][ < ε]_[1] _[/]_[3] _[ ∧|⟨][P, v]_ 2 _[⊥][⟩|][ < ε]_[1] _[/]_[2][}︂] _, Nu[ε,]_ 0[q] 0[2] = {︂( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _∈ MK,ε |_ ( _s_ 1 _, s_ 2) _∈ πs_ 1 _,s_ 2( _Vu_[q] 00[2][)] _[ ∧|⟨][P, v]_ 1 _[⊥][⟩|][ < ε]_[1] _[/]_[3] _[ ∧|⟨][P, v]_ 2 _[⊥][⟩|][ < ε]_[1] _[/]_[2][}︂] _._ 

It remains to enlight, why the defined set _Nu[ε]_ 0[has][the][desired][properties.] So let _u_ ˆ︁ _ε ∈♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, q] ε_[2][)][such][that] _[π][s]_ 1 _[,s]_ 2[(] _[u]_[ˆ︁] _[ε]_[)] _[⊂][π][s]_ 1 _[,s]_ 2[(] _[N] u[ ε]_ 0[).][Recall][also] that _πs_ 1 _,s_ 2( _Nu[ε]_ 0[)] _[⊂][S][K]_[and][p] _[ε][⊂][S][out][−][out]_[.][Hence][from][Figure][4.1][in][the][proof] of Lemma 134 we immediately see that over _πs_ 1 _,s_ 2( _Nu[ε,]_ 0[p][0][)] _[u]_[ˆ︁] _[ε]_[has][to][satisfy][the] relations _F_ 1[[] _[ε]_[]] _≥_ 0 _∧|⟨P, v_ 1 _[⊥][⟩|][<][ε]_[1] _[/]_[2][.][Here][we][remark][that][since] _[ε]_[1] _[/]_[2] _[>][c][G][ε]_[,][the] “inward-pointing behavior” of _XEε_ along _⟨P, v_ 1 _[⊥][⟩]_[=] _[ ε]_[1] _[/]_[2][and] _[⟨][P, v]_ 1 _[⊥][⟩]_[=] _[ C][G][ε]_[is][the] same, see also Theorem 133 ( _iii._ ). 

Analogously we obtain that over _πs_ 1 _,s_ 2( _Nuε,_ 0q[1] 0) _u_[ˆ︁] _ε_ has to satisfy the relations _F_ 2[[] _[ε]_[]] _≥_ 0 _∧|⟨P, v_ 2 _[⊥][⟩|][ < ε]_[1] _[/]_[2][.][In][fact,][by][Lemma][129,] _[F]_ 2[ [] _[ε]_[]] _≥ δ_[ˆ︁] for some _δ_[ˆ︁] _>_ 0. Let _yε ∈ R_[ˆ︃] ˆ︃ _ε._ Hence, by Lemma 206, we see that also the point _yε_ has to satisfy _F_ 2[[] _[ε]_[]] _≥_ 0 _∧|⟨P, v_ 2 _[⊥][⟩|][<][ε]_[1] _[/]_[3][provided][that] _[ε][>]_[0][is][small.][Hence][the][same] argument as in Lemma 134 implies that over _πs_ 1 _,s_ 2( _Nu[ε,]_ 0[p][0][)] _[u]_[ˆ︁] _[ε]_[has][also][to][satisfy] the relations _F_ 2[[] _[ε]_[]] _≥_ 0 _∧|⟨P, v_ 2 _[⊥][⟩|][<][ε]_[1] _[/]_[3][.][In][particular,][over] _[π][s]_ 1 _[,s]_ 2[(] _[N] u[ ε,]_ 0[p][0][)] _[u]_[ˆ︁] _[ε]_[is] contained in _Nu[ε,]_ 0[p][0][.][Arguments][for][the][remaining][sets][are][analogous.] 

_Surjectivity of_ Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2] _[:]_[The][argument][is][almost][the][same][as][in][the][surjec-] tivity in Theorem 253. The only difference in the logic is that now _πs_ 1 _,s_ 2( _u_ ˆ︁ _εn_ ) does not subsequentially _Cloc_[1][converge][to][some][(potentially)][broken][flow][line.] However, by Lemma 200 we know that 

**==> picture [199 x 21] intentionally omitted <==**

as _εn →_ 0. So by [Mes16, thm 4.22] _πs_ 1 _,s_ 2( _u_ ˆ︁ _εn_ ) subsequentially _Cloc_[1][converge] to some broken Morse flow tree _u_ with leaves corresponding to _p_ 0 _, q_ 0[1] _[, q]_ 0[2][and][a] single interior vertex. But by generic assumptions on _XE_ 0 it follows that _u ∈ ♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, q]_ 0[2][).] 

**Lemma 257.** _If m_ = 3 _, then Theorem 254 holds._ 

117 

**==> picture [201 x 97] intentionally omitted <==**

**----- Start of picture text -----**<br>
v 3<br>v 0<br>v 2<br>vb [int]<br>va [int] v 1<br>**----- End of picture text -----**<br>


Figure 6.6: The chosen tree _T ∈♣_ 3. _T_ has one interior edge, the vertex _v_ 0 is the root and recall that the exterior vertices _v_ 1 _, v_ 2 _, v_ 3 are ordered. 

_Proof._ Let us consider a tree _T ∈♣_ 3 as in Figure 6.6. 

The key difference from Lemma 256 is that now _T_ contains an interior edge. Interior edges, as we know from Corollaries 188 and 204, correspond to the space of positive finite-length trajectories. Such a space is clearly neither a stable, nor an unstable manifold, so the perturbations of such a space can not be fully captured by Fenichel theory. However, we will be able to construct the perturbed trees _iteratively under the backward flow ϕ[−] X[t] Eε_[as][was][discussed][in][Remark][205.] In particular, in order to track the perturbed trajectories along the interior edge, we will use the Exchange lemma 240. 

_Definition of_ Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2] _[,q]_ 0[3] _[:]_ 

First, as in Lemma 256, we take a generic _XE_ 0 and _u ∈♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, q]_ 0[2] _[, q]_ 0[3][).] We also lift with the map _i[out-out]_ a small neighborhood of _{p_ 0 _∪ u ∪ q_ 0[1] _[∪][q]_ 0[2] _[∪][q]_ 0[3] _[}]_ to _U_ 0 _∪ U_ 0 _[int] ∪ U_ 0[1] _[∪][U]_ 0[ 2] _[∪][U]_ 0[ 3] _[⊂][S][out][−][out]_[.][The][lift][of] _[u]_[will][be][denoted][by] _[u]_[0][.][We] construct manifolds 

**==> picture [207 x 17] intentionally omitted <==**

analogously to (6.14). Let _x ∈ u ∩R_ be the unique point that corresponds to the bifurcation of _u_ at the vertex _va[int]_[.][Then we construct a small 12-dimensional] ball _Dx_ as in Lemma 256. Now, similarly to (6.18) we define a _C[k]_ homotopy 

**==> picture [381 x 36] intentionally omitted <==**

Note that the domain of _H_ now contains a whole copy of the configuration space (R _/T_ Z _×S_[1] )[2] instead of _W_[˜︂] _sing[u]_[(][p][0][) and on this space act] _[ h]_ 1[[] _[ε]_[]][by the identity.][Recall] also that we see (R _/T_ Z _×S_[1] )[2] _×W_[˜︂] _sing[s]_[(][q] 0[1][)] _[×]_[ ˜︂] _Wsing[s]_[(][q] 0[2][) as a submanifold of the mani-] fold (R _/T_ Z _×S_[1] )[6] with the coordinates (( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _,_ ( _y_ 1 _, α_ 1 _, y_ 3 _, α_ 3) _,_ ( _z_ 2 _, β_ 2 _, z_ 3 _, β_ 3)). Similarly to (∆) from Lemma 256 it follows that 

- _h_[[0]] ⋔ 0 and _πs_ 1 _,θ_ 1 _,s_ 2 _,θ_ 2 (︂( _h_[[0]] ) _[−]_[1] (0))︂ is an embedded 2-dimensional submanifold of _πs_ 1 _,θ_ 1 _,s_ 2 _,θ_ 2( _Dx_ ) which can be locally written as 

**==> picture [166 x 19] intentionally omitted <==**

where ( _s_ 1( _r_ ) _, s_ 2( _r_ )) is a local parametrization of the 1-dimensional manifold _R_ , _θ_ 2( _s_ 1( _r_ ) _, s_ 2( _r_ )) is a function determined by _i[out-out]_ and _θ_ 1 vary in intervals around the function _θ_ 1( _s_ 1( _r_ ) _, s_ 2( _r_ )) (which is also given by the lift _i[out-out]_ ). 

118 

Hence if _ε_ 0 _>_ 0 is small, Stability Lemma 31 and Theorem 25 determine a _C[k]_ -family of isotopic submanifolds 

**==> picture [184 x 22] intentionally omitted <==**

of _πs_ 1 _,θ_ 1 _,s_ 2 _,θ_ 2( _Dx_ ). 

By the genericity of _XE_ 0, we know that at _x_ it holds that _u_ ⋔ _R_ . Also by Lemma 178 _x ∈/ Crit_ ( _E_ 0). So if _Dx_ is sufficiently small, then _R[θ]_ 0[1] _[∩][U]_ 0 _[ int]_ is transverse to the slow flow. 

Let _t >_ 0 be the time length of the trajectory of _u_ that corresponds to the _t,_ 0] interior edge. Now, in a small neighborhood of _ϕ_[[] _slow[−]_[(] _[i][out-out]_[(] _[x]_[))][we][would][like] to flow from _R[θ] ε_[1][with][the][fast-slow][flow][for][a][(slow)][time] _[−] t − δ_ 1, where _δ_ 1 _>_ 0 is small. The result will be denoted by ( _R[θ] ε_[1][)] _[∗]_[.][Since][the][evolution][of] _[R][θ] ε_[1] in time has to be captured by Exchange Lemmata 239 or 240, we can understand ( _R[θ] ε_[1][)] _[∗]_[only][as][a][set][that][comes][from][some] _[B][U] fen[,δ]_[given][by][Fenichel][coordinates.] In particular, by Remark 241 ( _R[θ] ε_[1][)] _[∗]_[will][not][contain][the][points][that][evolve][too] far in the _θ_ 1-direction from _Uε[int]_ (or more precisely, ( _R[θ] ε_[1][)] _[∗]_[will][not][overflow][from] the set (Φ _[fen] ε_ ) _[−]_[1] ( _∥b∥≤ δ_ )). 

Let _δ_ 2 _>_ 0 be small. Then by Exchange Lemma 239 and Remark 242 there is a closed _O_ ( _δ_ 2) neighborhood _Bδ_ 2 of _ϕslow[−] t_[(] _[i][out-out]_[(] _[x]_[))][such][that] _[B][δ]_ 2 _[∩][W] sing[ s]_[(] _[U]_ 0 _[ int]_[)] together with _{Bδ_ 2 _∩_ ( _R[θ] ε_[1][)] _[∗][}][ε][∈]_[(0] _[,ε]_ 0[]][form][a] _[C][k]_[family][of][isotopic][3-dimensional] submanifolds of (R _/T_ Z _× S_[1] )[2] , provided that _ε_ 0 _>_ 0 is small. We recall that as _ε →_ 0 ( _R[θ] ε_[1][)] _[∗]_[are approaching the stable manifold] _[ W] sing[ s]_[(] _[U]_ 0 _[ int]_[), since we are using] the backward-flow. 

Now, analogously to Lemma 256, we are in the situation where we want to perturb a certain transverse intersection which corresponds to the interior vertex _vb[int]_[.][In more detail, we want to perturb the “intersection” of] _W_[˜︂] _sing[u]_[(][p][0][)] _[,] W_[˜︂] _sing[s]_[(][q] 0[3][)] and _Bδ_ 2 _∩ Wsing[s]_[(] _[U]_ 0 _[ int]_[)][together][with][some][small][auxiliary][(12-dimensional)][ball] _D_ ˆ︂ _⊂_ (R _/T_ Z _× S_[1] )[6] (radius of _D_[ˆ︂] will be much smaller then _δ_ 2 _>_ 0). In particular, Stability Lemma 31 will gives us a _C[k]_ -family of points 

**==> picture [83 x 16] intentionally omitted <==**

provided that _ε_ 1 _>_ 0 is small. 

Finally, note that by Remark 205 and Corollary 204 each of y _ε_ determines the unique tree _uε ∈♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, q] ε_[2] _[, q] ε_[3][).][In][particular,][the][assignment] _[u][ ↦→][u][ε]_ gives us a well defined map Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2] _[,q]_ 0[3][.] 

_Injectivity of_ Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2] _[,q]_ 0[3] _[:]_ By Stability Lemma 31 and finiteness of _♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, q]_ 0[2] _[, q]_ 0[3][) we obtain that] two different elements of _♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, q]_ 0[2] _[, q]_ 0[3][) will contribute by two disjoint sets] _R[θ] ε_[1][.][Then][the][injectivity][of][Ψ] _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2] _[,q]_ 0[3][follows.] 

_Closeness of u_ 0 _and_ Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2] _[,q]_ 0[3][(] _[u]_[)] _[(i.e.][u][ε][):]_ We would like to show that for every _δ_ 0 _>_ 0 there is a _ε_ 0 _>_ 0 such that for every _ε ∈_ (0 _, ε_ 0] it holds that 

**==> picture [91 x 13] intentionally omitted <==**

119 

For this, we have to compare the distance of each edge of _uε_ from _u_ 0. The cases of edges between _vb[int]_ and _v_ 0 or _v_ 3 are solved as in Lemma 256. So let us focus on the interior edge. 

For _ε ∈_ [0 _, ε_ 1] let us denote by _yε_ the unique projection of y _ε_ into ( _R[θ] ε_[1][)] _[∗]_[.][In] particular, by the construction of y _ε_ it follows that _yε_ are _O_ ( _ε_ ) close to _y_ 0. Also, by Remark 241 the fast-slow trajectory from _yε_ reaches _R[θ] ε_[1] after a slow time _t_ 1 + _O_ ( _ε_ ). Let denote such a trajectory by _u_ ˜︁ _ε_ . 

Recall also that _R[θ] ε_[1] and _R[θ]_ 0[1][are] _[O]_[(] _[ε]_[)-close][in][the][“unstable”][direction] _[θ]_[2][.] Hence by Remark 241 and the monotonicity estimates from Remark 235 it follows that _u_ ˜︁ _ε_ and _u_ ˜︁0 are _O_ ( _ε_ ) close. Hence, also the terminate points of _u_ ˜︁ _ε_ and _u_ ˜︁0 are _O_ ( _ε_ ) close, and thus also their unique lifts to ( _h_[[] _[ε]_[]] ) _[−]_[1] (0) and ( _h_[[0]] ) _[−]_[1] (0) are _O_ ( _ε_ )- close. Then the distance of the remaining edges of _uε_ from _u_ 0 follows again as in Lemma 256. 

_Local uniqueness of_ Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2] _[,q]_ 0[3][(] _[u]_[)] _[(i.e.][u][ε][):]_ In particular, we are going to show that there is a closed neighborhood _Vu_ 0 of _u_ 0 with the following property: If _ε >_ 0 is sufficiently small, then _uε_ is the unique element of _♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, q] ε_[2] _[, q] ε_[3][)][that][lies][(entirely)][in] _[V][u]_ 0[.] Similarly to the proof of Theorem 253 we put 

**==> picture [193 x 15] intentionally omitted <==**

where _δ_ 3 _>_ 0 such that _δ_ 3 _≪_ min _{δ, δ_ 1 _, δ_ 2 _,_ radii of _Dx_ and _D_[ˆ︂] _}_ . I.e. we “glued” the balls _Bδ_ 3( _y_ 0) _, Bδ_ 3( _ϕtslow_[(] _[y]_[0][))][by][a][thin][tube] _[T][δ]_ 3[which][is][just][a][tubular][neigh-] _t_ ) _t_ borhood _νδ_ 3( _ϕ_[(0] _slow[,]_[(] _[y]_[0][)).][Recall][also][that] _[ϕ] slow_[(] _[y]_[0][) =] _[ i][out-out]_[(] _[x]_[).] 

Now, we claim that 

( _⃝_ ) If there is a _z ∈ Bδ_ 3( _y_ 0) _\_ ( _R[θ] ε_[1][)] _[∗]_[and][a][(slow][time)] _[t]_[1] _[>]_[0][such][that] _ϕ[t] f_[1] - _s_[(] _[z]_[)] _[ ∈R][θ] ε_[1] _[∩][B][δ]_ 3[(] _[ϕ] tslow_[(] _[y]_[0][)),][then] _[ϕ]_[[0] _f_ - _[,t] s_[1][]][(] _[z]_[)][does][not][lie][entirely][in] _[V] u[int]_ 0 _[.]_ 

In order to show ( _⃝_ ) we would like to use as in (□) (Theorem 253) the local invariance of ( _R[θ] ε_[1][)] _[∗]_[.][Hence,][let][us][inspect][the][topological][boundary] _[∂]_[(] _[R][θ] ε_[1][)] _[∗]_[.] First, it contains _R[θ] ε_[1][which has clearly nonempty intersection with] _[ V] u[int]_ 0[.][How-] ever, the slow flow is strictly outward-pointing from ( _R[θ] ε_[1][)] _[∗]_[along] _[R][θ] ε_[1][,][and][thus] no trajectory can enter ( _R[θ] ε_[1][)] _[∗]_[along] _[R][θ] ε_[1][.] 

Now we would like to show that the remaining components of the boundary _∂_ ( _R[θ] ε_[1][)] _[∗]_[lie][outside][of][the] _[V] u[int]_ 0[,][which][will][imply][(] _[⃝]_[).] By Remarks 241 under the backward-flow ( _R[θ] ε_[1][)] _[∗]_[contains,][as][a][part][of][the] boundary, ( _R[θ] ε_[1][)] _[∗][∩]_[(Φ] _[fen] ε_ ) _[−]_[1] ( _∥b∥≤ δ_ ), but since _δ_ 3 _≪ δ_ , we do need to worry about this. Recall also that ( _R[θ] ε_[1][)] _[∗][∩]_[(Φ] _[fen] ε_ ) _[−]_[1] ( _∥a∥≤ δ_ ) = _∅_ by Remark 235. The remaining boundary phenomena can be captured by the behavior of the slow variables. In particular, by Remark 241 and the fact that _δ_ 3 _≪ δ_ 1 it follows that ( _R[θ] ε_[1][)] _[∗][∩][ϕ] f[−]_ - _ts−δ_ 1( _R[θ] ε_[1][)][is][outside][of] _[V] u[int]_ 0[.][Since] _[δ]_[3][is][much][smaller][then][the] _t−δ_ 1 _,_ 0) radius of _Dx_ we can treat the case ( _R[θ] ε_[1][)] _[∗][∩][ϕ] f_[(] _[−]_ - _s_ ( _∂R[θ] ε_[1][) analogously.][And the] claim ( _⃝_ ) follows. Now, similarly to Lemma 256 the discs _D, D_[ˆ︂] _x_ induce small neighborhoods _Vu_[p] 0[0] _[, V] u_ q0[1] 0 _, Vu_ q0[2] 0 _, Vu_ q0[3] 0 . Finally, their union together with _Vu[int]_ 0[induce] _[V][u]_ 0[.] 

_Trap for trees:_ 

120 

In particular, we would like to construct a subset _Nu[ε]_ 0 _[⊂][V][u]_ 0[with the following] property: if _ε >_ 0 is small and _u_ ˆ︁ _ε ∈♣XEε_ ( _T_ ; _pε_ ; _qε_[1] _[, q] ε_[2] _[, q] ε_[3][)][such][that] _[π][s]_ 1 _[,s]_ 2[(] _[u]_[ˆ︁] _[ε]_[)] _[⊂] πs_ 1 _,s_ 2( _Nu[ε]_ 0[),][then] _[u]_[ˆ︁] _[ε][⊂][N] u[ ε]_ 0[.] This is done by the same trick as in Lemma 256, one only has ensure that the conditions _|⟨P, vi[⊥][⟩|][<][ε][j]_[are][still][satisfied][when][translated][over][the][interior] vertices. For this, one can use suitable powers of _ε_ , provided that _ε >_ 0 is sufficiently small. 

For example, we can define _Nu[ε]_ 0[as][the][union][of][the][following][five][sets.] 

**==> picture [460 x 107] intentionally omitted <==**

_Surjectivity of_ Ψ _[ε] T_ ; _p_ 0; _q_ 0[1] _[,q]_ 0[2] _[,q]_ 0[3] _[:]_[Now,][it][follows][from][the][same][argument][as][in] Lemma 256. 

Now, we are going to briefly discuss some **orientation conventions** . 

_Remark_ 258 _._ Let us consider the canonical orientations on (R _/T_ Z)[2] and (R _/T_ Z _× S_[1] )[2] which are given by coordinates ( _s_ 1 _, s_ 2) and ( _s_ 1 _, θ_ 1 _, s_ 2 _, θ_ 2) _._ Then on _S[out][−][out]_ we induce an orientation by the orientation on _SK ⊂_ (R _/T_ Z)[2] such that the map _i[out-out]_ is orientation preserving. 

Now, at each point _p_ 0 _∈ Crit_ ( _E_ 0) _\_ ∆0 we choose an arbitrary orientation of _WX[u] E_ 0[(] _[p]_[0][).][Then][by][Lemma][246][the][canonical][isomorphism] _[T][p]_ 0 _[W][ u] XE_ 0[(] _[p]_[0][)] _[∼]_[=] _T_ p0 _Wslow[u]_[(][p][0][)][induces][an][orientation][on] _[W] slow[ u]_[(][p][0][)][(where][p][0] _[⊂][S][out][−][out]_[).][More-] over, by Fenichel theory, we have an isomorphism 

**==> picture [297 x 15] intentionally omitted <==**

which induces an orientation of _Wf[u]_ - _s_[(][p] _[ε]_[).] Next, the orientation on _WX[s] E_ 0[(] _[p]_[0][)][is][given][by] 

**==> picture [223 x 17] intentionally omitted <==**

which gives us also an orientation of _Wslow[s]_[(][p][0][).][Analogously,][by][Fenichel][theory,] we have an isomorphism 

**==> picture [297 x 14] intentionally omitted <==**

which induce an orientation of _Wf[s]_ - _s_[(][p] _[ε]_[).] Note that the orientations of stable and unstable manifolds at p0 and p _ε_ match in the following sense: there are orientation-preserving isomorphisms 

**==> picture [324 x 18] intentionally omitted <==**

and 

**==> picture [243 x 16] intentionally omitted <==**

121 

_Remark_ 259 _._ Let _M_ be an oriented manifold with oriented submanifolds _Q_ 1 _, Q_ 2. Let moreover _N_ := _Q_ 1 ⋔ _Q_ 2. Then we orient _N_ by the convention that at some _x ∈ N_ the ordered set 

**==> picture [297 x 13] intentionally omitted <==**

is an oriented basis of _TxM_ . Here _{e_ 1 _, . . . , ej}_ is an oriented basis of _TxQ_ 1, _{ei_ +1 _, . . . , en}_ is an oriented basis of _TxQ_ 2. And finally _{ei_ +1 _, . . . , ej}_ is a basis of _TxN_ with the determined orientation. 

_Remark_ 260 _._ Let _p_ 0 _∈ Crit_ 1( _E_ 0) _\_ ∆0 _, q_ 0 _∈ Crit_ 0( _E_ 0) _\_ ∆0 and _pε, qε_ will be the corresponding _Crit_ ( _Eε_ ) _∩ MK,ε_ of indices 2 and 1, respectively. 

Let _u ∈MXE_ 0 ( _p_ 0 _, q_ 0) and _uε_ := Ψ _[ε] p_ 0 _,q_ 0[(] _[u]_[)] _[∈M][X] Eε_[(] _[p][ε][, q][ε]_[),][see][Theorem][253.] Our goal is to compute and compare the **orientation signs** sgn( _u_ ) and sgn( _uε_ ) _._ Let _x ∈ u_ . Then _x_ 0 and _xε_ will denote the corresponding points of the slow trajectory _u_ 0 and _uε_ . Here, the correspondence of _x_ 0 and _xε_ is given by Fenichel theory, see Theorem 253. 

By index reasons dim( _WX[s] E_ 0[(] _[q]_[0][))][=][2][and][dim(] _[W] X[ u] E_ 0[(] _[p]_[0][))][=][1.][We][would] like to give an orientation to the manifold _u ⊂ WX[s] E_ 0[(] _[q]_[0][)] _[∩][W][ u] XE_ 0[(] _[p]_[0][)][by][the] convention from Remark 259. For the oriented basis _{eb}_ of _TxWX[u] E_ 0[(] _[p]_[0][)][we][can] find _ea ∈ Tx_ (R _/T_ Z)[2] such that 

**==> picture [38 x 13] intentionally omitted <==**

is an oriented basis of _Tx_ (R _/T_ Z)[2] . But then, by the dimension reason, this is also an oriented basis of _TxWX[s] E_ 0[(] _[q]_[0][).][Hence,] _[e][b]_[induces][an][orientation][of] _[u]_[(as][a] manifold). 

Next, by index reasons dim( _Wf[s]_ - _s_[(][q] _[ε]_[))][=][3][and][dim(] _[W] f[ u]_ - _s_[(][p] _[ε]_[))][=][2.][Let][us] give an orientation to the manifold _uε ⊂ Wf[s]_ - _s_[(][q] _[ε]_[)] _[ ∩][W][ u] f_ - _s_[(][p] _[ε]_[)] _[.]_ 

Now, by (6 _._ 19) and (6 _._ 20), there is an orientation _reversing_ isomorphism identifying the basis 

**==> picture [79 x 13] intentionally omitted <==**

with an oriented basis of _Txε_ (R _/T_ Z _× S_[1] )[2] . Also _{∂θ_ 1 _, ea, eb}_ can be identified by an orientation _preserving_ isomorphism with an oriented basis of _TxεWf[s]_ - _s_[(][q] _[ε]_[).] And _{eb, ∂θ_ 2 _}_ can be identified by an orientation _preserving_ isomorphism with an oriented basis of _TxεWf[u]_ - _s_[(][p] _[ε]_[).][Hence,] _[−][e][b]_[induces][an][orientation][on] _[u][ε]_[as][a] manifold. 

Finally, by _C_[1] estimates from Fenichel theory, at _x_ the orientations of _u_ and _XE_ 0 _|u_ agree iff at _xε_ the orientations of _uε_ and _XEε|uε_ does not agree. Hence, 

**==> picture [255 x 13] intentionally omitted <==**

To the end, we refer the reader for the orientation conventions of trees to [Mes16]. We claim that these orientation conventions can be adapted to our setting and result in the same correspondence as in (6.22). 

122 

## **7. Cord algebras** 

This chapter aim is to introduce Morse models of cord algebras for _TK,ε_ and relate them to the existing cord algebras for the underlying knot _K_ . As a consequence of the multiple times scale dynamics, we will show directly the equivalence of cord algebra for _K_ and _TK,ε_ with Z coefficients. Moreover, we upgrade the cord algebra for _TK,ε_ by loop space coefficients Z[ _λ[±]_[1] _, µ[±]_[1] ] ( _[∼]_ = Z _π_ 1( _TK_ ) _[∼]_ = _H•_ (Ω _∗TK_ )). We recall that in the knot case, the loop space coefficients were important and the corresponding cord algebra contained much more information about the underlying knot, [CELN16]. In the torus case, the cord algebra with loop space coefficients will be greatly influenced by the geometry of _MK,ε_ - the space of outward-pointing chords. In particular, on the torus, we will be able to detect an analogy of a bit mysterious skein relation, which was on the knot, replacing short contractible cords by 1 _− µ_ . 

## **7.1 Topological cord algebra for knots** 

_Assumption_ 261 _._ From now on, _K_ will be an oriented framed knot in R[3] and the framing f _K_ will induce the choice of the longitude L _⊂ TK_ . We will choose the meridian m _⊂ TK_ such that m projects orthogonally onto _∗∈ K_ . 

**Definition 262.** _A_ _**topological cord** is a continuous map c_ : [0 _,_ 1] _→_ R[3] _such that c_ ([0 _,_ 1]) _∩_ L = _∅ and c_ (0) _, c_ (1) _∈ K \∗. Two topological cords are_ _**homotopic** if they are homotopic through topological cords._ 

_Remark_ 263 _._ A linear topological cord is a chord. 

**Definition 264.** _[CELN16] Let A[top] be a free unital noncommutative_ Z _-algebra generated by homotopy classes of topological chords and extra generators λ, µ such that λ and µ have inverses and commute together._ 

_Then the_ _**topological cord algebra of** K_ _**with loop space coefficients** is the quotient ring_ 

_Cord[top]_ ( _K_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) = _A[top] /I[top] ,_ 

_where I[top] is a two-sided ideal of A[top] generated by the skein relation as in Figure 7.1_ 

_Remark_ 265 _. Cord[top]_ ( _K_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) does not depend on the choice of _∗_ and is an invariant under ambient isotopy of _K_ . 

Using so-called string homology it was shown in the paper [CELN16] that _Cord[top]_ ( _K_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) is isomorphic to the 0-th degree Legendrian contact homology _LCH_ 0( _L[∗] K_ ) _._ 

In addition, in the same paper, it was proven that _Cord[top]_ ( _K_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) detects the unknot. 

_Remark_ 266 _._ If we put _λ[±]_[1] = _µ[±]_[1] = 1, then _Cord[top]_ ( _K_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) becomes a **Cord algebra of** _K_ **over** Z, denoted by _Cord[top]_ ( _K_ ; Z) _._ 

Note that _Cord[top]_ ( _K_ ; Z) is independent of the framing. In more detail, the cords, which are homotopic in _π_ 1(R[3] _, K_ ), are identified in the cord algebra. Specially, the cords from [0] _∈ π_ 1(R[3] _, K_ ) vanish in the cord algebra. 

123 

**==> picture [251 x 188] intentionally omitted <==**

**----- Start of picture text -----**<br>
( i. ) = 1  − µ<br>( ii. ) = ·µ and =  µ·<br>( iii. ) = ·λ and =  λ·<br>( iv. ) − = ·<br>**----- End of picture text -----**<br>


Figure 7.1: The skein relations for _I[top]_ . The black curves describe the knot _K_ , grey the longitude L, and in red are the cords. Skein relations describe the following phenomena: ( _i._ ) is for contractible cords, ( _ii._ ) and ( _iii._ ) are for cords crossing the framing (i.e. L) and the base point, respectively. Finally, ( _iv._ ) relates cords as they cross the knot. 

Since _λ_ = 1, by the skein relation ( _iii._ ) from Figure 7.1, the base point becomes redundant too. 

For various versions of _Cord[top]_ ( _K_ ) see also [Ng04, Ng05b, Oka25, Oka24]. 

## **7.2 Morse models for Cord algebras over** Z 

**Definition 267.** _[Pet24, Ng05b, Oka24]Let K be generic and XE_ 0 _be a generic approximation of −∇E_ 0 _._ 

_Let C_ 0 _[M]_[(] _[K]_[;][ Z][)] _[ be a free unital noncommutative]_[ Z] _[-algebra generated by][ Crit]_[0][(] _[E]_[0][)] _[\]_ ∆0 _. Let C_ 1 _[M]_[(] _[K]_[;][ Z][)] _[be][a]_[Z] _[-vector][space][generated][by][Crit]_[1][(] _[E]_[0][)] _[ \]_[ ∆][0] _[.][Let][D][K]_[:] _C_ 1 _[M]_[(] _[K]_[;][ Z][)] _[ →][C]_ 0 _[M]_[(] _[K]_[;][ Z][)] _[be][a][linear][map][which][is][defined][on][generators][as]_ 

**==> picture [337 x 35] intentionally omitted <==**

_Then the_ _**Morse cord algebra of** K_ _**over**_ Z _is the quotient ring_ 

_Cord[M]_ ( _K_ ; Z) = _C_ 0 _[M]_[(] _[K]_[;][ Z][)] _[/][I][K][,]_ 

_where IK is a two-sided ideal of C_ 0 _[M]_[(] _[K]_[;][ Z][)] _[generated][by][the][image][of][the][map] DK._ 

_Remark_ 268 _._ By Lemma 170 it follows that _DK_ ( _p_ 0) is a finite sum. 

**Theorem 269.** _[Pet24] Let K_ 0 _and K_ 1 _be connected by a generic ambient isotopy. Let XE_[0] 0 _[and][X] E_[1] 0 _[be][connected][by][a][generic][smooth][family][of][gradient-like][vector] fields {XE[r]_ 0 _[}][r][∈]_[[0] _[,]_[1]] _[approximating][ {−∇][E]_ 0 _[r][}][r][∈]_[[0] _[,]_[1]] _[.][By “generic” we understand that] only for a finite number of r ∈_ (0 _,_ 1) _the elements Kr and XE[r]_ 0 _[are][not][generic][in] the sense of Definition 267. Then_ 

**==> picture [167 x 15] intentionally omitted <==**

124 

**Definition 270.** _Let ε >_ 0 _be small. Let K be generic and XEε be a K-generic approximation of −∇Eε._ 

_Let C_ 0 _[M]_[(] _[T][K,ε]_[;][ Z][)] _[be][a][free][unital][noncommutative]_[Z] _[-algebra][which][is][gener-] ated by Crit_ 1( _Eε|MK,ε\_ ∆ _ε_ ) _. Let C_ 1 _[M]_[(] _[T][K,ε]_[;][ Z][)] _[be][a]_[Z] _[-vector][space][generated][by] Crit_ 2( _Eε|MK,ε\_ ∆ _ε_ ) _. Let DTK,ε_ : _C_ 1 _[M]_[(] _[T][K,ε]_[;][ Z][)] _[ →][C]_ 0 _[M]_[(] _[T][K,ε]_[;][ Z][)] _[ be][a][linear map][which] is defined on generators as_ 

**==> picture [366 x 35] intentionally omitted <==**

_Then the_ _**Morse cord algebra of** TK,ε_ _**over**_ Z _is the quotient ring_ 

_Cord[M]_ ( _TK,ε_ ; Z) = _C_ 0 _[M]_[(] _[T][K,ε]_[;][ Z][)] _[/][I][T] K,ε[,]_ 

_where ITK,ε is a two-sided ideal of C_ 0 _[M]_[(] _[T][K,ε]_[;][ Z][)] _[generated][by][the][image][of][the][map] DTK,ε._ 

**Theorem 271.** _Let ε >_ 0 _be small and K generic. Let XE_ 0 _and XEε be K-generic approximations of −∇E_ 0 _and −∇Eε, respectively._ 

_Then for i_ = 0 _,_ 1 _the canonical isomorphisms_ Θ _[ε] i_[:] _[C][i]_[(] _[K]_[;][ Z][)] _[→][C][i]_[(] _[T][K,ε]_[;][ Z][)] _satisfy_ Θ _[ε]_ 0 _[◦][D][K]_[=] _[ D][T] K,ε[◦]_[Θ] 1 _[ε][.]_ 

_In particular,_ 

**==> picture [169 x 15] intentionally omitted <==**

_Proof._ By Lemma 99 we obtain the cannonical isomorphisms Θ _[ε]_ 0 _[,]_[ Θ] 1 _[ε]_[.][Then][the] theorem follows from Theorems 253 and 254. See also Remarks 258 and 260 for the sign conventions. 

**Corollary 272.** _Let ε >_ 0 _be small. Let K_ 0 _and K_ 1 _be connected by a generic ambient isotopy. Let XE_[0] _ε[and][X] E_[1] _ε[be][connected][by][a][generic][smooth][family][of] gradient-like vector fields {XE[r] ε[}][r][∈]_[[0] _[,]_[1]] _[K][-approximating][{−∇][E] ε[r][}][r][∈]_[[0] _[,]_[1]] _[.][Then] Cord[M]_ ( _TK_ 0 _,ε_ ; Z) _[∼]_ = _Cord[M]_ ( _TK_ 1 _,ε_ ; Z) _._ 

## **7.3 Morse models for Cord algebras with loop space coefficients** 

## **7.3.1 Knot case** 

_Remark/Notation_ 273 _._ There is a canonical extension of Definition 168 of the trees _♣XE_ 0 ( _T_ ; _p_ 0; _q_ 0[1] _[, . . . , q]_ 0 _[m]_[).][We][would][like][to][allow][the][leaves][be][identified][not] only with the points in _Crit_ 0( _E_ 0) _\_ ∆0, but also with the Bott-critical submanifold ∆0. Let us denote such a space of trees by 

**==> picture [129 x 17] intentionally omitted <==**

By the argument from [CELN16, prop 7.14], one can still bound the number of potential bifurcations of the trees from above. Moreover, ∆0 is the unique global minimum of _E_ 0, and in particular dim( _WX[s] E_ 0[(∆][0][)) = 2.][So, a small adjustment of] the argument from Lemma 170 implies that for a generic approximation _XE_ 0 of _−∇E_ 0 it holds that _♣XE_ 0 ( _T_ ; _p_ 0; _Q_[1] 0 _[, . . . , Q][m]_ 0[) is a 0-dimensional compact manifold.] In addition, the set of all of these trees _♣XE_ 0 is finite. 

125 

_Remark/Notation_ 274 _._ Let us consider ∆0 with the induced metric from the flat metric on (R _/T_ Z)[2] . By 

**==> picture [18 x 12] intentionally omitted <==**

we denote a Morse function on ∆0 such that _−∇h_ ∆0 is Morse-Smale. 

It follows that _HM_ 0( _h_ ∆0; Z) _[∼]_ = Z and all elements of _Crit_ 0( _h_ ∆0) are homologous, see for example [AD13, rem 4.5.4]. 

Thus for simplicity, we shall assume that _Crit_ ( _h_ ∆0) consists of two critical points - _M_ ∆0 _, m_ ∆0 of indices 1 _,_ 0, respectively. 

Moreover, since the set _♣XE_ 0 is finite, we impose a generic condition that ~~_u_~~ _∩ Crit_ ( _h_ ∆0) = _∅_ for every _u ∈♣XE_ 0 . Last, we impose the condition that _∗∩ Crit_ ( _h_ ∆0) = _∅_ . 

This will give us a good choice of _h_ ∆0 for the cord algebra. 

**Definition 275.** _Let p_ 0 _∈ Crit_ 1( _E_ 0) _\_ ∆0 _and q_ 0[1] _[, . . . , q]_ 0 _[m][∈]_[(] _[Crit]_[0][(] _[E]_[0][)] _[ \]_[ ∆][0][)] _[ ∪] {m_ ∆0 _}, by {jℓ}ℓ_ =1 _,...,k we denote those indices from {_ 1 _, . . . , m} such that q_ 0 _[j][ℓ]_[=] _m_ ∆0 _. Let T ∈♣m. Let XE_ 0 _be a gradient-like vector field adapted to E_ 0 _. Then u is a_ _**Cascade Morse flow tree from** p_ 0 _**to** q_ 0[1] _[, . . . , q]_ 0 _[m]_ _**[modeled][on]**[T][if][the] following holds._ 

_u is a concatenation of a tree uc,_ 0 _and partial flow lines {u[j][ℓ] }, where_ 

- _uc,_ 0 _∈♣XE_ 0 ( _T_ ; _p_ 0; _Q_[1] 0 _[, . . . , Q][m]_ 0[)] _[with][Q][i]_ 0[=] _[ q]_ 0 _[i][if][i][ ̸]_[=] _[ j][ℓ][,][else][Q][i]_ 0[= ∆][0] _[.]_ 

- _Let_ ~~_u_~~ _c,_ 0 _∩ Q[j]_ 0 _[ℓ]_[=] _[x][j][ℓ][.][Then][u][j][ℓ][is][given][by][ϕ]_[[0] _−∇[,][∞] h_[)] ∆0[(] _[x][j][ℓ]_[)] _[.][In][particular,][the] omega limit of x[j][ℓ] is m_ ∆0 _._ 

_The convention is that the pairs of concatenated paths are identified with the single edge of T , which will be called_ _**broken** with the_ _**cascade** and the_ _**diagonal** part. So the leaves are identified with q_ 0[1] _[, . . . , q]_ 0 _[m][.]_ 

_The_ _**set of all Cascade Morse flow trees from** p_ 0 _**to** q_ 0[1] _[, . . . , q]_ 0 _[m]_ _**[modeled] on** T is denoted by_ 

_♣[c] XE_ 0[(] _[T]_[ ;] _[ p]_[0][;] _[ q]_ 0[1] _[, . . . , q]_ 0 _[m]_[)] _[.] The set of all such trees is denoted by ♣[c] XE_ 0 _[.]_ 

**Definition 276.** _[Pet24] We say that the chord P_ = _γ_ ( _s_ 2) _− γ_ ( _s_ 1) _**intersects framing at the starting point** , if the orthogonal projection of P to the normal plane at γ_ ( _s_ 1) _is a positive multiple of_ f _K_ ( _s_ 1) _. That is, if it holds_ 

**==> picture [157 x 13] intentionally omitted <==**

_for some α >_ 0 _. The_ _**set of all chords intersecting framing at the starting point** is denoted by F[S] . Analogously, we define the_ _**intersection of the framing at the endpoint** and the set F[E] ._ 

_Remark_ 277 _._ [Pet24] For generic _K_ and generic framing f _K_ the following holds. The closures _F[S] , F[E]_ are embedded one dimensional submanifolds of (R _/T_ Z)[2] with boundary of _s_ 1- and _s_ 2-special points, respectively. Moreover, _F[S]_ and _F[E]_ intersect ∆0 transversely _at the same points_ . 

126 

_Remark_ 278 _._ Definition 276 allows us to restrict the interpretation of the skein relation ( _ii._ ) from Definition 264 to chords that differ by the flow of _XE_ 0. 

The restriction of the skein relation ( _iii._ ) to chords flowing under the flow is clear. 

Recall that _F[S] , F[E]_ are well-defined also on ∆0. So, in fact, we can also interpret the skein relation ( _ii._ ) for the trivial chords flowing under the flow of _−∇h_ ∆0. The interpretation of ( _iii._ ) for the trivial chords is clear. 

Now we can, in the spirit of [Pet24], introduce a certain evaluation function _D_ ˆ︂ _u_ on a tree _u ∈♣[c] XE_ 0[.][Such][a][function][will][just][count][how][many][times][the][tree] _u_ intersects the framing and the base point as we flow from the root to the leaves. 

**Definition 279.** _Let u ∈♣[c] XE_ 0[(] _[T]_[ ;] _[ p]_[0][;] _[ q]_ 0[1] _[, . . . , q]_ 0 _[m]_[)] _[.][Recall also the notation for the] trees from Remark 165. Then the evaluation function D_[ˆ︂] _u is recursively defined on the vertices of T as_ 

**==> picture [384 x 121] intentionally omitted <==**

_where αk, βk are_ Z _-valued functions on the corresponding edges of the tree. The functions are determined by the skein relations_ ( _ii._ ) _,_ ( _iii._ ) _from Definition 264 and Remark 278 as we flow along XE_ 0 _with the chords in_ R[3] _. Here, k_ = 1 _corresponds to the intersections at the starting points and k_ = 2 _at the endpoints._ 

**Definition 280.** _[Pet24]Let K be a generic knot with generic framing_ f _K and base point ∗. Let XE_ 0 _be a generic approximation of −∇E_ 0 _and let h_ ∆0 _be generic. Let C_ 0 _[M]_[(] _[K]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] _[be][a][free][unital][noncommutative]_[Z] _[-algebra][generated] by_ ( _Crit_ 0( _E_ 0) _\_ ∆0) _∪{m_ ∆0 _} and extra generators λ, µ such that λ and µ have inverses and commute together. Let C_ 1 _[M]_[(] _[K]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] _[be][a]_[Z] _[-vector][space][gen-] erated by Crit_ 1( _E_ 0) _\_ ∆0 _. Let DK_ : _C_ 1 _[M]_[(] _[K]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] _[→][C]_ 0 _[M]_[(] _[K]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] _be a linear map which is defined on generators as_ 

**==> picture [288 x 31] intentionally omitted <==**

_Then the_ _**Morse cord algebra of** K_ _**with loop space coefficients** is the quotient ring_ 

**==> picture [259 x 14] intentionally omitted <==**

_where IK is a two-sided ideal of C_ 0 _[M]_[(] _[K]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] _[generated][by][the][image][of] the map DK and m_ ∆0 _−_ 1 + _µ._ 

_Remark_ 281 _._ One can also canonically extend the definition (7.1) of _DK_ to _M_ ∆0. I. e. we would like to consider also the flow lines of _−∇h_ ∆0 from _M_ ∆0 to _m_ ∆0 

127 

and count their intersections with _F[S/E]_ and the base point _∗_ . There are two such flow lines with opposite orientations. In addition, we will obtain 

**==> picture [257 x 17] intentionally omitted <==**

for some _α, β, α,_ ˜︁ _β_[˜︁] _∈_ Z, since the intersections are coming in pairs on ∆0. Moreover, ( _m_ ∆0 _−_ 1 + _µ_ ) _∼_ 0, so _DK_ ( _M_ ∆0) = 0. In particular, the generator _M_ ∆0 is redundant. 

_Remark_ 282 _._ In Definition 280 we used Cascade Morse flow trees. That is slightly different from [Pet24], where Andreas P. just perturbed appropriately the MorseBott function _E_ 0 to the Morse setting. So, the cord algebra _Cord[M]_ ( _K,_ Z[ _λ[±]_[1] _, µ[±]_[1] ]) from [Pet24] was not counting cascade flow trees. 

Both approaches are expected to be equivalent as a consequence of Multipletime scale dynamics. In more detail, one can see _XE_ 0 as the fast flow with ∆0 as the normally hyperbolic critical manifold and _−∇h_ ∆0 as the slow flow. For the correspondence of the fast-slow flow lines and flow lines with cascade, see [BH13]. See also Theorem 254. Our approach with cascades has an advantage that it will be in the same spirit as the _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]). A bit surprisingly, in the torus case, the cascades will be a significant simplification. 

**Theorem 283.** _[Pet24] For a generic_ ( _K,_ f _K, ∗, XE_ 0 _, h_ ∆0) _the sum in (7.1) is finite and the differential DK is well-defined. Moreover, Cord[M]_ ( _K_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) _is the knot invariant under a generic ambient isotopy._ 

## **7.3.2 Torus case** 

_Remark_ 284 _._ Now, in the similar flavor to the knot case, we would like to define _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) as a count of certain Cascade Morse flow trees _♣[c,out] XEε[−][out]_ . Our definition of _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) will be then strongly influenced by the fact that the trees from _♣[c,out] XEε[−][out]_ lie in _MK,ε_ . Namely, we will see that the cuspidal behavior of _MK,ε_ near ∆ _ε_ shifts the expected dimension of the trees by _−_ 1 for each leaf in ∆ _ε_ . 

So, first, we define _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) and then we continue with a _conceptual_ discussion that _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) makes sense and recapture the loop space coefficients in the same way as _Cord[M] K_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) _._ 

_Remark/Notation_ 285 _._ Similarly to Remark 273 we extend cannonically Definition 193 of the trees _♣[out] XEε[−][out]_ ( _T_ ; _pε_ ; _qε_[1] _[, . . . , q] ε[m]_[).][We would like to allow the leaves] to be identified not only with the points in _Crit_ 1( _Eε|MK,ε\_ ∆ _ε_ ), but also with ∆ _ε_ , which is a submanifold of the Bott submanifold ∆ _full ⊂_ (R _/T_ Z _× S_[1] )[2] (recall Definition 42 for ∆ _ε_ and ∆ _full_ ). Let us denote such a space of trees by 

**==> picture [141 x 17] intentionally omitted <==**

_Remark/Notation_ 286 _._ Similarly to Remark 274, let us consider ∆ _ε ⊂ MK,ε_ with the induced metric from the flat metric on (R _/T_ Z _× S_[1] )[2] . Recall that by Remark 87 it holds that ∆ _ε[∼]_ = (R _/T_ Z) _×_ [0 _,_ 1]. By 

**==> picture [18 x 13] intentionally omitted <==**

128 

we denote a Morse function on ∆ _ε_ such that _−∇h_ ∆ _ε_ is Morse-Smale and strictly inward-pointing on _∂_ ∆ _ε_ . 

For simplicity, we shall assume that _h_ ∆ _ε_ has two critical points - _M_ ∆ _ε, m_ ∆ _ε_ of indices 1 _,_ 0, respectively. We will also assume ~~_u_~~ _ε ∩_ (︂ _Crit_ ( _h_ ∆ _ε_ ) _∪ W−∇[s] h_ ∆ _ε_[(] _[M]_[∆] _ε_[)] )︂ = _∅_ for every _uε ∈ ♣[out] XEε[−][out]_ . To the last, we impose a condition on _h_ ∆ _ε_ that m _ε ∩ Crit_ ( _h_ ∆ _ε_ ) = _∅_ , where m _ε_ is the meridian curve in _TK,ε_ . 

**Definition 287.** _Let pε ∈ Crit_ 2( _Eε|MK,ε\_ ∆ _ε_ ) _and qε_[1] _[, . . . , q] ε[m][∈][Crit]_[1][(] _[E][ε][|][M] K,ε[\]_[∆] _ε_[)] _[∪] {m_ ∆ _ε}, by {jℓ}ℓ_ =1 _,...,k we denote those indices from {_ 1 _, . . . , m} such that qε[j][ℓ]_[=] _m_ ∆ _ε. Let T ∈♣m. Let XEε be a gradient-like vector field adapted to Eε. Then uε is a_ _**Cascade Morse flow tree from** pε_ _**to** qε_[1] _[, . . . , q] ε[m]_ _**modeled on** T if the following holds._ 

_uε is a concatenation of a tree uc,ε and partial flow lines {u[j][ℓ] }, where_ 

- _uc,ε ∈♣XEε_ ( _T_ ; _pε_ ; _Q_[1] _ε[, . . . , Q][m] ε_[)] _[with][Q][i] ε_[=] _[ q] ε[i][if][i][ ̸]_[=] _[ j][ℓ][,][else][Q][i] ε_[= ∆] _[ε][.]_ 

- _Let_ ~~_u_~~ _c,ε ∩ Q[j] ε[ℓ]_[=] _[x][j][ℓ][.][Then][u][j][ℓ][is][given][by][ϕ]_[[0] _−∇[,][∞] h_[)] ∆ _ε_[(] _[x][j][ℓ]_[)] _[.][In][particular,][the] omega limit of x[j][ℓ] is m_ ∆ _ε._ 

_The convention is that the pairs of concatenated paths are identified with the single edge of T , which will be called_ _**broken** with the_ _**cascade** and_ _**diagonal** part. So the leaves are identified with qε_[1] _[, . . . , q] ε[m][.]_ 

_The_ _**set of all Cascade Morse flow trees from** pε_ _**to** qε_[1] _[, . . . , q] ε[m]_ _**[modeled] on** T is denoted by_ 

_♣[c,out] XEε[−][out]_ ( _T_ ; _pε_ ; _qε_[1] _[, . . . , q] ε[m]_[)] _[.] The set of all such trees is denoted by ♣[c,out] XEε[−][out] ._ 

Now in analogy to Definition 288, we would like to introduce an evaluation function _D_[ˆ︂] _uε_ on a tree _uε ∈♣[c,out] XEε[−][out]_ . Such a function will just count how many times the realization of _uε_ in _TK,ε ⊂_ R[3] intersects the curves L _ε_ and m _ε_ . 

**Definition 288.** _Let uε ∈♣[c] XEε_[(] _[T]_[ ;] _[ p][ε]_[;] _[ q] ε_[1] _[, . . . , q] ε[m]_[)] _[.][Recall][also][the][notation][for] the trees from Remark 165. Then the evaluation function D_[ˆ︂] _uε is recursively defined on the vertices of T as_ 

**==> picture [388 x 121] intentionally omitted <==**

_where, for k_ = 1 _,_ 2 _, αk, βk are_ Z _-valued functions on the corresponding edges of the tree uε. They are_ ( _−_ 1) _[k]_[+1] _multiples of the algebraic intersection numbers of_ m _ε,_ L _ε with_ Γ _ε_ ( _πsk,θk_ ( _uε|_ e)) _, where uε|_ e _is the restriction of uε to the given edge_ e _of T ._ 

129 

**Definition 289.** _Let ε >_ 0 _be small. Let_ ( _K,_ f _K, ∗, h_ ∆ _ε_ ) _be generic and XEε be a generic approximation of −∇Eε. Let C_ 0 _[M]_[(] _[T][K,ε]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] _[ be a free unital noncommutative]_[ Z] _[-algebra generated] by Crit_ 1( _Eε|MK,ε\_ ∆ _ε_ ) _∪{m_ ∆ _ε} and extra generators λ, µ such that λ and µ have inverses and commute together. Let C_ 1 _[M]_[(] _[T][K,ε]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] _[be][a]_[Z] _[-vector][space] generated by Crit_ 2( _Eε|MK,ε\_ ∆ _ε_ ) _. Let_ 

**==> picture [277 x 16] intentionally omitted <==**

_be a linear map which is defined on generators as_ 

**==> picture [308 x 33] intentionally omitted <==**

_Then the_ _**Morse cord algebra of** TK,ε_ _**with loop space coefficients** is the quotient ring_ 

**==> picture [288 x 16] intentionally omitted <==**

_where ITK,ε is a two-sided ideal of C_ 0 _[M]_[(] _[T][K,ε]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] _[generated][by][the][image] of the linear map DTK,ε and m_ ∆ _ε −_ 1 _._ 

_Remark_ 290 _._ Due to the analogous argument as in Remark 281 we dropped from the definition of _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) the redundant generator _M_ ∆ _ε_ . 

_Example_ 291 _._ For simplicity, we restrict the coefficient group ring to Z2[ _λ[±]_[1] _, µ[±]_[1] ]. 

We would like to characterize _Cord[M]_ ( _TK,ε_ ; Z2[ _λ[±]_[1] _, µ[±]_[1] ]) in the case when _K_ is an unknot _KU_ with two binormal chords of Morse index 1 and two binormal chords of Morse index 2. 

For that, we can choose _KU_ as an ellipse in the _xy_ -plane with (oriented) framing _s ↦→ b_ ( _s_ ). The base point _∗_ is chosen to lie outside of the endpoints of the binormal chords of _K_ . The meridian curve m _ε_ has an orientation given by the _θ_ -coordinate. 

Next, ( _Crit_ 2( _Eε_ ) _∩ MKU ,ε_ ) _\_ ∆ _ε_ consists of two critical point - _pε, p_ ˆ︁ _ε_ . And (( _Crit_ 1( _Eε_ ) _∩ MKU ,ε_ ) _\_ ∆ _ε_ ) _∪{m_ ∆ _ε}_ = _{m_ ∆ _ε}_ . 

Let us pick _pε_ . It follows that _DTKU ,ε_ ( _pε_ ) counts only cascade flow lines from _♣[c,out] XEε[−][out]_ ( _pε, m_ ∆ _ε_ ). Let us discuss the expected dimension of _♣[c,out] XEε[−][out]_ ( _pε, m_ ∆ _ε_ ). We would like to focus on the cascade part of _♣[c,out] XEε[−][out]_ ( _pε, m_ ∆ _ε_ ) first. Note that on (R _/T_ Z _× S_[1] )[2] it holds that 

**==> picture [253 x 19] intentionally omitted <==**

So, dim _WXEε_ ( _pε,_ ∆ _full_ ) = 2, which is by 1 dimension higher, then we wanted! However, we are not counting trajectories in (R _/T_ Z _× S_[1] )[2] but rather in _MKU ,ε_ . 

Now, we would like to recall few facts about _MKU ,ε_ near ∆ _ε_ and the structure of the dynamics on that space. 

By Corollary 88, there is a _O_ ( _ε_ )-close subset ∆ _[cusp] ε ⊂_ ∆ _ε_ with the following property. Near ∆ _[cusp] ε_ , the normal projection _πN_ gives _MKU ,ε_ a structure of locally trivial stratified fiber bundle (=: _M_[ˆ︂] _KU ,ε_ ) over ∆ _[cusp] ε_ , and the typical fiber is a union of two cuspical regions. 

130 

Next, in Conjecture 110, we slightly restricted _M_[ˆ︂] _KU ,ε_ to some _M_[ˆ︂] ˆ︂ _KU ,ε_ , roughly said, by shrinking ∆ _[cusp] ε →_ ∆ _ε,δ_ . Then, by this conjecture, it follows that 

**==> picture [162 x 19] intentionally omitted <==**

We remark that Conjecture 110 is a consequence of the cuspical geometry of _MKU ,ε_ , Sternberg’s Linearization Theorem 108 and the outward-pointing behavior of _XEε_ on _∂M_[ˆ︂] ˆ︂ _KU ,ε_ . For the behavior of _XEε_ on _∂M_[ˆ︂] ˆ︂ _KU ,ε_ we only gave an evidence in Example 104, but we expect that a laborious local computation as in Section 3.4 will verify the claim. 

Hence, for a generic _XEε_ it holds that 

**==> picture [133 x 19] intentionally omitted <==**

Let us put _δ_ := _ε_ , so ∆ _ε,δ_ is _O_ ( _ε_ )-close subset of ∆ _ε_ . So, for _ε >_ 0 small, we expect that 

dim (︂ _♣[out] XEε[−][out]_ ( _pε,_ ∆ _ε_ ))︂ = 0 _,_ 

see also Figure 7.2, where the trajectories were computed numerically with _Mathematica_ (in the case that _K_ is a circle in _xy_ -plane). 

**==> picture [377 x 236] intentionally omitted <==**

**----- Start of picture text -----**<br>
ctriv<br>×<br>cpε<br>**----- End of picture text -----**<br>


Figure 7.2: A visualization of _W−∇[u] Eε_[(] _[p][ε]_[)] _[∩][M][K] U[,ε]_[on] _[T][K] U[,ε]_[.] The red curves depict the endpoints of chords emanating from _cε_ under the negative gradient flow constraint to _MKU ,ε_ . Similarly, the blue curves depict the starting points of chords emanating from _cε_ under the negative gradient flow constraint to _MKU ,ε_ . Note also a single pair of red and blue curves that are connected by a trivial chord _ctriv_ ; they represent a trajectory _uc,ε_ from _pε_ to ∆ _ε_ that stays the whole time in _MKU ,ε_ . 

In Figure 7.2 we saw a single _uc,ε_ which was a cascade part of some trajectory _uε ∈♣[c,out] XEε[−][out]_ ( _pε, m_ ∆ _ε_ ). Or more precisely, we saw a trace of _uc,ε_ in _TKU ,ε_ . That is the curve, which is given by concatenation of 

**==> picture [255 x 16] intentionally omitted <==**

131 

However, then there is also another trajectory _u_ ˜︁ _ε ∈♣[c,out] XEε[−][out]_ ( _pε, m_ ∆ _ε_ ) such that the trace _u_ ˜︁ _[trace] c,ε_ of the cascade part of _u_ ˜︁ _c,ε_ is symmetric to _u[trace] c,ε_ along the _xy_ -plane. See also Figure 7.3. 

**==> picture [295 x 171] intentionally omitted <==**

**----- Start of picture text -----**<br>
u [trace]<br>c,ε<br>u [trace]<br>˜︁ c,ε<br>cpε<br>**----- End of picture text -----**<br>


Figure 7.3: Traces of _uc,ε_ and _u_ ˜︁ _c,ε_ . 

Let us now compute the contributions of paths _uε_ and _u_ ˜︁ _ε_ to the differential _DTKU ,ε_ . Analogously to Remark 290, the diagonal parts of _uε_ and _u_ ˜︁ _ε_ are redundant in the count. So only the intersections of the traces _u[trace] c,ε ,_ ˜︁ _u[trace] c,ε_ with m _ε_ and L _ε_ matter. Let us consider the orientations as in Figure 7.4. 

**==> picture [295 x 172] intentionally omitted <==**

**----- Start of picture text -----**<br>
m ε<br>L ε (Γ ε ) ∗∂s<br>−<br>(Γ ε ) ∗∂θ<br>cpε<br>**----- End of picture text -----**<br>


Figure 7.4: Orientations of curves L _ε,_ m _ε_ and their intersections with traces _u[trace] c,ε_ and _u_ ˜︁ _[trace] c,ε_ . The orientations are induced by the basis _{∂s, −∂θ}._ 

So the algebraic intersection number of m _ε_ with the curves _u[trace] c,ε ,_ ˜︁ _u[trace] c,ε_ is in both cases +1. This will contribute in both cases by _·λ_ . 

More intersecting is the algebraic intersection number of L _ε_ with the curves _u[trace] c,ε ,_ ˜︁ _u[trace] c,ε_ . In the first case, we will get a contribution by _·µ_ and in the second case, there is no intersection, so the contribution is _·_ 1! Compare this with the skein relation ( _i._ ) from Definition 264. 

Since on the other half of the torus there are another two cascade flow lines 

132 

**==> picture [186 x 17] intentionally omitted <==**

**==> picture [198 x 71] intentionally omitted <==**

for some numbers _αi, βi ∈_ Z that come from the diagonal parts of the trajectories. Since in cord algebra it holds that _m_ ∆ _ε_ = 1, we obtain the relation 

**==> picture [99 x 13] intentionally omitted <==**

The same relation will also follow from the cascade flow trajectories from _p_ ˆ︁ _ε_ to _m_ ∆ _ε_ . Hence 

**==> picture [307 x 15] intentionally omitted <==**

Which matches the computation of _Cord[M]_ ( _KU_ ; Z2[ _λ[±]_[1] _, µ[±]_[1] ]) from [Pet24]. 

133 

## **8. Relation to symplectic geometry** 

In this chapter we attempt to show that our definitions of cord algebras for _TK,ε_ did not fall from the sky, but can be expected to arise from a _J_ -holomorphic curve invariant for one component of unit conormal bundle of _TK,ε_ - _L[∗]_ + _[T][K,ε]_[.] This invariant will be 0-th degree Legendrian contact homology _LCH_ 0( _L[∗]_ + _[T][K,ε]_[)] (with Z or Z[ _π_ 1( _L[∗]_ + _[T][K]_[)]][coefficients).] 

There are two approaches how to relate _Cord[M]_ ( _TK,ε_ ) with _LCH_ 0( _L[∗]_ + _[T][K,ε]_[).] Direct and indirect. 

The indirect approach is based on the fact that the identification of _Cord[M]_ ( _K_ ) with _LCH_ 0( _L[∗] K_ ) is known, [CELN16, Pet24]. We recall that this identification uses the so-called 0-th string homology _H_ 0 _[string]_ ( _K_ ). In addition, the identification of _LCH_ 0( _L[∗] K_ ) with _LCH_ 0( _L[∗]_ + _[T][K,ε]_[)][is][dictated][by][the][canonical][Legendrian][iso-] topy and the relation _Cord[M]_ ( _K_ ) to _Cord[M]_ ( _TK,ε_ ) was the aim of the last chapters. So, this chapter will be mainly focused on outlining the direct approach, i.e., the approach that does not involve the theories for the underlying knot. For this we construct propose a model of the 0-th string homology _H_ 0 _[string]_ ( _TK,ε_ ) as an intermediate step between _LCH_ 0( _L[∗]_ + _[T][K,ε]_[)][and] _[Cord][M]_[(] _[T][K,ε]_[).] To obtain a chain-level map from _LCH_ 0( _L[∗]_ + _[T][K,ε]_[)][to][the][string][homology] _[H]_ 0 _[string]_ ( _TK,ε_ ) we introduce a moduli space _MTK,ε_ of _J_ -holomorphic curves with boundaries on the Lagrangian manifold _L[∗]_ + _[T][K,ε][∪]_[R][3][with][an][arboreal][singularity][along] _[T][K,ε]_[.][We] will also analyze the geometric information about _J_ -holomorphic curves which arises from the local behavior near the arboreal singularity _TK,ε_ . 

## **8.1 Symplectic set-up** 

_Assumption_ 292 _._ We shall assume that the reader is familiar with some basic notions of symplectic geometry on the level of Appendices A and B. We will briefly recall some of the definitions and conventions. 

_Remark/Notation_ 293 _._ On the cotangent bundle _T[∗]_ R[3] we consider coordinates ( _q, p_ ). Then the Liouville one form _λ_ = _pdq_ determines the symplectic form _ω_ = _dλ_ . So the Liouville vector field _X_ is given by _X_ = _p∂p_ . Moreover, the Hamiltonian _H_ ( _x_ ) = (1 _/_ 2) _∥x[♯] ∥_[2] _gEuc_[determines the Hamiltonian vector field] _[ X][H]_[=] _p∂q_ . 

The unit cotangent bundle _S[∗]_ R[3] is a contact manifold with a contact form _λ_ 1 which is given by the restriction of _λ_ to _S[∗]_ R[3] . _ξ_ denotes the contact structure _ξ_ = ker _λ_ 1. Also, the restriction of _XH_ to _S[∗]_ R[3] is the Reeb vector field _R_ . 

For a submanifold _Q ⊂_ R[3] , the conormal bundle _L[∗] Q_ is a Lagrangian submanifold of _T[∗]_ R[3] . Then the unit conormal bundle _L[∗] Q_ = _L[∗] Q ∩ S[∗]_ R[3] is a Legendrian submanifold of _S[∗]_ R[3] . 

Especially, if _Q_ = _TK_ , then the Legendrian submanifold _L[∗] TK_ has two connected components: _L[∗]_ + _[T][K]_[and] _[L][∗] −[T][K]_[.][They][are][both][diffeomorphic][to] _[T][K]_[by] translations in (co)normal directions. _L[∗]_ + _[T][K]_[is][determined][by][a][choice][of][the] co-orientation on _TK_ . Our convention will be that we co-orient _TK_ by a normal vector that is pointing _inside_ of _νK_ . 

134 

Finally, _L[∗]_ + _[T][K]_[and] _[ L] −[∗][T][K]_[will be two Lagrangian submanifolds with the bound-] ary _TK_ such that _L[∗] ±[T][K][⊂][L][∗] ±[T][K]_[and] _[L][∗]_ + _[T][K][∪][T] K[L] −[∗][T][K]_[=] _[ L][∗][T][K][.]_ To any Reeb chord _**a**_ on _L[∗]_ + _[T][K]_[we][can][assign][its][degree] _[|]_ _**[a]**[|]_[as][in][Definition] 421. _|_ _**a** |_ is equal to a well-defined Maslov index of a certain loop of Lagrangian subspaces minus 1. Roughly speaking, such a loop is constructed by a concatenation of _T L[∗]_ + _[T][K]_[along][a][capping][path][from][the][endpoint][of] _**[a]**_[to][the][starting] point of _**a** ,_ translation of _T L[∗]_ + _[T][K]_[along] _**[a]**_[with][the][linearized][Reeb][flow][and][that] all is closed by a positive rotation at the endpoint of _**a**_ . The trivialization of the corresponding symplectic bundle is taken over a capping disc. 

_Remark_ 294 _._ There is a canonical symplectomorphism 

**==> picture [211 x 32] intentionally omitted <==**

For the Liouville vector field _∂s_ on the symplectization, it holds that _φ∗∂s_ = _X_ , hence _φ_ is a Liouville diffeomorphism. 

Moreover, _φ_ induces R-invariant extensions of _λ_ 1 _, R, ξ_ on _T[∗] N \ N_ that will be denoted by the same letters. More precisely, 

**==> picture [273 x 15] intentionally omitted <==**

Also, the 2-form form _dλ_ 1 is symplectic on _ξ_ and will be denoted by _ω_ 1. Next, _φ[∗] H_ = (1 _/_ 2) _e_[2] _[s]_ , hence ( _φ[−]_[1] ) _∗XH_ = _e[s] R_ . And moreover, _φ_ is a canonical diffeomorphism between Lagrangian submanifolds R _× L[∗] Q_ and _L[∗] Q \ Q_ . 

_Remark_ 295 _._ We would like to deduce Formula (B.3), i.e. _dϕ[t] H_[(] _[x]_[)] _[X][x]_[=] _[ X][y]_[+] _[tR][y]_[,] where _y_ = _ϕ[t] XH_[(] _[x]_[).] 

Since _φ_ is a Liouville diffeomorphism, we can make the computation in the symplectization R _× S[∗]_ R[3] . 

Recall the notation _x_ = ( _q, p_ ). By Remark 294, in R _× S[∗]_ R[3] we have that 

**==> picture [129 x 14] intentionally omitted <==**

Let _x ∈ S[∗]_ R[3] , then we define a curve 

**==> picture [120 x 32] intentionally omitted <==**

Hence _γ_ is an integral curve of _X_ = _∂s_ . Now we put _u_ ( _s_ ) := _ϕ[t] H_[(] _[γ]_[(] _[s]_[))][=] ( _s, ϕ[e] R[r][t]_[(] _[x]_[))] _[.]_[Then] 

**==> picture [321 x 27] intentionally omitted <==**

where ( _y,_ 0) = _ϕ[t] H_[(] _[x,]_[ 0).][The][same][computation][works][for][any][smooth][manifold] _N_ instead of R[3] . 

**Lemma 296.** _L[∗] K and L[∗]_ + _[T][K,ε][are][canonically][Legendrian][isotopic.]_ 

_Proof._ By Remark 295 we have that _ϕ[t] R_[(] _[q, p]_[) = (] _[q]_[ +] _[tp, p]_[), hence by the construc-] tion _ϕ[ε] R_[(] _[L][∗][K]_[)][=] _[L][∗]_ + _[T][K,ε]_[.][Next,] _[{][ϕ][t] R[}][t][∈]_[[0] _[,ε]_[]][is][an][ambient][contact][isotopy][and,][in] particular, also the desired Legendrian isotopy. 

135 

_Assumption_ 297 _._ From now on, we assume that _K_ , and hence also _TK,ε_ , are real analytic. Note that real analyticity can be achieved from a smooth manifold by a _C_[1] -perturbation, see [CE12, 5.8]. Moreover, recall that for _ε >_ 0 small and _K_ generic, the function _Eε_ is Morse-Bott by Lemmata 96 and 99. Thus, by Theorem 458 we will assume that all Reeb chords on _L[∗]_ + _[T][K,ε][⊂][S][∗]_[R][3][are][nondegenerate.] 

**Definition 298** ([CELN16]) **.** _An ω-compatible almost complex structure J on T[∗]_ R[3] _is called_ _**admissible** if_ 

- ( _i._ ) _On T[∗]_ R[3] _\ D[∗]_ R[3] _[∼]_ = R+ _× S[∗]_ R[3] _it holds that J|ξ is compatible with ω_ 1 _|ξ, invariant under translations in the Liouville direction, J_ ( _X_ ) = _R and J_ ( _R_ ) = _−X._ 

- ( _ii._ ) _On T[∗]_ R[3] _\ TK it holds that J|ξ is compatible with ω_ 1 _|ξ and preserves ⟨X, R⟩. Along the zero section_ 0R3 _the almost complex structure J agrees with the standard almost complex structure Jst defined by Jst_ ( _∂qi_ ) := _−∂pi._ 

- ( _iii._ ) _J is integrable near TK such that_ R[3] _and TK are real analytic._ 

- ( _iv._ ) _If s >_ 1 _and γR is a Reeb chord in_ ( _{s} × S[∗]_ R[3] _, λ_ 1) _with endpoints on {s} × L[∗]_ + _[T][K][,][then][φ][∗][J][is][“adapted”][to][γ][R][and][{][s][} × L][∗]_ + _[T][K][.] Roughly speaking, near γR there is a Pfaff-Darboux chart such that in the Lagrangian projection φ[∗] J is integrable and the sheets of L[∗]_ + _[T][K][are][real] analytic. For details, see [CELN16]._ 

- ( _v._ ) _There is an exhaustion_ R[3] =[⋃︁] _k∈_ N _[V] k[by][compact][domains][V] k[with][smooth] boundaries such that pullbacks π[−]_[1] ( _∂Vk_ ) _to T[∗]_ R[3] _are J-convex hypersurfaces, for the definition of J-convex hypersurfaces see_ [CE12] _._ 

_Moreover, a d_ ( _e[s] λ_ 1) _-compatible almost complex structure J_ 1 _on_ R _×S[∗]_ R[3] _is called_ _**admissible** if J_ 1 _satisfies conditions_ ( _i._ ) _and_ ( _iv._ ) _on the whole symplectization._ 

_Remark_ 299 _._ By [EGH00, pg 38] a contact manifold ( _M, α_ ) admits an exhaustion _M_ =[⋃︁] _k∈_ N _[V] k_[by][compact][domains] _[V] k_[with][smooth][pseudo-convex][boundaries,][if] for each _k_ any trajectory of the Reeb vector field _R|Vk_ does not have an internal tangency with _∂Vk_ . This is satisfied by ( _S[∗]_ R[3] _, λ_ 1). Indeed, by Example 432 ( _S[∗]_ R[3] _, λ_ 1) is contactomorphic to ( _T[∗] S_[2] _×_ R _, dt × λS∗S_ 2), hence _Vk_ := _Dk[∗][S]_[ 2] _[×]_ [ _−k, k_ ] will be the desired exhaustion, here _Dk[∗][S]_[ 2][=] _[ {][x][ ∈][T][ ∗][S]_[ 2] _[ | ||][x][♯][|| ≤][k][}][.] Example_ 300 _._ Let _ρ_ : [0 _, ∞_ ) _→_ [1 _, ∞_ ) be a smooth function such that _ρ_ ( _r_ ) = 1 for _r <_ 1 _/_ 3 and _ρ_ ( _r_ ) = _r_ for _r >_ 2 _/_ 3. Let us take _gEuc_ on R[3] together with the induced global coordinates ( _q, p_ ) on ( _T[∗]_ R[3] _, ω_ ) and define an almost complex structure _Jρ_ on _T[∗]_ R[3] by 

**==> picture [253 x 15] intentionally omitted <==**

Then _Jρ_ is _ω_ -compatible and satisfies conditions ( _i._ )-( _iii._ ) _,_ ( _v._ ) from Definition 298. After a suitable deformation near infinity through compatible almost complex structures, we will obtain _Jρ_ that satisfies also ( _iv._ ). 

136 

The following lemma is an analog to [CELN16, Lemma 8.6], where suitable charts around _K_ were constructed. 

**Lemma 301.** _Let J be an almost complex structure on T[∗]_ R[3] _with totally real submanifolds_ R[3] _and TK. Moreover, let J be integrable near TK such that_ R[3] _and TK are real analytic._ 

_Let δ >_ 0 _be small, then we put N_ := _S_[1] _× S_[1] _×_ ( _−δ, δ_ ) _. Then there exists a holomorphic embedding from some neighborhood Op_ (︂ _N, N_[C][)︂] _to_ ( _T[∗]_ R[3] _, J_ ) _such that_ 

**==> picture [220 x 13] intentionally omitted <==**

**==> picture [283 x 14] intentionally omitted <==**

( _iii._ ) _S_[1] _× S_[1] _× {_ 0 _} ×_ ( _i_ R _≥_ 0 _∩_ ( _−δ_ 1 _, δ_ 1)[2] ) _is mapped to L[∗]_ + _[T][K][,]_ 

_where δ_ 1 _>_ 0 _is small._ 

_In particular, this gives us local holomorphic coordinates_ C[2] _×_ C _around any point x ∈ TK, we call them the_ _**standard coordinates around** x._ 

_Proof._ Let us take a real analytic embedding Γ :[˜︁] _S_[1] _× S_[1] _↪→_ R[3] which determines _TK_ . Next, _w_ 1 and _w_ 2 will be real analytic unit vector fields tangent to _TK_ that are induced by the components of _S_[1] _× S_[1] . Then the unit real analytic vector field _n_ := _w_ 1 _× w_ 2 is perpendicular to _TK_ (with respect to _gEuc_ ). We can assume that _w_ 1 _, w_ 2 were chosen such that _{n, w_ 1 _, w_ 2 _}_ is a positively oriented basis frame on _T_ R[3] and _n_ is pointing inside of _νK_ . 

If ( _s, θ, ρ_ ) are coordinates on _N_ := _S_[1] _× S_[1] _×_ ( _−δ, δ_ ), then 

**==> picture [143 x 34] intentionally omitted <==**

is a real analytic embedding for _δ >_ 0 sufficiently small. Now, by Bruhat-Whitney Theorem, [CE12], _N_[C] is a well-defined complex manifold such that _N_ is a real analytic totally real submanifold of _N_[C] . Let _σ_ be the conjugation on ( _T[∗]_ R[3] _, −J_ ). Then by [CE12, Lemma 5.40] the composition _σ ◦ ϕ_[C] gives the desired ( _J, i_ )- holomorphic embedding from some small neighborhood _Op_ (︂ _N, N_[C][)︂] to ( _T[∗]_ R[3] _, J_ ). 

137 

## **8.2 Moduli spaces** 

**Definition 302.** _Let m ∈_ N0 _, J_ 1 _be an admissible almost complex structure on_ (R _× S[∗] , d_ ( _e[s] λ_ 1)) _and Dm_ +1 _be an unit_ ( _m_ + 1) _-punctured disc with some fixed choice of counterclockwisely placed boundary punctures p_ 0 _, . . . , pm_ +1 _. Then let_ _**a** ,_ _**b**_ 1 _, . . . ,_ _**b** m be Reeb chords on L[∗]_ + _[T][K][that are parametrized by times][ T]_[0] _[, T]_[1] _[, . . . , T][m][,] respectively. We define a moduli space_ 

_M[sy] TK_[(] _**[a]**[,]_ _**[ b]**_[1] _[, . . . ,]_ _**[ b]**[m]_[) :=] _[ {][u]_[ = (] _[a, f]_[)] _[ ∈][C]_[0][(] _[D][m]_[+1] _[,]_[ R] _[ ×][ S][∗]_[R][3][)] _[ |]_[ (] _[i.]_[)] _[ −]_[(] _[v.]_[)] _[}][/][ ∼][,]_ 

_where ∼ is a conformal reparametrization of the domain and_ 

- ( _i._ ) _On the interior the map u is_ ( _J_ 1 _, jκ_ ) _-holomorphic, i.e._ 

**==> picture [110 x 12] intentionally omitted <==**

_where κ is some conformal structure on Dm_ +1 _._ 

**==> picture [165 x 14] intentionally omitted <==**

- ( _iii._ ) _For a half-strip neighborhood of p_ 0 _there is a constant a_ 0 _such that_ 

**==> picture [214 x 13] intentionally omitted <==**

_uniformly in t as τ →∞. We say that p_ 0 _is a_ _**positive puncture asymptotic to a** ._ 

- ( _iv._ ) _If k ∈{_ 1 _, . . . , m}, then for a half-strip neighborhood of pk there is a constant ak such that_ 

**==> picture [228 x 13] intentionally omitted <==**

_uniformly in t as τ →∞. We say that pk is a_ _**negative puncture asymptotic to b** k._ 

- ( _v._ ) _u has a finite Hofer energy, see [BEH_[+] _03]._ 

**Theorem 303.** _[EES05a, CELN16, Kar19] For a generic admissible almost complex structure J_ 1 _the moduli space M[sy] TK_[(] _**[a]**[,]_ _**[ b]**_[1] _[, . . . ,]_ _**[ b]**[m]_[)] _[ is a manifold of the dimen-] sion_ 

**==> picture [205 x 30] intentionally omitted <==**

_If L[∗] TK is spin, there is a choice of coherent orientations for M[sy] TK_[(] _**[a]**[,]_ _**[ b]**_[1] _[, . . . ,]_ _**[ b]**[m]_[)] _[.]_ 

_Remark_ 304 _._ Since the almost complex structure _J_ 1 is invariant under R-translations, the quotient _M[sy] TK_[(] **[a]** _[,]_ **[ b]**[1] _[, . . . ,]_ **[ b]** _[m]_[)] _[/]_[R][becomes][an][oriented][manifold][of][dimension] _|_ _**a** | −_[∑︁] _[m] k_ =1 _[|]_ _**[b]**[k][| −]_[1.] 

**Definition 305.** _Let m ∈_ N0 _, J be an admissible almost complex structure on_ ( _T[∗]_ R[3] _, ω_ ) _and Dm_ +1 _be a unit_ ( _m_ + 1) _-punctured disc with some fixed choice of counterclockwisely placed boundary punctures p_ 0 _, . . . , pm_ +1 _. Then let_ _**a** be a Reeb chord on L[∗]_ + _[T][K][and]_ _**[n]**_[:=][(] _[n]_[1] _[, . . . , n][m]_[)] _[an][m][-tuple][of][positive][half-integers.][We] define a moduli space_ 

**==> picture [271 x 15] intentionally omitted <==**

_where ∼ is a conformal reparametrization of the domain and_ 

138 

- ( _i._ ) _u is_ ( _J, jκ_ ) _-holomorphic on interior, where κ is some conformal structure on Dm_ +1 _._ 

- ( _ii._ ) _Im_ ( _u|∂Dm_ +1) _⊂_ R[3] _∪ L[∗]_ + _[T][K][.]_ 

- ( _iii._ ) _p_ 0 _is a positive puncture asymptotic to_ _**a** . Here we used the fact that T[∗]_ R[3] _\ D[∗]_ R[3] _[∼]_ = R+ _× S[∗]_ R[3] _._ 

- ( _iv._ ) _If k ∈{_ 1 _, . . . , m}, then there is a point xk ∈ TK on a half-strip neighborhood of pk such that,_ 

**==> picture [62 x 13] intentionally omitted <==**

_uniformly in t as τ →∞. We say that pk is a_ _**switch at** xk between two (possibly the same) irreducible components of_ R[3] _∪ L[∗]_ + _[T][K][.]_ 

- ( _v._ ) _Let us take a standard holomorphic coordinates around xk. Let us identify the quadrant Q_ := _{z ∈_ (C _, i_ ) _| Im_ ( _z_ ) _≥_ 0 _, Re_ ( _z_ ) _≥_ 0 _,_ 0 _< |z| ≤_ 1 _} with a neighborhood of the puncture pk in Dm_ +1 _. Then u can be locally written in these coordinates as u_ ( _z_ ) = ( _u_ 1( _z_ ) _, u_ 2( _z_ )) _∈_ C[2] _×_ C _, where_ 

**==> picture [310 x 29] intentionally omitted <==**

_Here all br_ ;1 _belong to_ R[2] _, br_ ;2 _are all in_ R _or all in i_ R _and b_ 0;2 = 0 _. Finally, nk ∈_ 2[1][N][+] _[and][is][called][the]_ _**[winding][number][at]**[p][k][.][If][n][k][∈][/]_[N][+] _[,][we][say] that u_ _**switches sheets at** pk (via the orientation of ∂Dm_ +1 _). u_ 1 _will be called the_ _**tangent component of** u and u_ 2 _the_ _**normal component of** u._ 

( _vi._ ) _u has a finite Hofer energy._ 

**Theorem 306.** _[CELN16, CEL09] For a generic admissible almost complex structure J the moduli space MTK_ ( _**a** ,_ _**n**_ ) _is a manifold of the dimension_ 

**==> picture [184 x 30] intentionally omitted <==**

_After a choice of the spin structure on L[∗]_ + _[T][K][together][with][the][spin][structure][on]_ R[3] _, MTK_ ( _**a** ,_ _**n**_ ) _becomes naturally oriented._ 

_Proof._ Even though the _J_ -holomorphic curves from _MTK_ ( _**a** ,_ _**n**_ ) are now asymptotic rather to the arboreal singularity of R[3] _∪L[∗]_ + _[T][K]_[then to the clean Lagrangian] intersection of R[3] _∪ L[∗] TK_ , the arguments work in the same manner as in the case of clean intersections. 

_Remark_ 307 _._ Recall that by Remark 457 the cotangent lift gives us a bijective correspondence between unit speed binormal chords on the torus _T_ and Reeb chords on _L[∗] T_ . This restricts to a bijection between strictly inward-pointing chords on _T_ and Reeb chords on _L[∗]_[(once][we][co-orient] _[T]_[by][some][tubular] + _[T]_ neighborhood of a knot, see Chapter 2). 

Let _**a**_ be a (nondegenerate) Reeb chord on _L[∗]_ + _[T]_[and] _[ γ][M]_[be the corresponding] (nondegenerate) binormal chord on _T_ . Then by Theorem 458 it holds that 

**==> picture [87 x 13] intentionally omitted <==**

139 

Since _IndγM ∈{_ 0 _,_ 1 _,_ 2 _,_ 3 _,_ 4 _}_ , it follows that _|_ _**a** | ∈{−_ 1 _,_ 0 _,_ 1 _,_ 2 _,_ 3 _}_ . 

Let us assume that moreover _T_ = _TK_ for some _K_ . Then _IndγM ∈{_ 1 _,_ 2 _,_ 3 _}_ . Indeed _γM_ is strictly inward-pointing, so _γM[op]_[is][strictly][outward-pointing.][And] since Morse index does not care about the orientation of _γM_ , one can also apply Lemma 99 for the Morse index computations. Finally, we obtain that _|_ _**a** | ∈ {_ 0 _,_ 1 _,_ 2 _}_ . 

_Remark_ 308 _._ In the knot case the moduli space _MK_ ( _**a** ,_ _**n**_ ) was also introduced, see [CELN16]. Such a space counts punctured _J_ -holomorphic discs with boundary on the clean Lagrangian intersection _L[∗] K ∪_ R[3] . _MK_ ( _**a** ,_ _**n**_ ) is also a manifold, but now of the dimension 

**==> picture [186 x 30] intentionally omitted <==**

Moreover, if _**a**_ is a Reeb chord on _L[∗] K_ and _γM_ is the corresponding binormal chord on _K_ , then by Theorem 458 it holds that 

**==> picture [67 x 13] intentionally omitted <==**

where _IndγM ∈{_ 0 _,_ 1 _,_ 2 _}_ . 

**Corollary 309.** _Let_ _**a**_ 0 _and_ _**a** ε be the corresponding Reeb chords on L[∗] K and L[∗] TK,ε, respectively (they are identified via the canonical contact isotopy). Moreover, assume that their degrees are_ 1 _, then_ 

**==> picture [265 x 15] intentionally omitted <==**

_Remark_ 310 _._ For the dimension reasons, the moduli spaces _MK_ ( _**a**_ 0 _,_[1] 2 _[,]_[1] 2[)][were] used in [CELN16] as suitable “building blocks” in the identification of Legendrian contact homology _LCH_ 0( _L[∗] K_ ) with so-called string homology _H_ 0 _[string]_ ( _K_ ). In our case, dim _MTK,ε_ ( _**a** ε,_[1] 2 _[,]_[1] 2[)][is][1-dimensional][and][not][compact.][In][the] following section, we are going to compactify the moduli space and interpret _MTK,ε_ ( _**a** ε,_ 2[1] _[,]_[1] 2[)][geometrically.] 

## **8.3 Geometry of switches** 

_Remark_ 311 _._ Let us work a bit on the interplay of the conditions ( _iv._ ) and ( _v._ ) from Definition 305 of _MTK_ ( _**a** ,_ _**n**_ ). 

- Let us assume that _pk_ is switch at _xk_ from _L[∗]_ + _[T][K]_[to][ R][3][ with winding number] _nk_ . 

Let us consider the local coordinates of _u_ = ( _u_ 1 _, u_ 2) : _Q →_ C[2] _×_ C. We would like to inspect the normal component _u_ 2. Recall that by Lemma 301 at codom( _u_ 2) it holds that _L[∗]_ + _[T][K]_[is][viewed][as] _[i]_[R] _[≥]_[0][and][R][3][as][R][.] 

Then, after Schwarz Reflexion principle, _u_ 2 will become holomorphic also on _Q ∩_ (R _∪ i_ R). After inspecting _u_ 2 on real and imaginary numbers, it follows that 

**==> picture [170 x 13] intentionally omitted <==**

Moreover, after sending _z →_ 0 we see that _b_ 0;2 _∈_ ( _−_ 1) _[m][k]_ R _>_ 0. Specially, 

**==> picture [270 x 37] intentionally omitted <==**

140 

- Let us assume that _pk_ is a switch at _xk_ from R[3] to _L[∗]_ + _[T][K]_[with][winding] number _nk_ . 

After analysis similar as above, we obtain that 

**==> picture [136 x 12] intentionally omitted <==**

Also, after sending _z →_ 0 we get that _b_ 0;2 _∈ i_ R _>_ 0. Trivially, 

**==> picture [272 x 37] intentionally omitted <==**

- Let us assume that _pk_ is a switch at _xk_ from _L[∗]_ + _[T][K]_[back][to] _[L][∗]_ + _[T][K]_[with] winding number _nk_ . 

   - Again, after inspecting _u_ 2 on real and imaginary numbers, we obtain that 

**==> picture [140 x 12] intentionally omitted <==**

However, after sending _z →_ 0, it turns out that already _nk_ has to be even. In addition, _b_ 0;2 _∈ i_ R _>_ 0. Trivially, 

**==> picture [261 x 13] intentionally omitted <==**

_Notation_ 312 _._ Let _u ∈MTK_ ( **a** _,_ **n** ). Then for _i ∈{_ 1 _, . . . , m −_ 1 _}_ we denote by _c[u] pi,pi_ +1[:][[] _[a][i][, a][i]_[+1][]] _[→][T][ ∗]_[R][3][a][smooth][path][induced][by] _[u]_[along][the][boundary][arc] between the punctures _pi_ and _pi_ +1. The parametrization of _c[u] pi,pi_ +1[is][chosen][such] that it matches with 3-jets of _u_ at local coordinates 8.1 near punctures _pi, pi_ +1. 

**Theorem 313.** _Let_ _**a** be a Reeb chord on L[∗]_ + _[T][K][with][|]_ _**[a]**[|]_[=][0] _[and][J][be][generic.] Then the moduli space MTK_ ( _**a** ,_[1] 2 _[,]_[1] 2[)] _[admits][a][natural][compactification][to][a][com-] pact oriented_ 1 _-dimensional manifold MTK_ ( _**a** ,_[1] 2 _[,]_[1] 2[)] _[ with boundary.][The boundary] consists of_ 

- ( _i._ ) _moduli spaces MTK_ ( _**a** ,_[3] 2 _[,]_[1] 2[)] _[and][M][T][K]_[(] _**[a]**[,]_[1] 2 _[,]_[3] 2[)] _[,][where][one][of]_[1] 2 _[switches][was] replaced by a_[3] 2 _[switch.]_ 

- ( _ii._ ) _moduli spaces MTK_ ( _**a** ,_ 2 _,_[1] 2 _[,]_[1] 2[)] _[and][M][T][K]_[(] _**[a]**[,]_[1] 2 _[,]_[1] 2 _[,]_[ 2)] _[,][where][a]_[2] _[switch][ap-] peared on one of the boundary components that are mapped to L[∗]_ + _[T][K][.]_ 

- _In addition, the J-holomorphic curves of MTK_ ( _**a** ,_[1] 2 _[,]_[1] 2[)] _[have][the][following][ge-]_ 

- _ometry along_ R[3] 

- _If u ∈MTK_ ( _**a** ,_[1] 2 _[,]_[1] 2[)] _[,][then][c][u] p_ 1 _,p_ 2 _[is][strictly][outward-pointing][from][T][K][at][the] endpoints._ 

- _If u ∈MTK_ ( _**a** ,_[3] 2 _[,]_[1] 2[)] _[,][then][c][u] p_ 1 _,p_ 2 _[is][strictly][outward-pointing][from][T][K][at][a]_[2] _and tangent to TK at a_ 1 _. Moreover, near a_ 1 _c[u] p_ 1 _,p_ 2 _[cubically][deviates][into] νTK._ 

- _If u ∈MTK_ ( _**a** ,_[1] 2 _[,]_[3] 2[)] _[,][then][c][u] p_ 1 _,p_ 2 _[is][strictly][outward-pointing][from][T][K][at] a_ 1 _and tangent to TK at a_ 2 _. Moreover, near a_ 2 _the opposite path −c[u] p_ 1 _,p_ 2 _cubically deviates from νTK._ 

141 

_Proof._ The points ( _i._ ) _,_ ( _ii._ ) follow from SFT compactness as in [CEL09] and gluing analysis similar to [CELN16, EES05a]. For the explicit descriptions of possible local degenerations, see Remarks 314, 315, and 316. In these remarks, we will also show the bullet points of Theorem 313. 

_Remark_ 314 _._ We stress out that the boundary _∂MTK_ ( _**a** ,_[1] 2 _[,]_[1] 2[)][from][Theorem][313] does not contain _MTK_ ( _**a** ,_ 1). Even though the virtual dimension of _MTK_ ( _**a** ,_ 1) is 0, such a space is not a good candidate, since it is an empty space. This is due to our restriction of the conormal bundle _L[∗] TK_ to _L[∗]_ + _[T][K]_[,][see][Figure][8.1.][Compare] with [CELN16], where such degenerations were possible and corresponded to the so-called _δN_ -string operation. 

**==> picture [91 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
L [∗]<br>+ [T][K]<br>TK R [3]<br>L [∗] − [T][K]<br>**----- End of picture text -----**<br>


Figure 8.1: A local visualization of the normal component of a potential element _u ∈MTK_ ( _**a**_ ; 1) around the puncture _p_ 1 with the winding number 1. But we do not allow _u_ to have a boundary on _L[∗] −[T][K]_[.][So] _[u]_[can][not][exist.] 

_Remark_ 315 _._ We are going to geometrically enlight the boundary phenomenon _MTK_ ( _**a** ,_ 2 _,_[1] 2 _[,]_[1] 2[)] _[ ⊂][∂] MTK_ ( _**a** ,_[1] 2 _[,]_[1] 2[).][Analogous will hold for] _[ M][T][K]_[(] _**[a]**[,]_[1] 2 _[,]_[1] 2 _[,]_[ 2).][There] is a mark point _p ∈ ∂D_ 3 with cyclic order [ _p_ 0 _, p, p_ 1] and an 1-parametric family of curves _u_ ˜︁ _k ∈MTK_ ( _**a** ,_[1] 2 _[,]_[1] 2[)][with][the][following][property.] With increasing _k_ the points _u_ ˜︁ _k_ ( _p_ ) approach _TK_ along _L[∗]_ + _[T][K]_[.][By][Remark][311,][the][resulted][curve] _u ∈MTK_ ( _**a** ,_ 2 _,_[1] 2 _[,]_[1] 2[)][has][the][normal][component] _[u]_[2][near] _[p]_[of] _[O]_[(] _[z]_[4][).][So][the][family] _u_ ˜︁ _k_ intersects _TK_ “tangentially”. See also Figure 8.2. _L[∗]_ + _[T][K] × TK_ R[3] Figure 8.2: _On the left: u_ ˜︁ _k ∈MTK_ ( _**a**_ ;[1] 2 _[,]_[1] 2[)][around][the][mark][point] _[p]_[.] _[On][the] right: u ∈MTK_ ( _**a**_ ; 2 _,_[1] 2 _[,]_[1] 2[)][around][the][puncture] _[p]_[1][of][the][winding][number][2.] 

_Remark_ 316 _._ Now, we are going inspect locally the degenerations of _MTK_ ( _**a** ,_[1] 2 _[,]_[1] 2[)] as a[1][changes][to][a][3] 2[switch] 2[switch.] 

For each switch we write locally _u ∈ MTK_ ( _**a** ,_[1] 2 _[,]_[1] 2[)][in][the][local][coordinates] 

> _u_ = ( _u_ 1 _, u_ 2) : _Q →_ C[2] _×_ C. Again, we will be interested in the normal components - _u_ 2, for which we use Remark 311. 

> If _n_ 1 =[1] 2[, then near] _[ p]_[1][we can write that] _[ u]_[2][=] _[ b]_[0;2] _[z]_[ +] _[O]_[(] _[z]_[3][)] _[,]_[ where] _[ b]_[0;2] _[∈]_[R] _[>]_[0][.] In particular, _p_ 1 switches sheets from _L[∗]_ + _[T][K]_[to][R][3][.][By][the][order][of][the][leading] 

142 

term of _u_ 2, it follows that _c[u] p_ 1 _,p_ 2[is][not][tangent][to] _[T][K]_[at] _[c][u] p_ 1 _,p_ 2[(] _[a]_[1][).][Next,][recall] that we have chosen the co-orientation of _TK_ by the normal vector pointing inside of _νK_ . Hence, since _b_ 0;2 _∈_ R _>_ 0, _c[u] p_ 1 _,p_ 2[is][strictly][outward-pointing][from] _[T][K]_[at] _c[u]_[see][Figure][8.3.] _p_ 1 _,p_ 2[(] _[a]_[1][),] If _n_ 2 =[1] 2[, then near] _[ p]_[2][ we can write that] _[ u]_[2][=] _[ b]_[0;2] _[z]_[+] _[O]_[(] _[z]_[3][)] _[,]_[ where] _[ b]_[0;2] _[∈][i]_[R] _[>]_[0][.] By the same argument it follows that _p_ 2 switches sheets from R[3] to _L[∗]_ + _[T][K]_[and] _c[u] p_ 1 _,p_ 2[is][strictly][outward-pointing][from] _[T][K]_[at] _[c][u] p_ 1 _,p_ 2[(] _[a]_[2][),][see][Figure][8.3.] 

**==> picture [257 x 85] intentionally omitted <==**

**----- Start of picture text -----**<br>
L [∗]<br>+ [T][K]<br>TK R [3]<br>**----- End of picture text -----**<br>


Figure 8.3: _On the left:_ A local visualization of the normal component of _u ∈ MTK_ ( _**a**_ ; 2[1] _[,]_[1] 2[)][around][the][puncture] _[p]_[1][of][the][winding][number][1] 2[.][The][blue][arrows] depict the boundary orientation of _u_ , and the orange arrow represents the positive co-orientation of _TK_ . _On the right: u ∈MTK_ ( _**a**_ ;[1] 2 _[,]_[1] 2[)][around][the][puncture] _[p]_[2][of] the winding number[1] 2[.] 

Now, the winding numbers of the value[3] 2[.][In][these][cases] _[u]_[2][=] _[ O]_[(] _[z]_[3][),][so] _[c][u] p_ 1 _,p_ 2 is tangent to _TK_ at given endpoints. More precisely, if _n_ 1 =[3] 2[,][then][near] _[p]_[1][we] can write that _u_ 2 = _b_ 0;2 _z_[3] + _O_ ( _z_[5] ) _,_ where _b_ 0;2 _∈_ R _<_ 0, And if _n_ 2 = 2[3][,][then][near] _p_ 2 we can write that _u_ 2 = _b_ 0;2 _z_[3] + _O_ ( _z_[5] ) _,_ where _b_ 0;2 _∈ i_ R _>_ 0. Moreover, from the signs of coefficients of _O_ ( _z_[3] ) terms we obtain that _c[u] p_ 1 _,p_ 2[deviates][from] _[T][K]_[as] proposed in Theorem 313. See also Figure 8.4. 

**==> picture [263 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
L [∗]<br>+ [T][K]<br>R [3]<br>TK<br>**----- End of picture text -----**<br>


Figure 8.4: _On the left: u ∈MTK_ ( _**a**_ ;[3] 2 _[,]_[1] 2[)][around][the][puncture] _[p]_[1][with][winding] number[3] 2[.] _[On][the][right:][u][ ∈M][T][K]_[(] _**[a]**_[;][1] 2 _[,]_[3] 2[)][around][the][puncture] _[p]_[2][with][winding] number[3] 2[.] 

Now, let _u ∈MTK_ ( _**a** ,_[3] 2 _[,]_[1] 2[) and] _[ {][u]_[˜︁] _[k][}][k]_[ be a sequence of elements of] _[ M][T][K]_[(] _**[a]**[,]_[1] 2 _[,]_[1] 2[)] that converge to _u_ . We would like to geometrically describe how the holomorphic curves are deformed. By the above, we know that the normal components of _u_ ˜︁ _k_ are of the form _akz_ + _O_ ( _z_[3] ), where _ak →_ 0 as _k →∞_ . This means that for _k ≫_ 0 large each _cpu_[˜︁] 1 _k,p_ 2[intersects] _[T][K]_[additionally][at][some][time] _[a]_[1][+] _[ ε][k]_[.][Since] _[ε][k][→]_[0][as] _k →∞_ , we obtain certain vanishing “spikes”. See also Figure 8.5. In addition, these vanishing _ak_ coefficients will contribute as a gluing parameter which induces a parametrization of _MTK_ ( _**a** ,_[3] 2 _[,]_[1] 2[)][near] _[M][T][K]_[(] _**[a]**[,]_[1] 2 _[,]_[1] 2[).][Similarly,][we][can][describe] _MTK_ ( _**a** ,_[3] 2 _[,]_[1] 2[),][see][also][Figure][8.5.] 

143 

**==> picture [251 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
L [∗]<br>+ [T][K]<br>R [3]<br>TK<br>**----- End of picture text -----**<br>


Figure 8.5: _On the left:_ A local visualization of the normal component of _u_ ˜︁ _k ∈ MTK_ ( _**a**_ ; 2[1] _[,]_[1] 2[)][around][the][puncture] _[p]_[1][with][the][winding][number] 12[.][Note][that] due to the spike the curve _cpu_[˜︁] 1 _k,p_ 2[intersects] _[T][K]_[again][at][some][time] _[ε][k]_[.][Also][as] _k →∞_ the spike vanishes and the winding at _p_ 1 becomes 32[.] _On the right: u_ ˜︁ _k ∈MTK_ ( _**a**_ ; 2[1] _[,]_[1] 2[)][around][the][puncture] _[p]_[2][with][the][winding][number][1] 2[which] becomes[3] _[k][→∞]_[.] 2[as] 

**Conjecture 317.** _Let_ _**a** be a Reeb chord on L[∗]_ + _[T][K][and][J][be][generic.][Then][the] moduli space MTK_ ( _**a**_ ;[1] 2 _[, . . . ,]_ 2[1][)] _[with]_[2] _[ℓ][switches][admits][a][natural][compactifica-] tion to a compact oriented_ ( _|_ _**a** |_ + _ℓ_ ) _-dimensional manifold MTK_ ( _**a** ,_[1] 2 _[, . . . ,]_[1] 2[)] _[with] corners. The codimension_ 1 _strata consist of:_ 

**==> picture [404 x 29] intentionally omitted <==**

- ( _ii._ ) _moduli spaces MTK_ ( _**a** ,_ 2[1] _[, . . . ,]_[1] 2 _[,]_[ 2] _[,]_[1] 2 _[, . . .]_[1] 2[)] _[with]_[2] _[ℓ]_[+ 1] _[switches,][where][we] added one_ 2 _switch from L[∗]_ + _[T][K][back][to][L][∗]_ + _[T][K][(i.e.][not][from]_[R][3] _[to]_[R][3] _[).]_ 

- ( _iii._ ) _products of moduli spaces_ 

**==> picture [240 x 30] intentionally omitted <==**

_where the Reeb chords_ _**b** i have total degree |_ _**a** | −_ 1 _and the moduli spaces MTK_ ( _**b** i_ ;[1] 2 _[, . . . ,]_[1] 2[)] _[have][together]_[2] _[ℓ][switches.]_ 

- ( _iv._ ) _moduli spaces MTK_ ( _**a** ,_[1] 2 _[, . . . ,]_[1] 2 _[,]_[ 1] _[,]_ 2[1] _[, . . .]_[1] 2[)] _[with]_[2] _[ℓ][−]_[1] _[switches,][where][two] consecutive switches_[1] _[replaced][by][a][single]_[1] _[switch,][provided][that][the]_ 2 _[were]_ 

- _first replaced_ 2[1] _[switch][was][switching][from]_[R][3] _[to][L][∗]_ + _[T][K][.][See][also][Figure][8.6.]_ 

_The codimension_ 2 _strata consist of corners given by the combinations of phenomena_ ( _i._ ) _−_ ( _iv._ ) _and_ 

- ( _v._ ) _moduli spaces MTK_ ( _**a** ,_ 2[1] _[, . . . ,]_[1] 2 _[,]_[5] 2 _[,]_[1] 2 _[, . . .]_[1] 2[)] _[with]_[2] _[ℓ][switches,][where][one]_ 12 _switch was replaced by a_[5] 2 _[switch.]_ 

- ( _vi._ ) _moduli spaces MTK_ ( _**a** ,_[1] 2 _[, . . . ,]_[1] 2 _[,]_[ 2] _[,]_ 2[1] _[, . . .]_[1] 2[)] _[with]_[2] _[ℓ][−]_[1] _[switches,][where][two] consecutive switches_[1] _[replaced][by][a][single]_[2] _[switch,][provided][that][the]_ 2 _[were]_ 

- _first replaced_ 2[1] _[switch][was][switching][from][L][∗]_ + _[T][K][to]_[R][3] _[.][See][also][Figure][8.6.]_ 

_Partial proof._ The boundary codimension 1 configurations ( _i_ ) _−_ ( _ii._ ) were already discussed in Theorem 313, and the configuration ( _iii._ ) is just a standard breaking 

144 

phenomenon from Symplectic field theory, see [CELN16, BEH[+] 03]. The boundary codimension 1 configuration ( _iv._ ) is given by the collapse of two switches into a single one, which is realized by a vanishing “spike” in the conormal direction, see Figure 8.6. Note that this degeneration is not violating the boundary conditions coming from the arboreal singularity. For the same phenomenon, we refer to [CELN16]. 

**==> picture [281 x 101] intentionally omitted <==**

**----- Start of picture text -----**<br>
L [∗]<br>+ [T][K]<br>TK R [3]<br>**----- End of picture text -----**<br>


Figure 8.6: _Configuration_ ( _iv._ ) _:_ vanishing conormal “spike”. 

Now, we are going to inspect the codimension 2 phenomenon ( _vi._ ). The configuration ( _vi._ ) will appear as an intersection of two configurations ( _i._ ). We take an arc from _∂D_ 2 _ℓ_ +1 connecting punctures _pi, pi_ +1 of winding numbers 2[1] _[,]_[1] 2[.] Then, while collapsing the arc, we obtain a 2-parametric family of parameters which creates a corner. 

Let us take a local model of the normal component of _J_ -holomorphic curves near punctures _pi, pi_ +1. Since we would like to work with two punctures rather then the quadrant _Q_ , we take as a domain a punctured half disc _H_ := _{ζ ∈_ (C _, i_ ) _| Im_ ( _ζ_ ) _≥_ 0 _,_ 0 _< |ζ| ≤_ 1 _, ζ_ = _−ε}_ . Recall that we can translate the points from _H_ to _Q_ by _ζ ↦→ ζ_[1] _[/]_[2] . Then up to _O_ ( _ζ_[5] _[/]_[2] ), we can locally model the normal components of the _J_ -holomorphic curves on the holomorphic functions 

**==> picture [161 x 15] intentionally omitted <==**

where 0 _≤ δ ≤ ε_ . The function _fε,δ_ has the following properties. The zeros are _−ε, −δ,_ 0. Along ( _−_ 1 _, −ε_ ) _∪_ (0 _,_ 1), the real part of _fε,δ_ vanishes and the imaginary part matches the conormal boundary conditions. Analogously, along ( _−ε,_ 0) the imaginary part of _fε,δ_ vanishes. 

Geometrically, observe that the zero at _−δ_ corresponds to the intersection of two small spikes with _TK_ - one spike for each puncture. Also, as _−δ_ moves to _−ε_ the winding at _pi_ changes from[1] 2[to][3] 2[and][similarly][for][the][puncture] _[p][i]_[+1][.][See] also Figure 8.7. Hence, we can consider as gluing parameters _ε, δ_ with 0 _≤ δ ≤ ε_ . _L[∗]_ + _[T][K] •_ ~~_•_~~ _• TK_ R[3] Figure 8.7: _On the left: u ∈MTK_ ( _**a**_ ;[3] 2 _[,]_[1] 2[) around collapsing punctures] _[ p]_[1][and] _[ p]_[2][.] _On the right: u ∈MTK_ ( _**a**_ ; 2) around the puncture _p_ 1 with winding number 2. 

145 

Now, let us consider the codimension 2 phenomenon ( _v._ ). The configuration ( _v._ ) can be created from intersection of configurations ( _i._ ) and ( _ii._ ). I.e. ( _v._ ) can appear as a collapse of punctures with winding 2 and[1] 2[,][or][one][puncture] 3 5 can change its winding from 2[to] 2 _[,]_[see][Figure][8.8.][Since][both][deformations] correspond to different arcs of the punctured disc, we obtain a corner. _L[∗]_ + _[T][K] • • TK_ R[3] Figure 8.8: _On the left: u ∈MTK_ ( _**a**_ ;[3] 2 _[,]_[1] 2[)][around][the][puncture] _[p]_[1][with][winding] number[3] 2[.] _[On][the][right:][u][ ∈M][T][K]_[(] _**[a]**_[;][5] 2 _[,]_[1] 2[)][around][the][puncture] _[p]_[1][with][winding] number[5] 2[.] 

**Lemma 318.** _There is a constant ksw ∈_ N _such that every MTK_ ( _**a** ,_ _**n**_ ) _is empty, if the number of switches is bigger then ksw._ 

_Proof._ The lemma follows from similar argument as [CEL09, thm 1.2]. 

## **8.4 Broken and chain strings maps** 

In this section, we outline a chain map between the chain complexes for Legendrian contact homology and so-called String homology. Then, we discuss the relation to Morse model of the cord algebra. _The precise proofs of the statements will remain to be done._ 

Motivated by broken strings from [CELN16, ENS17], we are going to construct a degree zero string homology for _TK,ε_ . See also [Oka25]. 

_Notation_ 319 _._ In order to agree with the notation from [CELN16, ENS17], the ambient space R[3] will be denoted by _Q_ . 

Next, let us consider an ( _ε/_ 2)-radius tubular neighborhood _νε/_ 2 _TK,ε_ . Recall that the positive co-orientation _TK,ε_ is given by vectors pointing _inside_ of _νεK_ . Then we put 

**==> picture [113 x 13] intentionally omitted <==**

Let us fix _x_ 0 _∈_ ( _∂N_ + _\ TK,ε_ ) and _v_ 0 _∈ Tx_ 0 _N_ +. 

**Definition 320.** _A_ _**broken string with** ℓQ_ _**-strings** on TK,ε is a tuplet s_ = ( _a_ 1 _, . . . , a_ 2 _ℓ_ +1; _s_ 1 _, . . . , s_ 2 _ℓ_ +1) _consisting of real numbers_ 0 = _a_ 0 _< · · · < a_ 2 _ℓ_ +1 _and non-constant C[∞] -maps_ 

**==> picture [239 x 13] intentionally omitted <==**

_such that the following holds_ 

**==> picture [154 x 13] intentionally omitted <==**

146 

( _ii._ ) _for j_ = 1 _, . . . ,_ 2 _ℓ, sj_ ( _aj_ ) = _sj_ +1( _aj_ ) _∈ TK,ε._ 

( _iii._ ) _Let σj denotes the normal component of sj near its endpoints. Then for every_ 2 _k ∈_ N _the derivatives σj_[(2] _[k]_[)] _at the endpoints vanish. For i_ = 1 _, . . . , ℓ and every k ∈_ N _it holds that_ 

**==> picture [196 x 37] intentionally omitted <==**

_Paths s_ 2 _i are called Q_ _**-strings** and paths s_ 2 _i_ +1 _are called N_ _**-strings** , see Figure 8.9. We equip_ Σ _[◦] ℓ[;][the][set][of][broken][strings][with][ℓQ][-strings,][with][C][∞][topology,] and by completion extend it by also allowing constant_ 0 _time Q/N -strings;_ _**trivial** Q/N_ _**-strings** . The resulting space of all strings will be denoted by_ Σ _ℓ, and we put_ Σ[∆] _ℓ_[:=][Σ] _[ℓ][\]_[ Σ] _[◦] ℓ[.][Moreover,]_[Σ] _[Q] ℓ[n] will consist of broken strings with at least n >_ 0 _trivial Q-strings. The space of all broken strings will be denoted by_ Σ _._ 

**==> picture [147 x 60] intentionally omitted <==**

**----- Start of picture text -----**<br>
T<br>K,ε<br>**----- End of picture text -----**<br>


Figure 8.9: A visualization of a broken string on _TK,ε_ that conists of _Q_ -strings and _N_ -strings. Note the matching jet condions of _N/Q_ -strings at their endpoints. 

_Remark_ 321 _. Q_ -strings are outward-pointing from _TK,ε_ . This follows from the condition ( _iii._ ) in Definition 320 and the geometry of _N_ +. 

**Definition 322.** _A broken string from_ Σ _ℓ is called a string with a Q_ _**-tangency** if it contains a nontrivial Q-string s_ 2 _i with a vanishing first normal derivative σ_ 2[(1)] _i[at][some][endpoint][p][,][and][s]_[2] _[i][can][be][potentially][concatenated][at][p][with][some] non-trivial local N -string. (The second condition just dictates the sign of the first nonzero derivative σ_[(2] _[k][−]_[1)] ( _p_ ) _)._ 

_The subset of all of these strings is denoted by ∂[Q]_ Σ _ℓ. And analogously we define ∂[Q]_ Σ _[Q] ℓ[n][.]_ 

**Definition 323.** _A broken string from_ Σ _ℓ is called a string with a N_ _**-tangency** if it contains a nontrivial N -string s_ 2 _i−_ 1 _touching TK,ε at some interior point p._ 

_The subset of all of these strings is denoted by ∂[N]_ Σ _ℓ. And analogously we define ∂[N]_ Σ _[Q] ℓ[n][.]_ 

_Remark/Notation_ 324 _._ Let ev _Q,_ 2 _i_ : Σ _ℓ ×_ (0 _,_ 1) _→ Q_ be an evaluation map on interiors of _Q_ -strings _s_ 2 _i_ . In more detail, 

**==> picture [203 x 13] intentionally omitted <==**

**==> picture [312 x 14] intentionally omitted <==**

**==> picture [247 x 19] intentionally omitted <==**

147 

where _v_ ( _x_ ) is a _negatively_ co-oriented (normalized) normal vector at _x ∈ TK,ε_ . Compare _FQ_ also with maps for outward-pointing chords from Definition 41. Let _d ≥_ 0. We also introduce switch evaluation maps _TQ,[d]_ 2 _i_[: Σ] _[ℓ][→]_[R] _[d]_[by] 

**==> picture [139 x 20] intentionally omitted <==**

Analogously, we introduce also ev _N,_ 2 _i−_ 1 and _TN,[d]_ 2 _i−_ 1[.] 

**Definition 325.** _Let d ≥_ 0 _and_ ∆ _[d]_ = _{_ ( _λ_ 1 _, . . . , λd_ ) _∈_ R _[d] | λk ≥_ 0 _,_[∑︁] _k[λ] k[≤]_[1] _[}][.][A]_ _**weakly generic singular** d_ _**-chain** in_ Σ _[◦] ℓ[is][a][smooth][map][S]_[:][∆] _[d][→]_[Σ] _[◦] ℓ[such] that_ 

- ( _i._ ) _on Q-strings the maps FQ ◦ S and TQ[d]_[+1] _◦ S are stratum transverse to_ 0 _×_ [0 _, ∞_ ) _, respectively jet transverse to_ 0 _._ 

- ( _ii._ ) _on N -strings the maps TN[d]_[+1] _◦ S are jet transverse to_ 0 _,_ ev _N ◦ S_ ( _Int_ (∆ _[d]_ )) _∩ TK,ε_ = _∅ and_ (ev _N ◦ S|∂_ ∆ _d_ ) _[−]_[1] ( _TK,ε_ ) _are_ ( _d −_ 1) _-dimensional manifolds with corners. Moreover, the connected components of_ (ev _N ◦ S|∂_ ∆ _d_ ) _[−]_[1] ( _TK,ε_ ) _projects to ∂_ ∆ _[d] as immersed manifolds._ 

_Finally, on weakly generic singular chains, we introduce the following manifolds with corners_ 

**==> picture [342 x 17] intentionally omitted <==**

**==> picture [280 x 17] intentionally omitted <==**

_Remark_ 326 _._ The condition ( _ii._ ) from Definition 325 looks a bit artificial and will be used in the definition of the String homology, Definition 330. An obvious way to avoid ( _ii._ ) is to forget _N_ -strings and work only with _Q_ -strings with lengths bounded from below by some small positive number. But, as a consequence, we will then aim for constructing a string homology with coefficients only in Z and not in Z[ _π_ 1( _TK,ε_ )]. 

**Definition 327.** _Using the conditions_ ( _i._ ) _,_ ( _ii._ ) _from Definition 325 we define also weakly generic singular chains for ∂[Q]_ Σ _[◦] ℓ[and][∂][N]_[Σ] _[◦] ℓ[.]_ 

_Weakly generic singular chains for broken strings_ Σ _ℓ with a single trivial Q/N - string are introduced as follows. We again use the conditions_ ( _i._ ) _,_ ( _ii._ ) _, but not for the trivial string, and also the corner evaluation maps T[d]_[+1] _are not applied for the endpoints surrounding the trivial string._ 

_This induces weakly generic singular d-chains on the whole_ Σ _. We also extend the definitions of Mδ[d] Q_ ( _S_ ) _[and][M][ d] δN_ ( _S_ ) _[.]_ 

_Remark_ 328 _._ We can view the connected components of _Mδ[d] Q_ ( _S_ )[as weakly generic] singular _d_ -chains inside _S_ , let us denote them by _SQ_ . Analogously, _Mδ[d] N_ ( _S_ )[will] contribute by weakly generic singular ( _d −_ 1)-chains inside _S_ , let us denote them by _SN_ . 

**Definition 329.** _A_ _**string coproducts** δQ_ _**and** δN are defined on a weakly generic singular d-chain S by sums of SQ/SN with inserted trivial N/Q-strings at Mδ[d] Q_ ( _S_ ) _[and][M][ d] δN_ ( _S_ ) _[,][respectively.]_ 

148 

**Definition 330.** _By Ck[sing]_ + _ℓ_[(Σ] _[ℓ][, ∂][Q]_[Σ] _[ℓ][∪][∂][N]_[Σ] _[ℓ]_[)] _[we][denote][a][free]_[Z] _[-module][gener-] ated by weakly generic relative singular_ ( _k_ + _ℓ_ ) _-simplices in_ Σ _ℓ. Similarly, by Ck[sing]_ + _ℓ−n_[(Σ] _[Q] ℓ[n]_[)] _[we][understand][a][free]_[Z] _[-module][generated][by][weakly][generic][singular]_ ( _k_ + _ℓ − n_ ) _-simplices in the space of broken strings with n constant and n − ℓ non-constant Q-strings. We put_ 

**==> picture [407 x 32] intentionally omitted <==**

_Concatenations at the base point induce on Ck[string]_ (Σ) _the structure of a noncommutative (but strictly associative)_ Z _-algebra._ 

_The singular boundary operator ∂[sing] and the string coproducts δQ, δN induce a linear map of degree −_ 1 

**==> picture [212 x 16] intentionally omitted <==**

_see also Figure 8.10._ 

**==> picture [313 x 36] intentionally omitted <==**

_where I[string] is a two-sided ideal of C_ 0 _[string]_ (Σ) _generated by the image of ∂[sing]_ + _δQ_ + _δN ._ 

**==> picture [53 x 57] intentionally omitted <==**

**==> picture [250 x 75] intentionally omitted <==**

**==> picture [57 x 58] intentionally omitted <==**

Figure 8.10: String operations _δQ_ and _δN_ . 

_Remark_ 331 _._ Let us heuristically relate the skein relations arising from _I[string]_ to _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]). Hence let us consider a 1-dimensional family _s[t]_ of broken strings in _C_ 1 _[string]_ (Σ). Then from ( _∂[sing]_ + _δQ_ + _δN_ )( _s[t]_ ) = 0 we obtain the following skein relations: 

**==> picture [215 x 87] intentionally omitted <==**

**==> picture [39 x 40] intentionally omitted <==**

Now, we claim that the relation ( _i._ ) corresponds in _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]) to non/bifurcations of a gradient-like trajectory of chords on _MK,ε_ . Since the first term of ( _ii._ ) vanishes as a relative chain, the relation ( _ii._ ) translates to _m_ ∆ _ε_ = 1 in _Cord[M]_ ( _TK,ε_ ; Z[ _λ[±]_[1] _, µ[±]_[1] ]). Compare also with the skein relations for the knot case as in [CELN16, pg. 9] or [ENS17, pg. 22]. 

149 

_Assumption_ 332 _._ We assume that the reader is familiar with the Legendrian contact homology with loop space coefficients on the level of Appendix C. We will briefly recall the concept. 

_Remark/Notation_ 333 _. C_ ( _R_ ) is a graded ring, which is as a Z-module generated by the Reeb strings. Reeb strings are alternating words of Reeb chords on _L[∗]_ + _[T][K]_ and capping paths in _L[∗]_ + _[T][K]_[concatenating the ends of Reeb chords (and the base] point _x_ 0). The grading is given by a bidegree consisting of the singular chain degree and the sum of Reeb chord degrees. The differential on _C_ ( _R_ ) is given by _∂L_ := _∂[sing]_ + _∂[sy]_ , where _∂[sy]_ ( _**a**_ ) is counting holomorphic discs _M[sy] /_ R with the Reeb chord _**a**_ at the positive infinity. Then, the homology of ( _C_ ( _R_ ) _, ∂L_ ) is called **Legendrian contact homology** . 

**Theorem 334.** _For i_ = 0 _,_ 1 _there are well defined maps_ Φ _i_ : _Ci_ ( _R_ ) _→ Ci[string]_ (Σ) _that intertwine with boundary operators, i.e._ 

**==> picture [290 x 14] intentionally omitted <==**

_Sketch proof._ We define maps Φ _i_ on Reeb chords by 

**==> picture [145 x 38] intentionally omitted <==**

where [ _MTK,ε_ ( _**a** ,_[1] 2 _[, . . . ,]_[1] 2[)]][denotes][the][boundaries][of][the][disks][from][the][moduli] space, which become chains of broken strings after connecting the ends of _**a**_ by capping paths to the base point _x_ 0. 

Now, by Conjecture 317, the dimension of _MTK,ε_ ( _**a** ,_[1] 2 _[, . . . ,]_[1] 2[)][is] _[|]_ _**[a]**[|]_[ +] _[ ℓ]_[.][So,] Φ _i_ ( _**a**_ ) _∈ C|[string]_ _**a** |_ (Σ), and Φ _i_ preserves degree. Let us verify the equation (8 _._ 5) _._ We need to inspect how the codimension 1 strata of _MTK,ε_ ( _**a** ,_[1] 2 _[, . . . ,]_[1] 2[)][are][contributing][to] _[∂][sing]_[Φ(] _**[a]**_[)][provided][that] _[|]_ _**[a]**[|]_[ = 1.] By Conjecture 317 (Theorem 313), there are four types of configurations: 

- Discs with a[3][These discs contribute by [0] as relative chains, since] 2[switch.] 

- the normal jet conditions of the discs at[3] 2[switch][are][matching][with] _[∂][Q]_[Σ.] 

- Discs with a symplectization building which are counted by Φ( _∂L_ ( _**a**_ )). 

- Discs with a switch of winding 1 along R[3] which are counted by _δQ_ Φ( _**a**_ ) (this phenomenon appeared already in [CELN16]). 

- Discs with a switch of winding 2 along _L[∗]_ + _[T][K,ε]_[which are counted by] _[ δ][N]_[Φ(] _**[a]**_[).] Note that here we used the shift in grading of _C∗[sing]_ (Σ _[Q] ℓ[n]_[) by the number of] trivial _Q_ -strings. 

   - For example, _MTK,ε_ ( **a** _,_ 2 _,_[1] 2 _[,]_[1] 2[)] _[ ⊂][∂] MTK,ε_ ( **a** _,_[1] 2 _[,]_[1] 2[), so dim] _[ M][T][K,ε]_[(] **[a]** _[,]_[ 2] _[,]_[1] 2 _[,]_[1] 2[) =] 1. Hence, [ _MTK,ε_ ( **a** _,_ 2 _,_[1] 2 _[,]_[1] 2[)]] _[∈][C]_ 1 _[sing]_ (Σ2 _[Q]_[1][).][But][by][the][definition][we][have] that _C_ 1 _[sing]_ (Σ2 _[Q]_[1][) =] _[ C]_ 0+2 _[sing] −_ 1[(Σ] _[Q]_ 2[1][)] _[ ⊂][C]_ 0 _[string]_ (Σ). 

Now, let us discuss more the relations of _H_ 0 _[string]_ ( _TK,ε_ ) to _Cord[M]_ ( _TK,ε_ ) even though the reader is gently warned that the proceeding discussion will be slightly speculative. 

150 

**Definition 335.** _Let T_ 0 _>_ 0 _. Then by PK,ε we understand the space of paths H_[3] ([0 _, t_ 0] _,_ R[3] ; _TK,ε_ ) _that are outward-pointing from TK,ε at their endpoints._ 

_Next, by PK,ε[chord] ⊂PK,ε we denote the realization of the space MK,ε as a space of T_ 0 _-time chords (with constant speed parametrizations). By PK,ε_[∆] _[we][denote][the] constant paths._ 

_Remark_ 336 _. PK,ε_ is a Banach manifold with corners. This is followed by similar argument as the proof of Lemma 435. 

**Definition 337.** _By_ _**E** ε we denote the energy functional on H_ 3([0 _, T_ 0] _,_ R[3] ; _TK,ε_ ) _. Next, ∂[−] PK,ε is defined as the subset of ∂PK,ε, where −∇_ _**E** ε is strictly outwardpointing via Definition 32. Then by ∂−PK,ε we denote the closure of ∂[−] PK,ε in ∂PK,ε._ 

**Lemma 338.** _The flow of −∇_ _**E** ε is a “deformation” of PK,ε to PK,ε[chord] relative to ∂−PK,ε._ 

_More precisely. With respect to the flow of −∇_ _**E** ε the set ∂−PK,ε ∪PK,ε[chord] is a positively invariant exit set for PK,ε (compare with Conley index pairs from Definition 142). In addition, for every c ∈PK,ε there is a t_ 0 _∈_ [0 _, ∞_ ] _such that ϕ[t] −∇_[0] _**E** ε[∩]_[(] _[∂][−][P][K,ε][∪P] K,ε[chord]_[)] _[ ̸]_[=] _[ ∅][.]_ 

_Proof._ The lemma follows from the following observations. We know from Remark 439 that 

_Crit_ ( _**E** ε|PK,ε_ ) = _Crit_ ( _**E** ε|PK,εchord∪PK,ε_[∆][)] and also _PK,ε_[∆] _[⊂][∂][−][P][K,ε]_[.] Moreover, _PK,ε[chord]_ is locally invariant under the flow _ϕ−∇_ _**E** ε_ and _ϕ−∇_ _**E** ε_ has no periodic orbits. 

**Conjecture 339.** _Let K be generic and ε >_ 0 _small. Let c be a path from ∂PK,ε. Then c ∈ ∂[−] PK,ε iff c can be reparametrized such that one of the following conditions on normal jets σ of c holds:_ 

( _S_ ) _At the starting point we have_ (︂ _σ_[(1)] (0) _, σ_[(2)] (0) _, σ_[(3)] (0))︂ _∈_ 0 _×_ 0 _×_ ( _−∞,_ 0) _._ 

( _E_ ) _At the endpoint we have_ (︂ _σ_[(1)] ( _T_ 0) _, σ_[(2)] ( _T_ 0) _, σ_[(3)] ( _T_ 0))︂ _∈_ 0 _×_ 0 _×_ (0 _, ∞_ ) _._ 

- _Note that the curve c satisfying_ ( _S_ ) _or_ ( _E_ ) _can be viewed as a Q-string in ∂[Q]_ Σ1 _. Moreover, the analogous holds for paths in PK,ε[chord][.]_ 

_Heuristic proof._ Instead of general paths from _PK,ε_ we consider only _PK,ε[chord]_ (i.e. _MK,ε_ ). For this, we use the results of Section 3.5, where we investigated the behavior of _−∇Eε_ along _∂MK,ε_ . We would like to show that the chords _∂[−] PK,ε[chord]_ are precisely those boundary chords that appear as limits of interior chords while creating a single vanishing spike as in Figure 8.5. 

Let us restrict _MK,ε_ outside of weakly special and diagonal points. Recall that in Lemmata 54 and 58 we described _MK,ε|SK_ as a trivial bundle over the standard set _SK ⊂_ (R _/T_ Z)[2] with a typical fiber as the square. Then _−∇Eε_ is strictly outward-pointing along _{F_ 1[[] _[ε]_[]] _>_ 0 _∧ F_ 2[[] _[ε]_[]] = 0 _}_ . Observe that along this set, the chords have an exterior tangent at the endpoints. Moreover, as the chords are approaching the chord with the tangency at the endpoint, they are 

151 

additionally intersecting _once TK,ε_ close to the end-point. As the chords converge to the tangent one, the additional intersection points converge to the endpoint, see also Figure 8.11 left. In particular, the chords of _{F_ 1[[] _[ε]_[]] _>_ 0 _∧ F_ 2[[] _[ε]_[]] = 0 _}_ will correspond to ( _E_ ) _._ On the another hand, _−∇Eε_ is strictly inward-pointing along _{F_ 1[[] _[ε]_[]] = 0 _∧ F_ 2[[] _[ε]_[]] _>_ 0 _}_ . However, along this set, the chords have an exterior tangency at the starting points. Hence, these chords do not belong to the groups ( _S_ ) or ( _E_ ), see also Figure 8.11 right. 

**==> picture [213 x 144] intentionally omitted <==**

Figure 8.11: A visualization of the chords near to the boundary of _MK,ε|SK_ . _On the left:_ the chords approaching the chord with the tangency at the endpoint become shorter, and the tangency at the endpoint is exterior. Note that the purple point will converge to the endpoint - compare with the vanishing spikes from Figure 8.5. _On the right:_ the chords approaching the chord with tangency at the starting point become longer, and the tangency at the starting point is exterior. 

Now, let us inspect the behavior of chords from _MK,ε_ near the diagonal ∆ _ε_ . From Section 3.4 we know that near ∆ _ε_ the set _MK,ε_ looks like a fibration over ∆ _ε_ with cuspical fibers. Moreover we expect that _−∇Eε_ is strictly outward-pointing along both sets _{F_ 1[[] _[ε]_[]] _>_ 0 _∧ F_ 2[[] _[ε]_[]] = 0 _}_ and _{F_ 1[[] _[ε]_[]] = 0 _∧ F_ 2[[] _[ε]_[]] _>_ 0 _}_ . We would like to verify that the chords from these sets belong to the groups ( _S_ ) and ( _E_ ). For this, see Figure 8.12. 

152 

**==> picture [190 x 159] intentionally omitted <==**

**----- Start of picture text -----**<br>
c 2<br>x c ˜︁<br>c 1<br>**----- End of picture text -----**<br>


Figure 8.12: A visualization of the outward-pointing chords that starts at some _x ∈ TK,ε_ and are short, i.e. close to the diagonal. _TK,ε_ is drawn as a graph, where the positive co-orientation is pointing below the graph, i.e., below the graph is the interior of _νεK_ . The blue plane is the plane tangent to _TK,ε_ at _x_ . The orange lines describe the endpoints of the chords that emanate from _x_ and are tangent to _TK,ε_ at the start/endpoint. The chord _c_ 1 has an interior tangent at the starting point and lies entirely on the tangent blue plane. _c_ 2 has an exterior tangent at the endpoint and on its interior lies outside to _νεK_ . The purple chord _c_ ˜︁ is intersecting _TK,ε_ also in its interior at the purple point. As _c_ ˜︁ approaches _c_ 1, the purple point converges to the starting point. Also, as _c_ ˜︁ approaches _c_ 2, the purple point converges to the endpoint point. Compare with vanishing spikes from Figure 8.5. 

_Remark_ 340 _. On a chain map from Ck[string]_ (Σ) _to Ck[M]_[(] _[T][K,ε]_[;][ Z][[] _[λ][±]_[1] _[, µ][±]_[1][])] 

In the spirit of Lemma 338 and Conjecture 339 it seems natural to take singular chains in Σ and drag the _Q_ -strings with the flow of _−∇_ _**E** ε_ till _Crit_ ( _**E** ε_ ) or _∂[Q]_ Σ. In particular, _N_ -strings will be translated to the words of _λ, µ_ . During this process, we will be performing string coproduct operations. However, it is not known how to bound the number of these string operations. 

Therefore, such an obstacle was resolved for the knot case by different deformation of broken strings, see [CELN16]. Their approach was to shrink _Q_ -strings to piecewise-linear and then finally to linear. While keeping the (existing) switching points fixed, such a process will have control over the number of performed string operations. 

If we try to mimic the approach from [CELN16] in the torus case, we encounter the following problem. Let us try to shrink a single piecewise linear _Q_ -string to a linear one while fixing the endpoints. During this process, a _Q_ -string _s_ can become tangent to _TK,ε_ at one of its endpoints. If _s ∈ ∂[Q]_ Σ, then we can successfully forget about the string, since our theories are relative to this boundary. However, this is clearly not always the case. So the precise linearization process remains unknown. 

153 

## **Appendices** 

154 

## **A. Maslov index in** R[2] _[n]_ ( _, ω_ 0) 

## **A.1 Linear algebra** 

**Definition 341.** _A_ _**symplectic vector space**_ ( _V, ω_ ) _is a real finite dimensional vector space V together with a_ _**symplectic form** ω, that is, a skew–symmetric nondegenerate bilinear map ω_ : _V × V →_ R _._ 

_A map φ_ : ( _V_ 1 _, ω_ 1) _→_ ( _V_ 2 _, ω_ 2) _is called a_ _**linear symplectomorphism** if it is a vector space isomorphism and φ[∗] ω_ 2 = _ω_ 1 _._ 

_A basis {vi, wi}i of_ ( _V, ω_ ) _is called a_ _**symplectic basis** if_ 

**==> picture [235 x 13] intentionally omitted <==**

_Remark_ 342 _._ Every ( _V, ω_ ) has a symplectic basis, in particular ( _V, ω_ ) is evendimensional. Also, the choice of the symplectic basis uniquely determines _ω_ . For details, see [MS17, Thm 2.1.3.] 

_Example_ 343 _._ (R[2] _[n] , ω_ 0). Let ( _xi, yi_ ) be standard (Cartesian) coordinates on R[2] _[n]_ , then its basis vectors _{v[x][i] , w[y][i] }_ form a symplectic basis of the **standard symplectic form** _ω_ 0. Hence, in view of Remark 342, every symplectic vector space is symplectomorphic to (R[2] _[n] , ω_ 0) for some _n_ . 

More explicitly, _ω_ 0 is given as 

**==> picture [115 x 13] intentionally omitted <==**

0 _−_ 1 where _v, w ∈ R_[2] _[n] , J_ 0 := , and _⟨ , ⟩_ is the standard inner product. Here 1 0 (︄ )︄ _J_ 0 is called the **standard complex structure** , because we can identify (R[2] _[n] , ω_ ) with (C _[n] , i_ ) such that the action of _J_ 0 is identified with the multiplication by _i_ . 

The **symplectic group** _Sp_ (2 _n,_ R) is the group of all linear symplectomorphisms _φ_ : (R[2] _[n] , ω_ 0) _→_ (R[2] _[n] , ω_ 0). _Sp_ (2 _n,_ R) is connected, see [MS17, Prop 2.2.4]. _Example_ 344 _._ ( _V × V[∗] , ω×_ ), where 

**==> picture [209 x 13] intentionally omitted <==**

for ( _v, v[∗]_ ) _,_ ( _w, w[∗]_ ) _∈ V × V[∗] ._ 

Then the **anti-symplectic involution** on ( _V × V[∗] , ω×_ ) is the map _σst_ : ( _v_ 1 _, v_ 2 _[∗]_[)] _[ ↦→]_[(] _[v]_[1] _[,][ −][v]_ 2 _[∗]_[).][Note][that] _[σ] st[∗][ω][×]_[=] _[ −][ω][×]_[.] 

**Definition 345.** _Let V be a real even dimensional vector space. Then a_ _**linear complex structure** J is a (real) linear automorphism on V such that_ 

**==> picture [49 x 11] intentionally omitted <==**

_We will write_ ( _V, J_ ) _and call this tuple a_ _**complex vector space** ._ 

_Remark_ 346 _._ For any vector space ( _V, J_ ) of the real dimension 2 _n_ there are _n_ vectors _{vi}i_ such that _{vi, Jvi}i_ is a real basis of _V_ . In particular, there is a vector space isomorphism _φ_ : _V →_ R[2] _[n]_ such that _φ[∗] J_ 0 = _J_ . For details, see [MS17, Thm 2.5.1.] 

155 

**Definition 347.** _Let_ ( _V, J_ ) _be a complex vector space and ω a symplectic form on V . Then J is called_ _**compatible with** ω if_ 

_ω_ ( _Jv, Jw_ ) = _ω_ ( _v, w_ ) _for all v, w ∈ V_ 

_and_ 

_ω_ ( _v, Jv_ ) _>_ 0 _for all nonzero v ∈ V._ 

_**The space of all** J_ _**compatible with** ω will be denoted by_ 

**==> picture [44 x 13] intentionally omitted <==**

_Also, we define the space_ 

Ω( _V, J_ ) := _{ω symplectic form on V | J ∈J_ ( _V, ω_ ) _},_ 

_or equivalently,_ 

**==> picture [319 x 13] intentionally omitted <==**

_Remark_ 348 _._ If _J ∈J_ ( _V, ω_ ), then _gJ_ ( _v, w_ ) := _ω_ ( _v, Jw_ ) defines an inner product on _V_ and _h_ := _gJ_ + _iω_ defines a Hermitian inner product. 

**Lemma 349** ([MS17, Thm 2.5.5.]) **.** _J_ ( _V, ω_ ) _is non-empty and contractible._ 

_Proof._ Due to the existence of the symplectic basis, we only need to consider _J_ ( _R_[2] _[n] , ω_ 0). 

Elements of _J_ (R[2] _[n] , ω_ 0) can be characterized by 

**==> picture [389 x 15] intentionally omitted <==**

Thus 

**==> picture [176 x 14] intentionally omitted <==**

where in the first equality we used the definition of _J_ 0. In the next two equalities, we used consequently the first two identities of (A.1). Observe that 

**==> picture [56 x 11] intentionally omitted <==**

is a symmetric, positive definite, and symplectic matrix. Hence any _J ∈J_ (R[2] _[n] , ω_ 0) can be written uniquely in the form _J_ = _J_ 0 _P_ , where _P_ satisfies the conditions above. Then by [MS17, Thm 2.2.3.] from the eigendecompositions of _P_ and _P[α]_ we know that any power _P[α]_ is also of this kind for _α ≥_ 0. Hence, we can connect _J_ = _J_ 0 _P_[1] with _J_ 0 by sending the exponent 1 _→_ 0. Note that the obtained path lies in _J_ (R[2] _[n] , ω_ 0), which concludes the proof. 

˜ ˜ _Remark_ 350 _._ Let _g_ be an inner product on ( _V, J_ ). Then for _g_ := 1 _/_ 2(˜ _g_ + _J[∗] g_ ) we have _J[∗] g_ = _g_ . Hence Ω( _V, J_ ) is non-empty. Moreover, Ω( _V, J_ ) is convex and thus contractible. 

**Definition 351.** _A linear subspace_ Λ _of_ ( _V, ω_ ) _is called_ _**Lagrangian** if ω|_ Λ = 0 _and_ dim Λ =[1] 2[dim] _[ V][ .]_ 

_Remark_ 352 _._ Lagrangian subspaces are the largest linear subspaces on which the symplectic form vanishes. 

156 

_Remark_ 353 _._ Let Λ1 and Λ2 be transverse Lagrangians in ( _V, ω_ ). If _{v_ 1 _, . . . , vn}_ is a basis of Λ1, then there is an unique basis _{w_ 1 _, . . . , wn}_ of Λ2 such that _{v_ 1 _, . . . , vn, w_ 1 _, . . . , wn}_ is a symplectic basis of ( _V, ω_ ). See [KF19]. 

**Definition 354.** _A linear subspace R of_ ( _V, J_ ) _is called_ _**totally real** if R ∩ JR_ = _{_ 0 _} and_ dim _R_ =[1] 2[dim] _[ V][ .]_ 

**Lemma 355.** _For Lagrangian and totally real subspaces it holds:_ 

- ( _i._ ) _Let_ Λ _be a Lagrangian subspace in_ ( _V, ω_ ) _. Then_ Λ _⊥gJ J_ Λ _for every J ∈ J_ ( _V, ω_ ) _. In particular,_ Λ _is totally real._ 

- ( _ii._ ) _Let R be a totally real subspace in_ ( _V, J_ ) _. Then there is ω ∈_ Ω( _V, J_ ) _such that R is ω-Lagrangian. Moreover, the space of such ω is contractible._ 

_Proof._ Ad ( _i._ ): Let _v_ 1 _, v_ 2 _∈_ Λ. Then _gJ_ ( _Jv_ 1 _, v_ 2) = _ω_ ( _Jv_ 1 _, Jv_ 2) = _ω_ ( _v_ 1 _, v_ 2) = 0 _._ ˜ Ad ( _ii._ ): Let _g_ be any inner product on _R_ . It induces an inner product on ˜ _JR_ by _J[∗] g_ . This naturally induces the unique inner product _g_ on _V_ such that _R ⊥g JR_ . Hence _J[∗] g_ = _g_ and _g_ ( _J·, ·_ ) is our desired symplectic form. Since the space of inner products on _R_ is convex, the lemma follows. 

_Remark_ 356 _._ For a pair of totally real subspaces in ( _V, J_ ) there might not exist _ω ∈_ Ω( _V, J_ ) such that they become both Lagrangian. 

Indeed, let _R_ 1 = _⟨_ (1 _,_ 0) _[T] ,_ (0 _,_ 1) _[T] ⟩_ and _R_ 2 = _⟨_ ( _i,_ 0) _[T] ,_ (1 _, i_ ) _[T] ⟩_ in (C[2] _, i_ ). Assume that _R_ 1 is Lagrangian for some _ω ∈_ Ω(C[2] _, i_ ). Then 

**==> picture [301 x 52] intentionally omitted <==**

## **A.2 Maslov index** 

In this section, we start with the Maslov index for loops in the Lagrangian Grassmannian. Then we generalize this notion to loops in the totally real Grassmannian and paths in the Lagrangian Grassmannian. The section will be finished by introducing the notion of K¨ahler angles. 

**Definition 357.** _The_ _**Lagrangian Grassmanian**_ Λ( _n_ ) _is the manifold consisting of all Lagrangian subspaces of_ (R[2] _[n] , ω_ 0) _._ 

**Lemma 358** ([Arn67]) **.** _π_ 1(Λ( _n_ )) _[∼]_ = Z _._ 

_Proof._ First, fibre bundles can be seen as examples of fibrations, see [Hat19, Prop 4.48]. Hence, the determinant map det on _O_ ( _n_ ) and _U_ ( _n_ ) induce the following fibration sequences 

**==> picture [275 x 16] intentionally omitted <==**

Also, _U_ ( _n_ ) acts on Λ( _n_ ) transitively with stabilizer _O_ ( _n_ ) at R _[n]_ , and in particular Λ really has the structure of a manifold. Indeed, for an Λ _∈_ Λ( _n_ ), observe that Λ and _J_ 0Λ are orthogonal with respect to the standard inner product. Next, 

157 

if _B, B[′]_ are orthonormal bases of Λ _,_ Λ _[′] ∈_ Λ( _n_ ) respectively, then a linear map that maps _B_ to _B[′]_ and _J_ 0 _B_ to _J_ 0 _B[′]_ is a unitary automorphism. Here we used the fact that _GL_ ( _n,_ C) _∩ O_ (2 _n_ ) = _U_ ( _n_ ). From the ambiguity of the choice of orthonormal basis, it follows that the stabilizer of this action at R _[n]_ is _O_ ( _n_ ). Hence, we obtain a fibration 

**==> picture [131 x 13] intentionally omitted <==**

Recall that det of any orthogonal automorphism is equal to _±_ 1. Hence, we take det[2] to have well defined map on Λ( _n_ ) that assigns to any Λ _∈_ Λ( _n_ ) the determinant square of the unitary automorphism mapping the _{xi}i_ -plane _⊂_ R[2] _[n]_ to Λ. This induces a fibration 

**==> picture [129 x 17] intentionally omitted <==**

where _S_ Λ( _n_ ) is the set of Λ _∈_ Λ( _n_ ) such that det[2] (Λ) = 1. Since _SU_ ( _n_ ) acts transitively on _S_ Λ( _n_ ) with stabilizer _SO_ ( _n_ ), _S_ Λ( _n_ ) _[∼]_ = _SU_ ( _n_ ) _/SO_ ( _n_ ). Hence, we obtain the following commutative diagram of six fibrations 

**==> picture [154 x 100] intentionally omitted <==**

From this, we conclude the following LES of homotopy groups, see [Hat19, Thm 4.41]: 

**==> picture [395 x 44] intentionally omitted <==**

It remains to study _SU_ ( _n_ ) _/SO_ ( _n_ ). Since _SO_ ( _n_ ) is path connected and _SU_ ( _n_ ) is simply connected, the LES of homotopy groups shows us that _SU_ ( _n_ ) _/SO_ ( _n_ ) is simply connected and, in particular, path connected. Plugging this to the sequence (A.2) we obtain that 

**==> picture [161 x 23] intentionally omitted <==**

**Definition 359.** _Let γ be a continuous loop in_ Λ( _n_ ) _. Then the_ _**Maslov index of** γ is defined as_ 

**==> picture [111 x 14] intentionally omitted <==**

**Definition/Theorem 360** ([KF19]) **.** _Let_ Λ1 _∈_ Λ( _n_ ) _. Then_ Λ( _n_ ) _can be written as the following disjoint union_ 

**==> picture [97 x 25] intentionally omitted <==**

158 

_where each_ Σ _k_ (Λ1) _is the subset of_ Λ( _n_ ) _of all Lagrangian subspaces that have k-dimensional intersection with_ Λ1 _. It follows that_ Σ _k_ (Λ1) _is a submanifold of_ Λ( _n_ ) _such that_ dim Λ( _n_ ) = _n_ ( _n_ + 1) _/_ 2 _and_ codim Σ _k_ (Λ1) = _k_ ( _k_ + 1) _/_ 2 _. Then_ _**Maslov cycle (with respect to**_ Λ1 _**)** is the following stratified space_ 

**==> picture [153 x 25] intentionally omitted <==**

Σ(Λ1) _has the structure of a singular algebraic variety of codimension_ 1 _. Here, lower strata are at least of codimension_ 2 _in_ Σ(Λ1) _(specially codimension_ 1 _boundary of_ Σ(Λ1) _is empty)._ 

_Remark_ 361 _._ Let Λ2 be an element of Λ( _n_ ). Pick any Λ1 _∈_ Σ0(Λ2). Since Λ2 and Λ1 are transverse, they can be identified respectively with the _{xi}i_ –plane and the _{yi}i_ –plane in (R[2] _[n] , ω_ 0). Hence any Λ _∈_ Σ0(Λ1) can be uniquely expressed as a graph _{_ ( _a, Sa_ ) _| a ∈{xi}i_ –plane _⊂_ R[2] _[n] }_ for some linear map _S_ : R _[n] →_ R _[n]_ . Since Λ is Lagrangian, we deduce that _S_ is represented by a symmetric matrix. In fact, this gives us a diffeomorphism 

**==> picture [97 x 32] intentionally omitted <==**

where _S_[2] (Λ2) is the vector space of all quadratic forms on Λ2. 

Next, observe that any smooth curve _γ_ ( _t_ ) : ( _−ϵ, ϵ_ ) _→_ Λ( _n_ ), such that _γ_ (0) = Λ2 _,_ can be expressed as _{_ ( _a, S_ ( _t_ ) _a_ ) _| a ∈_ R _[n] }_ . Hence the tangent vector _γ_ _**.**_ (0) = Λˆ︁ 2 _**.**_ can be represented by the quadratic form _⟨·, S_ (0) _·⟩_ . This gives us a vector space isomorphism 

**==> picture [298 x 35] intentionally omitted <==**

This isomorphism is well defined, i.e. _Q_ (Λ2 _,_ Λ[ˆ︁] 2) does not depend on the choice of Λ1, see [RS93, Thm 1.1] . 

**Definition 362.** _Let γ_ : [0 _,_ 1] _→_ Λ( _n_ ) _be a smooth path. Then the number t ∈_ [0 _,_ 1] _is called a_ _**crossing** if γ_ ( _t_ ) _∈_ Σ _k_ (Λ1) _for some k ∈{_ 1 _, . . . , n}. At each crossing t the_ _**crossing form** is defined as_ 

**==> picture [175 x 16] intentionally omitted <==**

_Remark_ 363 _._ For any _k ∈{_ 0 _, . . . , n}_ , we could express the tangent space to Σ _k_ (Λ1) at any point Λ2 _∈_ Σ _k_ (Λ1) as 

**==> picture [338 x 21] intentionally omitted <==**

See [KF19, Lemma 10.2.4]. 

Moreover, any smooth path _γ_ in Λ( _n_ ) is tangent to Σ _k_ (Λ1) at the crossing _t_ if and only if _γ_ ( _t_ ) _∈_ Σ _k_ (Λ1) and Γ( _γ,_ Λ1 _, t_ ) = 0. This motivates the following definition, which can be seen as a certain generalization of transversality. 

**Definition 364.** _A crossing is called_ _**regular** if the corresponding crossing form is non-singular._ 

159 

_Remark_ 365 _._ Observe that Formulae (A.3) and (A.4) allow us to coorient Σ1(Λ1) using the quadratic forms. Hence, if _t_ is a regular crossing for _γ_ ( _t_ ) _∈_ Σ1(Λ1), then the signature of the crossing form is equal to the algebraic intersection number of _γ_ and Σ1(Λ1) at _γ_ ( _t_ ). 

**Definition 366.** _Let γ be a smooth path γ_ : [0 _,_ 1] _→_ Λ( _n_ ) _with only regular crossings. Then the_ _**relative Maslov index of** γ_ _**with respect to**_ Λ1 _is defined as_ 

**==> picture [400 x 29] intentionally omitted <==**

_Remark_ 367 _._ Regular crossings are isolated. Consequently, there is only a finite number of nonzero summands in Formula (A.5), see [RS93, pg. 9]. 

_Remark_ 368 _._ There is a natural extension of the relative Maslov index to all continuous paths in Λ( _n_ ). 

Indeed, every continuous path in Λ( _n_ ) is homotopic with fixed endpoints to some smooth path with only regular crossings, see [RS93, Lemma 2.1]. If any two smooth paths in Λ( _n_ ) have only regular crossings and are smoothly homotopic with fixed endpoints, then they have the same Maslov index, see [RS93, Lemma 2.2]. The rest follows from the Whitney approximation theorem, see [Lee13]. 

**Lemma 369** ([RS93, Thm 2.3 and Rem 2.6]) **.** _The relative Maslov index satisfies the following properties:_ 

_(Naturality) For_ Ψ _∈ Sp_ (2 _n,_ R) _we have_ 

**==> picture [120 x 13] intentionally omitted <==**

_(Concatenation) For a < b < c we have_ 

**==> picture [214 x 13] intentionally omitted <==**

_(Product) If n[′]_ + _n[′′]_ = _n, then_ Λ( _n[′]_ ) _×_ Λ( _n[′′]_ ) _can be seen as a submanifold of_ Λ( _n_ ) _and_ 

**==> picture [222 x 14] intentionally omitted <==**

_(Homotopy) Two paths in_ Λ( _n_ ) _with the same endpoints are homotopic with fixed endpoints if and only if they have the same Maslov index._ 

_(Zero) Let k ∈{_ 1 _, . . . , n}. Then for any path γ in_ Σ _k_ (Λ1) _we have_ 

**==> picture [66 x 13] intentionally omitted <==**

_(Loop) If γ is a loop in_ Λ( _n_ ) _, then_ 

**==> picture [84 x 13] intentionally omitted <==**

_In particular, the relative Maslov index of a loop does not depend on the choice of the Maslov cycle._ 

160 

_Remark_ 370 _._ If _γ_ ( _t_ ), where _t ∈_ [0 _,_ 1], is a path in Λ( _n_ ), then _−γ_ denotes the **opposite path** _γ_ (1 _− t_ ). Thus _γ ∗−γ_ is a contractible loop and consequently _µ_ ( _γ,_ Λ1) = _−µ_ ( _−γ,_ Λ1) for any Λ1 _∈_ Λ( _n_ ). 

_For the simplicity, we will use the following (natural) notation. If_ ( _V, J_ ) _is a complex vector space and V_ = _V_[1] _⊕· · · ⊕ V[k] , then the expression e[J] V[i] means e[J][|][V i] V[i] ._ 

**Definition 371** ([EES05a]) **.** _Let_ Λ1 _,_ Λ2 _∈_ Λ( _n_ ) _and J ∈J_ (R[2] _[n] , ω_ 0) _. Then the_ _**K¨ahler angle** θ_ (Λ1 _,_ Λ2) = ( _θ_ 1 _, . . . , θn_ ) _∈_ [0 _, π_ ) _[n] and orthogonal decomposition R_[2] _[n]_ = _W_[0] _⊕· · · ⊕ W[s] are defined inductively as follows. Take the Hermitian inner product h_ = _gJ_ + _iω_ 0 _._ 

_If_ dim(Λ1 _∩_ Λ2) = _r_ 0 _, then put_ 

**==> picture [274 x 14] intentionally omitted <==**

_Then we define_ Λ[1] _i_[:=][(Λ][1] _[∩]_[Λ][2][)] _[⊥][h][∩]_[Λ] _[i][∈]_[Λ(] _[n][ −][r]_[0][)] _[for][i]_[=][1] _[,]_[ 2] _[.][Next,][if] α_ 1 _∈_ (0 _, π_ ) _is the smallest angle such that_ dim( _e[α]_[1] _[J]_ Λ[1] 1 _[∩]_[Λ][1] 2[) =] _[ r]_[1] _[>]_[ 0] _[,][then][we][set]_ 

**==> picture [351 x 15] intentionally omitted <==**

_Then we define_ Λ[2] 1[:= (] _[e][α]_[1] _[J]_[Λ][1] 1 _[∩]_[Λ][1] 2[)] _[⊥][h][ ∩][e][α]_[1] _[J]_[Λ][1] 1 _[and]_[ Λ][2] 2[:= (] _[e][α]_[1] _[J]_[Λ][1] 1 _[∩]_[Λ][1] 2[)] _[⊥][h][ ∩]_[Λ][1] 2 _[.] Here_ Λ[2] 1 _[,]_[ Λ][2] 2 _[∈]_[Λ(] _[n][ −][r]_[0] _[−][r]_[1][)] _[.][Next,][if][α]_[2] _[∈]_[(0] _[, π]_[)] _[is][the][smallest][angle][such][that]_ dim( _e[α]_[2] _[J]_ Λ[2] 1 _[∩]_[Λ][2] 2[) =] _[ r]_[2] _[>]_[ 0] _[,][then][we][set]_ 

_θr_ 0+ _r_ 1+1 = _· · ·_ = _θr_ 0+ _r_ 1+ _r_ 2 = _α_ 1 + _α_ 2 _and W_[2] = ( _e[α]_[2] _[J]_ Λ[2] 1 _[∩]_[Λ][2] 2[)] _[ ⊕][J]_[(] _[e][α]_[2] _[J]_[Λ][2] 1 _[∩]_[Λ][2] 2[)] _[.]_ 

_Now, we repeat until θn is defined._ 

_Next, using the Hermitian splitting of_ R[2] _[n] we define θ_ (Λ1 _, ,_ Λ2) _J as θr_ 0+ _···_ + _rkJ|W k on W[k] ._ 

_Then by the_ _**positive rotation of**_ Λ1 _**to**_ Λ2 _**by** J we understand the path_ 

**==> picture [196 x 31] intentionally omitted <==**

_Also by the_ _**negative rotation of**_ Λ1 _**to**_ Λ2 _**by** J we understand the path_ 

**==> picture [215 x 32] intentionally omitted <==**

_where θ_ (Λ1 _,_ Λ2) _− π_ := ( _θ_ 1 _− π, . . . , θn − π_ ) _._ 

_Finally, when J is clear from the context, we can emphasize the angle by saying only_ _**rotation of**_ Λ1 _**to**_ Λ2 _**by** θ_ (Λ1 _,_ Λ2) _**or by** θ_ (Λ1 _,_ Λ2) _− π._ 

**Lemma 372.** _Let_ Λ1 _,_ Λ2 _∈_ Λ( _n_ ) _and J ∈J_ (R[2] _[n] , ω_ 0) _. If_ Λ1 ⋔ Λ2 _, then there is α ∈_ (0 _, π_ ) _such that e[αJ]_ Λ1 _∩_ Λ2 = _{_ 0 _}. In particular, K¨ahler angle is well-defined._ 

_Proof._ By the choice of the symplectic basis, we can assume that Λ1 is the _{xi}i_ - plane and _J_ = _J_ 0. If _J_ 0Λ1 _∩_ Λ2 = _{_ 0 _},_ we can put _α_ = _π/_ 2. 

161 

So let us consider the case when _J_ 0Λ1 _∩_ Λ2 = _{_ 0 _}._ Hence, as in the Remark 361, Λ2 is a graph _{_ ( _a, Sa_ ) _| a ∈{xi}i_ -plane and _S_ is a symmetrix matrix _}_ . Moreover 

**==> picture [274 x 82] intentionally omitted <==**

Hence, _e[αJ]_[0] Λ1 _∩_ Λ2 is non-trivial if and only if the system of equations 

**==> picture [80 x 37] intentionally omitted <==**

has a solution for _a, b ∈_ R _[n]_ and _α ∈_ (0 _, π_ ) _\ {π/_ 2 _}_ . This is equivalent to 

**==> picture [242 x 13] intentionally omitted <==**

But _S_ is symmetric, hence has a basis of eigenvectors with real eigenvalues. Thus _α_ exists and we are done. 

**Lemma 373.** _Let_ Λ1 _,_ Λ2 _∈_ Λ( _n_ ) _and J ∈J_ (R[2] _[n] , ω_ 0) _, then rot_ [Λ1 _,_ Λ2; _J,_ +] = _−rot_ [Λ2 _,_ Λ1; _J, −_ ] _._ 

_Proof._ Let us show the lemma in the case when Λ1 ⋔ Λ2 and _J_ 0Λ1 _∩_ Λ2 = _{_ 0 _}_ . Then the general case easily follows. Moreover, similarly as in Lemma 372 we can assume that Λ1 is the _{xi}i_ -plane and _J_ = _J_ 0. And hence analogously Λ2 = _{_ ( _a, Sa_ ) _}_ . 

Now, _e[βJ]_[0] Λ1 _∩_ Λ2, for some _β ∈_ (0 _, π_ ) _\ {π/_ 2 _}_ , is non-trivial if and only if the system of equations 

**==> picture [132 x 36] intentionally omitted <==**

has a solution for _a, b ∈_ R _[n]_ and _β ∈_ (0 _, π_ ) _\ {π/_ 2 _}_ . 

This is equivalent to 

**==> picture [81 x 13] intentionally omitted <==**

and hence to 

**==> picture [253 x 13] intentionally omitted <==**

Now, we compare Formulas (A.6) and (A.7). If we take a _gJ_ 0-orthogonal eigenbasis of _S_ , then eigenvectors generate (as _J_ 0-complex vector spaces) same orthogonal decompositions of R[2] _[n]_ for _θ_ (Λ1 _,_ Λ2) and _θ_ (Λ2 _,_ Λ1). And the lemma follows. 

**Definition 374.** _Let_ Λ1 _,_ Λ2 _∈_ Λ( _n_ ) _. Then_ Σ(Λ1 _,_ Λ2) _denote the set of all_ Λ _∈_ Λ( _n_ ) _such that_ Λ _∩_ Λ1 = Λ2 _∩_ Λ1 _._ 

**Lemma 375.** Σ(Λ1 _,_ Λ2) _is a contractible manifold._ 

162 

_Proof._ Observe that when Λ1 and Λ2 are transverse, then by the Remark 361 Σ(Λ1 _,_ Λ2) is identified with the space of symmetric _n × n_ -matrices and hence is contractible. 

Suppose that Λ1 and Λ2 are not transverse. We take a compatible _J_ and the induced Hermitian inner product _h_ . Since Λ _∩_ Λ1 is fixed for any Σ(Λ1 _,_ Λ2), we will restrict ourselves only to the Hermitian complement (Λ2 _∩_ Λ1) _[⊥][h]_ . Hence, analogously as before, Σ(Λ1 _,_ Λ2) is identified with the space of symmetric ( _n − k_ ) _×_ ( _n − k_ )-matrices, where _k_ = dim(Λ2 _∩_ Λ1), and we are done. 

**Lemma 376** ([CLM94]) **.** _Let_ Λ1 _,_ Λ2 _∈_ Λ( _n_ ) _. If J_ 1 _, J_ 2 _∈J_ (R[2] _[n] , ω_ 0) _, then the paths rot_ [Λ1 _,_ Λ2; _J_ 1 _, ±_ ] _and rot_ [Λ1 _,_ Λ2; _J_ 2 _, ±_ ] _are homotopic with fixed endpoints._ 

_Proof._ Due to Remark 373 we will inspect only the case of positive rotations. First observe that for any _J ∈J_ (R[2] _[n] , ω_ 0) the positive rotation of Λ1 to Λ2 by _J_ stays in Σ(Λ1 _,_ Λ2) for _t ∈_ (0 _,_ 1]. 

Since _J_ ( _R_[2] _[n] , ω_ 0) is contractible, there is a continuous family _{J[s] }s∈_ [1 _,_ 2] such that _J_[1] = _J_ 1 and _J_[2] = _J_ 2. Since by the Gram-Schmidt process the orthogonal complement depends continuously on the inner product, _{J[s] }s_ induces a continuous family of _gJ s_ -orthogonal splittings Λ1 = (Λ1 _∩_ Λ2) _⊕ C[s]_ . In more detail, let us consider the space _{P ∈_ End(Λ1) _| P_[2] = _P, P_ (Λ1) = Λ1 _∩_ Λ2 _}_ . Next, if _PJ_ denotes orthogonal projection induced by _J_ , then _{PJ s}s_ is the continuous family, where ker _PJ s_ = _C[s]_ . 

Hence for _ε >_ 0 _small_ is the map 

**==> picture [247 x 32] intentionally omitted <==**

is continuous, _γ|_ [1 _,_ 2] _×{_ 0 _}_ = Λ1 and _γ|_ [1 _,_ 2] _×_ (0 _,_ 1] _∈_ Σ(Λ1 _,_ Λ2). 

Since Σ(Λ1 _,_ Λ2) is by the Lemma 375 contractible, _any_ pair of paths from _γ_ (1 _,_ 1) and _γ_ (2 _,_ 1) to Λ2 makes together with _γ_ (1 _, t_ ) a contractible loop, see Figure A.1. 

**==> picture [246 x 203] intentionally omitted <==**

Figure A.1: The extension of _γ_ to the homotopy between rot[Λ1 _,_ Λ2; _J_ 1 _,_ +] and rot[Λ1 _,_ Λ2; _J_ 2 _,_ +] 

Hence there is a homotopy with fixed endpoints between rot[Λ1 _,_ Λ2; _J_ 1 _,_ +] and rot[Λ1 _,_ Λ2; _J_ 2 _,_ +]. 

163 

**Lemma 377.** _Let_ Λ1 _,_ Λ2 _∈_ Λ( _n_ ) _and J ∈J_ ( _R_[2] _[n] , ω_ 0) _. Then_ 

**==> picture [311 x 26] intentionally omitted <==**

_where k_ = dim(Λ1 _∩_ Λ2) _._ 

_Proof._ We will prove only that _µ_ (rot [Λ1 _,_ Λ2; _J,_ +] _,_ Λ1)) = ( _n − k_ ) _/_ 2. Then _µ_ (rot[Λ1 _,_ Λ2; _J, −_ ] _,_ Λ2)) = ( _k − n_ ) _/_ 2 can be shown by the analogous computation, and the rest follows from the Remarks 370, 373. 

First, we would like to show that _µ_ (rot[Λ1 _,_ Λ2; _J,_ +] _,_ Λ1)) = ( _n − k_ ) _/_ 2. 

Note that that there is a symplectic basis _{v_ 1 _, . . . , vn, w_ 1 _, . . . , wn}_ such that Λ1 = _{v_ 1 _, . . . , vn}_ and Λ2 = _{vn−k_ +1 _, . . . , vn, w_ 1 _, . . . , wn−k}_ . By the product and naturality properties of the Maslov index we can ignore the part with the constant rotation and consider only Λ1 as the _{xi}i[n]_ =1 _[−][k]_[–plane][and][Λ][2][as][the] _[{][y][i][}][n] i_ =1 _[−][k]_[–plane.] Moreover, by Lemma 376 we can assume that _J_ = _J_ 0. 

Hence we have 

**==> picture [294 x 15] intentionally omitted <==**

Observe that the only crossing appears at _t_ = 0. Next, let _ε >_ 0 small, then for _t ∈_ [0 _,_ 1) we have 

**==> picture [293 x 31] intentionally omitted <==**

Hence, the corresponding crossing form at _t_ = 0 is 

**==> picture [123 x 32] intentionally omitted <==**

and _µ_ (rot[Λ1 _,_ Λ2; _J,_ +] _,_ Λ1)) = ( _n − k_ ) _/_ 2 by Formula (A.5). The case _µ_ (rot _J,_[Λ] _−_[1] _[,]_[Λ][2] _,_ Λ1)) follows from the analoguos computations. In the remaining cases, we may choose a symplectic basis such that Λ2 is the _{xi}i[n]_ =1 _[−][k]_[–plane] (instead of Λ1) and the rest is analogous. 

**Definition 378.** _The_ _**totally real Grassmanian** R_ ( _n_ ) _is the manifold consisting of all totally real subspaces of_ (C _[n] , i_ ) _._ 

_Remark_ 379 _._ Analogously as for Λ( _n_ ) in Lemma 358 we see that _R_ ( _n_ ) has the structure of the homogenuous space. That is 

**==> picture [145 x 13] intentionally omitted <==**

Let us naively inspect the stratification of _R_ ( _n_ ). Let Σ _[real] k_ ( _R_ ) denote the subset of _R_ ( _n_ ) of all totally real subspaces that have _k_ -dimensional intersection with the totally real subspace _R_ . Take Σ _[real]_ 0 ( _i_ R[2] ), then from looking on graphs over R[2] we have 

**==> picture [266 x 15] intentionally omitted <==**

But Mat2 _×_ 2(R) _[∼]_ = R[4] and from the characteristic polynomial we see that the space of _A_ such that _±i ∈_ spectrum( _A_ ) has the dimension equal to 2. Hence Σ _[real]_ 0 ( _i_ R[2] ) is neither contractible nor even only simply connected. 

164 

However, by the Gram-Schmidt process, the natural inclusion Λ( _n_ ) _↪→ R_ ( _n_ ) is a deformation retract. 

Now we define a map 

**==> picture [121 x 48] intentionally omitted <==**

where _A ∈ GL_ ( _n,_ C) and _∗_ denotes conjugate transpose. Observe that _ρ_ is well defined. 

**Definition 380** ([MS12, C.3.]) **.** _Let γ be a continuous loop in R_ ( _n_ ) _. Then the_ _**Maslov index of** γ is defined as_ 

**==> picture [95 x 13] intentionally omitted <==**

_Remark_ 381 _._ [Oh15] Maslov index of a loop in _R_ ( _n_ ) is also well defined on homotopy classes of loops. In particular, when _γ_ is a loop in Λ( _n_ ) _⊂ R_ ( _n_ ), then Definitions 359 and 380 coincide. 

165 

## **B. Maslov index of Reeb chords** 

## **B.1 Vector bundles** 

**Definition 382.** _An_ _**orthogonal vector bundle**_ ( _E → M, g_ ) _is a continuous real vector bundle with an_ _**orthogonal structure** g, that is a continuous assignment of an inner product gx to the fibers Ex, for each x ∈ M ._ 

_Moreover, if F is a subbundle of E, then the subbundle F[⊥] is defined fiberwise as_ 

**==> picture [232 x 14] intentionally omitted <==**

_Remark_ 383 _._ Observe that _F ⊕ F[⊥][∼]_ = _E._ 

**Definition 384.** _A_ _**symplectic vector bundle**_ ( _E → M, ω_ ) _is a continuous real vector bundle with a_ _**symplectic structure** ω, that is a continuous assignment of (linear) symplectic forms ωx to the fibers Ex for each x ∈ M ._ 

_A_ _**Lagrangian subbundle**_ ( _L → M_ ) _is a subbundle of E with fibers consisting of Lagrangian subspaces._ 

_Two symplectic vector bundles_ ( _E_ 1 _→ M_ 1 _, ω_ 1) _and_ ( _E_ 2 _→ M_ 2 _, ω_ 2) _are_ _**isomorphic** , if there is a vector bundle isomorphism ψ_ : _E_ 1 _→ E_ 2 _such that ψ[∗] ω_ 2 = _ω_ 1 _._ 

_Next, two Lagrangian subbundles L_ 1 _⊂ E_ 1 _and L_ 2 _⊂ E_ 2 _are_ _**isomorphic** if there is an isomorphism ψ of symplectic bundles E_ 1 _and E_ 2 _such that ψL_ 1 = _L_ 2 _._ 

_A_ _**complex vector bundle**_ ( _E → M, J_ ) _is a continuous real vector bundle with a_ _**complex structure** J, that is a continuous assignment of linear complex structures Jx to Ex for each x ∈ M ._ 

_Two complex vector bundles_ ( _E_ 1 _→ M_ 1 _, J_ 1) _and_ ( _E_ 2 _→ M_ 2 _, J_ 2) _are_ _**isomorphic** if there is a vector bundle isomorphism ψ_ : _E_ 1 _→ E_ 2 _such that ψ[∗] J_ 2 = _J_ 1 _._ 

_A complex structure J is called_ _**compatible with** ω, if Jx is compatible with ωx on Ex for each x ∈ M . The_ _**Space of all** J_ _**compatible with** ω will be denoted by J_ ( _E, ω_ ) _. Analogously we define the space_ 

**==> picture [289 x 13] intentionally omitted <==**

_A_ _**Hermitian vector bundle**_ ( _E, ω, J_ ) _is a real vector bundle E with a symplectic structure ω and compatible complex structure J. Then a_ _**Hermitian structure** h is the Hermitian inner product on each fibre induced by ω and J._ 

_Remark_ 385 _._ [MS17, ch. 2.6] Note that symplectic vector bundles have local trivializations with fibers (R[2] _[n] , ω_ 0). This is done by a parametric version of the choice of a symplectic basis as in the case ( _V, ω_ ). Then the transition functions are elements of _Sp_ (2 _n,_ R). Conversely, _Sp_ (2 _n,_ R)-vector bundles uniquely determine symplectic vector bundles up to isomorphism. The analogous statement is also true for the complex vector bundles and _GL_ ( _n,_ C)-vector bundles, for Hermitian vector bundles and _U_ ( _n_ )-vector bundles, etc. 

_Remark_ 386 _._ [MS17, ch. 2.6] _J_ ( _E, ω_ ) and Ω( _E, J_ ) are nonempty and contractible. Also, if _R ⊂_ ( _E, J_ ) is a totally real subbundle, then the space of _ω ∈_ Ω( _E, J_ ) such that _J_ is _ω_ -Lagrangian is nonempty and contractible. 

166 

_Remark_ 387 _._ [Hir97] Since we would like to work with various trivializations of pullback bundles, it will be useful to recall the definition of the pullback bundle together with its charts. 

Let ( _E −→π M_ ) be a (real) rank _k_ vector bundle together with the maximal atlas _A_ and let _f_ : _N → M_ be a continuous map between topological spaces _π_ 0 _N, M_ . Then the **pullback bundle** _f[∗] E_ is given as a vector bundle ( _E_ 0 _−→ M_ 0) together with a maximal atlas _A_ 0, where 

**==> picture [193 x 48] intentionally omitted <==**

The maximal atlas _A_ 0 contains all charts ( _φ_ 0 _, U_ 0) that are constructed as follows. If ( _φ, U_ ) _∈A_ and _f[−]_[1] ( _U_ ) is non empty, then _U_ 0 := _f[−]_[1] ( _U_ ) and 

**==> picture [245 x 14] intentionally omitted <==**

The analogous construction also holds for _G_ -vector bundles with any structure group _G_ . 

_Remark_ 388 _._ Let _E → A_ 3 be a _G_ -vector bundle and consider continuous maps _f_ 1 : _A_ 1 _→ A_ 2, _f_ 2 : _A_ 2 _→ A_ 3 and _f_ 3 : _A_ 1 _→ A_ 3 such that _f_ 3 = _f_ 2 _◦ f_ 1. Then 

**==> picture [74 x 13] intentionally omitted <==**

_Remark_ 389 _._ If _E_ 1 and _E_ 2 are two _G_ -vector bundles over _M_ and _f_ is a continuous map _f_ : _N → M_ , then 

**==> picture [165 x 13] intentionally omitted <==**

**Theorem 390** ([BT11, Ste51]) **.** _Let M, N be topological spaces, where N is moreover a topological manifold, and f_ 1 _, f_ 2 _are two continuous maps from N to M . If f_ 1 _and f_ 2 _are homotopic and E → M is a real vector bundle, then the bundles f_ 1 _[∗][E][and][f]_ 2 _[ ∗][E][are][isomorphic.][Moreover,][the][same][statement][also][holds][for][any] G-vector bundles._ 

_Remark_ 391 _._ Based on Theorem 390 we can make the following useful observation. Let _A_ be a manifold that is a deformation retract onto _B_ , where _i_ and _r_ are the corresponding inclusion and retraction, respectively. If _E → A_ is a _G_ -vector bundle then 

**==> picture [217 x 13] intentionally omitted <==**

Hence, any trivialization of _E|B_ (if it exists) induces a trivialization of _E_ that agrees with the first one when restricted to _B_ . 

In particular, vector bundles over contractible manifolds are trivial (take for _B_ a point). Moreover, if the structure group is connected, then all trivializations are homotopic. 

**Definition 392.** _Let_ ( _E → M, ω_ ) _be a symplectic vector bundle and γ be a continuous positively oriented contractible loop γ_ : _S_[1] = _{_ ( _x_ 1 _, x_ 2) _∈_ R[2] _| x_[2] 1[+] _[x]_[2] 2[=] 1 _} → M , where the orientation of S_[1] _is induced from the canonical orientation of_ R[2] _. Let L[γ] be a Lagrangian subbundle of_ ( _γ[∗] E, γ[∗] ω_ ) _. Take some capping disc_ ~~_γ_~~ _of_ 

167 

_γ, that is a continuous map_ ~~_γ_~~ : _D_ = _{_ ( _x_ 1 _, x_ 2) _∈_ R[2] _| x_[2] 1[+] _[ x]_[2] 2 _[≤]_[1] _[} →][M][such][that]_ ~~_γ|_~~ _S_ 1 = _γ. Next, take a symplectic trivialization_ Φ : ~~(~~ ~~_γ[∗]_~~ _E,_ ~~_γ[∗]_~~ _ω_ ) _→_ ( _D ×_ R[2] _[n] , ω_ 0) _. We define the_ _**Maslov index of** L[γ]_ _**with respect to**_ Φ _**and**_ ~~_γ_~~ _as_ 

**==> picture [91 x 13] intentionally omitted <==**

_The Maslov index of L[γ] is_ _**well-defined** if it does not depend on the choice of_ Φ _and_ ~~_γ._~~ 

_Remark_ 393 _._ Definition 392 can be analogously rewritten in the language of complex vector bundles and totally real subbundles. 

_Remark_ 394 _._ First, we would like to discuss the well–definiteness of _µ_ ( _L[γ]_ ) for fixed ~~_γ_ .~~ But, since _D_ is contractible and _Sp_ (2 _n,_ R) is connected, all trivializations Φ are homotopic. Hence, all _µ_ (Φ _L[γ]_ ) are equal. 

Moreover, if _ψ_ : _E → E[′]_ is an isomorphism of symplectic vector bundles over _D_ , then _µ_ ( _L_ ) = _µ_ ( _ψL_ ). Indeed, Φ _ψ[−]_[1] is a symplectic trivialization of _E[′]_ and _µ_ ( _ψL_ ) does not depend on the choice of the trivialization. 

However, to investigate the dependence of the index on different choices of capping discs, we first need to introduce the first Chern number. 

_Remark_ 395 _._ We take a complex vector bundle over the sphere ( _E → S_[2] = _{_ ( _x_ 1 _, x_ 2 _, x_ 3) _∈_ R[3] _| x_[2] 1[+] _[ x]_[2] 2[+] _[ x]_[2] 3[= 1] _[}][, J]_[)][of][real][rank][2] _[n]_[.][Note][that] _[S]_[2][is][a][union] of the upper and the lower hemisphere: _S_[2] = _S_[+] _∪ S[−]_ . Also, the intersection of these hemispheres is a circle _S_[1] , which can be parametrized with respect to the canonical orientation of _S_[2] induced from R[3] in _t ∈_ [0 _,_ 1] as (cos _t,_ sin _t,_ 0). Then we choose _ω ∈J_ ( _E, ω_ ) and obtain a Hermitian bundle ( _E, ω, J_ ). Next, since the hemispheres _S[±]_ are contractible, there are unitary trivializations Φ _[±]_ : ( _E|S±, J_ ) _→ S[±] ×_ (R[2] _[n] , J_ 0). Restricting to _S_[1] = R _/_ Z, we have a continuous family of unitary linear maps Φ _[±] t_[:] _[E]_ [ _t_ ] _[→]_[R][2] _[n][.]_[Hence,][for][any] _[t][∈]_[[0] _[,]_[ 1],][Φ][+] _t_[(Φ] _[−] t_[)] _[−]_[1] _[∈] U_ ( _n_ ). 

**Definition 396.** _The_ _**first Chern number** of the complex vector bundle_ ( _E → S_[2] _, J_ ) _is defined as_ 

**==> picture [163 x 19] intentionally omitted <==**

_for t ∈_ [0 _,_ 1] _parametrizing the circle S_[1] _._ 

det _Remark_ 397 _._ From the fibration _SU_ ( _n_ ) _→ U_ ( _n_ ) _−→ S_[1] and the LES for homotopy groups, we have that the map det _∗_ : _π_ 1( _U_ ( _n_ )) _→ π_ 1( _S_[1] ) is an isomorphism. 

By Remark 386 and contractibility of _S[±]_ we obtain that all choices of _ω,_ Φ[+] and Φ _[−]_ are homotopic. Hence, we have a well-defined _c_ 1 for isomorphism classes of complex vector bundles over _S_[2] . 

If _E_ is trivial, then Φ[+] _t_[(Φ] _[−] t_[)] _[−]_[1][=][ 1][and] _[c]_ 1[vanishes.] 

_Remark_ 398 _._ By Remark 386 we can analoguosly define _c_ 1 for symplectic bundles over _S_[2] . 

_Remark_ 399 _._ Let ( _E → M, ω_ ) be a symplectic bundle and _f_ : _S_[2] _→ M_ an orientation preserving homeomorphism, then we put _c_ 1( _E_ ) := _c_ 1( _f[∗] E_ ). 

_Remark_ 400 _._ Let ( _E → S_[2] _, ω_ ) be a symplectic vector bundle and _L_ be a Lagrangian subbundle of _E|S_ 1. Then the unitary trivializations Φ _[±]_ give rise to the 

168 

loops Φ _[±] t[L]_ [ _t_ ] _[∈]_[Λ(] _[n]_[)][for] _[t]_[parametrizing] _[S]_[1][.][Now][we][would][like][to][investigate] how are the Maslov indices _µ_ (Φ _[±] L_ ) related? 

By the naturality and homotopy property of the Maslov index, we can assume that Φ[+] 0[= Φ] _[−]_ 0[and][Φ] _[−]_ 1 _[L]_ [1][=] _[ {][x][i][}][i]_[–plane][in][R][2] _[n]_[.] Next, observe that for each _t ∈_ [0 _,_ 1] it holds 

**==> picture [299 x 224] intentionally omitted <==**

Hence, we can compute 

where in the third equality, we used the concatenation and homotopy property of the Maslov index. 

Now, we are ready to continue the discussion from Remark 394. 

_Remark_ 401 _._ As in Definition 392 we take a symplectic vector bundle ( _E → M, ω_ ), a loop _γ_ in _M_ and a Lagrangian subbundle _L[γ]_ of _γ[∗] E_ . How does the Maslov index _µ_ ( _L[γ]_ ) depend on the choice of the capping disc? 

Let ~~_γ_[+]~~ , ~~_γ[−]_~~ denote two arbitrarily capping discs. They are continuous maps ~~_γ[±]_~~ : _D → M_ such that ~~_γ_~~[+] (cos _t,_ sin _t_ ) = ~~_γ[−]_~~ (cos _t,_ sin _t_ ) = _γ_ (cos _t,_ sin _t_ ) for each _t ∈_ [0 _,_ 1] (again, here we used parametrizations with respect to the canonical orientation of _D_ ). 

Next, since ~~_γ_[+]~~ and ~~_γ[−]_~~ agree on _∂D_ = _S_[1] , by the Pasting lemma, there exists the following gluing along _S_[1] . We introduce a continuous function 

**==> picture [194 x 13] intentionally omitted <==**

where ( ~~_γ[−]_~~ ) _[op]_ denotes capping disc ~~_γ[−]_~~ with opposite orientation. Clearly, there is a canonical orientation-preserving homeomorphism between _D ∪S_ 1 _D[op]_ and _S_[2] . Hence, by Remark 399 we get to the situation as in Remark 400. Hence, we obtain the following corollary. 

**Corollary 402.** _Let_ ( _E → M, ω_ ) _be a symplectic vector bundle, γ be a contractible loop in M and L[γ] be a Lagrangian subbundle of_ ( _γ[∗] E, γ[∗] ω_ ) _. If for any two capping discs γ[±] it holds that c_ 1( _**γ**[∗] E_ ) = 0 _, then the Maslov index µ_ ( _L[γ]_ ) _does not depend on the choice of the capping disc and is well-defined._ 

_Remark_ 403 _._ If _E_ 1 and _E_ 2 are two symplectic vector bundles over _S_[2] , then a straightforward computation shows that for the Whitney sum _E_ 1 _⊕ E_ 2 it holds that _c_ 1( _E_ 1 _⊕ E_ 2) = _c_ 1( _E_ 1) + _c_ 1( _E_ 2) (see for example [KF19]). 

169 

## **B.2 Basics of symplectic and contact manifolds** 

**Definition 404.** _The pair_ ( _M, ω_ ) _is called a_ _**symplectic manifold** , if ω is a_ _**symplectic form** on the smooth manifold M , that is a closed nondegenerate_ 2 _–form on M ._ 

**Definition 405.** _The_ _**Liouville form** λ on the symplectic manifold_ ( _M, ω_ ) _is a one form λ such that ω_ = _dλ. The_ _**Liouville vector field** X_ _**associated to** λ is the unique solution of the equation iXω_ = _λ._ 

**Definition 406.** _Two symplectic manifolds_ ( _M_ 1 _, ω_ 1) _and_ ( _M_ 2 _, ω_ 2) _are caled_ _**symplectomorphic** , if there is a diffeomorphism ψ_ : _M_ 1 _→ M_ 2 _such that ψ[∗] ω_ 2 = _ω_ 1 _. Here ψ is called a_ _**symplectomophism** ._ 

_Moreover, let λ_ 1 _and λ_ 2 _are Liouville forms on M_ 1 _and M_ 2 _, respectively. If ψ[∗] λ_ 2 = _λ_ 1 _, then ψ is called a_ _**Liouville diffeomorphism** ._ 

**Darboux’s Theorem 407** ([MS17]) **.** _Let_ ( _M_ 1 _, ω_ 1) _and_ ( _M_ 2 _, ω_ 2) _be two symplectic manifolds. If x_ 1 _and x_ 2 _are two points in M_ 1 _and M_ 2 _respectively, then there exist two neighbourhoods U_ 1 _and U_ 2 _of these points in M_ 1 _and M_ 2 _respectively such that_ ( _U_ 1 _, ω_ 1 _|U_ 1) _is symplectomorphic to_ ( _U_ 2 _, ω_ 2 _|U_ 2) _. In other words, all symplectic manifolds of the same dimension are locally symplectomorphic._ 

**Definition 408.** _Let H be a smooth function on the symplectic manifold_ ( _M, ω_ ) _. Then the_ _**Hamiltonian vector field** XH_ _**associated to** H is the unique solution of ω_ ( _XH, ·_ ) = _−dH. The induced flow of XH is called a_ _**Hamiltonian flow asociated to** H and denoted by ϕ[t] H[.]_ 

**Lemma 409.** _{ϕ[t] H[}][t][is][a][smooth][family][of][symplectomorphisms.]_ 

_Proof._ We would like to show that _dtd_[(] _[ϕ] H[t]_[)] _[∗][ω]_[= 0.][Then][it][follows][that][(] _[ϕ][t] H_[)] _[∗][ω]_[=] ( _ϕ_[0] _H_[)] _[∗][ω]_[=] _[ ω]_[.] 

We compute 

**==> picture [204 x 65] intentionally omitted <==**

where in the second equality we used Cartan´s magic formula. 

**Definition 410.** _Let_ ( _M, ω_ ) _be a_ 2 _n-dimensional symplectic manifold. Then its submanifold L is called_ _**Lagrangian** if_ dim _L_ = _n and ω|TL_ = 0 _._ 

**Definition 411.** _Let_ ( _M, ω_ ) _be a symplectic manifold with two Lagrangian submanifolds L_ 1 _, L_ 2 _. We say that L_ 1 _**and** L_ 2 _**intersect cleanly along a submanifold** K if L_ 1 _∩ L_ 2 = _K and TxK_ = _TxL_ 1 _∩ TxL_ 2 _for each x ∈ K._ 

**Definition 412.** _Let M be a smooth_ (2 _n_ +1) _–dimensional manifold. The_ _**contact form** α is a_ 1 _–form on M such that_ 

**==> picture [75 x 13] intentionally omitted <==**

_A hyperlane field ξ on M is called a_ _**contact structure** , if for every point x ∈ M there is a neighborhood Ux ⊆ M and a contact form α defined on Ux such that ξ|Ux_ = ker _α ⊆ TUx._ 

_The pair_ ( _M, ξ_ ) _is called a_ _**contact manifold** ._ 

170 

**Lemma 413** ([Han08]) **.** _A contact structure ξ is a kernel of some global contact form if and only if ξ is coorientable._ 

_If the contact form ξ is a kernel of some contact form α, then any nonvanishing function f defines a contact form fα with ξ_ = ker _fα. Moreover,_ ( _ξ, dα|ξ_ ) _is a symplectic vector bundle._ 

_In the view of Lemma 413, we will be studying only coorientable contact structures. Hence, we can write_ ( _M, α_ ) _as a contact manifold._ 

**Definition 414.** _Two contact manifolds_ ( _M_ 1 _, ξ_ 1 = ker _α_ 1) _and_ ( _M_ 2 _, ξ_ 2 = ker _α_ 2) _are called_ _**contactomorphic** , if there is a diffeomorphism ψ_ : _N_ 1 _→ N_ 2 _such that ψ∗_ ( _ξ_ 1) = _ξ_ 2 _. Here ψ is called a_ _**contactomorphism** ._ 

_Equivalently, we say that the diffeomorphism ψ is a_ _**contactomorphism** , if ψ[∗] α_ 2 = _fα_ 1 _for some nonvanishing function f on M_ 1 _._ 

_Moreover, if f_ = 1 _, then ψ is called a_ _**strict contactomorphism** ._ 

**Pfaff’s Theorem 415** ([Han08]) **.** _All contact manifolds of the same dimension are locally strictly contactomorphic._ 

**Definition 416.** _Let_ ( _M, α_ ) _be a contact manifold. Then the_ _**Reeb vector field** R_ _**asociated to** α is the unique solution of:_ 

_(i.) iRα_ = 1 _,_ 

_(ii.) iRdα_ = 0 _._ 

_The induced flow of R is called the_ _**Reeb flow** and denoted by ϕ[t] R[.]_ 

**Lemma 417.** _{ϕ[t] R[}][t][is][a][smooth][family][of][contactomorphisms.]_ 

_Proof._ The proof is analogous to the proof of the Lemma 409. Only here we have 

**==> picture [170 x 27] intentionally omitted <==**

**Definition 418.** _Let_ ( _M, α_ ) _be a_ (2 _n_ + 1) _-dimensional contact manifold. Then its submanifold L is called_ _**Legendrian** if_ dim _L_ = _n and α|T L_ = 0 _._ 

_Two Legendrian submanifolds are called_ _**Legendrian isotopic** if there is a smooth ambient isotopy between them through Legendrian submanifolds._ 

**Definition 419.** _Let_ ( _M, α_ ) _be a contact manifold with a Legendrian submanifold L. A curve γR_ : [0 _, T_ ] _→ M is called a_ _**Reeb chord on** L if it has endpoints on L and it is an integral of the Reeb flow ϕ[t] R[.]_ 

_Next, γR is called_ _**pure** if its endpoints lie on the same connected component of the Legendrian submanifold L. Otherwise γR is called_ _**mixed (from** L_ 0 _**to** L_ 1 _**)** , here L_ 0 _, L_ 1 _are two different connected components of L such that γR_ (0) _∈L_ 0 _, γR_ ( _T_ ) _∈L_ 1 _._ 

_Moreover, γR is called_ _**nondegenerate** if TγR_ ( _T_ ) _L_ ⋔ _dϕ[T] R[T][γ] R_[(0)] _[L][in][ξ][γ] R_[(] _[T]_[)] _[.]_ 

_Remark_ 420 _._ Let _γR_ be a pure Reeb chord on _L_ . Then there is a continuous (positively oriented) loop _γ_ : _S_[1] _→ M_ , parametrized by _t ∈_ R _/_ Z = _S_[1] , that satisfies the following: 

171 

- ( _i._ ) if _t ∈_ [0 _,_ 1 _/_ 3] _,_ then _γ_ ( _t_ ) = _c_ (3 _t_ ), where _c_ is a continuous “capping” path _c_ : [0 _,_ 1] _→L_ with _c_ (0) = _γR_ ( _T_ ) and _c_ (1) = _γR_ (0), 

- ( _ii._ ) if _t ∈_ [1 _/_ 3 _,_ 2 _/_ 3] _,_ then _γ_ ( _t_ ) = _γR_ (3 _Tt − T_ ), 

- ( _iii._ ) if _t ∈_ [2 _/_ 3 _,_ 1] _,_ then _γ_ ( _t_ ) = _γR_ ( _T_ ). 

We take the pullback bundle ( _γ[∗] ξ, γ[∗]_ ( _dα|ξ_ )). Next, we define its Lagrangian subbundle _L[γ]_ as follows (see also Figure B.1): 

- ( _i._ ) for _t ∈_ [0 _,_ 1 _/_ 3] we put _L[γ]_ [ _t_ ][:=] _[ T][γ]_[(] _[t]_[)] _[L]_ 

- ( _ii._ ) for _t ∈_ (1 _/_ 3 _,_ 2 _/_ 3] we put _L[γ]_ [ _t_ ][:=] _[ dϕ] R_[(3] _[Tt][−][T]_[)] _TγR_ (0) _L_ 

**==> picture [412 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
( iii. ) for t ∈ (2 / 3 ,  1) we put L [γ] [ t ] [:=] [rot[] [dϕ][T] R [T][γ] R [(0)] [L][, T][γ] R [(] [T] [)] [L] [;] [ J,] [ +](3] [t][ −] [2),] [where]<br>J is a complex structure in J  ( ξγR ( T ) , dα|ξγR ( T  )).<br>L<br>γ γR<br>c<br>Figure B.1: The Lagrangian subbundle L [γ] of γ [ξ] (in blue) and some capping disc<br>γ of γ (in grey).<br>**----- End of picture text -----**<br>


**Definition 421.** _Let γR and L[γ] are as in Remark 420. Then the_ _**Maslov index (or degree) of the pure Reeb chord** γR is defined as_ 

**==> picture [89 x 13] intentionally omitted <==**

_We say that |γR| is_ _**well-defined** , if µ_ ( _L[γ]_ ) _is well-defined in the sense of Definition 392 and moreover µ_ ( _L[γ]_ ) _does not depend on the choices of the capping path c and the complex structure J._ 

_Remark_ 422 _._ From Lemma 376 we obtain that the Maslov index of a pure Reeb chord does not depend on _J_ . 

172 

## **B.3 On cotangent bundles** 

_Example_ 423 _._ A classical example of the symplectic manifold is a **cotangent** _π i_ **bundle** ( _T[∗] N −→ N_ ). To see this, we introduce first a local coordinates ( _q ◦π, pi_ ) _i_ on _T[∗] U ⊂ T[∗] N_ . Let ( _q[i]_ ) _i_ be local coordinates on an open neighborhood _U ⊂ N_ . Then ( _pi_ ) _i_ are defined as follows. If _x ∈ T[∗] U_ , then _{dq[i] |q}i_ form a basis of _Tq[∗][N]_[for] _q_ = _π_ ( _x_ ). Therefore there are unique functions _pi_ : _x ↦→ x_ ( _∂qi|q_ ). For simplicity, we will write _q[i]_ := _q[i] ◦ π_ . Also, we will denote points of _T[∗] N_ as _x_ = ( _q, p_ ). 

Then we will define on _T[∗] N_ a 1-form _λ_ . For each _x ∈ T[∗] N_ , the linear map _λx_ : _TxT[∗] N →_ R is given by _λx_ := _x◦dπ_ . It will be useful to have a description of _λ_ in local coordinates. Since _dπ_ ( _x_ ) _∂qi|x_ = _∂qi|q_ and _dπ_ ( _x_ ) _∂pi|x_ = 0, we conclude that _λ_ =[∑︁] _i[p] i[dq][i]_[.] 

Now, we put _ω_ = _dλ_ , which can be locally written as _ω_ =[∑︁] _i[dp] i[∧][dq][i]_[.][Since] _ω_ is closed and nondegenerate, it is a symplectic form and _λ_ is a Liouville form on _T[∗] N_ . 

_Remark_ 424 _._ Since the cotangent bundle _T[∗] N_ has the global Liouville form _λ_ , we can introduce a global Liouville vector field _X_ , which is locally given by _X_ =[∑︁] _i[p] i[∂] pi_[.] 

Let _g_ be a Riemannian metric on _N_ . Then we define a function _H_ on _T[∗] N_ as 

**==> picture [260 x 16] intentionally omitted <==**

The corresponding Hamiltonian vector field can be expressed as follows. Let _x ∈ T[∗] N_ , then we take a normal coordinates ( _q[i]_ ) _i_ centered at _q_ and induced coordinates ( _pi_ ) _i_ . Then ( _XH_ ) _x_ =[∑︁] _i[p] i_[(] _[x]_[)] _[∂] q[i][|] x_[.] 

_The only Hamiltonian function on T[∗] N we will consider is the function (B.1)._ 

**Definition 425.** _Let Q be a submanifold without boundary in N . Then the_ _**conormal bundle of** Q is defined as_ 

**==> picture [311 x 14] intentionally omitted <==**

_Remark_ 426 _._ Since _TL[∗] Q_ is subbundle of _TT[∗] N |L∗Q_ and _π_ ( _T[∗] N |Q_ ) = _Q_ , we have a projection along fibers _dπ_ ( _TL[∗] Q_ ) = _TQ_ . Hence, on _TL[∗] Q_ vanish the Liouville form _λ_ . Since also dim _L[∗] Q_ = dim _T[∗] N/_ 2, _L[∗] Q_ is a Lagrangian submanifold of _T[∗] N_ . 

**Definition 427.** _The_ _**unit cotangent bundle** on_ ( _N, g_ ) _is defined as_ 

**==> picture [167 x 15] intentionally omitted <==**

_Moreover, let Q be a submanifold without boundary in N . Then the_ _**unit conormal bundle of** Q is defined as_ 

**==> picture [104 x 12] intentionally omitted <==**

_Remark_ 428 _._ Note that _S[∗] N ⊆ T[∗] N_ is a contact manifold with a contact structure _ξ_ = ker _λ_ 1, where _λ_ 1 := _λ|S∗N_ . Indeed, by coordinate description of _X_ , we see that _X_ is transverse to _S[∗] N_ . Hence _λ_ 1 _∧_ ( _dλ_ 1) _[n][−]_[1] = (1 _/n_ ) _iX_ ( _dλ_ ) _[n]_ = 0 on _S[∗] N_ , where _n_ = dim _N_ . 

173 

At each point _x ∈ S[∗] N_ , we take a coordinate description of _XH_ as in Remark 424. Observe that _XH|x_ satisfies equations for the Reeb vector field on _S[∗] N_ . And hence _XH|S∗N_ = _R_ . 

Thus, we conclude the following. Let _ϕ[t] H_[and] _[ϕ][t] R_[be][Hamiltonian][and][Reeb] flows on _T[∗] N_ and _S[∗] N_ respectively. Then 

**==> picture [241 x 14] intentionally omitted <==**

and hence there is a bijection between integral curves of the Hamiltonian flow _ϕ[t] H_ on _S[∗] N ⊂ T[∗] N_ and integral curves of the Reeb flow _ϕ[t] R_[.][These][curves][are][called] **corresponding** . 

_Remark_ 429 _._ From the coordinate descriptions of _R_ and _X_ we deduce the following. At each point _x_ of _S[∗] N_ and any submanifold _L[∗] Q_ of _T[∗] N_ , we have two splittings: 

**==> picture [143 x 30] intentionally omitted <==**

By the Lemma 413, ( _ξ, ω|ξ_ ) is a symplectic vector bundle. By looking on coordinates, we see that _Xx_ and _Rx_ form a symplectic basis of ( _ηx_ := _⟨Xx⟩×⟨Rx⟩, ω|ηx_ ). This extends to the symplectic vector bundle ( _η, ω|η_ ). 

Also _⟨Xx⟩, ⟨Rx⟩_ and _TxL[∗] Q_ are Lagrangian subspaces when restricted to _ηx_ and _ξx_ , respectively. And analogously these subspaces extend to the Lagrangian subbundles _⟨X⟩, ⟨R⟩_ and _T L[∗] Q_ of _η_ and _ξ_ respectively. 

_Remark_ 430 _._ Let _x, y ∈ S[∗] N_ such that _y_ = _ϕ[t] H_[(] _[x]_[)][for][some] _[t][∈]_[R][.][Then][by] Formula (B.2) we have _dϕ[t] H_[(] _[x]_[)] _[R][x]_[=] _[ R][y]_[and] _[dϕ][t] H_[(] _[x]_[)] _[ξ][x]_[=] _[ ξ][y]_[.] 

Moreover 

**==> picture [265 x 15] intentionally omitted <==**

This is immediate when _N_ = R _[n]_ , since then _ϕ[t] H_[(] _[q, p]_[) = (] _[q]_[ +] _[ tp, p]_[).][In the general] case, it is convenient to do the computation in the symplectization R _× S[∗] N_ , see also the computation in Remark 295 which works for any _N_ . 

_Remark_ 431 _._ [Han08] As a contact manifold, _S[∗] N_ can be identified with the space of cooriented contact elements of _N_ , which has a natural contact structure. In particular, different choices of _g_ on _N_ give us contactomorphic _S[∗] N_ . 

_Example_ 432 _. T[∗] S[n][−]_[1] _×_ R is a contact manifold with a contact form _dt − λ|S∗Sn−_ 1 _,_ where _t_ denotes R-direction and R _[n]_ is equipped with the standard inner product _⟨·, ·⟩_ . 

Then _T[∗] S[n][−]_[1] can be writen as 

**==> picture [247 x 14] intentionally omitted <==**

Now, we can define a map 

**==> picture [171 x 32] intentionally omitted <==**

where ( _q, p_ ) is written with respect to the standard coordinates on _T[∗]_ R _[n]_ . Here _q −⟨q, p⟩p_ is an orthogonal projection of the vector _qp_ to _Tp[∗][S][n][−]_[1][.] _[⟨][q, p][⟩]_[is][then] an orthogonal projection of _qp_ to _Np[∗][S][n][−]_[1][.] 

It follows that _ψ[∗]_ ( _dt − λ|S∗Sn−_ 1) = _λ|S∗_ R _n,_ hence it is a (strict) contactomorphism. 

174 

_Remark_ 433 _._ [Fer17] By the construction, a smooth ambient isotopy between two submanifolds _Q_ 1 _, Q_ 2 _∈ N_ induces a Legendrian isotopy between _L[∗] Q_ 1 _, L[∗] Q_ 2 _∈ S[∗] N._ 

_Remark_ 434 _._ [Fer17] Let _N_ be oriented manifold and _Q_ be a codim 1 oriented connected submanifold of _N_ . Then _L[∗] Q_ has two connected components _L[∗]_ + _[Q]_ and _L[∗] −[Q]_[.][Both][are][diffeomorphic][to] _[Q]_[.][Here] _[L][∗]_ + _[Q]_[is][determined][by][the][positive] co-orientation of _Q_ . 

Naturally, _L[∗]_ + _[Q]_[ and] _[ L] −[∗][Q]_[ will be two Lagrangian submanifolds with boundary] _Q_ such that _L[∗] ±[Q][ ⊂][L][∗] ±[Q]_[and] _[L][∗]_ + _[Q][ ∪][Q][L] −[∗][Q]_[ =] _[ L][∗][Q.]_ 

## **B.4 Binormal and Hamiltonian chords** 

In this section, we would like to describe relations between binormal and Hamiltonian chords. We begin with the discussion of the Morse index of binormal chords. Then we describe the splitting of _TT[∗] N_ into the horizontal and vertical parts. The section will be finished by introducing the Maslov index for Hamiltonian chords. 

**Lemma 435.** _Let Q be a submanifold of_ ( _N, g_ ) _and T >_ 0 _. Then the set_ 

**==> picture [315 x 14] intentionally omitted <==**

_is a smooth Hilbert manifold and at γ ∈H_[1] ([0 _, T_ ] _, N_ ; _Q_ ) _the tangent space is_ 

_TγH_[1] ([0 _, T_ ] _, N_ ; _Q_ ) = _{v ∈H_[1] ([0 _, T_ ] _, γ[∗] TN_ ) _|_ ( _v_ (0) _, v_ ( _T_ )) _∈ T_ ( _γ_ (0) _,γ_ ( _T_ ))( _Q × Q_ ) _}._ 

_Sketch proof._ For details [Kli95] or in more general setting [El´ı67]. Let dim _N_ = _n_ and dim _Q_ = _k_ . 

First, recall the following general fact. If _f_ : _U ⊂_ R _[n] → U[′] ⊂_ R _[n]_ is a diffeomorphism and _γ_ : [0 _, T_ ] _→_ R _[n]_ is of class _H_[1] , then _f ◦ γ_ : [0 _, T_ ] _→ U[′]_ is also of class _H_[1] . 

Let us pick a curve _γ ∈H_[1] ([0 _, T_ ] _, N_ ; _Q_ ). We would like to construct a chart around _γ_ . First, we take a trivialization Φ : _γ[∗] TN →_ [0 _, T_ ] _×_ R _[n]_ such that Φ( _Tγ_ (0) _Q_ ) = Φ( _Tγ_ ( _T_ ) _Q_ ) = R _[k]_ . 

Now, we pick an auxiliary Riemannian metric _g_ ˜︁ on _N_ . For the simplification, _g_ ˜︁ will have the property that some _neighbourhoods_ of _γ_ (0) and _γ_ ( _T_ ) in _Q_ are totally geodesic in _N_ . Observe that such a _g_ ˜︁ always exists. Indeed, first we pick a chart on _N_ around _u_ (0) that maps _Q_ to some vector space. Then the pullback of the Euclidean metric is locally our desired _g_ ˜︁. Next, we make the same for _u_ ( _T_ ). Finally, outside some small neighbourhoods of _γ_ (0) and _γ_ ( _T_ ) in _N_ we interpolate the pullback metric with any Riemannian metric on _N_ , and hence we obtain _g_ ˜︁ on the whole _N_ . 

Let _V ⊂ γ[∗] TN_ be a neighbourhood of the zero section such that the map exp[˜︁] _[g]_ : _Tγ_ ( _t_ ) _N ⊂ V → N_ is a diffeomorphism onto its image for each _t ∈_ [0 _, T_ ]. Now we put 

**==> picture [315 x 33] intentionally omitted <==**

175 

Observe that _Uγ_ is an open subset in 

**==> picture [204 x 15] intentionally omitted <==**

The latter is a closed subspace of _H_[1] ([0 _, T_ ] _,_ R _[n]_ ) and hence also a Hilbert space. Now the charts 

**==> picture [143 x 35] intentionally omitted <==**

define a smooth atlas on _H_[1] ([0 _, T_ ] _, N_ ; _Q_ ). Moreover, the induced structure does not depend on _g_ ˜︁. 

**Definition 436.** _We define the_ _**energy functional E** on H_ 1([0 _, T_ ] _, N_ ; _Q_ ) _as_ 

**==> picture [113 x 26] intentionally omitted <==**

**Definition 437.** _A (non-constant) curve γM_ : [0 _, T_ ] _→_ ( _N, g_ ) _is called a_ _**binormal chord on** Q if it is a geodesic with endpoints at Q and at these endpoints γM is perpendicular to Q._ 

_Remark_ 438 _._ [Kli95] _**E**_ is well defined. That is, _**E**_ does not depend on the choice of charts on _H_ 1. Moreover, _**E**_ is smooth. 

_Remark_ 439 _._ [Kli95] Critical points of _**E**_ are precisely the binormal chords and constant paths on _Q_ . 

**Definition 440.** _If γM ∈H_[1] ([0 _, T_ ] _, N_ ; _Q_ ) _is a critical point of_ _**E** , then the_ _**Morse index of** γM is defined as_ 

_IndγM_ := sup _{_ dim _V | V linear subspace of TγM H_[1] ([0 _, T_ ] _, N_ ; _Q_ ) _on which_ 

_the symmetric bilinear form D_[2] _E_ ( _γM_ ) _is negative definite}._ 

_Moreover, γM is called_ _**nondegenerate** if_ 

**==> picture [312 x 31] intentionally omitted <==**

**Morse Index Theorem 441** ([Amb61, Kli95, Bol77]) **.** _Let γM ∈H_[1] ([0 _, T_ ] _, N_ ; _Q_ ) _be a binormal chord. Then_ 

_IndγM_ = _index_ ( _H_ 0 _− HT_ ) + ∑︂ _{multiplicity of the conjugate point γM_ ( _t_ ) _},_ 0 _<t<T_ 

_where H_ 0 _, HT are the second fundamental forms of Q at γM_ (0) _, γM_ ( _T_ ) _, respectively, in directions of the normal vectors γ_ ̇ _M_ (0) _, γ_ ̇ _M_ ( _T_ ) _, respectively. For definitions of the second fundamental form and the multiplicity of a conjugate point, see [Kli95]._ 

**Definition 442.** _A curve γH_ : [0 _, T_ ] _→ T[∗] N is called a_ _**Hamiltonian chord on** L[∗] Q if it has endpoints at L[∗] Q and it is an integral curve of the Hamiltonian flow ϕ[t] H[.]_ 

_Moreover, a Hamiltonian chord γH is called_ _**nondegenerate** if TγH_ ( _T_ ) _L[∗] Q_ ⋔ _dϕ[T] H[T][γ] H_[(0)] _[L][∗][Q][in][T][γ] H_[(] _[T]_[)] _[T][ ∗][N][.]_ 

176 

**Lemma 443** ([KF19, Thm 2.3.1]) **.** _If γM_ ( _t_ ) _is a binormal chord on Q, then the map t ↦→_ ( _γM_ ( _t_ ) _, γ_ ̇ _M_ ( _t_ ) _[♭]_ ) _∈ T[∗] N defines a Hamiltonian chord γH_ ( _t_ ) _on L[∗] Q. Moreover, such an assignment defines a bijection between the sets of binormal chords on Q and Hamiltonian chords on L[∗] Q. These chords are called_ _**corresponding** ._ 

_Remark_ 444 _._ For details see [Spi, Apx 3]. Let ( _E −→π N_ ) be a vector bundle. _dπ_ Applying the tangent functor _T_ , we get a vector bundle ( _TE −→ TN_ ). 

The **Vertical subbundle** is the subbundle of _TE_ defined as _T[v] E_ := ker _dπ_ . For any _q ∈ N_ and _x ∈ Eq_ we define a map _Ix[v]_[as] 

**==> picture [135 x 44] intentionally omitted <==**

Observe that _Ix[v]_[is][a][vector][space][isomorphism][onto][its][image,][which][is] _[T] x[ v][E]_[.] Hence, we obtain a vector bundle isomorphism _I[v]_ : _π[∗]_ ( _E_ ) _→ T[v] E_ . 

A **Horizontal subbundle** is a choice of a subbundle _T[h] E_ of _TE_ such that _TE_ = _T[v] E ⊕ T[h] E_ . Take a Koszul connection _∇_ : Γ( _E_ ) _→_ Γ( _T[∗] N ⊗ E_ ). Then for any _q ∈ N, x ∈ Eq_ we define a map 

**==> picture [165 x 32] intentionally omitted <==**

where _s_ is a section _s_ : _N → E_ such that _s_ ( _q_ ) = _x_ and the map _Ix[h]_[does] not depend on the choice of _s_ . This leads to the vector bundle monomorphism _I[h]_ : _π[∗]_ ( _TN_ ) _→ TE_ , where the image of _I[h]_ is a horizontal subbundle. Moreover, every horizontal subbundle _T[h] E_ is determined by the unique Kozsul connection on _E_ . 

Hence, we obtain a vector bundle isomorphism _I_ = _I[h] × I[v]_ : _π[∗]_ ( _TN ⊕ E_ ) _→ TE_ . 

By _P_ = _P[h] × P[v]_ : _TE → π[∗]_ ( _TN ⊕ E_ ) we will denote the inverse map to _I_ . 

_Remark_ 445 _._ In our special case we have a vector bundle ( _E → N_ ) = ( _T[∗] N → N_ ) with a symplectic form _ω_ . Let _g_ be a Riemannian metric on _N_ . Fix a point _x_ = ( _q, p_ ) _∈ T[∗] N_ . Now, we take a normal coordinates ( _q[i]_ ) _i_ centered at _q_ and induced coordinates ( _pi_ ) _i_ . Then _{∂qi|x, −∂pi|x}i_ is a symplectic basis of ( _TxT[∗] N, ωx_ ). Next, _gq_ induce dual pairing on _TqN × Tq[∗][N]_[.][As][in][Example][344,] this give us a symplectic form ( _ω×_ ) _q_ on _TqN × Tq[∗][N]_[with][a][symplectic][basis] _{∂qi|q, −dq[i] |q}i_ . 

Moreover, _gq_ induce on ( _TqN × Tq[∗][N,]_[ (] _[ω][×]_[)] _[q]_[)][a][Hermitian][structure,][where][the] compatible complex structure ( _J[g]_ ) _q_ and the inner product ( _g[D]_ ) _q_ are 

**==> picture [317 x 31] intentionally omitted <==**

Here ( _ω×_ ) _q_ = ( _g[D]_ ) _q_ (( _J[g]_ ) _q·, ·_ ). 

We would like to describe _Ix_ with respect to the bases above. For this, we choose _∇_ as the dual connection to the Levi-Civita connection on ( _N, g_ ). For 

177 

_s_ : _N → T[∗] N_ we take a local section such that _s_ ( _q_ ˜︁) =[∑︁] _i[p] i_[(] _[x]_[)] _[dq][i][|] q_[.][Note][that] ˜︁ _s_ ( _q_ ) = _x_ and ( _∇s_ )( _q_ ) = 0. Then we obtain linear maps 

**==> picture [346 x 47] intentionally omitted <==**

Hence, _Ix_ = _Ix[h][×][ I] x[v]_[:] _[ T][q][N][×][ T] q[ ∗][N][→][T][x][T][ ∗][N]_[is][a][linear][symplectomorphism.] It follows that the map _I_ : _π[∗]_ ( _TN ⊕ T[∗] N_ ) _−→ TT[∗] N_ is an isomorphism of symplectic vector bundles. Moreover, the pullbacks _P[∗]_ ( _J[g]_ ) and _P[∗]_ ( _g[D]_ ) induce a Hermitian structure on _TT[∗] N_ . 

_Remark_ 446 _._ Observe that _P_ “splits” _X_ and _R_ at each point _x_ = ( _p, q_ ) _∈ S[∗] N_ . Indeed, by the formulas (B.5) we have 

**==> picture [179 x 34] intentionally omitted <==**

**Definition 447.** _Let V be a linear subspace of_ R _[n] . Then the_ _**conormal space of** V is defined as_ 

_L[∗] V_ := _V ×_ ( _V[⊥]_ ) _[∗]_ = _{_ ( _a, b_ ) _∈_ R[2] _[n]_ = R _[n] ×_ (R _[n]_ ) _[∗] | a ∈ V, b_ ( _v_ ) = 0 _for all v ∈ V }._ 

_Remark_ 448 _._ Observe that if we restrict _TxL[∗] Q_ to horizontal and vertical subspaces of _TxT[∗] N_ then we get 

**==> picture [231 x 16] intentionally omitted <==**

Indeed, since _P[h]_ = _dπ_ , the first mapping was already described in Remark 426. Because _Px[h]_[:] _[T][ h] x[L][∗][Q][→][T][q][Q]_[is][an][isomorphism,][we][get][that][dim] _[ T] x[ v][L][∗][Q]_[=] _n −_ dim _Q_ = dim _L[∗] q[Q]_[.][Since] _[P] x[ v]_[:] _[T][ v] x[T][ ∗][N][→][T][ ∗] q[N]_[is][an][isomorphism][with][an] inverse _Ix[v]_[,][it][is][enough][to][show][that] _[I] x[v]_[maps][every][element][of] _[L][∗] q[Q]_[to] _[T] x[ v][L][∗][Q]_[.] But, by the definition of _Ix[v]_[,] _[I] x[v]_[(] _[L][∗] q[Q]_[)][are][elements][of] _[T][x][L][∗][Q]_[that][are][in][ker] _[ dπ]_[,] which is _Tx[v][L][∗][Q]_[.] 

_Remark_ 449 _._ We would like to define the Maslov index of a Hamiltonian chord _γH_ on _L[∗] Q ⊂ T[∗] N_ . First, we would like to trivialize the symplectic bundle _γH[∗][TT][ ∗][N]_ appropriately. 

Let 

**==> picture [226 x 15] intentionally omitted <==**

be a continuous family of linear symplectomorphisms that satisfies the following: 

- (a) Φ _t_ : _Tγ[v] H_ ( _t_ ) _[T][ ∗][N][↦−→][L][∗][{]_[0] _[}]_[for][all] _[t][ ∈]_[[0] _[, T]_[],] 

- (b) Φ _t_ : _TγH_ ( _t_ ) _L[∗] Q ↦−→ L[∗] Vt_ for some vector subspaces _Vt ⊂_ R _[n]_ , where _t ∈ {_ 0 _, T }_ . 

Note that Φ _tdϕ[t] H_[(] _[γ][H]_[(0))Φ] 0 _[−]_[1] is a path in _Sp_ (2 _n,_ R) and hence maps Lagrangian subspaces to Lagrangian subspaces. 

178 

**Definition 450.** _Let_ Φ _be a trivialization as in Remark 449. Then the_ _**Maslov index of the Hamiltonian chord** γH is defined as_ 

**==> picture [286 x 41] intentionally omitted <==**

**Lemma 451** ([APS08, Prop 3.2]) **.** _µγH does not depend on the choice of the trivialization_ Φ _._ 

**Theorem 452** ([APS08, Prop 4.1]) **.** _Let γH and γM be corresponding chords on Q and L[∗] Q, respectively. Then γH is nondegenerate if and only if γM is nondegenerate._ 

_Moreover, if γH and γM are nondegenerate, then it holds_ 

**==> picture [275 x 23] intentionally omitted <==**

## **B.5 Binormal and Reeb chords** 

We will start this section with some discussion of the Maslov index in _T[∗] N_ . Then we conclude with the goal of this chapter, that is, a relation between the Morse index of a binormal chord and the Maslov index of the corresponding pure Reeb chord. 

**Lemma 453.** _Let_ dim _N_ = _n >_ 2 _and assume that every loop in Q is contractible in N . Then every loop in L[∗] Q is contractible in S[∗] N ._ 

_Proof._ Let _γ_ : _S_[1] _→L[∗] Q_ . We put _γ_ 0 := _π ◦ γ_ : _S_[1] _→ N_ . Since _γ_ 0 is contractible, there exists a capping disc ~~_γ_~~ 0 of _γ_ 0. 

Then _γ_ is a continuous section of _γ_ 0 _[∗][S][∗][N]_[.][Since] ~~_γ[∗]_~~ 0 _[S][∗][N][∼]_[=] _[ D][ ×][ S][n][−]_[1][for] _[S][n][−]_[1] simply connected, there is an extension of _γ_ to a continuous section ~~_γ_~~ : _S_[1] _→ S[∗] N_ . 

_From now on, N and Q will satisfy the assumptions of Lemma 453._ 

**Lemma 454.** _The first Chern number satisfies the following:_ 

**==> picture [348 x 14] intentionally omitted <==**

**==> picture [379 x 14] intentionally omitted <==**

_Proof._ Ad ( _i._ ): Let _**γ**_ 0 := _π ◦_ _**γ**_ : _S_[2] _→ N_ . We pick a Riemannian metric _g_ on _N_ . Then by the fact that _I_ is an isomorphism of symplectic vector bundles and Remark 388 about pullback maps, we have 

**==> picture [255 x 19] intentionally omitted <==**

Now _g_ induce _O_ ( _n_ )-structures on _**γ**[∗]_ 0 _[TN]_[and] _**[γ]**[ ∗]_ 0 _[T][ ∗][N]_[.][Pick] _[S]_[+] _[⊂][S]_[2][.][Then] we take an isometric trivialization 

**==> picture [139 x 15] intentionally omitted <==**

179 

and find the isometric trivialization 

**==> picture [157 x 15] intentionally omitted <==**

which is defined pointwise as _φ[v]_ +[:=] (︂( _φ[h]_ +[)] _[∗]_[)︂] _[−]_[1][.][We][also][define][an][automorphism] _σ_ ˜︂+ on _S_[+] _×_ (R _[n] ×_ (R _[n]_ ) _[∗]_ ) as ( _Id, σst_ ), where _σst_ is the anti-symplectic involution defined in Example 344. Then Φ[+] := _σ_ ˜︂+ _◦_ ( _φ[h]_ + _[, φ][v]_ +[)][is][an][unitary][trivialization][of] ( _**γ**[∗]_ 0[(] _[TN][⊕][T][ ∗][N]_[)] _[, ω][×][, J][g]_[).][Now][we][construct][analogously][Φ] _[−]_[.] But then det(Φ _t_[+][(Φ] _[−] t_[)] _[−]_[1][)][is][a][real][number][for][each] _[t][∈][S]_[1][.][Hence,][the][corre-] sponding loop has a zero degree. 

Ad ( _ii._ ): Observe that _η_ has a global frame spanned by nonvanishing Liouville and Reeb vector fields. Hence, also the pullback bundle _**γ**[∗] η_ has a global frame. Thus _**γ**[∗] η_ is trivial symplectic vector bundle and _c_ 1( _**γ**[∗] η_ ) = 0 _._ 

Since _S[∗] N_ is embedded into _T[∗] N_ , then, by the above, also _c_ 1( _**γ**[∗] TT[∗] N_ ) = 0. Next, _**γ**[∗] TT[∗] N_ can be written as a Whitney sum of _**γ**[∗] ξ_ and _**γ**[∗] η_ . By the property of _c_ 1 on the Whitney sum, the lemma follows. 

**Lemma 455.** _Let γ be a continuous loop γ_ : _S_[1] _→L[∗] Q ⊂ S[∗] N with a capping disc_ ~~_γ,_~~ _then µ_ ( _γ[∗] T L[∗] Q_ ) = 0 _._ 

_Proof._ Recall that _L[∗] Q_ is embedded in _L[∗] Q_ . First, we would like to show that _µ_ ( _γ[∗] TL[∗] Q_ ) = 0. 

Let ~~_γ_~~ 0 := _π ◦_ ~~_γ_~~ : _S_[1] _→ N_ . Pick a Riemannian metric _g_ on _N_ . Then as in Lemma 454 there is an isomorphism mapping ~~(~~ ~~_γ[∗]_~~ _TT[∗] N, ω_ ) to ~~(~~ ~~_γ[∗]_~~ 0[(] _[TN][⊕] T[∗] N_ ) _, ω×_ ). For simplicity, we will still denote it by _P_ . Then _P_ , when restricted to _S_[1] = _∂D_ , also identify Lagrangian subbundles _γ[∗] TLQ_ and _γ_ 0 _[∗]_[(] _[TQ][ ⊕][L][∗][Q]_[),][see] Remark 448. 

Then as in Lemma 454, isometric trivializations 

**==> picture [272 x 14] intentionally omitted <==**

define together with anti-symplectic involution _σst_ a symplectic trivialization Φ := _σ_ ˜︁ _◦_ ( _φ[h] , φ[v]_ ) of ~~_γ_~~ _[∗]_ 0[(] _[TN][⊕][T][ ∗][N]_[)][.] 

Now we pick Σ := Σ1(R _[n] × {_ 0 _}_ ). But, if _k_ := dim _Q_ , then the loop Φ _γ_ 0 _[∗]_[(] _[TQ][⊕] L[∗] Q_ ) lies completely in the _k_ -th stratum of Σ. Hence, by the zero property of the Maslov index _µ_ ( _γ[∗] TL[∗] Q_ ) = _µ_ (Φ _Pγ[∗] TL[∗] Q_ ) = 0. 

Now, we would like to show that _µ_ ( _γ[∗] ⟨R⟩_ ) = 0. As in the proof of the Lemma 454, nonvanishing Liouville and Reeb vector fields imply the existence of some symplectic trivialization Ψ1 of _γ[∗] η_ that maps _γ[∗] ⟨R⟩_ to the constant Lagrangian subspace in Λ(1). Hence _µ_ ( _γ[∗] ⟨R⟩_ ) = _µ_ (Ψ1( _γ[∗] ⟨R⟩_ )) = 0. 

Next, since _γ[∗] ξ_ is over a contractible disc, there exists a symplectic trivialization Ψ2 of _γ[∗] ξ_ . Then Ψ1 _×_ Ψ2 defines a symplectic trivialization of _γ[∗] η ⊕ γ[∗] ξ_ = _γ[∗]_ ( _η ⊕ ξ_ ) = _γ[∗] TT[∗] N_ . Now, we compute 

**==> picture [189 x 114] intentionally omitted <==**

180 

Which finishes the proof. 

**Corollary 456.** _If γR is a pure Reeb chord on L[∗] Q ⊂ S[∗] N , then |γR| exists and is well defined._ 

_Proof._ First, the existence of _|γR|_ . The existence of _c, J_ and ~~_γ_~~ immediately follows from our assumptions and Remark 386. Hence, we can apply the Definition 392 of the Maslov index _µ_ ( _L[γ]_ ). 

Next, the “well–definiteness” of _|γR|_ . By Corollary 402 and Lemma 454 we need to inspect only the dependence of _|γR|_ on _J_ and _c_ . 

For the various complex structures, it is enough to note the following. If we fix any trivialization of _γ[∗] ξ|_ [2 _/_ 3 _,_ 1], then by Lemma 376 any two complex structures from Remark 420 induce two paths in Λ( _n_ ) that are homotopic with fixed end points. 

Now, we would like to treat the case of two different capping paths. Let us take two discs ~~_γ_~~ 1 ~~_, γ_~~ 2 of the Reeb chord _γR_ that are bounding two different capping paths. If we parametrize their boundary in the standard way, we see that they agree on [1 _/_ 3 _,_ 1]. Next, the gluing _**γ**_ := ~~_γ_~~ 1 _∪_ [1 _/_ 3 _,_ 1] ~~_γ_~~ 2 is a map with a contractible domain. Hence _**γ**[∗] ξ_ is trivial and the trivialization of _**γ**[∗] ξ_ restricts to trivializations of ~~_γ_~~ 1 ~~_[∗]_~~ _ξ_ and ~~_γ_~~ 2 ~~_[∗]_~~ _ξ_ . With respect to these trivializations it follows that _µ_ ( _L[γ]_[1] ) _−µ_ ( _L[γ]_[2] ) is equal to the Maslov index of a loop in _L[∗] Q_ , which vanishes by Lemma 455. 

_Remark_ 457 _._ By Remark 428 and Lemma 443 we know that for any Reeb chord _γR_ : [0 _, T_ ] _→ S[∗] N_ with endpoints on _L[∗] Q_ there is the unique binormal chord _γM_ : [0 _, T_ ] _→ N_ with endpoints on _Q_ that is parametrized by the arc length, and vice versa. 

**Theorem 458.** _Let γR and γM be corresponding chords on L[∗] Q and Q, respectively. Then γR is nondegenerate if and only if γM is nondegenerate._ 

_Moreover, if γR and γM are nondegenerate, then it holds_ 

**==> picture [284 x 13] intentionally omitted <==**

_Proof._ First, the correspondence of nondegenerate chords follows from Theorem 452 and Formula (B.3). 

Next, by Theorem 452 it remains to show that 

**==> picture [257 x 23] intentionally omitted <==**

Let ~~_γ_~~ : _D → S[∗] N_ and _L[γ,]_[2] be a capping disc and a Lagrangian subbundle from the definition of _|γR|_ . Then we put ~~_γ_~~ 0 := _π ◦_ ~~_γ_~~ and _L[γ,]_[1] is a Lagrangian subbundle of _γ[∗] η_ defined as follows. Since _γ_ is a positively oriented loop, we can take a parametrization by _S_[1] = R _/_ Z and for _t ∈_ R _/_ Z we put 

**==> picture [210 x 17] intentionally omitted <==**

**==> picture [280 x 19] intentionally omitted <==**

- ( _iii._ ) for _t ∈_ (2 _/_ 3 _,_ 1) we put _L[γ,]_ [ _t_ ][1][:= rot[] _[dϕ] H[T][⟨][R][γ] R_[(0)] _[⟩][,][ ⟨][R][γ] R_[(] _[T]_[)] _[⟩]_[;] _[ J,]_[ +](3] _[t][−]_[2), where] _J_ is a complex structure in _J_ ( _ηγR_ ( _T_ ) _, η|ωγR_ ( _T_ )). 

181 

Observe that _µ_ ( _L[γ,]_[1] ) is well-defined. 

Now we would like to compute _µ_ ( _L[γ]_ ), where _L[γ]_ := _L[γ,]_[1] _⊕L[γ,]_[2] _⊂ γ[∗] TT[∗] N_ . The procedure will be similar to the proofs of Lemmata 455, 454. So _µ_ ( _L[γ]_ ) = _µ_ ( _PL[γ]_ ) for _P_ mapping ~~(~~ ~~_γ[∗]_~~ _TT[∗] N, ω_ ) to ~~(~~ ~~_γ[∗]_~~ 0[(] _[TN][⊕][T][ ∗][N]_[)] _[, ω][×]_[) as before, but Φ =] _[σ]_[˜︁] _[◦]_[(] _[φ][h][, φ][v]_[)] will be constructed as follows. 

We would like to use Remarks 383, 389 and 391. First, note that [ _−_ 1 _/_ 3 _,_ 1 _/_ 3] is contractible in _S_[1] = R _/_ Z and 

**==> picture [299 x 15] intentionally omitted <==**

Hence there exists 

**==> picture [214 x 15] intentionally omitted <==**

and some linear subspace _V ⊂_ R _[n]_ such that _φ[h]_ : _Tγ_ 0( _t_ ) _Q ↦→ V ⊂_ R _[n]_ for each _t ∈_ [ _−_ 1 _/_ 3 _,_ 1 _/_ 3]. Moreover, there exists a trivialization of ~~_γ[∗]_~~ 0 _[TN]_[that][extends] _φ[h]_ . We will denote this trivialization by the same symbol _φ[h]_ . This determines _φ[v]_ : ~~_γ[∗]_~~ 0 _[T][ ∗][N][→][D][×]_[(][R] _[n]_[)] _[∗]_[such that] _[ φ][v]_[:] _[ L][∗] γ_ 0( _t_ ) _[Q][ ↦→]_[(] _[V][⊥]_[)] _[∗]_[for each] _[ t][ ∈]_[[] _[−]_[1] _[/]_[3] _[,]_[ 1] _[/]_[3].] Finally, _σ_ ˜︁ = ( _Id, σst_ ) is the automorphism of _D ×_ R _[n] ×_ (R _[n]_ ) _[∗]_ , where _σst_ is the anti-symplectic on R _[n] ×_ (R _[n]_ ) _[∗]_ . 

Let us denote Φ := Φ[˜︁] _◦ P_ , then we compute 

**==> picture [351 x 58] intentionally omitted <==**

Here because Φ[˜︁] _L[γ]_[a][constant][path][in][Λ(] _[n]_[)] _[,]_[we][have] [0 _,_ 1 _/_ 3][is] 

**==> picture [114 x 18] intentionally omitted <==**

Next, 

and by Lemma 377 

Hence 

**==> picture [272 x 97] intentionally omitted <==**

On the other hand, we have 

**==> picture [117 x 31] intentionally omitted <==**

But 

**==> picture [96 x 14] intentionally omitted <==**

In order to compute _µ_ ( _L[γ,]_[1] ), we take a symplectic trivialization Ψ of ~~_γ[∗]_~~ _η_ that sends a nonvanishing frame spanned by _R_ and _X_ to fixed basis vectors. It follows 

182 

that 

**==> picture [369 x 56] intentionally omitted <==**

Because Ψ _L[γ,]_[1][constant][path][in][Λ(1),][we][have] [0 _,_ 1 _/_ 3][is] 

**==> picture [118 x 17] intentionally omitted <==**

Next, by Formula B.3 the only intersection of Ψ _L[γ,]_ [1 _/_[1] 3 _,_ 2 _/_ 3][with][Ψ] _[L][γ,]_ [0][1][appears][at] _t_ = 1 _/_ 3. Moreover, this intersection contributes with +1 _/_ 2. Hence 

**==> picture [129 x 25] intentionally omitted <==**

And by Lemma 377 

**==> picture [121 x 25] intentionally omitted <==**

Thus 

_µ_ ( _L[γ]_ ) = _|γR|_ + 2 _._ (B.10) 

Hence from Formulas (B.9) and (B.10) we obtain Formula (B.8), which finishes the proof. 

183 

## **C. Legendrian contact homology** 

_Remark_ 459 _._ [FHT01]Let _X_ be a smooth manifold. We define a **normalized singular chain complex** as graded free abelian groups _C∗_ ( _X_ ) together with the differential _∂[sing]_ : _C∗_ ( _X_ ) _→ C∗−_ 1( _X_ ), where 

**==> picture [222 x 30] intentionally omitted <==**

Here, ∆ _[i]_ is the convex hull of the standard basis _e_ 0 _, . . . , ei_ of R _[i]_[+1] and degenerate maps are those maps that are independent of at least one coordinate of R _[i]_[+1] . And for generators _α ∈ Ci_ ( _X_ ) we put _∂[c] α_ =[∑︁] _k_[(] _[−]_[1)] _[k][α][ ◦][δ] k[,]_[where] _[δ] k_[is][the][inclusion] of the _k_ -the face ∆ _[i][−]_[1] _→_ ∆ _[i]_ . 

Next, if _X_ 1 _, X_ 2 are smooth manifolds, then there is an Eilenberg-Zilber map 

**==> picture [211 x 13] intentionally omitted <==**

which assigns to ∆ _[i] ⊗_ ∆ _[j]_ the canonical subdivision of ∆ _[i]_[+] _[j]_ . For details, see [FHT01]. Moreover, _×_ satisfies associativity. _Remark_ 460 _._ [FHT01] Let _X_ be a smooth manifold and _x_ 0 _, x_ 1 _∈ X_ . Then Ω _x_ 0 _,x_ 1 _X_ denote a **Moore path space** . That is a set 

**==> picture [367 x 30] intentionally omitted <==**

equipped with the _C[∞]_ -compact-open topology and the multiplication _∗_ : Ω _x_ 0 _,x_ 1 _X×_ Ω _x_ 1 _,x_ 2 _X →_ Ω _x_ 0 _,x_ 2 _X_ given by concatenation as 

**==> picture [310 x 37] intentionally omitted <==**

Here the maps _γi_ have domains [0 _, Ti_ ]. If moreover _x_ 0 = _x_ 1, then Ω _x_ 0 _,x_ 0 _X_ is called a **Moore based loop space** and denoted Ω _x_ 0 _X_ . Last, if _x_ 1 is allowed to vary on _X_ , then the resulting space is called a **free-end Moore path space** and denoted Ω _x_ 0 _X_ . 

Observe that _∗_ is associative. 

If _X_ is path-connected, then the map evaluating paths at endpoints gives us a fibration 

**==> picture [266 x 14] intentionally omitted <==**

and Ω _x_ 0 _X_ is contractible. 

_Remark_ 461 _._ [FHT01] The composition of _×_ and _∗_ gives (︂ _C_ (Ω _x_ 0 _X_ ) _, ∂[c]_[)︂] a structure of a (strictly) associative differential graded ring. 

_Remark_ 462 _._ Now we would like to describe the structure of _H_ (Ω _x_ 0 _L[∗]_ + _[T][K]_[).] 

First recall that _L[∗]_ + _[T][K][∼]_[=] _[T][K]_[.][Since] _[T][K]_[has][the][universal][cover][R][2][,][by][the] lifting property _L[∗]_ + _[T][K]_[is][an][Eilenberg-MacLane][space] _[K]_[(] _[G,]_[ 1),][[Hat19].][Here] _G_ = Z[2] . 

From fibration (C.1) and LES of homotopy groups we obtain that _π_ 0(Ω _x_ 0 _L[∗]_ + _[T][K]_[)] _[ ∼]_[=] _π_ 1( _L[∗]_ + _[T][K]_[)][is][the][only][nonzero][homotopy][group][of] _[L][∗]_ + _[T][K]_[.] 

184 

By Hurewicz theorem, [FHT01], the only nonzero homology group of Ω _x_ 0 _L[∗]_ + _[T][K]_ is concentrated at the degree 0. Here 

**==> picture [138 x 27] intentionally omitted <==**

and the multiplicative structure at _H_ 0(Ω _x_ 0 _L[∗]_ + _[T][K]_[)][is][induced][by][the][group][struc-] ture of _π_ 1( _L[∗]_ + _[T][K]_[).] 

Hence 

**==> picture [157 x 13] intentionally omitted <==**

**Definition 463.** _Let x_ 0 _be a fixed point in L[∗]_ + _[T][K][and][ℓ][∈]_[N][0] _[.][A]_ _**[Reeb][string] with** ℓ_ _**chords** is a word_ 

**==> picture [103 x 9] intentionally omitted <==**

_where_ 

( _i._ ) _For k ∈{_ 1 _, . . . , ℓ},_ _**a** i are Reeb chords on L[∗]_ + _[T][K][parametrized][by][times][T][i][.]_ 

**==> picture [286 x 228] intentionally omitted <==**

**----- Start of picture text -----**<br>
( ii. ) α 1 ∈ Ω x 0 , a 1( T 1) L [∗] + [T][K][.]<br>( iii. ) For k ∈{ 2 , . . . , ℓ}, αk ∈ Ω a k− 1(0) , a k ( Tk ) L [∗] + [T][K][.]<br>( iv. ) αℓ +1 ∈ Ω a ℓ ( T 0) ,x 0 L [∗] + [T][K][.]<br>See also Figure C.1.<br>x 0<br>α 1 α 2<br>α 3 α 4<br>a 1 a 2 a 3<br>**----- End of picture text -----**<br>


Figure C.1: The Reeb string _α_ 1 _**a**_ 1 _α_ 2 _**a**_ 2 _α_ 3 _**a**_ 3 _α_ 4. Observe that Reeb chords (in blue) are traversed in the opposite direction. 

_Next, R[ℓ] denotes the set of Reeb strings with ℓ chords equipped with C[m] - compact-open topology. We put R_ :=[∐︁] _ℓ≥_ 0 _[R][ℓ][.][Then][the][concatenation][∗][at][x]_ 0 _gives R a structure of a H-space._ 

_Remark_ 464 _._ The sub- _H_ -space _R_[0] agrees with Ω _x_ 0 _L[∗]_ + _[T][K]_[.] 

_Remark_ 465 _._ The composition of _×_ and _∗_ gives _C_ ( _R_ ) the structure of a noncommutative but associative ring, which is graded by the degree of the singular chains. Next, we can extend the grading of _C_ ( _R_ ) by adding the sum of degrees of the Reeb chords that correspond to given Reeb strings. Since the degree of a Reeb chord is independent of a capping path, _C_ ( _R_ ) still has the structure of a strictly associative graded ring. 

185 

**Definition 466.** _Let_ _**a** ,_ _**b**_ 1 _, . . . ,_ _**b** m be Reeb chords on L[∗]_ + _[T][K][that are parametrized] by times T_ 0 _, T_ 1 _, . . . , Tm, respectively. If u ∈M[sy]_ ( _**a** ,_ _**b**_ 1 _, . . . ,_ _**b** m_ ) _/_ R _, then ∂_ ( _u_ ) _is a word_ 

**==> picture [149 x 13] intentionally omitted <==**

_where βk are boundary arcs of u projected to L[∗]_ + _[T][K][and][are][in][counterclockwise] order and orientation of ∂Dm_ +1 _. Hence_ 

**==> picture [139 x 14] intentionally omitted <==**

**==> picture [257 x 38] intentionally omitted <==**

**Definition 467.** _The differential ∂[sy] on C_ ( _R_ ) _is defined as follows. Let W ∈ C_ ( _R_ ) _be a chain of a type W_ = _α_ 1 _**a**_ 1 _. . ._ _**a** ℓαℓ_ +1 _, then_ 

**==> picture [359 x 43] intentionally omitted <==**

_Here ε is a sign from orientation of_ 0 _-dimensional manifold M[sy]_ ( _**a** ,_ _**b**_ 1 _, . . . ,_ _**b** m_ ) _/_ R _(see also Theorem 306), d is a singular chain degree and ∂_ ( _u_ ) _·k W is a word_ 

**==> picture [223 x 13] intentionally omitted <==**

**==> picture [412 x 252] intentionally omitted <==**

**----- Start of picture text -----**<br>
where paths αk and αk +1 are concatenated with paths β 1 and βm, respectively. See<br>Figure C.2.<br>x 0<br>α 1 α 2<br>α 3 α 4<br>a 1 a 2 a 3<br>β 1 u β 3<br>β 2<br>b 1 b 2<br>**----- End of picture text -----**<br>


Figure C.2: The Reeb string _∂_ ( _u_ ) _·_ 2 _α_ 1 _**a**_ 1 _α_ 2 _**a**_ 2 _α_ 3 _**a**_ 3 _α_ 4, where _∂_ ( _u_ ) = _β_ 1 _**b**_ 1 _β_ 2 _**b**_ 2 _β_ 3. 

_Remark_ 468 _._ By Stokes’ Theorem _L_ ( _**a**_ ) _−_[∑︁] _[m] k_ =1 _[L]_[(] _**[b]**[k]_[)] _[ ≥]_[0.][Hence, the sum in the] definition of _∂[sy]_ is finite. 

**Definition 469.** _∂L_ := _∂[sing]_ + _∂[sy]_ : _C_ ( _R_ ) _→ C_ ( _R_ ) _._ 

_Remark_ 470 _. ∂L_ has degree _−_ 1. 

186 

**Definition/Theorem 471** ([CELN16, EES05a]) **.** _∂L_[2][= 0] _[, the homology of]_[ (] _[C]_[(] _[R]_[)] _[, ∂][L]_[)] _is called_ _**Legendrian contact homology** LCH_ ( _L[∗]_ + _[T][K]_[)] _[and][is][an][invariant][un-] der all choices. In particular, LCH_ ( _L[∗]_ + _[T][K]_[)] _[is][an][invariant][under][Legendrian] isotopy of L[∗]_ + _[T][K][in][a][fixed][chosen][spin][structure.]_ 

**Definition 472.** _Let_ ( _R, ∂R_ ) _be a differential graded (dg) ring. An_ ( _R, ∂R_ ) _**-NCalgebra** is a dg ring_ ( _S, ∂S_ ) _together with a dg ring homomorphism_ ( _R, ∂R_ ) _→_ ( _S, ∂S_ ) _._ 

_Two_ ( _R, ∂R_ ) _-NC-algebras_ ( _S_ 1 _, ∂S_ 1) _,_ ( _S_ 2 _, ∂S_ 2) _are_ _**isomorphic** if there is a dg ring isomorphism_ ( _S_ 1 _, ∂S_ 1) _→_ ( _S_ 2 _, ∂S_ 2) _that intertwines with maps_ ( _R, ∂R_ ) _→_ ( _S_ 1 _, ∂S_ 1) _and_ ( _R, ∂R_ ) _→_ ( _S_ 2 _, ∂S_ 2) _._ 

_Here “NC” means “noncommutative”._ 

_Example_ 473 _._ By Remark 462, _LCH_ ( _L[∗]_ + _[T][K]_[) is an NC-algebra over the group ring] Z[ _π_ 1( _L[∗]_ + _[T][K]_[)]] _[.]_ 

187 

## **D. Proof of Lemma 45** 

First, we describe _K_ in suitable coordinates around _γ_ ~~(~~ ~~_s_ )~~ . For this, we can assume that _κ_ ~~(~~ ~~_s_ )~~ _>_ 0. We take the following isothermal coordinates ( _x, y, z_ ) _∈_ (R[3] _,_ (1 _/_ 2) _κ_ ~~(~~ ~~_s_ )~~ _gEuc_ ). We would like to find ~~_δ_~~ _s_[and] _[ε]_ 0 _,s_[in][these][coordinates.][Note] that the actual ~~_δ_~~ _s_[and] _[ε]_ 0 _,s_[need][to][be][scaled][by] _[κ]_ ~~[(]~~ ~~_s_ )~~ _/_ 2 and 2 _/κ_ ~~(~~ ~~_s_ )~~ , respectively. The coordinates are characterized by: 

- _γ_ ~~(~~ ~~_s_ )~~ = (0 _,_ 0 _,_ 0). 

- Around _γ_ ~~(~~ ~~_s_ )~~ the curve _γ_ is reparametrized by _t ∈_ ( _−δ, δ_ ) and given as 

**==> picture [150 x 46] intentionally omitted <==**

for some real constants _Y_ 1 _, Y_ 2 _, Z_ 1 _, Z_ 2. 

Here _δ >_ 0 was chosen sufficiently small, such that the above chart exists. Note that in these coordinates, _γ_ is not necessarily parametrized by arc length, but for purposes of this lemma, it is not an issue. 

Let _ε >_ 0. Then Γ _ϵ_ : ( _−δ, δ_ ) _×_ R _/_ 2 _π_ Z _→_ R[3] will still describe a parametrization of the torus _TK,ε_ , but now in our local coordinates. By symmetry, we can restrict ourself to [0 _, δ_ ). 

First, we treat the cases ( _i._ ) and ( _ii._ ). 

We introduce a smooth family of functions _{gt,ε}t∈_ [0 _,δ_ )[,][which][are][defined][as] 

**==> picture [217 x 30] intentionally omitted <==**

Here _πy, πz_ are the canonical projections on R[2] _y,z_[.][The][minimum][of] _[g][t,ε]_[describes] the square of the distance of the circle Γ _ε|t_ from the _x_ -axis. Recall that if the minimum is _ε_[2] , then Γ _ε|t_ is tangent to _C_ (0 _,_ 0 _,_ 0) _,ε_ 

Now, we inspect the uniqueness of the minimum of _gt,ε_ . Clearly, for _t_ = 0, there is a whole circle of minima. We can translate the problem into finding the minima of the distance between an ellipse _E_ and a point _p_ in the plane. Observe that if _p_ is lying outside of the _E_ then there is the unique point on _E_ achieving the minima. It corresponds to the touching point of _E_ and some circle with the center _p_ . And such a point is unique by the convexity of the circle and the ellipse. If _p_ lies inside _E_ , there could potentially be two minima, but we are not interested in this particular case. To achieve the translation of the problem we just project the circle Γ _ε|t_ to _πy,z_ (Γ _ε|s_ ) _⊂_ R[2] _y,z_[and] _[x]_[-axis][to][(0] _[,]_[ 0).][By][shrinking] _δ_ , if necessary, we can assume that _πy,z_ is an embedding for any _t ∈_ (0 _, δ_ ). First, let us find when _πy,z_ (Γ _ε|s_ ) lies outside of the point (0 _,_ 0). It will be sufficient to solve the inequality 

**==> picture [239 x 14] intentionally omitted <==**

188 

For this we split inequality (D.1) into two inequalities, where one will contain _ε_ -terms and the second _O_ ( _t_[3] )-terms. That is 

**==> picture [257 x 32] intentionally omitted <==**

First, inequality (D.2). There exists _ε_ 1 _>_ 0 such that for every _ε ∈_ (0 _, ε_ 1) it holds that for every _t ∈_ ( ~~√~~ 4 _/_ 3 _ε_[1] _[/]_[2] _, δ_ ) inequality (D.2) is satisfied. Next, inequality (D.3). Here we obtain immediately that there exists _δ_ 1 _∈_ (0 _, δ_ ) such that inequality (D.3) holds for _t ∈_ (0 _, δ_ 1). 

Altogether, inequality (D.1) holds for _t ∈_ ( ~~√~~ 4 _/_ 3 _ε_[1] _[/]_[2] _, δ_ 1). Note that for _δ_ 1 we can find _ε_ 1 _>_ 0 such that for every _ε ∈_ (0 _, ε_ 1] the intervals ( ~~√~~ 4 _/_ 3 _ε_[1] _[/]_[2] _, δ_ 1) are nonempty. And specially, the corresponding _gt,ε_ has the unique minimum. 

Now, we are going to explicitly find the minimum of _gt,ε_ . 

Let us assume that around (0 _,_ 0 _,_ 0) _γ_ contains no torsion (i.e. _z_ = 0). Then we can quickly find the minimum of _gt,ε_ . First note that _γ_ lies in the _xy_ -plane, and the _xy_ -plane is orthogonal to the circle Γ _ε|t_ and to the _x_ -axis. Hence by Lagrangian multipliers, the minimum is attended at _θ_ ( _t_ ) = _π_ (or in another words, at _γ_ ( _t_ ) _− εn_ ( _t_ )). In particular, if _γ_ does not contain any higher order terms of _t_ than of the second order, then _gt,ε_ ( _θ_ ( _t_ )) is given as on Figure D.1 and explicitly as 

**==> picture [291 x 50] intentionally omitted <==**

**==> picture [297 x 153] intentionally omitted <==**

**----- Start of picture text -----**<br>
distance [2]<br>gt,ε ( θ ( t ))<br>ε [2]<br>0 t<br>**----- End of picture text -----**<br>


Figure D.1: Graph of the function _gt,ε_ ( _θ_ ( _t_ )). 

When _γ_ also includes torsion, the computation of the desired _θ_ ( _t_ ) is more complicated. One needs to solve _∂θgt,ε_ ( _θ_ ) = 0, which is a quartic equation in _ℓ_ after the substitution cot( _θ/_ 2) = _ℓ_ . Our aim is to compute the Taylor expansion of _gt,ε_ ( _θ_ ( _t_ )) up to order 4. This can be done by cutting _gt,ε_ ( _θ_ ( _t_ )) into smaller pieces and computing the sufficiently high Taylor expansions of these pieces first. 

189 

Using _Mathematica_ we obtain that 

**==> picture [448 x 79] intentionally omitted <==**

Which can be rewritten as 

**==> picture [302 x 14] intentionally omitted <==**

where _P_ 1 and _P_ 2 are some expressions that depend on _{ε, Y_ 1 _, Y_ 2 _, Z_ 1 _}_ and have the property that _ε_[1] _[/]_[2] _P_ 1 and _ε_[1] _[/]_[2] _P_ 2 are _O_ ( _ε_[1] _[/]_[2] ). 

Now we are going to inspect analytical properties of _gt,ε_ ( _θ_ ( _t_ )) relative to _ε_[2] . In more detail, will describe the monotonicity of _gt,ε_ ( _θ_ ( _t_ )) and upper/lower bounds to _gt,ε_ ( _θ_ ( _t_ )), which will help us to localize the solutions of _gt,ε_ ( _θ_ ( _t_ )) = _ε_[2] . 

First, we inspect when _gt,ε_ ( _θ_ ( _t_ )) is growing. Hence, we study the inequality 

**==> picture [251 x 19] intentionally omitted <==**

Writing 1 _· t_[3] = (1 _/_ 4) _t_[3] + (3 _/_ 4) _t_[3] , we, analogously to inequality (D.1), split inequality (D.4) into two inequalities, where the first one is 

**==> picture [109 x 14] intentionally omitted <==**

Which holds for _t ∈_ (0 _, δ_ 2), where _δ_ 2 _>_ 0 is sufficiently small. 

Now we take the second inequality of the splinting of inequality (D.4). Here we substitute _t_ := _ε_[1] _[/]_[2] _t_ 1 and obtain 

**==> picture [277 x 15] intentionally omitted <==**

Then we divide the inequality by _ε_[3] _[/]_[2] , put _ε_ := 0 and obtain 

**==> picture [106 x 14] intentionally omitted <==**

Hence, altogether, there exists _δ_ 2 _, ε_ 2 _>_ 0 such that for every _ε ∈_ (0 _, ε_ 2] the function _gt,ε_ ( _θ_ ( _t_ ) is growing along (√︂4 _/_ 3 _ε_[1] _[/]_[2] _, δ_ 2). 

Now, we inspect when _gt,ε_ ( _θ_ ( _t_ )) is decreasing, that is the inequality 

**==> picture [251 x 19] intentionally omitted <==**

Again we put _t_ := _ε_[1] _[/]_[2] _t_ 1, so _O_ ( _t_[4] ) becomes _ε_[2] _O_ ( _t_[4] 1[).][Then][divide][the][inequality] by _ε_[3] _[/]_[2] _>_ 0 and put _ε_ := 0 _._ So we are left with 

**==> picture [79 x 14] intentionally omitted <==**

Hence there is _ε_ 3 _>_ 0 such that for every _ε ∈_ (0 _, ε_ 3] it holds that for every _t ∈_ (0 _, ε_[1] _[/]_[2] ) inequality (D.5) is satisfied. 

Next, we are going to inspect when _gt,ε_ ( _θ_ ( _t_ )) is smaller/bigger than _ε_[2] . 

190 

First, the inequality 

**==> picture [253 x 14] intentionally omitted <==**

We substitute _t_ := _ε_[1] _[/]_[2] _t_ 1. So _O_ ( _t_[5] ) becomes _ε_[5] _[/]_[2] _O_ ( _t_[5] 1[).][Then][we][consequently] divide inequality (D.6) by _ε_[2] , put _ε_ := 0 and obtain 

**==> picture [97 x 15] intentionally omitted <==**

Hence, there exists _ε_ 4 _>_ 0 such that for every _ε ∈_ [ _ε_ 4 _,_ 0) it holds that for every _t ∈_ (√︂1 _/_ 2 _ε_[1] _[/]_[2] _,_ √︂3 _/_ 2 _ε_[1] _[/]_[2] ) inequality (D.6) is satisfied. Now the inequality 

**==> picture [250 x 14] intentionally omitted <==**

We write 1 _· t_[4] = (1 _/_ 2) _t_[4] + (1 _/_ 2) _t_[4] . As before, we split inequality (D.7) into two inequalities. The first one is 

**==> picture [103 x 15] intentionally omitted <==**

This holds for _t ∈_ (0 _, δ_ 3), where _δ_ 3 _>_ 0 is sufficiently small. 

Now we take the second inequality of the splinting of inequality (D.7). Here we consequently substitute _t_ := _ε_[1] _[/]_[2] _t_ 1, divide the inequality by _ε_[3] _[/]_[2] , put _ε_ := 0 and obtain 

**==> picture [111 x 15] intentionally omitted <==**

Hence, altogether, there exists _δ_ 3 _, ε_ 5 _>_ 0 such that for every _ε ∈_ (0 _, ε_ 5] it holds that for every _t ∈_ ((23 _/_ 10) _ε_[1] _[/]_[2] _, δ_ 3) inequality (D.7) is satisfied. 

Next, we put ~~_δ_~~ _s_[:=][min] _[{][δ]_ 1 _[, δ]_ 2 _[, δ]_ 3 _[}]_[.][Then][for][every] _[δ]_ 0 _[∈]_[(0] _[, ]_ ~~_[δ]_~~ _s_ ~~[]]~~[we][put] _[ε]_ 0 _,s_[:=] min( _ε_ 1 _, ε_ 2 _, ε_ 3 _, ε_ 4 _, ε_ 5 _, δ_ 0 _, εgood_ ). This finishes the poofs of ( _i._ ). 

We will solve the cases ( _ii._ ) analogously. 

Since _γ_ is transverse to the _yz_ -plane, the intersection _Et,ε_ := _Ct,ε ∩{x_ = 0 _}_ is an ellipse. The parametrization of Γ _ε|t_ by _θ_ naturally induces the parametrization of _Eε,t_ , which will also be denoted by _θ_ . 

Let _{ht,ε}t∈_ [0 _,δ_ 0) be a smooth family of functions, where 

**==> picture [217 x 30] intentionally omitted <==**

Similarly as before, we are interested in finding the minimum of _ht,ε_ . First we inspect the uniqueness. Let _c_ : [0 _, δ_ 0) _→_ R[3] be a curve assigning to ̇ each _t_ the intersection of the line _{γ_ ( _t_ ) + _⟨γ_ ( _t_ ) _⟩}_ with the plane _{x_ = 0 _}_ . Then we are interested in solving the inequality 

**==> picture [243 x 14] intentionally omitted <==**

Which can be rewritten as 

**==> picture [76 x 14] intentionally omitted <==**

Hence, similarly to inequality (D.1), there exist _δ_ 4 _>_ 0 and _ε_ 6 _>_ 0 such that for every _ε ∈_ (0 _, ε_ 6) and every _t ∈_ ( _ε_[1] _[/]_[2] _, δ_ 4) inequality (D.8) is satisfied. And specially such a _ht,ε_ has the unique minimum. 

191 

Also, if _γ_ does not contain any higher order terms of _t_ than of the second order, then by Lagrangian multipliers we compute _θ_ ( _t_ ) = 0 and 

**==> picture [255 x 50] intentionally omitted <==**

In the general case, by _Mathematica_ , we obtain that 

**==> picture [309 x 15] intentionally omitted <==**

where _P_ 3 and _P_ 4 are some expressions that depend on _{ε, Y_ 1 _, Y_ 2 _, Z_ 1 _}_ and have the property that _ε_[1] _[/]_[2] _P_ 3 and _ε_[1] _[/]_[2] _P_ 4 are _O_ ( _ε_[1] _[/]_[2] ). 

Analogously, as above, we obtain the following analytical properties. First, there exist _δ_ 5 _>_ 0 and _ε_ 7 _>_ 0 such that for every _ε ∈_ [ _ε_ 7 _,_ 0) the function _ht,ε_ ( _θ_ ( _t_ )) is growing on (√︂4 _/_ 3 _ε_[1] _[/]_[2] _, δ_ 5) and decreasing on (0 _, ε_[1] _[/]_[2] ). Also there exists _ε_ 8 _>_ 0 such that for every _ε ∈_ [ _ε_ 8 _,_ 0) it holds that for every _t ∈_ ( ~~√~~ 1 _/_ 2 _ε_[1] _[/]_[2] _,_ ~~√~~ 3 _/_ 2 _ε_[1] _[/]_[2] ) the inequality _ht,ε_ ( _θ_ ( _t_ )) _<_ ( _ε/_ 2)[2] is satisfied. And there exist _δ_ 6 _>_ 0 and _ε_ 9 _>_ 0 such that for every _ε ∈_ (0 _, ε_ 9] it holds that for every _t ∈_ ((23 _/_ 10) _ε_[1] _[/]_[2] _, δ_ 6) the inequality _ht,ε_ ( _θ_ ( _t_ )) _>_ (2 _ε_ )[2] is satisfied. 

Now, we put ~~_δ_~~ _s_[:=][min] _[{][δ]_ 1 _[, . . . , δ]_ 6 _[}]_[.] Then for _δ_ 0 _∈_ (0 _,_ ~~_δ_~~ _s_ ~~[]]~~[we][put] _[ε]_ 0 _,s_[:=] min( _ε_ 1 _, . . . , ε_ 9 _, δ_ 0 _, εgood_ ). This finishes the proof of ( _i._ ) _−_ ( _ii._ ). 

192 

## **List of Symbols** 

_T[∗] N, S[∗] N_ cotangent and unit cotangent bundles over _N_ , respect. _L[∗] Q, L[∗] Q_ conormal and unit conormal bundles over _Q_ , respect. _L[∗]_ + _[Q,][ L][∗]_ + _[Q]_ one half of (unit) conormal bundles over the codim 1 

one half of (unit) conormal bundles over the codim 1 submanifold _Q_ , see Remark 293 

**==> picture [238 x 31] intentionally omitted <==**

space of outward-pointing chords on _TK,ε_ 

**==> picture [398 x 337] intentionally omitted <==**

**==> picture [371 x 66] intentionally omitted <==**

- _·f_ - _s t, ·f_ - _s τ_ fast-slow flow in slow/fast time scales _Bδ,Ufen_ box given by the codomain of Fenichel chart _XH, R_ Hamiltonian and Reeb vector fields _|_ _**a** |_ Reeb chord degree 

- _M[sy] TK[,][ M][T] K_ Moduli spaces of _J_ -holomorphic curves in the symplectization and with switches, respect. 

193 

## **Bibliography** 

- [AB95] D. M. Austin and P. J. Braam. _Morse-Bott theory and equivariant cohomology_ , pages 123–183. Birkh¨auser Basel, Basel, 1995. 

- [Abo11] Mohammed Abouzaid. A topological model for the Fukaya categories of plumbings. _Journal of Differential Geometry_ , 87(1), Jan 2011. 

- [Abo13] Mohammed Abouzaid. Symplectic cohomology and Viterbo’s theorem. _arXiv preprint arXiv:1312.3354_ , 2013. 

- [AD13] Mich´ele Audin and Mihai Damian. Morse Theory and Floer homology. Springer, 2013. 

- [AENV14] Mina Aganagic, Tobias Ekholm, Lenhard Ng, and Cumrun Vafa. Topological strings, D-model, and knot contact homology. _Advances in Theoretical and Mathematical Physics_ , 18(4):827–956, 2014. 

- [Amb61] Warren Ambrose. The index theorem in Riemannian Geometry. _Annals of Mathematics_ , 73:49, 1961. 

- [APS08] Alberto Abbondandolo, Alessandro Portaluri, and Matthias Schwarz. The homology of path spaces and Floer homology with conormal boundary conditions. _Journal of Fixed Point Theory and Applications_ , 4(2):263–293, Dec 2008. 

- [Arn67] V. I. Arnol’d. Characteristic class entering in quantization conditions. _Funkts. Anal. Prilozh._ , 1(1):1–14, 1967. 

- [Asp19] Johan Asplund. Fiber Floer cohomology and conormal stops. _arXiv preprint arXiv:1912.02547_ , 2019. 

- [BCR98] J. Bochnak, M. Coste, and M-F. Roy. _Real Algebraic Geometry_ . Springer, 1998. 

- [BEH[+] 03] Frederic Bourgeois, Yakov Eliashberg, Helmut Hofer, Kris Wysocki, and Eduard Zehnder. Compactness results in Symplectic Field Theory. _Geometry and Topology_ , 7(2):799–888, dec 2003. 

- [BH04] A. Banyaga and D. Hurtubise. _Lectures on Morse Homology_ . Texts in the Mathematical Sciences. Springer Netherlands, 2004. 

- [BH13] Augustin Banyaga and David E Hurtubise. Cascades and perturbed Morse-Bott functions. _Algebraic & Geometric Topology_ , 13(1):237–275, 2013. 

- [Bol77] John Bolton. The morse index Theorem in the case of two variable end-points. _Journal of Differential Geometry_ , 12(4):567–581, 1977. 

- [Bru99] Pavol Brunovsk´y. _C[r]_ -Inclination Theorems for singularly perturbed equations. _Journal of Differential Equations_ , 155:133–152, 1999. 

- [BT11] Raoul Bott and Loring W. Tu. _Differential forms in Algebraic Topology_ . Springer, 2011. 

- [CE12] Kai Cieliebak and Yakov Eliashberg. _From Stein to Weinstein and back: Symplectic geometry of affine complex manifolds_ . American Mathematical Society, 2012. 

- [CEL09] Kai Cieliebak, Tobias Ekholm, and Janko Latschev. Compactness for holomorphic curves with switching Lagrangian boundary conditions. _Journal of Symplectic Geometry_ , 8:267–298, 2009. 

- [CELN16] Kai Cieliebak, Tobias Ekholm, Janko Latschev, and Lenhard L. Ng. Knot contact homology, string topology, and the cord algebra. _arXiv: Symplectic Geometry_ , 2016. 

- [Cie18] Kai Cieliebak. _Nonlinear Functional Analysis_ . University of Augsburg, 2018. 

- [CLM94] Sylvain E. Cappell, Ronnie Lee, and Edward Y. Miller. On the Maslov index. _Communications on Pure and Applied Mathematics_ , 47:121–186, 1994. 

- [Con78] C. Conley. _Isolated Invariant Sets and the Morse Index_ . Number Nr. 38. Conference Board of the Mathematical Sciences, 1978. 

- [CP16] do Carmo and Manfredo P. _Differential geometry of curves and surfaces: Revised and updated Second edition_ . Dover Publications, 2016. 

- [CV23] Kai Cieliebak and Evgeny Volkov. Chern-Simons Theory and string topology. _arXiv preprint arXiv:2312.05922_ , 2023. 

- [dH15] Mat´ıas L. del Hoyo. Complete connections on fiber bundles. _arXiv: Differential Geometry_ , 2015. 

- [EENS13] Tobias Ekholm, John B Etnyre, Lenhard Ng, and Michael G Sullivan. Knot contact homology. _Geometry & Topology_ , 17(2):975–1112, 2013. 

- [EES05a] Tobias Ekholm, John Etnyre, and Michael Sullivan. The contact homology of Legendrian submanifolds in R[2] _[n]_[+1] . _Journal of Differential Geometry_ , 71(2):177 – 305, 2005. 

- [EES05b] Tobias Ekholm, John B. Etnyre, and Michael G. Sullivan. Legendrian contact homology in _P ×_ R. _arXiv: Symplectic Geometry_ , 2005. 

- [EGH00] Y. Eliashberg, A. Givental, and H. Hofer. _Introduction to Symplectic Field Theory_ , pages 560–673. Birkh¨auser Basel, Basel, 2000. 

- [Ekh18] Tobias Ekholm. Knot contact homology and open Gromov–Witten theory. In _Proceedings of the International Congress of Mathematicians: Rio de Janeiro 2018_ , pages 1063–1086. World Scientific, 2018. 

- [EKL20] Tobias Ekholm, Piotr Kucharski, and Pietro Longhi. Physics and geometry of knots-quivers correspondence. _Communications in Mathematical Physics_ , 379(2):361–415, 2020. 

- [Eld13] Jaap Eldering. Normally hyperbolic invariant manifolds: The noncompact case. Atlantis Press, 2013. 

- [El´ı67] Halld´or I. El´ıasson. Geometry of manifolds of maps. _Journal of Differential Geometry_ , 1:169–194, 1967. 

- [EM02] Yakov Eliashberg and Nikolai M. Mishachev. Introduction to the h-Principle. American Mathematical Soc., 2002. 

194 

- [ENS17] Tobias Ekholm, Lenhard Ng, and Vivek Shende. A complete knot invariant from contact homology. _Inventiones mathematicae_ , 211(3):1149–1200, October 2017. 

- [Fen77] Neil Fenichel. Asymptotic stability with rate conditions, ii. _Indiana University Mathematics Journal_ , 26(1):81–93, 1977. 

- [Fen79] Neil Fenichel. Geometric singular perturbation theory for ordinary differential equations. _Journal of Differential Equations_ , 31:53–98, 1979. 

- [Fer17] Antoine Ferm´e. Invariants of knots, embeddings and immersions via contact geometry. 2017. 

- [FHT01] Y. Felix, S. Halperin, and J.C. Thomas. _Rational Homotopy Theory_ . Graduate Texts in Mathematics. Springer New York, 2001. 

- [FM71] Neil Fenichel and J. K. Moser. Persistence and smoothness of invariant manifolds for flows. _Indiana University Mathematics Journal_ , 21(3):193–226, 1971. 

- [FN20] Urs Frauenfelder and Robert Nicholls. The moduli space of gradient flow lines and Morse homology. _arXiv preprint arXiv:2005.10799_ , 2020. 

- [FW22a] Urs Frauenfelder and Joa Weber. Lagrange multipliers and adiabatic limits i. _arXiv preprint arXiv:2210.11221_ , 2022. 

- [FW22b] Urs Frauenfelder and Joa Weber. Lagrange multipliers and adiabatic limits ii. 2022. [Gao20] Honghao Gao. Simple sheaves for knot conormals. _Journal of Symplectic Geometry_ , 18(4):1027–1070, 2020. 

- [GKM[+] 99] Tom´aˇs Gedeon, Hiroshi Kokubu, Konstantin Mischaikow, Hiroe Oka, and James F. Reineck. The Conley index for fast-slow systems i. one-dimensional slow variable. _Journal of Dynamics and Differential Equations_ , 11:427–470, 1999. 

- [GL89] Cameron McA. Gordon and John S Luecke. Knots are determined by their complements. _Journal of the American Mathematical Society_ , 2:371–415, 1989. 

- [GM12] M. Goresky and R. MacPherson. _Stratified Morse Theory_ . Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge / A Series of Modern Surveys in Mathematics. Springer Berlin Heidelberg, 2012. 

- [GP10] V. Guillemin and A. Pollack. _Differential Topology_ . AMS Chelsea Publishing. AMS Chelsea Pub., 2010. 

- [GPS18] Sheel Ganatra, J. F. Pardon, and Vivek V. Shende. Sectorial descent for wrapped Fukaya categories. _Journal of the American Mathematical Society_ , 2018. 

- [GWdPL76] C. G. Gibson, Klaus Wirthm¨uller, Andrew du Plessis, and Eduard Looijenga. Topological stability of smooth mappings. Springer, 1976. 

- [Han08] Geiges Hansj¨org. _An introduction to Contact Topology_ . Cambridge University Press, 2008. [Has17] Boris Hasselblatt. Ergodic Theory and negative curvature. Springer, 2017. 

- [Hat19] Allen Hatcher. _Algebraic Topology_ . Cambridge University Press, 2019. 

- [Hir97] Hirsch. _Differential Topology_ . Springer, 1997. 

- [HSD04] M.W. Hirsch, S. Smale, and R.L. Devaney. _Differential Equations, Dynamical Systems, and an Introduction to Chaos_ . Pure and Applied Mathematics - Academic Press. Elsevier Science, 2004. 

- [Hsu15] Ting-Hao Hsu. _A geometric singular perturbation theory approach to viscous singular shocks profiles for systems of conservation laws_ . Phd thesis, The Ohio State University, 2015. 

- [Hur12] David E. Hurtubise. Three approaches to Morse-Bott homology. _African Diaspora Journal of Mathematics_ , 2012. 

- [Jon95] Christopher Jones. Geometric singular perturbation theory. Springer, 1995. 

- [JT09] Christopher Jones and Siu-Kei Tin. Generalized exchange lemmas and orbits heteroclinic to invariant manifolds. _Discrete and Continuous Dynamical Systems - Series S_ , 2:967–1023, 2009. 

- [Kar19] Cecilia Karlsson. A note on coherent orientations for exact Lagrangian cobordisms. _Quantum Topology_ , 11(1):1–54, 2019. 

- [KF19] Otto Koert and Urs Frauenfelder. _Restricted three-body problem and Holomorphic curves_ . Birkhauser, 2019. 

- [Kli95] Wilhelm P.A. Klingenberg. _Riemannian Geometry_ . De Gruyter, Berlin, New York, 1995. 

- [Kue15] Christian Kuehn. Multiple time scale dynamics. Springer, 2015. 

- [Lee13] John M. Lee. _Introduction to smooth manifolds_ . Springer, 2013. 

- [Lek13] Yankı Lekili. Heegaard–Floer homology of broken fibrations over the circle. _Advances in Mathematics_ , 244:268–302, 2013. 

- [Lok18] Elizaveta Lokteva. On smooth knots and tangent lines. 2018. 

- [Mat12] John Mather. Notes on topological stability. _Bulletin of the American Mathematical Society_ , 2012. [Maz25] Thibaut Mazuir. Higher algebra of _A∞_ and Ω _BAs_ -algebras in Morse theory I. _Higher Structures_ , 9(1):88–178, May 2025. 

- [Mes16] Stephan Mescher. Perturbed gradient flow trees and _A∞_ -algebra structures on morse cochain complexes, 2016. 

- [MJN00] Jiˇr´ı Matouˇsek and Jaroslav Neˇsetˇril. Kapitoly z diskr´etn´ı matematiky. Karolinum, 2000. 

- [Moi52] Edwin E. Moise. Affine structures in 3-manifolds: V. The Triangulation Theorem and hauptvermutung. _Annals of Mathematics_ , 56(1):96–114, 1952. 

- [MS12] Dusa MacDuff and Dietmar Salamon. _J-holomorphic curves and Symplectic Topology_ . American Math. Soc., 2012. 

- [MS17] Dusa McDuff and Dietmar Salamon. _Introduction to Symplectic Topology_ . Oxford University Press, 2017. 

- [Muk15] Amiya Mukherjee. _Differential Topology_ . Hindustan Book Agency, 2015. 

- [Nad17] David Nadler. Arboreal singularities. _Geometry & Topology_ , 21(2):1231–1274, 2017. 

195 

- [Nel70] Edward Nelson. _Topics in Dynamics I: Flows_ . Princeton University Press, 1970. 

- [Ng04] Lenhard Ng. Framed knot contact homology. _arXiv preprint math/0407071_ , 2004. 

- [Ng05a] Lenhard Ng. Knot and braid invariants from contact homology I. _Geometry & Topology_ , 9(1):247– 297, 2005. 

- [Ng05b] Lenhard Ng. Knot and braid invariants from contact homology II. _Geometry & Topology_ , 9(3):1603–1637, August 2005. 

- [Nie81] Lars Tyge Nielsen. Transversality and the inverse image of a submanifold with corners. _Mathematica Scandinavica_ , 49:211–221, 1981. 

- [nLa25] nLab authors. cyclic order. `https://ncatlab.org/nlab/show/cyclic+order` , February 2025. Revision 17. 

- [NP20] Walter Neumann and Anne Pichon. Introduction to Lipschitz Geometry of singularities. _Lecture Notes in Mathematics_ , 2020. 

- [Oh15] Yong Geun Oh. Symplectic Topology and Floer homology. Cambridge University Press, 2015. 

- [Oka24] Yukihiro Okamoto. Legendrian non-isotopic unit conormal bundles in high dimensions. _arXiv preprint arXiv:2410.15936_ , 2024. 

- [Oka25] Yukihiro Okamoto. Toward a topological description of Legendrian contact homology of unit conormal bundles. _Algebraic & Geometric Topology_ , 25(2):951–1027, May 2025. 

- [Pap57] C. D. Papakyriakopoulos. On Dehn’s lemma and the asphericity of knots. _Annals of Mathematics_ , 66(1):1–26, 1957. 

- [PdM82] Jacob Palis and Welington de Melo. Geometric theory of dynamical systems. 1982. 

- [Pei67] Mauricio Matos Peixoto. On an approximation theorem of Kupka and Smale. _Journal of Differential Equations_ , 3:214–227, 1967. 

- [Pet24] Andreas Petrak. Definition of the cord algebra of knots using Morse Theory. _Algebraic & Geometric Topology_ , 24(6):2971–3042, Oct 2024. 

- [PT93] Jacob Palis and Floris Takens. Hyperbolicity and sensitive chaotic dynamics at homoclinic bifurcations : fractal dimensions and infinitely many attractors. Springer, 1993. 

- [Rol03] D. Rolfsen. _Knots and Links_ . AMS Chelsea Publishing Series. AMS Chelsea Pub., 2003. 

- [RS93] Joel Robbin and Dietmar Salamon. The Maslov index for paths. _Topology_ , 32(4):827–844, 1993. 

- [RV14] T. O. Rot and R. C. A. M. Vandervorst. Morse–Conley–Floer homology. _Journal of Topology and Analysis_ , 06(03):305–338, June 2014. 

- [Sal85] Dietmar Salamon. Connected simple systems and the Conley index of isolated invariant sets. _Transactions of the American Mathematical Society_ , 291(1):1–41, 1985. 

- [Sal90] Dietmar A. Salamon. Morse Theory, the Conley index and Floer homology. _Bulletin of The London Mathematical Society_ , 22:113–140, 1990. 

- [Sch93] Matthias Schwarz. _Morse Homology_ . Springer, 1993. 

- [Sch08] Stephen Schecter. Exchange lemmas 2: General exchange lemma. _Journal of Differential Equations_ , 245:411–441, 2008. 

- [She19] Vivek Shende. The conormal torus is a complete knot invariant. In _Forum of Mathematics, Pi_ , volume 7, page e6. Cambridge University Press, 2019. 

- [Shi67] Leonid Pavlovich Shilnikov. Existence of a countable set of periodic motions in a four-dimensional space in an extended neighborhood of a saddle-focus. In _Doklady Akademii Nauk_ , volume 172, pages 54–57. Russian Academy of Sciences, 1967. 

- [Sma61] Stephen Smale. On gradient dynamical systems. _Annals of Mathematics_ , 74:199, 1961. 

- [Spi] Michael Spivak. _A comprehensive introduction to Differential Geometry, vol. 2_ . Publish or Perish. 

- [Ste51] Norman Steenrod. _The Topology of Fibre Bundles. (PMS-14)_ . Princeton University Press, 1951. [SX14] Stephen Schecter and Guangbo Xu. Morse Theory for Lagrange multipliers and adiabatic limits. _Journal of Differential Equations_ , 257(12):4277–4318, 2014. 

- [Szm91] Peter Szmolyan. Transversal heteroclinic and homoclinic orbits in singular perturbation problems. _Journal of Differential Equations_ , 92:252–281, 1991. 

- [Tie08] Heinrich Tietze. Uber die topologischen invarianten mehrdimensionaler mannigfaltigkeiten.[¨] _Monatshefte f¨ur Mathematik und Physik_ , 19:1–118, 1908. 

- [Tro78] David Vincent Trotman. Stability of transversality to a stratification implies Whitney (a)regularity. _Inventiones mathematicae_ , 50:273–277, 1978. 

- [Web99] Joa Webber. J-holomorphic curves in cotangent bundles and the heat flow. _PhD Thesis, TU Berlin_ , 1999. 

- [Wig88] Stephen Wiggins. Global bifurcations and chaos. Springer, 1988. 

- [Wig94] Stephen Wiggins. Normally hyperbolic invariant manifolds in dynamical systems. Springer, 1994. 

196 

