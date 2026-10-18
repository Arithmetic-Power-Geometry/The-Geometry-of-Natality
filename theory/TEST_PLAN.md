# Pre-registered follow-up testing plan

1. Check T1-T8 by exhaustive enumeration of all loop-free digraphs on n<=3 and sampled n=4.
2. Confirm T8's exact five-vertex pair by independent BFS.
3. Compare P_k for k=0,1,2,3 against brute-force subsets of absent edges on small graphs.
4. Add SCC-condensation dynamic programming and compare time, memory, and exactness.
5. Search for counterexamples with matching degree sequences, SCC-size distributions, and source-reachability counts. Never describe coarse-signature separation as defeating all graph invariants.
6. For k>1, test non-submodularity and complementarity, not just runtime.
7. Publish full raw outputs, deterministic seeds, Python version, machine details, and repeated timing runs.
8. Track every citation in references.bib, append only checked entries, and keep a DOI/URL verification log. Bibliography count is not a quality metric.
