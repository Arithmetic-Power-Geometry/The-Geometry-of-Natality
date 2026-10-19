# Prompt 15 — GROOVE matched-grammar attempt and failure ledger
Date: 2026-10-19

## Candidate target for genuine external equivalence
Use the Prompt 14 bounded dynamic relay grammar, **not** the static Prompt 12 MILP model. The initial host graph has a Root node, Terminal node, and a finite typed Name pool. A state must represent:
- each live relay and its identity;
- permanently used name identities, including names of deleted relays;
- directed relay-to-relay and relay-to-terminal edges;
- shared live-relay capacity;
- forbidden edge-pair NACs and forbidden simultaneously live name pairs.

GROOVE rules must implement `create`, `add-edge`, `remove-edge`, `delete`. `create` must add a relay, mark its name as permanently used, check capacity and live-name NAC. `add-edge` must check its edge-specific NAC at rule application time. `delete` must remove incident arcs but **not** the used-name history. The root reachability goal must be identical to the Python `goal` predicate. Nonnegative action costs require either an explicit graph attribute and GROOVE exploration strategy capable of minimum-cost goal extraction, or export of labelled transitions for independent shortest-path evaluation.

## Actual attempt and blocker
Inspected `.github/workflows/gon-groove-smoke.yml`: it installs official GROOVE Generator, invokes `-h`, clones official GROOVE samples, and runs `attribute-types.gps`. This is **only an installation/sample smoke test**. There is **no** committed GoN-specific `.gps` graph grammar implementing the four actions, history, NACs and costs. Therefore a transition-by-transition bisimulation check against the GoN Python semantics cannot be run. We explicitly **fail** the matched GROOVE equivalence gate rather than equating an unrelated official sample run with validation. No fabricated state counts, costs or runtime.

## Minimal falsifiable equivalence test for Prompt 16
Start with two names, one terminal, capacity one, unit create/link/delete costs, and no forbidden pairs. Compare native and GROOVE successor labels and successor states from empty initial state, then compare reachable goals and minimum cost. Add an action-time edge NAC that forbids relay-to-terminal linking and verify both systems report infeasible. Add permanent used-name history and verify a deleted identity cannot be recreated. Add live capacity and inter-relay edge rewiring; use explicit graph serialization and a state canonicalizer preserving used-name history. Only after exact one-step correspondence should larger performance tests proceed.

**Status: genuine GROOVE equivalence NOT EXECUTED; this is a documented attempted specification and honest blocker.**
