You are one reviewer on an LLM review board for a mathematics paper.

This is a follow-up review cycle. You can revise your prior judgment after
reading the other reviewers. Do not defer to them automatically. Your job is to
audit their objections, keep the real ones, reject weak/hallucinated ones, and
surface anything everyone missed.

Review posture:
- Do not claim to certify the whole proof.
- Be concrete and location-grounded.
- Say when a disagreement requires human mathematical spot-checking.
- Return only JSON matching the provided schema.

Paper id: 2604.19237
Reviewer id: codex
Cycle: 2

Schema:
```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "paper_id",
    "reviewer",
    "cycle",
    "summary",
    "main_claims",
    "technical_objections",
    "missing_assumptions",
    "novelty_assessment",
    "recommended_verdict",
    "confidence",
    "followup_notes",
    "needs_human_spotcheck"
  ],
  "properties": {
    "paper_id": { "type": "string" },
    "reviewer": { "type": "string" },
    "cycle": { "type": "integer", "minimum": 1 },
    "summary": { "type": "string" },
    "main_claims": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["claim", "paper_location", "support_level", "notes"],
        "properties": {
          "claim": { "type": "string" },
          "paper_location": { "type": "string" },
          "support_level": {
            "type": "string",
            "enum": ["well_supported", "partially_supported", "unsupported", "unclear"]
          },
          "notes": { "type": "string" }
        }
      }
    },
    "technical_objections": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "objection",
          "paper_location",
          "evidence",
          "severity",
          "confidence",
          "would_change_verdict_if_true"
        ],
        "properties": {
          "objection": { "type": "string" },
          "paper_location": { "type": "string" },
          "evidence": { "type": "string" },
          "severity": {
            "type": "string",
            "enum": ["minor", "moderate", "major", "fatal"]
          },
          "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
          "would_change_verdict_if_true": { "type": "boolean" }
        }
      }
    },
    "missing_assumptions": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["assumption", "paper_location", "why_it_matters"],
        "properties": {
          "assumption": { "type": "string" },
          "paper_location": { "type": "string" },
          "why_it_matters": { "type": "string" }
        }
      }
    },
    "novelty_assessment": { "type": "string" },
    "recommended_verdict": {
      "type": "string",
      "enum": [
        "strong_select",
        "promising",
        "routine",
        "weak_evidence",
        "major_flaw",
        "contested"
      ]
    },
    "confidence": { "type": "number", "minimum": 0, "maximum": 1 },
    "followup_notes": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "changed_mind",
        "changes_from_prior_cycle",
        "valid_points_from_other_reviewers",
        "invalid_points_from_other_reviewers"
      ],
      "properties": {
        "changed_mind": { "type": "boolean" },
        "changes_from_prior_cycle": { "type": "string" },
        "valid_points_from_other_reviewers": {
          "type": "array",
          "items": { "type": "string" }
        },
        "invalid_points_from_other_reviewers": {
          "type": "array",
          "items": { "type": "string" }
        }
      }
    },
    "needs_human_spotcheck": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["question", "why_model_cannot_resolve"],
        "properties": {
          "question": { "type": "string" },
          "why_model_cannot_resolve": { "type": "string" }
        }
      }
    }
  }
}

```

Paper bundle:
```markdown
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

```

Your prior review:
```json
{
  "confidence": 0.63,
  "cycle": 1,
  "followup_notes": {
    "changed_mind": false,
    "changes_from_prior_cycle": "N/A for cycle 1.",
    "invalid_points_from_other_reviewers": [],
    "valid_points_from_other_reviewers": []
  },
  "main_claims": [
    {
      "claim": "For every Bott-integrable contact structure on a closed 3-manifold, Bott-integrable defining contact forms can have arbitrarily large systolic ratio.",
      "notes": "The strategy is coherent, but the final plug insertion has a boundary-scaling mismatch and relies on a sketched integrability addendum.",
      "paper_location": "Theorem 1, p.2 lines 63-66; proof in Section 5, p.7-p.8 lines 591-667",
      "support_level": "partially_supported"
    },
    {
      "claim": "A Bott-integrable contact form can be homotoped, preserving the Bott integral, so that outside arbitrarily small volume it is a finite union of linear Lutz pieces while Tmin is nearly preserved.",
      "notes": "The local Lutz computations support this, but the global chart patching and the uniform Tmin control through smoothing regions are compressed.",
      "paper_location": "Proposition 2 and proof, p.3-p.5 lines 300-504",
      "support_level": "partially_supported"
    },
    {
      "claim": "The ABHS plug admits a Bott integral with regular torus levels near the boundary.",
      "notes": "The proof describes a candidate Morse foliation, but does not explicitly verify invariance under the actual ABHS return map phi = phi_+ composed with phi_-.",
      "paper_location": "Addendum 4 and proof sketch, p.5-p.7 lines 528-590",
      "support_level": "unclear"
    },
    {
      "claim": "Replacing most of each linear Lutz piece by the plug keeps Tmin bounded below and makes total volume arbitrarily small.",
      "notes": "The volume strategy is plausible, but the cited plug model does not directly match the pulled-back boundary form a_l ds + lambda_l as written.",
      "paper_location": "Section 5, p.7-p.8 lines 608-667",
      "support_level": "partially_supported"
    }
  ],
  "missing_assumptions": [
    {
      "assumption": "A scaled ABHS plug exists for the boundary contact form lambda + a ds, with minimal period at least a and arbitrarily small prescribed volume.",
      "paper_location": "Section 5, p.7 lines 616-630",
      "why_it_matters": "This is needed for smooth gluing into a linear Lutz piece and for the claimed lower bound Tmin >= a_l. It is probably obtainable by applying Proposition 3 to lambda/a and multiplying the resulting form, but the paper should state and track the volume scaling."
    },
    {
      "assumption": "The necklace foliation constructed in Section 4 is invariant under the exact ABHS disk diffeomorphism phi, not only under an idealized rotation model.",
      "paper_location": "Section 4, p.6-p.7 lines 553-590",
      "why_it_matters": "Without h composed with phi equal to h, the function h does not descend to a Bott integral on the mapping torus."
    },
    {
      "assumption": "The finite Lutz charts used in Proposition 2 can be selected so that all chart overlaps lie in regions left unchanged by the later local modifications.",
      "paper_location": "Proposition 2 proof, p.3-p.4 lines 329-368",
      "why_it_matters": "This ensures the locally modified Lutz forms patch to a single smooth global contact form."
    },
    {
      "assumption": "The C1 approximation and smoothing in Proposition 2 can be chosen uniformly enough that every new periodic beta-orbit has period greater than Tmin(M,alpha)-epsilon.",
      "paper_location": "Proposition 2 proof, p.4-p.5 lines 385-503",
      "why_it_matters": "The final large-systolic-ratio estimate depends on a global lower bound for Tmin after linearisation."
    }
  ],
  "needs_human_spotcheck": [
    {
      "question": "Does the ABHS plug proposition, as used by the authors, already include or immediately imply the scaled boundary model lambda + a ds with the advertised period and volume estimates?",
      "why_model_cannot_resolve": "The paper cites external propositions and the provided text does not include their exact normalization conventions."
    },
    {
      "question": "Is the Morse foliation in Section 4 actually invariant under the precise ABHS diffeomorphism phi_+ composed with phi_-?",
      "why_model_cannot_resolve": "The proof relies on details of the ABHS construction and a figure-based foliation description; a human should check the original construction or draw the dynamics on the quotient."
    },
    {
      "question": "Can the Proposition 2 Lutz-chart cover be chosen with overlaps only in unchanged collars in full generality?",
      "why_model_cannot_resolve": "This is a standard-looking foliation-cover issue, but the paper suppresses the construction and the HTML/PDF text does not provide enough detail to rule out edge cases."
    }
  ],
  "novelty_assessment": "The claimed novelty is plausible: the paper appears to combine the ABHS large-systolic-ratio plug with Bott-integrability by adding an invariant Morse-Bott function on the plug and fitting it into linearized Lutz regions. I did not independently audit the full prior literature. The genuinely new point seems to be Addendum 4, and that is also one of the least detailed parts of the proof as written.",
  "paper_id": "2604.19237",
  "recommended_verdict": "contested",
  "reviewer": "codex",
  "summary": "The paper proposes to make the systolic ratio arbitrarily large within any Bott-integrable contact structure on a closed 3-manifold by linearising Lutz-form regions and inserting an ABHS small-volume plug equipped with a Bott integral. I did not attempt to certify the whole proof. The main local concern is that the plug is inserted into a region whose boundary model is a_l ds + lambda_l, while the quoted ABHS proposition is stated for lambda + ds; as written the gluing and period/volume estimates do not quite match without an explicit scaling lemma. The addendum constructing an invariant Morse function for the ABHS plug is also sketched rather than verified in the places where invariance under the actual diffeomorphism is needed.",
  "technical_objections": [
    {
      "confidence": 0.86,
      "evidence": "The pullback of the linear Lutz form is a_l ds + lambda_l, but Proposition 3 gives a plug equal to lambda + ds near the boundary. The text then sets beta_l = beta_{r_l,lambda_l,delta} and replaces the form on the image of Psi_l, which would glue to lambda_l + ds, not to lambda_l + a_l ds, unless a_l=1. The subsequent claim that the factor a_l makes the minimal period at least a_l requires an unstated scaled version of the plug, e.g. applying ABHS to lambda_l/a_l and then multiplying the contact form with adjusted volume control.",
      "objection": "The plug boundary model used in the insertion does not match the boundary model supplied by Proposition 3 as stated.",
      "paper_location": "Section 5, p.7 lines 616-630; Proposition 3, p.5 lines 518-526",
      "severity": "major",
      "would_change_verdict_if_true": true
    },
    {
      "confidence": 0.67,
      "evidence": "The proof says it suffices to exhibit h with h composed with phi equal to h, then describes a necklace Morse foliation on D/Z_n and says it lifts to the desired h. It does not check, leaf by leaf, that the actual composition phi_+ composed with phi_- preserves this foliation, especially in transition regions where phi_+ has radius-dependent rotation and where the phi_j are compactly supported in the beads.",
      "objection": "The claimed invariant Morse function for the ABHS plug is not fully verified.",
      "paper_location": "Section 4, p.5-p.7 lines 547-590",
      "severity": "major",
      "would_change_verdict_if_true": true
    },
    {
      "confidence": 0.55,
      "evidence": "The proof compares beta-periodic tori to alpha-tori with the same rational slope and states that the Reeb fields differ by a factor close to 1. For a global lower bound this needs uniform handling of vertical slopes, points where one derivative is small, and rational slopes appearing during smoothing. The text indicates substitutions for zero derivatives but does not spell out a projective-slope or compactness argument ensuring the period comparison is uniform over all smoothing regions.",
      "objection": "The Tmin preservation argument in Proposition 2 needs a more uniform treatment of slopes and smoothing regions.",
      "paper_location": "Proposition 2 proof, p.4-p.5 lines 385-503",
      "severity": "moderate",
      "would_change_verdict_if_true": false
    },
    {
      "confidence": 0.45,
      "evidence": "The proof chooses finitely many Lutz neighborhoods with no triple intersections and small pairwise-intersection volume, then modifies each chart while leaving boundary collars unchanged. It should justify that the overlaps can indeed be confined to such collars in the relevant r-coordinates and that the independently chosen piecewise-linear replacements agree smoothly on the resulting global complement.",
      "objection": "The construction of a global modified form from overlapping Lutz charts is underexplained.",
      "paper_location": "Proposition 2 proof, p.3-p.4 lines 329-368",
      "severity": "moderate",
      "would_change_verdict_if_true": false
    },
    {
      "confidence": 0.9,
      "evidence": "The text writes alpha_epsilon := beta_{epsilon,beta}; from context this should presumably be beta_{epsilon,delta}.",
      "objection": "There is a likely typo in the final definition of the modified contact form.",
      "paper_location": "Section 5, p.8 line 658",
      "severity": "minor",
      "would_change_verdict_if_true": false
    }
  ]
}

```

Other reviewers' latest reviews:
```json
[
  {
    "review": {
      "confidence": 0.62,
      "cycle": 1,
      "followup_notes": {
        "changed_mind": false,
        "changes_from_prior_cycle": "First cycle; no prior review.",
        "invalid_points_from_other_reviewers": [],
        "valid_points_from_other_reviewers": []
      },
      "main_claims": [
        {
          "claim": "There is no universal upper bound on the systolic ratio of Bott-integrable contact forms on any closed 3-manifold (Theorem 1).",
          "notes": "The overall proof structure is sound: drive volume to zero while keeping T_min bounded below. However, several intermediate steps (PL-approximation homotopy through contact forms, global Morse\u2013Bott extension after plug insertion) are only sketched and depend on details in [3]. Given the authors' track record and the plausibility of each step, I lean toward this being correct, but full verification requires checking [3, pp. 734-736].",
          "paper_location": "Abstract; Section 1 (Theorem 1); Section 5 (proof)",
          "support_level": "partially_supported"
        },
        {
          "claim": "A Bott-integrable contact form can be approximated (with controlled T_min and volume) by a form that is a union of linear Lutz pieces away from a set of arbitrarily small volume (Proposition 2).",
          "notes": "The main concern is the claim that the convex linear interpolation between the original Lutz plane curve and its piecewise-linear approximation defines a homotopy *through contact forms*. The contact condition for a Lutz form is a sign condition on a determinant involving f, g and their derivatives; it is not obvious that convex combinations of two valid Lutz curves remain valid Lutz curves unless the original curve is convex in the right sense (not stated). The homotopy claim is asserted without this check.",
          "paper_location": "Section 3 (Proposition 2 and proof)",
          "support_level": "partially_supported"
        },
        {
          "claim": "The ABHS plug admits a Bott integral whose level sets are regular tori near the boundary of the solid torus (Addendum 4).",
          "notes": "The construction of a \u03c6-invariant Morse function on D\u00b2 is described via its Morse foliation (Figure 2, necklace of level sets) and a branched-covering argument. The invariance under \u03c6 = \u03c6\u2081 \u2218 \u03c6\u2082 is geometrically plausible given the described rotational symmetry of the D_k arrangement. However, explicit verification of invariance (especially under \u03c6\u2082 acting on the connecting pieces of the necklace) is deferred to [3, pp. 734-736], and the indices of critical points of the resulting Morse function are not stated in the text.",
          "paper_location": "Section 4 (Addendum 4 and proof)",
          "support_level": "partially_supported"
        },
        {
          "claim": "After inserting plugs into all linear Lutz pieces, the resulting contact form on M is Bott-integrable.",
          "notes": "The paper appeals to Figure 3 (Morse foliation on the complement annulus) and says 'the Morse function can be chosen so that the new Morse\u2013Bott function coincides with the original near [the boundary].' The smooth global extension of the Morse\u2013Bott function across the plug boundaries, and the verification that the extended function is invariant under the modified Reeb flow, is not carried out explicitly.",
          "paper_location": "Section 5 (proof of Theorem 1)",
          "support_level": "partially_supported"
        },
        {
          "claim": "The systolic ratio of the resulting contact form can be made arbitrarily large.",
          "notes": "The volume estimate has two summands: the plug images (made small via Proposition 3(iv)) and the complement (made small by filling most of each linear Lutz piece with plugs). The lower bound on T_min involves both the plug period (\u2265 bN) and the period of \u03b1' in the complement of the plug images. The paper identifies T_min \u2265 (1-\u03b5)T(\u03b1) > 0, and vol \u2192 0 gives \u03c3 \u2192 \u221e. This is conceptually correct, but the formula for vol (involving a sum whose number of terms grows with N) needs careful checking to ensure the total can still be made small.",
          "paper_location": "Section 5 (volume and period estimates)",
          "support_level": "partially_supported"
        }
      ],
      "missing_assumptions": [
        {
          "assumption": "The original Lutz plane curve (f(r), g(r)) satisfies a convexity or star-shapedness condition that ensures convex combinations with its PL approximation remain valid Lutz curves.",
          "paper_location": "Section 3, proof of Proposition 2",
          "why_it_matters": "Without this, the claimed homotopy through Bott-integrable contact forms may pass through forms that are not contact, invalidating condition (i) of Proposition 2 and breaking the Bott-integrable path."
        },
        {
          "assumption": "The Morse function described on D\u00b2 (via Figure 2's necklace foliation) is genuinely invariant under the full diffeomorphism \u03c6 = \u03c6\u2081 \u2218 \u03c6\u2082, not just under the rotational component \u03c6\u2081.",
          "paper_location": "Section 4, proof of Addendum 4",
          "why_it_matters": "This invariance is required for the Morse function to descend to the mapping torus and give a well-defined Bott integral. If \u03c6\u2082 does not preserve the necklace level sets, the function on the mapping torus may not even be well-defined."
        },
        {
          "assumption": "The number of ABHS plugs needed to fill a given fraction of the linear Lutz pieces is bounded (as a function of N) in a way that permits the total plug volume to be made small.",
          "paper_location": "Section 5, volume estimate",
          "why_it_matters": "If the number of plugs grows with N without a corresponding decrease in individual plug volume, the total volume estimate may not converge to zero as required for the systolic ratio to diverge."
        }
      ],
      "needs_human_spotcheck": [
        {
          "question": "Does the convex linear interpolation between a valid Lutz plane curve and its PL approximation (with vertices on the original curve) necessarily produce a one-parameter family of curves all satisfying the Lutz contact condition f'g \u2212 fg' > 0?",
          "why_model_cannot_resolve": "This requires a pointwise sign computation on bilinear combinations of (f,g) and (f_PL, g_PL) and their derivatives. Without seeing the actual formulas for the contact condition and the class of curves used, a definitive answer is not possible. The HTML source loses mathematical formulas."
        },
        {
          "question": "Does [3, pp. 734-736] (Abbondandolo\u2013Bramham\u2013Hryniewicz\u2013Salom\u00e3o, Invent. Math. 211 (2018)) actually construct a Morse function on D\u00b2 invariant under the diffeomorphism \u03c6, or only the diffeomorphism \u03c6 itself?",
          "why_model_cannot_resolve": "The review relies on what [3] contains, which is an external reference not in the paper bundle. Addendum 4 is the key new claim, and whether its proof is self-contained or dependent on uncited material in [3] can only be determined by reading [3]."
        },
        {
          "question": "In Section 5, is the global Morse\u2013Bott function on M (after plug insertion) explicitly constructed to be smooth and Reeb-invariant, or is this left implicit via Figure 3?",
          "why_model_cannot_resolve": "Figure 3 is referenced but not viewable in the HTML source. The text is informal at this point, and verifying that the described extension is Reeb-invariant (not just topologically a Morse\u2013Bott foliation) requires seeing the figure and the supporting argument."
        },
        {
          "question": "What are the Morse indices of the critical points of the Morse function on D\u00b2 described in Section 4, and do they match the requirements for a Bott integral on the 3-dimensional mapping torus?",
          "why_model_cannot_resolve": "The index values were not rendered in the HTML conversion (they appear to be missing or garbled). Checking consistency with Bott-integrability on the 3-manifold requires the actual index values."
        }
      ],
      "novelty_assessment": "The central novelty is Addendum 4: establishing that the ABHS plug (previously known to have large systolic ratio and small volume) is also Bott-integrable. This is a non-trivial addendum because the ABHS construction was not designed with integrability in mind. The PL approximation technique in Proposition 2 is also new but is a natural and relatively straightforward tool. The conclusion \u2014 that no universal systolic bound holds for Bott-integrable forms \u2014 was open and is a meaningful contribution to the interplay between integrability and systolic geometry, complementing the positive bounds of Abbondandolo\u2013Benedetti\u2013Edtmair and Vialaret for more symmetric classes. The result is expected to be of genuine interest to the symplectic/contact topology community.",
      "paper_id": "2604.19237",
      "recommended_verdict": "promising",
      "reviewer": "claude",
      "summary": "The paper proves that there is no universal upper bound on the systolic ratio within the class of Bott-integrable contact forms on any closed 3-manifold (Theorem 1). The strategy has three steps: (1) approximate a given Bott-integrable contact form by a piecewise-linear Lutz form away from a small-volume set (Proposition 2), (2) insert ABHS plugs (solid tori with small volume and large minimal Reeb period) into the linear Lutz pieces, and (3) show the resulting contact form remains Bott-integrable by constructing a Morse\u2013Bott integral on each plug (Addendum 4). The systolic ratio then diverges because the total volume can be driven to zero while the minimal period stays bounded away from zero. The authors are established experts on Bott-integrable Reeb flows; the overall argument is coherent. The key novel contribution is Addendum 4 (Bott-integrability of the ABHS plug). Several sub-arguments are sketched at the level expected for a 10-page paper and rely heavily on [3, pp. 734-736] for details. Mathematical formulas are partially lost in the HTML rendering of the source, so formula-level verification was not possible.",
      "technical_objections": [
        {
          "confidence": 0.65,
          "evidence": "The contact condition for a Lutz form \u03b1 = f(r)d\u03b8 + g(r)d\u03c6 on S\u00b9 \u00d7 T\u00b2 is f'g \u2212 fg' > 0 (or analogously depending on orientation convention). If \u03b3(t) = (1\u2212t)(f,g) + t(f_PL, g_PL) is the convex interpolation, then (\u03b3')_f(\u03b3)_g \u2212 (\u03b3')_g(\u03b3)_f is a bilinear expression in the original and PL components that need not remain positive. No convexity assumption on the original curve is stated.",
          "objection": "The convex linear interpolation between a Lutz plane curve and its piecewise-linear approximation is claimed to give a homotopy through contact forms (Section 3), but the contact condition for Lutz forms \u2014 a positivity condition on f'g \u2212 g'f \u2014 is not obviously preserved under pointwise convex combination of two curves.",
          "paper_location": "Section 3, proof of Proposition 2, paragraph beginning 'Next we modify the contact form...'",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.55,
          "evidence": "The paper says 'details of the construction are given in [3, pp. 734-736]' and describes only the Morse foliation geometry (Figure 2, necklace structure). The invariance under \u03c6\u2082 (which acts on individual discs D_k by Hamiltonian diffeomorphisms) for the connecting pieces of the necklace is not argued. The cited pages in [3] describe the construction of \u03c6 for the purpose of Proposition 3, not for a Morse function.",
          "objection": "The invariance of the described Morse function on D\u00b2 under the ABHS diffeomorphism \u03c6 = \u03c6\u2081 \u2218 \u03c6\u2082 (Section 4) is asserted via geometric description but not proved in the paper; the details are deferred to [3, pp. 734-736]. It is unclear whether [3] actually constructs the Morse function or only the diffeomorphism \u03c6.",
          "paper_location": "Section 4, proof of Addendum 4",
          "severity": "moderate",
          "would_change_verdict_if_true": true
        },
        {
          "confidence": 0.5,
          "evidence": "The paper says the Morse foliation shown in Figure 3, 'with one additional critical point of index [0]', defines an extension to a Morse\u2013Bott foliation on the complement in the linear Lutz piece. The Reeb-invariance of this extension (which must hold for the function to qualify as a Bott integral) is not checked.",
          "objection": "The global Morse\u2013Bott function on the manifold M after plug insertion (Section 5) is constructed only at the level of 'the Morse function can be chosen so that it coincides with the original near the boundary.' The smoothness and Reeb-invariance of the global extension across the plug boundary circles is not verified.",
          "paper_location": "Section 5, paragraph beginning 'The image under \u03a8 of the Morse\u2013Bott foliation...'",
          "severity": "minor",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.4,
          "evidence": "The paper says 'the number of summands (i.e., the range of j) and the \u03b5_j depend on the chosen N. By then choosing N sufficiently small, we can ensure [the volume estimate].' This presupposes that the number of plugs does not grow faster than \u03b5_j can be shrunk, but no quantitative bound on the number of plugs as a function of N is given.",
          "objection": "The volume estimate in Section 5 involves a sum over plugs whose number of terms depends on N (the period lower bound). The claim that \u03a3\u03b5_k can be made arbitrarily small independently of N is stated but not argued in detail.",
          "paper_location": "Section 5, volume estimate equations",
          "severity": "minor",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.45,
          "evidence": "The proof says 'the last comment about convex linear interpolation still applies' for the smoothing, so condition (i) is satisfied. But the Bott integral F is defined on all of M; modifying the contact form changes the Reeb vector field, and F must remain invariant under the new Reeb flow. This is not explicitly checked for the smoothing homotopy.",
          "objection": "The paper does not verify that the Bott-integrable homotopy in Proposition 2(i) (passing through forms all sharing the same Bott integral F) is actually achievable for the smoothing of vertices in the PL curve. The smoothing regions introduce a curve that interpolates between two linear segments; whether the resulting contact form admits F as a Bott integral during the interpolation is not addressed.",
          "paper_location": "Section 3, Proposition 2(i) and its proof, final paragraphs",
          "severity": "minor",
          "would_change_verdict_if_true": false
        }
      ]
    },
    "reviewer": "claude"
  },
  {
    "review": {
      "confidence": 0.85,
      "cycle": 1,
      "followup_notes": {
        "changed_mind": false,
        "changes_from_prior_cycle": "",
        "invalid_points_from_other_reviewers": [],
        "valid_points_from_other_reviewers": []
      },
      "main_claims": [
        {
          "claim": "There is no universal upper bound for the systolic ratio of Bott-integrable contact forms on closed 3-manifolds.",
          "notes": "The claim is supported by an explicit construction that combines linearised Lutz pieces with ABHS plugs to arbitrarily decrease the contact volume while keeping the minimal period bounded from below.",
          "paper_location": "Theorem 1, page 2",
          "support_level": "well_supported"
        },
        {
          "claim": "The ABHS plug admits a Bott integral whose level sets near the boundary of the solid torus are regular tori.",
          "notes": "The paper explicitly constructs the required invariant Morse function on the mapping torus by analyzing the Morse foliation of the specific Hamiltonian diffeomorphisms making up the ABHS map.",
          "paper_location": "Addendum 4, page 7",
          "support_level": "well_supported"
        }
      ],
      "missing_assumptions": [],
      "needs_human_spotcheck": [],
      "novelty_assessment": "The result is a natural and interesting application of the ABHS plug to the restricted class of Bott-integrable contact forms. Showing that the ABHS plug itself can be made Bott-integrable by a careful choice of invariant Morse function is a nice technical addition that complements recent findings on the flexibility of integrable Reeb flows.",
      "paper_id": "2604.19237",
      "recommended_verdict": "promising",
      "reviewer": "gemini",
      "summary": "The authors show that the systolic ratio of Bott-integrable contact forms on closed 3-manifolds has no universal upper bound, proving that integrable contact forms can exhibit large systolic ratios just like general contact forms. The proof relies on piecewise linear approximations of Lutz forms combined with the insertion of a 'plug' constructed by Abbondandolo, Bramham, Hryniewicz, and Salom\u00e3o (ABHS). A key technical contribution is showing that the ABHS plug is Bott-integrable, which is achieved by constructing a Morse function invariant under the specific area-preserving diffeomorphism defining the plug.",
      "technical_objections": []
    },
    "reviewer": "gemini"
  }
]
```
