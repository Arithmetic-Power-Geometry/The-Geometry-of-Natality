# Prompt 1 — candidate mathematical definitions

**Typed model.** Let M=(S,A,→,c,s₀,G,obs) be a costed, typed identity-bearing transition system. States record a finite typed graph, a persistent used-identity history H, guards, capacities and other resources. Costs are nonnegative. Creation allocates an identity not in H and records it; restoration reactivates an existing identity; rewiring changes edges without allocating a new identity. Infinite identity universes require finite observation quotients or a carefully specified measure.

**Budgeted futures.** Fix observation map obs:S→O and equivalence ≡ on O. Define F_M(s,B)={ [obs(t)]_≡ : an admissible path s→*t has total cost ≤B }. Both compared models must use the *same* observations and equivalence. A symmetry quotient must preserve types, protected names, history, guards, costs, and goal/observation semantics.

**Natality gain.** For M₀ obtained solely by disabling creation actions in M₊, N(s,B)=|F_M₊(s,B)\\F_M₀(s,B)| if the quotient is finite. The sets are nested under this assumption, but N(s,B) itself need not be nondecreasing in B: a future may first need creation and later be reached by an expensive no-create route. This is a candidate observable, not a new law.

**Creation-conditioned distance.** d_C(s,o)=inf{cost(path): path reaches observation class o and contains ≥1 creation action}, inf ∅=+∞. Generally not a metric. Report d_all and d_no-create separately; if no-create is impossible, report essential creation rather than subtracting infinities.

**Interaction.** Fix creation capability set E and shared budget B. V_B(X)=|F_M_X(s,B)| where M_X enables precisely the creation capabilities X⊆E. For i,j∉X define ΔᵢⱼV_B(X)=V_B(X∪{i,j})−V_B(X∪{i})−V_B(X∪{j})+V_B(X). This is the classical second discrete set-function difference; sign is an empirical/mathematical question, not automatically positive.

**Obstruction.** O_G(s,B,X)=1 if no admissible path of cost ≤B reaches goal G with capability set X, else 0. A minimal constraint obstruction is a minimal guard/capacity constraint set whose relaxation changes O_G from 1 to 0; must be compared with existing constraint-diagnosis and correction-set literature.

**Curvature.** No defensible intrinsic geometric curvature has yet been defined. A matrix of second differences is an exploratory interaction descriptor, not curvature absent a geometric invariance principle and prior-art separation.

**Finiteness and negative results.** Zero-cost cycles and infinite names require special handling. Counts of fresh-name labels alone are invalid as possibility expansion; quotienting cannot erase history-sensitive constraints.
