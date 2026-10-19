# Prompt 16 — external validation, theorem falsification and publication gate
Date: 2026-10-19

## Scope and source recovery
Authoritative full manuscript source: `paper/gon_prompt15_authoritative.tex`, derived from recovered original 14-page paper. Prompt 16 adds a clearly labelled post-freeze section on bounded external evidence, negative results, and bibliography limitations. The original six propositions, four algorithms, four figures, eight tables are retained.

## 1. Repaired exact GitHub LaTeX/Biber build
The late `Missing $ inserted` error in Prompt 15 was traced to a source-specific bibliography entry `Burch1992` containing `10^{20}` outside math mode in a title. Changed it to `10\\textsuperscript{20}` in `paper/gon_prompt15_references.bib`, commit `ec1ee6ccccb5136f1582f5e017725d6fc72d29d8`. **CI run 39215799174 SUCCESS**: pdflatex, Biber, pdflatex twice, citation integrity, PDFinfo, and page render. Artifact ID **12169293815**; exact artifact PDF SHA256 **8b901bdba50b6c9ca92b42a4e35982b7ac5ab20f1c2ce91b9149b69abb8172d0**, 14 A4 pages, 421580 bytes. All 14 PNG pages downloaded and visually reviewed as a contact sheet; figures, tables, algorithms, bibliography present, no obvious clipping. This was **before** the subsequent post-freeze text integration and is not the final revised PDF. Workflow was extended to commit the compiled PDF to the research branch; first push failed due concurrent commits, and rebase/retry was added.

## 2. Official model-specific GROOVE executable result
`experiments/research_gate/groove_minimal_fixture.py` generates actual `.gst`, four `.gpr` rule files and a GROOVE `.gps` grammar. Rules: create, link, unlink, delete. Permanent `used` identity marker survives delete. One relay name and one terminal, no multi-relay capacity coupling, unit costs. Independently enumerated oracle: **four states, four transitions**. Official GROOVE Generator: **four states, four transitions**, exit code 0. CI run **39216318483 SUCCESS**; initial execution run 39215939756 SUCCESS; full logs, grammar and oracle are downloadable artifacts. This is a successful model-specific external executable check. **Counts alone do not establish transition-by-transition labelled bisimulation or optimal-cost equivalence**, and the grammar is not the full Prompt 14 semantics.


### Second GROOVE grammar: capacity-constrained deletion necessity
Prompt 16 subsequently added `gon_capacity_counterexample.gps`, with **two relay identities, capacity one, persistent used-name history, and a forbidden link for name zero**. Its official Generator exploration reported **four states and four transitions**, exactly the bounded native oracle counts; CI run **39216642551 SUCCESS**. The native unit-cost goal plan `delete(0), create(1), link(1,T)` has cost 3 and the delete-free model is infeasible. This is stronger external structural validation than a sample grammar, but counts alone are not a labelled bisimulation proof. The final manuscript text was updated to disclose both GROOVE grammars.


### Independent labelled transition verification (additional)
The committed `experiments/research_gate/groove_rule_equivalence_oracle.py` parses the actual generated GROOVE `.gst` and `.gpr` XML rule files and interprets context, negative, added, and deleted edges independently of the native oracle. It compared **the complete labelled transition relation** for both bounded grammars against separately specified native state machines: **4/4 states and 4/4 labelled arcs in each grammar**, exact equality. Official GROOVE Generator independently executed both grammars and reported the same counts. **CI run 39216837397 SUCCESS.** This is genuine finite semantic correspondence for fixed-node edge-only graph rules, but not general GROOVE semantics or a weighted shortest-path benchmark.

## 3. Falsified conjecture: delete-free positive reachability
`experiments/research_gate/prompt16_delete_essential_counterexample.py` independently enumerates a two-name, capacity-one, unit-cost instance. Initially name 0 is live, used; its terminal edge is forbidden. Goal: terminal reachability through name 1. Full optimum is **3** with plan `delete(0)`, `create(1)`, `link(1,T)`; delete-free planning is **infeasible**. CI run 39216318483 SUCCESS. This refutes the *unrestricted* conjecture that deletion can always be pruned for positive reachability under resource constraints and action-time guards. It does not refute a monotone delete-free theorem whose assumptions exclude these constraints. The observation is elementary and **not claimed novel**.

## 4. Audit of all 23 bibliography records
Crossref registration metadata audit in `experiments/research_gate/audit_bibliography_crossref.py`; CI 39216272108 SUCCESS, artifact 12169608288. **16 automated matches, 6 manual review, 1 Crossref 404**. The last DOI is confirmed by the ECEASST journal. A genuine wrong chapter DOI for König et al. (2018), `10.1007/978-3-319-75396-6_6`, was corrected to `10.1007/978-3-319-75396-6_5` in source-specific and root bibliographies; verified against University of Twente institutional record. See `research/GON_PROMPT16_BIBLIOGRAPHY_23_RECORD_AUDIT_2026-10-19.md`. No claim of 23 publisher-by-publisher verifications.

## 5. Theorem originality audit
Original propositions: (1) action-set monotonicity; (2) definition-level creation necessity; (3) standard UCS/Dijkstra optimality; (4) independent-product additive optimum; (5) conservative footprint certificate for the product condition; (6) permutation-equivariant orbit quotient. All are useful as rigorous conditional statements but are close to established shortest-path, decomposition and symmetry reduction. Prompt 16's new counterexample exposes an important boundary of pruning but does not constitute a foundational theorem. No demonstrated novel hardness, approximation, parameterized complexity or reduction result.

## 6. External validity and verdict
Static HiGHS 4,096 bounded cells; dynamic NetworkX 320 bounded cells; resource-limited synthetic benchmark 1,440 trials; GROOVE minimal four-state grammar. None are real operational repair traces or a semantically matched GROOVE cost-optimal comparison for full multi-relay model. Distinguish evidence by scope. Editorial rating **72/100 — major revision**. Improvement over Prompt 15 is due to successful full PDF CI, a real albeit tiny GROOVE executable grammar, explicit falsification, and bibliographic correction. Not Q1 submission-ready.

## Remaining gates for Prompt 17, if needed
1. Establish labelled transition and weighted goal-cost equivalence with a nontrivial multi-name GROOVE grammar, not merely equal state counts.
2. Independently source real failure/repair traces with provenance and preregister matched external baseline comparisons.
3. Derive a substantive original theorem with falsification and prior-art separation; or reposition as transparent tool-validation/software methods paper.
4. Complete publisher-level reference validation for flagged records.
5. Freeze the integrated source and verify its **own** exact CI-compiled committed PDF, pages and SHA before submission.
