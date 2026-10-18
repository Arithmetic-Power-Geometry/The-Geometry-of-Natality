# GoN research reset — stop the version loop
Date: 2026-10-18. Status: NOT Q1 READY. This is a decision document, not GoN V16.

## Diagnosis
V1–V15 have largely alternated between restating classical graph/knapsack/observation properties, running small exact checks, and repeating a negative Q1 verdict. More toy experiments alone will not close the novelty gap. No further numbered theory version should be issued without passing a novelty gate.

## What we actually have
- V1: rooted reachability and grouped BFS, with 1,000 toy-instance exact matches and one unreplicated timing comparison.
- V2–V4: SCC condensation, compositional accounting, successor-closed realizability.
- V5–V7: independent, tree and cyclic prerequisite activation, reducible to known knapsack/closure models.
- V8: reachability complementarity/redundancy via discrete mixed differences.
- V9: targeted precedence-knapsack and edge-augmentation prior-art audit.
- V10–V14: revelation, creation, observational equivalence, identity and storage bounds, mostly elementary counting.
- V15: explicit equal-degree cospectral DAGs with different rooted reachability; standard reachability is already a stronger distinguishing statistic.
None of these establishes a new field, an original optimization algorithm, or a Q1-level contribution.

## One proposed research question, not a result
**Adaptive generative intervention under local rules and incomplete action catalogues (AGI-LR).**
An agent initially sees a finite rooted directed graph and a finite set of enabled rewrite actions. Executing an action may create a new vertex and expose additional enabled actions. A fixed cost budget limits execution; rewards depend on *newly reachable created states*. A policy selects actions from the currently observed catalogue. The environment grammar and oracle must be specified before solving.

The central falsifiable question: Is there a restricted and application-relevant grammar for which a GoN-specific invariant or algorithm yields a provable guarantee or a reproducible decision advantage over established online planning / graph rewriting / exact mixed-integer baselines? **Unknown.** If the grammar reduces to known stochastic planning, precedence-constrained knapsack or graph rewriting, explicitly record the reduction and reject novelty.

## Four stop/go gates
G0 (definition): write a machine-checkable grammar, observability, action costs, rewards, horizon and feasibility. No claims until semantics are complete.
G1 (prior art): compare with graph transformation, stochastic/adaptive planning, online exploration, precedence-constrained knapsack and influence maximization; record explicit overlaps and bibliographic evidence. If equivalent, stop novelty claim.
G2 (theorem): formulate one nontrivial conjecture and attempt both proof and adversarial counterexamples; independently verify proof. No new V-number just for an elementary corollary.
G3 (evidence): implement exact oracle and at least two established baselines; run held-out seeds, non-toy scaling, runtime/memory/quality with uncertainty and reproducible artifacts.
Q1 manuscript GO only if a meaningful contribution survives G0–G3 and independent review. Otherwise pivot to a foundations book or a more modest methods note.

## What must not be done
- No claims of Q1 achievement from a theorem count, test count or repo activity.
- No fake performance improvements, synthetic citations, or citation-count targets without relevant sources.
- No treating a stronger observation model as a novel algorithm.
- No conflating state birth with revealing a fixed hidden catalogue.
- No new V16/V17 unless a substantive novelty gate passes.

## Immediate next executable milestone
Create AGI-LR formal specification and an exact finite-instance oracle, then benchmark against a general-purpose state-space planning baseline on the **same** observations and budget. First seek counterexamples to any alleged advantage. If all results match classical baselines, report this as a negative result and stop.
