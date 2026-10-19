# Prompt 15 — final execution evidence and unresolved PDF gate
Date: 2026-10-19

## Successful recovery and local proof
- Original source: Library `main(20261019-051759).tex`, preserved in GitHub `paper/original_20261019_recovered.tex`.
- Original supplied PDF: Library `main(20261019-051755).pdf`, **14 pages**. All 14 pages rendered as PNG and visually inspected using a contact sheet. No obvious clipped content.
- Original source locally compiled with `pdflatex`, `biber`, `pdflatex`, `pdflatex` and the earlier 23-entry local bibliography: **14 pages**, exit code 0. This local PDF is not byte-identical to the GitHub CI attempt, which uses a mapped bibliography.
- Six original propositions, four algorithms, four figures, eight tables, 23 cited keys recovered. Key compatibility and BibTeX structure audited; not all 23 publisher metadata independently verified.

## Failed CI attempts — do not conceal
- Initial source-integrity run 39212945506 failed because the root repository `references.bib` uses different citation keys (27 entries). Fixed with `paper/gon_prompt15_references.bib` (23 mapped entries).
- Full manuscript CI runs 39213210228, 39213411662, 39213741197, 39214031389, 39214409798 all failed in LaTeX compilation (latest error: `Missing $ inserted` at `\\end{document}`). An integrated post-freeze appendix was reverted to the complete original manuscript to avoid an uncompiled revision, but the GitHub-hosted TeX toolchain still fails. Local same-source compile with original local bibliography succeeded. Exact GitHub cause not isolated; the bibliography metadata mapping and runner TeX environment remain candidates, **not confirmed causes**.
- Therefore **no successful GitHub-compiled authoritative PDF exists** in this stage. The separate source-integrity workflow checks counts and keys but must not be described as PDF CI.

## Scientific gates
- True matched GROOVE grammar and transition/cost equivalence: NOT EXECUTED; see `GON_PROMPT15_GROOVE_MATCHED_GRAMMAR_BLOCKER_2026-10-19.md`.
- Novel structural theorem: NOT ESTABLISHED.
- External field validation: NOT PERFORMED.
- Original bibliography publisher-by-publisher validation: INCOMPLETE.
- Full post-freeze experimental integration into paper: INCOMPLETE.

## Editorial verdict
**64/100, major revision** (editorial judgment only). Strongest improvement: original complete source recovered. Do not submit to selective Q1. Prompt 16 should prioritize CI build reproducibility, real GROOVE semantics and reference verification before further prose drafting.
