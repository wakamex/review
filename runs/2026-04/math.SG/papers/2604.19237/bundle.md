# Review Bundle: 2604.19237

## Metadata

```json
{
  "abs_url": "https://arxiv.org/abs/2604.19237",
  "arxiv_id": "2604.19237",
  "bundle_sha256": "8a53bca0cb0f8ba8d13bd2bc9287448fc4c0583f50156707131400a8e88aa73f",
  "bundle_text_chars": 23432,
  "categories": [
    "math.SG",
    "math.DS"
  ],
  "comments": "10 pages, 3 figures",
  "month": "2026-04",
  "page_count": 10,
  "pdf_url": "https://arxiv.org/pdf/2604.19237",
  "raw_source_sha256": "ec411bf0a4c572aae4df474275ab1cca2c52a35bb919ac264cb7bff784ca4ef2",
  "source_path": "runs/2026-04/math.SG/assets/2604.19237/paper.html",
  "source_text_chars": 23432,
  "source_type": "arxiv_html",
  "source_url": "https://arxiv.org/html/2604.19237v1",
  "subjects": [
    "Symplectic Geometry (math.SG)",
    "Dynamical Systems (math.DS)"
  ],
  "title": "Bott-integrable contact forms with large systolic ratio",
  "topic": "math.SG",
  "truncated": false
}
```

## Source Text
Bott-integrable contact forms with large systolic ratio

Report GitHub Issue

×

Title:

Content selection saved. Describe the issue below:

Description:

Submit without GitHub
Submit in GitHub

Back to arXiv

Why HTML?

Report Issue

Back to Abstract

Download PDF

Abstract.

1 Introduction

2 The systolic geometry of Lutz forms

3 Linearising the contact form

4 Integrability of the ABHS plug

5 Proof of Theorem  1

References

License: arXiv.org perpetual non-exclusive license

arXiv:2604.19237v1 [math.SG] 21 Apr 2026

Bott-integrable
contact forms with large systolic ratio

Hansjörg Geiges

Mathematisches Institut, Universität zu Köln,
Weyertal 86–90, 50931 Köln, Germany

geiges@math.uni-koeln.de

,
Jakob Hedicke

Afdeling Wiskunde, Radboud Universiteit, Heyendaalseweg 135,
6525AJ Nijmegen, Netherlands

jakob.hedicke@gmail.com

and
Murat Sağlam

Mathematisches Institut, Universität zu Köln,
Weyertal 86–90, 50931 Köln, Germany

msaglam@math.uni-koeln.de

Abstract.

We show that there is no universal upper bound for the systolic
ratio of Bott-integrable contact forms on closed -manifolds,
thus providing further evidence for the relative flexibility
of integrable contact forms. For the proof, we study piecewise
linear approximations of Lutz forms and establish integrability
of a ‘plug’ constructed by Abbondandolo, Bramham, Hryniewicz
and Salomão for pushing up the systolic ratio.

Key words and phrases:
Reeb dynamics, Bott integrability, systolic ratio, contact structure

2020 Mathematics Subject Classification:
37J35, 37J55, 53C23, 53D35

1. Introduction

The systole of a closed Riemannian or Finsler manifold is the
length of the shortest non-contractible
closed geodesic. The systolic ratio
is the scale-invariant dimensionless quotient
between the power of the systole and the volume of the
-dimensional manifold. The systolic ratio has a long history,
especially in the Riemannian geometry of surfaces, and under
a variety of assumptions upper bounds are known; see [ 4 ]
for an overview, also with a view towards Finsler geometry.

The (co-)geodesic flow can be interpreted as the Reeb flow of the
Liouville contact form on the unit cotangent bundle;
see [ 8 ] for the Riemannian and [ 7 ] for the
Finsler case. Based on this fact, in [ 5 ] it was first
observed that contact geometry is a natural setting to study
questions in systolic geometry; see also [ 3 , 4 ] .

Given a closed manifold of dimension admitting a contact
form  , we denote by the Reeb vector field of  ,
and by the volume of with respect to the
volume form . If there are
any periodic Reeb orbits—which is always the case in dimension
three  [ 17 ] and conjecturally in all (odd) dimensions—the
infimum over the periods of all closed Reeb orbits is finite,
and actually a minimum by an argument as in [ 11 , p. 109] .
We denote this (positive) minimum by . The scale-invariant
systolic ratio is then defined as

| |
| |
| |

In general, there is no upper bound on this systolic ratio, that is,
given a contact manifold , one can find contact forms
, defining , with arbitrarily large
systolic ratio; see  [ 3 , 4 , 15 , 16 ] .
However, for many classes of Reeb flows in dimension three—to
which we now restrict our attention—the imposition
of additional symmetries leads to such bounds. Examples
are Reeb flows of contact forms that are
-close to a Zoll contact form  [ 1 , 2 ] ,
or Reeb flows of -invariant contact forms
on Seifert bundles with non-vanishing Euler number  [ 18 , 19 ] .

A symmetry assumption weaker than -invariance, but still believed to
be quite strong, is Bott integrability of the contact form
as defined in  [ 9 ] .
The main result of the present paper says that there is no universal
systolic inequality on the class of Bott-integrable contact forms
on any given closed contact -manifold. This shows that integrable
contact forms abound within the class of contact forms defining
a given integrable contact structure, and it provides further evidence that
the integrability requirement may be less restrictive than
expected. This theorem complements
the results about overtwisted Bott-integrable contact
structures in [ 10 ] , which can be read as
statements about the abundance of integrable contact structures
within the space of all contact structures.

Recall from [ 9 , 10 ] that a contact form on a
compact -manifold is called Bott integrable
if there is a Morse–Bott function invariant
under the Reeb flow of  . A contact structure on
said to be Bott integrable if there is some Bott-integrable
contact form with .

Theorem 1 .

Let be a Bott-integrable contact structure on
a closed -manifold  . Then for every there
exists a Bott-integrable contact form defining
with systolic ratio .

The strategy for the proof of this theorem is as
follows. As shown in [ 9 ] , Bott-integrable contact forms have a
simple description as so-called Lutz forms away from the singular level
sets of the Morse–Bott function. In Sections 2
and 3 we show that outside a set of
small volume these Lutz forms can be replaced by linear
Lutz forms, while keeping control over  . Into these
linear pieces we then insert plugs as constructed by
Abbondandolo, Bramham, Hryniewicz and Salomão in
[ 3 , 4 ] . These plugs are solid tori with a contact
form of small volume, standard near the boundary, and with
. By filling all but a small volume part of
the linear Lutz pieces with such plugs, the total volume can be made
arbitrarily small, whereas stays bounded from below.
In order to apply this construction in the Bott-integrable setting,
we need to construct an invariant Morse–Bott function
on the plug; this will be done in Section  4 .
The estimates on volume and that establish Theorem  1
are given in Section  5 .

A long-standing open question of Katok [ 12 ] asks whether every
low-dimensional volume-preserving dynamical system with zero entropy
can be approximated by integrable systems.
A version of that question on surfaces was studied in
[ 6 ] and [ 13 ] , where the authors show that there is a
gap between autonomous Hamiltonian diffeomorphisms and integrable
Hamiltonian diffeomorphisms in the -topology
and the Hofer metric, respectively.
Theorem 1 , taken together with the results of
Abbondandolo, Benedetti and Edtmair [ 1 , 2 ] on Zoll
contact forms, implies
that there exist integrable contact forms
that are far from Zoll contact forms in the -topology.
It would be interesting to understand whether there are
integrable contact forms far from -invariant ones.
The same question can be asked with the -topology replaced by
the Banach–Mazur pseudometric on contact forms
introduced in  [ 2 ] , which may be regarded as an
analogue of the Hofer metric on Hamiltonian diffeomorphisms.

2. The systolic geometry of Lutz forms

A Lutz form is a contact form on
that can be written as

| |
| |
| |

where is the coordinate on , and are those on
. With the orientation of defined by the
volume form , the contact condition
becomes

| |
| |
| |

since
and .

By the Reeb–Liouville theorem [ 9 , Theorem 2.2] ,
every connected component of a regular level set of a Bott integral
is a torus, and the Bott-integrable contact form is a Lutz form in a
neighbourhood of this torus.

The Reeb vector field of a Lutz form is given by

| (1) |
| |
| |
| |

Moreover, we have

| |
| |
| |

From these formulae it follows immediately that both
(and hence ) and are invariant under
reparametrisations . Indeed, with
, , the map induces
a strict contactomorphism between the Lutz forms
and
on and , respectively.

Although we shall not rely on the following estimates in the present paper,
we record them for future reference. Write for the
minimal period of on , in the case that
. When this ratio is
irrational, we set .
In the rational case, we have

| |
| |
| |
| |
| |

| |
| |
| |
| |
| |

When both and are non-zero, a better estimate is
given by in the last line, but the estimate with
also holds for one of the two being zero. For
, say, we have , and the
minimal period is .

The condition means that the velocity vector
of the plane curve always points to
the right of the position vector . Thus,
we may regard

| |
| |
| |

as a function of taking values in the interval . Then

| |
| |
| |

It follows that

| |
| |
| |

and

| |
| |
| |

3. Linearising the contact form

Let be a Bott-integrable contact form on a closed
-manifold  , with Bott integral .
The aim of this section is to show that one can homotope
to a linear Lutz form

| |
| |
| |

, , with Reeb vector field ,
on a collection of product neighbourhoods whose complement is
a set of arbitrarily small volume with respect to
the new contact form.

Proposition 2 .

Given , for every one can find a
Bott-integrable contact form with
the following properties:

(i)

is homotopic to via Bott-integrable contact
forms, all sharing the Bott integral  .

(ii)

and .

(iii)

There is an open subset with
such that is
the disjoint union of finitely many subsets
diffeomorphic to , with

| |
| |
| |

and with .
Here is the minimal period
of the Reeb flow on  , and is determined by
the identity .

Proof.

The Morse–Bott function on the closed manifold
has finitely many singular levels . For
sufficiently small, the union

| |
| |
| |

of neighbourhoods of the singular level sets will
satisfy .

By the Reeb–Liouville theorem [ 9 , Theorem 2.2] ,
the complement is foliated by tori, each of
which has a neighbourhood diffeomorphic to ,
where with , and
.
Thanks to being compact, we can choose finitely
many of these neighbourhoods whose interiors cover the complement of  .
Moreover, it may be assumed that there are no triple intersections
between these Lutz pieces or with  , and that the total volume of the
pairwise intersections is smaller than  .

Next we modify the contact form on each of the finitely
many product neighbourhoods as follows.
In a small neighbourhood of , containing the
intersection with or with another Lutz piece, we leave the plane curve
unchanged. Outside these neighbourhoods,
which we may assume to have total volume smaller than  ,
we choose a -close approximation by a piecewise linear
curve with vertices on the curve
and rational (or infinite) slope of the linear
pieces; the linear pieces need not be
parametrised linearly. The convex linear interpolation between
and defines a homotopy via contact forms
sharing the same Bott integral.

Finally, we smoothen the curve in small neighbourhoods of
the vertices of total volume (with respect to the
volume form defined by the contact form
corresponding to the new curves on all
the Lutz pieces) smaller than  .
The last comment about convex linear interpolation still applies, so
condition (i) in the proposition is satisfied by the resulting
contact form  .

With we denote
the collection of linear pieces, and with their complement, made up
of , the smoothing regions, and the regions near the
boundary of the original Lutz pieces where we have left
the contact form unchanged. By construction, we have
.

For a sufficiently -close approximation of the
curves describing the Lutz pieces,
the volume conditions in (ii) and (iii) will be satisfied by
the formula for from Section  2 .

The finitely many Lutz pieces making up the complement of
are now of the form

| |
| |
| |

with . By a linear
change of coordinates in , using an element of ,
and a reparametrisation of the -coordinate, we can bring the Lutz
pieces into the form described in (iii). The characterisations of
in terms of minimal period and volume are
clear from the formulae in Section  2 .

It remains to show that is bounded from below by
for a sufficiently -close
approximation  .
To this end, we need to relate the periodic orbits of and
on a Lutz piece , where
and
. By formula
( 1 ) from Section  2 for the
Reeb vector field on a Lutz piece, the flow of is
periodic on precisely when the slope
is rational or infinite. In particular,
this is the case on the linear pieces of  .

By the choice of vertices of the piecewise linear approximation
on the curve , and by the mean value theorem,
the slope of a linear piece
—before the
smoothing of  —is realised by
at some point ;
see Figure  1 . Then

| |
| |
| |

on for ,
else we replace the second factor by the quotient
.
The approximation being -close implies that
and (and hence the corresponding
minimal periods) differ by a factor close to  .

In the smoothing regions of , the slope
varies between two rational slopes and
of linear segments. By the intermediate value theorem, any rational
slope of between and in this region
equals for some
;
again, see Figure  1 .
As before, the Reeb flows of and differ by
a reparametrisation factor close to  , provided we choose
the linear segments in sufficiently short. This proves the
estimate for in (ii) and hence the proposition.
∎

\labellist

\hair

2pt
\pinlabel [t] at 9 335
\pinlabel [tr] at 171 286
\pinlabel slope [l] at 327 268
\pinlabel slope [r] at 278 196
\pinlabel slope [l] at 376 157
\endlabellist \includegraphics [scale=0.5]PL-Lutz

Figure 1. The smoothened piecewise linear Lutz form.

4. Integrability of the ABHS plug

The following proposition, due to Abbondandolo, Bramham, Hryniewicz and
Salomão (ABHS), lists the essential properties of their plug;
see [ 4 , Proposition 3.1] . The details of the
construction are contained in [ 3 , Proposition 2.27]
and [ 3 , Proposition 3.1] . We write for the Cartesian
coordinates and for the
radial coordinate on the closed unit disc  , and for the
angular coordinate on the circle .

Proposition 3 (ABHS) .

Let and a primitive of the standard area
form on be given. Then there is
a contact form on
the solid torus
with the following properties:

(i)

near the boundary of the solid torus;
in particular, the Reeb vector
field equals near the boundary.

(ii)

is isotopic relative to a neighbourhood of the boundary
and via contact forms to .

(iii)

The minimal period of the Reeb vector field is at least  .

(iv)

The volume is smaller than  .

We want to prove the following addendum to this proposition.

Addendum 4 .

The contact form in the preceding proposition admits a Bott integral
whose level sets near the boundary of the solid torus
are regular tori , that is,
and for close to  .

The key to Proposition  3 is the construction
of an area-preserving diffeomorphism of , equal to
the identity near
the boundary, with control over the compactly supported
primitive of the closed -form ,
the periodic points and
the Calabi invariant; see  [ 4 , Proposition 3.2] .
Choose a positive
primitive of ,
constant near the boundary. Then the contact form
on with Reeb vector field is
invariant under the diffeomorphism

| |
| |
| |

and hence descends to a contact form on
.

In order to prove Addendum  4 , we simply need to exhibit
a Morse function (or the corresponding
level sets) invariant under  , and with regular levels
in a neighbourhood of the boundary of the disc.
This Morse function then gives rise to a Bott integral, first on the
mapping torus ,
and then on its diffeomorphic copy ,
with the properties claimed in the addendum.

We now describe the relevant properties of  ; details
of the construction are given in [ 3 , pp. 734–736] .
For ease of notation, we assume ; the general case follows
by an appropriate rescaling as discussed after [ 4 , Proposition 3.2] .
The area-preserving diffeomorphism is a composition
of two Hamiltonian diffeomorphisms.

The construction of depends on a parameter  ;
when chosen sufficiently large, this yields the required estimates in
Proposition  3 . The properties of the diffeomorphism
of are:

(i)

Each circle is rotated in positive
direction through an angle at most .

(ii)

On a sufficiently large disc , the rotation angle
equals .

(iii)

Near the boundary of  , the map is the identity.

Next one chooses a finite collection of pairwise disjoint closed discs
, , in the sector

| |
| |
| |

with the total area of the close to .
For each one defines a Hamiltonian diffeomorphism  ,
compactly supported in the interior of  and acting
on analogously to the action of on  , but
rotating in negative direction. Then
extend this diffeomorphism of to a diffeomorphism
of equivariant with respect to the
-action generated by the rigid rotation of
through an angle . We may think of the
disc as being obtained by gluing the radial boundaries
of the sector ,
so we regard the as discs in .

The relevant properties of the Morse function are
encoded in the Morse foliation of level sets of  , which we now describe.
Away from a small disc around the centre
disjoint from the ,
the branched covering restricts to
a covering of annuli. Join the ‘beads’ in
into a necklace as shown in Figure  2 .
This gives rise to a Morse foliation with a critical point of
Morse index  at the centre of each  , and a critical point of
index  on each connecting piece of the necklace. The corresponding
Morse function on extends to a Morse function
on the disc , radially symmetric near
the centre, and with an index  critical point at the centre.
This function lifts to the desired Morse function on  .

\labellist

\hair

2pt
\pinlabel [l] at 513 151
\pinlabel [l] at 508 289
\pinlabel [r] at 0 151
\endlabellist \includegraphics [scale=0.52]morse-foliationD

Figure 2. The Morse foliation on the annulus .

5. Proof of Theorem  1

Starting from a Bott-integrable contact form on  ,
let be the contact form constructed in
Proposition  2 .
We consider a linear Lutz piece with

| |
| |
| |

, and
. We consider the annulus

| |
| |
| |

with area form . Given
(and smaller than  ), by a simple application of
Moser’s method  [ 14 ] we can choose an area-preserving
embedding

| |
| |
| |

with

| |
| |
| |

This extends to an embedding

| |
| |
| |

satisfying

| |
| |
| |

with
a primitive of .

Let
be the contact form on
provided by Proposition  3 . Notice that because of
the factor in front of , the minimal period
of the Reeb vector field will be bounded below by  rather
than  .

Now we replace the contact form on the
image of by .
The image under of the Morse–Bott foliation
on constructed in the preceding section,
near the image of the boundary , is the
product of a Morse foliation by circles in with
the -factor corresponding to the -coordinate.
So the Morse foliation on shown in
Figure  3 , with one additional critical point
of index  , defines an extension
to a Morse–Bott foliation on  for the new contact
form on  .
The Morse function can be chosen in such a way that the new Morse–Bott
function on coincides with the original
near .

\labellist

\hair

2pt
\pinlabel at 250 205
\pinlabel [l] at 509 3
\pinlabel [l] at 509 362
\endlabellist \includegraphics [scale=0.45]morse-foliationA

Figure 3. The Morse foliation on the annulus
.

By construction, we have

| |
| |
| |

and hence

| |
| |
| |

For the volume, we estimate

| |
| |
| |
| |
| |

| |
| |
| |
| |
| |

Here the summand corresponds to the volume of
the image of after the modification of
into
and comes from part (iv) of Proposition  3 ;
the summand is the volume of the complement
of this image, where is left unmodified.

The number of summands (i.e., the range of  ) and
the depend on the chosen .
By then choosing sufficiently small, we can ensure that
. With
we then have the estimate

| |
| |
| |

Since can be chosen as small as we like,
Theorem  1 is proved.

Acknowledgements .

J. H. is supported by the Radboud Excellence Initiative.
M. S. is supported by the Deutsche Forschungsgemeinschaft on the project
“Reeb flows with symmetries: dynamics and topology”
(SA 5534/1-1, Projektnummer 568330991).

References

[1]

A. Abbondandolo and G. Benedetti ,
On the local systolic optimality of Zoll contact forms,
Geom. Funct. Anal.
33 (2023), 299–363.

[2]

A. Abbondandolo, G. Benedetti and O. Edtmair ,
Symplectic capacities of domains close to the ball and Banach–Mazur
geodesics in the space of contact forms,
Duke Math. J.
174 (2025), 1567–1646.

[3]

A. Abbondandolo, B. Bramham, U. L. Hryniewicz and
P. A. S. Salomão ,
Sharp systolic inequalities for Reeb flows on the three-sphere,
Invent. Math.
211 (2018), 687–778.

[4]

A. Abbondandolo, B. Bramham, U. L. Hryniewicz and
P. A. S. Salomão ,
Contact forms with large systolic ratio in dimension three,
Ann. Sc. Norm. Super. Pisa Cl. Sci. (5)
19 (2019), 1561–1582.

[5]

J. C. Álvarez Paiva and F. Blacheff ,
Contact geometry and isosystolic inequalities,
Geom. Funct. Anal.
24 (2014), 648–669.

[6]

M. Brandenbursky and M. Khanevsky ,
-gap between entropy-zero Hamiltonians and autonomous diffeomorphisms
of surfaces,
Israel J. Math.
255 (2023), 311–324.

[7]

M. Dörner, H. Geiges and K. Zehmisch ,
Finsler geodesics, periodic Reeb orbits, and open books,
Eur. J. Math.
3 (2017), 1058–1075.

[8]

H. Geiges ,
Geometry on Manifolds – Riemannian Metrics, Symplectic Forms,
Contact Structures ,
Compact Textbooks in Mathematics, Birkhäuser Verlag, Basel (2026).

[9]

H. Geiges, J. Hedicke and M. Sağlam ,
Bott-integrable Reeb flows on -manifolds,
J. Lond. Math. Soc. (2)
109 (2024), Paper No. e12859, 42 pp.

[10]

H. Geiges, J. Hedicke and M. Sağlam ,
Bott-integrability of overtwisted contact structures,
Rev. Mat. Iberoam. , to appear.

[11]

H. Hofer and E. Zehnder ,
Symplectic Invariants and Hamiltonian Dynamics ,
Basler Lehrbücher,
Birkhäuser Verlag, Basel (1994).

[12]

A. Katok ,
Open problems in elliptic dynamics,
transcript of a talk at the Penn State seminar
Dynamics and its working tools ,
notes by V. Climenhaga,
September 1 (2009).

[13]

M. Khanevsky ,
A gap in the Hofer metric between integrable and autonomous Hamiltonian
diffeomorphisms on surfaces,
arXiv:2205.03492 .

[14]

J. Moser ,
On the volume elements on a manifold,
Trans. Amer. Math. Soc.
120 (1965), 286–294.

[15]

M. Sağlam ,
Contact forms with large systolic ratio in arbitrary dimensions,
Ann. Sc. Norm. Super. Pisa Cl. Sci. (5)
22 (2021), 1265–1308.

[16]

M. Sağlam ,
Reeb flows with small contact volume and large return time
to a global section,
J. Topol. Anal.
16 (2024), 541–560.

[17]

C. H. Taubes ,
The Seiberg–Witten equations and the Weinstein conjecture,
Geom. Topol.
11 (2007), 2117–2202.

[18]

S. Vialaret ,
Sharp systolic inequalities for invariant tight contact forms on
principal -bundles over  ,
Ann. H. Lebesgue
8 (2025), 995–1021.

[19]

S. Vialaret ,
Systolic inequalities for -invariant contact forms in dimension three,
Trans. Amer. Math. Soc. , to appear.

Experimental support, please
view the build logs
for errors. Generated by

L
A
T
E

xml

.

Instructions for reporting errors

We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile
support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the
methods listed below:

Click the "Report Issue" ( ) button, located in the page header.

Tip: You can select the relevant text first, to include it in your report.

Our team has already identified the following issues . We appreciate your time reviewing and reporting rendering errors we
may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability
should not be a barrier to accessing research. Thank you for your continued support in championing open access for
all.

Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a list of packages that need conversion , and welcome developer contributions .

BETA
