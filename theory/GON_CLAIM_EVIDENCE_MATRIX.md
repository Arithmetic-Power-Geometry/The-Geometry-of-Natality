# GoN claim–evidence matrix and red-team ledger
Date: 2026-10-18. Conservative audit of repository documents (not a full independent proof audit).

| Claim family | GoN files | Closest classical explanation | Evidence | Publication status |
|---|---|---|---|---|
| Reachability gain | V1, README | BFS, reachability, edge augmentation | 1,000 toy comparisons | Classical baseline |
| Reachability signatures | V2–V4 | SCC condensation, closure sets | exhaustive small graph checks | Priority unproven |
| Action budget | V5–V7 | knapsack, tree knapsack, precedence closure | toy exact matches | Classical reduction |
| Interaction | V8 | mixed set-function difference | constructive examples | Priority unproven |
| Adaptive revelation | V10–V11 | online exploration, partial observation | toy trace enumeration | Priority unproven |
| Identity capacity | V12–V14 | pigeonhole principle, register reuse | finite enumerations | Elementary |
| Degree/spectrum separation | V15 | rooted BFS vs coarse invariants | 4,096 labelled digraph enumeration | Elementary counterexample |
| New GoN algorithm | none established | TBD | no fair comparison | Missing |
| New GoN theorem with demonstrated priority | none established | TBD | no independent prior-art clearance | Missing |
| Q1 readiness | all | venue-specific standards | insufficient | NO |

## Integrity checks before a paper
1. Re-run committed Python scripts in a clean environment and compare generated summaries to committed independent summaries. Prior chat execution of JavaScript is not proof that the Python script ran.
2. Confirm all bibliographic DOIs and metadata against primary publishers.
3. Remove any unqualified 'novel', 'superior', 'Q1 achieved' statements.
4. Keep model-specific restrictions adjacent to every theorem.
5. Record limitations, counterexamples, and failed experiments in the repository.
