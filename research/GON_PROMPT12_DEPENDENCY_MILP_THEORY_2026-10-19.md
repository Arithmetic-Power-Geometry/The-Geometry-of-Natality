# Prompt 12 — richer creation-dependent repair and external MILP verification
Date: 2026-10-19

## Semantics and boundary
New *separate closed grammar*: root, two or more isolated terminal nodes, candidate fresh relay templates. Each relay has an integral nonnegative creation cost, a terminal coverage set, and a set of mandatory previously indexed prerequisite relays (acyclic dependency DAG). Selecting a relay creates a vertex, edges from each prerequisite relay to it (or root to it if no prerequisites), and edges from it to its terminals. All required terminals must be root-reachable. A shared integer **capacity counts created relays**. A negative application condition forbids specified relay pairs from coexisting. Each relay can be created once; no deletion, dynamic name identity, arbitrary global negative guard, cycles or preexisting network edges. The capacity is a shared creation-slot budget, **not an implemented globally fresh name allocator**. This is not a full graph-transformation system.

## Three falsifiable claims and counterexamples
- **C1 FALSE:** Choose the cheapest relay that covers a terminal. A cost-1 terminal relay requires a cost-5 predecessor, whereas an independent cost-3 terminal relay is cheaper overall. Optimal cost 3.
- **C2 FALSE:** Adding another relay template always strictly improves optimal repair cost. Adding an expensive duplicate to a cheaper feasible option leaves the optimum unchanged.
- **C3 FALSE:** Adding a selected relay to a feasible repair always preserves feasibility. A negative pair guard forbids simultaneous selection of two relays, so selecting both is invalid although selecting the first alone reaches the goal.

## Surviving conditional equivalence theorem (standard)
For a selected relay subset `S` closed under all prerequisite relations in the acyclic index ordering, every selected relay is root-reachable by induction on its index: relays with no prerequisites have a root edge, and each other selected relay has at least one incoming edge from its selected predecessors. A terminal is root-reachable iff it belongs to at least one selected relay's coverage set. Thus the repair objective is exactly the 0-1 integer program
```
min sum_i cost_i * x_i
s.t. sum_{i:t in cover_i} x_i >= 1      for every terminal t
     x_i <= x_j                         for every prerequisite j of i
     sum_i x_i <= capacity
     x_a + x_b <= 1                      for every forbidden pair (a,b)
     x_i in {0,1}.
```
Both directions hold: a feasible selected subset yields a legal creation order by increasing index, and every legal creation sequence yields a subset satisfying these constraints. **The theorem is a straightforward constraint encoding and is not asserted novel.** If prerequisites are cyclic, or the graph contains additional edges, this formulation is not certified.

## Independent exact baseline
- Internal: enumerate every relay subset, materialize directed graph edges, and run actual root-reachability traversal; check capacity, prerequisites, and forbidden pairs.
- **External:** `scipy.optimize.milp` calling independently maintained HiGHS branch-and-bound/MILP. The external optimizer receives a 0-1 linear constraint model, not the graph traversal implementation. The solver must return a proved optimum; timeouts/unproven results raise errors. Every chosen solution is replayed in graph semantics.
- Deterministic exhaustive test space: 3 relay templates; 2 terminals; 4 coverage masks per relay, 8 acyclic prerequisite patterns, 4 capacities, 2 negative-guard variants = **4,096** models. Includes infeasible cases and nontrivial prerequisites. Costs are fixed at 1,2,3 for this sweep, so **not** a complete cost-domain verification.
- This is a genuinely external mathematical programming baseline, but **not GROOVE**, and not an independently authored graph rewriting semantics. We cannot claim a GROOVE comparison.

## Novelty positioning
Node-weighted Steiner and rooted connected-subgraph integer programming are established. The following public primary sources show substantial prior art:
- Segev, *The node-weighted Steiner tree problem*, Networks (1987), DOI 10.1002/net.3230170102.
- Aneja, *An integer linear programming approach to the steiner problem in graphs*, Networks (1980), DOI 10.1002/net.3230100207.
- Rehfeldt, *Optimal connected subgraphs: Integer programming formulations and polyhedra*, Networks (2022), DOI 10.1002/net.22101.
The present DAG prerequisite + capacity + pairwise conflict formulation combines standard 0-1 constraints with rooted reachability; it has **no demonstrated new structural theorem**. No exhaustive novelty search is claimed.

## Verdict
Conditional equivalence proof: **PASS**. Counterexamples: **PASS**. External semantically matched MILP: **implemented; CI outcome recorded separately**. Originality: **NOT PASSED**. General graph-rewriting external validation: **NOT PASSED**. No selective Q1 submission recommendation.

## Prompt 13
Expand the closed model to dynamic allocation, actual graph rewriting with deletion and inter-relay rewiring, and negative application conditions evaluated at action time. Establish explicit finite transition-system semantics and test a matched GROOVE model (if unavailable, mark the gate incomplete). Formulate falsifiable hypotheses about order sensitivity and history-dependent reachability; develop adversarial minimal counterexamples and independent oracles. Build a pre-registered benchmark with variable costs, cyclic dependencies and infeasible cases. Then reconcile the full original manuscript claim by claim, integrate negative results, and produce a full-length LaTeX draft with auditable proofs, diagrams, baseline tables and verified citations. Do not claim originality or submission readiness without supporting evidence.
