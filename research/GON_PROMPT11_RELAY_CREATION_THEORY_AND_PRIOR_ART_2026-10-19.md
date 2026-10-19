# Prompt 11 — creation-enabled reachability: falsification, proof, and novelty audit
Date: 2026-10-19
Branch: `research/gon-stage1-20261019`

## Research question
Can a distinctive structural theorem be justified for creation-enabled dependency repair rather than merely reusing standard orbit quotients and independent component decomposition?

## Closed new model
We introduce a **separate**, precisely scoped directed relay-creation grammar. An initial directed graph has a root and `m` isolated terminal nodes. A finite candidate template `i` creates a fresh relay vertex `x_i` and installs arcs `root -> x_i` and `x_i -> t` for each terminal `t` in the template's nonempty cover set `S_i`, at nonnegative integral cost `c_i`. Each template can be chosen at most once. Goal: root reaches **every** terminal. No other old edges, inter-relay arcs, deletion, history, capacity, or identity-sensitive guards. This is not a model of arbitrary GoN rewrites.

## Three falsifiable hypotheses
- **H1 (FALSE):** Greedily create the currently cheapest relay that reaches an uncovered terminal. For two terminals, candidate covers `{0}`, `{1}`, `{0,1}` all cost 1. Cheapest-first deterministic order selects the first two (cost 2); selecting the third alone costs 1. Preserve this counterexample.
- **H2 (FALSE):** Adding a zero-cost relay strictly reduces optimal repair cost. If an existing zero-cost relay already covers the only terminal, a duplicate zero-cost relay does not reduce the optimum below zero. Monotonic nonincrease is valid; strict decrease is not.
- **H3 (TRUE for this closed model, NOT NEW):** For any selected template set `I`, root reaches all terminals iff `union_{i in I} S_i = U`. Therefore the minimum creation cost is exactly **weighted set cover** over `U` and `S_i`.

## Complete conditional proof
Initially each terminal is isolated. A terminal `t` gains an incoming arc only from a created relay `x_i` for which `t in S_i`; each created relay has an incoming root arc. Consequently, a root-to-`t` directed path exists iff at least one selected `S_i` contains `t`. Requiring this for every terminal is precisely the union-cover condition. Creating `I` incurs additive cost `sum_{i in I} c_i`; thus minimizing feasible creation cost is the weighted set-cover objective, in both directions. Given a Set Cover decision instance with universe `U`, subsets `S_i` and integer bound `k`, instantiate these templates with unit costs and ask for a plan costing at most `k`. This is a polynomial-time many-one reduction; membership in NP holds by verifying a selected subset and its union in polynomial time. The decision problem is NP-complete for this restricted grammar, **assuming the classical NP-completeness of Set Cover**. This is a textbook-style reduction, not an originality or priority claim. It also yields an exact `O(2^m m n)` terminal-subset dynamic program up to polynomial factors (where `m` is number of terminals and `n` templates), and an independent `O(2^n n m)` enumeration baseline. These are standard algorithmic techniques.

## Independent executable evidence
- `experiments/research_gate/creation_cover_complexity.py` materializes actual directed root-relay-terminal graphs and checks graph reachability by traversal; exhaustive enumeration of candidate subsets yields one exact oracle.
- The separately implemented subset-mask Dijkstra dynamic program is an independent optimization algorithm (it shares only the typed instance and input validation). For `m=3`, three ordered templates chosen from seven nonempty subsets and each cost in `{0,1,2}`, it checks `7^3 * 3^3 = 9,261` instances, including unreachable cases and zero costs. Tests verify explicit counterexamples, graph semantics, and exact costs.
- **External baseline status:** The independent graph enumeration is a semantically matched in-repository baseline, not GROOVE, NetworkX, or an independently authored external solver. No external graph transformation comparison was performed. We will not mislabel it.
- The 9,261 cases validate finite implementation agreement, not the general theorem by themselves; the proof is above.

## Prior art and novelty
The closed problem is *exactly* weighted Set Cover, and the hardness reduction is an obvious encoding of existing network design/reachability problems. In particular, earlier rooted connectivity augmentation literature already reduces Set Cover to directed rooted edge augmentation. A 2010 Dagstuhl research survey, `Approximating minimum cost connectivity problems`, explicitly discusses such a reduction (Theorem 8.2). https://drops.dagstuhl.de/opus/volltexte/2010/2497/pdf/09511.KortsarzGuy.Paper.2497.pdf
Additional nearby established work:
- Byrka, Grandoni and Jabal Ameli, `Breaching the 2-Approximation Barrier for Connectivity Augmentation: A Reduction to Steiner Tree`, SIAM Journal on Computing, DOI 10.1137/21M1421143: https://doi.org/10.1137/21M1421143
- `Node connectivity augmentation via iterative randomized rounding`, Mathematical Programming, DOI 10.1007/s10107-022-01854-z: https://doi.org/10.1007/s10107-022-01854-z
- Original Prompt 6 bibliography includes earlier graph transformation optimization and graph modification survey results. No exhaustive novelty search or full bibliographic verification is claimed.

**Novelty gate: NOT PASSED.** H3 is an exact and useful model characterization, but is transparently an encoding of Set Cover. It cannot be presented as a novel foundational theorem. No Q1-readiness upgrade is justified.

## Prompt 12
Develop a richer, genuinely creation-dependent repair model with explicit *inter-relay dependencies*, shared name allocation, negative application conditions and multi-target recovery. Before proposing novelty, derive precise connections to directed Steiner network, Set Cover, facility location, and graph rewriting. Pre-register at least three new falsifiable hypotheses, including adversarial counterexample generation and a theorem that is not a restatement of standard set cover, symmetry or separability. Implement a **truly external semantically matched baseline** (e.g. GROOVE with exact rule correspondence or an external MILP solver with verified formulation) and test model-to-baseline equivalence. If no new theorem survives, position the contribution as a transparent verification/software artifact rather than a new mathematical theory.
