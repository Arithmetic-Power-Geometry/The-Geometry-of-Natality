# GoN reproducibility decision: use official GROOVE baselines, not a fabricated comparison

**Status 2026-10-18: BLOCKED, NOT Q1 READY.** This is a concrete external-baseline acquisition and execution protocol, not another GoN theory version.

## Verified official resources
- GROOVE source and release: https://github.com/nl-utwente-groove/code ; official instructions describe building with `mvn clean package`.
- Official sample graph grammars: https://github.com/nl-utwente-groove/samples ; includes `attributed-graphs.gps`, `conditional-new.gps`, `control.gps`, `counting.gps` and `parameters.gps`.
- Official manual: https://groove.cs.utwente.nl/manual.html ; sections on graph/rule syntax, attributes, control, exploration and verification, checked against version 7.5.3.
- Official project homepage: https://groove.cs.utwente.nl/ .

## Minimal actual baseline protocol
1. Record Java, Maven, operating system, CPU, RAM, exact GROOVE release and sample-grammar commit SHA.
2. Import an unmodified official sample (start with `conditional-new.gps` and `attributed-graphs.gps`) and confirm that the official Generator executes; capture stdout/stderr and exit status.
3. Encode GoN's *existing* synthetic workflow-repair fixture in a separate GROOVE grammar, using valid official rule syntax and typed graph attributes; verify the expected two cost-3 solutions and no cost-below-3 solution.
4. Compare labelled traces and goal predicates with `applications/workflow_repair/independent_audit.py`. Record every mismatch, including differing identity, rule enabling, costs and duplicate states.
5. Only after equivalence passes, collect paired runtime, peak memory, explored states, and goal-quality metrics across held-out real incidents, using identical constraints.
6. If no real data, executable grammar, or new method exists, stop and report **no Q1 evidence**.

## Anti-loop scientific stop
Do not claim a GROOVE speedup from reading documentation. Do not invent `.gps` syntax or imply a conceptual rule mapping was executed. Do not append another finite-state, reachability, capacity or symmetry toy proof. The current fixture is reducible to established graph rewriting. **The GoN algorithmic novelty gate remains failed.**

## Current evidence
Previous local exact enumeration establishes only that the tiny synthetic fixture has two successful minimum-cost plans, each cost 3. No official GROOVE run, paired benchmark, real incident corpus, or new theorem has been demonstrated.

## Decision
Q1-ready: **NO**. Next deliverable is an *executed*, independently reproducible GROOVE grammar with raw run logs, not another research manifesto.
