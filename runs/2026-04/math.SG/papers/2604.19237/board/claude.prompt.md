You are the board synthesizer for an LLM review board.

Use the paper bundle and all review-cycle artifacts to produce a public-facing
board report. Your task is not to average votes. Your task is to identify which
claims and objections survived adversarial cross-review.

Rules:
- Do not claim the paper is formally verified.
- Include only objections that are supported by paper text or clear reasoning.
- Mark uncertain specialist questions as human spot-checks.
- Include a board score out of 10 and dimension sub-scores at the end for
  information/ranking. Do not simply average reviewer scores; score what
  survived cross-review.
- Return only JSON matching the provided schema.

Score calibration:
- 9-10: exceptional, likely field-shaping, technically very strong.
- 7-8: strong or clearly promising, worth surfacing, with manageable caveats.
- 5-6: competent or interesting but routine, unclear, or meaningfully caveated.
- 3-4: weakly supported, low novelty, or significant unresolved issues.
- 0-2: likely wrong, misleading, or not review-ready.
- Technical soundness should reflect surviving unresolved proof gaps.
- Reviewer confidence is a 0-10 version of how much the board trusts its
  assessment, not how good the paper is.

Paper id: 2604.19237

Schema:
```json
{
  "type": "object",
  "additionalProperties": false,
  "required": [
    "paper_id",
    "final_verdict",
    "confidence",
    "public_summary",
    "strongest_supported_claims",
    "strongest_objections",
    "reviewer_disagreements",
    "human_spotchecks",
    "audit_trail",
    "board_score_10",
    "dimension_scores",
    "score_rationale"
  ],
  "properties": {
    "paper_id": { "type": "string" },
    "final_verdict": {
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
    "public_summary": { "type": "string" },
    "strongest_supported_claims": {
      "type": "array",
      "items": { "type": "string" }
    },
    "strongest_objections": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["objection", "severity", "supporting_reviewers", "paper_location"],
        "properties": {
          "objection": { "type": "string" },
          "severity": {
            "type": "string",
            "enum": ["minor", "moderate", "major", "fatal"]
          },
          "supporting_reviewers": {
            "type": "array",
            "items": { "type": "string" }
          },
          "paper_location": { "type": "string" }
        }
      }
    },
    "reviewer_disagreements": {
      "type": "array",
      "items": { "type": "string" }
    },
    "human_spotchecks": {
      "type": "array",
      "items": { "type": "string" }
    },
    "audit_trail": {
      "type": "object",
      "additionalProperties": false,
      "required": ["cycles_used", "reviewers_used", "notes"],
      "properties": {
        "cycles_used": { "type": "integer", "minimum": 1 },
        "reviewers_used": {
          "type": "array",
          "items": { "type": "string" }
        },
        "notes": { "type": "string" }
      }
    },
    "board_score_10": { "type": "number", "minimum": 0, "maximum": 10 },
    "dimension_scores": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "technical_soundness",
        "novelty",
        "significance",
        "clarity",
        "reviewer_confidence"
      ],
      "properties": {
        "technical_soundness": { "type": "number", "minimum": 0, "maximum": 10 },
        "novelty": { "type": "number", "minimum": 0, "maximum": 10 },
        "significance": { "type": "number", "minimum": 0, "maximum": 10 },
        "clarity": { "type": "number", "minimum": 0, "maximum": 10 },
        "reviewer_confidence": { "type": "number", "minimum": 0, "maximum": 10 }
      }
    },
    "score_rationale": {
      "type": "string"
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

Review artifacts:
```json
[
  {
    "cycle": 1,
    "missing": false,
    "path": "runs/2026-04/math.SG/papers/2604.19237/review_cycles/cycle_01/reviews/claude.json",
    "review": {
      "confidence": 0.65,
      "cycle": 1,
      "dimension_scores": {
        "clarity": 6,
        "novelty": 7,
        "reviewer_confidence": 6,
        "significance": 7,
        "technical_soundness": 6.5
      },
      "followup_notes": {
        "changes_from_prior_cycle": "First cycle; no prior review to compare.",
        "invalid_points_from_other_reviewers": [],
        "valid_points_from_other_reviewers": []
      },
      "main_claims": [
        {
          "claim": "Theorem 1: For any Bott-integrable contact structure on a closed 3-manifold, contact forms with arbitrarily large systolic ratio exist within the Bott-integrable class.",
          "notes": "The proof strategy is clear and the pieces fit together logically, but the two core lemmas supporting it (Proposition 2 and Addendum 4) each have steps that are asserted rather than proved. If both lemmas are correct, the theorem follows; the overall argument is conditionally sound.",
          "paper_location": "Section 1, Theorem 1",
          "support_level": "partially_supported"
        },
        {
          "claim": "Proposition 2: Any Bott-integrable contact form can be homotoped (through Bott-integrable forms sharing the Bott integral) to one whose Lutz pieces are linear, with T_min bounded below by (1-\u03b5)\u00b7T_min(\u03b1) and the complement having arbitrarily small volume.",
          "notes": "The linearization strategy via PL approximation of the plane curve (f,g) is standard in spirit. However, (a) it is asserted without proof that convex interpolation between the original curve and its PL approximation preserves the contact condition f\u00b7g'\u2212g\u00b7f'>0; (b) the lower bound on T_min in the smoothing regions relies on an IVT/MVT sketch that is not fully worked out.",
          "paper_location": "Section 3, Proposition 2",
          "support_level": "partially_supported"
        },
        {
          "claim": "Addendum 4: The ABHS plug contact form on the solid torus admits a Morse\u2013Bott integral whose regular level sets near the boundary are tori.",
          "notes": "This is the central new technical contribution. The proof describes a Morse foliation ('necklace of beads') on the disc and claims it gives a Morse function invariant under the area-preserving diffeomorphism \u03c6 = \u03c6\u2082\u2218\u03c6\u2081. The \u03c6-invariance of this function is implicit\u2014it follows from the equivariance of \u03c6 under rotation by 2\u03c0/N and the fact that the necklace is an orbit under this rotation\u2014but is never explicitly stated or verified. The paper refers to [3, pp. 734\u2013736] for details of \u03c6 but does not reproduce enough to make the invariance argument self-contained.",
          "paper_location": "Section 4, Addendum 4",
          "support_level": "partially_supported"
        },
        {
          "claim": "The ABHS plug (Proposition 3) has properties: standard near boundary, T_min \u2265 1, volume < \u03b4 for any \u03b4 > 0.",
          "notes": "This is taken verbatim from published references [3, Propositions 2.27, 3.1] and [4, Proposition 3.1], which appeared in Inventiones Math. and Ann. Sc. Norm. Super. Pisa respectively. The paper correctly cites and applies these results.",
          "paper_location": "Section 4, Proposition 3",
          "support_level": "well_supported"
        },
        {
          "claim": "The systolic ratio of the resulting contact form can be made arbitrarily large by choosing \u03b4_i (plug volumes) sufficiently small.",
          "notes": "The volume and T_min estimates in Section 5 are written as sums that are qualitatively correct but the quantitative chain of inequalities is compressed and some intermediate steps are not displayed. The HTML rendering has likely dropped some formula content (denominators, exponents), making full verification impossible from this source.",
          "paper_location": "Section 5",
          "support_level": "partially_supported"
        }
      ],
      "missing_assumptions": [
        {
          "assumption": "The piecewise-linear approximation \u03b3\u0303 of the plane curve \u03b3 can always be chosen with rational (or infinite) slopes while remaining C\u00b9-close to \u03b3 and with vertices on \u03b3.",
          "paper_location": "Section 3, proof of Proposition 2",
          "why_it_matters": "This is needed for the Reeb flow on the linear pieces to be periodic (rational slope gives periodic orbits by formula (1)). The existence of such an approximation is geometrically obvious, but the paper does not state it as a lemma. If the curve \u03b3 has regions where rational-slope linear approximations cannot be made close while keeping vertices on \u03b3, the construction could fail."
        },
        {
          "assumption": "The ABHS diffeomorphism \u03c6 is equivariant under rotation by 2\u03c0/N in a way that makes the necklace construction well-defined on the quotient disc.",
          "paper_location": "Section 4, description of \u03c6\u2082",
          "why_it_matters": "The invariant Morse function is built on the quotient D\u00b2/(rotation by 2\u03c0/N) and then lifted. For this to work, \u03c6 must descend to a well-defined map on the quotient. The equivariance is stated ('extend this diffeomorphism of D\u00b2 to a diffeomorphism equivariant with respect to the Z_N-action') but its compatibility with \u03c6\u2081 (which only approximately rotates by 2\u03c0/N on large discs) is not verified."
        },
        {
          "assumption": "The contact form on the Lutz piece can be restricted to the sub-annulus needed for the Moser embedding, and the resulting embedding extends smoothly across the boundary to the unchanged Lutz form.",
          "paper_location": "Section 5, embedding construction",
          "why_it_matters": "The Moser embedding is used to embed the plug's domain into the linear Lutz piece. The boundary conditions must match on both sides for the Bott integral to extend across the boundary without introducing new critical points or breaking the Bott-Morse condition."
        }
      ],
      "needs_human_spotcheck": [
        {
          "question": "Does the Morse function constructed in the proof of Addendum 4\u2014via the 'necklace of beads' foliation on the disc\u2014actually satisfy \u03c6-invariance? Specifically, does \u03c6\u2082\u2218\u03c6\u2081 preserve the level sets of F as described?",
          "why_model_cannot_resolve": "The verification requires checking equivariance of \u03c6\u2082\u2218\u03c6\u2081 against the Morse foliation using the detailed construction in [3, pp. 734\u2013736], which is not reproduced in this paper and which I cannot access. The argument is plausible from symmetry, but the composition \u03c6\u2082\u2218\u03c6\u2081 may break the exact N-fold symmetry that the necklace relies on."
        },
        {
          "question": "Are the volume and T_min estimates in Section 5 quantitatively correct? The HTML source appears to have dropped several formulas (exponents, subscripts) in the chain of inequalities.",
          "why_model_cannot_resolve": "The HTML rendering is incomplete; the original PDF must be consulted to read the actual inequalities. The qualitative argument (small \u03b4_i makes volume small while T_min stays bounded below) is sound, but the specific bounds could contain errors not visible in this source."
        },
        {
          "question": "Does the convex interpolation between \u03b3 and its PL approximation \u03b3\u0303 preserve the contact condition f\u00b7g'\u2212g\u00b7f'>0 along the entire interpolation?",
          "why_model_cannot_resolve": "This requires a local calculation on the interpolated curve (1\u2212s)\u03b3+s\u03b3\u0303 and its derivative, taking into account the precise geometry of the approximation. The paper asserts it follows from C\u00b9-closeness, but the exact bound needed on the approximation is not stated, and whether 'sufficiently C\u00b9-close' can be made uniform across the compact complement of the singular level sets is a quantitative question."
        }
      ],
      "novelty_assessment": "The main novelty is the combination of two existing tools\u2014the ABHS plug construction [3,4] and the Bott integrability framework from the authors' own prior work [9]\u2014with the new ingredient being Addendum 4 (integrability of the ABHS plug) and the PL linearization technique of Proposition 2. Neither the ABHS plugs nor Bott integrability are new, but their combination to produce Bott-integrable contact forms with large systolic ratio is new and non-trivial. The paper correctly positions itself in the literature: it extends [9,10] (Bott integrability of various contact forms) and complements [1,2] (Zoll contact forms have bounded systolic ratio). The observation that integrable forms can have large systolic ratio is conceptually significant: it shows Bott integrability is strictly less rigid than S\u00b9-invariance or Zoll proximity. The novelty is genuine but incremental\u2014this is a natural next step given the authors' program, and the proof uses established plug technology with one new addendum. The connection to Katok's question (Section 1) is motivating context rather than a technical contribution.",
      "overall_score_10": 6.5,
      "paper_id": "2604.19237",
      "recommended_verdict": "promising",
      "reviewer": "claude",
      "score_rationale": "Technical soundness is 6.5: the proof architecture is correct and the key ingredients are from reliable published sources, but Addendum 4\u2014the central new technical claim\u2014is argued by sketch rather than proof, and Proposition 2 has unverified steps in the interpolation and the T_min lower bound. If both lemmas hold as claimed, the paper is a clean 8; the uncertainty is about whether they do. Novelty is 7: combining ABHS plugs with Bott integrability is a natural but non-trivial step that the authors are uniquely positioned to execute, and the linearization technique (Proposition 2) is an original device. Significance is 7: the result resolves a natural question about the rigidity of Bott-integrable contact forms, with connections to Katok's approximation problem. Clarity is 6: the paper is logically organized and the proof strategy is clearly explained, but the proofs of the two main new results are compressed to the point of incompleteness, and the HTML rendering has further obscured quantitative content. Reviewer confidence is 6: I can evaluate the structure and high-level plausibility of the argument, but full verification of Addendum 4 and the quantitative estimates in Section 5 requires the PDF and access to [3].",
      "summary": "The paper proves that on any closed 3-manifold carrying a Bott-integrable contact structure, there exist Bott-integrable contact forms with arbitrarily large systolic ratio. This answers a natural question left open by the literature on systolic inequalities in contact geometry. The proof proceeds in three main steps: (1) approximate any Bott-integrable contact form by piecewise-linear Lutz forms (Proposition 2), (2) insert ABHS plugs\u2014solid-torus contact forms with large T_min and small volume from Abbondandolo\u2013Bramham\u2013Hryniewicz\u2013Salom\u00e3o [3,4]\u2014into the linear Lutz pieces, and (3) establish that the ABHS plug carries a Bott integral (Addendum 4). The result complements known systolic inequalities for Zoll-close and S\u00b9-invariant contact forms, showing the class of Bott-integrable forms is strictly larger. The authors are established experts and the paper is published-quality in organization, but several key proof steps are asserted more than demonstrated, and the HTML source has lost some notation.",
      "technical_objections": [
        {
          "confidence": 0.7,
          "evidence": "The paper says 'we simply need to exhibit a Morse function... invariant under \u03c6' and then describes the foliation structure, but never states 'this function is invariant under \u03c6 because...' The argument is visual/informal and refers to [3, pp. 734\u2013736] for details that are not reproduced.",
          "objection": "The proof of Addendum 4 does not explicitly verify that the constructed Morse function F is invariant under the diffeomorphism \u03c6 = \u03c6\u2082\u2218\u03c6\u2081. The argument is implicit: because \u03c6 is equivariant with respect to rotation by 2\u03c0/N and the necklace construction is N-fold symmetric, F should be \u03c6-invariant. But this chain of reasoning is never written down.",
          "paper_location": "Section 4, proof of Addendum 4",
          "severity": "major",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.55,
          "evidence": "The paper states 'The convex linear interpolation between [\u03b3] and [\u03b3\u0303] defines a homotopy via contact forms sharing the same Bott integral' without justification. For a convex combination \u03b3_s = (1\u2212s)\u03b3 + s\u03b3\u0303, the derivative \u03b3_s' = (1\u2212s)\u03b3' + s\u03b3\u0303', and the contact condition becomes f_s\u00b7g_s'\u2212g_s\u00b7f_s'>0, which requires checking. The C\u00b9-closeness argument is implied but not executed.",
          "objection": "In Proposition 2, it is asserted without proof that the convex linear interpolation between the original plane curve \u03b3 and its piecewise-linear approximation \u03b3\u0303 yields a family of contact forms. The contact condition f\u00b7g'\u2212g\u00b7f'>0 is not obviously preserved under convex interpolation of curves, even when the interpolation is C\u00b9-small.",
          "paper_location": "Section 3, proof of Proposition 2, third paragraph",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.5,
          "evidence": "The proof says 'In the smoothing regions of [\u03b3\u0303], the slope varies between two rational slopes... By the intermediate value theorem, any rational slope between them is realised.' This handles smoothing regions within the Lutz pieces, but the proof of condition (ii) for the full manifold\u2014including neighborhoods of singular level sets\u2014is not addressed.",
          "objection": "The lower bound T_min(\u03b1') \u2265 (1\u2212\u03b5)\u00b7T_min(\u03b1) in condition (ii) of Proposition 2 is argued using MVT (for linear pieces) and IVT (for smoothing regions), but the argument does not account for what happens near the singular level sets of the Morse\u2013Bott function, where the Lutz form description does not apply.",
          "paper_location": "Section 3, final paragraph of proof of Proposition 2",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.95,
          "evidence": "The HTML rendering consistently drops subscripts, superscripts, and some inline math. For example, the Morse indices in the description of the necklace foliation are rendered as generic placeholders. This is an artifact of the source format, not the paper itself, but it prevents complete verification.",
          "objection": "The HTML source has lost mathematical content in several key places: the Morse index values in Section 4 ('a critical point of Morse index [?] at the centre of each D_i, and a critical point of index [?] on each connecting piece'), and some quantitative formulas in Section 5. The review cannot fully evaluate these steps.",
          "paper_location": "Section 4 (Morse indices), Section 5 (volume estimates)",
          "severity": "minor",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.4,
          "evidence": "The paper states the conclusion ('regular tori near the boundary') but does not verify it from the construction. The identification of the mapping torus with D\u00b2\u00d7S\u00b9 is via a diffeomorphism that depends on \u03c6, and the boundary behavior of F must be checked in the coordinates of the solid torus, not just the mapping torus.",
          "objection": "The paper introduces a Bott integral on the mapping torus of \u03c6 and then transfers it to the solid torus via the claimed diffeomorphism between the two. The regularity of level sets of the resulting Bott integral near the boundary of the solid torus (claimed in Addendum 4) needs to be checked carefully against the specific form of the diffeomorphism used to identify the mapping torus with the solid torus.",
          "paper_location": "Section 4, final paragraph of Addendum 4 proof",
          "severity": "minor",
          "would_change_verdict_if_true": false
        }
      ]
    },
    "reviewer": "claude"
  },
  {
    "cycle": 1,
    "missing": false,
    "path": "runs/2026-04/math.SG/papers/2604.19237/review_cycles/cycle_01/reviews/codex.json",
    "review": {
      "confidence": 0.57,
      "cycle": 1,
      "dimension_scores": {
        "clarity": 6.2,
        "novelty": 7.6,
        "reviewer_confidence": 5.7,
        "significance": 7.4,
        "technical_soundness": 6.3
      },
      "followup_notes": {
        "changes_from_prior_cycle": "N/A for cycle 1.",
        "invalid_points_from_other_reviewers": [],
        "valid_points_from_other_reviewers": []
      },
      "main_claims": [
        {
          "claim": "There is no universal upper bound for the systolic ratio among Bott-integrable contact forms defining any fixed Bott-integrable contact structure on a closed 3-manifold.",
          "notes": "The construction is credible and uses known ABHS plugs, but several gluing and exact-contact-structure details are only sketched.",
          "paper_location": "Theorem 1 and Section 5",
          "support_level": "partially_supported"
        },
        {
          "claim": "A Bott-integrable contact form can be modified so that, outside arbitrarily small volume, it is a finite union of linear Lutz pieces while the minimal Reeb period stays controlled from below.",
          "notes": "The local Lutz-form formulas support the idea, but the proof of uniform period control through piecewise-linear approximation and smoothing is terse.",
          "paper_location": "Proposition 2 and Section 3",
          "support_level": "partially_supported"
        },
        {
          "claim": "The ABHS plug can be equipped with a Bott integral whose regular boundary levels are tori.",
          "notes": "This is the key new ingredient, but the proof mostly describes a foliation from a figure and does not fully verify invariance under the actual ABHS return map.",
          "paper_location": "Addendum 4 and Section 4",
          "support_level": "unclear"
        },
        {
          "claim": "After plug insertion, the total contact volume can be made arbitrarily small while the systole remains bounded below.",
          "notes": "The volume-period estimates match the ABHS plug philosophy, but the order of parameter choices and seam compatibility should be made more explicit.",
          "paper_location": "Section 5",
          "support_level": "partially_supported"
        }
      ],
      "missing_assumptions": [
        {
          "assumption": "A Gray-stability pullback is allowed and preserves the reviewed properties.",
          "paper_location": "Theorem 1 conclusion and Section 5",
          "why_it_matters": "Without this standard step, the construction appears to prove the result for a contact structure isotopic to xi rather than for xi itself."
        },
        {
          "assumption": "The ABHS monodromy preserves the described necklace foliation exactly, not just up to isotopy or visual symmetry.",
          "paper_location": "Addendum 4 / Section 4",
          "why_it_matters": "Exact invariance is required for the Morse function to descend to the mapping torus and become a Bott integral for the plug."
        },
        {
          "assumption": "The piecewise-linear and smoothed Lutz approximations preserve the contact condition and period lower bounds uniformly on all modified regions.",
          "paper_location": "Proposition 2",
          "why_it_matters": "The final large systolic ratio depends on ruling out newly introduced short closed Reeb orbits."
        },
        {
          "assumption": "The local Bott integrals on original regions and inserted plugs can be matched smoothly on collars with Morse-Bott singular sets unchanged or controlled.",
          "paper_location": "Section 5",
          "why_it_matters": "Bott integrability is a global condition on one invariant Morse-Bott function, not just a local foliation away from seams."
        }
      ],
      "needs_human_spotcheck": [
        {
          "question": "Does the necklace foliation in Section 4 actually define a smooth Morse function invariant under the exact ABHS area-preserving diffeomorphism used in Proposition 3?",
          "why_model_cannot_resolve": "The paper gives only a compressed description and figures; checking this requires comparing against the detailed ABHS construction in the cited papers."
        },
        {
          "question": "Can the Proposition 2 period comparison be made uniform through all smoothing regions and special slope cases?",
          "why_model_cannot_resolve": "The arXiv HTML omits much notation, and the proof relies on geometric estimates that are not fully written out in the provided text."
        },
        {
          "question": "Is the final contact form explicitly pulled back to define the original contact structure xi, or is this handled implicitly by the authors' conventions?",
          "why_model_cannot_resolve": "This is probably a standard Gray-stability omission, but the provided proof text does not state it."
        }
      ],
      "novelty_assessment": "If correct, the paper gives a meaningful and interesting extension of the ABHS large-systolic-ratio plug method into the Bott-integrable category. The novelty seems concentrated in the integrable plug addendum and the compatibility with Lutz-form decompositions of Bott-integrable Reeb flows. The result is significant but relies heavily on existing ABHS technology and prior structure theorems for Bott-integrable contact forms.",
      "overall_score_10": 7.0,
      "paper_id": "2604.19237",
      "recommended_verdict": "promising",
      "reviewer": "codex",
      "score_rationale": "The main theorem is plausible and potentially important, and the overall strategy is coherent. I lowered technical soundness because the central new Addendum 4 and the global gluing of Bott integrals are not fully auditable from the text, and the exact fixed-contact-structure conclusion needs an explicit Gray-stability step. These look more like fixable proof-exposition gaps than clear false statements, so the paper remains promising rather than weak.",
      "summary": "The paper argues that every Bott-integrable contact structure on a closed 3-manifold admits Bott-integrable defining contact forms with arbitrarily large systolic ratio. The strategy is plausible: linearize Lutz-form regions away from small-volume singular neighborhoods, insert ABHS small-volume large-period plugs into the linear pieces, and add an invariant Morse-Bott integral on the plug. I do not certify the proof. My main concerns are local gaps in the central addendum proving integrability of the ABHS plug, plus some omitted compatibility details needed to conclude the result for the original contact structure rather than only an isotopic one.",
      "technical_objections": [
        {
          "confidence": 0.78,
          "evidence": "The construction produces contact forms homotopic or isotopic through contact forms to the starting one. Theorem 1 asks for a Bott-integrable contact form defining the given contact structure xi, not merely an isotopic contact structure. A standard Gray-stability pullback would likely fix this, and Bott integrability and systolic ratio should be diffeomorphism-invariant, but this step is not stated in the proof.",
          "objection": "The proof does not explicitly recover a contact form defining the original plane field xi after homotopies and plug insertions.",
          "paper_location": "Proposition 2(i), Proposition 3(ii), and the conclusion of Section 5",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.62,
          "evidence": "The text describes beads joined into a necklace and says the resulting Morse function lifts to the desired invariant Morse function. It does not explicitly verify preservation of the connecting level sets under the composition of the positive radial rotation and the negatively rotating bead maps, nor smooth matching at the supports of the Hamiltonian diffeomorphisms. Since exact invariance is needed for the function to descend to the mapping torus, this is a central proof obligation.",
          "objection": "The proof of Addendum 4 does not fully check that the proposed Morse foliation is invariant under the full ABHS diffeomorphism.",
          "paper_location": "Section 4, paragraphs beginning 'We now describe the relevant properties of phi' through the discussion of Figure 2",
          "severity": "major",
          "would_change_verdict_if_true": true
        },
        {
          "confidence": 0.55,
          "evidence": "The proof compares the slope of each linear segment, and each rational slope in a smoothing region, with a slope of the original curve at some point by the mean value or intermediate value theorem. It is not fully spelled out how this comparison is made uniformly over all finitely many pieces, including near vertices, infinite slopes, zero coefficients, and unchanged boundary regions, so that no new short closed Reeb orbit appears.",
          "objection": "The lower bound on the minimal Reeb period after linearisation and smoothing needs a more uniform argument.",
          "paper_location": "End of the proof of Proposition 2",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.51,
          "evidence": "The text says the Morse function can be chosen to coincide with the original near the boundary and extends the foliation as in Figure 3. A rigorous argument should identify the boundary collars, match function values and regular levels with the pre-existing Bott integral, and verify the Morse-Bott nondegeneracy of the resulting global function across the gluing region.",
          "objection": "The global Morse-Bott integral after inserting the plug is asserted rather than constructed with full seam checks.",
          "paper_location": "Section 5, paragraph beginning 'Now we replace the contact form'",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.48,
          "evidence": "The constants c_i and number of summands depend on the linearization parameter, while the plug period lower bound depends on the ABHS parameter T and the plug volumes on epsilon. The conclusion is plausible because there are finitely many pieces, but the proof should explicitly choose T large enough for all period lower bounds and then epsilon small enough for the volume estimate.",
          "objection": "The parameter-selection order in the final volume and systole estimates is somewhat compressed.",
          "paper_location": "End of Section 5",
          "severity": "minor",
          "would_change_verdict_if_true": false
        }
      ]
    },
    "reviewer": "codex"
  },
  {
    "cycle": 1,
    "missing": false,
    "path": "runs/2026-04/math.SG/papers/2604.19237/review_cycles/cycle_01/reviews/gemini.json",
    "review": {
      "confidence": 0.85,
      "cycle": 1,
      "dimension_scores": {
        "clarity": 9,
        "novelty": 8,
        "reviewer_confidence": 8,
        "significance": 8,
        "technical_soundness": 9
      },
      "followup_notes": {
        "changes_from_prior_cycle": "",
        "invalid_points_from_other_reviewers": [],
        "valid_points_from_other_reviewers": []
      },
      "main_claims": [
        {
          "claim": "There is no universal upper bound for the systolic ratio of Bott-integrable contact forms on closed 3-manifolds.",
          "notes": "The claim is supported by a sequential construction utilizing piecewise linear Lutz forms and the insertion of volume-reducing ABHS plugs.",
          "paper_location": "Theorem 1, Section 1",
          "support_level": "well_supported"
        },
        {
          "claim": "Every Bott-integrable contact form can be homotoped to a piecewise linear Lutz form outside a set of arbitrarily small volume, while preserving control over the minimum Reeb period.",
          "notes": "Follows from standard convex interpolations and approximations of the Lutz plane curves, along with explicit control of the resulting Reeb vector field periods.",
          "paper_location": "Proposition 2, Section 3",
          "support_level": "well_supported"
        },
        {
          "claim": "The ABHS plug admits a Bott integral whose level sets near the boundary of the solid torus are regular tori, preserving Bott integrability when glued.",
          "notes": "Proved by constructing an invariant Morse function on the disk for the area-preserving diffeomorphism used to build the plug, which relies on a carefully designed Morse foliation of annuli.",
          "paper_location": "Addendum 4, Section 4",
          "support_level": "well_supported"
        }
      ],
      "missing_assumptions": [],
      "needs_human_spotcheck": [],
      "novelty_assessment": "The result is highly interesting as it demonstrates unexpected flexibility in Bott-integrable contact forms, which might otherwise be expected to be rigid. Combining ABHS plugs with Bott-integrable structures via a newly constructed invariant Morse-Bott function on the plug is a clever, technically proficient, and novel contribution.",
      "overall_score_10": 8,
      "paper_id": "2604.19237",
      "recommended_verdict": "promising",
      "reviewer": "gemini",
      "score_rationale": "The paper is cleanly written and effectively executed. The proof strategy elegantly unites two disparate threads of symplectic geometry (ABHS volume-reduction plugs and Bott-integrable Lutz forms) through a rigorously constructed invariant Morse foliation. The result provides solid evidence for the relative flexibility of integrable contact structures.",
      "summary": "The paper demonstrates that there is no universal upper bound for the systolic ratio of Bott-integrable contact forms on any closed 3-manifold that admits a Bott-integrable contact structure. The proof operates by modifying an initial Bott-integrable contact form in two stages. First, Lutz forms are approximated by piecewise linear Lutz forms outside a set of arbitrarily small volume. Second, the authors insert 'plugs' constructed by Abbondandolo, Bramham, Hryniewicz, and Salom\u00e3o (ABHS plugs) into the linear pieces. These plugs have arbitrarily small volume but maintain a lower bound on the minimum period of the Reeb flow. The primary technical contribution is showing that these ABHS plugs can be made compatible with Bott integrability by explicitly constructing an invariant Morse-Bott function on the plug that smoothly patches with the original Morse-Bott function.",
      "technical_objections": []
    },
    "reviewer": "gemini"
  },
  {
    "cycle": 2,
    "missing": false,
    "path": "runs/2026-04/math.SG/papers/2604.19237/review_cycles/cycle_02/reviews/claude.json",
    "review": {
      "confidence": 0.65,
      "cycle": 2,
      "dimension_scores": {
        "clarity": 6,
        "novelty": 7,
        "reviewer_confidence": 6,
        "significance": 7,
        "technical_soundness": 6.5
      },
      "followup_notes": {
        "changes_from_prior_cycle": "I slightly increased the overall score from 6.5 to 7.0 after reading codex's review, which independently corroborated my concern about Addendum 4 and added the Gray-stability gap I had missed. I also upgraded the severity of the Addendum 4 objection to 'would_change_verdict_if_true: true' in line with codex's assessment. I did not move toward gemini's much higher scores because gemini's review does not engage with the specific invariance gap in Addendum 4.",
        "invalid_points_from_other_reviewers": [
          "Gemini's claim that Addendum 4 is 'well_supported' and that all claims are essentially proved is not credible. The paper's own text says 'we simply need to exhibit a Morse function invariant under \u03c6' without proving invariance\u2014gemini appears to credit the description of the foliation as a proof of invariance, which it is not.",
          "Gemini's zero technical objections for a 10-page paper with compressed proofs and an incomplete HTML rendering is implausible; the high reviewer_confidence score (8) reflects over-confidence rather than genuine resolution of the gaps identified by codex and me.",
          "Codex's 'would_change_verdict_if_true: true' for the Addendum 4 gap is well-placed, but codex's overall confidence of 0.78 on the Gray-stability objection seems slightly high\u2014this is likely a standard omission the authors know to fill in, not a missing argument they overlooked."
        ],
        "valid_points_from_other_reviewers": [
          "Codex: The construction produces contact forms homotopic to the original, and a Gray-stability step is needed to conclude the result for the original contact structure \u03be rather than merely an isotopic one. This was missing from my cycle 1 review and is a legitimate concern.",
          "Codex: The global Morse\u2013Bott seam matching across plug boundaries needs explicit treatment\u2014Bott integrability is a global condition, not just local away from seams.",
          "Codex: The parameter-selection order in Section 5 is compressed; T (ABHS parameter) and \u03b4\u1d62 (plug volumes) need to be chosen in a specific order that is not made explicit."
        ]
      },
      "main_claims": [
        {
          "claim": "Theorem 1: For any Bott-integrable contact structure on a closed 3-manifold, contact forms with arbitrarily large systolic ratio exist within the Bott-integrable class.",
          "notes": "The proof architecture is conditionally correct. If Proposition 2 and Addendum 4 are accepted, Theorem 1 follows from the estimates in Section 5. Both supporting lemmas have proof gaps. Additionally, codex correctly notes that the construction produces forms homotopic to the original, and a Gray-stability step is needed to recover a form defining the same contact structure \u03be\u2014this step is not stated.",
          "paper_location": "Section 1, Theorem 1",
          "support_level": "partially_supported"
        },
        {
          "claim": "Proposition 2: Any Bott-integrable contact form can be homotoped through Bott-integrable forms to one whose Lutz pieces are linear, with T_min bounded below by (1\u2212\u03b5)\u00b7T_min(\u03b1) and the complement having arbitrarily small volume.",
          "notes": "The PL-approximation strategy is natural. The contact condition f\u00b7g'\u2212g\u00b7f'>0 under convex interpolation is not verified. The T_min lower bound via MVT/IVT is sketched for linear and smoothing regions but not addressed near singular level sets where the Lutz description breaks down.",
          "paper_location": "Section 3, Proposition 2",
          "support_level": "partially_supported"
        },
        {
          "claim": "Addendum 4: The ABHS plug contact form admits a Morse\u2013Bott integral whose regular level sets near the boundary are tori.",
          "notes": "This is the central new technical result. The proof describes a Morse foliation ('necklace of beads') on the disc and asserts that it lifts to a \u03c6-invariant Morse function on the mapping torus. The \u03c6-invariance is never explicitly verified: the argument relies on the N-fold symmetry of the necklace and the equivariance of \u03c6\u2082, but the composition \u03c6\u2082\u2218\u03c6\u2081 may not preserve this symmetry exactly since \u03c6\u2081 only approximately rotates by 2\u03c0/N outside a large disc. The paper refers to [3, pp. 734\u2013736] for details that are not reproduced.",
          "paper_location": "Section 4, Addendum 4",
          "support_level": "unclear"
        },
        {
          "claim": "Proposition 3 (ABHS plug): Properties of the plug\u2014standard near boundary, T_min \u2265 1, volume < \u03b4\u2014hold as stated.",
          "notes": "Taken from published references [3, Propositions 2.27, 3.1] and [4, Proposition 3.1] in Inventiones Math. and Ann. Sc. Norm. Super. Pisa. Correctly cited and applied.",
          "paper_location": "Section 4, Proposition 3",
          "support_level": "well_supported"
        },
        {
          "claim": "The systolic ratio of the resulting contact form can be made arbitrarily large.",
          "notes": "Volume and T_min estimates are qualitatively sound. The parameter-selection order (choosing T large enough before \u03b4 small enough across all pieces) is compressed. The HTML rendering has lost some quantitative content, preventing full verification.",
          "paper_location": "Section 5",
          "support_level": "partially_supported"
        }
      ],
      "missing_assumptions": [
        {
          "assumption": "A Gray-stability step is applied to pull back the final contact form to one defining the original contact structure \u03be.",
          "paper_location": "Theorem 1 conclusion and Section 5",
          "why_it_matters": "The construction produces contact forms homotopic to \u03b1 through Bott-integrable forms, not necessarily defining the same plane field \u03be. Without this step (standard in the literature but not stated), Theorem 1 is proved only for a contact structure isotopic to \u03be."
        },
        {
          "assumption": "The composition \u03c6 = \u03c6\u2082\u2218\u03c6\u2081 is equivariant under rotation by 2\u03c0/N in a way that makes the necklace foliation on D\u00b2 well-defined as a \u03c6-invariant foliation.",
          "paper_location": "Section 4, construction of \u03c6",
          "why_it_matters": "The invariant Morse function is built on a quotient by this rotation and then lifted. For this to work, \u03c6 must descend to a well-defined map on the quotient. The equivariance of \u03c6\u2082 is stated, but compatibility with \u03c6\u2081 (which only approximately rotates on large discs) is not verified."
        },
        {
          "assumption": "The piecewise-linear approximation \u03b3\u0303 of the plane curve \u03b3 can always be chosen with rational (or infinite) slopes while remaining C\u00b9-close to \u03b3, with the C\u00b9-closeness uniform across the compact complement of the singular level sets.",
          "paper_location": "Section 3, proof of Proposition 2",
          "why_it_matters": "Needed for the Reeb flow on linear pieces to be periodic, and for the contact condition to be preserved under convex interpolation. The existence of such an approximation is geometrically plausible but not stated as a lemma."
        },
        {
          "assumption": "The lower bound on T_min in Proposition 2 holds uniformly across all modified regions, including the transition regions near singular level sets where the Lutz form description does not apply.",
          "paper_location": "Section 3, final paragraphs of proof of Proposition 2",
          "why_it_matters": "If any new short Reeb orbit appears in the transition regions, the bound T_min(\u03b1') \u2265 (1\u2212\u03b5)\u00b7T_min(\u03b1) fails, and the estimate in Section 5 for the systolic ratio breaks down."
        }
      ],
      "needs_human_spotcheck": [
        {
          "question": "Does the composition \u03c6 = \u03c6\u2082\u2218\u03c6\u2081 constructed in the ABHS paper [3, pp. 734\u2013736] actually preserve the level sets of the necklace Morse foliation described in Section 4? Specifically, does the composition of the positive radial rotation (\u03c6\u2081) and the negatively rotating bead maps (\u03c6\u2082) preserve the foliation exactly, not just up to isotopy?",
          "why_model_cannot_resolve": "Verifying this requires the detailed construction in [3, pp. 734\u2013736], which is not reproduced in this paper and to which I have no access. The argument is plausible by symmetry, but \u03c6\u2081 only approximately rotates by 2\u03c0/N (property (ii)) rather than exactly, so the composition may break the exact N-fold symmetry the necklace relies on."
        },
        {
          "question": "Do the volume and T_min estimates in Section 5 close quantitatively? The HTML source appears to have dropped exponents and subscripts in the chain of inequalities establishing the systolic ratio lower bound.",
          "why_model_cannot_resolve": "The HTML rendering is incomplete; the PDF must be consulted to read the actual inequalities. The qualitative argument is sound, but the specific bounds could contain errors invisible in this source."
        },
        {
          "question": "Does the convex interpolation (1\u2212s)\u03b3 + s\u03b3\u0303 between the original Lutz curve and its PL approximation preserve the contact condition f\u00b7g'\u2212g\u00b7f'>0 throughout the homotopy, uniformly across all Lutz pieces?",
          "why_model_cannot_resolve": "This is a local computation on the interpolated curve and its derivative. The paper asserts it follows from C\u00b9-closeness but the required quantitative bound is not stated, and whether uniform closeness can be achieved across the compact complement of the singular level sets is a non-trivial quantitative question."
        },
        {
          "question": "Is the Gray-stability step needed to recover a contact form defining exactly \u03be (rather than an isotopic contact structure) explicitly handled in the authors' framework, or is it genuinely missing?",
          "why_model_cannot_resolve": "This is likely a standard omission for experts in this field, but whether it is truly harmless depends on whether the Bott integrability and systolic ratio are preserved under the Gray diffeomorphism\u2014a point that would need to be checked in context."
        }
      ],
      "novelty_assessment": "The main novelty is the combination of the ABHS plug technology [3,4] with the Bott integrability framework from the authors' prior work [9,10], with the genuinely new ingredient being Addendum 4 (constructing a Bott integral on the ABHS plug) and the PL-linearization of Proposition 2. Neither ingredient is new in isolation, but their combination to produce Bott-integrable contact forms with large systolic ratio is non-trivial and resolves a natural question left open by [9]. The result is conceptually significant\u2014it shows Bott integrability is strictly less rigid than S\u00b9-invariance or Zoll-proximity, contributing to a clearer picture of the hierarchy of symmetry assumptions in contact systolic geometry. The connection to Katok's approximation question is motivating context rather than a direct contribution. Novelty is genuine but incremental: this is the natural next step in the authors' program, executed with the right tools.",
      "overall_score_10": 7,
      "paper_id": "2604.19237",
      "recommended_verdict": "promising",
      "reviewer": "claude",
      "score_rationale": "Technical soundness is 6.5: the proof architecture is sound and all major ingredients are from reliable published sources, but Addendum 4\u2014the sole new technical claim\u2014argues \u03c6-invariance by description rather than proof, and Proposition 2 leaves the contact condition under convex interpolation and the uniform T_min lower bound unverified. Both codex and I independently flagged the Addendum 4 gap; it is real and not explained away by gemini's confident but unargued dismissal. If both lemmas hold as stated, the paper is a clean 7.5\u20138; the uncertainty is whether they do. Novelty is 7.0: combining ABHS plugs with Bott integrability is a natural but non-trivial step that the authors are uniquely positioned to execute, and the PL-linearization technique is an original device. Significance is 7.0: the result resolves a natural question about the rigidity of Bott-integrable contact forms and complements the Zoll and S\u00b9-invariant systolic inequalities, with connections to Katok's approximation problem. Clarity is 6.0: the paper is well-organized and the proof strategy is clearly explained, but both main new results (Proposition 2 and Addendum 4) are argued at the level of sketch rather than proof, and the HTML rendering has lost quantitative content. Reviewer confidence is 6.0: I can evaluate the structure and high-level plausibility but cannot fully verify Addendum 4 without access to [3, pp. 734\u2013736] or the PDF. Score increased from 6.5 to 7.0 versus cycle 1, incorporating the Gray-stability gap raised by codex and reflecting that two independent reviewers (codex and me) finding the same gap in Addendum 4 provides stronger evidence that the gap is real rather than an artifact of reviewer inexpertise.",
      "summary": "The paper proves that on any closed 3-manifold carrying a Bott-integrable contact structure, Bott-integrable contact forms with arbitrarily large systolic ratio exist. The proof combines three ingredients: PL-linearization of Lutz forms (Proposition 2), insertion of ABHS plugs (Proposition 3, from published literature), and a new integrability addendum for the ABHS plug (Addendum 4). The paper is by established experts and the overall architecture is credible. However, Addendum 4\u2014the central new technical contribution\u2014argues the \u03c6-invariance of the constructed Morse function by description and reference rather than proof, and Proposition 2 leaves the contact condition under convex interpolation and the uniform T_min lower bound unverified. After reading gemini's and codex's reviews I maintain my cycle 1 assessment with small adjustments: gemini's dismissal of all technical concerns is too credulous, codex's Gray-stability gap is a legitimate addition I had missed, and the core concerns about Addendum 4 are corroborated independently by codex.",
      "technical_objections": [
        {
          "confidence": 0.72,
          "evidence": "The paper says 'we simply need to exhibit a Morse function... invariant under \u03c6' and then describes the foliation, but never writes down why \u03c6 preserves the level sets. The argument is visual and delegates key details to [3, pp. 734\u2013736] without reproducing them.",
          "objection": "The proof of Addendum 4 does not explicitly verify that the constructed Morse function F is invariant under \u03c6 = \u03c6\u2082\u2218\u03c6\u2081. The necklace foliation is N-fold symmetric and \u03c6\u2082 is constructed to be equivariant, but \u03c6\u2081 only approximately rotates by 2\u03c0/N on large discs (property (ii) of \u03c6) and is the identity near the boundary (property (iii)). The composition \u03c6\u2082\u2218\u03c6\u2081 therefore has a more complex action than pure rotation, and whether the necklace is genuinely preserved is not demonstrated.",
          "paper_location": "Section 4, proof of Addendum 4",
          "severity": "major",
          "would_change_verdict_if_true": true
        },
        {
          "confidence": 0.68,
          "evidence": "Theorem 1 states 'a Bott-integrable contact form defining \u03be'. The construction produces forms in a homotopy class. A Gray-stability pullback would fix this\u2014it is likely a standard omission\u2014but it is not stated anywhere in the paper.",
          "objection": "The proof does not explicitly apply Gray stability to recover a contact form defining the original contact structure \u03be after the homotopies and plug insertions. Proposition 2(i) produces forms homotopic through Bott-integrable forms, and Proposition 3(ii) produces a form isotopic via contact forms; the conclusion of Theorem 1 requires a form defining \u03be, not merely an isotopic contact structure.",
          "paper_location": "Proposition 2(i), Proposition 3(ii), Section 5 conclusion",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.55,
          "evidence": "The paper states 'The convex linear interpolation between [\u03b3] and [\u03b3\u0303] defines a homotopy via contact forms sharing the same Bott integral' with no justification. C\u00b9-closeness is implied but the required bound is not stated.",
          "objection": "In Proposition 2, the convex interpolation between the original curve \u03b3 and its PL approximation \u03b3\u0303 is asserted to preserve the contact condition f\u00b7g'\u2212g\u00b7f'>0 without verification. For a convex combination \u03b3\u209b = (1\u2212s)\u03b3 + s\u03b3\u0303, the derivative is \u03b3\u209b' = (1\u2212s)\u03b3' + s\u03b3\u0303', and the positivity of the cross-product is not obvious, especially near points where \u03b3\u0303 changes slope direction.",
          "paper_location": "Section 3, proof of Proposition 2, third paragraph",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.55,
          "evidence": "The paper says 'The Morse function can be chosen in such a way that the new Morse\u2013Bott function on [the Lutz piece] coincides with the original near [the boundary].' This is an assertion of compatibility, not a proof.",
          "objection": "The global Morse\u2013Bott integral after plug insertion is asserted rather than constructed with full seam verification. The Morse function must be matched across the boundary collar with the pre-existing Bott integral from the surrounding Lutz pieces, and the Morse\u2013Bott non-degeneracy of the resulting global function must be checked at the gluing region.",
          "paper_location": "Section 5, paragraph beginning 'Now we replace the contact form'",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.95,
          "evidence": "The HTML rendering consistently drops subscripts, superscripts, and Morse index numerals as generic placeholders.",
          "objection": "The HTML source has lost Morse index values in Section 4 ('a critical point of Morse index [?] at the centre of each D\u1d62') and some quantitative formulas in Section 5. The review cannot fully evaluate these steps.",
          "paper_location": "Section 4 (Morse indices), Section 5 (volume estimates)",
          "severity": "minor",
          "would_change_verdict_if_true": false
        }
      ]
    },
    "reviewer": "claude"
  },
  {
    "cycle": 2,
    "missing": false,
    "path": "runs/2026-04/math.SG/papers/2604.19237/review_cycles/cycle_02/reviews/codex.json",
    "review": {
      "confidence": 0.61,
      "cycle": 2,
      "dimension_scores": {
        "clarity": 6.1,
        "novelty": 7.5,
        "reviewer_confidence": 6.1,
        "significance": 7.3,
        "technical_soundness": 6.1
      },
      "followup_notes": {
        "changes_from_prior_cycle": "I slightly lowered my score after accepting Claude's more precise objection that convex interpolation of Lutz curves needs an explicit contact-condition argument. I did not adopt Gemini's stronger confidence, because that review did not address the exact invariance gap in Addendum 4 with location-grounded evidence.",
        "invalid_points_from_other_reviewers": [
          "Gemini's 'well_supported' ratings for Proposition 2 and Addendum 4 are too strong from the provided text; they assume the missing verifications rather than auditing them.",
          "Claude's concern that Proposition 2 fails to address singular level neighborhoods is weaker than stated: the proof leaves small neighborhoods of singular levels unchanged, so those regions should not create new period-control issues if the original systole is already accounted for.",
          "Claude's suggestion that rational-slope PL approximation with vertices on the curve may fail is not a serious objection as stated; rational slopes are dense and the construction occurs on finitely many compact regular Lutz regions, though a short lemma would improve exposition."
        ],
        "valid_points_from_other_reviewers": [
          "Claude's convex-interpolation objection in Proposition 2 is valid and should be added explicitly: positivity of f g' - g f' during the homotopy needs a uniform C1 margin argument.",
          "Claude's emphasis that Addendum 4 is the central new technical claim is valid; its proof should explicitly verify invariance under the full ABHS map, not just describe the foliation.",
          "Claude's warning about HTML loss of notation is a real limitation of review confidence, especially for Section 5 estimates and Morse index data.",
          "Gemini is probably right that the overall architecture is strong if the two key lemmas are filled in, and that the result is conceptually significant."
        ]
      },
      "main_claims": [
        {
          "claim": "There is no universal upper bound for the systolic ratio among Bott-integrable contact forms defining any fixed Bott-integrable contact structure on a closed 3-manifold.",
          "notes": "The construction is coherent and uses strong published ABHS input, but the proof depends on two compressed new ingredients: the integrable plug addendum and global gluing of Bott integrals.",
          "paper_location": "Theorem 1 and Section 5",
          "support_level": "partially_supported"
        },
        {
          "claim": "A Bott-integrable contact form can be homotoped, through Bott-integrable forms sharing the Bott integral, so that outside arbitrarily small volume it is a finite union of linear Lutz pieces while the minimal Reeb period remains controlled.",
          "notes": "Claude's objection about convex interpolation preserving the contact inequality is valid and sharpens my prior concern. The argument is plausible by uniform C1-closeness on compact pieces, but the proof should spell out the quantitative contact-condition margin and the period comparison through smoothing regions.",
          "paper_location": "Proposition 2 and Section 3",
          "support_level": "partially_supported"
        },
        {
          "claim": "The ABHS plug can be equipped with a Bott integral whose regular boundary levels are tori.",
          "notes": "This remains the central point requiring human mathematical spot-checking. The text describes a necklace Morse foliation but does not explicitly verify that the full ABHS return map preserves the foliation exactly.",
          "paper_location": "Addendum 4 and Section 4",
          "support_level": "unclear"
        },
        {
          "claim": "After plug insertion, the total contact volume can be made arbitrarily small while the systole remains bounded below.",
          "notes": "The qualitative estimate is credible and consistent with ABHS. The parameter order and collar compatibility should be written more explicitly, but I do not see a clear counterargument.",
          "paper_location": "Section 5",
          "support_level": "partially_supported"
        }
      ],
      "missing_assumptions": [
        {
          "assumption": "The ABHS monodromy preserves the described necklace foliation exactly, not merely up to isotopy or visual symmetry.",
          "paper_location": "Addendum 4 / Section 4",
          "why_it_matters": "Exact invariance is needed for the Morse function to descend to the mapping torus and define a Bott integral for the plug."
        },
        {
          "assumption": "The piecewise-linear Lutz approximation is chosen with a uniform C1 margin preserving f g' - g f' > 0 throughout the convex homotopy.",
          "paper_location": "Proposition 2",
          "why_it_matters": "The homotopy through contact forms is part of the contact-structure control and underlies the later Gray-stability step."
        },
        {
          "assumption": "The slope and parametrization estimates in Proposition 2 are uniform over all smoothing regions and special rational or infinite slope cases.",
          "paper_location": "Proposition 2",
          "why_it_matters": "The final systolic lower bound depends on excluding newly introduced short Reeb orbits."
        },
        {
          "assumption": "The local Bott integrals on original regions and inserted plugs can be matched smoothly on collars without creating non-Morse-Bott critical sets.",
          "paper_location": "Section 5",
          "why_it_matters": "Bott integrability is a global condition on one invariant Morse-Bott function, not just a local foliation away from seams."
        },
        {
          "assumption": "A Gray-stability pullback is applied, or an equivalent argument is used, to return from an isotopic contact structure to the original contact structure xi.",
          "paper_location": "Conclusion of Section 5",
          "why_it_matters": "The theorem is stated for contact forms defining a fixed contact structure, so isotopy of plane fields alone is not the literal conclusion."
        }
      ],
      "needs_human_spotcheck": [
        {
          "question": "Does the necklace foliation in Section 4 define a smooth Morse function invariant under the exact ABHS diffeomorphism used in Proposition 3?",
          "why_model_cannot_resolve": "The paper gives only a compressed description and figures; checking exact invariance requires comparing with the detailed ABHS construction in the cited papers."
        },
        {
          "question": "Can the Proposition 2 contact-condition and period-comparison estimates be made uniform through all piecewise-linear and smoothing regions?",
          "why_model_cannot_resolve": "The needed argument is plausible but quantitative; the HTML text omits enough notation that a reliable check requires the PDF and a line-by-line calculation."
        },
        {
          "question": "Does the final plug gluing produce one global smooth Morse-Bott integral with correct collar matching and Morse-Bott nondegeneracy?",
          "why_model_cannot_resolve": "The paper gestures to the foliation extension using Figure 3, but verifying smooth gluing of level sets and critical manifolds is a mathematical detail not fully present in the text."
        }
      ],
      "novelty_assessment": "The novelty remains genuine and worthwhile, but not field-shaping by itself. The paper combines ABHS large-systolic-ratio plugs with the authors' Bott-integrable/Lutz-form framework, with the main new contribution being the claim that the ABHS plug admits a compatible Bott integral. If Addendum 4 is correct, this is a clean and interesting flexibility result showing Bott integrability is much less restrictive than Zoll-like or S1-invariant settings.",
      "overall_score_10": 6.7,
      "paper_id": "2604.19237",
      "recommended_verdict": "promising",
      "reviewer": "codex",
      "score_rationale": "I still view the paper as promising: the theorem is natural, the strategy is coherent, and the ABHS input is reliable. The score is below a clean accept-level 7 because the central new Addendum 4 and the Lutz linearization homotopy contain proof obligations that are described rather than fully verified in the provided text. These look like fixable proof-exposition gaps rather than clear mathematical errors, so I do not downgrade to weak_evidence or major_flaw.",
      "summary": "The paper claims that any Bott-integrable contact structure on a closed 3-manifold admits Bott-integrable defining contact forms with arbitrarily large systolic ratio. The strategy remains plausible: linearize Lutz-form regions away from small-volume parts, insert ABHS plugs with small volume and controlled Reeb periods, and equip those plugs with a compatible Bott integral. After reading the other reviews, I still regard the result as promising but not fully certified from the text. The main unresolved point is the exact invariance of the proposed Morse foliation for the ABHS monodromy; a second important exposition gap is the preservation of the contact condition and period lower bound during the piecewise-linear Lutz approximation.",
      "technical_objections": [
        {
          "confidence": 0.68,
          "evidence": "The paper says it suffices to exhibit an invariant Morse function, then describes the bead necklace foliation. It states equivariance for the extension of the bead maps, but does not explicitly prove that the composition with the radial rotation used in ABHS preserves every level set of the constructed Morse function. Exact invariance is required for the function to descend to the mapping torus.",
          "objection": "The proof of Addendum 4 does not fully check that the proposed Morse foliation is invariant under the full ABHS diffeomorphism.",
          "paper_location": "Section 4, paragraphs describing phi_1, phi_2, the equivariant bead construction, and Figure 2",
          "severity": "major",
          "would_change_verdict_if_true": true
        },
        {
          "confidence": 0.64,
          "evidence": "For a Lutz form the contact condition is f g' - g f' > 0. Under gamma_s = (1-s)gamma + s gamma_tilde this determinant is not formally linear in a way that makes positivity automatic. It should follow from sufficiently uniform C1-closeness and compactness away from singular levels, but the argument is only asserted.",
          "objection": "The convex interpolation between the original Lutz curve and its piecewise-linear approximation is asserted to stay contact without a displayed margin estimate.",
          "paper_location": "Section 3, proof of Proposition 2, paragraph beginning 'Next we modify the contact form'",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.58,
          "evidence": "The proof compares slopes of linear pieces and smoothing regions with slopes of the original curve using the mean value and intermediate value theorems. It does not fully spell out uniform control over all finitely many regions, vertices, infinite-slope cases, zero coefficients, and unchanged collars, although these issues appear likely manageable.",
          "objection": "The lower bound on the minimal Reeb period after linearisation and smoothing is too compressed to audit fully.",
          "paper_location": "End of the proof of Proposition 2",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.52,
          "evidence": "The text says the Morse function can be chosen to coincide with the original near the boundary and extends the foliation shown in Figure 3. A rigorous proof should identify the collars, match function values and regular levels, and verify Morse-Bott nondegeneracy across the gluing region.",
          "objection": "The global Morse-Bott integral after inserting the plug is asserted rather than constructed with full seam checks.",
          "paper_location": "Section 5, paragraph beginning 'Now we replace the contact form'",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.74,
          "evidence": "The construction gives contact forms homotopic or isotopic through contact forms to the starting one. Theorem 1 asks for a form defining the original contact structure, not just an isotopic one. A standard Gray-stability pullback should fix this, and Bott integrability and systolic ratio are diffeomorphism-invariant, but the final proof does not say this.",
          "objection": "The proof does not explicitly recover a contact form defining the original plane field xi after homotopies and plug insertions.",
          "paper_location": "Proposition 2(i), Proposition 3(ii), and the conclusion of Section 5",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.5,
          "evidence": "The constants attached to the finitely many linear Lutz pieces depend on the preliminary linearization, while plug volume and period bounds depend on ABHS choices. The intended order is likely: fix the linearization, choose plug parameters for all finitely many pieces, then choose volumes sufficiently small. This should be made explicit.",
          "objection": "The final parameter-selection argument is compressed.",
          "paper_location": "End of Section 5",
          "severity": "minor",
          "would_change_verdict_if_true": false
        }
      ]
    },
    "reviewer": "codex"
  },
  {
    "cycle": 2,
    "missing": false,
    "path": "runs/2026-04/math.SG/papers/2604.19237/review_cycles/cycle_02/reviews/gemini.json",
    "review": {
      "confidence": 0.8,
      "cycle": 2,
      "dimension_scores": {
        "clarity": 7,
        "novelty": 8,
        "reviewer_confidence": 7,
        "significance": 8,
        "technical_soundness": 7
      },
      "followup_notes": {
        "changes_from_prior_cycle": "I have retained my 'promising' verdict but lowered the technical soundness and clarity scores. I incorporated the excellent observations from Claude and Codex regarding unverified assertions in Addendum 4 (\u03c6-invariance), Proposition 2 (convex interpolation), and the omitted Gray-stability step in the final proof.",
        "invalid_points_from_other_reviewers": [],
        "valid_points_from_other_reviewers": [
          "Claude and Codex correctly point out that the \u03c6-invariance of the Morse function in Addendum 4 is asserted from visual symmetry rather than rigorously verified.",
          "Claude correctly observes that the convex interpolation in Proposition 2 requires explicit C\u00b9 bounds to preserve the contact condition.",
          "Codex accurately notes the missing Gray-stability pullback required to strictly satisfy Theorem 1."
        ]
      },
      "main_claims": [
        {
          "claim": "There is no universal upper bound for the systolic ratio of Bott-integrable contact forms on closed 3-manifolds.",
          "notes": "The overall architecture is very sound, but as other reviewers pointed out, the final step requires an unstated Gray-stability pullback to ensure the contact structure strictly defines \u03be, and depends on lemmas with omitted technical details.",
          "paper_location": "Theorem 1, Section 1",
          "support_level": "partially_supported"
        },
        {
          "claim": "Every Bott-integrable contact form can be homotoped to a piecewise linear Lutz form outside a set of arbitrarily small volume, while preserving control over the minimum Reeb period.",
          "notes": "The existence of the approximation is intuitive, but the preservation of the contact condition during convex interpolation and the uniform lower bounds on T_min are asserted rather than rigorously calculated.",
          "paper_location": "Proposition 2, Section 3",
          "support_level": "partially_supported"
        },
        {
          "claim": "The ABHS plug admits a Bott integral whose level sets near the boundary of the solid torus are regular tori, preserving Bott integrability when glued.",
          "notes": "The authors construct a Morse foliation (the 'necklace of beads'), but they do not explicitly prove that the corresponding Morse function is exactly invariant under the ABHS diffeomorphism \u03c6 = \u03c6\u2082 \u2218 \u03c6\u2081.",
          "paper_location": "Addendum 4, Section 4",
          "support_level": "partially_supported"
        }
      ],
      "missing_assumptions": [
        {
          "assumption": "The ABHS area-preserving diffeomorphism exactly preserves the 'necklace' Morse foliation on the disc.",
          "paper_location": "Section 4, Addendum 4",
          "why_it_matters": "If the foliation is not strictly invariant under the diffeomorphism, the function will not descend to a valid Bott integral on the plug."
        },
        {
          "assumption": "Gray-stability pullback applies cleanly and preserves the systolic ratio bounds to yield a contact form strictly defining \u03be.",
          "paper_location": "Theorem 1 and Section 5",
          "why_it_matters": "Theorem 1 states the result for a fixed contact structure \u03be. Without Gray stability, the proof only holds up to isotopy."
        }
      ],
      "needs_human_spotcheck": [
        {
          "question": "Does the Morse function constructed via the 'necklace of beads' foliation rigorously satisfy exact invariance under the ABHS diffeomorphism \u03c6\u2082 \u2218 \u03c6\u2081?",
          "why_model_cannot_resolve": "The verification requires checking the precise definitions of \u03c6\u2081 and \u03c6\u2082 from the external ABHS papers [3, 4], which are not reproduced in the text bundle."
        },
        {
          "question": "Can the piecewise-linear approximation \u03b3\u0303 in Proposition 2 be made sufficiently C\u00b9-close uniformly to ensure the convex interpolation strictly preserves the contact condition and the uniform lower bounds on T_min?",
          "why_model_cannot_resolve": "The text abstracts away the quantitative calculus necessary to verify the bounds on the contact condition during interpolation."
        }
      ],
      "novelty_assessment": "The result is highly interesting and conceptually significant, demonstrating unexpected flexibility in Bott-integrable contact forms (which might otherwise be expected to be rigid like S\u00b9-invariant ones). The novel contribution is the marriage of ABHS plugs with Bott integrability via the invariant Morse foliation.",
      "overall_score_10": 7,
      "paper_id": "2604.19237",
      "recommended_verdict": "promising",
      "reviewer": "gemini",
      "score_rationale": "The paper tackles an interesting question and the proposed architecture\u2014combining ABHS volume-reduction plugs with Bott-integrable Lutz forms\u2014is elegant and conceptually sound. However, upon reviewing the other critiques, it is clear that critical technical steps are treated informally: the exact \u03c6-invariance of the Morse foliation in Addendum 4 is asserted visually, the contact condition during convex interpolation in Proposition 2 lacks rigorous C\u00b9-bounds, and a Gray-stability pullback is omitted. These gaps lower the technical soundness and clarity scores, though the paper remains a strong, promising contribution if these expositional and technical gaps are resolved.",
      "summary": "The paper demonstrates that there is no universal upper bound for the systolic ratio of Bott-integrable contact forms on any closed 3-manifold that admits a Bott-integrable contact structure. The proof operates by modifying an initial Bott-integrable contact form in two stages. First, Lutz forms are approximated by piecewise linear Lutz forms outside a set of arbitrarily small volume. Second, the authors insert 'plugs' constructed by Abbondandolo, Bramham, Hryniewicz, and Salom\u00e3o (ABHS plugs) into the linear pieces. These plugs have arbitrarily small volume but maintain a lower bound on the minimum period of the Reeb flow. The primary technical contribution is showing that these ABHS plugs can be made compatible with Bott integrability by explicitly constructing an invariant Morse-Bott function on the plug that smoothly patches with the original Morse-Bott function.",
      "technical_objections": [
        {
          "confidence": 0.85,
          "evidence": "The text states 'This gives rise to a Morse foliation... This function lifts to the desired Morse function on P' but lacks the algebraic verification that \u03c6 preserves the level sets of F.",
          "objection": "The proof of Addendum 4 does not explicitly verify that the constructed Morse function F is invariant under the diffeomorphism \u03c6 = \u03c6\u2082 \u2218 \u03c6\u2081. The argument is primarily visual/informal and heavily relies on symmetries that are not rigorously checked against the exact maps.",
          "paper_location": "Section 4, proof of Addendum 4",
          "severity": "major",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.9,
          "evidence": "The paper states 'The convex linear interpolation between \u03b3 and \u03b3\u0303 defines a homotopy via contact forms...' without providing the C\u00b9 bounds required to guarantee the contact condition is never violated.",
          "objection": "The convex linear interpolation between the original plane curve \u03b3 and its piecewise-linear approximation \u03b3\u0303 is asserted to yield a family of contact forms, but the contact condition f\u00b7g' - g\u00b7f' > 0 is not automatically preserved by convex combinations.",
          "paper_location": "Section 3, proof of Proposition 2",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        },
        {
          "confidence": 0.95,
          "evidence": "The proof concludes with 'Theorem 1 is proved' after bounding the volume and T_min, but does not execute the pullback to strictly recover the plane field \u03be.",
          "objection": "The construction produces a contact form that is isotopic to the original contact structure, but Theorem 1 claims to produce a contact form defining the exact contact structure \u03be. A Gray-stability pullback is required but missing.",
          "paper_location": "Section 5 (conclusion)",
          "severity": "moderate",
          "would_change_verdict_if_true": false
        }
      ]
    },
    "reviewer": "gemini"
  }
]
```
