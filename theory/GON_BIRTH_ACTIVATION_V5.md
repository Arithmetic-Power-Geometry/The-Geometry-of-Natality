# Geometry of Natality (GoN): Birth–Activation Calculus, V5
Status: mathematically specified candidate model; no established priority over graph-rewriting or network-design literature.

## 1. Model
A rooted directed graph G=(V,E,s) is given. A finite labelled catalogue of actions I is given. Each action a has a nonnegative integer cost c(a) and contributes a finite set of labelled new vertices B(a) and directed edges E(a). Labels are globally consistent: the same new vertex may be introduced by one action and connected by another. A feasible action set F is **dependency-closed**: if an action refers to a new vertex, its creator action must belong to F. The resulting graph has vertices V union union_{a in F} B(a) and edges E union union_{a in F} E(a). Actions never delete original vertices or edges. The cost is sum c(a).

Let R0=Reach_G(s), RF=Reach_(G[F])(s).
Accessibility A(F)=|(RF intersect V)\R0|.
Realized generation G(F)=|RF\V|.
Creation C(F)=|V_F\V|.
Total realized natality D(F)=A(F)+G(F).
Budgeted GoN potential Q_B=max{D(F): F dependency-closed, sum c(a)<=B}.

## 2. Theorems
V5.T1 (feasible monotonicity). If F subseteq F' are feasible, then RF subseteq RF', so D(F)<=D(F'). Proof: all vertices and edges persist.
V5.T2 (budget monotonicity). Q_B is nondecreasing in B. Proof: every B-feasible set remains feasible at larger budget.
V5.T3 (accounting). D(F)=A(F)+G(F) and G(F)<=C(F). Proof: disjoint partition of RF into old and new states.
V5.T4 (activation threshold). Suppose initially only s exists, and one action 'birth' creates b but no edges, while a second action 'activate' adds (s,b), requires birth, and both cost 1. Then Q_0=Q_1=0 and Q_B=1 for B>=2. Proof: feasible subsets are empty, {birth}, {birth,activate}.
V5.C1. The discrete marginal Q_2-Q_1=1 exceeds Q_1-Q_0=0. Hence budget response need not be discretely concave.
V5.T5 (lack of submodularity even without dependencies). With original vertices {s,a,b}, no edges, two independent edge-addition actions add s->a and a->b. D({first})=1, D({second})=0, D({both})=2, so D is not submodular.
V5.T6 (exact dynamic program for disjoint modules). Suppose m independent modules each consists of a private new vertex b_i and two actions birth_i, activate_i; activate_i requires birth_i; there are no cross-module edges and all initial states are reachable. Let module activation cost w_i=c(birth_i)+c(activate_i), reward r_i>=0 equal to the number of newly reachable states of module i when activated, and no partial activation yields reward. Then Q_B equals the 0-1 knapsack optimum max sum_{i in J} r_i subject to sum_{i in J} w_i<=B. Proof: a positive reward requires both actions in each module, and modules are independent; selecting partial actions never improves reward.
V5.C2. The general GoN birth–activation optimization includes 0-1 knapsack as a special case when arbitrary nonnegative integer costs and rewards are permitted. Thus it is NP-hard in the usual binary encoding (standard reduction); this is not claimed a new hardness result.
V5.T7 (weighted birth frontier). In the disjoint-module model, all attainable (cost,reward) pairs are subset sums of (w_i,r_i); the Pareto frontier is the nondominated subset-sum set. Proof: correspondence in T6.

## 3. Important modeling boundary
For T6, a module reward r_i can be implemented by creating r_i new private vertices as a batch and connecting them from s in the activation action. The creation action must introduce all these vertices and the activation action must connect all of them. Costs may be arbitrary nonnegative integers.

## 4. Comparison to established methods
- Fixed-vertex SCC augmentation is the correct baseline for accessibility-only transformations.
- Dependency-constrained activation is a network-design/knapsack-like model; it is NOT intrinsically a new algorithmic class.
- Graph rewriting and transition-system extension are relevant to state creation.
- Submodular maximization guarantees cannot be applied blindly because complementarity can violate submodularity.
- Compare GoN exact DP with exhaustive action-subset search, standard 0-1 knapsack DP, and integer programming where available.
- Any computational speedup from using knapsack DP instead of brute force is an expected classical advantage, not evidence of a new GoN algorithm.

## 5. Open originality targets
O1: characterize a nontrivial interacting-module action grammar with a new sharp bound.
O2: find a useful invariant stable under admissible rewrites but not reducible to existing SCC/closure signatures.
O3: prove and test a non-obvious approximation guarantee under explicitly restricted generative interactions.
O4: derive a compositional geometry for attainable natality vectors with an operationally justified distance, not a decorative embedding.
