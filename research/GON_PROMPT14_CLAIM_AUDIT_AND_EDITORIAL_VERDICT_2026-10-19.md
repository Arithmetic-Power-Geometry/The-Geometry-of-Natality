# Prompt 14 — adversarial claim audit, dynamic rewiring and manuscript reconstruction
Date: 2026-10-19

## Source provenance
Read repository `paper/GoN_Cost_Optimal_Repair_Planning_DRAFT.md`, Prompt 10 claim audit and Prompt 13 dynamic report, plus prior Prompt 1–13 evidence as summarized in the research reports. The extant working draft has two proved standard propositions, two implemented algorithms, and unfilled proposed figures/tables. Earlier original PDF was reported as 14 pages, six propositions, four algorithms, four figures, eight tables and 23 references, but their full corresponding texts were **not recovered**. We therefore cannot claim a complete line-by-line audit of that original PDF or all 23 bibliographic records.

## Claim-evidence matrix
| Claim | Verdict |
|---|---|
| Exact finite UCS with complete history key | Standard, conditional; tested Prompt 3 |
| General graph rewriting optimality | NOT established |
| Exact orbit quotient for equivariant grammar | Prompt 2/4 bounded; identity-sensitive counterexample |
| Independent-product decomposition | Prompt 5 conditional; shared cap cost 2 vs 4 |
| Greedy cheapest restart | False, Prompt 6 |
| Standard savings exchange formula | True conditional, not novel |
| Frozen 72 synthetic benchmark, 1440 isolated trials | Prompt 7–9 CI evidence |
| General quotient speedup | Contradicted on tested small cells, -3.851ms plain-minus-quotient |
| Relay-creation Set Cover reduction | Prompt 11 standard |
| Static prerequisite MILP | Prompt 12 4096 bounded exact external HiGHS cases |
| Dynamic action-time NAC and deletion | Prompt 13 576 bounded cells |
| Inter-relay rewiring, persistent name history and action-time edge NAC | Prompt 14 new executable grammar; 320 bounded cells independently checked locally |
| Matched GROOVE graph grammar | NOT implemented |
| Novel foundational theorem | NOT established |
| Real network field validation | NOT done |
| Full original 6-proposition/4-figure/8-table reconstruction | NOT complete |
| Independently audited all 23 original references | NOT done |

## Prompt 14 semantics
Finite relay names 0..n-1, live set A, permanently allocated history H, directed edges E between live relays or from a live relay to terminal t. Root is attached to relay zero when live. Actions: create unused name, add allowed edge, remove edge, delete live relay and incident edges. Creation checks live capacity and pairwise live-name exclusion; edge insertion checks a negative forbidden-edge set at application time. Deletion does not clear H. Each action has nonnegative cost. No unrestricted GROOVE semantics.

## Falsifications
- H1: name recycling after deletion is false in permanent-H grammar.
- H2: syntactically possible relay arc can always be inserted is false with forbidden-edge NAC.
- H3: delete/unlink elimination is universally valid is false when the goal requires a name to have been created and later deleted. Example: initial A=H=empty; create relay 0, then delete it yields A=empty,H={0}; empty plan cannot achieve this history-sensitive goal. Earlier normalization proof applies only to monotone terminal-reachability goal and downward-closed live guards.

## External baseline
Prompt 14's NetworkX Dijkstra runs on a **separately generated** explicit finite state graph, not on the native action generator. Local check: 320 parameter cells, 208 unreachable, zero cost disagreements. This is external graph search, **not a matched independent GROOVE rewriting grammar**. Prompt 12 external HiGHS MILP applies to a different static grammar; it is not directly comparable to this dynamic grammar.

## Manuscript
Committed `paper/gon_prompt14_manuscript.tex` is an expanded evidence-bounded manuscript. A separate local 4-page PDF rendering was compiled with pdflatex twice and every page rendered and inspected, with no overfull boxes after link shortening. The local PDF is a separately composed research reconstruction, not byte-identical to the committed GitHub TeX; GitHub CI will compile the committed version. **Neither constitutes a complete original 14-page restoration**. Journal submission is not cleared.

## Independent editorial verdict
Research-stage readiness **58/100** (subjective editorial score, not journal acceptance probability). Methodological honesty and bounded oracle verification are strong; novelty, external semantic baseline, field validation, and full bibliographic clearance are inadequate. Major revision. Do not submit to selective Q1.

## Prompt 15
1. Recover the complete original PDF/TeX and bibliography, or explicitly confirm unavailable artifacts. Build a line-level theorem/algorithm/figure/table/citation traceability matrix.
2. Implement a real GROOVE grammar for the same finite dynamic relay instances, verify one-step transition bisimulation, action-time NAC and costs, and independently reproduce minimum repairs. If GROOVE cannot be run, mark the gate failed.
3. Search for distinctive falsifiable structural theorems that survive prior art and history-sensitive counterexamples; otherwise recast as verification/reproducibility software paper.
4. Pre-register a heterogeneous variable-cost benchmark with larger state spaces, independent topology hashes and multi-host repetitions. Include negative results and limits.
5. Independently validate all references against publisher metadata and DOI.
6. Produce the actual full manuscript with complete figures, algorithms, theorem proofs and data availability; compile and visually inspect every page of the **same committed source**.
7. Commit source, PDF, figures, raw evidence, claim matrix and verified CI; independently assess submission readiness and recommend a suitable journal only if gates pass.
