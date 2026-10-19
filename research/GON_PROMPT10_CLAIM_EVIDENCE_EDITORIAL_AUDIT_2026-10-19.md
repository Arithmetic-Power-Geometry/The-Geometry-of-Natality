# Prompt 10 — independent claim-to-evidence and editorial audit
Date: 2026-10-19

## Reconstruction
Source: `paper/gon_prompt10_reconstructed.tex`. This is a **research-stage short manuscript**, not a complete submission-ready replacement of the original 14-page paper. It preserves exact restricted grammar assumptions and negative findings.

## Claim-to-evidence matrix
| Claim | Evidence | Verdict |
|---|---|---|
| UCS optimal on finite nonnegative graph with complete state key | Standard Dijkstra invariant; Prompt 3 implementation | Standard conditional theorem |
| Exact finite orbit canonicalization | Prompt 2 tests and Prompt 4 independent transition-equivariance checks | Bounded certified grammar only |
| General graph rewrite quotient correctness | No universal proof; trusted role certificate | NOT ESTABLISHED |
| Conservative independence decomposition | Prompt 5 footprint certificate, full UCS comparisons and trace enumeration | Closed DSL only |
| Shared capacity invalidates naive separability | CE-02 strict 2 vs 4 cost gap | Verified counterexample |
| Cheapest absolute restart first is optimal | Prompt 6 counterexample | FALSE |
| Largest positive savings under cardinality constraint | Exchange proof, 80,973 finite checks | TRUE but standard, not novel |
| Frozen synthetic manifest | Prompt 7 72 cells, deterministic seeds and hashes | Verified |
| 36 matched cells, 36 refusal cells | Prompt 8 and 9 independent audit | Verified |
| 1,440 resource-limited trials, zero censored | Prompt 9 CI run 39208415337 and artifact 12166458810 | Verified |
| Quotient speedup | Prompt 9 median plain-minus-quotient -3.851 ms | CONTRADICTED on tested cases |
| Decomposition small timing differences | Prompt 9 +0.743/+0.740/+0.427 ms | Descriptive only |
| Real network validity, matched GROOVE, original structural theorem | No evidence | NOT ESTABLISHED |

## Bibliographic verification
- Hoffmann, Lomonosov, Sitharam: Springer primary record confirms exact title, author names, LNCS 1779 pp 309--324, DOI `10.1007/3-540-45104-8_25`; conference AGTIVE 1999, printed 2000 / online 2003. https://doi.org/10.1007/3-540-45104-8_25
- Crespelle, Drange, Fomin, Golovach: Elsevier primary record confirms *Computer Science Review* 48 (2023), article 100556, DOI `10.1016/j.cosrev.2023.100556`. https://doi.org/10.1016/j.cosrev.2023.100556
- Varró-Gyapay and Varró citation retained from Prompt 6, **not independently reverified in this audit**.
- Existing root `references.bib` and all 23 manuscript references were **not individually verified**. Bibliography clearance incomplete; do not claim otherwise.

## Manuscript production limits
- The short reconstruction is not a complete revision of the original manuscript's 6 propositions, 4 algorithms, 4 figures and 8 tables. It intentionally excludes unsupported claims rather than silently carrying them forward.
- Reconstructed PDF compilation and visual QA require a successful CI artifact and independent page inspection.
- No original, externally reviewed novelty theorem. No external real-world data, coupled graph semantics, or matched GROOVE baseline.
- Estimated selective Q1 foundational-readiness **60/100** (editorial judgment, not acceptance probability). Correctness/reproducibility is stronger than novelty and external validity. Decision: **major revision; do not submit yet**.

## Prompt 11
Develop and test a genuinely distinctive theorem in an explicitly richer creation-enabled graph-repair model; establish relation to graph transformation, planning and symmetry prior art; implement matched GROOVE semantics or a rigorously equivalent external baseline; add heterogeneous externally sourced dependency networks with licenses and provenance; pre-register broader multi-machine experiments; independently verify every bibliography entry; then rebuild a full-length submission manuscript with diagrams, algorithms, theorem proof appendices, uncertainty and reproducibility statements. If no novel theorem survives falsification, position the work as a software verification / reproducibility note instead.
