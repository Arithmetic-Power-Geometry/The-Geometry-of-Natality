# Prompt 13 — verified CI and manuscript build
Date: 2026-10-19

- Successful workflow: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39211442172
- Tested commit: `897a87443842b0795a918c3e057640e4f47e0cc5`.
- All steps passed. Python 3.11; external NetworkX 3.4.2; five unit tests passed, including bounded deterministic sweep comparing native UCS with independently constructed state graph and NetworkX shortest paths.
- The sweep loops through **576** valid parameter combinations (name pools 1–3, targets 1–2, valid capacities 0–2, create/link costs 0–2, delete costs 0–1, two NAC choices); duplicate NAC cases at one name are retained as separate parameter cells. Machine-readable JSON is in the CI artifact. Do not interpret as 576 distinct topologies.
- PDF compiled with pdflatex twice, `pdfinfo` and `pdftotext` structural checks passed. GitHub log reports **3 pages**, 201,478 PDF bytes, no `Overfull` warning in workflow log.
- Artifact: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39211442172/artifacts/12168260191
- Artifact ZIP SHA256: `4d6541802395cdf8773cc7b6f180ea7eb52bf4d45b28fbbcbe4ae967e3f4f554`.
- **Visual page inspection NOT completed.** CI text extraction and structural inspection are not a substitute for rendering and inspecting each page.
- This is a three-page expanded research note, not the complete original 14-page manuscript reconstruction.
- **External NetworkX baseline is an independent shortest-path algorithm on an independently enumerated state graph, not GROOVE or an independent graph-rewriting tool.**
- Originality, full bibliography audit, and Q1 readiness remain NOT PASSED.
