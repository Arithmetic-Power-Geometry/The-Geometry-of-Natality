# Generative Natality Calculus v3.0 — typed extensions and composition

**Status:** Formal candidate framework, with elementary propositions. Not a priority claim or a proof of superiority over existing categorical/transition-system models.

## A. Typed model
A finite rooted transition system is S=(X,T,s), with finite state set X, T subseteq X×X, and s in X.
An **extension** i:S->S' consists of an injective map i:X->X' preserving the root and all transitions: (x,y) in T implies (i(x),i(y)) in T'. The extension is *induced* if also the converse holds on original states. Define R(S) as states reachable from s.

A natality transformation is an extension together with a declared cost and an action identifier. We work up to root-preserving isomorphism, avoiding reliance on arbitrary state names.

## B. Axioms
GN1 Finite rooted transition systems.
GN2 Root-preserving injective transition homomorphisms.
GN3 Composable interventions with compatible embeddings.
GN4 Observations are invariant under isomorphism.
GN5 New states are relative to a specified embedding; not absolute metaphysical creation.
GN6 Nonnegative costs; composite costs may be additive only if declared.
GN7 Optional **inducedness** forbids silently changing old-to-old transitions.
GN8 Optional **monotonicity** forbids deleting old transitions or states.

## C. Definitions
For i:S->S':
- Accessible original gain A(i)=|R(S') intersect i(X)|-|R(S)|. (Embedding identifies original states.)
- Realized generative gain G(i)=|R(S')\i(X)|.
- Created-state count C(i)=|X'\i(X)|.
- Total reachable gain D(i)=|R(S')|-|R(S)|=A(i)+G(i).
- Latent creation L(i)=C(i)-G(i).
- Efficiency E(i)=D(i)/cost(i) when cost(i)>0; undefined at zero cost.
- Birth signature B(i)=(A(i),G(i),L(i)).
- Full natality signature N(i)=(A(i),G(i),C(i)).
- Reachability horizon H(S)=X\R(S).
- Generative frontier: Pareto nondominated signatures among admissible interventions under budget.

## D. Propositions and proofs
P1 (nonnegativity). A,G,C,L>=0 and G<=C. Proof: transition preservation makes i(R(S)) a subset of R(S'); all terms are set cardinalities of differences.
P2 (conservation accounting). D=A+G and C=G+L. Proof: partition X' into i(X) and its complement, then partition new states into reachable and unreachable.
P3 (compositional additivity). For S0 -i-> S1 -j-> S2, let K(i)=|R(S1)|-|R(S0)|. Then K(j∘i)=K(i)+K(j). Likewise C(j∘i)=C(i)+C(j). Proof: telescope cardinality differences, and injections preserve cardinalities. WARNING: this does not say A or G are individually additive.
P4 (old/new conversion). In a two-stage composition, a state newly created at stage 1 but only reachable at stage 2 is counted as stage-2 accessibility gain relative to S1, while counted as realized generative gain relative to S0. Therefore G(j∘i) need not equal G(i)+G(j). Proof: example below.
P5 (invariance). N(i) is preserved under commuting isomorphisms of source and target. Proof: commuting bijections preserve images and reachability.
P6 (zero natality despite structural change). Adding a transition between two already reachable states may change T without changing N. Hence N is not a complete invariant of transition-system extensions.
P7 (induced-extension counterexample). Adding an edge between two old vertices violates inducedness but remains an injective transition-preserving extension. Thus inducedness must not be silently assumed for graph edge augmentation.
P8 (monotonicity of total reachability). For composable extensions, |R(S0)|<=|R(S1)|<=|R(S2)|. Proof: image of each earlier path persists.

## E. Exact counterexample to naive additivity of G
S0 has X0={s}, T0=empty.
S1 adds isolated vertex b, X1={s,b}, T1=empty: G(i)=0, C(i)=1.
S2 adds edge s->b without new vertices: G(j)=0, A(j)=1.
But G(j∘i)=1. Hence realized generation is NOT additive under composition, while total reachable gain and creation count are additive. This is a mathematical bookkeeping phenomenon, not yet novel research.

## F. Geometry beyond counting: future testable objects
For a fixed S and declared admissible extension family M, define the set of achievable signatures Q_B(S)={N(i): i in M, cost(i)<=B}, a finite subset of N^3. Define its Pareto frontier by the usual coordinatewise order. The **birth polytope** conv(Q_B(S)) subset R^3 is a legitimate convex-geometric object, but it may be trivial and is not claimed new.
Possible next theorem target: characterize which integer triples (A,G,C) are realizable under specific local generative rules, and determine computational complexity of their Pareto frontier. Without fixed rules, such statements are vacuous.

## G. Scientific safeguards
- 'Creation' means new states relative to an explicit embedding.
- Standard category-theoretic, graph rewriting and transition-system literature must be compared.
- No general differential curvature or geometric dimension is defined.
- Do not call this a novel mathematical field until a substantive theorem beyond existing theory is established.
