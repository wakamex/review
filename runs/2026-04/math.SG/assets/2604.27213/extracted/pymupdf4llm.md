## **HARD LEGENDRIAN UNKNOTS** 

## JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

ABSTRACT. We initiate the study of Reidemeister hardness of Legendrian unknot front projections. Using normal rulings, we obstruct several infinite families of hard unknot diagrams from being drawn with max-tb unknot fronts, along with 1.7 million of the 2.6 million hard unknot diagrams studied in [ABD[+] 24]. We construct infinitely many smoothly hard max-tb unknot diagrams, and bound their minimum possible writhe. With respect to these bounds, our constructions are conjecturally sharp. 

## CONTENTS 

||CONTENTS||
|---|---|---|
|1.|Introduction|1|
|2.|Obstructing hardness|8|
|3.|Constructing hard Legendrian unknots|22|
|4.|Impostors|25|
|References||30|



## 1. INTRODUCTION 

The study of hard diagrams of the unknot is a fixture of knot theory, dating back to the origins of the subject [Goe34]. It has evolved throughout the years via cornerstone theoretical results [HL01, HN10, Lac15], and continues today through modern techniques of computational analysis and reinforcement learning [PZ16, ABD[+] 24, BCL[+] 24, LdMS24]. 

More generally, the study of complexity measures for which the unknotting problem admits a monotonic solution has a rich history. In the 2010s, Henrich and Kauffman [HK14] exhibited a quadratic upper bound on crossing number increase for hard unknot diagrams. They leveraged work of Dynnikov [Dyn06] from the early 2000s, who showed that grid diagrams for the unknot can be simplified monotonically in grid dimension with a finite set of moves. In turn, Dynnikov was inspired by the work of Birman and Menasco [BM92] in the 1990s and of Bennequin [Ben83] in the 1980s. The latter used contact topology and its imprint on Seifert surfaces to study braids, while the former proved a Markov-type theorem without stabilizations for braid representations of the unknot, marking the first complexity non-increasing unknotting theorem. 

There are various notions of Reidemeister hardness that have been studied in the literature, and we begin by establishing some clarifying language. Given a knot diagram _D_ , let cr( _D_ ) denote its crossing number. If _{Di}[n] i_ =0[is a sequence of diagrams, we let] cr( _{Di}_ ) := sup _i_ cr( _Di_ ). By a _planar_ (resp. _spherical_ ) _unknotting Reidemeister sequence_ we mean a sequence of diagrams _{Di}[n] i_ =0[such][that] _[D][n]_[is][the][trivial][diagram][of][the][unknot][and,][up][to][planar][(resp.][spherical)] isotopy, _Di_ +1 is obtained from _Di_ by a Reidemeister move (see Figure 1). 

JB was partially supported by NSF Grant DMS-2038103 and an AMS-Simons Travel Grant. AC was partially supported by NSF Grant DMS-2532551 and an AMS-Simons Travel Grant. 

1 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

2 

**==> picture [322 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
RI RII RIII<br>**----- End of picture text -----**<br>


FIGURE 1. Reidemeister moves, up to rotations and mirroring. 

**Definition 1.1.** Let _D_ be a diagram of the unknot. 

- (1) We say that _D_ is _weakly hard_ if, in any unknotting Reidemeister sequence _{Di}_ with _D_ 0 = _D_ , there exists an _i_ such that cr( _Di_ ) _<_ cr( _Di_ +1). 

- (2) We say that _D_ is _strongly hard_ if any unknotting Reidemeister sequence _{Di}_ with _D_ 0 = _D_ satisfies cr( _{Di}_ ) _>_ cr( _D_ ). 

When the distinction is important, we include the adjective _planar_ or _spherically_ to indicate we are considering unknotting Reidemeister sequences on the plane or sphere. If a distinction between weak and strong hardness is unimportant, we will simply say _hard_ . 

In other words, weak hardness means that there is no unknotting Reidemeister sequence which is monotonically non-increasing in crossing number, while strong hardness means that the crossing number must increase before it can decrease. Note that strong hardness implies weak hardness, and that one may produce a weakly but not strongly hard diagram by performing crossing-increasing Reidemeister moves on a strongly hard diagram. 

The earliest example of a hard unknot diagram, drawn in Figure 2, was discovered by Goeritz in 1934 [Goe34]. By inspecting each region of the diagram, including the compactified outer region, one can verify that there are no available Reidemeister moves which preserve or decrease the crossing number. Taking for granted that the Goeritz knot is in fact the unknot, it follows that the diagram is strongly spherically hard. Over time, many examples have been discovered and their complexities studied; see [BCL[+] 24] for a recent survey and [ABD[+] 24] for a dataset with 2.6 million diagrams. 

**==> picture [152 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
FIGURE 2. The Goeritz unknot.<br>**----- End of picture text -----**<br>


1.1. **Legendrian knots.** Consider R[3] with the contact structure _ξ_ = ker( _dz − y dx_ ). A knot Λ _⊂_ R[3] is _Legendrian_ if it is everywhere tangent to _ξ_ . Legendrian knot theory is central to modern contact and symplectic topology, leading to rich theories of surgery [Gom98, DG01, CEK24], classification [EH01, Che02, CN13], cobordism [Cha10, EHK12, BST15, CG22], and more [Etn05]. 

A Legendrian knot is completely determined by its _front projection F_ to the ( _x, z_ )-plane, as the _y_ -coordinate can be recovered from _y_ = _dx[dz]_[.][Generic][front][projections][have][semicubical][cusps] in place of vertical tangencies, and strands with more negative ( _x, z_ )-slope always cross over 

HARD LEGENDRIAN UNKNOTS 

3 

**==> picture [322 x 8] intentionally omitted <==**

**----- Start of picture text -----**<br>
RI RII RIII<br>**----- End of picture text -----**<br>


FIGURE 3. Legendrian Reidemeister moves, up to natural symmetries. 

strands with more positive ( _x, z_ )-slope. Any two front projections of the same Legendrian knot are related by a set of _Legendrian Reidemeister moves_ ; see Figure 3. 

A Legendrian knot Λ has three classical invariants: its topological knot type, its _ThurstonBennequin invariant_ tb(Λ), and its _rotation number_ rot(Λ). After the knot type, the former is the integral framing induced by the contact structure, and can be computed combinatorially from the front projection _F_ as follows: 

**==> picture [171 x 23] intentionally omitted <==**

**==> picture [311 x 23] intentionally omitted <==**

Every knot type _K_ has a maximum Thurston-Bennequin invariant tb( _K_ ), a consequence of the Bennequin inequality tb(Λ) + _|_ rot(Λ) _| ≤−χ_ (Σ) where Σ is any Seifert surface [Ben83, Eli92]. Consequently, the maximum Thurston-Bennequin invariant of the unknot is _−_ 1, witnessed by the front projection with two cusps and no crossings. 

FIGURE 4. A Legendrian realization of the Goeritz unknot with tb = _−_ 4. 

1.2. **Hard Legendrian unknots.** Given a smooth knot diagram _D_ , it is straightforward to find a _D_ . Legendrian representative of the knot with a front projection planar isotopic to For example, after a planar isotopy of _D_ we may assume that all overcrossings have negative slope, all undercrossings have positive slope, and all vertical tangencies are nondegenerate. Turning every vertical tangency into a cusp produces a front projection for a Legendrian representative Λ of the knot type. Figure 4 gives a Legendrian representative of the Goeritz unknot. Another example is the Legendrian representative of Adams’ “nasty unknot" [Ada94, Figure 1.29] given in Figure 5. 

Neither of these Legendrian unknots achieve the maximum Thurston-Bennequin invariant of _−_ 1: the Legendrian Goeritz unknot has tb = _−_ 4, and the Legendrian nasty unknot has tb = _−_ 3. In general, as the reader may freely experiment with and confirm, approximating known hard diagrams (c.f. [BCL[+] 24]) by fronts with near-maximal Thurston-Bennequin invariant is difficult. The question of hardness as it relates to the rigidity of a Legendrian knot imposed by the contact structure therefore appears interesting. In particular, it is natural to ask whether some notion of unknot hardness can be achieved with tb = _−_ 1. 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

4 

FIGURE 5. Adams’ nasty unknot on the left, and a Legendrian realization with tb = _−_ 3 on the right. (The smooth diagram is strongly hard on the plane, but not even weakly hard on the sphere.) 

**Definition 1.2** (Legendrian hardness) **.** By a _Legendrian unknotting Reidemeister sequence_ we mean an unknotting Reidemeister sequence of front projections _{Fi}[n] i_ =0[where, up to planar isotopy of] fronts, _Fi_ +1 is obtained from _Fi_ via a Legendrian Reidemeister move, for 1 _≤ i ≤ n_ . We say that a front projection _F_ of a Legendrian unknot is 

- (1) _weakly Legendrian hard_ if in any Legendrian unknotting Reidemeister sequence _{Fi}_ with _F_ 0 = _F_ , there exists an _i_ such that cr( _Fi_ ) _<_ cr( _Fi_ +1). 

- (2) _strongly Legendrian hard_ if any Legendrian unknotting Reidemeister sequence _{Fi}_ with _F_ 0 = _F_ satisfies cr( _{Fi}_ ) _>_ cr( _F_ ). 

When the distinction is unimportant, we simply say _Legendrian hard_ . 

**Definition 1.3** (Smooth hardness) **.** We say that a front projection _F_ of a Legendrian unknot is _smoothly ∗-hard_ (or _smoothly hard_ when a distinction is unimportant) if its _smooth resolution_ , the diagram _D_ obtained by smoothing all cusps, is _∗_ -hard. Here “ _∗_ -hard" stands for any notion of hardness in Definition 1.1. 

Smooth hardness is strictly stronger than Legendrian hardness, as smoothed Legendrian Reidemeister moves comprise a strict subset of smooth Reidemeister moves. A max-tb example . witnessing the difference is given in Figure 6 

FIGURE 6. A Legendrian hard max-tb unknot which is not smoothly hard. The second row depicts the smooth resolution and a sequence of RIII and RI moves; the resulting diagram clearly monotonically simplifies. 

We arrive at the main question of this article. Despite the historical trajectory from Bennequin’s seminal work in contact topology, to Dynnikov’s (naturally Legendrian) grid complexity, to the study of hard unknots, it appears to not have been asked before. 

HARD LEGENDRIAN UNKNOTS 

5 

**Question 1.4.** Is there a smoothly hard front projection of the max-tb unknot? 

Beyond experimental intrigue, investigating Question 1.4 is attractive from the point of view of the unknotting problem. Max-tb unknot fronts form a well-defined class of unknot diagrams which are geometrically motivated and have additional rigidity; one might speculate that there are improved polynomial bounds on the number of unknotting Reidemeister moves for such a class of diagrams (c.f. [Lac15]). 

On the other hand, hardness is also well-motivated from a contact topological point of view. For example, a Legendrian knot is _Lagrangian slice_ if it bounds a Lagrangian disk in the standard symplectic 4-ball [Cha10, CNS16]. One may further ask for such a Lagrangian disk to be _decomposable_ , a combinatorial condition on the front projection [EHK12], or _regular_ , a type of geometric compatibility with a Weinstein structure on the 4-ball [EGL18]. While decomposable implies regular [CET21], it is an open question as to whether the converse holds in this setting [Bre24]. However, by work of Conway, Etnyre, and Tosun [CET21], a Legendrian knot is regularly Lagrangian slice if an only if it can be presented as a max-tb unknot in the boundary of a Weinstein Kirby diagram for the 4-ball. By understanding hardness of max-tb unknots, one might hope to better understand the relationship between regularity and decomposability. 

1.3. **Main results.** We first formalize the experimental observation that it is difficult to draw hard unknot diagrams with max-tb fronts. Using the theory of normal rulings, we establish the following obstructions. 

**Theorem 1.5.** _Let F be a front projection of the max-tb unknot._ 

- (1) _If_ writhe( _F_ ) _≤_ 1 _, then F is not weakly Legendrian hard._ 

- (2) _The smooth resolution of F cannot contain any of the oriented tangles, up to rotation and reversal of total orientation, depicted in Figure 7._ 

_In particular, if D is a hard diagram of the unknot and either_ writhe( _D_ ) _>_ 1 _or D contains one of the tangles in Figure 7, then D cannot be drawn as a max-tb unknot front._ 

**==> picture [329 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
(A) (B) (C)<br>**----- End of picture text -----**<br>


FIGURE 7. Tangles prohibited in a max-tb unknot front. 

There are several known recipes for constructing complicated diagrams of the unknot. Theorem 1.5 prevents many of these from being max-tb unknots. 

**Corollary 1.6.** _The following families of unknots cannot be witnessed by a max-tb front:_ 

- (1) _Hard generalized Freedman-He-Wang unknots_ [BCL[+] 24, §4.1] _._ 

- (2) _Generalized Goeritz unknots_ [BCL[+] 24, §4.2] _._ 

- (3) _Hass-Nowik unknots_ [HN10, Figure 2] _._ 

Using additional obstructions and more sophisticated arguments, we can obstruct a family of hard unknots due to Kauffman and Lambropoulou. 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

6 

**Theorem 1.7.** _The hard unknots of Kauffman-Lambropoulou_ [KL11] _constructed by rational tangles cannot be witnessed by a max-tb front._ 

Beyond the families above, there are 21 diagrams of the unknot highlighted in the survey [BCL[+] 24, Appendix A]. Not all of them are hard in the sense of Definition 1.1, but they are a representative sampling of well-known complicated diagrams. With Theorem 1.5 and additional ad hoc arguments using normal rulings, we can obstruct almost all of them from being max-tb unknots. 

**Theorem 1.8.** _Of the 21 unknot diagrams (up to mirroring) surveyed in_ [BCL[+] 24, Appendix A] _, at least 20 of them cannot be witnessed by a max-tb front._ 

The one diagram we have not obstructed is Haken’s infamous Gordian unknot (see [BCL[+] 24, Figure 25], [PZ16], [Ste09], or the discussion in [G[+] 11]) with 141 crossings and writhe 37. See Table 1 for an accounting of the diagrams considered by Theorem 1.8. 

The recent article [ABD[+] 24] applied reinforcement learning to generate and study 2.6 million hard unknot diagrams. Using Theorem 1.5 and a Python script which computes writhes and searches for prohibited tangles via PD codes, we can obstruct about 67% of them from being max-tb fronts. 

**Corollary 1.9.** _Of the 2,623,588 hard diagrams (up to mirroring) of the unknot studied in_ [ABD[+] 24] _, at least 1,770,489 cannot be witnessed by a max-tb front._ 

_Remark_ 1.10 _._ Below (Conjecture 1.12) we state a conjectural sharp writhe obstruction that a smoothly spherically hard max-tb unknot front must have writhe _≥_ 4. This, together with the prohibited tangles, would obstruct 2,227,501 (about 85%) of the 2,623,588 hard diagrams (up to mirroring) from being witnessed by a max-tb front. 

These obstructions confirm that it is difficult, and in many cases impossible using known examples, to draw a complicated unknot diagram with a max-tb front. Nevertheless, we construct infinitely many smoothly hard max-tb unknots. To state our main result in an even stronger form, note that if _F_ is a front projection of a max-tb unknot, then writhe( _F_ ) = _−_ 1 + 1 _[≥]_[0][.][Let][minwr][R][2][and][minwr] _[S]_[2][denote][the][minimum][writhe][of][a][max-tb][unknot] 2[(#][ of cusps][)] front projection which is smoothly hard on the plane and sphere, respectively. Question 1.4 may then be rephrased as asking whether either of these quantities is finite, and then further refined by asking for the minimum value. 

**Theorem 1.11.** _Smoothly hard Legendrian unknots exist on both the plane and sphere, and_ 

**==> picture [84 x 28] intentionally omitted <==**

An example of a smoothly (strongly, spherically) hard max-tb unknot of writhe 4 is given in Figure 8. In Section 3 we verify its smooth hardness and give other constructions of infinitely many smoothly hard max-tb unknots, establishing the upper bounds of the theorem. 

Our work suggests the following sharp version of Theorem 1.11. 

**Conjecture 1.12.** _For smoothed max-tb Legendrian unknots,_ 

**==> picture [64 x 28] intentionally omitted <==**

To prove Conjecture 1.12, one must increase the lower bounds in Theorem 1.11. As alluded to above, our lower bounds are obtained by appealing to the existence and uniqueness of _normal_ 

HARD LEGENDRIAN UNKNOTS 

7 

FIGURE 8. A smoothly strongly hard max-tb unknot of writhe 4 on the sphere. 

_rulings_ of a max-tb unknot front, a decomposition of the front into certain planar disks first considered by Eliashberg [Eli87] and formalized by Fuchs [Fuc03] and Chekanov and Pushkar [CP07]. The _ruling polynomial_ is a Legendrian isotopy invariant which collects graded counts of normal rulings, and is closely related to the Chekanov-Eliashberg DGA [Fuc03, FI04, Sab05, Lev14]. 

Attempting to use this strategy to prove that minwrR2 _>_ 2 leads one to consider writhe-2 diagrams which admit unique normal rulings. Unlike the writhe-1 case, there are many such fronts representing nontrivial knot types. 

**Definition 1.13.** An _impostor_ is a front projection _F_ which satisfies the following properties: 

- (1) The knot represented by _F_ is not the unknot. 

- (2) The front _F_ admits a unique normal ruling. 

- (3) Up to smooth RIII moves, there are no available crossing-decreasing smooth Reidemeister moves. 

**Theorem 1.14.** _There are infinitely many writhe-_ 2 _impostors._ 

In other words, a writhe-2 impostor is a front which is immune to the normal ruling proof strategy used for obtaining the lower bounds in Theorem 1.11. A proof of Conjecture 1.12 will therefore need to appeal to other topological features of the diagram, which is a subtle problem to overcome. 

1.4. **Further questions.** Beyond Conjecture 1.12, we include some other questions of interest. First, as referenced above, normal ruling invariants may be extracted from the Chekanov-Eliashberg DGA, a deep and widely used tool in Legendrian knot theory. It is known that there are nontrivial Legendrian knots whose DGA is stable-tame isomorphic to that of the max-tb unknot (see [CNS16, p. 821] or [EN20, Appendix A]), which in particular implies that the ruling invariants are identical to that of the unknot. Referencing Definition 1.13, a _strong impostor_ is a front satisfying (1) and (3), and in place of (2), the requirement that the DGA is stable-tame isomorphic to that of the max-tb unknot. Our impostors constructed in Theorem 1.14 are smoothly isotopic to a subset of the pretzel knots referenced by [CNS16] and [EN20]. We do not know if they are Legendrian isotopic, nor have we directly computed the stable-tame isomorphism class of the DGA. Thus: 

**Question 1.15.** Are there infinitely many writhe-2 strong impostors? 

Finally, recall that a knot diagram _D_ is _composite_ if there is an embedded planar circle _C_ such that _|D ∩ C|_ = 2, and there are crossings of _D_ both inside and outside of _C_ . A diagram is _prime_ otherwise. All of our constructions of smoothly hard Legendrian unknots are composite, and crucially so. 

**Question 1.16.** Is there a smoothly hard prime front projection of the max-tb unknot? 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

8 

1.5. **Organization.** In Section 2 we review background on normal rulings of Legendrian knots and use them to prove the various obstruction theorems and corollaries stated above. In Section 3, we construct hard unknots, obtaining the upper bounds of Theorem 1.11. Finally, in Section 4 we construct writhe-2 impostors to prove Theorem 1.14 and discuss their implications . and complications toward a complete proof of Conjecture 1.12 

1.6. **Acknowledgments.** The authors thank Josh Sabloff for interest in our work, and James Hughes for feedback, corrections, and discussion on a preliminary draft. 

## 2. OBSTRUCTING HARDNESS 

We recall the definition of a normal ruling of a Legendrian knot. Given a front projection _F_ , assume that the _x_ -coordinates of all crossings and cusps are distinct. A _normal ruling_ of _F_ is a subset of the crossings, called _switches_ , or _switched crossings_ , such that: 

- (1) Performing 0-resolutions of all switches yields a link of 2-cusp max-tb unknots. We refer to the planar disks bounded by the unknots as _ruling disks_ . 

- (2) Each strand of the 0-resolution near a switch belongs to a different ruling disk. 

- (3) If _x_ 0 is the _x_ -coordinate of a switch, then the ruling disks adjacent to the switch are either disjoint or nested in an arbitrarily small interval ( _x_ 0 _−ϵ, x_ 0+ _ϵ_ ); see Figure 9. This condition is referred to as _normality_ . 

**==> picture [200 x 181] intentionally omitted <==**

FIGURE 9. The normality condition near switched crossings on the left, and the three normal rulings of the trefoil on the right. 

Not every Legendrian knot admits a normal ruling. By [Fuc03, FI04, Sab05], existence of a normal ruling of a knot is equivalent to existence of an augmentation of the Chekanov-Eliashberg DGA. In particular, a Legendrian knot admitting a ruling has maximal Thurston-Bennequin invariant in its topological type. 

Specifying to normal rulings of the max-tb unknot, observe that the standard 2-cusp projection admits a unique (trivial) normal ruling. By [CP07], counts of normal rulings are a Legendrian isotopy invariant, hence any front projection _F_ of the max-tb unknot admits a unique normal ruling. One can moreover show that this unique ruling is _orientable_ in that every switch is a positive crossing. 

HARD LEGENDRIAN UNKNOTS 

9 

The combinatorial formula for the Thurston-Bennequin number gives 

**==> picture [158 x 31] intentionally omitted <==**

where _n_ is the number of ruling disks. Hence, writhe( _F_ ) = _n −_ 1. To _F_ we may associate a graph _G_ with vertices for each ruling disk and edges for each switch adjacent to two eyes. By [CP07, §6], the Euler characteristic of _G_ is invariant under Legendrian isotopy. From the standard 2- cusp unknot front we have _χ_ ( _G_ ) = 1, i.e. _n −_ (# of switches) = 1. Combining this observation with the above calculation, we see 

writhe( _F_ ) = (# of switches) _._ 

Summarizing the important facts: 

**Lemma 2.1.** _Any front projection of the max-tb unknot admits a unique normal ruling and_ writhe( _F_ ) _is given by the number of switches. Moreover, each switch is a positive crossing._ 

This is used in the proof of the following proposition, which establishes the writhe obstruction in Theorem 1.5 and the lower bounds in Theorem 1.11. 

**Proposition 2.2.** _Let F be a front projection of a max-tb unknot with_ writhe( _F_ ) _≤_ 1 _. Then F admits either a simplifying Legendrian RI or a simplifying Legendrian RII move. In particular, F is not smoothly hard on the plane or the sphere._ 

_Proof._ The only max-tb unknot front with writhe( _F_ ) = 0 is the standard two-cusp projection, so assume that writhe( _F_ ) = 1. After a planar isotopy we may further assume that all crossings and cusps have distinct _x_ -coordinates, hence _F_ admits a unique normal ruling. As writhe( _F_ ) = 1, this unique ruling has one switched crossing at an _x_ -coordinate we denote _x_ sw. Decompose the front as 

**==> picture [106 x 10] intentionally omitted <==**

where _F_ sw := _F ∩{|x − x_ sw _| < ϵ}_ , _F_ LC = _F ∩{x ≤ x_ sw _− ϵ}_ , and _F_ RC = _F ∩{x ≥ x_ sw + _ϵ}_ . Here _ϵ >_ 0 is chosen sufficiently small enough so that the switched crossing is the only crossing in _F_ sw. In this case, _F_ sw is either a _nested_ or _non-nested_ switch region (see Figure 10) and the left and right cusp regions each have two cusps. If neither cusp region contains crossings, then _F_ admits a simplifying Legendrian RI move, so we may assume by reflective symmetry that the left cusp region _F_ LC contains crossings. 

Observe that the cusp regions cannot contain any of the three forbidden “clasp" subregions . indicated in the top row of Figure 11 If they did, the modifications drawn in the bottom row of the same figure would produce distinct normal rulings of _F_ , contradicting uniqueness. 

We now proceed with casework based on the the type of switch region. 

CASE 1: Non-nested switch region. 

In the switch region we color the boundary of uppermost ruling disk red. Let _C_ denote the rightmost left cusp in _FLC_ , which, up to reflective symmetry, we may assume is red. By assumption, there must be a first (from the right) crossing of the upper blue and lower red strand. Since _C_ is red, the upper blue strand must either intersect the lower red strand again, or intersect the upper red strand. 

In the former case, the outlawed configurations in Figure 11 force the configuration pictured on the left of Figure 12, where the blue ruling disk intersects the red ruling disk in a ribbon singularity (any other behavior of the lower blue strand would result in a clasp as in Figure 11). We call such a region an _R[∗]_ -region. Note that passing through an _R[∗]_ -region from the right to 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

10 

**==> picture [306 x 234] intentionally omitted <==**

**----- Start of picture text -----**<br>
F = F LC F SW F RC<br>F SW = or or<br>non-nested nested nested<br>**----- End of picture text -----**<br>


FIGURE 10. Decomposition of a writhe-1 unknot front into three regions. 

**==> picture [60 x 103] intentionally omitted <==**

**==> picture [62 x 103] intentionally omitted <==**

**==> picture [60 x 103] intentionally omitted <==**

**==> picture [59 x 102] intentionally omitted <==**

**==> picture [61 x 102] intentionally omitted <==**

**==> picture [60 x 104] intentionally omitted <==**

FIGURE 11. Configurations that violate uniqueness of normal rulings. 

the left is the identity map on the ordering of the strands (i.e. an _R[∗]_ -region is a pure braid). Therefore, in general, we pass through some number of _R[∗]_ -regions; if there are no crossings to the left of an _R[∗]_ -region, there is a Legendrian RII as pictured on the right side of Figure 12. 

Therefore, returning to the context of the first paragraph in CASE 1, we may assume that after the initial red-blue crossing, the upper blue strand has a next intersection with the upper red strand. Up to a planar isotopy that doesn’t affect the switched crossing, we further assume that 

HARD LEGENDRIAN UNKNOTS 

11 

**==> picture [70 x 33] intentionally omitted <==**

**==> picture [76 x 55] intentionally omitted <==**

**==> picture [121 x 9] intentionally omitted <==**

**----- Start of picture text -----**<br>
R [∗] R [∗]<br>**----- End of picture text -----**<br>


FIGURE 12. Identifying the simplifying Legendrian RII move after passing through some number of _R[∗]_ -regions. 

**==> picture [66 x 44] intentionally omitted <==**

**==> picture [72 x 44] intentionally omitted <==**

FIGURE 13. The other type of Legendrian RII move in CASE 1. 

FIGURE 14. The possibilities in CASE 2. 

the two crossings in question occur before any crossings involving the lower blue strand; see the left side of Figure 13. If there are no additional crossings to the left of this region, there is a Legendrian RII as pictured on the right of the same figure. Consequently, we have reduced the proof to CASE 2. 

## CASE 2: Nested switch region. 

There must be a first crossing, from the right, of a red and blue strand. By reflective symmetry, assume without loss of generality that the intersection is with the upper red and blue strands. In order to eventually form a red cusp, there must be a next red-blue crossing. It cannot be another crossing of the upper strands lest there be a clasp as in Figure 11, so the next crossing must . produce either one of the two regions indicated in the top row of Figure 14 

In the left possibility, if there are no further crossings then there is a Legendrian RII as indicated below. Otherwise, we return to CASE 1. In the right possibility, suppose first that there 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

12 

are no additional crossings to the left of the region. Then the left cusp region is determined as indicated, and after a Legendrian isotopy yields a forbidden clasp region. Therefore, there must be additional crossings, which takes us back to the start of CASE 2. 

To conclude, the structure of the proof so far is to cycle between CASE 1 and CASE 2 repeatedly with the only terminating condition being a Legendrian RII move. By compactness of _F_ , the proof must terminate. Therefore, there exists a simplifying Legendrian RII. □ 

Next we establish the prohibited tangles of Theorem 1.5, stated separately as: 

**Proposition 2.3.** _The oriented tangles depicted in Figure 15, up to rotation and total reversal of orientation (but not mirroring) cannot appear in a max-tb unknot front._ 

**==> picture [329 x 108] intentionally omitted <==**

**----- Start of picture text -----**<br>
(A) (B) (C)<br>**----- End of picture text -----**<br>


FIGURE 15. Tangles prohibited in a max-tb unknot front. 

_Proof._ Recall that the unique normal ruling of a max-tb front has the property that every switched crossing is a positive crossing. 

Beginning with the tangle (A), note that each of the three crossings is negative. If the tangle were found in a max-tb unknot front, then none of the three crossings could be switched. The lack of switches means that each strand of the tangle can have 0, 1, or 2 cusps. We will systematically refer to the strand beginning on the lower-left of the tangle as the red strand; the strand beginning on the upper left will be called the blue strand. If one of the strands has 0 cusps, we can normalize it to have slope 0. Assume that the slope-0 strand is the red strand; see the left of Figure 16. Necessarily, the slopes of the blue strand at the crossings, from left to right, are positive, negative, and positive. With the assumed orientation, this is only possible with at least 4 cusps, which is a contradiction. 

If the red strand has one cusp, then at least two of the crossings must occur on one of the two smooth loci of the red strand. If all three of the crossings occur on the same smooth locus, then the argument from the previous case applies, so assume that two of the crossings occur on one smooth locus. The middle of Figure 16 then depicts the two possible cases, up to natural symmetries. In either case the slopes and orientations of the blue strand force more than two cusps. The argument for the third case, where the red strand has two cusps, is similar. Note that a hypothetical normal ruling forces one red cusp to be an up-cusp and the other to be a downcusp. We may also assume that each of the three smooth loci of the red projection supports one intersection, lest we reduce to previous cases. The two cases are depicted on the right side of Figure 16 and again require more than two blue cusps. 

Moving on to tangle (B), note that again all three crossings are negative, hence none of them can be switched in a max-tb unknot ruling. This is impossible, as the strand with the self-crossing would be unicolored, violating a defining property of a ruled front. 

HARD LEGENDRIAN UNKNOTS 

13 

**==> picture [421 x 211] intentionally omitted <==**

FIGURE 16. The minimal cusp cases of tangle (A). Solid lines are Legendrian realized, dashed curves are topologically necessary paths. 

In the tangle (C), the self-crossing of the looping strand is now positive, while the other two crossings are negative. By the same argument in the previous paragraph, we see that the positive crossing must be switched. As the other crossings cannot be switched, the switched loop must be an eye. Moreover, by orientation considerations the color of the strand passing through the loop must be distinct from the color adjacent to the switch. As this strand has no switched crossings, it has either 0, 1, or 2 cusps, as in the analysis of tangle (A). Thus, there are three possibilities for the front, depicted in the top row of Figure 17. Each of the configurations leads to a contradictory extraneous (non-orientable) ruling, possibly after some Reidemeister moves which do not affect the initial ruling, as depicted in the lower row of the figure. □ 

_Remark_ 2.4 _._ The mirroring and orientation of the prohibited tangles in Figure 7 is important. For example, see Figure 18 for a max-tb unknot which contains the mirror of a tangle prohibited by . Proposition 2.3 

With the proof of Theorem 1.5 completed by the previous two propositions, we prove Corol. lary 1.6 

_Proof of Corollary 1.6._ In Figure 19 we recall the construction of generalized Goeritz unknots, generalized Freedman-He-Wang unknots, and Hass-Nowik unknots. The integral boxes represent half-twists (so that the classical Goeritz unknot corresponds to _n_ = 3); a box labeled _K_ is any knot, _K_[¯] is its mirror, and the two strands passing through the box form a cut open copy of the knot and its blackboard pushoff. From the diagrams it is immediate that the generalized Goeritz and Hass-Nowik unknots have prohibted tangles of type (A), so these can never be max-tb unknots. The generalized Freedman-He-Wang unknot has writhe 0, so any hard diagram arising from this construction cannot be a max-tb unknot. □ 

In preparation for the proof of Theorem 1.7, we record another useful observation using the . same idea underlying Proposition 2.3 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

14 

**==> picture [421 x 211] intentionally omitted <==**

FIGURE 17. The minimal cusp cases of tangle (C) in the top row, and the resulting extraneous normal rulings in the bottom row. 

**==> picture [338 x 105] intentionally omitted <==**

FIGURE 18. A max-tb unknot front with the mirror of a prohibited tangle. 

**Proposition 2.5.** _If a tangle of the form in Figure 20 appears in a max-tb unknot front, then both crossings must be switched._ 

_Proof._ It is not possible for exactly one of the crossings to orientably switch, for otherwise there would be an unswitched intersection of the same color. Thus, assume for the sake of contradiction that neither of the crossings are switched. 

Normalize the leftmost crossing so that the overcrossing strand has more negative slope. We additionally may assume without loss of generality that there are no cusps on the segments from this crossing to the boundary of the tangle, i.e. the segments with the arrows in Figure 20, as these have no other intersections with the rest of the tangle. Now we consider all possibilities of minimal cusp examples according to whether the rest of the undercrossing strand has 0, 1, or 2 cusps. By symmetry it suffices to consider the case of 0 or 1 cusp. The two minimal cusp examples are given on the right side of Figure 20, and both lead to extraneous rulings after switching both crossings (c.f. Figure 17). This contradicts uniqueness of rulings, so both crossings must be switched. □ 

Next, we consider the hard unknot diagrams of Kauffman and Lambropoulou. There are a few variations (see [KL11, p. 33]) that can each be obstructed by a similar argument, so we restrict to 

HARD LEGENDRIAN UNKNOTS 

15 

**==> picture [361 x 185] intentionally omitted <==**

**----- Start of picture text -----**<br>
¯<br>n −n K K<br>2 n − 1<br>− 2 n<br>**----- End of picture text -----**<br>


FIGURE 19. Generalized Goeritz (top left, _n ≥_ 3), generalized Freedman-HeWang (top right), and Hass-Nowik (bottom, _n ≥_ 4) unknots. 

**==> picture [102 x 88] intentionally omitted <==**

**==> picture [223 x 88] intentionally omitted <==**

FIGURE 20. A tangle (left) requiring all crossings to be switched. 

their main construction, which we recall now. Given a tuple ( _a_ 1 _, a_ 2 _, . . . , a_ 2 _n_ ) of positive natural numbers with _n ≥_ 2, Kauffman and Lambropoulou prove that the diagram in Figure 21 is hard. (The reader may quickly verify that the diagram is not hard on the sphere when _n_ = 1.) 

**==> picture [358 x 180] intentionally omitted <==**

**----- Start of picture text -----**<br>
±a 1 ±a 2 n− 1<br>∓a 2 ∓a 2 n<br>∓a 1 ∓a 2 n− 1<br>±a 2<br>**----- End of picture text -----**<br>


FIGURE 21. Kauffman-Lambropoulou hard unknots. 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

16 

_Proof of Theorem 1.7._ If both strands entering the left of the central twist box labeled _∓a_ 2 _n_ are oriented in the same direction, then the writhe of the diagram is _∓a_ 2 _n_ ; otherwise, if the strands have opposite orientation the writhe is _±a_ 2 _n_ . If the diagram is a max-tb unknot, then Theorem 1.5 requires the writhe to be _a_ 2 _n ≥_ 2. Therefore, under this assumption, there are two cases to consider: the choice of signs leading to a central box labeled _a_ 2 _n_ and the strands entering the box with the same orientation, or the choice of signs leading to a central box labeled _−a_ 2 _n_ and the strands entering the box with opposite orientation. 

## CASE 1: Central box _a_ 2 _n_ , strands in the same direction. 

We will show that this case cannot occur. Orient the strands passing through the _a_ 2 _n_ box from left to right. Let _s ∈ S_ 3 denote the permutation induced by the the 3-braid _σ_ 2 _[−][a]_[1] _σ_ 1 _[a]_[2] _[· · ·][ σ]_ 2 _[−][a]_[2] _[n][−]_[1] , where we index (horizontal) strands from the bottom. Note that _s[−]_[1] (3) = 3, for otherwise the strand exiting the upper right of the _a_ 2 _n_ box would turn around, pass backward through the above 3-braid, and exit the top left of the _−a_ 1 box heading west. It would then circle around the top of the diagram and enter the upper right of the _a_ 2 _n−_ 1 box, once again emerging from the top left of the _a_ 1 box in a westward direction. But this contradicts the fact that the strands passing through the _a_ 2 _n_ box are oriented eastward. 

Assume for the sake of contradiction that _s[−]_[1] (3) = 2. Then the upper left 3-braid region determines a westward orientation for the strand emanating from the lower left of the _−a_ 1 box, and thus an eastward orientation for the bottom horizontal strand. Note that the upper strand on the left side of the _−a_ 1 box must be oriented eastward, since this strand enters the _a_ 2 _n_ box from its left after passing through the 3-braid region. This, then, means that the strand emanating from the upper right of the _a_ 2 _n−_ 1 box is oriented eastward, and because _s[−]_[1] (3) = 2, that all three lower strands are eastwardly-oriented. See Figure 22. The case _s[−]_[1] (3) = 1 is nearly identical, and is left to the reader. These arguments show that CASE 1 cannot occur. 

**==> picture [368 x 178] intentionally omitted <==**

**----- Start of picture text -----**<br>
−a 1 −a 2 n− 1<br>a 2 a 2 n<br>a 1 a 2 n− 1<br>−a 2<br>**----- End of picture text -----**<br>


FIGURE 22. Orientation contradiction when _s[−]_[1] (3) = 2. 

CASE 2: Central box _−a_ 2 _n_ , strands in opposite direction, _n ≥_ 3. 

Now consider the diagram where the central box is _−a_ 2 _n_ and the strands passing through the box have opposite orientation. Suppose for the sake of contradiction that the diagram is a ruled max-tb unknot. First assume _n ≥_ 3. Since _a_ 2 _n ≥_ 2, Proposition 2.5 implies that all crossings in the tangle formed by the _−a_ 2 _n_ box must be switched. Therefore, the two strands emanating from the right of the _−a_ 2 _n_ box have the same color (blue), and the two strands emanating from the 

HARD LEGENDRIAN UNKNOTS 

17 

left have the same color (red). Since the writhe of the diagram is _a_ 2 _n_ , there are no other switches. As no other crossings in the diagram are switched, two strands of the same color cannot pass through any of the other boxes, for otherwise this would violate the ruling property. 

This latter observation forces the lower strand emanating from the left of the _−a_ 1 box to the right of the _−a_ 2 _n_ box to be red. It turns around and enters the _−a_ 2 box from the left as the lower strand, forcing the other strand passing through the box to be blue, and the third strand in the 3- braid region to be red. Analyzing the _a_ 3 box, the same reasoning implies that the strands exiting to the right of the _−a_ 2 are red on the bottom and blue on top. In particular, _a_ 2 must be even. Since _n ≥_ 3, the same argument applies by studying the region between the _a_ 3 and _−a_ 4 box and we conclude that _a_ 3 is even. Continuing, we conclude that _a_ 2 _, . . . , a_ 2 _n−_ 2 are even. 

**==> picture [392 x 145] intentionally omitted <==**

**----- Start of picture text -----**<br>
a 1 a 3 a 2 n− 1<br>−a 2 −a 2 n<br>−a 1 −a 3<br>a 2<br>**----- End of picture text -----**<br>


FIGURE 23. The portion of the diagram relevant for the contradiction when _n ≥_ 3 and the central box is _−a_ 2 _n_ . 

On the other hand, consider the two red strands exiting to the left of the _−a_ 2 _n_ box. It follows that _a_ 2 _n−_ 1 must be odd, lest there be two red strands passing through the _a_ 2 _n−_ 2 box. 

Now we investigate the orientations of the strands. Orient the blue strands incident to the _−a_ 2 _n_ box as indicated in Figure 23; this determines the orientation of the rest of the blue strand in the upper left 3-braid region (but it does not determine the orientation of the red strand, as this depends on the parity of _a_ 2 _n_ ). Notice, however, that the red strand must pass through the _−a_ 2 box from right to left, for otherwise Proposition 2.5 would imply that all _an ≥_ 2 crossings in that box are switched, which is a contradiction. Following along this strand, we see that the strands pass through the _−a_ 1 box with opposite orientation. Appealing once again to Proposition 2.5, we are forced to conclude _a_ 1 = 1. Evenness of _a_ 2 then forces the red strands to enter in opposite orientation through the _−a_ 3 box. Earlier, though, we concluded that _a_ 3 is even, and Proposition 2.5 then forces both of these crossings to switch, a contradiction. 

CASE 3: Central box _−a_ 2 _n_ , strands in opposite direction, _n_ = 2. 

For the special case _n_ = 2, the same argument implies _a_ 2 is even and _a_ 1 = 1. The difference is that _a_ 3 = _a_ 2 _n−_ 1 is definitively odd, so we do not yet have a contradiction. However, the same reasoning we applied to the _−a_ 1 box applies to the _−a_ 3 box and we conclude that, in fact, _a_ 3 = 1. Moreover, to prevent the _−a_ 2 box from becoming a prohibited (A) tangle, we in fact have _a_ 2 = 2. Letting _a_ 4 =: 2 _k_ , these simplifications then lead us to the diagram on the left side of Figure 24. 

Next, observe that any front projection _F_ of the max-tb unknot with its unique normal ruling has the following property. Viewing the smooth diagram _D ⊂ S_[2] , and given any point _p ∈/ D_ , there is a circle _C ⊂ S_[2] passing through _p_ , intersecting _D_ transversely and away from double 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

18 

**==> picture [433 x 97] intentionally omitted <==**

**----- Start of picture text -----**<br>
− 2 k<br>**----- End of picture text -----**<br>


FIGURE 24. The case _n_ = 2, and the dual graph for _−_ 2 _k_ = _−_ 2. 

points, such that _C_ intersects each color no more than twice. (These circles correspond to vertical lines in the front projection.) We claim that the diagram in Figure 24 does not have this property. 

This is easiest to see from the perspective of the dual graph of the diagram, with edges colored according to the ruling. We have drawn the dual graph for _−_ 2 _k_ = _−_ 2 on the right, with the vertex corresponding to the region at infinity drawn as a black rectangle; it will be clear that the argument holds for any _k_ . The above circle property implies the following property of the dual graph: given any interior vertex, there is a walk from the rectangle at infinity to the prescribed vertex and back to the rectangle at infinity such that each edge color is traversed no more than twice. 

Our diagram fails to have this property because of the starred vertex. Note that any walk from the starred vertex to the rectangle at infinity traverses at least two red edges. Therefore, any “circle" from the rectangle to the starred vertex and back must traverse at least four red edges. This is a contradiction, which completes the proof. □ 

Now we prove Theorem 1.8. The summary of the obstructions is in Table 1. 

_Proof of Theorem 1.8._ Any of the diagrams with writhe 0 or 1 that are weakly planar hard are ruled out from being max-tb unknot fronts by the writhe obstruction in Theorem 1.5. This accounts for [BCL[+] 24, Figures 8, 10, 11, 12, 15, 19, 20, 28]. By inspection, the (appropriately mirrored, as indicated in Table 1) [BCL[+] 24, Figures 14, 18, 23, 24, 28] contain tangle (A), [BCL[+] 24, Figure 13] contains tangle (B), and the [BCL[+] 24, Figures 21, 22] contain tangle (C), obstructing each of these. 

This leaves the appropriately mirrored [BCL[+] 24, Figures 9, 16, 17, 27]. The rest of the proof is dedicated to ad hoc arguments using the same reasoning underlying Proposition 2.3 for these figures. We can quickly dispense of [BCL[+] 24, Figure 16], because it has writhe 1, hence the hypothetical unique oriented normal ruling would have one switch, which is a positive crossing. One can quickly verify that none of the 8 positive crossings, when switched, yield a decomposition of the diagram into two planar disks. The remaining three diagrams are considered in three separate arguments. 

CASE 1: [BCL[+] 24, Figure 27]. 

We begin with the simplest argument for [BCL[+] 24, Figure 27] (which is the same as [PZ16, Figure 27]). First, note that in a diagram of the max-tb unknot, any tangle of the form given in Figure 25 (or its mirror) must have at least one switched crossing, for if it didn’t, the selfintersecting strand would violate the ruling condition. The diagram in question has 16 pairwise disjoint tangle regions of this form, hence a hypothetical normal ruling would have at least 16 switched crossings. This contradicts the fact that the writhe is 4. 

CASE 2: [BCL[+] 24, Figure 17], the Ochiai I unknot. 

HARD LEGENDRIAN UNKNOTS 

19 

|[BCL+24,Figure_∗_]|**Mirror**|**W.P.H?**|**S.S.H?**|**Writhe**|**Max-tb front?**|**Obstruction**|
|---|---|---|---|---|---|---|
|8||✓|✓|0|X|writhe|
|9|✓|✓|✓|3|X|ad hoc|
|10||✓|✓|0|X|writhe|
|11|✓|✓|✓|1|X|writhe|
|12||✓|✓|1|X|writhe|
|13||✓|✓|2|X|tangle(B)|
|14|✓|X|X|2|X|tangle(A)|
|15||✓|✓|1|X|writhe|
|16||?|X|1|X|ad hoc|
|17||?|X|2|X|ad hoc|
|18||?|X|5|X|tangle(A)|
|19||✓|X|0|X|writhe|
|20||✓|X|0|X|writhe|
|21|✓|?|X|3|X|tangle(C)|
|22||✓|✓|3|X|tangle(C)|
|23|✓|?|X|5|X|tangle(A)|
|24||✓|✓|5|X|tangle(A)|
|25||?|X|37|?||
|26|✓|?|X|1|X|tangle(A)|
|27|✓|✓|✓|4|X|ad hoc|
|28||✓|✓|0|X|writhe|



TABLE 1. Analyzing the unknot diagrams in [BCL[+] 24, Appendix A] using the figure enumerations in that article. For diagrams with nonzero writhe, we have indicated whether we use the mirror of their diagram to obtain a non-negative writhe. W.P.H stands for weakly planar hard (the weakest form of hardness) and S.S.H stands for strongly spherically hard (the strongest form of hardness). 

**==> picture [88 x 88] intentionally omitted <==**

FIGURE 25. A tangle requiring at least one switched crossing. 

The relevant unknot diagram is drawn on the left of Figure 26, with positive (negative) crossings highlighted in green (resp. pink). Assume for the sake of contradiction that there is a max-tb front witnessing the diagram, so that it admits a unique normal ruling which is moreover orientable. Then none of the negative crossings may be switched. Consequently, we must color the strand emanating north from the crossing labeled _a_ to crossing _b_ with a single color. Likewise, the strand emanating east from crossing _c_ to crossing _d_ must be uni-colored. Since it crosses the red strand at an unswitched crossing, we must use a different color (blue). Similarly, the strand emanating east from _e_ to _f_ must be uni-colored with a third color (yellow) as it intersects 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

20 

both red and blue at unswitched crossings. This produces the partial coloring in the middle of . Figure 26 

**==> picture [356 x 171] intentionally omitted <==**

**----- Start of picture text -----**<br>
e<br>c<br>b a<br>d<br>f<br>**----- End of picture text -----**<br>


**==> picture [109 x 168] intentionally omitted <==**

FIGURE 26. The Ochiai I unknot, [BCL[+] 24, Figure 17]. 

Now we consider the positive crossings _b_ and _c_ . Note that it is not possible for both crossings to be switched, for otherwise the strand emanating north from _b_ to _c_ would be simultaneously red and blue. The same reasoning applied to the strand emanating west from _b_ to _c_ implies that at least one of these crossings must be switched. Thus, precisely one of _b_ or _c_ must be a switched crossing. 

On the right of Figure 26 we consider the case where _b_ is switched and _c_ is unswitched. As a consequence, the strand from the overcrossing at _d_ to _b_ must be blue. But this forces a switch at crossing _d_ , where both strands are blue. At this point, we have used two switches, and since the writhe of the diagram is 2 there are no other switched crossings. We are then forced to color the rest of the diagram as indicated in the third panel of the figure, which yields a contradiction: there are intersections of the yellow color at unswitched crossings. The case where _c_ is switched and _b_ is unswitched is similar. 

CASE 3: The mirror of [BCL[+] 24, Figure 9], the _D_ 43 unknot. 

The mirror of [BCL[+] 24, Figure 9] requires a similar but more involved ad hoc argument. The diagram is drawn on the left side of Figure 27; for simplicity, we have suppressed explicit crossing information and have only indicated the orientation and whether the crossing is positive or negative, which is all that is needed for the argument. 

Assume for the sake of contradiction that the diagram admits a normal ruling. Since the writhe is 3, there are three switched crossings, all positive. Beginning at the positive crossing labeled _a_ in the right side of Figure 27, the strand emanating to the west passes through a sequence of negative crossings, all necessarily unswitched, until it reaches the positive crossing labeled _b_ . We color this stretch red. Note that _b_ cannot be a switch, for otherwise the orientation would force the red strand to turn north. To avoid a red-red unswitched intersection, the subsequent crossing needs to switch, sending the red strand east; the same argument holds for the next three crossings, resulting in 5 switches. Thus, _b_ is unswitched. The strand from _b_ to _a_ is thus red, and we see that _a_ is necessarily a switched crossing. We color the other strands adjacent to _a_ blue, and note that the eastward segment extends through a negative crossing to the positive crossing labeled _c_ . 

HARD LEGENDRIAN UNKNOTS 

21 

**==> picture [299 x 226] intentionally omitted <==**

**----- Start of picture text -----**<br>
e<br>b<br>a<br>d c<br>**----- End of picture text -----**<br>


**==> picture [125 x 201] intentionally omitted <==**

FIGURE 27. The mirror of the _D_ 43 unknot, [BCL[+] 24, Figure 9]. 

Now consider the segment beginning at the crossing labeled _d_ and heading north. This passes through both blue and red via unswitched crossings en route to the positive crossing labeled _e_ , hence is necessarily a third color, yellow. 

**==> picture [226 x 226] intentionally omitted <==**

**----- Start of picture text -----**<br>
e<br>b<br>a<br>h<br>f d c<br>j<br>i<br>g<br>**----- End of picture text -----**<br>


FIGURE 28. The final contradiction ruling out [BCL[+] 24, Figure 9]. 

Next, in Figure 28, consider the segment emanating to the west from crossing _d_ to the positive crossing labeled _f_ . We claim that this segment must be the fourth and final color, green, of the assumed normal ruling. It cannot be red, as the entire red ruling disk is already drawn. It cannot be yellow, for the crossing at _d_ would result in a yellow-yellow intersection that cannot be orientably switched. If it were blue and _d_ were unswitched, then _c_ would be a blue-blue 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

22 

intersection which cannot be orientably switched. If it were blue and _d_ were switched, then the trigon involving _c, d_ , and the negative crossing north of _d_ would violate the normality condition at a switch under any possible Legendrian realization of the diagram. Thus, the _d_ -to- _f_ segment must be green. 

Now we turn our attention to the unicolored strand emanating west from the crossing labeled _g_ , passing through two unswitched crossings, and terminating at crossing _h_ . This strand cannot be blue, because _h_ would be a blue-blue intersection which cannot be orientably switched. It cannot be green, for if _h_ were unswitched there would be an unswitched green-green intersection to the right of _f_ , and if _h_ were switched then _f_ would be a green-green intersection which cannot be orientably switched. Thus, the _g_ -to- _h_ segment must be yellow. 

Finally, observe that the two horizontal segments (dashed and dotted in Figure 28) which intersect this yellow segment must be green and blue, in some combination. Indeed, they cannot be the same color, for otherwise the positive crossing at _i_ would involve a same-color intersection which cannot be orientably switched. As the segment emanating north from _g_ and terminating at _j_ also intersects these green and and blue segments at unswitched crossings, it must be colored yellow. However, this produces our contradiction: at crossing _g_ , there is a yellow-yellow intersection which cannot be orientably switched. □ 

## 3. CONSTRUCTING HARD LEGENDRIAN UNKNOTS 

We identify a class of minimally-twisting Legendrian arcs which are smoothly hard relative to their endpoints. Precisely: 

**Definition 3.1.** A _(left) building block_ is a front projection _Fℓ ⊂_ ( _−∞,_ 0] _x ×_ R _z_ such that 

   - (1) _Fℓ ∩{x_ = 0 _}_ consists of two points, 

   - (2) the front projection _F_[ˆ] _ℓ ⊂_ R[2] obtained by closing _Fℓ ∩{x_ = 0 _}_ with a right cusp represents a max-tb unknot, 

   - (3) the only good spherical Reidemeister move available in _D_[ˆ] _ℓ_ , the smoothing of _F_[ˆ] _ℓ_ , is a RII _[−]_ move corresponding to a region bounded by said right cusp, and 

   - (4) the exhaustion of RIII moves in _D_[ˆ] _ℓ_ reveals no other good Reidemeister moves and additionally leaves the region corresponding to the RII _[−]_ move unaffected. 

- A _(right) building block_ is defined analogously for a front in [0 _, ∞_ ) _×_ R. We call a building block _strong_ if the following additional property holds: 

   - (5) After introducing an additional positive crossing near the endpoints at _x_ = 0 (see Figure 31, for example), the created smooth RIII move and its exhaustion leads to no new good Reidemeister moves. 

**Lemma 3.2.** _The front projections in Figure 29 are strong building blocks of writhe_ 2 _._ 

FIGURE 29. Two (left, strong) building blocks of writhe 2. 

HARD LEGENDRIAN UNKNOTS 

23 

_Proof._ That each front admits a right-cusp closure to the max-tb unknot is immediate (see the top of Figure 30), as is the observation that each smoothing has only one available good Reidemeister (RII _[−]_ ) move corresponding to the right-cusp region highlighted in yellow in the middle row of Figure 30. These observations give (1), (2), and (3) of Definition 3.1. It remains to verify (4). To that end, we have also highlighted (in blue and green, and blue, respectively) the available RIII moves for each smoothed building block. On the left, performing each move (blue or green) only introduces the corresponding inverse RIII move (red); moreover, neither move interacts with the yellow region. On the right, the blue RIII introduces its inverse (red) and a new RIII (green); performing the green move leads to a dead end, and again the yellow region is untouched. Thus, for both blocks, (4) holds. 

**==> picture [12 x 10] intentionally omitted <==**

**==> picture [12 x 10] intentionally omitted <==**

**==> picture [24 x 21] intentionally omitted <==**

**==> picture [62 x 42] intentionally omitted <==**

**==> picture [16 x 13] intentionally omitted <==**

**==> picture [11 x 8] intentionally omitted <==**

**==> picture [13 x 12] intentionally omitted <==**

**==> picture [16 x 11] intentionally omitted <==**

**==> picture [9 x 9] intentionally omitted <==**

**==> picture [29 x 19] intentionally omitted <==**

**==> picture [18 x 9] intentionally omitted <==**

**==> picture [12 x 13] intentionally omitted <==**

**==> picture [22 x 15] intentionally omitted <==**

**==> picture [15 x 13] intentionally omitted <==**

**==> picture [12 x 13] intentionally omitted <==**

**==> picture [15 x 14] intentionally omitted <==**

**==> picture [15 x 15] intentionally omitted <==**

**==> picture [15 x 8] intentionally omitted <==**

FIGURE 30. The building block proof in Lemma 3.2. 

The verification of strongness boils down to an exhaustion of the Reidemeister graph of the diagram with the additional positive crossing; we verify this explicitly for the second front, and leave the slightly more tedious check of the first front to the reader.[1] 

Fixing the already present blue RIII move, the newly created RIII move leads to a linear chain of RIII moves which terminates; this is depicted in Figure 31. One may check that at no point the linear chain of RIII moves beginning with the blue region (as shown on the right side of Figure 30) admits a nontrivial interaction with the new linear chain of RIII moves. Therefore, the indicated building block is strong. □ 

_Remark_ 3.3 _._ Given the examples in Figure 29, it is straightforward to concoct building blocks with larger complexity, either in crossing number and/or writhe, by weaving eyes in and out of each other to create additional clasps. See Figure 32 for two example families, one which remains minimal in writhe and another which increases in writhe. The blocks in Figure 29 are variations on the simplest examples (in both crossing number and writhe) the authors were able to construct. In fact, by Proposition 2.2 and Proposition 3.4 below, it follows that the writhe of a building block must be at least 2, hence these examples are writhe-minimizing. 

> 1No generality of our results is lost by only considering the second front, for which we explicitly verify strongness; we have simply provided two examples for the sake of variety. 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

24 

**==> picture [29 x 20] intentionally omitted <==**

**==> picture [16 x 10] intentionally omitted <==**

**==> picture [12 x 8] intentionally omitted <==**

**==> picture [29 x 20] intentionally omitted <==**

**==> picture [29 x 10] intentionally omitted <==**

**==> picture [8 x 7] intentionally omitted <==**

**==> picture [29 x 20] intentionally omitted <==**

**==> picture [10 x 9] intentionally omitted <==**

**==> picture [15 x 11] intentionally omitted <==**

- FIGURE 31. Proving strongness in Lemma 3.2. 

**==> picture [162 x 161] intentionally omitted <==**

FIGURE 32. On the top, an infinite family of building blocks of writhe 2. On the bottom an infinite family of building blocks with increasing writhe. 

**Proposition 3.4.** _Given left and right building blocks Fℓ and Fr, the front projection obtained by their sum as on the right side of Figure 33 is a smoothly spherically hard max-tb unknot of writhe_ wr( _Fℓ_ ) + wr( _Fr_ ) _. Given a strong building block Fℓ, the front projection obtained as on the left side of Figure 33 is a smoothly planar hard max-tb unknot of writhe_ wr( _Fℓ_ ) + 1 _._ 

_Proof._ First, we consider the spherical recipe on the right. By definition, _F_[ˆ] _ℓ_ and _F_[ˆ] _r_ are maxtb unknots; the composite front is obtained by performing a Legendrian surgery (smoothly, a connect sum) on split copies _F_[ˆ] _ℓ ⊔ F_[ˆ] _r_ of the fronts. Being a split sum of unknots, the result is an unknot. The Thurston-Bennequin invariant is maximized because the Legendrian surgery on fillable knots induces a Lagrangian filling of the composite [Cha10, EHK12]. The Legendrian surgery also destroys both available good RII _[−]_ present in the smoothing _D_[ˆ] _ℓ ⊔ D_[ˆ] _r_ and thus the composite diagram has no good Reidemeister moves. Moreover, by (4) of Definition 3.1, the available RIII moves on either side of the diagram sum do not interact and thus lead to no emergent good moves; it follows that the diagram is smoothly spherically hard. The writhe computation follows from the fact that writhe is additive under connect sum. 

HARD LEGENDRIAN UNKNOTS 

25 

**==> picture [330 x 92] intentionally omitted <==**

**----- Start of picture text -----**<br>
Fℓ Fℓ Fr<br>**----- End of picture text -----**<br>


FIGURE 33. On the left, a planar hard max-tb unknot of writhe wr( _Fℓ_ ) + 1. On the right, a spherically hard max-tb unknot of writhe wr( _Fℓ_ ) + wr( _Fr_ ). 

FIGURE 34. The 0-resolution of a front projection of the standard Legendrian unknot with respect to its unique ruling. 

Next, we consider the planar recipe on the left. The resulting front is smoothly an unknot because of the spherical RIII move off to infinity, and the Thurston-Bennequin calculation is immediate. It only remains to verify that the diagram is smoothly hard on the plane. This is where the assumption of strongness enters: the additional positive crossing in the diagram creates a smooth RIII move. However, by assumption, the exhaustion of this RIII move leads to no good Reidemeister moves on the plane. Thus, the diagram is smoothly hard on the plane. □ 

**Example 3.5.** The front in Figure 8 is given by applying Proposition 3.4 to the leftmost building block in Figure 29 and (the rotation of) the rightmost building block in the same figure. The front is therefore smoothly spherically hard. 

## 4. IMPOSTORS 

Given the relatively small number of cases which arise in proving Proposition 2.2, it is tempting to apply the approach of that proof to a writhe-2 front projection _F_ of the max-tb unknot. In the present section we disabuse ourselves of this temptation by constructing infinitely many _impostors_ — writhe-2 front projections of Legendrian knots which are not the max-tb unknot, but whose classical invariants and ruling polynomial agree with those of the max-tb unknot. While the only structural feature of _F_ needed to prove Proposition 2.2 was the uniqueness of its ruling, these examples demonstrate that additional structure will be necessary in analyzing the writhe-2 case. 

4.1. **Writhe 2 diagrams of the standard unknot.** We explain the origin of our impostors by first making an observation about 0-resolutions of writhe-2 front projections of the max-tb unknot. Given any ruling _R_ of a front projection _F_ (of any Legendrian knot in (R[3] _, ξ_ std)), we may denote by Λ0( _F, R_ ) the front projection obtained by performing the 0-resolution at each switch of _R_ . See Figure 34. When the ruling _R_ is understood (e.g., when _F_ admits a unique ruling), we will write Λ0( _F_ ). 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

26 

**==> picture [238 x 163] intentionally omitted <==**

FIGURE 35. The three configurations of _B_ and _R_ prohibited by Figure 10 fail to lead to an extraneous ruling if _Y_ meets the clasp region at a switch. 

**Proposition 4.1.** _Let F be a front projection of the max-tb unknot with_ writhe( _F_ ) = 2 _. Then there is a sequence of Legendrian RIII moves which, when applied to F , produces a front projection F[′] with the property that_ Λ0( _F[′]_ ) _consists of three pairwise unlinked Legendrian eyes._ 

_Proof._ Because _F_ is a front projection of the max-tb unknot, it admits a unique ruling; because writhe( _F_ ) = 2, the resolution Λ0( _F_ ) of this ruling consists of three Legendrian eyes, which we denote _B_ , _R_ , and _Y_ . We will show that the components _B_ and _R_ must be unlinked in the absence of _Y_ , possibly after first applying some Legendrian RIII moves to _F_ . We will make no assumption about the existence of a switch between these components, and thus the argument will apply to any pair of the three components. 

Even without a switch between _B_ and _R_ , we may find a portion _{x_ 0 _− ϵ ≤ x ≤ x_ 0 + _ϵ}_ of the front projection in which the regions bounded by _B_ and _R_ are either nested or disjoint. For instance, such a region may be found near the right cusps of _F_ . We can now proceed to apply the casework of Proposition 2.2, except that ruling out the clasp subregions depicted in the top row of Figure 11 may first require the application of Legendrian RIII moves. 

Specifically, a clasp subregion _rc_ may fail to lead to an extraneous ruling if the third component _Y_ shares a switch with _B_ or _R_ along the boundary of _rc_ . In this case, we say that _rc_ is a _switched_ clasp subregion. See Figure 35. For instance, suppose _Y_ and _B_ share a switch along the boundary of _rc_ , as depicted in Figure 36. In this case, we may destroy the subregion _rc_ by applying a Legendrian RIII move which slides _R_ across the switch. See the top row of Figure 36. Notice that this modification creates additional crossings between _R_ and _Y_ , but does not create a prohibited clasp subregion between these components. If a prohibited clasp subregion between _R_ and _Y_ were created by this move, then the two crossings of _R_ and _B_ which occur along the boundary of _rc_ could have been made into switches, providing an extraneous ruling of _F_ . See the bottom row of Figure 36. 

Following the elimination of all clasp subregions, _B_ and _R_ admit an initial region analogous to the switch region _F_ sw used in Proposition 2.2. We may now apply the argument of Proposition 2.2 to the link _B ∪ R_ in the absence of _Y_ to see that _B_ and _R_ are unlinked. Because the Legendrian Reidemeister moves used to eliminate switched clasp regions between _B_ and _R_ do not create additional clasp regions, the same argument applies to the pairs _B, Y_ and _R, Y_ . □ 

27 

HARD LEGENDRIAN UNKNOTS 

**==> picture [77 x 67] intentionally omitted <==**

**==> picture [77 x 36] intentionally omitted <==**

**==> picture [77 x 47] intentionally omitted <==**

FIGURE 36. By applying a Legendrian RIII we may eliminate the clasp regions seen in Figure 35. This will create additional crossings between _R_ and _Y_ , but does not create prohibited clasps, lest _F_ admit an extraneous ruling. 

Proposition 4.1 tells us that the Legendrian eyes _B_ , _R_ , and _Y_ of Λ0( _F_ ) form either an unlink or a Brunnian link. Mohnke has shown in [Moh01] that it is not possible to form the Borromean rings out of three max-tb Legendrian unknots, regardless of their front projections. On the other hand, there exist non-trivial, _n_ -component Brunnian links whose components are all max-tb Legendrian unknots, for any _n ≥_ 2. See Figure 37 for an example when _n_ = 3. 

**==> picture [280 x 130] intentionally omitted <==**

FIGURE 37. A 3-component Brunnian link. 

Given our requirement that _B_ , _R_ , and _Y_ be eyes, we have the following question: 

**Question 4.2.** Does there exist a Legendrian realization of a Brunnian link whose front projection consists of Legendrian eyes? 

The authors suspect that the answer to this question is no, and thus that _B ⊔ R ⊔ Y_ is an unlink. The 3-component case could plausibly be answered with some tedious casework in the front projection, but the impostors we produce in the next subsection undermine the usefulness of knowing _B ⊔ R ⊔ Y_ to be an unlink, so we do not pursue this casework here. 

4.2. **Constructing impostors.** Proposition 4.1 provides a recipe for constructing all front projections of the max-tb Legendrian unknot with writhe 2: join three pairwise-unlinked Legendrian eyes in R[2] _xz_[into][a][single][component][by][adding][two][switched][crossings,][and][then][perform][ar-] bitrary Legendrian RIII moves. Note that the RIII moves have no effect on hardness. One can 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

28 

FIGURE 38. A front projection of _m_ (946) which admits no simplifying Legendrian Reidemeister moves. 

FIGURE 39. On the left, a front projection of 11 _n_ 139 which admits no simplifying Legendrian Reidemeister moves. Twisting the blue and yellow bands around each other _m_ times produces a front projection of _P_ ( _−_ 2 _m −_ 5 _, −_ 3 _,_ 3). 

resolve the question of writhe-2 hardness by either showing that this recipe always results in a diagram which admits a simplifying Reidemeister move or by using the recipe to construct a hard diagram for the standard unknot. We have done neither. 

The essential problem with this strategy is that, while every writhe-2 diagram of the standard Legendrian unknot results from the algorithm described, the algorithm can also produce nontrivial knot types. Consider Figure 38, which exhibits a front projection _F_ of a Legendrian knot of smooth type _m_ (946). As depicted, this front projection admits rulings _R_ 1 and _R_ 2 so that the 0-resolutions Λ0( _F, R_ 1) and Λ0( _F, R_ 2) are both unlinks of three Legendrian eyes. 

While the front projection seen in Figure 38 disrupts our initial strategy, recall that the standard Legendrian unknot has ruling invariant 1. So one may revise the strategy and hope to show that any _uniquely-ruled_ front projection resulting from our recipe must admit a simplifying Legendrian RII move. This hope is quickly dashed by the front projection seen on the left of Figure 39. This is a front projection for a Legendrian knot Λ of smooth type 11 _n_ 139, with classical invariants tb(Λ) = _−_ 1 and r(Λ) = 0. Rutherford has shown in [Rut06] that the (ungraded) ruling polynomial of a Legendrian knot is determined by its smooth isotopy class and classical invariants, and Cornwell-Ng-Sivek have exhibited in [CNS16] a Legendrian 11 _n_ 139 with these classical invariants whose ruling polynomial is 1. It follows that the Legendrian 11 _n_ 139 depicted in Figure 39 has a unique ruling, and is thus an impostor. 

In fact, by twisting the blue and yellow bands in our front projection of 11 _n_ 139, we obtain infinitely many front projections which have writhe 2, admit a unique ruling, and whose 0- resolution under this ruling is a 3-component unlink of Legendrian eyes. Indeed, the writhe and 0-resolution of these examples are evident in Figure 39, and we will compute the ruling polynomials of these fronts by determining their smooth type. 

**Proposition 4.3.** _The Legendrian knot whose front is given in the right panel of Figure 39, which includes m full twists of the blue and yellow bands of_ 11 _n_ 139 _, is smoothly isotopic to the pretzel knot P_ ( _−_ 2 _m −_ 5 _, −_ 3 _,_ 3) _._ 

_Proof._ Figures 40 to 42 exhibit a smooth isotopy from our diagram to the pretzel knot _P_ ( _−_ 2 _m −_ 5 _, −_ 3 _,_ 3). Specifically, the diagram obtained by smoothing the front in Figure 39 is seen in the 

29 

**==> picture [126 x 6] intentionally omitted <==**

**----- Start of picture text -----**<br>
HARD LEGENDRIAN UNKNOTS<br>**----- End of picture text -----**<br>


**==> picture [58 x 68] intentionally omitted <==**

**==> picture [76 x 60] intentionally omitted <==**

FIGURE 40. The first two steps of our smooth isotopy. 

**==> picture [390 x 187] intentionally omitted <==**

**----- Start of picture text -----**<br>
(A) (B) (C)<br>8 m 8 m − 4 8 m − 4<br>8 m − 4 8 m − 8 8 m − 8<br>(D) (E) (F)<br>**----- End of picture text -----**<br>


FIGURE 41. Unraveling the tangle. The number in each picture represents the number of crossings in the region between the two vertical bars. 

leftmost panel of Figure 40. By reflecting the blue and red arcs of that diagram, we obtain a diagram with 6 fewer crossings, as seen in the middle panel of Figure 40. Next, we push the three crossings highlighted in the middle panel along the indicated arcs, obtaining the rightmost . panel of Figure 40 The next stage of our isotopy focuses on the tangle highlighted in that panel. 

The relevant tangle is seen in panel (A) of Figure 41, where we have highlighted the fact that the vertical ordering of the bands is preserved after _m_ full twists. This highlighting is reversed in panel (B), where we have moved one half-twist of the bands into view. Next, we reflect the red arc and then the blue arc to obtain panel (C). The four crossings revealed in panel (B) have now been reduced to two, and we obtain panel (D) by pushing these crossings along the band. Moving another half-twist of the bands into view brings us to panel (E), which bears a superficial resemblance to panel (B); notice, however, the crossing data along the vertical arc. Adding a twist to the vertical arc in panel (E) produces panel (F), and from here we may iterate the process which transforms (B) into (F). The difference in highlighting between panels (B) and (F) does not prevent us from applying these steps. Notice that we have removed four crossings between the bands at the expense of creating three crossings: two in the bottom-left of the tangle, and one in the vertical arc. By iterating the process, we transform the 8 _m_ crossings of panel (A) into 4 _m_ crossings in the bottom-left of the tangle, plus 2 _m −_ 1 crossings along the vertical arc. Applying the isotopy of Figure 41 to the tangle highlighted in the last panel of Figure 40 produces the first . panel of Figure 42 

Finally, the 4 _m_ crossings in the bottom-left of the tangle are pushed along the band, as indicated in the first panel of Figure 42. The red arc in the second panel of that figure is then 

JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

30 

**==> picture [201 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
2 m<br>− 2 m − 4  {<br>4 m<br>− 2 m − 4  { − 2 m − 5  {<br>**----- End of picture text -----**<br>


FIGURE 42. The final steps of our smooth isotopy to _P_ ( _−_ 2 _m −_ 5 _, −_ 3 _,_ 3). 

reflected, decreasing by one the number of crossings in the diagram. At last, the highlighted crossing in the third panel of Figure 42 is pushed along the indicated arc, producing the diagram for _P_ ( _−_ 2 _m −_ 5 _, −_ 3 _,_ 3) seen in the final panel. 

**==> picture [10 x 8] intentionally omitted <==**

From the front projection we see that our Legendrian _P_ ( _−_ 2 _m −_ 5 _, −_ 3 _,_ 3) has Thurston-Bennequin number _−_ 1 and rotation number 0. In [CNS16] (c.f. [EN20, Appendix A]), Cornwell-NgSivek gave a Legendrian realization of _P_ ( _−n, −_ 3 _,_ 3), for each _n ≥_ 4, whose Chekanov-Eliashberg DGA is stable tame isomorphic to that of the unknot. In particular, Cornwell-Ng-Sivek produce a Legendrian _P_ ( _−_ 2 _m −_ 5 _, −_ 3 _,_ 3) with the same classical invariants as ours, and with ruling polynomial 1. We conclude, via Rutherford’s result cited above, that each of our Legendrian pretzel knots has a unique ruling, and thus that we have infinitely many impostors. 

## REFERENCES 

- [ABD[+] 24] Taylor Applebaum, Sam Blackwell, Alex Davies, Thomas Edlich, András Juhász, Marc Lackenby, Nenad Tomašev, and Daniel Zheng, _The unknotting number, hard unknot diagrams, and reinforcement learning_ , 2024, arXiv:2409.09032. 

- [Ada94] C.C. Adams, _The Knot Book: An Elementary Introduction to the Mathematical Theory of Knots_ , W.H. Freeman and Company, 1994. 

- [BCL[+] 24] Benjamin A. Burton, Hsien-Chih Chang, Maarten Löffler, Arnaud de Mesmay Clément Maria, Saul Schleimer, Eric Sedgwick, and Jonathan Spreer, _Hard diagrams of the unknot_ , Exp. Math. **33** (2024), no. 3, 482–500. 

- [Ben83] Daniel Bennequin, _Entrelacements et equations de Pfaff_ , Astérisque **107** (1983), 87–161. 

- [BM92] Joan S. Birman and William W. Menasco, _Studying links via closed braids. V. The unlink_ , Trans. Amer. Math. Soc. **329** (1992), 585–606. 

- [Bre24] Joseph Breen, _Regularly slice implies once-stably decomposably slice_ , 2024, arXiv:2410.21031. 

- [BST15] Frédéric Bourgeois, Joshua M Sabloff, and Lisa Traynor, _Lagrangian cobordisms via generating families: Construction and geography_ , Alg. Geom. Topol. **15** (2015), no. 4, 2439–2477. 

- [CEK24] Roger Casals, John B. Etnyre, and Mark Kegel, _Stein traces and characterizing slopes_ , Math. Ann. **389** (2024), 1053–1098. 

- [CET21] James Conway, John B. Etnyre, and Bülent Tosun, _Symplectic fillings, contact surgeries, and Lagrangian disks_ , Int. Math. Res. Not. **2021** (2021), no. 8, 6020–6050. 

- [CG22] Roger Casals and Honghao Gao, _Infinitely many Lagrangian fillings_ , Ann. of Math. **195** (2022), no. 1, 207–249. 

- [Cha10] Baptiste Chantraine, _Lagrangian concordance of Legendrian knots_ , Algebr. Geom. Topol. **10** (2010), no. 1, 63– 85. 

- [Che02] Yuri Chekanov, _Differential algebra of Legendrian links_ , Invent. Math. **150** (2002), no. 3, 441–483. 

HARD LEGENDRIAN UNKNOTS 

31 

|[CN13]<br>[CNS16]<br>[CP07]<br>[DG01]<br>[Dyn06]<br>[EGL18]<br>[EH01]<br>[EHK12]<br>[Eli87]<br>[Eli92]<br>[EN20]<br>[Etn05]<br>[FI04]<br>[Fuc03]<br>[G+11]<br>[Goe34]<br>[Gom98]<br>[HK14]<br>[HL01]<br>[HN10]<br>[KL11]<br>[Lac15]<br>[LdMS24] <br>[Lev14]<br>[Moh01]<br>[PZ16]<br>[Rut06]<br>[Sab05]<br>[Ste09]|Wutichai Chongchitmate and Lenhard Ng,_An atlas of Legendrian knots_, Exp. Math.**22**(2013), no. 1, 26–37.<br>Christopher Cornwell, Lenhard Ng, and Steven Sivek, _Obstructions to Lagrangian concordance_, Algebr.<br>Geom. Topol.**16**(2016), no. 2, 797–824.<br>Yu Chekanov and P.E. Pushkar,_Combinatorics of fronts of Legendrian links and the Arnol’d 4-conjectures_, Rus-<br>sian Math. Surveys**60**(2007), 95–149.<br>Fan Ding and Hansjorg Geiges,_Symplectic fllability of tight contact structures on torus bundles_, Algebr. Geom.<br>Topol.**1**(2001), no. 1, 153–172.<br>I. A. Dynnikov,_Arc-presentations of links: Monotonic simplifcation_, Fund. Math.**190**(2006), no. 1, 29–76 (eng).<br>Yakov Eliashberg, Sheel Ganatra, and Oleg Lazarev, _Flexible Lagrangians_, International Mathematics Re-<br>search Notices**2020**(2018), no. 8, 2408–2435.<br>John B. Etnyre and Ko Honda,_Knots and Contact Geometry I: Torus Knots and the Figure Eight Knot_, J. Sym-<br>plectic Geom.**1**(2001), no. 1, 63 – 120.<br>Tobias Ekholm, Ko Honda, and Tamás Kálmán, _Legendrian knots and exact Lagrangian cobordisms_, J. Eur.<br>Math. Soc. (JEMS)**18**(2012), 2627–2689.<br>Yakov Eliashberg, _A theorem on the structure of wave fronts and its application in symplectic topology_, Funct.<br>Anal. Its. Appl.**21**(1987), 227–232.<br>, _Contact 3-manifolds twenty years since J. Martinet’s work_, Ann. Inst. Fourier (Grenoble) **42** (1992),<br>no. 1-2, 165–192.<br>John B. Etnyre and Lenhard Ng,_Legendrian contact homology in_R3, Surv. Differ. Geom.**25**(2020), 103–161.<br>John B. Etnyre,_Legendrian and transversal knots_, Handbook of Knot Theory (William Menasco and Morwen<br>Thistlewaite, eds.), Elsevier B.V., 2005, pp. 105–186.<br>Dmitry Fuchs and Tigran Ishkhanov, _Invariants of Legendrian knots and decompositions of front diagrams_,<br>Mosc. Math. J.**4**(2004), no. 3, 707–717.<br>Dmitry Fuchs, _Chekanov–Eliashberg invariant of Legendrian knots: existence of augmentations_, J. Geom. Phys.<br>**47**(2003), no. 1, 43–65.<br>Timothy Gowers et al.,_Are there any very hard unknots?_, MathOverfow, 2011.<br>Lebrecht Goeritz,_Bemerkungen zur knotentheorie_, Abh. Math. Sem. Univ. Hamburg**10**(1934), no. 1, 201–210.<br>Robert E Gompf,_Handlebody construction of Stein surfaces_, Ann. of Math. (1998), 619–693.<br>Allison Henrich and Louis H. Kauffman,_Unknotting unknots_, Amer. Math. Monthly**121**(2014), no. 5, 379–<br>390.<br>Joel Hass and Jeffrey C. Lagarias,_The number of Reidemeister moves needed for unknotting_, J. Amer. Math. Soc.<br>**14**(2001), no. 2, 399–428.<br>Joel Hass and Tahl Nowik, _Unknot diagrams requiring a quadratic number of Reidemeister moves to untangle_,<br>Discrete Comput. Geom.**44**(2010), no. 1, 91–95. MR 2639820<br>Louis H. Kauffman and Sofa Lambropoulou,_Hard unknots and collapsing tangles_, pp. 187–247, World Sci-<br>entifc Publishing, 2011.<br>Marc Lackenby,_A polynomial upper bound on Reidemeister moves_, Ann. of Math.**182**(2015), no. 2, 491–564.<br> Corentin Lunel,<br>Arnaud de Mesmay,<br>and Jonathan Spreer,<br>_Hard diagrams of split links_,<br>2024,<br>arXiv:2412.03372.<br>Caitlin Leverson,_Augmentations and rulings of Legendrian links_, J. Symplectic Geom.**14**(2014), 1089–1143.<br>Klaus Mohnke, _Legendrian links of topological unknots_, Topology, geometry, and algebra: interactions and<br>new directions (Stanford, CA, 1999), Contemp. Math., vol. 279, Amer. Math. Soc., Providence, RI, 2001,<br>pp. 209–211. MR 1850749<br>Carlo Petronio and Adolfo Zanellati,_Algorithmic simplifcation of knot diagrams: new moves and experiments_,<br>J. Knot Theory Ramifcations**25**(2016), no. 10, 1650059, 30. MR 3548477<br>Dan Rutherford,_The Thurston-Bennequin number, Kauffman polynomial, and ruling invariants of a Legendrian_<br>_link: The Fuchs conjecture and beyond_, Int. Math. Res. Not. IMRN**2006**(2006), no. 9, Art. ID 78591, 15.<br>Joshua M. Sabloff, _Augmentations and rulings of Legendrian knots_, Int. Math. Res. Not. IMRN **2005** (2005),<br>no. 19, 1157–1180.<br>Ian Stewart,_Professor Stewart’s Cabinet of Mathematical Curiosities_, Basic Books, 2009.|
|---|---|



JOSEPH BREEN, AUSTIN CHRISTIAN, AND ANGELA WU 

32 

UNIVERSITY OF ALABAMA, TUSCALOOSA, AL 35401 _Email address_ : jjbreen@ua.edu _URL_ : https://sites.google.com/view/joseph-breen 

CALIFORNIA POLYTECHNIC STATE UNIVERSITY, SAN LUIS OBISPO, CA 93407 _Email address_ : achris66@calpoly.edu _URL_ : https://sites.google.com/view/austin-christian 

BUCKNELL UNIVERSITY, LEWISBURG, PA 17837 _Email address_ : ajw031@bucknell.edu _URL_ : https://angelamath.com/ 

