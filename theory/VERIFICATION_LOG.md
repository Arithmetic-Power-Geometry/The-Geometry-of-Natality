# Verification log — 2026-10-18

- Ran an independent local exhaustive enumerator for all 64 loop-free directed graphs on 3 labelled vertices, fixed source 0.
- Confirmed the corrected single-edge formula and unrestricted P1 in **64/64** cases.
- Confirmed explicit 5-vertex distinguishing pair: P1(G_A)=4 and P1(G_B)=2, with equal |V|=5, |E|=3 and initial reachability 1.
- An initial version incorrectly equated |R(v)\\R(s)| with |R(v)|; a counterexample was caught and the theorem and test were corrected in commits befbd24 and f9fddcb.
- The remaining theorems are supplied with written arguments, but **not all have been mechanically checked**.
- Bibliography contains five foundational entries. Publisher or bibliographic index spot checks confirm Tarjan 1972 and Nemhauser et al. 1978; full source-by-source metadata audit remains open.
- No new empirical performance advantage or mathematical priority claim is made.
