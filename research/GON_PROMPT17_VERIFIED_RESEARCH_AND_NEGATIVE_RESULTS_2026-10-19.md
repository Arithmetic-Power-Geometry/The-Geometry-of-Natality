# Geometry of Natality — Prompt 17 scientific audit and evidence
Date: 2026-10-19
Branch: `research/gon-stage1-20261019`

## 1. Matched three-relay GROOVE grammar
Source: `experiments/research_gate/gon_prompt17_three_relay.py`.
CI: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39217969120 (**SUCCESS**).
Evidence: `gon-prompt17-three-relay-evidence` artifact.

A new graph grammar has three relay names (0,1,2), two terminal identities, live capacity 2, one-shot creation with persistent `used` flags, forbidden cross-links, NACs and link/unlink/delete actions. The initial state has relay 0 live. Two new relays must both serve their respective targets.

- Native state-machine oracle: **28 reachable states, 60 canonical labelled transitions**.
- Independent interpreter of the committed GROOVE XML `.gst` and `.gpr` rules: **28 states, exactly the same 60 canonical labelled transitions**.
- Official GROOVE Generator: **28 states, 64 raw rule-labelled transitions**. Four duplicate rule variants encode identical semantic creation actions under alternative absent-relay NACs. These duplicate transitions are intentionally collapsed by canonicalization.
- Independent native Dijkstra, XML-graph Dijkstra and Bellman--Ford all compute optimal weighted goal cost **12**.
- One optimal plan: `create1, link1, delete0, create2, link2`.
- Action costs: `delete0=4, create1=2, create2=3, link1=1, link2=2`; remaining allowed actions positive.

**External equivalence boundary:** GROOVE executes the real three-relay grammar and confirms state count. The independent XML interpreter proves canonical labelled transition agreement with the native state machine, but no direct export of GROOVE's complete labelled transition graph was compared. GROOVE Generator does not solve the weighted goal problem; the weight result comes from two independently coded shortest-path methods on the independently interpreted grammar. Thus *full GROOVE weighted optimality equivalence is still open*.

### Genuine failure discovered and repaired
The first executable grammar produced **46 GROOVE states and 107 raw transitions**, compared with 28 native states. This exposed missing terminal-type anchors in unlink/delete rules; GROOVE could match the unconstrained terminal endpoint to unintended nodes. Corrected the rules by adding the terminal self-loop type context, then independently re-ran the grammar and confirmed 28 states, 64 raw transitions. Also fixed a **false-green CI**: an initial Python assertion failure was masked by `python | tee` without `pipefail`. The CI now uses `set -euo pipefail`, requires nonempty JSON and asserts the official GROOVE state count. Preserve these negative findings.

## 2. Falsifiable conjecture outcomes
**H1, false:** Every optimal plan for capacity-constrained two-target repair must delete the initially unusable relay before any creation. Counterexample: the cost-12 optimum creates and links relay 1 first, deletes relay 0, then creates and links relay 2. A capacity-two state permits the first creation while the unusable relay remains live.

**H2, conditional and elementary:** If live capacity is k, all k slots are occupied, and a goal requires an additional distinct relay to be created, then some existing relay must cease to be live before that creation, provided creation does not simultaneously evict another relay. Proof: otherwise immediately after creation there would be k+1 live relays, contradicting capacity k. This is a counting invariant, not a novel theorem.

**H3, false as a novelty claim:** Weighted optimality and exact state correspondence alone imply a new graph-rewriting theorem. Counterpoint: bounded state equivalence and Dijkstra/Bellman--Ford are established methods. A genuinely distinctive theorem is not yet established. Do not claim novelty.

## 3. Prior art and publication positioning
The surviving capacity observation is pigeonhole counting. The graph search theorem is classical shortest-path optimality. The restricted relay-cover hardness is classical weighted Set Cover. The canonicalization results are standard finite symmetry reduction. The source should be framed as a **reproducible verification/graph-repair tool study**, not as a new foundational graph-rewriting theory until a precise new result survives prior-art separation.

## 4. Bibliography
Prompt 16 audited all 23 records: 16 automated Crossref matches, six metadata exceptions, one non-Crossref DOI confirmed by the official ECEASST journal; the erroneous König 2018 DOI was corrected. No new publisher-by-publisher verification is claimed in Prompt 17. Retain `research/GON_PROMPT16_BIBLIOGRAPHY_23_RECORD_AUDIT_2026-10-19.md` as the controlling ledger. Open: original publisher-level crosschecks for flagged records.

## 5. External datasets
**No independent real operational network repair trace was obtained, frozen or benchmarked in Prompt 17.** Experiments are explicitly synthetic and bounded. No fabricated provenance, live-network failure trace or claimed real-world performance improvement.

## 6. Editorial readiness
**74/100 — major revision; not Q1 submission-ready.** Improved external grammar scale, canonical semantic comparison and falsification. Still missing: GROOVE-exported transition graph and cost-matched solver; real trace; distinctive theorem; publisher-level flagged citation checks. Production gate must be independently rechecked on the newly integrated manuscript source before freezing.

## 7. Prompt 18 if requested
Only pursue a direct export and comparison of the official GROOVE transition graph, independent cost-preserving simulation or GROOVE-based cost solver, and one genuinely testable structural claim; acquire real traces only if provenance is established. Rebuild and inspect the exact committed integrated PDF; do not invent new results or repeat the original 14-page reconstruction.
