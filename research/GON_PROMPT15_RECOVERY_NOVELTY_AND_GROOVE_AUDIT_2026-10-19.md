# Prompt 15 — recovered full manuscript, formal gate audit, external baseline status
Date: 2026-10-19

## Major recovery
User Library yielded the complete source `main(20261019-051759).tex` (42,558 bytes), alongside the original 14-page PDF `main(20261019-051755).pdf` (487,802 bytes). Preserved **unchanged** at `paper/original_20261019_recovered.tex`. The original source contains **six propositions, four algorithms, four figures, eight tables**, and cites all **23** entries in repository `references.bib`. No missing citation keys, no uncited bibliography entries, and no duplicate bibliography keys/DOIs were found by local structural checks. Every BibTeX entry includes author, title, year, DOI. **These are structural checks, not publisher verification of each DOI or metadata**.

## Authoritative source
`paper/gon_prompt15_authoritative.tex` is derived from recovered original and adds a post-freeze evidence section, a history-sensitive deletion counterexample proposition, and a reproducibility and limits section. It preserves original propositions/algorithms/figures/tables. Its reference file is root `references.bib`; compile from repository root with Biber. CI builds and renders the **committed** authoritative source.

## Claim-to-evidence audit
| Original item | Status |
|---|---|
| Proposition 1: reachability/cost monotonicity under added actions | Conditional and standard; compare restricted planning graphs |
| Proposition 2: creation-essential recovery | Finite counterexample witness, not general originality |
| Proposition 3: finite UCS optimality | Standard Dijkstra argument; Prompt 3 bounded replay |
| Proposition 4: independent decomposition | Standard product theorem; Prompt 5 certificate, shared cap refusal |
| Proposition 5: conservative footprint certificate | Implemented only for closed independent-component DSL; not arbitrary graph grammar |
| Proposition 6: fresh-name quotient | Requires full equivariance of transitions, costs, goals, history; Prompt 2/4 restricted exact tests |
| Algorithms 1–4 | Exhaustive, UCS, guarded decomposition, orbit UCS; different grammar scopes; no universal graph rewriting proof |
| Figures 1–4 | Source-embedded TikZ diagrams; graphical content not evidence of generality |
| Tables 1–8 | Synthetic fixture, settings, counts and conditional scope; no real field results |
| Original 23 references | Keys complete, DOI fields present and unique; external publisher-level audit incomplete |

## Falsification and originality
Prompt 6's greedy hypotheses failed; standard savings lemma survived. Prompt 11 reduced closed relay creation to weighted Set Cover; Prompt 12 static DAG dependencies correspond to standard binary MILP constraints; Prompt 13/14 dynamic relay rewriting has explicit history and action-time guards but no original complexity or approximation breakthrough. The recovered source itself explicitly disclaims novel calculus or performance superiority. A **history-sensitive counterexample** refutes universal deletion elimination: a goal requiring a name allocated but not live requires create then delete. This is an elementary counterexample, not a novel structural theorem. Novelty gate **NOT PASSED**.

## GROOVE external equivalence: attempted audit, not achieved
Inspected the existing official `.github/workflows/gon-groove-smoke.yml`. It downloads GROOVE Generator and runs its help command and an **official example grammar**. It does not encode the GoN repair actions, goal, action costs, persistent allocation history, or action-time negative guards. Previous sample runs include failures. A genuine GROOVE bisimulation/cost-matched baseline therefore remains **NOT IMPLEMENTED**, and no equivalence or performance claim is made. The external HiGHS MILP and NetworkX checks remain bounded checks of their respective restricted models, not substitutes for GROOVE.

## External validation
Prompt 9: 72 synthetic cases, 36 matched and 36 refusal, 1,440 resource-limited trials, no censored; plain-minus-quotient median -3.851ms on tiny symmetry cases. Prompt 12: 4,096 models matched with HiGHS MILP. Prompt 13: 576 bounded parameter cells matched with NetworkX. Prompt 14: 320 bounded inter-relay rewrite cells matched with independently constructed NetworkX state graph. No real dependency traces, cross-host performance, or general graph rewriting semantics.

## Remaining publication gates
- Publisher metadata verification for all 23 citations, including DOI title/year/authors.
- True semantically matched GROOVE grammar with graph transformation rules, costs and goal extraction.
- New distinctive falsifiable theorem or clear software-verification contribution.
- Larger independently sourced workloads with provenance and meaningful uncertainty.
- Journal-ready integrated interpretation and independent editorial review.

**Editorial readiness: 64/100, major revision (subjective, not acceptance probability).** The score rises primarily because the complete original source has now been recovered; novelty and external validation remain blockers. Do not submit to selective Q1.

## Prompt 16 — focused outstanding gates
1. Use `paper/gon_prompt15_authoritative.tex` as sole authoritative manuscript; do not rebuild from short notes.
2. Independently verify every one of the 23 bibliography entries against publisher/DOI primary metadata; repair any inaccuracies with a dated audit ledger.
3. Build an actual GROOVE `.gps` grammar matching a tiny specified GoN instance, encode costs and terminal goals, and verify one-step transitions against native semantics. Preserve failed experiments and logs.
4. Pre-register and run heterogeneous externally sourced networks with provenance and fair algorithmic baselines; avoid extrapolating from synthetic tests.
5. Investigate a theorem that cannot be reduced to ordinary shortest paths, Set Cover, greedy matroid choice, or independent product decomposition; falsify aggressively.
6. Rebuild the committed authoritative PDF with bibliography, visually inspect every rendered page and correct layout; preserve SHA and CI evidence.
7. Independent journal-readiness assessment. If novelty fails, pivot to a transparent verification/software methods paper rather than claim foundational novelty.
