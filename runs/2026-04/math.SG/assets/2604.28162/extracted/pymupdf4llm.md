# **HEEGAARD FLOER HOMOLOGY AND MAXIMAL TWISTING NUMBERS** 

ALBERTO CAVALLO AND IRENA MATKOVIČ 

Abstract. We adapt the Ozsváth-Szabó full path algorithm to every star-shaped graph and establish a correspondence between negative-twisting tight contact structures on any Seifert fibred space over _S_[2] , and its Heegaard Floer homology groups equipped with the Alexander filtration induced by the regular fibre. This provides the complete classification of negative-twisting structures on these manifolds; in particular, we distinguish them by their contact invariant _c_[+] . We prove that every such structure is symplectically fillable and extend a known obstruction to Stein fillability. In addition, we show that the number of negative-twisting structures can be expressed combinatorially in terms of the Seifert coefficients of the star-shaped graph, while their _d_ 3-invariant and homotopy type are determined explicitly through our correspondence. Our results also complete the classification of fillable structures on any small Seifert fibred space. 

## 1. Introduction 

In [39] Ozsváth and Szabó introduced the full path algorithm as a way to compute the Heegaard Floer group _HF[−]_ ( _Y_ Γ) combinatorially, when _Y_ Γ is the 3-manifold presented by a suitable plumbing tree Γ. Namely, under the assumption that Γ is negative-definite, and that there is at most one "bad vertex", they showed that every homogeneous non-torsion class _α ∈ HF[−]_ ( _Y_ Γ) has even (Maslov) grading and can be written (up to multiplication by _U_ ) as _FP[−]_ Γ _,_ u[(1)][where] _[F][ −] P_ Γ _,_ u[:] _HF[−]_ ( _S_[3] ) _→ HF[−]_ ( _Y_ Γ _,_ s) is the corresponding cobordism map. 

Ozsváth and Szabó defined the graded maps _F[◦]_ induced by 4-dimensional Spin _[c]_ -cobordisms in [38], and they immediately appeared as a tool of primary importance in low dimensional topology considering the number of their applications. In the full path setting, the 4-manifold is the plumbing _P_ Γ given by the graph, while the Spin _[c]_ -structure can be identified with the characteristic vector _V ∈_ Char(Γ) corresponding to its first Chern class _c_ 1(u) _∈ H_[2] ( _P_ Γ; Z), as the manifold is simply connected, and s = u _|Y_ Γ. The true value of the full path algorithm is that it gives a practical method to not only identify _HF[−]_ ( _Y_ Γ) up to isomorphism, but also to determine precisely when two characteristic vectors _V_ 1 and _V_ 2 satisfy _FP[−]_ Γ _,_ u1[(1)][=] _[F][ −] P_ Γ _,_ u2[(1)][;][in][practical] terms, the full path defines an equivalence relation on the set of characteristic vectors, whose quotient set is precisely _HF[−]_ ( _Y_ Γ). Ozsváth and Szabó showed in [39, Theorem 1.2] that this correspondence holds also when we consider Heegaard Floer homology with integral coefficients, but in this paper we work with F the field with two elements. 

Later on, the full path has been extensively studied by Némethi [34]. He introduced the family of almost-rational graphs, whose precise definition is given in Section 2, generalising the one in [39]; Némethi proved that the full path, called computational sequence in his terminology, still recovers _HF[−]_ ( _Y_ Γ). The work of Némethi found many application in algebraic geometry; more specifically, in the study of singularities, see [34]. An example is given by the characterisation of rational singularities as the ones whose resolution is a Heegaard Floer _L_ -space, a property which is read from the Heegaard Floer groups and is, in this case, combinatorial thanks to the full path. 

Némethi [34] used the full path as the starting point to define lattice cohomology: a purely combinatorial invariant of a 3-manifold, defined from any plumbing tree, which recently has been showed by Zemke [55] to coincide with Heegaard Floer homology. 

2020 _Mathematics Subject Classification._ 57K18, 57K33, 57K43, 32Q35. 

2 

**==> picture [70 x 70] intentionally omitted <==**

**----- Start of picture text -----**<br>
− 2<br>− 3<br>− 1<br>− 5<br>**----- End of picture text -----**<br>


Figure 1. The manifold _−_ Σ(2 _,_ 3 _,_ 5) which is an _L_ -space, and thus its Heegaard Floer group _HF[−]_ has vanishing _U_ -torsion. 

It is important to note that the isomorphism given in the proof is not just an extension of the one in [39, Theorem 1.2], but it required a general version of the link surgery formula in Heegaard Floer. The fact that, once the assumption of the graph being almost-rational is dropped, the equivalence classes given by the full path cannot span the whole _HF[−]_ can already be seen from the simple example in Figure 1. The reason is that any graph representing _−_ Σ(2 _,_ 3 _,_ 5) gives a plumbing with positive _b_[+] 2[,][while][the][manifold][is][an] _[L]_[-space][(it][is][the][only][such][Brieskorn] sphere); Heegaard Floer cobordism maps have a restricted behaviour when the second positive Betti number is non-zero: the image of _F[−]_ is necessarily a torsion class [38]. Note that by definition _L_ -spaces have zero torsion in _HF[−]_ . 

Our first result concerns precisely the homology classes in _HF[−]_ ( _YG_ ) which can be identified with full paths, in the case that _G_ is a star-shaped graph. This kind of trees in low dimensional topology corresponds exactly to Seifert fibred spaces (with a sphere as base orbifold). In [8] we studied the relation between the full path and contact topology when the graph is negativedefinite: note that any Seifert fibred space can be oriented in this way. In this paper we focus on the other orientation, whose graph is _indefinite_ (with _b_[+] 2[=][1][),][and][the][singular][case][where][the] manifold is actually a surface bundle over the circle, see Sections 2 and 4. 

**The full path algorithm for a star-shaped graph.** Let _G_ be a star-shaped graph, with negative framings _m_ (1) _, ..., m_ ( _|G|_ ), and write _YG_ and _PG_ for the corresponding 3-manifold and plumbing. Let _V ∈ H_[2] ( _PG_ ; Z) be a characteristic vector, we write [ _V_ ] for its full path, see [39, 8] and Section 2 for the definition. As in [39, Lemma 2.3] we define the subspace 

**==> picture [262 x 14] intentionally omitted <==**

for any integer _n_ ⩾ 0; we say that [ _V_ ] _ends correctly_ when _Z ∈B_ 0 for each _Z ∈_ [ _V_ ]. This is equivalent to the definition we use in [8]. 

There is an involution _J_ : _HF[◦]_ ( _M,_ s) _→ HF[◦]_ ( _M,_ s) on the Heegaard Floer groups of any 3-manifold _M_ , which commutes with the maps induced by diffeomorphisms and cobordisms [41, Theorem 2.4]; moreover, if _ξ_ is a contact structure on _M_ then _J_ acts by conjugation on the contact invariant _c[◦]_ ( _ξ_ ) _∈ HF[◦]_ ( _−M,_ s _ξ_ ), that is _J c[◦]_ ( _ξ_ ) = _c[◦]_ ( _ξ_ ) _∈ HF[◦]_ ( _−M,_ s _ξ_ ), see [19]. In addition, when _L ⊂ M_ is an oriented link then _J_ identifies the filtration _F[L]_ on _HF[◦]_ ( _M,_ s) with _F[−][L]_ on _HF[◦]_ ( _M,_ s), given by reversing the orientation of _L_ , see [46, Lemma 3.12]. Dai and Manolescu [11] showed that in the full path setting we have _J_ [ _V_ ] = [ _−V_ ] for every characteristic vector _V ∈ H_[2] ( _PG_ ; Z) when _G_ is an almost-rational graph. The operation that maps characteristic vectors to their negation can be extended to the lattice cohomology group, see [36, Section 2.2]. The Heegaard Floer group _HF_[�] ( _M,_ s) can be decomposed as 

**==> picture [190 x 17] intentionally omitted <==**

according to the parity of the Maslov grading; namely, when _b_ 1( _M_ ) = 0 given s _∈_ Spin _[c]_ ( _M_ ) a class _α_ has even parity when _d_ ( _M,_ s) _− M_ ( _α_ ) is even, and it has odd parity otherwise. Using the commutativity of the cobordism maps in Heegaard Floer [38], we have that _F_[�] _PG,_ u : _HF_[�] ( _S_[3] ) _→_ 

3 

� _HF_ ( _M,_ s) coincides with _ψ∗ ◦FP[−] G,_ u[, where] _[ ψ][∗]_[:] _[ HF][ −] ∗_[(] _[M]_[)] _[ →] HF_[�] _∗_ ( _M_ ) is induced by setting _U_ = 0 in _CF[−]_ ( _M_ ). The results in [39, 34] show that, for a negative-definite _G_ , when _V_ = _c_ 1(u) then [ _V_ ] ends correctly if and only if _F_[�] _PG,_ u(1) is non-zero; moreover, the fact that these classes form a basis of _HF_[�] ev( _YG_ ) is well-known to experts, see [8, Proposition 2.2] for a complete proof. 

**Theorem 1.1** _Let G be an indefinite star-shaped graph with negative framings, and let YG_ = _∂PG be the_ 3 _-manifold presented by the graph. Then the homology classes_ [ _V_ ] = _FP[−] G,_ u[(1)] _[∈] HF[−]_ ( _YG,_ s) _, ranging among each V ∈_ Char( _G,_ s) _such that V_ = _c_ 1(u) _and_ s = u _|YG, span the subgroup_ Tor _HF[−]_ ( _YG,_ s) _; furthermore, they satisfy the following properties:_ 

- _the full path_ [ _V_ ] _corresponds to a non-zero class if and only if there exists an n_ ⩾ 0 _such that Z ∈Bn for each Z ∈_ [ _V_ ] _;_ 

- _the homology classes_ [ _V_ ] = _F_[�] _PG,_ u(1) _∈ HF_[�] ( _YG,_ s) _where_ [ _V_ ] _ends correctly form a basis of the subgroup HF_[�] od( _YG,_ s) _;_ 

- _the involution J coincides with the natural involution in lattice cohomology, and it acts as J_ [ _V_ ] = [ _−V_ ] _on each full path._ 

In the case that _G_ is a _singular_ star-shaped graph (we mean when _b[−]_ 2[(] _[P][G]_[)][=] _[|][G][|][−]_[1][and] _b_[+][=][0][),][the][corresponding][version][of][Theorem][1.1][has][been][proved][by][Rustamov][in][[49,] 2[(] _[P][G]_[)] Theorem 1.2], we give some details in Section 2. 

From standard Heegaard Floer theory the following duality canonical isomorphisms hold: 

� _HF ∗_ ( _−M,_ s) _≃ HF_[�] _−∗_ ( _M,_ s) _[•]_ and _HF∗_[+][(] _[−][M,]_[ s][)] _[ ≃][HF] −∗[ −]_[(] _[M,]_[ s][)] _[•]_[ ;] in particular, the second one holds in this form only when s _∈_ Spin _[c]_ ( _M_ ) is a torsion Spin _[c]_ - structure, see Section 2 for more details. We know from Ozsváth and Szabó’s results, and our Theorem 1.1 above, that the homology classes given by full paths always have the same parity; hence, we can never obtain a basis of the whole _HF_[�] ( _M,_ s) only with them (except when _M_ is an _L_ -space). Such a basis can be instead obtained using the duality isomorphism: say [ _V_ 1] _, ....,_ [ _Vt_ ] is the set of all the full paths of Char( _G[∗]_ ) that end correctly; then we can define the functionals _T_ [ _V_ 1] _, ..., T_ [ _Vt_ ], which are then homology classes in _HF_[�] ( _YG,_ s), and together with the full paths [ _W_ 1] _, ...,_ [ _Wt_ +1] of Char( _G_ ) they form a (canonical) basis of _HF_[�] ( _YG,_ s). Note that both _YG_ and _−YG_ = _YG∗_ can be presented by a star-shaped graph with negative framings, see Section 2. 

In Theorem 1.1 we identify the full path of a _V ∈_ Char( _G_ ) that ends correctly with both a homology class in _HF[−]_ ( _YG_ ), and its projection to _HF_[�] ( _YG_ ). Duality allows us to identify in a similar way the functional _T_ [ _V_ ] with a class in _HF_[�] ( _−YG_ ) and its inclusion in _HF_[+] ( _−YG_ ). In our previous works we gave many details about this properties, see [2, 8] and Section 2 below. 

ev od Say _G_ is negative-definite, and write _γ ∈ HF_[�] _∗_[(] _[Y][G][,]_[ s][)][and] _[δ][∈] HF_[�] _∗_[(] _[Y][G][,]_[ s][)][for][two][non-zero] homogenous classes. The full path gives us a combinatorial formula, in terms of the Alexander filtration _F_ on characteristic vectors [36, 34, 5, 8], for the _τ_ -invariant [45, 24, 2] of a regular fibre _K_ associated to these classes; note that in the case of _γ_ the formula has already appeared in [8, Equation 3.1], and it comes from the results of Alfieri in [1]. By Theorem 1.1 we have _γ_ = [ _W_ 1] + _· · ·_ + [ _Wk_ ] and _δ_ = _T_ [ _V_ 1] + _· · ·_ + _T_ [ _Vh_ ], where _F_ ( _Wi_ ) _< F_ ( _Wk_ ) _, F_ ( _Wh_ ) for _i < k, h_ and _F_ ( _Vi_ ) _> F_ ( _V_ 1) for _i >_ 1. 

**Theorem 1.2** _Say γ, δ ∈ HF_[�] _∗_ ( _YG,_ s) _are as above, and YG_ = _M_ ( _e_ 0; _r_ 1 _, ..., rn_ ) _is Seifert fibred with negative-definite standard graph. Then one has_ 

**==> picture [424 x 27] intentionally omitted <==**

_where Q and Q∗ are the intersection matrices of G and G[∗] , and e_ ( _YG_ ) := _r_ 1 + _..._ + _rn_ + _e_ 0 _._ 

4 

Note that similar formulae can be obtained when _G_ is indefinite, see Theorem 3.3. We show in Section 3 that the filtration _F[K]_ , induced by the regular fibre on _HF_[�] ( _YG_ ), can be determined combinatorially. 

In this paper we use the Hirzebruch-Jung convention [35, 50] on negative continued fractions; namely, for any rational number _r ∈_ (0 _,_ 1) we set _−_[1] _r_[=][[] _[m]_[1] _[, ..., m][k]_[]][with] _[m][i]_[⩽] _[−]_[2][integer][to][be] the number defined by the following recursive sequence: 

**==> picture [241 x 40] intentionally omitted <==**

The reason why this convention is useful in low dimensional topology is the following: it provides a simple way to express the resulting framing of the slam-dunk of a chain of unknots in a smooth surgery presentation of a 3-manifold. In particular, the lens space _L_ ( _p, q_ ) with 1 ⩽ _q < p_ coprime is diffeomorphic to _−[p]_[on][the][unknot,][and][then][to][the][surgery][on][a][chain][of][unknots] _q_[-surgery] whose framings are the terms in the negative continued fraction of _−[p] q_[.] 

**The classification of negative-twisting structures.** The _maximal twisting number_ of tight contact structures on a Seifert fibred space _M_ = _M_ ( _e_ 0; _r_ 1 _, ..., rn_ ) captures the maximal difference between the contact and fibration framing of a regular fibre _K_ . When _M_ is a rational homology sphere and its graph has at least three legs, this is 

**==> picture [397 x 26] intentionally omitted <==**

for a tight contact structure _ξ_ on _M_ . By convention [20], if tw( _M, ξ_ ) ⩾ 0 then we say that _ξ_ is _zero-twisting_ ; otherwise, we say it is _negative-twisting_ . In [8, Section 4] we specify how to define the maximal twisting number of the regular fibre in a Seifert fibration on a lens space, when the standard graph has two legs. 

We recall that in [20, Section 2] Ghiggini established a criterion that determines precisely when a certain negative integer is the twisting number of a tight structure on a Seifert fibred space. Ghiggini’s result was originally stated only when the standard graphs have exactly three legs and _e_ 0 = _−_ 1 or _−_ 2. We extended this criterion to any Seifert fibred space in [8, Proposition 4.1]. An analogous result was obtained by Massot in [31]. 

The following is a standard definition in elementary number theory, see [35]: we call a rational number _[p] q[<]_[1][a] _[best][upper][approximation]_[for] _[r][∈]_[(0] _[,]_[ 1)] _[∩]_[Q][when] _[p] q[>][r,]_[gcd(] _[p, q]_[)][=][1][and][no] rational number _h[k]_[with][1][⩽] _[h]_[⩽] _[q]_[and][1][⩽] _[k]_[⩽] _[p]_[is][in][the][interval][(] _[r,][p] q_[)][.][Note][that][after][we][fix] _q_ ⩾ 2 the best upper approximation is unique (provided it exists). 

**Theorem 1.3** (Ghiggini-Massot’s algorithm for negative maximal twisting numbers) _The Seifert fibred space M_ = _M_ ( _e_ 0; _r_ 1 _, . . . , rn_ ) _with n_ ⩾ 3 _and ri ∈_ (0 _,_ 1) _rational admits a tight contact structure ξ with twisting number equal to_ tw( _M, ξ_ ) = _−q < −_ 1 _if and only if there exist positive integer numbers p_ 1 _, . . . , pn such that_ 

_•[p] q[i][is][the][best][upper][approximation][for][r][i][when][i]_[ = 1] _[, ..., n][;]_ 

_• p_ 1 + _..._ + _pn_ = _−e_ 0 _q_ + _n −_ 2 _._ 

_Furthermore, we have that −_ 1 _is a twisting number if and only if e_ 0 ⩽ _−_ 2 _._ 

The starting point of our classification is to determine exactly which negative integers can be twisting number of a tight structure on _YG_ . In [8, Theorem 1.4] we showed that when _G_ is negative-definite the twisting number is unique; this is no longer the case here. For this reason we call tw( _YG_ ) the highest and tw( _YG_ ) the lowest negative twisting number of _YG_ . 

In [8, Theorem 1.1] the uniqueness of the twisting number when _G_ is negative-definite allowed us to classify the negative-twisting tight structures on _YG_ . In particular, we showed that all 

5 

such structures are Stein fillable, and the filling is smoothly the same 4-manifold: this is _XG_ the manifold obtained by blowing down the graph _G_ . We prove in Section 3 that this procedure can be done also when _G_ is either indefinite or singular; moreover, it still produces a Stein domain provided that _YG_ is not an _L_ -space. The difference with respect to the case in [8] lies in the fact that now not every negative-twisting structure is obtained in this way; namely, Ghiggini [20] already showed that oppositely oriented Brieskorn spheres may also carry non-Stein fillable structures. Nonetheless, we prove in Sections 4, 5 and 6 that the Stein fillable structures realised on _XG_ are precisely the ones whose twisting number is tw( _YG_ ). 

**Proposition 1.4** _Suppose that YG_ = _M_ ( _e_ 0; _r_ 1 _, . . . , rn_ ) _is a Seifert fibred space such that G is not negative-definite. The tight contact structures on M whose negative twisting number is_ tw( _YG_ ) _are precisely the Legendrian surgeries on all possible Legendrian realisations of the complete blowdown XG of G; moreover, when G is singular and YG is not a torus bundle over S_[1] _there are no other negative-twisting structures._ 

_Furthermore, every such ξ is Stein fillable and distinguished, up to isotopy, by its contact invariant c_[+] ( _ξ_ ) = _T_ [ _V_ ] _∈ HF_[+] ( _−YG,_ s _ξ_ ) _where V ∈_ Char( _G,_ s _ξ_ ) _._ 

Here, we exclude torus bundles over the circle because for these manifolds the classification has already been done by Honda [27], we give more details in Section 4. 

Note that not every characteristic vector _V_ whose full path ends correctly is such that _T_ [ _V_ ] is the contact invariant of a structure _ξ_ as above. This only happens when the strict transform of _V_ , see [4, Section 5] for details, is the characteristic vector of a Stein structure on _XG_ ; in this case, we say that _V_ is a _realised characteristic vector_ . As we discuss in Section 5, for a vector to be realised we require an additional technical assumption in order for _V_ to be uniquely determined in its full path: _V_ should be an "initial" vector, see [8] and Section 2 for details about this terminology. 

Let _V_ can = ( _m_ (1)+2 _, ..., m_ ( _|G|_ )+2) be the canonical characteristic vector [34], then we denote by scan the Spin _[c]_ -structure on _YG_ induced by _V_ can. We know from [4] that when _G_ is negative-definite _V_ can is realised by the Milnor fillable contact structure _ξ_ can; in fact, one has _c_[+] ( _ξ_ can) = _T_ [ _V_ can] _∈ HF_[+] ( _−YG,_ scan), and then _M_ ( _V_ can) = _d_ 3( _ξ_ can), and scan = s _ξ_ can. We keep this terminology also for a generic _G_ , even though _V_ can and _ξ_ can are not canonical in the same sense. 

In [8, Definition 2.6] we introduced the height _F_ of a full path [ _V_ ] as the number of central steps in [ _V_ ]. Here, we generalise this definition to any homogeneous non-zero class in _HF_[�] ( _YG,_ s), see Definition 3.5. In Section 3 we also prove that the height is equivalent to the Alexander filtration induced in homology by the regular fibre. 

**Theorem 1.5** _If YG_ = _M_ ( _e_ 0; _r_ 1 _, . . . , rn_ ) _with n_ ⩾ 3 _is an indefinite Seifert fibred space, then a negative twisting number_ tw( _YG, ξ_ ) _<_ tw( _YG_ ) _of a tight contact structure ξ on YG is given by_ 

**==> picture [186 x 11] intentionally omitted <==**

_for any realised characteristic vector V_ = _V_ can _such that_ [ _V_ ] _∈ HF_[�] _d_ 3( _ξ_ can)( _YG,_ scan) _; in addition, we have that_ 

**==> picture [144 x 13] intentionally omitted <==**

_All the negative twisting numbers are obtained in this way; therefore, they are determined by the Heegaard Floer homology of YG. Furthermore, when_ scan _is spin we have that_ 

**==> picture [134 x 13] intentionally omitted <==**

_where Q is the intersection matrix of the graph G._ 

For the other twisting numbers the classification is more complex, and in order to classify these "additional" structures we need to distinguish two different behaviours depending on the graph _G_ . We say that an indefinite Seifert fibred space _YG_ is of _type B_ when _G_ contains one of the 

6 

**==> picture [224 x 67] intentionally omitted <==**

**----- Start of picture text -----**<br>
− 2 ξ 1 ξ 2 ξ 3<br>− 3 ξ 12 ξ 23<br>− 1<br>− 6 − 4 ξ 13<br>**----- End of picture text -----**<br>


Figure 2. The oppositely oriented Brieskorn sphere _−_ Σ(2 _,_ 3 _,_ 23) is a manifold of type B. The Stein fillable structures _ξi_ have contact invariant _T_ [ _Vi_ ], where _Vi_ = (1 _,_ 0 _, −_ 1 _, −_ 4 _, −_ 4 + 2 _i_ ) for _i_ = 1 _,_ 2 _,_ 3. The structures in each row of the pyramid have twisting number _−_ 5 _, −_ 11 and _−_ 17 respectively. 

seven graphs in Figure 6 as a subgraph, and of _type A_ otherwise. These seven special graphs are exactly the only Seifert fibred spaces, whose base orbifold is a sphere, which are torus bundles over a circle, see [23, Subsection 2.1]. 

For a manifold of type A we show that there is always at most one additional structure for each Spin _[c]_ -structure, and we construct them using the results of Massot [31]. For one of type B we instead show that additional structures form _pyramids_ : for each homotopy class of contact structures, which consists of _ξ_ 1 _, ..., ξk_ , then there are _[k]_[(] _[k]_ 2 _[−]_[1][)] structures, that we denote by _ξij_ for 1 ⩽ _i < j_ ⩽ _k_ , with twisting number different from tw( _YG_ ); note that the number _k_ depends on the choice of the homotopy class which in turn is fixed by the underlying Spin _[c]_ -structure. 

The only two infinite families of oppositely oriented Brieskorn spheres whose classification of tight contact structures appears in literature are of type B; namely, these are _−_ Σ(2 _,_ 3 _,_ 6 _k −_ 1) for _k_ ⩾ 2, which was done by Ghiggini and Van Horn-Morris in [22], and _−_ Σ(2 _,_ 3 _,_ 6 _k_ + 1) for _k_ ⩾ 1, which was done by Tosun in [51] by an analogous argument. More generally, the count of tight structures is known also for particular surgeries on a singular fibre of _−_ Σ(2 _,_ 3 _,_ 6 _k_ +1), due to Wan [53]. In Figure 2 we show the manifold _−_ Σ(2 _,_ 3 _,_ 23) which belongs to the first family; in this case there are 6 structures, they are all homotopic and belong to the same pyramid. 

One of the additional advantages of our identification between negative-twisting contact structures and the full path algorithm is the following: we can describe the classification without needing to distinguish between manifolds of type A and B. In fact, our main result can be stated in the form below. 

**Theorem 1.6** _Suppose that YG_ = _M_ ( _e_ 0; _r_ 1 _, . . . , rn_ ) _is a Seifert fibred space, and G is indefinite. The tight contact structures ξ on M whose negative twisting number is −q_ = tw( _YG, ξ_ ) _<_ tw( _YG_ ) _are in one-to-one correspondence with the unordered pairs_ ( _Vi, Vj_ ) _for i ̸_ = _j of realised characteristic vectors in_ Char( _G,_ s _ξ_ ) _such that_ 

**==> picture [314 x 16] intentionally omitted <==**

_Furthermore, these structures are all symplectically fillable._ 

The exact number of negative-twisting tight contact structures on _YG_ , up to isotopy, is equal to the upper bound from convex surface theory. We write this number explicitly in Section 6. 

**Proposition 1.7** _Suppose that YG_ = _M_ ( _e_ 0; _r_ 1 _, . . . , rn_ ) _is a Seifert fibred space, and G is indefinite. Then ξ is a negative-twisting tight structure if and only if c_[+] ( _ξ_ ) _∈ HF_ red[+][(] _[−][Y][G][,]_[ s] _[ξ]_[)] _[is] non-vanishing. Furthermore, if_ tw( _YG, ξ_ ) _<_ tw( _YG_ ) _then c_[+] ( _ξ_ ) = _T_ [ _V_ 1] + _..._ + _T_ [ _Vk_ ] _for some k_ ⩾ 2 _, where V_ 1 _, ..., Vk are realised characteristic vectors in_ Char( _G,_ s _ξ_ ) _which satisfy_ 

**==> picture [310 x 12] intentionally omitted <==**

_and_ ( _V_ 1 _, Vk_ ) _is the unordered pair corresponding to ξ in Theorem 1.6._ 

7 

In Sections 6 and 7 we describe exactly what are the coordinates, with respect to the canonical basis _{T_ [ _V_ 1] _, ..., T_ [ _Vt_ ] _}_ , of the contact invariant _c_[+] ( _ξ_ ) _∈ HF_ red[+][(] _[−][Y][G][,]_[ s] _[ξ]_[)][ for each structure appearing] in Theorem 1.6 and Proposition 1.7. 

**Applications.** We prove the following results in Section 8. Our first example concerns Brieskorn spheres; in other words, any Seifert fibred space which is an integral homology sphere, see [50]. Equipped with the non-canonical orientation, a Brieskorn sphere is presented by an indefinite plumbing graph; therefore, the classification of its negative-twisting structures is a special case of Proposition 1.4 and Theorem 1.6. 

**Corollary 1.8** _Suppose that Y_ = Σ( _a_ 1 _, ..., an_ ) _is a canonically oriented Brieskorn sphere; then −Y is always of type A except when Y_ = Σ(2 _,_ 3 _,_ 6 _k ±_ 1) _with k_ ⩾ 1 _. Furthermore, any negativetwisting structure ξ on −Y is either as in Proposition 1.4, when_ tw( _−Y, ξ_ ) = tw( _−Y_ ) _, or is isotopic to the unique structure such that_ tw( _−Y, ξ_ ) = tw( _−Y_ ) _._ 

In the two cases remaining we know from [22, 51] that there is a unique pyramid of size _k −_ 1 and _k_ respectively; in particular, it is a famous result of Etnyre and Honda [15] that _−_ Σ(2 _,_ 3 _,_ 5) admits no tight structure. Combining our classifications in this paper and in [8], we determine exactly which Brieskorn spheres have a unique structure with a given orientation. 

**Theorem 1.9** _The only Brieskorn spheres carrying a unique tight contact structure, up to isotopy, are_ Σ(2 _,_ 3 _,_ 5) _, −_ Σ(2 _,_ 3 _,_ 11) _and −_ Σ(2 _,_ 3 _,_ 7) _. Such a structure is negative-twisting and Stein fillable._ 

Combining a previous result of Matkovič [32] with the ones in this paper, we complete the classification of fillable structures on any small Seifert fibred space. In particular, every negativetwisting structure on these manifolds is fillable, confirming a conjecture in [32]. 

**Theorem 1.10** _Every symplectically fillable structure on M_ ( _e_ 0; _r_ 1 _, r_ 2 _, r_ 3) _is either included in our classifications (either above or in_ [8, Theorem 1.1] _or_ [32, Theorem 1.1] _) when e_ 0 ⩽ _−_ 1 _, or is included in the classification in_ [21, Theorem 1.1] _when e_ 0 ⩾ 0 _._ 

_Proof._ Any fillable structure is tight and then either negative- or zero-twisting. Then the claim follows from Proposition 1.4, Theorem 1.6 and [8] in the first case, and from [21, 32] in the second one. Note that when _n_ = 3 the structures considered in the latter papers are the only zero-twisting structures on _M_ , as half convex Giroux torsion makes the structure overtwisted; moreover, when _e_ 0 ⩽ _−_ 2 there are no zero-twisting structures by convex surface theory arguments [54]. □ 

This includes rational surgeries on the torus knot _Td_ 2 _,±d_ 1, except for the slope _±d_ 1 _d_ 2 when fillable structures are easily determined anyway. In general, for surgeries on torus links we have the following result. 

**Corollary 1.11** _Every negative-twisting structure on Sr_[3][(] _[T][kd]_ 2 _[,][±][kd]_ 1[)] _[with][r][∈]_[Q] _[,][k]_[⩾][1] _[and]_[1][⩽] _d_ 2 ⩽ _d_ 1 _coprime is either included in our classifications (either above or in_ [8, Corollary 1.2] _), or it is the connected sum of some tight structures on lens spaces._ 

For surgeries on torus knots we can explicitly determine surgery interval which admit any given twisting number. Note that _Sr_[3][(] _[T][d]_ 2 _[,d]_ 1[)][is][of][type][B][only][when][(] _[d]_[2] _[, d]_[1][) = (2] _[,][ ±]_[3)][and] _[r][∈]_[(0] _[,]_[ 1)][.] 

**Proposition 1.12** _The manifold Sr_[3][(] _[T][d]_ 2 _[,d]_ 1[)] _[with][r][∈]_[Q] _[carries][a][negative-twisting][tight][structure] if and only if r < d_ 1 _d_ 2 _− d_ 2 _− d_ 1 _. When_ ( _d_ 2 _, d_ 1) = (2 _,_ 3) _there are at most two possible negative twisting numbers: one is always equal to −d_ 2 _− d_ 1 _, while the other is_ 

**==> picture [412 x 14] intentionally omitted <==**

8 

_where_ [ _n_ 1 _, ..., nh_ ] = _−[d]_[1][+] _[d] s_[2] +1[+] _[sd]_[1] _[d]_[2] _is reduced. Furthermore, when_ ( _d_ 2 _, d_ 1) = (2 _,_ 3) _one twisting number is always equal to −_ 5 _, while the other ones are_ 

**==> picture [310 x 43] intentionally omitted <==**

_The manifold Sr_[3][(] _[T][d]_ 2 _[,][−][d]_ 1[)] _[carries][a][tight][structure][with][twisting][number][−]_[1] _[if][and][only][if][r][>] −d_ 2 _d_ 1 _; moreover, when_ ( _d_ 2 _, d_ 1) = (2 _,_ 3) _another negative twisting number appears if and only if it exists for Sr_[3][(] _[T][d]_ 2 _[,d]_ 1[)] _[,][and][its][value][is][lowered][by]_[2(] _[d]_[1] _[d]_[2] _[−][d]_[1] _[−][d]_[2][)] _[.][When]_[(] _[d]_[2] _[, d]_[1][)][=][(2] _[,]_[ 3)] _[the] other twisting numbers are the ones on Sr_[3][(] _[T]_[2] _[,]_[3][)] _[lowered][by]_[2] _[.]_ 

Combining Proposition 1.12 with the elementary number theory in Section 6, we can determine the exact number of negative-twisting structures on either _Sr_[3][(] _[T][d]_ 2 _[,d]_ 1[)][or] _[S] r_[3][(] _[T][d]_ 2 _[,][−][d]_ 1[)][.][Take] [ _m_ 1 _, ..., mk_ ] to be _−d_ 1 _d_ 2 + _r_ and _− d_ 1 _dd_ 12 _d_ +2+ _r−r_ 1[respectively,][then][we][have:] 

- either _|m_ 1 + _d_ 1 + _d_ 2 _| · |m_ 2 + 1 _| · · · |mk_ + 1 _|_ or _|m_ 1 + 1 _| · |m_ 2 + 1 _| · · · |mk_ + 1 _|_ structures with twisting number tw( _−Y_ ), when either _r < d_ 1 _d_ 2 _− d_ 1 _− d_ 2 or _r > −d_ 1 _d_ 2; 

- either _|m_ 3 + 1 _| · · · |mk_ + 1 _|_ pyramids of size _|m_ 2 + 1 _|_ or _|m_ 7 + 1 _| · · · |mk_ + 1 _|_ pyramids of size _|m_ 6 + 1 _|_ when ( _d_ 2 _, d_ 1) = (2 _,_ 3) and 0 _< r <_ 1, at most one in each Spin _[c]_ -structure; 

- max _{|mh − nh| · |mh_ +1 + 1 _| · · · |mk_ + 1 _|,_ 1 _}_ structures with twisting number smaller than tw( _−Y_ ) (if it existed) when ( _d_ 2 _, d_ 1) = (2 _,_ 3), at most one in each Spin _[c]_ -structure, where [ _n_ 1 _, ..., nh_ ] is either the reduced fraction _−[d]_[1][+] _[d] s_[2] +1[+] _[sd]_[1] _[d]_[2] or _− s_ +1+ _d_ 1+ _d_ 1 _d_ +2 _−d_ 2( _s−_ +(2 _s_ +2)) _d_ 1 _dd_ 21 _d_ 2[for][an] _[s >]_[ 0][.] 

In Theorem 1.6 we show that every negative-twisting structure on a Seifert fibred space is symplectically fillable; moreover, Proposition 1.4 tells us that when the twisting number is equal to tw( _YG_ ) we can actually produce a Stein filling. In some cases it is possible to show that Stein fillings do not exist. 

We introduce some terminology for negative-twisting structures on Seifert fibred spaces _YG_ of type B, based on Figures 2 and 3. We say that a contact structure _ξ_ with tw( _YG, ξ_ ) _<_ tw( _YG_ ) is a _pyramidion_ if it appeared as the apex of its pyramid; in other words, when it has the lowest twisting number in its homotopy class. In the same way, we say that _ξ_ is a _casing stone_ if it appeared in a pyramid with base _ξ_ 1 _, ..., ξk_ as either _ξ_ 1 _j_ for 1 _< j < k_ or _ξlk_ for 1 _< l < k_ . 

**==> picture [104 x 79] intentionally omitted <==**

**----- Start of picture text -----**<br>
ξ 1 ξ 2 ξ 3 ξ 4<br>ξ 23<br>ξ 12 ξ 34<br>ξ 13 ξ 24<br>ξ 14<br>**----- End of picture text -----**<br>


Figure 3. We call the grey structures casing stones, and the red one pyramidion. If the pyramid appeared in a spin structure then _c_[+] ( _ξ_ 23) and _c_[+] ( _ξ_ 14) would both be selfconjugate. 

**Proposition 1.13** _Let YG be a Seifert fibred space with G indefinite, and ξ be a negative-twisting structure on YG. If_ tw( _YG, ξ_ ) _<_ tw( _YG_ ) _and c_[+] ( _ξ_ ) _is self-conjugate under J , that is J c_[+] ( _ξ_ ) = _c_[+] ( _ξ_ ) _, then ξ is not Stein fillable._ 

_Proof._ We describe the argument for the obstruction, which comes from Ghiggini’s work [18]. By the proof of Proposition 1.7 we have that _c_[+] ( _ξ_ ) = _T_ [ _V−h_ ] + _· · ·_ + _T_ [ _Vh_ ] _∈ HF_[+] ( _−YG,_ s _ξ_ ) for some _V±_ 1 _, ..., V±h ∈_ Char( _G,_ s _ξ_ ) realised; since _c_[+] ( _ξ_ ) is self-conjugate, we can assume that [ _V−i_ ] = 

9 

[ _−Vi_ ] = _J_ [ _Vi_ ] for every _i_ . Suppose that _YG_ admits a Stein filling ( _X, J_ ); from [44, 19] we know that _FX,J_[+][(] _[c]_[+][(] _[ξ]_[)) = 1][ and] _[ F] X,_[+] _−J_[(] _[c]_[+][(] _[ξ]_[)) =] ~~_[F]_~~ _X,_[+] _−J_[(] _[c]_[+][(] _ξ_ )) = 1, while from Plamenevskaya [48] we obtain that _J_ coincides with _−J_ as a Spin _[c]_ -structure. Hence, for each _i_ we have _F_[+] ~~_[F]_~~[+] _X,J_[(] _[T]_[[] _[V][i]_[]][) =] _X,J_[(] _[T]_[[] _[V][−][i]_[]][)] which implies _F_[+][and][this][is][a][contradiction.] □ _X,J_[(] _[c]_[+][(] _[ξ]_[)) = 0][,] 

Note that _c_[+] ( _ξ_ ) is self-conjugate for any additional structure on a type A manifold provided that s _ξ_ is spin. When the structure is neither a casing stone nor a pyramidion a different obstruction, coming from a result of Christian and Menke in [9], has been given in [33, 16] for a certain choice of the coefficients. 

For Brieskorn spheres Corollary 1.8 and Proposition 1.13 obstruct Stein fillability for every negative-twisting structure _ξ_ with tw( _YG, ξ_ ) _<_ tw( _YG_ ) except when _YG_ = _−_ Σ(2 _,_ 3 _,_ 6 _k ±_ 1). In the latter case, from the results mentioned above, only the casing stones can possibly be Stein fillable. 

**Sample computations.** We now illustrate our method by writing the classification explicitly in two examples: the first one is _−_ Σ(3 _,_ 4 _,_ 47) = _S_ 1[3] _/_ 4[(] _[T]_[3] _[,]_[4][)][, while the second one is] _[ M]_[(] _[−]_[2;] 2[1] _[,]_[1] 2 _[,]_[4] 7 _[,]_ 11[6][)][,] see Figure 4. We want to highlight that our method, which involves computing the realised characteristic vectors through the full path algorithm, behaves in the same way independently of the fact that the first manifold is a surgery on a torus knot. We also observe that the number of structures and pyramids (when the manifold is of type B), and the maximal twisting number, can be determined immediately using the formulae in Subsection 6.1 and Ghiggini-Massot’s algorithm in Theorem 1.3, while by using the full path we can see the gradings of each contact structure. 

**==> picture [262 x 83] intentionally omitted <==**

**----- Start of picture text -----**<br>
− 2<br>− 2 − 2 − 2 − 4<br>− 2<br>− 1 − 4<br>− 2 − 6<br>− 12 − 4 − 2<br>**----- End of picture text -----**<br>


Figure 4. A plumbing graph representing _−_ Σ(3 _,_ 4 _,_ 47) = _M_ ( _−_ 1;[2] 3 _[,]_[1] 4 _[,]_ 47[4][)][(left),][and] one representing _M_ ( _−_ 2; 2[1] _[,]_[1] 2 _[,]_[4] 7 _[,]_ 11[6][)][(right).] 

Let us assume that _M_ = _−_ Σ(3 _,_ 4 _,_ 47) = _M_ ( _−_ 1;[2] 3 _[,]_[1] 4 _[,]_ 47[4][)][.][Then][the][possible][negative][twisting] numbers are _−_ 7 and _−_ 223; in fact, we have that 

( _p_ 1 _, p_ 2 _, p_ 3) = (5 _,_ 2 _,_ 1) and ( _P_ 1 _, P_ 2 _, P_ 3) = (149 _,_ 56 _,_ 19) ; hence, comparing each _ri_ with _[p]_ 7 _[i]_[and] 223 _[P][i]_[for] _[ i]_[ = 1] _[,]_[ 2] _[,]_[ 3][, from Equation (6.1) the number of contact] structures is 

**==> picture [170 x 9] intentionally omitted <==**

matching the computation in Table 1 and in Proposition 1.12. 

The realised characteristic vectors are obtained as described in Theorem 5.4: 

**==> picture [344 x 12] intentionally omitted <==**

The combined height in Tables 1 and 2 is the maximum height of any homology class [ _Vi_ ] + [ _Vj_ ] among realised vectors with the given gradings (provided that there are at least two of them). Note that the unique structure on _M_ with twisting number _−_ 223 appears in grading 19 because, according to Theorems 1.5 and 1.6, we need height _F_ ([ _Vi_ ] + [ _Vj_ ]) = _−_ 1 _−_ tw( _M_ ) = 222. 

10 

|s_ξ_|_d_3(_ξ_)|_V ∈_Char(_M_)<br>realised|Combined<br>height|tw(_M, ξ_)|
|---|---|---|---|---|
|scan =<br>scan|19|(1_,_0_,_0_, −_2_, −_10_, −_2)<br>(1_,_0_,_0_, −_2_, −_2_,_2)|222|_−_7 and _−_223|
||15|(1_,_0_,_0_, −_2_, −_10_,_0)<br>_•_<br>(1_,_0_,_0_, −_2_, −_2_,_0)<br>_•_|198|_−_7|
||11|(1_,_0_,_0_, −_2_, −_10_,_2)<br>_•_<br>(1_,_0_,_0_, −_2_, −_2_, −_2)<br>_•_|174||
||5|(1_,_0_,_0_, −_2_, −_8_, −_2)<br>_•_<br>(1_,_0_,_0_, −_2_, −_4_,_2)<br>_•_|126||
||3|(1_,_0_,_0_, −_2_, −_8_,_0)<br>_•_<br>(1_,_0_,_0_, −_2_, −_4_,_0)<br>_•_|102||
||1|(1_,_0_,_0_, −_2_, −_8_,_2)<br>_•_<br>(1_,_0_,_0_, −_2_, −_4_, −_2)<br>_•_|78||
||_−_1|(1_,_0_,_0_, −_2_, −_6_, −_2)<br>_•_<br>(1_,_0_,_0_, −_2_, −_6_,_0)<br>_•_<br>(1_,_0_,_0_, −_2_, −_6_,_2)<br>_•_|30||



Table 1. There are 16 negative-twisting contact structures on _M_ = _−_ Σ(3 _,_ 4 _,_ 47) which is of type A. One of them has twisting number _−_ 223, while for the other fifteen this is _−_ 7. 

We now assume that _M_ = _M_ ( _−_ 2;[1] 2 _[,]_[1] 2 _[,]_[4] 7 _[,]_ 11[6][)][; we use the same procedure as above.][The possible] negative twisting numbers are _−_ 1 _, −_ 3 and _−_ 5; in fact, we have that _e_ 0 ⩽ _−_ 2 and 

**==> picture [312 x 12] intentionally omitted <==**

hence, from Equation (6.2) and comparing each _ri_ with _[p]_ 3 _[i]_[and] _[P]_ 5 _[i]_[for] _[i]_[=][1] _[, ...,]_[ 4][,][the][number][of] contact structures is 

**==> picture [318 x 11] intentionally omitted <==**

matching the computation in Table 2. 

The realised characteristic vectors are again obtained from Theorem 5.4: 

**==> picture [340 x 12] intentionally omitted <==**

**Remark 1.14** _We prove in Theorem 1.5 that for any V ∈_ Char( _G_ ) _realised one has_ 

**==> picture [210 x 12] intentionally omitted <==**

_This means that for every_ [ _V[′]_ ] _∈ HF_[�] _M_ ( _V_ )( _YG,_ u _|YG_ ) _, where c_ 1(u) = _V , such that_ [ _V[′]_ ] = [ _V_ ] _we have_ height _F_ ([ _V_ ] + [ _V[′]_ ]) _>_ height _F_ [ _V_ can] _. Hence, the combined height in Tables 1 and 2 can only equal_ height _F_ [ _V_ can] _if the contact structure with invariant T_ [ _V_ ] _is alone in its homotopy class._ 

11 

|s_ξ_|_d_3(_ξ_)|_V ∈_Char(_M_)<br>realised|Combined<br>height|tw(_M, ξ_)|
|---|---|---|---|---|
|scan|5<br>36|(0_,_0_,_0_, −_2_,_0_, −_4_,_0)<br>(0_,_0_,_0_,_0_,_0_, −_2_,_0)<br>(0_,_0_,_0_,_2_,_0_,_0_,_0)|4|_−_1_, −_3 and _−_5|
|scan|5<br>36|(0_,_0_,_0_, −_2_,_0_,_0_,_0)<br>(0_,_0_,_0_,_0_,_0_,_2_,_0)<br>(0_,_0_,_0_,_2_,_0_,_4_,_0)|4|_−_1_, −_3 and _−_5|
|s1 =<br>s1|1<br>4|(0_,_0_,_0_, −_2_,_0_, −_2_,_0)<br>(0_,_0_,_0_,_0_,_0_,_0_,_0)<br>(0_,_0_,_0_,_2_,_0_,_2_,_0)|4|_−_1_, −_3 and _−_5|
|s2|_−_7<br>36|(0_,_0_,_0_, −_2_,_0_,_2_,_0)<br>(0_,_0_,_0_,_0_,_0_,_4_,_0)|2|_−_1 and _−_3|
|s2|_−_7<br>36|(0_,_0_,_0_,_0_,_0_, −_4_,_0)<br>(0_,_0_,_0_,_2_,_0_, −_2_,_0)|2|_−_1 and _−_3|
|s3|_−_3<br>4|(0_,_0_,_0_, −_2_,_0_,_4_,_0)<br>_•_|0|_−_1|
|s3|_−_3<br>4|(0_,_0_,_0_,_2_,_0_, −_4_,_0)<br>_•_|0|_−_1|



Table 2. There are 26 negative-twisting contact structures on _M_ = _M_ ( _−_ 2;[1] 2 _[,]_[1] 2 _[,]_[4] 7 _[,]_ 11[6][)] which is of type B. Three of them have twisting number _−_ 5, eight of them have twisting number _−_ 3, and for the other fifteen this is _−_ 1. The structures are distributed into seven pyramids: three of size 3, two of size 2, and two of size 1. Note that _|H_ 1( _M_ ; Z) _|_ = 36, but only seven Spin _[c]_ -structures support realised characteristic vectors. 

**Acknowledgements.** We are indebted to Paolo Ghiggini for his mathematical insight and invaluable help. We thank the Matematiska institutionen at Uppsala universitet for their friendly hospitality. A.C. has been partially supported by the HORIZON-ERC-2023-ADG 101141468 KnotSurf4d project. 

## 2. On the full path algorithm 

We assume that the reader is familiar with [8, Section 2]. Every Seifert fibred space whose base orbifold is a sphere is presented by a star-shaped graph that we call the _standard graph_ . Unless the manifold is either _S_[3] _, S_[1] _× S_[2] or a lens space, the standard graph has at least three legs and it is unique once we fix our convention [50]. 

We denote the standard graph of a Seifert fibred space _M_ by _G_ , or by Γ when we assume _M_ to be oriented in the way its graph is negative-definite. We take _M_ = _M_ ( _e_ 0; _r_ 1 _, ..., rn_ ) where _e_ 0 _∈_ Z and _ri ∈_ (0 _,_ 1) _∩_ Q; in addition, for the reason we explained above, in this paper we always assume that _n_ ⩾ 3. As usual the framings on the vertices in the legs of _G_ are determined by the negative continued fraction expansion of the _ri_ ’s; hence, except for the central vertex whose framing is _e_ 0, all the others are smaller or equal than _−_ 2. 

12 

The dual graph _G[∗]_ is then the standard graph of 

**==> picture [182 x 12] intentionally omitted <==**

in particular, we have that _e_ ( _−M_ ) = _−e_ ( _M_ ) where _e_ ( _M_ ) = _e_ 0 + _r_ 1 + _..._ + _rn_ . We know from the literature [50] that 

**==> picture [205 x 46] intentionally omitted <==**

Since removing the central vertex always produces a negative-definite graph, the plumbing _PG_ is negative-definite if and only if _b_[+] 2[(] _[P][G][∗]_[)][=][1][,][or][vice-versa] _[b]_[+] 2[(] _[P][G]_[)][=][1][if][and][only][if] _[P][G][∗]_[is] negative-definite. 

We call _G[′]_ any _maximal S_[3] _-subgraph_ of _G_ ; in other words, a maximal subgraph that can be cancelled by a sequence of blow-downs, starting from _G_ . The graph _G[′]_ always corresponds to the Seifert fibration of a torus knot _Td_ 2 _,±d_ 1 in _S_[3] , including the degenerate cases _T_ 1 _,d_ 1 and _T_ 1 _,_ 1; the differences appearing in these two cases are highlighted in [8, Sections 4 and 5]. 

Let us denote by _Y_ any 3-manifold presented by an _almost-rational graph_ , that is the union of some negative-definite plumbing trees such that lowering the framing of one vertex makes _Y_ an _L_ -space. We always denote by _−Y_ the manifold obtained by reversing the orientation. Every Seifert fibred space _M_ as above with _e_ ( _M_ ) _̸_ = 0 has standard graph which is almost-rational with exactly one orientation. 

We recall the notation about Heegaard Floer maps relating the three main flavours of the homology groups: 

**==> picture [218 x 17] intentionally omitted <==**

and 

**==> picture [460 x 46] intentionally omitted <==**

**==> picture [184 x 17] intentionally omitted <==**

where the first is the subgroup of the classes with Maslov grading _i_ with the same parity of the correction term _d_ ( _Y,_ s), that is _i − d_ ( _Y,_ s) _≡_ 0 mod 2, while the second one is generated by the classes with Maslov grading _j_ such that _j − d_ ( _Y,_ s) _≡_ 1 mod 2. 

It follows from [39, 34], see also [8, Theorem 2.1], that if _Y_ is almost-rational then 

**==> picture [324 x 15] intentionally omitted <==**

and 

**==> picture [380 x 18] intentionally omitted <==**

We know that the full path algorithm from [39] provides a basis as an F-vector space of 

**==> picture [374 x 23] intentionally omitted <==**

through the canonical duality _HF_[�] _∗_ ( _−Y,_ s) _≃ HF_[�] _−∗_ ( _Y,_ s) _[•]_ . We want to show that a relation similar to Equation (2.3) holds for _−M_ when _M_ is a negative-definite Seifert fibred space. We recall that a 4-manifold _X_ , together with a Spin _[c]_ -structure u, induces maps in Heegaard Floer homology between _S_[3] and ( _Y_ = _∂X,_ s = u _|Y_ ); moreover, when _c_ 1(u) is torsion the image has Maslov grading equal to 

**==> picture [342 x 25] intentionally omitted <==**

13 

and when _b_ 1( _X_ ) = 0 the homology class _FX,[−]_ u[(1)][is][non-torsion][if][and][only][if] _[b]_[+] 2[(] _[X]_[) = 0][,][see][[38].] 

**Theorem 2.1** _Let Y be a negative-definite Seifert fibred space, and denote by_ Γ _its standard graph and by P_ Γ _∗ the plumbing associated to its dual_ Γ _[∗] so that ∂P_ Γ _∗_ = _−Y . Then assuming that the central vertex of_ Γ _[∗] has negative framing, the full paths of_ Γ _[∗] ending correctly provide an_ F _-basis of HF_[�] od( _−Y,_ s) _. More specifically, for every characteristic vector V ∈_ Z _|_ Γ _∗| ≃ H_ 2( _P_ Γ _∗_ ; Z) _one has F[−][where][c]_[1][(][u][) =] _[ V][ .] P_ Γ _∗ ,_ u[(1) = [] _[V]_[ ]] _[ ∈]_[Tor] _[HF][ −]_[(] _[−][Y,]_[ s][)] 

Note that this implies that we have a basis _{_ [ _V_ 1] _, ...,_ [ _Vt_ ] _, T_ [ _W_ 1] _, ..., T_ [ _Wt_ +1] _}_ of _HF_[�] ( _−Y,_ s), obtained by identifying the full path of each characteristic vector _Vi_ = _c_ 1(u _i_ ) with _F_[�] _P_ Γ _∗ ,_ u _i_ (1) and of each _Wj_ = _c_ 1(v _j_ ) with _FP[−]_ Γ _,_ v _j_[(1)][where][v] _[j][∈]_[Spin] _[c]_[(] _[P]_[Γ][)][,][assuming][they][end][correctly.][Then][the] functional _T_ [ _Wj_ ] : _HF[−]_ ( _Y,_ s) _→_ F defined by 

**==> picture [269 x 14] intentionally omitted <==**

ev is an element of Ker _U ⊂ HF_[+] ( _−Y,_ s), and then it is identified with one of _HF_[�] ( _−Y,_ s) by Equation (2.1). In the same way, we have that _{T_ [ _V_ 1] _, ..., T_ [ _Vt_ ] _,_ [ _W_ 1] _, ...,_ [ _Wt_ +1] _}_ is a basis of _HF_[�] ( _Y,_ s), see [8, Subsection 2.4] for more details. 

We postpone the proof of Theorem 2.1 to Subsection 2.3. We do not give all the possible details about characteristic vectors and the full path, as we refer to the original paper of Ozsváth and Szabó [39] for these; nonetheless, we will highlight the differences between the indefinite and negative-definite case. Note that even though the original proof works for every almost-rational graph, here we rely heavily on the fact that graph is star-shaped. We do not think that our results can be generalised easily to a larger family of 3-manifolds. 

2.1. **The surgery exact triangle.** We start by describing the strategy of the proof of Theorem 2.1. Say _Y_ is represented by the negative-definite graph Γ, and let _P_ = _P_ Γ _∗_ be the plumbing of Γ _[∗]_ ; we consider the following exact surgery triangle 

**==> picture [342 x 53] intentionally omitted <==**

where _−Y_ 0 is the connected sum of lens spaces obtained by removing the centre of Γ _[∗]_ , and _−Y_ 1 is the manifold whose graph has framing on the centre lowered by one respect to Γ _[∗]_ . Clearly, we have that _−Y_ 0 is presented by a negative-definite tree, but _−Y_ 1 may not. Since lowering the framing on the central vertex enough times yields a tree with no bad vertices, and then a negative-definite _L_ -space, we can use an inductive argument to prove that the set _{FP,[−]_ u[(1)] _[}]_[ where] _c_ 1(u) = _V ∈ H_[2] ( _P_ ; Z) is a system of generators of Tor _HF[−]_ ( _−Y_ ). 

A main problem immediately arises: since _−Y_ has indefinite graph, while the manifold we use in the initial step has negative-definite graph, this means that at some point in the argument we may be forced to consider an intermediate case where the manifold is not a rational homology sphere. The full path algorithm works also in this case, with the due modifications, as showed by Rustamov [49, Theorem 1.2]. 

We devote this subsection to describe the maps involved in the exact triangle in Equation (2.5). We recall that each map is induced by a 4-dimensional cobordism _W_ between two vertices of the triangle, and it is given by summing the maps induced in Heegaard Floer homology by each pair ( _W,_ v) with v _∈_ Spin _[c]_ ( _W_ ); Ozsváth and Szabó showed that such maps are all vanishing except for a finite number of v’s. 

14 

Let Γ _[∗]_ 0[be][the][graph][of] _[−][Y]_[0][,][and][Γ] _[∗]_ 1[be][the][one][of] _[−][Y]_[1][;][denote][by] _[P]_[0][and] _[P]_[1][the][corresponding] plumbings _P_ Γ _[∗]_ 0[and] _[ P]_[Γ] _[∗]_ 1[.][By construction the plumbing] _[ P]_[0][ is negative-definite and] _[ P]_[1][=] _[ P]_[0] _[∪][−][Y]_[0] _[W]_[,] where _W_ is the cobordism from _−Y_ 0 to _−Y_ 1 given by the 2-handle attachment on the central vertex. A Spin _[c]_ -structure on _W_ can then be determined by the first coordinate of a characteristic vector _V ∈ H_[2] ( _P_ 1; Z), and the components of _f_ are precisely the maps _FW,[◦]_ v1[:] _[HF][ ◦]_[(] _[−][Y]_[0] _[,]_[ s][0][)] _[→] HF[◦]_ ( _−Y_ 1 _,_ s1) where v1 _|−Y_ 0= s0 and v1 _|−Y_ 1= s1. In order to give a complete notation, for any u0 _∈_ Spin _[c]_ ( _P_ 0) such that u0 _|−Y_ 0= s0 the vector _V_ = ( _v_ 1 _, ..., v|_ Γ _∗_ 1 _[|]_[)][is][identified][with] _[c]_[1][(][u][1][)][where] u1 = u0 _∪−Y_ 0 _,_ s0 v1, while _V[′]_ = ( _v_ 2 _, ..., v|_ Γ _∗_ 1 _[|]_[)][is][identified][with] _[c]_[1][(][u][0][)] _[∈][H]_[2][(] _[P]_[0][;][ Z][)][.][Since] _[Y]_[0][is][an] _L_ -space, for every s0 _∈_ Spin _[c]_ ( _Y_ 0) there is an u0 as above such that _FP[◦]_ 0 _,_ u0[(1) =] _[ θ]_[s] 0[,][the][generator] of _HF[◦]_ ( _−Y_ 0 _,_ s0); hence, we have that 

**==> picture [188 x 14] intentionally omitted <==**

The cobordism between _−Y_ 1 and _−Y_ is instead given by a blow-up on the central vertex. Therefore, the map _g_ has two components that we denote by _gε_ with _ε_ = _±_ 1. Since we are using the inductive argument mentioned above, we can assume that Theorem 2.1 holds for _P_ 1, thus if _b_[+] 2[(] _[P]_[1][)][=][1][(resp.] _[b]_[+] 2[(] _[P]_[1][)][=][0][)][then][each][non-zero][class] _[γ][∈] HF_[�] ( _−Y_ 1 _,_ s1) with odd (resp. even) grading can be written as _F_[�] _P_ 1 _,_ u1(1) for a certain u1 _∈_ Spin _[c]_ ( _P_ 1). We conclude that 

**==> picture [244 x 17] intentionally omitted <==**

where v1 = u1 _|W_ and s0 = u1 _|−Y_ 0. Note that exactness implies that _gε_ ( _γ_ ) = 0 if _f_ v _i_ ( _θ_ s0) _̸_ = 0 only for an odd number of v _i ∈_ Spin _[c]_ ( _W_ ) for which _f_ v _i_ ( _θ_ s0) = _f_ v1( _θ_ s0). 

Finally, the map _h_ is gotten by adding a 0-framed 2-handle along the regular fibre of _−Y_ (a meridian of central vertex). We observe that then its dual _h[•]_ : _HF[⋆]_ ( _Y_ 0) _→ HF[⋆]_ ( _Y_ ) corresponds to attaching the 2-handle on the central vertex of _Y_ 0 (the symbol _⋆_ denotes the flavour dual to _◦_ ); in other words, the map _h[•]_ would play the same role as _f_ if we took the exact triangle with the oppositely oriented manifolds instead. For this reason we can just write 

**==> picture [182 x 15] intentionally omitted <==**

where _η_ s0 is the generator of _HF[⋆]_ ( _Y_ 0 _,_ s0), the Spin _[c]_ -structure v _∈_ Spin _[c]_ ( _W[′]_ ) is such that s0 = v _|Y_ 0, and s = v _|Y_ , while u = u0 _∪Y_ 0 _,_ s0 v. Note that one always has that _b_[+] 2[(] _[P]_[Γ][) = 0][.] 

2.2. **Heegaard Floer homology and plumbings of star-shaped graphs.** Let us use the notation ( _Z,_ s) for a Seifert fibred space with _b_ 1( _Z_ ) = 1. We recall that since _H_[2] ( _Z_ ; Z) _≃_ Z _⊕_ G where G is a finite abelian group, we have infinitely many Spin _[c]_ -structures: we denote by t the _|_ G _|_ ones with torsion first Chern class, and with j the other ones which are indexed by _{i} ×_ G with _i ∈_ Z _\ {_ 0 _}_ . 

Taking a look at its Heegaard Floer homology [41], since _b_ 1( _Z_ ) = 1 we have that _HF[−]_ ( _Z,_ t) has rank two as an F[ _U_ ]-module; therefore, we have two correction terms that we denote by _d_ od(t) and _d_ ev(t), similarly to the notation in [49], note that the difference _d_ od(t) _− d_ ev(t) is odd. In addition, the group _HF_[+] ( _Z,_ t) possesses two distinguished F[ _U_ ]-submodules isomorphic to _T_ := F[ _U, U[−]_[1] ] _/U ·_ F[ _U_ ] with degree given by the correction terms. 

On the other hand, for non-torsion Spin _[c]_ -structures we need to be careful as the version of _HF[−]_ considered here and in [49] is not the original one defined by Ozsváth and Szabó: we set 

**==> picture [130 x 14] intentionally omitted <==**

identifying it with its completion as an F[[ _U_ ]]-module. In this way, we have that 

**==> picture [166 x 13] intentionally omitted <==**

and _HF[−]_ ( _Z,_ j) has only _U_ -torsion elements. For these Spin _[c]_ -structures we cannot define the Maslov grading as an absolute Z-grading, but just as an F-grading. 

15 

ev If t is torsion then we say that a homology class is in _HF_[�] ( _Z,_ t) when its grading has the same parity of _d_ ev(t). This means that the image under _ψ∗_ of generators of distinct F[ _U_ ]-towers always live in subgroups that have opposite parity. 

**Proposition 2.2** _Suppose that Y and Z are closed oriented_ 3 _-manifolds such that b_ 1( _Y_ ) = 0 _and b_ 1( _Z_ ) = 1 _. Then_ 

**==> picture [310 x 17] intentionally omitted <==**

_for every_ s _∈_ Spin _[c]_ ( _Y_ ) _and every_ t _∈_ Spin _[c]_ ( _Z_ ) _torsion._ 

_Proof._ For _Y_ it follows by the canonical duality _HF_[�] _∗_ ( _−Y,_ s) _≃ HF_[�] _−∗_ ( _Y,_ s) _[•]_ which holds for every 3-manifold and preserves the parity of the Maslov grading. For _Z_ we need to observe that the correction terms of _−Z_ are _−d_ od(t) and _−d_ ev(t); since as in [49] we set _d_ od( _−Z,_ t) := _−d_ ev( _Z,_ t) and vice-versa, the parity of the homology classes is swapped under the duality identification. □ From now on we assume that _Z_ is a Seifert fibred space with _b_ 1( _Z_ ) = 1; we exclude _S_[1] _× S_[2] as this case is not relevant in the paper. From [49, Theorem 1.2] we know that the full path ev algorithm provides bases of _HF_[�] ( _Z,_ s) and the even subgroup of _HF −_ ( _Z,_ s). 

**Lemma 2.3** (Rustamov) _Let Z be as above, and denote by G its standard graph. Then for every_ s _∈_ Spin _[c]_ ( _Z_ ) _we have that there are_ u1 _, ...,_ u _t ∈_ Spin _[c]_ ( _PG_ ) _extending_ s _such that the maps FP[−] G,_ u _j_[:] _HF[−]_ ( _S_[3] ) _→ HF[−]_ ( _Z,_ s) _altogether give an_ F[ _U_ ] _-basis {FP[−] G,_ u1[(1)] _[, ..., F] P[ −] G,_ u _t_[(1)] _[}][of]_[Tor] _[HF][ −]_[(] _[Z,]_[ s][)] _when_ s _is non-torsion, and an_ F[ _U_ ] _-basis of_ F[ _U_ ] _d_ ev _⊕_ Tor _HF[−]_ ( _Z,_ s) _when_ s _is torsion._ 

We now need to prove an equivalent version of the lemma above in the case that Γ _[∗]_ is indefinite. 

**Lemma 2.4** _Let Y be a negative-definite Seifert fibred space, and denote by_ Γ _its standard graph. Then for every_ s _∈_ Spin _[c]_ ( _−Y_ ) _we have that there are_ u1 _, ...,_ u _t ∈_ Spin _[c]_ ( _P_ Γ _∗_ ) _extending_ s _such that the maps FP[−]_ Γ _∗ ,_ u _j_[:] _[HF][ −]_[(] _[S]_[3][)] _[→][HF][ −]_[(] _[−][Y,]_[ s][)] _[altogether][give][{][F][ −] P_ Γ _∗ ,_ u1[(1)] _[, ..., F] P[ −]_ Γ _∗ ,_ u _t_[(1)] _[}][,][an]_ F[ _U_ ] _-basis of_ Tor _HF[−]_ ( _−Y,_ s) _._ 

_Proof._ We assume that the framing on the central vertex of Γ _[∗]_ is negative (that is _e_ 0 _> −n_ ), otherwise _Y_ would be an _L_ -space and there is nothing to prove as Tor _HF[−]_ ( _−Y,_ s) _≃{_ 0 _}_ . We keep the notation of Subsection 2.1; hence, we set _P_ = _P_ Γ _∗_ (with _b_[+] 2[(] _[P]_[) = 1][) and] _[ ∂P]_[=] _[ −][Y]_[while] _∂P_ Γ = _Y_ (with _b_[+] 2[(] _[P]_[Γ][) = 0][).][We][can][use][the][minus][flavour][of][the][triangle.] 

We take the exact triangle in Equation (2.5). We take the map _h[•]_ : _HF_[+] ( _Y_ 0) _→ HF_[+] ( _Y_ ) defined by fixing Spin _[c]_ -structures u0 on _P_ Γ0 such that s0 = u0 _|Y_ 0 and by 

**==> picture [142 x 35] intentionally omitted <==**

Since _b_[+] 2[(] _[P]_[Γ][) = 0][ the map] _[ F][P]_ Γ _[,]_[u][ is non-zero in] _[ HF][ ∞]_[[38], then the commutativity of the cobordism] maps implies _FP_[+] Γ _,_ u[(1) =] _[ π][∗]_[(] _[F] P[ ∞]_ Γ _,_ u[(1))][where] _[π][∗]_[:] _[ HF][ ∞][→][HF]_[ +][.][This][means][that][Im] _[ F]_[ +] _P_ Γ _,_ u[is][the] subgroup _T_[+] of _HF_[+] ( _Y_ ); therefore, by duality we obtain that 

**==> picture [252 x 14] intentionally omitted <==**

To find a system of generators of Tor _HF[−]_ ( _−Y_ ), and extract a basis from it, we proceed as follows. Since the components of _g_ lie in different Spin _[c]_ -structures, it follows easily that we can find u _[′]_ 1 _[, ...,]_[ u] _t[′][∈]_[Spin] _[c]_[(] _[P]_[)][extending][s][such][that][the][set] _[{][F][ −] P,_ u _[′] i_[(1) =] _[ g][ε]_[(] _[F] P[ −]_ 1 _,_ u _[′] i[|][P]_ 1[(1))] _[}]_[1][⩽] _[i]_[⩽] _[t]_[,][where] _[ε]_ denotes the restriction of u _[′] i_[to the cobordism induced by the blow-up, is a system of generators of] Tor _HF[−]_ ( _−Y,_ s) as an F[ _U_ ]-module. From standard algebra we know that we can extract a basis from it. □ 

16 

As we mentioned in the previous subsections, if _Y_ is negative-definite then one of the results coming from Ozsváth-Szabó’s full path algorithm is that there is a basis of _HF_[�] ev( _Y,_ s) which consists of homology classes of the form _F_[�] _P_ Γ _,_ u(1) with u _∈_ Spin _[c]_ ( _P_ Γ). We can now show an equivalent version for _−Y_ ; for _Z_ this follows in the same way using the results in [49]. 

**Corollary 2.5** _Suppose that M is a Seifert fibred space. If b_ 1( _M_ ) = 1 _then there is a basis of_ � ev � _c HF_ ( _M,_ s) _which consists of homology classes of the form FPG,_ u(1) _with_ u _∈_ Spin ( _PG_ ) _._ 

od _Furthermore, if M is indefinite then there is a basis of HF_[�] ( _M,_ s) _which consists of homology classes of the form F_[�] _PG,_ u(1) _with_ u _∈_ Spin _[c]_ ( _PG_ ) _._ 

_Proof._ From the commutativity of the cobordism maps we have that _F_[�] = _ψ∗ ◦ F[−]_ , thus implying that if _F_[�] _PG,_ u(1) is non-zero then _FP[−] G,_ u[(1)][ is also non-zero.][When] _[ M]_[is indefinite the claim follows] from [39], Proposition 2.2, and Lemma 2.4 and its proof. □ 

In general, when the manifold is not a rational homology sphere we cannot determine a priori whether _d_ ev( _Z,_ t) is the maximal or the minimal between the two correction terms. However, if we apply the same results to ( _−Z,_ t), then by duality _d_ od( _Z,_ t) = _−d_ ev( _−Z,_ t); hence, the full path allows us to find both correction terms combinatorially. 

2.3. **The full path of any standard graph.** In this section we consider a star-shaped graph _G_ whose central vertex _S_ 1 has negative framing _m_ (1), and each other vertex _Si_ has framing _m_ ( _i_ ) ⩽ _−_ 2 for 1 ⩽ _i_ ⩽ _|G|_ . We denote by _Q_ the intersection matrix of the graph, so that _m_ (1) _, ..., m_ ( _|G|_ ) are the element on the main diagonal of _Q_ . 

Following the methods in [39, Section 2] and the notation in [8, Section 2], we fix a Spin _[c]_ - structure s on the 3-manifold presented by _G_ , and we introduce the set Z[⩾][0] _×_ Char( _G,_ s) where we identify a characteristic vector _V_ with _c_ 1(u) _∈ H_[2] ( _PG_ ; Z) for every Spin _[c]_ -structure u extending s on the plumbing _PG_ . We recall that _V_ = ( _v_ 1 _, ..., v|G|_ ) is characteristic when _vi ≡ m_ ( _i_ ) mod 2 for 1 ⩽ _i_ ⩽ _|G|_ . We denote each pair ( _k, V_ ) by _U[k] · V_ to highlight the relation with Heegaard Floer homology. 

Ozsváth and Szabó define the following equivalence relation on the set Z[⩾][0] _×_ Char( _G,_ s). Whenever the equality _vi_ = _−m_ ( _i_ ) + 2 _n_ holds for some integers _i_ and _n_ we have that 

**==> picture [198 x 14] intentionally omitted <==**

while 

**==> picture [200 x 14] intentionally omitted <==**

for every _k_ ⩾ 0. 

**Definition 2.6** _The equivalence classes of ∼ are the full paths, and we denote them by_ [ _V_ ] _where V_ = ( _v_ 1 _, ..., v|G|_ ) _is a characteristic vector. Let Bn be the subset of characteristic vectors such that |vi|_ ⩽ _−m_ ( _i_ ) + 2 _n for every_ 1 ⩽ _i_ ⩽ _|G|; if V ∈B_ 0 _then we say that_ [ _V_ ] ends correctly _if any other Z ∈_ [ _V_ ] _is also in B_ 0 _. Furthermore, the vector V is called_ initial _when_ 

**==> picture [116 x 12] intentionally omitted <==**

_while it is called_ terminal _when_ 

**==> picture [110 x 12] intentionally omitted <==**

_for i_ = 1 _, ..., |G|, see_ [39, 8] _._ 

It is proved in [39, Proposition 3.2] that if _Q_ is negative-definite then the full paths ending correctly have unique initial and terminal characteristic vectors; moreover, as we mentioned in ev the previous subsections their number equals the dimension of _HF_[�] . Regarding the uniqueness, the proof in [39] holds in the same way when _Q_ is indefinite; this is no longer true if det( _Q_ ) = 0: 

17 

in this case a full path that ends correctly may have loops in it, see [49, Section 3] for some examples. Note that, when this happens, every vector _Z_ in [ _V_ ] possesses coordinates _wi_ and _wj_ that are equal to _m_ ( _i_ ) and _−m_ ( _j_ ). 

We now define the space H[+] ( _G,_ s). Given a function _ϕ_ : Char( _G,_ s) _→T_ 0[+] with finite support, there is an induced map 

**==> picture [334 x 15] intentionally omitted <==**

then we set H[+] ( _G,_ s) to be the set of functions _ϕ_ whose induced map _ϕ_[�] is constant among each full path. Clearly, the space H[+] ( _G,_ s) inherits the structure of an infinitely generated F[ _U_ ]-module, or is zero in the case every full path is unbounded and then no non-zero _ϕ_ has finite support. 

**Lemma 2.7** _There is an identification between the subspace_ Ker _U[n]_[+1] _⊂_ H[+] ( _G,_ s) _for every n_ ⩾ 0 _and the space Kn of the maps from_ Z[⩾][0] _×_ Char( _G,_ s) _/ ∼ to_ F _which vanish on the full paths containing a representative of the form U[k] · V with k > n._ 

_Proof._ The proof follows the one of the second part of [39, Lemma 2.3]. The homomorphism Ker _U[n]_[+1] _→Kn_ is induced by the duality map 

**==> picture [180 x 40] intentionally omitted <==**

where ( _·_ )0 denotes the component of _T_ 0[+][in degree zero.][This map is injective, because if] _[ U][ k][·][ϕ]_[(] _[V]_[ )] _[∈][/]_ Ker _U ⊂T_ 0[+] and _U[n]_[+1] _· ϕ_ ( _V_ ) = 0 for any _k_ ⩽ _n_ and _V ∈_ Char( _G,_ s), then _ϕ_ ( _V_ ) has at the same time degree at least 2( _n_ + 1) and at most 2 _n_ ; thus _ϕ_ is zero. The map is also surjective, because for each _τ ∈Kn_ we can define 

**==> picture [172 x 32] intentionally omitted <==**

Clearly, we have that _ϕ ∈_ H[+] ( _G,_ s) and _U[n]_[+1] _· ϕ_ = 0. □ 

We define a map _T_[+] inducing an F[ _U_ ]-equivariant Spin _[c]_ -preserving map from an appropriate subspace of _HF_[+] to 

**==> picture [146 x 27] intentionally omitted <==**

Let _M_ be any Seifert fibred space whose standard graph _G_ has _e_ 0 ⩽ _−_ 1: we define _Z ⊂ HF[−]_ ( _M_ ) to be equal to Im _g_ as in the exact triangle in Subsection 2.1. 

When _G_ is negative-definite the map _g_ is surjective [39]. When _G_ is indefinite then _Z_ consists of the classes with odd degree; in other words, the ones that generate Tor _HF[−]_ ( _M_ ) because of Lemma 2.4. Finally, when _b_ 1( _M_ ) = 1 the subspace _Z_ is spanned by the torsion and the F[ _U_ ]- towers whose degrees have even parity, see Lemma 2.3. 

We set _T_[+] : _Z[•] →_ H[+] ( _G_ ) as follows: the plumbing _PG_ , turned upside-down, can be viewed as giving a cobordism from _−M_ to _S_[3] ; now fix _α ∈Z[•]_ the subgroup such that _Z[•] ⊕Z[⊥]_ = _HF_[+] ( _−M_ ) determined by the parity of the Maslov grading, and let 

**==> picture [120 x 14] intentionally omitted <==**

be the map given by 

**==> picture [200 x 17] intentionally omitted <==**

where u _∈_ Spin _[c]_ ( _PG_ ) is the Spin _[c]_ -structure whose first Chern class is _V_ . The fact that _T_[+] is welldefined, equivariant and Spin _[c]_ -preserving follows from Lemmate 2.3 and 2.4 and the properties 

18 

of the maps induced by cobordisms, see [45, Theorem 7.1], while that it is constant among full paths from [42, Theorem 3.1]. In addition, it is also easy to check that if _U[n]_[+1] _· α_ = 0 then 

**==> picture [155 x 21] intentionally omitted <==**

is in _Kn_ for _n_ ⩾ 0. 

Note that when _G_ is negative-definite then _Z[•]_ is the whole _HF_[+] ( _−M_ ). This is the case studied by Ozsváth and Szabó in [39] and by Némethi in [34]. We prove that _T_[+] is an isomorphism; note that when _b_ 1( _M_ ) = 1 we have the same result from [49, Theorem 1.2]. 

**Proposition 2.8** (Rustamov) _Suppose that Z is a Seifert fibred space such that b_ 1( _Z_ ) = 1 _, and let G be its standard graph. Then T_[+] : _Z[•] →_ H[+] ( _G_ ) _is a_ Spin _[c] -preserving isomorphism of_ F[ _U_ ] _-modules, where here Z[•] is the odd subgroup of HF_[+] ( _−Z_ ) _._ 

We are now ready to prove the relation between the full path and the Heegaard Floer homology groups of Seifert fibred spaces stated in Theorem 2.1. 

_Proof of Theorem 2.1._ We are going to prove that _HF_ red( _Y_ ) _≃_ H[+] (Γ _[∗]_ ) where _Y_ is the negativedefinite Seifert fibred space represented by Γ. Note that because of Equation (2.3) we know that _Td_[+] ( _Y,_ s)[contains][precisely][all][the][classes][with][even][parity][of] _[HF]_[ +][(] _[Y,]_[ s][)][;][hence,][for][these][manifolds] we can identify the quotient _HF_ red with the subgroup of the classes in _HF_[+] with odd parity. Theorem 2.1 will then follow by duality, Lemma 2.4 and Corollary 2.5. 

We prove that _T_[+] : _Z[•]_ = _HF_ red( _Y_ ) _→_ H[+] (Γ _[∗]_ ) is an isomorphism. We use the same notation as in Subsection 2.1; hence, we call _Y_ 1 the manifold obtained by lowering the central vertex of _G_ by one, and _Y_ 0 the one by removing it. The manifold _Y_ 0 has negative-definite standard graph. We have the following commutative diagram with exact lines, 

**==> picture [240 x 56] intentionally omitted <==**

where the first line comes from Lemma 2.4, while the second one is purely combinatorial and follows from [39, Lemma 2.10]. We recall that _T_ 1[+][and] _[T]_[ +] 0[are][isomorphisms][by][induction.][Note] that since _e_ ( _−Y_ ) _>_ 0, lowering the framing on the central vertex may yield a manifold _−Y_ 1 with _b_ 1( _Y_ 1) = 1. 

We prove that _T_[+] is injective: suppose that _α ∈ HF_ red( _Y_ ) is such that _T_[+] ( _α_ ) = 0, thus _T_[+][=][0][;][this][implies] _[g][•]_[(] _[α]_[)][=][0][and][then] _[α]_[=][0][,][because] _[T]_[ +][an][isomorphism][and] _[g][•]_[is] 1[(] _[g][•]_[(] _[α]_[))] 1[is] injective. We prove that _T_[+] is surjective: take _ϕ ∈_ H[+] ( _G_ ), thus F[+] (G[+] ( _ϕ_ )) = 0; hence, there exists a class _β ∈ HF_[+] ( _−Z_ 1) such that _T_ 1[+][(] _[β]_[)][=][G][+][(] _[ϕ]_[)][and] _[f][•]_[(] _[β]_[)][=][0][.][By][exactness][we][find][a] class _α ∈Z[•]_ such that _g[•]_ ( _α_ ) = _β_ , and then by commutativity we have 

**==> picture [214 x 13] intentionally omitted <==**

we conclude that _T_[+] ( _α_ ) = _ϕ_ using the injectivity of G[+] . 

From Lemma 2.7 the subgroup Ker _U ∩ HF_ red( _Y,_ s) coincides with the space _K_ 0 of maps from Z[⩾][0] _×_ Char(Γ _[∗] ,_ s) _/ ∼_ to F which vanish on the full paths containing a representative of the form od _U[k] · V_ with _k_ ⩾ 1. In addition, by duality we have an identification between _HF_[�] ( _−Y_ ) and the full paths of Γ _[∗]_ which end correctly. □ 

We conclude this section by completing the proof of Theorem 1.1, our first main result in the introduction. All the claims are already proven in Theorem 2.1, we just need to show that the conjugation involution _J_ commutes with the isomorphism _T_[+] . 

19 

_Proof of Theorem 1.1._ As we mentioned above the claim and the first two items follow from Theorem 2.1. The fact that _J_ coincides with the reflection [ _V_ ] _�→_ [ _−V_ ], on the set of the full paths for every standard graph _G_ , can be observed for any manifold _M_ , presented by a star-shaped graph with negative framings, from the commutativity of the cobordism maps under _J_ [19]; in fact, set [ _V_ ] = _c_ 1(u) then we have that _J_ [ _V_ ] = _J · FP[−] G,_ u[(1)][=] _[F] P[ −] G,−_ u[(1)][=][[] _[−][V]_[ ]][.][In][addition,][if] _α ∈ HF[−]_ ( _M,_ s) is not represented by a full path then by our results in this section it belongs to the canonical F[ _U_ ]-tower whose parity is either even (when _b_ 1( _M_ ) = 0) or odd (when _b_ 1( _M_ ) = 1); hence, both the involutions are the identity on this subgroup because they preserve the Maslov grading. □ 

## 3. Invariants from the standard graph 

3.1. **Gradings.** The set of the characteristic vectors of a plumbing tree _G_ , that here we assume to be either negative-definite or indefinite, corresponds to Spin _[c]_ ( _PG_ ). Therefore, each vector induce a Spin _[c]_ -structure on the manifold _YG_ = _∂PG_ . Using linear algebra, we describe an easy criterion to determine when the latter structure is induced by different vectors. 

**Proposition 3.1** _Suppose that G is a plumbing tree such that b_ 1( _YG_ ) = 0 _, and let QG be its intersection matrix. Two characteristic vectors V, W ∈ H_[2] ( _PG_ ; Z) _extends the same_ Spin _[c] -structure on YG if and only if Q[−] G_[1][(] _[V][−][W]_[)] _[ ∈]_[2][Z] _[|][G][|][.][Furthermore,][the][vector][V][extends][a][spin][structure][if] and only if Q[−] G_[1] _[V][∈]_[Z] _[|][G][|][.]_ 

_Proof._ As explained in [39], the vectors _V_ and _W_ correspond to _c_ 1(u1) and _c_ 1(u2) where u _i ∈_ Spin _[c]_ ( _PG_ ). The matrix _QG_ is the intersection form of _PG_ , which is simply connected; therefore, the Spin _[c]_ -structure on the boundary is the same if and only if the Chern classes are in the same equivalence class of _H_[2] ( _PG_ ; Z) _/_ 2 _QG · H_[2] ( _PG_ ; Z), which means precisely that the vector _V − W_ is in the image of 2 _QG_ over the integers. 

We have that s _∈_ Spin _[c]_ ( _YG_ ) is spin if and only if s = s; hence, in terms of vectors if and only if _V_ and _−V_ restrict to the same structure on _YG_ . Using the previous part of the statement, we then have that _V_ extends a spin structure if and only if _Q[−] G_[1][(] _[V][−]_[(] _[−][V]_[ ))] _[∈]_[2][Z] _[|][G][|]_[which][implies] the claim. □ 

We now consider the standard graph Γ of a negative-definite Seifert fibred space _Y_ . We know from [39, 34] that each characteristic vector _W_ whose full path ends correctly has a well-defined _[Q][−]_[1] _[W]_[+] _[|]_[Γ] _[|]_ grading _M_ ( _W_ ) = _[W][ T]_ 4 , which coincides with the Maslov grading. From Theorem 2.1 we know that if _V_ = _c_ 1(u) _∈ H_[2] ( _P_ Γ _∗_ ; Z) ends correctly then _F_[�] _P_ Γ _∗ ,_ u(1) _∈ HF_[�] ( _−Y_ ) can be identified with its full path [ _V_ ] through the isomorphism 

**==> picture [232 x 17] intentionally omitted <==**

since _b_[+][we][can][define][the][Maslov][grading][of] _[V]_[as] 2[(] _[P]_[Γ] _[∗]_[) = 1] 

**==> picture [357 x 25] intentionally omitted <==**

using Equation (2.4). It is easy to check that, with this definition in place, the isomorphism _T_[+] used in the proof of Theorem 2.1 is degree-preserving; in particular, if _V_ 1 _, V_ 2 _∈_ Char(Γ _[∗] ,_ s) end correctly then _M_ ( _V_ 1) _− M_ ( _V_ 2) is even. 

Let us consider the knot _K ⊂ Y_ isotopic to a regular fibre of the Seifert fibration. As in [8, Sections 2 and 3] we have that _K_ is presented as an unmarked leaf of Γ, attached to the central od vertex. The knot _K_ allows us to define the Alexander filtration on _HF_[�] ( _−Y_ ), in the same way 

20 

ev as we did in [8] for _HF_[�] ( _Y_ ): 

**==> picture [353 x 28] intentionally omitted <==**

for every characteristic vector _V ∈_ Char(Γ _[∗]_ ), where _D ⊂ P_ Γ _∗_ is the disk bounded by _K_ . We recall that we are indexing the central vertex as _S_ 1; moreover, if _V_ 1 _, V_ 2 _∈_ Char(Γ _[∗] ,_ s) end correctly then _F_ ( _V_ 1) _−F_ ( _V_ 2) is an integer: 

**==> picture [208 x 25] intentionally omitted <==**

where _B_ = ( _b_ 1 _, ..., b_ Γ _∗_ ) = _Q[−] ∗_[1] � _V_ 1 _−_ 2 _V_ 2 � from Proposition 3.1. 

**Remark 3.2** _We proved in_ [8, Lemma 2.4] _that if W_ 1 _, W_ 2 _∈_ Char(Γ _,_ s) _end correctly and F_ ( _W_ 1) = _F_ ( _W_ 2) _then they are in the same full path. The same proof works also for −Y : if V_ 1 _, V_ 2 _∈_ Char(Γ _[∗] ,_ s) _end correctly and F_ ( _V_ 1) = _F_ ( _V_ 2) _then they are in the same full path. Say {_ [ _V_ 1] _, ...,_ [ _Vt_ ] _}_ od _is the basis of HF_[�] ( _−Y,_ s) _given by the full paths ending correctly, this means that there are intervals_ [ _aVi, bVi_ ] _⊂_ Q _such that bVi < aVi_ +1 _for i_ = 1 _, ..., t, and the i-th interval contains only the values of F taken by the vectors in the full path_ [ _Vi_ ] _._ 

From what we said in Section 2 we have a basis _{_ [ _W_ 1] _, ...,_ [ _Wt_ +1] _, T_ [ _V_ 1] _, ..., T_ [ _Vt_ ] _}_ of _HF_[�] ( _Y,_ s); the first part is given by the full paths _{_ [ _W_ 1] _, ...,_ [ _Wt_ +1] _}_ that end correctly, which is a basis of _HF_ � ev( _Y,_ s) from [39, 34], while the second part is given by _HF_ � od( _Y,_ s) _≃ HF_ � ev( _−Y,_ s) _⊥_ , because od _{_ [ _V_ 1] _, ...,_ [ _Vt_ ] _}_ is a basis of _HF_[�] ( _−Y,_ s) by Theorem 2.1 and Corollary 2.5. ev In [8, Section 2] we defined the filtration _F_ on _HF_[�] ( _Y,_ s), while Equation (3.2) does the same od � od � for _HF_[�] ( _−Y,_ s). We can extend _F_ on _HF_ ( _Y,_ s), and then on the whole _HF_ ( _Y,_ s), in the same way as the Alexander filtration in knot Floer homology, see [40]; this means the subspace of the functionals _T_ [ _V_ ] such that _F_ ( _T_ [ _V_ ]) ⩽ _m_ is the orthogonal of the one of the vectors _V_ such that _F_ ( _V_ ) ⩽ _−m −_ 1. Explicitly, we write 

**==> picture [330 x 28] intentionally omitted <==**

3.2. **Tau-invariants.** Let _Fm[K]_[be][the][level] _[m]_[of][the][filtration][on] _CF_[�] ( _M_ ) induced by the regular fibre _K ⊂ M_ , that is the leaf attached to the first vertex of its standard graph. Then for _γ ∈ HF_[�] ( _M_ ) non-zero the invariant _τγ_ ( _K_ ) is defined as the minimal _m_ such that _Fm[K]_[contains][a] cycle representing _γ_ , see [45, 2]. 

In [1], and more explicitly in [8, Equation (3.1)] is showed how to compute the _τ_ -invariant of _K_ in an almost-rational graph _Y_ , with respect to a homology class represented by a full path [ _W_ ] that ends correctly: 

**==> picture [341 x 27] intentionally omitted <==**

Here, we prove that the same formula holds also for any star-shaped graph whose corresponding 3-manifold is a rational homology sphere. In the proof we use some terminology from the lattice cohomology setting, but in this paper we do not introduce this object explicitly. We refer to the existing literature [34, 36, 5, 55, 1] for details. 

**Theorem 3.3** _Suppose that_ Γ _is the negative-definite standard graph of a Seifert fibred space Y , and let γ ∈ HF_[�] _∗_ ( _−Y,_ s) _be a non-zero homogeneous class. Then_ 

**==> picture [310 x 27] intentionally omitted <==**

21 

_where γ_ = [ _V_ 1] + _· · ·_ + [ _Vk_ ] _for some Vi ∈_ Char(Γ _[∗]_ ) _initial such that_ [ _Vi_ ] _ends correctly, and F_ ( _V_ 1) _< · · · < F_ ( _Vk_ ) _._ 

_Proof._ In [5] Borodzik, Liu and Zemke prove that there is an isomorphism between the full completed versions of the link Floer and the lattice cohomology chain complex of a link given by attaching leaves to a plumbing tree, with the assumption that the latter one represents a rational homology sphere. 

In our setting, where we are interested in the regular fibre _K_ of Γ _[∗]_ , we just consider the knot case; hence, we refer to [5, Theorem 5.1] which gives an isomorphism _CFK_ ( _−Y, K_ ) _≃_ CFL(Γ _[∗] , S_ 0) of _A∞_ -modules over the ring F[ _U, V_ ], where _S_ 0 denotes the leaf attached to the centre and CFL(Γ _[∗] , S_ 0) is the generalised knot lattice complex. As explained in [5, Lemma 5.9] this isomorphism respects both the Maslov and the Alexander grading; in particular, the gradings gr _w_ and _A_ in [5] corresponds precisely to our definition of _M_ and _F_ for any _V ∈_ Char(Γ _[∗]_ ). For more details about the algebraic setting we refer to [5]. 

It is important to observe that the isomorphism in [5, Theorem 5.1] requires the full version of the surgery formula in Heegaard Floer, see [55]; nonetheless, it restricts to the characteristic vectors of Γ _[∗]_ , which are the generators in cube grading zero of the complex [36]. It is possible to check directly, see [36, Lemma 3.1], that if _V_ 1 and _V_ 2 are related by a step in the full path then their sum is in fact in the image of the differential. Since we now know from Theorem 1.1 that any _γ_ as in the statement can be identified with a linear combination of full paths (ending correctly), we can compute the invariant _τγ_ ( _K_ ) using the isomorphism in [5]: 

**==> picture [334 x 45] intentionally omitted <==**

because _Vk_ is initial, and _F_ increases along the full paths; note that the cycles whose homology class is _γ_ are precisely linear combinations of characteristic vectors in the [ _Vi_ ]’s, see [36, 55]. We conclude by observing that _e_ (1 _Y_ )[=] _[ −] e_ ( _−_ 1 _Y_ )[=] _[ −][e]_ 1 _[T][Q] ∗[−]_[1] _[e]_[1][.] □ 

We now prove Theorem 1.2 by showing that there is a combinatorial formula for any non-zero homogeneous homology class in _HF_[�] _∗_ ( _Y,_ s) when _Y_ has negative-definite standard graph. The formula depends on the parity of the Maslov grading of the class; hence, we need to distinguish ev od the case of _γ ∈ HF_[�] _∗_[(] _[Y,]_[ s][)][and] _[δ][∈] HF_[�] _∗_[(] _[Y,]_[ s][)][.] 

_Proof of Theorem 1.2._ The first case follows by Equation (3.4). For the second case, using the formula� in [2, Lemma 2.2] and Theorem 3.3, we can compute the invariant _τδ_ ( _K_ ) where _δ ∈ HF ∗_ ( _Y,_ s) is the class identified with _T_ [ _V_ 1] + _· · ·_ + _T_ [ _Vk_ ] and _F_ ( _V_ 1) _< · · · < F_ ( _VK_ ): 

**==> picture [396 x 62] intentionally omitted <==**

We can show that the Alexander filtration _F_ corresponds precisely to the filtration _F[K]_ in knot Floer homology. 

**Corollary 3.4** _For every integer m the subgroup of HF_[�] ( _Y_ ) _generated by the vectors_ [ _Wi_ ] _for i_ = 1 _, ..., t_ +1 _and the functionals T_ [ _Vj_ ] _for j_ = 1 _, ..., t such that F_ ( _·_ ) ⩽ _m coincides with the image of i∗_ : _H∗_ ( _Fm[K] CF_[�] ( _Y_ )) _→ HF_[�] ( _Y_ ) _, the m-level of the filtration induced by K._ 

22 

_Proof._ It follows by Theorem 3.3 and Equation (3.5) because now we can compute the _τ_ -invariant of _K_ with respect to every homogeneous class _α_ in _HF_[�] ( _Y_ ), and by definition _τα_ ( _K_ ) is the minimal _m_ such that _Fm[K] HF_[�] ( _Y_ ) contains _α_ . □ 

3.3. **The height function.** In [8, Definition 2.6] we introduced an invariant called the _height function_ of a full path [ _W_ ] which ends correctly as _−e[T]_ 1 _[Q][−] G_[1] _W_ +2 _W[′]_ , where _W_ and _W[′]_ are the initial vectors of [ _W_ ] and [ _−W_ ] respectively; moreover, from [8, Subsection 2.2] the height of [ _W_ ] also coincides with the number of central steps, that are steps in a full path taken when _w_ 1 = _−m_ (1) among the full path. We now proceed to define a general version of this invariant. 

**Definition 3.5** _Assume M is a Seifert fibred space with b_ 1( _M_ ) = 0 _. Let γ ∈ HF_[�] ( _M,_ s) _be a homology class which can be written as a linear combination of full paths_ [ _Z_ 1] _, ...,_ [ _Zk_ ] _ending correctly, and let the Zi’s be the initial vectors. Then the height of γ is_ 

**==> picture [194 x 20] intentionally omitted <==**

_that is the difference between the maximal and the minimal value of the Alexander filtration, induced by the leaf K, on all the full paths which are components of γ._ 

_In other words, if Z_ 1 _[′][, ..., Z] k[′][are][the][initial][vectors][of]_[[] _[−][Z]_[1][]] _[, ...,]_[ [] _[−][Z][k]_[]] _[while][the][Z][i][’s][are][ordered] in the way that F_ ( _Z_ 1) _< · · · < F_ ( _Zk_ ) _, then_ 

**==> picture [268 x 27] intentionally omitted <==**

Note that the initial vector _V[′]_ of the full path [ _−V_ ] is equal to _−V_ , where _V_ is the terminal vector of [ _V_ ]. Let us consider _Z_ 1 and _−Zk[′]_[=] _Zk_ ; since they restrict to the same Spin _[c]_ -structure on _M_ , we know from Proposition 3.1 that there exists an integral vector _B_ such that 2 _QGB_ = _Z_ 1+ _Zk[′]_[;] therefore, we have the following corollary. 

**Corollary 3.6** _The height of γ can be expressed without involving the Alexander filtration as_ height _F_ ( _γ_ ) = _|b_ 1 _|, where B_ = ( _b_ 1 _, ..., b|G|_ ) _is the vector defined above._ 

_Proof._ We have that 

**==> picture [353 x 40] intentionally omitted <==**

and this number is non-negative by definition. 

3.4. **Blowing down the graph.** When Γ is negative-definite there is a unique way to blowdown the graph. This is no longer true for Γ _[∗]_ , but in this paper we will often consider a special 4-manifold _X_ obtained in such a way. We recall that if _e_ 0 ⩾ 0 then the corresponding Seifert fibred manifold is an _L_ -space. 

**Lemma 3.7** _Suppose that_ Γ _is the negative-definite standard graph of a Seifert fibred space, and every maximal S_[3] _-subgraph_ (Γ _[∗]_ ) _[′] represents the fibration of Td_ 2 _,d_ 1 _for_ 1 ⩽ _d_ 2 ⩽ _d_ 1 _fixed coprime integers. Then there is a canonical way to blow-down_ Γ _[∗] completely so that_ (Γ _[∗]_ ) _[′] disappears; furthermore, the resulting_ 4 _-manifold X_ Γ _∗ satisfies b_[+] 2[(] _[X]_[Γ] _[∗]_[) = 1] _[.]_ 

_Proof._ The framings on each leg of Γ _[∗]_ are given by the continued fraction expansion of _ri_ , which means that they are all not bigger than _−_ 2. If _e_ 0 _< −_ 1 then the maximal _S_[3] -subgraph is empty, and there is nothing to prove, if _e_ 0 = _−_ 1 then we start precisely by blowing down the central vertex and we continue by always blowing down the _−_ 1-circle in the leg of (Γ _[∗]_ ) _[′]_ with the highest coefficient (at that step). This is possible because (Γ _[∗]_ ) _[′]_ represents a torus knot. 

As described in [8, Section 5] the manifold _X_ Γ _∗_ is obtained by attaching 2-handles on an appropriate cable of a torus link. Since we are always blowing down a circle with framing _−_ 1, we 

23 

have that _b_[+][preserved.][The][subgraph][(Γ] _[∗]_[)] _[′]_[is][negative-definite][thus] _[b]_[+][is][the][same][as] 2[is] 2[(] _[X]_[Γ] _[∗]_[)] the one of Γ _[∗]_ without the legs containing (Γ _[∗]_ ) _[′]_ . □ 

When a star-shaped graph _G_ is negative-definite the manifold _XG_ is a Stein domain, see [8, Section 5]. When _G_ is indefinite and it either contains the standard graph of _Td_ 2 _,−d_ 1 or _G[′]_ is not unique, we are going to show in Corollary 3.11 that _YG_ is an _L_ -space. 

**Remark 3.8** _It follows by a result of Lisca and Matić_ [28] _that if −Y , the Seifert fibred space whose standard graph is_ Γ _[∗] , is not an L-space then the manifold X_ Γ _∗ described by the procedure in Lemma 3.7 is obtained by attaching Stein_ 2 _-handles to D_[4] _._ 

Note that the converse of this remark does not hold: take the standard graph of _M_ ( _−_ 1;[2] 3 _[,]_[1] 2 _[,]_[1] 3[)] _[ ∼]_[=] _S−_[3] 9[(] _[T]_[2] _[,][−]_[3][)][,][we][have][that] _[X]_[Γ] _[∗]_[is][a][Stein][domain][even][though][this][3-manifold][is][an] _[L]_[-space.][How-] ever, all of its structures are zero-twisting and thus they do not concern the topic of this paper. 

**Remark 3.9** _By_ [30] _a Seifert fibred L-space whose standard graph has central vertex with framing e_ 0 ⩾ _−_ 1 _admits no negative-twisting structures._ 

Using the same notation in [8], we recall that given a plumbing tree _G_ the characteristic vector _V_ can = ( _m_ (1) + 2 _, ..., m_ ( _|G|_ ) + 2) _∈_ Char( _G_ ) is called _canonical vector_ . 

**Theorem 3.10** ( _L_ -space criterion) _A Seifert fibred space is an L-space if and only if when it is oriented in the way that its standard graph is indefinite, that is when e_ 0 ⩾ _−_ 1 _, the canonical vector V_ can _does not end correctly._ 

_Proof._ From Theorem 2.1 we know that a Seifert fibred space with indefinite standard graph Γ _[∗]_ is an _L_ -space if and only if Γ _[∗]_ has no characteristic vector whose full path ends correctly. Since _V_ can is the vector with minimal coordinates among the ones that initiate their full path, if there exists a _V ∈_ Char(Γ _[∗]_ ) whose full path ends correctly then the same necessarily holds for _V_ can too. □ 

The following result follows from [29, Theorem 1.3], but it can also be seen as a consequence of the _L_ -space criterion. 

**Corollary 3.11** _If the maximal S_[3] _-subgraph of G either corresponds to the fibration of a negativetorus knot or is not unique, then the underlying Seifert fibred space is an L-space._ 

_Proof._ It is easy to check that under the given assumptions _V_ can cannot end correctly; thus we just conclude by applying Theorem 3.10. □ 

We prove the following property of _V_ can which we are going to apply in Sections 4 and 7. 

**Lemma 3.12** _Suppose that Y is a Seifert fibred space with standard graph_ Γ _and b_ 1( _Y_ ) = 0 _. If_ Γ _is negative-definite then F_ ( _W_ can) _> F_ ( _W_ ) _for any initial W ∈_ Char(Γ) _different from W_ can _. Similarly, for its dual_ Γ _[∗] one has F_ ( _V_ can) _< F_ ( _V_ ) _for any V ∈_ Char(Γ _[∗]_ ) _with the same properties._ 

_Proof._ According to the definition of _F_ , we just have to prove that _e[T]_ 1 _[Q][−]_[1] _[W]_[can] _[>][e][T]_ 1 _[Q][−]_[1] _[W]_[and] _e[T]_ 1 _[Q] ∗[−]_[1] _[V]_[can] _[< e][T]_ 1 _[Q] ∗[−]_[1] _[V]_[ .][Consider][the][generic][intersection][matrix] 

**==> picture [80 x 27] intentionally omitted <==**

for any standard graph _G_ , where _A_ is the matrix made by the tridiagonal blocks _A_ 1 _, ..., An_ corresponding to the legs of _G_ , and **e** is the vector whose all entries are one. Since each _Ai_ is the intersection matrix of a chain of unknots, it is an irreducible negative-definite _M_ -matrix; hence, each _A[−]_[1][and][then] _[A][−]_[1][,][has][negative][entries.] _i_[,] 

Now take the Schur complement of _A_ expressed by ∆:= _e_ 0 _−_ **e** _[T] A[−]_[1] **e** : since det _QG_ = 0, one has ∆ = 0 and the block inverse formula gives _e[T]_ 1 _[Q][−] G_[1][=][∆] _[−]_[1][(1] _[,][−]_ **[e]** _[T][ A][−]_[1][)][.][Then][the][row][vector] 

24 

_−_ **e** _[T] A[−]_[1] has positive entries, thus every entry of _e[T]_ 1 _[Q][−] G_[1] has the same sign as ∆. By standard linear algebra, we have the congruence 

and then 

**==> picture [326 x 68] intentionally omitted <==**

This implies that 

_•_ if _G_ is negative-definite then ∆ _<_ 0, and then every entry of _e[T]_ 1 _[Q][−] G_[1][is][negative;] _•_ if _G_ is indefinite then ∆ _>_ 0, and then every entry of _e[T]_ 1 _[Q][−] G_[1][is][positive.] Now let _Z_ = ( _z_ 1 _, ..., z|G|_ ) be any initial characteristic vector in _G_ ; since _zi_ ⩾ _m_ ( _i_ ) + 2 for each _i_ , we have that _Z − Z_ can = 0 has non-negative coordinates. Therefore, we conclude that in the case of Γ one has _e[T]_ 1 _[Q][−]_[1][(] _[W][−][W]_[can][)] _[ <]_[ 0][,][while][in][the][case][of][Γ] _[∗]_[one][has] _[e][T]_ 1 _[Q] ∗[−]_[1][(] _[V][−][V]_[can][)] _[ >]_[ 0][.][This] proves the claim. □ 

## 4. The classification when _b_ 1 = 1 

Let _Z_ be a Seifert fibred space whose standard graph _G_ has at least three legs, and such that _b_ 1( _Z_ ) = 1; hence, we have _e_ ( _Z_ ) = _e_ 0 + _r_ 1 + _· · ·_ + _rn_ = 0. These manifolds are surface bundles, obtained by capping off a regular fibre in a Seifert fibred space by performing 0-surgery on it. We are going to classify all the negative-twisting structures on _Z_ . 

We recall that for torus bundles the classification follows by the results of Honda [27]; namely, there is a unique Stein fillable structure, together with infinitely many structures obtained by adding (non-vertical) Giroux torsion along the torus. These structures are weakly but not strongly fillable, see [12, Theorem 1]. 

**Theorem 4.1** _Let Z_ = _M_ ( _e_ 0; _r_ 1 _, . . . , rn_ ) _be a genus g >_ 1 _surface bundle obtained by_ 0 _-surgery on a Seifert fibred knot in a rational homology sphere. The negative-twisting tight contact structures on Z are precisely the Legendrian surgeries on all the Legendrian realisations of the blow-down of the standard graph; moreover, they are all Stein fillable and distinguished, up to isotopy, by their contact invariant c_[+] _in HF_[+] ( _−Z_ ) _._ 

We briefly describe why the 4-manifold _XG_ is a Stein domain; in particular, these manifolds always have at least one Stein fillable structure. We use Lemma 3.7 after we modify _G_ by lowering the framing on a vertex _Si_ outside of an _S_[3] -subgraph _G[′]_ (we have _n_ ⩾ 3); in this way, we obtain a negative-definite graph _G_[�] such that _X_ � _G_ is a Stein domain, which differs from _XG_ by having framing (say _k_ ) lowered by one on a single Legendrian knot _Ki ⊂_ ( _S_[3] _, ξ_ std). If either _Si_ can be chosen to be not connected to the centre of _G_ , or _G[′]_ represents _Td_ 2 _,d_ 1 with _d_ 2 _>_ 1, then _k <_ TB _ξ_ std( _Ki_ ) because either the knot type _Ki_ is an unknot, thus _k_ ⩽ _−_ 3, or _Ki_ is a positive torus knot, thus TB _ξ_ std( _Ki_ ) _>_ 0. In the remaining case when _G[′]_ represents _T_ 1 _,d_ 1, the framing on _Si_ should be low enough for this vertex not to be blown down together with _G[′]_ , see Figure 5 for an example. 

The above argument shows that when _e_ ( _Z_ ) = 0 (and _n_ ⩾ 3) the canonical vector _V_ can ends correctly. Therefore, the maximal _S_[3] -subgraph of _G_ is unique, because as said in Corollary 3.11 this would not be possible otherwise. 

We mentioned that a manifold _Z_ = _M_ ( _e_ 0; _r_ 1 _, ..., rn_ ) as above is a genus _g_ ⩾ 1 surface bundle when _n_ ⩾ 3. Let _Ki_ be a regular fibre of the Seifert fibration presented by any graph Γ _i_ , obtained by removing the _i_ -th leg from _G_ . It is a classical result [23, Subsection 2.1] that a surface bundle which is Seifert fibred over a sphere has fibre of genus _g_ = 1 if and only if its standard graph 

25 

**==> picture [170 x 64] intentionally omitted <==**

**----- Start of picture text -----**<br>
− 3 − 3<br>− 3 − 3<br>− 1 − 1<br>− 3 − 4<br>**----- End of picture text -----**<br>


Figure 5. The standard graph _G_ of _Z_ = _M_ ( _−_ 1;[1] 3 _[,]_[1] 3 _[,]_[1] 3[)][(left),][and][the][one][of] _[Y] G_[ �][=] _M_ ( _−_ 1;[1] 3 _[,]_[1] 3 _[,]_[1] 4[)][(right).][The][framing][on][the][lower][vertex][can][be][at][most] _[−]_[3][;][otherwise,] the vertex would be inside _G[′]_ . 

is one of the seven in Figure 6, and then the structures with Giroux torsion in [12, Theorem 1] appear only in these cases. 

We can show that _g_ is also determined combinatorially. Note that since _e_ ( _Z_ ) = _e_ 0+ _r_ 1+ _· · ·_ + _rn_ = 0, we have that _ri_ = _−e_ (Γ _i_ ) and Γ _i_ is negative-definite; therefore, the negative rational number _e_ (Γ1 _i_ )[coincides][with][[] _[D][i]_[]] _[ ·]_[ [] _[D][i]_[]][,][the][self-intersection][of][the][disk] _[D][i][⊂][P]_[Γ] _[i]_[whose][boundary][is] _[K][i]_[.] 

**Proposition 4.2** _Let_ Γ _be the negative-definite standard graph of a Seifert fibred space, and K be the regular fibre. Then we have that g_ 3( _Y_ Γ _, K_ ) = _τξ_ can( _K_ ) _where ξ_ can _is the contact structure on Y_ Γ _induced by the Milnor fibre. In particular, one has_ 

**==> picture [186 x 27] intentionally omitted <==**

_where Q_ Γ _is the intersection matrix of_ Γ _._ 

_Proof._ A result of Pichon and Seade [47, Theorem 4.1] says, in particular, that the link _KN_ given as _N_ leaves attached to the centre of Γ is fibred when _N_ is big enough; therefore, as _KN_ is a positive cable of the regular fibre _K_ = _K_ 1, we have that the latter knot is rationally fibred in _Y_ Γ. We know from [3, Theorem 5.1] that _K_ supports the same structure _ξ_ of _KN_ ; moreover, since _KN_ consists of parallel copies of _K_ , then _ξ_ is transverse to the Seifert fibration of _YG_ . From a result of Lisca and Matić [29, Corollary 2.2] we can argue that _ξ_ is fillable, and according to our classification [8, Theorem 1.1 and Proposition 5.2], that is actually Stein fillable and its contact invariant is _T_ [ _W_ ] _∈ HF_[�] ( _−Y_ Γ) for some initial _W ∈_ Char( _Y_ Γ) whose full path ends correctly. Consider _o_ the order of [ _K_ ] _∈ H_ 1( _Y_ Γ; Z), and _S_ a page of the corresponding open book. The value[1] _[−][χ]_[(] 2 _[S]_[)] _[/][o]_ is equal to the (rational) Seifert genus _g_ 3( _Y_ Γ _, K_ ), and this can be computed 

**==> picture [448 x 156] intentionally omitted <==**

**----- Start of picture text -----**<br>
− 2 − 2 − 2<br>− 2<br>− 2 − 2 − 2 − 2 − 2 − 2 − 2<br>− 2 − 2 − 2<br>− 2 − 2 − 2 − 2 − 2 − 2 − 2 − 2 − 2 − 2<br>− 3 − 2 − 2 − 2<br>− 2 − 2<br>− 3 − 4 − 3<br>− 1 − 1 − 1 − 2<br>− 3 − 4 − 6 − 2<br>**----- End of picture text -----**<br>


Figure 6. All the possible standard graphs corresponding to torus bundles over _S_[1] . 

26 

combining the definition of self-linking number (of a rationally null-homologous knot) with [7, Theorem 2.1], and using the relative Adjunction inequality[1] in [25]. In fact, we have 

**==> picture [318 x 13] intentionally omitted <==**

and SL _ξ_ ( _KN_ ) = _−χ_ ( _S_ ) by [2, Theorem 1.3] because pages of open books are homologically trivial symplectic surfaces (in any strong symplectic filling), forcing the inequalities to be sharp. More specifically, we can write _τξ_ ( _K_ ) =[1] _[−][χ]_[(] 2 _[S]_[)] _[/][o]_ = _g_ 3( _Y_ Γ _, K_ ) which can be determined using Alfieri’s formula for the _τ_ -invariant, that is _τξ_ ( _K_ ) =[1] 2[(] _−e_ 1(Γ)[+] _[ e]_ 1 _[T][Q][−]_ Γ[1] _[W]_[)][,][see][Equation][(3.4).] Since the rational Seifert genus is the maximal non-zero value for the Alexander filtration induced by _K_ , we have that _F_ ( _W_ ) should be maximal among initial vectors that end correctly. Using Lemma 3.12, we conclude that _W_ = _W_ can and then _ξ_ = _ξ_ can by [4, Corollary 5.5]. □ 

We can now give a condition that allows us to determine the genus _g_ of a fibre of any surface bundle _Z_ . We have that _g_ 3( _Y_ Γ _i, Ki_ ) is equal to 2[1] _[−][χ]_ 2[(][Σ] _o_[)][,][where] _[ o]_[is the][order of][[] _[K][i]_[]] _[ ∈][H]_[1][(] _[Y]_[Γ] _[i]_[;][ Z][)] and Σ is the rational Seifert surface which realises its Thurston norm, see [7] for more details. If Σ has genus _g_ then _χ_ (Σ) = 2 _−[o] b[−]_[2] _[g]_[,][where][we][set] _[−][e]_[(Γ] _[i]_[)][=] _[r][i]_[=] _a[b][∈]_[Q] _[>]_[0][and][then] _[o] b_[is] precisely _|_ Σ _|_ , and this happens if and only if any graph Γ _i_ satisfies 

**==> picture [315 x 24] intentionally omitted <==**

by Proposition 4.2. A posteriori the value of _g_ in this equation does not depend on the leg _i_ . 

4.1. **The Maslov grading: a special case.** In the previous section we computed the Maslov grading of a non-zero homology class [ _V_ ] _∈ HF[−]_ ( _M,_ s), represented by a characteristic vector, _[T][Q][−]_[1] _[V]_[+] _[|][G][|][−][ε]_ when _M_ is a Seifert fibred space with _b_ 1( _M_ ) = 0; namely, we have that _M_ ( _V_ ) = _[V]_ 4 where _ε_ is zero if _G_ is negative-definite, while it is 6 if _G_ is indefinite. 

We know from Heegaard Floer theory that the Maslov grading is a well-defined absolute Z- grading also when _b_ 1( _M_ ) = 1 and _c_ 1(s) is torsion. We show that there exists an analogous formula for _M_ also in this case. 

**Proposition 4.3** _Let_ ( _Z,_ t) _be a Seifert fibred space with b_ 1( _Z_ ) = 1 _and_ t _a torsion_ Spin _[c] -structure; moreover, take a V ∈_ Char( _G,_ t) _such that_ [ _V_ ] _∈ HF[−]_ ( _Z,_ t) _is non-zero. Then_ 

**==> picture [125 x 26] intentionally omitted <==**

_where B ∈_ Q _[|][G][|] is any vector such that QB_ = _V ._ 

_Proof._ The fact that at least one vector _B_ exists is equivalent to the fact that t is torsion; in fact, as a class in _H_ 1( _Z_ ; Q) one has that t is equivalent to a spin structure, and we conclude as in the proof of Proposition 3.1. It is also easy to check that if _B_ 1 and _B_ 2 are as in the statement then the expression for _M_ is well-defined: 

**==> picture [445 x 14] intentionally omitted <==**

because _B_ 1 _− B_ 2 _∈_ Ker _Q_ and _Q_ is symmetric. 

Using Equation (2.4) and Corollary 2.5, we only have to check that _c_[2] 1[(][u][)[] _[P][G]_[] =] _[ B][T][ QB]_[where] _V_ = _c_ 1(u). This follows from the standard fact that _c_[2] 1[(][u][)[] _[P][G]_[]][=] _[A][T][ QA]_[where] _[A]_[is][a][vector] that represents _c_ 1(u) in the basis _{S_ 1 _, ..., S|G|}_ of _H_ 2( _PG_ ; Z) given by the vertices; hence, we have that _A_ satisfies _QA_ = _V_ because _V_ represents the Chern class in the dual basis _{D_ 1 _, ..., D|G|}_ of _H_ 2( _PG, Z_ ; Z) given by the dual of the vertices. □ 

> 1Note that the authors in [25] use a different convention for the Alexander grading, resulting in the opposite sign before the last term of the inequality. 

27 

4.2. **The maximal twisting number.** We prove the equivalent of [8, Proposition 4.2], showing that only one negative twisting number of a tight structure exists on _Z_ unless it is a torus bundle. 

**Proposition 4.4** _If Z_ = _M_ ( _e_ 0; _r_ 1 _, . . . , rn_ ) _satisfies b_ 1( _Z_ ) = 1 _, then all the negative-twisting tight contact structures on Z without Giroux torsion have the same twisting number._ 

_Proof._ When _g_ = 1 the claim is obvious from Honda’s classification [27], because there is only one (Stein fillable) structure without Giroux torsion. Below we show that for _g >_ 1 there is a unique negative twisting number. 

We proceed as in the proof of [8, Proposition 4.2]. We know from Ghiggini-Massot’s algorithm that _−q < −_ 1 is a twisting number if and only if there exist positive integers _p_ 1 _, ..., pn_ such that _pqi_[is][the][best][upper][approximation][for] _[r][i]_[and] _[p]_[1][ +] _[ · · ·]_[ +] _[ p][n]_[=] _[ −][e]_[0] _[q]_[ +] _[ n][ −]_[2][.] 

Suppose first that _e_ 0 ⩽ _−_ 2, then _−_ 1 is a twisting number and we are proving that no other _−q_ can be. Since _[p] q[i] −[−]_ 1[1] _[<][p] q[i][<]_[ 1][,][we][have][that] _[p] q[i] −[−]_ 1[1][⩽] _[r][i][<][p] q[i]_[and][hence] 

**==> picture [320 x 25] intentionally omitted <==**

Since we have _e_ ( _Z_ ) = 0, the above inequalities can be fulfilled only for _e_ 0 = _−_ 2 and _ri_ = _[p] q[i] −[−]_ 1[1][;] as usual we write _ri_ = _a[b][i] i_[for][the][corresponding][reduced][fraction.][This][means][in][particular][that] _ai < q_ and hence _ri_ and its best upper approximations _[p] q[i]_[are][Farey][neighbours][which][gives][the] relation: 

1 = _aipi − biq_ = _bi_ ( _q −_ 1) + _ai − biq_ = _ai − bi ._ This now leads to _ri_ = 1 _− a_[1] _i_[for] _[i]_[ = 1] _[, ..., n]_[and][after][summing][up][to] 

**==> picture [111 x 25] intentionally omitted <==**

Since _ai_ ⩾ 2, we have _a_[1] _i_[+] _[· · ·] a_[1] _n_[⩽] _[n]_ 2[;][so] _[ n][−]_[2][ ⩽] _[n]_ 2[implies] _[ n]_[ ⩽][4][.][Clearly, when] _[ n]_[ = 4][ we need to] have _ri_ =[1] 2[for][each] _[i]_[,][while][when] _[n]_[ = 3][the][only][possibilities][for][(] _[a]_[1] _[, a]_[2] _[, a]_[3][)][are][(3] _[,]_[ 3] _[,]_[ 3)] _[,]_[(2] _[,]_[ 4] _[,]_[ 4)] and (2 _,_ 3 _,_ 6). A quick computation of the _bi_ ’s allows us to conclude that a _q >_ 1 can only exist in the case of torus bundles, where the other twisting numbers are obtained adding Giroux torsion. Now suppose that _e_ 0 = _−_ 1 and let _−q_ be the highest negative twisting number on _Z_ . To prove that no other _−Q < −q_ works, we follow the same steps as above. To the contrary we assume that _Q > q_ gives best upper approximations _[P] Q[i]_[of] _[r][i]_[and][satisfy] _[P]_[1][ +] _[ · · ·]_[ +] _[ P][n]_[=] _[ Q]_[ +] _[ n][ −]_[2][.][Then] since _[P] Q[i][<][p] q[i]_[we][have] _[P] Q[i][−] −[p] q[i]_[⩽] _[r][i][<][P] Q[i]_[which][implies] 

**==> picture [404 x 27] intentionally omitted <==**

Again, as _e_ ( _Z_ ) = 0, this forces _ri_ = _a[b][i] i_[=] _[P] Q[i][−] −[p] q[i]_[and][because] _[a][i][< Q]_[,][the][pairs] _[r][i]_[and] _[P] Q[i]_[are][Farey] neighbours. From 

**==> picture [249 x 12] intentionally omitted <==**

we see that then also _ri_ and _[p] q[i]_[are Farey neighbours and we can write] _[ r][i]_[=] _[p] q[i][−] a_[1] _iq_[.][Inserting into] _e_ ( _Z_ ) = 0 and knowing that _p_ 1 + _· · ·_ + _pn_ = _q_ + _n −_ 2, we get exactly the equality _a_ 11[+] _[ · · ·]_[ +] _a_[1] _n_[=] _n −_ 2 as above. When _n_ = 4 we cannot at the same time satisfy _a_ 11[+] _a_ 12[+] _a_ 13[+] _a_ 14[=][2][and] _b_ 1 _[b]_[2] _[b]_[3] _[b]_[4][while][when] _[n]_[ = 3][the][only][possibilities][for][(] _[a]_[1] _[, a]_[2] _[, a]_[3][)][are][(3] _[,]_[ 3] _[,]_[ 3)] _[,]_[(2] _[,]_[ 4] _[,]_[ 4)] _a_ 1[+] _a_ 2[+] _a_ 3[+] _a_ 4[= 1][,] and (2 _,_ 3 _,_ 6) as before with all _bi_ ’s equal to 1. The latter ones again correspond to torus bundles where the other twisting numbers are obtained adding Giroux torsion. □ 

28 

The twisting number is determined by the height function, as in the negative-definite case. Note that since blowing down _G_ yields the Stein domain _XG_ , for every _Z_ we have that _T_ [ _V_ can] is the contact invariant of a fillable structure on _Z_ . 

For this reason _G_ necessarily has full paths which have an initial and a terminal vector, as if all of them were having loops in them then some coordinates would satisfy _vi_ = _±m_ ( _i_ ) at every step, while _V_ can ends correctly and is not of this form. Note that this is not the case with _S_[1] _× S_[2] , whose unique full path ending correctly is always a loop; in fact, the manifold _XG ≃ S_[2] _× D_[2] , obtained by blowing down any of its standard graphs (all of them have two legs), is not a Stein filling of _S_[1] _× S_[2] . 

**Theorem 4.5** _We have that_ tw( _Z, ξ_ ) = _−_ 1 _−_ height _F_ [ _V_ can] _for every negative-twisting structure ξ on Z without Giroux torsion. This number is either equal to −d_ 1 _− d_ 2 _when the S_[3] _-subgraph G[′] of G is the Seifert fibration of Td_ 2 _,d_ 1 _with_ 1 ⩽ _d_ 2 ⩽ _d_ 1 _coprime, or to −_ 1 _when G[′] is empty._ 

_Proof._ From the proof of Proposition 4.4 and [8, Proposition 4.2] we have that tw( _Z, ξ_ ) is equal to the maximal twisting number of the fibration of _Td_ 2 _,d_ 1 in _S_[3] , and the latter one is _−d_ 1 _− d_ 2 as we know from [8, Theorem 4.3]. In addition, in the proof of the latter result is explained that 1 _−d_ 1 _−d_ 2 = height _F_ [ _W_ can] where _W_ can is the canonical vector of _G[′]_ ; the fact that height _F_ [ _V_ can] = height _F_ [ _W_ can] can be proved in the same way as [8, Remark 4.4]. 

Similarly, we know that tw( _Z, ξ_ ) = _−_ 1 when _G[′]_ is empty; since in this case _e_ 0 ⩽ _−_ 2, we also have that _V_ can is both initial and terminal and this means height _F_ [ _V_ can] = 0. □ 

Completing the classification of negative-twisting structures on a Seifert fibred space _Z_ with _e_ ( _Z_ ) = 0 now only requires a simple observation. 

_Proof of Theorem 4.1._ After determining the unique twisting number in Theorem 4.5, the proof is exactly the same as the ones of [8, Theorem 1.1 and Proposition 5.1]. □ 

## 5. The highest negative twisting number 

5.1. **The contact invariant.** Let ( _M, ξ_ ) be a contact 3-manifold, we are going to use the contact invariant _c[◦]_ ( _ξ_ ) _∈ HF[◦]_ ( _−M,_ s _ξ_ ) defined in [44], where _◦_ stands either for the hat or the plus flavour. 

From this section on we take _Y_ as a negative-definite Seifert fibred space with _b_ 1( _Y_ ) = 0, and we set as _−Y_ the manifold obtained by swapping orientation. In order to be consistent with the previous sections, we call Γ _[∗]_ the standard graph of _−Y_ = _M_ ( _e_ 0; _r_ 1 _, ..., rn_ ) with _n_ ⩾ 3 and _P_ Γ _∗_ its plumbing; recall that _b_[+] 2[(] _[P]_[Γ] _[∗]_[) = 1][.][In][addition,][we][only][consider][the][case][where] _[Y]_[(and][then][also] _−Y_ ) is not an _L_ -space. 

Let us take the basis _{_ [ _W_ 1] _, ...,_ [ _Wt_ +1] _, T_ [ _V_ 1] _, ..., T_ [ _Vt_ ] _}_ of _HF_[�] ( _Y,_ s) given by characteristic vectors, whose full path ends correctly, for a fixed Spin _[c]_ -structure on _Y_ . We recall that, using Equation (2.3), in the proof of Theorem 2.1 we showed that Ker _U ∩ HF_ red( _Y,_ s) can be canonically identified od with _HF_[�] ( _Y,_ s) through the inclusion _ρ∗_ ; hence, we refer to _B_ = _{T_ [ _V_ 1] _, ..., T_ [ _Vt_ ] _}_ as a basis of both Ker _U ∩ HF_ red( _Y,_ s) (from Theorem 2.1) and the odd subgroup of _HF_[�] ( _Y,_ s). 

Let us consider a contact structure _ξ_ on _−Y_ . Its contact invariant _c_[+] ( _ξ_ ) lives in _HF_[+] ( _Y,_ s _ξ_ ); moreover, if _c_[+] ( _ξ_ ) _∈ HF_ red is non-zero then from what we said above it can be written as a linear combination of elements in _B_ , and identified with � _c_ ( _ξ_ ) _∈ HF_[�] od( _Y,_ s). 

� **Proposition 5.1** _Let −Y be as above and equip it with a ξ such that c_ ( _ξ_ ) _is non-zero. If d_ 3( _ξ_ ) + _d_ ( _Y,_ s _ξ_ ) _is odd, or equivalently if c_[+] ( _ξ_ ) _∈ HF_ red( _Y,_ s _ξ_ ) _, then ξ is negative-twisting._ 

_Proof._ From standard Heegaard Floer theory and Theorem 2.1 we have that 

� _d_ 3( _ξ_ ) + _d_ ( _Y,_ s _ξ_ ) = _−M_ ( _c_ ( _ξ_ )) + _d_ ( _Y,_ s _ξ_ ) = _M_ ( _Va_ ) _− d_ ( _−Y,_ s _ξ_ ) _,_ 

29 

where _Va ∈_ Char(Γ _[∗] ,_ s _ξ_ ) is such that: _γa_ := [ _Va_ ] _∈ HF_[�] ( _−Y,_ s _ξ_ ) satisfies _⟨γa,_ � _c_ ( _ξ_ ) _⟩_ = 1, with respect to the duality identification _HF_[�] _∗_ ( _−Y,_ s) _≃ HF_[�] _−∗_ ( _Y,_ s) _[•]_ , and has minimal Alexander filtration � _F_ ( _Va_ ). In particular, the invariant _c_ ( _ξ_ ) is in the odd subgroup of _HF_[�] ( _Y,_ s _ξ_ ) and _T_ [ _Va_ ] _∈B_ is one of its coordinates. 

We mimic the second part of the proof of [8, Theorem 1.1]: using the definition of twisting number in Equation (1.1) and the tau-Bennequin inequality for the _tb_ -number in [8, Theorem 1.4], we can write 

**==> picture [264 x 26] intentionally omitted <==**

where _K_ is the regular fibre of _−Y_ . Now let _Vb_ be as _Va_ but with maximal Alexander filtration, implying that if _J γb_ := [ _−Vb_ ] _∈ HF_[�] ( _−Y,_ s _ξ_ ) then _⟨J γb,_ � _c_ ( _ξ_ ) _⟩_ = _⟨J γb, J_ � _c_ ( _ξ_ ) _⟩_ = _⟨γb,_ � _c_ ( _ξ_ ) _⟩_ = 1. From Equation (3.2), Theorem 3.3 and [2, Lemma 2.2] we write 

**==> picture [402 x 27] intentionally omitted <==**

which by leads to 

**==> picture [443 x 49] intentionally omitted <==**

5.2. **Realised characteristic vectors.** Since _−Y_ is not an _L_ -space, from Remark 3.8 we know that the 4-manifold _X_ := _X_ Γ _∗_ , obtained by blowing down the graph Γ _[∗]_ , is a Stein domain with _b_[+][A][famous][result][of][Plamenevskaya][[48]][then][implies][that][there][exists][a][unique][Spin] _[c]_[-] 2[(] _[X]_[) = 1][.] structure v on _X_ such that _F_[+][=][1][,][where] _[ξ]_[is][induced][by][any][Stein][structure][on] _[X] X,_ v[(] _[c]_[+][(] _[ξ]_[))] corresponding to a given sequence of stabilisations. 

More specifically, let (Γ _[∗]_ ) _[′]_ be the _S_[3] -subgraph of Γ _[∗]_ and let _ℓ_ be equal to _|_ Γ _[∗] |−|_ (Γ _[∗]_ ) _[′] |_ , we have that ( _X, J_ ) is determined by ( _−_ 1)-contact surgery on a Legendrian realisation _K_ 1 _∪ ... ∪Kℓ_ of the blown down graph; moreover, we have that _c_ 1(v) = **V** _∈_ Char( _X_ ) and **V** = (rot _ξ_ ( _K_ 1) _, ...,_ rot _ξ_ ( _Kℓ_ )) where _ξ_ = _J|−Y_ . Let _sj_ be the number of stabilisations on _Kj_ (which is a Legendrian positive torus knot by Corollary 3.11) in the surgery presentation, then the smooth framing of the knot _Kj_ is given by 

**==> picture [94 x 13] intentionally omitted <==**

while 

**==> picture [288 x 13] intentionally omitted <==**

The vector **V** is characteristic because TB _ξ_ std( _Td_ 2 _,d_ 1) = SL _ξ_ std( _Td_ 2 _,d_ 1) is always odd. 

**Remark 5.2** _We recall that here we denote a positive torus knot by Td_ 2 _,d_ 1 _with d_ 2 ⩽ _d_ 1 _. This convention is different with respect to the one we used in_ [8, Section 4] _; in fact, there we take d_ 1 _to be the denominator of r_ 1 _where M_ ( _−_ 1; _r_ 1 _, r_ 2) _is the Seifert fibration of Td_ 2 _,d_ 1 _and r_ 1 _> r_ 2 _._ 

A natural generalisation of [8, Proposition 5.2] can be shown for manifolds as _−Y_ . 

**Lemma 5.3** _Let −Y be an indefinite Seifert fibred space which is not an L-space, and_ ( _X, J_ ) _the Stein filling obtained by blowing down the standard graph. Then there exists a full path_ [ _V_ ] _which ends correctly such that T_ [ _V_ ] = _c_[+] ( _J|−Y_ ) _∈ HF_ red( _Y, J|−Y_ ) _where V ∈_ Char(Γ _[∗]_ ) _is the corresponding initial vector._ 

30 

_Proof._ In light of Theorems 1.1 and 2.1 we just have to show that � _c_ ( _ξ_ ) has odd parity, in other words that _c_[+] ( _ξ_ ) _̸_ = Θ[+] , and then conclude as in the proof of [8, Proposition 5.2]. We recall that the latter proof is based on the result of Bodnár-Plamenevskaya in [4, Section 5] saying that the strict transform induces (through the blow-downs) an automorphism of _HF_[+] which commutes with the cobordism maps. In cite [4] this is done for negative-definite graphs, but by Theorem 1.1 the proof can be repeated in the same way when the graph is indefinite. 

Suppose that _c_[+] ( _ξ_ ) = Θ[+] _∈_ Ker _U ∩_ Im _U[n]_ for _n_ ⩾ 1, then the map _FX,_[+] v[would][send][Θ][+][to] 1. Since we know from Lemma 3.7 that _b_[+] 2[(] _[X]_[)][=][1][,][we][obtain][a][contradiction][with] _[F] X,[∞]_ v[being] vanishing [38]; namely, by commutation we would have _FX,_[+] v[(Θ][+][) =] _[ π][∗]_[(] ~~_[F]_~~ _X,[∞]_ v[(1)) =] _[ π][∗]_[(0) = 0][.] □ 

In our case we can track down _V_ starting from **V** and going backwards along the blow-down procedure, and we denote the set of these vectors as the _realised_ characteristic vectors in Char(Γ _[∗]_ ). 

Before we give a description of which vectors are realised, we recall that there are four different types of an _S_[3] -subgraph _G[′]_ of a standard graph _G_ . Other than the empty set and the one given by the fibration of _Td_ 2 _,d_ 1 when _d_ 2 _>_ 1, we have the following two where the first one is just the centre of Γ _[∗]_ (the fibration of _T_ 1 _,_ 1) while the second one consists also of a string of _d_ 1 _−_ 1 vertices with framing _−_ 2 (the fibration of _T_ 1 _,d_ 1 when _d_ 1 _>_ 1). 

**==> picture [214 x 8] intentionally omitted <==**

When _e_ 0 = _−_ 1 we call _G[′′]_ the subgraph of _G_ made by the vertices that are not in _G[′]_ , but are connected to the centre; in addition, in this case we also call _G[′′] i_[for] _[i]_[=][1] _[,]_[ 2][the][(eventual)] unique vertex in the _i_ -th leg that is not in _G[′] ∪ G[′′]_ , but is connected to _G[′]_ . Let us denote by _T_ the number of consecutive vertices with framing _−_ 2 at the end of the first leg. 

**Theorem 5.4** _Let G be the standard graph of any Seifert fibred space. An initial vector V ∈_ Char( _G_ ) _is realised if and only if its coordinates_ ( _v_ 1 _, ..., v|G|_ ) _are as follows:_ 

**==> picture [248 x 82] intentionally omitted <==**

_where m_ ( _j_ ) _is the framing of the j-th vertex of G._ 

_Proof._ Let _V_ be a vector as in the statement, then applying the strict transform, see [4, Section 5], to _V_ yields the vector in Char( _XG_ ) whose coordinates are untouched outside of _G[′] ∪ G[′′] ∪ G[′′]_ 1 _[∪][G][′′]_ 2[,] and increased by 1 _,_ 2 + _T_ and _d_ 1 + _d_ 2 _−_ 1 in _G[′′]_ 1 _[,][G][′′]_ 2[and] _[G][′′]_[respectively;][moreover,][the][framings] on the components are increased by 1 _,_ 2 + _T_ and _d_ 1 _d_ 2 respectively (the ones in _G[′′]_ become torus knots isotopic to _Td_ 2 _,d_ 1). It is then easy to check that each choice of _V_ corresponds to a choice of the rotation numbers in the surgery presentation of _XG_ . 

Suppose that _V_ is realised. Since [ _V_ ] ends correctly then _V_ must agree with _V_ can on _G[′]_ ; moreover, again by using the strict transform as above we obtain that each coordinate _x_ of _j ∈ G[′′]_ is increased to _x_ + _d_ 1 + _d_ 2 _−_ 1 when we blow down. The value _x_ = _m_ ( _ji_ ) + 2 (the one of _V_ can) is the lowest possible; therefore, we obtain 

**==> picture [354 x 12] intentionally omitted <==**

31 

where the _ji_ ’s are the vertices of _G_ that survive the blow-downs. We can now conclude by observing that the values of the rotation number are symmetric, which means the maximum is reached by 

**==> picture [460 x 31] intentionally omitted <==**

� od Let us consider a contact structure _ξ_ on _−Y_ such that _c_ ( _ξ_ ) _∈ HF_[�] ( _Y,_ s _ξ_ ) is non-vanishing; as we discussed above, the condition on the parity is equivalent to the fact that _d_ 3( _ξ_ ) + _d_ ( _Y,_ s _ξ_ ) is odd. We proved in [8, Theorem 1.4] that every negative-twisting structure on _Y_ has the same twisting number; the same is no longer true when we reverse the orientation as shown by Ghiggini and Van Horn-Morris in [22, Proposition 2.7]. We introduce the following terminology: we say that tw( _−Y_ ) is the highest value among all the negative twisting numbers of tight structures on _−Y_ ; in the same way, we say that tw( _−Y_ ) is the lowest one. Note that since these are negative numbers, then the highest one actually has the smallest absolute value. We are going to ignore tw( _−Y_ ) in the remaining of the section; for this reason, we postpone the proof that this invariant is well-defined to Lemma 6.1. 

**Proposition 5.5** _Suppose that ξ is any structure on −Y induced by_ ( _X, J_ ) _as described above. Then we have that_ 

**==> picture [202 x 12] intentionally omitted <==**

_and this number is either equal to −d_ 1 _−d_ 2 _when the S_[3] _-subgraph_ (Γ _[∗]_ ) _[′] of_ Γ _[∗] is the Seifert fibration of Td_ 2 _,d_ 1 _with_ 1 ⩽ _d_ 2 ⩽ _d_ 1 _coprime, or to −_ 1 _when_ (Γ _[∗]_ ) _[′] is empty._ 

_Proof._ We refer to [8, Section 4] for more details about this proof, as it similar to the one we did in the negative-definite case. The proof that tw( _−Y_ ) is determined by _d_ 1 and _d_ 2 is the same as in [8, Proposition 4.2 and Theorem 4.3]; moreover, that this number equals _−_ 1 _−_ height _F_ [ _V_ can] follows as in [8, Remark 4.4]. 

By construction the regular fibre _K_ of _−Y_ bounds a Lagrangian surface in ( _X, J_ ) whose boundary is its Legendrian realisation _K_ ; hence, there are transverse push offs of _K_ and _−K_ bounding a symplectic surface in ( _X, J_ ). We use [2, Theorem 1.3] to write 

**==> picture [216 x 13] intentionally omitted <==**

which implies 

**==> picture [142 x 14] intentionally omitted <==**

by [8, Theorem 1.3] and the symmetries of knot Floer homology. We can now apply Theorem 3.3 and as in the proof of Proposition 5.1 we obtain 

**==> picture [274 x 27] intentionally omitted <==**

where _V[′]_ is the initial vector of [ _−V_ ] and _V_ the one such that _T_ [ _V_ ] = � _c_ ( _ξ_ ) from Lemma 5.3. 

The fact that height _F_ [ _V_ ] = height _F_ [ _V_ can] follows easily from Theorem 5.4 and the definition of height in Section 3.3. This concludes the proof as it shows that tw( _−Y, ξ_ ) = tw( _−Y_ ). □ 

In Section 6 we are going to show that the structures obtained by blowing down Γ _[∗]_ are the only ones whose twisting number is tw( _−Y_ ). We now prove the following lemma, which is going to be useful in Section 7. 

**Lemma 5.6** _Let ξ be a structure on −Y such that its contact invariant satisfies_ 0 = _c_[+] ( _ξ_ ) = _T_ [ _V_ 1] + _..._ + _T_ [ _V k_ ] _∈ HF_ red( _Y,_ s _ξ_ ) _, where each initial vector V[i] ∈_ Char(Γ _[∗] ,_ s _ξ_ ) _has full path ending correctly and V[i]_ = _V[j] when i ̸_ = _j. Then V[i] is a realised characteristic vector for i_ = 1 _, ..., k._ 

32 

_Proof._ Glue a symplectic cap ( _C, ω_ ) of ( _−Y,_ s _ξ_ ) to ( _X,_ v), which always exists from a result of Eliashberg [13], so that we get the closed 4-manifold _X_[�] equipped with the Spin _[c]_ -structure �v such � that v = v _∪_ s _ξ J_ , where _J_ is an almost-complex structure compatible with _ω_ ; we denote by **V** _∈_ Char( _X,_ s _ξ_ ) the characteristic vector such that _c_ 1( **V** ) = v. 

By results of Plamenevskaya [48] and Ghiggini [19], and the gluing formula for the mixed invariant [45] we can choose ( _C, ω_ ) in the way that _b_[+] 2[(] _[C]_[)][ ⩾][1][and][Φ][ �] _X,_ �v[(1) =] _[ F] X,_[+] v[(] _[c]_[+][(] _[ξ]_[))][,][where] here we are using that the mixed invariant Φ is well-defined because _b_[+] 2[(] _[X]_[)][=][1][.][Take] **[V]**[as] the vector **V** _[i]_ = ( **v** 1 _[i][, ...]_[)] _[∈]_[Char][(] _[X,]_[ s] _[ξ]_[)][obtained][by][applying][the][strict][transform][to] _[V][i]_[for][any] _i_ = 1 _, ..., k_ ; according to these choices, we have that ( _X,_[�] �v) has non-vanishing mixed invariant, thus [�v] _∈ H_[2] ( _X_ ; Z) is a basic class and we can use the general version of the Adjunction inequality, see [17, 37]. 

Consider the surface Σ given by gluing the core of the _j_ -th 2-handle of _X_ to a properly embedded surface in _X_ bounding the corresponding attaching sphere. We index the 2-handles in the same way as the vertices of Γ _[∗]_ ; of course, some vertices (namely the ones in the _S_[3] -subgraph) disappear after the blow-downs; hence, their index does not appear among the **v** _j[i]_[’s,][the][coordinates][of] **[V]** _[i]_[.] When _j_ comes from a vertex of Γ _[∗]_ outside of (Γ _[∗]_ ) _[′′] ∪_ (Γ _[∗]_ ) _[′′]_ 1 _[∪]_[(Γ] _[∗]_[)] 2 _[′′]_[then][Σ][is][a][sphere][and] 2 = _χ_ (Σ) ⩽ _−_ [Σ] _·_ [Σ] _± c_ 1(v)[Σ] ⩽ _−m_ ( _j_ ) _−|_ **v** _j[i][|]_[ =] _[ −][m]_[(] _[j]_[)] _[ −|][v] j[i][|][ ,]_ where _V[i]_ = ( _v_ 1 _[i][, ..., v] |[i]_ Γ _[∗] |_[)][.][Thus] 

_m_ ( _j_ ) + 2 ⩽ _vj[i]_[⩽] _[−][m]_[(] _[j]_[)] _[ −]_[2] 

and similar inequalities hold for the vertices in (Γ _[∗]_ ) _[′′]_ 1[and][(Γ] _[∗]_[)] _[′′]_ 2[;][we][write][only][the][second][case] explicitly: 2 = _χ_ (Σ) ⩽ _−m_ ( _j_ ) _−_ 2 _− T −|_ **v** _j[i][|]_[ =] _[ −][m]_[(] _[j]_[)] _[ −]_[2] _[ −][T][−|][v] j[i]_[+ 2 +] _[ T][|][ ,]_ 

where _T_ is as in Theorem 5.4, which implies 

**==> picture [164 x 15] intentionally omitted <==**

When _j_ comes from a vertex in (Γ _[∗]_ ) _[′′]_ , the attaching sphere is _Td_ 2 _,d_ 1, the strict transform increases the framing by _d_ 1 _d_ 2 and 

**==> picture [459 x 29] intentionally omitted <==**

**==> picture [178 x 15] intentionally omitted <==**

Since each _V[i]_ is initial, we have _vj[i]_[=] _[m]_[(] _[j]_[) + 2][when] _[j][∈]_[(Γ] _[∗]_[)] _[′]_[;][hence,][for][every] _[i]_[=][1] _[, ..., k]_[and] _j_ = 1 _, ..., |_ Γ _[∗] |_ we showed that _vj[i]_[is][always][inside][the][range][of][the][possible][values][for][a][realised] characteristic vector, as prescribed by Theorem 5.4. □ 

## 6. The classification for indefinite Seifert fibred spaces 

6.1. **Background.** The starting point of our classification is the observation due to Ghiggini [20] and Massot [31] that every negative-twisting structure on a Seifert fibred space over a sphere admits a convex decomposition into background and solid tori. The _background_ is the piece diffeomorphic to Σ0 _,n × S_[1] where Σ0 _,n_ is an _n_ -punctured sphere and _n_ is the number of singular fibres; the possible boundary slopes are determined from the Seifert constants through the GhigginiMassot’s algorithm in Theorem 1.3, and their common denominator fixes the unique tight contact structure with twisting number equal to the negative of this denominator on Σ0 _,n × S_[1] , see [20, Section 3] and [8, Proposition 5.1]. 

**Lemma 6.1** _Every Seifert fibred space M with b_ 1( _M_ ) = 0 _has only finitely many negative twisting numbers._ 

33 

_Proof._ We do the proof in the case that _e_ ( _M_ ) _>_ 0, because for negative-definite manifolds we already know from [8, Section 4] that the twisting number is unique. The claim follows by finding an appropriate upper bound for _|_ tw( _M_ ) _|_ through the Ghiggini-Massot’s algorithm, in terms of the negative continued fractions of the Seifert coefficients of _M_ ; more specifically, here we prove that if _−q_ is a negative twisting number then _q < e[n]_ ( _[−] M_[2] )[where] _[n]_[is][the][number][of][legs.] 

By definition for each leg there is a positive integer _pi_ such that _[p] q[i]_[is][the][best][upper][approxi-] mation for _ri_ ; equivalently, the number _pi_ is the smallest integer such that _[p] q[i][> r][i]_[and no fraction] with denominator lower than _q_ is between them. Let _ri_ = _a[b][i] i_[as][reduced][fraction,][then][there][is][a] unique integer _ci_ , with 1 ⩽ _ci_ ⩽ _ai_ , such that _pi_ = _[q][b][i] a_[+] _i[c][i]_ ; indeed, we have that _ci_ is the smallest positive residue of _−qbi_ mod _ai_ , and then _a[c][i] i[∈]_[(0] _[,]_[ 1]][.] 

The twisting-number condition says _p_ 1 + _· · ·_ + _pn_ = _−e_ 0 _q_ + _n −_ 2. Using the expression above for each _pi_ we obtain 

**==> picture [460 x 67] intentionally omitted <==**

The botany of the negative-twisting contact structures on an indefinite Seifert fibred space _−Y_ depends on its standard graph. For this reason we introduce the following definition: we say that _−Y_ is a manifold of _type B_ when its standard graph Γ _[∗]_ contains one of the seven graphs in Figure 6, which means the standard graph of a Seifert fibred torus bundle over a circle appears as a subgraph of Γ _[∗]_ ; otherwise, we say that _−Y_ is a manifold of _type A_ . We recall that _−Y_ is not an _L_ -space since the latter ones do not carry any negative-twisting structures. 

The strategy of the classification is to construct some structures on _−Y_ whose contact invariant _c_[+] is non-vanishing and lives in _HF_ red; we saw in Proposition 5.1 that these are necessarily negative-twisting. The classification then follows using the usual scheme: based on the work of Honda [26, 27], we find an upper bound via convex decompositions, then we show that it is realised by the ones we explicitly constructed. 

The explicit value of the upper bound, for a given twisting number _−q_ is obtained as follows. For each leg take the positive reduced fraction _[p] q[i]_[to][be][the][best][upper][approximation][for] _[r][i]_[.][In] the continued fraction expansion: if _− r_[1] _i_[=][[] _[m][i]_ 1 _[, ..., m][i] ki_[]][then] _[−] p[q] i_[=][[] _[m][i]_ 1 _[, ..., m][i] hi−_ 1 _[, n][i] hi_[]][where] either _hi_ = _ki_ + 1 or _hi_ ⩽ _ki_ and _n[i] hi[> m] h[i] i_[.][We][have][that][the][number][of][contact][structures,][up] to isotopy, with twisting number _−q < −_ 1 is at most _T_ (1 _, q_ ) _· · · T_ ( _n, q_ ) where each _T_ ( _i, q_ ) is equal to 1 when _hi > ki_ or to 

**==> picture [298 x 35] intentionally omitted <==**

when _hi_ ⩽ _ki_ . The number of contact structures with twisting number _−_ 1 is instead equal to 

**==> picture [284 x 36] intentionally omitted <==**

as already shown in the proofs of [8, Theorem 1.1 and Proposition 5.1] in the negative-definite case, and Theorem 4.1 in the singular case; same arguments hold also for _−Y_ by Proposition 5.5. More generally, this argument can be used to prove Proposition 1.4, which says that all the negative-twisting structures, with the highest possible twisting number, are induced by a Stein structure on the 4-manifold obtained by blowing down the standard graph. 

34 

_Proof of Proposition 1.4._ As mentioned above, it follows by Lemma 3.7, Theorem 4.1 and Proposition 5.5, using the same arguments in [8, Theorem 1.1 and Proposition 5.1]. □ 

Generally the described upper bound takes into account that the background admits a unique ( _−q_ )-twisting structure up to isotopy and counts all possible tight extensions to the glued-in solid tori, as has been described to more details in the proof of [8, Proposition 5.1]. 

Below we separately analyse which twisting numbers (other than the highest) manifolds of type A and B admit, and classify the corresponding structures. 

6.2. **Manifolds of type A.** Following the work in [31, 6], we start this subsection by recalling the properties of a contact structure which is tangent to the fibres of a Seifert fibred space _M_ . The result below follows from [31, Subsection 4.2, Lemma 7.2 and Proposition 8.9]. 

**Proposition 6.2** _Suppose that ξ is a contact structure on a Seifert fibred space M ; if ξ is tangent to the fibres then_ ( _M, ξ_ ) _has a (weak) symplectic filling_ ( _W, ω_ ) _and ξ is negative-twisting. Furthermore, there is a Legendrian realisation of a regular fibre of M which bounds a Lagrangian surface in_ ( _W, ω_ ) _._ 

_Proof._ Starting from the Seifert fibration _M → B_ , where the base _B_ is a symplectic 2-dimensional orbifold (of genus zero) with isolated cyclic singularities, one can consider the associated singular disk bundle _D → B_ where each fibre is equipped with (a quotient of) the symplectic form[1] 2[d(] _[r]_[2][d] _[θ]_[)][.] As explained in [31], this is a symplectic orbifold ( _D, ωD_ ) which can be resolved to get the desired filling _W_ ; more specifically, the resolution gives a branched cover _c_ : _W → D_ . The regular fibres of _D_ are Lagrangian disks whose boundary is Legendrian, and isotopic to a regular fibre _K_ of _M_ . Since the regular fibres are preserved by the branched cover, we have that _K_ is fixed by _c_ and then it still bounds a Lagrangian surface in ( _W, ω_ := _c[∗] ωD_ ) with the same boundary condition. □ 

Using Ghiggini-Massot’s algorithm, the possible values of a negative twisting number (of a tight structure) on _−Y_ can be determined exactly through elementary number theory. This set of integers only depends on the Seifert coefficients of _−Y_ = _M_ ( _e_ 0; _r_ 1 _, ..., rn_ ); moreover, from Lemma 6.1 we also know that it is finite and thus we can identify the invariant tw( _−Y_ ), the lowest twisting number of _−Y_ . We can pinpoint a special family of indefinite Seifert fibred spaces which can be considered minimal for a given background of tw( _−Y_ ); these manifolds allow us to determine the values of the twisting numbers of any other _−Y_ of type A. 

We introduce the following terminology: we say that a manifold of type A is _without tails_ when it has at least two negative twisting numbers (a posteriori, we know there will be exactly two of them) and _|_ tw( _−Y_ ) _| > ai_ for all _i_ = 1 _, ..., n_ , where _ri_ = _a[b][i] i_[as][a][positive][reduced][fraction.][A] simple example of a manifold without tails is the oppositely oriented Brieskorn sphere _−_ Σ(2 _,_ 5 _,_ 9) whose standard graph is in Figure 7. 

**==> picture [104 x 70] intentionally omitted <==**

Figure 7. The manifold _−Y_ = _−_ Σ(2 _,_ 5 _,_ 9), corresponding to _M_ ( _−_ 1;[1] 2 _[,]_[2] 5 _[,]_[1] 9[)][.][Comput-] ing the negative twisting numbers yields _|_ tw( _−Y_ ) _|_ = 17 _>_ 2 _,_ 5 _,_ 9. 

35 

**Lemma 6.3** _Let −Y be a manifold of type A. Then either −Y has a unique negative twisting number, or is without tails, or it is related to a manifold M without tails such that:_ 

- _for any leg i such that |_ tw( _−Y_ ) _|_ ⩽ _ai one has − r_[1] _i_[= [] _[m]_ 1 _[i][, ..., m][i] ki_[]] _[,][while][the][corresponding] leg of M either has coefficient − r_[1] _i[′]_[= [] _[m]_ 1 _[i][, ..., m][i] li_[]] _[with][l][i][< k][i][or][it][is][missing;]_ 

- _if −q is a twisting number of −Y then the same is true for M ._ 

_Proof._ It is clear that if _−Y_ is in neither of the first two categories then _q_ = _|_ tw( _−Y_ ) _|_ ⩽ _ai_ for at least one _i_ . We first construct an _M_ such that its _i_ -th leg has coefficient _ri[′]_[as][in][the][statement] for every such _i_ ; then we prove that the set of the negative twisting numbers of _−Y_ is contained in the one of _M_ ; finally, we show that _M_ is also of type _A_ . 

We have already observed that _[p] q[i]_ as a best upper approximation for _ri_ = _a[b][i] i_[with] _[q] < ai_ has continued fraction expansion of the form [ _m[i]_ 1 _[, ..., m][i] hi−_ 1 _[, n][i] hi_[]][with] _[h][i]_[⩽] _[k][i]_[and] _[n][i] hi[> m] h[i] i_[.][Taking] _li_ = _hi −_ 1, where we interpret 0 as no leg, gives us the desired truncation; note that in this way _ri[′]_ is the biggest left Farey neighbour of _[p][i]_ with denominator at most _q_ . Indeed, the rational number _q pqi_ is a best upper approximation also for _ri[′]_[and][so][are][all][the][numbers][[] _[m][i]_ 1 _[, ..., m][i] ji−_ 1 _[, s][i] ji_[]][with] _ji_ ⩽ _hi_ and _s[i] ji[> m][i] ji_[(or] _[s][i] ji[> n][i] ji_[if] _[j][i]_[=] _[ h][i]_[).][Since][the][absolute][value] _[q]_[of][any][twisting][number] of _−Y_ is a numerator of a continued fraction of the described form, the corresponding _[P] q[i]_[remains] a best upper approximation for the truncated fraction _ri[′]_[.][Consequently,][since][the] _[P][i]_[’s][are][the] same with respect to _ri_ and _ri[′]_[so][is][their][sum,][and][then] _[−][q]_[is][also][a][twisting][number][of] _[M]_[.] Since _−Y_ has at least two twisting numbers, by the argument above the same is true for _M_ . Since _M_ cannot be of type B, as its standard graph is a subgraph of the one of _−Y_ , it follows that it is of type A and then without tails. □ We now analyse negative-twisting structures on a manifold without tails. For any _q >_ 1 we can analogously say that a manifold is without tails with respect to the twisting number _−q_ when _q > ai_ for each _i_ . 

**Theorem 6.4** _If −Y is a manifold of type A without tails then it has exactly two negative twisting numbers._ 

_Proof._ Let _−Y_ = _M_ ( _e_ 0; _r_ 1 _, ..., rn_ ) with _ri_ = _a[b][i] i_[as a reduced fraction, and denote by][ Γ] _[∗]_[its standard] graph. Being of type A without tails, the manifold _−Y_ admits tight contact structures with at least two twisting numbers: the highest tw( _−Y_ ) from Section 5 and the lowest tw( _−Y_ ) with _ai < |_ tw( _−Y_ ) _|_ for _i_ = 1 _, ..., n_ . 

We assume to the contrary with the statement that there exists another twisting number _−q_ . If we write _q_ = _|_ tw( _−Y_ ) _|_ , for the absolute value of the lowest twisting number, and _q_ = _|_ tw( _−Y_ ) _|_ , for the absolute value of the highest one, we have strict inequalities _q < q < q_ . We will first describe how the best upper approximations for _ri_ corresponding to the three twisting numbers are related to each other, and then prove that they cannot all three satisfy the twisting number relation appearing in Ghiggini-Massot’s algorithm. 

We write _[p] qi_[0] _[,][p] q[i][,]_[and] _[p] qi_[1] for the best upper approximations for _ri_ when _i_ = 1 _, ..., n_ . Note that when _q_ = 1 we have that _p_[0] 1[=] _[−][e]_[0] _[−]_[1][and] _[p]_[0] _i_[=][1][for] _[i]_[=][2] _[, ..., n]_[;][in][this][way,][the][relation] _p_[0] 1[+] _[ ...]_[ +] _[ p] n_[0][=] _[ −][e]_[0] _q_ + _n −_ 2 is still satisfied, see [8, Section 4]. 

Since _−Y_ is without tails, the Seifert coefficient _ri_ and the best upper approximations _[p] i_[1] are _q_ Farey neighbours. We describe a subgraph _G_ of Γ _[∗]_ as the truncation we obtain by looking at a manifold without tails with respect to _q >_ 1: the graph _G_ is determined by _M_ ( _e_ 0; _[d] c_ 1[1] _[, ...,][d] cn[n] ′[′]_[)] where _[d] ci[i]_[is][the][biggest][left][Farey][neighbour][with] _[c][i]_[⩽] _[q]_[(when][it][is][non-zero)][of] _[p] q[i]_[;][similarly,][we] define _[u] vi[i]_[as][a][left][Farey][neighbour][of] _[p] qi_[0][.] 

36 

For each leg _i_ = 1 _, ..., n_ let 

**==> picture [460 x 150] intentionally omitted <==**

At each level, the twisting number relation is 

**==> picture [396 x 32] intentionally omitted <==**

From the first column of _Xi_ = _Xi_[(0)] _Mi_ we obtain _pi_ = _σip_[0] _i_[+] _[ τ][i][u][i]_[and] _[q]_[=] _[ σ][i] q_ + _τivi_ , which can be rephrased as 

**==> picture [280 x 28] intentionally omitted <==**

Summing over _i_ , substituting in the twisting number relation, and repeating the same computation for _Xi_[(1)] = _XiNi_ , gives 

**==> picture [390 x 32] intentionally omitted <==**

If we consider the composition _MiNi_ then the corresponding lower-left entry is _σi[′][τ][i]_[ +] _[ τ] i[ ′][π][i]_[,][so] the same computation gives 

**==> picture [311 x 31] intentionally omitted <==**

and subtracting Equations (6.3) from Equation (6.4) yields 

**==> picture [156 x 31] intentionally omitted <==**

We have that _τi, τi[′][, π][i][, σ] i[′][>]_[ 0][,][thus] _[σ] i[′]_[=] _[ π][i]_[= 1][for] _[i]_[ = 1] _[, ..., n]_[.][Now][from] _[X][i]_[=] _[ X] i_[(0)] _Mi_ , using _πi_ = 1, the lower-right entry gives _ci_ = _ρiq_ + _vi_ while the lower-left one gives 

**==> picture [302 x 12] intentionally omitted <==**

hence, we showed that _τi_ = _[q] c[−] iq_ for _i_ = 1 _, ..., n_ . Plugging this into Equation (6.3) and dividing by _q − q >_ 0 now gives 

**==> picture [284 x 25] intentionally omitted <==**

We can assume that each _ci_ ⩾ 2 if we observe that the subgraph _G_ can have _n[′]_ ⩽ _n_ legs; in fact, it is possible that some legs of Γ _[∗]_ disappear in the process, and in this case the coefficient _[d] ci[i]_[would] be[0][Nonetheless,][we][note][that] 1[1][and][this][reduces][by][1][the][right-hand][side][of][Equation] 1[.] _ci_[=] (6.5) corresponding to the missing _i_ -th leg. 

37 

To complete the proof, we now just have to determine all the possible subgraphs _G_ such that 1 1 _c_ 1[+] _[ ...]_[ +] _cn′_[=] _[n][′][ −]_[2][with] _[c][i]_[⩾][2][.][We][already][solved][this][problem][in][the][proof][of][Proposition] 4.4, and we know that the only cases are (2 _,_ 3 _,_ 6) _,_ (2 _,_ 4 _,_ 4) _,_ (3 _,_ 3 _,_ 3) and (2 _,_ 2 _,_ 2 _,_ 2). Since we want _Y_ (and then _−Y_ ) to not be an _L_ -space, using Theorem 3.10 we conclude that: if _e_ 0 = _−_ 1 then _n[′]_ = 3 and the _di_ ’s are (1 _,_ 1 _,_ 1); meanwhile, if _e_ 0 ⩽ _−_ 2 then 

**==> picture [252 x 34] intentionally omitted <==**

because by construction the manifold presented by _G_ has two distinct negative twisting numbers and thus non-negative _e_ , which forces _e_ 0 = _−_ 2 and _di_ = _ci −_ 1. This means that Γ _[∗]_ contains a subgraph isomorphic to the standard graph of a torus bundle, see Figure 6, and this is impossible because the manifold is of type A. □ 

**Proposition 6.5** _If −Y is a manifold of type A without tails then all the negative-twisting tight structures on −Y are symplectically fillable, and they are distinguished by c_[+] _in HF_ red( _Y_ ) _._ 

_Proof._ The manifold _−Y_ has exactly two negative twisting numbers because of Theorem 6.4. Since _q_ = _|_ tw( _−Y_ ) _| > ai_ for _i_ = 1 _, ..., n_ , Massot in [31, Theorem 8.7] tells us that _−Y_ actually has a unique contact structure _ξ_ 0 with twisting number _q_ , which is tangent to the fibres; hence, this structure is symplectically fillable because of Proposition 6.2. 

The fact that all the tight contact structures with twisting number _q_ = _|_ tw( _−Y_ ) _|_ are the ones in Proposition 5.5, which means they are induced by Stein structures on the blown down graph _X_ Γ _∗_ , has been discussed in Proposition 1.4. More specifically, we observe that the upper bound (for these structures) from convex surface theory is precisely equal to the number of realised characteristic vectors; we know that these vectors are in one to one correspondence with the contact structures we are considering by Lemma 5.3. Hence, the last claim holds when _ξ_ satisfies tw( _−Y, ξ_ ) = tw( _−Y_ ), and each contact invariant is of the form _T_ [ _V_ ] _∈ HF_ red( _Y_ ) for a certain realised characteristic vector _V_ . 

To distinguish the invariant of the structure _ξ_ 0, we use the fact that there exists a Legendrian knot _K_ , smoothly isotopic to a regular fibre of _−Y_ , bounding a Lagrangian surface Σ in a symplectic filling of ( _−Y, ξ_ ) from Proposition 6.2. By the same argument in the proof of Propositions 5.1 and 5.5 we have 

**==> picture [160 x 15] intentionally omitted <==**

Note that in this case there is an additional detail to discuss: the fact that SL _ξ_ 0( _±K_ ) = 2 _τξ_ 0( _±K_ ) _−_ 1 does not follow just by [2, Theorem 1.3]; the knot _±K_ is indeed the boundary of a symplectic surface Σ _[±]_ , but the filling is not necessarily Stein (Massot [31] only guarantees is symplectic). The result still holds with little modifications: from [2, Theorem 4.1] we still have the slice-Bennequin inequality 

**==> picture [208 x 15] intentionally omitted <==**

where _ω_ is the symplectic form. This inequality is sharp because Σ _[±]_ is symplectic; a proof of this fact can be found in [14, Lemma 2.13]. 

ev Assume first that _c_[+] ( _ξ_ 0) = Θ[+] s _ξ_ 0[;][since][in][this][case] �[�] _[c]_[(] _[ξ]_[0][)] _[∈] HF_[�] ( _Y,_ s _ξ_ 0), we can compute _τξ_ 0( _K_ ) := _−τ_ � _c_ ( _ξ_ 0)( _K_ ) from Theorem 3.3; namely, write _c_ ( _ξ_ 0) = [ _W_ 1] + _· · ·_ + [ _Wk_ ] where _F_ ( _W_ 1) _<_ ev _· · · < F_ ( _Wk_ ) are initial, and _{_ [ _W_ 1] _, ...,_ [ _Wt_ ] _}_ is the canonical basis of _HF_[�] ( _Y,_ s _ξ_ 0) given by the 

38 

full paths. By definition of twisting number and conjugation we can then write 

**==> picture [350 x 57] intentionally omitted <==**

where _W_ can _∈_ Char( _P_ Γ _,_ s _ξ_ 0) and _W_ 1 _[′]_[is][the][initial][vector][of][[] _[−][W]_[1][]][.][This][is][not][possible][by][the] assumptions we made. 

Now we know that _c_[+] ( _ξ_ 0) _∈ HF_ red( _Y,_ s _ξ_ 0). Suppose that _c_[+] ( _ξ_ 0) = _T_ [ _V_ ] for some realised _V_ ; then doing the same computation as above, but using Equation (3.5) instead, yields _q_ = _−_ 1 _−_ height _F_ [ _V_ can] = tw( _−Y_ ) by Proposition 5.5. This is again a contradiction; therefore, the invariant _c_[+] ( _ξ_ 0) is distinct from the one of all the other structures on _−Y_ . □ 

We summarise the shrinking process that lead us to the family of manifolds without tails. We started from the set of all Seifert fibred spaces whose base orbifold is a sphere; among these we first restrict to the ones with indefinite standard graph, as we already classified the negative twisting structures in the other cases, see [8, Theorem 1.1] and Theorem 4.1. As we mentioned in Remark 3.9, we do not consider indefinite _L_ -spaces because they do not carry such kind of structures. By examining the standard graph, we exclude manifolds of type B: the ones whose graph contains a subgraph isomorphic to one in Figure 6; we then compute the twisting numbers and observe that we do not need to consider manifolds with a unique twisting number: for these Proposition 1.4 shows that the classification is the one already given in Proposition 5.5. Finally, the condition on tw( _−Y_ ) identifies our minimal manifolds, the ones whose standard graph is simple enough to prove Theorem 6.4; for a generic _−Y_ the same result requires Lemma 6.3, this is included in Proposition 6.7. 

**Remark 6.6** _The fact that −Y has at most two negative twisting numbers can be extended to any manifold of type A by applying Lemma 6.3._ 

From Lemma 6.3 we know that _−Y_ can be obtained performing surgery on an _M_ without tails. This surgery can be done in the contact setting in all tight structures on _M_ . As we have described the structures with the highest twisting number tw( _−Y_ ) for any _−Y_ already in Section 5, we restrict here to _M_ equipped with the unique structure _ξ_ 0 with twisting number tw( _M_ ), which is tangent to the fibres by [31, Theorem 8.7]. Going from _M_ to _−Y_ we perform surgery on push-offs of its singular fibres. Using notation from the proof of Lemma 6.3, we have that _M_ has Seifert coefficients [ _m[i]_ 1 _[, ..., m][i] hi−_ 1[]][,][while][the][corresponding][best][upper][approximations] equals [ _m[i]_ 1 _[, ..., m][i] hi−_ 1 _[, n][i] hi_[]][and][the][Seifert][coefficient][of] _[−][Y]_[to][[] _[m][i]_ 1 _[, ..., m][i] hi−_ 1 _[, m][i] hi[, ..., m] k[i] i_[]][with] _m[i]_[This means that the contact framing of the] _[ i]_[-th singular fibre in][ (] _[M, ξ]_[0][)][ is exactly] _[ n][i] hi[> n] h[i] i_[.] _hi_ and as _m[i]_[can][realise][the][desired][surgery][as][Legendrian][surgery.][The][obtained][contact] _hi[< n] h[i] i_[we] structures differ by the Spin _[c]_ -structures on the symplectic cobordism and therefore by contact invariant. Comparing to the upper bound, we complete the classification realising that there are no other negative twisting structures on _−Y_ . 

**Proposition 6.7** _Suppose that −Y is a manifold of type A. A negative-twisting tight contact structure on −Y is either isotopic to one of the_ tw( _−Y_ ) _-structures, obtained by complete blowdown of_ Γ _[∗] , or to a_ tw( _−Y_ ) _-structure, obtained by a negative contact surgery on (some) fibres of the corresponding manifold M without tails equipped with its unique structure tangent to the fibres. In particular, all the negative-twisting structures on −Y are symplectically fillable._ 

_Proof._ We notice that the number of constructed structures in both families exactly agrees with predicted upper bound as computed in Subsection 6.1. Indeed, for tw( _−Y_ )-structures the proof is 

39 

the same as in the negative definite case [8, Proposition 5.1]; for tw( _−Y_ )-structures, obtained by Legendrian surgery on tails, we directly see that there are exactly ( _n[i] hi[−][m] h[i] i_[)] _[·]_[ �] _[k] j_ = _[i] hi_ +1 _[|][m][i] j_[+ 1] _[|]_ choices of stabilisations. All structures are symplectically fillable: the tw( _−Y_ )-structures are Stein fillable as proved in Section 5 and the tw( _−Y_ )-structures are obtained by Legendrian contact surgery from the tangent contact manifold ( _M, ξ_ 0) which is symplectically fillable by Proposition 6.5. □ 

Regarding the contact invariant of _ξ_ , we can already prove the following result. 

**Corollary 6.8** _If ξ is a negative-twisting structure on the manifold −Y of type A then c_[+] ( _ξ_ ) _∈ HF_ red( _Y,_ s _ξ_ ) _._ 

_Proof._ Again from Lemma 5.3 we know that the claim holds when _ξ_ satisfies tw( _−Y, ξ_ ) = tw( _−Y_ ), while from Proposition 6.5 when _−Y_ is without tails. When _−Y_ has tails there is a cobordism map _F_[+] : _HF_[+] ( _Y,_ s _ξ_ ) _→ HF_[+] ( _−M,_ s _ξ_ 0) by Proposition 6.7, induced by Legendrian surgery, where _ξ_ 0 is tangent to the fibres of a manifold _M_ without tails. It is a property of Heegaard Floer maps that if _c_[+] ( _ξ_ ) = Θ[+] s _ξ_[then] _[F]_[ +][(] _[c]_[+][(] _[ξ]_[)) =] _[ c]_[+][(] _[ξ]_[0][)] _[ ̸]_[= 0][,][because][(] _[M, ξ]_[0][)][is][symplectically][fillable,] and _c_[+] ( _ξ_ 0) = Θ[+] s _ξ_ 0[,][which][is][not][possible][by][Proposition][6.5.] □ 

Suppose that ( _−Y, ξ_ ) is as in Proposition 6.7, and satisfies tw( _−Y, ξ_ ) = tw( _−Y_ ) _<_ tw( _−Y_ ). Since the structure is fillable, we have that _c_[+] ( _ξ_ ) is non-zero; moreover, we have that _c_[+] ( _ξ_ ) cannot be expressed as _T_ [ _V_ ] for any realised characteristic vector. Lemma 5.6 and Corollary 6.8 then tell us that _c_[+] ( _ξ_ ) = _T_ [ _V_ 1] + _T_ [ _V_ 2] + _· · ·_ is in _HF_ red( _Y,_ s _ξ_ ), where _V_ 1 and _V_ 2 are distinct realised characteristic vectors, both inducing s _ξ_ on _−Y_ and such that _M_ ( _V_ 1) = _M_ ( _V_ 2). 

6.3. **Manifolds of type B.** For this type of Seifert fibred spaces there can be more than two possible negative twisting numbers; however, all the structures can be described using an explicit procedure which is based on the case of _−_ Σ(2 _,_ 3 _,_ 6 _k −_ 1) done in [22] by Ghiggini and Van HornMorris, their argument has been also applied in [51] for _−_ Σ(2 _,_ 3 _,_ 6 _k_ + 1). 

Let Γ _[∗]_ be the standard graph of _−Y_ of type B. Fix _G ⊂_ Γ _[∗]_ a subgraph isomorphic to one of a torus bundle in Figure 6. We say that _−Y_ is _short_ when for each leg of Γ _[∗]_ there is at most one vertex which is not in _G_ . We now briefly sketch the procedure for a short manifold _−Y_ of type B; at the end of section we show that the general case follows easily. 

Given _M_ a Seifert fibred torus bundle over a circle, from [27] we know that the negative-twisting structures on _M_ are all obtained by adding Giroux torsion along a fibre, starting from the unique Stein fillable structure _ζ_ 0 obtained by blowing down the standard graph. For every s _∈_ Spin _[c]_ ( _−Y_ ) we denote by _ξl_ for _l_ = 1 _, ..., k_ the structures on ( _−Y,_ s) with twisting number equal to tw( _−Y_ ); hence, the integer _k_ is the number of realised characteristic vectors inducing s. We construct _ξab_ for 1 ⩽ _a < b_ ⩽ _k_ on ( _−Y,_ s), forming a pyramid of size _k_ as in Figure 3, as follows: add _b − a_ times Giroux torsion to _ζ_ 0, then _ξab_ is gotten from the latter structure, which is weakly fillable [12], by performing ( _−_ 1)-contact surgery on an _ℓ_ -component link made by the vertices in Γ _[∗] \ G_ . 

Any graph _G_ in Figure 6 represents the torus bundle _M_ by capping off the regular fibre of any Seifert fibred space _M[′]_ obtained by removing one leg from _G_ . We can then compute the size of the exceptional orbit in the resulting monodromy, as the regular fibre of _M[′]_ is a knot with Seifert fibred complement and thus produces a periodic monodromy on the torus. The regular fibre of _M_ corresponds to a regular orbit; therefore, its size is determined by lcm(a1 _,_ a2 _, ..._ ) where the a _i_ ’s are the denominators of the Seifert coefficients of _M_ . These numbers are crucial for the procedure that we are going to describe; hence, we write them in Table 3. 

Let _B_ = ( _b_ 1 _, ..., b|_ Γ _∗|_ ) be the vector such that _bl_ is either zero when _Sl ∈ G_ , or the number in the corresponding column of Table 3 otherwise. Note that Γ _[∗]_ may have more legs than _G_ ; hence, 

40 

|_M_|1st leg|2nd leg|3rd leg|4th leg|Regular fbre|
|---|---|---|---|---|---|
|_M_(_−_1; 1<br>2_,_ 1<br>3_,_ 1<br>6)<br>_M_(_−_2; 1<br>2_,_ 2<br>3_,_ 5<br>6)<br>_M_(_−_1; 1<br>2_,_ 1<br>4_,_ 1<br>4)<br>_M_(_−_2; 1<br>2_,_ 3<br>4_,_ 3<br>4)<br>_M_(_−_1; 1<br>3_,_ 1<br>3_,_ 1<br>3)<br>_M_(_−_2; 2<br>3_,_ 2<br>3_,_ 2<br>3)<br>_M_(_−_2; 1<br>2_,_ 1<br>2_,_ 1<br>2_,_ 1<br>2)|3<br>3<br>2<br>2<br>1<br>1<br>1|2<br>2<br>1<br>1<br>1<br>1<br>1|1<br>1<br>1<br>1<br>1<br>1<br>1|–<br>–<br>–<br>–<br>–<br>–<br>1|6<br>6<br>4<br>4<br>3<br>3<br>2|



Table 3. The number of fixed points of the monodromy of the regular fibre of _M_ , and _M[′]_ for each choice of the leg to remove. We order the legs as in Figure 6. 

this means that we may still have additional vertices which are attached to the centre of Γ _[∗]_ but that are not in _G_ . 

**Lemma 6.9** _Let −Y be of type B and short, and V_ 1 _, ..., Vk ∈_ Char(Γ _[∗] ,_ s) _the realised characteristic vectors. Assume that F_ ( _V_ 1) _< · · · < F_ ( _Vk_ ) _, then V j_ + _k_ +1 = ( _j_ + _k −_ 1) _B_ + _V_ 1 _for j ∈{_ 1 _− k,_ 3 _−_ 2 _k, ..., k −_ 1 _}; moreover, one has that M_ ( _V_ 1) = _· · · M_ ( _Vk_ ) _._ 

_Proof._ Since there are finitely many cases, as we have seven torus bundles and the combinatorics of the vertices is exhausted by Table 3, we can check by hand that if the _Vi_ ’s are realised and induce the Spin _[c]_ -structure s then their coordinates should satisfy the relation in the statement. We can then write each _V_ 1 _, ..., Vk_ as _Vσ_ ( _j_ ) where _σ_ ( _j_ ) = _[j]_[+] _[k]_ 2[+][1] , while _|j|_ ⩽ _k −_ 1 and _j_ + _k ≡_ 1 mod 2. To show that all the vectors have the same Maslov grading, we need that _Vσ[T]_ ( _j_ +1) _[Q] ∗[−]_[1] _[V] σ_ ( _j_ +1)[=] _Vσ[T]_ ( _j_ ) _[Q] ∗[−]_[1] _[V] σ_ ( _j_ )[,][and][then][that][(] _[V] σ_ ( _j_ )[+] _[ B]_[)] _[T][ Q][−] ∗_[1] _[B]_[=][0][for][each] _[j]_[.][Again][because][we][are][dealing] with a finite number of cases, we can check that _Q[−] ∗_[1] _[B]_[=][(] _[b][′]_ 1 _[, ..., b][′] |_ Γ _[∗] |_[)][where] _[b][′] l_[=][0][if] _[l][∈]_[Γ] _[∗][\][ G]_ and the vector _B[′]_ obtained by removing these _|_ Γ _[∗] \ G|_ components from _Q[−] ∗_[1] _[B]_[is in][ Ker] _[ Q][G]_[.][Since] each _Vσ_ ( _j_ ) coincides with _W_ can, the canonical vector of _G_ , on _G_ , we are only left to show that _W_ can _[T][B][′]_[= 0][for][each][one][of][the][seven][possible] _[G]_[;][the][vector] _[W]_[can][induces][an][s][0][with][torsion][first] Chern class, thus there exists a _W_ such that _QGW_ = _W_ can and _W_ can _[T][B][′]_[=] _[W][ T][ Q][G][B][′]_[=][0][.][Note] that in [20, Theorem 3.12] Ghiggini proves this result for _−_ Σ(2 _,_ 3 _,_ 6 _k −_ 1) geometrically. □ We now need to specify a different notation in order to simplify the construction; we do this mainly because we often reference [22] and we prefer to keep the notation introduced by Ghiggini and Van Horn-Morris to avoid confusion for the reader. We write _M_ **[n]** where **n** = ( _n_ 1 _, ..., nℓ_ ) for the manifold _−Y_ such that _nl_ is the absolute value of the framing of the _l_ -th vertex in Γ _[∗] \ G_ ; for each s _∈_ Spin _[c]_ ( _M_ **[n]** ) we then denote _ξ_ 1 _, ..., ξk_ (s _,_ **n** ) by _η_ 0 **[n]** _, j_[and][we][take] _[j]_[from][Lemma][6.9][applied] to _M_ **[n]** . Note that we know from the previous subsection that _η_ 0 **[n]** _, j_[is][obtained][by][Legendrian] surgery on the blow-down of Γ _[∗]_ and _c_[+] ( _η_ 0 **[n]** _, j_[)][=] _[T]_[[] _[V] σ_ ( _j_ )[]][where] _[σ]_[(] _[j]_[)][:=] _[j]_[+] _[k]_[(][s] 2 _[,]_ **[n]**[)+][1] . In addition, we denote the _ξab_ ’s as _ηi, j_ **[n]**[for][integers][1][⩽] _[i]_[=] _[b][ −][a][<][k]_[(][s] _[,]_ **[ n]**[)][and] _[|][j][|]_[⩽] _[k]_[(][s] _[,]_ **[ n]** _[′]_[)] _[ −]_[1][such][that] _j_ + _k_ (s _,_ **n** _[′]_ ) _≡_ 1 mod 2, where **n** _[′]_ = **n** _− iB_ . **Remark 6.10** _It is easy to check that k_ (s _,_ **n** _− iB_ ) _coincides with k_ (s _,_ **n** ) _− i. In addition, if ι is the maximal i such that ηi,j_ **[n]** _[exists][then][k]_[(][s] _[,]_ **[ n]** _[′]_[)][=] _[k]_[(][s] _[,]_ **[ n]** _[ −][ιB]_[)][=][1] _[;][in][fact,][from][Lemma][6.9] we would have V_ 1 _, V_ 2 _realised by η_ 0 **[n]** _,j[′]_ 1 _[and][η]_ 0 **[n]** _,j[′]_ 2 _[on][M]_ **[n]** _[′][such][that][V]_[2] _[ −][V]_[1][= 2] _[B][,][and][then][enough]_ 

41 

_choice to construct a structure ηι_ **[n]** +1 _,j[on][M]_ **[n]** _[.][This][is][consistent][with][the][fact][that][the][contact] structures {ηi,j_ **[n]** _[}][form][a][pyramid][of][size][k]_[(][s] _[,]_ **[ n]**[)] _[for][each]_[s] _[ ∈]_[Spin] _[c]_[(] _[M]_ **[n]**[)] _[.]_ 

We observe that in [22] we have _ℓ_ = _|_ Γ _[∗] \ G|_ = 1 and _−_ **n** is equal to one less than the tbnumber of the Legendrian realisation of the vertex, while _j_ coincides with the rotation number. This correspondence would not hold directly here, as when we blow down, the coordinates of _Vj_ , as well as the framing of the surgery, change according to the strict transform, see Theorem 5.4. This is the reason why we symmetrise _j_ . 

Denote by ( _M, ζi_ ) the structure obtained by adding Giroux torsion _i_ -times to _ζ_ 0. It is known that the contact invariant � _c_ ( _ζi_ ) vanishes, while � _c_ ( _ζ_ 0) does not as _ζ_ 0 is Stein fillable. Since we want to use _ζi_ to define the structures _ηi, j_ **[n]**[,][we][use the][same strategy from][[22] and][work with] _HF_[�] with twisted coefficients [43]. We refer to [22] for more details about the construction. 

Ozsváth and Szabó define Heegaard Floer homology with twisted coefficients as a module over the group algebra F[ _H_[1] ( _M_ ; Z)]; in particular, whenever _M_ is a rational homology sphere the action of the group algebra vanishes, meaning that this construction only gives more information when _b_ 1( _M_ ) _>_ 0. In our case, we take _M_ as the torus bundle over the circle represented by _G_ . The only module that we consider, as in [22], is Λ := F[ _H_[1] ( _M_ ;[Z] 2[)]][,][which][we][identify][with][the] 1 ring of the Laurent polynomials F[ _t_ 2 _, t[−]_ 2[1] ]. We denote this homology group by _HF_[�] ( _M_ ). 

It is proved [44] that there is a twisted contact invariant � _c_ ( _ζi_ ) which is defined as an equivalence _[ℓ]_ class in _HF_[�] ( _M,_ s _ζi_ ) up to multiplication for an invertible element _t[±]_ 2 with _ℓ ∈_ Z; moreover, such an invariant is non-vanishing when a structure is weakly fillable, as _ζi_ is. We denote by s0 the spin structure on _M_ which supports _ζi_ for every _i_ ⩾ 0. We also recall that from [43] and [22, Sections 3 and 4] we have Stein cobordisms ( _V_ **n** _, J_ **n** ) induced by the Legendrian surgery on a Legendrian realisation of the link _F ⊂ M_ , represented by the vertices in Γ _[∗] \ G_ , and ( _W, J_ ) from ( _M, ζi_ +1) to ( _M, ζi_ ) which reduces Giroux torsion by one, which give the following maps 

� � _F_ ~~_V_~~ **n** _,J_ **n**[:] _HF_[�] ( _−M_ **[n]** _,_ s) _−→ HF_[�] ( _−M,_ s0) and _F W,J_[:] _HF_[�] ( _−M,_ s0) _−→ HF_[�] ( _−M,_ s0) where � 1 _F_ ~~_W_~~ _,J_[(] _[α]_[) = (] _[t]_ 2 + _t[−]_ 2[1] ) _· α_ for any _α ∈ HF_[�] ( _−M,_ s0) _._ (6.6) In addition, we have that _F_[�] ~~_V_~~ **n** _,J_ **n**[(][�] _[c]_[(] _[η] i, j_ **[n]**[))][=][�] _[c]_ ( _ζi_ ) for every _j_ such that _|j|_ ⩽ _k_ (s _,_ **n** ) _− i −_ 1 and � _j_ + _k_ (s _,_ **n** ) _≡ i_ + 1 mod 2, the invariant _c_ ( _ζ_ 0) is a generator of _HF_[�] ( _−M,_ s0), and _F_[�] ~~_W_~~ _,J_[(][�] _[c]_ ( _ζi_ )) = � _c_ ( _ζi_ +1); moreover, according to the argument in [22, Lemma 4.13], the involution _J_ , which acts as _t �→ t[−]_[1] , together with the fact that each _ζi_ for _i_ ⩾ 0 is self-conjugate can be used to remove the ambiguity in the definition of the twisted cobordism maps in [43]. We can compute _HF_[�] ( _M,_ s0) for each of the seven torus bundle over the circle. This is done in [22, Lemma 4.9] for _M_ ( _−_ 1 _,_[1] 2 _[,]_[1] 3 _[,]_[1] 6[)] _[≃][S]_ 0[3][(] _[T]_[2] _[,]_[3][)][using][the][exact][triangle][with][twisted][coefficients] [43]. The same argument applies here, we give a brief description in the following lemma. 

**Lemma 6.11** _For each M as above we have that HF_[�] ( _M,_ s0) _≃_ Λ _∗ ⊕_ Λ _∗−_ 1 _; moreover, the contact_ � _invariant c_ ( _ζ_ 0) _can be identified with_ [1] _⊂{_ 0 _} ⊕_ Λ _−∗ ⊂ HF_[�] ( _−M,_ s0) _. The values of the Maslov grading are listed in Table 4._ 

_Proof._ � We use the full path algorithm, which holds for _M_ as we know from Section 2, to compute _HF_ ( _M_ ) first, see Table 4. At this point we apply the exact triangle 

**==> picture [272 x 57] intentionally omitted <==**

42 

|_M_|Full paths|_M_(_V_)|�<br>_HF ∗_(_M_)|�<br>_HF_<br>~~_∗_~~(_M,_s0)|
|---|---|---|---|---|
|_M_(_−_1; 1<br>2_,_ 1<br>3_,_ 1<br>6)|(1_,_0_, −_1_, −_4)|_−_1<br>2|F_−_1<br>2 _⊕_F_−_3<br>2|Λ_−_1<br>2 _⊕_Λ_−_3<br>2|
|_M_(_−_2; 1<br>2_,_ 2<br>3_,_ 5<br>6)|(0_,_0_,_0_,_0_,_0_,_0_,_0_,_0_,_0)|3<br>2|F 3<br>2 _⊕_F 1<br>2|Λ 3<br>2 _⊕_Λ 1<br>2|
|_M_(_−_1; 1<br>2_,_ 1<br>4_,_ 1<br>4)|(1_,_0_, −_2_, −_2)<br>(_−_1_,_0_,_0_,_4)|_−_1<br>4<br>_−_3<br>4|F 1<br>4 _⊕_F_−_1<br>4 _⊕_F_−_3<br>4 _⊕_F_−_5<br>4|Λ_−_1<br>4 _⊕_Λ_−_5<br>4|
|_M_(_−_2; 1<br>2_,_ 3<br>4_,_ 3<br>4)|(0_,_0_,_0_,_0_,_0_,_0_,_0_,_0)<br>(_−_2_,_0_,_0_,_0_,_2_,_2_,_0_,_0)|5<br>4<br>_−_1<br>4|F 5<br>4 _⊕_F 3<br>4 _⊕_F 1<br>4 _⊕_F_−_1<br>4|Λ 5<br>4 _⊕_Λ 1<br>4|
|_M_(_−_1; 1<br>3_,_ 1<br>3_,_ 1<br>3)|(1_, −_1_, −_1_, −_1)<br>(_−_1_,_3_,_1_, −_1)<br>(_−_1_,_3_, −_1_,_1)|0<br>_−_2<br>3<br>_−_2<br>3|F2<br>1<br>3 _⊕_F0_⊕_F2<br>_−_2<br>3 _⊕_F_−_1|Λ0_⊕_Λ_−_1|
|_M_(_−_2; 2<br>3_,_ 2<br>3_,_ 2<br>3)|(0_,_0_,_0_,_0_,_0_,_0_,_0)<br>(_−_2_,_0_,_0_,_0_,_2_,_2_,_0)<br>(_−_2_,_0_,_2_,_0_,_0_,_2_,_0)|1<br>_−_1<br>3<br>_−_1<br>3|F1_⊕_F2<br>2<br>3 _⊕_F0_⊕_F2<br>_−_1<br>3|Λ1_⊕_Λ0|
|_M_(_−_2; 1<br>2_,_ 1<br>2_,_ 1<br>2_,_ 1<br>2)|(0_,_0_,_0_,_0_,_0)<br>(_−_2_,_2_,_2_,_0_,_0)<br>(_−_2_,_2_,_0_,_2_,_0)<br>(_−_2_,_2_,_0_,_0_,_2)|1<br>2<br>_−_1<br>2<br>_−_1<br>2<br>_−_1<br>2|F4<br>1<br>2 _⊕_F4<br>_−_1<br>2|Λ 1<br>2 _⊕_Λ_−_1<br>2|



Table 4. The Heegaard Floer homology of the seven torus bundles in Figure 6. Note � thatfull paths _c_ ( _ζ_ 0) contain= _T_ [ _W_ canloops.] whereIn _W_ addition,can is thewefirsthavevectorthat for _M_ (� _c_ each( _ζ_ 0)) = _M −_ in _d_ the3( _ζ_ 0table,) = _−M_ all( _W_ thecanother). 

with both untwisted and twisted coefficients. The manifold _M[′′]_ is obtained by increasing by one the framing of the last leg of _G_ , while _M[′]_ is the one presented by the graph _G_ without the last leg; note that _M[′′]_ and _M[′]_ are _L_ -spaces. In the first case we obtain that the map _F_ is zero by counting the dimension of the groups; in addition, in the second case, where the corresponding 1 map is _F ⊗_ Λ by [22, Theorem 3.2], this immediately implies that _HF_[�] ( _M_ ) _≃ HF_[�] ( _M_ )[ _t_ 2 _, t[−]_ 2[1] ]. We obtain the first claim by observing that the gradings of the other two maps are the same in both cases. 

Regarding the second claim, we know [44] that _M_ ( _ζ_ 0) = _−d_ 3( _ζ_ 0) because s0 is spin, and then _c_ 1(s0) is torsion; in particular, the contact invariant has a well-defined Maslov grading. It follows from the discussion above and the computation in Table 4 that � _c_ ( _ζ_ 0) lives in the unique summand of _HF_[�] ( _−M,_ s0) with the correct grading. □ 

It is described in [22] that both the Legendrian surgeries above can be done at the same time on the Legendrian link _L ∪C_ in ( _M, ζi_ +1), where _L_ is a Legendrian realisation of _F_ and _C_ the link in [22, Figure 3]. There, the link _C_ is shown only for _M ≃ S_ 0[3][(] _[T]_[2] _[,]_[3][)][,][but][Van][Horn-Morris] presents equivalent constructions for every torus bundle in his thesis, see [52]. This implies that 

43 

we have the following commutative diagram 

**==> picture [318 x 72] intentionally omitted <==**

where s _[′]_ is the Spin _[c]_ -structure induced by any realised characteristic vector _Vσ_ ( _j_ ) + _B_ and **m** = **n** + _B_ . We need to argue that the manifold appearing in the upper right corner is indeed ( _M_ **[m]** _,_ s _[′]_ ). 

In [22, Section 4] the link _L∪C_ appears on a page of a genus one abstract open book decomposition ( _S, ϕ_ ) for _M_ , compatible with _ζi_ +1; more specifically, Ghiggini and Van Horn-Morris describe how to read the monodromy of the torus bundle from the given open book in [22, Figure 3]. In their paper _L_ is a knot; hence, it is drawn as a longitude _F_ of the (punctured) torus _S_ . In our case _L_ is a link, whose monodromy is obtain as a product of the one of _F_ ; it follows that each component of _L_ appears on _S_ as a multiple of _F_ , according to Table 3. 

It is known that ( _−_ 1)-contact surgery on a contact 3-manifold can be seen by adding positive right-handed Dehn twists to the monodromy of a compatible open book. Therefore, the manifold obtained by doing Legendrian surgery on _L ⊂_ ( _M, ζi_ +1) is identified by lowering the smooth surgery framings precisely by _bl_ on each component of _L_ , where _bl_ is the corresponding coordinate of _B_ . This can be seen in the same way as in [22, Proposition 4.1]. 

_j_ **Remark 6.12** _From_ [22, Lemma 4.12] _we have that F_[�] ~~_V_~~ **n** _,J_ **n**[(] _[η]_ 0 **[n]** _,j_[) =] _[ t]_ 2 _for every |j|_ ⩽ _k_ (s _,_ **n** ) _−_ 1 � _and j_ + _k_ (s _,_ **n** ) _≡_ 1 mod 2 _, and maps each c_ ( _ηi,j_ **[n]**[)] _[to][the][contact][invariant]_[�] _[c]_[(] _[ζ][i]_[)] _[whose][Maslov] grading does not depend on i, because of Lemma 6.11. Since_ Spin _[c] -cobordism maps have welldefined degree shift, we have that every structure ηi,j_ **[n]** _[has][the][same][d]_[3] _[-invariant:][it][is][a][standard] result in contact topology that this and the induced_ Spin _[c] -structure determine the homotopy type of the structure. Furthermore, Lemma 5.3 implies that c_[+] ( _ηi,j_ **[n]**[)] _[ ∈][HF]_[red][(] _[−][M]_ **[n]** _[,]_[ s][)] _[.]_ 

Based on the previous discussion, we can now use an inductive argument to find how to express � _c_ ( _ηi,j_ **[n]**[)][in][terms][of][the][homology][classes] _[{][T]_[[] _[V]_ 1[]] _[, ..., T]_[[] _[V] k_ (s _,_ **n** )[]] _[}]_[=] _[{]_[�] _[c]_[(] _[η]_ 0 **[n]** _,j_[)] _[}]_[in] _HF_[�] od( _−M_ **n** _,_ s). Note that these elements are linearly independent from Theorem 2.1; moreover, as we mentioned in od Subsection 5.1, there is a (canonical) isomorphism between _HF_[�] and _HF_ red _∩_ Ker _U_ . 

� **Corollary 6.13** _The contact invariant c_ ( _ηi,j_ **[n]**[)] _[is][equal][to]_[�] _[c]_[(] _[η] i_ **[n]** _−_ 1 _,j−_ 1[)+][�] _[c]_[(] _[η] i_ **[n]** _−_ 1 _,j_ +1[)] _[in] HF_[�] ( _−M_ **[n]** _,_ s) _for any_ 0 _< i < k_ (s _,_ **n** ) _and j such that |j|_ ⩽ _k_ (s _,_ **n** ) _− i −_ 1 _and j_ + _k_ (s _,_ **n** ) _≡ i_ + 1 mod 2 _. Proof._ The proof is based on the one of [22, Theorem 1.3]. Let **o** = **n** _− B_ , and note that because we are assuming _i >_ 0 then _k_ (s _,_ **n** ) ⩾ 2 thus the manifold _M_ **[o]** exists. We start with _i_ = 1: from Equation (6.6), Diagram (6.7) and Remark 6.12 we have that 

**==> picture [429 x 41] intentionally omitted <==**

**==> picture [206 x 17] intentionally omitted <==**

The fact that � _c_ ( _ζ_ 1) is non-zero implies that � _c_ ( _η_ 1 **[n]** _,j_[)][is][non-zero][and][by][Remark][6.12][and][Lemma] od **n** 5.6 we obtain that the latter is a linear combination of the subgroup of _HF_[�] ( _M ,_ s) generated by _T_ [ _V_ 1] _, ..., T_ [ _Vk_ (s _,_ **n** )]. We conclude by observing that the map _F_[�] ~~_V_~~ **n** _,J_ **n**[is][injective][by][construction] on this subgroup. 

44 

We finish with the inductive step when _i >_ 1: 

**==> picture [460 x 110] intentionally omitted <==**

We finish the section by showing that the number of negative-twisting structures on any _−Y_ of type B equals the upper bound, see Subsection 6.1. 

**Proposition 6.14** _Suppose that −Y is a manifold of type B. Then a negative-twisting tight contact structure on −Y is isotopic to ηi,j_ **[n]** _[for][some]_[s] _[ ∈]_[Spin] _[c]_[(] _[−][Y]_[ )] _[.][Furthermore,][such][structures][are][all] symplectically fillable and distinguished by their contact invariant c_[+] _∈ HF_ red _._ 

_Proof._ We recall hat each structure _η_ 0 **[n]** _,j_[is][obtained][by][blowing][down][Γ] _[∗]_[.][We][start][by][assuming] that _−Y_ = _M_ **[n]** is short; hence we have that _{ηi,j_ **[n]** _[}]_[ is a pyramid for each][ s] _[ ∈]_[Spin] _[c]_[(] _[M]_ **[n]**[)][ by Remark] 6.10. We saw that any such structure is obtained by ( _−_ 1)-contact surgery on a Legendrian knot in a weakly fillable manifold, namely ( _M, ζi_ ); therefore, they are weakly fillable themselves, and then strongly fillable as _M_ **[n]** is a rational homology sphere. In addition, the fact that these structure have pairwise distinct _c_[+] can be seen from Corollary 6.13, as each one can be expressed by a different linear combination of _{_ � _c_ ( _η_ 0 **[n]** _,j_[)] _[}]_[.] 

We have to show that the number of the structures of the form _ηi,j_ **[n]**[,][among][every][s][on] _[M]_ **[ n]**[,] coincides with the upper bound in Subsection 6.1. We first observe the following: from GhigginiMassot’s algorithm the twisting numbers on each _G_ are in an arithmetic progression of ratio k := lcm(a1 _,_ a2 _, ..._ ); meanwhile, the structures as _η_ 0 **[n]** _,j_[are][precisely][the][ones][with][twisting][number] equal to tw( _M_ **[n]** ) and there are as many as the upper bound, see Propositions 1.4 and 6.5, and [8, Proposition 5.1]. We proceed by induction on the maximal size of a pyramid of _M_ **[n]** . 

If there is only one layer then the proof follows as said above. Suppose that there is more than one layer; then we consider each twisting number _−q_ separately. If _−q_ = tw( _M_ **[n]** ) then we are done for the same reason. Since the number of the structures _ηi,j_ **[n]**[coincides with the ones in] _[ η] i_ **[o]** _−_ 1 _,j_ where **o** = **n** _− B_ , and this holds for every Spin _[c]_ -structure, we just have to prove that the upper bound for _−q_ on _M_ **[n]** equals the upper bound for _−q_ + k on _M_ **[o]** ; we then conclude by induction. From Subsection 6.1 we know that we can compute the upper bound leg-by-leg (we only care about the ones where there is a vertex in Γ _[∗] \ G_ ) by comparing the resulting continued fractions for _ri_ and _[p] q[i]_[,][for] _[M]_ **[ n]**[,][and] _[r] i[′]_[and] _qp−[′] i_ k[,][for] _[M]_ **[ o]**[.][Since][tw][(] _[M]_ **[ a]** _[, η] i,j_ **[a]**[)][=][tw][(] _[M, ζ][i]_[)][for][every] **[a]**[as][in] [22, Proposition 2.7], one has that _[p] q[i]_[and] _qp−[′] i_ k[are][also][the][best][upper][approximations][for][r] _[i]_[=][b] a _i[i]_[,] the _i_ -th Seifert coefficient of the torus bundle _M_ . We assume _q −_ k _>_ 1, the other case is similar. We have _− r_[1] _i_[=][[] _[m][i]_ 1 _[, ..., m][i] ki_[]][and] _[−] p[q] i_[=] [ _m[i]_ 1 _[, ..., m][i] ki−_ 1 _[, n][i] ki_[]][where] _[n][i] ki[>][m][i] ki_[.][Then][one][gets][precisely] _[−] r_[1] _i[′]_[=][[] _[m][i]_ 1 _[, ..., m][i] ki_[+] _[ b][i]_[]][,][where] _bi_ = a[k] _i_[is][the][corresponding][number][in][Table][3,][and] 

**==> picture [460 x 68] intentionally omitted <==**

45 

If _−Y_ is not short then it is obtained by Legendrian contact surgery on (some) fibres of a short manifold of type B, exactly as in the case of manifolds of type A with tails. Hence, the claims in the statement are obtained with the same arguments of Proposition 6.7 and Corollary 6.8. □ 

It follows that the contact invariant of _ηi,j_ **[n]**[is][always][a][linear][combination][of] _[T]_[[] _[V]_ 1[]] _[, ..., T]_[[] _[V] k_ (s _,_ **n** )[]][,] the realised characteristic vectors in Char(Γ _[∗] ,_ s). In Section 7 we determine the coordinates of _c_[+] exactly, depending on the parity of _k_ (s _,_ **n** ). 

7. The correspondence with Heegaard Floer homology 

From our exposition so far we deduce the following corollary for a _−Y_ whose standard graph Γ _[∗]_ has _b_[+][to][1.] 2[equal] 

**Corollary 7.1** _Every negative-twisting structure ξ on −Y is symplectically fillable; moreover, negative-twisting structures are precisely the ones with_ 0 _̸_ = _c_[+] ( _ξ_ ) _∈ HF_ red( _−Y_ ) _._ 

_Proof._ This follows from Corollary 6.8 and Propositions 5.1, 6.7 and 6.14. □ 

7.1. **The full path determines the twisting numbers.** Let us take the set _{V_ 0 _, ...VS−_ 1 _} ⊂_ Char(Γ _[∗] ,_ scan) of the realised characteristic vectors such that _M_ ( _Vl_ ) = _M_ ( _V_ can) for _l_ = 0 _, ..., S −_ 1, where scan _∈_ Spin _[c]_ ( _−Y_ ) is induced by _V_ can. It follows from the discussion in Section 5 that the _T_ [ _−Vl_ ]’s are the contact invariants of the _ξl_ ’s in Proposition 5.5 homotopic to the structure _ξ_ can; therefore, one has tw( _−Y, ξl_ ) = tw( _−Y_ ). We fix the convention that _V_ 0 is the initial vector of [ _−V_ can], and we compute the values of the possible negative twisting numbers. 

**Theorem 7.2** _There exists a tight structure ξ on −Y such that_ tw( _−Y, ξ_ ) = _−q <_ tw( _−Y_ ) _if and only if q_ = 1+height _F_ ([ _V_ can]+[ _−Vl_ ]) _for l_ = 1 _, ..., S −_ 1 _. In particular, there are S integers which appear as the negative-twisting number of a contact structure on −Y ._ 

In order to prove this result we need to reformulate both sides of the equivalence, which is the content of the following preliminary lemmate. 

Let us first consider a realised characteristic vector _V_ . We write 2 _U_ := _V − V_ can, and we define 

**==> picture [190 x 23] intentionally omitted <==**

where _Q∗_ is the intersection matrix of Γ _[∗]_ . Then 

**==> picture [310 x 14] intentionally omitted <==**

hence, by Proposition 3.1 and Equation (3.1), the vector _V_ is one of the _Vl_ ’s introduced at the beginning of the subsection if and only if _U_ is in the right range (for _V_ to be a realised vector), _X ∈_ Z _[|]_[Γ] _[∗][|]_ (which ensures that _V_ and _−V_ can are the same in Spin _[c]_ ( _−Y_ )), and _U[T] X_ = 0 (so that _M_ ( _V_ ) = _M_ ( _V_ can)). Moreover, when _l ∈{_ 1 _, ..., S −_ 1 _}_ we have 

**==> picture [294 x 14] intentionally omitted <==**

For vertices on the _i_ -th leg we define 

**==> picture [110 x 13] intentionally omitted <==**

then from _Q∗X_ = _V_ can + _U_ one gets for a single leg 

**==> picture [297 x 16] intentionally omitted <==**

for _q_ := 1 _− x_ 1. 

**Lemma 7.3** _When q >_ 1 _we have that U[T] X_ = 0 _if and only if u_ 1 = 0 _and u[i] j_[(] _[z] j[i][−]_[1)][=][0] _[for] each leg and every j_ = 1 _, ..., ki._ 

46 

_Proof._ Because the matrix ( _−Q∗_[(] _[i]_[)][)] _[−]_[1][has strictly positive entries (it is the inverse of an irreducible] positive-definite _M_ -matrix) and the right-hand side of Equation (7.1) has non-negative coordinates, we get _zj[i][>]_[ 0][.][Since] _[Z]_[(] _[i]_[)][is][integral,][this][implies] _[z] j[i]_[⩾][1][and][then] _[x][i] j_[= 1] _[ −][z] j[i]_[⩽][0][for][every] vertex on every leg. In addition, when _q >_ 1 one has _x_ 1 = 1 _− q <_ 0. Since the coordinates of _U_ are non-negative, while the ones of _X_ are non-positive, we have that _U[T] X_ = 0 is equivalent to _u_ 1 = 0 and _u[i] j[x][i] j_[= 0][for][every] _[i]_[and] _[j]_[.] □ 

For each leg _i_ we define 

_pi_ := _z_ 1 _[i]_[= 1] _[ −][x][i]_ 1 

where here the index 1 refers to the attachment vertex of the _i_ -th leg. Then from the first row of _Q∗X_ = _V_ can + _U_ , using _u_ 1 = 0, we get 

**==> picture [380 x 31] intentionally omitted <==**

and then to 

**==> picture [285 x 32] intentionally omitted <==**

In addition, for each leg we write _ri_ = _a[b][i] i_[for][its][positive][reduced][fraction.][A][standard][adjugate] computation on Equation (7.1) yields 

**==> picture [303 x 16] intentionally omitted <==**

where _D_[(] _[i]_[)] := adj( _−Q∗_[(] _[i]_[)][)] _[e]_ 1[has][positive][integer][entries.][This][means] _[a] i[p] i[−][b] i[q][>]_[ 0][and][then] 

**==> picture [66 x 26] intentionally omitted <==**

Combining these observations with Lemma 7.3, in order for a _q_ obtained from the _Vl_ ’s to be a twisting number we need the following reinterpretation of the best upper approximation condition. 

**Lemma 7.4** (Leg lemma) _Assume −Y_ = _M_ ( _e_ 0; _r_ 1 _, ..., rn_ ) _and fix i ∈{_ 1 _, ..., n}. Then for integers_ 1 _< p < q the fraction[p] q[is][the][best][upper][approximation][for][r][i][if][and][only][if][there][exist][vectors] Z, U ∈_ Z _[k][i] such that_ 

- _(1) z_ 1 = _p;_ 

- _(2)_ 0 ⩽ _uj_ ⩽ _uj where_ 2 _uj_ + _m[i] j_[+ 2] _[is][the][maximal][value][of][the][j][-th][coordinate][in][the][i][-th][leg] for a realised characteristic vector as in Theorem 5.4;_ 

_(3) AZ_ = _U_ + _qe_ 1 + _eki where −A_ := _Q∗_[(] _[i]_[)] _is the intersection matrix of the i-th leg of_ Γ _[∗] ; (4) uj_ ( _zj −_ 1) = 0 

_for every j_ = 1 _, ..., ki where ki is the length of the i-th leg._ 

Since the leg lemma concerns a single leg, we opt to skip the leg index _i_ in the notation for simplicity. We still describe the leg as a part of the standard graph in order to keep all the usual assumptions. 

We will prove the Leg lemma by induction on the length of the leg. Let _ri[′]_[be][the][Seifert] coefficient of the linear graph obtained by removing the first vertex from the _i_ -th leg, then we have _− r_[1] _i_[=] _[m][i]_ 1[+] _[ r] i[′]_[.][We][set] _[a][j]_[:=] _[−][m][i] j[>]_[0][for][the][framings][of][the][vertices][in][the] _[i]_[-th][leg.][The] original and cut coefficient are then related by the Möbius transform Φ( _x_ ) = _a_ 1 _− x_[1][which][has] inverse Φ _[−]_[1] ( _y_ ) = _a_ 11 _−y_[,][as] _[r][i]_[= Φ] _[−]_[1][(] _[r] i[′]_[)][.] 

47 

In particular, given _p >_ 1 we have that _[p] q_[is][the][best][upper][approximation][for] _[r][i]_[if][and][only][if] _a_ 1 _p−q_ is for _r[′]_[Indeed,][the][value][of][Φ][on][a][rational][number][is][given][by] _p i_[.] 

**==> picture [142 x 27] intentionally omitted <==**

so the new denominator is _k_ and if we have the restriction _k_ ⩽ _p_ then the new denominator is at most _p_ ; moreover, the restriction _h < q_ becomes a restriction on the new numerator _a_ 1 _k − h_ to be at least _a_ 1 _k −_ ( _q −_ 1). The inequality _ri < h[k][<][p] q_[is][then][equivalent][to] 

**==> picture [164 x 27] intentionally omitted <==**

_Proof of the Leg lemma._ We proceed by induction on the length _ki_ of the leg. Let us assume that _ki_ = 1, then Property (3) becomes _a_ 1 _p_ = _u_ 1 + _q_ + 1 while Property (4) is _u_ 1( _p −_ 1) = 0; this becomes equivalent to _u_ 1 = 0 and then _a_ 1 _p − q_ = 1, which holds if and only if _ri_ = _a_ 11[is][a][Farey] neighbour of _[p]_[For][such] _[r][i]_[the latter][condition][is equivalent][to be the][best][upper][approximation.] _q_[.] Now assume _ki >_ 1: we start with the if implication. By the first row of Property (3) 

**==> picture [275 x 12] intentionally omitted <==**

by Property (2) 0 _≤ u_ 1 _≤ u_ 1, which restricts _z_ 2 to the interval 

**==> picture [150 x 10] intentionally omitted <==**

and from Property (4) we have that _z_ 1 = _p >_ 1 implies _u_ 1 = 0 and _z_ 2 = _a_ 1 _p − q_ . Let _A[′]_ be the chain matrix for _a_ 2 _, . . . , aki_ , and write _Z[′]_ = ( _z_ 2 _, . . . , zki_ ) and _U[′]_ = ( _u_ 2 _, . . . , uki_ ). Then rows 2 _, . . . , ki_ of Property (3) are exactly 

**==> picture [288 x 13] intentionally omitted <==**

so if Properties (1) – (4) hold for ( _q, p_ ) on _A_ then they also hold for ( _p, z_ 2) on _A[′]_ with the bounds _u_ 2 _, . . . , uki_ . We have _z_ 2 = _a_ 1 _p − q_ , thus _[z] p_[2][=] _[a]_[1] _[p] p[−][q]_ = Φ( _[p] q_[)][.][If][there][were][a][forbidden][fraction] _h[k]_ in ( _ri,[p] q_[)][ with] _[ h < q]_[and] _[ k]_[⩽] _[p]_[,][then since] _[ p >]_[ 1][ its transform][ Φ(] _h[k]_[)][ would be a forbidden fraction] in ( _ri[′][,][z] p_[2][)][with][denominator] _[k][<][p]_[,][and][numerator][bounded][appropriately;][that][contradicts][the] inductive hypothesis applied to the cut leg and fraction _[z] p_[2][.] 

We continue by showing the only if implication. We prove the inductive step: assuming the claim is true for chains of length _ki −_ 1 with coefficients _a_ 2 _, . . . , aki_ , we prove it for _a_ 1 _, . . . , aki_ . Since _p >_ 1, we have that _[a]_[1] _[p] p[−][q]_ is the best upper approximation of _ri[′]_[.][By inductive hypothesis we] have _Z[′] , U[′] ∈_ Z _[k][i][−]_[1] satisfying the four properties for the cut leg. Extending to the first coordinate, we set _z_ 1 = _p_ and _u_ 1 = _a_ 1 _p − q − z_ 2 = 0 by Properties (1) and (3) from inductive hypothesis, which clearly fulfil all four conditions. □ 

We state an alternative version of Ghiggini-Massot’s algorithm, so that we can determine possible negative twisting numbers in a more useful way for our applications. 

**Proposition 7.5** _If there exist positive integer numbers p_ 1 _, ..., pn such that_ 

_• p_ 1 + _..._ + _pn_ = _−e_ 0 _q_ + _n −_ 2 _;_ 

_• there are Z_[(] _[i]_[)] _and U_[(] _[i]_[)] _as in the Leg lemma when setting p_ = _pi for i_ = 1 _, ..., n, then the Seifert fibred space −Y_ = _M_ ( _e_ 0; _r_ 1 _, . . . , rn_ ) _admits a tight contact structure with twisting number equal to −q. The converse is also true if each best upper approximation[p] q[i][has][p][i][>]_[ 1] _[.] Proof._ It follows by Theorem 1.3. If _pi >_ 1 for _i_ = 1 _, ..., n_ then we just need a comparison with the Leg lemma; if _pi_ = 1 for some _i_ then the second item still gives us _ri <_[1][and][we][clearly][see] _q_[,] that there are no forbidden rationals in ( _ri,_[1] _q_[)][,][as] _[h]_[ ⩽] _[q]_[is][equivalent][to][1] _q_[⩽] _h_[1][.] □ 

48 

We can now prove Theorem 7.2, but first we need the following lemma to handle some specific cases which are not covered by Proposition 7.5. 

**Lemma 7.6** _Consider a −Y_ = _M_ ( _e_ 0; _r_ 1 _, ..., rn_ ) _such that M_ = _M_ ( _e_ 0; _r_ 1 =[b] a1[1] _[, ..., r][n][−]_[1][=][b] a _n[n] −[−]_ 1[1][)] _[is] a torus bundle as in Figure 6. If −q is a twisting number then we can find a realised characteristic vector V such that, given_ 2 _X_ = _Q[−] ∗_[1][(] _[V]_[+] _[ V]_[can][)] _[and]_[2] _[U]_[=] _[ V][−][V]_[can] _[,][one][has][X][∈]_[Z] _[|]_[Γ] _[∗][|][,][U][T][ X]_[= 0] _and q_ = 1 _− x_ 1 = 1 _− e[T]_ 1 _[X][.] Proof._ As we mentioned in the proof of Proposition 6.14, we have _q_ = _q_ + _k_ k for 0 ⩽ _k_ ⩽ _K_ where k = lcm(a1 _, ...,_ a _n−_ 1), _q_ = _|_ tw( _−Y_ ) _|_ , and _K_ is the maximal integer satisfying _rn <_[1] _q_[.][We] set _V_ = _V_ can except for the coordinates of the _n_ -th leg which are 

**==> picture [200 x 13] intentionally omitted <==**

for 0 ⩽ _k_ ⩽ _K_ where _− r_[1] _n_[= [] _[m]_ 1 _[n][, ..., m][n] kn_[]][.][Note][that][when] _[k]_[= 0][the][first][coordinate][on][the] _[n]_[-th] leg coincides with _−m[n]_ 1 _[−]_[2] _q_ , while when _k_ = _K_ it is equal to 

**==> picture [248 x 12] intentionally omitted <==**

because _−m[n]_ 1[⩾] _q_ + _K_ k + 1, thus _V_ is realised by Theorem 5.4; moreover, one has _[V]_[ +] 2 _[V]_[can] = _V_ can everywhere except on the _n_ -th leg where is equal to (1 _− q − k_ k _,_ 0 _, ...,_ 0), while _U_ is zero except on the _n_ -th leg where is equal to 

**==> picture [204 x 13] intentionally omitted <==**

Using the Schur complement and the fact from the proof of Lemma 6.9 that for each _M_ there exists an integral vector _B[′] ∈_ Ker _QG_ such that _W_ can _[T][B][′]_[= 0][,][where] _[G]_[is][the][standard][graph][of] _[M]_ and _W_ can its canonical vector, from standard linear algebra we obtain 

**==> picture [158 x 24] intentionally omitted <==**

where _QGW_ = _W_ can such that _w_ 1 = 1 _− q − k_ k. Hence, we have that _U[T] X_ = 0 while the vector _W_ , and then _X_ , is integral if and only if _w_ 1 _≡_ 1 + b _[−] i_[1] mod a _i_ for _i_ = 1 _, ..., n −_ 1, which in our case reduces to _q ≡−_ b _[−] i_[1] mod a _i_ , and we can check that the latter congruence is always satisfied: in fact, it does not depend on _k_ but for _k_ = 0 the vector _V_ is the initial vector of [ _−V_ can], and the corresponding _X_ is then certainly integral. 

We now just need to observe that _e[T]_ 1 _[X]_[=] _[ w]_[1][= 1] _[ −] q − k_ k = 1 _− q_ and we are done. □ 

_Proof of Theorem 7.2._ We write _q_ = _|_ tw( _−Y_ ) _|_ . Suppose that _−q_ is defined by the height function. Construct vectors _X_ and _U_ as described immediately after the statement of the theorem, take _q_ = 1 _− x_ 1, and set _pi_ = 1 _− x[i]_ 1[⩾][1][.][By][Lemma][7.3][we][have] _[u]_[1][=][0][,][thus][Equation][(7.2)][holds;] hence, by Proposition 7.5 we know that _q_ is obtained from Ghiggini-Massot’s algorithm, and then is indeed the twisting number of a tight structure on _−Y_ . In addition, when _U_ corresponds to _Vl_ for _l_ = 1 _, ..., S −_ 1 one has that _q_ = 1 + height _F_ [ _V_ can], and then _q_ = _q_ by Proposition 5.5. Suppose now that _−q < −_ 1 is a twisting number, to show that _q_ = 1 _− x_ 1 for some _Vl_ when _pi >_ 1 for _i_ = 1 _, ..., n_ we use Proposition 7.5 to find vectors _Z_[(] _[i]_[)] _, U_[(] _[i]_[)] satisfying Equation (7.1) for each leg. In other words 

**==> picture [258 x 17] intentionally omitted <==**

with 0 ⩽ _u[i] j_[⩽] _u_ ~~_[i]_~~ _j_[and] _[z] j[i]_[⩾][1][for] _[j]_[=][1] _[, ..., k][i]_[.][We][have] _[X]_[(] _[i]_[)][=] **[1]** _[ −][Z]_[(] _[i]_[)][with][non-positive][entries] on the legs, and we set the centre coordinate _u_ 1 = 0. From Equation (7.2) this is exactly what is needed so that the first row of _Q∗X_ = _V_ can + _U_ holds, so we get an integer solution _U_ whose 

49 

entries are in the right range; finally, Lemma 7.3 gives _U[T] X_ = 0. Now set _V_ = _V_ can + 2 _U_ : it is realised by construction, and 

**==> picture [222 x 23] intentionally omitted <==**

with _x_ 1 = 1 _− q_ . Hence, the vector _V_ has the same Maslov grading and induces the same Spin _[c]_ - structure as _−V_ can; this means _V_ = _Vl_ for some _l ∈{_ 0 _, ..., S −_ 1 _}_ . Since the value of _x_ 1 cannot be _−_ height _F_ [ _V_ can], otherwise _q_ = _q_ in light of Proposition 5.5, it has to be _−_ height _F_ ([ _V_ can] + [ _−Vl_ ]) for some _l_ = 1 _, ..., S −_ 1. 

We need to prove the claim when _pi_ = 1 for some _i_ , note that we are assuming that _q_ = _q_ . We cannot have _p_ 3 = 1 if _n_ = 3: this is true because removing _pi_ from Equation (7.2) gives that _q_ would be a twisting number for the lens space whose standard graph is Γ _[∗]_ without the 3rd leg, but by [8, Proposition 4.2] when _n_ = 2 there is only one twisting number (of a regular fibre of the fibration determined by the graph) and ( _p_ 1 _, p_ 2 _,_ 1) gives rise to _−q_ . We can then proceed by induction on the number of _pi_ ’s equal to 1. 

From [8, Proposition 4.2 and Theorem 4.3] we know that if _pi_ = 1 then the _i_ -th leg is not contained in the _S_[3] -subgraph of Γ _[∗]_ , and as we remarked in the proof of Proposition 5.5 their proofs also hold in the indefinite case. Removing the _i_ -th leg yields an indefinite graph, except when _−Y_ is as in Lemma 7.6. To see this we consider the _n_ -tuple ( _p_ 1 _, p_ 2 _,_ 1 _, ...,_ 1) which gives rise to ~~_−_~~ _q_ , and the same is true when we remove one 1. We know that if the new graph is negativedefinite then there is only one twisting number [8, Proposition 4.2], thus we conclude that _q_ = _q_ and this is impossible. If the new graph is singular and not as in Figure 6 then there is still only one twisting number by Proposition 4.4. 

Say _G_ is obtained by removing the _n_ -th leg where _pn_ = 1, by induction there is a realised characteristic vector _V[′]_ such that 2 _X[′]_ := _e[T]_ 1 _[Q][−] G_[1][(] _[V][′]_[ +] _[ V]_ can _[′]_[)] _[∈]_[2][Z] _[|][G][|]_[,][one][has][(] _[V][′][ −][V]_ can _[′]_[)] _[T][ X]_[= 0] and _q_ = 1 _− x[′]_ 1[=][1] _[ −][e][T]_ 1 _[X][′]_[.][We][show][that][if][we][extend] _[X][′]_[to] _[X]_[=][(] _[X][′][,]_[ 0] _[, ...,]_[ 0)][on][the][last][leg] then _V_ = 2 _Q∗X − V_ can satisfies all the properties we want. The integrality condition is automatic as _X[′]_ is integral, we have _x_ 1 = _e[T]_ 1 _[X]_[=] _[ e][T]_ 1 _[X][′]_[=] _[ x][′]_ 1[,][and][(] _[V][−][V]_[can][)] _[T][ X]_[= (] _[V][′][ −][V]_ can _[′]_[)] _[T][ X][′]_[= 0][.][We] need to show that _V_ is realised: its coordinates on the _n_ -th leg are 

**==> picture [186 x 13] intentionally omitted <==**

so we just have to check the first one. Since the best upper approximation for _rn_ is[1][we][have] _q_[,] that _−m[n]_ 1[⩾] _[q]_[ + 1][;][therefore,][we][conclude][that] 

**==> picture [276 x 12] intentionally omitted <==**

which is precisely the range of the possible values for _V_ to be realised, see Theorem 5.4. □ 

This completes the proof that the full path algorithm determines the twisting numbers. 

_Proof of Theorem 1.5._ It follows from Theorem 7.2 and Proposition 5.5. When s _ξ_ is spin then 

**==> picture [402 x 27] intentionally omitted <==**

is a twisting number; the fact that it is the lowest one is a consequence of the total ordering of _F_ on the full paths of Char(Γ _[∗] ,_ s _ξ_ ) ending correctly, and Lemma 3.12 which tells us that _V_ can and _−V_ can reach the extremal values of _F_ among these vectors. □ 

7.2. **The full path determines the contact structures.** We now show that the total number of negative-twisting contact structures, up to isotopy, which we determined in Section 6, is the same as the number of unordered pairs of realised characteristic vectors sharing the same Spin _[c]_ - structure and Maslov grading. 

50 

The assumption of _−Y_ being indefinite is not needed for the result we are proving here, but we keep the notation to avoid confusion, as we know the result holds in the negative-definite case. 

**Theorem 7.7** _Suppose that −Y_ = _M_ ( _e_ 0; _r_ 1 _, ..., rn_ ) _is a Seifert fibred space. Let V_ 1 _and V_ 2 _be two realised characteristic vectors and set_ 2 _X_ = _Q[−] ∗_[1][(] _[V]_[1][+] _[ V]_[2][)] _[and]_[2] _[U]_[=] _[ V]_[1] _[−][V]_[2] _[.][Then][the][number][of] ordered pairs_ ( _V_ 1 _, V_ 2) _for which X is integral, U[T] X_ = 0 _and −q_ = _−_ 1+ _e[T]_ 1 _[X][is][a][twisting][number] of −Y is equal to the number of negative-twisting structures on −Y , up to isotopy._ 

By Proposition 3.1 we know that _X_ being integral is equivalent to _V_ 1 and _−V_ 2 inducing the same Spin _[c]_ -structure on _−Y_ , while by Equation (3.1) that _M_ ( _V_ 1) = _M_ ( _V_ 2); moreover, from the definition of height we have that _q_ ⩾ 1. We recall that the number of negative-twisting structures coincides with the upper bound from convex surface theory, which we explicitly write in Subsection 6.1; in particular, these structures are precisely the ones constructed in Subsections 6.2 and 6.3, together with the ones induced by Stein structures on the blown down standard graph. 

**Lemma 7.8** _Let[p] q[be][the][best][upper][approximation][for][r][∈]_[(0] _[,]_[ 1)] _[ ∩]_[Q] _[for][some][q][>]_[ 1] _[;][expand][−] p[q] into the negative continued fraction_ [ _n_ 1 _, ..., nh_ ] _and call B the negative of its chain matrix. Then there exists a positive integral vector W such that BW_ = _qe_ 1 _; moreover, one has w_ 1 = _p and wh_ = 1 _._ 

_Proof._ If we define _w_ 0 := _q_ and _w_ 1 := _p_ and then recursively 

**==> picture [122 x 12] intentionally omitted <==**

the continued fraction relation ensures _wh_ = 1, while the row equations become: 

_•_ for the first row: ( _−n_ 1) _w_ 1 _− w_ 2 = _q_ ; 

- for the interior rows: _−wj−_ 1 + ( _−nj_ ) _wj − wj_ +1 = 0; 

- for the last row: _−wh−_ 1 + ( _−nh_ ) _wh_ = 0. 

This is exactly _BW_ = _qe_ 1. □ 

_Proof of Theorem 7.7._ Fix a twisting number _−q_ ; for each leg _i_ let _[p] q[i]_[be][the][best][upper][approx-] imation for _ri_ , and let _− p[q] i_[=][[] _[n][i]_ 1 _[, ..., n][i] hi_[]][and] _[−] r_[1] _i_[=][[] _[m][i]_ 1 _[, ..., m][i] ki_[]][be][the][corresponding][negative] continued fractions. 

For an ordered pair ( _V_ 1 _, V_ 2) contributing to the twisting number _−q_ we have _V_ 1 = _Q∗X_ + _U_ and _V_ 2 = _Q∗X − U_ . If we define _Z_[(] _[i]_[)] := **1** _− X_[(] _[i]_[)] as in the previous subsection, then on the _i_ -th leg we have that Equation (7.1) holds. Moreover, the following properties are already established: _zj[i]_[⩾][1] _[,]_[0][ ⩽] _[u][i] j_[⩽] _u_ ~~_[i]_~~ _j_[,][the][vertex-dependent][bound][from][the][realised][definition,][and] _[u][i] j_ � _zj[i][−]_[1] � = 0 for every _i_ = 1 _, ..., n_ and _j_ = 1 _, ..., ki_ . For any given _q_ the vectors _Z_[(] _[i]_[)] and _U_[(] _[i]_[)] are determined by the best upper approximation up to the dependence given by Equation (7.1) from the Leg lemma. The count of admissible ordered pairs ( _V_ 1 _, V_ 2) is then equal to the product of the numbers of the possible difference vectors _U_[(] _[i]_[)] on each leg. 

Let us compute the latter number for an arbitrary leg. Looking at the dependence condition _−Q_[(] _[i]_[)] _Z_[(] _[i]_[)] _− U_[(] _[i]_[)] = _qe_ 1 + _eki_ , we use the auxiliary Lemma 7.8 to express _qe_ 1 as _−R_[(] _[i]_[)] _W_[(] _[i]_[)] , where _R_[(] _[i]_[)] is the chain matrix corresponding to _pqi_[and] _[W]_[ (] _[i]_[)][a][positive][integral][vector][with] _[w]_ 1 _[i]_[=] _[ p][i]_[and] _wh[i]_[= 1][.] 

We recall that _− p[q] i_[=][[] _[n][i]_ 1 _[, ..., n][i] hi_[]][has] _[n][i] j_[=] _[m][i] j_[for] _[j]_[=][1] _[, ..., h][i][−]_[1][and][either] _[h][i]_[=] _[k][i]_[+ 1][or] _hi_ ⩽ _ki_ with _m[i] hi[<][n][i] hi_[.][We][check][for][possible][values][of] _[u][i] j_[row-by-row][in] _[−][Q]_[(] _[i]_[)] _[Z]_[(] _[i]_[)] _[−][U]_[(] _[i]_[)][=] _−R_[(] _[i]_[)] _W_[(] _[i]_[)] + _eki_ . Since _z_ 1 _[i]_[=] _[w]_ 1 _[i]_[=] _[p][i]_[,][we][have] _[u][i]_ 1[=][0][,][and][inductively] _[z] j[i]_[=] _[w] j[i]_[for] _[j]_[⩽] _[h][i]_[and] _u[i] j_[=][0][for] _[j][<][h][i]_[.][At][the] _[h][i]_[-th][row][we][finally][have] _[z] h[i] i_[=] _[w] h[i] i_[=][1][and][for] _[u][i] hi_[there][are] _[m][i] j[−][n][i] j_ choices, while in all later tail coordinates there are 1 _− m[i] j_[of][them.] 

51 

**==> picture [459 x 61] intentionally omitted <==**

and this agrees exactly with the upper bound in Subsection 6.1. Because the choices on different legs are independent once _q_ is fixed, the total number of ordered pairs with twisting number _−q < −_ 1 is _T_ (1 _, q_ ) _· · · T_ ( _n, q_ ). 

When _q_ = 1, the interval condition is vacuous (there is no _h <_ 1), so the above description degenerates. In this case every vertex contributes its full number of values: the centre contributes for _|e_ 0 + 1 _|_ , while each leg vertex _m[i] j_[contributes][for] _[|][m][i] j_[+ 1] _[|]_[.][The][total][is] 

**==> picture [112 x 35] intentionally omitted <==**

Different twisting numbers give disjoint classes of vectors _X_ . Thus the total number of ordered pairs is the sum of the fixed _q_ -contributions, which is exactly our statement. □ 

We can find a correspondence between the sets of ordered and unordered pairs of realised characteristic vectors; namely, we have that if _V_ 1 and _V_ 2 _[′]_[are][as][above][then][the][vector] _[V]_[2][is][also] realised, for symmetry reasons, where _V_ 2 _[′]_[is][the][initial][vector][of][the][full][path][[] _[−][V]_[2][]][.][Therefore,] the ordered pair ( _V_ 1 _, V_ 2 _[′]_[)][is][identified][with][(] _[V]_[1] _[, V]_[2][)][(as][an][unordered][pair),][and][then] _[V]_[1][and] _[V]_ 2 _[′]_ induce conjugated Spin _[c]_ -structures on _−Y_ if and only if _V_ 1 and _V_ 2 induce the same one. We also know that by definition, see Section 3, one has 

**==> picture [333 x 33] intentionally omitted <==**

The number of unordered pairs ( _V_ 1 _, V_ 2) of realised characteristic vectors with same Maslov grading and Spin _[c]_ -structure, which appears in the statement of Theorem 1.6, then also coincides with the number of negative-twisting structures. 

_Proof of Theorem 1.6._ The correspondence follows from the discussion above and Theorem 7.7, while fillability follows from Corollary 7.1. □ 

As we mentioned before, when _q_ = _−_ tw( _−Y_ ) then the upper bound coincides with the number of realised characteristic vectors. In this setting the corresponding ordered pairs are of the form ( _V, V[′]_ ), while the unordered ones are of the form ( _V, V_ ). 

7.3. **The contact invariant.** We start this subsection by showing that, when _−Y_ is type A, there is at most one contact structure _ξ_ such that tw( _−Y, ξ_ ) _<_ tw( _−Y_ ) in each s _∈_ Spin _[c]_ ( _−Y_ ); meanwhile, when _−Y_ is type B, there is at most one pyramid in each s _∈_ Spin _[c]_ ( _−Y_ ). Later on, we determine exactly what are the coordinates of the contact invariant _c_[+] ( _ξ_ ) _∈ HF_ red( _Y,_ s) with respect to the canonical basis _B_ = _{T_ [ _V_ 1] _, ..., T_ [ _Vt_ ] _}_ given by the full path algorithm. We recall that od _B_ can be identified with a basis of _HF_[�] ( _Y,_ s), see Section 2, and thus we can also identify _c_ +( _ξ_ ) with � _c_ ( _ξ_ ); moreover, by Lemma 5.6 all the coordinates of the contact invariant, with respect to _B_ , correspond to realised characteristic vectors. For this reason, here we only consider the subset of _B_ spanned by such vectors. 

We also recall the terminology that we introduced in Section 6. An indefinite Seifert fibred space _−Y_ = _M_ ( _e_ 0; _a[b]_[1] 1 _[, ...,] a[b][n] n_[)][which][is][not][an] _[L]_[-space][can][be][either][of][type][B,][when][its][standard] graph has a subgraph _G_ isomorphic to one of a torus bundle in Figure 6, or of type A otherwise. We say that a manifold of type B is short when there is at most one vertex not in _G_ on each leg; 

52 

otherwise, we say it is long. We say that a manifold of type B is without tails when _|_ tw( _−Y_ ) _| > ai_ for _i_ = 1 _, ..., n_ ; otherwise, if it has two distinct negative twisting numbers then we say it has tails. We proved in Lemma 6.3 and Proposition 6.7 that when _−Y_ has tails any negative-twisting structure is obtained from a manifold _M_ of type A without tails, equipped with the contact structure tangent to the fibres, by doing Legendrian surgery on some new vertices attached to the standard graph of _M_ . Similarly, we proved in Proposition 6.14 that negative-twisting structures on a long manifold of type B are obtained from a short one through the same construction. 

We specified in Subsection 6.3 that structures may form pyramids. Consider 

**==> picture [184 x 12] intentionally omitted <==**

the decreasing sequence of all the negative twisting numbers on _−Y_ ; then a pyramid of size _k_ is the family of all the negative-twisting structures _ξij_ for 1 ⩽ _i_ ⩽ _j_ ⩽ _k_ , in a fixed homotopy type, such that tw( _−Y, ξij_ ) = _−qj−i_ for every _i, j_ . In the terminology of the previous subsection, a pyramid of size _k_ is the family of all the realised characteristic vectors _V_ 1 _, ..., Vk ∈_ Char( _−Y,_ s) with fixed Maslov grading such that each unordered pair ( _Vi, Vj_ ) corresponds to a negative-twisting structure, in the sense of Theorem 1.6, and height _F_ ([ _Vi_ ] + [ _Vi_ +1]) is the same for _i_ = 1 _, ..., k −_ 1. 

**Lemma 7.9** _Suppose that −Y is an indefinite Seifert fibred space, then if −Y is of type A then every_ s _∈_ Spin _[c]_ ( _−Y_ ) _admits at most one structure with twisting number smaller than q_ = tw( _−Y_ ) _. Furthermore, if −Y is of type B then every_ s _∈_ Spin _[c]_ ( _−Y_ ) _supports exactly a single pyramid of size k_ (s) _._ 

_Proof._ If _−Y_ is short of type B then the claim has been already proved in Subsection 6.3. If _−Y_ is of type A without tails then, by the results of Massot [31] and the discussion in Subsection 6.2, we know there is a _ξ_ 0 such that 

**==> picture [143 x 13] intentionally omitted <==**

and _ξ_ 0 is tangent to the fibres and supports a spin structure s0. From Theorem 1.6 we know that _q_ = _−_ 1 + _e[T]_ 1 _[Q] ∗[−]_[1] _[V]_[can][,][because][s][0][is][spin;][since] _[V]_[can][realises][min] _[ F]_[(] _[V]_[ )][among][any][initial] _V ∈_ Char(Γ _[∗]_ ) by Lemma 3.12, we have that _c_[+] ( _ξ_ ) = _T_ [ _V_ can] + _T_ [ _−V_ can] and _−e[T]_ 1 _[Q] ∗[−]_[1] _[V]_[can][=] height _F_ ([ _V_ can] + [ _−V_ can]); in particular, one has s0 = scan. If another such structure existed we should find another realised characteristic vector _V_ such that _e[T]_ 1 _[Q] ∗[−]_[1] _[V]_[=] _[ e][T]_ 1 _[Q] ∗[−]_[1] _[V]_[can][by][Theorem] 7.7, and then _F_ ( _V_ ) = _F_ ( _V_ can). This is not possible because _F_ induces a total ordering on the full paths that end correctly, see Remark 3.2. Suppose that _−Y_ is not in one of these two families, we prove the claim by induction on the number of vertices we need to add to the standard graph of a manifold (either short or without tails) to obtain _−Y_ ; note that if _−Y_ is of type A and has only one negative twisting number then there is nothing to prove. 

Consider the map induced by ( _−_ 1)-contact surgery _FW,J_[+][:] _[ HF]_[ +][(] _[−][Y,]_[ s][)] _[ →][HF]_[ +][(] _[M][′][,]_[ s] _[′]_[)][, which] as we know maps _T_ [ _Vi_ ] to _T_ [ _Vi′_[]][where] _[C]_[=] _[{][V]_[1] _[, ..., V][k]_[(][s][)] _[}]_[are][the][realised][characteristic][vectors][in] Char(Γ _[∗] ,_ s) while _Vi[′]_[is][obtained][by][removing][the][coordinate][of][the][new][vertex][from] _[V][i]_[.][Notice] that _FW,J_[+][is][injective][on] _[C]_[because][then] _[X]_[Γ] _[∗]_[would][admit][a][Stein][structure] _[I]_[,][extending] _[J]_[,][such] that _F_[+][for] _[i]_[ = 1] _[,]_[ 2][,][contradicting][the][usual][result][of][Plamenevskaya][[48].] _X_ Γ _∗ ,I_[(] _[T]_[[] _[V][i]_[]][) = 1] 

Say that _V_ 1 _, ..., Vh_ such that _F_ ( _V_ 1) _< · · · < F_ ( _Vh_ ) would form a maximal pyramid, and assume that there is a _Vh_ +1 such that either _F_ ( _Vh_ +1) _> F_ ( _Vh_ ) or _F_ ( _Vh_ +1) _< F_ ( _V_ 1). We consider first the case that s and s _[′]_ supports negative-twisting tight structures with the same twisting numbers; then by incduction _F_ ( _V_ 1 _[′]_[)] _[ <][ F]_[(] _[V] h[′]_ +1[)] _[ <][ F]_[(] _[V][h]_[)][ but we now use the fact that] _[ F] W,J_[+][has well-defined] Maslov and Alexander grading shift, see [44, 43, 19, 22], and we immediately have a contradiction. In the case s _[′]_ supports a structure with an additional twisting number _q_ , then Theorem 7.7 and 

53 

the same argument of the degree shifts of _FW,J_[+][imply][that] _[q]_[is][also][the][twisting][number][of][a] contact structure which induces s, and this is again not possible. 

Note that when _−Y_ is of type _B_ the argument above and Lemma 6.9 also imply that _Vh_ +1 should necessarily extend the pyramid whose base is made by _V_ 1 _, ..., Vh_ , contradicting the maximality that we assumed at the beginning. Therefore, we need to have _h_ = _k_ (s) and all the realised characteristic vectors form a pyramid of size _k_ (s). □ 

We proved that the Stein structures _{Ji}_ on the cobordism obtained by attaching new vertices on a standard graph, which extend a fixed Spin _[c]_ -structure s _[′]_ , are in one-to-one correspondence with the choices of coordinates for the resulting characteristic vector to be realised. In addition, the Spin _[c]_ -structures _Ji|−Y_ , where the manifold _−Y_ is obtained this way, which support tight structures with at least two distinct negative twisting numbers are all distinct. 

**Theorem 7.10** _Suppose that −Y is an indefinite Seifert fibred space, and let ξ be a negativetwisting structure on −Y such that_ tw( _−Y, ξ_ ) _<_ tw( _−Y_ ) _. Denote by V_ 1 _, ..., Vk_ (s _ξ_ ) _the realised characteristic vectors in_ Char(Γ _[∗] ,_ s _ξ_ ) _, in increasing order according to F ; then_ 0 = _c_[+] ( _ξ_ ) _∈ HF_ red( _Y_ ) _and we have that:_ 

_A) if −Y is of type A then ξ is unique, up to isotopy, and c_[+] ( _ξ_ ) = _T_ [ _V_ 1] + _T_ [ _Vk_ (s _ξ_ )] _; B) if −Y is of type B then ξ_ = _ξij for some_ 1 ⩽ _i < j_ ⩽ _k_ (s _ξ_ ) _, and c_[+] ( _ξ_ ) = _αiT_ [ _Vi_ ] + _αi_ +1 _TVi_ +1 + _· · ·_ + _αjT_ [ _Vj_ ] _where αl_ = � _jl−−ii_ � mod 2 _for l_ = _i, i_ + 1 _, ..., j. Furthermore, the twisting number is determined by_ 

**==> picture [281 x 33] intentionally omitted <==**

_Proof of Theorem 7.10 and Proposition 1.7._ We already saw in Corollary 7.1 that for indefinite Seifert fibred spaces _c_[+] is non-vanishing in _HF_ red precisely for negative-twisting structures. The claim about the height function follows immediately by Theorem 7.7. The coordinates of the contact invariant are determined using the same cobordism map we used in the proof of Lemma 7.9, and the fact that such a map is injective on the subgroup spanned by _V_ 1 _, ..., Vk_ (s _ξ_ ), provided that we can identify them for manifolds that are either short or without tails. 

For the type A case we did this in the proof of Lemma 7.9, while for the type B one by Corollary 6.13 we have that _c_[+] ( _ξij_ ) = _c_[+] ( _ξij−_ 1) + _c_[+] ( _ξi_ +1 _j_ ) leading to the binomial coefficient formula in the statement. Hence, for each _ξij_ the Alexander filtration of any coordinate _T_ [ _Vl_ ] of _c_[+] ( _ξij_ ) is in the interval [ _F_ ( _Vi_ ) _, F_ ( _Vj_ )], with extremal points included, and the unordered pair ( _Vi, Vj_ ) is unique, in accordance to the correspondence in Theorem 7.7. □ 

## 8. Applications 

8.1. **Brieskorn spheres.** In this subsection we collect some results about Brieskorn spheres. We start by showing that every oppositely oriented Brieskorn sphere _−Y_ , different from _−_ Σ(2 _,_ 3 _,_ 6 _k ±_ 1) for _k_ ⩾ 1, is of type A and that _−Y_ has at most one structure with twisting number smaller than tw( _−Y_ ). We need the following lemma. 

**Lemma 8.1** _If −Y_ = _−_ Σ( _a_ 1 _, ..., an_ ) _is an oppositely oriented Brieskorn sphere, and_ Γ _[∗] is its standard graph, then any Seifert fibred space M whose standard graph is obtained by removing a vertex from_ Γ _[∗] is such that e_ ( _M_ ) ⩽ 0 _._ 

_Proof._ Since _−Y_ is an integral homology sphere, the matrix _Q[−] ∗_[1] has integral entries. In addition, we have that the diagonal entries corresponding to the terminal vertex of any leg are non-negative; otherwise, if _qii_ := _e[T] i[Q] ∗[−]_[1] _[e][i][<]_[0][then][adding][a][new][vertex][to][the] _[i]_[-th][leg][with][framing] _[q][ii]_[would] produce a graph _G_[�] such that _e_ ( _−Y_ ) _< e_ ( _MG_ �) = 0, which is not possible because Γ _[∗]_ is indefinite. 

54 

We now know that _qii_ ⩾ 0 for each vertex _Si_ as above. If _qii_ = 0 then removing _Si_ yields _e_ ( _M_ ) = 0. Suppose that _qii >_ 0; we have that the graph _G_[�] , obtained by lowering the framing of _Si_ by one and adding vertices with framings given by the negative continued fraction of _− qiiqii−_ 1[,] satisfies _e_ ( _M_ ) _< e_ ( _MG_ �) = 0. □ 

_Proof of Corollary 1.8._ Suppose that _−Y_ is of type B, and denote by _G_ 0 _⊂_ Γ _[∗]_ a subgraph isomorphic to one of a torus bundle in Figure 6. Since we cannot have _G_ 0 = Γ _[∗]_ , we can choose a vertex at the end of a leg which is outside of _G_ 0 and remove it; hence, by Lemma 8.1 we obtain a new subgraph _G_ , which contains _G_ 0, such that 0 = _e_ ( _MG_ 0) ⩽ _e_ ( _MG_ ) ⩽ 0. This immediately implies that _G_ = _G_ 0, and then Γ _[∗]_ is obtained by adding a single vertex to the standard graph of a torus bundle. Checking by hand all the possible cases, we determine that the Seifert fibred spaces of this form which are Brieskorn spheres are _−_ Σ(2 _,_ 3 _,_ 6 _k ±_ 1) for _k_ ⩾ 1. 

If _−Y_ is of type A then, by Theorem 6.4 and Remark 6.6, at most two negative twisting numbers are realised by tight structures. Suppose that there is a _ξ_ such that tw( _−Y, ξ_ ) = tw( _−Y_ ), then it is unique from Lemma 7.9 because _Y_ is an integral homology sphere. □ 

We now show that there are only three Brieskorn spheres with a unique tight contact structure; namely, with the canonical orientation we only have Σ(2 _,_ 3 _,_ 5) (the fact that it carries a unique tight structure is well-known and follows from the techniques in [15]), while with opposite orientation we have _−_ Σ(2 _,_ 3 _,_ 11) and _−_ Σ(2 _,_ 3 _,_ 7) (they both have only one tight structure by [20, 51]). We show that there are no other ones. 

_Proof of Theorem 1.9._ We first observe that a Brieskorn sphere with a unique fillable structure has blown down standard graph _XG_ with either _−_ 2-framed unknots or 0-framed positive trefoils. We assume that _Y_ = Σ( _a_ 1 _, ..., an_ ) is a canonically oriented Brieskorn sphere. 

If _G_ = Γ is negative-definite then the only way we can have _e_ ( _Y_ ) _<_ 0 is when _e_ 0 = _−_ 2, there are three legs, and all the vertices of Γ have framing _−_ 2. Hence, we have _−Y_ = _M_ ( _−_ 1; _a_[1] _[,]_[1] _b[,]_[1] _c_[)] where _c > b > a_ ⩾ 2 are integers; we need that _a, b_ and _c_ are pairwise coprime and that _e_ ( _−Y_ ) = _a_[1][+][1] _b_[+][1] _c[−]_[1] _[ >]_[ 0][:][this][can][only][happen][when] _[a]_[ = 2] _[,][b]_[ = 3] _[,]_[and] _[c]_[ = 5][.] If _G_ = Γ _[∗]_ is indefinite then the analysis is more involved. When _−Y_ is of type B then from Corollary 1.8 and [20, 51] we only have the two manifolds in the statement, so we consider a _−Y_ of type A. Assume first that _e_ 0 ⩽ _−_ 2, then _n_ = 3 because otherwise we would have _M_ ( _−_ 2;[1] 2 _[,]_[1] 2 _[,]_[1] 2 _[,]_[1] 2[)] as subgraph; hence, we can write _Y_ = _M_ ( _−_ 1; _a_[1] _[,]_[1] _b[,]_[1] _c_[)][and] _a_[1][+][1] _b_[+][1] _c[−]_[1][=] _[−] abc_[1][with] _[a, b, c]_[as] above: this is only possible when _a_ = 2 _, b_ = 3 and _c_ = 7 which leads to a type B manifold. Assume now that _e_ 0 = _−_ 1, we have that _X_ Γ _∗_ has only unknots with framing _−_ 2 otherwise either _M_ ( _−_ 1;[1] 2 _[,]_[1] 3 _[,]_[1] 6[)][would][be][a][subgraph][of][Γ] _[∗]_[,][or] _[Y]_[=] _[S] d_[3] 1 _d_ 2 _−d_ 1 _−d_ 2 _−_ 1[(] _[T][d]_ 2 _[,d]_ 1[)][by][Lemma][8.1] but this is not a Brieskorn sphere. We consider the possible _S_[3] -subgraph (Γ _[∗]_ ) _[′]_ : from what we said before this cannot be neither empty nor the fibration of any _Td_ 2 _,d_ 1 with _d_ 1 _, d_ 2 _>_ 1. If (Γ _[∗]_ ) _[′]_ coincides with the centre then _M_ ( _−_ 1;[1] 3 _[,]_[1] 3 _[,]_[1] 3[)][would][be][a][subgraph;][in][the][same][way,][if][(Γ] _[∗]_[)] _[′]_ coincides with _M_ ( _−_ 1;[1] 2[)][then] _[M]_[(] _[−]_[1;][1] 2 _[,]_[1] 4 _[,]_[1] 4[)][would][be][a][subgraph.][This][is][not][possible][as][both] correspond to torus bundles. 

The last case to consider is when (Γ _[∗]_ ) _[′]_ is _M_ ( _−_ 1; _n_ +1 _n_[)][when] _[n]_[⩾][2][,][and][here][we][have] _[G]_[�][:=] _M_ ( _−_ 1; _n_ +1 _n[,] n_ +31 _[,] n_ +31[)][as][a][subgraph][of][Γ] _[∗]_[.][If][Γ] _[∗]_[=] _[G]_[�][then][applying][Lemma][8.1][we][obtain][a] subgraph _G_ such that 0 _< e_ ( _M_ � _G_ ) ⩽ _e_ ( _MG_ ) ⩽ 0, which is not possible; therefore, we conclude that _−Y_ = _MG_ � _≃ S−_[3] 2 _,−_ 2[(] _[T]_[2] _[,]_[2] _[n]_[+2][)][and][this][is][never][a][Brieskorn][sphere.] □ 

Note that if an oppositely oriented Brieskorn sphere _−Y_ of type A had no tight structure with twisting number tw( _−Y_ ) (the structure tangent to the fibres as in [31]) then from the proof of Corollary 1.8 it should have a unique realised characteristic vector (that is _V_ can); hence, this implies that _−Y_ is as in Theorem 1.9 which, conversely, does not mention any manifold of type 

55 

A. This means that any Brieskorn sphere _−Y_ different from _−_ Σ(2 _,_ 3 _,_ 5) always carries a (unique) contact structure tangent to the fibres. 

8.2. **Surgeries on torus knots.** In this subsection we prove our results about _Sr_[3][(] _[T][d]_ 2 _[,][±][d]_ 1[)][ where] _r ∈_ Q and 1 _< d_ 2 _< d_ 1 coprime. Namely, we first show that our classification results hold for these manifolds, and then we compute all the possible values of the negative twisting numbers for a tight structure on _Sr_[3][(] _[T][d]_ 2 _[,][±][d]_ 1[)][.] 

_Proof of Corollary 1.11._ It is well-known that any surgery on a torus link is a Seifert fibred space, except when the framing on a component is the exceptional slope (that is _±d_ 2 _d_ 1); therefore, it can be presented by a star-shaped graph. When this graph is negative-definite then the classification is given by [8, Corollary 1.2]; otherwise, by Proposition 1.4 and Theorem 1.6. 

If the exceptional slope appears then the graph would have a leg which consists of a single vertex with framing zero; hence, the central vertex can be cancelled, and then the manifold is the connected sum of the lens spaces (possibly _S_[1] _× S_[2] ’s) represented by the remaining legs. It is a result of Colin [10] that a tight structure decomposes along connected sums, and tight structures on lens spaces were already classified explicitly, see [26]. □ 

_Proof of Proposition 1.12._ Surgeries on a positive torus knot above the bound _d_ 1 _d_ 2 _− d_ 1 _− d_ 2 are precisely the _L_ -spaces, and have normalised Seifert coefficients with _e_ 0 ⩾ _−_ 1; hence, they admit only zero-twisting structures. Meanwhile, all the others admit negative-twisting structures by [29]. As we explained in Section 5, once we have negative-twisting structures, we have those with the highest twisting number, which is computed, as for Proposition 5.5, to be _−d_ 1 _− d_ 2. 

For ( _d_ 2 _, d_ 1) _̸_ = (2 _,_ 3) with these restrictions, the manifold _Sr_[3][(] _[T][d]_ 2 _[,d]_ 1[)][is][Seifert][fibred][of][type][A;] hence, there is at most one additional twisting number. It is of the form _q_ := _d_ 1 + _d_ 2 + _sd_ 1 _d_ 2 because it is denominator of the best upper approximations for _r_ 1 and _r_ 2 simultaneously, and we get that the best upper approximation of _r_ 3 is of the form _[p] q_[3][=] _d_ 1+ _ds_ 2+1+ _sd_ 1 _d_ 2[as][a][reduced][fraction] by requiring that the three approximations sum up to 1 +[1] _q_[(by][Ghiggini-Massot’s][algorithm).] Now for the possible values of the surgery coefficient _r_ , we determine _r_ 3 so that it has _[p] q_[3][as][the] best upper approximation. 

Surgeries on _T_ 2 _,_ 3 (when _r ∈_ (0 _,_ 1)) are of type B: they are negative-definite for _r <_ 0, give the torus bundle _M_ ( _−_ 1;[1] 2 _[,]_[1] 3 _[,]_[1] 6[)][with][infinitely][many][twisting][numbers][of][the][form] _[−]_[5] _[ −]_[6] _[s]_[for] _[r]_[= 0][,] while for surgeries in (0 _,_ 1) we need that _−_ 6 + _r < −_ 6 +[1] _s_[for][[] _[−]_[6] _[,][ −][s]_[]][to][be][a][twisting][number.] Surgeries on negative torus knots are, on the other hand, _L_ -spaces for surgery coefficients smaller or equal than _−d_ 1 _d_ 2. All other surgeries have _e_ 0 = _−_ 2 and thus _−_ 1 as their highest twisting number. If we write _Sr_[3][(] _[T][d]_ 2 _[,d]_ 1[)][as] _[M]_[(] _[−]_[1;] _[ r]_[1] _[, r]_[2] _[,] d_ 1 _d_ 12 _−r_[)][,][then] _[S] r_[3][(] _[T][d]_ 2 _[,][−][d]_ 1[)][is] _[M]_[(] _[−]_[2; 1] _[ −] r_ 1 _,_ 1 _− r_ 2 _,_ 1 _− d_ 1 _d_ 12+ _r_[)][.][Now][the][possible][denominators][of][the][best][upper][approximations][of][1] _[ −][r]_[1] and 1 _− r_ 2 simultaneously take the form _q[′]_ := _−d_ 1 _− d_ 2 + _d_ 1 _d_ 2 _l_ , and the best upper approximation of the third coefficient is forced to be _[p] q_ 3 _[′][′]_[=][1] _[ −] −d_ 1 _−ld−_ 2+1 _d_ 1 _d_ 2 _l_[and] _[l][>]_[2][whenever][(] _[d]_[2] _[, d]_[1][)][=][(2] _[,]_[ 3)] by the sum-equal-to 2 +[1][condition.][We][conclude][the][proof][by][noticing][the][equivalence] _q[′]_ 

**==> picture [441 x 26] intentionally omitted <==**

and the fact that the Möbius transform 

**==> picture [146 x 27] intentionally omitted <==**

which takes _r_ 3 = _d_ 1 _d_ 12 _−r_[to] _[r]_ 3 _[′]_[=][1] _[ −] d_ 1 _d_ 12+ _r_[,][maps][also] _d_ 1+ _ds_ 2+1+ _sd_ 1 _d_ 2[to][1] _[ −] −d_ 1 _−d_ 2+ _s_ +1 _d_ 1 _d_ 2( _s_ +2)[and] preserves the continued fraction relations that characterise the best upper approximations (see 

56 

Subsection 6.1). In the case of ( _d_ 2 _, d_ 1) = (2 _,_ 3), we can check by hand that also the twisting number _−_ 5 on _Sr_[3][(] _[T]_[2] _[,]_[3][)][gives][rise][to][the][twisting][number] _[−]_[7][on] _[S] r_[3][(] _[T]_[2] _[,][−]_[3][)][.] □ 

We conclude the paper by showing how the computation in Proposition 1.12, together with the explicit expression of the upper bound in Subsection 6.1, can be used to determine the number of negative-twisitng structures on every surgery on a torus knot. We do the case of _M_ = _Sr_[3][(] _[T][d]_ 2 _[,d]_ 1[)][,] and we explain how to recover the same result for _Sr_[3][(] _[T][d]_ 2 _[,][−][d]_ 1[)][.] 

We first note that the standard graph of _M_ has three legs and _e_ 0 = _−_ 1; moreover, the centre and the first two legs form the _S_[3] -subgraph which coincides with the fibration of _Td_ 2 _,d_ 1. The set of realised characteristic vectors is then completely determined by the third leg, because from Theorem 5.4 we know that the coordinates of such vectors are fixed on the _S_[3] -subgraph. The framing of the third leg is _−d_ 1 _d_ 2 + _r_ whenever _r < d_ 1 _d_ 2 _− d_ 1 _− d_ 2; note that when _r_ is bigger than this number _M_ is an _L_ -space with _e_ 0 = _−_ 1 which has no negative-twisting structures, see Remark 3.9. We write _−d_ 1 _d_ 2 + _r_ as the negative continued fraction [ _m_ 1 _, ..., mk_ ], whose coefficients correspond to the framings of the vertices of the third leg. 

Since we know from Proposition 5.5 and [8, Theorem 1.4] that the number of contact structures with twisting number tw( _−Y_ ) is equal to the number of realised characteristic vectors, we conclude that such a quantity is 

**==> picture [178 x 12] intentionally omitted <==**

where the first term accounts for the restricted values of the coordinate of the vertex attached to the centre, as in Theorem 5.4. 

For the other twisting numbers we distinguish the case of a type B (when ( _d_ 2 _, d_ 1) = (2 _,_ 3)) or a type A manifold. In the first case by Theorem 7.10 we just have to count how many pyramids appear; since 0 _< r <_ 1 and we have that _−_ 6 + _r_ = [ _−_ 6 _, −k −_ 1 _, m_ 3 _, ..., mk_ ], where _k_ is the size of the pyramid of the short manifold _M_ ( _−_ 1; 2[1] _[,]_[1] 3 _[,]_ 6 _[k] k_[+1] +5[)][,][while][the][best][upper][approximation][for] _k_ the lowest twisting number is 6 _k−_ 1[,][we][obtain][that][there][are] 

**==> picture [274 x 12] intentionally omitted <==**

In the second case by Theorem 7.10 we have to count the structure with the unique non-highest twisting number _−q_ . We computed in Proposition 1.12 that _−q_ exists only when 0 _< r < d_ 1 _d_ 2 _− d_ 1 _− d_ 2 and _−d_ 1 _d_ 2 + _r_ falls in the interval given by 

**==> picture [278 x 27] intentionally omitted <==**

for a positive _s_ when the fraction is reduced. Note that the left-most endpoint of the interval corresponds to the manifold without tails, while the right-most one to the best upper approximation (for each rational in the interval); hence, we have that the number we want is 

**==> picture [162 x 12] intentionally omitted <==**

as _mi_ = _ni_ for _i_ = 1 _, ..., h −_ 1. Finally, for _Sr_[3][(] _[T][d]_ 2 _[,][−][d]_ 1[)][we][just][need][to][identify][the][standard][graph:][this][has] _[e]_[0][=] _[ −]_[2][,][the][first] two legs as in the fibration of _Td_ 2 _,−d_ 1, and the third leg with framing _− d_ 1 _dd_ 12 _d_ +2+ _r−r_ 1[.][Everything][that] we said above can then be replicated. 

## References 

> [1] A. Alfieri, _Deformations of lattice cohomology and the upsilon invariant_ , arxiv:2010.07511. 

> [2] A. Alfieri and A. Cavallo, _Holomorphic curves in Stein domains and the tau-invariant_ , arXiv:2310.08657. 

> [3] K. Baker, J. Etnyre and J. Van Horn-Morris, _Cabling, contact structures and mapping class monoids_ , J. Differ. Geom., **90** (2012), no. 1, pp. 1–80. 

> [4] J. Bodnár and O. Plamenevskaya, _Heegaard Floer invariants of contact structures on links of surface singularities_ , Quantum Topol., **12** (2021), no. 3, pp. 411–437. 

57 

- [5] M. Borodzik, B. Liu and I. Zemke, _Lattice homology, formality, and plumbed L-space links_ , J. Eur. Math. Soc., (2024). 

- [6] J. Bowden, _Contact structures, deformations and taut foliations_ , Geom. Topol., **20** (2016), no. 2, pp. 697–746. 

- [7] A. Cavallo, _On Bennequin-type inequalities for links in tight contact_ 3 _-manifolds_ , J. Knot Theory Ramications, 29 (2020), no. 8, 2050055. 

- [8] A. Cavallo and I. Matkovič, _Fillable structures on negative-definite Seifert fibred spaces_ , in preparation. 

- [9] A. Christian and M. Menke, _A JSJ-type decomposition theorem for symplectic fillings_ , arXiv:1807.03420. 

- [10] V. Colin, _Chirurgies d’indice un et isotopies de sphéres dans les variétés de contact tendues_ , C. R. Acad. Sci. Paris Sér. I Math., **324** (1997), pp. 659–663. 

- [11] I. Dai and C. Manolescu, _Involutive Heegaard Floer homology and plumbed three-manifolds_ , J. Inst. Math. Jussieu, **18** (2019), no. 6, pp. 1115–1155. 

- [12] F. Ding and H. Geiges, _Symplectic fillability of tight contact structures on torus bundles_ , Algebr. Geom. Topol., **1** (2001), pp. 153–172. 

- [13] Y. Eliashberg, _A few remarks about symplectic filling_ , Geom. Topol. **8** (2004), pp. 277–293. 

- [14] J. Etnyre and M. Golla, _Symplectic hats_ , J. Topol., **15** (2022), no. 4, pp. 2216–2269. 

- [15] J. Etnyre and K. Honda, _On the nonexistence of tight contact structures_ , Ann. Math. (2), **153** (2001), no. 3, pp. 749–766. 

- [16] J. Etnyre and N. Sağlam, _Surgeries on the trefoil and symplectic fillings_ , arXiv:2308.00068. 

- [17] R. Fintushel and R. Stern, _Immersed spheres in_ 4 _-manifolds and the immersed Thom conjecture_ , Turkish J. Math., **19** (1995), pp. 145–157. 

- [18] P. Ghiggini, _Strongly fillable contact_ 3 _-manifolds without Stein fillings_ , Geom. Topol., **9** (2005), pp. 1677–1687. 

- [19] P. Ghiggini, _Ozsváth-Szabó invariants and fillability of contact structures_ , Math. Z., **253** (2006), no. 1, pp. 159–175. 

- [20] P. Ghiggini, _On tight contact structures with negative maximal twisting number on small Seifert manifolds_ , Algebr. Geom. Topol., **8** (2008), no. 1, pp. 381–396. 

- [21] P. Ghiggini, P. Lisca and A. Stipsicz, _Classification of tight contact structures on small Seifert_ 3 _-manifolds with e_ 0 ⩾ 0, Proc. Am. Math. Soc., **134** (2006), no. 3, pp. 909–916. 

- [22] P. Ghiggini and J. Van Horn-Morris, _Tight contact structures on the Brieskorn spheres −_ Σ(2 _,_ 3 _,_ 6 _n −_ 1) _and contact invariants_ , J. Reine Angew. Math., **718** (2016), pp. 1–24. 

- [23] A. Hatcher, _Notes on basic of_ 3 _-manifold topology_ , Available at `http://pi.math.cornell.edu/~hatcher/3M/ 3Mdownloads.html` . 

- [24] M. Hedden, _An Ozsváth-Szabó Floer homology invariant of knots in a contact manifold_ , Adv. Math., **219** (2008) no. 1 pp. 89–117. 

- [25] M. Hedden and K. Raoux, _Knot Floer homology and relative adjunction inequalities_ , Selecta Math. (N.S.), **29** (2023), no. 1, 48 pp. 

- [26] K. Honda, _On the classification of tight contact structures I._ , Geom. Topol., **4** (2000), pp. 309–368. 

- [27] K. Honda, _On the classification of tight contact structures II._ , J. Differential Geom., **55** (2000), pp. 83–143. 

- [28] P. Lisca and G. Matić, _Tight contact structures and Seiberg-Witten invariants_ , Invent. Math., **129** (1997), pp. 509–525. 

- [29] P. Lisca and G. Matić, _Transverse contact structures on Seifert_ 3 _-manifolds_ , Algebr. Geom. Topol., **4** (2004), pp. 1125–1144. 

- [30] P. Lisca and A. Stipsicz, _Ozsváth-Szabó invariants and tight contact_ 3 _-manifolds III_ , J. Symplectic Geom., **5** (2007), no. 4, pp. 357–384. 

- [31] P. Massot, _Geodesible contact structures on_ 3 _-manifolds_ , Geom. Topol., **12** (2008), no. 3, pp. 1729–1776. 

- [32] I. Matkovič, _Fillability of small Seifert fibered spaces_ , Math. Proc. Camb. Philos. Soc., **174** (2023), no. 3, pp. 585–604. 

- [33] H. Min, _Strongly fillable contact structures without Liouville fillings_ , arXiv:2205.09912. 

- [34] A. Némethi, _On the Ozsváth-Szabó invariant of negative definite plumbed_ 3 _-manifolds_ , Geom. Topol., **9** (2005), pp. 991–1042. 

- [35] I. Niven, H. Zuckerman and H. Montgomery, _An introduction to the theory of numbers_ , New York etc.: John Wiley & Sons, Inc.. xiii, 529 pp. (1991). 

- [36] P. Ozsváth, A. Stipsicz and Z. Szabó, _Knots in lattice homology_ , Comment. Math. Helv., **89** (2014), no. 4, pp. 783–818. 

- [37] P. Ozsváth and Z. Szabó, _The symplectic Thom conjecture_ , Ann. Math. (2), **151** (2000), no. 1, pp. 93–124. 

- [38] P. Ozsváth and Z. Szabó, _Absolutely graded Floer homologies and intersection forms for four-manifolds with boundary_ , Adv. Math., **173** (2003), pp. 179–261. 

- [39] P. Ozsváth and Z. Szabó, _On the Floer homology of plumbed three-manifolds_ , Geom. Topol., **7** (2003), no. 1, pp. 185–224. 

58 

- [40] P. Ozsváth and Z. Szabó, _Knot Floer homology and the four-ball genus_ , Geom. Topol., **7** (2003), pp. 615–639. 

- [41] P. Ozsváth and Z. Szabó, _Holomorphic disks and three-manifold invariants: properties and applications_ , Ann. of Math. (2), **159** (2004), no. 3, pp. 1159–1245. 

- [42] P. Ozsváth and Z. Szabó, _Holomorphic triangle invariants and the topology of symplectic four-manifolds_ , Duke Math. J., **121** (2004), no. 1, pp. 1–34. 

- [43] P. Ozsváth and Z. Szabó, _Holomorphic disks and genus bounds_ , Geom. Topol., **8** (2004), pp. 311–334. 

- [44] P. Ozsváth and Z. Szabó, _Heegaard Floer homology and contact structures_ , Duke Math. J., **129** (2005), no. 1, pp. 39–61. 

- [45] P. Ozsváth and Z. Szabó, _Holomorphic triangles and invariants for smooth four-manifolds_ , Adv. Math., **202** (2006), no. 2, pp. 326–400. 

- [46] P. Ozsváth and Z. Szabó, _Holomorphic disks, link invariants and the multi-variable Alexander polynomial_ , Algebr. Geom. Topol., **8** (2008), no. 2, pp. 615–692. 

- [47] A. Pichon and J. Seade, _Fibred multilinks and singularities f g_ , Math. Ann., **342** (2008), no. 3, pp. 487–514. 

- [48] O. Plamenevskaya, _Contact structures with distinct Heegaard Floer invariants_ , Mathematical Research Letters, **11** (2004), pp. 547–561. 

- [49] R. Rustamov, _On Heegaard Floer homology of plumbed three-manifolds with b_ 1 = 1, arXiv:math/0405118. 

- [50] N. Saveliev, _Invariants for homology_ 3 _-spheres_ , Encyclopaedia of Mathematical Sciences 140. Low-Dimensional Topology 1. Berlin: Springer. 

- [51] B. Tosun, _Tight small Seifert fibered manifolds with e_ 0 = _−_ 2, Algebr. Geom. Topol., **20** (2020), no. 1, pp. 1–27. 

- [52] J. Van Horn-Morris, _Constructions of open book decompositions_ , Ph. D. dissertation, University of Texas at Austin, 2007. 

- [53] S. Wan, _Tight contact structures on some families of small Seifert fiber spaces_ , Acta Math. Hung., **173** (2024), no. 1, pp. 286–296. 

- [54] H. Wu, _Legendrian vertical circles in small Seifert spaces_ , Commun. Contemp. Math., **8** (2006), pp. 219–246. 

- [55] I. Zemke, _The equivalence of lattice and Heegaard Floer homology_ , Duke Math. J., **174** (2025), no. 5, pp. 857–910. 

HUN-REN Alfréd Rényi Insitute of Mathematics, Budapest 1053, Hungary _Email address_ : `acavallo@impan.pl` 

Uppsala Universitet, Uppsala 751 06, Sweden _Email address_ : `irma6504@student.uu.se` 

