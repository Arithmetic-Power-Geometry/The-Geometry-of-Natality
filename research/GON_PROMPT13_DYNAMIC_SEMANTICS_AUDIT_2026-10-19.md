# Prompt 13 — bounded dynamic rewriting, oracle and manuscript audit
Date: 2026-10-19

## Executable semantic extension
`experiments/research_gate/dynamic_repair_p13.py` adds bounded finite name allocation with permanent used-name history, create, link, unlink, delete, shared live capacity and **action-time** pairwise NAC. States are `State(active,links,used)`. Deletion removes incident links and frees live capacity but does not release a used identity. The terminal recovery predicate requires at least one active relay link per terminal. Nonnegative action costs. No inter-relay rewiring, cyclic prerequisite semantics, globally reusable fresh names, general negative conditions, or full GROOVE grammar are implemented.

## Falsification and proofs
- H1 false: deletion allows identity reuse. A name in `used` remains unavailable even when inactive.
- H2 false: independently valid relay creations can always coexist. A forbidden pair rejects the second creation at action time.
- H3 conditional normalization: in this grammar, with only positive terminal-link goals and pairwise exclusion on live names, some optimal plan contains no delete/unlink actions. For any successful plan, take its final active names and links. Creating only those names (each once) and linking only final links is valid: every intermediate live set is a subset of the legal final live set, so capacity and pairwise NAC hold; its total cost is no greater because omitted operations are nonnegative. This is a standard monotonicity/plan-pruning argument and **not** a novel theorem. It fails with prerequisite effects, destructive terminal guards, or goals depending on intermediate history.

## Independent oracle and scope
The native algorithm uses state-based uniform-cost search and its own action generator. The external NetworkX solver operates on an independently generated state transition graph and computes single-source weighted shortest paths. Matching optimal costs provide bounded differential evidence, not a separately authored GROOVE semantics. Tests cover fixed small pools, terminal sizes, capacities, costs including zeros, pairwise NAC and unreachable instances. Exact tested cell count must be taken from successful CI JSON, not guessed.

## Paper reconstruction
`paper/gon_prompt13_manuscript.tex` is an expanded research-stage technical draft integrating verified Prompt 1–12 results, negative timing results and new Prompt 13 semantics. It is **not a full reconstruction of the original 14-page manuscript**, and bibliography clearance remains incomplete. The paper explicitly refuses unrestricted graph-rewrite or novelty claims.

## Gate status
- Dynamic executable grammar: implemented (restricted).
- Independent exact graph shortest path: implemented via NetworkX, CI pending at report creation.
- Matched GROOVE grammar: not implemented.
- Independent original theorem: not established.
- Full original manuscript reconstruction and verified citations: incomplete.
- PDF visual inspection: pending successful CI and downloaded artifact.

## Prompt 14
1. Read all original manuscript files and Prompt 1–13 artifacts; build a proposition-by-proposition claim traceability matrix with theorem proof status.
2. Extend semantics to *actual* inter-relay rewiring and action-time negative graph application conditions; establish independent operational replay and bounded bisimulation tests against a GROOVE model, or explicitly fail that gate.
3. Stress-test the conditional no-delete/no-unlink lemma against histories, transient goals, cyclic prerequisites and allocation reuse; preserve minimal counterexamples.
4. Implement heterogeneous, variable-cost benchmark and compare native UCS, external NetworkX, static HiGHS MILP where semantics genuinely match.
5. Audit all bibliographic records against publishers and DOIs.
6. Produce a complete 14+ page full manuscript with original verified propositions, algorithms, figures, tables, reproducibility and negative results. Compile, render and inspect every PDF page; verify CI; commit the complete evidence and independent Q1 editorial verdict.
7. If no original contribution is found, position as software verification and reproducibility, not a foundational theory.
