# Geometry of Natality (GoN) V9 — adversarial prior-art audit
Date: 2026-10-18. Verdict: Q1-level novelty NOT established.

## Publisher-confirmed related literature
- Boyd (1993), *Polyhedral results for the precedence-constrained knapsack problem*, Discrete Applied Mathematics 41(3), 185–201, DOI 10.1016/0166-218X(90)90053-F. Publisher: https://www.sciencedirect.com/science/article/pii/0166218X9090053F
- You and Yamada (2007), *A pegging approach to the precedence-constrained knapsack problem*, European Journal of Operational Research 183(2), 618–632, DOI 10.1016/j.ejor.2006.10.031. Publisher: https://www.sciencedirect.com/science/article/abs/pii/S0377221706010642
- Espinoza, Goycoolea and Moreno (2015), *The precedence constrained knapsack problem: Separating maximally violated inequalities*, Discrete Applied Mathematics 194, 65–80, DOI 10.1016/j.dam.2015.05.020. Publisher: https://www.sciencedirect.com/science/article/pii/S0166218X15002462
- *Adding Edges for Maximizing Weighted Reachability*, Algorithms 13(3), article 68 (2020): https://www.mdpi.com/1999-4893/13/3/68 . Bibliographic author details not yet independently audited; do not append a guessed BibTeX entry.

## Claim-by-claim comparison
V4 successor-closed reachability signatures: classical SCC and closure reachability.
V5 independent birth-activation modules: classical knapsack.
V6 ancestor-closed tree activation: tree/precedence-constrained knapsack.
V7 SCC contraction: standard preprocessing of cyclic precedence constraints.
V8 mixed discrete synergy: standard set-function interaction and reachability complementarity.
These are useful textbook material but do not support priority claims.

## Distinguishing feature worth investigating
A GoN intervention can introduce states not present in the baseline state universe, with identity-preserving embeddings and staged realization. This is a modeling distinction from fixed-item knapsack, but graph rewriting and evolving transition systems already allow creation. It is NOT a proven novelty result.

## Research gates
1. Explicitly define an application where creation of previously unenumerated states is essential.
2. Compare with graph transformation systems, dynamic network design, PCKP, and edge augmentation, not merely BFS.
3. Establish a nontrivial theorem for constrained creation + realization, or demonstrate empirically meaningful decision gains on held-out tasks.
4. Provide exact optimality certificates for small cases, runtime/memory/scaling and effect sizes on larger cases.
5. Independent mathematical and bibliographic review.
6. Until gates pass: do not claim Q1 readiness or a new mathematical field.
