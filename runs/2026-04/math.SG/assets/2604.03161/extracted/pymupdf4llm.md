## **TROPICAL DISK POTENTIALS FOR ALMOST TORIC MANIFOLDS** 

## S. VENUGOPALAN AND C. WOODWARD 

Abstract. Using our previous work [46], we give a tropical formula for disk potentials for Lagrangian tori in almost toric four-manifolds, that is, fibrations by Lagrangian tori with only toric and focus-focus singularities, generalizing results of Mikhalkin [34] for holomorphic spheres in the projective plane. As examples, we directly compute potentials for Lagrangian tori in del Pezzo surfaces equipped with monotone symplectic forms. These formulas were established in the monotone case by different methods in Pascaleff-Tonkonog [39], and investigated from the point of view of the Gross-Siebert program in Carl-Pumperla-Siebert [5], Bardwell-Evans–Cheung–Hong–Lin [2] and also Lau-Lee-Lin [24]. 

||Contents||
|---|---|---|
|1.|Introduction|2|
|2.|Almost toric manifolds|14|
|2.1.|Focus-focus singularities|14|
|2.2.|Modifcations of almost toric structures|19|
|3.|Tropical limit theorems|22|
|3.1.|Disk potentials|22|
|3.2.|Broken Maps|24|
|3.3.|Tropical limit theorems for moduli spaces|27|
|3.4.|Relative maps|29|
|3.5.|Intersecting polyhedral decompositions|33|
|4.|Curves in the elementary pieces|35|
|4.1.|Holomorphic spheres in toric varieties|36|
|4.2.|Disks in toric varieties|38|
|4.3.|Spheres meeting the focus-focus singularities|39|
|4.4.|Computing multiplicities via desingularization|43|
|4.5.|Counting by bunching|45|
|5.|Tropical graphs of rigid disks|48|
|5.1.|Standard decompositions|48|
|5.2.|Collisions at generic points|55|
|5.3.|Collisions in the interior|57|
|5.4.|Tropical graphs spiral outward|60|
|6.|Newton polygons and mutations|61|
|6.1.|The dual afne manifold|61|
|6.2.|Mutations and wall-crossing|66|



1 

2 

## S. VENUGOPALAN AND C. WOODWARD 

|6.3.|The Newton polygon of the potential|70|
|---|---|---|
|6.4.|Potentials of smoothings of toric singularities|71|
|6.5.|The classifcation of potentials|75|
|7.|Explicit computations for del Pezzo surfaces|77|
|7.1.|Potentials of toric del Pezzo surfaces|77|
|7.2.|Potentials of non-toric del Pezzo surfaces|80|
|Appendix A.<br>Rigid spheres||82|
|Appendix B.<br>Code for computing potentials and Jacobian rings||84|
|References||88|



## 1. Introduction 

Mikhalkin [34] has given a tropical formula for the counts of holomorphic spheres in the projective plane, which was generalized to toric varieties of arbitrary dimension by Nishinou-Siebert [35]. In this paper, we generalize Mikhalkin’s formula to the case of holomorphic spheres or disks with boundary in moment fibers of almost toric symplectic four-manifolds. The formula is a special case of our previous work on the behavior of holomorphic curves under degeneration [46]; the results extend, partially, to almost toric manifolds of dimension greater than four. The formula overlaps with the formulas for the potentials established in Pascaleff-Tonkonog [39], who used the behavior of the potentials under mutation. It also overlaps with work of Bardwell-Evans–Cheung–Hong–Lin [2], who give a tropical method for computing the potentials of toric moment fibers for del Pezzo surfaces that have semi-Fano degeneration; see also Lau-Lee-Lin [24] for connection to the Strominger-Yau-Zaslow point of view for mirror symmetry. Gromov-Witten invariants of blow-ups of projective spaces are computed tropically in Parker [38], from a somewhat different viewpoint. The techniques here extend to a formula for counting disks with boundary in Lagrangians such as those corresponding to simply laced root systems on del Pezzo surfaces, as we will explain in a sequel [52] where we extend the results to tropical Lagrangians. 

Recall that an almost toric structure on a symplectic manifold as studied in Leung and Symington [26] is a Lagrangian fibration with _elliptic singularities_ occurring in the moment map for a torus action on a symplectic four-manifold or _focus-focus singularities_ allowed, in which the torus fiber is allowed to develop a node. The base of the fibration, equipped with the location of the singular fibers, is called an _almost toric diagram_ . An example of an almost toric diagram for the five-times blow-up of the projective plane (the del Pezzo surface of degree four) is shown in Figure 1, with the images of the focus-focus singularities marked with _×_ ’s. Vianna [49] has given explicit constructions of almost toric manifolds on del Pezzo surfaces. 

Holomorphic disks in such symplectic four-manifolds have tropical descriptions in terms of graphs in the base. Bardwell-Evans–Cheung–Hong–Lin [2] and Gr¨afnitz [18], [17] prove tropical correspondences in the case of toric moment fibers for del Pezzo surfaces that have a semi-Fano degeneration. The existence of such a formula was suggested in Vianna’s thesis [49], and in previous work by Carl-Pumperla-Siebert 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

3 

**==> picture [123 x 122] intentionally omitted <==**

**==> picture [122 x 123] intentionally omitted <==**

Figure 1. An almost toric diagram for the del Pezzo of degree four and the twelve tropical disks contributing to the potential of the monotone torus 

[5], The tropical computations reproduce the maximally mutable Laurent polynomials found in mirror symmetry; see, for example, Akhtar et al. [1] on the basis of _maximal mutability_ . The results in Bardwell-Evans et al. [2] take a detour through algebraic geometry. In this paper, we apply the degeneration (that is, tropical) techniques we developed in Venugopalan-Woodward [46] to directly compute various disk counts in almost toric manifolds. In principle, these techniques apply to symplectic manifolds of any dimension, but potentials for four-dimensional almost-toric manifolds have a particularly nice formula. As examples we give tropical computations of the disk potentials of Lagrangian torus fibers of monotone del Pezzo surfaces, which were first computed in Pascaleff-Tonkonog [39], and from a tropical point of view in Bardwell-Evans–Cheung–Hong–Lin [2] for del Pezzo surfaces of degree at least three. In particular, for the monotone del Pezzo surfaces we give a combinatorial proof that the potential of the Lagrangian torus is mutable, and so equivalent to one of the mutable Laurent polynomials described in Akhtar et al. [1] (following Pascaleff-Tonkonog [39].) The right-hand part of Figure 1 shows the tropical disks in the five-times blow-up. The monotone Lagrangian torus with its trivial local system gives a summand in the Fukaya category with _w_ = 12 (and so 12 is an eigenvalue of quantum multiplication by the first Chern class; see [48, Theorem 1.7] and note that the leading order term in the open-closed map for the point class is non-zero). 

We describe in more detail the disk counts that we wish to compute. Let _X_ be a compact symplectic manifold and _L ⊂ X_ be a compact Lagrangian equipped with a relative spin structure and a local system. Let ΛQ _,≥_ 0 = Q[[ _q_[R] ]] be the Novikov field in a formal variable _q_ with non-negative real exponents and rational coefficients, and Λ = ΛQ _⊗_ Q C the version with complex coefficients. The space of Morse chains _CF_ ( _L, L_ ) on _L_ with coefficients in Λ has a natural _A∞_ structure introduced by Fukaya, giving rise to a space of projective Maurer-Cartan solutions _MC_ ( _X, L_ ) with a _disk potential_ 

**==> picture [259 x 13] intentionally omitted <==**

4 

## S. VENUGOPALAN AND C. WOODWARD 

counting holomorphic disks with boundary in _L_ , weighted by powers of the formal variable with areas as exponents. The same statement holds over the rationals ΛQ, but the complex version allows for more critical points and so more non-trivial brane structures. Up to equivalence, the potential _WX,L_ is invariant of all choices. We will be mainly interested in the monotone case, in which one typically computes the simpler version consisting of a count of disks passing through a generic point on the Lagrangian, weighted by holonomies of a given local system. The results of this paper extend more generally to the non-monotone case, with the caveat that in this one is computing a function on the Maurer-Cartan space up to isomorphism, rather than a well-defined potential that is a Laurent polynomial independent of all choices. In the first purpose of the paper we use degeneration techniques to count such disks. Let _T_ be a two-dimensional torus with Lie algebra t, integral lattice tZ _⊂_ t, and dual t _[∨]_ . Let _X_ be a compact almost toric four-manifold with an almost toric moment map Φ : _X → B_ , where _B_ is an affine integral manifold modelled on t _[∨]_ , and _L_ = Φ _[−]_[1] ( _λ_ ) a Lagrangian torus fiber. Denote by 

**==> picture [43 x 11] intentionally omitted <==**

the set of focus-focus values, so that each fiber Φ _[−]_[1] ( _b_ ) _, b ∈ B_[foc] is a nodal torus (with one or more nodes.)[1] Let 

**==> picture [67 x 12] intentionally omitted <==**

be a polyhedral decomposition of _B_ . Quotienting by the circle actions normal to the facets gives a degeneration denoted _X_ . We will choose particularly simple decompositions in order to compute disk potentials: 

**Definition 1.1.** The decomposition _P_ is _elementary_ if one of the possibilities holds exclusively: Each _P ∈P_ either 

- (a) contains a (possibly empty) collection of focus-focus values _b ∈ B_[foc] all of which lie on the same branch cut in the base diagram, and in which case _P_ is equivalent to the polytope shown in Figure 16, up to the action of _GL_ (2 _,_ Z); 

- (b) contains the projection _λ_ = Φ( _L_ ) of the Lagrangian _L_ ; 

- (c) intersects the boundary of Φ( _X_ ) and contains at most one vertex of Φ( _X_ ). 

The broken manifold is equipped with the datum of a dual complex and a cutting datum in the sense of Definition T-3.24, meaning a collection of polytopes _P[∨]_ for each _P ∈P_ with inclusions _P[∨] → Q[∨]_ for each face _Q ⊂ P_ . Given a cutting datum, the dual complex is the union 

(2) _B[∨]_ = _∪P ∈P P[∨] / ∼,_ 

where _∼_ is the identification of faces. See [46, Section 3.3] for detailed definitions. For a polyhedral decomposition of an almost toric manifold, the interior of the dual complex has the structure of a singular affine manifold modeled on t. The singular points in the affine manifold _B[∨]_ correspond to the polytopes _P ∈P_[foc] containing 

- 1More generally, one could allow affine manifolds with singularities in the sense of [47]. 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

5 

the focus-focus values _b ∈ B_[foc] . We call the complement of these points 

**==> picture [257 x 26] intentionally omitted <==**

the _smooth locus_ in _B[∨]_ . In the neck stretching limit the holomorphic disks with boundary in _L_ degenerate to broken maps associated to some set _T_ of tropical graphs Γ in _B[∨]_ . The notion of _tropical graphs_ in _B[∨]_ is well-defined; each edge of a tropical graph Γ in _B[∨]_ is an affine linear segment, and the edges are joined at vertices where a balancing condition holds as in Mikhalkin [34]. (See Section 3.2 for details.) The balancing condition holds at all vertices _v_ except if _v_ is a disk vertex, or if _P_ ( _v_ ) intersects the boundary _∂_ Φ( _X_ ) or if _P_ ( _v_ ) contains focus-focus singular values _b ∈ B_[foc] . In these three cases, we require vertices to be univalent, this condition is laid down in the following definition. 

**Definition 1.2.** A tropical graph Γ in _B[∨]_ has _collisions in the interior_ if for any vertex of Γ for which the polytope _P_ ( _v_ ) intersects _∂_ Φ( _X_ ), 

- (a) the valence of _v_ is _|v|_ = 1, and 

- (b) _P_ ( _v_ ) intersects exactly a single facet _Q_ of Φ( _X_ ) and the direction _T_ ( _e_ ) _∈_ t of the adjacent edge _e_ is the primitive normal to _Q_ . 

A tropical graph Γ in _B[∨]_ has collisions only at _generic points_ if for each vertex _v_ such the polytope _P_ ( _v_ ) contains a focus-focus value _b ∈ B_[foc] , _v_ is an open vertex and the valence of _v_ is _|v|_ = 1; otherwise, the valence is most _|v|_ = 3. 

For a large class of manifolds and Lagrangians, including in the monotone case, there exist subdivisions _P_ for which all graphs Γ have collisions at interior points, see Proposition 5.1 below. 

The direction of the edge emanating from a disk vertex is called the _initial direction_ of the tropical graph. For univalent vertices _v_ mapping to polytopes containing the focus-focus values, the directions _T_ ( _e_ ) of the adjacent edges _e ∈_ Edge(Γ) are constrained to lie in the shear directions as explained in Section 2. 

We assign orientations to edges of the tropical graphs whose collisions are only at generic interior points. By Lemma 3.19, there is a unique assignment of edge orientations with the following property: Given a rigid map _u_ with tropical graph Γ, cutting an edge _e_ = ( _v_ + _, v−_ ) pointing towards _v−_ produces maps _uv_ +, _uv−_ that are rigid if the constraint on the map component _uv−_ corresponding to the vertex on which _e_ is incident. 

We add some additional data to the tropical graph: The degeneration associated to the polyhedron _P_ is a union of _cut spaces XP , P ∈P_ . We prove later that if a map _uv_ lies in a piece _XP_ ( _v_ ) containing focus-focus singularities, _uv_ meets exactly one focus-focus singularity, which we denote by _xv ∈ XP_ ( _v_ ). To the tropical graph Γ underlying _u_ , we add the data of _xv_ to every such univalent vertex _v_ . The additional data plays a role in the formula (4) in the following theorem: a graph isomorphism _ϕ_ on Γ is in Aut(Γ) exactly if _P_ ( _v_ ) = _P_ ( _ϕ_ ( _v_ )) for all vertices _v_ , _ϕ_ maps Vert (Γ) to itself, and for univalent vertices _v_ as above, _xv_ = _xϕ_ ( _v_ ). 

S. VENUGOPALAN AND C. WOODWARD 

6 

**Theorem 1.3.** _Let X be a compact almost toric manifold of dimension four, L a Lagrangian torus fiber of_ Φ _and P an elementary polyhedral decomposition, for which any disk contributing to the potential WX ,L has a tropical graph with all collisions in generic interior points. Then the count of rigid Maslov index two disks with boundary in L is a count of tropical graphs_ 

**==> picture [286 x 31] intentionally omitted <==**

_where the multiplicities m_ ( _v_ ) _are as in Definition 1.4 below, and_ Aut(Γ) _denotes the group of automorphisms of_ Γ _. The same holds for counts of holomorphic spheres in X with constraints._ 

The multiplicities in the Theorem combine Mikhalkin’s multiplicity formula [34], the Bryan-Pandharipande multiple cover formula [4], and the Cho-Oh [9] counts of disks in toric varieties meeting the interior. The combination of these formulas appears in Gr¨afnitz [17] for spheres, Lin in the case of disks in K3 surfaces, appears in Lin [29, Definition 3.3]; also compare with Theorem 1.1 in Cheung-Mandel [8]. In each picture, the graph (drawn in blue) represents Γ, the point (drawn in cyan) represents the Lagrangian image, if present, the purple point a focus-focus value, a solid segment a part of the image of the divisor at infinity _D_ of _X_ , a dotted line (drawn in black) a divisor _XQ_ created by the multiple cut, and a dotted line (drawn in purple) a branch cut. 

**Definition 1.4.** The multiplicities _m_ ( _v_ ) of vertices _v ∈_ Vert(Γ) of valence at most three are defined as follows: 

- (a) (Holomorphic cylinders) The multiplicity 

**==> picture [45 x 12] intentionally omitted <==**

for bivalent vertices _v ∈_ Vert (Γ) such that the polytope _P_ ( _v_ ) has no focusfocus values _b ∈ B_[foc] , does not meet the boundary of the moment polytope Φ( _X_ ) and _v_ has adjacent edges _e_ 1 _, e_ 2 _∈_ Edge (Γ) in the same directions _T_ ( _e_ 1) = _T_ ( _e_ 2). 

**==> picture [84 x 102] intentionally omitted <==**

- (b) (Holomorphic pairs of pants) The Mikhalkin multiplicity 

**==> picture [125 x 12] intentionally omitted <==**

for trivalent vertices _v ∈_ Vert (Γ) such that the polytope _P_ ( _v_ ) contains no focus-focus values _b ∈ B_[foc] , and edge directions 

**==> picture [117 x 13] intentionally omitted <==**

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

7 

(exactly two of which are incoming) satisfying the balancing condition 

_T_ ( _e_ 1) + _T_ ( _e_ 2) + _T_ ( _e_ 3) = 0; 

otherwise, _m_ ( _v_ ) = 0. 

**==> picture [126 x 104] intentionally omitted <==**

**----- Start of picture text -----**<br>
e 1 e 2<br>e 3<br>**----- End of picture text -----**<br>


- (c) (Collisions of cylinders with boundary) The multiplicity 

_m_ ( _v_ ) = 1 

if _v ∈_ Vert (Γ) is a univalent vertex such that _P_ ( _v_ ) contains no focus-focus values _b ∈ B_[foc] and intersects a facet _Q_ of the toric boundary ∆= Φ( _X_ ) with direction _µ ∈_ R[2] the primitive generator of the normal direction to _TQ_ . 

**==> picture [115 x 85] intentionally omitted <==**

- (d) (Multiple covers near focus-focus singularities) Denote by _ℓ_ ( _µ_ ) _∈_ Z _>_ 0 the lattice length of the direction _µ_ = _T_ ( _e_ ) of the adjacent edge _e ∈_ Edge(Γ). The Bryan-Pandharipande multiplicity is 

_m_ ( _v_ ) = ( _−_ 1) _[ℓ]_[(] _[µ]_[)] _[−]_[1] _/ℓ_ ( _µ_ )[2] 

for the univalent closed vertices _v ∈_ Vert (Γ) such that the polytope _P_ ( _v_ ) contains a single focus-focus value _b ∈ B_[foc] . 

**==> picture [102 x 124] intentionally omitted <==**

- (e) (Disks with boundary in the Lagrangian) The Cho-Oh multiplicity 

_m_ ( _v_ ) = 1 

S. VENUGOPALAN AND C. WOODWARD 

8 

if _v ∈_ Vert(Γ) is a univalent vertex such that the polytope _P_ ( _v_ ) contains the Lagrangian _λ_ = Φ( _L_ ) and the adjacent edge _e ∈_ Edge(Γ) has direction _T_ ( _e_ ) that is a primitive lattice vector. 

_Example_ 1.5 _._ (Potential for the degree four del Pezzo) Consider the almost toric diagram for the del Pezzo surface of degree four shown in Figure 1. Twelve tropical graphs representing Maslov index two disks are shown. The first four Γ1 _, . . . ,_ Γ4 have two vertices, each univalent, while the last eight have two three univalent vertices and one trivalent vertex. Each of the multiplicities _m_ ( _v_ ) of the vertices is equal to one, by the Definition above. The initial directions of the tropical graphs are ( _±_ 1 _, ±_ 1), each with multiplicity one, and ( _±_ 1 _,_ 0) _,_ (0 _, ±_ 1), each with multiplicity two, since there are two choices of focus-focus singularity to interact with in each of these directions. It follows that 

_WL_ ( _y_ 1 _, y_ 2) = (1 + _y_ 1)[2] (1 + _y_ 2)[2] _/_ ( _y_ 1 _y_ 2) _−_ 4 _._ 

**==> picture [69 x 191] intentionally omitted <==**

**----- Start of picture text -----**<br>
(1 ,  1)<br>( − 1 ,  0)<br>(3 ,  1)<br>(2 ,  0)<br>**----- End of picture text -----**<br>


Figure 2. An almost toric diagram for the Chekanov torus and the four tropical disks contributing to the potential 

_Example_ 1.6 _._ (Potential for the Chekanov torus) An almost toric diagram for P[2] is shown in Figure 2, which has a single focus-focus singularity and three facets with normal vectors (1 _,_ 0) _,_ ( _−_ 1 _, −_ 1), and ( _−_ 3 _,_ 1). The diagram is obtained by mutation from the standard toric diagram of P[2] , as shown in Figure 37. The corresponding monotone torus fiber is known as the Chekanov torus, as studied in Vianna [50]. There are three graphs Γ1 _,_ Γ2 _,_ Γ3 with two bivalent vertices each, and both multiplicities are one in this case. The final graph Γ4 has initial direction (2 _,_ 0), and has a trivalent vertex with incoming edges (2 _,_ 0) and (1 _,_ 1) and so Mikhalkin multiplicity two. The contribution of this graph to the potential is therefore 2 _y_ 1[2][,][with][a][total] potential of 

**==> picture [192 x 13] intentionally omitted <==**

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

9 

There are three critical values of _WL_ , corresponding to three local systems on _L_ which taken together split-generate the Fukaya category of the complex projective plane P[2] . 

_Example_ 1.7 _._ (The number of exceptional curves in the degree one del Pezzo is the same as the number of roots of the _E_ 8 root system) The same formula holds for rigid holomorphic spheres in del Pezzos, as explained in an Appendix A, simply by disallowing open vertices in item (e), in which case the formula is similar to one in Gr¨afnitz [17, Proposition 4.48]. For example, it is well-known that a del Pezzo of degree one contains 240 lines, that is, rigid embedded holomorphic spheres, which is the same as the number of roots of the _E_ 8 root system connected to this del Pezzo by Manin [31]; see [42], [45]. One can see these 240 spheres as follows: Figure 3 shows 252 cartoon diagrams (approximate moment images) for stable genus zero maps to the del Pezzo of degree one. Of these, exactly 12 have self-intersections: 

- (a) the 9 curves of the 81 curves of the last type that intersect the same focusfocus singularity twice, and 

- (b) the 3 curves corresponding to tropical graphs with the trivalent vertex with determinant 3; see the self-intersection computation in Mikhalkin [34]. 

Thus, there are 240 = 252 _−_ 12 embedded such curves. Testa [45, Lemma 2.3] explains the difference between the number in terms of the 12 curves in the anticanonical linear system. (These are half of the 24 nodal fibers in the standard realization of a _K_ 3 surface.) 

It remains to define multiplicities for vertices with valence four or more. To define these multiplicities, we require a perturbation of the tropical graph which we describe next. 

**Definition 1.8.** Let _v_ be a spherical vertex in a tropical graph Γ, and let Γ _v_ be the subgraph consisting of _v_ and its incident edges. Suppose _e_ 1 _, . . . , ek ∈_ Edge(Γ) are incoming edges at _v_ where _k ≥_ 3, and _e_ 0 is the outgoing edge. A _perturbation_ Γ[pert] _v_ of Γ _v_ is a graph in _B[∨]_ , each of whose incoming edges _e[′] i_[,][1] _[≤][i][≤][k]_[is][the][edge] _[e][i]_ translated by an amount _ℓi_ , where 

(5) _ℓ_ 1 _≫ ℓ_ 2 _≫· · · ≫ ℓk,_ 

and the vector ( _ℓ_ 1 _, . . . ℓk_ ) is generic so that all sphere vertices in Γ[pert] _v_ are trivalent, and a disk vertex, if present, is monovalent. 

Note that for sphere vertices we may consider perturbations where two of the parameters _ℓk−_ 1, _ℓk_ may be taken to be zero, assuming that the directions of the edges _ek−_ 1, _ek_ are not parallel. Indeed, two non-parallel edges in general position will intersect, and the effect of the perturbation is to rule out more than two edges intersecting at a point. 

**Definition 1.9.** (Multiplicity for higher valent vertices) Let Γ be a tropical graph as in Theorem 1.3, and let _v_ be a vertex of Γ with valence more than three. The 

10 

**==> picture [169 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
S. VENUGOPALAN AND C. WOODWARD<br>**----- End of picture text -----**<br>


**==> picture [92 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
84 + 84 +3 + 81 = 252<br>**----- End of picture text -----**<br>


Figure 3. Cartoon diagrams for the 252 degree one curves in Bl[8] P[2] 

**==> picture [192 x 73] intentionally omitted <==**

**----- Start of picture text -----**<br>
e 4<br>e 5<br>e 1 ℓ 1<br>ee 32 v ℓ 2 ℓ 3 e [′] 3 e [′] 1<br>Γ v e [′] 2 Γ [pert] v<br>**----- End of picture text -----**<br>


Figure 4. Perturbing incoming edges of _v_ with parameters _ℓ_ 1 _> ℓ_ 2 _> ℓ_ 3. The pairs _e_ 1, _e_ 5 and _e_ 2, _e_ 3 are coincident in Γ. 

multiplicity of _v_ is defined by is 

**==> picture [173 x 41] intentionally omitted <==**

where the sum ranges over all perturbed graphs of Γ _v_ that respect a fixed ordering (5) of incoming edges. (We will see later that different orderings (5) of the incoming edges produce the same multiplicity. ) 

Both the dual complex and tropical graphs can be viewed in a simplified way, for judiciously chosen polyhedral decompositions, which aids the counting of tropical graphs in Theorem 1.3, especially in the monotone case. These simplified tropical 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

11 

**==> picture [204 x 84] intentionally omitted <==**

**----- Start of picture text -----**<br>
ℓ 1 ℓ 1<br>e [′] 1<br>ℓ 3 ℓ 3 e [′] 1<br>ℓ 2 e [′] 3 ℓ 2 e [′] 3<br>e [′] 2 e [′] 2<br>**----- End of picture text -----**<br>


Figure 5. Perturbing Γ in Figure 4 with parameters _ℓ_ 2 _> ℓ_ 3 _> ℓ_ 1 produces two perturbed graphs. 

graphs called _A-tropical graphs_ lie in a dual affine manifold: Given an almost toric four manifold ( _X,_ Φ), the associated _dual affine manifold A_ ( _X_ ) is a singular affine integral manifold modelled over t that is complete and without boundary equipped with 

(a) a singular point _b[∨] ∈A_ ( _X_ ) corresponding to each focus-focus values _b ∈ B_[foc] ; the monodromy of the tangent space _T_ Z _A_ ( _X_ ) around the singular point _b_ is a shear matrix _Ab ∈ GL_ (2 _,_ Z) whose primitive eigendirections are 

(6) _µ_[+] _b[, µ][−] b[∈][T][x] b[A]_[(] _[X]_[)] _[,]_ with singular points _b_ 1, _b_ 2 _∈ B_[foc] lying on the same branch cut allowed to coincide; 

(b) and a distinguished (smooth point) _P_ 0 _[∨]_ = _{λ}_ corresponding to the Lagrangian fiber. 

The dual affine manifold arises naturally from the dual complexes of our polyhedral decompositions as explained in (42). There is a bounded open set _S ⊂A_ ( _X_ ) such that the complement 

**==> picture [99 x 12] intentionally omitted <==**

is an affine annulus with no singular points. We assume in this introduction that the divisor at infinity _D ⊂ X_ is irreducible; in this case there is a distinguished vector field 

**==> picture [111 x 12] intentionally omitted <==**

called the _primitive outward direction_ that is flat with respect to the affine structure, and is shown in Figure 22. Going one around the annulus produces a monodromy 

**==> picture [143 x 12] intentionally omitted <==**

of tangent spaces _T A_ ( _X_ ) that is equal to the composition of shears at all the focusfocus values. The outward vector _µ_ out( _x_ ) is fixed by _h_ . The dual affine manifold _A_ ( _X_ ) can be read off from the moment polytope Φ( _X_ ) up to equivalence as described in Remark 6.3. For examples of dual affine manifolds, see Figures 6 and 23. 

Tropical graphs in the dual complex _B[∨]_ give rise to _A-tropical graphs_ in the dual affine manifold _A_ ( _X_ ) by forgetting bivalent vertices, and the data of the polytopes _P_ ( _v_ ) corresponding to vertices _v_ . The graphs are defined as follows: 

S. VENUGOPALAN AND C. WOODWARD 

12 

**Definition 1.10.** ( _A_ -tropical graph) Let _A_ ( _X_ ) be an affine manifold corresponding to a manifold _X_ (as in (42)). Let _λ ∈A_ ( _X_ ) correspond to the Lagrangian torus _L ⊂ X_ . An _A-tropical graph T_ for _X_ consists of a graph 

**==> picture [111 x 12] intentionally omitted <==**

whose vertices are partitioned into disk and sphere vertices 

Vert(Γ) = Vert (Γ) _∪_ Vert (Γ) _,_ 

## a _tropical embedding_ 

**==> picture [70 x 12] intentionally omitted <==**

into the affine manifold _A_ ( _X_ ) consisting of 

- (a) a tropical position _T_ ( _v_ ) _∈A_ ( _X_ ) for every vertex _v_ such that _T_ ( _v_ ) = _λ_ for all disk vertices _v ∈_ Vert (Γ), 

- (b) and for any edge _e_ = ( _v_ + _, v−_ ), a map from _e_ to an affine linear segment in _B[∨]_ of rational direction _T_ ( _e_ ) connecting _T_ ( _v_ +), _T_ ( _v−_ ) satisfying a _balancing condition_ , namely that the sum of directions of edges at any vertex _v_ with valence _|v| ≥_ 3 is zero: 

**==> picture [64 x 24] intentionally omitted <==**

where _T_ ( _e_ ) is viewed as an element in _TT_ ( _v_ ) _,_ Z _A_ ( _X_ ). 2 In the case that an edge _e_ is incident on a single vertex _v_ , _T_ maps _e_ to a semi-infinite affine linear segment originating at _T_ ( _v_ ). 

**Definition 1.11.** ( _A_ -tropical tree, index two trees) An _A_ -tropical graph (Γ _, T_ ) is an _A-tropical tree_ if Γ is a tree, and there is a single disk vertex. An _A_ -tropical tree (Γ _, T_ ) in _A_ ( _X_ ) has _index two_ if the edges can be assigned orientations such that each vertex _v ∈_ Vert( _T_ ) has exactly one outgoing edge _e ∋ v_ , and one of the vertices _v ∈_ Vert( _T_ ) has a semi-infinite outgoing edge _e_ out (that is, an edge incident on a single vertex), and 

- (a) (Tree) a tree _T_ with directed edges Edge( _T_ ) so that 

- (b) (Leaves) Each univalent vertex _v_ maps either to 

   - (i) the point _λ ∈A_ ( _X_ ) corresponding to the Lagrangian torus, in which case the adjacent edge _e_ to _v_ is called the _input leaf_ 

- (ii) to a singular point _b[∨] , b ∈ B_[foc] , and in this case the direction of the edge incident on _v_ is required to be a Z+-multiple of either _µ_[+] _b_[or] _[µ][−] b_[.] 

- (c) (Final direction) The direction of the outgoing semi-infinite outgoing edge _e_ out is _µ_ out. 

We later show that _A_ -tropical trees of index two correspond to broken disks of Maslov index two, justifying the terminology. 

Theorem 1.3 gives a method to compute the disk potentials of del Pezzo surfaces as conjectured by Akhtar et al. [1]. Examples of admissible graphs are given in 

> 2In general, in an _A_ -tropical graph, the direction _T_ ( _e_ ) of an edge _e_ is the primitive slope of the segment _e_ multiplied by a positive integer called the multiplicity. When an affine chart is given, _T_ ( _e_ ) is an element in t _Z_ . 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

13 

**==> picture [278 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
shear<br>Φ( X )<br>shear A ( X ) shear<br>shear<br>**----- End of picture text -----**<br>


Figure 6. Left: an almost toric diagram for Bl[5] P[2] . Right: The dual affine manifold, and the blue dotted lines indicate the direction _µb_ in which a tropical curve emanates from a singular point _b_ . 

Section 5, and shown in Figure 1 for the del Pezzo of degree four. Theorem 1.12 is a simpler version of Theorem 1.3 for judiciously chosen polyhedral decompositions. For such decompositions all collisions occur in the annulus _A_ ann( _X_ ). 

The techniques of this paper can also be used, in good cases, to compute disk potentials of almost toric manifolds in dimensions higher than four in which case the focus-focus values form subsets of positive dimension, but in this paper we focus on the case of almost toric structures on del Pezzo surfaces. Although the techniques here are not restricted to the monotone case, it is difficult to formulate clean theorems in the non-monotone cases as the disk potential in the monotone case is only defined as a function on the space of projective Maurer-Cartan solutions up to equivalence. But the space of such solutions is unknown, even for toric varieties. 

**Theorem 1.12.** _Suppose X is a symplectic monotone four-manifold equipped with an almost toric structure with base B and let L be a monotone torus fiber of the projection_ Φ : _X → B. The formula in Theorem 1.3 for the disk potential may be taken to be a sum over A-tropical graphs in the affine manifold A_ ( _X_ ) _._ 

We give some examples of the computations in Section 6. Theorem 1.12 also implies fairly easily that the Newton polygon of the potential of an almost toric manifold is the dual of the moment polytope. 

The polynomials described in [1] were previously determined based on the _maximal mutability_ property; we also show that Theorem 1.3 implies the mutation formula for monotone tori in del Pezzo surfaces, originally proved in Pascaleff-Tonkonog [39]: 

**Theorem 1.13.** _Let X be a compact monotone symplectic four-manifold with almost toric diagrams_ ∆ _,_ ∆ _[′] related by a mutation, that is, nodal slide and transferring the cut as in Definition 2.13, and let L, L[′] ⊂ X denote the corresponding monotone torus fibers. Then their potentials WL, WL′ are related by the mutation formula, as in Definition 6.10 below._ 

Combining Theorems 1.3 and 1.13 we give a combinatorial proof that the potentials are as claimed in the monotone case: 

14 

## S. VENUGOPALAN AND C. WOODWARD 

|del Pezzo surface|Manin root system|disk potential|
|---|---|---|
|P2<br>P1 _×_P1<br>Bl1 P2<br>Bl2 P2<br>Bl3 P2<br>Bl4 P2<br>Bl5 P2<br>Bl6 P2<br>Bl7 P2<br>Bl8 P2|_A_1<br>_A_1<br>_A_1_⊕A_2<br>_A_4<br>_D_5<br>_E_6<br>_E_7<br>_E_8|_y_1+_y_2+ 1_/y_1_y_2<br>_y_1+ 1_/y_1+_y_2+ 1_/y_2<br>_y_1+_y_2+ 1_/_(_y_1_y_2) +_y_1_y_2<br>(1 +_y_1+_y_2)(1 + 1_/_(_y_1_y_2))_−_1<br>(1 +_y_1)(1 +_y_2)(1 + 1_/_(_y_1_y_2))_−_2<br>(1 +_y_1+_y_2)(1 + 1_/y_1)(1 + 1_/y_2)_−_3<br>(1 +_y_1)2(1 +_y_2)2_/_(_y_1_y_2)_−_4<br>(1 +_y_1+_y_2)3_/_(_y_1_y_2)_−_6<br>(1 +_y_1+_y_2)4_/_(_y_1_y_2)_−_12<br>(1 +_y_1+_y_2)6_/_(_y_1_y_2<br>2)_−_60|



Table 1. Potentials of del Pezzo surfaces 

**Corollary 1.14.** _(Pascaleff-Tonkonog_ [40] _.) The potential WL of the monotone Lagrangian torus fiber L ⊂ X of a del Pezzo surface X is given by a tropical disk count in A_ ( _X_ ) _. For the almost toric structures described by Vianna_ [49] _, the potential is equal to the formulas in Akhtar et al_ [1] _reproduced in Table 1 below._ 

The relationship of these potentials with the rational elliptic surfaces considered to be mirror to the del Pezzos is studied in Lutz [30]. Each critical value of the potential is an eigenvalue of quantum multiplication by the first Chern class, as explained, for example, in Sheridan [43]. Note that depending on the almost toric structure, not all eigenvalues can appear as critical values, hence the _⊆_ in the column heading. 

In a sequel to this work, we identify split generators for the Fukaya category of monotone del Pezzos using the almost toric diagrams and tropical Lagrangians. 

## 2. Almost toric manifolds 

2.1. **Focus-focus singularities.** An _almost toric structure_ on a symplectic fourmanifold is a pair of functions that act like a moment map for a completely integrable Hamiltonian two-torus action except for a finite number of _focus-focus singularities_ where the torus fibers acquire a node. By the Arnold-Liouville theorem, that the image of such a moment map has an affine integral structure, which we define following Symington [44] and Gross [20]. We use here a definition that is a simplified one given in [47], where we assumed a stratification on the singular set. 

**Definition 2.1.** (Singular affine integral manifold) 

- (a) An _integral affine structure_ on a topological _n_ -manifold _B_ is an equivalence class of an atlases, where each atlas _{_ ( _Ui, ϕi_ ) _}i∈I_ in the equivalence class has the property that for any _i, j ∈ I_ the coordinate change map _ϕj ◦ ϕ[−] i_[1] is given by the action of an element _g_ in semi-direct product R _[n] ×SLn_ (Z) in the sense that 

   - _ϕj ◦ ϕ[−] i_[1][(] _[x]_[) =] _[ gx,][ ∀][x][ ∈][ϕ][i]_[(] _[U][i][ ∩][U][j]_[)] 

and two atlases are equivalent if their union is an atlas of this type. 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

15 

- (b) A _tropical affine manifold with singularities_ (c.f. Gross [20, Definition 1.24]) is a topological manifold _B_ with an integral affine structure on the complement of a finite union 

**==> picture [77 x 14] intentionally omitted <==**

of codimension at least two topological submanifolds _Zk ⊂ B_ . 

The integral affine manifolds we encounter in this paper may be obtained by gluing together open subsets of plane at a subset of _branch cuts_ . Each branch cut _Ci ⊂_ R[2] is a ray whose intersection _Ci ∩_ ∆is a line segment whose end-points _∂Ci_ = _{ζ, bi} ⊂_ ∆ consist of a vertex _ζ_ of ∆and a singular point _bi_ . The singular affine manifold _B_ is obtained by gluing the trivial affine structure on _B\{C_ 1 _, . . . , Ck}_ along the branch cut _Ci_ with a _shear_ conjugate to a matrix of the form 

**==> picture [262 x 27] intentionally omitted <==**

Of course, a given affine manifold may be represented by different polytopes that are related to each other by “transferring the cut” operations From Definition 2.13. In the pictures, we draw only the line segments _Ci ∩_ ∆with dotted lines. 

**Definition 2.2.** An _almost toric moment map_ for a symplectic four-manifold ( _X, ω_ ) is a smooth surjective map Φ : _X → B_ to a two-dimensional singular affine integral manifold _B_ satisfying the following: For any _x ∈ X_ there is a Darboux chart ( _q_ 1 _, p_ 1 _, q_ 2 _, p_ 2) on a neighborhood _U ⊂ X_ of _x_ , and a representation of _B_ as a polytope ∆ _⊂_ R[2] so that Φ _|U_ is a product of maps of the form 

- (a) (Non-singular) Φ _i_ ( _qi, pi_ ) = _pi_ ; 

- (b) (Elliptic) Φ _i_ ( _qi, pi_ ) = 2[1][(] _[q] i_[2][+] _[ p]_[2] _i_[);][and] 

- (c) (Focus-focus) Φ( _qi, pi, qi_ +1 _, pi_ +1) = ( _qipi_ + _qi_ +1 _pi_ +1 _, qipi_ +1 _− qi_ +1 _pi_ ). 

The triple ( _X, ω,_ Φ) is called an _almost toric manifold_ and the map Φ is an _almost toric moment map_ . The last singularities at the origin in the second and third cases are called _elliptic_ and _focus-focus singularities_ respectively. The set of focus-focus singularities is denoted by _X_[foc] _⊂ X_ . 

The focus-focus singularities represent nodal singularities in the fibers; see Figure 7. We often fix the representation of the affine manifold _B_ as a polytope ∆ _⊂_ R[2] with branch cuts. Then, the map 

**==> picture [56 x 11] intentionally omitted <==**

is an honest moment map on the complement Φ _[−]_[1] ( _B\ ∪i Ci_ ) of the preimage of the branch cuts _Ci_ . The data ∆ _⊂ B_ with branch cuts ( _C_ 1 _, . . . , Ck_ ) and focus-focus values _B_[foc] _⊂_ ∆is called the _base diagram_ of the almost toric manifold. 

The reader may wish to keep in mind the following example: 

_Example_ 2.3 _._ (Spherical pendulum, see e.g. Duistermaat [12]) A completely integrable structure on the cotangent bundle _X_ = _T[∗] S_[2] is given by the energy of the spherical pendulum and its angular momentum. The energy is defined by a sum of kinetic and potential terms, 

**==> picture [171 x 23] intentionally omitted <==**

16 

## S. VENUGOPALAN AND C. WOODWARD 

**==> picture [120 x 79] intentionally omitted <==**

Figure 7. A focus-focus singularity 

where _π_ : _T[∗] S_[2] _→ S_[2] is the projection, _ξ ∈_ R[3] is the direction of gravity and _∥v∥_ is the norm defined using the standard invariant metric. The angular momentum is defined by 

_ψ_ : _X →_ R _, v �→⟨ι_ ( _v_ ) _, ξ⟩_ 

where _ι_ : _T[∗] S_[2] _→_ R[3] is the moment map for the _SO_ (3)-action. Combining the two functions gives rise to a map 

**==> picture [105 x 13] intentionally omitted <==**

Its moment image has boundary given by the set of points corresponding to the “horizontal motions” on the sphere [12, 3.6]. The map Ψ has a single interior critical point _x_ + _∈_ Crit(Ψ) which is a focus-focus singularity corresponding to the unstable equilibrium of the spherical pendulum, and an elliptic critical point _x− ∈_ Crit(Ψ) corresponding to the stable equilibrium that lies over the boundary. An application of the Arnold-Liouville theorem gives an almost toric structure for _X_ with a moment map Φ with the following properties: a single focus-focus singularity, a moment image equal to the cone on the vectors ( _−_ 1 _,_ 1) and (1 _,_ 1), with the stable equilibrium _x−_ mapping to (0 _,_ 0) and the unstable equilibrium _x_ + mapping to (0 _,_ 1). See Figure 42, which also has the disks contributing to the disk potential drawn. This ends the Example. 

The following proposition is a well-known consequence of the Arnold-Liouville theorem [13, Chapter 2]: 

**Proposition 2.4.** _Let_ Φ : _X → B be an almost toric moment map in the sense of Definition 2.2. Then B has the structure of an tropical affine manifold with singularities the set B_[foc] _of images of the focus-focus critical points._ 

The inverse image of the boundary of the moment polytope is an immersed symplectic submanifold of codimension two. We call this inverse image 

**==> picture [85 x 13] intentionally omitted <==**

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

17 

of the boundary _∂_ Φ( _X_ ) the _divisor at infinity_ , borrowing terminology from algebraic geometry. The following is immediate from the list of allowable singularities in Definition 2.2: 

**Lemma 2.5.** _The divisor at infinity D ⊂ X is an immersed symplectic submanifold, whose self-intersections are the points x in X where the moment map_ Φ _has rank_ 0 _, but x is not a focus-focus point._ 

That is, the self-intersection points are the elliptic singularities of rank two, which would be the torus fixed points in the case of a toric surface. The irreducible components of the divisor at infinity 

**==> picture [101 x 10] intentionally omitted <==**

are called the _boundary divisors_ , of in algebraic geometry language, the prime components of the divisor at infinity _D_ . For example, if _X_ is a toric manifold then the _D_ 1 _, . . . , Dk_ are the prime invariant divisors in _X_ , which are the inverse images of the facets 

**==> picture [93 x 12] intentionally omitted <==**

under the moment map Φ. The vertices that are the images of elliptic singularities may be characterized alternatively as follows: 

**Proposition 2.6.** _A vertex b of_ Φ( _X_ ) _is the image of an elliptic singularity if b is not contained in any branch cut, or if b is contained in a branch cut Ci, the adjacent edges e−, e_ + _to b are not parallel after applying the shear si to e_ + _._ 

_Proof._ After gluing the affine structures on either side of the branch cut, if it exists, the condition for _b_ to be the image of an elliptic singularity is exactly that _b_ is contained in two facets of the moment image in a neighborhood of _b_ . □ 

The following result will be used to facilitate the computation of Maslov indices of holomorphic disks by counts of intersection numbers with the divisor at infinity. By a result of Symington [44], see also Li-Ming-Ning [27]: 

**Definition 2.7.** A _symplectic pair_ ( _X, D_ ) consisting of a symplectic manifold _X_ and a finite union of codimension two symplectic submanifolds _D_ . The pair ( _X, D_ ) is _log Calabi-Yau_ if _D_ represents the first Chern class of _X_ in the sense that 

**==> picture [114 x 13] intentionally omitted <==**

By a result of Symington [44, Proposition 8.2], see also Li-Ming-Ning [27], the pair consisting of an almost toric manifold and its divisor at infinity is log Calabi-Yau. The same identity holds in the relative cohomology _H_[2] ( _X, L_ ) for any Lagrangian fiber fiber _L_ over an interior point. 

_Example_ 2.8 _._ Let _X_ be almost toric four-manifold with moment image ∆= Φ( _X_ ). The _boundary divisor D_ = Φ _[−]_[1] ( _∂_ Φ( _X_ )) can be made into an embedded symplectic two-torus _D_ = _[∼] T_[2] by performing nodal trades at all torus fixed points as explained below in Section 2.2. In particular, the first Chern class is represented by an embedded symplectic torus. 

S. VENUGOPALAN AND C. WOODWARD 

18 

**Definition 2.9.** An almost toric manifold _X_ is called _monotone_ if the symplectic class [ _ω_ ] _∈ H_[2] ( _X_ ) is a positive multiple of the first Chern class _c_ 1( _X_ ) _∈ H_[2] ( _X_ ): 

**==> picture [114 x 12] intentionally omitted <==**

_Example_ 2.10 _._ By a _del Pezzo surface_ we mean a non-singular projective algebraic surface with ample anti-canonical divisor class, whose symplectic form is taken to lie in the anti-canonical class. Uniqueness of these symplectic structures up to symplectomorphic follows from McDuff [32]. According to Ohta-Ono [37], any monotone symplectic four-manifold is of this form. Vianna [49] has given examples of almost toric structures on del Pezzo surface, shown in Figure 8, and shown that these contain monotone torus fibers: The diagrams constructed there are obtained by a combination of monotone blow-ups and nodal trades and slides, starting from the standard toric diagram for the complex projective plane. These operations preserve monotonicity. 

**==> picture [59 x 58] intentionally omitted <==**

Figure 8. Almost toric diagrams for the del Pezzo surfaces 

We are particularly interested in almost toric diagrams for del Pezzo surfaces where the focus-focus values are close to the vertices. 

**Definition 2.11.** A base diagram ( _B,_ ∆ _, C, B_[foc] ) of a monotone almost toric manifold _X_ is _of Vianna type_ if the cut loci _Ci_ in _C_ do not intersect, and the image of the monotone fiber _λ_ = Φ( _L_ ) does not lie on any branch cut. 

Later we wil need the following relationship between the volume of the the moment polytope and the degree of the del Pezzo surface: 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

19 

**Lemma 2.12.** _Let X be a compact connected almost toric four-manifold. The moment polytope_ ∆ _determines, by its volume, the square of the first Chern class via the relation_ 

**==> picture [198 x 26] intentionally omitted <==**

_Proof._ Indeed, the Duistermaat-Heckman measure is Lebesgue measure for toric varieties, by the local model for Lagrangian torus fibers. See for example Guillemin [22, Theorem 2.10] for the toric case; the almost toric case has a similar proof. □ 

2.2. **Modifications of almost toric structures.** The following are operations on almost toric manifolds of dimension four, as shown in Figure 9. Let _X_ be an almost toric symplectic four manifold with symplectic form _ω_ . 

**==> picture [210 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
Nodal trade<br>Transferring the cut<br>Nodal slide<br>**----- End of picture text -----**<br>


Figure 9. Operations on almost toric diagrams 

**Definition 2.13.** Suppose an almost toric structure on a compact symplectic fourmanifold _X_ with base diagram ∆is given. 

- (a) _Transferring the cut_ is an operation which produces a new almost toric structure on _X_ with the same number _|B_[foc] _|_ of focus-focus values as follows. Suppose the base diagram ∆ _[′]_ has cuts ( _C_ 1 _, . . . , ck_ ). The new cuts are 

( _C_ 1 _[′][, . . . , C] k[′]_[) = (] _[C]_[1] _[, . . . , C][i][−]_[1] _[, C] i[′][, s][i][C][i]_[+1] _[, . . . , s][i][C][k]_[)] 

where _Ci[′]_[is][obtained][as][follows.] Given a branch cut starting at _b_ in the direction of _v_ , 

**==> picture [106 x 12] intentionally omitted <==**

**==> picture [220 x 30] intentionally omitted <==**

**==> picture [260 x 32] intentionally omitted <==**

S. VENUGOPALAN AND C. WOODWARD 

20 

The base ∆ _[′]_ of the new almost toric structure is the union 

**==> picture [89 x 12] intentionally omitted <==**

of “half” of the base ∆ _−_ with the sheared “other half” _si_ (∆+) where _si ∈ GL_ (2 _,_ R) is a shear along _Ci_ . The new base ∆ _[′]_ has a new vertex at the point of intersection _Ci[′][∩][∂]_[∆.][In][the][example][in][Figure][10][the][shear] _[s]_[2][is] 

**==> picture [76 x 27] intentionally omitted <==**

- (b) A _nodal trade_ modifies the base diagram ∆so that the number of focusfocus values _B_[foc] increases by one, as follows. Suppose the base diagram ∆ has an elliptic critical point _x ∈ X_ over a vertex _b ∈_ ∆adjacent to facets _Q_ 1 _, Q_ 2 _⊂_ ∆whose normal vectors are _ν_ 1 _, ν_ 2. A nodal trade adds a focusfocus singularity _x[′] ∈ X_[foc] whose image is at a point _b[′] ∈ B_[foc] on the ray in the direction _ν_ 1 + _ν_ 2 from the vertex _b_ , and a new cut _Ck_ +1 from _b[′]_ to _b_ . 

- (c) A _nodal slide_ modifies the base diagram ∆by changing the position of a focus-focus value _b ∈ B_[foc] in the direction of the adjacent cut _Ci ⊂_ ∆, and adjusting the length of the cut _Ci_ if necessary so that it ends at the focusfocus value _b_ . 

- (d) A _mutation_ produces a new base diagram ∆ _[′]_ which is a combination of transferring the cut and a nodal slide in which one of the focus-focus values _bi ∈ B_[foc] is moved in the direction of the branch cut until it is close to the other intersection point of the line containing the branch cut with the moment polytope Φ( _X_ ), and performing an accompanying shear 

**==> picture [79 x 13] intentionally omitted <==**

of the moment polytope. 

**==> picture [276 x 125] intentionally omitted <==**

**----- Start of picture text -----**<br>
(0 ,  1)<br>(0 ,  1)<br>Transferring<br>the cut C 1<br>C 1 ( [1] 2 [,] [1] 2 [)]<br>C 2 C 3 C 2 [′]<br>(0 ,  0)<br>(1 ,  0)<br>s 2<br>s 2 C 3<br>(0 , − 1)<br>**----- End of picture text -----**<br>


Figure 10. Transferring a cut 

The Hamiltonian isotopy class of a Lagrangian fiber of an almost toric structure is invariant under modifications of almost toric structures except for a nodal slide that crosses a focus-focus fiber: Let 

**==> picture [115 x 13] intentionally omitted <==**

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

21 

be a smooth family of almost toric structures on a simply-connected four-manifold _X_ , _µ ∈_ R[2] , and 

**==> picture [64 x 13] intentionally omitted <==**

a regular monotone Lagrangian fiber of Φ _t_ for each _t ∈_ [0 _,_ 1]. 

**Lemma 2.14.** _Suppose that X,_ Φ _t, Lt is a family of smooth almost toric fibers with fixed moment image, so that_ Φ _t_ ( _X_ ) _and_ Φ _t_ ( _Lt_ ) _are independent of t ∈_ [0 _,_ 1] _as above. The Hamiltonian isotopy class of Lt is independent of t._ 

_Proof._ It suffices to check that the isotopy is exact in the sense of, for example, Weinstein [51]. By assumption _X_ is simply-connected, each loop _γt_ : _S_[1] _→ Lt_ bounds a disk _ut_ . We may assume that _ut_ is smoothly varying in _t ∈_ [0 _,_ 1] since the isotopy is smooth. By continuity, _ut_ has constant Maslov index _I_ ( _ut_ ) and so constant area _A_ ( _ut_ ) by monotonicity. The deformation _Lt_ defines a family of closed one-forms _αt,s ∈_ Ω[1] ( _Lt_ ), so that _Lt_ + _s_ is the graph of _αt,s_ in some Weinstein neighborhood of _Lt_ and the deformation one-forms _αt_ := _ds[d][α][t,s][|][s]_[=0][are][independent][of][the][choice][of] neighborhood. By Stokes’ theorem 

**==> picture [109 x 28] intentionally omitted <==**

Since the areas are constant, the periods of _αt_ vanish. Hence the one-forms _αt_ are exact, which implies the deformation _Lt_ is exact. □ 

On the other hand, the fibers of a family of focus-focus values which cross the monotone value gives new isotopy classes of monotone Lagrangian tori. Using this operation, Vianna [49] shows that every monotone del Pezzo surface has the structure of an almost toric manifold (even with a triangular base), shown in Figure 8. An example of an almost toric diagram for the blow-up of the projective plane at five points is shown in Figure 1. The diagrams with triangular base corresponds to solutions to Markov-type equations, as explained in Vianna [49]. Diagrams for Bl _[k]_ P[2] _, k_ = 5 _,_ 7 _,_ 8 are shown in Figure 11. 

**==> picture [168 x 101] intentionally omitted <==**

**----- Start of picture text -----**<br>
E 8<br>E 7<br>D 5<br>**----- End of picture text -----**<br>


Figure 11. Triangular almost toric diagrams 

22 

## S. VENUGOPALAN AND C. WOODWARD 

## 3. Tropical limit theorems 

We describe the degeneration techniques from Venugopalan-Woodward [46] which allow the computation of disk potentials for Lagrangians submanifolds. In [46] these tropical limit theorems were stated for treed disks, while here we are concerned only with disks passing through a generic point on the Lagrangian. 

3.1. **Disk potentials.** The disk potential of a monotone Lagrangian brane is a count of Maslov-index-two holomorphic disks with the Lagrangian as boundary condition. Let ( _X, ω_ ) be a compact symplectic manifold. By a _Lagrangian brane_ we mean a compact relatively-spin graded Lagrangian _L ⊂ X_ . For such a brane (at least, under rationality constraints discussed in [6]) the potential in a Morse model is defined as follows. Let 

**==> picture [48 x 11] intentionally omitted <==**

be a Morse function. Let 

**==> picture [132 x 14] intentionally omitted <==**

denote the Novikov fields in a formal variable _q_ , and Λ _≥_ 0 _⊂_ Λ the Novikov ring generated by elements with non-negative _q_ -valuation. The group of _Floer cochains_ 

**==> picture [104 x 27] intentionally omitted <==**

is the free group generated by the set of critical points 

**==> picture [76 x 12] intentionally omitted <==**

By the construction in Charest-Woodward [7], the group _CF_ ( _L_ ) has an _A∞_ structure with composition maps 

**==> picture [180 x 13] intentionally omitted <==**

defined given by weighted counts of treed holomorphic disks _u_ : _C → X_ with boundary in _L_ . Here “treed” refers to the definition of _C_ as the union of a surface part _S_ and a tree part _T_ . The map _u_ is required to be pseudoholomorphic on the surface part on _S_ (with respect to some domain-dependent almost complex structure, after perturbation) and a gradient flow on the tree part _T_ (with respect to some domain-dependent function, after perturbation). The details will not concern us very much, since we will be interested in a simplified version in which we count holomorphic disks with boundary in _L_ with point constraints. Strict units 

**==> picture [71 x 12] intentionally omitted <==**

are provided by a homotopy unit construction. The resulting Fukaya category Fuk( _X_ ) may be curved, meaning that the zero-th composition map _m_ 0 may be non-zero. Let _CF_[odd] ( _L_ )+ _⊂ CF_ ( _L_ ) denote the space generated by elements with positive _q_ -valuation. Let _MC_ ( _X, L_ ) denote the space of elements _b ∈ CF_[odd] ( _L_ ) of solutions to the _projective Maurer-Cartan equation_ 

**==> picture [205 x 12] intentionally omitted <==**

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

23 

The coefficient in front of the identity gives rise to the _disk potential_ 

(8) _WX,L_ : _MC_ ( _X, L_ ) _→_ Λ _≥_ 0 

counting holomorphic disks with boundary in _L_ . The pair ( _MC_ ( _X, L_ ) _, WX,L_ ) is independent of all choices up to gauge transformation. In the monotone case, there is a simplified definition of the disk potential which avoids the machinery of _A∞_ algebras. Namely, we restrict to the case _b_ = 0 and obtain a function also denoted 

**==> picture [95 x 12] intentionally omitted <==**

on the space of local systems 

**==> picture [131 x 12] intentionally omitted <==**

which counts disks passing through a generic point. The arguments in Oh [36] show that the potential is independent of the choice of almost complex structure, and depends only on the Hamiltonian isotopy class of _L_ . In this paper we will focus on the monotone case. However, many of the techniques apply also to the computation of potentials for non-monotone Lagrangians; for example, the Lagrangians near the anti-canonical divisor considered in [19]. 

The regularization scheme described in [36] to define the potential uses a generic domain-independent almost complex structure. In order to make contact with the theory of broken maps in [46] we will use domain-dependent almost complex structures as in Cieliebak-Mohnke [10]. These moduli spaces have additional interior markings corresponding to the intersection of the maps with a Donaldson hypersurface _D ⊂ X_ of large degree, disjoint from the Lagrangian, and so that the Lagrangian _L_ is exact in the complement of _D_ . We denote by the moduli space of maps satisfying the given constraints, and _Md_ ( _X, L_ ) the union over all types with _d_ semi-infinite boundary edges. 

To each holomorphic disk, we associate a map type as follows. The vertices Vert(Γ) of the type Γ correspond to components of the domain, while the edges Edge(Γ) correspond to either nodes or markings. Edges _e ∈_ Edge _→_ (Γ) corresponding to markings are incident on one vertex each, and those _e ∈_ Edge _−_ (Γ) corresponding to nodes are incident on two vertices. The set of edges by definition have a partition 

## Edge(Γ) = Edge (Γ) _∪_ Edge (Γ) 

into an open and closed subsets. The closed leaves correspond to intersections with the Donaldson divisor. The vertices _v ∈_ Vert(Γ) are decorated with the homotopy classes [ _uv_ ] of the corresponding map _uv_ . For a boundary marking corresponding to _e ∈_ Edge _,→_[(][Γ][)][we][have][an][evaluation][map] 

## ev _e_ : _M_ ( _X, L_ ) _→ L_ 

evaluating the map at the corresponding boundary marking _ze ∈ C_ . The underlying _domain type_ Γ is obtained by forgetting the labelling of the vertices by homotopy classes. 

**Definition 3.1.** (Disk potential for monotone Lagrangians) Given a Lagrangian brane _L_ , the disk potential of _L_ is the count of Maslov-index-two disks with a single 

S. VENUGOPALAN AND C. WOODWARD 

24 

point constraint on the boundary _Y_ = ( _p ∈ L_ ) defined by the formula 

**==> picture [288 x 32] intentionally omitted <==**

where 

- Γ ranges over types of maps with no boundary input markings and a single output marking that is constrained to map to a point _p ∈ L_ , that is, _Y_ = ( _p_ ); 

- Hol _L_ ([ _∂u_ ]) _∈_ Λ _[×]_ is the evaluation of the local system Hol _L ∈_ Rep( _L_ ) on the homotopy class of loops [ _∂u_ ] _∈ π_ 1( _L_ ) defined by going around the boundary of each disk component in the treed disk once, 

- _d_ (Γ) _∈_ Z _≥_ 0 is the number of interior markings, 

- and _ϵ_ ( _u_ ) _∈{±_ 1 _}_ is the orientation sign of _u_ defined using the relative spin structure. For almost toric moment fibers we assume that the relative spin structure is the standard torus-invariant spin structure. 

_Remark_ 3.2 _._ For a monotone pair ( _X, L_ ), the disk potential is independent of choices, by an argument similar to that in Theorem 6.31 below. In the general case, the disk potential is defined as a function on the Maurer-Cartan moduli space as in (8). 

3.2. **Broken Maps.** Broken maps arise from multi-directional neck stretching. We review the theory from Venugopalan-Woodward [46], which is a version of Brett Parker’s work for closed maps. 

_Notation_ 3.3 _._ Let _X_ be a compact symplectic four-manifold with an almost toric structure with codomain _B_ , containing the image of the almost toric moment map ∆= Φ( _X_ ), and focus-focus image _B_[foc] _⊂ B_ . The locus _B − B_[foc] is equipped with an affine structure modelled on t _[∨]_ , where _T ≃_ ( _S_[1] )[2] . A subset _P ⊂ B_ is a _polyhedron_ if in a coordinate chart _U ⊂ B − B_[foc] homeomorphic to an open subset of R _[n]_ , the intersection _P ∩ U_ is the inverse image of a finite intersection of halfspaces _H_ 1 _, . . . , Hk_ in R _[n]_ . The polyhedron _P_ is _rational_ if the half spaces _Hi_ have rational normal vectors. Let ∆ _⊂ B_ be a polyhedron; we have in mind the case that ∆= Φ( _X_ ) is the moment image of an almost toric moment map. 

**Definition 3.4.** A _polyhedral decomposition_ of ∆ _⊂ B_ is a collection _P_ of rational polyhedra _P ⊂ B_ such that 

- (a) _B_ is equal to the union _∪P ∈P P_ ; 

- (b) The intersection of any two polytopes _P_ 0 _, P_ 1 _∈P_ is either empty or a face of each; 

- (c) each focus-focus value _b ∈ B_[foc] is contained in the interior of some polyhedron _P ∈P_ ; and 

- (d) any polyhedron _P ∈P_ intersects the boundary _∂_ ∆transversally. 

Given such _P_ , for any polytope _P ∈P_ , there is a cut space 

**==> picture [90 x 13] intentionally omitted <==**

where _TP ⊂ T_ is the torus whose Lie algebra is the annihilator of the span of _TP ⊂_ t _[∨]_ , and _P[◦]_ is the complement of the faces _Q ⊂ P, Q ∈P_ of _P_ . The _broken_ 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

25 

_manifold_ associated to _P_ is the disjoint union 

**==> picture [58 x 25] intentionally omitted <==**

where _XP_ is the _thickening_ of _XP_ defined by 

**==> picture [94 x 13] intentionally omitted <==**

This ends the definition. 

We will consider in this paper only the case that the Lagrangian is a fiber of the almost toric structure. In particular, we assume that the Lagrangian submanifold _L ⊂ X_ is disjoint from the cuts so that _L_ lies in a component _XP_ of the broken manifold _X_ where _P ∈P_ is a top-dimensional polytope. 

_Example_ 3.5 _._ The simplest examples of polyhedral decompositions are those cut out by a collection of lines with rational directions. If _B_ is realized as a subset of R[2] with cut loci _Ci ⊂ B_ , then any line _H_ in _B_ not passing through the cut loci defines a polyhedral decomposition with three pieces. On the other hand, if _H_ passes through a cut _Ci_ then the complement of _H_ is not locally a convex polytope (as the halfspaces undergo shears through the cut loci). Instead, changing the direction of _H_ after it passes through _Ci_ results in an allowable cut. See Figures 12, 21, 24 for examples. 

As described in [46], in the neck-stretching limit holomorphic maps converge to broken maps, which is a version of Parker’s exploded maps in [38]. A broken map is equipped with a tropical structure, which we recall here. 

**Definition 3.6.** A _tropical structure_ on a graph 

**==> picture [111 x 12] intentionally omitted <==**

is a collection of polytope assignments _P_ ( _v_ ) _∈P_ for vertices _v ∈_ Vert(Γ) and _edge directions_ 

**==> picture [69 x 14] intentionally omitted <==**

with _P_ ( _e_ ) defined by 

**==> picture [112 x 12] intentionally omitted <==**

so that the graph Γ is realizable in the dual complex _B[∨]_ of the neck-stretching in the following sense: There exist a collection of _tropical positions_ of the vertices in the dual complex 

**==> picture [167 x 13] intentionally omitted <==**

that satisfy 

**==> picture [268 x 13] intentionally omitted <==**

for any edge _e_ = ( _v_ + _, v−_ ). The image of _T_ (Γ) under the map to _B[∨]_ induced by _v �→T_ ( _v_ ) is called a _realization of a tropical graph_ , and the underlying graph equipped with the edge directions _{T_ ( _e_ ) _}e_ and vertex polytopes _{P_ ( _v_ ) _}v_ is called a _tropical graph_ . This ends the Definition. 

S. VENUGOPALAN AND C. WOODWARD 

26 

A broken map is a collection of holomorphic maps on punctured curves associated to the vertices of a tropical graph. We equip _X_ with an almost complex structure that is cylindrical near each cut; this induces a collection of almost complex structures on _XP_ that are invariant with respect to the translation action of t _P_ . 

**Definition 3.7.** Given such a graph Γ a broken map with domain type Γ is a collection 

_uv_ : _Cv[◦][→X] P_ ( _v_ ) _[, v][∈]_[Vert(Γ)] 

of pseudoholomorphic maps satisfying certain matching conditions explained below on the lifts of nodal points. Each of the domain components _Cv[◦]_[is][an][irreducible] curve component _Cv ⊂ C_ (possibly with boundary) punctured at interior nodal points, that is, 

_Cv[◦]_[:=] _[ C][v][\{]_[interior][nodes] _[}][.]_ 

The matching conditions are described as follows. Suppose that _we[±][∈][C][v] ±_[are][the] lifts of a node _we_ corresponding to an edge _e_ = ( _v_ + _, v−_ ). At the cylindrical or strip-like ends of _Cv±\we[±]_[,][the][map] _[u][v] ±_[is][asymptotic][to][a][map][given][by][the][action] of a one-parameter subgroup corresponding to some _direction T_ ( _e_ ) _∈_ t _P_ ( _e_ ) _,_ Z. The matching condition at the node _we_ is that the map ( _πT[⊥]_ ( _e_ ) _[◦][u][v][±]_[)][has][a][removable] singularity at the node _we[±]_[,][and] 

(11) ( _πT[⊥]_ ( _e_ ) _[◦][u][v]_ +[)(] _[w] e_[+][) = (] _[π] T[⊥]_ ( _e_ ) _[◦][u][v] −_[)(] _[w] e[−]_[)] _[ ∈X] P_ ( _e_ ) _[/T] T_ ( _e_ ) _,_ C _[.]_ 

The quantities in the left-hand side and right-hand side of (11) are called _projected tropical evaluations_ . In case _Q_ is a facet so that _XQ_ is a divisor of the compactified spaces _X P_ ( _v±_ ), this condition is simply that _uv±_ ( _z±_ ) _∈ XQ_ are equal but if _Q_ is higher codimension the condition says roughly that the ratios of derivatives match. In the latter case, we may consider a different compactification _X P_ ( _v±_ ) _,T_ ( _e_ ) of _XP_ ( _v±_ ) for which the space 

(12) _YT_ ( _e_ ) := _{_ [ _x_ ] = _TT_ ( _e_ ) _,_ C _x_ : _x ∈ X P_ ( _v±_ ) _}_ 

of orbit closures is a divisor in _X P_ ( _v±_ ) _,T_ ( _e_ ) ; then (11) says that the points _uv±_ ( _z±_ ) _∈ YT_ ( _e_ ) are equal in the compactifications _X P_ ( _v±_ ) _,T_ ( _e_ ). The object defined so far is an _unframed broken map_ . 

A _broken map_ consists of an unframed broken map and a _framing_ , which is a linear isomorphism 

**==> picture [268 x 14] intentionally omitted <==**

such that any pair of holomorphic coordinates _z_ +, _z−_ in the neighborhood of _we_[+][,] _we[−]_[satisfying] 

(14) d _z_ +( _we_[+][)] _[ ⊗]_[d] _[z][−]_[(] _[w] e[−]_[) = fr] _[e]_ 

are _matching coordinates_ in the sense that the following 

**==> picture [345 x 21] intentionally omitted <==**

holds. The quantities in the left-hand side and right-hand side of (15) are called the _tropical evaluations_ at _we_[+][and] _[w] e[−]_[respectively.][This][ends][the][Definition.] 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

27 

_Remark_ 3.8 _._ An unframed broken map has a finite number of framings as explained in Remark T-4.26. 

A sample polyhedral degeneration of the almost toric diagram of the degree four del Pezzo surface is shown in Figure 12. Let _u_ = ( _uv_ ) _v ∈_ Vert(Γ) be a broken map. The graph Γ with the additional data of the homotopy classes of the maps [ _uv_ ] is called the _type_ of the broken map _u_ and denoted 

**==> picture [110 x 13] intentionally omitted <==**

Denote by _M_ Γ( _X , L_ ) the moduli space of broken maps of type Γ. 

**==> picture [87 x 88] intentionally omitted <==**

**==> picture [191 x 88] intentionally omitted <==**

Figure 12. A polyhedral decomposition of an almost toric diagram and three Maslov-two broken disks 

The disk potential in a broken manifold is defined similarly to the unbroken case, the only difference being that one counts broken disks. Assuming that _L ⊂X_ is a monotone Lagrangian brane contained in a top-dimensional component _XP ⊂X_ , the _disk potential_ is 

**==> picture [288 x 32] intentionally omitted <==**

where Γ ranges over types of broken disks with no boundary input markings and a single output marking that is constrained to map to a point _p ∈ L_ , that is, _Y_ = ( _p_ ). Furthermore, Hol _L_ ([ _∂u_ ]), _d_ (Γ), _ϵ_ ( _u_ ) are as in (9); and the area of a broken map _u_ is the sum of the areas of the projections of its components, that is, 

**==> picture [271 x 27] intentionally omitted <==**

where _πP_ ( _v_ ) : _XP_ ( _v_ ) _→ XP_ ( _v_ ) is the projection to the base of the fibration. When ( _X, L_ ) is monotone, the fact that _WX ,L_ is independent of all choices will be a consequence of the tropical limit theorem in the next section. 

3.3. **Tropical limit theorems for moduli spaces.** In [46], we showed that the Fukaya algebra of a Lagrangian is equivalent to Fukaya algebra defined by counting broken maps. In particular, the corresponding disk potentials 

**==> picture [237 x 12] intentionally omitted <==**

are equivalent up to a gauge transformation on _MC_ ( _X, L_ ) = _[∼] MC_ ( _X , L_ ) _._ Returning to the monotone case, one has equality of the broken and unbroken potentials: 

S. VENUGOPALAN AND C. WOODWARD 

28 

**Theorem 3.9.** _Suppose L ⊂ X is monotone and Y_ = _{p} consists of a point constraintdimensionalatcobordisma single boundaryM_ ˜ ( _X, L, Ypoint_ )1 _whosep ∈ Lboundary. There exists a compact oriented one-_ 

**==> picture [221 x 16] intentionally omitted <==**

_(here the superscript − indicates reversed orientation) is the union of the original moduli space of Maslov-index-two disks M_ ( _X, L, Y_ )0 _and the broken moduli space of disks M_ ( _X , L, Y_ )0 _that is a compact one-manifold with boundary._ 

_Proof._ We assume the reader is familiar with the neck-stretching framework in our previous paper [46]. Let 

**==> picture [133 x 12] intentionally omitted <==**

be a family of almost complex structures corresponding to neck-stretching along the inverse images of the proper faces in the polyhedral decomposition _P_ as in [46]. Denote by _M_ ( _X, L, J_ ) denote the moduli space of pairs ( _t, u_ ) where _u_ is _Jt_ holomorphic. In general, _M_ ( _X, L, J_ ) has boundary components arising from disk bubbling. 

The situation is dramatically simplified if _L_ is monotone: Suppose, by way of contradiction, that there exist a _Jt_ -holomorphic map _u_ : _C → X_ that lies in a boundary component of _M_ ( _X, L, Y_ ) has an edge _Te ⊂ C_ of infinite length _ℓ_ ( _e_ ) = _∞_ . Cutting at this edge produces maps 

**==> picture [65 x 11] intentionally omitted <==**

with boundary in _L_ with say the disk _C_ + containing the point constraint on _L_ . Stability forces each component _u±_ to have positive area, since each has at most two semi-infinite edges. Monotonicity implies that _I_ ( _u−_ ) _≥_ 2. The total Maslov index is then 

**==> picture [124 x 12] intentionally omitted <==**

which is a contradiction. Therefore, the only boundary configurations are broken maps and configurations that are holomorphic with respect to the original complex structure. □ 

In particular, any broken disk is the end of a family of unbroken disks, and we define the Maslov index of the broken disk to be the Maslov index of the corresponding family of unbroken disks. The same holds for the area. Since the Lagrangian is assumed monotone, the monotonicity relation holds for broken disks as well, so the Maslov index two broken disks have a fixed area. By the Gromov compactness result in [46], there are finitely many such broken disks. It follows that the potential _WX ,L_ has finitely many terms. The existence of the cobordism from Theorem 3.9 implies that the disk potential may be computed by degeneration: 

**Corollary 3.10.** _Let L ⊂ X be a monotone Lagrangian contained in the interior of some piece_ Φ _[−]_[1] ( _P_ ) _⊂ X. The potentials_ 

**==> picture [177 x 13] intentionally omitted <==**

_are equal as functions on_ Rep( _L_ ) _._ 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

29 

_Proof._ The statement of the Corollary follows from the fact that the signed count of ends of the cobordism in Theorem 3.9 is equal to zero. □ 

3.4. **Relative maps.** In this section we introduce terminology for a _relative map_ , which is a version of a broken map obtained by cutting some tropical edges. 

**Construction 3.11.** _Let u_ : _C →X be a broken map with domain type_ Γ _. Cutting a tropical edge Te ⊂ C in a broken map u produces two relative maps u_ + _, u−, both of which contain a cylindrical end corresponding to the edge e. The graph_ Γ _± of u± contains an edge e±, called a_ relative edge _resulting from the cutting of e that is incident on a single vertex in_ Γ _±._ 

- **Definition 3.12.** (a) A _type of relative map_ is a type Γ a broken map with a distinguished subset Edgerel(Γ) _⊂_ Edge _→,_ of _relative semi-infinite edges_ , and for each relative edge _e_ ,a polytope _P_ ( _e_ ) _∈P_ and a slope _T_ ( _e_ ) _∈_ t _P_ ( _e_ ) _,_ Z as in the case with broken maps at the nodes. 

   - (b) An _unframed relative map_ of type Γ is a map _u_ : _C →X_ so that for each _e ∈_ Edgerel(Γ), the cylindrical end of _Cv_ corresponding to _e_ the map _uv_ is asymptotic to a trivial cylinder of slope _T_ ( _e_ ). 

   - (c) A _framed relative map_ is an unframed relative map with the additional data of a framing at each such cylindrical end. 

Let _M_ Γ( _X , L_ ) resp. _M_[fr] Γ[(] _[X][, L]_[) denote the moduli space of unframed resp.][framed] relative maps of type Γ. Evaluation at the cylindrical ends corresponding to relative edges defines a _evaluation map_ as follows: Given a relative map let _z_ be a local holomorphic coordinate corresponding to the cylindrical end, compatible with the given framing. The evaluation map for relative maps is then 

**==> picture [225 x 20] intentionally omitted <==**

It induces a _projected evaluation map_ 

**==> picture [247 x 17] intentionally omitted <==**

where ( _πT[⊥]_ ( _e_ )[is][the][projection.] We now reconsider the situation considered at the beginning of this section in which we break an edge to obtain two relative types. We use the evaluation maps on relative markings to introduce moduli spaces of relative maps with constraints. 

**Definition 3.13.** A _system of constraints_ for a type Γ consists of, for every relative edge _e ∈_ Edgerel(Γ), 

- (Map constraint) a submanifold _Ye ⊂XP_ ( _e_ ) and 

- (Tropical constraint) an affine subspace Υ _e ⊂ P_ ( _e_ ) _[∨]_ that is parallel to the vector subspace t[rel] _e ⊂_ t _P_ ( _e_ ) _/ ⟨T_ ( _e_ ) _⟩_ . 

Let 

(18) _Y_ = ( _Ye_ ) _e∈_ Edgerel(Γ) _,_ 

S. VENUGOPALAN AND C. WOODWARD 

30 

be a system of constraints for which Γ has a realization _T_ : Vert(Γ) _→ B[∨]_ where for any relative edge _e_ incident on a vertex _ve_ satisfies the tropical constraint 

(19) _T_ ( _ve_ ) _∈_ Υ _e._ 

The moduli space of relative maps with constraints _Y_ is 

_M_ Γ( _X , L, Y_ ) = _{u ∈M_ Γ( _X , L_ ) _|_ ev _e_ ( _u_ ) _∈Ye, ∀e ∈_ Edge _−_ (Γ) _}._ 

The _tropical symmetry groups_ of a relative map with constraints is a collection 

**==> picture [78 x 13] intentionally omitted <==**

that satisfies 

(20) _gv_ + _gv[−] −_[1] _[∈{][z][T]_[ (] _[e]_[)][:] _[ z][∈]_[C] _[×][}] ∀e_ = ( _v_ + _, v−_ ) _∈_ Edge (Γ) _._ so that the translated maps ( _gvuv_ ) _v∈_ Vert(Γ) satisfy the given constraints. This ends the Definition. 

In four-dimensional examples, _Ye_ is either a point or the entire space _XP_ ( _e_ ) which we call an _trivial constraint_ . In the case of a point constraint, the tropical constraint _Ye[T]_[is a line in the direction] _[ T]_[ (] _[e]_[), and in the case of an trivial constraint, the tropical] constraint is also trivial, that is, _Ye[T]_[=] _[ P]_[(] _[e]_[)] _[∨]_[.] 

In general, the counts of maps with constraints depend on the choice of almost complex structure, in the same way that counts of holomorphic disks depend on this choice in the closed case as well. However, the count is invariant if all non-trivial constraints at relative markings are point constraints, and the type Γ _v_ of any disk component _v ∈_ Vert (Γ) is _primitive_ in the sense that it is not decomposable into types Γ1 and Γ2 of positive area. For example, if ( _XP_ ( _v_ ) _, L_ ) is toric, and torusinvariant divisors of _XP_ ( _v_ ) are relative divisors, then Γ _v_ is primitive exactly if _v_ has exactly one tropical edge or relative marking. 

**Proposition 3.14.** _Let_ Γ _be a type of a relative broken map to_ ( _X , L_ ) _, whose glued type is either a disk or a sphere, and the type_ Γ _v of any disk vertex v ∈_ Vert(Γ) _is primitive. Let Y_ = ( _Ye_ ) _e∈_ Edgerel(Γ) _be a collection of constraints each of which is either an trivial constraint or a point constraint, and so that the moduli space M_ Γ( _L, Y_ ) _of maps of type_ Γ _with constraints Y , and a single point constraint on the boundary, has expected dimension zero. Then the count m_ (Γ) _of maps of type_ Γ _is independent of the choice of almost complex structure, perturbation data, and generic point constraints Y. Moreover, for any two constraint data Y_ 0 _[,][Y]_ 1 _[,][there][is] a cobordism between the moduli spaces M_ Γ( _L, Y_ 0[)] _[,][M]_[Γ][(] _[L,][ Y]_ ~~1~~[)] _[.][The][tropical][con-] straints {_ Υ _e}e are assumed to be fixed._ 

_Proof._ The invariance statement in the Proposition is a standard cobordism arguhomotopyment: Givenbetweentwo datathem.( _P_ Let ~~_b_~~ _[,][ Y]_ ~~_b_~~ _M_[)] ˜[for] Γ( _L, Y[b][∈{]_ ) be[0] _[,]_[ 1] the _[}]_[let] parametrized[(] _[P]_ ~~_t_~~ _[,][ Y] t_[)] _[, t][∈]_ moduli[[0] _[,]_[ 1]] space[be][a][generic] for the family. We obtain a compact oriented cobordism between the moduli spaces for ( _P b[,][ Y]_ ~~_b_~~[)][for] _[b][∈{]_[0] _[,]_[ 1] _[}]_[,][because][bubbling][is][ruled][out][as][follows:][The][primitive-] ness assumption ensures that there is no disk bubbling. Formation of non-tropical interior nodes cuts down the expected dimension by two. Therefore, formation of 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

31 

interior nodes does not occur if ( _P_ ~~_t_~~ _[,][ Y] t_[) is generically chosen.][Since the index of the] maps in the parametrized moduli space is 1, by Remark 3.15 (b), there cannot be a limit map with an additional tropical node. □ 

_Remark_ 3.15 _._ (On tropical graphs of relative maps) 

- (a) If a relative map type Γ has associated moduli space _M_ Γ( _X , L_ ) of expected dimension zero, then its tropical symmetry group is finite, as explained in Lemma 4.39 of [46]. Consequently the tropical graph of Γ is _rigid_ . That is, the tropical graph of Γ has a unique set of vertex positions that satisfy the tropical constraint (19) at relative markings. 

- (b) The tropical behavior in the limit of relative maps is similar to the case of broken maps without relative markings. Suppose a sequence _{uν}ν_ of relative maps (all whose non-trivial constraints are point constraints) with a tropical graph Γ converges to a limit _u∞_ with a tropical graph Γ _[′]_ = Γ, then, the dimension of the tropical symmetry group satisfies 

dim( _T_ trop(Γ _[′]_ )) _>_ dim( _T_ trop(Γ)) _._ 

The proof is the same as the non-relative case in [46, Theorem 8.3], with the additional feature that both Γ and Γ _[′]_ satisfy tropical point constraints. In particular, if Γ is rigid, dim( _T_ trop(Γ _[′]_ )) _≥_ 2. Since the tropical symmetry group acts freely on the moduli space of maps, dim _M_ Γ _′_ ( _L, Y_ ) _≥_ 2, and since formation of tropical nodes does not affect the expected dimension of moduli spaces, we conclude that dim _M_ Γ( _L, Y_ ) _≥_ 2.[3] 

In the following result, we show that the moduli space of broken maps associated to a polyhedral decomposition of a symplectic four-manifold is honestly a product of moduli spaces associated to the pieces, rather than a fiber product. Such a product description is special to the genus zero, dimension four case; in general such a result can be expected only after further degeneration as explained in our previous work [47]. Denote by _LP_ ( _v_ ) the intersection _L ∩_ Φ _[−]_[1] ( _P_ ( _v_ )), which is either trivial or equal to _L_ . The result involves the automorphism group of the map type which we recall here: 

**Definition 3.16.** An _automorphism of a map type_ Γ is a graph automorphism _ϕ_ : Γ _→_ Γ for which _P_ ( _v_ ) = _P_ ( _ϕ_ ( _v_ )) for all vertices, the homotopy classes of the maps at _v_ and _ϕ_ ( _v_ ) are the same, and _ϕ_ preserves the ordering of boundary markings _e ∈_ Edge _→,_ (Γ) and interior markings Edge _→,_ (Γ). The group of automorphisms of Γ is denoted by Aut(Γ). 

> 3The tropical constraint (19) takes a more complicated form when a non-trivial constraint _Ye ⊂XP_ ( _e_ ) _/⟨T_ ( _e_ ) _⟩_ has positive dimension, and the constraint needs to be valid for maps in the compactification _M_ ( _L, Y_ ). Indeed, for maps in the compactification _M_ ( _L, Y_ ), the vertex containing the relative marking _ze_ may lie in _P[∨]_ for some _P ⊂ P_ ( _ve_ ). A positive dimensional constraint _Ye_ is required to be a manifold with cylindrical ends, and the tropical constraint is defined not just in _P_ ( _e_ ) _[∨]_ but also in polytopes _P[∨] ⊃ P_ ( _e_ ) _[∨]_ where _Ye_ has a cylindrical end in the _P_ -cylindrical end of _XP_ ( _e_ ). We do not need to consider such constraints in this paper. 

S. VENUGOPALAN AND C. WOODWARD 

32 

**Theorem 3.17.** (Distribution of constraints) _Let Y_ = ( _p ∈ L_ ) _be a point constraint, and let_ Γ _be a rigid map type for the constraint Y so that every subtype_ Γ _v consisting of a vertex v and the adjacent edges e is primitive. There exists a system of constraints (see Definition 3.13)_ 

**==> picture [117 x 13] intentionally omitted <==**

_for the graphs_ Γ( _v_ ) _⊂_ Γ _associated to the vertices v so that the moduli space M_ Γ( _X , L, Y_ ) _of broken maps of type_ Γ _admits a compact oriented cobordism_ 

**==> picture [360 x 40] intentionally omitted <==**

_to the product of moduli spaces over vertices v of_ Γ _, where µe ∈_ Z+ _is the lattice length of the edge slope T_ ( _e_ ) _, and_ 

**==> picture [118 x 21] intentionally omitted <==**

_Any tropical edge e has one end-point v_ + _where Y_ ~~_v_~~ + _[has][a][point][constraint][at][the] lift of the node we, and another end-point v− where the constraint Y_ ~~_v_~~ _−[at][the][node] we is trivial._ 

_Proof of Theorem 3.17._ The proof is an inductive argument based on the fact that for each edge, the moduli space of relative maps on one side of the edge must be rigid. First, we consider the case of replacing the matching condition at a single edge _e_ with a constraint at one of the lifts of the node _we_ . Assuming that cutting the edge _e_ in Γ produces relative map types Γ+, Γ _−_ , the moduli space of broken maps _M_ Γ( _X , L, Y_ ) is the inverse image ev _[−] e_[1][(∆)][of][the][diagonal][where] 

ev _e_ = (ev _e_ + _,_ ev _e−_ ) _,_ ev _e±_ : _M_ Γ _±_ ( _X , L, Y_ ) _→XP_ ( _e_ ) _/⟨T_ ( _e_ ) _⟩_ 

is the projected evaluation map. The moduli spaces _M_ Γ _±_ ( _X , L, Y_ ) are even dimensional, since they either involve spheres, or disks with their boundary on an oriented Lagrangian, and matching conditions are defined on even-dimensional manifolds. Therefore, one of them, say, _M_ Γ+( _X , L, Y_ ) is two-dimensional and _M_ Γ _−_ ( _X , L, Y_ ) is zero-dimensional. Then, we claim that the moduli space of broken maps is bijective to a product 

**==> picture [301 x 13] intentionally omitted <==**

where _Y±_ are obtained from _Y_ ~~_±_~~[by adding] _[ Y][e] ±_[at the broken edges,] _[ Y][e] −_[is the trivial] constraint, and _Ye_ + is a generic point constraint. To prove the claim, consider a map 

**==> picture [221 x 13] intentionally omitted <==**

Via the cobordism in Proposition 3.14, we may replace the point constraint _Ye_ + by the point ev _e−_ ( _u−_ ), and under the cobordism 

**==> picture [195 x 13] intentionally omitted <==**

we may replace the map _u_ + with a map a map _u[′]_ +[.][Then,][(] _[u][′]_ + _[, u][−]_[)][gives][rise][to] _n_ (Γ+ _,_ Γ _−_ ) unframed broken maps, and each of these has _µe_ framings. Theorem 3.17 follows by applying the above reasoning inductively, cutting one edge at a time. The 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

33 

product of the factors _n_ (Γ+ _,_ Γ _−_ ) from all the steps is equal to _n_ (Γ), which is the number of ways of distributing _d_ markings onto vertices _v ∈_ Vert(Γ) containing _d_ ( _v_ ) markings; two distributions are considered the same if they are related by an automorphism of Γ. □ _Example_ 3.18 _._ We consider the polyhedral decomposition in Figure 12, and one of the Maslov-index-two disks contributing to the potential, which is an rigid element of the moduli space of broken maps with a point constraint on the Lagrangian. The constraints are distributed as shown in Figure 13: the moduli space for that type is a product of moduli spaces on the pieces with an additional constraint at one of the cylindrical ends on the piece containing the Lagrangian, and another additional constraint on moduli space for the piece meeting the toric boundary. 

**==> picture [185 x 93] intentionally omitted <==**

Figure 13. The moduli space as a product of moduli spaces for its pieces 

The distribution of constraints give orientations on the edges of the tropical graph. In the statement of Theorem 3.17, for an edge _e_ = ( _v_ + _, v−_ ), if an end-point _v_ + has a point constraint and the end-point _v−_ has an trivial constraint, we orient the edge _e_ from _v−_ to _v_ +. This system of orientations on the tropical graph is called the _constraint orientation_ and it satisfies the following property. 

**Lemma 3.19.** _Let_ Γ _be the tropical graph of a rigid disk. At any vertex v of_ Γ _with P_ ( _v_ ) _∈P/ ∂, there is exactly one outgoing edge e ∈_ Edge(Γ) _with respect to the constraint orientation._ 

_Proof._ The result follows from index considerations. The Maslov index of a disk or sphere is equal to twice the number of intersections with toric divisors, so for a rigid disk, exactly one of these intersections is unconstrained. □ 

3.5. **Intersecting polyhedral decompositions.** Two transversely intersecting polyhedral decompositions combine to give a new polyhedral decomposition. The combined decomposition has a family of dual complexes. We outline this construction from [46, Example 3.30]: 

- **Definition 3.20.** (a) A pair of polyhedral decompositions _P_ 0, _P_ 1 of t _[∨]_ intersect _transversally_ if any pair of polytopes _P_ 0 _∈P_ 0, _P_ 1 _∈P_ 1 intersect transversely. 

   - (b) For a transversally intersecting pair, we define a _combined_ polyhedral decomposition 

**==> picture [253 x 12] intentionally omitted <==**

S. VENUGOPALAN AND C. WOODWARD 

34 

- (c) For any minimal dimensional polytope _P_ 01 and a constant _ρ >_ 0, there is a family of dual polytopes ( _P_ 01 _[∨]_[)] _[ρ]_[:=] _[ P]_ 0 _[ ∨][×][ δP][ ∨]_ 1[,][which][glue][(as][in][(][2][))][to][yield] a family of dual complexes 

**==> picture [249 x 15] intentionally omitted <==**

- (d) By assumption, each _b ∈ B_[foc] is contained in the interior of a polytope _P ∈P_ of maximal dimension, and we denote by _b[∨]_ := _Pb[∨]_[the][corresponding] _[dual] focus-focus singularity_ in _B[∨]_ . 

_Example_ 3.21 _._ The simplest instance of this construction is a multiple cut consisting of two single cuts shown in Figure 14. The dual complex is a rectangle, and we obtain a family of possible complexes by varying the ratio of the sides of the rectangle. 

**==> picture [352 x 96] intentionally omitted <==**

**----- Start of picture text -----**<br>
P 1 ∈P 1<br>Bρ [∨] Γ<br>P 0 [∨] P 0 ∈P 0 ρP 0 [∨] ρP 0 [∨]<br>P 1 [∨] P 1 [∨]<br>P 1 [∨]<br>**----- End of picture text -----**<br>


Figure 14. The combination _P_ of the polyhedral decompositions _P_ 0, _P_ 1 has a family of dual complexes _{Bρ[∨][}][ρ]_[.][The][tropical][graph][Γ] is not realizable in _Bρ[∨]_[if] _[ρ]_[is][large][enough.] 

If the parameter _ρ_ is large enough, we may view the combined multiple cut _P_ as performing the cut _P_ 0 followed by _P_ 1. This is equivalent to saying that any tropical graph Γ in _Bρ[∨]_[can][be][transformed][to][a][tropical][graph][in] _[B]_ 0 _[∨]_[by][collapsing][all][edges] whose directions have a non-zero in the t _P_ 1-direction for any _P_ 1 _∈P_ 1. The edges left uncollapsed are edges in _B_ 0 _[∨]_[and][are][defined][as][follows.] 

**Definition 3.22.** Let _P_ := _P_ 0 _∩P_ 1 be the combination of two transversely intersecting multiple cuts _P_ 0 and _P_ 1. An edge _e_ of a tropical graph Γ in _Bρ[∨]_[(from][(][21][))] is a _B_ 0 _[∨][-edge]_[if] _[P]_[(] _[e]_[) =] _[ P]_[0] _[ ∩][P]_[1][,] _[P][i][∈P][i]_[,][and] _[T]_[ (] _[e]_[) = (] _[T]_[0] _[,]_[ 0)] _[ ∈]_[t] _[P]_ 0 _[×]_[ t] _[P]_ 1[.] 

Note that the condition in the Definition is automatically satisfied in the case when _P_ 1 is top-dimensional and so, t _P_ 1 = _{_ 0 _}_ . 

**Proposition 3.23.** _Given an area bound E_ 0 _, there exists ρ_ 0 _for which the following holds. For a map type_ Γ _with area ≤ E_ 0 _whose tropical graph_ Γ _is realizable in Bρ[∨] (from_ (21) _) for some ρ ≥ ρ_ 0 _,_ 

- _(a)_ Γ _is realizable in Bρ[∨][for][all][ρ][ ≥][ρ]_[0] _[,][and]_ 

- _(b) there is a tropical graph_ Γ0 _in B_ 0 _[∨][and][an][edge][collapse][morphism]_[Γ] _[→]_[Γ][0] _that collapses all edges that are not B_ 0 _[∨][-edges.]_ 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

35 

_Example_ 3.24 _._ The graph Γ in Figure 14 does not have any _B_ 0 _[∨]_[edge][in][the][path] from _v_ 0 to _v_ 1. Since _v_ 0 and _v_ 1 lie in different polytopes of _P_ 0, the proposition implies that the graph is not realizable in _Bρ[∨]_[for][large][enough] _[ρ]_[.][This][conclusion][is][easy][to] deduce from the figure. 

_Proof of Proposition 3.23._ We claim that there are a finite number of tropical graphs Γ corresponding to broken maps _u_ satisfying a given area bound _A_ ( _u_ ) _≤ E_ 0, and that are realizable in some _Bρ[∨]_[.][This][claim][follows][from][the][proof][of][Proposition][T-][8.41][,] which bounds the number of tropical graphs in a fixed dual complex. Indeed, the proof of Proposition T-8.41 applies even if the parameter _ρ_ varies, because the proof does not rely on realizations of tropical graphs. The proof of part (a) now follows, because the set of realizations of a given tropical graph Γ is convex. Therefore the set of _ρ_ for which Γ is representable in _Bρ[∨]_[is][an][interval.] 

For part (b), consider a tropical graph Γ that is representable in _Bρ[∨]_[for] _[ρ][≥] ρ_ 0. Consider the continuous family of complexes _{ ρ_[1] _[B] ρ[∨][}][ρ]_[which][limits][to] _[B]_ 0 _[∨]_[.][By] assumption, there is a sequence of realizations 

**==> picture [77 x 26] intentionally omitted <==**

By compactness, after passing to a subsequence, we may assume that _ιν_ converges to a limit _ι∞_ : Γ _→ B_ 0 _[∨]_[.][In][the][limit] _[ι][∞]_[,][any][edge] _[e]_[of][Γ][that][is][not][a] _[B]_ 0 _[∨]_[-edge][is] mapped to a point. Indeed, suppose that _P_ ( _e_ ) = _P_ 0 _∩ P_ 1, _P_ 0 _∈P_ 0, _P_ 1 _∈P_ 1 so that t _P_ ( _e_ ) = t _P_ 0 _×_ t _P_ 1, and the t _P_ 1-component of _ιν_ ( _e_ ) is non-zero. The length of _ιν_ ( _e_ ) is bounded by _ρcν_[for][a][uniform][constant] _[c]_[.][Therefore,] 

**==> picture [83 x 16] intentionally omitted <==**

Thus, if Γ0 is defined by collapsing all the _B_ 0 _[∨]_[-edges][in][Γ,] _[ι][∞]_[is][a][realization][of][Γ][0] in _B_ 0 _[∨]_[.] □ 

## 4. Curves in the elementary pieces 

By an _elementary piece_ , we mean a piece in the broken symplectic manifold that is either a toric manifold possibly containing the Lagrangian torus fiber, or is an almost toric manifold with a collection of focus-focus singularities along the same branch cut. We will show in Section 5 that almost toric del Pezzos possess polyhedral decompositions with the following property: For any broken disk contributing to the potential the tropical graph has “collisions in the interior” in the sense of Definition 1.2. In the case of holomorphic spheres in toric varieties, the sphere with two intersections with the boundary divisors is called a _holomorphic cylinder_ , and the one with three intersections is called a _holomorphic pair of pants_ . 

The disk potential is a sum over the set of rigid tropical graphs, and each summand is a product of the curve counts corresponding to each of the vertices. We precisely define the weighted curve count _m_ ( _v_ ) on each vertex. On a broken map type Γ we apply the distribution of constraints result (Theorem 3.17) so that the moduli space is a (weighted) product of the moduli spaces of relative maps _M_ Γ( _v_ )( _XP_ ( _V_ ) _, LP_ ( _v_ ) _, Y_ ~~_v_~~[).] 

S. VENUGOPALAN AND C. WOODWARD 

36 

**Definition 4.1.** For any vertex _v ∈_ Vert(Γ), define, for some particular perturbation data, the _count of unframed relative maps_ as 

**==> picture [240 x 33] intentionally omitted <==**

where Hol _L_ ([ _∂uv_ ]) is from (9) and is equal to 1 if _u_ is a sphere. 

We adopt the convention of absorbing the framing symmetry factor of an edge _e_ into the vertex _v_ where there is a point constraint on _uv_ at the edge _e_ , and define the _count of framed relative maps_ 

**==> picture [273 x 34] intentionally omitted <==**

where the product is over edges _e_ incident on _v_ , and for which _Yv,e_ is a point constraint. 

_Remark_ 4.2 _._ Under a primitivity assumption, the counts _m_ ( _v_ ) are independent of the choice of perturbation by the argument of Proposition 3.14. 

**Proposition 4.3.** _The disk potential of a monotone Lagrangian L compatible with the polyhedral decomposition P above_ 

**==> picture [145 x 25] intentionally omitted <==**

_where the sum is over all rigid map types_ Γ _._ 

_Proof._ By monotonicity, the area of any rigid broken disk contributing to the potential is 1, and therefore the exponent of _q_ is 1. The statement of the Proposition is immediate from Theorem 3.17. □ 

Our goal is now to compute the multiplicities of the vertices. In theory, all of the multiplicities already appear in the literature, but in various foundational schemes. We give proofs for each case, since none are particularly long. 

4.1. **Holomorphic spheres in toric varieties.** We first count holomorphic spheres in toric varieties that intersect boundary divisors at isolated points. The holomorphic spheres we consider form a component of a broken map, and are therefore modelled on a graph Γ _v_ single vertex _v_ and a set Edgerel(Γ _v_ ) of relative edges. 

_Notation_ 4.4 _._ In the notation of Section 3.2, such maps are defined on punctured domain curves 

**==> picture [215 x 15] intentionally omitted <==**

We suppose that _P_ ( _v_ ) is a polytope not containing any focus-focus singularity, or the image of the Lagrangian. If _P_ ( _v_ ) does not intersect _∂_ ∆then _XP_ ( _v_ ) _≃_ (C _[×]_ ) _[n]_ ; otherwise it additionally contains a divisor at infinity corresponding to _XP_ ( _v_ ) _∩_ Φ _[−]_[1] ( _∂_ ∆). When _uv_ is viewed as a map to the toric compactification _X P_ ( _v_ ), _u_ has 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

37 

removable singularities at punctures. Equivalently, in the neighborhood of a relative marking _ze_ , the map _u_ is asymptotically close at the puncture to a trivial cylinder 

**==> picture [195 x 14] intentionally omitted <==**

for some _ci ∈_ C _[×]_ , where 

**==> picture [155 x 12] intentionally omitted <==**

is the _direction_ of the relative edge _e_ . 

The directions _{T_ ( _e_ ) _}e_ are part of the data of the map type Γ of the map _u_ , and they satisfy a _balancing condition_ as follows: 

**Lemma 4.5.** _Let uv_ : P[1] _\{ze}e →_ (C _[×]_ ) _[n] be a relative map with a single component in a toric piece XP_ ( _v_ ) _≃_ (C _[×]_ ) _[n] that does not intersect the boundary divisor of X. The edge directions Te ∈_ Z _[n] at the relative markings ze satisfy_ 

(23) 

**==> picture [64 x 24] intentionally omitted <==**

_Proof._ The statement of the lemma is a computation with fundamental groups. Let _γe_ be a loop around _ze_ . The product of the loops[�] _e_[[] _[γ][e]_[]][is][the][identity][in] _π_ 1(P[1] _\{ze}e_ ), and therefore, 

**==> picture [163 x 34] intentionally omitted <==**

Since 

**==> picture [136 x 13] intentionally omitted <==**

the balancing condition follows. □ 

_Remark_ 4.6 _._ We also consider holomorphic cylinders intersecting the boundary. Such a map lies on a piece _XP_ that intersects the boundary divisor Φ _[−]_[1] ( _∂_ ∆) of _X_ , has a single relative marking _ze_ of slope _T_ ( _e_ ) and an intersection with the divisor Φ _[−]_[1] ( _∂_ ∆) _∩XP_ . The argument in the proof of the balancing condition implies that _T_ ( _e_ ) is the outward normal vector of Φ _[−]_[1] ( _∂_ ∆) _∩XP_ . 

**Proposition 4.7.** _Let XP_ ( _v_ ) _be a projective toric variety with_ dim( _X_ ) = 4 _. Let_ Γ _be a relative map type with a single vertex v with a collection of constraints Y that are one of the following:_ 

- _(a)_ (Holomorphic cylinder in the interior) _The vertex v has two relative edges e, e[′] with slopes T_ ( _e_ ) _, −T_ ( _e_ ) _, XP_ ( _v_ ) _does not intersect the boundary of_ Φ _[−]_[1] ( _∂_ ∆) _, and Y consists of a point constraint at the relative marking ze, or_ 

- _(b)_ (Holomorphic cylinder intersecting the boundary) _the vertex v has a relative edge of primitive slope T_ ( _e_ ) _, and a single intersection with a boundary toric divisor XP_ ( _v_ ) _∩_ Φ _[−]_[1] ( _∂_ ∆) _that is not a relative divisor, and Y consists of a point constraint at the relative marking ze, or_ 

- _(c)_ (Holomorphic pair of pants in the interior) _the vertex v has three relative markings z_ 1 _, z_ 2 _, z_ 3 _, whose slopes T_ 1 _, T_ 2 _, T_ 3 _sum to zero, XP_ ( _v_ ) _does not intersect the boundary of_ Φ _[−]_[1] ( _∂_ ∆) _, and Y consists of point constraints at two of the markings z_ 1 _, z_ 2 _._ 

S. VENUGOPALAN AND C. WOODWARD 

38 

_In all the cases, the moduli spaces are zero-dimensional, and_ 

**==> picture [339 x 34] intentionally omitted <==**

_Proof._ For a toric variety equipped with the standard alost complex structure, the moduli spaces of spheres intersecting boundary divisors at isolated points is transversely cut out, and the evaluation map at a single marking is submersive. By a similar proof, the evaluation maps at two markings with non-parallel slopes is also submersive. 

Suppose that the almost complex structure is standard (and domain-independent). For a holomorphic cylinder with _|Te|_ = _d_ , the map _uv_ is a _d_ -fold cover of its image. ( _v_ ) On any such curve, markings can be labelled in _[d] d_ distinct ways, and therefore, every curve contributes _d_[1][to] _[m]_[(] _[v]_[)][unfr][.][Thus] 

**==> picture [130 x 13] intentionally omitted <==**

The curve count for holomorphic pairs of pants is similar to the counts in Mikhalkin [34, Theorem 1] and Nishinou-Siebert [35, Proposition 8.8]. We outline the proof in Lemma 4.4 in Venugopalan-Woodward [46]. For a map type Γ of holomorphic pair of pants with constraints _Y_ on two of the markings, any two maps in the moduli space _M_ Γ( _X, Y_ ) are related by an element _g_ of the tropical symmetry group _T_ trop(Γ) _≃_ (C _[×]_ )[2] that does not alter the projected evaluation at the relative markings, A tropical symmetry _g ∈ T_ trop(Γ) does not alter the projected evaluations at _z_ 1, _z_ 2 exactly if _g ∈ TTj ,_ C for _j_ = 1 _,_ 2. That is, there exist _zj ∈_ C _[×]_ , _j_ = 1 _,_ 2 such that 

(25) _g_ = _z_ 1 _[T]_[1][=] _[ z]_ 2 _[T]_[2] _[.]_ By the calculation in the proof of [46, Lemma 4.4], (25) has det( _T_ 1 _, T_ 2) solutions for ( _g, z_ 1 _, z_ 2). Given a solution ( _g, z_ 1 _, z_ 2), the pairi ( _g, θ_ 1 _z_ 1 _, θ_ 2 _z_ 2) is also a solution where _θj[|T][j][|]_ = 1 for _j_ = 1 _,_ 2, and so, there are _[|]_[ det] _|T_[(] 1 _[T] ||T_[1] _[,]_ 2 _[T] |_[2][)] _[|]_ distinct values of _g ∈ TT_ 1 _,_ C _∩ TT_ 2 _,_ C, Therefore, 

**==> picture [314 x 38] intentionally omitted <==**

4.2. **Disks in toric varieties.** Next we deal with pieces of the degeneration containing the Lagrangian. Let _X_ be a compact toric variety and _L ⊂ X_ a Lagrangian torus orbit. Let _Y_ = _{y} ⊂ L_ be a generic point constraint. 

**Lemma 4.8.** _Suppose L is a moment fiber in a toric manifold X equipped with its standard complex structure, and Di ⊂ X be a boundary divisor. The number of rigid disks u_ : _C → X with boundary in L passing through a generic point Y_ = _{Y }, Y_ = _{y ∈ L} and with a single intersection with Di is m_ ( _X, Y_ ) = 1 _._ 

_Proof._ The proof is similar to that for the statements about spheres in the previous subsection, but now using the description of holomorphic disks as Blaschke products as described in Cho-Oh [9]. Suppose that _X_ is given as the git quotient of a vector 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

39 

space _X_[˜] = C _[k]_ by the linear action of a torus _G ⊂_ (C _[×]_ ) _[k]_ . Any disk in _X_ with boundary in _L_ lifts to a disk in _X_[˜] with boundary in some torus _L_[˜] = ( _S_[1] ) _[k]_ mapping to _L_ under the quotient map. Such a holomorphic disk is given by a product 

**==> picture [270 x 43] intentionally omitted <==**

By [9, Theorem 5.1], the Maslov index of such a product is the sum 

**==> picture [71 x 34] intentionally omitted <==**

The only rigid such disks meeting _Di_ are those Blaschke products with _di_ = 1. This justifies (e). □ 

This completes the proof of Theorem 1.3. 

**==> picture [34 x 32] intentionally omitted <==**

Figure 15. Holomorphic curves in the toric local models 

**Proposition 4.9.** _Suppose that X is a compact symplectic manifold of arbitrary dimension, L is contained in a piece XP_ 0 _of X which is a toric variety, that is, P_ 0 _∈P is a polytope of maximal dimension and_ Φ( _L_ ) _is contained in P_ 0 _, and L is a toric moment fiber. Then the disk potential WL has no constant term, that is, the coefficient of y_[0] _in W vanishes._ 

_Proof._ The proof of the statement of the Proposition follows from the non-existence of Blaschke products with trivial boundary class. That is, let _u_ : _C → XP_ 0 be a holomorphic in the toric variety _XP_ 0 with boundary in a Lagrangian torus fiber. By the classification in Cho-Oh [9], the boundary class [ _u_ ( _∂C_ )] _∈ H_ 1( _L_ ) is nontrivial. □ 

4.3. **Spheres meeting the focus-focus singularities.** In this section we give the Bryan-Pandharipande formula from [4] for the holomorphic spheres in pieces containing the focus-focus singularities. In elementary polyhedral decompositions, the piece _XP_ containing a focus-focus singularity has moment polytope of the form shown in Figure 16 or Figure 17. The compactification _X P_ obtained by adding boundary divisors corresponding to the facets of Φ( _XP_ ) is a singular fibration 

(27) _f_ : _X P →_ P[1] _._ 

The fibers _f[−]_[1] (0) and _f[−]_[1] ( _∞_ ) are orbifold spheres. For a focus-focus singularity _x ∈XP_ , the fiber _f[−]_[1] ( _f_ ( _x_ )) is a nodal sphere with a node at _x_ . Any other fiber 

S. VENUGOPALAN AND C. WOODWARD 

40 

of _f_ is a P[1] . We denote by _S_ 0 and _S∞_ the sections of _f_ that are inverse images of boundary divisors of _X P_ . A special case of such a cut space occurs when _f[−]_[1] (0) and _f[−]_[1] ( _∞_ ) are smooth spheres, and one of the sections _S_ 0 is a ( _−_ 1)-sphere. In this case _X P_ is isomorphic to a point blow-up of P[1] _×_ P[1] . 

**==> picture [193 x 81] intentionally omitted <==**

**----- Start of picture text -----**<br>
S 0<br>( m, n )<br>f [−] [1] (0) u<br>f [−] [1] ( ∞ )<br>( m 1 , n 1) ( m, n − m )<br>S∞<br>**----- End of picture text -----**<br>


**==> picture [95 x 63] intentionally omitted <==**

Figure 16. Left: Moment image of a cut space _XP_ containing a focus-focus singularity, and a holomorphic curve _u_ in _XP_ . Right: The particular case when _X P_ = Bl(P[1] _×_ P[1] ), and 1 = _m_ = _−m_ 1, _n − m_ = _−n_ 1. 

**Lemma 4.10.** _Let u_ : P[1] _→ X P be a holomorphic map with a single intersection point u_[1] ( _X P −XP_ ) _with the boundary divisor, given by the inverse images of the four facets in Figure 16. Then the image of u lies on one of the nodal fibers of the map f (in_ (27) _)._ 

_Proof._ The proof is a computation involving intersection numbers with the fibers. The projection _f ◦ u_ : P[1] _→_ P[1] is holomorphic and intersects at most one of 0 _, ∞∈_ P[1] . Therefore, _f ◦ u_ is constant, and the image of _u_ lies in a fiber of _f_ . Since regular fibers of _f_ intersect two of the boundary divisors of _X P_ , the only possibility is that _u_ maps to one of the spheres in a nodal fiber. □ 

**==> picture [237 x 80] intentionally omitted <==**

**----- Start of picture text -----**<br>
S 0<br>f [−] [1] (0) u ( m, n )<br>f [−] [1] ( ∞ )<br>( m 1 , n 1) k ( m, n − mk )<br>S∞<br>**----- End of picture text -----**<br>


Figure 17. Moment image of a cut space _XP_ with multiple focus-focus singularities whose shear matrices have the same eigendirection, and a holomorphic curve _u_ in _XP_ . 

In the rest of the section, we count the number of holomorphic spheres in a focusfocus piece that have a single relative marking, or in other words, the sphere has a single intersection with boundary divisors. For simplicity of notation, we assume that _XP_ has a single focus-focus singularity, but the proof in the general case is similar. Denote by 

_β_ 0 resp. _β∞ ∈ H_ 2( _X P_ ) 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

41 

the homology class of the sphere in the nodal fiber that meets the section _S_ 0 resp. _S∞_ . We consider one of these, say _β_ 0, since the other can be analyzed in a similar way. For any positive integer _d_ , denote by 

**==> picture [90 x 12] intentionally omitted <==**

the count of relative spheres in _X P_ in the class d _β_ 0 that have a single intersection (of maximum multiplicity) with the divisor _S_ 0. The constraint _Y_ has a single element _S_ 0, indicating that the evaluation map at the relative marking is unconstrained. 

We first consider the special case when the cut space is the point blow-up of a product of projective lines and prove the following Proposition. Later, as part of the proof of Theorem 1.3 (part Definition 1.4 (d)) we show that the case of general _X P_ reduces to this special case. 

**Proposition 4.11.** (Bryan-Pandharipande formula) _Let X be the point blow-up of_ P[1] _×_ P[1] _with exceptional divisor E intersecting the divisor Y . The count m_ ( _X, Y_ ) _of d-fold covers of E meeting Y with a single intersection of maximal tangency is_ 

**==> picture [96 x 25] intentionally omitted <==**

## _as in Definition 1.4_ (d) _._ 

Proposition 4.11 would be a special case of localization computation in BryanPandharipande [4, (13)], except that we are using a different foundational scheme for which virtual localization is not easily available. For the sake of completeness, we give a different argument. Note that the relevance of the Bryan-Pandharipande formula for disk counts near the focus-focus singularities appears also in Lin [28] and Gr¨afnitz-Ruddat-Zaslow [19] 

**Definition 4.12.** For any _d ∈_ N, define for short a relative Gromov-Witten invariant 

_nd_ := # _{u_ : P[1] _→ E_ of class _d_ [ _E_ ] with a tangency of order _d_ with _Y } ∈_ Q 

where # denotes the signed, weighted count described in [46]. 

The results of [46] imply that the number _nd_ is independent of the choice of domaindependent almost complex structure, using a Donaldson hypersurface to stabilize domains. Proposition 4.11 claims that 

**==> picture [84 x 13] intentionally omitted <==**

The proof uses the following recursive relation, for which we introduce some terminology. 

**Definition 4.13.** A _partition_ Θ of a positive integer _d_ is a decomposition 

**==> picture [81 x 11] intentionally omitted <==**

for some _k ≥_ 1, positive integers _di_ that are non-decreasing in _i_ . Set 

**==> picture [115 x 13] intentionally omitted <==**

S. VENUGOPALAN AND C. WOODWARD 

42 

**Lemma 4.14.** _The curve counts {nd}d ∈_ Q _of_ (4.12) _satisfy a recursive relation_ 

**==> picture [271 x 32] intentionally omitted <==**

_for all d >_ 1 _._ 

_Proof._ The two sides of the expression in (28) can be realized as curve counts for different almost complex structures. After perturbation, the curves counted by _md_ lie in a small neighborhood of _E_ . So, we may assume that _X_ is the blow-up of P[2] at a point _p_ and _Y_ is the strict transform of a line through _p_ . Denote the homology classes of _E, Y ⊂ X_ by 

**==> picture [142 x 12] intentionally omitted <==**

Given _d_ + 1 generic points _x_ = ( _x_ 0 _, . . . , xd_ ) in _X_ , let 

**==> picture [81 x 12] intentionally omitted <==**

be the number of curves _u_ : P[1] _→ X_ of class _de_ + _f ∈ H_ 2( _X_ ) passing through _x_ 0 _, . . . , xd_ . We claim that 

**==> picture [80 x 11] intentionally omitted <==**

if _d >_ 1. Indeed, we may perform the curve count using an almost complex structure _J_ for which _E_ is _J_ -holomorphic. Since 

**==> picture [112 x 12] intentionally omitted <==**

any _J_ -holomorphic curve with class _de_ + _f_ necessarily lies in _E_ , which is impossible. To obtain the expression as a sum over partitions in (28), we perform the curve count in a carefully chosen broken manifold. We cut _X_ into two pieces 

**==> picture [147 x 14] intentionally omitted <==**

in such a way that all the point constraints _x_ 0 _, . . . , xd_ lie in _X_ +. The exceptional divisor class _e_ splits into classes _e± ∈ H_ 2( _X±_ ). Any broken curve 

**==> picture [176 x 12] intentionally omitted <==**

counted by _N_ ( _de_ + _f, x_ ) belongs to the class _f_ + _de_ + in _X_ + and _de−_ in _X−_ . The curve component _C−_ may be disconnected, and the class of each connected component of _u−_ is a multiple of _e−_ . Thus, _u−_ determines a partition Θ of _d_ . The expression inside the summation sign in (28) is the count of the curves _u−_ with no constraint on the relative divisor _Y_ , weighted by intersection multiplicities _di_ at the relative divisor _Y_ The denominator accounts for permutations of markings arising from the stabilizing divisor. To finish the proof, it remains to count the number of possibilities for the second component _u_ + for a fixed first component _u_ +. The curve _u_ + has degree (1 _, d_ ) with _d_ + 1 non-relative point constraints, and point constraints of order _d_ 1 _, . . . , dk_ along the relative divisor. An explicit calculation as Section 4.1 shows that there is exactly one curve satisfying these constraints, and (28) follows. □ 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

43 

_Proof of Proposition 4.11._ There is a unique sequence _{nd}d∈_ N that satisfies _n_ 1 = 1 and the recursive relation (28) for all _d >_ 1. Therefore, it is enough to show that _nd_ = ( _−_ 1) _[d]_[+1] _/d_[2] satisfies (28). Denote _md_ := _dnd_ . Observe that the right-hand-side of (28) is equal to the coefficient of _x[d]_ in the product 

**==> picture [316 x 28] intentionally omitted <==**

which is equal to 

(29) _e_[(] _[m]_[1] _[x]_[+] _[m]_[2] _[x]_[2][+] _[...]_[ )] _._ The substitution _md_ = ( _−_ 1) _[d]_[+1] _/d_ reduces the expression (29) to 

**==> picture [78 x 13] intentionally omitted <==**

Therefore, the expression (28) vanishes for _d >_ 1, proving the Proposition. 

**==> picture [10 x 8] intentionally omitted <==**

_Proof of Theorem 1.3, part Definition 1.4_ (d) _._ The computation reduces to the BryanPandharipande formula as follows. Let _XP_ ( _v_ ) be a piece of the broken manifold containing focus-focus singularities. By assumption _XP_ ( _v_ ) does not contain the Lagrangian, and the moment image of _XP_ ( _v_ ) is as in Figure 16. We are considering tropical graphs with a single vertex _v_ mapping to _P_ ( _v_ ); the corresponding component of the broken map has a single intersection with the divisor at infinity. The space _X P_ ( _v_ ) is a singular fibration over P[1] (see (27)). By Lemma 4.10, the map _uv_ maps to a sphere _E_ 0 in a nodal fiber. For a suitably chosen symplectic form on _X_ := Bl _p_ (P[1] _×_ P[1] ), a neighborhood _U_ of the exceptional divisor _E ⊂ X_ is symplectomorphic to a neighborhood _U_ 0 of _E_ 0 _⊂ X P_ ( _v_ ). Via a deformation of the symplectic form on _X P_ ( _v_ ), we may assume the symplectic area of the spheres _E_ 0 (and _E_ ) are sufficiently small. By Gromov’s monotonicity theorem, we conclude that holomorphic spheres of area _ω_ ( _E_ 0) that intersect _E_ 0 _⊂ X_ are contained in _U_ 0. Therefore, the count is 

**==> picture [398 x 29] intentionally omitted <==**

4.4. **Computing multiplicities via desingularization.** So far we have proved the counting formula in Theorem 1.3 under the assumption that the tropical graphs contributing to the sum do not have valence higher than three. In this Section, we extend the result to the case that higher valence vertices occur. The idea is that the relative curve counts are invariant under perturbations of the positions of the edges of the tropical graph, so that we may assume that all of the vertices are trivalent. This is a special case of the splitting argument in our previous paper [47], by splitting the edge matching condition at all incident edges of higher valent vertices. The resulting split graphs only contain trivalent graphs and can be counted in the standard way. 

As in the Introduction, we define 

**==> picture [123 x 30] intentionally omitted <==**

44 

## S. VENUGOPALAN AND C. WOODWARD 

where the sum ranges over all the perturbations Γ _v,±_ of Γ _v_ . 

**==> picture [355 x 259] intentionally omitted <==**

**----- Start of picture text -----**<br>
XP ( v )<br>XPb<br>b b<br>P XPp XPb b XPp<br>p p P 1 P 1 p<br>B [∨]<br>ρ ρ<br>P ( v ) Pp Pb Pb Pp<br>B [∨] × ρB 1 [∨] B [∨] × ρB 1 [∨]<br>Γ v e 1 Γ [pert] v, + e 1 Γ [pert] v,− e 1 v 1 ∼ ev 11<br>v v 1 v 0 v 0<br>e 0 e 0<br>e 0<br>**----- End of picture text -----**<br>


Figure 18. Perturbations of Γ _v_ . In each case, the figure shows the space and the multiple cut, the dual complex, and the tropical graph. 

## **Proposition 4.15.** _In the above setting, m_ ( _v_ ) = _m_[pert] ( _v_ ) _._ 

_Proof._ To prove the Proposition, we recall the notion of _splitting the matching condition_ from our earlier work [47]. The splitting process produces a version of a broken map, called a _split map_ in which there is no matching condition on a subset of tropical edges, called _split edges_ . Defining a split map requires a choice of a non-zero vector, called the _cone direction ηe ∈_ t _/⟨T_ ( _e_ ) _⟩_ at each of split edge. A _split map_ with a single split edge _e_ = ( _v_ + _, v−_ ) and a cone direction _ηe_ is defined as a broken map _u_ = ( _uv_ ) except that the matching condition at _e_ is not necessarily satisfied, and instead the tropical graph Γ must satisfy a version of the Fulton-Sturmfels cone condition: There exists _ϵ >_ 0 such that 

Disc(Γ) = [0[˜] _, ϵ_ ) _η,_ 

## where the _discrepancy cone_ 

**==> picture [224 x 16] intentionally omitted <==**

and _T_ ˜Γ ranges over all vertex positions for the graph Γ.[˜] The cone condition implies that the tropical graph Γ has one degree of freedom and[˜] _T_ trop(Γ)[˜] _≃_ C _[×]_ . The FultonSturmfels condition appeared in their study of the K¨unneth decomposition of the diagonal in toric varieties. 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

45 

Splitting an edge has the effect of dropping the matching condition at the node, and increasing the dimension of the tropical symmetry group by 2. In the fourdimensional case, suppose that cutting an edge _e_ splits a rigid tropical graph Γ into Γ+ and Γ _−_ , and the matching condition is a constraint on _M_ Γ+( _X_ ) (as in Theorem 3.17). In the split tropical graph Γ[˜] obtained by splitting the edge _e_ , the tropical symmetry group _T_ trop(Γ[˜] +) is C _[×]_ , and _T_ trop(Γ[˜] _−_ ) = Id. 

The cone condition in the case that there is more than one split edge can be described as follows. Suppose that there are _n_ split edges ordered as _e_ 1 _, . . . , en_ with deformation directions _ηi ∈_ t _/⟨T_ ( _ei_ ) _⟩_ . The set of discrepancies is a cone for each of the split edges, with the discrepancy being much larger for _ei_ compared to _ej_ whenever _i < j_ . Specifically, the cone condition states that there are constants _ϵ_ 1 _, . . . , ϵn >_ 0 such that the set of discrepancies 

**==> picture [271 x 16] intentionally omitted <==**

at the split edges is 

**==> picture [147 x 34] intentionally omitted <==**

where 

**==> picture [240 x 12] intentionally omitted <==**

The same moduli space of split maps is obtained if the splitting step is performed one split edge at a time in the order _e_ 1 _, . . . , en_ . 

Let Γ be rigid tropical graph contributing to the disk potential. We split the matching condition at the following collection of nodes: Consider a spherical vertex _v ∈_ Vert (Γ) with valence more than three. Choose an ordering _e_ 1 _, . . . , ek_ of incoming edges at _v_ . We may assume that _ek−_ 1 and _ek_ are not parallel. We split the edges _e_ 1 _, . . . , ek−_ 2 in that order. We carry out such splitting at all higher valent spherical vertices, in any order. Given a rigid tropical graph Γ, a split tropical graph ˜Γ _−→[κ]_ Γ is uniquely determined by a Γ[pert] _v_ at every higher valent vertex _v_ as follows: We obtain the perturbation Γ _v_[pert] by starting from a realization of the split graph Γ,[˜] and drawing the incoming (split) edges _e_ 1 _, . . . ek−_ 2 parallel to their original direction _T_ ( _ei_ ). See Figure 19 for an example. 

Proposition S-6.8 gives a cobordism between the moduli space of split maps and deformed maps with a large enough deformation parameter. □ 

Similarly, perturbations allows us to avoid the situation that vertices at focusfocus value have valence more than one, since for generic perturbations no edge of Γ passes through a focus-focus value _b[∨] ∈ B[∨] , b ∈ B_[foc] . 

4.5. **Counting by bunching.** We give a formula for counting curves where there are multiple edges emanating from a focus-focus singularity. A consequence is the binomial nature of the coefficients of the disk potential along edges of its Newton polytope. We start by defining a bunched version of tropical graphs. 

46 

**==> picture [169 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
S. VENUGOPALAN AND C. WOODWARD<br>**----- End of picture text -----**<br>


**==> picture [373 x 254] intentionally omitted <==**

**----- Start of picture text -----**<br>
(3 ,  2)<br>˜Γ<br>B [∨] Γ (3 ,  2)<br>(3 ,  2) Γ [pert] v<br>(3 ,  1)<br>Split e 1 (3 ,  0) e 2 e 1<br>v (3 ,  0)<br>(3 ,  0) e 2 e 1<br>e 1 , e 2<br>(0 ,  1) ,  (0 ,  1)<br>˜Γ<br>(3 ,  2)<br>Split e 1, e 2<br>(3 ,  0) e 1<br>e 2<br>**----- End of picture text -----**<br>


Figure 19. The vertex _v_ in the tropical graph Γ has two incoming edges in the direction (0 _,_ 1). Splitting _e_ 2 produces the split graph Γ.[˜] The corresponding perturbed graph at _v_ is Γ[pert] _v_ . 

**Definition 4.16.** (a) (Coincident edges) Given a map type Γ, a collection of edges _ei_ = ( _vi, w_ ) is _coincident_ if they share an end-point _w_ , the other endpoints of each of the edges lie on the same focus-focus singularity in _X_ , that is, for all _i_ , _vi_ is univalent, _P_ ( _vi_ ) = _P_ , and the map _uvi_ is incident on a focus-focus singularity _b ∈ XP_ . 

- (b) (Bunching of a tropical graph) Given a broken map type Γ, its _bunching_ Γ _b_ := _b_ (Γ) is given by replacing any set of coincident edges _e_ 1 _, . . . , ek_ with a single edge _e_ with _T_ ( _e_ ) :=[�] _i[T]_[ (] _[e][i]_[).][Thus][a] _[bunched][map][type]_[Γ] _[b]_[has][the] property that no two distinct edges are coincident. 

The _multiplicity of a bunched map type_ Γ _b_ is the sum of the multiplicity of all map types whose bunching it is. That is, 

**==> picture [115 x 27] intentionally omitted <==**

This ends the Definition. 

We describe a formula to compute multiplicity of bunched graphs under the assumption that at any vertex there is at most one bunched incident edge. 

**Definition 4.17.** The _bunched multiplicity mb_ ( _v_ ) _of the vertex v_ is equal to the ordinary multiplicity _m_ ( _v_ ) 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

47 

- (a) if there is no bunched edge incident on _v_ , and 

- (b) if _v_ has a bunched edge _e_ incident on it, _mb_ ( _v_ ) is defined as follows: Let Γ _b,e ⊂_ Γ _b_ be the subgraph consisting of vertices of _v_ , _w_ and the non-bunched incoming edge of _v_ , denoted by _f_ 0 and the outgoing edge of _v_ denoted by _f_ 1. Let Γ _e_ be any subgraph whose bunching is Γ _b,e_ . Thus, Γ _e_ consists of vertices _v_ , _w_ 1 _, . . . , wn_ where _e_ is the bunching of _ei_ = ( _wi, v_ ) and _wi_ is univalent. Then, we define 

**==> picture [20 x 11] intentionally omitted <==**

**==> picture [213 x 28] intentionally omitted <==**

The multiplicity _m_ (Γ _b_ ) can be written as a product of multiplicities over trivalent vertices 

**==> picture [116 x 28] intentionally omitted <==**

**Proposition 4.18.** _Let_ Γ _b be a bunched map type, and let v ∈_ Vert(Γ _b_ ) _be a trivalent vertex with an incident bunched edge e, another incoming edge f_ 0 _and an outgoing edge f_ 1 _. Then,_ 

**==> picture [69 x 27] intentionally omitted <==**

_where the direction T_ ( _e_ ) = _nµb, n ∈_ N _and µb ∈_ tZ _is primitive, and k_ := _|µb × T_ ( _f_ 0) _|._ 

_Proof._ First we write down the contribution to the multiplicity of a subgraph Γ _e_ consisting of all edges that are bunched into _e_ in Γ _b_ . That is, _b_ (Γ _e_ ) = Γ _e,b_ . An equivalence class[4] of a subgraph Γ _e_ whose bunching is Γ _e,b_ is determined by the number of occurrences _dν_ of the input _νµb_ for each _ν ∈_ N in the graph Γ _e_ . We apply the perturbation described in Definition 1.8 to the higher valent vertex _v_ in Γ _e_ to obtain a perturbed graph (Γ _e_ ) _v_[pert] where the vertex _v_ is split into trivalent vertices _v_ 1 _, . . . , vd_ , each with an incoming edge _ei_ = ( _wi, vi_ ), so that 

**==> picture [233 x 26] intentionally omitted <==**

Furthermore, the automorphism group of Γ _e_ has order 

**==> picture [97 x 25] intentionally omitted <==**

corresponding to permutations of edges _ei_ going to the focus-focus value with the same direction _T_ ( _ei_ ). Thus the contribution of the graph Γ _e_ to the sum _mb_ ( _v_ ) in (30) is 

**==> picture [270 x 33] intentionally omitted <==**

> 4The equivalence class in this context is given by permuting the set of edges which have the same multiplicity and which get bunched to _e_ . 

S. VENUGOPALAN AND C. WOODWARD 

48 

The sum of contributions of all subgraphs Γ _e_ is the coefficient of _x[n]_ in 

**==> picture [388 x 59] intentionally omitted <==**

Using the power series expansion of ln(1 + _x_ ) this is equal to 

_e[kx] e[−][kx]_[2] _[/]_[2] _e[kx]_[3] _[/]_[3] _· · ·_ = _e[k]_[ ln(1+] _[x]_[)] = (1 + _x_ ) _[k] . k_ The coefficient of _x[n]_ in the expression is � _n_ �. 

**==> picture [10 x 8] intentionally omitted <==**

**==> picture [299 x 63] intentionally omitted <==**

**----- Start of picture text -----**<br>
f 1 f 1 f 1<br>Γ [pert] v, + e b bv b e Γ [pert] v,−<br>−nµb ( k − n ) µb<br>f 0 f 0 f 0<br>**----- End of picture text -----**<br>


Figure 20. Bunchings of one-sided perturbations of a vertex at a singular point _b_ . 

_Remark_ 4.19 _._ Proposition 4.15 on the equality of counts of (+) and ( _−_ )-perturbations can alternately be proved by explicitly counting both sides via bunching. 

## 5. Tropical graphs of rigid disks 

In this Section we study special polyhedral decompositions for the almost toric manifolds of the type considered in Vianna [49], which we call standard decompositions, for which all of the multiplicities of vertices appearing in tropical graphs corresponding to Maslov-index-two disks are those described in Definition 1.4. Similar to Mikhalkin [34] and Bardwell-Evans et al [2], we have a holomorphic-to-tropical correspondence in this case which takes place in affine manifold diffeomorphic to the punctured plane (with number of punctures equal to the number of corners in the moment polytope) which we call the _dual affine manifold._ 

5.1. **Standard decompositions.** We begin by describing a standard polyhedral decomposition in the case of a base diagram where the focus-focus values are close to the boundary. 

**Proposition 5.1.** _Let X be a monotone almost toric four-manifold with moment map_ Φ : _X →_ t _[∨] ,_ Φ( _X_ ) _is a convex polytope, and a monotone Lagrangian torus L_ := Φ _[−]_[1] ( _ℓ_ ) _for ℓ ∈_ Φ( _X_ ) _. There is an elementary polyhedral decomposition (as in Definition 1.1) P and cutting datum for which all collisions in rigid tropical disks occur at interior generic points. Consequently, Theorem 1.3 applies to the triple_ ( _X,_ Φ _, P_ ) _._ 

The decomposition is constructed by taking the polytopes to be the intersections of polytopes in two polyhedral decompositions defined as follows. 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

49 

**Definition 5.2.** (Intersection of polyhedral decompositions) Two decompositions _P_ 0 and _P_ 1 of R _[n] intersect transversally_ if any pair _P_ 0 _∈P_ 0, _P_ 1 _∈P_ 1 intersects transversely. The _intersection P_ := _P_ 0 _∩P_ 1 is defined as the polyhedral decomposition, each of whose polytopes is an intersection _P_ 0 _∩ P_ 1 of _P_ 0 _∈P_ 0, _P_ 1 _∈P_ 1. 

**Definition 5.3.** For an almost toric manifold with no elliptic singularities, define a _standard decomposition_ to be a polyhedral decomposition of the form 

**==> picture [79 x 10] intentionally omitted <==**

where 

- (a) _P_ ann is an _annular cut_ , which is a single piece-wise linear path encircling _λ_ = Φ( _L_ ) and all the focus-focus values _B_[foc] and whose complement is the union of an inner ball and an outer annulus in Φ( _X_ ); 

- (b) and _P_ in is an _inner cut_ that separates each of the branch cuts _C_ 1 _, . . . , Ck_ and the Lagrangian projection _ℓ_ = Φ( _L_ ) from each other and is precisely described as follows: The one-dimensional part of _P_ in consists of a polygon _P_ 0 that bounds _ℓ_ , and semi-infinite rays _Pi, Pi[′][∈P]_[in][emanating][from][the] vertices, where _i_ is the index set for the vertices, pairs of which, _Pi_ , _Pi[′]_[,][are] parallel to branch cuts _Ci_ , and _Ci_ lies between _Pi_ , _Pi[′]_[.][See][Figure][21][for] example. 

In the case when the almost toric structure has elliptic singularities, a standard decomposition is defined similarly, with the only difference that the annular cut is a piece-wise linear path with self-crossings near elliptic singularities. Each elliptic singularity _x_ corresponds to a zero-dimensional polytope _Rx_ which a self-crossing of the annular cut. The collection of these zero-dimensional polytopes is denoted by 

_P_[ell] := _{Rx ∈P_ : _x_ is an elliptic singularity _}._ 

See Figure 24 for an example. This ends the Definition. 

_Notation_ 5.4 _._ The polytope _P_ 0 containing _ℓ_ has facets consisting of _long facets_ 

(32) _Fµ_ := _{⟨x, µ⟩_ = 1 _− ϵ}_ 

parallel to each facet of Φ( _X_ ) and _short facets_ 

(33) _Fν_ := _{⟨x, ν⟩_ = _cν}_ 

near the vertices of Φ( _X_ ), where the vector _ν ∈_ tZ lies outside Φ( _X_ ) _[∨]_ (Definition 5.5 below). The constants _ϵ_ , _cν_ are chosen so that for a small enough _ϵ_ 0 _>_ 0, _P_ 0 contains (1 _− ϵ_ 0)Φ( _X_ ), see Proposition 5.13 in the following section. 

**Definition 5.5.** (Dual of a polytope) Let ∆ _⊂_ t _[∨]_ be a polytope with rational edge directions. The _dual_ of ∆, denoted by ∆ _[∨] ⊂_ t, is the convex hull of the primitive normals _µ ∈_ tZ of the facets of ∆. 

The dual complexes of _P_ ann and _P_ in combine to give a one-parameter family of dual complexes 

(34) _{B[∨]_ ( _ρ_ ) _}ρ>_ 0 

for _P_ as in the following Lemma which is proved as part of [46, Example 3.30]. 

**==> picture [9 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
50<br>**----- End of picture text -----**<br>


**==> picture [79 x 91] intentionally omitted <==**

**==> picture [285 x 115] intentionally omitted <==**

**----- Start of picture text -----**<br>
S. VENUGOPALAN AND C. WOODWARD<br>Pann<br>Cut<br>Pin<br>**----- End of picture text -----**<br>


Figure 21. A standard polyhedral decomposition _P_ on Bl8 P[2] defined as the intersection of _P_ ann and _P_ in. 

**Lemma 5.6.** (A family of dual complexes) _Let P_ 0 _, P_ 1 _be polyhedral decompositions of_ R _[n] with dual complexes B_ 0 _[∨][and][B]_ 1 _[∨][respectively,][and][both][P]_[0] _[and][P]_[1] _[have][a] cutting datum. Then, the intersection P_ 0 _∩P_ 1 _has a family of dual complexes and cutting data parametrized by ρ >_ 0 _, where for any polytope P_ 01 _∈ P_ 0 _∩ P_ 1 _in P, where P_ 0 _∈P_ 0 _and P_ 1 _∈P_ 1 _, the dual polytope P_ 01 _[∨]_[(] _[ρ]_[)] _[is][the][product][P]_ 0 _[ ∨][×][ ρP][ ∨]_ 1 _[.]_ 

Via the following lemma, we show that for any _ρ >_ 0 the dual complex _B[∨]_ := _B[∨]_ ( _ρ_ ) is a singular integral affine manifold with corners whose singular set is 

**==> picture [303 x 14] intentionally omitted <==**

**Lemma 5.7.** (A singular affine manifold) _Let P be a polyhedral decomposition defined on a two-dimensional base diagram_ ∆ _⊂_ t _[∨] of an almost toric manifold, such that any focus-focus value is contained in a top-dimensional polytope P ∈P and edges intersect branch cuts transversally. Then, the interior of the dual complex B[∨] is a singular affine manifold modelled on_ t _with singularities at B[∨][,]_[foc] _._ 

_Proof._ Let _P_[br] _⊂P_ denote the subset of polytopes _P_ that intersect branch cuts. For any polytope _P ∈P\P_[br] , the dual _P[∨] ⊂_ t _P ⊂_ t. An affine structure is induced by the embedding 

**==> picture [263 x 40] intentionally omitted <==**

Here, the equivalence relation is as in (2). We remark that top-dimensional dual polytopes _Q[∨]_ are embedded by (35). If a one-dimensional polytope _P ∈P_[br] with end points _Q_ 0 _, Q_ 1 _∈P_ intersects a branch cut _Ci_ , the dual _P[∨]_ has two embeddings _ij_ : _P[∨] →_ t, _j_ = 0 _,_ 1 whose images lie on the boundary of the image of _i_ . That is, _ij_ ( _P[∨]_ ) _⊂ i_ ( _∂Q[∨] j_[).][The][embeddings] _[i]_[0] _[, i]_[1][are][related][to][each][other][by][a][shear] transformation (7). Thus, we obtain an affine structure on _B[∨] \B[∨][,]_[foc] by gluing the affine structure on the domain of (35) along the one-dimensional edges _ij_ ( _P[∨]_ ), _P ∈P_[br] . □ 

_Example_ 5.8 _._ Figure 22 shows a standard polyhedral decomposition of an almost toric moment polytope of Bl[8] P[2] . The dual complex _B[∨]_ is an affine manifold obtained 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

51 

by gluing together the dual polytopes 

**==> picture [147 x 13] intentionally omitted <==**

We choose coordinates arising from the moment polytope, that is, the complement of the branch cut produces an chart of the dual complex that is a subset of t. In particular, in this chart, the direction _µQ∨ ∈_ t of any one-dimensional dual polytope _Q[∨]_ ( _Q ∈P_ ) is given by the normal of the facet _Q ⊂_ t _[∨]_ . The dual complex _B[∨]_ , which is an affine manifold is obtained by gluing three pairs of edges by shear maps, namely the outer green edges of _P_ 0 _[∨]_[and] _[P]_ 1 _[ ∨]_[are][glued][by][the][shear][map] _[A]_[1] _[∈][GL]_[(2] _[,]_[ Z][),] those of _P_ 2 _[∨]_[and] _[P]_ 3 _[ ∨]_[are][glued][by] _[A]_[2][,][and][those][of] _[P]_ 4 _[ ∨]_[and] _[P]_ 5 _[ ∨]_[are][glued][by] _[A]_[3][.][The] shear maps _A_ 1, _A_ 2, _A_ 3 _∈ GL_ (2 _,_ Z) are given by 

**==> picture [251 x 27] intentionally omitted <==**

The matrix _A_ 1 has (1 _,_ 0) as an eigenvector with eigenvalue 1, and sends (3 _, −_ 1) to ( _−_ 6 _, −_ 1); _A_ 2, _A_ 3 can similarly be read off from Figure 22. More precisely, the gluing is defined on neighborhoods of the outer green edges by a map 

**==> picture [103 x 10] intentionally omitted <==**

where the constant _b ∈_ t is chosen so that the respective edges are identified by the gluing. Various tropical graphs corresponding to rigid broken maps are given in Figures 26, 27 and 28. This ends the Example. 

**==> picture [383 x 172] intentionally omitted <==**

**----- Start of picture text -----**<br>
(3 ,  2)<br>Q 3 ( − 3 , − 1) ρ<br>Q 2 P 3 Q [∨] 3 (0 ,  1)<br>P 2 P 4 Q 4 ρ Q [∨] 3 Q [∨] 4<br>Q [∨] 4<br>P 0 A 2<br>P P 1 P 6 P 5 Q 5 P 0 [∨] PP 4 [∨] 5 [∨] A 3<br>Q 1 Q 6 ( − 3 , − 1) QQ [∨] 2 [∨] 1 Q [∨] 6 Q [∨] 5 (0 ,  1) B [∨] ( ρ )<br>A 1<br>(1 ,  0) (1 ,  0)<br>( − 6 , − 1) (3 , − 1)<br>**----- End of picture text -----**<br>


Figure 22. Left: A polyhedral decomposition _P_ for _X_ := Bl[8] P[2] . The polytope _P_ 0 is top-dimensional, _Pi_ , _Qi_ , _i_ = 1 _, . . . ,_ 6 are zerodimensional. Right: Dual complex _B[∨]_ ( _ρ_ ). 

_Notation_ 5.9 _._ Let _P_ be a standard polyhedral decomposition of an almost toric manifold _X_ , with dual complex _B[∨]_ . 

52 

## S. VENUGOPALAN AND C. WOODWARD 

**==> picture [167 x 130] intentionally omitted <==**

**----- Start of picture text -----**<br>
µ out<br>(3 ,  2)<br>A 2<br>A 3<br>( − 6 , − 1) (3 , − 1)<br>A 1<br>**----- End of picture text -----**<br>


Figure 23. Dual affine manifold corresponding to the polyhedral decomposition _P_ of Bl8 P[2] in Figure 22. 

**==> picture [362 x 181] intentionally omitted <==**

**----- Start of picture text -----**<br>
µout<br>Rx<br>Ry<br>Q 4<br>Q 3 Rx [∨] Q [∨] 4<br>P 3 P 4 Q [∨] 3 Ry [∨]<br>Q 2<br>P 2 Rz Q [∨] 2<br>P 1 shear<br>Q 1 P 1 [∨]<br>P 10 P 9 Q [∨] 1 P 10 [∨] Rz [∨]<br>Q [∨] 10<br>µout<br>shear<br>**----- End of picture text -----**<br>


Figure 24. Left: A multiple cut on an almost toric manifold with three elliptic singularities at vertices of the pentagon. Right: The dual complex. An outward pointing vector field _µout_ is defined on _Q[∨] i_[,] _[i]_[ = 1] _[, . . . ,]_[ 10.] 

- (a) (Annular part of the dual complex) The _annular part of the dual complex_ is a subset of the dual complex _B[∨]_ defined as 

**==> picture [312 x 16] intentionally omitted <==**

In the absence of elliptic singularities, the top-dimensional polytopes in _B_ ann _[∨]_ are rectangles, where both _P_ in _[∨]_[,] _[P][ ∨]_ ann[are][one-dimensional.][In][case][there][are] elliptic singularities, _B_ ann _[∨]_[also consists of the dual polytope] _[ R] x[∨]_[corresponding] to each elliptic singularity _x_ . 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

53 

**==> picture [289 x 97] intentionally omitted <==**

**----- Start of picture text -----**<br>
x<br>Rx<br>Q 2 Φ( X ) Q [∨] 2 µout µ [(2)] out<br>Rx [∨]<br>µ [(1)] out<br>Q 1 Q [∨] 1<br>µout<br>**----- End of picture text -----**<br>


Figure 25. Dual polytope _Rx[∨]_[corresponding][to][an][elliptic][singular-] ity _x_ , and the extensions of the outward normal vector _µ_ out to _Rx[∨]_[.] 

- (b) (Normals to facets) In the absence of elliptic singularities, the affine manifold _B_ ann _[∨][⊂][B][∨]_[has][a][parallel][vector][field] 

(37) _µ_ out _∈_ Vect( _B_ ann _[∨]_[)] 

made up of primitive normals to facets. Such a vector field exists, since in the absence of elliptic singularities, the shear at a vertex maps the primitive normal of a facet to that of the adjacent one. If there are elliptic singularities, _µ_ out is defined only on the complement _B_ ann _[∨][\]_[(] _[∪] R∈P_[ell] _[R][∨]_[)][of][the][dual] polytopes corresponding to the elliptic singularities. In the dual polytope _Rx[∨]_ corresponding to an elliptic singularity _x_ , that shares facets with rectangular dual polytopes _Q[∨]_ 1[and] _[Q][∨]_ 2[,][the][parallel][extension][of] _[µ]_[out] _[|][Q][∨] i_[,] _[i]_[ = 1] _[,]_[ 2,][to] _[R] x[∨]_ is denoted by _µ_[(] out _[i]_[)][,][see][Figure][25][.] 

**Definition 5.10.** A vector _v ∈ TbB_ ann _[∨]_[is] _[outward][pointing]_[if] 

- (a) _b_ is in a rectangular dual polytope in _B_ ann _[∨]_[,][and] _[v]_[=] _[nµ]_[out][where] _[n][∈]_[Z] _[>]_[0] and _µ_ out is from (37)), 

(b) or _b_ lies in a polytope _Rx[∨][∈P]_[ell][corresponding][to][an][elliptic][singularity,][and] _v_ = _n_ 1 _µ_[(1)] out[+] _[ n]_[2] _[µ]_[(2)] out[,][where] _[n][i][∈]_[Z] _[≥]_[0][and] _[µ]_[(] out _[i]_[)][is][as][in][Figure][25][.] For an outward pointing vector _v_ , the _intersection number n∂_ ( _v_ ) _with the boundary divisor_ is _n_ resp. _n_ 1 + _n_ 2 in case (a) resp. (b). 

_Remark_ 5.11 _._ (Balancing condition) Recall that for a tropical graph Γ, the standard balancing condition holds for vertices _v_ lying in zero-dimensional polytopes, that is, dim( _P_ ( _v_ )) = 0. The balancing condition is that 

**==> picture [251 x 25] intentionally omitted <==**

where _σv_ ( _e_ ) is _−_ 1 resp. 1 if _e_ points towards resp. away from _v_ . We generalize the condition to vertices _v_ with dim( _P_ ( _v_ )) = 1. For an edge _e_ if _P_ ( _e_ ) _∈P/_[br] then, we view _T_ ( _e_ ) as an element in t via the embedding (35). If _P_ ( _e_ ) _∈P_[br] , there are two embeddings _i_ 0 _, i_ 1 : _P_ ( _e_ ) _[∨] →_ t related by a shear _A ∈ GL_ (2 _,_ Z), and we have _A_ ( _i_ 0( _T_ ( _e_ ))) = _i_ 1( _T_ ( _e_ )). The following cases arise. 

**Case 1:** Suppose _P_ ( _v_ ) _∈P/_[br] and _P_ ( _v_ ) does not intersect _∂_ Φ( _X_ ). Then, the standard balancing condition holds. 

S. VENUGOPALAN AND C. WOODWARD 

54 

**Case 2:** Suppose _P_ ( _v_ ) _∈P/_[br] and _P_ ( _v_ ) intersects a face _Fν_ of _∂_ Φ( _X_ ) with outward normal vector _ν ∈_ tZ. Then, 

**==> picture [267 x 24] intentionally omitted <==**

where _nv ∈_ Z _≥_ 0 is the intersection number of _uv_ with Φ _[−]_[1] ( _Fν_ ). 

**Case 3:** Suppose _P_ ( _v_ ) _∈P_[br] , with incident edges _{ei}i_ in the _i_ 0-side and _{fj}j_ in the _i_ 1-side. If _P_ ( _e_ ) _∈P_[br] , we choose a side arbitrarily. Then, the balancing condition is 

**==> picture [241 x 35] intentionally omitted <==**

_Remark_ 5.12 _._ (Inner and annulus parts of the dual complex) The dual complex partitions into an inner and an annulus part. The inner part is the dual complex of _P_ in, and is independent of _ρ_ . For any _ρ_ , define 

_B_ in _[∨]_[:=] _[ ∪] Q∈P_ in:dim( _Q_ )=0 _[Q][∨][⊂][B][∨]_[(] _[ρ]_[)] _[,] B_ ann _[∨]_[(] _[ρ]_[) :=] _[ B][∨]_[(] _[ρ]_[)] _[\]_[ int(] _[B]_ in _[∨]_[(] _[ρ]_[))] _[.]_ For example, in Figure 22, _B_ in _[∨]_[=] _[ ∪]_[1] _[≤][i][≤]_[6] _[P][i]_[and] _[ B]_ ann _[∨]_[=] _[ ∪]_[1] _[≤][i][≤]_[6] _[Q][i]_[.][If the almost toric] manifold has no elliptic singularities, the annulus part _B_ ann _[∨]_[is][obtained][by][gluing][a] set of rectangular dual complexes _Q[∨] i_[via][shears.][Each] _[Q][∨] i_[corresponds][to][a][point] of intersection between the decompositions _P_ in and _P_ ann. 

If the almost toric manifold has elliptic singularities, “gluing by shear” is replaced by additional polytopes. For every elliptic singularity _x ∈ X_ , there is a top-dimensional dual polytope _Rx[∨]_[that shares facets with rectangles] _[ Q][∨] i_[,] _[ Q][∨] j_[.][There] is no shear going from _Q[∨] i_[to] _[R] x[∨]_[to] _[Q][∨] j_[.][See][Figures][24][and][25][.][This][ends][the] Remark. 

**==> picture [297 x 160] intentionally omitted <==**

**----- Start of picture text -----**<br>
v 2<br>(3 ,  2)<br>u 2<br>u 1<br>u 0 v 1<br>v 0<br>**----- End of picture text -----**<br>


Figure 26. Left: A broken map in Bl8 P[2] whose starting direction is a normal to a divisor. Right: Tropical curve in the dual complex. The polyhedral decomposition and dual complex are as in Figure 22 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

55 

**==> picture [323 x 214] intentionally omitted <==**

**----- Start of picture text -----**<br>
L (3 u,  0)0 u 1 u 2<br>u 3 (3 , − 1)<br>u 0 u 2<br>u 1 u 3 v 0 v 2 (0,-1)<br>v 1<br>(3,-1)<br>(3,0) v 3<br>**----- End of picture text -----**<br>


Figure 27. Left: A broken map in Bl8 P[2] . Middle: The corresponding cartoon tropical curve. Right: Actual tropical graph in the dual complex. 

5.2. **Collisions at generic points.** In this section we describe the conditions on a standard polyhedral decomposition that ensures that for broken disks of Maslov index 2, collisions occur at generic points in the sense of Definition 1.2. The following is the precise statement: 

**Proposition 5.13.** (Collisions at generic points) _There exists a constant ϵ >_ 0 _such that the following holds: Suppose P is a standard polyhedral decomposition P satisfying_ 

   - _(a) P_ 0 _⊃_ (1 _− ϵ_ )Φ( _X_ ) _where P_ 0 _∈P is the polytope containing the Lagrangian fiber_ Φ( _L_ ) _, and_ 

   - _(b) for any cut space XPb (Pb ∈P) that contains focus-focus singularities, the primitive normal ν ∈_ tZ _to the facet Pb ∩ P_ 0 _does not lie in_ Φ( _X_ ) _[∨] ._ 

- _Then in a broken disk of Maslov index two in XP with tropical graph_ Γ _,_ 

   - _(a) the disk vertex v_ 0 _of_ Γ _is univalent,_ 

   - _(b) the initial slope of_ Γ _lies in_ Φ( _X_ ) _[∨] , and_ 

   - _(c) if for a vertex v, XP_ ( _v_ ) _contains a focus-focus singularity, then, v is univalent._ 

**Lemma 5.14.** (Areas of disks in toric orbifolds) _Let X be a toric orbifold with moment map_ Φ : _X →_ t _[∨] and suppose the moment polytope_ ∆:= Φ( _X_ ) _containing_ 0 _in the interior. Let u_ : _D\{_ 0 _} → X\_ Φ _[−]_[1] ( _∂_ ∆) _be a holomorphic disk with boundary in the Lagrangian L_ = Φ _[−]_[1] (0) _, with_ lim _z→_ 0 _u_ ( _z_ ) _∈_ Φ _[−]_[1] ( _∂_ ∆) _, and u∗_ [ _∂D_ ] = _ξ ∈_ tZ _. Then,_ 

(40) 

Area( _u_ ) = _cξ,_ 

56 

**==> picture [169 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
S. VENUGOPALAN AND C. WOODWARD<br>**----- End of picture text -----**<br>


**==> picture [348 x 227] intentionally omitted <==**

**----- Start of picture text -----**<br>
(2 ,  1)<br>(3 ,  2)<br>(3 ,  2)<br>v 5<br>(1 ,  1)<br>v 4<br>(1 ,  0)<br>L<br>v 3<br>u 6 u 5<br>u 4<br>u 3 ( − 1 ,  0) v 6<br>u 0 u 2<br>u 7 u 1 v 0 (1,0) ≃<br>v 1 v 2<br>v 6 (-1,0)<br>u 8 v 7 v 8<br>(2,1)<br>≃<br>(1,1)<br>**----- End of picture text -----**<br>


Figure 28. Left: A broken map in Bl8 P[2] whose starting direction is a normal to a divisor. Middle: The corresponding cartoon tropical curve. Right: Actual tropical graph in the dual complex. 

_where cξ >_ 0 _is such that for the plane Fξ_ := _{⟨x, ξ⟩_ = _cξ} ⊂_ t _[∨] , the intersection_ ∆ _∩ Fξ is non-empty and contained in ∂_ ∆ _._ 

_Proof._ The proof is identical to that of Theorem 8.1 in Cho-Oh [9] which computes the area of disks that intersects the boundary divisor at a single smooth point. □ 

The next result gives a lower bound on the constants _cξ_ occuring in the area formula (40) when _ξ_ is not in the dual of Φ( _X_ ). 

**Lemma 5.15.** _Let_ ∆ _⊂_ t _[∨] ≃_ R[2] _be the moment polytope of a compact toric orbifold all whose faces are of the form Fµ_ = _{⟨x, µ⟩_ = 1 _} where µ ∈_ tZ _is a primitive vector. For any ξ ∈_ tZ _let cξ be the constant such that for the hyperplane_ 

**==> picture [117 x 14] intentionally omitted <==**

_the intersection_ ∆ _∩ Fξ is non-empty and contained in ∂_ ∆ _. There is a constant C >_ 1 _such that for any ξ ∈_ tZ _\_ Φ( _X_ ) _[∨] ,_ 

**==> picture [36 x 12] intentionally omitted <==**

_Proof._ We consider the case when _ξ ∈/_ Φ( _X_ ) _[∨]_ and _Fξ_ intersects ∆at a vertex _x_ 0, the proof of the other cases is the same. Suppose _x_ 0 is the intersection of facets _Fµi_ = _{⟨y, µi⟩_ = 1 _}_ , _i_ = 1 _,_ 2 of ∆. Then, _ξ_ lies in the cone generated by _µ_ 1, _µ_ 2, that is, 

**==> picture [113 x 12] intentionally omitted <==**

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

57 

for some _t ∈_ [0 _,_ 1], _C_ 1 _≥_ 0. We have _cξ_ = _C_ 1, because _Fξ_ passes through _Fµ_ 1 _∩ Fµ_ 2. Since _ξ ∈/_ ∆ _[∨]_ , _C_ 1 _>_ 1. Define _C >_ 1 to be the least value for which the set ( _C_ ∆ _[∨] \_ ∆ _[∨]_ ) _∩_ tZ is non-empty. We conclude _cξ_ = _C_ 1 _≥ C_ because _ξ ∈_ tZ _∩ C_ 1∆ _[∨]_ . □ 

_Proof of Proposition 5.13._ We first prove (a), namely that the disk vertex is univalent. Suppose the disk vertex _v_ 0 of Γ is not univalent, and as incident edges _e_ 1 _, . . . , ek_ , _k ≥_ 2. There is a decomposition of the homology class 

**==> picture [134 x 33] intentionally omitted <==**

where _ui_ is disk in _XP_ 0 with a single relative node with direction _T_ ( _ei_ ). For reasons of dimension of the moduli space, among the edges _e_ 1 _, . . . , ek_ , there is exactly one outgoing edge (with respect to the constraint orientation from Lemma 3.19) which we assume to be _e_ 1. We arrive at a contradiction by constructing a non-constant broken map whose area is smaller than that of _u_ . Let _u[′]_ 1[be][the][relative][map][consisting][of] all the sphere components of _u_ that are connected to _u_ 0 via _e_ 1. There is a relative map _u[′′]_ 1[homotopic][to] _[u][′]_ 1[such][that][(] _[u]_[1] _[, u][′′]_ 1[)][satisfy][the][matching][condition][at][the] edge _e_ 1. Then, ( _u_ 1 _, u[′′]_ 1[)][is][a][broken][map][with][positive][area,][but][whose][area][is][less] than Area( _u_ ) which is a contradiction, since ( _X, L_ ) is monotone. Therefore, the disk vertex of Γ is univalent. 

To prove part (b), we again assume the contrapositive, namely that the initial slope of the broken map does not lie in Φ( _X_ ) _[∨]_ . In other words, we assume that for the disk component _u_ 0 : _D → XP_ 0 of _u_ , the element 

**==> picture [93 x 12] intentionally omitted <==**

does not lie in Φ( _X_ ) _[∨]_ . By Lemma 5.14, and the condition _P_ 0 _⊃_ (1 _− ϵ_ )Φ( _X_ ), we get Area( _u_ 0) = (1 _− ϵ_ ) _cξ_ . Here _cξ >_ 0 is defined by the condition that the plane _{⟨x, ξ⟩_ = _cξ}_ intersects Φ( _X_ ) at the boundary _∂_ Φ( _X_ ). By Lemma 5.15, _cξ ≥ C_ , and thus, 

**==> picture [100 x 12] intentionally omitted <==**

We fix _ϵ_ so that (1 _− ϵ_ ) _C >_ 1 so that the assumed case does not occur. That is, the initial slope of the broken map _u_ lies in Φ( _X_ ) _[∨]_ . 

Next, we prove (c) which says that there are no collisions at singular points of the dual complex, that is, there cannot be a vertex _v_ with valence at least 2 and _P_ ( _v_ ) = _Pb_ and _XPb_ contains a focus-focus singularity. Lemma 5.21 shows that tropical graphs in the annular part of the dual complex spiral outwards. A collision at a singular point can occur only if the disk component _u_ 0 : _D → XP_ 0 of _u_ intersects the divisor _XP_ 0 _∩ XPb_ . This can happen only if _ξ_ is equal to the primitive normal of the facet _P_ 0 _∩ Pb_ , which by assumption, does not lie in Φ( _X_ ) _[∨]_ . Therefore, by (c) such a disk does not exist. □ 

5.3. **Collisions in the interior.** In this Section, we prove that collisions happen in the interior. 

**Proposition 5.16.** (Collisions in the interior) _Suppose that X is a monotone symplectic four-manifold with an almost toric structure with no elliptic singularities._ 

S. VENUGOPALAN AND C. WOODWARD 

58 

- _For a large enough ρ, for a tropical graph_ Γ _corresponding to a disk of Maslov index_ 2 _, there is a single vertex v∂ with P_ ( _v∂_ ) _∈P∂. Furthermore,_ 

   - _(a) the map uv∂ is a holomorphic cylinder intersecting a boundary divisor_ Φ _[−]_[1] ( _Fν_ ) _where Fν is a facet of_ Φ( _X_ ) _with normal vector ν ∈_ tZ _, and_ 

   - _(b) v∂ is univalent with incident edge e∂ and T_ ( _e∂_ ) = _ν._ 

_Proof._ First, we show that for a large _ρ_ , any tropical graph has outward-pointing edges. We recall from Definition 5.3 that a good polyhedral decomposition is a combination of _P_ ann and _P_ in. We apply Proposition 3.23 with _P_ 0 := _P_ ann and _P_ 1 := _P_ in and conclude the following: There exists _ρ_ 0 such that the set of tropical graphs realizable in _Bρ[∨]_[is][the][same][for][all] _[ρ][≥][ρ]_[0][.][Proposition][3.23][(][b][)][implies] that in any such tropical graph Γ, any path from the disk vertex _v_ 0 to a vertex in the boundary contains an outward-pointing edge in the sense of Definition 5.10 (or a _B_ 0 _[∨]_[-edge][in][the][terminology][of][Proposition][3.23][).][Let] _[S][⊂]_[Edge(Γ)][denote][the] set of outward-pointing edges in Γ, and let Γ0 _⊂_ Γ _\S_ be the connected component containing the disk vertex _v_ 0. By the terminology of Definition 5.10, for any edge _e_ in _S_ , _n∂_ ( _T_ ( _e_ )) is the intersection number of _T_ ( _e_ ) with the boundary divisor. For the reader’s convenience we recall that in the case with no elliptic singularity, the direction of an outward pointing edge _e_ is _n∂_ ( _T_ ( _e_ )) _µ_ out and _P_ ( _e_ ) _[∨]_ is a rectangle. The proof proceeds via the following claim. 

_Claim_ 5.17 _._ For the subgraph Γ0 _⊂_ Γ as above, 

**==> picture [291 x 27] intentionally omitted <==**

where _n∂_ ( _T_ ( _e_ )) is the intersection number of _T_ ( _e_ ) with the boundary divisor (Definition 5.10). 

_Proof of Claim._ We construct an augmentation of _u|_ Γ0 denoted by _u_ aug with tropical graph Γaug, by adding vertices to Γ0 corresponding to each edge in _S_ . 

First, consider the case that an edge _e ∈ S_ that lies in a rectangular dual polytope _P_ ( _e_ ) _[∨]_ . Suppose _e_ is incident on the vertex _ve_ in Γ0. In a realization of Γ, the edge _e_ exits _P_ ( _e_ ) _[∨]_ at an edge _Q[∨] ⊂ P_ ( _e_ ) _[∨]_ . We add vertex _ve[′]_[as][the][other][end-point] of _e_ , with _P_ ( _ve[′]_[)][:=] _[Q]_[,][and][let] _[u][v] e[′]_[be][a][holomorphic][cylinder][which][is][an] _[n][e]_[-fold] cover of a fiber of the projection _X P_ ( _e_ ) _∨ → X Q_ . Each fiber _F_ = _[∼]_ P[1] itself is a toric variety, with moment polytope the fiber Φ( _F_ ) of the projection from _P_ ( _e_ ) _[∨]_ to _Q_ . As a special case of the Archimedes’ formula [21, Theorem 6.4] the area of the fiber is _ϵ_ , up to a universal normalization constant, which with our conventions is equal to 1. Indeed, as _ϵ →_ 1, the broken map corresponding to a Maslov index two disk with direction _T_ ( _e_ ) consists of a sphere with image _F_ and a disk with small area; it follows that the area of _F_ tends to 1 as _ϵ →_ 1. Hence the area of _uve′_ is _ne_ Vol( _F_ ). 

Next, consider an edge _e ∈ S_ that lies in the dual polytope _Rx[∨]_[corresponding][to] an elliptic singularity _x_ . Suppose _T_ ( _e_ ) = _n_ 1 _µ_[(1)] out[+] _[ n]_[2] _[µ]_[(2)] out[as][in][Definition][5.10][(][b][).] If _n_ 1 or _n_ 2 vanishes, we add a single vertex _ve[′]_[as][the][second][endpoint][of] _[e]_[exactly] as in the preceding case. If both _n_ 1, _n_ 2 are non-vanishing, we add 3 vertices as in Figure 29. In all cases, the sum of the areas of the maps corresponding to the new 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

59 

vertices is _neϵ_ . The map _u_ aug has[�] _e∈S[n][e]_[intersections][with][boundary][divisors.] Therefore, the area of _u_ aug is[�] _e∈S[n][e]_[.][The][equation][(][41][)][follows.] □ 

Since the total area if _u_ is 1, from (41), we conclude that _S_ has a single element _e_ and _ne_ = 1. Any map _u_ other than _u_ aug that contain _u|_ Γ0 has area more than that of _u_ aug. We conclude that _u_ = _u_ aug, which proves the Proposition. □ 

**==> picture [307 x 99] intentionally omitted <==**

**----- Start of picture text -----**<br>
x<br>uw 2<br>w 2<br>ewoutout [R] x [∨] Augment ww 0 out w 1 uuwwout 0, uw 1<br>Γ0<br>**----- End of picture text -----**<br>


Figure 29. Left: The subgraph of the tropical graph Γ0 _⊂_ Γ 

**==> picture [416 x 242] intentionally omitted <==**

**----- Start of picture text -----**<br>
Q [∨] 2<br>shear<br>( − 1 ,  1)<br>R 1 [∨]<br>x  + 2 y = 1 Q [∨] 1<br>−x  + 2 y = 1<br>Q 2<br>R 1<br>P 2 P 2 [∨] (0 ,  1)<br>−x  +  y = 1 Q 1 P 1 P 1 [∨]<br>**----- End of picture text -----**<br>


Figure 30. Left: A portion of a moment polytope containing a _A_ 1 _/_ Z2-singularity and an elliptic singularity. Right : A tropical graph of a Maslov index two disk. 

S. VENUGOPALAN AND C. WOODWARD 

60 

5.4. **Tropical graphs spiral outward.** We now give a complete description of tropical graphs corresponding to rigid broken disks in standard decompositions, and prove Proposition 5.1. We assume that edges in the tropical graph are oriented by the constraint orientation from Lemma 3.19. 

We define a notion of _outward-pointing_ cones on the annulus part of the dual complex, which will be used to show that the tropical graphs corresponding to broken disks of Maslov index two _spiral outward_ towards the boundary of the moment polytope. 

**Definition 5.18.** (Outward pointing cone) 

- (a) (On the interior of a rectangle) Let _P[∨] ⊂ B_ ann _[∨]_[(] _[ρ]_[)][be][a][rectangular][dual] polytope given by _P[∨]_ = _P_ 0 _[∨][×][ρP][ ∨]_ 1[.] For any _x ∈_ int( _P[∨]_ ), the _outward pointing cone_ is a half space 

         - _Hx_ := _{v ∈ TxB[∨]_ : _gP_ ( _v, µ_ out) _≥_ 0 _},_ 

   - where _gP_ is the product metric on _P_ 0 _[∨][×][ ρP][ ∨]_ 1[.] 

- (b) (On the boundaries of rectangles) Let _P[∨] , Q[∨] ⊂ B[∨]_ be rectangular polytopes whose intersection _P[∨] ⊂ Q[∨]_ is an edge. For any _x ∈ P[∨] ∩ Q[∨]_ , the outward pointing cone is 

      - _Hx_ := _{v ∈ TxB[∨]_ : _gP_ ( _v, µ_ out) _, gQ_ ( _v, µ_ out) _≥_ 0 _}._ 

- (c) (Near elliptic singularities) Let _x ∈ X_ be an elliptic singularity and let _Rx[∨][⊂][B][∨]_[be][the][corresponding][dual][polytope][that][shares][edges][with][rect-] angular dual polytopes _P_ 0 _[∨]_[,] _[P]_ 1 _[ ∨]_[.][For][any] _[y][∈][R] x[∨]_[,][the][outward-pointing][cone] _Hy ⊂ TyB[∨]_ is obtained by parallel transporting (with respect to the affine structure) the half planes in the interior of _P_ 0 _[∨]_[or] _[P]_ 1 _[ ∨]_[.][Both][give][the][same] half planes. 

_Example_ 5.19 _._ In Figure 22, for _x ∈ Q[∨]_ 1[the][half][plane] _[H][x]_[is][bounded][by][(1] _[,]_[ 0),] whereas for _x ∈ Q[∨]_ 2[the][half][plane] _[H][x]_[is][bounded][by][(] _[−]_[3] _[,][ −]_[1).][The][half-planes] remain constant while passing over a shear. For _x ∈ Q[∨]_ 1 _[∩][Q]_ 2 _[∨]_[,] _[H][x]_[is][a][cone] R _≥_ 0 _⟨_ (1 _,_ 0) _,_ ( _−_ 3 _, −_ 1) _⟩_ . 

**Lemma 5.20.** _Suppose ℓ ⊂ B_ ann _[∨][(defined][in][Remark][5.12][)][is][an][oriented][line][seg-] ment starting at a point x ∈ B_ ann _[∨][and][which][is][outward-pointing][at][x][.][Then,][ℓ][is] outward-pointing everywhere._ 

The proof is straightforward and left to the reader. 

**Lemma 5.21.** _Let_ Γ _be a tropical graph in B[∨]_ ( _ρ_ ) _corresponding to a broken disk of Maslov index two, with disk vertex v_ 0 _with incident edge e_ 0 _._ 

- _(a) Any edge e ∈_ Edge(Γ) _\{e_ 0 _}, when equipped with the constraint orientation, has direction lying in the outward pointing cone._ 

- _(b) All vertices v ∈_ Vert(Γ) _except for disk vertices lie in the annulus part B_ ann _[∨]_[(] _[ρ]_[)] _of the dual complex._ 

_Proof of Lemma 5.21._ A tropical graph Γ has a path emanating from a disk vertex _v_ 0 lying in _P_ 0 _[∨]_[,][and][this][path][intersects][the][annulus] _[B]_ ann _[∨]_[in][an][outward-pointing] 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

61 

direction. In fact, in such a path _v_ 0 is the only vertex not lying in the annulus _B_ ann _[∨]_[.] Any other path starting from a univalent vertex starts out at a piece _XP_ where _P_ contains a focus-focus value and _P[∨]_ is a point in _∂B_ ann _[∨]_[and][is][outward][pointing;] therefore such a path is contained in _B_ ann _[∨]_[.][Finally,][when paths collide,][their merger] is a path with an outward-pointing direction, because the set of outward pointing directions is a cone at any point. 

**==> picture [10 x 8] intentionally omitted <==**

## 6. Newton polygons and mutations 

In this section we prove various theorems on the potentials of almost toric fourmanifolds manifolds; namely that potentials for mutations of almost toric diagrams are related by algebraic mutation in Theorem 6.8, that the Newton polygon is the convex hull of the normal vectors to the facets in Theorem 6.15, and that the potential coefficients are binomial along edges in Theorem 6.16. 

6.1. **The dual affine manifold.** Given a monotone almost toric manifold, the standard decomposition of Section 5 gives a family of dual complexes, whose limit is an dual affine manifold. Up to equivalence, a dual affine manifold can be constructed directly from the base diagram of the almost toric manifold, without considering the polyhedral decomposition. We show that the potential is preserved by these equivalences. Thus we obtain a direct combinatorial way of computing the potential from the base diagram of a monotone almost toric manifold. In the next section, we consider the question of deformations of the dual affine manifold that involve crossing a wall, causing the potential to mutate. 

Given an almost toric manifold _X_ and a standard decomposition _P_ , the corresponding dual affine manifold _A_ ( _X_ ) is defined as the limit of dual complexes: 

_Notation_ 6.1 _._ A standard polyhedral decomposition _P_ of an almost toric manifold _X_ has a family of dual complexes _{B[∨]_ ( _ρ_ ) _}ρ>_ 0 (see (34)). The parameter _ρ_ is the ratio of sides of certain rectangles that occur in the dual complex. By taking the parameter _ρ_ in the dual complex to infinity, we obtain a singular affine manifold (complete, without boundary) as follows. We have natural inclusions of singular integral affine manifolds 

**==> picture [151 x 13] intentionally omitted <==**

arising from the canonical isomorphisms between the neighborhood of _P_ 0 _[∨]_[in] _[B][∨]_[(] _[ρ]_[)] and _B[∨]_ ( _ρ[′]_ ). (We recall that _P_ 0 contains the Lagrangian fiber, and thus, _P_ 0 _[∨]_[is][the] point in the dual complex where the disk vertices lie.) 

## **Definition 6.2.** The union 

**==> picture [251 x 26] intentionally omitted <==**

is the _dual affine manifold_ for _X_ . The Lagrangian point is the element _λ_ := _P_ 0 _[∨]_ where _P_ 0 contains the image of the Lagrangian. 

S. VENUGOPALAN AND C. WOODWARD 

62 

See Figure 23 for an example. The dual affine manifold depends on the decomposition _P_ , but the dual affine manifolds corresponding to various standard decompositions have the same potential, see Remark 6.9. We denote by _T_ Z( _A_ ( _X_ )) _⊂ T A_ ( _X_ ) the set of integral tangent directions. 

_Remark_ 6.3 _._ Given an almost toric manifold ( _X,_ Φ) that does not have elliptic singularities, the dual affine manifold _A_ ( _X_ ) is given by 

(43) (Φ( _X_ ) _∪_ ( _∪iFi ×_ R _≥_ 0)) _/ ∼_ 

where Φ( _X_ ) is embedded in t by an arbitrary choice of a linear identification t _≃_ t _[∨]_ , _Fi_ ranges over all facets of Φ( _X_ ), _Fi ×_ R _≥_ 0 _⊂_ t is a rectangle where _R≥_ 0 is in the outward normal direction of the facet _Fi_ , _Fi × {_ 0 _}_ is the facet _Fi ⊂_ Φ( _X_ ), and _∼_ makes the following identification: For a vertex _v ∈ Fi ∩ Fj_ of Φ( _X_ ), the line R _≥_ 0 _×{v}_ in the rectangles _Fi ×_ R _≥_ 0, _Fj ×_ R _≥_ 0 are identified and the affine structures in the neighborhoods are identified via a shear. See Figure 6. 

**Definition 6.4.** Given an almost toric diagram and gluing datum, the _tropical potential_ of the dual affine manifold _A_ with distinguished point _λ_ is 

**==> picture [241 x 25] intentionally omitted <==**

where _∂_ Γ _∈_ ( _TλA_ )Z is the initial slope of Γ, and Γ ranges over all _A_ -tropical trees of index two, and m(Γ) =[�] _v∈_ Vert(Γ) _[m]_[(] _[v]_[)][is][defined][in][Definition][1.4][.] 

_Remark_ 6.5 _._ By the definition of the dual affine manifold as the limit of dual complexes, the potential _W_ ( _A,λ_ ) is equal to the potential computed from broken map in a standard decomposition in (16). 

_Remark_ 6.6 _._ By choosing an identification 

(44) _TλA ≃_ t _≃_ R[2] 

that sends ( _TλA_ )Z to tZ and Z[2] , the potential is a Laurent polynomial 

**==> picture [81 x 15] intentionally omitted <==**

Transforming the identification by _A ∈ GL_ (2 _,_ Z) has the effect of applying a multiplicative transformation to each monomial in the potential _W_ : the monomial _x[a] y[b] c_ is transformed to _x[c] y[d]_ where _A[t]_[�] _[a] b_ � = � _d_ �. 

The potential of a dual affine manifold is unchanged by homotopies that do not contain a “wall” in the sense of the following definition: 

**Definition 6.7.** (Wall configurations) 

- (a) An _A_ -tropical disk has _index zero_ if it does not have any semi-infinite edges. 

- (b) A dual affine manifold _A_ ( _X_ ) with a Lagrangian point _λ ∈A_ ( _X_ ) is a _wall configuration_ if there is an _A_ -tropical disk of index zero in ( _A_ ( _X_ ) _, λ_ ). A wall configuration is _simple_ if the _A_ -tropical disk has two vertices – a disk vertex at _λ_ and a sphere vertex at a singular point _b_ . (More complicated wall configurations exist, but in this paper we only encounter simple walls.) 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

63 

- (c) Dual affine manifolds _A_ 0, _A_ 1 are _equivalent_ , if there is a continuous family of dual affine manifolds _{At}t∈_ [0 _,_ 1] that does not contain any wall configuration. 

For example, two distinct singular points _b_ 0, _b_ 1 on the same branch cut in an affine manifold _A_ 0 may coalesce to the same point in an equivalent affine manifold _A_ 1 producing equivalent dual affine manifolds. See Figure 31 for example. 

**==> picture [384 x 65] intentionally omitted <==**

**----- Start of picture text -----**<br>
Φ( X ) b 0, b 1 A ( X ) Φ( X ) bb 01 A ( X ) b 0<br>b 0, b 1 b 1 b 1<br>A [′]<br>A A<br>**----- End of picture text -----**<br>


Figure 31. Moving the singular point _b_ 1 inward (towards the Lagrangian point _λ_ ) removes a rectangle from the dual affine manifold, but does not change the equivalence class. 

For an almost toric manifold _X_ and a monotone Lagrangian fiber, the dual affine manifold can be determined up to equivalence by the construction (43), which produces a dual manifold where all focus-focus singularities in a branch cut coincide. Equivalent dual manifolds are obtained by moving the singularities and _P_ 0 _[∨]_[,][while] avoiding walls. 

**Theorem 6.8.** _For a pair of equivalent dual affine manifolds_ ( _A_ 0 _, λ_ 0) _,_ ( _A_ 1 _, λ_ 1) _, W_ ( _A_ 0 _,λ_ 0) = _W_ ( _A_ 1 _,λ_ 1) _._ 

_Proof._ Suppose, as in the assumption in the statement of the Theorem, that the affine manifolds _A_ 0, _A_ 1 are connected by a path _{At}t_ that does not contain a wall configuration. After a small perturbation, we may assume that the path _{At}t_ is generic in a sense pointed out later in the proof. 

We first list the possible reasons a family of tropical graphs ends at a point. In particular, if a tree Γ with edge slopes _{T_ ( _e_ ) _}e_ has an embedding _Tt_ in _At_ for _t ∈_ ( _t_ 0 _− ϵ, t_ 0) but does not have an embedding in _At_ 0, then one of the following occurs: 

- (1) An edge length goes to zero, that is, for an edge _e_ = ( _v−, v_ +) of Γ, 

**==> picture [120 x 17] intentionally omitted <==**

- (2) or in the limit _t → t_ 0, the embedding of an edge _e_ passes through a singular point. 

Consider case (1) where the length of an edge _e_ = ( _v−, v_ +) goes to zero in the tropical embedding. Define the limit tropical graph 

**==> picture [80 x 21] intentionally omitted <==**

to be the tropical disk where the end-points of _e_ , _v_ + and _v−_ are replaced by a single vertex _v_ . Let _S±_ be the set of index two tropical disks in ( _At_ 0 _±ϵ, λt_ 0 _±ϵ_ ) for a small enough _ϵ >_ 0 which deform to Γ0 as _ϵ →_ 0. 

S. VENUGOPALAN AND C. WOODWARD 

64 

The curve count in _S_ + and _S−_ is the same since they are both smoothings of Γ0 as we now explain. We observe that in Γ at most one end-point of _e_ has valence one, in which case, the univalent vertex is _v−_ since the edge incident on a univalent vertex is outgoing. Therefore the following cases (see Figure 32) arise: 

**==> picture [389 x 115] intentionally omitted <==**

**----- Start of picture text -----**<br>
Tt 0 −ϵ Tt 0 Tt 0 −ϵ Tt 0<br>v− e v + ℓ ( e ) = 0 v− e v + ℓ ( e ) = 0<br>Type 1A Type 1B<br>Tt 0 −ϵ Tt 0<br>Index 0<br>λ e v + λ<br>v− Type 1C<br>**----- End of picture text -----**<br>


Figure 32. Types of end-points for a one-dimensional family of tropical graphs. 

Case 1A: First, consider the case that both _v_ +, _v−_ have valence at least 3 in Γ. Consider any tropical graph Γ _± ∈ S±_ , and let Γ _±,v ⊂_ Γ _±_ be the subgraph consisting of the vertices that get collapsed to _v_ in Γ0. The positions of the incoming edges[5] of Γ _±,v_ , collectively denoted by _ℓ±_ ( _v_ ), are fixed across all graphs Γ _± ∈ S±_ , and these positions are perturbations of the edge positions in Γ0. Thus _{_ Γ _±,v_ : Γ _± ∈ S±}_ is the set of split perturbations (as in Definition 1.8) of Γ0 _,v ⊂_ Γ0 with splitting data _ℓ±_ . Therefore, by the proof of the last part of Theorem 1.3 in Section 4.4, 

**==> picture [134 x 27] intentionally omitted <==**

For any Γ _± ∈ S±_ , the vertices in Γ _±\_ Γ _±,v_ , alongwith their incident edges, are the same as the corresponding vertices in Γ0. Therefore, the count of tropical graphs in _S_ + and in _S−_ is the same. 

Case 1B: Next, consider the case that _v−_ is univalent and maps to a singular point _b_ of _A_ ( _X_ ). In this case, _e_ may be one of the multiple coincident (as in Definition 4.16) edges _e_ 1 _, . . . , ek_ whose lengths go to zero simultaneously, all of which are incident on univalent vertices lying on the singular point _b_ , and whose other endpoint is _v_ +. In Γ0, the vertex _v_ obtained by collapsing the edges _e_ 1 _, . . . , ek_ lies on the singularity _b ∈At_ 0. By the genericity of the path _{At}t_ , we may assume the following: _b_ does not coincide with other singular points in _At_ for _t_ close to _t_ 0; _v_ has a single input edge; and there is no collision at the singular point for _t_ = _t_ 0 in the neighborhood of _t_ 0. Then for any Γ _± ∈ S±_ , the subgraph Γ _±,v_ is a ( _±_ )-perturbation (or equivalently ( _∓_ )-perturbation, depending on the sign convention) of Γ0 _,v_ . By Proposition 4.15, the counts of (+) and ( _−_ )-perturbations of (Γ _, Tt_ 0) are equal to 

5 By ‘position’, we mean the starting point and direction. 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

65 

each other. Therefore, the count of tropical graphs in _S_ + is equal to the count in _S−_ . 

Case 1C: Next, consider the case that _v−_ is univalent and is a disk vertex. We rule out this case by showing that _At_ 0 is a wall configuration. Since _v_ + has valence at least 3 in Γ, the vertex _v_ in Γ has valence at least 2. The tropical disk Γ has one semi-infinite edge, and therefore the same is true of Γ0. Therefore, there is an edge _e_ 0 _∋ v_ of Γ0, such that the subgraph Γ _[′]_ 0 _[⊂]_[Γ][0][consisting][of] _[v]_[and][all][the][vertices] whose path to _v_ contains _e_ , is a tropical disk of index 0. Therefore, _At_ 0 is a wall configuration which is a contradiction. 

Finally, we consider the case (2) where an edge _e_ passes through a focus-focus singularity _b_ in _At_ 0. We subdivide the edge, and add a vertex _v_ that lies on _b_ . This graph is the same as the graph in case 1B and can be analyzed in the same way. See the top row of Figure 33 for an example. □ 

**==> picture [387 x 166] intentionally omitted <==**

**----- Start of picture text -----**<br>
Wall<br>e 1 ( − 3 ,  2)<br>( −e 2 ,  0) b ( − 3 ,  2) e 1<br>e 0 ( − 1 ,  2) Slidedown b b ( − 1 ,  2) Slidedown b ( − 3 ,  2) b ( − 1 ,  2)<br>e 0<br>e 1<br>e 1<br>(-1,2) b b (1,2)<br>e e<br>(-1,0) (1,0)<br>Slide b<br>to the left<br>(0,2) (0,2)<br>e 0 e 0<br>**----- End of picture text -----**<br>


Figure 33. Sliding a node does not change the count of these tropical graphs. The top left is a bunched tropical graph. 

To apply Theorem 6.8, we need to show that a path of dual affine manifolds does not contain a wall. For this purpose, it is helpful to have a notion of an annular part of a dual affine manifold, which is a slight variation of the corresponding notion (36) for dual complexes: For our purposes we consider dual affine manifolds ( _A, λ_ ) that are close to those obtained from a base diagram ∆of an almost toric manifold and a polyhedral decomposition _P_ . Therefore, we may assume that for any ( _A, λ_ ) there is a related moment polytope ∆. In such a case, we choose a bounded convex polygon _S ⊂A_ ( _X_ ) that contains all the singular points of _A_ ( _X_ ), _λ_ lies in the interior of _S_ , and for any vertex _v_ of ∆from which a branch cut emanates, the outermost singular point _bv_ on the branch cut is a vertex of _S_ , and furthermore the line _ℓbv_ of slope _µbv_ through _bv_ intersects _S_ only at _bv_ . We define the _annular part of the dual manifold_ to be 

(45) _A_ ( _X_ )ann := _A_ ( _X_ ) _\_ int( _S_ ) _._ 

S. VENUGOPALAN AND C. WOODWARD 

66 

_Remark_ 6.9 _._ In this remark, we show that certain dual affine manifolds are not walls. Using the definition of _A_ ( _X_ )ann, it can be seen in a straightforward way that for a dual affine manifold ( _A_ 0 _, λ_ 0) corresponding to a standard polyhedral decomposition, there are no walls nearby. Therefore the potential is invariant under small deformations. 

- (a) Firstly, in ( _A_ 0 _, λ_ 0), all collisions involving inputs from singular points happen in the annulus, and consequently ( _A_ 0 _, λ_ 0) is not a wall. Similarly, if ( _At, λt_ ) is a family of dual affine manifolds obtained from polyhedral decompositions _Pt_ , the potential _W_ ( _At,λt_ ) is _t_ -independent, since no element in the family ( _At, λt_ ) is a wall. 

- (b) By the definition of a standard polyhedral decomposition, all singular points on a branch cut coincide in _A_ 0. Let _At_ be a family obtained by separating the singular points. Collisions involving inputs from singular points continue to happen in the annulus if the singular points are moved by small amounts, and therefore the potential is not altered. 

6.2. **Mutations and wall-crossing.** By a mutation of the moment polytope of an almost toric manifold, we mean a change in the almost toric structure by which one of the focus-focus values is moved from one side of the polytope to the other, as in Definition 2.13. Lemma 2.14 implies that the disk potential is not altered by a nodal slide as long as the focus-focus value does not cross the image of the monotone torus in the moment polytope. By Vianna’s work [50], such a crossing changes the Hamiltonian isotopy class of the monotone Lagrangian torus fibers. Pascaleff-Tonkonog [39] proved that the change in potential is given by a mutation of Laurent polynomials. We prove the same result (Proposition 6.14) using tropical methods. The tropical approach to the change in potential also figures prominently in the GrossSiebert approach to mirror symmetry. See for example Gr¨afnitz-Ruddat-Zaslow [19] (where the potential is computed for a non-monotone torus close to the anticanonical divisor.) 

**Definition 6.10.** (Mutation of a Laurent polynomial) Given a vector 

**==> picture [84 x 14] intentionally omitted <==**

the _mutation coordinate change_ associated to _ν_ is the map 

(46) _Sν_ : (C _[×]_ )[2] _→_ (C _[×]_ )[2] _,_ ( _y_ 1 _, y_ 2) _�→_ ( _y_ 1(1 + _y_ 1 _[ν]_[2] _[y]_ 2 _[−][ν]_[1] ) _[ν]_[1] _, y_ 2(1 + _y_ 1 _[ν]_[2] _[y]_ 2 _[−][ν]_[1] ) _[ν]_[2] ) _._ The _mutation_ of a function _W_ : (C _[×]_ )[2] _→_ C in the direction _ν_ is defined as the pullback[6] 

_Sν[∗][W]_[: (][C] _[×]_[)][2] _[→]_[C] _[.]_ 

_Remark_ 6.11 _._ Suppose that _W_ is a Laurent polynomial. The mutation _Sν[∗][W]_[is][a] rational function obtained by replacing each monomial in _W_ as follows: 

_y_ 1 _[µ]_[1] _[y]_ 2 _[µ]_[2] _�→ y_ 1 _[µ]_[1] _[y]_ 2 _[µ]_[2][(1 +] _[ y]_ 1 _[ν]_[2] _[y]_ 2 _[−][ν]_[1] ) _[µ]_[1] _[ν]_[1][+] _[µ]_[2] _[ν]_[2] _._ 

In the following result, we show that a mutation of an almost toric manifold (Definition 2.13 (d)) corresponds to a simple wall crossing in the dual affine manifold. 

- 6More general mutations are considered in Coates et al [11]. 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

67 

**==> picture [341 x 68] intentionally omitted <==**

**----- Start of picture text -----**<br>
t  =  −ϵ t  = 0 t  =  ϵ<br>A 0 Aϵ<br>λ−ϵ b−ϵ ν µb b 0 bϵ<br>λ 0<br>A−ϵ λϵ<br>**----- End of picture text -----**<br>


Figure 34. Crossing a wall in the direction _ν_ = (0 _,_ 1). 

**Proposition 6.12.** _Suppose X_ 0 _, X_ 1 _are almost toric manifolds related by a mutation where a single focus-focus singularity b ∈ X_[foc] _is moved from one side of the polytope to another. Let_ ∆0 _,_ ∆1 _be base diagrams of X_ 0 _, X_ 1 _of Vianna type and let_ ( _A_ 0 _, λ_ 0) _,_ ( _A_ 1 _, λ_ 1) _be dual affine manifolds obtained via standard decompositions applied to_ ∆0 _,_ ∆1 _, with singular points b_ 0 _∈A_ 0 _, b_ 1 _∈A_ 1 _corresponding to the singularity b in the almost toric manifold. Then, A_ 0 _, A_ 1 _are connected by a path of dual manifolds_ ( _At, λt_ ) _t∈_ [0 _,_ 1] _which contains a single wall_ ( _At_ 0 _, λt_ 0) _,_ 0 _< t_ 0 _<_ 1 _. Furthermore,_ ( _At_ 0 _, λt_ 0) _is a simple wall, with an index zero tropical disk connecting λt_ 0 _to bt_ 0 _by a linear segment with slope µb._ 

_Proof of Proposition 6.12._ The path of dual manifolds is given by moving the singular point _b_ 0 to _b_ 1 along a straight line, with a slight perturbation so that the Lagrangian point _λt_ does not lie on it. We rule out any other wall occuring in the path _{At}t∈_ [0 _,_ 1] as follows: Moving the singular point _bt_ inward has the effect of removing a rectangle from the dual affine manifold (see Figure 31), therefore, the notion of outward-pointing cones from Definition 5.18 is defined on the annulus part of _At_ . In a tropical graph in _At_ , paths emanating from focus-focus singularities are in the outward pointing cone,[7] and are contained in the annulus _At,_ ann (as in (45)) except if their starting point is _bt_ . Therefore, two such paths can merge only in the annulus, and a merged path can not be pass through the Lagrangian point _λt_ . Therefore, any wall in _At_ is a simple wall with the index zero tropical disk emanating from _bt_ . The path _{At}_ is such that a line of slope _µb_ passing through _λ_ can intersect the path _{bt}_ at only one point _bt_ 0, and there is exactly one wall configuration in the path _{At}t_ . □ 

_Notation_ 6.13 _._ (Sign convention) A mutation formula is defined for a simple wallcrossing satisfying a sign convention. Let _{_ ( _At, λt_ ) _}t∈_ [ _−ϵ,ϵ_ ] be a path of dual affine manifolds, which at _t_ = 0, crosses a simple wall at _t_ = 0 with index zero disk being the path ( _λ_ 0 _, b_ 0) in the primitive direction _µb ∈_ Z[2] . A mutation formula is defined for this wall-crossing if the vector path ( _λt, bt_ ) rotates counter-clockwise (with respect to the R[2] coordinates from the identification (44) ) at time _t_ = 0, and the wall-crossing is in the direction _ν_ = _µ[⊥] b_[,][where][for][a][vector][(] _[a, b]_[)] _[ ∈]_[R][2][,] 

(47) ( _a, b_ ) _[⊥]_ := ( _−b, a_ ) _._ 

> 7Note that this property is special to the particular kind of almost toric diagrams, in the monotone case, considered here. 

S. VENUGOPALAN AND C. WOODWARD 

68 

For example, in Figure 34, the index zero disk ( _λ_ 0 _, b_ 0) has primitive direction _µb_ = (1 _,_ 0), and _ν_ = (0 _,_ 1). 

A simple wall-crossing respecting the above sign convention changes the potential of the dual affine manifold by a mutation. 

**Proposition 6.14.** _Suppose the path {_ ( _At, λt_ ) _}t∈_ [ _−ϵ,ϵ_ ] _has no wall besides a simple wall at t_ = 0 _. Suppose the wall-crossing at t_ = 0 _respects the sign convention from Notation 6.13 and is in the direction ν. Then,_ 

**==> picture [259 x 13] intentionally omitted <==**

**==> picture [236 x 68] intentionally omitted <==**

**----- Start of picture text -----**<br>
t  =  −ϵ t  = 0<br>λ−ϵ<br>v−<br>e λ 0<br>v + v<br>**----- End of picture text -----**<br>


Figure 35. The edge length _ℓ_ ( _e_ ) goes to 0 in ( _A_ 0 _, λ_ 0). 

_Proof of Proposition 6.14._ By the proof of Theorem 6.8, the potential _W_ ( _At,λt_ ) is discontinuous at _t_ = _t_ 0 only if _At_ has a tropical disk of type 1C, which can occur only if _At_ 0 has a wall configuration, so _t_ 0 = 0. Furthermore, since _A_ 0 only has simple walls, the tropical disk of type 1C is of the form shown in Figure 35. 

**==> picture [341 x 60] intentionally omitted <==**

**----- Start of picture text -----**<br>
( k, l )<br>A 0 Aϵ ( k, l )<br>λ−ϵ b−ϵ ν µb b 0 ( k  +  k 1 , l ) ( −k 1 ,  0)<br>λ 0<br>A−ϵ λϵ<br>**----- End of picture text -----**<br>


Figure 36. Corresponding to a disk with initial slope ( _k, l_ ), _l ≥_ 0, in _A−ϵ_ , there is a bunched disk in _Aϵ_ for each _k_ 1. Here, the edge with direction ( _−k_ 1 _,_ 0) is a bunched edge. 

We count all such contributions. By the _GL_ (2 _,_ Z)-equivariance of the mutation formula (46) (see [39, Remark 4.2]), it is enough to consider the case when _ν_ = (0 _,_ 1) and _µb_ = _±_ (1 _,_ 0). Corresponding to any tropical disk with initial slope ( _k, l_ ), _l ≥_ 0 in _At_ , _t <_ 0, there is a bunched tropical disk of the form shown in Figure 36 in _At_ , _t >_ 0 for each _k_ 1 _∈_ [0 _, k_ ] _∩_ Z. Such a bunched tropical disk has a multiplicity of � _kl_ 1� by Proposition 4.18. Thus, going from _A−ϵ_ to _Aϵ_ transforms the potential as 

**==> picture [220 x 31] intentionally omitted <==**

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

69 

which is the same as the mutation _Sν_ . In a similar way, corresponding to a collection of terms _x[k] y[−][l]_ (1 + _x_ ) _[l]_ , _l ≥_ 0, in _WAϵ_ , there is a single term in _x[k] y[−][l]_ in _WA−ϵ_ . Therefore, (48) follows. □ 

**Theorem 6.15.** _Let X be a compact almost-toric manifold with polytope_ ∆= Φ( _X_ ) _⊂_ R[2] _and monotone Lagrangian L. Let_ ∆ _[′] ⊂_ R[2] _be a new almost-toric diagram obtained by a nodal slide that moves the focus-focus value b ∈_ ∆ _across λ_ = Φ( _L_ ) _in the direction ν ∈_ Z[2] _followed by transferring the cut as in Figure 37,_[8] _and let X[′] be the corresponding almost toric manifold with monotone Lagrangian L[′] ⊂ X[′] . The potentials of L and L[′] are related by a mutation WL′_ = _Sν[∗][W][L][.]_ 

**==> picture [205 x 121] intentionally omitted <==**

**----- Start of picture text -----**<br>
a a a<br>ν<br>b b<br>b<br>**----- End of picture text -----**<br>


Figure 37. Nodal slide in the direction _ν_ and transferring the cut respecting the sign convention of Notation 6.13. 

_Proof._ The potential in both cases is equal to the potential of the corresponding dual affine manifold _A_ , _A[′]_ as defined in (42), and by Proposition 6.12, the dual affine manifolds _A_ , _A[′]_ are connected by a path that crosses a simple wall. By Proposition 6.14, crossing a simple wall mutates the potential as claimed in the Theorem. □ 

**Theorem 6.16.** _Let X be a monotone almost toric four-manifold with a polytope_ ∆= Φ( _X_ ) _⊂_ t _[∨] whose facets have normal vectors µ_ ( _Q_ 1) _, . . . , µ_ ( _Qk_ ) _with convex hull N . Let L be a (unique if it exists) monotone moment fiber in X. The potential of L has coefficients_ 1 _at each νi and has binomial coefficients on the edges joining µ_ ( _Qi_ ) _and µ_ ( _Qi_ +1) _for each i. Namely if ζ is the k-th lattice point between µ_ ( _Qi_ ) _n_ +1 _and µ_ ( _Qi_ +1) _out of a total of n_ + 1 _then the coefficient of y[ζ] in WL is_ � _k_ � _._ 

We first prove a lemma about tropical graphs contributing to the potential that are on the boundary of the moment polytope. Let _b ∈ B_[foc] be a focus-focus value in a base diagram of Vianna type, close to a corner of ∆= Φ( _X_ ) that is the intersection of facets _Qi_ and _Qi_ +1. Let _Pb ⊂P_ be the collection of those polytopes meeting the cone _Cb_ on vectors _νi, νi_ +1 normal to adjacent facets _Qi, Qi_ +1 of ∆, with vertex of the cone _Cb_ at _λ_ = Φ( _L_ ), that is, the polytopes in the corner “near _b_ ”. 

> 8The Lagrangian fiber in the middle picture in Figure 37 is depicted as perturbed, to show that in the affine dual, _λ_ lies to the left of the line of motion of _b_ , so the sign convention of Figure 34 is followed. In the third picture, the cut is transferred so that the perturbed _λ_ lies in the part of the moment polytope whose embedding in R[2] is left unchanged. 

S. VENUGOPALAN AND C. WOODWARD 

70 

**Lemma 6.17.** _Suppose that_ Γ _is a tropical graph contributing to the potential with initial direction ζ that is in the convex hull of two vectors νi, νi_ +1 _normal to adjacent facets Qi, Qi_ +1 _of_ ∆ _, meeting at a vertex b ∈_ ∆ _. Then_ Γ _is contained in the union of polytopes P[∨] for P ∈Pb._ 

_Proof._ As before, we consider a polyhedral decomposition _P_ with Φ( _L_ ) contained in a “big inner piece” _P_ 0 as in Figure 21. Consider a coefficient _κν_ of _y[ν]_ in _WL_ where _ν_ is on the boundary of the Newton polygon Newt( _WL_ ) of _WL_ . Let _u_ : _C →X_ be a broken disk corresponding to the type Γ with inner piece _u_ 0 : _C_ 0 _→XP_ 0[.][Necessarily] _u_ 0 is a Blaschke disk with homology class 

**==> picture [145 x 16] intentionally omitted <==**

where _vi_ is the disk with degree one in the _i_ -th component from (26) in the direction _νRi_ . The assumption that _ν_ is in the convex hull of _νi, νi_ +1 implies 

**==> picture [74 x 11] intentionally omitted <==**

Hence 

**==> picture [210 x 12] intentionally omitted <==**

We claim that there is not enough energy left for the tropical graph to escape the corner. For each face _Qi ⊂_ Φ( _X_ ), let _Pi ⊂_ Φ( _X_ ) be the parallel face of one of the outer trapezoids opposite the face _Qi_ and let _δi_ be the symplectic volume of the corresponding divisor _XPi_ in _X P_ 0[.][We][may][assume][that][the][decomposition] _[P]_ is chosen with _Pi_ sufficiently close to _Qi_ so that the symplectic volume _δi_ of _XPi_ satisfies _δi > ϵ_ . Suppose _u_ has components _u_ 0, mapping to ~~_X_~~ _P_ 0[,][and] _[u]_[1][mapping][to] some _XP_ 1[.][Then] 

**==> picture [398 x 24] intentionally omitted <==**

_Proof of Theorem 6.16._ The proof is by reduction to case of potentials for cyclic quotient singularities computed previously. Let _L_ be a monotone torus fiber. By Lemma 6.17, the tropical graphs Γ that contribute to the _y[ν]_ -coefficient in _WL_ are contained in the union _Bb[∨]_[of][polytopes] _[P][ ∨]_[for] _[P][∈P][b]_[.][The][dual][complex] _[B] b[∨]_[is] the dual complex considered in Proposition 6.23 and the claim follows from that Theorem. □ 

6.3. **The Newton polygon of the potential.** We first show that the Newton polygon as the dual of the moment polytope, that is, the convex hull of the normal vectors to the facets. 

**Definition 6.18.** Let _W_ : (C _[×]_ ) _[n] →_ C be a Laurent polynomial given as a sum of terms 

**==> picture [90 x 25] intentionally omitted <==**

The _Newton polytope_ 

Newt( _WL_ ) = hull _{ν|κν_ = 0 _} ⊂_ R _[n]_ 

of _WL_ is the convex hull of the exponents _ν_ for non-zero coefficients _κν_ = 0 _._ 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

71 

**Theorem 6.19.** _Let X be an almost toric four-manifold with moment polytope_ Φ( _X_ ) _⊂_ R[2] _and let WL be the disk potential of a monotone torus fiber L ⊂ X. The Newton polytope_ Newt( _WL_ ) _⊂_ Z[2] _is equal to the dual_ Φ( _X_ ) _[∨] (as in Definition 5.5)._ 

_Proof._ The inclusion of Newt( _WL_ ) in the convex hull of the vectors _µ_ ( _Qi_ ) was shown in Proposition 5.13 (b). To prove the reverse inclusion, we need to show that the primitive normal _µj ∈_ tZ to a facet of Φ( _X_ ) appears in the Newton polygon of the potential _WL_ . For this purpose, we use the multiple cut _P_ in from Definition 5.3 (see Figure 21) with the polytope _P_ 0 containing Φ( _L_ ) being large enough that it contains (1 _− ϵ_ )Φ( _X_ ) for a small _ϵ >_ 0 determined later in the proof. For a broken map _u_ with initial slope _µj_ , the disk component _u_ 0 has Maslov index two and intersects a relative divisor of _XP_ 0 corresponding to a long facet _Qj ⊂ P_ 0. The broken map has a sphere component _u_ 1 that shares a tropical node with the disk _u_ 0 and that lies either in the neck piece _XQj_ or in the piece _XPj_ corresponding to the trapezoid _Pj ∈P_ adjacent to the facet _Qj_ . The piece _XPj_ has a fibration structure over P[1] and any sphere that projects to a non-constant sphere in P[1] has area bounded below by some constant _δ >_ 0 independent of _ϵ_ . As a result, for _ϵ_ sufficiently small, _u_ 1 lies in _XPj_ and must be a fiber. The sphere _u_ 1 does not meet the other relative divisors of _XPj_ , and thus the broken map _u_ just consists of _u_ 0 and _u_ 1. It follows that the number of such broken maps is equal to 1. In particular, each normal vector _νj_ to a facet appears in the Newton polygon. □ 

6.4. **Potentials of smoothings of toric singularities.** In this section we compute the disk potential for a class of non-compact toric manifolds which model del Pezzo surfaces locally. These are the so-called _smoothings of cyclic quotient T -singularity_ , which are the most general cyclic quotient surface singularities of algebraic varieties admitting a Q-Gorenstein smoothing. These singularities also possess an almost toric smoothing in the following sense: By an orbifold, we mean a Deligne-Mumford stack in the sense of [25]. The notions of symplectic orbifolds, toric orbifolds etc. are then obtained by obvious modifications of the usual definitions. 

**Definition 6.20.** An almost toric manifold _X_ a _smoothing_ of a toric orbifold _X_ 0 if the almost toric diagram ∆for _X_ is the same as that ∆0 of _X_ 0, with some collection of focus-focus values _b ∈ B_[foc] with branch cut pointing towards the vertex of ∆. 

We describe a toric model for cyclic surface singularities, and an almost toric smoothing for _T_ -singularities. 

- _Notation_ 6.21 _._ (a) A _cyclic surface singularity_ is a quotient of C[2] by a finite cyclic group and is specified by a pair of coprime integers _p_ , _q_ . 

   - (b) The singularity denoted by _p_[1][(1] _[, q]_[)][is][a][quotient][C][2] _[/]_[Υ][by][the][group] 

**==> picture [104 x 12] intentionally omitted <==**

with action given by 

**==> picture [114 x 12] intentionally omitted <==**

S. VENUGOPALAN AND C. WOODWARD 

72 

The function 

**==> picture [182 x 25] intentionally omitted <==**

descends to C _/_ Υ and is a moment map for a ( _S_[1] )[2] -action, and the moment polytope is the wedge 

**==> picture [182 x 14] intentionally omitted <==**

- (c) A _cyclic quotient T -singularity_ is a cyclic quotient singularity of the form 1[(1] _[, dpq][−]_[1).] Its smoothing is the almost toric manifold _X_ 0 with the 

- _dp_[2] same moment polytope as _X_ , along with _d_ -focus-focus singularities lying on the line _{λ_ ( _p, q_ ) : _λ ≥_ 0 _}_ . Note that the base diagram of _X_ is the most general one possible. Therefore, a cyclic surface singularity has an almost toric smoothing exactly if it is a _T_ -singularity. 

- (d) In the particular case when _p_ = 1, the _T_ -singularity is an _Ad−_ 1-singularity which we denote by _Md_ . Furthermore, the _T_ -singularity is the Z _p_ -quotient of an _Adp−_ 1-singularity, and the smoothing of example 7.8 in Evans [13] is fiberwise a Z _p_ -quotient of a smoothing of an _Adp−_ 1-singularity. 

**==> picture [150 x 24] intentionally omitted <==**

**----- Start of picture text -----**<br>
(0 ,  1) ( dp [2] , dpq − 1)<br>( p, q )<br>**----- End of picture text -----**<br>


**==> picture [308 x 16] intentionally omitted <==**

The sense in which _X_ is a smoothing of _X_ 0 is explained in Evans [13, Chapter 7]. The following example is the important one for our purposes: 

_Example_ 6.22 _._ Cyclic quotient _T_ -singularities are quotients of _An_ -singularities by finite groups. For coprime positive integers _q < p_ and an integer _d ≥_ 0 let _X_ 0 be a cyclic quotient of type 1[(1] _[, dpq][ −]_[1)][in][the][language][of][Evans][[][13][,][Chapter][7].][The] _dp_[2] orbifold _X_ 0 is equipped with a toric structure whose moment polytope is the cone 

**==> picture [172 x 14] intentionally omitted <==**

on the vectors (0 _,_ 1) and ( _dp_[2] _, dpq −_ 1). It has a smoothing _X_ with _d_ focus-focus singularities along a line in the _p, q_ direction. The dual polytope is a line segment with vertices at ( _−_ 1 _,_ 0) and ( _dpq −_ 1 _, −dp_[2] ). It contains _dp_ lattice points 

**==> picture [283 x 14] intentionally omitted <==**

In particular, the _smoothing of the An singularity_ is the almost toric manifold with polytope given by the cone on the rays (0 _,_ 1) and (1 _, n_ + 1) and _n_ + 1 focus-focus singularities along the ray (0 _,_ 1). 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

73 

Convexity of the cylindrical end, as in Ritter-Smith [41, Section 3] implies that monotone Lagrangians in such smoothings have well-defined potentials. For any monotone Lagrangian torus _L_ the moduli space of holomorphic disks bound _L_ with any particular energy bound is compact. As such _L_ has a well-defined _local potential_ 

**==> picture [93 x 13] intentionally omitted <==**

by counting Maslov index two holomorphic disks in _X_ with boundary in _L_ passing through a generic point in _L_ . 

**==> picture [338 x 100] intentionally omitted <==**

**----- Start of picture text -----**<br>
ρ<br>λ λ<br>Φ( L )<br>µ out<br>b Q [∨] Pb [∨] Pb [∨]<br>shear shear<br>Q [∨] µ out<br>ρ<br>B [∨] A ( X )<br>ρ<br>**----- End of picture text -----**<br>


Figure 39. Multiple cut on the _T_ -singularity, its dual complex _Bρ[∨]_ and dual affine _A_ ( _X_ ). 

**==> picture [325 x 95] intentionally omitted <==**

**----- Start of picture text -----**<br>
λ<br>Pb [∨] µb ν Pb [∨] ( Aϵ, λϵ ) =  A ( X )<br>( A−ϵ, λ−ϵ ) λ Cross wall in<br>direction ν = ( −p, −q )<br>**----- End of picture text -----**<br>


Figure 40. A tropical disk in a _T_ -singularity, before and after crossing the wall indicated by _µb_ . 

The main result of this subsection is the computation of the potential of a smoothing of a cyclic quotient _T_ -singularity: 

**Proposition 6.23.** _Let X be the smoothing of a cyclic quotient T -singularity X_ 0 _with normal vectors to facets µ_ 1 = ( _−_ 1 _,_ 0) _and µ_ 2 = ( _−_ 1 + _dpq, −dp_[2] ) _. Let L ⊂ X be a monotone Lagrangian torus fiber over a point λ ∈_ Φ( _X_ ) _. Thus_ 

**==> picture [71 x 12] intentionally omitted <==**

_and ℓ is further away from the vertex of_ Φ( _X_ ) _than any of the focus-focus singularities. The potential_ 

**==> picture [93 x 13] intentionally omitted <==**

_has coefficients given by binomial coefficients on the line segment from µ_ 1 _to µ_ 2 _; namely_ 

**==> picture [150 x 14] intentionally omitted <==**

S. VENUGOPALAN AND C. WOODWARD 

74 

_Proof of Proposition 6.23._ The proof is by applying the mutation formula. Under a standard decomposition, the affine dual manifold _A_ ( _X_ ) corresponding to a _T_ - singularity is as in Figure 39. This space is the same as ( _Aϵ, λϵ_ ) in Figure 40, which is obtained ( _A−ϵ, λ−ϵ_ ) by _d_ simple wall-crossings. Each of the wall-crossings respects the sign convention of Notation 6.13, and is in the direction _ν_ = ( _p, q_ ). In ( _A−ϵ, λ−ϵ_ ), there is only one rigid tropical disk, and it has slope ( _dpq −_ 1 _, −dp_[2] ). Then, 

**==> picture [388 x 53] intentionally omitted <==**

Figure 41. Four of of the eight tropical disks for the smoothing of an _A_ 3 singularity 

_Example_ 6.24 _._ We describe the computation for the disk potential of the spherical pendulum from Example 2.3. The potential of the toric fiber depicted in Theorem 42 on the left is 

**==> picture [152 x 14] intentionally omitted <==**

The potential of the moment fiber on the right is 

**==> picture [148 x 14] intentionally omitted <==**

The two potentials _WL, WL′_ are related by the _mutation formula_ 

(49) _y_ 1 = _y_ 1 _[′][,][y]_[2][=] _[ y]_ 2 _[′]_[(1 +] _[ y]_ 1 _[−]_[1][)] from Definition 6.10. 

The reader may deduce Proposition 6.23 by taking a decomposition separating the focus-focus values and applying Proposition 4.18 to each focus-focus value. However, we formally give the proof at the end of the next section after proving the mutation formula. 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

75 

Figure 42. Computing the disk potential of the spherical pendulum 

6.5. **The classification of potentials.** In this section we reprove the PascaleffTonkonog result [39] that the potentials are the mutable polynomials as expected, via a somewhat indirect argument involving their mutability. A similar argument was used in Pascaleff-Tonkonog [39], but the argument here is entirely combinatorial. We will need some definitions from Coates-Kasprzyk-Pitton-Tveiten [11]. 

**Definition 6.25.** A convex polytope _P_ in R[2] is _Fano_ if if it is of maximum dimension dim( _P_ ) = 2, its dual _P[∨]_ contains the origin, and the vertices _v ∈_ Vert( _P_ ) of _P_ are primitive lattice vectors in Z[2] . 

We give a slightly more general definition of mutation that the one in 6.10, to follow the terminology in [11]: 

**Definition 6.26.** Given a vector _w ∈_ Z[2] and a Laurent polynomial _a_ ( _y_ 1 _, y_ 2), the _mutation_ with respect to ( _w, a_ ) is the map 

**==> picture [182 x 14] intentionally omitted <==**

**Definition 6.27.** Given a Laurent polynomial _W_ the _mutation graph G_ ( _W_ ) is the graph whose vertices Vert( _G_ ( _W_ )) are repeated mutations _W[′]_ of _W_ and edges Edge( _G_ ( _W_ )) connecting _W, W[′]_ are mutations of _W_ to _W[′]_ . 

_Example_ 6.28 _._ Let _W_ ( _y_ 1 _, y_ 2) = _y_ 1 + _y_ 2 + ( _y_ 1 _y_ 2) _[−]_[1] be the standard potential for the projective plane. The associated graph is then the graph of Markov triples, as explained in [1, Section 3.2]. Indeed, in this case the possible mutations are those corresponding to edges, and correspond to the mutations of almost toric structure described in Definition 2.13, see the proof of Proposition 3.9 in [11]. 

**Definition 6.29.** A Laurent polynomial _W_ is is _maximally mutable_ if its Newton polygon _P_ = Newt( _W_ ) is a Fano polytope, the constant term of _W_ is zero, and the mutation graph _G_ ( _W_ ) of _W_ is maximal among all Laurent polynomials with Newton polytope _P_ . 

Given a Fano polytope _P ⊂_ R[2] and an edge _e_ , denote by _ve ∈_ Z[2] the direction of the edge _e_ and _ne ∈_ Z the _singularity content_ of the cone over _e_ in the sense of Coates-Kasprzyk-Pitton-Tveiten [11]. This ends the Definition. 

_Remark_ 6.30 _._ In the cases considered here, the singularity content _ne_ of an edge _e_ will simply be its lattice length. 

We recall from Coates-Kasprzyk-Pitton-Tveiten [11]: 

S. VENUGOPALAN AND C. WOODWARD 

76 

**Theorem 6.31.** _(Proposition 3.9, Theorem 3.12 of_ [11] _) Let W be a Laurent polynomial in two variables with Fano Newton polygon_ Newt( _W_ ) _. Then the following are equivalent: Denote by we ∈_ R[2] _the primitive inward pointing normal vector to e._ 

- _(a) W is maximally mutable;_ 

- _(b) W is mutable with respect to_ ( _we,_ (1 + _y[v][e]_ ) _[n][e]_ ) _for each edge e of_ Newt( _W_ ) _;_ 

- _(c) W coincides with one of the polynomials in Table 1, up to mutation and SL_ (2 _,_ Z) _-equivalence._ 

To apply the Theorem, we first prove, similar to Pascaleff-Tonkonog [40]: 

**Proposition 6.32.** _Let X be a compact monotone almost-toric four-manifold with monotone Lagrangian torus fiber L. The disk potential WL is maximally mutable._ 

_Proof._ Theorem 6.15 shows that the potential _WL′_ of the monotone moment fiber in the mutated diagram is a mutation of _WL._ Since _L[′]_ is a disk potential for a monotone Lagrangian, _WL′_ is a Laurent polynomial, and since it is an almost toric moment fiber, it has vanishing constant term by Proposition 4.9. It follow that _WL_ is mutable with respect to all three of the directions corresponding to the edges of Newt( _WL_ ). By Theorem 6.31, the mutation graph of _WL_ is maximal. □ 

**Corollary 6.33.** _Let L be the smooth monotone fiber of an almost toric structure on a monotone del Pezzo surface X. Then the disk potential WL is the mutation of the potentials in Table 1 corresponding to the del Pezzo surface X._ 

_Proof._ By Theorem 6.31 ( Proposition 3.9 of Coates-Kasprzyk-Pitton-Tveiten [11]) and Proposition 6.32, the disk potential _WL_ must be one of the potentials in Table 1, up to mutation. It remains to check that in fact the potential _WL_ is the potential for the del Pezzo surface _X_ containing _L_ . Thus the potential _WL_ must be the potential _W_ for a del Pezzo surface _X[′]_ with an almost toric diagram ∆ _[′]_ with the same volume as ∆. By Lemma 2.12, _X[′]_ has the same degree as _X_ . The only two del Pezzos with the same degree are (P[1] )[2] and Bl[1] P[2] , which both have _c_[2] 1[equal] to 8. We distinguish these two cases by a cohomology argument. Suppose that _WL_ is equivalent by mutation to _W_ which is the standard potential for either (P[1] )[2] and Bl[1] P[2] . By mutating the original almost toric diagram, we obtain an almost toric diagram ∆ _[′]_ with Lagrangian fiber _L[′]_ is equal to _WL′_ = _W._ We claim that in fact the diagram ∆ _[′]_ has at most one focus-focus value at any vertex. Indeed, if there is more than one focus-focus value at any corner then the normal vectors _vi, vi_ +1 at a vertex would be related by the composition of at least two shears, and so _|_ det( _vivi_ +1) _| ≥_ 2 which is not the case. After a nodal trade, we obtain a base diagram without focus-focus values. 

After absorbing the focus-focus values into the vertices by nodal trades, one obtains a toric structure on _X_ with polytope dual to Newt( _W_ ). The two possible toric varieties (P[1] )[2] and Bl[1] P[2] are not diffeomorphic, since (P[1] )[2] has no homology classes of square _−_ 1. Therefore, _WL_ must be mutation-equivalent to the toric potential _WL′_ on _X_ . □ 

_Remark_ 6.34 _._ An inspection of the tables in Vianna shows that Newt( _WL_ ) is the Newton polygon of the potential in Corollary 6.33 for a suitable diagram. For most 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

77 

|_X_|Manin Root System|_≈_Critval(_W_)|
|---|---|---|
|P2<br>P1 _×_P1<br>Bl1 P2<br>Bl2 P2<br>Bl3 P2<br>Bl4 P2<br>Bl5 P2<br>Bl6 P2<br>Bl7 P2<br>Bl8 P2|_A_1<br>_A_1<br>_A_1_⊕A_2<br>_A_4<br>_D_5<br>_E_6<br>_E_7<br>_E_8|3_α, α_3 = 1<br>4_,_0_⊕_2_, −_4<br>_−_0_._33_,_3_._8_, −_2_._23_±_1_._94_I_<br>(_−_1)_⊕_2_,_4_._73_, −_2_._86_±_0_._94_I_<br>(_−_2)_⊕_3_,_(_−_3)_⊕_2_,_6<br>(_−_3)_⊕_5_,_8_._09_, −_3_._09<br>(_−_4)_⊕_7_,_12<br>(_−_6)_⊕_8_,_21<br>(_−_12)_⊕_9_,_52<br>(_−_60)_⊕_10_,_372_._|



Table 2. Critical values of the potential for del Pezzos 

of these, the diagram giving the potential in 6.33 is easily read off. For example, for the del Pezzo of degree 1, the diagram is labelled _C_ 2 in Vianna’s Figure 16 in [49]. For the del Pezzo of degree 2, the diagram is labelled _B_ 2 in Figure 15 in [49]. 

## 7. Explicit computations for del Pezzo surfaces 

We now discuss each of these potentials in turn, with the goal of illustrating the tropical formulas by computing various coefficients of the potentials. For blow-ups at less than four points, the corresponding del Pezzo surfaces admit toric structures. For convenience, we record the critical values of the potentials for del Pezzos in Table 2. 

7.1. **Potentials of toric del Pezzo surfaces.** The disk potential of monotone toric manifolds was computed in Cho-Oh [9]. Suppose that a monotone toric variety _X_ has convex Delzant polytope _P_ . Denote the primitive normal vectors to the facets 

**==> picture [75 x 11] intentionally omitted <==**

The potential for monotone torus _L_ is the function 

**==> picture [148 x 34] intentionally omitted <==**

called the _Givental-Hori-Vafa potential_ , see Givental [15]. (Even if _L_ is not monotone, the potential for _L_ in the sense of (1) is equivalent to the Givental-Hori-Vafa potential by the results of Fukaya-Oh-Ohta-Ono [14].) 

7.1.1. _The projective plane._ Let _X_ = P[2] . The canonical toric structure has moment polytope Φ( _X_ ) a triangle as shown in Figure 43, where we have drawn the cartoon diagrams for the broken disks. By a _cartoon diagram_ , we mean a collection of subsets _Cv ⊂ P_ ( _v_ ) that are the moment images of some collection _u_ ~~_[′]_~~ _v_[of][smooth] (not necessarily pseudoholomorphic) maps isotopic to _uv_ . The tropical graphs Γ 

S. VENUGOPALAN AND C. WOODWARD 

78 

contributing to the potential _WL_ each have a single edge and no vertex. The critical values are of the form 3 _α_ for _α_[3] = 1. Another example is computed in Example 1.6. 

**==> picture [173 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
1 1 1<br>**----- End of picture text -----**<br>


Figure 43. Cartoon diagrams of Maslov-index-two disks in P[2] 

7.1.2. _The quadric surface._ Let _X_ = P[1] _×_ P[1] . The canonical toric structure has polytope given by a product of intervals 

**==> picture [100 x 13] intentionally omitted <==**

shown in Figure 44. The potential is the monotone torus fiber is 

_WL_ ( _y_ 1 _, y_ 2) = _y_ 1 + 1 _/y_ 1 + _y_ 2 + 1 _/y_ 2 _._ 

The critical points and values are easily found by hand to be 

Crit( _WL_ ) = _{y_ 1 = _±_ 1 _, y_ 2 = _±_ 1 _},_ Critval( _WL_ ) = _{±_ 4 _,_ 0 _}._ 

**==> picture [253 x 78] intentionally omitted <==**

**----- Start of picture text -----**<br>
w = 2,0,0,-2 w = 2,-2<br>**----- End of picture text -----**<br>


Figure 44. Two almost toric diagrams for P[1] _×_ P[1] and cartoon diagrams of Maslov-index-two disks 

A second almost toric diagram of the quadric surface is shown in Figure 44. This diagram and is related to the realization of _X_ as a compactification of the cotangent bundle of the two-sphere. The moment polytope 

**==> picture [191 x 13] intentionally omitted <==**

is a triangle, with the vertex at the bottom representing an _A_ 1-singularity. The potential for this almost toric structure is is 

**==> picture [194 x 12] intentionally omitted <==**

The critical values are easily found by hand to be 

**==> picture [114 x 12] intentionally omitted <==**

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

79 

Thus the monotone torus fiber _L[′]_ for the second moment polytope is not Hamiltonian isotopic to the monotone fiber _L_ for the first polytope. In fact this can be easily seen by readers familiar with the technology of open-closed maps: The Lagrangian _L[′]_ is disjoint from the Lagrangian two-sphere _L[′′]_ given by the zero-section, whose moment image connects the two focus-focus critical values near the bottom vertex of the diagram. The image of _HF_ ( _L[′]_ ) = _[∼] H_ ( _S_[2] ) = _[∼]_ C[2] under the open closed map is two-dimensional, since the classical, leading order term in the open closed map is non-zero. Hence _L[′′]_ split generates the 0-eigencategory, while _L[′]_ with two local systems generates the _±_ 4-eigencategories. 

7.1.3. _The del Pezzo of degree eight._ Let _X_ = Bl[1] P[2] . The toric structure has a polytope given by a trapezoid with normal vectors (1 _,_ 0) _,_ (0 _,_ 1) _,_ (0 _, −_ 1) _,_ (1 _, −_ 1) _._ The potential of the monotone torus is 

**==> picture [175 x 12] intentionally omitted <==**

We used Mathematica to compute the critical points and critical values in Table 2. 

7.1.4. _The del Pezzo of degree seven._ Let _X_ = Bl[2] P[2] be the twice blow-up of the projective plane. The toric structure has polytope Φ( _X_ ) given by a square with a corner cut off. In Figure 45, the cartoon diagrams Γ are drawn below the approximate images of the curves in the moment polytope. The tropical graphs associated to these curves can be reconstructed by examining the tangent vectors to the paths at the vertices. That is, to draw the tropical graph from the cartoon picture, one would simply straighten out the edges. In order to give a complete description, one would also have to describe the dual complex of some polyhedral decomposition, which we find tedious as the answer is independent of which polyhedral decomposition one chooses. The potential for the monotone torus may be computed as in Cho-Oh [9] as 

**==> picture [224 x 12] intentionally omitted <==**

There is also an almost toric structure on _X_ with two focus-focus singularities whose polytope ∆is a quadrilateral, is shown in Figure 45. The potential _WL′_ ( _y_ ) has six terms. Since the potentials _WL, WL′_ have five terms and six terms respectively, the tori _L, L[′]_ are not Hamiltonian isotopic. 

**==> picture [106 x 76] intentionally omitted <==**

Figure 45. Cartoon diagrams for Maslov-index-two disks in Bl[2] P[2] 

S. VENUGOPALAN AND C. WOODWARD 

80 

7.1.5. _The del Pezzo of degree six._ The thrice-blow up _X_ = Bl[3] P[2] is toric with moment polytope Φ( _X_ ) a hexagon as shown in Figure 46. The potential for the monotone torus fiber for this toric structure is 

**==> picture [257 x 11] intentionally omitted <==**

We used Mathematica to compute the critical points and critical values: 

Critval( _WL_ ) = _{−_ 2 _, −_ 3 _,_ 6 _}._ 

**==> picture [33 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
w = 6,-2,-3<br>**----- End of picture text -----**<br>


Figure 46. Cartoon diagrams for Maslov-index-two disks in Bl[3] P[2] 

## 7.2. **Potentials of non-toric del Pezzo surfaces.** 

7.2.1. _The del Pezzo of degree five._ The four-times blow-up of the projective plane does not admit a toric monotone symplectic form. An almost toric diagram for the monotone symplectic form with two focus-focus singularities is shown in Figure 47. The potential of the monotone Lagrangian torus is 

**==> picture [293 x 12] intentionally omitted <==**

Some of the cartoon diagrams contributing to the potential are shown in Figure 47. We used Mathematica to compute the critical points and critical values in Table 2. 

Figure 47. Cartoon diagrams of disks contributing to the potentials for Bl[4] P[2] 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

81 

7.2.2. _The del Pezzo of degree four._ The five-times blow up of the projective plane has an almost toric diagram shown in Figure 1, with corresponding potential 

_WL_ ( _y_ 1 _, y_ 2) = 2 _y_ 1 + 2 _y_ 2 + 2 _/y_ 1 + 2 _/y_ 2 + _y_ 1 _y_ 2 + _y_ 2 _/y_ 1 + _y_ 1 _/y_ 2 + 1 _/_ ( _y_ 1 _y_ 2) _._ 

The cartoon diagrams for the disks are shown in Figure 1. We used Mathematica to compute the critical points and critical values in Table 2. 

7.2.3. _The cubic surface._ The six-times blow-up has an almost toric diagram shown in Figure 48. The potential is given by a count of disks in Figure 48 and is given by _WL_ ( _y_ 1 _, y_ 2) = 3 _y_ 1 + 3 _y_ 2 + _y_ 1[2] _[/y]_[2][+] _[ y]_ 2[2] _[/y]_[1][+ 3] _[y]_[1] _[/y]_[2][+ 3] _[y]_[2] _[/y]_[1][+ 3] _[/y]_[1][+ 3] _[/y]_[2][+ 1] _[/]_[(] _[y]_[1] _[y]_[2][)] _[.]_ 

**==> picture [17 x 5] intentionally omitted <==**

**----- Start of picture text -----**<br>
w=-6,21<br>**----- End of picture text -----**<br>


Figure 48. Cartoon diagrams for disks contributing to the potentials for Bl[6] P[2] 

7.2.4. _The del Pezzo of degree two._ The seven-times blow-up has an almost toric base diagram shown in Figure 49. Some of the cartoon diagrams for the disks contributing to the potential are shown in Figure 49. The potential of the monotone torus fiber is 

_WL_ ( _y_ 1 _, y_ 2) = ( _y_ 2 + 1 _/y_ 2)(1 _/y_ 1[2][+ 4] _[/y]_[1][+ 6 + 4] _[y]_[1][+] _[ y]_ 1[2][) + (2] _[/y]_ 1[2][+ 8] _[/y]_[1][+ 8] _[y]_[1][+ 2] _[y]_ 1[2][)] _[.]_ We used Mathematica to compute the critical points and critical values in Table 2. 

7.2.5. _The del Pezzo of degree one._ The eight-times blow-up Bl[8] P[2] has an almost toric diagram described by Vianna [49] whose polytope is the triangle 

**==> picture [153 x 12] intentionally omitted <==**

shown in Figure 50. Some of the disks contributing to the potential, which has 372 terms, are shown in Figure 50. The potential _WL_ in Figure 50 is that in Akhtar et al [1, Figure 1]. Note that the coefficients along each edge of the Newton polygon are binomial, as justified in Theorem 6.16. We used Mathematica to compute the critical points and critical values shown in Table 2. 

82 

**==> picture [169 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
S. VENUGOPALAN AND C. WOODWARD<br>**----- End of picture text -----**<br>


**==> picture [13 x 6] intentionally omitted <==**

**----- Start of picture text -----**<br>
(2,0)<br>**----- End of picture text -----**<br>


**==> picture [100 x 98] intentionally omitted <==**

**----- Start of picture text -----**<br>
Coefficients of WL :<br>1 4 6 4 1<br>2 8 0 8 2<br>1 4 6 4 1<br>slope (1,0)<br>Critical values:<br>slope (1,-1)<br>w = -12,52<br>slope (2,-1)<br>**----- End of picture text -----**<br>


Figure 49. Cartoon diagrams for disks contributing to the potential for the torus for Bl[7] P[2] 

## Appendix A. Rigid spheres 

This appendix contains a digression on counting rigid holomorphic stable maps of genus zero in almost toric four-manifolds; these are closely related to the socalled _exceptional spheres_ in del Pezzo surfaces considered in the algebraic geometry literature, for example Testa [45]. 

**Definition A.1.** A _rigid sphere_ in an almost complex four-manifold _X_ is a holomorphic map _u_ : P[1] _→ X_ of Chern number _c_ 1( _u_ ) = 1. 

**Lemma A.2.** _Suppose X is a compact symplectic manifold of dimension four. Any rigid sphere u lies in a component of the moduli space M_ ( _X_ ) _of stable maps to X of expected dimension zero._ 

_Proof._ The dimension of the moduli space is the index of the linearized operator. By Riemann-Roch (see [33, Appendix C]) the dimension of _TuM_ Γ( _X_ ) at any rigid sphere _u_ is dim( _X_ ) + _c_ 1( _u_ ) _−_ 6 = 0, as claimed. □ 

Rigid spheres are closely related to the _exceptional spheres_ in the theory of del Pezzo surfaces, which are defined to be embedded smooth genus zero curves of selfintersection minus one. These two definitions are not quite the same in the case of del Pezzo surfaces of degree one; see the discussion in Remark A.5. The same techniques as in the case of disks shows the following: 

**Theorem A.3.** _The signed count E_ ( _X_ ) _∈_ Z _of rigid spheres is equal to a sum of multiplicities m_ (Γ) _∈_ Q _over tropical graphs_ Γ _in A_ ( _X_ ) _with all incoming edges colinear with the lines_ Θ _[±] b[emanating out of focus-focus values][ b][ ∈][B]_[foc] _[, and outgoing] edge normal to a facet of the moment polytope_ Φ( _X_ ) _. After desingularization, each contribution m_ (Γ) _is given by the same product of multiplicities m_ ( _v_ ) _over vertices v ∈_ Vert(Γ) _as above in Definition 1.4._ 

_Proof._ The proof is identical to that of Theorem 1.3 except for the fact that all incoming edges of the tropical graphs of the broken maps arising from the degeneration emanate from the focus-focus values _b ∈ B_[foc] . □ 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

83 

**==> picture [254 x 226] intentionally omitted <==**

**----- Start of picture text -----**<br>
Criticalw = -60,values372<br>1<br>(3,2)<br>9/2 -3/2<br>(0,2)<br>(3,0) (0,1) [(0,1)]<br>(3,0)<br>(2,-1) (3,-1)<br>1<br>9<br>**----- End of picture text -----**<br>


Figure 50. Cartoon diagrams for Maslov-index-two disks in Bl[8] P[2] 

By enumeration of graphs we obtain the following: 

**Theorem A.4.** _(see Testa_ [45] _) The number E_ ( _X_ ) _of rigid spheres u_ : P[1] _→ X is given in the following table._ 

**==> picture [350 x 29] intentionally omitted <==**

_Remark_ A.5 _._ In all but the case of the degree one del Pezzo, every stable map of non-zero lowest area has embedded image as explained in Testa [45]. However, for the degree one case there are 240 of _−_ 1 curves and 252 stable maps of Chern number 

S. VENUGOPALAN AND C. WOODWARD 

84 

one. See Figure 51 for the cartoon diagram and tropical graph for one of the 27 lines on the cubic surface. 

**==> picture [45 x 5] intentionally omitted <==**

**----- Start of picture text -----**<br>
E(X) = (3)(3)(3) = 27<br>**----- End of picture text -----**<br>


Figure 51. Cartoon diagrams (left) and tropical graphs (right) for one of the 27 lines on the cubic surface 

## Appendix B. Code for computing potentials and Jacobian rings 

In the course of writing the paper, we found it useful to have computer-assisted calculations of sets of critical values of potentials and subrings of the Jacobian ring. We include the code for these computations below. We begin with the computation of the critical values for P[2] using Mathematica: In the code below, the variables have the following meaning: 

Critpoint the set of critical points Critval the set of critical values Crithess the set of determinants of the Hessian at each of the critical values For _X_ = P[2] , all of the determinants in Crithess are non-zero which indicates that the Landau-Ginzburg potential _w_ is Morse in this case. 

```
w[y1_,y2_]=y1+y2+1/(y1*y2);
=
g[y1_,y2_]{y1*D[w[y1,y2],y1],y2*D[w[y1,y2],y2]};
=
h[y1_,y2_]D[w[y1,y2],{{y1,y2}},{{y1,y2}}];
Critpoint=NSolve[g[y1,y2]==0,{y1,y2}]
Critval=w[y1,y2]/.Critpoint
Crithess=Det[h[y1,y2]]/.Critpoint
{{y1->-0.5+0.866025I,
y2->-0.5+0.866025I},{y1->-0.5-0.866025I,
y2->-0.5-0.866025I},{y1->1.,y2->1.}}
{-1.5+2.59808I,-1.5-2.59808I,3.}
{-1.5+2.59808I,-1.5-2.59808I,3.}
```

The ring generated by the potential _W_ in Jac( _W_ ) for _X_ = P[2] can be computed by hand, or (as practice for later more complicated example) verified using the following code from Macaulay2: 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

85 

```
i1:r1=QQ[y1,y2,Y1,Y2]/(y1*Y1-1,y2*Y2-1,y1-Y1*Y2,y2-Y1*Y2)
i2:r2=QQ[z]
```

`i4 : gen = map(r1,r2,{y1+y2+Y1*Y2}) i5 : i1= kernel gen i6 : factor i1_0 o6 = (z-3)(z^2+3z+9)` Mathematica can be used to compute the critical points P[1] _×_ P[1] with its standard almost toric diagram. For 

`w[y1_, y2_] = y1 + 1/y1 + y2 + 1/y2` we obtain critical values `{4., 0., 0., -4.}` For _X_ = P[1] _×_ P[1] the potential for the almost toric diagram whose moment polytope is a triangle has potential `w[y1_, y2_] = y1*y2 + y2/y1 + 1/y2 + 2*y2;` The critical values are `{4, -4.}` 

This gives an example of an almost toric diagram where the Fukaya category cannot be generated by monotone moment fibers, since the critical value 0 does not occur. For _X_ = Bl[1] P[2] we have using Mathematica for the toric potential: `w[y1_, y2_] = y1 + y2 + 1/y2 + y2/y1; Critval = {-0.33, 3.8, -2.23 + 1.94 I, -2.23 - 1.94 I}` For _X_ = Bl[2] P[2] with the standard toric structure we have via Mathematica: `w[y1_, y2_] = y1 + y2 + 1/y1 + 1/y2 + 1/(y1*y2) ; Critval = {-1., -1., 4.73, -2.86 + 0.94 I, -2.86 - 0.94 I}` The ring generated by _W_ in Jac( _W_ ) for _X_ = Bl[2] P[2] was calculated using Macaulay2. `r1 = QQ[y1,y2,Y1,Y2]/(y1*Y1 -1, y1*Y2-1, y1 - Y1 + y1*y2, y2 - Y2 + y1*y2); r2 = QQ[z]; = gen map(r1,r2,{y1+Y1+y1+Y2+y1*y2}); i1= kernel gen; factor i1_0 o16 = (z+1)(z^3 +z^2 -18z-43)` 

. The critical points for the toric structure on _X_ = Bl[3] P[2] were computed via Mathematica: 

`w[y1_, y2_] = y1 + y2 + 1/y1 + 1/y2 + y1*y2 + 1/(y1*y2); Critval = {-3., -3., -2., -2., 6., -2.}` The ring generated by _W_ in Jac( _W_ ) for _X_ = Bl[3] P[2] was computed using Macaulay2. `r1 = QQ[y1,y2,Y1,Y2]/(y1*Y1 -1, y*Y2-1); w = y1 + y2 + Y1 + Y2 + y1*y2 + Y1*Y2; d1 = y1*diff(y1,w) - Y1*diff(Y1,w); d2= y2*diff(y2,w) - Y2*diff(Y2,w); = r2=r1/(d1,d2); r3=QQ[z]; gen map(r2,r3,{w}); i1= kernel gen; factor i1_0` 

S. VENUGOPALAN AND C. WOODWARD 

86 

```
o9=(z-6)(z+2)(z+3)
```

Mathematica gives the critical values for _X_ = Bl[4] P[2] : 

```
w[y1_,y2_]=2y1+2y2+1/y1+1/y2+y1*y2+y1/y2+y2/y1;
Critval={-3.,-3.,-3.,-3.,8.09,-3.09,-3.}
```

Note that the potential is not Morse, as the Hessian is degenerate for some of the _−_ 3 critical points. The critical values for _X_ = Bl[5] P[2] are 

```
w[y1_,y2_]=2y1+2y2+2/y1+2/y2+y1*y2+y1/y2+y2/y1+1/(y1*y2);
Critval={-4.,-4.,-4.,-4.,-4.,-4.,12.,-4.}
```

In this case, all the _−_ 4 critical points are degenerate; mathematica gives a somewhat misleading answer in this case since the critical set is not isolated. The ring generated by _w_ in the Jacobian ring was computed using Macaulay. 

```
r1=QQ[y1,y2,Y1,Y2]/(y1*Y1-1,y2*Y2-1);
w=2*y1+2*y2+2*Y1+2*Y2+y1*Y2+y2*Y1+y1*y2+Y1*Y2;
d1=y1*diff(y1,w)-Y1*diff(Y1,w);
-
d2=y2*diff(y2,w)Y2*diff(Y2,w);r2=r1/(d1,d2);
r3=QQ[z];gen=map(r2,r3,{w});i1=kernelgen;factori1_0
```

```
o10=(z-12)(z+4)
```

This sub-ring is dimension two, as opposed to the three-dimension ring one expects. Thus the Jacobian ring of the disk potential, and so not equal to the quantum cohomology; see Barrott [3] for the potential that does have the correct Jacobian ring. 

The code for computing the potential and its critical points in Mathematica for _X_ = Bl[6] P[2] is: `w[y1_, y2_] = 3 y1 + 3 y2 + y1^2/y2 + y2^2/y1 + 3 y1/y2 + 3 y2/y1 + 3/y1 + 3/y2 + 1/(y1*y2); = g[y1_, y2_] {y1*D[w[y1, y2], y1], y2*D[w[y1, y2], y2]}; = h[y1_,y2_] D[w[y1,y2],{{y1,y2}},{{y1,y2}}]; Critpoint = NSolve [ g[y1, y2] == 0, {y1, y2}]; = Critpointapprox {Round[y1, .01], Round[y2, .01]} /. Critpoint Critval = Round[w[y1, y2], .01] /. Critpoint Crithess = Round[Det[h[y1, y2]], .01] /. Critpoint {{2.12 + 0.22 I, -3.12 - 0.22 I}, {2.09 + 0.23 I, -3.09 - 0.23 I}, {-0.49 - 0.14 I, -0.51 + 0.14 I}, {-0.49 - 0.14 I, -0.51 + 0.14 I}, {-0.6 + 0.62 I, -0.4 - 0.62 I}, {-0.6 + 0.62 I, -0.4 - 0.62 I}, {-0.52 - 0.69 I, -0.48 + 0.69 I}, {-0.52 - 0.69 I, -0.48 + 0.69 I}, {1., 1.}} {-6., -6., -6., -6., -6., -6., -6., -6., 21.} {0., 0., 0., 0., 0., 0., 0., 0., 243.}` 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

87 

There are only four critical points with critical values _w_ = _−_ 6, and one critical point with value _w_ = 21. The first Chern class obeys the relation ( _c_ 1 +6)[2] ( _c_ 1 _−_ 21) = 0, as a special case of the computations Givental [16], as explained in Sheridan’s appendix in [43]. In particular _c_ 1‘ _−_ 21 is a generalized eigenvector of _c_ 1 + 6 rather than an actual eigenvector. On other hand, one might compare the potential above to the potential used in Sheridan [43], which is of the correct dimension: 

`r1 = QQ[a,b,c,d]; w = a^3+b^3+c^3+d^3-a*b*c*d - 6 ; r2 = r1/(3*a^2 - b*c*d, 3*b^2 - a*c*d, 3*c^2 - a*b*d, 3*d^2 - a*b*c); r3=QQ[z]; gen = map(r2,r3,{w}); i1= kernel gen; factor i1_0 o7 = (z-21)(z+6)^2` The code for computing the critical points for _X_ = Bl[7] P[2] via Mathematica is: `w[y1_, y2_] = (y2 + 1/y2)*(1/y1^2 + 4/y1 + 6 + 4 y1 + y1^2) + (2/y1^2 + 8/y1 + 8 y1 + 2 y1^2); Critval = {-12., -12., -12., -12., -12., -12., -12., -12., 52., -12., -12., \ -12., -12., -12., -12., -12.}` The ring generated by _c_ 1 was computed using Macaulay2: `r1 = QQ[y1,Y1,y2,Y2]/(y1*Y1 -1, y2*Y2-1); w = ((1 + y1 + y2)^4 - 12 *y1 * y2)*Y1*Y2; d1 = y1*diff(y1,w) - Y1*diff(Y1,w); - d2= y2*diff(y2,w) Y2*diff(Y2,w); r2=r1/(d1,d2); r3=QQ[z]; gen = map(r2,r3,{w}); i1= kernel gen; factor i1_0 o9 = (z-52)(z+12)` 

The following Macaulay2 computation shows that the Jacobian ring of the disk potential is not isomorphic to the quantum cohomology, since the sub-ring generated by _c_ 1( _X_ ) has rank two. 

`r1 = QQ[y1,Y1,y2,Y2]/(y1*Y1 -1, y2*Y2-1); w = (y2 + Y2)*(Y1^2 + 4*Y1 + 6 + 4 * y1 + y1^2) + (2*Y1^2 + 8*Y1 + 8 * y1 + 2 * y1^2); d1 = y1*diff(y1,w) - Y1*diff(Y1,w); - d2= y2*diff(y2,w) Y2*diff(Y2,w); r2=r1/(d1,d2); r3=QQ[z]; gen = map(r2,r3,{w}); i1= kernel gen; factor i1_0 o9 = (z-52)(z+12)` The Hori-Vafa-style mirror, roughly adapted from [23], has better properties. It is given in Macaulay2 by the following code: `i66 : r1 = QQ[a,b,c,d]; w = a^4+b^4+c^4+d^4-a^2*b*c*d ; r2 = r1/(4*a^3 - 2*a*b*c*d, 4*b^3 - a^2*c*d, 4*c^3 - a^2*b*d, 4*d^3 - a^2*b*c); = r3=QQ[z];gen map(r2,r3,{w}); i1= kernel gen; factor i1_0 o72 = (z)^2(z-64)` In particular, the sub-ring generated by _c_ 1( _X_ ) = _w_ has dimension four, as expected. 

S. VENUGOPALAN AND C. WOODWARD 

88 

The code for computing the critical points for _X_ = Bl[8] P[2] via Mathematica is: `w[y1_, y2_] = (1 + y1)^9 / (y1^6 * y2) + (3 + 18 y1 + 45 y1^2 + 45 y1^4 + 18 y1^5 + 3 y1^6)/ y1^3 + (3 + 9 y1 + 9 y1^2 + 3 y1^3 )*y2 + y1^3*y2^2; Critval = {-60., -60., -60., -60., -60., -60., -60., -60., -60., -60., -60., \ -60., -60., -60., -60., -60., -60., -60., -60., -60., -60., -60., \ -60., -60., -60., 372.}` 

The subring generated by _c_ 1 was computed using Macaulay2: `i1 : r1 = QQ[y1,y2,Y1,Y2]/(y1*Y1 -1, y2*Y2-1) i4 : w = (1 + y1)^9 * (Y1^6 * Y2) + (3 + 18 * y1 + 45 * y1^2 + 45 * y1^4 + 18 * y1^5 + 3 * y1^6) * Y1^3 + (3 + 9 * y1 + 9 * y1^2 + 3 * y1^3 )*y2 + y1^3*y2^2; d1 = y1*diff(y1,w) - Y1*diff(X,w); d2= y2*diff(y2,w) - Y2*diff(Y2,w); r2=r1/(d1,d2); r3=QQ[z]; gen = map(r2,r3,{w}); i1= kernel gen; factor i1_0 o11 = (z-372)(z+60)` 

The ring generated by _z_ = _c_ 1 _−_ 60 is given by the Macaulay2 code: `r1 = QQ[a,b,c,d]; w = a^6+b^6+c^6+d^6-a*b^2*c^3*d ; r2 = r1/(6*a^5 - b^2*c^3*d, 6*b^5 - a*2*b*c^3*d, - - 6*c^5 a*b^2*3*c^2*d, 6*d^5 a*b^2*c^3); r3=QQ[z]; gen = map(r2,r3,{w}); i1= kernel gen; factor i1_0 o21 = (z)^2(z-432)` 

Thus the Jacobian ring of the Hori-Vafa potential re-produces the correct sub-ring generated by the canonical class, while the disk potential of the monotone torus does not. 

## References 

- [1] Mohammad Akhtar, Tom Coates, Alessio Corti, Liana Heuberger, Alexander Kasprzyk, Alessandro Oneto, Andrea Petracci, Thomas Prince, and Ketil Tveiten. Mirror symmetry and the classification of orbifold del Pezzo surfaces. _Proc. Amer. Math. Soc._ , 144(2):513–527, 2016. 

> [2] Sam Bardwell-Evans, Man-Wai Mandy Cheung, Hansol Hong, and Yu-Shen Lin. Scattering diagrams from holomorphic discs in log Calabi-Yau surfaces. _J. Differential Geom._ , 130(1):–, 2025. 

> [3] Lawrence Jack Barrott. Explicit equations for mirror families to log Calabi-Yau surfaces. _Bull. Korean Math. Soc._ , 57(1):139–165, 2020. 

> [4] Jim Bryan and Rahul Pandharipande. The local Gromov-Witten theory of curves. _J. Amer. Math. Soc._ , 21(1):101–136, 2008. With an appendix by Bryan, C. Faber, A. Okounkov and Pandharipande. 

> [5] Michael Carl, Max Pumperla, and Bernd Siebert. A tropical view on Landau-Ginzburg models. _Acta Math. Sin. (Engl. Ser.)_ , 40(1):329–382, 2024. 

- [6] Fran¸cois Charest and Chris Woodward. Floer trajectories and stabilizing divisors. _J. Fixed Point Theory Appl._ , 19(2):1165–1236, 2017. 

- [7] Fran¸cois Charest and Chris T. Woodward. Floer cohomology and flips. _Mem. Amer. Math. Soc._ , 279(1372):v+166, 2022. 

- [8] Man-Wai Cheung and Travis Mandel. Donaldson-Thomas invariants from tropical disks. _Selecta Math. (N.S.)_ , 26(4):Paper No. 57, 46, 2020. 

- [9] Cheol-Hyun Cho and Yong-Geun Oh. Floer cohomology and disc instantons of Lagrangian torus fibers in Fano toric manifolds. _Asian J. Math._ , 10(4):773–814, 2006. 

DISK POTENTIALS OF ALMOST TORIC MANIFOLDS 

89 

- [10] Kai Cieliebak and Klaus Mohnke. Symplectic hypersurfaces and transversality in GromovWitten theory. _J. Symplectic Geom._ , 5(3):281–356, 2007. 

- [11] Tom Coates, Alexander M. Kasprzyk, Giuseppe Pitton, and Ketil Tveiten. Maximally mutable Laurent polynomials. _Proc. A._ , 477(2254):Paper No. 20210584, 21, 2021. 

- [12] J. J. Duistermaat. On global action-angle coordinates. _Comm. Pure Appl. Math._ , 33(6):687– 706, 1980. 

- [13] Jonny Evans. _Lectures on Lagrangian torus fibrations_ , volume 105 of _London Mathematical Society Student Texts_ . Cambridge University Press, Cambridge, 2023. 

- [14] Kenji Fukaya, Yong-Geun Oh, Hiroshi Ohta, and Kaoru Ono. Lagrangian Floer theory and mirror symmetry on compact toric manifolds. _Ast´erisque_ , (376):vi+340, 2016. 

- [15] Alexander B. Givental. Homological geometry and mirror symmetry. In _Proceedings of the International Congress of Mathematicians, Vol. 1, 2 (Z¨urich, 1994)_ , pages 472–480. Birkh¨auser, Basel, 1995. 

- [16] Alexander B. Givental. Equivariant Gromov-Witten invariants. _Internat. Math. Res. Notices_ , (13):613–663, 1996. 

- [17] Tim Graefnitz. Tropical correspondence for smooth del Pezzo log Calabi-Yau pairs. _J. Algebraic Geom._ , 31(4):687–749, 2022. 

- [18] Tim Gr¨afnitz. Theta functions, broken lines and 2-marked log Gromov-Witten invariants. _Manuscripta Math._ , 176(4):Paper No. 41, 34, 2025. 

- [19] Tim Gr¨afnitz, Helge Ruddat, and Eric Zaslow. The proper Landau-Ginzburg potential is the open mirror map. _Adv. Math._ , 447:Paper No. 109639, 69, 2024. 

- [20] Mark Gross. _Tropical geometry and mirror symmetry_ , volume 114 of _CBMS Regional Conference Series in Mathematics_ . Published for the Conference Board of the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI, 2011. 

- [21] Victor Guillemin. Kaehler structures on toric varieties. _J. Differential Geom._ , 40(2):285–309, 1994. 

- [22] Victor Guillemin. _Moment maps and combinatorial invariants of Hamiltonian T[n] -spaces_ , volume 122 of _Progress in Mathematics_ . Birkh¨auser Boston, Inc., Boston, MA, 1994. 

- [23] Kentaro Hori and Cumrun Vafa. Mirror symmetry, 2000. 

- [24] Siu-Cheong Lau, Tsung-Ju Lee, and Yu-Shen Lin. Syz mirror symmetry for del pezzo surfaces and affine structures. _arXiv: 2206.01681_ , 2024. 

- [25] Eugene Lerman. Orbifolds as stacks? _Enseign. Math. (2)_ , 56(3-4):315–363, 2010. 

- [26] Naichung Conan Leung and Margaret Symington. Almost toric symplectic four-manifolds. _J. Symplectic Geom._ , 8(2):143–187, 2010. 

- [27] Tian-Jun Li, Jie Min, and Shengzhen Ning. Almost toric presentations of symplectic log calabiyau pairs. _arXiv: 2303.09964_ , 2023. 

- [28] Yu-Shen Lin. Open Gromov-Witten invariants on elliptic K3 surfaces and wall-crossing. _Comm. Math. Phys._ , 349(1):109–164, 2017. 

- [29] Yu-Shen Lin. On the tropical discs counting on elliptic k3 surfaces with general singular fibres. _arXiv: 1710.10625_ , 2019. 

- [30] Wendelin Lutz. Mirrors to del Pezzo surfaces and the classification of _T_ -polygons. _SIGMA Symmetry Integrability Geom. Methods Appl._ , 20:Paper No. 095, 20, 2024. 

- [31] Yu. I. Manin. _Cubic forms_ , volume 4 of _North-Holland Mathematical Library_ . North-Holland Publishing Co., Amsterdam, second edition, 1986. Algebra, geometry, arithmetic, Translated from the Russian by M. Hazewinkel. 

- [32] Dusa McDuff. From symplectic deformation to isotopy. In _Topics in symplectic_ 4 _-manifolds (Irvine, CA, 1996)_ , First Int. Press Lect. Ser., I, pages 85–99. Int. Press, Cambridge, MA, 1998. 

- [33] Dusa McDuff and Dietmar Salamon. _J-holomorphic curves and symplectic topology_ , volume 52 of _American Mathematical Society Colloquium Publications_ . American Mathematical Society, Providence, RI, second edition, 2012. 

- [34] Grigory Mikhalkin. Enumerative tropical algebraic geometry in R[2] . _J. Amer. Math. Soc._ , 18(2):313–377, 2005. 

90 

## S. VENUGOPALAN AND C. WOODWARD 

- [35] Takeo Nishinou and Bernd Siebert. Toric degenerations of toric varieties and tropical curves. _Duke Math. J._ , 135(1):1–51, 2006. 

- [36] Yong-Geun Oh. Floer cohomology of Lagrangian intersections and pseudo-holomorphic disks. I. _Comm. Pure Appl. Math._ , 46(7):949–993, 1993. 

- [37] Hiroshi Ohta and Kaoru Ono. Symplectic 4-manifolds with _b_[+] 2[=][1.][In] _[Geometry][and][physics] (Aarhus, 1995)_ , volume 184 of _Lecture Notes in Pure and Appl. Math._ , pages 237–244. Dekker, New York, 1997. 

- [38] Brett Parker. Tropical enumeration of curves in blowups of C _P_[2] . _J. Differential Geom._ , 129(1):165–223, 2025. 

- [39] James Pascaleff and Dmitry Tonkonog. The wall-crossing formula and Lagrangian mutations. _Adv. Math._ , 361:106850, 67, 2020. 

- [40] James Pascaleff and Dmitry Tonkonog. The wall-crossing formula and Lagrangian mutations. _Adv. Math._ , 361:106850, 67, 2020. 

- [41] Alexander F. Ritter and Ivan Smith. The monotone wrapped Fukaya category and the openclosed string map. _Selecta Math. (N.S.)_ , 23(1):533–642, 2017. 

- [42] Vera V. Serganova and Alexei N. Skorobogatov. Adjoint representation of E8 and del Pezzo surfaces of degree 1. _Ann. Inst. Fourier (Grenoble)_ , 61(6):2337–2360 (2012), 2011. 

- [43] Nick Sheridan. On the Fukaya category of a Fano hypersurface in projective space. _Publ. Math. Inst. Hautes Etudes[´] Sci._ , 124:165–317, 2016. 

- [44] Margaret Symington. Four dimensions from two in symplectic topology. In _Topology and geometry of manifolds (Athens, GA, 2001)_ , volume 71 of _Proc. Sympos. Pure Math._ , pages 153–208. Amer. Math. Soc., Providence, RI, 2003. 

- [45] Damiano Testa. The irreducibility of the spaces of rational curves on del Pezzo surfaces. _arXiv: math/0609355_ , 2006. 

- [46] Sushmita Venugopalan and Chris Woodward. Tropical Fukaya algebras. _arXiv: 2004.14314_ , 2020. 

- [47] Sushmita Venugopalan and Chris Woodward. Splitting the diagonal for broken maps. _arXiv: 2504.15583_ , 2025. 

- [48] Sushmita Venugopalan, Chris T. Woodward, and Guangbo Xu. Fukaya categories of blowups. _J. Inst. Math. Jussieu_ , 25(1):85–214, 2026. 

- [49] Renato Vianna. Infinitely many monotone Lagrangian tori in del Pezzo surfaces. _arXiv: 1602.03356_ , 2016. 

- [50] Renato Ferreira de Velloso Vianna. Infinitely many exotic monotone Lagrangian tori in CP[2] . _J. Topol._ , 9(2):535–551, 2016. 

- [51] Alan Weinstein. Removing intersections of Lagrangian immersions. _Illinois J. Math._ , 27(3):484– 500, 1983. 

- [52] Chris Woodward. Disks bounding tropical lagrangians in almost toric manifolds. In preparation. 

