# GoN competitor comparison and decision gate (2026-10-18)

This is a **literature-based comparison**, not a performance result for GoN.

| Method | Established capability | Evidence | GoN implication |
|---|---|---|---|
| GROOVE | graph transformations, state-space exploration, isomorphism reduction, CTL/LTL verification | https://groove.cs.utwente.nl/ | GoN cannot claim these operations as novel |
| Bruni & Rensink (2025) | GROOVE reaction-system reachability, causal analysis, model checking; roughly order-of-magnitude improvement over BioResolve on reported workloads | https://doi.org/10.1007/s11047-025-10045-6 | A GoN comparison must include competitive search and causal analysis |
| Hybrid fuzzy PSO + rule composition (2025) | GROOVE-based reachability with search and rule composition; reported reductions against several heuristic comparators | https://www.mdpi.com/2297-8747/30/3/65 | A GoN heuristic needs stronger baselines than BFS alone |
| König et al. (2025) | Counterexample-guided abstraction refinement for generalized graph-transformation systems | https://doi.org/10.1007/978-3-031-94706-3_8 | Abstract state summaries alone do not establish originality |

## Directly observed completed GoN CI results
- Official GROOVE release binary + Generator help: **PASS** (run 39145685509).
- Two independent synthetic workflow-repair oracles agree: **PASS** (run 39147296943).
- Actual workflow-repair translation to a GROOVE `.gps` grammar: **NOT YET EXECUTED**.
- Matched GoN-vs-GROOVE runtime, states, memory and trace correctness: **NOT YET MEASURED**.

## One falsifiable research hypothesis, not a claim
**H1:** A property-preserving GoN repair-specific reduction can improve the number of expanded states or peak memory versus standard GROOVE exploration *without losing any minimum-cost successful repair plan* on previously unseen graph-repair instances.

A candidate reduction must come with: (1) a formal equivalence relation, (2) a proof of property and minimum-cost preservation under explicit assumptions, (3) a nontrivial case where GROOVE does not already apply an equivalent reduction, (4) a real executed matched benchmark including GROOVE and a competitive search method, (5) counterexamples and ablations.

**Reject H1** if its assumptions fail on realistic cases, if its reduction is already covered by prior art, or if the measured advantage disappears under fair baselines.

## Anti-loop policy
No numbered GoN theory revisions, fabricated Q1 scores, unexecuted performance claims, or bibliography-only milestones. The next experimental commit must include a *runnable GROOVE grammar* and captured generator results; otherwise record the specific execution blocker. **Q1-ready: NO.**
