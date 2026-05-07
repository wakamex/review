# **LEGENDRIAN POSITION OF VEERING TRIANGULATIONS** 

## CHI CHEUK TSANG 

Abstract. We make a first step towards connecting the theory of veering triangulations and bicontact structures as tools for studying (pseudo-)Anosov flows: We show that given a veering triangulation corresponding to an Anosov flow with orientable stable and unstable foliations, the edges of the triangulation can be realized as Legendrian arcs with respect to a strongly adapted bicontact structure that supports the Anosov flow. Along the way, we show that every veering triangulation can be placed in ‘steady position’, where each pair of edge projections that intersect in the orbit space only intersect once transversely. By a previous result of the author, this implies that horizontal surgery of veering triangulations correspond to horizontal Goodman surgery of pseudo-Anosov flows. 

## 1. Introduction 

A flow on a 3-manifold is **Anosov** if it has a contracting and an expanding direction. A flow is **pseudo-Anosov** if it is Anosov except possibly having finitely many singular orbits where the contracting and expanding directions are pronged. Aside from their interest as dynamical objects, work by many authors have shown a deep connection between these flows and many other topological and geometric structures on 3-manifolds, including taut foliations [Mos96, Cal00, Fen02], hyperbolic geometry [Fen16, FL25], and Floer homology [AT25a, AT25b, Zun]. 

In recent years, a plethora of new tools for studying (pseudo-)Anosov flows have emerged. These include veering triangulations [FSS25, Tsa23b], orbit spaces [BFM25, BBM24, BM26], geometric types [Iak22, Iak25], and bicontact structures [Mit95, CLMM22, Hoz24, Mas25, Sal25, AS]. While there is some understanding of the relation between the first three of these [LMT23, SS24, SS23, Hal25], the literature on bicontact structures has been rather isolated from this cluster of ideas. The purpose of this paper is to take a first step in making a connection, by showing an interaction between veering triangulations and bicontact structures. 

Let us first give a brief review of these objects. A **veering triangulation** is an ideal triangulation of an oriented 3-manifold along with combinatorial data, including coorientations on the faces and a coloring of the edges by red and blue, satisfying certain conditions. Given a pseudo-Anosov flow _ϕ_ on a closed oriented 3-manifold _M_ with no perfect fits relative to _C_ , there is an associated veering triangulation ∆of the drilled 3-manifold _M \C_ . It is known that ∆can be placed in **transverse position** with respect to _ϕ_ in _M_ [LMT23]. This means that the faces of ∆can be arranged to be positively transverse to _ϕ_ , and the edges of ∆can be arranged to be transverse to the 

1 

2 

## CHI CHEUK TSANG 

**==> picture [34 x 11] intentionally omitted <==**

**----- Start of picture text -----**<br>
( ξ + , ξ− )<br>**----- End of picture text -----**<br>


Figure 1. Left: The edges of a veering triangulation rotate towards the stable foliation as one moves along the flow. Right: The contact planes of a supporting bicontact structure ( _ξ_ + _, ξ−_ ) rotate towards the stable foliation as one moves along the flow. 

stable and unstable foliations of _ϕ_ . In fact, once placed in this position, ∆determines _ϕ_ up to isotopic equivalence. 

In more detail, the edges of ∆are determined by the **edge rectangles** in the orbit space of _ϕ_ . These are rectangles with two opposite corners on points of _C_[�] . Taking the convention that the stable foliation is vertical and the unstable foliation is horizontal in the orbit space, the rectangle corresponding to the top edge of each tetrahedron is taller and thinner than that of the bottom edge. That is, as one moves along the flow, the rectangles ‘rotate towards’ the stable foliation. The color of the edges determine which quadrant the rotation takes place in: the red edges are **positive** , i.e. lie in the first and third quadrants, while the blue edges are **negative** , i.e. lie in the second and fourth quadrants. See Figure 1 left. 

Meanwhile, for the purposes of this paper, a **bicontact structure** is a pair ( _ξ_ + _, ξ−_ ) consisting of a positive contact structure and a negative contact structure that intersects transversely at every point. We say that a bicontact structure **supports** a flow _ϕ_ if the generating vector field _ϕ_[˙] is contained in the intersection _ξ_ + _∩ ξ−_ . It is known that every Anosov flow with orientable stable and unstable foliations is supported by a bicontact structure. Conversely, if a bicontact structure ( _ξ_ + _, ξ−_ ) is **strongly adapted** , meaning _ξ_ + admits a contact form whose Reeb flow _R_ + is contained in _ξ−_ , then it supports an Anosov flow with orientable stable and unstable foliations. 

When a bicontact structure ( _ξ_ + _, ξ−_ ) supports an Anosov flow, the contact condition forces the contact planes _ξ_ + and _ξ−_ to rotate towards the stable foliation as one moves along the flow, with _ξ_ + doing so within the second and fourth quadrants, and _ξ−_ doing so within the first and third quadrants. See Figure 1 right. 

Notice the similarity in behaviors of the blue/red edges of veering triangulations and the positive/negative contact planes of bicontact structures, respectively. Our main theorem makes this observation precise: 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

3 

**Theorem 1.1.** _Let ϕ be an Anosov flow with orientable stable and unstable foliations on a closed oriented 3-manifold M with no perfect fits relative to C. Let_ ∆ _be the veering triangulation associated to_ ( _ϕ, C_ ) _. Then there exists a strongly adapted bicontact structure_ ( _ξ_ + _, ξ−_ ) _on M supporting ϕ, such that_ ∆ _can be put in transverse position with respect to ϕ, with the blue edges of_ ∆ _being Legendrian with respect to ξ_ + _and the red edges of_ ∆ _being Legendrian with respect to ξ−._ 

In the rest of this introduction, we explain an application to horizontal Goodman surgery, explain the strategy of proof to Theorem 1.1, and finally present a speculative framework on the connection between veering triangulations and bicontact structures. 

1.1. **Horizontal Goodman surgery.** In [Tsa24c], we defined a surgery operation on pseudo-Anosov flows which we called **horizontal Goodman surgery** . To briefly summarize: A **positive/negative horizontal surgery curve** to a pseudo-Anosov flow _ϕ_ is a curve _c_ that is positive/negative, respectively, and **steady** , in the sense that whenever there is **crossing** of _c_ , i.e. an orbit segment from _x ∈ c_ to _y ∈ c_ , then the tangent line _Tc|y_ lies closer to the stable foliation than _Tc|x_ . Cutting along an annulus _A_ containing _c_ and transverse to _ϕ_ , then regluing by a Dehn twist of positive/negative degree _n_ , respectively, returns a surgered pseudo-Anosov flow _ϕ_ 1[on][the][surgered] _n_[(] _[c]_[)] manifold _M_ 1 _n_[(] _[c]_[).] 

Furthermore, we conjectured that, in a precise way, horizontal Goodman surgery on pseudo-Anosov flows and **horizontal surgery** on veering triangulations correspond to each other. The latter is a combinatorial operation defined in [Tsa23a] that takes in a veering triangulation ∆, a **positive/negative horizontal surgery curve** _c_ satisfying some combinatorial conditions, and a positive/negative integer _n_ , respectively, and returns a surgered veering triangulation ∆ 1 _n_[(] _[c]_[).] 

In [Tsa24b, Theorem 7.1], we showed one direction of this conjecture for veering triangulations that can be placed in **steady position** , which means that the union of blue edges and the union of red edges are each steady, in the same sense as for horizontal surgery curves of pseudo-Anosov flows defined above. In other words, we wish for the blue/red edges to rotate steadily towards the stable foliation as one moves along the flow. Using the same ideas for proving Theorem 1.1, we are now able to show that such a position can always be arranged. 

**Theorem 1.2.** _Let ϕ be a pseudo-Anosov flow on a closed oriented 3-manifold M with no perfect fits relative to C. Then the veering triangulation_ ∆ _associated to_ ( _ϕ, C_ ) _can be placed in steady position with respect to ϕ._ 

Combining Theorem 1.2 and [Tsa24b, Theorem 7.1], we obtain the following corollary. 

**Corollary 1.3.** _Let ϕ be a pseudo-Anosov flow on a closed oriented 3-manifold M with no perfect fits relative to C. Let_ ∆ _be the veering triangulation associated to_ ( _ϕ, C_ ) _. Then for every positive/negative horizontal surgery curve c_ ∆ _of_ ∆ _, there is an isotopic_ 

CHI CHEUK TSANG 

4 

_positive/negative horizontal surgery curve cϕ of the flow ϕ, which is disjoint from C. Moreover, for every positive/negative integer n, the veering triangulation_ ∆ 1 _[is][the] n_[(] _[c]_[∆][)] _veering triangulation associated to_ ( _ϕ_ 1 _n_[(] _[c]_[∆][)] _[,][ C]_[)] _[.]_ 

1.2. **Strategy of proof.** Prior to this paper, Theorem 1.2 has been known for layered veering triangulations. We review the argument here, since our proof of Theorem 1.1 and Theorem 1.2 will be built on these ideas. 

A veering triangulation ∆is **layered** if it is the veering triangulation associated to some ( _ϕ, C_ ) where the restriction _ϕ[◦]_ of _ϕ_ to the complement _M[◦]_ = _M \C_ is the suspension of a pseudo-Anosov map _f_ on some surface _S[◦]_ . Here, recall that _f_ being a pseudo-Anosov map means that there exists **stable/unstable measure foliations** ( _ℓ[s/u] , µ[s/u]_ ) such that _f∗_ ( _ℓ[s] , µ[s]_ ) = ( _ℓ[s] , λ[−]_[1] _µ[s]_ ) and _f∗_ ( _ℓ[u] , µ[u]_ ) = ( _ℓ[u] , λµ[u]_ ) for some _λ >_ 1. In this case, the stable and unstable measured foliations induce a flat metric on _S[◦]_ . This in turn induces a flat metric on the orbit space _O_[�] _[◦]_ = _O\_[�] _C_[�] _[∼]_ = _S_[�] _[◦]_ of _ϕ[◦]_ , and a Solv metric on _M[◦]_ . 

We can now position edges of the veering triangulation by first pulling tight the diagonals of edges rectangles in _O_[�] _[◦][∼]_ = _S_[�] _[◦]_ , so that they become straight lines in the flat metric, and then taking the **canonical lifts** of these straight lines, i.e. lifting a straight line of slope _m_ to height[1] 2[log] _[λ][ |][m][|]_[in] _M_[�] _[◦][∼]_ = R _× S_[�] _[◦]_ . 

There is a bicontact geometry perspective to this canonical lifting procedure: The stable and unstable measured foliations on _S[◦]_ determine closed 1-forms _ds_ and _du_ . Using these, we can define the positive/negative contact forms 

**==> picture [270 x 32] intentionally omitted <==**

**==> picture [56 x 10] intentionally omitted <==**

A straightforward computation verifies that (ker _α_ + _[S][,]_[ ker] _[ α] −[S]_[)][is][a][strongly][adapted] bicontact structure supporting the lift of _ϕ[◦]_ , which is generated by _∂t∂_[.][The][canonical] lift of a diagonal _d ⊂ O_[�] _[◦]_ can now be defined as the unique arc _d[∧]_ in _M_[�] _[◦]_ lying over _d_ that is Legendrian with respect to the lifted contact structure ker � _α±_ on _M_[�] _[◦]_ , where the � sign on _α±_ is negative/positive depending on whether _d_ has positive/negative slope, respectively. It is clear that the union of positive/negative canonical lifts are steady. The other important property is what we refer to as the **slope criterion** : Whenever _R_ 1 and _R_ 2 are edge rectangles where _R_ 2 is taller and thinner than _R_ 1, then at every intersection point of the diagonals _dR_ 1 and _dR_ 2, we have _|_ slope( _dR_ 2) _| > |_ slope( _dR_ 1) _|_ . This implies the following property which we refer to as the **crossing criterion** : Any crossings between the canonical lifts _d[∧][d][∧]_[of] _[d][∧][d][∧] R_ 1[and] _R_ 2[are] _R_ 2[over] _R_ 1[.] 

The crossing criterion ensures that we can fill in the rest of the triangulation from the choice of the canonical lifts as the edges. For instance, taking _R_ 2 to be the top edge rectangle and _R_ 1 to be the bottom edge rectangle of a tetrahedron rectangle, the 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

5 

crossing criterion ensure that the top edge _d[∧] R_ 2[lies][above][the][bottom][edge] _[d][∧] R_ 1[,][so][that] the tetrahedron is not ‘flipped inside out’. 

Taking the quotient of the triangulation under _π_ 1 _M[◦]_ , we have realized the veering triangulation ∆in steady position. Moreover, the forms _α_ + and _α−_ descend to contact forms on _M[◦]_ , and the blue/red edges of ∆are Legendrian with respect to ker _α_ + _[S] /−_[,] respectively. 

Here, strictly speaking, the forms _ds, du_ on _S[◦]_ are only well-defined if _ℓ[s]_ and _ℓ[u]_ are orientable. Otherwise, they are locally well-defined up to a sign. Similarly, _α_ + _[S]_[and] _α−[S]_[on] _[M][ ◦]_[are][only][well-defined][if] _[ℓ][s]_[and] _[ℓ][u]_[are][orientable,][and] _[f]_[preserves][those] orientations. Otherwise, they are locally well-defined up to a sign. 

The main insight of this paper is that, with some work, the above argument can be carried over with the notion of a Birkhoff section. Here, a **Birkhoff section** to a pseudo-Anosov flow _ϕ_ is an immersed surface with boundary _S_ where 

- the interior int( _S_ ) is embedded and is transverse to the flow, 

- the boundary _∂S_ lies along closed orbits of _ϕ_ , and 

- every orbit of _ϕ_ meets _S_ in finite forward and backward time. 

The first item implies that the stable/unstable foliations of _ϕ_ induce singular 1- dimensional foliations _ℓ[s/u]_ on int( _S_ ). The third item implies that there is a first return map _f_ on int( _S_ ), which must preserve the foliations _ℓ[s/u]_ . From this, one can show that _f_ is a pseudo-Anosov map with stable/unstable foliations _ℓ[s/u]_ . 

Then as above, we have a flat metric on _S[◦]_ = int( _S_ ) _\_ sing( _f_ ), which induces a flat metric on the universal cover _O_[�] _[◦][∼]_ = _S_[�] _[◦]_ of the orbit space _O[◦]_ = _O\_ ( _∂S_[�] _∪_ sing([�] _ϕ_ )) of the restriction _ϕ[◦]_ of _ϕ_ to _M[◦]_ = _M \_ ( _∂S ∪_ sing( _ϕ_ )), and a Solv metric on _M[◦]_ . The problem now is that _∂S ∪_ sing( _ϕ_ ) may not be contained in _C_ , in which case the edge rectangles used to define ∆will not live in _O_[�] _[◦]_ . Instead, they live in _O_ and become punctured in _O[◦]_ . This means that when we pull the diagonals tight, they will in general be caught on the punctures _∂S_[�] , a priori in a possibly complicated way, so the slope criterion may not be satisfied. 

What we will show is that if we first choose the diagonals to be the first-horizontalthen-vertical arcs from the corners to an appropriate choice of a center _anchor_ , then upon pulling it tight, as in Figure 2, the resulting choice of piecewise linear diagonals will satisfy a proxy of the slope criterion. Namely, diagonals of the same color may overlap along segments, but the segments immediately beyond the overlap satisfy the appropriate slope inequality. See Figure 3 left, and see Proposition 6.1 for the detailed statement. This uses nothing more than elementary Euclidean geometry, but does require a bit of casework. It will also be convenient for us to add in some _buoys_ to the orbit space, so that the diagonal gets caught on the buoys instead of _∂S_[�] . 

6 

## CHI CHEUK TSANG 

Figure 2. Our first construction of the diagonals is to take the firsthorizontal-then-vertical arcs from the corners to an appropriate choice of a center anchor, then pull it tight. 

Figure 3. Modifying the piecewise linear diagonals from Figure 2. From left to right: Peeling apart the overlaps, rounding the corners, and rotating near the intersection points of diagonals of opposite color. 

We will then show in Proposition 7.10 that we can modify these piecewise linear diagonals to be smooth and satisfying the slope criterion on the nose. This involves three substeps: We first peel apart the overlaps, then round the corners, and finally rotate near the intersection points of diagonals of opposite color to arrange for the slope criterion. See Figure 3. Among these, the first substep is the most technical, since we have to ensure that when we peel apart each individual pair of diagonals, we do not break the slope criterion for other pairs. 

With the slope criterion being arranged, we can take the canonical lifts of the diagonals and fill in the triangulation as in the layered case. This proves Theorem 1.2. 

The proof of Theorem 1.1 is more roundabout. We first construct the veering triangulation ∆as in Theorem 1.2. Since we are assuming that the flow _ϕ_ is Anosov and has orientable stable and unstable foliations, the bicontact form ( _α_ + _[S][, α] −[S]_[)][from][Equa-] tion (1.1) is well-defined. However, it is only defined on _M[◦]_ = _M \∂S_ . We will show in Construction 8.2 and Construction 8.3 that we can extend the bicontact structure over each component of _∂S_ while maintaining strong adaptedness. This gives us a strongly adapted bicontact form ( _α_ + _, α−_ ) on _M_ . In particular, ( _α_ + _, α−_ ) supports an Anosov flow _ψ_ . 

Meanwhile, since our diagonals were chosen to lie away from _∂S_[�] , the canonical lifts, which are the edges of ∆, lie away from _∂S_ . This means that ∆intersects _∂S_ in the interior of its faces in meridional discs. After our operation on the bicontact form, we can arrange for these meridional discs to be transverse to the new flow _ψ_ . This implies that ∆is in Legendrian position with respect to _ψ_ . That is, we have proved Theorem 1.1 but for _ψ_ . 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

7 

The last step is to apply uniqueness of flows with respect to which ∆can be put in transverse position, in order to conclude that _ϕ_ and _ψ_ are isotopically equivalent. Transferring the triangulation and the bicontact structure through the isotopic equivalence, we deduce Theorem 1.1 for _ϕ_ . 

1.3. **Hexality of veering triangulations.** We present a speculative picture of how the theories of veering triangulations and bicontact structures could intertwine. To motivate things, let us consider the 3-torus _T_[3] = R[3] _/_ Z[3] , and consider the three curves 

**==> picture [134 x 83] intentionally omitted <==**

and the three tori 

**==> picture [152 x 49] intentionally omitted <==**

For every triple of integers _nx, ny, nz ∈_ Z, we denote by _Mnx,ny,nz_ the manifold _T nx_[3] 1 _[,] ny_[1] _[,] nz_[1][(] _[c][x][, c][y][, c][z]_[)][obtained][by] _n_ 1 _w_[surgery][on] _[c][w]_[,][where][we][take][the][longitude][on] _∂ν_ ( _cw_ ) to be a coordinate curve, for _w_ = _x, y, z_ . 

Suppose _nx >_ 0 _, ny <_ 0 _, nz >_ 0. Then _Mnx,ny,_ 0 is the mapping torus of the Anosov map 1 1 _nx_ 1 0 _ny L[n][x] R[n][y]_ = 0 1 1 1 on the torus _Txy_ , and, up to isotopy, _cz_ is an orbit of the � � � � Anosov suspension flow. Since _Mnx,ny,nz_ can be obtained from _Mnx,ny,_ 0 by performing 1 _nz_[-surgery along the orbit] _[ c][z]_[, it admits the Goodman-Fried surgered Anosov flow, which] we denote by _ϕxy_ . 

Interchanging the roles of _x_ and _z_ , we can consider _Mnx,ny,nz_ as a surgery of _M_ 0 _,ny,nz_ along the orbit _cx_ . As such, it admits another Anosov flow _ϕyz_ . 

By construction, _Txy\cz_ is a Birkhoff section for _ϕxy_ , thus we can obtain a bicontact form ( _α_ + _, α−_ ) supporting _ϕxy_ by first defining the contact forms as in Equation (1.1), then filling in along _cz_ as in Construction 8.2. Then one can check that _Tyz\cx_ is a Birkhoff section to the Reeb flow _R_ + of _α_ +. In particular, the monodromy of _R_ + on _Tyz\cx_ is in the same mapping class as that of _ϕyz_ . We conjecture that we can arrange things so that _R_ + = _ϕyz_ . 

**Conjecture 1.4.** _There exists a bicontact form_ ( _α_ + _, α−_ ) _supporting ϕxy where the Reeb flow R_ + _to α_ + _is isotopically equivalent to ϕyz._ 

8 

## CHI CHEUK TSANG 

**==> picture [134 x 76] intentionally omitted <==**

**----- Start of picture text -----**<br>
cy<br>cz<br>cx<br>**----- End of picture text -----**<br>


Figure 4. The setup on the 3-torus. 

Symmetrically, we could make the same conjecture regarding Reeb flows of bicontact forms supporting _ϕyz_ . The following conjecture morally combines these two versions of Conjecture 1.4. 

**Conjecture 1.5.** _There exists two positive contact structures ξx, ξz and a negative contact structure ξy on Mnx,ny,nz such that_ 

- _ϕxy is isotopically equivalent to a Reeb flow of ξz and is supported by_ ( _ξx, ξy_ ) _._ 

- _ϕyz is isotopically equivalent to a Reeb flow of ξx and is supported by_ ( _ξz, ξy_ ) _._ 

In other words, we predict that between _ϕxy_ and _ϕyz_ , the role of the Anosov flow orbits and the positive Reeb flow orbits are interchanged. In particular, (vertical) GoodmanFried surgery of _ϕxy_ along the orbit _cz_ would be the same as horizontal Goodman surgery of _ϕyz_ along the positive horizontal surgery curve _cz_ . Moreover, performing this surgery gets us from the setup on _Mnx,ny,nz_ to that on _Mnx,ny,nz_ +1. 

We now bring veering triangulations into the picture. The Anosov flow _ϕxy_ has no perfect fits relative to _cz_ , thus there is an associated veering triangulation ∆ _xy_ . More specifically, ∆ _xy_ can be built from a blue shearing region with core _cx_ and a red shearing region with core _cy_ . See Figure 4. Here, a **blue/red shearing region** is a solid torus cellulated in a specific way. We refer to [SS23] for details. For this discussion, it suffices to know that every veering triangulation has a canonical, combinatorially defined, decomposition into shearing regions. 

Similarly, there is a veering triangulation ∆ _yz_ associated to ( _ϕyz, cx_ ), whose blue shearing region has core _cz_ and red shearing region has core _cy_ . In other words, between ∆ _xy_ and ∆ _yz_ , the roles of the drilled out orbit and the core of the blue shearing region are swapped. We propose considering this as a veering triangulation analogue of Conjecture 1.5. 

Generalizing this example, we make the following ambitious ‘hexality’ conjecture. 

**Conjecture 1.6.** _Let ϕ be an Anosov flow on M with orientable stable and unstable foliations, with no perfect fits relative to C. Let_ ∆ _be the associated veering triangulation. Let A be the collection of cores of the blue shearing regions of_ ∆ _, and B be the collection of cores of the red shearing regions of_ ∆ _._ 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

9 

- _(I) For every sufficiently positive na and nc, the surgered manifold M_ 1[1] _na[,] nc_[(] _[A][,][ C]_[)] 

- _admits the Anosov flow ϕ_ 1[1] _[obtained][by][performing][horizontal][Goodman] na[,] nc_[(] _[A][,][ C]_[)] 

- _surgery along A and (vertical) Goodman-Fried surgery along C._ 

   - _We conjecture that there exists two positive contact structures ξa, ξc, a negative contact structure ξb, and an Anosov flow ϕ[σ]_[+] _on M_ 1[1] _[such][that] na[,] nc_[(] _[A][,][ C]_[)] 

      - _ϕ_ 1[1] _[is][isotopically][equivalent][to][a][Reeb][flow][of][ξ][c][and][is][supported] na[,] nc_[(] _[A][,][ C]_[)] 

      - _by_ ( _ξa, ξb_ ) _._ 

      - _ϕ[σ]_[+] _is isotopically equivalent to a Reeb flow of ξa and is supported by_ ( _ξc, ξb_ ) _._ 

_Here, the superscript σ_ + _denotes that we have swapped the roles of the Anosov orbits and the_ positive _Reeb flow orbits. While we have chosen not to reflect this in the notation, ϕ[σ]_[+] _should depend on na and nc. Larger choices of na and nc amount to performing (vertical) Goodman-Fried surgery along A and horizontal Goodman surgery along C on ϕ[σ]_[+] _._ 

- _(II) From Corollary 1.3, we know that the surgered triangulation_ ∆ _na_ 1[(] _[A]_[)] _[is][the] veering triangulation associated to_ ( _ϕ_ 1[1] _na[,] nc_[(] _[A][,][ C]_[)] _[,][ C]_[)] _[.]_ 

_We conjecture that the Anosov flow ϕ[σ]_[+] _from (I) has no perfect fits relative to A. This would allow us to talk about the veering triangulation_ ∆ _[σ]_[+] _associated to_ ( _ϕ[σ]_[+] _, A_ ) _._ 

_While we have chosen not to reflect this in the notation,_ ∆ _[σ]_[+] _should depend on nc. A larger choice of nc amount to performing horizontal surgery along C on_ ∆ _[σ]_[+] _. On the other hand,_ ∆ _[σ]_[+] _should not depend on na._ 

- _(III) Swapping the roles of A and B in (I) and (II) gives_ 

   - _an Anosov flow ϕ[σ][−] , well-defined up to (vertical) Goodman-Fried surgery along B and horizontal Goodman surgery along C, and_ 

   - _a veering triangulation_ ∆ _[σ][−] , well-defined up to horizontal Goodman surgery along C._ 

_We conjecture that we have the following isotopic equivalences:_ 

   - ( _ϕ[σ]_[+] ) _[σ]_[+] _[∼]_ = _ϕ where both sides are taken up to (vertical) Goodman-Fried surgery along C and horizontal Goodman surgery along A_ 

   - ( _ϕ[σ][−]_ ) _[σ][−][∼]_ = _ϕ where both sides are taken up to (vertical) Goodman-Fried surgery along C and horizontal Goodman surgery along B_ 

   - (( _ϕ[σ]_[+] ) _[σ][−]_ ) _[σ]_[+] _[∼]_ = (( _ϕ[σ][−]_ ) _[σ]_[+] ) _[σ][−] where both sides are taken up to (vertical) Goodman-Fried surgery along C and horizontal Goodman surgery along A and B._ 

- _In other words, we have a S_ 3 _-torsor of Anosov flows {ϕ[ρ] }ρ∈S_ 3 _. See Figure 5 left._ 

CHI CHEUK TSANG 

10 

**==> picture [345 x 147] intentionally omitted <==**

**----- Start of picture text -----**<br>
ϕ ∆<br>σ + σ− σ + σ−<br>ϕ [σ] [+] ϕ [σ][−] ∆ [σ] [+] ∆ [σ][−]<br>σ− σ + σ− σ +<br>( ϕ [σ] [+] ) [σ][−] ( ϕ [σ][−] ) [σ] [+] (∆ [σ] [+] ) [σ][−] (∆ [σ][−] ) [σ] [+]<br>σ + σ− σ + σ−<br>(( ϕ [σ] [+] ) [σ][−] ) [σ] [+] [∼] = (( ϕ [σ][−] ) [σ] [+] ) [σ][−] ((∆ [σ] [+] ) [σ][−] ) [σ] [+] [∼] = ((∆ [σ][−] ) [σ] [+] ) [σ][−]<br>**----- End of picture text -----**<br>


Figure 5. An illustration of Conjecture 1.6(III). 

_Similarly, we conjecture that we have the following combinatorial isomorphisms:_ 

- (∆ _[σ]_[+] ) _[σ]_[+] _[∼]_ = ∆ _where both sides are taken up to horizontal surgery along A_ 

- (∆ _[σ][−]_ ) _[σ][−][∼]_ = ∆ _where both sides are taken up to horizontal surgery along B_ 

- ((∆ _[σ]_[+] ) _[σ][−]_ ) _[σ]_[+] _[∼]_ = ((∆ _[σ][−]_ ) _[σ]_[+] ) _[σ][−] where both sides are taken up to horizontal surgery along A and B._ 

_In other words, we have a S_ 3 _-torsor of veering triangulations {_ ∆ _[ρ] }ρ∈S_ 3 _. See Figure 5 right._ 

**Outline of paper.** In Section 2 and Section 3, we review some background on pseudoAnosov flows and veering triangulations, respectively. 

In Section 4, we explain how the crossing criterion on an edge candidate system allows one to fill in a veering triangulation from the edges (Proposition 4.6). In Section 5, we explain how a Birkhoff section allows one to talk about canonical lifts, and how this allows one to translate the crossing criterion on an edge candidate system to the slope criterion on a diagonal system (Proposition 5.13). 

The proof of the main theorems Theorem 1.1 and Theorem 1.2 will span Section 6, Section 7, and Section 8. In Section 6, we construct a piecewise linear diagonal system that satisfies a proxy of the slope criterion (Proposition 6.1). In Section 7, we modify this piecewise linear diagonal system into one that satisfies the slope criterion on the nose (Proposition 7.10). From there, Theorem 1.2 will follow. 

In Section 8, we show how one can fill in bicontact forms over the boundary orbits of a Birkhoff section. From there, Theorem 1.1 will follow. 

**Acknowledgement.** We thank Michael Landry for discussions about approaches to Proposition 6.3. We thank Antonio Alfieri, Surena Hozoori, Federico Salmoiraghi, and Samuel Taylor for helpful conversations. 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

11 

This project was initiated while the author was supported by a CRM postdoctoral fellowship at Centre Interuniversitaire de Recherches en G´eom´etrie et Topologie (CIRGET) at Montr´eal, Qu´ebec, during the Fall 2025 semester, and completed while the author was supported by the National Science Foundation under Grant No. DMS-2424139 at the Simons Laufer Mathematical Sciences Institute (SLMath) in Berkeley, California, during the Spring 2026 semester. 

## 2. Pseudo-Anosov flows 

2.1. **Basic definitions.** A **flow** on a 3-manifold _M_ is a continuous map _ϕ_ : R _×M → M_ , which we write as _ϕ[t]_ ( _x_ ) = _ϕ_ ( _t, x_ ), satisfying _ϕ_[0] ( _x_ ) = _x_ and _ϕ[s]_ ( _ϕ[t]_ ( _x_ )) = _ϕ[s]_[+] _[t]_ ( _x_ ) for every _s, t ∈_ R _, x ∈ M_ . 

**Example 2.1** (Suspension flow) **.** Let _f_ : _S → S_ be a homeomorphism of a surface. The **mapping torus** of _f_ is the 3-manifold _Mf_ = R _× S/_ ( _s, x_ ) _∼_ ( _s −_ 1 _, f_ ( _x_ )). The **suspension flow** on _Mf_ is defined by _ϕ[t] f_[(] _[s, x]_[) = (] _[s]_[ +] _[ t, x]_[).] ♢ 

A flow _ϕ_ is **smooth on an open set** _U_ if the function _ϕ_ : R _× M → M_ is smooth on R _× U_ . In this case, we define the **generating vector field** _ϕ_[˙] by _ϕ_[˙] _|x_ = _dt[d]_ �� _t_ =0 _[ϕ][t]_[(] _[x]_[)][for] every˙ _x ∈ U_ . We also define the **tangent line field** _Tϕ_ to be the line field spanned by _ϕ_ . A flow _ϕ_ is **smooth** if it is smooth on the whole 3-manifold _M_ . 

Let _ϕ_ 1 and _ϕ_ 2 be flows defined on 3-manifolds _M_ 1 and _M_ 2 respectively. We say that _ϕ_ 1 and _ϕ_ 2 are **orbit equivalent** if there is a homeomorphism _h_ : _M_ 1 _→ M_ 2 sending the oriented flow lines of _ϕ_ 1 to that of _ϕ_ 2, but not necessarily preserving their parametrizations. 

**Definition 2.2** (Anosov flow) **.** An **Anosov flow** is a smooth flow _ϕ_ on a closed oriented 3-manifold _M_ for which there is a Riemannian metric _g_ and a splitting of the tangent bundle into three line bundles _TM_ = _E[s] ⊕ Tϕ ⊕ E[u]_ such that, for some _C, λ >_ 1, 

**==> picture [116 x 14] intentionally omitted <==**

**==> picture [440 x 45] intentionally omitted <==**

A pseudo-Anosov flow is essentially an Anosov flow with finitely many singular orbits. The singular orbits are modeled after the following construction. 

_λ_ 0 **Construction 2.3** (Pseudo-hyperbolic orbit) **.** Consider the map : R[2] _→_ R[2] . 0 _λ[−]_[1] � � By first quotienting R[2] by ( _x, y_ ) _∼_ ( _−x, −y_ ), then taking the _n_ -fold branched cover over the origin, we obtain a uniquely defined map _fn,_ 0 _,λ_ : R[2] _→_ R[2] that preserves the lifts of the quadrants. Let _fn,k,λ_ : R[2] _→_ R[2] be the composition of _fn,_ 0 _,λ_ and rotating by[2] _[πk] n_[anticlockwise.][Let] _[M][n,k,λ]_[be][the][mapping][torus][of] _[f][n,k,λ]_[and][consider] 

CHI CHEUK TSANG 

12 

the suspension flow on _Mn,k,λ_ . Let _γn,k,λ_ be the suspension of the origin. We refer to it as the **pseudo-hyperbolic orbit** . ♢ 

**Definition 2.4** (Pseudo-Anosov flow) **.** A **pseudo-Anosov flow** is a flow _ϕ_ on a closed oriented 3-manifold _M_ for which there is a path metric _d_ that is induced from a Riemannian metric _g_ away from a finite collection of closed orbits sing( _ϕ_ ), which we call the **singular orbits** , such that: 

- Away from the singular orbits, 

**–** _ϕ_ is smooth, and 

**–** there is a splitting of the tangent bundle into three line bundles _TM_ = _E[s] ⊕ Tϕ ⊕ E[u]_ , such that, for some _C, λ >_ 1, 

**==> picture [116 x 14] intentionally omitted <==**

for every _v ∈ E[s] , t >_ 0, and 

**==> picture [109 x 14] intentionally omitted <==**

for every _v ∈ E[u] , t <_ 0. 

- Around each singular orbit _γ_ , there exists a neighborhood _N_ of _γ_ in _M_ , a neighborhood _Nn,k,λ_ of the pseudo-hyperbolic orbit _γn,k,λ_ in _Mn,k,λ_ , for some _n ≥_ 3, _k ∈_ Z, and _λ >_ 1, and a homeomorphism _h_ : _Nn,k,λ → N_ such that 

**–** _h_ is bi-Lipschitz on _Nn,k,λ_ and smooth away from _γn,k,λ_ , and 

- _h_ sends oriented flow lines to oriented flow lines, but not necessarily preserving their parametrization. 

**==> picture [9 x 11] intentionally omitted <==**

Given a pseudo-Anosov flow, one can show that the splitting _TM_ = _E[s] ⊕ Tϕ ⊕ E[u]_ in _M \_ sing( _ϕ_ ) is automatically _ϕ[t]_ -invariant and continuous, see [FH19, Proposition 5.1.4]. Furthermore, the plane field _E[s] ⊕ Tϕ_ integrates uniquely to a 2-dimensional foliation Λ _[s]_ on _M \_ sing( _ϕ_ ), see [FH19, Theorem 6.1.1], which can be extended into a singular 2-dimensional foliation on _M_ . We call Λ _[s]_ the **stable foliation** . Similarly, we have the **unstable foliation** Λ _[u]_ which is tangent to _Tϕ ⊕ E[u]_ away from the singular orbits. See Figure 6 for the local form of the stable and unstable foliations near a point on a nonsingular orbit (left) and near a point on a 3-pronged singular orbit (right). 

Let _ν_ be a tubular neighborhood of a closed orbit _γ_ . The local stable and unstable leaves of _γ_ cut _ν_ into an even number of components. We refer to these components as the **quadrants** at _γ_ . 

If _γ_ is non-singular and has four quadrants, we say that it is **orientation-preserving** . Otherwise it has two quadrants and we say that it is **orientation-reversing** . 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

13 

**==> picture [79 x 114] intentionally omitted <==**

**==> picture [74 x 120] intentionally omitted <==**

Figure 6. The stable and unstable foliations near a point on a nonsingular orbit (left) and near a point on a 3-pronged singular orbit (right). 

A flow is **transitive** if it has a dense orbit. For a pseudo-Anosov flow, this is equivalent to the set of closed orbits being dense, see [BM26, Proposition 1.4.9]. All pseudo-Anosov flows in this paper will be transitive. 

We remark that Definition 2.2 and Definition 2.4 are usually referred to as the definition of _smooth_ (pseudo-)Anosov flows. In comparison, one can find a definition of _topological_ (pseudo-)Anosov flows in, for example, [BM26, Definition 1.1.10]. Every smooth pseudoAnosov flow is a topological Anosov flow. Conversely, it is known that every transitive topological pseudo-Anosov flow is orbit equivalent to a smooth pseudo-Anosov flow, see [Sha21, Theorem A] and [AT24, Theorem 5.11]. 

2.2. **Orbit space.** Let _ϕ_ be a pseudo-Anosov flow on _M_ . Let _ϕ_[�] be the lifted flow on the universal cover _M_[�] . It can be shown that the space of orbits _O_ of _ϕ_[�] , with the quotient topology, is homeomorphic to R[2] , see [BM26, Theorem 1.3.14]. The lifted stable/unstable foliations Λ[�] _[s/u]_ induce singular 1-dimensional foliations _O[s/u]_ on _O_ . The deck transformations _π_ 1 _M_ act on _O_ preserving the foliations _O[s/u]_ . We refer to the space _O_ with the foliations _O[s/u]_ as the **orbit space** of _ϕ_ . 

Throughout this paper, we will often use the same notation for an orbit of _ϕ_[�] and the point of _O_ that it projects down to. Also, we will adopt the convention of illustrating leaves of the stable foliation as green vertical lines and leaves of the unstable foliation as purple horizontal lines. Finally, we adopt the convention of orienting the orbit space _O_ so that orbits come out of the page. 

The stable and unstable leaves of each point _γ_ � _∈O_ cut _O_ into an even number of � components. We refer to these components as the **quadrants** at _γ_ . 

The stabilizer of each point _γ_ � _∈O_ is either trivial or cyclic. The latter case is true � � if and only if _γ_ projects to a closed orbit _γ_ . In this case the stabilizer is _⟨_ [ _γ_ ] _⟩[∼]_ = Z, where [ _γ_ �] is a suitable conjugate of [ _γ_ ] _∈ π_ 1 _M_ , and we say that the point _γ_ � is **periodic** . Furthermore, the closed orbit _γ_ is orientation-preserving if and only if _γ_ � is nonsingular � � � and the action of [ _γ_ ] preserves each quadrant at _γ_ . In this case, we also say that _γ_ is **orientation-preserving** . 

CHI CHEUK TSANG 

14 

Each stable or unstable leaf in _O_ contains at most one periodic point. We will also use the following fact repeatedly in this paper. 

**Proposition 2.5.** _Let C be a finite collection of closed orbits of ϕ. Let C_[�] _be the collection of orbits of ϕ_[�] _that project down to an orbit in C. Then C_[�] _is a discrete π_ 1 _M -invariant collection of points in O._ □ 

A **rectangle** in _O_ is a subspace homeomorphic to [0 _,_ 1][2] with the restriction of _O[s/u]_ identified with the foliation by vertical/horizontal lines respectively. 

Let _R_ 1 and _R_ 2 be two rectangles. We say that _R_ 2 is **taller** than _R_ 1 if every _O[s]_ -leaf that intersects _R_ 1 also intersects _R_ 2. We say that _R_ 1 is **wider** than _R_ 2 if every _O[u]_ -leaf that intersects _R_ 2 also intersects _R_ 2. If _R_ 2 is taller than _R_ 1 and _R_ 1 is wider than _R_ 2, then we write _R_ 2 _> R_ 1 and say that _R_ 2 **lies above** _R_ 1. The reason for this terminology shall become clear in Section 3.2. 

We say that two points _γ_ �1 and _γ_ �2 **span** a rectangle _R_ if they are opposite corners of _R_ . In this case we write _R_ = _R_ ( _γ_ �1 _,_ � _γ_ 2). 

2.3. **Steadiness.** Let _ϕ_ be a pseudo-Anosov flow on _M_ . Fix a Riemannian metric _g_ on _M \_ sing( _ϕ_ ) as in Definition 2.4. Let _x_ be a point in _M \_ sing( _ϕ_ ). Pick unit vectors _e[s/u]_ in _E[s/u] |x_ , respectively, such that ( _e[s] , ϕ, e_[˙] _[u]_ ) determines a positive basis of _TM |x_ . Suppose _ℓ_ is a line in _TM |x_ spanned by a vector _ae[s]_ + _bϕ_[˙] + _ce[u]_ . We say that _ℓ_ is **transverse to** _ϕ_ if ( _a, c_ ) _̸_ = (0 _,_ 0). In this case, we define the **slope** of _ℓ_ (with respect to _g_ ) to be _[a] c[∈]_[R] _[P]_[ 1][=][ R] _[ ∪{∞}]_[.][We][say][that] _[ℓ]_[is] **[positive/negative]**[if][the][slope][of] _[ℓ]_ is positive/negative, respectively. Note that while the slope of _ℓ_ depends on the choice of the Riemannian metric _g_ , whether _ℓ_ is positive/negative depends only on _ℓ_ . 

Now let _c_ be a 1-manifold, possibly disconnected and with boundary, in _M \_ sing( _ϕ_ ). We say that _c_ is **transverse to** _ϕ_ if _c_ is smoothly embedded and its tangent line field _Tc_ is transverse to _ϕ_ at every point of _c_ . In this case, we say that _c_ is **positive/negative** if _Tc_ is positive/negative, respectively, at every point of _c_ . We adopt the convention of illustrating positive 1-manifolds in red and negative 1-manifolds in blue. 

Let _c_ 1 and _c_ 2 be 1-manifolds in _M_ . We say that a triple ( _x, y, t_ ) _∈ c_ 1 _× c_ 2 _×_ (0 _, ∞_ ) is a time _t_ **crossing** of _c_ 2 over _c_ 1 if _y_ = _ϕ[t]_ ( _x_ ). If _c_ 1 = _c_ 2 = _c_ , we abbreviate this to a time _t_ **crossing** of _c_ . 

**Definition 2.6** (Steady 1-manifold) **.** Suppose _e_ is a positive or negative 1-manifold in _M \_ sing( _ϕ_ ). We say that _e_ is **steady** if for every crossing ( _x, y, t_ ) of _c_ , we have _|_ slope( _Te|y_ ) _| > |_ slope( _dϕ[t]_ ( _Te|x_ )) _|_ . ♢ 

Note that steadiness is independent of the choice of the Riemannian metric. We refer to [Tsa24c, Section 3.1] for an explanation of the terminology. 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

15 

2.4. **Contact structures.** Let _M_ be an oriented 3-manifold. A **positive contact form** on _M_ is a 1-form _α_ + satisfying _α_ + _∧ dα_ + _>_ 0. The **Reeb vector field** of a positive contact form _α_ + is the unique vector field _R_ + satisfying _α_ +( _R_ +) = 1 and _dα_ +( _R_ + _, ·_ ) = 0. A **positive contact structure** on _M_ is a plane field that can be locally defined as the kernel of a positive contact 1-form. Similarly, a **negative contact form** is a 1-form _α−_ satisfying _α− ∧ dα− <_ 0. A **negative contact structure** is a plane field that can be locally defined as the kernel of a negative contact 1-form. Note that we allow contact structures that are non-coorientable as plane fields. 

Contact structures offer us a convenient way of checking for steadiness. Recall that a 1-manifold _e_ , possibly disconnected and with boundary, is **Legendrian** with respect to a contact structure _ξ_ if it is tangent to _ξ_ at every point. 

**Proposition 2.7.** _Let ϕ be a pseudo-Anosov flow. Let U be a ϕ[t] -invariant open subset in M \_ sing( _ϕ_ ) _. Suppose ξ_ + _is a positive contact structure on U such that Tϕ ⊂ ξ_ + _at every point of U . Then every 1-manifold e in U that is transverse to ϕ and Legendrian with respect to ξ_ + _is negative and steady._ 

_The symmetric statement holds with ‘positive’ and ‘negative’ interchanged._ 

_Proof._ This is only a slightly more general version of [Tsa24c, Proposition 3.18], and the same proof carries over: The positive contact criterion implies that for every _y ∈ U_ , _dϕ[t]_ ( _ξ_ + _|ϕ−t_ ( _y_ )) rotates strictly monotonically counterclockwise around _ϕ_[˙] _|y_ as _t_ increases. Thus for any crossing ( _x, y, t_ ), we have slope( _Te|y_ ) _<_ slope( _dϕ[t]_ ( _Te|x_ )) _<_ 0. □ 

Conversely, contact structures can be used to build Anosov flows. For the purposes of this paper, a **bicontact structure** is a pair ( _ξ_ + _, ξ−_ ) consisting of a positive contact structure _ξ_ + and a negative contact structure _ξ−_ that are transverse to each other at every point. We say that a bicontact structure ( _ξ_ + _, ξ−_ ) **supports** a flow _ϕ_ if _Tϕ_ = _ξ_ + _∩ξ−_ at every point. 

Meanwhile, a **bicontact form** is a pair ( _α_ + _, α−_ ) consisting of a positive contact form _α_ + and a negative contact form _α−_ such that _ξ_ + = ker _α_ + and _ξ−_ = ker _α−_ are transverse to each other at every point. We say that a bicontact form ( _α_ + _, α−_ ) **supports** a flow _ϕ_ if its associated bicontact structure ( _ξ_ + _, ξ−_ ) supports _ϕ_ . 

**Definition 2.8** (Strongly adapted) **.** A bicontact form ( _α_ + _, α−_ ) is **strongly adapted** if the Reeb vector field _R_ + of _α_ + is contained in _ξ−_ at every point. ♢ 

**Theorem 2.9** ([Hoz24, Theorem 1.10]) **.** _Let ϕ be a smooth flow on a closed oriented 3-manifold M . Then ϕ is Anosov with orientable stable and unstable foliations if and only if it is supported by a strongly adapted bicontact form._ 

## 3. Veering triangulations 

- 3.1. **Definition.** An **ideal tetrahedron** is a tetrahedon with its 4 vertices removed. The removed vertices are called the **ideal vertices** . An **ideal triangulation** of a 

16 

## CHI CHEUK TSANG 

**==> picture [96 x 63] intentionally omitted <==**

**----- Start of picture text -----**<br>
0<br>0<br>π<br>π<br>0<br>0<br>**----- End of picture text -----**<br>


Figure 7. A tetrahedron in a veering triangulation. There are no restrictions on the colors of the top and bottom edges. 

3-manifold _M_ is a decomposition of _M_ into finitely many ideal tetrahedra glued along pairs of faces. 

A **taut structure** on an ideal triangulation is a labeling of the dihedral angles by 0 or _π_ , such that: 

- Each tetrahedron has exactly two dihedral angles labeled by _π_ , and they are opposite to each other. 

- The angle sum around each edge in the triangulation is 2 _π_ . 

A **transverse taut structure** is a taut structure along with a coorientation on each face, such that for any edge _e_ with dihedral angle labeled by 0 in a tetrahedron _t_ , exactly one of the faces of _t_ that are adjacent to _e_ is cooriented into _t_ . A **transverse taut ideal triangulation** is an ideal triangulation with a transverse taut structure. 

A **veering triangulation** is a transverse taut ideal triangulation with a coloring of the edges by red or blue, so that going counterclockwise around the four 0-labelled edges, starting from an endpoint of a _π_ -labelled edge, the edges are colored red, blue, red, blue, in that order. See Figure 7. 

3.2. **Agol-Gu´eritaud construction.** Let _ϕ_ be a pseudo-Anosov flow on _M_ . Let _C_ be a�nonempty finite collection of �closed orbits of _ϕ_ , containing all the singular orbits. Let _C_ � be the collection of orbits of _ϕ_ that project down to an orbit of _C_ . By Proposition 2.5, _C_ is a _π_ 1 _M_ -invariant discrete collection of points in _O_ . 

A **perfect fit** in _O_ is a properly embedded subspace homeomorphic to [0 _,_ 1][2] _\{_ (1 _,_ 1) _}_ with the restriction of _O[s/u]_ identified with the foliation by vertical/horizontal lines respectively. We say that _ϕ_ has **no perfect fits** relative to _C_ if every perfect fit in _O_ contains at least one point of _C_[�] . We remark that in this case _ϕ_ must be transitive, see [Tsa24a, Remark 2.11]. 

When _ϕ_ has no perfect fits relative to _C_ , Agol-Gu´eritaud showed that one can build a veering triangulation from the data of the pair ( _ϕ, C_ ). To explain this, we introduce a few more definitions. 

**Definition 3.1** (Edge/face/tetrahedron rectangle) **.** An **edge rectangle** in _O_ is a rectangle with two opposite corners on _C_[�] . An edge rectangle is **red** if its bottom-left and top-right corners lie in _C_[�] , and **blue** if its top-left and bottom-right corners lie in _C_[�] . 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

17 

Figure 8. From left to right: an edge rectangle, a face rectangle, and a tetrahedron rectangle. Yellow dots denote elements of _C_[�] . 

**==> picture [94 x 94] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>3<br>[ c ]<br>2<br>1<br>c<br>**----- End of picture text -----**<br>


Figure 9. The setting of Proposition 3.2. 

A **face rectangle** in _O_ is a rectangle with one corner on _C_[�] and the two opposite sides to the corner containing elements of _C_[�] in their interior. Note that each face rectangle contains three edge subrectangles. Two of these edge rectangles have the same color, while the remaining one has the opposite color. 

A **tetrahedron rectangle** in _O_ is a rectangle all of whose sides contain elements of _C_[�] in their interior. Note that each tetrahedron rectangle _T_ contains four face subrectangles and six edge subrectangles. We refer to the edge subrectangle that is as tall as _T_ as the **top** edge subrectangle, and the edge subrectangle that is as wide as _T_ as the **bottom** edge subrectangle. 

See Figure 8 for examples of edge/face/tetrahedron rectangles. 

♢ 

The key consequence of the no perfect fit condition is the following. 

**Proposition 3.2.** _Suppose ϕ has no perfect fits relative to C. Let c be a point on O. Let S be the collection of points s ∈ C_[�] _in a fixed quadrant of c that span a rectangle with c with no points of C_[�] _in the interior of R_ ( _c, s_ ) _. The elements of S are totally ordered by the relation s_ 1 _< s_ 2 _if R_ ( _c, s_ 1) _< R_ ( _c, s_ 2) _. Under this order, S is order isomorphic to_ Z _._ 

_Furthermore, suppose c is periodic. Let k be the smallest positive exponent such that_ [ _c_ ] _[k] preserves each quadrant at c. Then_ [ _c_ ] _[k] acts as a translation m �→ m_ + _m_ 0 _for some m_ 0 _∈_ Z+ _. See Figure 9._ 

_Proof._ Let _ℓ[s]_ be the stable half-leaf of _c_ that borders the fixed quadrant. We can define an order-preserving map _π_ : _S → ℓ[s][∼]_ = R by mapping each _s ∈ S_ to the point of _ℓ[s]_ that 

CHI CHEUK TSANG 

18 

shares an unstable leaf with _s_ . [SS24, Lemma 4.10] states that the image of _π_ has no accumulation points. Thus _S_ must be order isomorphic to Z. 

If _c_ is periodic, then [ _c_ ] _[k]_ acts as a translation on _ℓ[s][∼]_ = R. Thus it must act as a translation on _S_ as well. □ 

We are now ready to state the Agol-Gu´eritaud construction. 

**Construction 3.3** (Agol-Gu´eritaud [LMT23, Section 4.1], [SS24, Section 5.8]) **.** Take an ideal tetrahedron _tR_ for each tetrahedron rectangle _R_ . Fix a bijection between the four ideal vertices of _tR_ with the four points of _C_[�] on the boundary of _R_ . This induces a bijection between: 

- The six edges of _tR_ with the six edge subrectangles of _R_ . 

- The four faces of _tR_ with the four face subrectangles of _R_ . 

Whenever two tetrahedron rectangles _R_ 1 and _R_ 2 intersect in rectangle that is a face subrectangle of both _R_ 1 and _R_ 2, we glue _tR_ 1 and _tR_ 2 along their corresponding faces. This gives a ideal triangulation ∆.[�] 

We define a veering structure on ∆[�] by declaring the edge of _tR_ corresponding to the top/bottom edge rectangle to be the top/bottom edge, respectively, and coloring an edge red/blue if its corresponding edge rectangle is red/blue, respectively. 

The deck transformations _π_ 1 _M_ act naturally on ∆[�] , preserving the veering structure. In fact, _π_ 1 _M_ acts freely on the set of edge/face/tetrahedron rectangles, thus the action of _π_ 1 _M_ on the edges/faces/tetrahedra is free, so the quotient ∆= ∆[�] _/π_ 1 _M_ is a triangulation. Moreover, by Proposition 3.2 applied to points in _C_[�] , one can show that ∆is a finite triangulation of a 3-manifold homeomorphic to _M \C_ . 

We refer to ∆as the **veering triangulation associated to** ( _ϕ, C_ ). 

♢ 

3.3. **Positioning of veering triangulations.** In Construction 3.3, we mentioned that the veering triangulation ∆lives on a 3-manifold homeomorphic to _M \C_ . In particular, we can transfer ∆into a triangulation of _M \C_ . However, the construction does not specify how ∆interacts with _ϕ_ after this transfer. In this subsection, we will define three increasingly strong ways ∆can be positioned with respect to _ϕ_ . 

**Definition 3.4** (Transverse position) **.** Let _ϕ_ be a pseudo-Anosov flow on _M_ and let _C_ be a nonempty finite collection of closed orbits of _ϕ_ . Let ∆be a veering triangulation on _M \C_ . We say that ∆is in **transverse position** with respect to _ϕ_ if: 

- each face _f_ of ∆is positively transverse to the orbits of _ϕ_ , and 

- each edge _e_ of ∆extends to a smoothly embedded compact arc _e_ that is transverse to the stable and unstable foliations of _ϕ_ . ♢ 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

19 

Transverse position is sufficient for basic applications of the correspondence theory between pseudo-Anosov flows and veering triangulations. For example, we have the following existence and uniqueness result. 

**Theorem 3.5** (Landry-Minsky-Taylor [LMT23, Theorem 5.1], Landry-Taylor [Tsa24b, Theorem 6.1]) **.** _Let ϕ be a pseudo-Anosov flow on M with no perfect fits relative to C. Then the veering triangulation_ ∆ _associated to_ ( _ϕ, C_ ) _can be placed in transverse position with respect to ϕ. Moreover, ϕ is the only pseudo-Anosov flow on M with respect to which_ ∆ _can be placed in transverse position, up to orbit equivalence by a map isotopic to identity._ □ 

However, we need the following stronger condition in order to apply the horizontal surgery machinery of [Tsa24c] and [Tsa24b]. 

**Definition 3.6** (Steady position) **.** Let _ϕ_ be a pseudo-Anosov flow with no perfect fits relative to _C_ , and let ∆be the veering triangulation associated to ( _ϕ, C_ ). Suppose ∆is in transverse position with respect to _ϕ_ . We further say that ∆is in **steady position** with respect to _ϕ_ if: 

- the union of red edges of ∆is positive and steady, and 

- the union of blue edges of ∆is negative and steady. 

♢ 

In this paper, we will certify steady position using the following even stronger condition. 

**Definition 3.7** (Legendrian position) **.** Let _ϕ_ be a pseudo-Anosov flow with no perfect fits relative to _C_ , and let ∆be the veering triangulation associated to ( _ϕ, C_ ). Suppose ∆is in transverse position with respect to _ϕ_ . 

Let ( _ξ_ + _, ξ−_ ) be a bicontact structure on a _ϕ[t]_ -invariant open subset _U ⊂ M \C_ that supports the restriction of _ϕ_ to _U_ . We say that ∆is in **Legendrian position** with respect to _ϕ_ and ( _ξ_ + _, ξ−_ ) if: 

- the union of red edges lies in _U_ and is Legendrian with respect to _ξ−_ , and 

- the union of blue edges lies in _U_ and is Legendrian with respect to _ξ_ +. ♢ 

**Proposition 3.8.** _If_ ∆ _is in Legendrian position then it is in steady position._ 

> _Proof._ If ∆is in Legendrian position, then the red edges are transverse to _ϕ_ and Legendrian to a negative contact structure containing _Tϕ_ , so by Proposition 2.7, they are steady. Similarly, we deduce that the blue edges are steady. □ 

## 4. From edges to triangulations 

In this section, we state a set of sufficient criteria for a collection of arcs to be realized as the edges of a veering triangulation. 

CHI CHEUK TSANG 

20 

4.1. **Edge candidates.** We first set up some terminology. Let _ϕ_ be a pseudo-Anosov flow on _M_ with no perfect fits relative to _C_ . 

**Definition 4.1** (Diagonal) **.** Let _R_ be an edge rectangle in the orbit space _O_ . A **diagonal** of _R_ is an arc in _O_ between the two elements of _C_[�] at the corners of _R_ that is transverse to the foliations _O[s]_ and _O[u]_ . A **diagonal system** is a collection _{dR | R_ is an edge rectangle _}_ that is equivariant, i.e. _g · dR_ = _dg·R_ for every _g ∈ π_ 1 _M_ . ♢ 

**Definition 4.2** (Edge candidate) **.** Let _R_ be an edge rectangle in the orbit space _O_ . An **edge candidate** for _R_ is a smoothly embedded arc in _M_[�] between the two elements of _C_[�] at the corners of _R_ that projects homeomorphically to a diagonal of _R_ . An **edge candidate system** is a collection _{d[∧] R[|][ R]_[is][an][edge][rectangle] _[}]_[that][is][equivariant,][i.e.] _g · d[∧] R_[=] _[ d][∧] g·R_[for][every] _[g][∈][π]_[1] _[M]_[.][Note][that][the][projection][of][an][edge][candidate][system] onto _O_ is a diagonal system. ♢ 

## 4.2. **Crossing criterion.** We are now ready to state our criteria. 

**Definition 4.3** (Face embeddedness criterion) **.** We say that a diagonal system _{dR}_ satisfies the **face embeddedness criterion** if for every pair of edge rectangles _R_ 1 _< R_ 2 that share a corner, int( _dR_ 1) and int( _dR_ 2) are disjoint. 

We say that an edge candidate system _{d[∧] R[}]_[ satisfies the] **[ face embeddedness criterion]** if for every pair of edge rectangles _R_ 1 _< R_ 2 that share a corner, there are no crossings between int( _d[∧] R_ 1[) and][ int][(] _[d] R[∧]_ 2[), equivalently, if the diagonal system obtained by projecting] _{d[∧] R[}]_[to][the][orbit][space][satisfies][the][face][embeddedness][criterion.] ♢ 

The following lemma justifies our terminology. 

**Lemma 4.4.** _A diagonal system {dR} satisfies the face embeddedness criterion if and only if for every face rectangle Q, the interiors of diagonals_ int( _dR_ 1) _,_ int( _dR_ 2) _,_ int( _dR_ 3) _, for the three edge subrectangles R_ 1 _, R_ 2 _, R_ 3 _⊂ Q are disjoint._ 

_Proof._ Recall that each face rectangle has exactly two edge subrectangles of the same color. The interiors of the edge subrectangles of opposite color are disjoint, so the interiors of their diagonals are automatically disjoint. The remaining pair of edge subrectangles that have the same color share a corner, so the interiors of their diagonals are disjoint if the face embeddedness criterion is satisfied. 

Conversely, if _R_ 1 _< R_ 2 are two edge rectangles that share a corner, then by Proposition 3.2, there exists a sequence of edge rectangles _R_ 1 = _R_ 1 _[′][< R]_ 2 _[′][< ... < R] n[′]_[=] _[ R]_[2][such] that _Ri[′]_[and] _[R] i[′]_ +1[are][edge][subrectangles][of][a][common][face][rectangle.][If][int][(] _[d][R] i[′]_[)][and] int( _dRi[′]_ +1[)][are][disjoint][for][each] _[i]_[,][then] _[d][R] j[′]_[separates] _[d][R]_ 1 _[′][, ..., d][R] j[′] −_ 1[from] _[d][R] j[′]_ +1 _[, ..., d][R][n][′]_[in] _n_ � _i_ =1 _[R] i[′]_[for][any] _[j]_[.][Hence][int(] _[d][R]_ 1[)][and][int(] _[d][R]_ 2[)][are][disjoint.] □ 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

21 

**==> picture [260 x 129] intentionally omitted <==**

**----- Start of picture text -----**<br>
d [∧] R d [∧] R<br>Figure 10. Analyzing arcs FQ [∧] [∩] [D][R] [.]<br>**----- End of picture text -----**<br>


**Definition 4.5** (Crossing criterion) **.** We say that an edge candidate system _{d[∧] R[}]_ satisfies the **crossing criterion** if the edge candidates _d[∧] R_[are][smoothly][embedded,][and] for every _R_ 1 _< R_ 2, every intersection point between the projections of int( _d[∧] R_ 1[)][and] int( _d[∧] R_ 2[)][in] _[O]_[is][the][projection][of][a][crossing][of][int(] _[d][∧] R_ 2[)][over][int(] _[d][∧] R_ 1[).] ♢ 

**Proposition 4.6.** _Let ϕ be a pseudo-Anosov flow on M with no perfect fits relative to C. Let {d[∧] R[}][be][an][edge][candidate][system][satisfying][the][face][embeddedness][and][the][crossing] criteria. Then the veering triangulation_ ∆ _associated to_ ( _ϕ, C_ ) _can be put in transverse position_ � _with respect to ϕ, with_ int( _d[∧] R_[)] _[being][the][edges][of][the][lifted][triangulation]_[∆][�] _[on] M ._ 

_Proof._ � The strategy of the proof is to build the triangulation ∆[�] in the universal cover _M_ starting with int( _d[∧] R_[)][as][the][edges.] 

For each face rectangle _Q_ , let _FQ_ be the ideal triangle bounded by the projected diagonals in the three edge subrectangles of _Q_ , minus the three vertices at _C_[�] . Note that Lemma 4.4 is used here. Pick a lift _FQ[∧]_[of] _[F][Q]_[in] _M_[�] , such that _FQ[∧]_[restricts][to][int][(] _[d][∧] R_[)] over the interior of the diagonal in each edge subrectangle _R_ . 

We do this for one representative in each _π_ 1 _M_ -orbit of face rectangles, and then extend this over all face rectangles equivariantly. Here, we use the fact that _π_ 1 _M_ acts freely on the face rectangles. 

We now analyze the intersections between the triangles _FQ[∧]_[.][By][first][making][a] _[π]_[1] _[M]_[-] equivariant perturbation of _FQ[∧]_[, or equivalently, making a perturbation of the projections] of _FQ[∧]_[in] _[M]_[,][then][taking][the][lift][of][those][projections,][we][can][assume][that][the][triangles] intersect in a _π_ 1 _M_ -invariant collection of arcs and curves, and that the number of _π_ 1 _M_ -orbits of such arcs and curves is finite. Here, each arc can either end at a point in the interior of a triangle, at a point in the interior of an edge, or at an ideal vertex. 

We first isotope the triangles so that the arcs cannot end on the interior of edges: For every edge rectangle _R_ , let _DR[∼]_ = int( _d[∧] R_[)] _[ ×]_[ R][be][the][union][of][orbits][of] _[ϕ]_[�][that][pass] through int( _d[∧] R_[).][Each][triangle] _[F] Q[ ∧]_[that][intersects] _[D][R]_[must][do][so][either][in][a][compact] arc, a half-infinite arc, or a bi-infinite arc, depending on whether _Q_ shares zero, one, or two points of _C_[�] with _R_ , respectively. See Figure 10 left. 

22 

## CHI CHEUK TSANG 

**==> picture [98 x 85] intentionally omitted <==**

**----- Start of picture text -----**<br>
R [′]<br>Q<br>R [′′]<br>R<br>**----- End of picture text -----**<br>


Figure 11. If _R_ is an edge rectangle and _Q_ is a face rectangle that intersect, then either we have _Q < R_ or _Q > R_ . 

**==> picture [71 x 63] intentionally omitted <==**

**==> picture [71 x 63] intentionally omitted <==**

**==> picture [79 x 57] intentionally omitted <==**

**==> picture [80 x 57] intentionally omitted <==**

Figure 12. We can get rid of arcs and circles of intersection between faces by cutting and pasting along them. 

In the compact arc case, we claim that the endpoints of the arc must both lie below int( _d[∧] R_[)][or][both][lie][above][int][(] _[d][∧] R_[).][Indeed,][since] _[R]_[is][an][edge][rectangle][and] _[Q]_[is][a][face] rectangle that intersect, either we have _Q < R_ or _Q > R_ . Without loss of generality suppose the former is true. Then also using the fact that _Q_ and _R_ do not share points of _C_[�] , we see that _Q_ has exactly two edge rectangles _R[′]_ and _R[′′]_ that intersect _R_ , both of which lie below _R_ , as in Figure 11. Thus applying the crossing criterion, the endpoints of the arc _FQ[∧][∩][D][R]_[,][which][must][lie][on][int][(] _[d][∧] R[′]_[)][and][int][(] _[d][∧] R[′′]_[)][respectively,][must][lie][below] int( _d[∧] R_[).] 

From this claim, we can isotope the triangles, along orbits of _ϕ_[�] and relative to their edges, so that no triangles intersect int( _d[∧] R_[),][see][Figure][10][.][Doing][so][for][one][representative] _[R]_ in each _π_ 1 _M_ -orbit of edge rectangle, then extending it by _π_ 1 _M_ -equivariance, we will have arranged it so that the triangles _FQ[∧]_[only intersect in arcs that end on ideal vertices] and in circles. 

We can now get rid of these arcs and circles of intersection by cutting and pasting along them, see Figure 12. After doing so, we now have a collection of mutually disjoint triangles _FQ[∧]_[.][We][declare][these][to][be][the][faces][of][the][constructed][triangulation.] 

For each tetrahedron rectangle _T_ , the faces _FQ[∧]_[corresponding][to][the][four][face][subrect-] angles of _T_ bound a region in _M_[�] _\C_[�] foliated by orbit segments of _ϕ_[�] . Moreover, _ϕ_[�] enters 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

23 

the region on two faces and exits the region on the remaining two. Thus the region is an ideal tetrahedron. This shows that we have constructed an ideal triangulation of _M_[�] _\C_[�] . Moreover, by construction, this is the veering triangulation ∆[�] . Taking the quotient by _π_ 1 _M_ gives us the proposition. □ 

## 5. From diagonals to edges 

Proposition 4.6 gives a method of putting veering triangulations in transverse position. However, this is not very wieldy in practice since there is too much freedom in picking arcs in 3-manifolds. In this section, we build on Proposition 4.6 and give another set of sufficient criteria for building veering triangulations, but this time in terms of just the diagonals and also achieving Legendrian position automatically. 

5.1. **Birkhoff sections.** The key notion in this section is that of a Birkhoff section. 

**Definition 5.1** (Birkhoff section) **.** A **Birkhoff section** to a pseudo-Anosov flow _ϕ_ is an immersed surface with boundary _S_ where 

- the interior int( _S_ ) is embedded and is transverse to the flow, 

- the boundary _∂S_ lies along closed orbits of _ϕ_ , and 

- every orbit of _ϕ_ meets _S_ in finite forward and backward time. 

♢ 

It is a classical result that Birkhoff sections exist in plenty: 

**Theorem 5.2** ([Bru95]) **.** _Every transitive pseudo-Anosov flow admits a Birkhoff section S. Moreover, given any finite collection of closed orbits C, the boundary orbits of S can be chosen to be orientation-preserving and disjoint from C._ 

_Proof._ This follows from the proof of [Bru95, Theorem 1], using the fact that since _C_ is finite, the set of orientation-preserving closed orbits that do not belong to _C_ is dense. □ 

The importance of Birkhoff sections is that they reduce the 3-dimensional dynamics of a pseudo-Anosov flow into the 2-dimensional dynamics of a pseudo-Anosov map: Let _S_ be a Birkhoff section to a pseudo-Anosov flow _ϕ_ . The first item of Definition 5.1 implies that the stable/unstable foliations of _ϕ_ induce singular 1-dimensional foliations _ℓ[s/u]_ on int( _S_ ). The last item of Definition 5.1 implies that there is a first return map _f_ on int( _S_ ), which must preserve the foliations _ℓ[s/u]_ . 

From this, one can show that _f_ is a pseudo-Anosov map with stable/unstable foliations _ℓ[s/u]_ , i.e. there exists transverse measure _µ[s/u]_ on _ℓ[s/u]_ such that _f∗µ[s]_ = _λ[−]_[1] _µ[s]_ , _f∗µ[u]_ = _λµ[u]_ for some _λ >_ 1 which we refer to as the **dilatation** of _f_ , see [FLP12, Lemma 14.12]. 

CHI CHEUK TSANG 

24 

**Proposition 5.3.** _There is an orbit equivalence h from the suspension flow on Mf to the restriction of ϕ to M \∂S. Moreover, h can be arranged to be smooth on Mf[◦]_[=] _Mf \_ sing( _ϕf_ ) _._ 

_Proof._ By an arbitrarily small homotopy along flow lines, we can first ensure that int( _S_ ) is smoothly embedded in _M \_ sing( _ϕ_ ). Once this is arranged, the first return time _T_ is a smooth function on int( _S_ ) away from the singular points. Pick a function _ρ_ : _{_ ( _t, x_ ) _∈_ R _×_ int( _S_ ) _| t ∈_ [0 _, T_ ( _x_ )] _} →_ R that is smooth away from [0 _, T_ ( _x_ )] _× {x}_ for singular points _x_ , and where _ρ_ ( _t, x_ ) = _t_ for _t_ close to 0 or _T_ ( _x_ ). We can then extend the embedding int( _S_ ) _⊂ M \∂S_ into an orbit equivalence _h_ by sending ( _t, x_ ) to _ϕ[ρ]_[(] _[t,x]_[)] ( _x_ ). This orbit equivalence is smooth away from singular orbits. □ 

- 5.2. **Quasi-translation structures.** We introduce the following terminology. 

**Definition 5.4** ((Quasi-)translation structure) **.** For the purposes of this paper, we define a **translation structure** on a surface _S_ to be an atlas of charts into R[2] with transition functions of the form ( _x, y_ ) _�→_ ( _x_ + _x_ 0 _, y_ + _y_ 0). 

Building on this, we define a **quasi-translation structure** on _S_ to be an atlas of charts into R[2] with transition functions of the form ( _x, y_ ) _�→_ ( _±λx_ + _x_ 0 _, ±λ[−]_[1] _y_ + _y_ 0). ♢ 

On a surface equipped with a quasi-translation structure, we can talk about quantities on R[2] that are preserved by homeomorphisms of the form ( _x, y_ ) _�→_ ( _±λx_ + _x_ 0 _, ±λ[−]_[1] _y_ + _y_ 0). This includes: 

- Linear arcs, smooth arcs. 

- For a point _v_ on a smooth arc _p_ , whether slope _v_ ( _p_ ) is positive or negative. 

- For an intersection point _v_ between two smooth arcs _p_ and _q_ , whether _|_ slope _v_ ( _p_ ) _| < |_ slope _v_ ( _q_ ) _|_ . 

We also introduce the following terminology. 

**Definition 5.5** (Piecewise linear arc) **.** Let _S_ be a surface equipped with a quasitranslation structure. A **piecewise linear arc** on _S_ is an arc _p_ along with a finite collection of points _v_ 1 _, ..., vk−_ 1 _∈ p_ such that _p_ is a concatenation of linear subarcs _p_ 1 _∗v_ 1 _... ∗vk−_ 1 _pk_ . We refer to the points _v_ 1 _, ..., vk−_ 1 as well as the endpoints _v_ 0 _, vk_ of _p_ as the **nodes** , and the linear subarcs _pi_ as the **segments** . 

Note that we allow for the possibility that slope( _pi_ ) = slope( _pi_ +1) at _vi_ . In particular, we can always add nodes in the interior of the segments. This is the reason why we have to specify the nodes as part of the data of a piecewise linear arc. If slope( _pi_ ) _̸_ = slope( _pi_ +1) then we say that _vi_ is a **turn** . This subtle point will come up in Section 7.1. 

We say that _e_ is **positive** if every _pi_ has positive slope. In this case, we say that _p_ is **convex** if either 0 _<_ slope( _p_ 1) _< ... <_ slope( _pk_ ) or slope( _p_ 1) _> ... >_ slope( _pk_ ) _>_ 0. Similarly we define **negative** and **negative convex** piecewise linear paths. ♢ 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

25 

**==> picture [127 x 53] intentionally omitted <==**

**----- Start of picture text -----**<br>
q 2 q 2<br>p 2 p 2<br>r<br>r p 1<br>q 1<br>**----- End of picture text -----**<br>


Figure 13. The setting of Definition 5.6. 

**Definition 5.6** (Overlap of piecewise linear arcs) **.** Let _S_ be a surface equipped with a quasi-translation structure. Let _p_ and _q_ be two piecewise linear arcs in _S_ , which are either both positive or both negative. Suppose _p_ and _q_ overlap along a (possibly degenerate) subarc _r_ . That is, we can write _p_ = _p_ 1 _∗v_ 1 _r ∗v_ 2 _p_ 2 and _q_ = _q_ 1 _∗v_ 1 _r ∗v_ 2 _q_ 2, for (possibly degenerate) subarcs _p_ 1 _, p_ 2 _, q_ 1 _, q_ 2. Here, by a **degenerate subarc** , we just mean a point. Note that we do not assume that _v_ 1 or _v_ 2 is a node of _p_ or _q_ . 

In this setting, we write _|_ slope _r_ ( _p_ ) _| < |_ slope _r_ ( _q_ ) _|_ if either 

   - _p_ 1 and _q_ 1 are degenerate and _|_ slope _v_ 2( _p_ 2) _| < |_ slope _v_ 2( _q_ 2) _|_ , or 

- _p_ 1 _, p_ 2 _, q_ 1 _, q_ 2 are all nondegenerate and _|_ slope _vi_ ( _pi_ ) _| < |_ slope _vi_ ( _qi_ ) _|_ for _i_ = 1 _,_ 2. 

- See Figure 13. ♢ 

5.3. **From Birkhoff sections to quasi-translation structures.** In this subsection, we explain how quasi-translation structures naturally come up when studying Birkhoff sections to pseudo-Anosov flows. 

Let _S_ be a Birkhoff section to a pseudo-Anosov flow _ϕ_ on _M_ with orbit space _O_ . Let _f_ be the pseudo-Anosov first return map defined on int( _S_ ). By Proposition 5.3, there is an orbit equivalence between the suspension flow on _Mf_ and the restriction of _ϕ_ to _M \∂S_ . This induces an orbit equivalence _h_ between the suspension flow on _Mf[◦]_[=] _[ M][f][\]_[ sing][(] _[ϕ][f]_[)] and the restriction of _ϕ_ to _M[◦]_ = _M \_ ( _∂S ∪_ sing( _ϕ_ )). Taking a lift, we have an orbit equivalence[�] _h_ between the universal covers _M_[�] _f[◦]_[and] _M_[�] _[◦]_ . 

The space of orbits in _M_[�] _f[◦]_[can be identified with the universal cover of] _[ S][◦]_[=][ int][(] _[S]_[)] _[\]_[ sing][(] _[f]_[),] while the space of orbits in _M_[�] _[◦]_ is the universal cover of the **punctured orbit space** _O[◦]_ = _O\_ ( _∂S_[�] _∪_ sing([�] _ϕ_ )). Thus[�] _h_ induces an identification of universal covers _S_[�] _[◦][∼]_ = _O_[�] _[◦]_ preserving the stable and unstable foliations. We refer to this common space, together with the stable and unstable foliations, as the **translation orbit space** . 

The reason for this terminology is that the measures on the stable and unstable foliations of _f_ induce a translation structure on _S_[�] _[◦]_ . Each element _g ∈ π_ 1( _Mf[◦]_[)][acts][on] this translation structure by a homeomorphism locally of the form ( _x, y_ ) _�→_ ( _±λ[k] x_ + _x_ 0 _, ±λ[−][k] y_ + _y_ 0), where _λ_ is the dilatation of _f_ and _k ∈_ Z. We refer to _k_ as the **height** of _g_ . 

CHI CHEUK TSANG 

26 

For _k ∈_ Z, let _π_ 1( _M[◦]_ ) _k_ be the set of elements _g ∈ π_ 1( _M[◦]_ ) with height _k_ . The set _π_ 1( _M[◦]_ )0 is exactly the subgroup _π_ 1( _S[◦]_ ) _< π_ 1( _Mf[◦]_[)] _[∼]_[=] _[π]_[1][(] _[M][ ◦]_[).][Thus] _[π]_[1][(] _[M][ ◦]_[)][0][acts] properly discontinuously on _O_[�] _[◦][∼]_ = _S_[�] _[◦]_ , with quotient _S[◦]_ . 

One can compactify _S[◦]_ into a compact surface with boundary cl( _S[◦]_ ) by adding a boundary component to each puncture. Accordingly, one can extend _O_[�] _[◦]_ into a space cl( _O_[�] _[◦]_ ) _[∼]_ = cl([�] _S[◦]_ ), so that _π_ 1( _M[◦]_ )0 also acts properly discontinuously on the extended space, with quotient cl( _S[◦]_ ). 

We record the following fact, which will play a key role in our analysis in Section 7. 

**Lemma 5.7.** _Let K be a compact set in_ cl( _O_[�] _[◦]_ ) _. Then the collection of π_ 1( _M[◦]_ ) _h-orbits of K is locally finite in_ cl( _O_[�] _[◦]_ ) _for every h._ 

_Proof._ For _h_ = 0, this follows from the fact that _π_ 1( _M[◦]_ )0 _[∼]_ = _π_ 1( _S[◦]_ ) acts properly discontinuously on cl( _O_[�] _[◦]_ ) _[∼]_ = cl([�] _S[◦]_ ). 

For general _k_ , the set _π_ 1( _M[◦]_ ) _k_ is a coset _π_ 1( _M[◦]_ )0 _· gk_ . Thus the collection of orbits _π_ 1( _M[◦]_ ) _k · K_ = _π_ 1( _M[◦]_ )0 _·_ ( _gk · K_ ) is also locally finite. □ 

Since the deck transformations of _S_[�] _[◦][∼]_ = _O_[�] _[◦]_ over _O[◦]_ is the subgroup _π_ 1( _M_[�] _[◦]_ ) _< π_ 1( _M[◦]_ ) _[∼]_ = _π_ 1( _Mf[◦]_[), where][ �] _M[◦]_ := _M_[�] _\_ ( _∂S_[�] _∪_ sing([�] _ϕ_ )), there is an induced quasi-translation structure on the punctured orbit space _O[◦]_ . In the sequel, we will refer to this structure as the **quasi-translation structure induced by** _S_ . For these quasi-translation surfaces, we have the following construction of convex piecewise linear arcs. 

**Construction 5.8** (Tight arc) **.** Let _B_ be a discrete collection of points in _O_ , containing � _∂S ∪_ sing([�] _ϕ_ ). Let _R_ be a rectangle in _O_ . Let _ℓ_ 1 and _ℓ_ 2 be the two unstable sides of _R_ . Let _R_[!] be the surface obtained by slitting _R_ along the stable leaf segments lying between points of _B_ and points on _ℓ_ 2, see Figure 14. Observe that _R_[!] is simply connected and contained� in _O[◦]_ , thus we can lift _R_[!] to _O_[�] _[◦]_ then use the translation structure charts of _O[◦]_ to identify _R_[!] with a subset of R[2] . 

Let _s_ 1 and _s_ 2 be two opposite corners of _R_ , where _si ∈ ℓi_ for _i_ = 1 _,_ 2. Then the geodesic _p_ between _s_ 1 and _s_ 2 in _R_[!] _⊂_ R[2] (with respect to the standard flat Riemannian metric on R[2] ) is a positive convex piecewise linear arc, where we declare the nodes on _p_ to be the points of _B_ that lie on _p_ . 

Intuitively, _p_ is the arc that one would get if one places pegs at _B_ , lays a tight piece of string hooked across the unstable side _ℓ_ 1 from _s_ 1 to the corner _w_ and the stable side from _w_ to _s_ 2, then releases the hook. See Figure 14. Motivated by this mental picture, we refer to _p_ as a **tight arc** between _s_ 1 and _s_ 2 with respect to _B_ . We refer to _w_ as the **hook** of _p_ . ♢ 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

27 

**==> picture [215 x 100] intentionally omitted <==**

**----- Start of picture text -----**<br>
ℓ 2<br>γ 2<br>B B<br>ℓ 1<br>w<br>γ 1 R [!] ⊂ R R [!] ⊂ R [2]<br>**----- End of picture text -----**<br>


Figure 14. Constructing the tight arc between _γ_ 1 and _γ_ 2 near _w_ with respect to _B_ 

5.4. **Canonical lifts.** We continue the setting from the previous subsection. Let _d_ be a smooth arc on _O[◦]_ . Suppose that _d_ either has positive slope everywhere or negative slope everywhere. Consider the collection of arcs _D_ that consists of the _π_ 1 _M_ -translates of _d_ . Let _D_[�] be the collection of preimages of arcs in _D_ under the cover _S_[�] _[◦][∼]_ = _O_[�] _[◦] →O[◦]_ . This is a _π_ 1( _M[◦]_ ) _[∼]_ = _π_ 1( _Mf[◦]_[)-invariant][collection.] 

Recall that _Mf[◦]_[=][ R] _[ ×][ S][◦][/]_[(] _[s, x]_[)] _[ ∼]_[(] _[s][ −]_[1] _[, f]_[(] _[x]_[)),][thus] _M_[�] _f[◦]_[=][ R] _[ ×][ S][◦]_[.][For][each][element] _[d]_[�] of _D_[�] , we pick a smooth parametrization of _d_[�] , and define the **canonical lift** of _d_[�] (with respect� to _S_ ) to� be the� curve _d_[�] _[∧]_ ( _t_ ) = ([1] 2[log] _[λ][ |]_[ slope] _d_[ �] ( _t_ )[(] _[d]_[�][)] _[|][,][d]_[�][(] _[t]_[))][in] � _M_[�] _f[◦]_[.][In][particular,] _d[∧]_ projects to _d_ . Let _D[∧]_ be the collection of such canonical lifts _d[∧]_ . We claim that _g · d_[�] _[∧]_ = ( _g · d_[�] ) _[∧]_ for every _g ∈ π_ 1( _Mf[◦]_[).][It is clear that both arcs project to] _g·d_[�] , so it suffices to show that the arcs have the same R-coordinate over each point _g·d_[�] ( _t_ ). The element _g_ acts on _M_[�] _f[◦]_[locally of the form (] _[s, x, y]_[)] _[ �→]_[(] _[s]_[ +] _[ k,][ ±][λ][k][x]_[ +] _[ x]_[0] _[,][ ±][λ][−][k][y]_[ +] _[ y]_[0][).] Thus the point of _g · d_[�] _[∧]_ lying over _g · d_[�] ( _t_ ) has R-coordinate[1] 2 _[|]_[ log] _[λ]_[ slope][ �] _d_ ( _t_ )[(] _[d]_[�][)] _[|]_[ +] _[ k]_[,] while the point of ( _g · d_[�] ) _[∧]_ lying over _g · d_[�] ( _t_ ) has R-coordinate[1] 2[log] _[λ][ |]_[ slope] _g·d_[�] ( _t_ )[(] _[g][ ·][d]_[�][)] _[|]_[ =] 12[log] _[λ]_ ��� _λ_ 2 _k_ slope � _d_ ( _t_ )( _d_ �)���, and the two expressions agree. 

In particular, this implies that _D_[�] _[∧]_ is a _π_ 1( _M[◦]_ ) _[∼]_ = _π_ 1( _Mf[◦]_[)-invariant][collection][as][well.] Let _D[∧]_ be the image of _D_[�] _[∧]_ in _M_[�] _[◦]_ . The projection of _D[∧]_ to _O_ are exactly the _π_ 1 _M_ - translates of the initial arc _d_ . In particular, there is an element _d[∧] ∈D[∧]_ lying over _d_ . We refer to it as the **canonical lift** of _d_ (with respect to _S_ ). 

**Construction 5.9** (Bicontact form associated to Birkhoff section) **.** We give another perspective on the canonical lift construction in terms of bicontact structures: The measured foliations ( _ℓ[s] , µ[s]_ ) and ( _ℓ[u] , µ[u]_ ) on _S_ determine closed 1-forms _ds_ and _du_ on _S[◦]_ , locally well-defined up to a sign. Using these, we can locally define the 1-forms 

**==> picture [270 x 32] intentionally omitted <==**

on R _× S[◦]_ . These are locally positive/negative contact forms, respectively, under the orientation _dtdsdu >_ 0. It is straightforward to verify that _ξ_ + _[S]_[=][ ker] _[ α]_ + _[S]_[and] _[ ξ] −[S]_[=][ ker] _[ α] −[S]_ 

CHI CHEUK TSANG 

28 

are transverse, intersecting in the line spanned by _∂t∂_[at][every][point.][Thus][(] _[ξ]_ + _[S][, ξ] −[S]_[)][is][a] bicontact structure, and if _f_ has orientable stable/unstable foliations, so that _α±[S]_[are] well-defined, then ( _α_ + _[S][, α] −[S]_[)][is][a][bicontact][form.] 

In the latter case, one can further compute that the Reeb flow to _α_ + _[S]_[is] 

**==> picture [149 x 26] intentionally omitted <==**

thus ( _α_ + _[S][, α] −[S]_[)][is][a][strongly][adapted][bicontact][form.] 

**Remark 5.10.** Similarly, one can compute that 

**==> picture [154 x 26] intentionally omitted <==**

In the terminology of [Hoz25], ( _α_ + _[S][, α] −[S]_[)][is] **[strongly][bi-adapted]**[.][However,][the][filling] of the bicontact forms that we will do over _∂S_ in Section 8 will destroy the property that _R− ⊂ ξ_ + and only retain strong adaptedness. ♢ 

Since _f[∗] ds_ = _λds_ and _f[∗] du_ = _λ[−]_[1] _du_ up to a sign, _α_ + and _α−_ descend to locally defined positive/negative contact forms on _Mf[◦]_[.][They][determine][a][bicontact][structure][(] _[ξ]_[+] _[, ξ][−]_[)] supporting _ϕf_ , and if _f_ has orientable stable/unstable foliations, and _f_ preserves those orientations, so that _α±_ are well-defined, then ( _α_ + _, α−_ ) is a strongly adapted bicontact form supporting _ϕf_ . 

By Proposition 5.3, the orbit equivalence _Mf[◦][∼]_[=] _[M][ ◦]_[can][be][assumed][to][be][smooth.] Thus we can transfer ( _ξ_ + _, ξ−_ ) into a bicontact structure that supports _ϕ_ on _M[◦]_ . The canonical lift of _d ⊂O[◦]_ can now be defined as the unique arc in _M_[�] _[◦]_ lying over _d_ that is Legendrian with respect to the lifted contact structure _ξ_[�] _±_ on _M_[�] , where the sign is negative/positive depending on whether _d_ has positive/negative slope, respectively. ♢ 

**Remark 5.11.** Suppose _∂S_ is disjoint from sing( _ϕ_ ), then the canonical lift construction can be extended to arcs _d_ with endpoints on sing([�] _ϕ_ ) and where the slope of int( _d_ ) is constant near the endpoints: One first takes the canonical lift int( _d_ ) _[∧]_ of int( _d_ ) away from the endpoints. Since the slope of int( _d_ ) is constant near the endpoints, each end of int( _d_ ) _[∧]_ limits onto a single point on sing([�] _ϕ_ ). The **canonical lift** of _d_ can thus be defined to be the union of int( _d_ ) _[∧]_ and these limit points. ♢ 

## 5.5. **Slope criterion.** We are now ready to state our new criterion for diagonals. 

**Definition 5.12** (Slope criterion) **.** Let _S_ be a Birkhoff section to _ϕ_ with boundary orbits disjoint from _C_ . We say that a diagonal system _{dR}_ satisfies the **slope criterion** with respect to _S_ if under the induced quasi-translation structure on _O[◦]_ , the interior of every _dR_ is a smooth arc in _O[◦]_ with constant slope near its endpoints, and for every _R_ 1 _< R_ 2, 

- if _R_ 1 and _R_ 2 share a corner, then int( _dR_ 1) and int( _dR_ 2) are disjoint, and 

29 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

- if _R_ 1 and _R_ 2 do not share a corner, then int( _dR_ 1) and int( _dR_ 2) intersect at exactly one point _v_ , with _|_ slope _v_ ( _dR_ 1) _| < |_ slope _v_ ( _dR_ 2) _|_ . 

♢ 

**Proposition 5.13.** _Let ϕ be a pseudo-Anosov flow on M with no perfect fits relative to C. Let {dR} be a diagonal system satisfying the slope criterion with respect to a Birkhoff section S. Then the veering triangulation_ ∆ _associated to_ ( _ϕ, C_ ) _can be put in Legendrian position with respect to ϕ and the bicontact form_ ( _α_ + _[S][, α] −[S]_[)] _[,][with][d][R][being] the projections to O of the edges of the lift_ ∆[�] _to M_[�] _._ 

> _Proof._ For each _R_ , we let _d[∧] R_[be][the][canonical][lift][of] _[d][R]_[.][Here][we][use][the][fact][that] _[d][R]_ has constant slope near its endpoints, so that we can take its canonical lift even if it has an endpoint on a singular point, as explained in Remark 5.11. The first item in Definition 5.12 immediately implies that _{dR}_ , thus _{d[∧] R[}]_[,][satisfies][the] face embeddedness criterion. 

Next, we verify that _{d[∧] R[}]_[ satisfies the crossing criterion:][Suppose] _[ R]_[1] _[< R]_[2][and suppose] _v_ is an intersection point between int( _dR_ 1) and int( _dR_ 2). By the slope criterion, we have _|_ slope _v_ ( _dR_ 1) _| < |_ slope _v_ ( _dR_ 2) _|_ . But for _i_ = 1 _,_ 2, the R-coordinate of _d[∧] Ri_[over] _[v]_[is] 1[so] _[v]_[is][the][projection][of][a][crossing][of] _[d][∧][d][∧]_ 2[log] _[λ][ |]_[ slope] _[v]_[(] _[d][R][i]_[)] _[|]_[,] _R_ 2[over] _R_ 1[.] 

Thus by Proposition 4.6, the veering triangulation ∆can be placed in transverse position with respect to _ϕ_ , with _d[∧] R_[being][the][edges][of][∆][�][.][As][explained][in][Construction][5.9][,] _[d][∧] R_ are Legendrian with respect to _α_[�] _±[S]_[,][lifted][from][the][contact][forms] _[α] ±[S]_[associated][to] _[S]_ and which support _ϕ_ on _M[◦]_ . Thus ∆is in fact in Legendrian position with respect to _ϕ_ . □ 

## 6. Constructing piecewise linear diagonals 

The final three sections of this paper is devoted to proving the main theorems Theorem 1.1 and Theorem 1.2. In this section, we will construct an initial diagonal system. The precise objective is the following proposition. 

**Proposition 6.1.** _Let ϕ be a pseudo-Anosov flow on M with no perfect fits relative to C. Let S be a Birkhoff section with boundary orbits disjoint from C. Then there exists a diagonal system {dR} such that:_ 

- _(1) The interior of each dR is a piecewise linear arc in O[◦] , under the quasi-translation structure induced from S._ 

- _(2) The system {dR} satisfies the following proxy of the slope criterion: For every R_ 1 _< R_ 2 _of the same color,_ 

   - _if R_ 1 _and R_ 2 _share a corner, then_ int( _dR_ 1) _and_ int( _dR_ 2) _are disjoint, and_ 

   - _if R_ 1 _and R_ 2 _do not share a corner, then_ int( _dR_ 1) _and_ int( _dR_ 2) _overlap along a (possibly degenerate) subarc r, with |_ slope _r_ ( _dR_ 1) _| < |_ slope _r_ ( _dR_ 2) _|._ 

30 

## CHI CHEUK TSANG 

Figure 15. Our diagonals _dR_ will be the union of two half-diagonals, each half-diagonal being a tight arc near near the corner that lies on the same stable leaf as the anchor, with respect to the buoys. 

- _(3) If b is a node of some diagonal dR_ 1 _that lies on some other diagonal dR_ 2 _, then it is a node of dR_ 2 _._ 

- _(4) If b_ 1 _and b_ 2 _are adjacent nodes on a diagonal, then b_ 1 _and b_ 2 _do not lie in the same π_ 1 _M -orbit._ 

We provide a quick outline of our construction: In Section 6.1, we will choose a point _αR_ in the interior of each edge rectangle _R_ , which we refer to as the **anchor** . This terminology is taken from [LMT23], but we will strengthen their work in order to choose anchors with better properties. Writing the elements of _C_ at the corners of _R_ to be _s_ 1 and _s_ 2, we refer to the subrectangles _R_ ( _s_ 1 _, αR_ ) and _R_ ( _s_ 2 _, αR_ ) as the **anchor subrectangles** . 

Our diagonals _dR_ will be the union of two half-diagonals, each contained in an anchor subrectangle. In turn, each half-diagonal is the tight arc whose hook is the corner that lies on the same stable leaf as the anchor, with respect to a collection _B_ , which we refer to as the **buoys** (terminology also taken from [LMT23]). The larger the collection _B_ , the more ‘tight’ the half-diagonals will be. Thus the diagonals will end up resembling Figure 15. 

By choosing enough buoys, we can ensure that the diagonals lie within _O[◦]_ . Then (1) will be true. We will explain this in Section 6.2. 

The bulk of the remaining work is to show (2), regarding the slope inequality. To this end, we inspect the intersections of anchor subrectangles. There are many possible configurations here, but the strategy is the uniform: We tighten the half-diagonals by enlarging the collection of buoys _B_ . For the sake of presentation, we divide up the cases into three batches, to be covered from Section 6.3 to Section 6.5. 

The third and fourth items are technical conditions that will come into play in Section 7.1. We will arrange for them in Section 6.6. 

6.1. **Casting anchors.** We make the following definition. 

**Definition 6.2** ((Strict) anchor system) **.** An **anchor** for an edge rectangle _R_ is a point contained in the interior of _R_ . 

An **anchor system** is a collection _{αR | R_ is an edge rectangle _}_ that is 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

31 

**==> picture [122 x 115] intentionally omitted <==**

**----- Start of picture text -----**<br>
R 3<br>αR 3<br>R 2<br>αR 2 R 1<br>αR 1<br>s<br>**----- End of picture text -----**<br>


Figure 16. Definition of strictly staircase monotone. 

- equivariant, i.e. _g · αR_ = _αg·R_ , and 

- **staircase monotone** , i.e. for every _R_ 1 _< R_ 2 that share a corner _s_ , _R_ ( _s, αR_ 1) is wider and strictly shorter than _R_ ( _s, αR_ 2). 

This is the same definition as in [LMT23, Section 5.1.1]. Meanwhile, the following definition is new. 

A **strict anchor system** is a collection of one anchor _αR_ per edge rectangle _R_ that is 

- equivariant, and 

- **strictly staircase monotone** , i.e. for every _R_ 1 _< R_ 2 that share a corner _s_ , _R_ ( _s, αR_ 1) is strictly wider and strictly shorter than _R_ ( _s, αR_ 2). See Figure 16. 

♢ 

In [LMT23, Lemma 5.10], Landry-Minsky-Taylor showed that anchor systems exist. The goal of this subsection is to prove the following upgrade. 

**Proposition 6.3.** _There exists a strict anchor system {αR}. Moreover, given any finite collection of closed orbits B, the anchors αR can be chosen to be periodic and disjoint from B_[�] _._ 

We reuse the following notions in [LMT23] and blackbox some lemmas whose proofs are not important to this paper. 

**Definition 6.4** (Core point, staircase, pinched) **.** Let _R_ be an edge rectangle. There exists a bi-infinite sequence of edge rectangles ( _Rn_ ) _n∈_ Z such that _R_ 0 = _R_ , and such that for each _n_ , there exists a tetrahedron rectangle _Tn_ such that _Rn_ +1 is the top edge subrectangle and _Rn_ is the bottom edge subrectangle of _Tn_ . It can be shown that[�] _n[R][n]_ is a single periodic point, see [LMT23, Fact 4.4]. We refer to this point as the **core point** of _R_ and denote it by _c_ ( _R_ ). 

Let _s_ be a point of _C_[�] . Consider the collection of edge rectangles that occupy a common quadrant of _s_ . This collection is totally ordered by the relation ‘lying above’. We refer to the union of these rectangles as a **staircase** at _s_ . If _R_ 1 _, ..., Rn_ are consecutive 

CHI CHEUK TSANG 

32 

rectangles in the staircase with _c_ ( _R_ 1) = _..._ = _c_ ( _Rn_ ), we say that _R_ 1 _, ..., Rn_ are **pinched** , and also that _c_ is a **pinched** core point. 

If _c_ is a pinched core point, the **preimage** of _c_ is the collection _O[◦]_ of edge rectangles that have core point at _c_ . It can be shown that all edge rectangles in _O[◦]_ have the same color, see [LMT23, Lemma 5.6]. Depending on whether these rectangles are red/blue, we say that _c_ is **red/blue** respectively. ♢ 

**Lemma 6.5** ([LMT23, Lemma 5.5]) **.** _For any edge rectangles Q_ 1 _and Q_ 2 _that share a corner s, if Q_ 2 _> Q_ 1 _, then either c_ ( _Q_ 1) = _c_ ( _Q_ 2) _, or R_ ( _s, c_ ( _Q_ 1)) _is strictly wider and strictly shorter than R_ ( _s, c_ ( _Q_ 2)) _._ 

In other words, the core points are almost a strict anchor system, except they might overlap for pinched rectangles. Thus one needs to push the pinched core points apart. The following definition gives a permissible region for one to do so. 

**Definition 6.6** (Core box) **.** A **core box system** is a collection of rectangles _{b_ ( _R_ ) _| R_ is an edge rectangle _}_ satisfying: 

- _c_ ( _R_ ) _∈ b_ ( _R_ ) _⊂_ int( _R_ ) for every edge rectangle _R_ , 

- _b_ ( _g · R_ ) = _g · b_ ( _R_ ) for every _g ∈ π_ 1 _M_ and edge rectangle _R_ , and 

- for any edge rectangles _R_ 1 and _R_ 2 that share a corner _s_ , if _R_ 1 _< R_ 2 and _c_ ( _R_ 1) _̸_ = _c_ ( _R_ 2), then _R_ ( _s, t_ 1) is strictly wider and strictly shorter than _R_ ( _s, t_ 2), for every _t_ 1 _∈ b_ ( _R_ 1) and _t_ 2 _∈ b_ ( _R_ 2). ♢ 

**Lemma 6.7** ([LMT23, Claim 5.7]) **.** _There exists a core box system._ 

Meanwhile, the following lemma gives a framework for the pushing process. 

**Lemma 6.8.** _Let c be a pinched core point. Let P be the preimage of c. There exists an embedding of partially ordered sets_ 

**==> picture [444 x 37] intentionally omitted <==**

_for some m_ 0 _, n_ 0 _, r ∈_ Z+ _, where elements of P are ordered by the relation ‘lying above’ and the element of G are ordered by_ ( _m_ 1 _, n_ 1) _≤_ ( _m_ 2 _, n_ 2) _if m_ 1 _≤ m_ 2 _and n_ 1 _≤ n_ 2 _, such that:_ 

**==> picture [413 x 56] intentionally omitted <==**

- _R_ 1 _, R_ 2 _∈_ P _share a corner if and only if ι_ ( _R_ 1) _and ι_ ( _R_ 2) _share a coordinate._ 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

33 

**==> picture [310 x 132] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>M<br>3<br>[ c ]<br>2 3<br>1<br>N 2<br>1<br>1<br>2<br>[ c ]<br>1 2 3 4<br>N<br>3 M<br>**----- End of picture text -----**<br>


Figure 17. Defining the embedding _ι_ : _P → G_ . 

_Proof._ We first suppose that _c_ is orientation-preserving. Let _M, N ⊂ C_[�] be the two sets of corners of rectangles in _P_ occupying the two quadrants of _c_ . By Proposition 3.2, _M_ and _N_ are order isomorphic to Z under the relation _m_ 1 _< m_ 2 if _R_ ( _c, m_ 1) _< R_ ( _c, m_ 2). Moreover, identifying _M, N[∼]_ = Z, the element [ _c_ ] acts by _m �→ m_ + _m_ 0 and _n �→ n_ + _n_ 0 on _M_ and _N_ respectively, for some _m_ 0 _, n_ 0 _∈_ Z+. We define the embedding _ι_ by mapping a rectangle _R_ to its pair of corners in _C_[�] . We demonstrate a local example in Figure 17. 

It remains to show that the image of _ι_ lies in some strip _{_ ( _m, n_ ) _∈_ Z[2] _|[m] n_ 0[0] _[n][ −][r][≤][m][ ≤] m_ 0[First][note][that][for][each] _[m][ ∈][M]_[,][there][can][only][be][finitely][many][elements][of] _n_ 0 _[n]_[ +] _[ r][}]_[.] _P_ that have a corner at _m_ . This is because otherwise there will be a staircase _S_ at _m_ with infinitely many consecutive pinched elements. But _⟨_ [ _m_ ] _⟩_ acts cofinitely on _S_ , and for any _R ∈ S_ , [ _m_ ] _· R_ cannot be pinched with _R_ , since _c_ ([ _m_ ] _· R_ ) = [ _m_ ] _· c_ ( _R_ ) _̸_ = _c_ ( _R_ ). Now using the equivariance under _⟨_ [ _c_ ] _⟩_ , we deduce that every _m ∈ M_ can have only boundedly many elements of _P_ that have a corner at _m_ . A similar statement holds for every _n ∈ N_ . It follows from this that the image of _ι_ lies within a strip. 

The proof when _c_ is orientation-reversing is similar. We outline the key differences: We define _M, N_ in the same way. Now [ _c_ ] maps _M_ to _N_ and _N_ to _M_ . We choose the identifications _M, N[∼]_ = Z such that the map [ _c_ ] : _N → M_ is identity. Then the map [ _c_ ] : _M → N_ is _m �→ m_ + _r_ for some _r ∈_ Z+. Since [ _c_ ] _· R > R_ for each _R ∈_ R, the image of _ι_ must lie within the strip _{_ ( _m, n_ ) _∈_ Z[2] _| m ≤ n ≤ m_ + _r}_ . □ 

**Lemma 6.9.** _Fix a core box system {b_ ( _R_ ) _}. Let c be a pinched core point. Let P be the collection of edge rectangles that have core point c. Then there exists a collection of rectangles {b[′]_ ( _R_ ) _| R ∈P} satisfying_ 

- _b[′]_ ( _R_ ) _⊂ b_ ( _R_ ) _,_ 

- [ _c_ ] _· b[′]_ ( _R_ ) = _b[′]_ ([ _c_ ] _· R_ ) _for every R ∈P, and_ 

- _for every R_ 1 _, R_ 2 _∈P that share a corner s, if R_ 1 _< R_ 2 _, then R_ ( _s, t_ 1) _is strictly wider and strictly shorter than R_ ( _s, t_ 2) _, for every t_ 1 _∈ b[′]_ ( _R_ 1) _and t_ 2 _∈ b[′]_ ( _R_ 2) _._ 

34 

## CHI CHEUK TSANG 

**==> picture [295 x 146] intentionally omitted <==**

**----- Start of picture text -----**<br>
m 2<br>m 1<br>c<br>( m 2 , n 1) ( m 1 , n 1)<br>n 1<br>( m 2 , n 2) ( m 1 , n 2 )<br>n 2<br>[ c ]<br>[ c ]<br>**----- End of picture text -----**<br>


Figure 18. Defining the maps _r, t_ . 

_Proof._ Let _P_ be the union of rectangles in _P_ . There exists an embedding Ψ : _P �→_ R[2] that maps _O[s/u]_ to vertical/horizontal lines and is equivariant under the action of _⟨_ [ _c_ ] _⟩_ on _P_ and the action of _⟨_ [ _c_ ] _⟩_ on R[2] with 

**==> picture [299 x 37] intentionally omitted <==**

for some _λ >_ 1, as explained in [LMT23, Claim 5.8]. 

Without loss of generality suppose _c_ is red. We fix an embedding _P �→ G_ as in Lemma 6.8. Up to composing Ψ with the reflection ( _x, y_ ) _�→_ ( _y, x_ ), we can assume that if _ι_ ( _R_ 1) and _ι_ ( _R_ 2) have the same first/second coordinate, then Ψ( _R_ 1) and Ψ( _R_ 2) share a corner that lies in the first/third quadrant of 0 in R[2] , respectively. 

We first suppose that _c_ is orientation-preserving. Consider the map _r_ : R+ _×_ R _− →_ R[2] defined by ( _x, y_ ) _�→_ ( _u, v_ ) = (log _λ x −_ log _λ_ ( _−y_ ) _, −_ log _λ x −_ log _λ_ ( _−y_ )). The stable leaves are sent to lines of slope 1, while the unstable leaves are sent to lines of slope _−_ 1. The action of _⟨_ [ _c_ ] _⟩_ is conjugated to the translation [ _c_ ] _·_ ( _u, v_ ) = ( _u −_ 2 _, v_ ). 

We now define an embedding _t_ : Z[2] _→_ R[2] by _t_ ( _m, n_ ) = ( _− m[m]_ 0 _[−] n[n]_ 0 _[,]_[2] _m[m]_ 0 _[−]_[2] _n[n]_ 0[).][Observe] that the composed map _r[−]_[1] _t_ satisfies the following properties: 

- [ _c_ ] _· r[−]_[1] _t_ ( _m, n_ ) = _r[−]_[1] _t_ ( _m_ + _m_ 0 _, n_ + _n_ 0) for every ( _m, n_ ) _∈_ Z[2] , 

- for every _m, n_ 1 _, n_ 2 _∈_ Z with _n_ 1 _< n_ 2, _R_ (0 _, r[−]_[1] _t_ ( _m, n_ 1)) is strictly thinner and strictly shorter than _R_ (0 _, r[−]_[1] _t_ ( _m, n_ 2)), and 

- for every _m_ 1 _, m_ 2 _, n ∈_ Z with _m_ 1 _< m_ 2, _R_ (0 _, r[−]_[1] _t_ ( _m_ 1 _, n_ )) is strictly wider and strictly taller than _R_ (0 _, r[−]_[1] _t_ ( _m_ 2 _, n_ )). 

See Figure 18. 

This implies that the composed map _T_ := Ψ _[−]_[1] _r[−]_[1] _tι_ satisfies the following properties: 

- [ _c_ ] _· T_ ( _R_ ) = _T_ ([ _c_ ] _· R_ ) for every _R ∈P_ , and 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

35 

**==> picture [321 x 138] intentionally omitted <==**

**----- Start of picture text -----**<br>
4<br>(4 ,  4)<br>3<br>4<br>(3 ,  3) 2 H<br>[ c ]  · H<br>(2 ,  2) (3 ,  4) 1 3<br>(1 ,  1) c<br>2<br>(1 ,  2)(2 ,  3) (1 ,  3)<br>1 [ c ] [−] [1] · H<br>2 (2 ,  4) 1<br>3<br>1 2 3 4<br>4<br>**----- End of picture text -----**<br>


Figure 19. The map _T_ in the orientation-reversing case. This figure illustrates the case when _r_ = 2. 

- for every _R_ 1 _, R_ 2 _∈P_ that share a corner _s_ , if _R_ 1 _< R_ 2, then _R_ ( _s, T_ ( _R_ 1)) is strictly wider and strictly shorter than _R_ ( _s, T_ ( _R_ 2)). 

Using the fact that the image of _ι_ lies within a strip _{_ ( _m, n_ ) _∈_ Z[2] _| m[n]_[0] 0 _[m][ −][r][≤][n][≤] n_ 0[we][can][compose][Ψ][with][a][dilation][(] _[x, y]_[)] _[�→]_[(] _[ρx, ρy]_[)][for][large] _[ρ]_[,][so][that] _m_ 0 _[m]_[ +] _[ r][}]_[,] _T_ ( _R_ ) _∈ b_ ( _R_ ) for every _R ∈P_ . Thus it remains to take _b[′]_ ( _R_ ) to be a small rectangle neighborhood of _T_ ( _R_ ), _⟨_ [ _c_ ] _⟩_ -equivariantly, for each _R ∈P_ . 

Next, we tackle the case when _c_ is orientation-reversing. We set _H_ = _{_ ( _m, n_ ) _∈ G |_ 0 _≤ m < r, n < r}_ , then _H_ is a fundamental domain of the action of _⟨_ [ _c_ ] _⟩_ on _G_ . We define the maps _r_ and _t_ as in the orientation-preserving case, but now we set 

**==> picture [273 x 37] intentionally omitted <==**

In other words, we define _T_ to be Ψ _[−]_[1] _r[−]_[1] _tι_ on _ι[−]_[1] ( _H_ ), and extend by equivariance. We then claim that _T_ satisfies the following properties: 

- [ _c_ ] _· T_ ( _R_ ) = _T_ ([ _c_ ] _· R_ ) for every _R ∈P_ , and 

- for every _R_ 1 _, R_ 2 _∈P_ that share a corner _s_ , if _R_ 1 _< R_ 2, then _R_ ( _s, T_ ( _R_ 1)) is strictly wider and strictly shorter than _R_ ( _s, T_ ( _R_ 2)). 

The first item follows from our definition by equivariance. For the second item, observe that if _ι_ ( _R_ 1) = ( _m, n_ 1) and _ι_ ( _R_ 2) = ( _m, n_ 2) with _n_ 1 _< n_ 2, then either ( _m, n_ 1) _,_ ( _m, n_ 2) _∈_ [ _c_ ] _[k] H_ , in which case the property is inherited from Ψ _[−]_[1] _r[−]_[1] _tι_ , or ( _m, n_ 1) _∈_ [ _c_ ][2] _[k][−]_[1] _H_ and ( _m, n_ 2) _∈_ [ _c_ ][2] _[k] H_ , in which case the property holds since _r[−]_[1] _t_ ( _m, n_ 1) lies in the second quadrant R _− ×_ R+ while _r[−]_[1] _t_ ( _m, n_ 2) lies in the fourth quadrant R+ _×_ R _−_ . One can check similarly if _ι_ ( _R_ 1) = ( _m_ 1 _, n_ ) and _ι_ ( _R_ 2) = ( _m_ 2 _, n_ ) with _m_ 1 _< m_ 2. See Figure 19. 

As in the orientation-preserving case, it remains to compose Ψ with a dilation so that _T_ ( _R_ ) _∈ b_ ( _R_ ) for every _R ∈P_ , and take _b[′]_ ( _R_ ) to be a small rectangle neighborhood of _T_ ( _R_ ), _⟨_ [ _c_ ] _⟩_ -equivariantly, for each _R ∈P_ . □ 

CHI CHEUK TSANG 

36 

Putting the core boxes and the smaller boxes in Lemma 6.9 together, we deduce the following lemma. 

**Lemma 6.10.** _There exists a collection of rectangles {b[′]_ ( _R_ ) _| R is an edge rectangle} satisfying_ 

- _b[′]_ ( _R_ ) _⊂_ int( _R_ ) _,_ 

- _g · b[′]_ ( _R_ ) = _b[′]_ ( _g · R_ ) _for every g ∈ π_ 1 _M and edge rectangle R, and_ 

- _for any edge rectangle R_ 1 _and R_ 2 _that share a corner s, if R_ 1 _< R_ 2 _, then R_ ( _s, t_ 1) _is strictly wider and strictly shorter than R_ ( _s, t_ 2) _, for every t_ 1 _∈ b[′]_ ( _R_ 1) _and t_ 2 _∈ b[′]_ ( _R_ 2) _._ 

_Proof._ Fix a core box system _{b_ ( _R_ ) _}_ . For each non-pinched rectangle _R_ , we set _b[′]_ ( _R_ ) = _b_ ( _R_ ). Since each pinched rectangle has a unique pinched core point, we can apply Lemma 6.9 to one representative in each _π_ 1 _M_ -orbit of pinched core points, then extend equivariantly, in order to define _b[′]_ ( _R_ ) for all pinched rectangles. The first two items are immediate. The third item follows from the last item of Definition 6.6 and the last item in Lemma 6.9. □ _Proof of Proposition 6.3._ Fix a collection of rectangles _{b[′]_ ( _R_ ) _}_ as in Lemma 6.10. We pick _αR_ to be a periodic point in _b[′]_ ( _R_ ) disjoint from _B_[�] for a representative _R_ of each _π_ 1 _M_ -orbit of edge rectangles and extend to all other edge rectangles by equivariance. □ 

6.2. **Keeping diagonals away from boundary orbits.** For the rest of this section, we fix a strict anchor system _{αR}_ that is disjoint from _∂S_[�] . We use the following terminology: If _R_ is an edge rectangle with corners _s_ 1 _, s_ 2 _∈C_ , we refer to the subrectangles _R_ ( _s_ 1 _, αR_ ) and _R_ ( _s_ 2 _, αR_ ) as the **anchor subrectangles** . 

Let _B_ be a discrete collection of points in _O_ . We refer to the points in _B_ as the **buoys** . The **anchor half-diagonal** in an anchor subrectangle _R_ ( _si, αR_ ) with respect to _B_ is the tight arc between _si_ and _αR_ whose hook is the corner that lies on the same stable leaf as _αR_ , with respect to _B_ . The **anchor diagonal** in _R_ with respect to _B_ is the union of the two anchor half-diagonals with respect to _B_ . If _B_ is _π_ 1 _M_ -invariant, then the collection of anchor diagonals with respect to _B_ is a diagonal system. 

We first add enough buoys so that the interior of the anchor diagonals lie within _O[◦]_ . 

**Lemma 6.11.** _There exists a discrete π_ 1 _M -invariant collection of points B_ 0 _such that for every discrete collection of points B ⊃B_ 0 _, the interior of the anchor diagonals with respect to B lie within O[◦] ._ 

_Proof._ Since _∂S_[�] is discrete, for every anchor subrectangle _R[′]_ , we can find a finite collection of periodic points _BR′ ⊂_ int( _R[′]_ ) such that all points of _∂S_[�] _∩ R[′]_ lie strictly to one side of the anchor half-diagonal in _R[′]_ with respect to _BR′_ . This property continues 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

37 

to hold for the anchor half-diagonal in _R[′]_ with respect to any _B ⊃BR′_ . In particular, it implies that the interior of the anchor half-diagonal lies within _O[◦]_ . 

We take the union of _BR′_ over one representative in each _π_ 1 _M_ -orbit of anchor subrectangles, then take its _π_ 1 _M_ -orbit, in order to get _B_ 0. Here we use the fact that the anchors are disjoint from _∂S_[�] to ensure that the anchor diagonals have interior disjoint from _∂S_[�] , after concatenating the anchor half-diagonals. □ 

6.3. **Analyzing half-diagonal intersections.** In this subsection, we begin analyzing intersection points between diagonals. Since our diagonals come as the union of two half-diagonals, it is natural to analyze intersection points between half-diagonals instead. We do so by categorizing pairs of anchor rectangles as follows. 

**Definition 6.12** (Type (0)/(I)/(II) pairs) **.** Suppose _R_ 1 and _R_ 2 are edge rectangles of the same color, with _R_ 1 _< R_ 2. Suppose _R_ 1 _[′]_[=] _[R]_[(] _[s]_[1] _[, α][R]_ 1[)][and] _[R]_ 2 _[′]_[=] _[R]_[(] _[s]_[2] _[, α][R]_ 2[)][are] anchor subrectangles of _R_ 1 and _R_ 2 that intersect. 

We say that the pair ( _R_ 1 _[′][, R]_ 2 _[′]_[) is of] **[type (0)]**[ if] _[ R]_ 1 _[′]_[and] _[ R]_ 2 _[′]_[overlap along some subsegment] of a side. 

We say that the pair ( _R_ 1 _[′][, R]_ 2 _[′]_[)][is][of] **[type][(I)]**[if] _[R]_ 1 _[′]_[and] _[R]_ 2 _[′]_[are][not][of][type][(0),][and][the] **hooked arcs** _h[′] i_[obtained][by][traversing][the][unstable][side][of] _[R] i[′]_[containing] _[s][i]_[then][the] stable side of _Ri[′]_[containing] _[α][R] i_[,][for] _[i]_[ = 1] _[,]_[ 2,][are][disjoint.] 

We say that the pair ( _R_ 1 _[′][, R]_ 2 _[′]_[)][is][of] **[type][(II)]**[if] _[R]_ 1 _[′]_[and] _[R]_ 2 _[′]_[are][not][of][type][(0),][and][the] hooked arcs _h[′]_ 1[and] _[h][′]_ 2[defined][above][intersect.] ♢ 

The analysis for type (0) pairs is relatively straightforward and only uses the following lemma. 

**Lemma 6.13.** _Let B be a discrete collection of points in O. Let P and Q be two rectangles in O, with Q > P , and which share a corner v. Let p be a tight arc between v and its opposite corner in P with respect to B ∩_ int( _P_ ) _, and q be a tight arc between v and its opposite corner in Q with respect to B ∩_ int( _Q_ ) _. Suppose that the interiors of p and q lie in O[◦] ._ 

_Furthermore, suppose that v and the hooks wp and wq of p and q either all lie on the same stable or all lie on the same unstable leaf. Then p and q overlap along a (possibly degenerate) connected subarc r containing v, and are disjoint away from r. Moreover, we have |_ slope _r_ ( _p_ ) _| < |_ slope _r_ ( _q_ ) _|._ 

_Proof._ Without loss of generality, suppose _p_ and _q_ are positive and _v_ , _wp_ , _wq_ lie on the same unstable leaf. Let _R_ = _P ∩ Q_ and define _R_[!] as in Construction 5.8. Choose a chart of _R_[!] into R[2] such that _v_ is mapped to the bottom-left corner. Then _p ∩ R_ and _q ∩ R_ are geodesics in _R_[!] _⊂_ R[2] . See Figure 20 left. 

To show that _p_ and _q_ overlap in a (possibly degenerate) connected subarc _r_ containing _v_ , it suffices to show that there cannot exist subarcs _p[′] ⊂ p_ and _q[′] ⊂ q_ which cobound a 

38 

## CHI CHEUK TSANG 

**==> picture [191 x 91] intentionally omitted <==**

**----- Start of picture text -----**<br>
q [′]<br>p [′]<br>tp<br>Q P<br>**----- End of picture text -----**<br>


Figure 20. Left: The setting of Lemma 6.13. Right: There cannot exists subarcs _p[′] ⊂ p_ and _q[′] ⊂ q_ that cobound a disc. 

disc. Suppose otherwise, and suppose _p[′]_ has a turn _tp_ = ( _xt, yt,p_ ). Then _q[′]_ must contain a point ( _xt, yt,q_ ) with _yt,q ≤ yt,p_ , since otherwise _q_ would pass through one of the slits in _R\R_[!] . See Figure 20 right. In fact we must have _yt,q < yt,p_ , otherwise _p[′]_ and _q[′]_ would not cobound a disc. Similarly, if _q[′]_ has a turn _tq_ = ( _xt, yt,q_ ). Then _p[′]_ must contain a point ( _xt, yt,p_ ) with _yt,p < yt,q_ . Thus _p[′]_ and _q[′]_ cannot both have turns. 

Without loss of generality, suppose _p[′]_ has no turns, so that _p[′]_ is actually a straight arc. But then _q[′]_ must also be straight, since otherwise the path obtained by excising _q[′]_ out of _q_ and replacing it with _p[′]_ is shorter. Thus _p[′]_ and _q[′]_ completely overlap and cannot cobound a disc. 

We write _p_ = _r∗v_ 2 _p_ 2 and _q_ = _r∗v_ 2 _q_ 2. If _|_ slope _v_ 2( _p_ 2) _| > |_ slope _v_ 2( _q_ 2) _|_ , then _p_ 2 and _q_ 2 must intersect somewhere in their interiors. This contradicts the connectedness of the overlap between _p_ and _q_ which we have just proved. Simiarly, if _|_ slope _v_ 2( _p_ 2) _|_ = _|_ slope _v_ 2( _q_ 2) _|_ , then _p_ 2 and _q_ 2 must overlap along some nondegenerate subarc, contradicting the definition of _r_ . Thus _|_ slope _v_ 2( _p_ 2) _| < |_ slope _v_ 2( _q_ 2) _|_ , so we have _|_ slope _r_ ( _p_ ) _| < |_ slope _r_ ( _q_ ) _|_ . □ 

**Lemma 6.14.** _Let B be a discrete π_ 1 _M -invariant collection of points. Let {dR} be the diagonal system consisting of anchor diagonals with respect to B. Then whenever_ ( _R_ 1 _[′][, R]_ 2 _[′]_[)] _[is][a][type][(0)][pair][of][anchor][rectangles,][the][anchor][half-diagonals][in][R]_ 1 _[′][and][R]_ 2 _[′] overlap along a (possibly degenerate) subarc r, with |_ slope _r_ ( _dR_ 1) _| < |_ slope _r_ ( _dR_ 2) _|._ 

_Proof._ Write _R_ 1 _[′]_[=] _[ R]_[(] _[s]_[1] _[, α][R]_ 1[)][and] _[R]_ 2 _[′]_[=] _[ R]_[(] _[s]_[2] _[, α][R]_ 2[).][Since][both] _[s][i]_[and] _[α][R] i_[are][periodic,] if _R_ 1 _[′]_[and] _[R]_ 2 _[′]_[overlap][along][some][subsegment][of][a][side,][we][must][have][either] _[α][R]_ 1[=] _[ α][R]_ 2 or _s_ 1 = _s_ 2. In the former case, we have _R_ 1 _[′][< R]_ 2 _[′]_[since][we][are][assuming][that] _[R]_[1] _[< R]_[2][,] thus we conclude by Lemma 6.13. In the latter case, we have _R_ 1 _[′][< R]_ 2 _[′]_[since] _[{][α][R][}]_[is][a] strict anchor system, thus we conclude by Lemma 6.13 as well. □ 

In the next two subsections, we will analyze the type (I) and type (II) pairs. Suppose we have such a pair ( _R_ 1 _[′][, R]_ 2 _[′]_[).][The][stable][and][unstable][leaves][that][contain][the][sides][of] _R_ 2 _[′]_[cut][the][orbit][space] _[O]_[into][nine][components.][Since] _[R]_ 1 _[′]_[and] _[R]_ 2 _[′]_[do][not][overlap][along] any sides, _s_ 1 and _αR_ 1 must lie in the interior of one of these components. Thus there are 81 possible configurations here. 

Of these configurations, we can rule out all but 8 by using the assumptions that: 

39 

**==> picture [270 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
LEGENDRIAN POSITION OF VEERING TRIANGULATIONS<br>**----- End of picture text -----**<br>


**==> picture [312 x 163] intentionally omitted <==**

**----- Start of picture text -----**<br>
I-1 I-2 I-3 I-4<br>II-1 II-2 II-3 II-4<br>**----- End of picture text -----**<br>


Figure 21. The possible configurations of type (I) and (II) pairs. 

- _R_ 1 is an edge rectangle, thus _s_ 2 cannot lie within _R_ 1 _[′]_[.] 

- _R_ 2 is an edge rectangle, thus _s_ 1 cannot lie within _R_ 2 _[′]_[.] 

- _R_ 1 _< R_ 2. 

- _R_ 1 and _R_ 2 are of the same color. 

- _R_ 1 _[′]_[and] _[R]_ 2 _[′]_[intersect.] 

Of the remaining 8 configurations, 4 of them are of type (I). We exhibit these in Figure 21 top row (in the case when _R_ 1 and _R_ 2 are red), and label them type (I-1) - (I-4) accordingly. 

The last 4 configurations are of type (II). We exhibit these in Figure 21 bottom row (in the case when _R_ 1 and _R_ 2 are red), and label them type (II-1) - (II-4) accordingly. 

- 6.4. **Eliminating avoidable intersections.** We turn to analyze the type (I) pairs. 

**Lemma 6.15.** _There exists a discrete π_ 1 _M -invariant collection of points B_ 0 _such that for every discrete π_ 1 _M -collection of points B ⊃B_ 0 _, if {dR} is the diagonal system consisting of anchor diagonals with respect to B, then whenever_ ( _R_ 1 _[′][, R]_ 2 _[′]_[)] _[is][a][type][(I)] pair of anchor rectangles, the half-diagonals in R_ 1 _[′][and][R]_ 2 _[′][are][disjoint.]_ 

_Proof._ We will argue for each sub type (I-1)-(I-4) one-by-one, using a similar strategy in each case. 

**Type (I-1).** For each type (I-1) pair ( _R_ 1 _[′][, R]_ 2 _[′]_[),][we][let] _[Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[) =] _[ R]_[(] _[h][R]_ 1 _[′][, h][R]_ 2 _[′]_[)][be][the] subrectangle of _R_ 2 _[′]_[spanned][by][the][hooks] _[h][R]_ 1 _[′]_[and] _[h][R]_ 2 _[′]_[.][Note][that][if] _[B]_[contains][a][point] in _Q_ ( _R_ 1 _[′][, R]_ 2 _[′]_[), then the half-diagonals in] _[ R]_ 1 _[′]_[and] _[ R]_ 2 _[′]_[will be disjoint.][See][ Figure 22][.][Thus] if we can argue that for every fixed _R_ 2 _[′]_[,][the][intersection] _[Q]_[(] _[R]_ 2 _[′]_[) =][ �] _R_ 1 _[′][Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][taken] over all _R_ 1 _[′]_[for][which][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][is][a][type][(I-1)][pair][is][a][(nonempty)][rectangle,][then][we] can be done by simply picking _B_ 0 to consist of one periodic point lying in _Q_ ( _R_ 2 _[′]_[)][for] one representative _R_ 2 _[′]_[in][each] _[π]_[1] _[M]_[-orbit,][then][taking][the] _[π]_[1] _[M]_[-translates.] 

40 

**==> picture [90 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
CHI CHEUK TSANG<br>**----- End of picture text -----**<br>


**==> picture [256 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
I-1 I-2 I-3 I-4<br>**----- End of picture text -----**<br>


**==> picture [44 x 59] intentionally omitted <==**

**==> picture [51 x 59] intentionally omitted <==**

**==> picture [41 x 64] intentionally omitted <==**

Figure 22. Lemma 6.15 holds if we place buoys in the shaded rectangles. 

To argue that _Q_ ( _R_ 2 _[′]_[)][is][a][rectangle,][we][analyze][which] _[R]_ 1 _[′]_[can][come][up.][If][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][is][a] type (I-1) pair, then the anchor _αR_ 1 must lie in the edge rectangle _R_ 2, but not on an unstable leaf that passes through _R_ 2 _[′]_[.][Since][the][anchors][are][periodic,][there][are][only] finitely many anchors in _R_ 2. Meanwhile, for each such anchor _α_ , there are only finitely many _⟨_ [ _α_ ] _⟩_ -orbits of edge rectangles that can have _α_ as its anchor. Hence the collection of rectangles _R_ 1 _[′]_[that][can][come][up][for][a][fixed] _[R]_ 2 _[′]_[lies][within][a][collection][of][the][form] _{_ [ _αi_ ] _[k] · Si,j | i_ = 1 _, ..., p, j_ = 1 _, ..., Ji, k ∈_ Z _}_ , where _αi_ are the anchors that lie in _R_ 2 but not in _R_ 2 _[′]_[.] 

In fact, we can further restrict to a collection of the form _{_ [ _αi_ ] _[k] · Si,j | i_ = 1 _, ..., p, j_ = 1 _, ..., Ji, k_ = _−Ki,j, ..., Ki,j}_ , since for each _i, j_ , [ _αi_ ] _[k] · Si,j_ becomes thinner than _R_ 2 for large _k_ , and is disjoint from _R_ 2 _[′]_[for][large] _[−][k]_[.][In][other][words,] _[Q]_[(] _[R]_ 2 _[′]_[)][is][only][a][finite] intersection of rectangles _Q_ ( _R_ 1 _[′][, R]_ 2 _[′]_[).][Since][each] _[Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][contains][the][hook] _[h][R]_ 2 _[′]_[,][a] finite intersection of them is nonempty, thus a rectangle. 

**Type (I-2).** For each type (I-2) pair ( _R_ 1 _[′][, R]_ 2 _[′]_[),][we][let] _[Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[) =] _[ R]_[(] _[h][R]_ 1 _[′][, h][R]_ 2 _[′]_[).][As][in] the type (I-1) case, if _B_ contains a point in _Q_ ( _R_ 1 _[′][, R]_ 2 _[′]_[),][then][the][half-diagonals][in] _[R]_ 1 _[′]_ and _R_ 2 _[′]_[will][be][disjoint.][See][Figure][22][.][Thus][it][suffices][to][argue][that][every][fixed] _[R]_ 2 _[′]_[,] the intersection _Q_ ( _R_ 2 _[′]_[) =][ �] _R_ 1 _[′][Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][taken][over][all] _[R]_ 1 _[′]_[for][which][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][is][a][type] (I-2) pair is a rectangle. 

As in the type (I-1) case, we analyze which _R_ 1 _[′]_[can][come][up.][If][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][is][a][type][(I-2)] pair, then the anchor _αR_ 1 must lie in _R_ 2 _[′]_[.][Since][the][anchors][are][periodic,][there][are][only] finitely many anchors in _R_ 2 _[′]_[.][Meanwhile,][for][each][such][anchor] _[α]_[,][there][are][only][finitely] many _⟨_ [ _α_ ] _⟩_ -orbits of edge rectangles that can have _α_ as its anchor. Hence the collection of rectangles _R_ 1 _[′]_[that][can][come][up][for][a][fixed] _[R]_ 2 _[′]_[lies][within][a][collection][of][the][form] _{_ [ _αi_ ] _[k] · Si,j | i_ = 1 _, ..., p, j_ = 1 _, ..., Ji, k ∈_ Z _}_ , where _αi_ are the anchors that lie in _R_ 2 _[′]_[.] 

In fact, we can further restrict to a collection of the form _{_ [ _αi_ ] _[k] · Si,j | i_ = 1 _, ..., p, j_ = 1 _, ..., Ji, k ≤ Ki,j}_ , since for each _i, j_ , [ _αi_ ] _[k] · Si,j_ becomes thinner than _R_ 2 _[′]_[for][large] _k_ . Note that _unlike_ the type (I-1) case, this collection is infinite. Nevertheless, since [ _αi_ ] _[k] · Si,j_ becomes shorter as _k →−∞_ , the intersection _Q_ ( _R_ 2 _[′]_[) =][ �] _R_ 1 _[′][Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][is][still] a rectangle. 

**Type (I-3).** This case is very similar to the type (I-2) case, but with the roles of _R_ 1 _[′]_ and _R_ 2 _[′]_[exchanged.][For][each][type][(I-3)][pair][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[),][we][let] _[Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[) =] _[ R]_[(] _[h][R]_ 1 _[′][, l][R]_ 2 _[′]_[),] where _lR_ 2 _[′]_[is][the][remaining][fourth][corner][of] _[R]_ 2 _[′]_[.][If] _[B]_[contains][a][point][in] _[Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[),][then] the half-diagonals in _R_ 1 _[′]_[and] _[R]_ 2 _[′]_[will][be][disjoint.][See][Figure][22][.][Thus][it][suffices][to] 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

41 

argue that every fixed _R_ 1 _[′]_[,][the][intersection] _[Q]_[(] _[R]_ 1 _[′]_[) =][ �] _R_ 2 _[′][Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][taken][over][all] _[R]_ 2 _[′]_ for which ( _R_ 1 _[′][, R]_ 2 _[′]_[)][is][a][type][(I-3)][pair][is][a][rectangle] 

A similar argument as in the type (I-2) case shows that the collection of _R_ 2 _[′]_[that][can] come up for a fixed _R_ 1 _[′]_[lies][within][a][collection][of][the][form] _[{]_[[] _[α][i]_[]] _[k][ ·][ S][i,j][|][ i]_[ = 1] _[, ..., p, j]_[=] 1 _, ..., Ji, k ≥−Ki,j}_ . From this, we see that _Q_ ( _R_ 1 _[′]_[)][is][a][rectangle.] 

**Type (I-4).** This case is a bit more interesting. For each type (I-4) pair ( _R_ 1 _[′][, R]_ 2 _[′]_[),][we] choose a stable leaf _ℓ_ passing through the interior of _R_ 1 _[′][∩][R]_ 2 _[′]_[.][We][let] _[Q]_[1][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][be] the subrectangle of _R_ 1 consisting of points lying in the same component of _R_ 1 _\ℓ_ as _αR_ 1 _[′]_[,][but][lying][outside][of] _[R]_[2][.][Symmetrically,][we][let] _[Q]_[2][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][be][the][subrectangle][of] _R_ 2 consisting of points lying in the same component of _R_ 2 _\ℓ_ as _αR_ 2 _[′]_[,][but][lying][outside] of _R_ 1. Then if _B_ contains a point in _Q_ 1( _R_ 1 _[′][, R]_ 2 _[′]_[)][and][a][point][in] _[Q]_[2][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[),][then][the] half-diagonals in _R_ 1 _[′]_[and] _[R]_ 2 _[′]_[will][be][disjoint.][See][Figure][22][.][Thus][we][have][to][argue] that the intersections _Q_ 1( _R_ 1 _[′]_[)][=][�] _R_ 2 _[′][Q]_[1][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][and] _[Q]_[2][(] _[R]_ 2 _[′]_[)][=][�] _R_ 1 _[′][Q]_[2][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][are] rectangles. 

A priori this could be tricky without choosing _ℓ_ more carefully. Fortunately, each intersection, say the one for _Q_ 1( _R_ 1 _[′]_[),][is][taken][over][a][finite][collection] _[{]_[[] _[α][i]_[]] _[k][ ·][ S][i,j][|][ i]_[ =] 1 _, ..., p, j_ = 1 _, ..., Ji, k_ = _−Ki,j, ..., Ki,j}_ , where _αi_ are the anchors in _R_ 1 _[′]_[,][since][for][each] _i, j_ , [ _αi_ ] _[k] · Si,j_ is thinner than _R_ 1 _[′]_[for][large] _[k]_[,][and][is][shorter][than] _[R]_ 1 _[′]_[for][large] _[−][k]_[.][Thus] _Q_ 1( _R_ 1 _[′]_[)][are] _[Q]_[2][(] _[R]_ 2 _[′]_[)][are][indeed][rectangles.] □ 

6.5. **Tightening remaining half-diagonals.** We turn to the type (II) pairs. The analysis in this case is simple once we prove the following lemma. 

**Lemma 6.16.** _Let B be a discrete collection of points in O. Let P and Q be two rectangles in O, with Q > P , and which do not share a corner. Let p be a tight arc between two opposite corner in P with respect to B ∩_ int( _P_ ) _, and q be a tight arc between two opposite corner in Q with respect to B ∩_ int( _Q_ ) _. Suppose that the interiors of p and q lie in O[◦] ._ 

_Suppose p and q are of the same color. Then p and q overlap along a (possibly degenerate) connected subarc r, and are disjoint away from r. Moreover, we have |_ slope _r_ ( _p_ ) _| < |_ slope _r_ ( _q_ ) _|._ 

_Proof._ If the unstable side of _P_ containing the hook of _p_ lies closer to the unstable side of _Q_ containing the hook of _q_ than the other unstable side of _P_ , then the same argument as in Lemma 6.13 works, since we can still consider the slit rectangle ( _P ∩ Q_ )[!] . So in the following we restrict to the remaining case when the unstable side of _P_ containing the hook of _p_ lies further from the unstable side of _Q_ containing the hook of _q_ than the other unstable side of _P_ . For ease of reference, we position the rectangles so that the hook of _p_ is the top-left corner of _P_ and the hook of _q_ is the bottom-right corner of _Q_ . See Lemma 6.16 left. 

We first claim that there cannot exist subarcs _p[′] ⊂ p_ and _q[′] ⊂ q_ which cobound a disc, with _q[′]_ lying above _p[′]_ . Suppose otherwise, then let _R_ be the rectangle with corners at 

42 CHI CHEUK TSANG 

**==> picture [254 x 77] intentionally omitted <==**

**----- Start of picture text -----**<br>
q<br>q<br>p [′] p<br>p<br>r q [′′] q [′]<br>P<br>p [′′]<br>Q<br>**----- End of picture text -----**<br>


Figure 23. Left: The setting of Lemma 6.16. Middle: By convexity, _p_ cannot osculate _q_ from above. Right: There cannot exists subarcs _p[′] ⊂ p_ and _q[′] ⊂ q_ that cobound a disc. 

the common endpoints of _p[′]_ and _q[′]_ . Since all points of _∂S ∩ R_ have to lie below _p[′]_ and above _q[′]_ , we can consider the set _R_[!] _⊂O[◦]_ obtained by slitting the points of _∂S ∩ R_ lying below _p[′]_ downwards, and slitting the points lying above _q[′]_ upwards. Choose a chart of _R_[!] into R[2] , both _p[′]_ and _q[′]_ have to be geodesics, hence they cannot bound a disc, contradiction. 

Next, suppose _p_ and _q_ overlap along a subarc _r_ . Since _P_ and _Q_ do not share a corner, _r_ does not contain an endpoint of _p_ or _q_ , so we can write _p_ as a concatenation _p_ 1 _∗v_ 1 _r ∗v_ 2 _p_ 2 and _q_ as a concatenation _q_ 1 _∗v_ 1 _r ∗v_ 2 _q_ 2 near _r_ . Let us first suppose that _r_ is degenerate, then since _p_ and _q_ are convex, we have slope _r_ ( _p_ 1) _≥_ slope _r_ ( _p_ 2) and slope _r_ ( _q_ 1) _≤_ slope _r_ ( _q_ 2). In particular, we cannot have both slope _r_ ( _p_ 1) _<_ slope _r_ ( _q_ 1) and slope _r_ ( _p_ 2) _>_ slope _r_ ( _q_ 2). That is, _p_ cannot osculate _q_ from above at _r_ . 

The same conclusion holds when _r_ is nondegenerate, for we have slope _v_ 1( _p_ 1) _≥_ slope _v_ 1( _r_ ) and slope _v_ 2( _r_ ) _≥_ slope _v_ 2( _p_ 2), and slope _v_ 1( _q_ 1) _≤_ slope _v_ 1( _r_ ) and slope _v_ 2( _r_ ) _≤_ slope _v_ 2( _q_ 2) by convexity of _p_ and _q_ . See Figure 23 middle. 

Using this observation, we claim that there cannot exist subarcs _p[′] ⊂ p_ and _q[′] ⊂ q_ which cobound a disc, with _q[′]_ lying below _p[′]_ as well. Suppose otherwise, then _p_ and _q_ must cross each other at the two endpoints of _p[′]_ and _q[′]_ , possibly after overlapping along some segment. But since _P < Q_ , we must see subarcs _p[′′] ⊂ p_ and _q[′′] ⊂ q_ cobounding a disc elsewhere, with _q[′′]_ lying above _p[′′]_ . See Figure 23 right. This contradicts what we have proven above. 

Thus we conclude that _p_ and _q_ overlap in a (possibly degenerate) connected subarc _r_ . The same argument as in Lemma 6.13 shows that we have _|_ slope _r_ ( _p_ ) _| < |_ slope _r_ ( _q_ ) _|_ . □ 

**Lemma 6.17.** _There exists a discrete π_ 1 _M -invariant collection of points B_ 0 _such that for every discrete π_ 1 _M -collection of points B ⊃B_ 0 _, if {dR} is the diagonal system consisting of anchor diagonals with respect to B, then whenever_ ( _R_ 1 _[′][, R]_ 2 _[′]_[)] _[is][a][type][(II)] pair of anchor rectangles, the anchor half-diagonals in R_ 1 _[′][and][R]_ 2 _[′][overlap][along][a] (possibly degenerate) subarc r containing s_ 1 = _s_ 2 _, with |_ slope _r_ ( _dR_ 1) _| < |_ slope _r_ ( _dR_ 2) _|._ 

_Proof._ We will argue for each sub type (II-1)-(II-4) as in Lemma 6.15. 

43 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

**==> picture [312 x 71] intentionally omitted <==**

**----- Start of picture text -----**<br>
II-1 II-2 II-3 II-4<br>**----- End of picture text -----**<br>


Figure 24. Lemma 6.17 holds if we place buoys in the shaded rectangles. 

**Type (II-1).** For each type (II-1) pair ( _R_ 1 _[′][, R]_ 2 _[′]_[),][we][let] _[Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][=] _[R]_[(] _[h][R]_ 1 _[′][, α][R]_ 2 _[′]_[)][be] the subrectangle of _R_ 2 _[′]_[spanned][by][the][hook] _[h][R]_ 1 _[′]_[and][the][anchor] _[α][R]_ 2 _[′]_[.][If] _[B]_[contains][a] point _b_ in _Q_ ( _R_ 1 _[′][, R]_ 2 _[′]_[),][then][we][can][apply][Lemma][6.16][to][the][rectangles] _[R]_[(] _[s]_[1] _[, b]_[)] _[ < R]_ 2 _[′]_ in order to conclude. See Figure 24. Thus it suffices to argue that for every fixed _R_ 1 _[′]_[,] the intersection _Q_ ( _R_ 1 _[′]_[) =][ �] _R_ 2 _[′][Q]_[(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][taken][over][all] _[R]_ 2 _[′]_[for][which][(] _[R]_ 1 _[′][, R]_ 2 _[′]_[)][is][a][type] (II-1) pair is a rectangle. 

But the set of such _R_ 2 _[′]_[is contained in a collection of the form] _[ {]_[[] _[α][i]_[]] _[k][·][S][i,j][|][ i]_[ = 1] _[, ..., p, j]_[=] 1 _, ..., Ji, k ≥−Ki,j}_ , where _αi_ are the anchors in _R_ 1 _[′]_[,][since][for][each] _[i, j]_[,][[] _[α][i]_[]] _[k][·][ S][i,j]_[is] shorter than _R_ 2 _[′]_[for][large] _[−][k]_[.][From][this,][we][deduce][that] _[Q]_[(] _[R]_ 1 _[′]_[)][is][a][rectangle.] 

**Type (II-2).** This case is similar to the type (II-1) case, but with the roles of _R_ 1 _[′]_[and] _R_ 2 _[′]_[interchanged.][We][omit][the][details.] 

**Type (II-3) and (II-4).** If ( _R_ 1 _[′][, R]_ 2 _[′]_[)][is][of][type][(II-3)][or][(II-4),][then] _[R]_ 2 _[′][< R]_ 1 _[′]_[and][we] can directly apply Lemma 6.16. Note that in these cases we do not have to specify a collection _B_ 0. □ 

## 6.6. **Putting the diagonals back together.** 

_Proof of Proposition 6.1._ Let _B_ be the union of the discrete _π_ 1 _M_ -invariant collections of points in Lemma 6.11, Lemma 6.15, and Lemma 6.17. Let _{dR}_ be the diagonal system consisting of anchor diagonals with respect to _B_ . Then (1) is true by construction. 

Next, we show (2). Suppose _R_ 1 _< R_ 2 are two edge rectangles of the same color. If _R_ 1 and _R_ 2 share a corner _s_ , then the pair of anchor subrectangles _R_ 1 _[′][⊂][R]_[1][and] _[R]_ 2 _[′][⊂][R]_[2] that contain _s_ intersect and is of type (0). Aside from this pair, the only other pair of anchor subrectangles that could possibly intersect are the other anchor subrectangles _R_ 1 _[′′][⊂][R]_[1][and] _[R]_ 2 _[′′][⊂][R]_[2][,][and][they][would][be][of][type][(I-1).][Thus][in][this][case][(2)][follows] from Lemma 6.14 and Lemma 6.15. 

If _R_ 1 and _R_ 2 share an anchor, then two pairs of anchor subrectangles intersect and both are of type (0). Thus in this case (2) follows from Lemma 6.14. 

In the remaining cases, the pairs of anchor subrectangles can only be of types (I) or (II). In fact, exactly one pair will be of type (II), since the union of the two hooked arcs (defined in Definition 6.12) in the two anchor subrectangles of _Ri_ , for _i_ = 1 _,_ 2, intersect exactly once. Thus in this case (2) follows from Lemma 6.15 and Lemma 6.17. 

44 

## CHI CHEUK TSANG 

Finally, we address (3) and (4). Since the half-diagonals are tight paths with respect to _B_ , by definition their nodes are exactly the point that lie on _B_ . Thus (3) holds. Suppose there is a segment _σ_ whose endpoints are nodes that lie in the same _π_ 1 _M_ -orbit. We can add a node at any point in the interior of _σ_ . Since the _π_ 1 _M_ -orbits of the existing nodes is a countable set, while _σ_ consists of uncountably many points, we can choose the new node so that _σ_ is split into two segments, each satisfying (4). 

A priori one has to worry about the new node violating (3). This only happens if the new node is chosen to be a point lying on a segment _σ[′]_ intersecting _σ_ transversely. But since there are only countably many segments in total, there are only countably many choices of the new node that can result in this, so this situation can be avoided as well. □ 

## 7. Perturbing the diagonals 

In this section, we explain how the diagonal systems of Proposition 6.1 can be perturbed to satisfy the slope criterion. 

7.1. **Perturbing for transversality.** We refer to a diagonal system _{dR}_ satisfying Proposition 6.1(1)-(4) as a **PLO (Piecewise Linear Overlapping) diagonal system** . Observe that Proposition 6.1(3) allows us to talk about segments of the diagonal system unambiguously. 

**Definition 7.1** (Overlap) **.** Suppose _σ_ is a nondegenerate segment in the intersection of two diagonals _dR_ 1 and _dR_ 2. Then the rectangles _R_ 1 and _R_ 2 are of the same color and they intersect. Up to swapping _R_ 1 and _R_ 2, we can assume that _R_ 1 _< R_ 2. We say that the triple ( _dR_ 1 _, dR_ 2 _, σ_ ) is an **overlap** of _dR_ 2 over _dR_ 1 along _σ_ . ♢ 

**Lemma 7.2.** _For any PLO diagonal system, the set of π_ 1 _M -orbits of overlaps is finite._ 

_Proof._ Lift the diagonals _{dR}_ to the translation orbit space _O[◦]_ . Here we can talk about the exact values of slopes. Since there are only finitely many _π_ 1 _M_ -orbits of edge rectangles, thus diagonals in _O_ , so there are only finitely many _π_ 1 _M[◦]_ -orbits of diagonals in _O[◦]_ . Let _d_[�] 1 _, ..., d_[�] _r_ be a collection of one representative in each _π_ 1 _M[◦]_ -orbit. To show the lemma, it suffices to show that for each _i_ = 1 _, ..., r_ , there are only finitely many diagonals that can form an overlap with _d_[�] _i_ . 

To this end, pick a large _N_ so that _λ_[2] _[N] >_[max] min _[i] i_ min[max] _|[|]_ slope([ slo][p][e][(] _d[d] i[i]_ )[)] _|[|]_[,][where] _[λ]_[is][the][dilatation][of] the pseudo-Anosov first return map _f_ , and max _|_ slope( _di_ ) _|_ and min _|_ slope( _di_ ) _|_ denotes the maximum and minimum, respectively, over _|_ slope( _σ_ ) _|_ where _σ_ is a segment of _di_ . Then for every overlap ( _d_[�] _i, g · d_[�] _j, σ_ ), we must have _|_ height( _g_ ) _| ≤ N_ . Meanwhile, by Lemma 5.7, the collection _π_ 1( _M[◦]_ )[ _−N,N_ ] _· d_[�] _j_ =[�] _[N] h_ = _−N[π]_[1][(] _[M][ ◦]_[)] _[h][ ·][d]_[�] _[j]_[is][locally][finite,][so] only finitely many diagonals can form an overlap with _d_[�] _i_ . □ 

The content of this subsection is to show that one can inductively reduce the number of _π_ 1 _M_ -orbits of pairs ( _R_ 1 _, R_ 2) where there is an overlap of _dR_ 2 over _dR_ 1. Once this is 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

45 

**==> picture [77 x 86] intentionally omitted <==**

**----- Start of picture text -----**<br>
dR 2 dQ 1<br>σ [′]<br>σ<br>dR 2 [′]<br>**----- End of picture text -----**<br>


Figure 25. If _σ, σ[′] ∈_ Σ are adjacent segments on _dQ_ 1, then there is an overlap ( _dQ_ 1 _, dR_ 2 _, σ_ ) if and only if there is an overlap ( _dQ_ 1 _, dR_ 2 _, σ[′]_ ) for the same _R_ 2. 

arranged, we have a diagonal system consisting of piecewise linear arcs that intersect in points. 

**Definition 7.3** (Peripheral, elementary overlap) **.** We say that an overlap ( _dR_ 1 _, dR_ 2 _, σ_ ) is 

- **peripheral** if _σ_ contains an endpoint of the intersection _dR_ 1 _∩ dR_ 2 that is not a point of _C_[�] , and 

- **elementary** if there does not exist overlaps ( _dR_ 1 _, dR_ 3 _, σ_ ) and ( _dR_ 3 _, dR_ 2 _, σ_ ). 

The following observation underlies the terminology of ‘elementary’: If ( _dR_ 1 _, dR_ 3 _, σ_ ) and ( _dR_ 3 _, dR_ 2 _, σ_ ) are overlaps, then ( _dR_ 1 _, dR_ 2 _, σ_ ) is an overlap. Thus elementary overlaps are the ones that cannot be ‘decomposed’ in this way. ♢ 

**Lemma 7.4.** _If there exists an overlap, then there exists a peripheral elementary overlap._ 

_Proof._ Suppose we are given an overlap ( _dR_ 1 _, dR_ 2 _, σ_ ). We write _dQ_ 1 = _dR_ 1 and keep this diagonal fixed. Consider the collection Σ = _{σ |_ there exists an overlap ( _dQ_ 1 _, dR_ 2 _, σ_ ) _}_ . We claim that[�] _σ∈_ Σ _[σ]_[cannot][be][the][entire] _[d][Q]_ 1[.] 

To see this, observe that if _σ, σ[′] ∈_ Σ are adjacent segments on _dQ_ 1, then there is an overlap ( _dQ_ 1 _, dR_ 2 _, σ_ ) if and only if there is an overlap ( _dQ_ 1 _, dR_ 2 _, σ[′]_ ) for the same _R_ 2. Indeed, otherwise there will exist overlaps ( _dQ_ 1 _, dR_ 2 _, σ_ ) and ( _dQ_ 1 _, dR_ 2 _[′][, σ][′]_[) where] _[ R]_[2][=] _[ R]_ 2 _[′]_[.] But then _dR_ 2 and _dR_ 2 _[′]_[intersect][at][the][shared][node][of] _[σ]_[and] _[σ][′]_[,][where][it][fails][the][slope] inequality of Proposition 6.1(2). See Figure 25. 

Thus if[�] _σ∈_ Σ _[σ]_[=] _[ d][Q]_ 1[, then there would exist] _[ d][R]_ 2[overlapping over] _[ d][Q]_ 1[along all segments] of _dQ_ 1, which is impossible since _Q_ 1 _< R_ 2. 

Thus we can pick a element _ρ ∈_ Σ that is **outermost** , in the sense that _ρ_ contains an endpoint of the subarc[�] _σ∈_ Σ _[σ]_[that][is][not][a][point][of] _[C]_[�][.][This][property][implies][that][any] overlap ( _dQ_ 1 _, dR_ 2 _, ρ_ ) is automatically peripheral. 

We now fix _ρ_ and consider the collection _R_ = _{dR_ 2 _|_ there exists an overlap ( _dQ_ 1 _, dR_ 2 _, ρ_ ) _}_ . Pick some _dR_ 2 _[′][∈R]_[.] If ( _dQ_ 1 _, dR_ 2 _[′][, ρ]_[)][is][non-elementary,][then][there][exists][overlaps] 

CHI CHEUK TSANG 

46 

( _dQ_ 1 _, dR_ 2 _[′′][, ρ]_[) and (] _[d][R]_ 2 _[′′][, d][R]_ 2 _[′][, ρ]_[).][Here, (] _[d][R]_ 2 _[′′][, d][R]_ 2 _[′][, ρ]_[) being an overlap implies that] _[ R]_ 2 _[′′][< R]_ 2 _[′]_[.] If ( _dQ_ 1 _, dR_ 2 _[′′][, ρ]_[)][is][non-elementary,][then][we][repeat][the][argument,][and][so][on.] By Lemma 7.2, _R_ is finite, so the process stops eventually and we end up with a peripheral elementary overlap ( _dQ_ 1 _, dQ_ 2 _, ρ_ ). □ 

Suppose we are given a peripheral elementary overlap ( _dQ_ 1 _, dQ_ 2 _, ρ_ ). We will explain how to modify the PLO diagonal system so that there are no longer any overlaps of _dQ_ 2 over _dQ_ 1, while not creating any new pairs of rectangles that overlap. To this end, we introduce the following definition. 

**Definition 7.5** (Bookkeeping nodes) **.** A set of **bookkeeping nodes** for ( _Q_ 1 _, Q_ 2) is a subset _V_ of the set of nodes of the diagonal system _{dR}_ that contain the endpoints and turns of _r_ = _dQ_ 1 _∩ dQ_ 2, such that adjacent elements of _V_ on _dQ_ 1 or _dQ_ 2 lie in different _π_ 1 _M_ -orbits. In particular, _V_ cuts _dQ_ 1 and _dQ_ 2 into linear subarcs, which we refer to as the **bookkeeping segments** . 

We emphasize that we allow nodes of the diagonal system inbetween bookkeeping nodes, thus bookkeeping segments are unions of segments in general. ♢ 

A set of bookkeeping nodes always exist: One can simply choose the _π_ 1 _M_ -orbits of all nodes on _r_ . Our modification of the PLO diagonal system will be broken into smaller steps, each retaining the property that we have a PLO diagonal system, but reducing the number of bookkeeping nodes on _dQ_ 1 _∩ dQ_ 2. Once _dQ_ 1 _∩ dQ_ 2 only has one bookkeeping node, there will no longer be any overlap of _dQ_ 2 over _dQ_ 1. 

For the rest of this subsection, we fix a peripheral elementary overlap ( _dQ_ 1 _, dQ_ 2 _, ρ_ ) and fix a set of bookkeeping nodes _V_ . Without loss of generality we suppose that _dQ_ 1 and _dQ_ 2 are red. Throughout, we will work in the translation orbit space _O_[�] _[◦]_ . 

As noted in the proof of Lemma 7.2, there are only finitely many _π_ 1 _M[◦]_ -orbits of diagonals in _O_[�] _[◦]_ . Let _d_[�] 1 _, ..., d_[�] _r_ be a collection of one representative in each _π_ 1 _M[◦]_ -orbit. Pick a large _N_ so that 

**==> picture [294 x 29] intentionally omitted <==**

Since the overlap is peripheral, _ρ_ contains an endpoint _u_ of _dQ_ 1 _∩ dQ_ 2. Since at least one of _dQ_ 1 and _dQ_ 2 is non-smooth at _u_ , _ρ_ is contained in a bookkeeping segment _σ_ that has _u_ as an endpoint. Let _v_ be the other endpoint of _σ_ . We write _dQ_ 1 as _σ ∗u σQ[′]_ 1[and] _[d][Q]_ 2 as _σ ∗u σQ[′]_ 2[near] _[u]_[.][Since] _[u]_[is][an][endpoint][of] _[d][Q]_ 1 _[∩][d][Q]_ 2[,][we][have][slope][(] _[σ] Q[′]_ 2[)] _[ >]_[ slope][(] _[σ]_[)] or slope( _σQ[′]_ 1[)] _[<]_[slope][(] _[σ]_[).][Without][loss][of][generality][suppose][the][former][is][true.][See] Figure 26 an illustration of our setup. 

Let _D_ + = _{dR | Q_ 2 _≤ R_ and _dQ_ 2 _∩ dR_ contains a subarc _σR ⊂ σ_ containing _v}_ . For every _dR ∈D_ +, we modify _dR_ as follows: Consider the linear arc _σR_[+][with][slope] slope( _σ_ ) + _ε_ starting at _v_ and ending at a point _bR_ on the segment _σR[′]_[of] _[d][R]_[after] _[σ][R]_[.] 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

47 

**==> picture [89 x 57] intentionally omitted <==**

**----- Start of picture text -----**<br>
dQ 2<br>dQ 1<br>u<br>v<br>σ<br>**----- End of picture text -----**<br>


Figure 26. The setup for modifying a PLO diagonal system. 

**==> picture [210 x 55] intentionally omitted <==**

**----- Start of picture text -----**<br>
dR dQ 2 dR dQ 2<br>σ [′]<br>σR [′] Q 2 dQ 1 dQ 1<br>σR σR [+]<br>σQ 2 =  σ σQ [+] 2<br>**----- End of picture text -----**<br>


Figure 27. Modifying a PLO diagonal system to reduce the number of bookkeeping nodes on _dQ_ 1 _∩ dQ_ 2. 

We delete from _dR_ the union of _σR_ and the subarc of _σR[′]_[from] _[u]_[to] _[b][R]_[,][then][add][back] in _σ_[+][See][Figure][27][.] _R_[.] 

We extend the modification equivariantly to the _π_ 1 _M_ -orbit of _dR_ . Here the condition on consecutive elements in Definition 7.5 plays a role in ensuring that no two consecutive bookkeeping segments on a diagonal are to be modified, so that the procedure is well-defined. 

We verify that the modified diagonal system is still PLO: Each diagonal is still piecewise linear, and with _ε_ small enough, they stay within _O[◦]_ , so Proposition 6.1(1) is clear. 

Upon adding _bR_ as the new nodes after modification, Proposition 6.1(3) is violated only if some new segment _σR_[+][passes][through][some][node,][but][such][a][scenario][can] only occur for countably many values of _ε_ . Similarly, Proposition 6.1(4) is violated after modification only if a new node _bR_ happens to lie in the orbit of a pre-existing node, but this only happens for countably many values of _ε_ . The conclusion is that Proposition 6.1(3) and (4) hold after modification for generic choices of _ε_ . We remark that the fact that we have to add new nodes _bR_ is the reason we have introduced the technical Definition 7.5, since we wish to keep track of our progress in the metric of nodes _prior_ to the modification. 

Thus it remains to show Proposition 6.1(2). Suppose that _R_ 1 _< R_ 2 have the same color. Lift _dR_ 1 and _dR_ 2 to _d_[�] _R_ 1 and _d_[�] _R_ 2 in _O_[�] _[◦]_ . Up to translation, we can suppose that _d_[�] _R_ 1 is one of the representatives we chose for Equation (7.1). We can then write _d_[�] _R_ 2 = _g · dj_ for some _g ∈ π_ 1( _M[◦]_ ). Notice that Equation (7.1) is preserved if we pick _ε_ small enough. This implies that we must have height( _g_ ) _≥−N_ , and Proposition 6.1(2) holds with _r_ degenerate whenever if height( _g_ ) _≥ N_ . The upshot is that by Lemma 5.7, we only have to check Proposition 6.1(2) for finitely many possibilities of _R_ 2. 

48 CHI CHEUK TSANG 

**==> picture [189 x 26] intentionally omitted <==**

**----- Start of picture text -----**<br>
dR 1 [d] Q 2 dR 1 [d] Q 2<br>dR 2 dQ 1 dR 2 dQ 1<br>**----- End of picture text -----**<br>


Figure 28. Analysis for Proposition 6.1(2) if _dR_ 1 _, dR_ 2 _∈D_ +. 

**==> picture [184 x 25] intentionally omitted <==**

**----- Start of picture text -----**<br>
dR 2 dR 1 [d] Q 2 dR 2 dR 1 [d] Q 2<br>dQ 1 dQ 1<br>**----- End of picture text -----**<br>


Figure 29. Analysis for Proposition 6.1(2) if _dR_ 1 _∈D_ + but _dR_ 2 _̸∈D_ +. 

If neither _dR_ 1 nor _dR_ 2 has a translate that lies in _D_ +, then the modification does not involve _dR_ 1 and _dR_ 2 so Proposition 6.1(2) holds from before. 

Suppose _dR_ 1 has a translate that lies in _D_ +. Up to applying the translation, we arrange it so that _dR_ 1 _∈D_ +. If _dR_ 2 _∈D_ +, then after modification _dR_ 1 and _dR_ 2 overlap in the same number of segments and the slope inequality continues to hold. See Figure 28. 

If _dR_ 2 _̸∈D_ +, then depending on whether _dR_ 1 and _dR_ 2 overlapped along some segment of _σ_ , after modification _dR_ 1 and _dR_ 2 either overlap in the same number of segments, or one less segment, and the slope inequality continues to hold. See Figure 29. 

Now suppose _dR_ 1 does not have a translate that lies in _D_ +, but _dR_ 2 does. Up to applying the translation, we arrange it so that _dR_ 2 _∈D_ +. By the hypotheses that ( _dQ_ 1 _, dQ_ 2 _, ρ_ ) is elementary, _dR_ 1 cannot contain both _v_ and _σR[′]_ 2[Then][depending][on][whether] _[d][R]_ 1 contained a subarc of _σ_ , after modification _dR_ 1 and _dR_ 2 either overlap in the same number of segments, or one less segment, and the slope inequality continues to hold. See Figure 30. 

Finally, it is clear that the number of bookkeeping nodes on _dQ_ 1 _∩ dQ_ 2 has been reduced by one. 

Performing this construction inductively, we will eventually reduce the number of bookkeeping nodes _dQ_ 1 _∩ dQ_ 2 to one, at which point _dQ_ 1 and _dQ_ 2 no longer overlap. In turn, performing such a sequence of constructions inductively, we will eventually get rid of all overlaps. 

We summarize our progress so far in the following lemma. 

**Lemma 7.6.** _Under the hypothesis of Proposition 6.1, there exists a diagonal system {dR} such that:_ 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

49 

**==> picture [173 x 129] intentionally omitted <==**

**----- Start of picture text -----**<br>
dR 2 dQ 2 dR 2 [d] Q 2<br>dQ 1 dQ 1<br>dR 1 dR 1<br>dR 2 dQ 2 dR 1 dR 2 dQ 2 dR 1<br>dQ 1 dQ 1<br>**----- End of picture text -----**<br>


Figure 30. Analysis for Proposition 6.1(2) if _dR_ 2 _∈D_ + but _dR_ 1 _̸∈D_ +. By the elementary hypothesis, the bottom scenario cannot happen. 

- _(1) The interior of each dR is a piecewise linear arc in O[◦] , under the quasi-translation structure induced from S._ 

- _(2) The system {dR} satisfies the slope criterion for diagonals of the same color, i.e. for every R_ 1 _< R_ 2 _of the same color,_ 

   - _if R_ 1 _and R_ 2 _share a corner, then_ int( _dR_ 1) _and_ int( _dR_ 2) _are disjoint, and_ 

   - _if R_ 1 _and R_ 2 _do not share a corner, then_ int( _dR_ 1) _and_ int( _dR_ 2) _intersect at exactly one point v, with |_ slope _v_ ( _dR_ 1) _| < |_ slope _v_ ( _dR_ 2) _|._ 

7.2. **Perturbing for smoothness.** The goal of this subsection is to upgrade Lemma 7.6 from piecewise linear to smooth. 

**Lemma 7.7.** _Under the hypothesis of Proposition 6.1, there exists a diagonal system {dR} such that:_ 

- _(1) The interior of each dR is a smooth arc in O[◦] with constant slope near its endpoints, under the quasi-translation structure induced from S._ 

- _(2) The system {dR} satisfies the slope criterion for diagonals of the same color, i.e. for every R_ 1 _< R_ 2 _of the same color,_ 

   - _if R_ 1 _and R_ 2 _share a corner, then_ int( _dR_ 1) _and_ int( _dR_ 2) _are disjoint, and_ 

   - _if R_ 1 _and R_ 2 _do not share a corner, then_ int( _dR_ 1) _and_ int( _dR_ 2) _intersect at exactly one point v, with |_ slope _v_ ( _dR_ 1) _| < |_ slope _v_ ( _dR_ 2) _|._ 

_Proof._ Let _{dR}_ be a diagonal system as in Lemma 7.6. We lift everything to the translation orbit space _O_[�] _[◦]_ . As noted in the proof of Lemma 7.2, there are only finitely 

50 

## CHI CHEUK TSANG 

**==> picture [56 x 80] intentionally omitted <==**

**----- Start of picture text -----**<br>
νv 2<br>v 2<br>νv 1<br>v 1<br>**----- End of picture text -----**<br>


Figure 31. Perturbing the diagonals to be smooth. 

many _π_ 1 _M[◦]_ -orbits of diagonals in _O[◦]_ . Let _d_[�] 1 _, ..., d_[�] _r_ be a collection of one representative in each _π_ 1 _M[◦]_ -orbit. Pick a large _N_ so that Equation (7.1) holds. 

By Lemma 5.7, the set of _π_ 1( _M[◦]_ )[ _−N,N_ ]-orbits of _d_[�] _i_ is locally finite. Thus we can choose a rectangular neighborhood _νv_ of each non-smooth node _v_ of _d_[�] _i_ , such that 

- each _d_[�] _i ∩ νv_ can be written as _σ_ 1 _∗v σ_ 2 where _σ_ 1 and _σ_ 2 are linear and exit _νv_ through its vertical sides, 

- _νv_ is disjoint from _g · νw_ , for every _g ∈ π_ 1( _M[◦]_ )[ _−N,N_ ], unless _g · w_ = _v_ , and 

- _νv_ is disjoint from _g · d_[�] _j_ , for every _g ∈ π_ 1( _M[◦]_ )[ _−N,N_ ], _j_ = 1 _, ..., r_ , unless _g · d_[�] _j_ passes through _v_ . 

See Figure 31 left. 

We� now modify each _d_[�] _i_ as follows: For each non-smooth node _v_ of _d_[�] _i_ , we write _di ∩ νv_ = _σ_ 1 _∗v σ_ 2 as above. Choose a chart of _νv_ , identifying it with a rectangle [ _x_ 0 _, x_ 1] _×_ [ _y_ 0 _, y_ 1] _⊂_ R[2] . Without loss of generality suppose 0 _<_ slope( _σ_ 1) _<_ slope( _σ_ 2), so that we can write _d_[�] _i ∩ νv_ as a graph _y_ = _f_ ( _x_ ), where _f_ is a piecewise linear function that concaves upwards. We replace _d_[�] _i ∩ νv_ with a graph _y_ = _g_ ( _x_ ) instead, where _g_ is a smooth function that concaves upwards, and agreeing with _f_ near _x_ = _x_ 0 and _x_ = _x_ 1. See Figure 31 right. 

We then extend these modifications in a _π_ 1( _M[◦]_ )-equivariant way. 

We now check the items in the statement of the proposition. (1) is clear provided that the neighborhoods _νv_ are chosen to be small enough. 

Again, the bulk of the proof is checking (2). Since _g_ concaves upwards, max slope( _d_[�] _i_ ) and min slope( _d_[�] _i_ ) are unchanged by the modification. Thus Equation (7.1) is preserved. 

Suppose that _R_ 1 _< R_ 2 have the same color. Lift _dR_ 1 and _dR_ 2 to _d_[�] _R_ 1 and _d_[�] _R_ 2 in _O_[�] _[◦]_ . Up to translation, we can suppose that _d_[�] _R_ 1 is one of the representatives we chose for Equation (7.1). We can then write _d_[�] _R_ 2 = _g · dj_ for some _g ∈ π_ 1( _M[◦]_ ). Then as in Section 7.1, we can assume that _|_ height( _g_ ) _| ≤ N_ . 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

51 

Let _v_ be the point of intersection between _d_[�] _R_ 1 and _d_[�] _R_ 2 prior to the modification. If both _d_[�] _R_ 1 and _d_[�] _R_ 2 were smooth at _v_ , then by the choice of _νv_ , the modifications on _d_[�] _R_ 1 and _d_[�] _R_ 2 were done away from _v_ , so the slope inequality continues to hold. 

If _d_[�] _R_ 1 was smooth at _v_ but not _d_[�] _R_ 2, then by the choice of _νv_ , the modifications on _d_[�] _R_ 1 were done away from _νv_ , so that after modification, _d_[�] _R_ 1 and _d_[�] _R_ 2 is a straight line and a convex curve within _νv[∼]_ = [ _x_ 0 _, x_ 1] _×_ [ _y_ 0 _, y_ 1], with _d_[�] _R_ 1 lying above _d_[�] _R_ 2 near _x_ = _x_ 0 and the other way around near _x_ = _x_ 1. Thus they intersect once and satisfy the slope inequality. If both _d_[�] _R_ 1 and _d_[�] _R_ 2 were not smooth at _v_ , then _d_[�] _R_ 1 and _d_[�] _R_ 2 are convex curves within _νv[∼]_ = [ _x_ 0 _, x_ 1] _×_ [ _y_ 0 _, y_ 1], with _d_[�] _R_ 1 lying above _d_[�] _R_ 2 near _x_ = _x_ 0 and the other way around near _x_ = _x_ 1. Thus they intersect once and satisfy the slope inequality as well. □ 7.3. **Rotating to eliminate misalignments.** The goal of this subsection is to remove ‘of the same color’ in Lemma 7.7(2). This will finally give us a diagonal system satisfying the slope criterion. 

Let _{dR}_ be a diagonal system as in Lemma 7.7. As noted in the proof of Lemma 7.2, there are only finitely many _π_ 1 _M[◦]_ -orbits of diagonals in _O[◦]_ . Let _d_[�] 1 _, ..., d_[�] _r_ be a collection of one representative in each _π_ 1 _M[◦]_ -orbit. Pick a large _N_ so that Equation (7.1) holds. 

**Definition 7.8** (Misalignment) **.** Suppose _R_ 1 _< R_ 2 are of different colors. Then the diagonals _dR_ 1 and _dR_ 2 must intersect at a single point _v_ . Suppose _|_ slope _v_ ( _dR_ 1) _| ≥ |_ slope _v_ ( _dR_ 2) _|_ . If _R_ 1 is red while _R_ 2 is blue, then we say that ( _dR_ 1 _, dR_ 2 _, v_ ) is a **upward misalignment** . If _R_ 1 is blue while _R_ 2 is red, then we say that ( _dR_ 1 _, dR_ 2 _, v_ ) is a **downward misalignment** . In both cases, we say that _v_ is the **projection** of the misalignment. ♢ 

It is helpful to have a 3-dimensional mental picture of a misalignment: Let _{d[∧] R[}]_[be][the] collection of canonical lifts of _{dR}_ . Let _v_ 1 _∈ d[∧] R_ 1[and] _[v]_[2] _[∈][d][∧] R_ 2[be][the][points][projecting] down to _v_ . Then there is an orbit segment of _ϕ_[�] from _v_ 2 to _v_ 1. One should think of this orbit segment as the misalignment. Furthermore, if we orient the orbit segment to go from the blue canonical lift to the red canonical lift, then the orbit segment is oriented upwards/downwards if the misalignment is upwards/downwards respectively. 

## **Lemma 7.9.** _There are only finitely many π_ 1 _M -orbits of misalignments._ 

_Proof._ Suppose we have a misalignment between _dR_ 1 and _dR_ 2. Up to translation, we can suppose that _d_[�] _R_ 1 is one of the representatives we chose for Equation (7.1). We can then write _d_[�] _R_ 2 = _g · dj_ for some _g ∈ π_ 1( _M[◦]_ ). Then as in Section 7.1, we have _|_ height( _g_ ) _| ≤ N_ , thus there are only finitely many possibilities for _R_ 2. □ 

52 

## CHI CHEUK TSANG 

Figure 32. Modifications in the proof of Proposition 7.10. 

We are now ready to modify our diagonals. 

**Proposition 7.10.** _Under the hypothesis of Proposition 6.1, there exists a diagonal system {dR} satisfying the slope criterion._ 

_Proof._ We first argue that up to a _C_[1] -small perturbation, we can assume that all misalignments have distinct projections: For each _i_ = 1 _, ..., r_ , we consider the set of points on _d_[�] _i_ that is the projection of a misalignment involving _d_[�] _i_ . By a _C_[1] -small perturbation of _d_[�] _i_ , we can make these points all disjoint. See Figure 32 top. Then up to a further perturbation, we can make these points all non-periodic and occupy distinct _π_ 1 _M[◦]_ -orbits. Once this is arranged, all misalignments have distinct projections. 

Note that this also implies that if ( _dR_ 1 _, dR_ 2 _, w_ ) is a misalignment, then there does not exist a third diagonal _dR_ 3 such that _|_ slope _w_ ( _dR_ 1) _| ≥|_ slope _w_ ( _dR_ 3) _| ≥|_ slope _w_ ( _dR_ 2) _|_ , for otherwise either ( _dR_ 1 _, dR_ 3 _, w_ ) or ( _dR_ 3 _, dR_ 2 _, w_ ) is a misalignment with the same projection. 

By doing the perturbation _C_[1] -small enough, we preserve Equation (7.1). Now let _ℓ_ 1 _, ..., ℓs_ be a collection of one representative in each _π_ 1 _M[◦]_ -orbit of misalignments, so that each _ℓj_ involves some _d_[�] _i_ , and let _w_ 1 _, ..., ws_ be their projections. 

By Lemma 5.7, the set of _π_ 1( _M[◦]_ )[ _−_ 3 _N,_ 3 _N_ ]-orbits of the points _wj_ , and the set of _π_ 1( _M[◦]_ )[ _−_ 3 _N,_ 3 _N_ ]-orbits of diagonals is locally finite. Thus we can choose neighborhoods _νwj_ of _wj_ so that 

- _νwj_ and _g · νwi_ are disjoint for every _g ∈ π_ 1( _M[◦]_ )[ _−_ 3 _N,_ 3 _N_ ] and _i, j_ = 1 _, ..., s_ , unless _g_ = 1 and _i_ = _j_ , and 

- _νwj_ and _g · d_[�] _i_ are disjoint for every _g ∈ π_ 1( _M[◦]_ )[ _−_ 3 _N,_ 3 _N_ ] and _i, j_ = 1 _, ..., s_ , unless _g · d_[�] _i_ passes through _wj_ . 

We now explain how to modify the diagonals within the neighborhoods _νwj_ . Without loss of generality suppose _wj_ is the projection of an upward misalignment ( _d_[�] 1 _, d_[�] _[′] , wj_ ). Then we modify _d_[�] 1 so that its slope at _wj_ is (1 _− ε_ ) slope _wi_ ( _d_[�] _[′]_ ), and such that its slope in _νwj_ stays within a factor of [ _−λ[−][N] , λ[N]_ ] of its original slope at _wj_ . See Figure 32 bottom. 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

53 

We then extend these modifications in a _π_ 1( _M[◦]_ )-equivariant way. 

By the choice of _νwj_ , these modifications eliminate the misalignments at _wj_ while not creating any new misalignments. Thus the slope criterion is satisfied. □ 

## 7.4. **Steady position.** Theorem 1.2 now quickly follows. 

_Proof of Theorem 1.2._ By Proposition 7.10, we have a diagonal system satisfying the slope criterion. Hence by Proposition 5.13, we can put ∆in Legendrian position. By Proposition 2.7, this implies that ∆can be put in steady position. □ 

## 8. Filling in the bicontact form 

In this section, we finish the proof of Theorem 1.1. The key construction is filling the bicontact form ( _α_ + _[S][, α] −[S]_[)][from][Equation][(5.1)][over][the][boundary][orbits] _[∂S]_[.] 

8.1. **Filling models.** Fix a Birkhoff section _S_ as in Theorem 5.2 and a diagonal system _{dR}_ as in Proposition 7.10. Applying Proposition 5.13 as in the proof of Theorem 1.2, we can put ∆in Legendrian position with respect to _ϕ_ and the bicontact form ( _α_ + _[S][, α] −[S]_[)] from Equation (5.1), and such that the projections to _O_ of the edges of ∆[�] are _dR_ . In particular, since _dR_ have interiors in _O[◦]_ , the edges of ∆are disjoint from the boundary orbits _∂S_ . In other words, _∂S_ intersects ∆by passing through the interior of faces. 

Let _γ_ be a boundary orbit of _S_ . Let _νγ_ be a tubular neighborhood of _γ_ , and let _mγ ∈ π_ 1( _∂νγ_ ) be the (oriented) meridian. Since we assumed that _γ_ is orientationpreserving, the local stable leaf of _γ_ intersects _νγ_ in two parallel curves, each of slope _dγ ∈ π_ 1( _∂νγ_ ) with intersection number one with _mγ_ . (In the literature _dγ_ is usually referred to as the **degeneracy slope** at _γ_ .) We can then write the slope on _∂νγ_ induced by _S_ as _pγµγ_ + _qγdγ_ , where _pγ >_ 0 and _qγ_ = 0. We refer to _[p] qγ[γ]_[as][the] **[slope]**[of] _[S]_[at] _γ_ . 

In the following construction, we will specify a choice of tubular neighborhood _νγ_ for each boundary orbit _γ_ . We will also construct a ‘shell’ around _γ_ , i.e. a collar neighborhood of _∂νγ_ , and endow specific coordinates on it. 

**Construction 8.1** (Shell around boundary orbits) **.** The foliations _ℓ[s/u]_ have 4 _pγ_ quadrants at the puncture _γ[◦]_ , which we label as q1 _, ...,_ q4 _pγ_ in a counterclockwise way starting from an unstable half-leaf. Recall that the measures on _ℓ[s/u]_ determine closed 1-forms _ds_ and _du_ on each quadrant q _k_ . We can locally integrate these closed 1-forms into functions _s_ and _u_ such that ( _s, u_ ) = (0 _,_ 0) at _γ[◦]_ . Set 

**==> picture [80 x 32] intentionally omitted <==**

Then for each _j ∈_ Z _/_ 4, the region[�] _k[{]_[(] _[t, x, y]_[)] _[ ∈]_[R] _[ ×]_[ q] _[j]_[+4] _[k][|][ x][ ∈]_[[] _[−][ε, ε]_[]] _[, y][∈]_[[] _[−][ε, ε]_[]] _[} ⊂]_ R _× S[◦]_ descends to a quadrant _Qj_ of _γ_ in _M[◦]_ . Taking the union over _Qj_ and _γ_ itself, we get a tubular neighborhood _νγ_ of _γ_ in _M_ . 

54 

## CHI CHEUK TSANG 

**==> picture [223 x 133] intentionally omitted <==**

**----- Start of picture text -----**<br>
Q 2 Q 2<br>Q 3 Q 3<br>y y<br>Q 1 Q 1<br>x Q 0 x Q 0<br>p [1] p<br>q [=] 3 q [=] [ −] [1] 3<br>**----- End of picture text -----**<br>


Figure 33. The tubular neighborhoods constructed in Construction 8.1. 

Note that 

_Q_ 0 _[∼]_ = _{_ ( _t, x, y_ ) _|_ R _/_ ( _pγ_ Z) _×_ R[2] _\{_ (0 _,_ 0) _} | x ∈_ [0 _, ε_ ] _, −x ≤ y ≤ x} Q_ 1 _[∼]_ = _{_ ( _t, x, y_ ) _|_ R _/_ ( _pγ_ Z) _×_ R[2] _\{_ (0 _,_ 0) _} | y ∈_ [0 _, ε_ ] _, −y ≤ x ≤ y} Q_ 2 _[∼]_ = _{_ ( _t, x, y_ ) _|_ R _/_ ( _pγ_ Z) _×_ R[2] _\{_ (0 _,_ 0) _} | x ∈_ [ _−ε,_ 0] _, ε_ ] _, x ≤ y ≤−y} Q_ 3 _[∼]_ = _{_ ( _t, x, y_ ) _|_ R _/_ ( _pγ_ Z) _×_ R[2] _\{_ (0 _,_ 0) _} | y ∈_ [ _−ε,_ 0] _, y ≤ x ≤−y}_ 

We set 

**==> picture [394 x 170] intentionally omitted <==**

as follows: 

**==> picture [25 x 13] intentionally omitted <==**

where 

**==> picture [165 x 31] intentionally omitted <==**

**==> picture [135 x 37] intentionally omitted <==**

See Figure 33 left. 

Alternatively, we can map 

**==> picture [25 x 13] intentionally omitted <==**

( _t, x, y_ ) _�→_ ( _x, y, t_ + _ρ_ ( _y_ )) on _Q_ 0 ( _t, x, y_ ) _�→_ ( _x, y, t_ ) on _Q_ 1 _, Q_ 2 _, Q_ 3 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

55 

where 

**==> picture [126 x 37] intentionally omitted <==**

See Figure 33 right. 

Under either of these coordinates, we can isotope the faces of ∆along orbits so that they are surfaces of the form _{z_ = _z_ 0 _}_ within the shells[�] _Q_[□] _j_[.] 

Now recall the bicontact form ( _α_ + _[S][, α] −[S]_[)][constructed][in][Section][5.4][.][We][can][compute] that 

**==> picture [190 x 34] intentionally omitted <==**

on each _Qj_ . 

Thus under Equation (8.1), we have 

**==> picture [234 x 34] intentionally omitted <==**

where 

**==> picture [120 x 36] intentionally omitted <==**

Similarly, under Equation (8.2), we have 

**==> picture [224 x 34] intentionally omitted <==**

where 

**==> picture [282 x 54] intentionally omitted <==**

_p p_ Next, we will construct, for each _[p] q[∈]_[Q] _[\{]_[0] _[}]_[, a strongly adapted bicontact form (] _[α]_ + _q[, α] −q_[)] _p p p_ on _ν q_ = [ _−ε, ε_ ] _×_ [ _−ε, ε_ ] _×_ R _/p_ Z such that ( _α_ + _q[, α] −q_[) = (] _[α]_ + _[S][, α] −[S]_[) on the shell constructed] in Construction 8.1. These will be used to fill the bicontact form ( _α_ + _[S][, α] −[S]_[)][into][the] boundary orbits. 

Note that the constructions for the cases when _[p] q[>]_[0][and] _[p] q[<]_[0][are][different.][This] asymmetry is due to the asymmetry between _α_ + and _α−_ in the definition of strongly adapted. 

CHI CHEUK TSANG 

56 

**Construction 8.2** (Filling bicontact form when _[p] q[>]_[ 0)] **[.]**[Choose][a][smooth][decreasing] function _ρ_ : R _→_ R such that 

**==> picture [130 x 37] intentionally omitted <==**

and such that _ρ[′]_ is an even function. Let 

**==> picture [335 x 68] intentionally omitted <==**

**==> picture [120 x 37] intentionally omitted <==**

We record the following positivity properties 

**==> picture [25 x 13] intentionally omitted <==**

**==> picture [90 x 87] intentionally omitted <==**

We now define 

**==> picture [264 x 37] intentionally omitted <==**

We compute 

**==> picture [104 x 19] intentionally omitted <==**

thus 

_p p α_ + _q[∧][dα]_ + _q_[= (log] _[ λ]_[)(1 +] _[ h]_[(] _[x]_[)] _[η][′′]_[(] _[y]_[))] _[dxdydz][>]_[ 0] 

under the orientation _dxdydz >_ 0, by Equation (8.3). Thus _α_ + is a positive contact form with Reeb vector field _R_ + = _∂y∂_[.] 

Meanwhile, we define 

**==> picture [222 x 19] intentionally omitted <==**

We compute 

**==> picture [216 x 18] intentionally omitted <==**

thus 

_p p α−q[∧][dα] −q_[= (log] _[ λ]_[)][2][(] _[−]_[1 +] _[ ρ][′]_[(] _[x]_[)(] _[η]_[(] _[y]_[)] _[ −][η][′]_[(] _[y]_[)] _[y]_[))] _[dxdydz][<]_[ 0] _p q_ by Equation (8.3). Thus _α−_[is][a][negative][contact][form.] 

57 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

We compute that 

**==> picture [356 x 111] intentionally omitted <==**

_p p p p_ By Equation (8.3), the last coefficient is positive, thus _α−q[∧][α]_ + _q_[= 0.][That][is,][(] _[α]_ + _q[, α] −q_[)] _p p_ is a bicontact form, and the line field ker _α_ + _q[∩]_[ker] _[ α] −q_[is][transverse][to][the][meridional] discs _{z_ = _z_ 0 _}_ . 

_p p p q q q_ Since _α−_[(] _[R]_[+][)][=][0,][(] _[α]_ + _[, α] −_[)][is][a][strongly][adapted][bicontact][form.][Also][note][that] _p p_ ( _α_ + _[S][, α] −[S]_[) = (] _[α]_ + _q[, α] −q_[)][on][the][shell][constructed][in][Construction][8.1][.] ♢ 

**Construction 8.3** (Filling bicontact form when _[p] q[<]_[ 0)] **[.]**[Choose][a][smooth][decreasing] function _ρ_ : R _→_ R such that 

**==> picture [120 x 37] intentionally omitted <==**

Choose a smooth increasing convex function _η_ : R _→_ R such that 

**==> picture [122 x 37] intentionally omitted <==**

We record the following positivity properties 

(8.4) 

**==> picture [90 x 69] intentionally omitted <==**

We now define 

**==> picture [218 x 19] intentionally omitted <==**

We compute 

**==> picture [225 x 19] intentionally omitted <==**

thus 

**==> picture [256 x 20] intentionally omitted <==**

CHI CHEUK TSANG 

58 

by Equation (8.4). Thus _α_ + is a positive contact form with Reeb vector field _R_ + = _∂[∂] ∂y[−][η][′]_[(] _[x]_[)] _[ρ][′]_[(] _[y]_[)] _∂t_[.] 

Meanwhile, we define 

**==> picture [228 x 19] intentionally omitted <==**

We compute 

**==> picture [233 x 18] intentionally omitted <==**

thus 

**==> picture [366 x 63] intentionally omitted <==**

**==> picture [286 x 56] intentionally omitted <==**

_p p p p_ The third coefficient is positive by Equation (8.4), thus _α−q[∧][α]_ + _q_[= 0.][That][is,][(] _[α]_ + _q[, α] −q_[)] _p p_ is a bicontact form, and the line field ker _α_ + _q[∩]_[ker] _[ α] −q_[is][transverse][to][the][meridional] discs _{z_ = _z_ 0 _}_ . 

_p p p q q q_ Since _α−_[(] _[R]_[+][)][=][0,][(] _[α]_ + _[, α] −_[)][is][a][strongly][adapted][bicontact][form.][Also][note][that] _p p_ ( _α_ + _[S][, α] −[S]_[) = (] _[α]_ + _q[, α] −q_[)][on][the][shell][constructed][in][Construction][8.1][.] ♢ 

## 8.2. **Legendrian position.** We are now ready to prove Theorem 1.1. 

_Proof of Theorem 1.1._ For each boundary orbit _γ_ , we first isotope the faces of ∆along orbits so that they are surfaces of the form _{z_ = _z_ 0 _}_ within the shells. Next, we cut out _pγ_ � _γ[ν][γ]_[from] _[M]_[and][glue][in][�] _γ[ν] qγ_ in order to get a strongly adapted bicontact form ( _α_ + _, α−_ ) defined on a 3-manifold homeomorphic to _M_ . In particular ( _α_ + _, α−_ ) supports an Anosov flow _ψ_ . 

Meanwhile, we can extend ∆ _∩_ ( _M \_[�] _γ[ν][γ]_[) into a copy of ∆placed in transverse position] with respect to _ψ_ on the reglued manifold by extending the faces by meridional discs _{z_ = _z_ 0 _}_ . Applying the uniqueness part of Theorem 3.5, this implies that _ϕ_ and _ψ_ are orbit equivalent through a map isotopic to identity. 

Moreover, since the blue edges are Legendrian with respect to _ξ_ + = ker _α_ + and the red edges are Legendrian with respect to _ξ−_ = ker _α−_ , ∆is in fact placed in Legendrian position with respect to _ψ_ . We pull back ( _α_ + _, α−_ ) using the orbit equivalence to get a bicontact structure supporting _ϕ_ . Then the pullback of ∆is in Legendrian position with respect to _ϕ_ and the pulled back bicontact structure. □ 

LEGENDRIAN POSITION OF VEERING TRIANGULATIONS 

59 

## References 

- [AS] Antonio Alfieri and Federico Salmoiraghi. Gluing Anosov flows via convex surface theory. In preparation. 

- [AT24] Ian Agol and Chi Cheuk Tsang. Dynamics of veering triangulations: infinitesimal components of their flow graphs and applications. _Algebr. Geom. Topol._ , 24(6):3401–3453, 2024. `doi:10.2140/agt.2024.24.3401` . 

- [AT25a] Antonio Alfieri and Chi Cheuk Tsang. Heegaard floer theory and pseudo-anosov flows i: Generators and categorification of the zeta function, 2025. URL: `https://arxiv.org/ abs/2504.15420` , `arXiv:2504.15420` . 

|[AT25a]|nents of their fow graphs and applications. _Algebr. Geom. Topol._, 24(6):3401–3453, 2024.<br>`doi:10.2140/agt.2024.24.3401`.<br>Antonio Alferi and Chi Cheuk Tsang. Heegaard foer theory and pseudo-anosov fows i:<br>Generators and categorifcation of the zeta function, 2025. URL: `https://arxiv.org/`<br>`abs/2504.15420`, `arXiv:2504.15420`.|
|---|---|
|[AT25b]|Antonio Alferi and Chi Cheuk Tsang. Heegaard foer theory and pseudo-anosov fows|
||ii: Diferential and fried pants, 2025. URL: `https://arxiv.org/abs/2506.07163`, `arXiv:`|
||`2506.07163`.|
|[BBM24]|Thomas Barthelm´e, Christian Bonatti, and Kathryn Mann. Non-transitive pseudo-Anosov|
||fows, 2024. URL: `https://arxiv.org/abs/2411.03586`, `arXiv:2411.03586`.|
|[BFM25]|Thomas Barthelm´e, Steven Frankel, and Kathryn Mann. Orbit equivalences of pseudo-|
||Anosov fows._Invent. Math._, 240(3):1119–1192, 2025.`doi:10.1007/s00222-025-01332-1`.|
|[BM26]|Thomas Barthelm´e and Kathryn Mann. Pseudo-anosov fows: A plane approach, 2026.|
||URL: `https://arxiv.org/abs/2509.15375`, `arXiv:2509.15375`.|
|[Bru95]|Marco Brunella. Surfaces of section for expansive fows on three-manifolds. _J. Math. Soc._|
||_Japan_, 47(3):491–501, 1995. `doi:10.2969/jmsj/04730491`.|
|[Cal00]|Danny Calegari. The geometry of **R**-covered foliations. _Geom. Topol._, 4:457–515, 2000.|
||`doi:10.2140/gt.2000.4.457`.|
|[CLMM22]|Kai Cieliebak, Oleg Lazarev, Thomas Massoni, and Agustin Moreno. Floer theory of anosov|
||fows in dimension three, 2022. URL:`https://arxiv.org/abs/2211.07453`, `arXiv:2211.`|
||`07453`.|
|[Fen02]|S´ergio R. Fenley. Foliations, topology and geometry of 3-manifolds: **R**-covered foliations|
||and transverse pseudo-Anosov fows. _Comment. Math. Helv._, 77(3):415–490, 2002. `doi:`|
||`10.1007/s00014-002-8348-9`.|
|[Fen16]|S´ergio R. Fenley. Quasigeodesic pseudo-Anosov fows in hyperbolic 3-manifolds and con-|
||nections with large scale geometry. _Adv. Math._, 303:192–278, 2016. `doi:10.1016/j.aim.`|
||`2016.05.015`.|
|[FH19]|Todd Fisher and Boris Hasselblatt. _Hyperbolic fows_. Zurich Lectures in Advanced Mathe-|
||matics. EMS Publishing House, Berlin, [2019] ©2019. `doi:10.4171/200`.|
|[FL25]|Steven Frankel and Michael Landry. From quasigeodesic to pseudo-anosov fows, 2025.|
||URL: `https://arxiv.org/abs/2510.02217`, `arXiv:2510.02217`.|
|[FLP12]|Albert Fathi, Fran¸cois Laudenbach, and Valentin Po´enaru._Thurston’s work on surfaces_, vol-|
||ume 48 of_Mathematical Notes_. Princeton University Press, Princeton, NJ, 2012. Translated|
||from the 1979 French original by Djun M. Kim and Dan Margalit.|
|[FSS25]|Steven Frankel, Saul Schleimer, and Henry Segerman. From veering triangulations to|
||link spaces and back again, 2025. URL: `https://arxiv.org/abs/1911.00006`, `arXiv:`|
||`1911.00006`.|
|[Hal25]|Layne Hall. Recognising perfect fts, 2025. URL: `https://arxiv.org/abs/2501.00232`,|
||`arXiv:2501.00232`.|
|[Hoz24]|Surena Hozoori. Symplectic geometry of Anosov fows in dimension 3 and bi-contact|
||topology. _Adv. Math._, 450:Paper No. 109764, 41, 2024. `doi:10.1016/j.aim.2024.109764`.|
|[Hoz25]|Surena Hozoori. Strongly adapted contact geometry of Anosov 3-fows. _J. Fixed Point_|
||_Theory Appl._, 27(2):Paper No. 37, 37, 2025. `doi:10.1007/s11784-025-01180-9`.|
|[Iak22]|Ioannis Iakovoglou. A new combinatorial invariant caracterizing anosov fows on 3-manifolds,|
||2022. URL: `https://arxiv.org/abs/2212.13177`, `arXiv:2212.13177`.|
|[Iak25]|Ioannis Iakovoglou. Markovian families for pseudo-anosov fows, 2025. URL: `https://`|
||`arxiv.org/abs/2509.19530`, `arXiv:2509.19530`.|



60 

## CHI CHEUK TSANG 

- [LMT23] Michael P. Landry, Yair N. Minsky, and Samuel J. Taylor. Flows, growth rates, and the veering polynomial. _Ergodic Theory Dynam. Systems_ , 43(9):3026–3107, 2023. `doi: 10.1017/etds.2022.63` . 

- [Mas25] Thomas Massoni. Anosov flows and Liouville pairs in dimension three. _Algebr. Geom. Topol._ , 25(3):1793–1838, 2025. `doi:10.2140/agt.2025.25.1793` . 

- [Mit95] Yoshihiko Mitsumatsu. Anosov flows and non-Stein symplectic manifolds. _Ann. Inst. Fourier (Grenoble)_ , 45(5):1407–1421, 1995. URL: `http://www.numdam.org/item?id=AIF_1995_ _45_5_1407_0` . 

- [Mos96] Lee Mosher. Laminations and flows transverse to finite depth foliations. _Preprint_ , 1996. 

- [Sal25] Federico Salmoiraghi. Surgery on Anosov flows using bi-contact geometry. _Ergodic Theory Dynam. Systems_ , 45(12):3832–3864, 2025. `doi:10.1017/etds.2025.10196` . 

- [Sha21] Mario Shannon. Hyperbolic models for transitive topological anosov flows in dimension three, 2021. `arXiv:2108.12000` . 

- [SS23] Saul Schleimer and Henry Segerman. From veering triangulations to dynamic pairs, 2023. `arXiv:2305.08799` . 

- [SS24] Saul Schleimer and Henry Segerman. From loom spaces to veering triangulations. _Groups Geom. Dyn._ , 18(2):419–462, 2024. `doi:10.4171/ggd/742` . 

- [Tsa23a] Chi Cheuk Tsang. Veering branched surfaces, surgeries, and geodesic flows. _New York J. Math._ , 29:1425–1495, 2023. 

- [Tsa23b] Chi Cheuk Tsang. _Veering Triangulations and Pseudo-Anosov Flows_ . PhD thesis, 2023. URL: `https://www.proquest.com/dissertations-theses/ veering-triangulations-pseudo-anosov-flows/docview/2869041415/se-2` . 

- [Tsa24a] Chi Cheuk Tsang. Constructing Birkhoff sections for pseudo-Anosov flows with controlled complexity. _Ergodic Theory Dynam. Systems_ , 44(8):2308–2360, 2024. `doi:10.1017/etds. 2023.105` . 

- [Tsa24b] Chi Cheuk Tsang. Examples of anosov flows with genus one birkhoff sections, 2024. URL: `https://arxiv.org/abs/2402.00229` , `arXiv:2402.00229` . 

- [Tsa24c] Chi Cheuk Tsang. Horizontal goodman surgery and almost equivalence of pseudo-anosov flows, 2024. `arXiv:2401.01847` . 

- [Zun] Jonathan Zung. Anosov flows and the pair of pants differential. In preparation. 

_Email address_ : `chicheuk@hotmail.com` 

