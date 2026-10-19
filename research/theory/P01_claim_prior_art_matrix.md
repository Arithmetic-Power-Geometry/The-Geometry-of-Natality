# Prompt 1 — targeted claim/prior-art matrix

This is an initial literature separation, **not** a comprehensive novelty proof.

| Proposed claim | Existing work and primary anchor | Assessment |
|---|---|---|
| Graph states and creation/deletion rules | Rensink, GROOVE Simulator (2004), https://research.utwente.nl/en/publications/the-groove-simulator-a-tool-for-state-space-generation/ | Graph rewriting and allocation are established. |
| Graph reachable futures | Rensink, Verification Techniques for Graph Rewriting, https://research.utwente.nl/en/publications/verification-techniques-for-graph-rewriting-tutorial/ | Terminal graphs, reachability and behavioral semantics already studied. |
| Fresh-name quotient | Nominal Rewriting with Name Generation, https://nms.kcl.ac.uk/maribel.fernandez/papers/PPDP05.pdf | Name freshness and equivariance are established; history preservation requires proof. |
| Interaction ΔᵢⱼV | Golovin/Krause submodularity survey, https://www.cs.cmu.edu/~dgolovin/papers/submodular_survey12.pdf ; Bach, https://arxiv.org/abs/1511.00394 | Second differences and submodularity are established; natality-specific structural results remain open. |
| Cost-optimal repair | Dijkstra/UCS and the original `prop:ucs` | Classical weighted shortest path. |
| Independent decomposition | Original `prop:decomp` and `prop:footprint` | Classical product decomposition with strict independence. |
| Minimal obstruction | Constraint diagnosis and model-checking counterexamples | Direct primary-source MUS/MCS comparison still required. |
| Natality curvature | Discrete derivative analogy | Not established as curvature; reject unearned geometric claim. |
| Operational external validity | Prompt 17 GROOVE bounded grammar, 28 states | Synthetic finite equivalence is not real operational validation. |

**Research gaps:** dynamic-domain planning and object-creation planning; identity-history-preserving quotient congruence; sign constraints for budgeted interaction; minimal obstruction certificates beyond existing correction-set methods. Do not infer that an unfamiliar label makes the underlying mathematical object new.
