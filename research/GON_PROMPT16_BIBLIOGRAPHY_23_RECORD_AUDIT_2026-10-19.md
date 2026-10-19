# Prompt 16 — 23-record bibliography metadata audit and correction ledger
Date: 2026-10-19

CI run: https://github.com/Arithmetic-Power-Geometry/The-Geometry-of-Natality/actions/runs/39216272108 . Complete machine-readable Crossref registration metadata report is retained as the run artifact `gon-prompt16-crossref-23-record-audit` (23 records).

**Automated Crossref audit:** 16 exact/normalized matches; 6 require manual review; 1 DOI not found in Crossref. This is not 23 publisher-level validations. One genuine wrong DOI was identified and corrected in both `paper/gon_prompt15_references.bib` and root `references.bib`.

| Citation key | Automated status | Explanation |
|---|---|---|
| `Rensink2004` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Burch1992` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Emerson2005` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Campbell2021` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Bruni2025` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Rensink2004Comparison` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Newman2003` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Tarjan1972` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Ghasemi2026` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Eswaran1976` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Boyd1993` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `You2007` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Espinoza2015` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Kempe2003` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Nemhauser1978` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Plump1999` | Crossref matched | DOI/title/year/first-author matched audit criteria. |
| `Ghamarian2012` | Manual review | Crossref year 2011 online vs institutional 2012 volume 14 publication; institutional record confirms 2012: https://research.utwente.nl/en/publications/modelling-and-analysis-using-groove-2/ |
| `Ehrig2006` | Manual review | Crossref book entry lacks first-person author metadata; claimed 2006 title/year match; authors require direct publisher validation. |
| `Konig2018` | Manual review | **Confirmed substantive error repaired**: old DOI 10.1007/978-3-319-75396-6_6 pointed to different chapter; corrected DOI 10.1007/978-3-319-75396-6_5. Institutional source: https://research.utwente.nl/en/publications/a-tutorial-on-graph-transformation/ . Remaining author flag due LaTeX accented surname parsing. |
| `Konig2025` | Manual review | Title and year match; first author false flag due accent normalization; publisher-author crosscheck remains. |
| `Adam2026` | Manual review | Title and year match; first author false flag due LaTeX accent normalization; publisher-author crosscheck remains. |
| `Fernandez2005` | Manual review | Crossref abbreviated title; author's own bibliography and King's College record support complete subtitle. https://www.gabbay.org.uk/gabbay_bib.html |
| `GhamarianGraphPassing2012` | Crossref 404, official journal confirmed | Crossref returned 404 (not registered there); official journal site explicitly verifies DOI and title https://eceasst.org/index.php/eceasst/article/view/1948 |

## Interpretation and limits
The six manual flags are **not** six confirmed bad references. They include Unicode surname parsing, an online-vs-print year discrepancy, book-level metadata omissions, and an abbreviated DOI-registration title. The König 2018 DOI was a confirmed incorrect DOI, now corrected. The non-Crossref ECEASST DOI is corroborated directly by the journal site. We did not query the publisher primary page for every one of the 23 references; therefore complete publisher-by-publisher verification remains open.

## Further action
Preserve the DOI correction, rerun the exact committed manuscript PDF and visual inspection, and improve the accent-aware comparison in the audit script if an automated full match is required. Do not silently change printed publication years based on online-first Crossref dates.
