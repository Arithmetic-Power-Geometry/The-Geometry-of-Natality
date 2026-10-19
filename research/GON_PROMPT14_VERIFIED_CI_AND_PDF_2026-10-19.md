# Prompt 14 — verified GitHub CI and PDF build
Date: 2026-10-19
- Successful run: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39212261515
- Tested commit: `841d7d804e6ea6bab32a74063c1fe86d4ec9656b`.
- All CI steps passed: external NetworkX installation, Python compilation, 320 parameter-cell independent state graph comparison, exact JSON assertion, TeX installation, twice pdflatex, pdfinfo and pdftotext, artifact upload.
- GitHub compiled `paper/gon_prompt14_manuscript.tex` PDF: **3 pages**, 201,900 bytes. Log has no overfull warnings. CI artifact ID `12168236768`, ZIP SHA256 `19109b37395f150ae4be78255d1a6ea7ed420e3fb57061ba61ce52a8ac73ce9d`.
- Artifact: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39212261515/artifacts/12168236768
- Separately composed **local** four-page expanded PDF was compiled twice and all four rendered pages inspected; no overfull boxes. It is **not byte-identical to GitHub manuscript**. GitHub PDF was structurally inspected in CI, **not yet visually inspected page-by-page**. Do not conflate these checks.
- Original full 14-page manuscript and its 23 bibliographic records are not reconstructed or fully audited.
- Novelty gate, GROOVE gate and journal-submission gate: **NOT PASSED**.
