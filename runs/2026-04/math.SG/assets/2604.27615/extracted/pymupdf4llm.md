# **Monodromy action of mirror stops for toric Calabi-Yau surfaces** 

Michela Barbieri, Andrew Hanlon, Jeff Hicks 

## **Abstract** 

Mirror symmetry predicts an action by the fundamental group of a conjectural stringy K¨ahler moduli space on the derived category of an algebraic variety. For a toric variety, a model for this space is understood, but constructing the action is still an open problem in general. We propose that this action can be studied on the _A_ -side via a moduli space of Legendrians isotopic to the FLTZ Legendrian. For the _An−_ 1 singularity, we construct an annular braid-group action on the corresponding partially wrapped Fukaya category by exact autoequivalences. The standard braid subgroup recovers the Seidel–Thomas action on the derived category, while the additional annular generator corresponds to tensor product with _O_ ( _−_ 1). 

We additionally extend the Floer theoretic approach to homological mirror symmetry for toric varities to the setting of semiprojective toric Deligne-Mumford stacks over an arbitrary field. 

## **1 Introduction** 

Homological mirror symmetry is a predicted duality between certain symplectic and complex manifolds called mirror pairs. Broadly, a mirror pair consists of a symplectic manifold ( _X, ωX_ ), a complex manifold ( _X, J_[ˇ] _X_ ˇ[), and a dictionary between certain symplectic invariants of] _[ X]_[and algebro-] geometric invariants of _X_[ˇ] . For historical reasons arising from string theory, the symplectic geometric data is called the “ _A_ -side” while the algebro-geometric data is called the “ _B_ -side”. In many cases, mirror symmetry is an involution in the sense that both sides of the correspondence carry mutually mirror symplectic and complex structures. 

**==> picture [342 x 115] intentionally omitted <==**

**----- Start of picture text -----**<br>
( X, ωX , JX ) (  X, ω [ˇ] X  ˇ [, J] X [ ˇ] [)]<br>Symplectic Invariants Fuk( X, ωX ) Fuk(  X, ω [ˇ] X  ˇ [)]<br>Algebraic Invariants D [b] ( X, JX ) D [b] (  X, J [ˇ] X  ˇ [)]<br>**----- End of picture text -----**<br>


In this paper, we will focus on the correspondence Fuk( _X, ωX_ ) _↔ D[b]_ ( _X, J_[ˇ] _X_ ˇ[).][Here,][Fuk(] _[X, ω][X]_[)] denotes a Fukaya-type _A∞_ category of Lagrangians in _X_ (wrapped/partially wrapped as appropriate), and _D[b]_ ( _X, J_[ˇ] _X_ ˇ[)][denotes][the][bounded][derived][category][of][coherent][sheaves][on] _[X]_[ˇ][.][A][further] expectation of the theory is that this duality is defined over families of symplectic and complex manifolds so that we have an identification of the moduli spaces of structures on _X_ and _X_[ˇ] : 

**==> picture [104 x 13] intentionally omitted <==**

1 

This already indicates that the symplectic story needs to be expanded, as the moduli space of complex structures itself naturally carries a complex structure, while the moduli space of symplectic structures on _X_ is a real manifold locally identified with _H_[2] ( _X,_ R). To account for this discrepancy, the space _Mω_ should be replaced with the conjectural “stringy K¨ahler moduli space” (SKMS), which complexifies the moduli space of symplectic structures on _X_ . In examples, we can define proxies for the SKMS (see Section 2.2 for an overview). 

While Fuk( _X, ωX_ ) depends only on the symplectic structure on _X_ , a choice of complex structure _JX_ on _X_ enhances Fuk( _X, ωX_ ) with additional structure. At the most concrete level, the definition of Fuk( _X, ωX_ ) at the chain level requires a choice of almost complex structure. The conjectured existence of a stability condition on Fuk( _X, ωX_ ) arising from a _JX_ -holomorphic volume form on _X_ is an algebraic shadow of this additional data. On the _B_ -side, we have a similar appearance of stability conditions on categories, arising from a choice of K¨ahler form _ωX_ ˇ[on] _[X]_[ˇ][.][This][points][to][a] subtle interplay between the complex (resp. K¨ahler) moduli space and the Fukaya category of _X_ (resp. derived category of _X_[ˇ] ). This leads to the following question. 

**Question 1.1** ([Seg11; DW25] and others; see also the survey [Spe23])[ˇ] **.** _Does there exist a local system of Fukaya categories (resp. derived categories of coherent sheaves) over M[X] J[(resp.][M] Xω_[ ˇ] _[)?]_ 

The difficulty of the question is compounded by a lack of rigorous definition of _MXω_[ˇ][and technical] limitations in the definition of Fuk( _X, ωX_ ). Even defining a local system of derived categories is challenging [PPS25]. In practice, we can use heuristics from mirror symmetry to guess _M[X] J_[,][and] then look for interesting actions of _π_ 1( _M[X] J[,]_[ (] _[X, J][X]_[))][on][Fuk(] _[X, ω][X]_[)][and/or] _[D][b]_[( ˇ] _[X, J] X_[ ˇ][)][via][derived] autoequivalences (up to natural isomorphism). This provides an algebraic description of a local system of categories. The seminal example of this action is given in [ST01] when _X_[ˇ] is the _An−_ 1- singularity. Seidel and Thomas produced novel autoequivalences on the _B_ -side—called spherical twists—by exhibiting a configuration of Lagrangian spheres on an _A_ -side mirror and studying the symplectic Dehn twists around these spheres. The braiding of symplectic Dehn twists manifests itself as a braid relation among these autoequivalences of _D[b]_ ( _X_[ˇ] ). 

When _X_[ˇ] is a toric variety, there are explicit descriptions of a space of Laurent polynomials whose fundamental group should act on the derived category. We will describe the space briefly here and refer to Section 2.1.2 and the survey [Spe23][ˇ] for more details. Namely, the _B_ -side incarnation of Question 1.1 can be interpreted as the following conjecture. 

**Conjecture 1.2** (Toric HMS monodromy conjecture) **.** _There is an action_ 

**==> picture [325 x 29] intentionally omitted <==**

_where d is the number of rays in the fan of X_[ˇ] _, T is an algebraic torus of rank equal to_ dim( _X_[ˇ] ) _, and V_ ( _EA_ ) _is a hypersurface cut out by the principal A-determinant of a matrix A determined by the toric GIT problem._ 

However, we note that [DS15, Remark 2.8] points out that the space on the left side of (1), which we will denote by **FIPS** as in (2), should merely map to, but not coincide with, the SKMS. In this paper, we propose that another stand-in for the toric SKMS is the moduli space of piecewise Legendrians isotopic to the FLTZ stop mirror to _X_[ˇ] (see Definition A.1). Although this space of Legendrians is much larger, we note that the fundamental group on the left side of (1) is already difficult to compute in general, which is part of what makes Conjecture 1.2 challenging (see [Bar26]), 

2 

and we hope that the Legendrian moduli space at least has combinatorially describable generators. The main contribution of this paper is to verify that proposal for the _An−_ 1 singularity by exhibiting a family of Fukaya categories over such a moduli space of Legendrian stops naturally inducing a braid group action. 

## **1.1 Results** 

Let _X_[ˇ] _n_ be the _An−_ 1 singularity, understood as the toric stack [C[2] _/_ Z _n_ ], where the action of a primitive _n_ -th root of unity _ζ_ is given by ( _z_ 1 _, z_ 2) _�→_ ( _ζz_ 1 _, ζ[n][−]_[1] _z_ 2). We study a moduli of stops version of categorical monodromy for this example. On the _A_ -side, we work with _X_ = _T[∗] T_[2] and the FLTZ stop Λ _n ⊂ Y_ = _∂∞X_ . We use the Floer-theoretic approach to toric HMS in Appendix A to identify the resulting partially wrapped Fukaya category with _D[b]_ ( _X_[ˇ] _n_ ) (see Section 2.1 for a discussion of other approaches to toric HMS). Rather than varying a Landau–Ginzburg potential, we vary the stop itself inside the component of the stop moduli space consisting of Legendrians isotopic to Λ _n_ . To make that component concrete, we use an explicit graph model in a cylinder and then pass to Legendrian lifts which lie in a moduli space denoted _L[emb]_ Λ _n_[(] _[Y]_[ )][(see][Definition][3.7).] 

The first main result is a colloquial summary of Theorem 4.1 proved in Section 4. 

**Theorem A** (Paraphrase of Theorem 4.1) **.** A smooth path in _L[emb]_ Λ _n_[(] _[Y]_[ )][determines][an][exact][La-] grangian correspondence between the partially wrapped Fukaya categories at its endpoints. These correspondences depend only on the endpoint-fixed homotopy class of the path and are compatible with concatenation. Consequently, _π_ 1( _L[emb]_ Λ _n_[(] _[Y]_[ ))][acts][on] _[H]_[0] _[W]_[(] _[X,]_[ Λ] _[n]_[).] 

The precise theorem constructs the underlying correspondences and proves the stop-avoidance and composition properties needed for this action. 

Our second main result identifies the annular braid group inside the same stop moduli space. 

**Theorem B** (Corollary 3.12) **.** There is an inclusion 

**==> picture [114 x 14] intentionally omitted <==**

induced by explicit annular braid loops in the graph model, where _Bn,_ 1 is the braid group with _n_ uncolored strands and one distinguished strand. 

The proof combines explicit braid loops with a weighted Voronoi construction, which assigns to a configuration of points a canonical area-one planar graph, and then carries these graphs to Legendrian stops by the lift construction. 

Combining Theorems A and B with the HMS equivalence Theorem A.3 gives the following consequence. 

**Corollary C.** The action of _Bn,_ 1 on _H_[0] _W_ ( _X,_ Λ _n_ ) induces an action of _Bn,_ 1 on _D[b]_ ( _X_[ˇ] _n_ ) by exact autoequivalences. Its restriction to the subgroup _Bn ⊂Bn,_ 1 recovers the Seidel–Thomas braid action, and the extra generator _ρ_ acts by tensor product with _O_ ( _−_ 1). 

The identification of the braid generators with Seidel–Thomas twists is proved in Section 5. The description of _ρ_ is a generalization of the toric line bundle monodromy action in [Han19; HH22] to toric Deligne–Mumford stacks. This generalization of the line bundle monodromy action, in turn, relies on extending the Floer-theoretic proof of toric HMS to Deligne–Mumford stacks, as outlined in Appendix A. 

We also use the same stop moduli picture to read off changes in the Bondal–Thomsen collection (Section 5.2), to describe equivalences between VGIT chambers (Section 5.3), and to study partial resolutions of the _An−_ 1 singularity (Section 5.4). 

3 

## **1.2 Related results** 

This paper adds to the considerable body of mathematics analyzing the mirror monodromy action. Even the study of the toric case (Conjecture 1.2) has received considerable attention for which we do not attempt to give a comprehensive overview. We again note the braid group action in Corollary 5.1 was first constructed in [ST01]. The largest class of toric varieties for which Conjecture 1.2 is proven is the class of quasi-symmetric GIT quotients [HLS20]. 

When restricting to the context of stringy K¨ahler moduli space actions compatible with homological mirror symmetry for toric varieties, the following works are perhaps the most closely related to this paper. 

- The simplest part of the conjectural action (1) comes from a real torus in **FIPS** . The action of the fundamental group of this real torus is mirror to tensoring by line bundles as shown in [Han19] (see also [TWZ19; HH22; She22; BW25]). In many ways, our results can be seen as generalizations of the explicit construction of Hamiltonians exhibiting this action, which can be equivalently reformulated as isotopies of stops. 

- Spenko[ˇ] and Van den Bergh have proven the restriction of Conjecture 1.2 to toric boundary divisors in [SVdB24].[ˇ] They construct the action first on the _A_ -side by considering families of fibers of Hori-Vafa potentials and their wrapped Fukaya categories and then apply homological mirror symmetry [GS22] to pass to the _B_ -side. We note that they do not pass to the FLTZ stop and extending their approach to obtain Conjecture 1.2 itself would require a technical analysis of partially wrapped Fukaya categories associated to Hori-Vafa potentials of a rather different nature than that required here for families of Legendrian stops. 

- In the quasi-symmetric setting, [Zho25; HZ22] give an _A_ -side description of the action in [HLS20] using the microlocal sheaf model for the Fukaya category of ( _X,_ ΛΣ). Notably, they produce families of (piecewise linear) FLTZ skeleta that induce the action. However, we note that their arguments rely on the window equivalences of [Seg11; HL15; BFK19] and, in contrast to the results here, do not produce the action from the topology of the moduli space. 

   - For some examples, a similar construction, again using window technology in the proofs, is given in [DK21] where the autoequivalences are put in the context of perverse schobers [KS14; BKS18], which are meant to fill in the local system of categories over the discriminant locus. 

## **1.3 Conjectures and Questions** 

There are several directions that we leave unexplored. For example, we work with the space of stops with embedded Lagrangian projection to make a combinatorial comparison to the space of embedded graphs, but there is no geometric reason to constrain to this set. In fact, we conjecture: 

**Conjecture 1.3.** _Let_ Σ _be a fan so that X_[ˇ] Σ _is a toric Calabi-Yau. The Fayet-Iliopoulos parameter space (2) is homotopy equivalent to L_ ΛΣ( _Y_ ) _._ 

Conjecture 1.3 has a parallel combinatorial version in dimension two; we could not find a proof of this (seemingly simpler) statement in the literature: 

**Conjecture 1.4.** _The moduli space Nn_ (R[2] ) _of planar graphs with n bounded faces is homotopy equivalent to_ uConf _n_ (R[2] ) _, the configuration space of n unlabeled points in the plane._ 

4 

The complex structure moduli space is believed to be related to the Bridgeland stability manifold [Bri09a]. The relationship to Bridgeland stability conditions has been made explicit in the setting of 3-fold flops [DW25] and Dynkin diagrams [Bri09b], the latter covering the setting of this paper. 

**Question 1.5.** _Can the moduli space of mostly Legendrian stops be related in any way to the space of stability conditions on the partially wrapped Fukaya category? We note that a generic choice of mostly Legendrian stop gives a preferred choice of generators of the partially wrapped Fukaya categories supported on (small negative pushoffs of) cotangent fibers. For the FLTZ stop, these generators coincide with the Bondal-Thomsen line bundles. Thus, it is also natural to ask whether there is a (geometric) stability condition on the partially wrapped Fukaya category for which the Bondal-Thomsen generators are stable._ 

_Remark_ 1.6 _._ There is precedent for studying homological mirror symmetry where the _B_ -side is not K¨ahler (and does not even admit a symplectic structure). For instance, HMS for the Hopf surface is studied in [War21]. In that work, the _A_ -side category can be understood to be a generalization of the partially wrapped Fukaya category to the non-exact setting. In particular, the moduli space of stops is still a reasonable object. Should we interpret the stop moduli space in the non-K¨ahler setting as a stringy “symplectic” moduli space on the mirror? 

## **1.4 Outline** 

The remainder of the paper is organized as follows. Section 2 is an in-depth literature review covering both _A_ -side and _B_ -side perspectives on the toric SKMS; it also contains a worked example of how these different viewpoints fit together in the case of the _An−_ 1 singularity. We use some notation from this review throughout the paper. 

The new mathematical arguments are contained in Sections 3 to 5. In Section 3, we provide the geometric heart of this paper: a definition of the moduli space of Legendrian stops and the identification of the braid group inside the fundamental group of this moduli space. Section 4 contains a rather technical construction that allows us to lift paths in this moduli space to symplectomorphisms of the corresponding stopped symplectic manifolds. While important to the main result, this section can be safely skipped by readers who are primarily interested in the geometric and algebraic aspects of the main theorem. 

The last section, Section 5, contains examples and applications; in particular, we examine how the action of the fundamental group of the moduli space of Legendrian stops on the _A_ -side translates through the mirror to the spherical and line bundle twists, provide a dictionary to the diagrammatic methods of the Bondal–Thomsen collection, and extend the result to obtain equivalences between VGIT chambers and actions on partial resolutions of the _An−_ 1 singularity. 

Finally, in Appendix A, we extend the Floer-theoretic proof of homological mirror symmetry for toric varieties to toric Deligne-Mumford stacks. We use only the simplest example of this result in this paper, the _An−_ 1 quotient stack, but have included the full result as it may be of future use to the community. 

## **1.5 Acknowledgements** 

We are grateful to Ed Segal for encouraging us to produce an _A_ -side moduli mirror whose monodromy induces variation of GIT. We thank Charlotte Bartram, Sheel Ganatra, Oleg Lazarev, Nick Sheridan, and Spela[ˇ] Spenko,[ˇ] for useful conversations, as well as the organizers of “Higher categorical methods in algebra and geometry” at which we were originally inspired to work on this 

5 

problem. We also thank Michael Wemyss for asking us about the partially resolved case, which led to Section 5.4. Finally, we thank Charlie Egan and Louis Theran for introducing us to Voronoi diagrams as a method to obtain a planar graph from a configuration of points. Some figures were created using PyPlot [Hun07]. 

AH was supported by the National Science Foundation through awards DMS-2549013 (previously as DMS-2412043) and DMS-2549038. JH was supported by EPSRC grants EP/V049097/1 and EP/Z53528X/1. 

## **2 A review of the Stringy K¨ahler moduli of toric mirrors** 

This section is a literature review and a source of motivation for the constructions in Sections 3 and 4. The proofs later in the paper do not rely on the heuristic open-Gromov–Witten discussion below, except through the standard background and the precise references explicitly cited there. 

The homological mirror symmetry framework for toric varieties is well established [Abo06; Fan+11; _X_ ˇΣ are trivial,Kuw20].as Anare advantagethe symplecticof thismodulisettingofisthethatsymplecticthe complexmirrormoduli _X_ . ofHowever,the torictheDMstringystack K¨ahler moduli space _MXω_[ˇ][of][the][toric][variety][may][be][non-trivial.] 

There is no rigorous definition of the stringy K¨ahler moduli space _MXω_[ˇ][of][a] _[B]_[-side][model] [Bri09a]; in this section, we provide an extended review of the literature with an emphasis on the moduli space of _A_ -side Landau-Ginzburg superpotentials on the mirror (Section 2.1) and its relationship to variation of GIT (Section 2.2). In Sections 2.3 and 2.4 we give two worked-out examples of the construction of the SKMS of the _A_ 1 singularity and the braid group action on the derived category of the _An−_ 1 singularity. 

## **2.1 Moduli of** _A_ **-side Landau-Ginzburg models** 

We first give an overview of the symplectic motivation. For this section, a smooth toric variety is determined by the data of a smooth fan Σ _⊂ N_ R = _N ⊗_ R. At the level of precision employed in this literature review, one may replace a toric variety with a smooth toric stack (see Appendix A). We will use _n_ to denote the rank of _N_ . A mirror to a toric variety _X_[ˇ] Σ defined from this data is a symplectic Landau-Ginzburg model ( _X, ωX , W_ Σ _[X]_[),][where] _[X]_[is][symplectomorphic][to] _[T][ ∗][T][ n]_[with] the standard symplectic form and _W_ Σ _[X]_[:] _[X][→]_[C][is][a][superpotential][determined][by][the][data][of][the] fan Σ. We note that the superpotential is not unique and, by asking that _W_ Σ _[X]_[be][holomorphic,] the choice of superpotential can be understood to reflect the variation of the complex structure of _X_ . There are several recipes for constructing a potential _W_ Σ _[X]_[,][but][one][method][that][makes][all] choices explicit arises from considering SYZ mirror symmetry and open Gromov-Witten theory. When constructed in this fashion, the choices are determined by the data of a K¨ahler structure on the mirror (see [Aur08, Section 2.2] for a summary of this philosophy). More specifically, a choice of K¨ahler form on _X_[ˇ] determines a moment map _X_[ˇ] _→_ ∆ _⊂_ R _[n]_ with generic fibers being _n_ -tori, _T[n]_ . To our knowledge, this construction has not been rigorously worked out in the literature (see [Aur07, Section 4.2] for a discussion on the current state of this viewpoint). For us, the following heuristic suffices: we think of the complex structure induced on _X_ as identifying _X_ with the _subset_ Log _[−]_[1] (∆) _⊂_ (C _[∗]_ ) _[n]_ resembling an affinoid domain. The open Gromov-Witten potential _W_ Σ _[X]_[also] depends on the choice of _ωX_ ˇ[.][This][is][a][formal][power][series][with] _[real]_[coefficients][which][provides] an _ωX_ ˇ[-weighted][count][of][pseudoholomorphic][disks][in] _[X]_[ˇ][with][boundary][on][SYZ][tori.] Ignoring possible issues of convergence, the resulting function _W_ Σ _[X]_[:] _[X][→]_[C][is][holomorphic][with][respect][to] 

6 

the complex structure on _X_ (also determined by _ωX_ ˇ[).][In][practice,][these][power][series][are][difficult] to compute when _X_[ˇ] is not Fano[1] . 

It is expected that equipping _X_[ˇ] with a complexified K¨ahler form corresponds to modifying the open Gromov-Witten potential so that it is a formal power series with _complex_ coefficients. It is unclear to us how — or even if — a complexified K¨ahler form on _X_[ˇ] corresponds to a modification of the complex structure on _X_ . However, since the _A_ -model is determined by _W_ Σ _[X]_[(and][only] uses the complex structure as auxiliary data), one viewpoint is that the moduli space of suitably complexified open Gromov-Witten potentials _M[X] J_[is the appropriate] _[ A]_[-side analogue to the stringy] K¨ahler moduli space _MXω_[ˇ][.][Without dwelling on the mathematical gaps in the story,][let us describe] some expected features of this moduli space in a worked example (Section 2.1.1) and give a purely algebraic prescription for this moduli space in the setting of toric varieties (Section 2.1.2). 

## **2.1.1 A local system of categories over the SKMS: the projective line** 

We briefly recall the construction of [Han19, Section 1.1]. Consider _X_[ˇ] Σ = P[1] . The open GromovWitten potential is _W_ Σ _[X]_[(] _[z]_[)][=] _[z]_[ +][ex][p(] _z[−][α]_[)] , where _α_ corresponds to the symplectic area of P[1] . For every _c ∈_ C _[∗]_ we have a complexified potential: 

**==> picture [88 x 39] intentionally omitted <==**

We therefore have a “local system” of symplectic Landau-Ginzberg models (C _[∗] , W_ Σ _,c_ ) over C _[∗]_ . By associating to each symplectic LG model a Fukaya category, we expect to build a local system of categories over C _[∗]_ . The model for the Fukaya category with the cleanest description in this setting is the Fukaya-Seidel category, whose objects are Lagrangian submanifolds of C _[∗]_ that fiber over the positive real axis under _W_ Σ _[X]_[outside][of][a][compact][set.][By][definition,][a][generating][set][for][the] Fukaya-Seidel category is prescribed by choosing paths in the base C from the critical values of the potential _W_ Σ _[X]_[which][eventually][agree][with][the][positive][real][axis,][and][taking][the][Lagrangian][lifts] (thimbles) of these paths. If we take the loop _c_ = exp( _iθ_ ) for _θ ∈_ [0 _,_ 2 _π_ ], the critical values _±_ 2 _[√] c_ twist around each other, and we can “follow” the Lagrangians through this loop (see Figure 1). 

**==> picture [222 x 69] intentionally omitted <==**

**----- Start of picture text -----**<br>
× ×<br>× ×<br>× ×<br>**----- End of picture text -----**<br>


Figure 1. A loop of potentials _W_ Σ _[X]_[(] _[z]_[)][=] _[z]_[+][exp(] _[iθ]_[)] _[z][−]_[1][corresponding][to][an][autoequivalence] of Fukaya-Seidel categories. The figures represent the critical values of the potential in C. The red and blue paths lift to Lagrangian submanifolds, and are twisted as we rotate the parameter exp( _iθ_ ) _∈ S_[1] . The green path corresponds to a Lagrangian sphere in _X_ ; this autoequivalence can also be described in terms of the spherical twist around this object. 

> 1These potentials have been computed for toric CY surfaces [Cha+17, Theorem 4.2], the case that we are interested in. 

7 

Under the HMS dictionary, the resulting autoequivalence of the Fukaya-Seidel category is iden- _−_ tified with _−⊗O_ ( 1). This story was generalized in [Han19], where it was shown that monodromy arising from rotation of the arguments of the monomials in the Hori-Vafa potential could be used to construct the mirror action to tensor product by a line bundle for the monomial-admissible Fukaya-Seidel category. 

Something unique to this example (and not present in the case of HMS for P _[n]_ ) is that there is a Lagrangian _S_[1] which parameterizes the unit circle in C _[∗]_ . The autoequivalence of the Fukaya-Seidel category built by monodromy over the SKMS can be obtained by taking the symplectic Dehn twist around this Lagrangian sphere. This induces a spherical twist functor on the Fukaya-Seidel category. 

## **2.1.2 Hori-Vafa potential and FIPS** 

In practice, homological mirror symmetry for toric varieties does not use the open Gromov-Witten potential, but rather one of several different substitutes — see Table 1 for a summary of these alternative approaches as well as the current state of HMS for each model. 

One of the most commonly used substitutes — the Hori-Vafa potential [HV00]— allows one to define a purely formal stand-in for the SKMS via “complex variation” of the coefficients of the superpotential. For a fan Σ, it is defined as 

**==> picture [116 x 27] intentionally omitted <==**

Here, we have used the identification of characters on the _A_ -side with cocharacters on our input _B_ -side. 

_Remark_ 2.1 _._ The Hori-Vafa potential can be viewed as a “first-order” approximation of the open Gromov-Witten potential. To see this relation, we observe that there is a connection between the 1-dimensional cones of Σ and homology classes [ _ρ_ ] _∈ H_ 2( _X_[ˇ] Σ _, T[n]_ ; Z) (where _T[n]_ is the orbit of 1 in the algebraic torus). When _X_[ˇ] Σ is Fano and we let _cρ_ = exp( _−ω_ ([ _ρ_ ])), the Hori-Vafa and open Gromov-Witten potentials agree (subject to the domain of definition). In many other cases, the appearance of higher-order terms in the open Gromov-Witten potential doesn’t meaningfully alter the symplectic geometry of the symplectic Landau-Ginzburg model. For this reason, the literature frequently glosses over any potential discrepancies between these two potentials in the non-Fano case. 

To construct a “Stringy K¨ahler Moduli space” for this model, one takes the space of “valid” potentials _W_ HV _,_ Σ( _z_ ). Let _d_ denote the number of 1-dimensional cones of Σ, and let _n_ = rank( _N_ ); equivalently, in a linear toric GIT presentation with torus rank _r_ , one has _n_ = _d − r_ . The _d_ coefficients _cρ ∈_ C can vary, but not all coefficient choices are allowed. In particular, we must avoid those lying on _V_ ( _EA_ ), where _EA_ is the principal _A_ -determinant as defined and studied in [GKZ94], a higher-dimensional generalization of a discriminant. The Fayet-Iliopoulos Parameter Space ( **FIPS** ) is defined as the parameter space over which these potentials live: 

**==> picture [317 x 28] intentionally omitted <==**

where by construction there is a natural action of (C _[∗]_ ) _[n]_ = (C _[∗]_ ) _[d][−][r]_ via _A_ on the coefficients, which we quotient out. 

8 

|**Potential Data**|**State of HMS**|**Moduli of Potentials**|**Local Systems over Moduli space**|
|---|---|---|---|
|OGW Potential|No _A_-model defned<br>yet in this setting.|This model most accurately<br>captures the physical defni-<br>tion of the SKMS of ˇ_X_Σ.|No defned _A_-model|
|Hori-Vafa poten-<br>tial|After suitable defor-<br>mation to a tropical<br>limit, we have HMS<br>[Abo06].|By<br>defnition,<br>this<br>is<br>the<br>**FIPS**, which has a completely<br>combinatorial defnition|Due to the rigidity of the data used to defne FS-<br>category, it is difcult to construct parallel transport<br>maps. Parallel transports are known to exist on the<br>fber category [ˇSVdB24].|
|Monomial Admis-<br>sibility Data|HMS<br>proven<br>[Han19].|Moduli space by defnition is<br>the torus (_S_1)_|_Σ(1)_|_|There exists a local system of categories over the mod-<br>uli space, with autoequivalences mirror to twists by<br>line bundles.|
|FLTZ<br>Skeleton<br>(microlocal)|HMS<br>is<br>proven<br>[Fan+11; Kuw20]|Unclear how to construct the<br>moduli space from data|Under additional hypothesis, non-characteristic de-<br>formations of skeleta correspond to window derived<br>equivalences [Zho25; HZ22]|
|FLTZ<br>Skele-<br>ton<br>(partially<br>wrapped)|HMS<br>is<br>proven<br>[HH22].|Defnition 3.6|For variation of Legendrian stops [Syl19]. For FLTZ<br>stops, Theorem 4.1|
|SYZ<br>in<br>comple-<br>ment of smooth<br>anticanonical|HMS not yet proved<br>in this setting|No interesting moduli of LG<br>potential in this setting, but<br>now have non-trivial moduli<br>of complex structure|In some settings, the _A_-side mirror contains La-<br>grangian spheres [GM18], giving rise to spherical au-<br>toequivalences of the Fukaya category [ST01, Section<br>3e] via symplectic Dehn twist.|



Table 1. Different frameworks for HMS for toric varieties. 

It is worth noting that **FIPS** does not always coincide with the understanding of the stringy K¨ahler Moduli space as the complex structure moduli space; see [DS15, Remark 2.8]. The **FIPS** has the nice property of being a smooth Deligne-Mumford stack. 

## **2.2** _B_ **-side moduli via Toric Variation of GIT** 

Given the patchwork landscape of different _A_ -side Landau-Ginzburg models and approaches to defining the SKMS, we turn to the _B_ -side to look for corroborating evidence. Despite our lack of a formal definition of the _B_ -side SKMS, we can recover a shadow of this conjectural space through toric variation of GIT. 

Toric geometry is equivalent to the geometry of _linear toric Geometric Invariant Theory (GIT)_ problems, the simplest kinds of GIT problems. Linear toric GIT problems are given by an algebraic torus _T[∼]_ = (C _[∗]_ ) _[r]_ acting on a vector space _V_ = _[∼]_ C _[d]_ , where _r_ is the rank and _d_ is the dimension. After choosing bases for _T_ and _V_ , these actions are always given by 

**==> picture [356 x 12] intentionally omitted <==**

where _qij ∈_ Z are integers for _i ∈{_ 1 _, . . . , r}, j ∈{_ 1 _, . . . , d}_ . We obtain an _r × d_ integer matrix _Q_ = ( _qij_ ), called the _weight matrix_ whose columns _{qk}[d] k_ =1[are called] _[ weight vectors]_[.][GIT is an algebraic] framework for building “nice” quotients. In most cases, to obtain well-behaved quotients, we will have to remove some bad orbits (the unstable locus) with non-generic behaviour before taking the quotient. As a result, GIT quotients are not unique and depend on a choice of stability condition specifying the unstable locus we remove. In our setup, the stability condition is determined by a character _θ_ of _T_ , making our ‘stability space’ the character lattice _M_ = hom( _T,_ C _[∗]_ ) = _[∼]_ Z _[r]_ . There is an entirely combinatorial process which computes the unstable locus _Uθ ⊂_ C _[d]_ to be removed before forming the (stack) quotient [(C _[d] \ Uθ_ ) _/_ (C _[∗]_ ) _[r]_ ]; see, for instance, [CLS11, Chapter 14], or [CIJ18, Section 4] for a clear and brief introduction. 

The stability space _M_ has a wall-and-chamber decomposition. The chambers of the space correspond to stability conditions with the same unstable loci (and hence yield the same GIT quotients). A fundamental result is that these chambers are the interiors of the top-dimensional cones of a toric fan, often called the secondary or GKZ fan [CLS11, Chapter 14]. The GIT quotients corresponding to characters interior to the maximal cones of the GKZ fan are smooth toric DeligneMumford stacks as per [BCS05]. These are the only GIT quotients we will discuss, and from now on, when we say GIT quotients, we are referring to these. 

_Remark_ 2.2 _._ The stability condition space for toric linear GIT is naturally discrete, but admits a straightforward enhancement to a real manifold via symplectic geometry. Linear toric GIT can be recast as symplectic reduction [KN79], see also the survey [Woo10]. In this framework, the standard coordinatewise (C _[∗]_ ) _[d]_ -action on C _[d]_ restricts to a Hamiltonian action of ( _S_[1] ) _[d]_ , and the GIT action corresponds to a Hamiltonian action of ( _S_[1] ) _[r]_ . These Hamiltonian actions give us moment map projections _π_ 1 and _π_ 2: 

**==> picture [110 x 32] intentionally omitted <==**

where (under mild conditions on the action) ∆ _⊂ M_ R = _M ⊗_ Z R is the image of _p_ inside our continuous real enhancement of the GIT parameter space. Associated to a generic point _q ∈_ ∆, the symplectic reduction/quotient _X_[ˇ] _q_ := _π_ 2 _[−]_[1][(] _[q]_[)] _[/]_[(] _[S]_[1][)] _[r]_[carries][a][Hamiltonian][(] _[S]_[1][)] _[d][−][r]_[action][whose] 

10 

**==> picture [43 x 50] intentionally omitted <==**

**==> picture [43 x 50] intentionally omitted <==**

**==> picture [43 x 47] intentionally omitted <==**

**==> picture [43 x 43] intentionally omitted <==**

**==> picture [333 x 31] intentionally omitted <==**

**----- Start of picture text -----**<br>
M R<br>q <  0 q >  0<br>**----- End of picture text -----**<br>


Figure 2. Variation of GIT can also be understood in terms of varying the moment map parameter in symplectic reduction. Here, we look at the variation of symplectic reduction for the _A_ 1 singularity. 

moment polytope is _p[−]_[1] ( _q_ ). The combinatorial type of _p[−]_[1] ( _q_ ) varies with _q_ , as drawn in Figure 2. The different chambers of the GIT problem correspond to regions over which the combinatorial type of _p[−]_[1] ( _q_ ) is constant. 

## **2.2.1 Tropicalizations of the Hori-Vafa potential and VGIT chambers** 

The Hori-Vafa potential can also be read from the presentation of a toric Calabi-Yau variety via linear toric GIT. Consider the dual weight matrix _Q[∨]_ : Z _[r] →_ Z _[d]_ ; the cokernel _A_ : Z _[d] → N_ (where _N_ has rank _d − r_ and may have torsion) gives both the toric fans of the quotients and the form of the superpotential _W_ . We ignore any torsion part of _N_ , consider the remaining cokernel map _A_ , and by picking bases, we can view _A_ as a ( _d − r_ ) _× d_ matrix. We can describe _A_ by its set of column vectors _{ρi}_ , which correspond to the rays generating the 1-dimensional cones of Σ. The Hori-Vafa potential is now given by 

**==> picture [96 x 25] intentionally omitted <==**

The Calabi-Yau property implies that the convex hull _P ⊂_ R _[d][−][r]_ of the rays _{ρi}_ lies in an affine hyperplane. The compact polytope _P_ is called the _primary polytope_ , and coherent triangulations of _P_ give the fans of the GIT quotients by taking cones over the simplices of the triangulation [GKZ94, Chapter 7, Theorem 1.7]. By the same argument, one sees that the Hori-Vafa potential factors as _WA_ ( _z_ 1 _, . . . , zn_ ) = _z_ 1 _· fA_ ( _z_ 2 _, . . . , zn_ ). The Newton polytope of _fA_ is _P_ . When the tropicalization of _fA_ is a smooth tropical hypersurface, the tropical hypersurface is combinatorially dual to a triangulation of _P_ ; similarly, every choice of coherent triangulation for _P_ specifies a choice of coefficients for _fA_ with a dually-tessellated tropicalization. 

## **2.2.2 Derived autoequivalences on the** _B_ **-side** 

The previous section suggests that the VGIT parameter space is a “tropicalization” of the SKMS. Indeed, the **FIPS** naturally embeds into the _secondary toric stack_[2] , which is a toric DeligneMumford stack (in the sense of [BCS05]) whose fan is given by the secondary fan. Under this tropicalization map, fixed points in the toric variety associated to the secondary fan correspond, via the orbit-cone correspondence, to maximal cones (or chambers) of the secondary fan, and hence to 

> 2One way to see this is that the Newton polytope of the principal _A_ -determinant _EA_ is the secondary polytope, whose normal fan is the secondary fan. 

11 

GIT quotients. The intersections of arbitrarily small neighborhoods around these fixed points with **FIPS** are called _large complex structure limits_ (LCSLs), with one such LCSL for each GIT quotient. This gives us a “clean statement” of our expectation that there exists a local system of categories over the SKMS: the fundamental groupoid of **FIPS** , with basepoints chosen at the LCSLs of the GIT quotients, acts on the derived categories of the quotients via line bundle twists and certain equivalences known as _window equivalences_[3] , _D[b]_ ( _X_[ˇ] ) _→ D[b]_ ( _X_[ˇ] _[′]_ ). These window equivalences arise 

**==> picture [282 x 129] intentionally omitted <==**

Figure 3. A picture of **FIPS** = _[∼]_ C _[∗] \{_ 1 _}_ for the _A_ 1 singularity. The path _γ_ can be chosen to represent a ‘window’ equivalence _D[b]_ ( _X_[ˇ] geo) = _[∼] D[b]_ ( _X_[ˇ] stack) as per [Seg11]. There are countably infinitely many of these, and the choice is non-canonical. 

via the Artin stack [ _V/T_ ], as in the framework of [HL15], with explicit constructions developed in [Seg11; HLS16; BFK19; HLS20]. 

In fact, [HLS16] shows that composing a window equivalence with the inverse of another corresponds to a _spherical twist about a spherical functor_ , where a spherical functor is a generalization of the spherical objects introduced in [ST01]. 

**Definition 2.3.** [Huy06, Chapter 8] An object _E[•] ∈ D[b]_ ( _X_[ˇ] ) is called _spherical_ if 

1. _E[•] ⊗ ωX_ ˇ _[∼]_[=] _[ E][•]_[,][where] _[ω] X_[ ˇ][is][the][canonical][bundle,][and] 

2. 

**==> picture [242 x 33] intentionally omitted <==**

We define the _spherical twist TE •_ : _D[b]_ ( _X_[ˇ] ) _→ D[b]_ ( _X_[ˇ] ) about a spherical object to be the cone on the evaluation map: 

**==> picture [342 x 12] intentionally omitted <==**

where **R** Hom( _E[•] , F[•]_ ) denotes the derived Hom complex.[4] By [Huy06, Proposition 8.6], the spherical twist _TE •_ : _D[b]_ ( _X_[ˇ] ) _→ D[b]_ ( _X_[ˇ] ) about any spherical object _E[•] ∈ D[b]_ ( _X_[ˇ] ) is an autoequivalence. The conjecture may be rephrased as saying that the fundamental groupoid of **FIPS** , with basepoints chosen at the relevant large complex structure limits, acts on _D[b]_ ( _X_[ˇ] ) via spherical twists. While we do not give any details here, these spherical twists are explicitly determined by the GIT data, 

> 3Also referred to as grading restriction rules. 

> 4There are some technical issues with the definition of the spherical twist because taking cones is not functorial. We bypass any such issues because in our geometric context, where our triangulated category is the derived category of a DM stack, we can describe any spherical twist (even about a spherical functor) as a Fourier-Mukai transform. 

12 

and the expected representation can be described quite precisely. However, Conjecture 1.2 remains unproven even in the toric or abelian GIT setting. 

That said, partial results are known. For quasi-symmetric GIT problems (a special case of Calabi-Yau where _EA_ = 0 defines a hyperplane arrangement), Conjecture 1.2 was proven in [HLS20]. In addition, [Kit18] verified the conjectural representation when restricted to large radius paths in two-dimensional examples. The first author’s thesis [Bar26] studies Conjecture 1.2 for toric CalabiYau 3-folds of Picard rank 2 from this _B_ -side perspective. When the action of the torus _T_ on the vector space _V_ lands in _SL_ ( _V_ ) (i.e., the weight vectors sum to 0), the GIT quotients are Calabi-Yau (they have trivial canonical line bundle) and their derived categories are equivalent [HL15]. 

## **2.3 Worked Example: SKMS, VGIT, and FIPS for the** _A_ 1 **singularity** 

Suppose we have C _[∗]_ acting on C[3] with weight matrix _Q_ = ( _−_ 1 _,_ 2 _, −_ 1), i.e., 

**==> picture [150 x 13] intentionally omitted <==**

The stability space _M_ = _[∼]_ Z is an integer lattice of rank 1. We have two GIT quotients: 

**==> picture [251 x 34] intentionally omitted <==**

where _X_[ˇ] _stack_ denotes the GIT quotient for _θ >_ 0, while _X_[ˇ] _geo_ denotes the GIT quotient for _θ <_ 0. _θ_ = 0 is our wall. _X_[ˇ] _stack_ is a smooth stack associated to the _A_ 1 surface singularity, and _X_[ˇ] _geo_ is the crepant resolution of the _A_ 1 surface singularity. 

## **2.3.1** _A_ **-side moduli** 

We provide a non-rigorous but instructive example motivating the expectation that the Stringy K¨ahler moduli space is covered by charts corresponding to different toric stacks on the _A_ -side. The toric K¨ahler form on _X_[ˇ] _geo_ is determined completely by the value _α_ := _ωX_ ˇ[(][P][1][)] _[ ∈]_[R] _[>]_[0][,][and the open] Gromov-Witten potential is 

**==> picture [306 x 13] intentionally omitted <==**

While _W_ Σ _[X]_[is][a][priori][only][defined][on] _[X]_[,][it][can][be][extended][to][a][holomorphic][function][on][all] of (C _[∗]_ )[2] _⊃ X_ . The relationship between _X_ and the potential _W_ Σ _[X]_[can][be][loosely][understood] via tropicalization. Observe in Figure 4 that the bottom left-hand connected component of the complement of the amoeba approximates the moment polytope for ( _X, ω_[ˇ] _X_ ˇ[).][The][preimage][of][this] region under the Log map is (via our loose interpretation of [Aur07, Section 4.2]) the space _X_ . Continuing down this line of reasoning, we might charitably say that the fiber of _W_ Σ _[X]_[lives][“at][the] boundary” of _X_ . As _|α| →_ 0, we see several kinds of degeneration occurring: 

- The moment map of _K_ P1, as drawn in Figure 2, degenerates as the edge corresponding to the P[1] toric orbit shrinks to zero length. 

- The zero set of _W[[X]]_ 

   - _[[X]]_[a][double][root.] Σ[develops] 

- The combinatorial type of the tropicalization of _W_ Σ _[X]_[changes.] 

13 

**==> picture [181 x 181] intentionally omitted <==**

Figure 4. Tropicalization of the fiber of the open Gromov-Witten potential. The region highlighted in red approximates the moment polytope for _K_ P1 defined by the symplectic form such that _ωα_ (P[1] ) = _α_ . 

Note that, at this juncture, only positive values of _α_ arise from the mirror symmetry construction. Negative values of _α_ are recovered by considering the OGW invariants of toric stacks. In this example, a negative value of _α_ arises from the toric stack _X_[ˇ] _stack_ . Again, the open Gromov-Witten invariants come from counts of pseudoholomorphic curves with boundary on Lagrangian tori; to the best of our knowledge, the symplectic machinery has not been developed to provide a count of these _X_ ˇ _geo_ andcurves. _X_ ˇ _stack_ In hasthe beenclosedcheckedGromov-Witten[BG09, Corollaryinvariant3.4],setting,and correspondsthe agreementto settingof GWtheinvariantsparameteron exp( _α_ ) from _W_ Σ _[X]_[to] _[−]_[1.] 

As before, the symplectic viewpoint is agnostic to the sign of _α_ , and we may consider any nonzero (even complex) value of _α_ . The natural coordinate to parameterize this space is _c ∈_ C _[∗] \ {_ 1 _}_ , which is equal to exp( _α_ ) on the portion of the stringy K¨ahler moduli space parameterized by OGW invariants of _K_ P1 or C[2] _/_ Z2. Observe that the removed point _c_ = 1 corresponds to when _α_ = 0. We can then study the “variation of Landau-Ginzburg model” via tropicalization of the fiber, as drawn in Figure 5. 

_Remark_ 2.4 _._ When _X_[ˇ] Σ is a toric Calabi-Yau, there is another choice of _A_ -side mirror [CLL12] (for the setting of the _An−_ 1 singularity, this is described in [Cha+17]). If _W_ ( _x_ 1 _, . . . , xn_ ) is the open Gromov-Witten potential, the mirror can also be presented as the symplectic manifold 

**==> picture [288 x 12] intentionally omitted <==**

with Landau-Ginzburg potential _u_ . When presented in this manner, one can see in the _An−_ 1 example that _X_ contains an _An−_ 1 configuration of Lagrangian 2-spheres; more generally, the work of [GM18] constructs a similar configuration of Lagrangian 3-spheres in the setting of mirror symmetry for toric Calabi-Yau 3-folds. 

## **2.3.2** _B_ **-side moduli** 

On the _B_ -side, we understand from variation of GIT that the [A[2] _/_ Z2] stack and its resolution _K_ P1 fit into the same moduli space. 

14 

**==> picture [57 x 58] intentionally omitted <==**

**==> picture [58 x 58] intentionally omitted <==**

**==> picture [58 x 58] intentionally omitted <==**

**==> picture [58 x 58] intentionally omitted <==**

**==> picture [57 x 58] intentionally omitted <==**

**==> picture [142 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
α <  0 α >  0<br>**----- End of picture text -----**<br>


Figure 5. Variation of the tropicalization. Suggestively, we draw the real parameter space for _α_ to match that of the VGIT parameter space from Figure 2. In the left domain, the “large connected component” of the amoeba complement does not vary, and agrees with the moment polytope for the symplectic orbifold C[2] _/_ Z2 from Figure 2. On the right-hand side, the “large connected component” of the amoeba complement has a side length given by _α_ . 

**==> picture [327 x 52] intentionally omitted <==**

**----- Start of picture text -----**<br>
X− X +<br>M<br>θ <  0 θ >  0<br>**----- End of picture text -----**<br>


Figure 6. Secondary fan for the _A_ 1 singularity GIT problem. Above each chamber, we have added the fan associated with the GIT quotient. Note that we take the toric _stack_ associated to the fan. 

1 1 1 The dual of the weight matrix has cokernel given by the matrix _A_ = . Hence our 0 1 2 � � mirror is ((C _[∗]_ )[2] _, W_ ), where _W_ ( _x, y_ ) = _x_ ( _a_ + _by_ + _cy_[2] ). In this case, the exceptional locus is _V_ ( _EA_ ) = _V_ ( _abc_ ( _b_[2] _−_ 4 _ac_ )), and 

**==> picture [296 x 30] intentionally omitted <==**

where _u_ = 4 _ac/b_[2] is invariant under the (C _[∗]_ )[2] -action. 

## **2.4 Worked Example: Braid group action on the derived category of the** _An−_ 1 **singularity** 

In fact, for all _An−_ 1 we can construct a linear toric GIT problem such that the GIT quotients are resolutions of the _An−_ 1 surface singularity. The problem is rank _n −_ 1 and dimension _n_ + 1: (C _[∗]_ ) _[n][−]_[1] ↷C _[n]_[+1] (for details, see [DS15]). The stability lattice is hence rank _n −_ 1, and the number of quotients will be equal to the number of possible partitions of the set _{_ 1 _, . . . , n}_ . The GIT quotient _X_[ˇ] _stack_ corresponding to the coarsest partition _{_ 1 _, . . . , n}_ is isomorphic to the stack 

15 

[C[2][ �] 1 _,n−_ 1[Z] _[n]_[],][and][the][GIT][quotient] _[X]_[ˇ] _[geo]_[corresponding][to][the][finest][set][partition] _[{{]_[1] _[}][, . . . ,][ {][n][}}]_ is the classical geometric (non-stacky) resolution obtained via repeated blow ups. All the other quotients will be stacky and in some sense intermediate between _X_[ˇ] _stack_ and _X_[ˇ] _geo_ . The Hori-Vafa mirror model to the _An−_ 1 singularity is ((C _[∗]_ )[2] _, W_ : (C _[∗]_ )[2] _→_ C) with superpotential 

**==> picture [285 x 31] intentionally omitted <==**

In this example, the discriminant locus of _W_ ( _x, y_ ) is the discriminant ∆ _n_ of a generic single-variable polynomial of degree _n_ . These are the coefficients for which the polynomial[�] _[n] i_ =0 _[a][i][y][i]_[has a double] root. As a result, there is a homotopy equivalence **FIPS** _→_ uConf _n_ (C) which sends each potential _W_ to its set of _n_ distinct complex roots. The fundamental group _π_ 1(uConf _n_ (C)) is isomorphic to the braid group _Bn_ on _n_ strands. In their seminal paper [ST01], Seidel and Thomas proved, by analogy with the symplectic side, that _Bn_ acts (faithfully) on the _B_ -side of the _An−_ 1 example via _spherical twists_ about _spherical objects_ . 

In [ST01], they define an ( _An−_ 1)-configuration to be a collection of spherical objects _E_ 1 _, . . . , En−_ 1 such that 

**==> picture [197 x 34] intentionally omitted <==**

Their theorem states that the twists _TEi_ of an ( _An−_ 1)-configuration satisfy the braid relations for the braid group _Bn_ up to graded natural isomorphism: 

**==> picture [238 x 29] intentionally omitted <==**

This indexing is intentional: the singularity is of type _An−_ 1, while the braid group is on _n_ strands because it comes from the configuration space of the _n_ roots of a degree- _n_ polynomial. It turns out that the GIT quotients for the _An−_ 1 singularity have ( _An−_ 1)-configurations of spherical objects. Say we look at the stacky quotient _X_[ˇ] _stack_ = _[∼]_ [C[2] _/_ 1 _,n−_ 1Z _n_ ]. We note that Pic( _X_[ˇ] _stack_ ) = _[∼]_ Z _n_ and consider line bundle twists of the structure sheaf of the origin _O_ 0( _i_ ), for _i ∈{_ 0 _,_ 1 _, . . . , n −_ 1 _}_ . 

We claim that _O_ 0(1) _, . . . , O_ 0( _n −_ 1) form an ( _An−_ 1)-configuration. We can show this by computing Hom _Db_ ( ˇ _Xstack_ )[(] _[O]_[0][(] _[i]_[)] _[,][ O]_[0][(] _[j]_[))] _[∼]_[=][Hom] _D[b]_ ( _X_[ˇ] _stack_ )[(] _[O]_[0] _[,][ O]_[0][(] _[j][−][i]_[)),][where] _[i, j][∈{]_[1] _[, . . . , n][ −]_[1] _[}]_[.] This is the same as computing Ext groups Ext _[k]_ ( _O_ 0 _, O_ 0( _j − i_ )), and in this case it is sufficient[5] to compute local Ext. For the quotient stack [C[2] _/_ 1 _,n−_ 1Z _n_ ], the weighted Koszul resolution of _O_ 0 is: 

**==> picture [349 x 12] intentionally omitted <==**

Applying _Hom_ Coh( ˇ _Xstack_ )[(] _[−][,][ O]_[0][(] _[j][ −][i]_[))][gives][the][complex:] 

**==> picture [350 x 12] intentionally omitted <==**

We then take global sections, which in this case means taking Z _n_ -invariant sections (i.e., degree 0 modulo _n_ components). The case _i_ = _j_ shows that _O_ 0( _i_ ) are spherical objects. For _|j − i|_ = 1 we see a 1-dimensional Hom space, and for _|j − i| ≥_ 2 there are no sections. This is consistent with what we observed at the end of the previous section on paths and loops in **FIPS** . 

> 5The local-to-global Ext spectral sequence ([Huy06], p.85) simplifies because the support of our sheaves is a point and hence there is no higher cohomology ([Har77], Theorem 3.5). 

16 

**==> picture [118 x 86] intentionally omitted <==**

**==> picture [103 x 103] intentionally omitted <==**

**==> picture [106 x 104] intentionally omitted <==**

**==> picture [430 x 22] intentionally omitted <==**

**----- Start of picture text -----**<br>
(a) Skeleton for the fiber of the (b) Tropicalization of the fiber of (c) Coamoeba of the fiber of the<br>superpotential the superpotential superpotential with skeleton<br>**----- End of picture text -----**<br>


Figure 7. Homological mirror symmetry for the _A_ 2 singularity. We’ve taken the Hori-Vafa potential _W_ = _x_ (1 + _y_[3] ), and we’ve drawn the fiber _W[−]_[1] (1). The FLTZ skeleton replaces the fiber of the superpotential with a mostly Legendrian stop. 

_Remark_ 2.5 _._ In [Tho06], Thomas describes a connected component _Y_ of the space of Bridgeland stability conditions on the _A_ -side of _An−_ 1 mirror examples and shows that _Y_ is the universal cover of the configuration space uConf _n_ (C) of _n_ distinct points in C. This gives a geometric origin for the braid group actions. 

## **3 Legendrian lifts of embedded Lagrangian graphs** 

As Table 1 indicates, it is technically difficult to address variation of symplectic Landau-Ginzburg potentials directly in the context of homological mirror symmetry. Instead, we follow the approach that has been the most computationally successful to date and work with the following substitute for the Fukaya-Seidel category: the partially wrapped Fukaya category stopped at a skeleton of a generic superpotential fiber. In this setup, the data ( _X, W_ Σ _[X]_[:] _[X][→]_[C][)][is][replaced][by][(] _[X,]_[ Λ][Σ][),] where ΛΣ _⊂ ∂X_ is a mostly Legendrian subset (the FLTZ stop) of the contact boundary of _X_ . For a class of toric varieties including Fano _X_[ˇ] , ΛΣ can be realized as the Lagrangian core of a fiber of _W_ Σ _[X]_[in][[GS22;][Zho20]][—][see][Figure][7][for][a][sketch][(see][also][[Gan+24,][Section][2.2]][for][an][overview] of the symplectic aspects of the construction). 

One could imagine constructing a map 

**==> picture [90 x 32] intentionally omitted <==**

that sends each LG superpotential to a Legendrian skeleton for the superpotential fiber in a consistent manner. We could then construct a “local system” of partially wrapped Fukaya categories over _L_ ( _Y_ ) and subsequently pull it back to a local system of categories over the stringy K¨ahler moduli space or **FIPS** . The construction of the Legendrian skeleton, unfortunately, depends on many choices and it is unclear how to make these choices consistently except in the simplest of examples. 

Since we are unable to approach the problem in this fashion, we examine _L_ ( _Y_ ) directly without making reference to _M[X] JX_[.][Note][that] _[L]_[(] _[Y]_[ )][is][much,][much][larger][than] _[M][X] J_[(in][the][same][way][that] the space of all symplectic forms on _X_[ˇ] is much larger than the set of all K¨ahler forms on _X_[ˇ] ). 

The remainder of this section is dedicated to setting up a method to understand (part of) _L_ ( _Y_ ) in our example of interest by lifting graphs on a cylinder to Legendrians. 

17 

**==> picture [200 x 59] intentionally omitted <==**

Figure 8. An isotopy of embedded graphs giving a path in _N_ ( _M_ ). 

## **3.1 Space of graph embeddings** 

We now set up a framework for discussing paths of embedded graphs where the combinatorial type of the graph is allowed to change, as in Figure 8. These will later parameterize certain cell complexes whose top-dimensional cells are Lagrangian or Legendrian submanifolds. 

**Definition 3.1.** Let _M_ be a manifold and let _G_ be a finite graph, regarded as a CW complex. Choose a parametrization of each edge _e_ by _I_ = [0 _,_ 1], and write _e_ : _I → M_ for the restriction of a continuous map _ϕ_ : _G → M_ to that edge. Let _E_ 0( _ϕ_ ) _⊂ E_ ( _G_ ) be the set of edges on which _e_ is constant, and let _∼ϕ_ be the equivalence relation on _V_ ( _G_ ) generated by the endpoints of the edges in _E_ 0( _ϕ_ ). A degenerate graph embedding is such a map _ϕ_ : _G → M_ satisfying the following properties: 

- Each edge restriction _e_ is either an embedding or the constant map; 

- for vertices _v, w ∈ V_ ( _G_ ), one has _ϕ_ ( _v_ ) = _ϕ_ ( _w_ ) if and only if _v ∼ϕ w_ ; 

- if _e_ is non-constant, then _e_ ((0 _,_ 1)) is disjoint from _ϕ_ ( _V_ ( _G_ )); 

- if _e ̸_ = _f_ are non-constant edges, then _e_ ((0 _,_ 1)) _∩ f_ ((0 _,_ 1)) = ∅; and 

- no cycle is completely collapsed: for every cycle _c_ = _e_ 1 _, e_ 2 _, . . . , ek_ , at least one map _ei_ is non-constant. 

Equivalently, a degenerate graph embedding is an ordinary graph embedding after contracting the constant edges, with the additional requirement that no cycle of _G_ is entirely contracted. The set _{ϕ_ : _G → M }_ of degenerate graph embeddings can be equipped with the subspace topology by considering it as a subset of all continuous maps from the CW complex of _G_ to _M_ . We then denote by 

**==> picture [174 x 34] intentionally omitted <==**

where DegEmb( _G, M_ ) is the smooth space of degenerate graph embeddings of fixed combinatorial type, and two degenerate graph embeddings _ϕ_ : _G → M_ and _ϕ[′]_ : _G[′] → M_ are declared equivalent if their images agree in _M_ .[6] To avoid excessive notation, we will from now on write _ϕ ∈N_ ( _M_ ) to refer to the equivalence class given by some choice of parameterization _ϕ_ : _G → M_ . We let _N_ 1( _M_ ) denote the moduli space of graph embeddings with 1 marked point. 

We will use this quotient model throughout. Concretely, when we say that a map _K →N_ ( _M_ ) is continuous, we mean that every point of _K_ has a neighborhood on which the map can be represented by a continuous family in some DegEmb( _G, M_ ) after passing, if necessary, to a common 

> 6In fact, after picking a metric on _M_ , each equivalence class has a preferred representative whose domain is minimal under the relation of edge contraction and where every edge has a constant speed parameterization. 

18 

subdivision of the source graphs. Thus all continuity statements below are checked locally on fixed combinatorial models and then descend to _N_ ( _M_ ) by the continuity of the quotient map. To establish further notation, we will write _ϕ[t]_ : _G[t] → M_ to denote a path _I →N_ ( _M_ ), understanding that the combinatorial type of _G[t]_ may vary with the parameter _t_ . Given an element _ϕ ∈N_ ( _M_ ), let _Nϕ_ ( _M_ ) (resp. _Nϕ,_ 1( _M_ )) denote the pointed space corresponding to the connected component of _N_ ( _M_ ) (resp. _N_ 1( _M_ )) containing the embedding _ϕ_ . 

We now restrict to the setting where dim( _M_ ) = 2, _M_ is compact (possibly with boundary), and we have chosen an area form _ωM ∈_ Ω[2] ( _M_ ). The faces of a degenerate graph embedding _ϕ_ : _G → M_ are the connected components of the complement of the image of _ϕ_ and are denoted by _F_ ( _ϕ_ ). Note that we do not require our faces to be simply connected. As we forbid collapsing of cycles, given an isotopy of embedded graphs _ϕ[t]_ : _G[t] → M_ , for each _t ∈ I_ we obtain an induced map on the set of faces _F_ ( _ϕ[t]_ ): _F_ ( _ϕ_[0] ) _→ F_ ( _ϕ[t]_ ). We say that the isotopy is area-preserving if 

**==> picture [126 x 13] intentionally omitted <==**

for all _f ∈ F_ ( _ϕ_[0] ) and _t ∈ I_ . This allows us to specialize the moduli space of graphs to those which preserve area: for a fixed _ϕ_ : _G → M_ , let _Nϕ,_[Area] 1[(] _[M]_[)][denote][the][moduli][space][of][pointed][graph] embeddings _ψ_ for which there is an area-preserving isotopy from _ϕ_ to _ψ_ . 

We will now further restrict to a particular set of examples. From here on, let _M_ = [ _R[−] , R_[+] ] _×S_[1] with coordinates ( _r, q_ 2), where _R[−] ≪_ 0 _≪ R_[+] . Equip _M_ with the standard area form _dr ∧ dq_ 2, and let _ϕn_ : ( _Gn, •_ ) _→ M_ denote the embedded graph with vertical lines at _r_ = 0 _, r_ = _n_ , and _n_ evenly spaced horizontal line segments [0 _, n_ ] _×{k/n}_ for _k_ = 0 _, . . . , n −_ 1 (see Figure 9 for this graph when _n_ = 4). This graph has _n_ simply connected faces, each of area one. 

**==> picture [12 x 35] intentionally omitted <==**

**----- Start of picture text -----**<br>
q<br>2<br>∈<br>S<br>1<br>**----- End of picture text -----**<br>


**==> picture [171 x 173] intentionally omitted <==**

**==> picture [56 x 12] intentionally omitted <==**

**----- Start of picture text -----**<br>
r ∈ [ −R, R ]<br>**----- End of picture text -----**<br>


Figure 9. The protagonist of our story, the graph embedding _ϕn_ : _Gn → M_ when _n_ = 4. We’ve also indicated a marked point. The area of each closed square is one. 

**Proposition 3.2.** _Consider the configuration space_ uConf _n_ ( _M_ ) _of n unlabeled points in M . There is an inclusion_ 

_π_ 1(uConf _n_ ( _M_ )) _�→ π_ 1( _Nϕ_[Area] _n_ ( _M_ )) _._ 

19 

_Proof._ The proof is based on the following simpler map. Consider the subset _Nϕ[c] n_[(] _[M]_[)][of] _[N][ϕ] n_[(] _[M]_[)] where every simply connected face is convex with respect to the flat metric on _M_ . Then we have maps 

**==> picture [301 x 55] intentionally omitted <==**

where Cent sends an embedded graph with convex simply connected faces to the centroids of its simply connected faces, and Vor[0] sends a configuration of points to the corresponding Voronoi diagram. The triangle commutes up to homotopy: observe that the linear interpolation 

**==> picture [259 x 32] intentionally omitted <==**

is well defined as _H[t]_ ( _x_ ) _i_ always belongs to the face _fi_ due to the convexity of the faces, and therefore _H[t]_ ( _x_ ) _i_ = _H[t]_ ( _x_ ) _j_ implies _i_ = _j_ . To extend this proof to the moduli space of planar graphs with faces of area one, we fit (7) as face _A_ of the following diagram, which contains maps we have yet to define. 

**==> picture [375 x 277] intentionally omitted <==**

**----- Start of picture text -----**<br>
Nϕn ( M ) Cent [+] uConf n ( M )<br>C<br>Cent id<br>A<br>Nϕ [c] n [(] [M] [)] Vor [0] uConf n ( M )<br>j<br>id<br>B<br>Nϕ [Area] n ( M ) i Nϕ [c,] n [Area] ( M ) Vor [w] [x] uConf n ( M ) (8)<br>**----- End of picture text -----**<br>


We will prove that all the inner faces of the diagram commute up to homotopy. The proposition follows from the homotopy commutativity of the outer face. The key tool is a generalization of 

20 

the Voronoi diagram. Let _W_ = R _[n] ≥_ 0 _[×]_[ R][2] _≥_ 0[be][a][weight][space.][The][power][diagram][7][determined][by] weights _w ∈ W_ 

Vor _[w]_ : uConf _n_ ( _M_ ) _→N_ ( _M_ ) 

is defined in the following way. The assignment Vor _[w]_ ( _x_ ) is the graph whose faces _fi_ are characterized by 

**==> picture [296 x 47] intentionally omitted <==**

These generalize Voronoi diagrams in the sense that when _w_ = 0, we recover the standard Voronoi construction. For each _x ∈_ uConf _n_ ( _M_ ), define _Wadm_[+][(] _[x]_[)][to][be][the][set][of][weights][so][that][every][face] of _w_ -power diagram has positive area. 

**Lemma 3.3.** _The space Wadm_[+][(] _[x]_[)] _[is][convex.][As][a][consequence,][for][any][w]_[0] _[, w]_[1] _[∈][W] adm_[ +][(] _[x]_[)] _[,][the][path] ws_ := (1 _− s_ ) _w_ 0 + _sw_ 1 _gives a path_ Vor _[w][s]_ ( _x_ ) _∈Nϕ[c] n_[(] _[M]_[)] 

Observe that all maps Vor _[w]_ are homotopic via linear interpolation of the _w_ -coordinate. We are now ready to describe the objects and morphisms in this diagram: 

- The space _Nϕ[c,] n_[Area] ( _M_ ) is the space of degenerately embedded graphs with convex simply connected faces of area one. Given _x ∈_ uConf _n_ ( _M_ ), we solve the semi-discrete optimal transport problem by yielding a transport map _T_ : _M → M_ that minimizes the transport cost between the measure (dependent on _x_ ) 

**==> picture [235 x 31] intentionally omitted <==**

and the standard area form _dr ∧ dq_ 2. Here _δxi_ is the Dirac measure, and _χ{R±}×S_ 1 is the measure which integrates over the boundary circles. By general principles of the semi-discrete optimal transport problem [CATD93], the solution is unique (up to a set of measure zero). Furthermore, by [AHA98], the regions _T[−]_[1] ( _xi_ ) correspond (up to a set of measure zero) to the faces of a power diagram Vor _[w][x]_ for the subsets _{xi, {R[−] } × S_[1] _, {R_[+] _} × S_[1] _}_ for a certain set of weights _wx_ = _{wi, wN , wS}_ , which also depend continuously on the _xi_ . In this sense, the weighted Voronoi graph is the minimizing planar graph selected by the transport problem. It is immediate from the construction of the power diagram that the diagram varies continuously in both the weight parameters _wx_ and points _xi_ . We define the map Vor _[w][x]_ : uConf _n_ ( _M_ ) _→Nϕ[c,] n_[Area] ( _M_ ) to assign to each point configuration this power diagram. As noted previously, linearly interpolating the weights _wx →_ 0 gives homotopy commutativity of the square _B_ . 

- The recent work [BG25] constructs a map 

**==> picture [151 x 14] intentionally omitted <==**

with the property that Cent[+] ( _ϕ_ ) _⊂ M \_ Im( _ϕ_ ), i.e., the points belong to the faces. Furthermore, this map extends the centroid map in the sense that it agrees with the centroid map when restricted to _N[c]_[This][gives][us][commutativity][of] _[C]_[.] _ϕn_[(] _[M]_[).] 

> 7Also called the Laguerre-Voronoi diagram, Dirichlet cell complex, radical Voronoi tessellation or sectional Dirichlet tessellation. 

21 

The unlabeled face commutes by construction. 

After picking basepoints and applying _π_ 1 to the outer face of (8), we obtain 

**==> picture [192 x 15] intentionally omitted <==**

so _j∗ ◦ i∗ ◦_ Vor _[w] ∗[x]_ is injective. 

_Remark_ 3.4 _._ In fact, it is possible to prove a homotopy equivalence between _Nϕn_ ( _M_ ) and the smaller space _Nϕ_[Area] _n_ ( _M_ ). However, we do not need it in our construction. 

It will be practical to identify the subgroup _π_ 1(uConf _n_ ( _M_ )) _⊂ π_ 1( _Nϕ_[Area] _n_ ( _M_ )). Let _τ_ 1 _∈ π_ 1( _Nϕ_[Area] _n_ ( _M_ )) denote the loop drawn in Figure 10a and let _ρ ∈ π_ 1( _Nϕ_[Area] _n_ ( _M_ )) be the loop induced by a 1 _/n_ -rotation of the _q_ 2 coordinate. Denote by _τk_ = _ρ[k][−]_[1] _τ_ 1 _ρ[−]_[(] _[k][−]_[1)] (corresponding to the twist of the _k_ -th and ( _k_ + 1)-th faces). 

(a) A loop in _Nϕ_[Area] 4 ( _M_ ) corresponding to a generator of the braid group, _τ_ 1. 

(b) ~~A loo~~ p in _Nϕ_ ~~[Area]~~ 4 ( _M_ ) corresponding to the generator _ρ_ . 

Figure 10. Generators of the braid group via variation of embedded graphs. 

**Proposition 3.5.** _The elements τ_ 1 _, . . . , τn−_ 1 _and ρ lie in π_ 1(uConf _n_ ( _M_ )) _⊂ π_ 1( _Nϕ_[Area] _n_ ( _M_ )) _. Moreover, these are identified with the usual generators of π_ 1(uConf _n_ ( _M_ )) = _[∼] Bn,_ 1 _, where Bn,_ 1 _is the braid group on n uncolored strands and one colored strand, and τn_ = _ρ[n][−]_[1] _τ_ 1 _ρ[−]_[(] _[n][−]_[1)] _is the cyclic translate used to keep the annular indexing symmetric._ 

_Proof._ Let _M[◦]_ = ( _R[−] , R_[+] ) _× S_[1] be the interior of the cylinder. Choose a collar of _∂M_ and an isotopy of embeddings _rt_ : _M → M_ , _t ∈_ [0 _,_ 1], with _r_ 0 = id _M_ and _rt_ ( _M_ ) _⊂ M[◦]_ for every _t >_ 0. Applying _rt_ pointwise gives a deformation retraction of unordered configuration spaces, so the inclusion 

**==> picture [140 x 12] intentionally omitted <==**

_∼_ is a homotopy equivalence. Choose a homeomorphism _h_ : _M[◦] −→_ R[2] _\ {_ 0 _}_ . This induces a homeomorphism 

**==> picture [162 x 13] intentionally omitted <==**

Now let Conf _n,_ 1(R[2] ) denote the configuration space of _n_ unlabeled points together with one colored point in the plane, and let 

**==> picture [102 x 14] intentionally omitted <==**

22 

be the map recording the colored point. This is the usual Fadell–Neuwirth fibration, whose fiber over _y ∈_ R[2] is uConf _n_ (R[2] _\{y}_ ). Since R[2] is contractible, inclusion of the fiber over 0 is a homotopy equivalence. Hence 

uConf _n_ ( _M_ ) _≃_ uConf _n_ ( _M[◦]_ ) _[∼]_ = uConf _n_ (R[2] _\ {_ 0 _}_ ) _≃_ Conf _n,_ 1(R[2] ) _,_ 

and therefore 

**==> picture [204 x 14] intentionally omitted <==**

To identify generators, choose the base configuration in _M_ so that under _h_ it becomes _n_ equally spaced points on a small circle around the origin. Then the loop _τi_ becomes the standard half-twist exchanging the _i_ -th and ( _i_ +1)-st neighboring points inside a disk disjoint from the puncture, while _ρ_ becomes the rigid rotation of the entire configuration by angle 2 _π/n_ around the puncture. In [Man97, Proposition 1], these are exactly the standard generators for the annular braid group: the half-twists _bi_ for 1 _≤ i < n_ together with the annular rotation. The subgroup generated by _τ_ 1 _, . . . , τn−_ 1 is therefore the standard copy of _Bn_ inside _Bn,_ 1, and adjoining the cyclic translate _τn_ does not enlarge this subgroup. The extra loop _ρ_ records the motion of the distinguished strand around the annulus. 

## **3.2 Lagrangian projection for mostly Legendrian subsets** 

In this section, we fix notation for Legendrian submanifolds and describe their front and Lagrangian projections, which are useful for 2-dimensional visualizations. We then use Lagrangian projections to lift certain degenerate embeddings of graphs to Legendrians. Throughout, we typically restrict our discussion to our example of interest. 

Let ( _q_ 1 _, q_ 2) be standard flat coordinates on _T_[2] and let _Y_ be the contact manifold given by the unit cosphere bundle _S[∗] T_[2] _⊂ T[∗] T_[2] with respect to the standard metric on _T_[2] . Then _Y_ = _[∼] T_[2] _× S_[1] , which we give coordinates ( _q_ 1 _, q_ 2 _, θ_ ), where _θ_ is the coordinate on the _S_[1] factor measured as the angle against the covector _dq_ 1. The contact form on this space is 

**==> picture [140 x 12] intentionally omitted <==**

A 1-submanifold Λ _⊂ Y_ is called Legendrian if _λstd|_ Λ = 0. A mostly 1-Legendrian subset ([GPS24b, Definition 1.6]) is a degenerate graph embedding Λ: _G → Y_ where every non-constant edge is a Legendrian 1-submanifold. 

**Definition 3.6.** Let _L_ Λ( _Y_ ) denote the subspace of _N_ Λ( _Y_ ) consisting of those graphs which are mostly Legendrian subsets of _Y_ . 

˙ If ( ˙ _q_ 1 _, q_ 2) = (0 _,_ 0) along a Legendrian submanifold of _Y_ , the Legendrian can be conveniently described by its projection to the base _T_[2] . This is called the _front projection_ . One recovers the Legendrian Λ from its front projection _pfront_ (Λ) _⊂ T_[2] by specifying an orientation on each edge of the projection; the Legendrian condition then uniquely determines the lift (see (9)). Suggestively, we draw front projections as (possibly immersed) graphs in _T_[2] with “hairs” indicating the cooriented ˙ unit conormals, as in Figure 11a. If ( ˙ _q_ 1 _, q_ 2) = (0 _,_ 0) along an edge, we draw multiple covectors to capture the _θ_ -component of the parameterization as in Figure 11b. This projection is frequently used in the mirror symmetry literature (see, for instance, [Fan+14, Figure 2]). 

Consider now a different contact form for the same contact structure on this space: 

**==> picture [103 x 12] intentionally omitted <==**

23 

**==> picture [171 x 172] intentionally omitted <==**

(a) The front projection of a mostly 1-Legendrian of _Y_ 0, with vertices of the graph indicated by black nodes. Observe that even though the image of the front projection is only an immersed graph in _T_[2] (the projections of the red and blue edges to _T_[2] intersect one another), its lift to _Y_ 0 is embedded. 

**==> picture [172 x 174] intentionally omitted <==**

(b) The front projection of a mostly 1-Legendrian of _Y_ 0. Vertices are unmarked. By specifying multiple covectors at a single point, we describe the Legendrian along edges where the tangent space is parallel to the _θ_ -coordinate (see the orange “spokes” of covectors joining the red and blue cycles) 

Figure 11. Two examples of front projections. 

where 

**==> picture [416 x 13] intentionally omitted <==**

We will restrict ourselves to the subset _Y_ 0 := _{_ ( _q_ 1 _, q_ 2 _, r_ ) _| r_ = _r_ ( _θ_ ) _, θ ∈_ ( _−π/_ 2 + _ε, π/_ 2 _− ε_ ) _}_ . On this subset, the contact form is given by _λ_ = _dq_ 1 + _rdq_ 2. If a submanifold is contained in _Y_ 0 and is parameterized by ( _q_ 1( _t_ ) _, q_ 2( _t_ ) _, r_ ( _t_ )), the Legendrian condition simplifies to 

**==> picture [261 x 12] intentionally omitted <==**

On _Y_ 0, we can also consider the projection to the ( _q_ 2 _, r_ ) coordinates, giving us the _Lagrangian projection_ : 

**==> picture [90 x 30] intentionally omitted <==**

In the examples we consider, it is easier to visualize the Legendrians via this projection, as the images are embedded graphs rather than immersed ones. For the Lagrangian projection, we now regard the same cylinder with the coordinates reversed and write _M_ = _S_[1] _×_ ( _R[−] , R_[+] ), with coordinates ( _q_ 2 _, r_ ) and area form _dr ∧ dq_ 2, where _R[−]_ = _−_ cot _ε_ and _R_[+] = cot _ε_ . 

**Definition 3.7.** Let _L[emb]_ Λ ( _Y_ ) denote the set of mostly Legendrians of _Y_ 0 based at Λ which are homeomorphic to their image under _plag_ . 

As with the front projection, the relation (9) allows us to recover Λ from _plag ◦_ Λ (up to a translation in the _q_ 1 coordinate) by fixing a basepoint _z_ 0 _∈_ Im( _plag ◦_ Λ) and defining _q_ 1( _z_ 1) = � _zz_ 01 _[−][r dq]_[2][.] 

24 

There is a necessary and sufficient condition determining whether a degenerate embedded graph _ϕ_ : _G → M_ can be lifted to a Legendrian. 

**Proposition 3.8.** _Let ϕ_ : ( _G, •_ ) _→ M be a degenerate embedded pointed graph. Suppose for every cycle c in G we have_ 

**==> picture [265 x 26] intentionally omitted <==**

_Then there exists a unique mostly Legendrian_ Λ: ( _G, •_ ) _→ Y_ 0 _satisfying_ 

**==> picture [304 x 13] intentionally omitted <==**

_Proof._ To construct the lift, it suffices to give the _q_ 1 coordinate. For any _x ∈ G_ , pick a path _γx_ : [0 _,_ 1] _→ G_ with _γx_ (0) = _•_ and _γx_ (1) = _x_ . Then we define 

**==> picture [100 x 28] intentionally omitted <==**

For any different choice of path _γx[′]_[,][the][closed][loop] _[γ] x[−]_[1] _· γx[′]_[represents][a][class][in] _[H]_[1][(] _[G]_[),][so][the] condition (10) ensures that the two resulting values of _q_ 1( _x_ ) differ by an integer. Therefore, we have a well-defined function _q_ 1 : _G →_ R _/_ Z which does not depend on the choice of path _γx_ . If _e_ : [0 _,_ 1] _→ G_ is a non-constant oriented edge and we choose, for each _s ∈_ [0 _,_ 1], the path _γe_ ( _s_ ) to be a fixed path from _•_ to _e_ (0) followed by _e|_ [0 _,s_ ], then 

**==> picture [174 x 29] intentionally omitted <==**

Differentiating with respect to _s_ gives 

**==> picture [159 x 23] intentionally omitted <==**

so (9) holds along _e_ . Hence each non-constant edge lifts to a Legendrian curve, and the resulting graph is mostly Legendrian. The marked point fixes the remaining translation ambiguity by imposing _q_ 1( _•_ ) = 0, so the lift is unique as a pointed Legendrian. 

Observe that if a cycle _c_ bounds a face _f ∈ F_ ( _ϕ_ ), then by Stokes’ theorem, 

**==> picture [156 x 28] intentionally omitted <==**

So, the condition in Proposition 3.8 is equivalent to checking that all the faces of _ϕ_ : _G → M_ have integer area and that (10) is satisfied on cycles generating the image of the map _H_ 1( _G_ ) _→ H_ 1( _M_ ). _Example_ 3.9 _._ The graph from Figure 9 lifts to a mostly Legendrian as every face has area one and _r_ ˙ _q_ 2 integrates to 0 over the blue cycle. In fact, the lift of Figure 9 has Legendrian front projection drawn in Figure 11b. 

By carrying out Proposition 3.8 in families, we obtain a lift of moduli spaces of embedded graphs. For later use, define 

**==> picture [342 x 28] intentionally omitted <==**

and let _Nϕ_[Area] _[,]_[lift] ( _M_ ) denote its image under the map forgetting the marked point. 

25 

**Corollary 3.10.** _Suppose that ϕ_ : ( _G, •_ ) _→ M lifts to_ Λ: ( _G, •_ ) _→ Y_ 0 _. Then there exists a lifting map_ Λ( _−_ ) : _Nϕ,_[Area] 1 _[,]_[lift] ( _M_ ) _→L[emb]_ Λ ( _Y_ 0) _._ 

_Proof._ We must show that the lift from Proposition 3.8 varies continuously in families. By the quotient-topology convention above, it is enough to work locally on a parameter space _K_ where a map _K →Nϕ,_[Area] 1 _[,]_[lift] ( _M_ ) is represented by a continuous family of pointed degenerate embeddings 

**==> picture [75 x 12] intentionally omitted <==**

for one fixed subdivided graph _G_ . Because every _ϕk_ lies in _Nϕ,_[Area] 1 _[,]_[lift] ( _M_ ), the integer period condition (10) holds for all _k_ . 

Choose once and for all, for each vertex _x ∈ G_ , a combinatorial path _γx_ in _G_ from the marked point _•_ to _x_ . For every parameter _k ∈ K_ , define 

**==> picture [148 x 28] intentionally omitted <==**

Since the 1-form _−r dq_ 2 is smooth on _M_ and the maps _ϕk ◦γx_ vary continuously in the compact-open topology, the value _q_ 1 _,k_ ( _x_ ) depends continuously on _k_ for each vertex _x_ . Choose an orientation on each edge _e_ : [0 _,_ 1] _→ G_ with initial vertex _ve_ = _e_ (0). For _x_ = _e_ ( _s_ ) on such an edge, define 

**==> picture [208 x 29] intentionally omitted <==**

For fixed _e_ , the right-hand side depends continuously on ( _k, s_ ) because it is the sum of the continuous vertex value _q_ 1 _,k_ ( _ve_ ) and a path integral over the continuously varying family of edge segments _ϕk ◦ e|_ [0 _,s_ ]. At _s_ = 1, this agrees with the vertex value _q_ 1 _,k_ ( _e_ (1)) modulo Z by the integer period condition (10). Hence these edgewise formulas glue to a continuous map 

**==> picture [179 x 12] intentionally omitted <==**

whose restriction over each _k_ satisfies (9) on every non-constant edge and is therefore precisely the lift supplied by Proposition 3.8. The construction is independent of the chosen representative family, because two local lifts differ by a _q_ 1-translation and the marked point normalization forces that translation to be zero. Hence the local constructions glue on overlaps and descend to a continuous map 

**==> picture [156 x 18] intentionally omitted <==**

Note that the marking makes this map canonical. The marking fixes the _q_ 1-translation ambiguity of the Legendrian lift so that the target is the embedded-projection subspace rather than a lift only defined up to deck transformation. 

**Proposition 3.11.** _The Lagrangian projection induces a continuous map_ 

**==> picture [242 x 17] intentionally omitted <==**

_Moreover,_ pr _lag ◦_ Λ( _−_ ) _is the forgetful map_ 

**==> picture [142 x 17] intentionally omitted <==**

_that drops the marked point._ 

26 

_Proof._ Let Λ[1] _∈L[emb]_ Λ ( _Y_ 0) and choose a path Λ _[t]_ in _L[emb]_ Λ ( _Y_ 0) from the base Legendrian Λ to Λ[1] . Because each Λ _[t]_ has embedded Lagrangian projection, _ϕ[t]_ := _plag ◦_ Λ _[t]_ is a path of embedded graphs in _M_ . For every bounded face _ft_ of _ϕ[t]_ , let _ct_ = _∂ft_ be the positively oriented boundary cycle. As in the discussion following Proposition 3.8, Stokes’ theorem and the Legendrian condition give 

**==> picture [118 x 27] intentionally omitted <==**

The left-hand side depends continuously on _t_ , hence is constant; thus every bounded face of _ϕ[t]_ has the same area as the corresponding face of _ϕ_[0] for all _t_ . Moreover, every _ϕ[t]_ lifts by construction, so (10) holds for each _t_ . Thus the projected path is area-preserving and liftable, so _ϕ_[1] belongs to _Nϕ_[Area] _[,]_[lift] ( _M_ ). 

Continuity of pr _lag_ is immediate from the quotient-topology model for _L[emb]_ Λ ( _Y_ 0) and the continuity of the pointwise projection _plag_ : _Y_ 0 _→ M_ . Finally, if _ψ ∈Nϕ,_[Area] 1 _[,]_[lift] ( _M_ ), then the lift Λ _ψ_ was defined precisely so that _plag ◦_ Λ _ψ_ is the underlying unpointed graph. Hence pr _lag ◦_ Λ( _−_ ) is the forgetful map. 

**Corollary 3.12.** _There is an inclusion_ 

**==> picture [102 x 16] intentionally omitted <==**

_Proof._ By Propositions 3.2 and 3.5, the classes of the explicit loops _τ_ 1 _, . . . , τn−_ 1 _, ρ_ generate a subgroup 

**==> picture [92 x 15] intentionally omitted <==**

canonically identified with _Bn,_ 1. We choose the marked-point section on the bottom annular cycle and use it to lift _B_ to the pointed graph space. Consider the subset _C ⊂Nϕ_[Area] _n,_ 1[(] _[M]_[) of graphs where] the marked point belongs to the “bottom” cycle of _Gn_ , that is, the cycle which is the boundary of the bottom annulus. The forgetful map _C →Nϕ_[Area] _n_ ( _M_ ) is a trivial _S_[1] fibration, so choosing the marked point on the bottom cycle gives a section and hence a split injection on _π_ 1. 

We conclude from Corollary 3.12 that our explicit braid loops in graph space also define homotopically interesting loops of Legendrian stops. The embedded-projection hypothesis allows the Lagrangian projection to serve as a left inverse to the lift map on this component. While we only consider Legendrian stops that are the lifts of graphs, it is natural to conjecture the following. 

**Conjecture 3.13.** _The spaces L[emb]_ Λ _n_[(] _[Y]_[ )] _[and][L]_[Λ] _n_[(] _[Y]_[ )] _[are][homotopy][equivalent.]_ 

## **4 Induced action on partially wrapped Fukaya categories** 

Over each point Λ _∈L[emb]_ Λ _n_[(] _[Y]_[ ),][we][have][an][associated][partially][wrapped][Fukaya][category] _[W]_[(] _[X,]_[ Λ).] In this section, we will build geometric equivalences between these categories using Lagrangian correspondences, which will give a local system of triangulated categories _H_[0] _W_ ( _X,_ Λ). The ambient contact boundary remains _Y_ = _∂∞X_ throughout, while _Y_ 0 _⊂ Y_ denotes the standard coordinate chart used for our lifted graph model. For brevity of notation, we fix _n_ in this section and denote _N_ := _Nϕ_[Area] _n,_ 1 _[,]_[lift] ( _M_ ), and let _N[I]_ be the space of smooth paths (recall that these are paths factoring through DegEmb( _G, M_ ) for some combinatorial type _G_ ). The entirety of this section will prove the following. 

27 

**Theorem 4.1.** _After fixing any continuous system of auxiliary choices in the construction below, we define a continuous map_ 

**==> picture [144 x 14] intentionally omitted <==**

_to the space of cylindrical Lagrangian submanifolds, smoothly depending on the parameters_ ( _A, ρ_ ) _∈_ (0 _,_ 1) _×_ R _>_ 0 _. We additionally construct filtrations_ 

- _U[ρ] ⊂N[I] with U[ρ] ⊂ U[ρ][′] whenever ρ > ρ[′] and_ 

- _UA,ρ ⊂ U[ρ] with UA,ρ ⊂ UA′,ρ whenever A < A[′] ._ 

_The maps_ Corr _A,ρ and filtrations satisfy the following properties:_ 

- _(a) The filtrations are exhaustive,_ 

- _(b) There is compatibility with the lifting map_ Λ( _−_ ) : _N →L[emb]_ Λ _n_[(] _[Y]_[0][)] _[in][the][sense][that][for][ϕ][t][∈][U][A,ρ]_ 

**==> picture [207 x 15] intentionally omitted <==**

_The next items provide compatibility between the different choices of ρ, A. Pick IA×Iρ ⊂_ (0 _,_ 1) _×_ R _>_ 0 _parameters we would like to interpolate over._ 

- _(c) Given a smooth path ϕ[t] ∈_[�] ( _A,ρ_ ) _∈IA×Iρ[U][A,ρ][and][any][smooth][path]_[(] _[A][s][, ρ][s]_[)][:] _[I][→][I][A][×][I][ρ][,]_ Corr _As,ρs_ ( _ϕ[t]_ ) _parameterizes a Hamiltonian isotopy of Lagrangian submanifolds._ 

- _(d) Whenever ϕ[t,s] ∈ UA,ρ is a smooth homotopy of smooth paths relative endpoints,_ Corr _A,ρ_ ( _ϕ[t,]_[0] ) _∼_ Corr _A,ρ_ ( _ϕ[t,]_[1] ) _(where ∼ represents Hamiltonian isotopy in X[−] × X avoiding the product stop_ (Λ _ϕ_ 0 _×_ Λ _ϕ_ 1) _)._ 

- _(e) Whenever ϕ[t]_ 0 _[, ϕ]_ 1 _[t][∈N][ I][satisfy][ϕ]_[1] 0[=] _[ϕ]_[0] 1 _[and][can][therefore][be][concatenated,][there][is][a][preferred] Hamiltonian isotopy between_ Corr _A,ρ_ ( _ϕ[t]_ 0 _[·][ ϕ]_ 1 _[t]_[)] _[and]_[Corr] _[A,ρ]_[(] _[ϕ][t]_ 0[)] _[ ◦]_[Corr] _[A,ρ]_[(] _[ϕ]_ 1 _[t]_[)] _[,][where][the][former] operation is concatenation of paths and the latter is geometric composition in the middle factor. Furthermore, there exists ρ sufficiently small and A sufficiently close to_ 1 _so that this isotopy provides an equivalence of objects in_ Ob( _W_ ( _X[−] × X,_ Λ _ϕ_ 00 _[×]_[ Λ] _[ϕ]_[1] 1[))] _[.]_ 

**Corollary 4.2** (Parameter-independent groupoid action) **.** _For any path ϕ[t] with endpoints ϕ_[0] _, ϕ_[1] _, the geometric composition with the correspondence_ Corr _A,ρ_ ( _ϕ[t]_ ) _gives an exact functor_ 

**==> picture [210 x 15] intentionally omitted <==**

_well-defined up to natural isomorphism for sufficiently large A and small ρ. These functors assemble into a functor from the fundamental groupoid_ Π1( _N_ ) _to the groupoid of triangulated categories and exact equivalences. In particular, for any basepoint ϕ ∈N there is a group homomorphism_ 

**==> picture [158 x 14] intentionally omitted <==**

28 

_Proof._ By the stopped-correspondence formalism for exact cylindrical Lagrangians in product sectors, together with Items b and e (see, for instance, [GPS24b, Theorem 1.4 and Proposition 1.37]), the correspondence Corr _A,ρ_ ( _ϕ[t]_ ) defines the functor. By Proposition 4.5, it is independent of the auxiliary choices in the construction. Item d shows that it depends only on the endpoint-fixed homotopy class of _ϕ[t]_ , and Item e identifies 

**==> picture [168 x 14] intentionally omitted <==**

up to natural isomorphism for _A_ sufficiently close to 1 and _ρ_ sufficiently small (by Item a); furthermore, replacing ( _A, ρ_ ) with choices closer to (1 _,_ 0) defines an equivalent functor. 

Of these items, the most delicate are Item a and Item b, which motivate the whole construction. We now describe the role that ( _A, ρ_ ) play in the construction. The map Corr _A,ρ_ will be defined as the composition of several maps, each smoothly dependent on the parameters _A ∈_ (0 _,_ 1) and _ρ ∈_ R _>_ 0. The first stage of the construction assigns to a path of graphs a time-dependent Hamiltonian on _M_ : 

**==> picture [122 x 14] intentionally omitted <==**

where Ham( _M_ ) is the space of Hamiltonian functions _H_ : _M →_ R and Ham _[I]_ ( _M_ ) is its free path space. For a path _ϕ[t] ∈N[I]_ , the output ( _HA_ ) _∗_ ( _ϕ[t]_ ) is the time-dependent Hamiltonian produced from the infinitesimal flux of the isotopy at each time _t_ . This is then upgraded to the composition: 

**==> picture [361 x 17] intentionally omitted <==**

where _C_ is the space of contactomorphisms Ψ[˜] _[t]_ : _Y → Y_ that preserve the contact form (Ψ[˜] _[t]_ ) _[∗] λ_ = _λ_ , _P C_ is the path space (based at the identity), and Lag( _X[−] ×X_ ) is the space of cylindrical Lagrangian submanifolds of _X[−] ×X_ . Given any basepoint _ϕ_[0] _∈N_ , we now have a diagram which, unfortunately, does not commute: 

**==> picture [301 x 58] intentionally omitted <==**

where _P_ ( _N , ϕ_[0] ) is the path space of _N_ based at _ϕ_[0] . If the diagram did strictly commute, we could apply, for instance, [GPS24b, Theorem 1.4] to obtain equivalences between the categories we construct. However, such an equality cannot hold, as the combinatorial type of _ϕ[t]_ : _G[t] → M_ changes discontinuously over the _t_ parameter (so the image of Λ _ϕ_ 1 may not be homeomorphic to Λ _ϕ_ 0; on the other hand the image of Ψ[1] (Λ _ϕ_ 0) is obtained by a flow and is therefore homeomorphic to Λ _ϕ_ 0). 

The parameters ( _A, ρ_ ) allow us to “fudge” the relation (12) (as drawn in Figure 12a) in the following way: 

- The parameter _A_ describes how close the diagram (12) is to commuting. In our setting the stop attached to _ϕ_ is the Legendrian lift Λ _ϕ_ , and _the main content of the proof of Theorem 4.1_ is the endpoint estimate 

**==> picture [316 x 19] intentionally omitted <==**

where _dHaus_ is the Hausdorff distance on _Y_ 0. 

29 

**==> picture [171 x 171] intentionally omitted <==**

**==> picture [171 x 174] intentionally omitted <==**

(a) Our isotopies do not send loops of graphs to loops (b) A thickening _RA_ ( _ϕ_[1] ) is defined by the blue reof Legendrians, but come close. Here is a hypothetical gion (linguistically, the “thickening” of the graph Lagrangian projection of Ψ[˜][1] (Λ _ϕ_ 0), where _ϕ[t]_ is the loop refers to the complement). Each blue region has from Figure 10a. area _A_ , and Ψ[˜][1] (Λ _ϕ_ 0) belongs to the complement. 

Figure 12. Fudging the commutativity of the diagram (12). 

- The parameter _ρ_ controls the time- _ρ_ Reeb flow Φ _[ρ]_ : _Y → Y_ . Instead of asking for (12) to commute, we observe that for any mostly Legendrian stop, there exists _ρ_ 0 such that 

**==> picture [69 x 12] intentionally omitted <==**

for all 0 _< ρ < ρ_ 0. More generally, for each fixed 0 _< ρ ≤ ρ_ 0 there exists _ε_ (Λ _, ρ_ ) _>_ 0 such that 

**==> picture [303 x 14] intentionally omitted <==**

In that spirit, define a subspace of Legendrians which are disjoint from themselves up to time _ρ_ : 

**==> picture [270 x 22] intentionally omitted <==**

Observe that[�] _ρ[L][ρ]_[=] _[ L]_[Λ] _n_[(] _[Y]_[ ).][For][later][reference,][we][record][the][actual][filtrations:] 

**==> picture [308 x 33] intentionally omitted <==**

where _δ_ (Λ _, ρ_ ) denotes the Hausdorff-stability constant from Lemma 4.6 applied to the pair (Λ _,_ Λ); this is well defined because Λ _∈L[ρ]_ implies Φ _[ρ]_ (Λ) _∩_ Λ = _∅_ . Then (Item b _[′]_ ) proves that these filtrations are exhaustive (Item a) while being a strong enough bound to produce Item b. Provided that the map Corr _A,ρ_ is smooth in the _A, ρ_ parameters, Item d immediately follows as every isotopy of exact Lagrangians is a Hamiltonian isotopy. We will also isolate in Proposition 4.5 the fact that the Hamiltonian-isotopy class of Corr _A,ρ_ is independent of all auxiliary choices in the construction. The remainder of the section constructs the maps from (11), proves (Item b _[′]_ ) (and that it implies Item b), and proves Items c and e. Each portion will describe one of the maps _HA, C_ or Γ _[ρ]_ , and the various properties of those maps which give us Items b, c and e. 

30 

## **4.1 Preliminary step: constructing thickenings** _RA_ 

We first construct a preliminary map 

**==> picture [110 x 13] intentionally omitted <==**

smoothly depending on the parameter _A ∈_ (0 _,_ 1), where Thick _ϕn_ ( _M_ ) is the space of thickenings of planar graphs isotopic to _ϕn_ (see Figure 12b). Each element _V ∈_ Thick _ϕn_ ( _M_ ) is a subset _V ⊂ M_ with _n_ disjoint simply connected components with smooth boundary, and two connected components with topology _I × S_[1] containing the boundary components of _M_ . Once a graph _ϕ_ is fixed, we write _V_ =[�] _f ∈F_ ( _ϕ_ ) _[V][f]_[when][we][decompose][over][the][connected][components.][We][say] that _V_ is a thickening of _ϕ_ : _G → M_ if _Vf ⊂ f_ for every face _f ∈ F_ ( _ϕ_ ). It is an _A_ -thickening if Area( _Vf_ ) = _A ·_ Area( _f_ ) for every _f ∈ F_ ( _ϕ_ ). 

Fix once and for all the point-selection map for Jordan domains from [BG25]. Applied facewise, this gives the marked interior points already denoted Cent[+] _f_[(] _[ϕ]_[).][Each][bounded][face] _[f]_[of] _[ϕ]_[is][a] Jordan domain, so we may choose an orientation-preserving Riemann mapping 

**==> picture [66 x 14] intentionally omitted <==**

which restricts to a diffeomorphism on the interior and satisfies _uf,ϕ_ (0) = Cent[+] _f_[(] _[ϕ]_[).][Any][two][such] maps differ by rotation of the disk, so the subsets _uf,ϕ_ ( _Dr_[2][)][and][the][induced][radial][projection][to] _∂f_ are independent of that ambiguity. For fixed ( _f, ϕ_ ), the area profile 

**==> picture [122 x 15] intentionally omitted <==**

is smooth and strictly increasing on [0 _,_ 1) and extends continuously to _r_ = 1, with _af,ϕ_ (0) = 0 and _af,ϕ_ (1) = Area( _f_ ). Hence for every _A ∈_ (0 _,_ 1), there is a unique number _rA,f_ ( _ϕ_ ) _∈_ (0 _,_ 1) such that 

**==> picture [134 x 12] intentionally omitted <==**

and the dependence of _rA,f_ ( _ϕ_ ) on ( _A, ϕ_ ) is smooth. We define 

**==> picture [144 x 17] intentionally omitted <==**

Write also 

**==> picture [116 x 27] intentionally omitted <==**

The _A_ -thickening map _RA_ then sends _ϕ_ to _VA_ ( _ϕ_ ) _∈_ Thick _ϕn_ ( _M_ ). As the interior Riemann maps depend smoothly on the center point and the Jordan domain, _RA_ is continuous on _N_ . Furthermore, given a smooth path _ϕ[t]_ , _RA_ ( _ϕ[t]_ ) smoothly parameterizes thickenings. 

## **4.2 Constructing the Hamiltonians** _HA_ 

Given a smooth path _ϕ[t] ∈N_ and choice of _A_ , we will produce a time-dependent Hamiltonian isotopy of _M_ that induces the isotopy of thickenings _RA_ ( _ϕ[t]_ ). Throughout this subsection, we abbreviate 

**==> picture [240 x 27] intentionally omitted <==**

31 

For a fixed time _t_ , the infinitesimal motion of _∂RA_ ( _ϕ[t]_ ) along the path determines an exact 1-form on that boundary. At each face _f_ , we obtain a primitive function _HA,f[t]_[:] _[∂V] A,f[t][→]_[R][for][the][flux] of the isotopy of _∂VA,f[t]_[,][unique][up][to][a][constant.][We][want][to][extend][this][primitive][to][a][smooth] function on _M_ . A naive smooth cutoff extension would make the derivative of the constructed Hamiltonian grow dramatically. In this subsection, we construct an extension whose derivative on _M \ VA[t]_[is][bounded][independently][of] _[A]_[.] 

To figure out how to fill this function over the thickening, we look to what we wish we could do: construct a Hamiltonian which would honestly realize the isotopy _ϕ[t]_ . First, look at the corresponding infinitesimal flux primitive along the graph itself. After passing locally in _t_ to a common subdivision representing the family, we define 

**==> picture [355 x 52] intentionally omitted <==**

where [ _•, x_ ] is any path in the source graph from the marked point to the point mapping to _x_ . The next lemma shows that this definition is intrinsic. 

_t t_ **Lemma 4.3.** _Given a smooth path ϕ[t] the formula_ (14) _defines a piecewise smooth function H_ : _Im_ ( _ϕ_ ) _→_ R _which is independent of the chosen source path_ [ _•, x_ ] _. It is unchanged by subdivision of the source graph, and hence descends to the quotient-topology path space N[I] . Moreover, if e_ : [0 _,_ 1] _→ G is an oriented edge, then along the corresponding arc of Im_ ( _ϕ[t]_ ) _we have_ 

**==> picture [207 x 24] intentionally omitted <==**

_Proof._ If _γ, γ[′]_ are two source paths from _•_ to _x_ , their difference is a cycle _c_ := _γ[−]_[1] _· γ[′]_ in _G_ . The corresponding values of (14) differ by 

**==> picture [121 x 35] intentionally omitted <==**

Since _ω_ = _d_ ( _r dq_ 2), Stokes’ theorem rewrites this as 

**==> picture [171 x 34] intentionally omitted <==**

Every time-slice _ϕ[τ]_ belongs to _N_ , so (10) implies that � _ϕ[τ]_ ( _c_ ) _[r dq]_[2][is][an][integer.][As][a][continuous] integer-valued function of _τ_ , it is locally constant. Hence the displayed derivative is zero, proving independence of the source path. 

Subdividing the source graph does not change the geometric strip in _M_ traced by the chosen path, and any inserted constant edge contributes zero to the integral. Thus (14) is unchanged under subdivision. By the quotient-topology convention for _N[I]_ , two local representatives agree after passing to a common subdivision, so the construction descends to the quotient. 

Finally, if 0 _≤ s_ 0 _< s_ 1 _≤_ 1, subtracting the formulas for _H t_ ( _ϕt_ ( _e_ ( _s_ 1))) and _H t_ ( _ϕt_ ( _e_ ( _s_ 0))) gives 

**==> picture [304 x 35] intentionally omitted <==**

32 

Differentiating under the integral sign yields 

**==> picture [312 x 28] intentionally omitted <==**

which is equivalent to the displayed edgewise derivative formula. 

In our ideal world, we would next produce _H[t]_ : _M →_ R with the property that _H[t] |_ Im( _ϕt_ ) = _H t_ . 8 We can take a brute force extension _Hradt_[of] _[H] t_ by radially extending over each face of the graph using any normalized disk model _uf_ : _D_[2] _→ M_ sending 0 to the selected point Cent[+] _f_[(] _[ϕ][t]_[).][More] precisely, for each face _f_ of _ϕ[t]_ we have a function 

**==> picture [116 x 32] intentionally omitted <==**

The function _Hrad[t]_[:] _[M][→]_[R][is][then][piecewise][defined][on][the][faces][by][constant][radial][extension] from the boundary, and is defined to be zero at the image of Cent[+] ( _ϕ[t]_ ). This brute force extension, _H[t]_[is][the][“filler”][we][choose.] _rad_[,] 

Recall that _HA,f[t]_[:] _[∂V] A,f[t][→]_[R][is][a][primitive][for][the][flux][of][the][isotopy][of] _[∂V] A,f[ t]_[.][This][is][only] defined up to a constant, which we now normalize. Let _πA,f[t]_[:] _[∂V] A,f[t][→][∂D]_[2][be the radial projection] in such a normalized disk model. Because, in any such normalized disk model _uf_ , the isotopy of _∂VA,f[t]_[is][obtained][by][radially][transporting][the][isotopy][of] _[∂f]_[,][the][induced][infinitesimal][flux][1-form] on _∂VA,f[t]_[is][exactly] 

**==> picture [70 x 15] intentionally omitted <==**

Consequently, _HA,f[t][−]_[(] _[H]_ 1 _[t] ,f[◦][π] A,f[t]_[) is constant on] _[ ∂V] A,f[t]_[.][We remove the ambiguity of this constant] by minimizing the _L_[2] distance between _HA,f[t]_[and] _[H]_ 1 _[t] ,f[◦][π] A,f[t]_[.] We now glue together our flux primitive and our brute force extension. Pick (smoothly in the parameter _rA_ ) a partition of unity _ρ_ 1 _, ρ_ 2 _, ρ_ 3 : [0 _,_ 1] _→_ R subordinate to an open cover of the interval by neighborhoods of [0 _, rA/_ 3], [ _rA/_ 4 _,_ 1 _− rA/_ 4], and [1 _− rA/_ 3 _,_ 1]. Using any such normalized disk model _uf_ : _D_[2] _→ M_ of the face _f_ of _ϕ[t]_ , we define 

**==> picture [276 x 33] intentionally omitted <==**

Then, we define _HA,pre[t]_[:] _[M][→]_[R][piecewise][to][agree][with] _[H] A,pre,f[t]_[on][each][face.][This][function][is] smooth on a small neighborhood of the _VA,f[t]_[.][It][additionally][satisfies][the][following][two][properties:] 

**==> picture [216 x 17] intentionally omitted <==**

2. There exists a constant _B_ (dependent on the fixed path _ϕ[t]_ but not on _A_ ) so that _|dHA,pre[t][|][ < B]_ over the complement of _VA[t]_[where][defined;][this][is][because] _[H] A,pre[t]_[converges][to] _[H] rad[t]_[over][the] complement of _VA[t]_[.] 

> 8However, there is usually no such extension, as an isotopy of graphs need not be induced from an ambient smooth isotopy of _M_ . 

33 

_t t_ Since _ρ_ 3 _≡_ 1 on a collar of _r_ = 1, the piecewise-defined function _HA,pre[t]_[restricts to] _[H]_ along Im( _ϕ_ ). Finally, fix a compact family of isotopies and _A_ 0 _<_ 1. For every _A_ 0 _≤ A <_ 1 we will now smooth _HA,pre,f[t]_[.][The][non-smooth][locus][of] _[H] A,pre[t]_[is][contained][within][the][complement][of] _[V] A[t]_[.][Choose][a] smoothly varying mollifier scale _σA,ϕ,t_ strictly smaller than[1] 2[dist(Im(] _[ϕ][t]_[)] _[, ∂V] A[t]_[).][Mollifying] _[H] A,pre[t]_ in those charts and patching by a partition of unity produces our Hamiltonian _HA[t]_[.] 

Because the boundary of _M_ is fixed throughout the isotopy, the induced boundary flux vanishes there. We therefore build into the admissible choices a fixed collar neighborhood _C∂ ⊂ M_ of _∂M_ on which 

**==> picture [178 x 15] intentionally omitted <==**

for every ( _A, ϕ[t] , t_ ). 

Because the complements _M \ VA[t]_[shrink][onto][Im(] _[ϕ][t]_[)][as] _[A][→]_[1,][and][because][Item][2][gives][a] uniform bound for _dH[t]_[those][complements][where][defined,][this][smoothing][can][be][chosen] _A,pre_[on] continuously in the parameters so that for every fixed isotopy _ϕ[t]_ , 

**==> picture [274 x 21] intentionally omitted <==**

This smoothing still preserves property Item 1 and can be done in a way that preserves Item 2 (up to possibly increasing the constant _B_ ). 

Given _ϕ[t] ∈N[I]_ , denote by ( _HA_ ) _∗_ ( _ϕ[t]_ ) the time-dependent Hamiltonian _t �→ HA[t]_[.][By][Item][1,][the] Hamiltonian flow Ψ _[t]_ ( _HA_ ) _∗_ ( _ϕ[t]_ )[has][the][property][that][Ψ] _[t]_ ( _HA_ ) _∗_ ( _ϕ[t]_ )[(] _[V] A,f_[0][) =] _[ V] A,f[t]_[.] 

## **4.3 Construction of the contactomorphism lift** _C_ 

Throughout this section, we will frequently use the notation _x_ := _plag_ (˜ _x_ ) for _x_ ˜ _∈ Y_ 0. Let _H[t] ∈_ Ham( _M_ ) be a time-dependent Hamiltonian function which vanishes on a collar neighborhood of _∂M_ . Via the identification _Y_ 0 = _[∼] Sq_[1] 1 _[×][ M]_[,][we][pull] _[H][t]_[back][to][a][function][on] _[Y]_[0][by] 

**==> picture [126 x 13] intentionally omitted <==**

Because _H[t]_ vanishes on a collar of _∂M_ , this pullback has support in a compact subset of _Y_ 0. Write _α_ := _r dq_ 2, so _λ_ = _dq_ 1 + _α_ and _ω_ = _dα_ . Let _XH t_ be the Hamiltonian vector field on _M_ in the convention _ιXHt ω_ = _dH[t]_ . The strict contact lift of _XH t_ is 

**==> picture [124 x 15] intentionally omitted <==**

since its Lie derivative on _λ_ is zero. Because _H[t]_ vanishes on a collar of _∂M_ , this vector field has compact support in _Y_ 0 and extends by zero to all of _Y_ . Thus the resulting flow Ψ[˜] _[t] H[t]_[ :] _[Y][→][Y]_ preserves the contact form _λ_ , projects to the Hamiltonian flow Ψ _[t] H_[on] _[M]_[,][and][changes][the] _[q]_[1][–] coordinate by 

**==> picture [380 x 28] intentionally omitted <==**

We now briefly discuss the origin of the normalization term that appeared earlier in (14). Consider an isotopy _ϕ[t] ∈N[I]_ which leaves the graph itself fixed but moves the basepoint. If we were able to 

34 

construct an extension of the infinitesimal flux primitive _H t_ to _M_ , our normalization would ensure that our contact Hamiltonian flow commutes with the Legendrian lift map: 

**==> picture [90 x 54] intentionally omitted <==**

˜ Equivalently, if _x[τ] ∈_ Im( _ϕ[τ]_ ) is a smooth family and _x[τ] ∈_ Λ _ϕτ_ is the corresponding family of lifts, then differentiating the path-integral formula defining the Legendrian lift gives 

**==> picture [376 x 30] intentionally omitted <==**

This is the restriction of (15) to the ideal Hamiltonian extension: if _H[τ] |_ Im( _ϕτ_ ) = _H τ_ and _xτ_ = Ψ _[τ]_[then] _[α]_[(] _[X][H][τ]_[ )(] _[x][τ]_[)] _[ dτ]_[=] _[ α]_[( ˙] _[x][τ]_[)] _[ dτ]_[and][the][second][term][above][is][exactly][the] _[α]_[(] _[X][H][τ]_[ )][contri-] _H_[(] _[x]_[0][),] bution to the contact evolution. We record the identity separately because it is the version used below to compare the approximate contact flow with the canonical Legendrian lift. 

Although the smoothed Hamiltonians _HA[t]_[constructed above only approximate this ideal exten-] sion, the error vanishes as _A →_ 1, which is enough to prove the required Hausdorff convergence of the Legendrian lifts. 

**Proof of (Item b** _[′]_ **):** We need to examine the case where our time-dependent Hamiltonian is ( _HA_ ) _∗_ ( _ϕ[t]_ ) = _{HA[τ][}][τ][∈]_[[0] _[,]_[1]][.][To][reduce][notation,][write][Ψ] _[t] A_[:= Ψ] _[t]_ ( _HA_ ) _∗_ ( _ϕ[t]_ )[and][˜Ψ] _[t] A_[:=][˜Ψ] _[t]_ ( _HA_ ) _∗_ ( _ϕ[t]_ )[in][the] remainder of this section. Fix an auxiliary Riemannian metric on _Y_ 0. Let _d_ denote the induced distance on _Y_ 0, _dM_ its restriction to _M_ , and let _dHaus_ be the associated Hausdorff distance. Since _S_[1] _× M_ is compact, there exists a constant _Cd >_ 1 such that 

**==> picture [342 x 14] intentionally omitted <==**

for all ( _q_ 1 _, z_ ) _,_ ( _q_ 1 _[′][, z][′]_[)] _[ ∈][S]_[1] _[ ×] M_ , where _|q_ 1 _− q_ 1 _[′][|]_[denotes][the][distance][between][the] _[q]_[1][–coordinates][in] R _/_ Z. 

We will prove the following slightly stronger fixed-time statement: for each fixed _t ∈_ [0 _,_ 1], 

**==> picture [306 x 19] intentionally omitted <==**

Taking _t_ = 1 yields (Item b _[′]_ ). Our previous computations have shown that the Hausdorff distance between the Lagrangian projections of these sets goes to zero, so it remains to control the _q_ 1 coordinate. Set 

**==> picture [178 x 14] intentionally omitted <==**

so _αA_ ( _t_ ) _→_ 0 as _A →_ 1. Let 

**==> picture [136 x 27] intentionally omitted <==**

By Item 1, the Hamiltonian flow carries _KA_[0][to] _[ K] A[τ]_[, so Ψ] _[τ] A_[(Im(] _[ϕ]_[0][))] _[ ⊂][K] A[τ]_[.][Let Ret] _[τ] A_[:] _[K] A[τ][→]_[Im(] _[ϕ][τ]_[)] be the facewise radial retraction, and let 

35 

Ret _[τ] A,s_[,] _[s][∈]_[[0] _[,]_[ 1],][be][the][corresponding][radial][homotopy][from][the][identity][to][Ret] _[τ] A_[.][Since][the] family _ϕ[τ]_ , _τ ∈_ [0 _, t_ ], is compact and the normalized disk models vary smoothly, the radial fibers shrink uniformly as _A →_ 1: 

**==> picture [220 x 22] intentionally omitted <==**

In particular, _dM_ ( _z,_ Ret _[τ] A_[(] _[z]_[))] _[ ≤][ℓ][A]_[for][every] _[τ][∈]_[[0] _[, t]_[]][and] _[z][∈][K] A[τ]_[.] We first prove a uniform one-sided estimate. Fix _y_ ˜0 _∈_ Λ _ϕ_ 0 and write 

**==> picture [280 x 14] intentionally omitted <==**

Set 

**==> picture [154 x 12] intentionally omitted <==**

˜ ˜ ˜ and let _xA_ ( _τ_ ) _∈_ Λ _ϕτ_ be the lifted path with _xA_ (0) = _y_ 0. If _xA_ ( _τ_ ) passes through vertices, subdivide [0 _, t_ ]; the following estimate is applied edgewise and the pieces add. 

Consider the strip 

**==> picture [256 x 13] intentionally omitted <==**

Let _α_ := _r dq_ 2, so that _ω_ = _dα_ . Write 

**==> picture [334 x 12] intentionally omitted <==**

Choose real lifts of the _q_ 1–coordinates starting from the common value at _τ_ = 0. 

**==> picture [278 x 59] intentionally omitted <==**

Here the _HA_ –term comes from the contact evolution formula (15), and the _H_ –term comes from the normalization of the graph flux primitive in (14) and (16). The remaining line integrals record the motion along the time-slice graph, using the Legendrian condition (9). The oriented boundary of the strip is 

**==> picture [121 x 12] intentionally omitted <==**

Since _ω_ = _dα_ , Stokes’ theorem gives 

**==> picture [231 x 28] intentionally omitted <==**

Substituting this into the first line and taking absolute values gives 

**==> picture [384 x 65] intentionally omitted <==**

36 

The first term is controlled by the approximation of _HA[τ]_[to the graph flux primitive and the uniform] derivative bound. Indeed, after enlarging the constant in Item 2, we have on _KA[τ]_ 

**==> picture [458 x 12] intentionally omitted <==**

It remains to bound the geometric terms in (19). The vector fields _XHA[τ]_[are uniformly bounded] on the compact sets _KA[τ]_[,][again][by][Item][2][and][compactness][of] _M_ . The radial homotopies have uniformly bounded _C_[1] dependence on ( _τ, z_ ) for _A_ sufficiently close to 1. Hence there is a constant _L_ , independent of _A_ , such that _|∂τ SA| ≤ L_ , while 

**==> picture [114 x 28] intentionally omitted <==**

If _Cω_ is the operator norm of _ω_ with respect to the auxiliary metric, then 

**==> picture [130 x 34] intentionally omitted <==**

The initial radial path is constant, because _yA_ (0) _∈_ Im( _ϕ_[0] ) and the retraction fixes Im( _ϕ_[0] ). If _Cα_ := su ~~p~~ _M[|][α][|]_[,][the][final][radial][path][has][length][at][most] _[ℓ][A]_[,][and][therefore] 

**==> picture [120 x 28] intentionally omitted <==**

Combining these estimates gives 

**==> picture [280 x 12] intentionally omitted <==**

uniformly in the initial point _y_ ˜0. Since _dM_ ( _yA_ ( _t_ ) _, xA_ ( _t_ )) _≤ ℓA_ , (17) implies 

**==> picture [122 x 26] intentionally omitted <==**

˜ For the reverse Hausdorff estimate, fix _x ∈_ Λ _ϕt_ and put _x_ = _plag_ (˜ _x_ ). By the convergence of Lagrangian projections, choose _yA ∈_ Ψ _[t] A_[(Im(] _[ϕ]_[0][))][with] _[d][M]_[(] _[y][A][, x]_[)] _[≤][α][A]_[(] _[t]_[),][and][let] _[y]_[˜] _[A][∈]_[˜Ψ] _[t] A_[(Λ] _[ϕ]_[0][)] ¯ be the point over _yA_ . Set _xA_ := Ret _[t] A_[(] _[y][A]_[)][and][let] _[x]_[˜¯] _[A][∈]_[Λ] _ϕ[t]_[be][its][lift.][The][one-sided][estimate][just] proved gives _d_ (˜ _yA, x_ ¯[˜] _A_ ) _→_ 0 uniformly, while 

**==> picture [146 x 12] intentionally omitted <==**

Since _plag_ : Λ _ϕt →_ Im( _ϕ[t]_ ) is a homeomorphism from a compact space to its image, its inverse is uniformly continuous. Therefore _d_ ( _x_ ¯[˜] _A,_ ˜ _x_ ) _→_ 0, uniformly in _x_ ˜. Thus 

**==> picture [128 x 24] intentionally omitted <==**

Together with the one-sided estimate, this proves (18). 

37 

## **4.4 Constructing the correspondence** Γ _[ρ]_ 

Let Ψ[˜] _[t]_ be a contact isotopy starting at the identity. Take a collar neighborhood of the boundary of _X_ so that _X_ = _[∼] X_ int _∪∂X_ ( _∂X ×_ [0 _,_ 1)). We write the collar coordinate as _s_ , normalized in the outward direction: _s_ = 0 is the finite gluing locus with _X_ int, while _s →_ 1 approaches the contact boundary, equivalently the positive end after completing. Thus the interpolation is the identity where it is glued to the interior, and its limiting contact map at infinity is Ψ[˜][1] . Let _ht_ : _Y →_ R be the contact Hamiltonian of the isotopy, so if _Xt_ = _∂t_ Ψ[˜] _[t] ◦_ (Ψ[˜] _[t]_ ) _[−]_[1] and _λY_ denotes the contact form on _Y_ , then _ht_ = _λY_ ( _Xt_ ). On the completed collar, write the Liouville form as _rλY_ . Choose a smooth cutoff _χ_ ( _r_ ) which is 0 near the finite gluing locus and 1 on the cylindrical end, and define the time-dependent Hamiltonian 

**==> picture [114 x 12] intentionally omitted <==**

extended by zero over _X_ int. With the convention _ιXKt ω_ = _dKt_ , the time-one flow Φ of _Kt_ is the identity over _X_ int and, where _χ_ = 1, is the standard symplectization lift of Ψ[˜][1] . In particular Φ is cylindrical at infinity with boundary contactomorphism Ψ[˜][1] . Moreover, Hamiltonian isotopy gives 

**==> picture [228 x 28] intentionally omitted <==**

and this primitive is constant on the cylindrical end. Thus, suppressing the completion notation, we obtain an exact cylindrical symplectomorphism Φ: _X → X_ . Consider the graph of Φ, which is a Lagrangian submanifold Γ(Φ) _⊂ X[−] × X_ parameterized by 

**==> picture [70 x 12] intentionally omitted <==**

Since Φ is exact, choose _f_ Φ : _X →_ R with 

**==> picture [90 x 11] intentionally omitted <==**

Pulling back the Liouville form _λX −×X_ = _−π_ 1 _[∗][λ][X]_[ +] _[ π]_ 2 _[∗][λ][X]_[along][the][parameterization][of][Γ(Φ)][gives] 

**==> picture [168 x 13] intentionally omitted <==**

Thus _f_ Φ is an exact primitive for Γ(Φ). Therefore, Γ(Φ) is exact and cylindrical. The chosen polarization gives the diagonal its canonical grading and orientation data, and the graph isotopy between the diagonal and Γ(Φ) induced by the chosen isotopy transports this brane structure to canonical grading and orientation data on Γ(Φ). With this primitive and brane structure, Γ(Φ) supports an object of _W_ ( _X[−] × X_ ). For _ρ >_ 0, let _w[ρ]_ : _X → X_ denote the time- _ρ_ flow of the wrapping Hamiltonian, and set 

**==> picture [283 x 12] intentionally omitted <==**

We will also write Γ _[ρ]_ (Ψ[˜] _[t]_ ) := Γ _[ρ]_ (Φ) for the correspondence determined by a contact isotopy Ψ[˜] _[t]_ with Ψ[˜][0] = id. 

**Lemma 4.4** (Existence of smooth auxiliary choices) **.** _After fixing once and for all the point-selection map on piecewise smooth Jordan domains from [BG25], the spaces of partitions of unity, smoothing data, and collar/interior extensions used in the construction of HA and_ Γ _[ρ] are contractible. In particular, after fixing a compact family of paths in N[I] and a compact parameter range in_ ( _A, ρ_ ) _, these choices may be made continuously in all parameters._ 

38 

_Proof._ By the quotient topology discussion in Section 3.1, a compact family in _N[I]_ is covered by finitely many open sets on which the graphs are represented on one fixed subdivided domain. On each such chart, the bounded faces form smooth families of Jordan domains and the annular ends form smooth families of collars. The point-selection map from [BG25] therefore gives smooth interior basepoints for the faces. Local normalized disk models exist on such charts, and the radial constructions built from them are independent of the residual rotation ambiguity of the disk. Hence: 

- admissible partitions of unity and mollifier choices form convex sets; and 

- collar cutoffs and interior extensions are contractible because they are determined by ordinary cutoff functions on a fixed collar model. 

On overlaps, two local choices differ by elements of these same contractible spaces. Since the parameter spaces are paracompact, the local families glue after a partition-of-unity argument, giving globally smooth choices on the compact family. 

**Proposition 4.5** (Well-definedness of Corr _A,ρ_ ) **.** _Fix a smooth system of auxiliary choices in the construction of HA and_ Γ _[ρ] (namely, the partition of unity and smoothing used to define HA, together with the smooth extension of the boundary contact isotopy over X_ int _; the radial constructions use the fixed point-selection map from [BG25]). Then, on triples_ ( _A, ρ, ϕ[t]_ ) _with ϕ[t] a smooth path in_ DegEmb( _G, M_ ) _, the recipe_ (11) _defines a smooth map_ 

**==> picture [204 x 14] intentionally omitted <==**

_If two such systems of auxiliary choices are used, then for every fixed_ ( _A, ρ, ϕ[t]_ ) _the resulting cylindrical exact Lagrangians are connected by an exact isotopy in X[−] × X. If moreover ϕ[t] ∈ UA,ρ, this isotopy may be chosen through Lagrangians disjoint from the product stop_ 

**==> picture [52 x 13] intentionally omitted <==**

_In particular,_ Corr _A,ρ_ ( _ϕ[t]_ ) _is independent of all auxiliary choices up to Hamiltonian isotopy, and for ϕ[t] ∈ UA,ρ it is independent up to Hamiltonian isotopy avoiding the product stop._ 

_Proof._ For a fixed system of auxiliary choices, smoothness of the map 

**==> picture [120 x 14] intentionally omitted <==**

follows from the construction: each stage in (11) is chosen smoothly in the relevant parameters. We now compare two systems of auxiliary choices. First consider the radial constructions entering _RA_ and _HA_ . The interior basepoints are fixed by the chosen point-selection map from [BG25]. For a given face, any two normalized disk models sending 0 to that basepoint differ by a rotation of the disk. This rotation is harmless for the present construction, since the subsets _Dr_[2] _[⊂][D]_[2][ are rotation-invariant:][it does not change the associated thickening] _[ V][A,f]_[, the radial retract,] or the radially extended pre-Hamiltonian as a function on the face, but only reparameterizes the angular variable. Hence the radial part of the construction is canonical once the point-selection map is fixed. 

For fixed radial data, the boundary primitive _HA,f_ is uniquely determined by the flux condition together with the normalization 

**==> picture [94 x 12] intentionally omitted <==**

39 

The remaining choices in the construction of _HA_ are contractible. Indeed, admissible partitions of unity form a convex set, and if _HA_[0][and] _[H] A_[1][are][two][admissible][smooth][choices,][then] 

**==> picture [123 x 14] intentionally omitted <==**

is again a smooth admissible choice. It still agrees with the prescribed boundary primitive on _∂VA_ , and it satisfies the same type of bound as in Item 2 (after enlarging the constant if necessary). Thus any two choices used to define _HA_ are joined by a smooth family of admissible Hamiltonians, so their Hamiltonian flows are joined by a smooth family of Hamiltonian flows. 

Finally, in the definition of Γ _[ρ]_ , after fixing the collar 

**==> picture [134 x 12] intentionally omitted <==**

extending the boundary map to the identity over _X_ int amounts to choosing an interpolation in the collar direction. The space of such interpolations is contractible, so different choices yield isotopic graphs and therefore an exact isotopy of cylindrical Lagrangians; the subsequent time- _ρ_ wrapping preserves this exact isotopy. 

Combining these three observations, any two full systems of auxiliary choices are connected by a smooth family of auxiliary data, and applying (11) along this family gives an exact isotopy between the corresponding Lagrangians Corr _A,ρ_ ( _ϕ[t]_ ). Any exact Lagrangian isotopy is Hamiltonian, so the resulting correspondence is well defined up to Hamiltonian isotopy. 

If _ϕ[t] ∈ UA,ρ_ , the proof of (Item b _[′]_ ) is unchanged along the interpolation, since it only uses Items 1 and 2 and smooth dependence of the smoothing data. Hence the same argument used in the proof of Item b shows that every member of this isotopy is disjoint from the product stop. Therefore the Hamiltonian isotopy may be taken relative to the stop, as claimed. 

**Lemma 4.6** (Hausdorff openness of fixed-time Reeb disjointness) **.** _Fix an auxiliary Riemannian metric on Y , and let dHaus denote the induced Hausdorff distance on compact subsets. Let_ Λ _−,_ Λ+ _⊂ Y be compact and fix ρ >_ 0 _. If_ 

**==> picture [365 x 31] intentionally omitted <==**

_dHaus_ (Λ _−[′][,]_[ Λ] _[−]_[)] _[ < δ]_ 

_still satisfies_ 

**==> picture [86 x 13] intentionally omitted <==**

_Proof._ Since Φ _[ρ]_ (Λ _−_ ) and Λ+ are compact and disjoint, their distance 

**==> picture [110 x 12] intentionally omitted <==**

is strictly positive. Because _Y_ is compact, the time- _ρ_ Reeb flow Φ _[ρ]_ : _Y → Y_ is uniformly continuous, so there exists _δ >_ 0 such that 

**==> picture [198 x 12] intentionally omitted <==**

If _y ∈_ Λ _[′] −_[,][choose] _[x][ ∈]_[Λ] _[−]_[with] _[d]_[(] _[x, y]_[)] _[ < δ]_[.][Then] 

**==> picture [328 x 12] intentionally omitted <==**

Hence Φ _[ρ]_ ( _y_ ) _∈/_ Λ+ for all _y ∈_ Λ _[′] −_[,][proving][the][claim.] 

40 

**Lemma 4.7** (Wrapped graph criterion for the product stop) **.** _Let_ Ψ[˜] _[t] be a contact isotopy of Y starting at the identity, and let F_ : _X → X be the associated exact symplectomorphism constructed above. Then, for compact_ Λ _−,_ Λ+ _⊂ Y , the wrapped graph_ Γ _[ρ]_ ( _F_ ) _is disjoint at infinity from the product stop_ Λ _− ×_ Λ+ _if and only if_ 

**==> picture [108 x 13] intentionally omitted <==**

_In particular, if the condition on the right-hand side holds, then_ Γ _[ρ]_ ( _F_ ) _supports an object of_ 

**==> picture [112 x 11] intentionally omitted <==**

_Proof._ Near infinity, _F_ is the symplectization of the contactomorphism Ψ[˜][1] , so Γ( _F_ ) is cylindrical over the Legendrian graph 

**==> picture [142 x 14] intentionally omitted <==**

The wrapping _w[ρ]_ acts on this end by the time- _ρ_ Reeb flow in the second factor. Moreover, because _F_ preserves the cylindrical end, points of Γ( _F_ ) reach infinity in one factor if and only if they do so in the other, so the only possible intersection with the product stop occurs in the _Y ×Y_ corner. The equivalence therefore follows immediately, and since Γ _[ρ]_ ( _F_ ) is exact and cylindrical by construction, this is exactly the condition needed for it to define an object of the stopped category. 

## **Proof of Item b:** Set 

**==> picture [124 x 13] intentionally omitted <==**

and write Ψ[˜] _[t]_[for][the][contact][isotopy][produced][above.][Let] _[F][A]_[ :] _[X][→][X]_[be][the] _A_[:= (] _[C][ ◦]_[(] _[H][A]_[)] _[∗]_[)(] _[ϕ][t]_[)] associated exact symplectomorphism, so that by definition 

**==> picture [106 x 14] intentionally omitted <==**

Assume _ϕ[t] ∈ UA,ρ_ . Since Λ1 _∈L[ρ]_ , we have 

**==> picture [82 x 13] intentionally omitted <==**

Let _δ_ (Λ1 _, ρ_ ) be the constant from Lemma 4.6 applied to the pair (Λ1 _,_ Λ1). By the definition of _UA,ρ_ , we have 

_dHaus_ (Ψ[˜][1] _A_[(Λ][0][)] _[,]_[ Λ][1][)] _[ < δ]_[(Λ][1] _[, ρ]_[)] _[.]_ 

Therefore Lemma 4.6 gives 

**==> picture [106 x 14] intentionally omitted <==**

Applying Lemma 4.7 with Λ _−_ = Λ0 and Λ+ = Λ1, we conclude that 

**==> picture [196 x 14] intentionally omitted <==**

which proves Item b. 

**Proof of Item c:** Let _ϕ[t] ∈_[�] ( _A,ρ_ ) _∈IA×Iρ[U][A,ρ]_[and][(] _[A][s][, ρ][s]_[)][:] _[I][→][I][A][ ×][ I][ρ]_[.][By][construction][of] _[R][A]_[,] _HA_ , _C_ , and Γ _[ρ]_ , together with Proposition 4.5, the family 

**==> picture [92 x 14] intentionally omitted <==**

is a smooth exact isotopy of cylindrical Lagrangians. Because _ϕ[t]_ lies in every _UAs,ρs_ , the proof of Item b shows that each member of this family is disjoint from the product stop. Any exact isotopy of exact cylindrical Lagrangians is Hamiltonian, so this gives the required Hamiltonian isotopy. 

41 

**Proof of Item e:** Let Ψ[˜] _[t]_ 0 _[,]_[˜Ψ] _[t]_ 1[be][the][contact][isotopies][associated][to] _[ϕ][t]_ 0 _[, ϕ]_ 1 _[t]_[,][and][let][Φ][0] _[,]_[ Φ][1][ :] _[X][→] X_ be the corresponding Liouville-domain maps. These isotopies start at the identity, but their endpoints need not. Since our graphs are parameterized by 

**==> picture [76 x 12] intentionally omitted <==**

geometric composition in the middle factor satisfies 

**==> picture [132 x 12] intentionally omitted <==**

Thus the order of correspondences agrees with the order of path concatenation, but reverses the written order of the underlying endomorphisms of _X_ . 

**==> picture [192 x 14] intentionally omitted <==**

For 0 _≤ s ≤_ 1, define 

**==> picture [136 x 12] intentionally omitted <==**

Then 

**==> picture [238 x 14] intentionally omitted <==**

Since _s �→ w[sρ]_ is a Hamiltonian isotopy of _X_ , the family _Ks_ is an exact isotopy of exact graphs in _X[−] × X_ , hence a Hamiltonian isotopy. 

The Lagrangian _K_ 0 is the correspondence attached to the pointwise composition 

**==> picture [108 x 14] intentionally omitted <==**

By reparameterizing the _t_ -coordinates of the two components independently, this contact isotopy is endpoint-fixed homotopic to 

**==> picture [203 x 34] intentionally omitted <==**

Choose the auxiliary data for the concatenated path _ϕ[t]_ 0 _[·][ ϕ]_ 1 _[t]_[by pulling back the auxiliary data used] for _ϕ[t]_ 0[and] _[ϕ][t]_ 1[on][the][two][half-intervals.][With][this][choice][of][auxiliary][data,][the][resulting][contact] isotopy is exactly (Ψ[˜] 1 _·_ Ψ[˜] 0) _[t]_ . Let Corr _[sp] A,ρ_[(] _[ϕ]_ 0 _[t][·][ ϕ]_ 1 _[t]_[)][denote][the][correspondence][constructed][from][this] special choice system. Then 

**==> picture [106 x 16] intentionally omitted <==**

By Proposition 4.5, this is Hamiltonian isotopic to the correspondence produced from our fixed global auxiliary choices. Therefore 

**==> picture [106 x 14] intentionally omitted <==**

This proves the unstopped composition statement. 

For the final stopped statement, let 

**==> picture [230 x 15] intentionally omitted <==**

By Item a, after shrinking _ρ_ and taking _A_ sufficiently close to 1 if necessary, we may assume that the concatenated path _ϕ[t]_ 0 _[·][ ϕ][t]_ 1[lies][in] _[U][A,ρ]_[.][Then,][Proposition][4.5][upgrades][the][isotopy][between] _[K]_[0][and] 

42 

Corr _A,ρ_ ( _ϕ[t]_ 0 _[·][ϕ][t]_ 1[) to one through objects of] _[ W]_[(] _[X][−][×][X,]_[ Λ][0] _[ ×]_[Λ][2][).][The reparameterization from fixed-] time composition to concatenation does not change the time-one boundary contactomorphism, so once stop-avoidance is established it persists throughout that part of the isotopy. 

It therefore remains to consider the isotopy obtained by turning off the middle wrapping. The corresponding boundary contactomorphisms form a compact family 

**==> picture [190 x 15] intentionally omitted <==**

so that the full wrapped graph criterion applies to Φ _[ρ] ◦_ Ξ _A,s_ . As _A →_ 1, the maps Ψ[˜][1] 0 _,A_[and][˜Ψ][1] 1 _,A_ send Λ0 and Λ1 arbitrarily close to Λ1 and Λ2, respectively, by (Item b _[′]_ ); and as _ρ →_ 0, the inserted Reeb flow Φ _[sρ]_ converges uniformly to the identity in _s_ . Hence, for _ρ >_ 0 sufficiently small and _A <_ 1 sufficiently close to 1 (depending on the chosen pair of paths, equivalently on the compact isotopy family under consideration), we have 

**==> picture [244 x 14] intentionally omitted <==**

where _δ_ (Λ2 _, ρ_ ) is the constant from Lemma 4.6 for the pair (Λ2 _,_ Λ2). By Lemma 4.6, this implies 

**==> picture [206 x 14] intentionally omitted <==**

and then Lemma 4.7 shows that every intermediate correspondence in the preferred isotopy avoids the product stop Λ0 _×_ Λ2. Therefore the isotopy from Corr _A,ρ_ ( _ϕ[t]_ 0 _[·][ ϕ][t]_ 1[)][to][Corr] _[A,ρ]_[(] _[ϕ][t]_ 0[)] _[ ◦]_[Corr] _[A,ρ]_[(] _[ϕ]_ 1 _[t]_[)] takes place inside 

**==> picture [128 x 15] intentionally omitted <==**

as needed.[9] 

## **5 Applications** 

With the technical work of establishing a monodromy action via Theorem 4.1 in hand, we now examine this action in the context of homological mirror symmetry. In particular, we demonstrate several ways in which it is explicitly computable. 

## **5.1 Isotopies of the FLTZ Legendrian mirror to the** _An−_ 1 **singularity** 

We first turn to our main example, the FLTZ stop mirror to the _An−_ 1 singularity _X_[ˇ] _n_ . Let Λ _n_ be the FLTZ stop (Definition A.1) associated to the stacky fan given by the pair consisting of the fan Σ _n_ in R[2] whose cones are 

**==> picture [242 x 12] intentionally omitted <==**

and the homomorphism _β_ : Z[2] _→_ Z[2] satisfying _β_ (1 _,_ 0) = (1 _,_ 0) and _β_ (0 _,_ 1) = (1 _, n_ ). Note that Pic( _X_[ˇ] _n_ ) = _[∼]_ Z _/n_ Z generated by _O_ (1) := _O_ ( _D_ (1 _,n_ )) where _D_ (1 _,n_ ) is the toric divisor corresponding to R _≥_ 0 _·_ (1 _, n_ ). 

Combining Theorem 4.1 and Corollary 3.12 gives a new proof of the following result (see Section 1.2 for other approaches). 

> 9Technically speaking, these Lagrangians need to be equipped with grading/orientation data in the sense of [GPS24a, Section 5.3]. However, as our Lagrangians are isotopic to conormals they have canonical grading/orientation data relative to the tautological polarization of _X_ . 

43 

**==> picture [171 x 174] intentionally omitted <==**

Figure 13. The Lagrangian projection of the FLTZ stop Λ4 for the fan of the _A_ 3 singularity. 

**==> picture [439 x 62] intentionally omitted <==**

Figure 14. A loop of mostly Legendrians starting at the FLTZ Legendrian Λ4. 

**Corollary 5.1.** _There exists an action of Bn,_ 1 _on the triangulated category H_[0] _W_ ( _X,_ Λ _n_ ) _by exact autoequivalences (well-defined up to natural isomorphism)._ 

In fact, we can go further and intrinsically identify these autoequivalences of the partially wrapped Fukaya category as geometric operations. Recall that we have preferred generators _τ_ 1 _, . . . , τn−_ 1 and _ρ_ of _Bn,_ 1 and a cyclic translate _τn_ inside the moduli space of degenerate graphs that are identified in Proposition 3.5. We let _Fτi_ and _Fρ_ be the corresponding autoequivalences from Corollary 5.1. We first describe the _Fτi_ . 

**Theorem 5.2.** _For each i ∈{_ 1 _, . . . , n −_ 1 _}, let Ki denote the linking disk of the Legendrian component of_ Λ _n whose projection under plag is the horizontal line separating the two bounded faces where τi is supported. Then_ 

**==> picture [52 x 12] intentionally omitted <==**

_Here TKi is the spherical twist on Ki._ 

_Proof._ Fix _i_ , and consider the Lagrangian correspondence Corr _A,ρ_ ( _τi_ ). Let Ψ[˜] _[t] τi_[denote][the][corre-] sponding contact isotopy, and let Φ _τi_ : _X → X_ be the associated exact symplectomorphism from Section 4.4. Observe that the restriction of this correspondence to _X_ int _[−][×][X]_[int][has][cylindrical] boundary; in the notation of Section 4.4, 

**==> picture [186 x 17] intentionally omitted <==**

is a pushoff of the diagonal Lagrangian. Hence [HHL26, Proposition 3.5] (see also [GPS24b, Proposition 1.37]) gives an isomorphism in the Fukaya category 

**==> picture [112 x 12] intentionally omitted <==**

44 

**==> picture [186 x 172] intentionally omitted <==**

Figure 15. The unique intersection between the FLTZ stop Λ _n_ and the positive pushoff Φ _[ρ]_ (Ψ[˜] _[t] τi_[(Λ] _[n]_[))] is circled in the figure. 

where the term _Ei_ corresponds to the intersection between Γ _[ρ]_ (Φ _τi_ ) and the skeleton of _X[−] × X_ outside of _X_ int _[−][×][ X]_[int][.][By][the][same][argument][as][in][[HHL26,][Proposition][4.7],][this][intersection] corresponds to the unique intersection between Φ _[ρ]_ (Ψ[˜] _[t] τi_[(Λ] _[n]_[))][and][Λ] _[n]_[.] For the loop _τi_ , there is exactly one such intersection, namely the one indicated in Figure 15. By construction of the loop _τi_ , this intersection lies on the horizontal stop component separating the two bounded faces braided by _τi_ . Therefore _Ei_ = _Ki × Ki_ . Since a linking disk is spherical, (3) identifies the kernel [ _Ki × Ki →_ ∆ _X_ int] with the spherical twist _TKi_ . Hence 

**==> picture [52 x 12] intentionally omitted <==**

We will show in Proposition 5.6 that _Ki_ corresponds under Theorem A.3 to the twist _O_ 0( _−i_ ) of the structure sheaf of the origin. However, we do not do so immediately as our argument will use the Bondal–Thomsen generators and a local analysis of the FLTZ stop from Section 5.2. 

Instead, we now turn to the simpler _Fρ_ . From Proposition 3.5, the underlying graph isotopy is given by a 1 _/n_ translation in the _q_ 2 direction and hence lifts to an isotopy of Λ _n_ that moves the component corresponding to the ray generated by (1 _, n_ ) according to _q_ 1 + _nq_ 2 = _t_ for _t ∈_ [0 _,_ 1]. On Lagrangians wrapped up to the stop, it follows that Φ _ρ_ acts by ‘dragging’ the end of the Lagrangian along this isotopy. However, we have another description of such a Hamiltonian in Appendix A.2, namely, _Hcyl[F]_[where] _[F]_[is][a][support][function][for][the][divisor] _[−][D]_[(1] _[,n]_[)][.][While][this][observation][gives][a] rather explicit geometric description of the autoequivalence, it also allows us to identify its mirror. 

**Proposition 5.3.** _Let Fρ denote the autoequivalence induced by the annular generator ρ. Under the HMS equivalence of Theorem A.3, one has_ 

**==> picture [96 x 12] intentionally omitted <==**

_Proof._ From the discussion preceding the proposition, we are computing the autoequivalence induced by the Hamiltonian _Hcyl[F]_[in][the][notation][of][Appendix][A.2,][where] _[F]_[is][the][support][function] for the divisor _−D_ (1 _,n_ ). If we were working with a toric variety, [HH22, Theorem 3.13], which is a translation of [Han19, Theorem 4.5] to the partially wrapped setting, would imply that this is mirror to tensoring by _O_ ( _−D_ (1 _,n_ )). However, Theorem A.3 extends the HMS equivalence used in 

45 

[Han19; HH22] to toric Deligne-Mumford stacks following the same proof scheme. In particular, tracing morphism spaces between tropical Lagrangian sections as in the proof of [Han19, Theorem 4.5] shows the functor induced by the time-1 flow of _Hcyl[F]_[corresponds][under][Theorem][A.3][to] tensoring by the line bundle corresponding to _F_ . 

Therefore, in our setting, we indeed obtain that _Fρ_ is mirror to _−⊗O_ ( _−D_ (1 _,n_ )), and under our conventions, _O_ ( _−D_ (1 _,n_ )) = _O_ ( _−_ 1). 

## **5.2 The Bondal-Thomsen collection and a local model for mapping cones** 

We next turn to the Bondal-Thomsen collection, which we will use to identify the linking disks in Theorem 5.2 on the coherent side. The underlying stratification of the torus induced by the FLTZ skeleton is called the Bondal stratification [Bon06]. One can combinatorially assign a line bundle to every stratum of the Bondal stratification following [HHL24, Section 2.3] or [FH23]. In our example of interest, this assignment is depicted on the far left image of Figure 17 and described in Example 5.5. 

This subsection records a local 2-dimensional mutation rule rather than a global theorem: an algorithm for more general stratifications would be desirable, but here we only explain how the Bondal–Thomsen collection changes under a single local modification. It would be interesting to relate this move (and possible generalizations) to the theory developed in [Ber+25]. 

Suppose that we are in the situation where the dimension of our torus is two and we have a zero-dimensional stratum whose FLTZ stop locally looks like that for affine space, so that there is a resolution _C•_ ( _S[ϕ] , O[ϕ]_ ) that has the shape as drawn in Figure 16a. Consider the object of the derived category given by the mapping cone 

**==> picture [136 x 16] intentionally omitted <==**

_Remark_ 5.4 _._ We make a quick remark about the existence of a quasi-isomorphism between _M_ and _A_ , which is equivalent to having a short exact sequence 

**==> picture [124 x 14] intentionally omitted <==**

This occurs when we modify our local model so that the two 1-dimensional strata do not share a higher-dimensional cone (i.e., we are at a 0-stratum that does not correspond to a 2-cone of Σ in the FLTZ construction). This differs from the local model drawn in Figure 16a via removal of the orange stratum. 

Consider the chain maps 

**==> picture [366 x 11] intentionally omitted <==**

Then the following sequence (read from right to left) is exact (with chain nullhomotopy indicated 

46 

**==> picture [139 x 139] intentionally omitted <==**

**==> picture [139 x 140] intentionally omitted <==**

**==> picture [380 x 177] intentionally omitted <==**

**----- Start of picture text -----**<br>
B A A B A A<br>A<br>A<br>M M<br>B g 1 A A B M M A A<br>f 1 g 2<br>D f 2 C C D C C<br>(a) The local model for the resolution (b) Modifying the stratification and la-<br>C• ( S [ϕ] , O [ϕ] ) at a 0-stratum. belling.<br>**----- End of picture text -----**<br>


Figure 16. Variation of the Legendrian skeleton can be reinterpreted as a variation of stratification for _C•_ ( _S[ϕ] , O[ϕ]_ ). 

from left to right): 

**==> picture [384 x 131] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 0 −g g<br>d [1] = 1 g 0  d [2] =  − 1<br>d [0] = �1 − 1 g � 0 1 1   1 <br>A A [⊕] [2] ⊕ M A ⊕ M [⊕] [2] M<br>h [0] = 10 h [1] = 00 10 00 h [2] = �0 − 1 0�<br>0 0 0 1<br>**----- End of picture text -----**<br>


As a result, we may replace _C•_ ( _S[ϕ] , O[ϕ]_ ) with the homotopic resolution drawn in Figure 16b. _Example_ 5.5 _._ For the example of _X_[ˇ] Σ _n_ , we have this local model at each 0-dimensional stratum of the FLTZ skeleton. For a fixed 0-stratum (indexed by _i ∈{_ 0 _, . . . , n −_ 1 _}_ ), the sheaves labelling the 

47 

**==> picture [266 x 88] intentionally omitted <==**

**----- Start of picture text -----**<br>
O O O<br>O ( − 3) O ( − 3) O ( − 3)<br>O ( − 2) M M<br>O ( − 2)<br>O ( − 1) O ( − 1) O ( − 1)<br>**----- End of picture text -----**<br>


Figure 17. The effect of a local modification on the Bondal–Thomsen collection. 

resolution _C•_ ( _S[ϕ] , O[ϕ]_ ) from [HHL24] are: 

**==> picture [382 x 12] intentionally omitted <==**

By comparison with (6), we see that the complex _M_ is quasi-isomorphic to the ideal sheaf _I_ 0( _−i_ ). The variation of skeleton therefore corresponds to the variation of stratification and labelling drawn in Figure 17. 

With an understanding of these local models in hand, we are now prepared to identify the linking disks appearing in Theorem 5.2 and prove that they correspond to the expected spherical twists. 

**Proposition 5.6.** _For i ∈{_ 1 _, . . . , n −_ 1 _}, let Ki be the linking disk of the horizontal stop component of plag_ (Λ _n_ ) _indexed by the_ 0 _-stratum i. Under the HMS equivalence of Theorem A.3, one has_ 

**==> picture [76 x 12] intentionally omitted <==**

_Equivalently, after reversing the cyclic order of the horizontal components, the corresponding linking disk is mirror to O_ 0( _i_ ) _._ 

_Proof._ Fix _i_ . In the local model at the 0-stratum indexed by _i_ , the labels are 

**==> picture [202 x 12] intentionally omitted <==**

and these agree with the line bundles assigned to small negative pushoffs of the cotangent fibers at these points under Theorem A.3. The mutated object is 

**==> picture [142 x 16] intentionally omitted <==**

Comparing with the Koszul resolution (6), we obtain 

**==> picture [62 x 12] intentionally omitted <==**

the ideal sheaf of the origin twisted by _O_ ( _−i_ ). 

Reading off the homotopic resolution after the local modification, the corresponding horizontal 1-stratum is represented by the cone of the canonical map _Mi → A_ . Under the mirror functor, its linking disk is therefore identified with 

**==> picture [110 x 14] intentionally omitted <==**

by [GPS24b, Theorem 1.10]. The short exact sequence 

**==> picture [174 x 12] intentionally omitted <==**

shows that this cone is _O_ 0( _−i_ ). 

48 

**Corollary 5.7.** _Under the HMS equivalence, one has_ 

**==> picture [80 x 13] intentionally omitted <==**

_After the cyclic relabelling i �→−i, this is precisely the Seidel–Thomas action by twists about_ 

**==> picture [102 x 12] intentionally omitted <==**

_In particular, the subgroup generated by the τi acts by the Seidel–Thomas spherical twists._ 

_Proof._ Combine Theorem 5.2 and Proposition 5.6 with Proposition 3.5. Since Pic( _X_[ˇ] Σ _n_ ) = _[∼]_ Z _n_ , the collections _{O_ 0( _−i_ ) _}_ and _{O_ 0( _i_ ) _}_ differ only by a cyclic relabelling. 

## **5.3 Equivalences between VGIT chambers** 

Given _I_ = _{i_ 0 _< · · · < ik} ⊂{_ 0 _,_ 1 _,_ 2 _,_ 3 _, · · · , n}_ with _i_ 0 = 0 and _ik_ = _n_ , let (Σ _[I] n[, β] n[I]_[)][be][the] stacky fan in _N_ = Z[2] whose underlying fan Σ _[I] n_[has][rays] _[ρ][i]_[=][R] _[≥]_[0] _[· ⟨]_[1] _[, i][⟩]_[for] _[i][∈][I]_[and][2-] dimensional cones _ρia−_ 1 + _ρia_ for _a_ = 1 _, . . . , k_ , and whose stacky map is 

**==> picture [136 x 14] intentionally omitted <==**

We abbreviate _X_[ˇ] Σ _In,βIn_ and ΛΣ _In,βIn_ by _X_[ˇ] Σ _In_ and ΛΣ _In_ , respectively. 

Whenever _I ⊂ I[′]_ , we have that _X_[ˇ] Σ _In′[→][X]_[ˇ][Σ] _[In]_ is a crepant partial resolution of singularities. The categories _D[b]_ ( _X_[ˇ] Σ _In′_[)] _[, D][b]_[( ˇ] _[X]_[Σ] _[In]_[)][are][(non-] canonically) equivalent. In the language of Section 2.2 these fans correspond to different chambers of the GIT parameter space. 

This derived equivalence can be observed from the perspective of variation of skeleta. In the Lagrangian projection, the associated stop ΛΣ _In_ consists of horizontal circles at heights _i ∈ I_ , and _i − j_ equally spaced vertical line segments connecting the circles corresponding to adjacent indices _i > j_ . The associated graph has compact faces of area 1. 

**==> picture [164 x 167] intentionally omitted <==**

Figure 18. Fan, Lagrangian, and front projections for different VGIT chambers. 

For fixed _n_ , all such Lagrangian projections of ΛΣ _In_ are isotopic via area-preserving isotopy. For example, on the right we draw two such fans and the Lagrangian projections of the FLTZ stops. One isotopy realizing their derived equivalence comes from rotating the 2nd and 4th vertical line segments by 90 degrees (although there are many non-equivalent isotopies). 

By applying the variation of the Bondal-Thomsen collection to the front projection of this isotopy (following Section 5.2), we can compute the derived equivalence between these categories at the level of generating objects. 

49 

**==> picture [69 x 69] intentionally omitted <==**

**==> picture [79 x 80] intentionally omitted <==**

Figure 19. The Cox Skeleton and its Lagrangian projection 

**==> picture [69 x 69] intentionally omitted <==**

**----- Start of picture text -----**<br>
11 2<br>**----- End of picture text -----**<br>


**==> picture [79 x 79] intentionally omitted <==**

Figure 20. Partial resolution of _A_ 3 singularity. The regions can be braided around each other provided that the permutation sends the regions labelled 1 to each other. 

_Remark_ 5.8 _._ We could consider the “Cox Skeleton” for the _A_ 1 singularity, as drawn in Figure 19. The partially wrapped Fukaya category associated to this skeleton agrees with the Cox category (as defined in [Bal+25]) for the resolved _A_ 1 singularity; it also matches the skeleton from [DK21] at the discriminant point of the schober. While this Cox Legendrian is embedded, the isotopy of non-embedded graphs in the plane corresponding to a braid twist would cause a self-intersection to form in the Legendrian lift, and we thus expect its autoequivalence group to be smaller. 

## **5.4 Partial Resolutions of the** _An−_ 1 **singularity** 

As another consequence, we can recover a result of [DS15] on partial resolutions of the _An−_ 1 singularity. As before, let _X_[ˇ] Σ _In_ be the toric stack associated to a partial resolution of the _An−_ 1 singularity. Denote by _X_ ~~Σ~~ _[I] n_[the][underlying][space][of][this][stack.][By][[DS15],][there][is][an][equivalence] of categories 

**==> picture [272 x 16] intentionally omitted <==**

where _Ozi_ ( _j_ ) are the twists of the skyscraper sheaf at the stacky points of _X_[ˇ] Σ _In_ . The objects _Ozi_ ( _j_ ) are mirror to the linking disks of Λ _[I] n_[corresponding][to][the] _[q]_[2][=][0][horizontal][line][segments][in][the] Lagrangian projection of Λ _[I] n_[by][the][same][argument][as][in][Proposition][5.6.][By][Theorem][A.3,][we] therefore have an equivalence of categories _D[b]_ Coh( _X_ ~~Σ~~ _[I] n_[)] _[ ∼]_[=] _[ W]_[(] _[X,]_[ Λ] _I_ ~~_n_~~[)][where][Λ] _I_ ~~_n_~~[is][the][Legendrian] lift of the graph _ϕI_ ~~_n_~~[:][(] _[G,][ •]_[)] _[→][M]_[consisting][of][the][segment][[0] _[, n]_[]] _[ × {]_[0] _[}]_[and][cycles] _[r]_[=] _[i]_[for][each] _i ∈ I \ {n}_ (where we deduce HMS at the intermediate stack from quotienting the derived category of the smooth stack / localizing the _A_ -side via stop removal). 

We now record the braid-group actions that arise for these partial resolutions. The graph _ϕI_ ~~_n_~~[has] faces of integer areas _i_ 1 _−i_ 0 _, i_ 2 _−i_ 1 _, . . . , ik −ik−_ 1 where _I_ = _{i_ 0 _, i_ 1 _, . . . , ik}_ with 0 = _i_ 0 _< · · · < ik_ = _n_ . Let _π_ : _Bk → Sk_ denote the homomorphism recording the induced permutation of the strands. Given a coloring function _C_ : _{_ 1 _, . . . , k} →_ N, we define the _C_ -partitioned braid group 

**==> picture [226 x 13] intentionally omitted <==**

50 

to be those braids whose induced permutation fixes the coloring. Given _I_ , we produce a coloring function by _C[I]_ ( _j_ ) = _ij − ij−_ 1. By the same argument as Corollary 3.12, we have a natural inclusion 

**==> picture [108 x 17] intentionally omitted <==**

This gives an action of the _C_ -partitioned braid group[10] on _W_ ( _X,_ Λ _In_[).][In a similar fashion, whenever] _I, I[′] ⊂{_ 0 _, . . . , n}_ satisfy the property that there exists _σ ∈ Sk_ with _C[I] ◦ σ_ = _C[I][′]_ , it follows that Λ _I_ ~~_n_~~ _[′][∈L][emb]_ Λ _I_ ~~_n_~~[(] _[Y]_[ )][and][therefore][we][obtain][equivalences] 

**==> picture [276 x 18] intentionally omitted <==**

## **A Homological mirror symmetry for semiprojective toric Deligne-Mumford stacks** 

As noted in Section 2.1, there are various approaches to toric homological mirror symmetry. In this appendix, we outline how to extend the direct geometric approach [Abo09] to semiprojective toric Deligne-Mumford stacks over an arbitrary field k (or even over Z with respect to the split torus) in the sense of [BCS05]. We expect that the Floer-theoretic HMS equivalence can be extended to a broader class of toric stacks, namely those satisfying [Kuw20, Condition 1.1] for which HMS is proved sheaf-theoretically, but doing so would require technical work beyond the scope of this appendix, where we rely on what has been done for toric varieties to the largest extent possible. 

More precisely, recall that a smooth toric Deligne-Mumford stack _X_ Σ _,β_ from [BCS05] is encoded by the data of a simplicial fan Σ in _N_ R = _N ⊗_ R where _N_ is a lattice and a homomorphism _β_ : Z[Σ(1)] _→ N_ such that for all _ρ ∈_ Σ(1) we have _β_ ( _eρ_ ) = _bρuρ_ for some _bρ >_ 0 where _eρ_ is the standard basis vector of Z[Σ(1)] corresponding to _ρ_ and _uρ_ is the primitive generator of _ρ_ . We say that _X_ Σ _,β_ is semiprojective if the underlying coarse moduli space _X_ Σ is a semiprojective toric variety. Combinatorially, semiprojectivity means that Σ has full-dimensional convex support and there is a convex piecewise-linear function on Σ. Equivalently, Σ is the normal fan to a full-dimensional lattice polyhedron. Throughout this appendix, we will at times abbreviate _X_ Σ _,β_ to _X_ . 

**Definition A.1** ([Fan+14]) **.** The _FLTZ skeleton_ mirror to a toric stack is a cylindrical singular Lagrangian in _T[∗]_ ( _M_ R _/M_ ) = _M_ R _/M × N_ R where _M_ is the dual lattice to _N_ given by 

**==> picture [382 x 55] intentionally omitted <==**

where _π_ : _M_ R _→ M_ R _/M_ is the natural projection and 

_σ[⊥][β]_ = _m ∈ M_ R _|_ there exists _ℓ ∈_ Z[Σ(1)][�] _[∗]_ such that _⟨β_ R _[∗][m]_[ +] _[ ℓ, a][⟩]_[= 0][for][all] _[a][ ∈⟨][e][ρ][|][ ρ][ ∈][σ][⟩] ._ � � � Further, we set the _FLTZ stop_ to be ΛΣ _,β_ = _∂∞_ LΣ _,β_ . 

_Remark_ A.2 _._ In [Fan+14] and much of the literature on the coherent-constructible correspondence, (22) differs by a minus sign on the _σ_ factor. However, the category of sheaves with microsupport in LΣ _,β_ is most naturally identified in [GPS24a] with the opposite of the wrapped Fukaya stopped at ΛΣ _,β_ , _W_ ( _T[∗] M_ R _/M,_ ΛΣ _,β_ ). Following [GPS24a, Remark 1.2], one can simply negate the skeleton in order to avoid taking opposite categories, and thus it is natural to work with _W_ ( _T[∗] M_ R _/M,_ ΛΣ _,β_ ). 

> 10In [DS15], this is called the mixed braid group. 

51 

With our notation defined, we can now state the theorem that this appendix is concerned with. 

**Theorem A.3.** _If X_ Σ _,β is a smooth semiprojective toric Deligne-Mumford stack, there is a pretriangulated equivalence_ 

**==> picture [156 x 15] intentionally omitted <==**

_sending a line bundle to the corresponding tropical Lagrangian section._ 

Note that we use the term pre-triangulated equivalence to mean that the functor is fully faithful and its image generates (cf. [GPS24b]). 

## **A.1 The dg-category of line bundles on a toric stack** 

We now fix a smooth semiprojective toric stack _X_ = _X_ Σ _,β_ . In this section, we discuss line bundles on _X_ and the dg-enhancement of the derived category of _X_ that we need in Theorem A.3. 

Since _X_ is smooth, the Picard group of _X_ is isomorphic to the cokernel of the map _β[∗]_ : _M →_ Z[Σ(1)] dual to _β_ and given explicitly by _m �→_ ( _⟨m, β_ ( _eρ_ ) _⟩_ ) _ρ∈_ Σ(1). That is, any divisor[�] _aρDρ_ with _aρ ∈_ Z gives rise to a line bundle _OX_ ([�] _aρDρ_ ) and _OX_ ([�] _aρDρ_ ) = _[∼] OX_ ([�] _cρDρ_ ) if and only if there is an _m ∈ M_ such that _aρ_ = _cρ_ + _⟨m, β_ ( _eρ_ ) _⟩_ for all _ρ ∈_ Σ(1). Note that these coincide with equivariant line bundles on k[Σ(1)] with respect to the action by the kernel of the map of tori induced by _β_ . For the purposes of homological mirror symmetry, it is convenient to combinatorially encode these line bundles as support functions. Let 

**==> picture [418 x 13] intentionally omitted <==**

Using that Σ is simplicial, we can equivalently (and more canonically) characterize SF(Σ _, β_ ) as the set of piecewise linear functions on Σ that lift to integral piecewise linear functions on the smooth p fan Σ[p] in R[Σ(1)] with cones _σ_ = _⟨eρ | ρ ∈ σ⟩_ for _σ ∈_ Σ. With that observation, it is natural to define _ι_ : _M →_ SF(Σ _, β_ ) by setting _ι_ ( _m_ ) to be the support function on Σ corresponding to the linear function _⟨β[∗] m, ·⟩_ on Σ.[p] Given this setup, the following is straightforward to verify. 

## **Proposition A.4.** _The Picard group of X is isomorphic to_ SF(Σ _, β_ ) _/ι_ ( _M_ ) _._ 

Given _F ∈_ SF(Σ _, β_ ), we will denote the associated line bundle by _OX_ ( _F_ ). One can compute the cohomology of _OX_ ( _F_ ) by a Cech[ˇ] complex in essentially the same way as for a line bundle on a toric variety. Namely, the toric stack _X_ (Σ _,β_ ) with chosen stacky fan (Σ _, β_ ) has a canonical Cech[ˇ] cover. For each _σ ∈_ Σ there is an associated toric stack _U_ ( _σ,β|σ_ p ). We note that 

**==> picture [360 x 28] intentionally omitted <==**

respecting the natural _M_ grading on the left-hand side and the higher cohomology of _OX_ ( _F_ ) on _U_ ( _σ,β|σ_ p ) vanishes by the identification of _OX_ ( _F_ ) restricted to _U_ ( _σ,β|σ_ p ) with an equivariant line p bundle on the affine toric variety associated to _σ_ . We choose an ordering _{σi}i_ =1 _,...,|_ Σ(dim( _M_ )) _|_ of the maximal cones of Σ. Then, the Cech[ˇ] complex 

**==> picture [281 x 28] intentionally omitted <==**

52 

computes the degree _m ∈ M_ part of _H[d]_ ( _OX_ ( _F_ )) for any _F ∈_ SF(Σ _, β_ ) where the _m_ subscript on the global sections denotes the degree _m_ summand. We note that _U_ ( _σ_ 0 _,β|σ_ p0 ) _∩ . . . ∩ U_ ( _σd,β|σd_ p ) = _U_ ( _τ,β|τ_ p) for cone _τ_ = _σ_ 0 _∩ . . . ∩ σd ∈_ Σ so (23) implies that 

**==> picture [350 x 34] intentionally omitted <==**

Following [Abo09, Section 6.3], we now define a dg category _C_[ˇ] ( _X_ ) whose objects are the line bundles _OX_ ( _F_ ) and 

**==> picture [250 x 25] intentionally omitted <==**

equipped with the Cech differential and cup product.[ˇ] We let _Ddg[b]_[(] _[X]_[) be the pre-triangulated closure] of _C_[ˇ] ( _X_ ). 

**Proposition A.5.** _Ddg[b]_[(] _[X]_[)] _[is][a][dg][enhancement][of][D][b]_[(] _[X]_[)] _[.]_ 

_Proof._ By construction and Proposition A.4, the morphism complexes in _C_[ˇ] ( _X_ ) compute the derived morphisms between all line bundles on _X_ . Thus, the claim follows from the fact that line bundles generate _D[b]_ ( _X_ ). While this claim holds more generally for smooth quasi-projective DeligneMumford stacks, we could not find a clean reference. In the case of interest here, [HHL24] shows that there is a resolution of the diagonal by direct sums of line bundles, which in the proper case implies generation, and in the non-proper case also implies generation after compactifying. 

## **A.2 Tropical Lagrangian sections to Morse theory** 

In this section, we construct the mirror tropical Lagrangian sections to line bundles on _X_ and analyze their Floer theory analogously to [Abo09; Han19; HH22]. Given a piecewise linear function _F_ on _|_ Σ _|_ , we will extend _F_ continuously to a piecewise linear function on _N_ R (if necessary) and consider smoothings of the form 

**==> picture [296 x 27] intentionally omitted <==**

where _g_ : R _≥_ 0 _→_ R _≥_ 0 is a smooth function that is constant near 0, _η_ : _N_ R _→_ R is a smooth symmetric mollifier function supported on the ball of radius 1, we set _ηt_ ( _u_ ) = _t[−][n] η_ ( _u/t_ ), and _r_ = _|u|_ is the length of _u_ with respect to a Euclidean metric on _N_ R. 

Calculating as in [HH22, Lemma 3.1], we have 

**==> picture [385 x 28] intentionally omitted <==**

where _·_ is the Euclidean inner product and we’ve identified _N_ R with its tangent space. If we assume that _g_ ( _r_ ) = _εr_ outside of a compact set, then _H[F,g]_ is 1-homogeneous outside of a compact set, that is, it is a cylindrical Hamiltonian on _T[∗]_ ( _M_ R _/M_ ) = _M_ R _/M × N_ R. Given _F ∈_ SF(Σ _, β_ ) and 0 _< a ≪_ 1, we set _Fa_ = _F − FK[a]_[where] _[F][ a] K_[is][the][support][function][of][the][(real)][scaling][of][the] canonical divisor _−_[�] _aDρ_ and, if necessary, we extend this function so that _Fa_ ( _u_ ) is a positive piecewise linear function with lim _a→_ 0 _Fa_ ( _u_ ) = + _∞_ monotonically for _u_ outside of _|_ Σ _|_ . We define 

53 

_Hcyl[F,a,ε]_ = _H[F][a][,g]_ where _g_ ( _r_ ) = _εr_ outside of a compact set. From (24) and again calculating as in [HH22, Lemma 3.1], we have that 

**==> picture [314 x 21] intentionally omitted <==**

for some constant _CF_ on a complement of a compact subset in the cone 

_Uρ[ε]_[= cone] _[{][u][ ∈][N]_[R] _[| |][u][|]_[ = 1] _[, u][ ∈]_[star(] _[ρ]_[)] _[,]_[and] _[d]_[(] _[u, σ]_[)] _[ > ε]_[for][all] _[σ][∈]_[Σ][such][that] _[ρ][ ̸∈][σ][}]_ for all _ρ ∈_ Σ(1). For any _a <_ 1 _/_ (max _ρ bρ_ ) we can choose _ε_ small enough so that _bρdHcyl[F,a,ε]_ ( _uρ_ ) _̸∈_ Z on the complement of a compact subset of _Uρ[ε]_[since] _[b][ρ][F]_[(] _[u][ρ]_[)] _[∈]_[Z][.][Thus,][for][any] _[a][<]_[1] _[/]_[(max] _[ρ][b][ρ]_[),] it follows that the cylindrical Lagrangian 

**==> picture [128 x 21] intentionally omitted <==**

satisfies _∂∞L[a,ε][∩]_[Λ][Σ] _[,β]_[=] _[∅]_[for][all][sufficiently][small] _[ε]_[and][hence][determines][an][object][of] _cyl_[(] _[F]_[)] _W_ ( _T[∗] M_ R _/M,_ ΛΣ _,β_ ). Note that _L[a,ε] cyl_[has][canonical][grading][and][orientation][data][by][[GPS24a],][and] we always work with that data when viewing _L[a,ε] cyl_[(] _[F]_[)][as][an][object][of] _[W]_[(] _[T][ ∗][M]_[R] _[/M,]_[ Λ][Σ] _[,β]_[).][Further,] all _L[a,ε]_[for][small] _[a, ε]_[are][Hamiltonian][isotopic][through][an][isotopy][avoiding][Λ][Σ] _[,β]_[at][infinity][and] _cyl_[(] _[F]_[)] hence the object _L[a,ε] cyl_[(] _[F]_[)][in] _[W]_[(] _[T][ ∗][M]_[R] _[/M,]_[ Λ][Σ] _[,β]_[)][is][independent][of] _[a, ε]_[up][to][quasi-isomorphism.] Therefore, we may at times drop _ε_ and/or _a_ from the notation. 

Moreover, we can construct explicit cofinal wrappings of these objects by taking _a, ε_ to zero. 

**Proposition A.6.** _For_ 0 _< a <_ 1 _/_ max _ρ bρ and ε >_ 0 _sufficiently small as above, taking a, ε monotonically to zero gives a cofinal wrapping of L[a,ε] cyl_[(] _[F]_[)] _[.]_ 

_Proof._ Over _|_ Σ _|_ , we can check that the isotopy is positive at infinity by the same calculation as in [HH22, Lemma 3.3] using (24). Moreover, (25) shows that every point in _L[a,ε] cyl_[(] _[F]_[)][over] _[|]_[Σ] _[|]_ approaches ΛΣ _,β_ as _a, ε_ go to zero. Away from _|_ Σ _|_ , we have taken _Fa_ = _u/a_ to be a linear function with monotonically increasing slope approaching _∞_ as _a_ goes to zero. We thus have a cofinal wrapping by [GPS24b, Lemma 2.2]. 

Note that the upper bound _a <_ 1 _/_ max _ρ bρ_ is not relevant for the claim that taking _a_ to 0 gives a cofinal wrapping. However, this bound prevents the Lagrangian from intersecting the stop as _a_ changes and thus (potentially) changing _L[a,ε] cyl_[(] _[F]_[)][as][an][object][of] _[W]_[(] _[T][ ∗][M]_[R] _[/M,]_[ Λ][Σ] _[,β]_[).][As][such,][we] define _B_ := 1 _/_ max _ρ∈_ Σ(1) _bρ_ and use this upper bound in later constructions. 

Now, we will compute the subcategory of _W_ ( _T[∗] M_ R _/M,_ ΛΣ _,β_ ) consisting of the _Lcyl_ ( _F_ ) by passing to an equivalent category that is better suited for a direct analysis of Floer theory. Namely, we will work in the context of monomial admissibility in the sense of [Han19]. We will identify _T[∗] M_ R _/M_ with _M ⊗_ C _[∗]_ by choosing a strictly convex function _φ_ : _M_ R _→_ R and taking the Legendre transform. More explicitly, _M_ R is the base of the Log map and we use _φ_ to make the standard symplectic form on _T[∗] M_ R _/M_ into the K¨ahler form 

**==> picture [218 x 27] intentionally omitted <==**

where _pj_ are coordinates on _N_ R and _qj_ are the corresponding dual coordinates on _M_ R _/M_ . For _ρ ∈_ Σ(1), we set 

_Cρ[δ]_[=] _[ {][u][ ∈]_[star(] _[ρ]_[)] _[ |][ d]_[(] _[u, σ]_[)] _[ ≥][δ]_[for][all] _[σ][∈]_[Σ][such][that] _[ρ][ ̸∈][σ][}]_ for any _δ >_ 0. The following is a slight generalization of [Han19, Corollary 2.40]. 

54 

**Proposition A.7.** _For sufficiently small δ, there exist kρ ∈_ R _>_ 0 _and a strictly convex φ such that for all z_ = ( _p, q_ ) _outside of a compact set, the maximum_ 

**==> picture [269 x 21] intentionally omitted <==**

_is achieved by a ρ such that p ∈ Cρ[δ][.]_ 

_Proof._ The claim follows from the same argument as [Han19, Corollary 2.40], which does not use smoothness of the fan. This is perhaps more easily seen by noting that, in the language of [Han19], our proposition is asserting the existence of a monomial division adapted to the stacky fan (Σ _, β_ ). In particular, the construction of a K¨ahler form adapted to a polytope from [Zho20] holds when the normal fan is simplicial. 

Now, we proceed to construct monomially admissible Lagrangian sections in the sense of [Han19] and a category of these objects. For _F ∈_ SF(Σ _, β_ ), we define _Hmon[F,ε]_[=] _[ H][F,g]_[where] _[g]_[(] _[r]_[) =] _[ ε]_[and] 

**==> picture [134 x 14] intentionally omitted <==**

By (24), we have that 

**==> picture [283 x 15] intentionally omitted <==**

over _Cρ[δ]_[for][all] _[ε < δ]_[.][As][in][the][cylindrical][case,][we][will][at][times][assume] _[ε]_[to][be][sufficiently][small,] drop it from the notation, and simply write _Lmon_ ( _F_ ). 

Then, following [Han19, Section 3] and using Proposition A.7 to prove that Floer theory is well-defined, we can construct a category _Fmon_ (Σ _, β_ ) by localization. The objects of the ordered category are pairs ( _Lmon_ ( _F_ ) _, a_ ) with _a ∈_ (0 _, B_ ) and “right-way” morphisms are Floer cochain complexes. That is, we define hom ( _Lmon_ ( _F_ 1) _, a_ 1) _,_ ( _Lmon_ ( _F_ 2) _, a_ 2) to be � � 

**==> picture [355 x 46] intentionally omitted <==**

where _e_ ( _Lmon_ ( _F_ 1) _,a_ 1) is a formal degree zero identity element. The Floer chain complexes and higher operations are computed with respect to the canonical brane structures on these sections and (domain dependent) almost complex structures making the functions _z[b][ρ][u][ρ]_ holomorphic over the complement of a compact subset of _Cρ[δ]_[for][all] _[ρ][∈]_[Σ(1).][Then,] _[F][mon]_[(Σ] _[, β]_[)][is][defined][as][the] localization at natural continuation elements in _CF_ ( _Lmon_ ( _F − FK[a]_[1][)] _[, L][mon]_[(] _[F][ −][F] K[ a]_[2][)) when] _[ a]_[1] _[< a]_[2][.] 

To make computations in _W_ ( _T[∗] M_ R _/M,_ ΛΣ _,β_ ) and prove Theorem A.3, we can work instead with _Fmon_ (Σ _, β_ ) thanks to the following. 

**Proposition A.8.** _There is a pre-triangulated equivalence Fmon_ (Σ _, β_ ) _−→W[∼]_ ( _T[∗] M_ R _/M,_ ΛΣ _,β_ ) _taking_ ( _Lmon_ ( _F_ ) _, a_ ) _to L[a] cyl_[(] _[F]_[)] _[for][every][F][∈]_[SF(Σ] _[, β]_[)] _[.]_ 

_Proof._ First, we note that there is a quasi-equivalence between _Fmon_ (Σ _, β_ ) and the subcategory of _W_ ( _T[∗] M_ R _/M,_ ΛΣ _,β_ ) consisting of the Lagrangian sections _Lcyl_ ( _F_ ). This follows from the same argument as in [HH22, Theorem 3.5] where the main idea is to use Lagrangians which are the graphs of _dH[F,g]_ where _g_ is a monotonic function that is linear on a large interval after which it becomes constant. If the interval is large enough, the integrated maximum principle implies that 

55 

the Floer theory is that of _Lcyl_ ( _F_ ) in a Liouville subdomain while (25) precludes the introduction of additional intersections while interpolating to a _Lmon_ ( _F_ ). The details are exactly the same as in [HH22, Theorem 3.5]. 

It remains to verify that _W_ ( _T[∗] M_ R _/M,_ ΛΣ _,β_ ) is generated by the _Lcyl_ ( _F_ ). To see this, for any _θ ∈ M_ R _/M_ , we consider the Lagrangian _Lθ_ given by the outward conormal to a small ball around _θ ∈ M_ R _/M_ .[11] By [GPS24a, Proposition 5.22 and Remark 5.23] and stop removal, the Lagrangians _Lθ_ generate _W_ ( _T[∗] M_ R _/M,_ ΛΣ _,β_ ). We conclude by showing that each _Lθ_ is Hamiltonian isotopic to some _Lcyl_ ( _F_ ) in the complement of ΛΣ _,β_ , which is a generalization of [HH22, Lemma 3.14]. By definition, the Lagrangian _Lθ_ can be written as the graph of the differential of a function _f_ : _N_ R _→_ R that satisfies 

**==> picture [108 x 12] intentionally omitted <==**

on _Uρ[ε]_[for][all] _[ρ][∈]_[Σ(1)][where] _[g]_[(] _[u]_[)][is][an][arbitrarily][small][positive][function.][Let] _[F][∈]_[SF(Σ] _[, β]_[)][be] such that 

**==> picture [293 x 28] intentionally omitted <==**

For sufficiently small _g_ ( _u_ ), it then follows from (25) that _bρdft_ ( _uρ_ ) _̸∈_ Z where _ft_ = (1 _− t_ ) _f_ + _tHc[F] yl_[.] That is, we have produced a Hamiltonian isotopy from _Lθ_ to _Lcyl_ ( _F_ ) in the complement of ΛΣ _,β_ . 

Note that the proof of generation by tropical Lagrangian sections in [HH22] is more involved and uses an inductive argument by restriction to the toric boundary divisors. The corresponding approach for stacks should go through as well, but we have chosen to take a more direct path in Proposition A.8 that uses natural generators of the derived category that have received recent interest. Namely, the support functions defined by (28) correspond to the line bundles that are summands of the pushforward of the canonical bundle under the toric Frobenius morphism. To obtain mirror Lagrangians to the summands of the pushforward of the structure sheaf under toric Frobenius, which have been dubbed the Bondal-Thomsen or Thomsen collection [Tho00; Bon06; HHL24; Bal+25], one takes the inward conormal to a small ball around _θ_ rather than the outward conormal _Lθ_ . See Section 5.2. 

_Remark_ A.9 _._ It should also be possible to avoid passing to _Fmon_ (Σ _, β_ ) altogether and carry out the Morse theory arguments that follow directly in the cylindrical setting. While such an approach would be more direct when working from scratch, we have opted to instead rely on work already in the literature to the extent that is possible. The more direct approach would be interesting to pursue in another venue and could also allow one to work with more general fans. 

With Proposition A.8 in hand, we can now carry out the strategy in [Abo09] (also outlined in [Han19, Section 3.5]) and pass to Morse theory. 

First, we need to carry out the Morse theory analogue of the construction of _Fmon_ (Σ _, β_ ). We start with an ordered category whose objects are pairs ( _Hmon[F][, a]_[)][with] _[a][∈]_[(0] _[, B]_[)][and][we][define] hom ( _Hmon[F]_[1] _[, a]_[1][)] _[,]_[ (] _[H] mon[F]_[2] _[, a]_[2][)] to be � � 

**==> picture [387 x 61] intentionally omitted <==**

> 11The Lagrangians _Lθ_ are introduced and studied in a more general context in [GPS24a, Section 5.2]. 

56 

where _e_ ( _HmonF_ 1 _[,a]_ 1[)][is][a][formal][degree][zero][identity][element][and] _[CM]_[denotes][the][Morse][complex][with] respect to a Riemannian metric on _N_ R inducing a complex structure on _T[∗] M_ R _/M_ satisfying the property required in the construction of _Fmon_ (Σ _, β_ ) above, which is well-defined by a slight generalization of [Han19, Proposition 3.28] with an essentially identical proof. Higher _A∞_ operations are defined by counts of Morse trees. Then, we define _M_ (Σ _, β_ ) to be the localization at any chain-level representative of a generator of _HM −HmonFK[a]_[2][+] _[ H] monFK[a]_[1] _∼_ = k. The concluding result of this section � � reduces the computation of _Fmon_ (Σ _, β_ ) to _M_ (Σ _, β_ ) by applying [FO97, Theorem 2.3]. 

**Proposition A.10.** _The natural identifications between objects and morphisms induce a quasiequivalence_ 

**==> picture [110 x 12] intentionally omitted <==**

_Proof._ The proof is identical to that of [Han19, Corollary 3.31], which is itself modeled on [Abo09, Theorem 5.8]. The only modification is to replace every instance of the monomial _z[u][ρ]_ for some _ρ ∈_ Σ(1) with _z[b][ρ][u][ρ]_ . 

## **A.3 Proof of Theorem A.3** 

We will now identify the structures developed in Appendix A.1 and Appendix A.2 to prove Theorem A.3. Namely, Theorem A.3 follows immediately from Proposition A.5, Proposition A.8, Proposition A.10 and the following. 

**Proposition A.11.** _There is a quasi-equivalence_ 

**==> picture [88 x 14] intentionally omitted <==**

## _taking_ ( _Hmon[F][, a]_[)] _[to][O][X]_[(] _[F]_[)] _[for][all][F][∈]_[SF(Σ] _[, β]_[)] _[and][a][ ∈]_[(0] _[, B]_[)] _[.]_ 

Since we have described _M_ (Σ _, β_ ) and _C_[ˇ] ( _X_ ) entirely in terms of support functions, the proof of Proposition A.11 is essentially identical to that of the non-stacky case in [Abo09] and its reproduction in [Han19, Section 3.5] with some minor adjustments allowing for Σ to not be complete. Nevertheless, the remainder is dedicated to outlining the proof of Proposition A.11 in our notation closely following the aforementioned references. 

In order to proceed in the most efficient manner and take advantage of the literature, it will be useful to pass to Morse theory on a compact set (see [Han19, Remark 3.33] though we note that we expect the argument to be considerably more complicated outside of the semi-projective and simplicial setting). To that end, if Σ is complete, we can assume without loss of generality that all _Hmon[F]_[that][appear][in][objects][of] _[M]_[(Σ] _[, β]_[)][satisfy][(27)][on] _[C] ρ[δ]_[outside][the][interior][of][a][compact][set] _Y ⊂ N_ R whose boundary is a large level set of the function on _N_ R induced by (26). In other words, when Σ is complete, _Y_ = _∇φ_ ( _Q_ ) where _Q ⊂ M_ R is given by 

**==> picture [75 x 13] intentionally omitted <==**

for all _ρ_ and some large constant _y_ , and Proposition A.7 implies that _Q_ is a moment polytope of _X_ Σ. If Σ is not complete, we simply take _Y_ = _∇φ_ ( _Q_ ) for some large moment polytope _Q_ of a simplicial completion of Σ and additionally assume that all _Hmon[F]_[are linear away from a neighborhood of the] images of the facets of _Q_ that are dual to rays of Σ. In general, the result is that all critical points 

57 

and Morse flow trees involved in computing morphisms in _M_ (Σ _, β_ ) lie in the interior of _Y_ as in [Han19, Proposition 3.28]. 

Now, we pass from Morse theory on _Y_ to simplicial chains on _Y_ . We let _Yb_ be the triangulation obtained as the image under _∇φ_ of the barycentric subdivision _Qb_ of _Q_ . Given a function _h_ on _Y_ such that _h_ ( _uρ_ ) is constant on _Yρ_ := _∇φ_ ( _Qρ_ ) for every facet _Qρ_ with primitive normal vector _uρ_ , we define _∂h_[+] _[Y][b]_[to][be][the][closure][of][the][maximal][simplices] _[τ]_[of] _[Y][b]_[where] _[∂τ][ ∩][∂Y][⊂][Y][ρ]_[and] _[h]_[(] _[u][ρ]_[)][is] positive. To define the simplicial category, we again start with an ordered category whose objects are pairs ( _F, a_ ) with _F ∈_ SF(Σ _, β_ ) and _a ∈_ (0 _, B_ ) and define 

**==> picture [415 x 54] intentionally omitted <==**

where _e_ ( _F_ 1 _,a_ 1) is a formal degree zero identity element and _C_ denotes the relative simplicial cochains on a simplicial pair. This is a dg-category with product induced by the cup product and the inclusion 

**==> picture [347 x 18] intentionally omitted <==**

as defined more generally in [Abo09, Definition E.2]. We define Simp _mon_ ( _Y_ ) to be the localization _∼_ at any chain-level representative of a generator of _H_ � _Yb, ∂−_[+] _FK[a]_[2][+] _[F][ a] K_[1] � = k lying in the degree 0 _∈ M_ piece of hom(( _F, a_ 1) _,_ ( _F, a_ 2)) with _a_ 2 _> a_ 1. We then have the following categorical version of the usual identification, used by Abouzaid, of the Morse cohomology of boundary convex functions with relative cohomology. 

**Proposition A.12.** _There is a quasi-equivalence_ 

**==> picture [120 x 13] intentionally omitted <==**

_taking_ ( _Hmon[F][, a]_[)] _[to]_[(] _[F, a]_[)] _[for][all][F][∈]_[SF(Σ] _[, β]_[)] _[and][a][ ∈]_[(0] _[, B]_[)] _[.]_ 

_Proof._ The claim follows from [Abo09, Corollary 4.33] as described in the last paragraph of the proof of Proposition 6.7 of [Abo09] (see also [Han19, Proposition 3.38]). 

Before comparing the simplicial category to the Cech[ˇ] category of line bundles, it is helpful to simplify the former slightly by removing the push-offs by _FK_ from the stop that were needed for wrapping in the Fukaya and Morse categories and working more directly on _Q_ . Since we need to keep the large wrapping if Σ is not complete, we define a new family of piecewise-linear functions _F_ 0 _[a]_[such][that] _[F]_ 0 _[ a]_[is][0][on] _[|]_[Σ] _[|]_[and] _[F]_ 0 _[ a]_[is][positive][away][from] _[|]_[Σ] _[|]_[and][tends][monotonically][to][+] _[∞]_[as] _[a]_ tends to 0. For example, we can take _F_ 0 _[a]_[to][be][a][support][function][for] _[−]_[�] _ρ∈_ Σ _Q_ (1) _\_ Σ(1) _a_ 1 _[D][ρ]_[where] Σ _Q_ is the normal fan to _Q_ . Now, we define a category Simp _mon_ ( _Q_ ) defined exactly as Simp _mon_ ( _Y_ ) except replacing all _FK[a]_[with] _[F]_ 0 _[ a]_[,] _[Y][b]_[with] _[Q][b]_[,][and][defining] _[∂] h_[+] _[Y][b]_[to][be][the][closure][of][the][maximal] simplices _τ_ of _Qb_ where _∂τ ∩ ∂Q ⊂ Qρ_ and _h ◦∇φ_ ( _uρ_ ) is positive. Note that if Σ is complete, _F_ 0 is identically zero and Simp _mon_ ( _Q_ ) can be defined without the parameter _a_ and any localizations by simply setting the hom spaces to be direct sums of _C_ � _Qb, ∂F_[+] 2 _−F_ 1+ _m[Q][b]_ �. The proof of the following is identical to that of [Han19, Proposition 3.39]. 

58 

**Proposition A.13.** _There is a quasi-equivalence_ 

Simp _mon_ ( _Y_ ) _≃_ Simp _mon_ ( _Q_ ) 

_which is the identity on objects._ 

The final step of identifying Simp _mon_ ( _Q_ ) with _C_[ˇ] ( _X_ ) is almost entirely topological: one identifies simplicial cochains with Cech[ˇ] cochains and observes that the toric Cech[ˇ] cover on _X_ indexes a topological Cech[ˇ] cover of _Q_ after dualizing the index set from Σ _Q_ . 

**Proposition A.14.** _There is a quasi-equivalence_ 

**==> picture [106 x 13] intentionally omitted <==**

_taking_ ( _F, a_ ) _to OX_ ( _F_ ) _for all F ∈_ SF(Σ _, β_ ) _and a ∈_ (0 _, B_ ) _._ 

_Proof._ In the complete case, the claim follows from Proposition 6.9 and the claim in the proof of Proposition 6.7 of [Abo09] (see also [Han19, Proposition 3.40]). 

If Σ is not complete, let _XQ_ be the smooth toric Deligne-Mumford stack associated to Σ _Q_ with stacky fan structure extending that of Σ by setting _bρ_ = 1 for all _ρ ∈_ Σ _Q_ (1) _\_ Σ(1). We choose _F_ 0 _[a]_[to] 1 be the support function of _−_[�] _ρ∈_ Σ _Q_ (1) _\_ Σ(1) _a[D][ρ]_[ as suggested above.][In that case, Abouzaid’s results] (and considering the _M_ grading) identify Simp _mon_ ( _Q_ ) with the localization of _C_[ˇ] ( _XQ_ ) at the natural transformation given by tensoring by a defining section of the divisor _D_ :=[�] _ρ∈_ Σ _Q_ (1) _\_ Σ(1) _[D][ρ]_[(cf.] [Han19, Theorems 4.5 and 4.9]). As observed in [Sei08][12] , this localization is _C_[ˇ] ( _XQ \ D_ ). Moreover, by construction, we have _X_ = _XQ \ D_ . 

We end by noting that chaining together Proposition A.12, Proposition A.13, and Proposition A.14 gives Proposition A.11 which was the goal of this section. 

## **References** 

- [Abo06] Mohammed Abouzaid. “Homogeneous coordinate rings and mirror symmetry for toric varieties.” _Geometry and Topology_ 10 (2006), pp. 1097–1156. 

- [Abo09] Mohammed Abouzaid. “Morse homology, tropical geometry, and homological mirror symmetry for toric varieties.” _Selecta Mathematica_ 15 (2009), pp. 189–270. 

- [AHA98] Franz Aurenhammer, Friedrich Hoffmann, and Boris Aronov. “Minkowski-type theorems and least-squares clustering.” _Algorithmica_ 20 (1998), pp. 61–76. 

- [Aur07] Denis Auroux. “Mirror symmetry and T-duality in the complement of an anticanonical divisor.” _Journal of G¨okova Geometry Topology_ 1 (2007), pp. 51–91. 

- [Aur08] Denis Auroux. “Special Lagrangian fibrations, wall-crossing, and mirror symmetry.” _Surveys in Differential Geometry_ 13.1 (2008), pp. 1–48. 

- [Bal+25] Matthew R. Ballard, Christine Berkesch, Michael K. Brown, Lauren Cranton Heller, Daniel Erman, David Favero, Sheel Ganatra, Andrew Hanlon, and Jesse Huang. _King’s Conjecture and the Cox category_ . 2025. arXiv: `2501.00130 [math.AG]` . url: `https: //arxiv.org/abs/2501.00130` . 

> 12In Seidel’s paper, this observation is made in the context of varieties, but it applies equally to toric DeligneMumford stacks by, for instance, thinking of the objects as equivariant sheaves on affine space. 

59 

|[Bar26]|Michela Barbieri. “Mirror symmetry monodromy actions on derived categories.” PhD|
|---|---|
||thesis. University College London, Apr. 2026.|
|[BCS05]|Lev Borisov, Linda Chen, and Gregory Smith. “The orbifold Chow ring of toric Deligne-|
||Mumford stacks.”_Journal of the American Mathematical Society_ 18.1 (2005), pp. 193–|
||215.|
|[Ber+25]|Christine Berkesch, Lauren Cranton Heller, Gregory G. Smith, and Jay Yang._Cellular_|
||_free resolutions for normalizations of toric ideals_. 2025. arXiv: `2512.17871`.|
|[BFK19]|Matthew Ballard, David Favero, and Ludmil Katzarkov. “Variation of geometric in-|
||variant theory quotients and derived categories.”_Journal f¨ur die reine und angewandte_|
||_Mathematik (Crelles Journal)_ 2019.746 (2019), pp. 235–303.|
|[BG09]|Jim Bryan and Tom Graber. “The crepant resolution conjecture.”_Proc. Sympos. Pure_|
||_Math_. Vol. 80. 2009, pp. 23–42.|
|[BG25]|Igor Belegradek and Mohammad Ghomi. “Point selections from Jordan domains in Rie-|
||mannian surfaces.”_Transactions of the American Mathematical Society_ 378.03 (2025),|
||pp. 1681–1696.|
|[BKS18]|Alexey Bondal, Mikhail Kapranov, and Vadim Schechtman. “Perverse schobers and|
||birational geometry.” _Selecta Mathematica_ 24.1 (2018), pp. 85–143.|
|[Bon06]|Alexei Bondal. “Derived categories of toric varieties.” Vol. 3. 1. Abstracts from the|
||workshop held January 29–February 4, 2006, Organized by Klaus Altmann, Victor|
||Batyrev and Bernard Teissier, Oberwolfach Reports. Vol. 3, no. 1. 2006, pp. 284–286.|
|[Bri09a]|Tom Bridgeland. “Spaces of stability conditions.” _Algebraic geometry—Seattle 2005._|
||_Part_ 1 (2009), pp. 1–21.|
|[Bri09b]|Tom Bridgeland. “Stability conditions and Kleinian singularities.”_International Math-_|
||_ematics Research Notices_ 2009.21 (2009), pp. 4142–4157.|
|[BW25]|Jishnu Bose and Harold Williams. _Contact isotopies in the coherent-constructible cor-_|
||_respondence_. 2025. arXiv: `2505.05012`.|
|[CATD93]|Juan Antonio Cuesta-Albertos and A Tuero-Diaz. “A characterization for the solution|
||of the Monge—Kantorovich mass transference problem.”_Statistics & probability letters_|
||16.2 (1993), pp. 147–152.|
|[Cha+17]|Kwokwai Chan, Siu-Cheong Lau, Naichung Conan Leung, and Hsian-Hua Tseng. “Open|
||Gromov–Witten invariants, mirror maps, and Seidel representations for toric mani-|
||folds.” _Duke Mathematical Journal_ 166.8 (2017), pp. 1405–1462.|
|[CIJ18]|Tom Coates, Hiroshi Iritani, and Yunfeng Jiang. “The crepant transformation conjec-|
||ture for toric complete intersections.” _Advances in Mathematics_ 329 (2018), pp. 1002–|
||1087.|
|[CLL12]|Kwokwai Chan, Siu-Cheong Lau, and Naichung Conan Leung. “SYZ mirror symmetry|
||for toric Calabi-Yau manifolds.”_Journal of Diferential Geometry_ 90.2 (2012), pp. 177–|
||250.|
|[CLS11]|David A Cox, John B Little, and Henry K Schenck._Toric varieties_. Vol. 124. American|
||Mathematical Society, 2011.|



60 

|[DK21]|Will Donovan and Tatsuki Kuwagaki. “Mirror symmetry for perverse schobers from|
|---|---|
||birational geometry.” _Communications in Mathematical Physics_ 381 (2021), pp. 453–|
||490.|
|[DS15]|Will Donovan and Ed Segal. “Mixed braid group actions from deformations of surface|
||singularities.” _Communications in Mathematical Physics_ 335.1 (2015), pp. 497–543.|
|[DW25]|Will Donovan and Michael Wemyss. “Stringy K¨ahler moduli, mutation and mon-|
||odromy.” _Journal of Diferential Geometry_ 129.1 (2025), pp. 115–164.|
|[Fan+11]|Bohan Fang, Chiu-Chu Melissa Liu, David Treumann, and Eric Zaslow. “A categorif-|
||cation of Morelli’s theorem.” _Inventiones mathematicae_ 186.1 (2011), pp. 79–114.|
|[Fan+14]|Bohan Fang, Chiu-Chu Melissa Liu, David Treumann, and Eric Zaslow. “The coherent–|
||constructible correspondence for toric Deligne–Mumford stacks.” _International Math-_|
||_ematics Research Notices_ 2014.4 (2014), pp. 914–954.|
|[FH23]|David Favero and Jesse Huang. “Rouquier dimension is Krull dimension for normal|
||toric varieties.” _European Journal of Mathematics_ 9.4 (2023), p. 91.|
|[FO97]|Kenji Fukaya and Yong-Geun Oh. “Zero-loop open strings in the cotangent bundle and|
||Morse homotopy.” _Asian J. Math_ 1.1 (1997), pp. 96–180.|
|[Gan+24]|Sheel Ganatra, Andrew Hanlon, Jef Hicks, Daniel Pomerleano, and Nick Sheridan.|
||_Homological mirror symmetry for Batyrev mirror pairs_. 2024. arXiv: `2406.05272`.|
|[GKZ94]|I. M. Gelfand, M. M. Kapranov, and A. V. Zelevinsky. _Discriminants, resultants and_|
||_multidimensional determinants_. Modern Birkh¨auser Classics. Reprint of the 1994 edi-|
||tion. Boston, MA: Birkh¨auser Boston, Inc., 1994, pp. x+523. isbn: 978-0-8176-4770-4.|
|[GM18]|Mark Gross and Diego Matessi. “On homological mirror symmetry of toric Calabi-Yau|
||threefolds.” _Journal of Symplectic Geometry_ 16.5 (2018), pp. 1249–1349.|
|[GPS24a]|Sheel Ganatra, John Pardon, and Vivek Shende. “Microlocal Morse theory of wrapped|
||Fukaya categories.” _Annals of Mathematics_ 199.3 (2024), pp. 943–1042.|
|[GPS24b]|Sheel Ganatra, John Pardon, and Vivek Shende. “Sectorial descent for wrapped Fukaya|
||categories.” _Journal of the American Mathematical Society_ 37.2 (2024), pp. 499–635.|
|[GS22]|Benjamin Gammage and Vivek Shende. “Mirror symmetry for very afne hypersur-|
||faces.” _Acta Mathematica_ 229.2 (2022), pp. 287–346.|
|[Han19]|Andrew Hanlon. “Monodromy of monomially admissible Fukaya-Seidel categories mir-|
||ror to toric varieties.” _Advances in Mathematics_ 350 (2019), pp. 662–746.|
|[Har77]|Robin Hartshorne. _Algebraic geometry_. Vol. 52. Springer Science & Business Media,|
||1977.|
|[HH22]|Andrew Hanlon and Jef Hicks. “Aspects of functoriality in homological mirror sym-|
||metry for toric varieties.” _Advances in Mathematics_ 401 (2022), p. 108317.|
|[HHL24]|Andrew Hanlon, Jef Hicks, and Oleg Lazarev. “Resolutions of toric subvarieties by|
||line bundles and applications.” _Forum of Mathematics, Pi_ 12 (2024), e24.|
|[HHL26]|Andrew Hanlon, Jef Hicks, and Oleg Lazarev. “Relating categorical dimensions in|
||topology and symplectic geometry.” _Transactions of the American Mathematical Soci-_|
||_ety_ (2026). Published electronically March 11, 2026. doi: `10.1090/tran/9633`. url:|
||`https://doi.org/10.1090/tran/9633`.|



61 

|[HL15]|Daniel Halpern-Leistner. “The derived category of a GIT quotient.” _Journal of the_|
|---|---|
||_American Mathematical Society_ 28.3 (2015), pp. 871–912.|
|[HLS16]|Daniel Halpern-Leistner and Ian Shipman. “Autoequivalences of derived categories via|
||geometric invariant theory.” _Advances in Mathematics_ 303 (2016), pp. 1264–1299.|
|[HLS20]|Daniel Halpern-Leistner and Steven Sam. “Combinatorial constructions of derived|
||equivalences.” _Journal of the American Mathematical Society_ 33.3 (2020), pp. 735–|
||773.|
|[Hun07]|J. D. Hunter. “Matplotlib: A 2D graphics environment.” _Computing in Science &_|
||_Engineering_ 9.3 (2007), pp. 90–95.|
|[Huy06]|Daniel Huybrechts. _Fourier-Mukai transforms in algebraic geometry_. Clarendon Press,|
||2006.|
|[HV00]|Kentaro Hori and Cumrun Vafa. _Mirror symmetry_. 2000.|
|[HZ22]|Jesse Huang and Peng Zhou. “Variation of GIT and variation of Lagrangian skeletons|
||II: Quasi-symmetric case.” _Advances in Mathematics_ 408 (2022), p. 108597.|
|[Kit18]|Alexandre Fabrice Kite. “Fundamental Group Actions on Derived Categories.” Avail-|
||able at `https://kclpure.kcl.ac.uk/ws/portalfiles/portal/115640240/2019_`|
||`Kite_Alexandre_Fabrice_1477558_ethesis.pdf`. PhD thesis. King’s College Lon-|
||don, Dec. 2018.|
|[KN79]|George Kempf and Linda Ness. “The length of vectors in representation spaces.”|
||_Algebraic geometry (Proc. Summer Meeting, Univ. Copenhagen, Copenhagen, 1978)_.|
||Vol. 732. Lecture Notes in Math. Springer, Berlin, 1979, pp. 233–243. isbn: 3-540-|
||09527-6.|
|[KS14]|Mikhail Kapranov and Vadim Schechtman._Perverse schobers_. 2014. arXiv:`1411.2772`.|
|[Kuw20]|Tatsuki Kuwagaki. “The nonequivariant coherent-constructible correspondence for toric|
||stacks.” _Duke Mathematical Journal_ (2020).|
|[Man97]|Sandro Manfredini. “Some subgroups of Artin’s braid group.” _Topology and its Appli-_|
||_cations_ 78.1 (1997). Braid Groups and Related Topics, pp. 123–142.|
|[PPS25]|James Pascalef, Emanuele Pavia, and Nicol`o Sibilla. _Higher local systems and the_|
||_categorifed monodromy equivalence_. 2025. arXiv: `2501.10241`.|
|[Seg11]|Ed Segal. “Equivalences between GIT quotients of Landau-Ginzburg B-models.”_Com-_|
||_munications in mathematical physics_ 304 (2011), pp. 411–432.|
|[Sei08]|Paul Seidel. “_A∞_-subalgebras and natural transformations.”_Homology, Homotopy and_|
||_Applications_ 10.2 (2008), pp. 83–114.|
|[She22]|Vivek Shende. “Toric mirror symmetry revisited.” _Comptes Rendus. Math´ematique_|
||360.G7 (2022), pp. 751–759.|
|[ˇSpe23]|ˇSpela ˇSpenko. “HMS symmetries and hypergeometric systems.” _European Congress of_|
||_Mathematics_. EMS Press, Berlin, 2023, pp. 489–510.|
|[ST01]|Paul Seidel and Richard Thomas. “Braid group actions on derived categories of coher-|
||ent sheaves.” _Duke Math. J._ 108.1 (2001), pp. 37–108. issn: 0012-7094,1547-7398.|
|[Syl19]|Zachary Sylvan. _Orlov and Viterbo functors in partially wrapped Fukaya categories_.|
||2019. arXiv: `1908.02317`.|



62 

- [Tho00] Jesper Funch Thomsen. “Frobenius direct images of line bundles on toric varieties.” _J. Algebra_ 226.2 (2000), pp. 865–874. 

- [Tho06] Richard P Thomas. “Stability conditions and the braid group.” _Communications in Analysis and Geometry_ 14.1 (2006), pp. 135–161. 

- [TWZ19] David Treumann, Harold Williams, and Eric Zaslow. “Kasteleyn operators from mirror symmetry.” _Selecta Mathematica_ 25.4 (2019), p. 60. 

- [SVdB24][ˇ] ˇSpela ˇSpenko and Michel Van den Bergh. _HMS symmetries of toric boundary divisors_ . 2024. arXiv: `2403.15660` . 

- [War21] Abigail Ward. _Homological mirror symmetry for elliptic Hopf surfaces_ . 2021. arXiv: `2101.11546` . 

- [Woo10] Chris Woodward. “Moment maps and geometric invariant theory.” _Les cours du CIRM_ 1.1 (2010), pp. 55–98. 

- [Zho20] Peng Zhou. “Lagrangian Skeleta of Hypersurfaces in (C _[∗]_ ) _[n]_ .” _Selecta Mathematica_ 26.26 (2020). 

- [Zho25] Peng Zhou. “Variation of GIT and variation of Lagrangian skeletons I: flip and flop.” _Tunisian Journal of Mathematics_ 7.1 (2025), pp. 1–52. 

M. Barbieri, Department of Mathematics, University College London 

_E-mail address_ : `michela.barbieri.21@ucl.ac.uk` 

A. Hanlon, Department of Mathematics, University of Oregon 

_E-mail address_ : `ahanlon@uoregon.edu` 

J. Hicks, School of Mathematics and Statistics, University of St Andrews 

_E-mail address_ : `jeff.hicks@st-andrews.ac.uk` 

63 

