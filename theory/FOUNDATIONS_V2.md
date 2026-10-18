# The Geometry of Natality — foundational architecture v2.0
Status: candidate mathematical research framework; no novelty claim established.

## Scope
Layer I: accessibility changes on a fixed directed graph.
Layer II: changes to graph structure and admissible actions.
Layer III: generative extensions of the underlying state space.
These layers are different mathematical objects; do not conflate them.

## General model
A natality system is (X,T,A,c,O), where X is a finite set of states, T subseteq X×X is a transition relation, A is a finite set of labelled interventions, c:A->R_>=0 is a cost, and O maps each reachable-state set to an observation. Each intervention set F determines an extended system (X_F,T_F) with a canonical injection i_F:X->X_F; assume consistency of injections for nested F when making monotonicity claims.

Axiom N1: every system has a distinguished initial state s in X.
N2: for each admissible F, a finite system (X_F,T_F) and injection i_F exist.
N3: intervention outcomes are evaluated using the reachable states from i_F(s).
N4: if F subseteq F', injections X_F->X_F' commute and preserve transitions (only under *monotone natality*).
N5: comparison of genuinely created states requires a declared identity embedding; otherwise 'newness' is representation-dependent.
N6: observation O and admissible intervention family must be declared before comparisons.
N7: cost budget B restricts F to sum(c(a):a in F)<=B.
N8: isomorphism of all structured data preserves all observables by definition.

Definitions:
- Accessibility gain: newly reachable states that belong to the embedded original X.
- Ontic creation count: |X_F\i_F(X)| (all newly created states, whether reachable or not).
- Realized generative gain: |R_F(i_F(s))\i_F(X)| (newly created and reachable states).
- Reachability horizon: original unreachable states.
- Natality vector: (accessibility gain, realized generative gain, total creation count).
- Natality frontier: Pareto maximal natality vectors among interventions within budget.
- Natality profile: optimal scalarized score as a function of budget and declared utility.
- Natality synergy: g(F union H)-g(F)-g(H)+g(F intersect H), for the chosen scalar gain.
- Natality observability limit: any two systems with the same observation under O cannot be distinguished by a statistic that factors only through O.

Proposition G1 (creation bound): 0<=realized generative gain<=ontic creation count. Proof: newly created reachable states are a subset of newly created states.
Proposition G2 (monotone accessibility): under N4 and compatible embeddings, the reachable set embeds into the larger reachable set. Proof: every path remains valid.
Corollary G2a: cardinality of reachable states cannot decrease under N4, though *newly created states* and *accessibility gain* must be tracked separately to avoid double counting.
Proposition G3 (isomorphism invariance): all three natality-vector coordinates are preserved by a source-preserving structured isomorphism. Proof: it bijects original, created and reachable sets.
Theorem G4 (observability impossibility): if O(S)=O(S'), every statistic f=h∘O has f(S)=f(S'). Proof: substitution. Therefore claims of distinguishing identical complete observations are logically impossible.
Counterexample G5 (accessibility without creation): X={s,a}, T=empty, add (s,a); accessibility gain=1, realized generative gain=0.
Counterexample G6 (creation without realization): X={s}, add isolated new state b; ontic creation count=1, realized generative gain=0.
Example G7 (realized generation): X={s}, add new state b and edge s->b; realized generative gain=1.
Counterexample G8 (synergy): interventions add s->a and a->b on X={s,a,b}; gain is superadditive on this pair, so standard submodularity cannot be assumed.

## Discrete structural results
Let C(G) be the SCC condensation DAG and C_s the source component.
Theorem S1 (SCC invariance): for fixed-source reachability, reachable original vertices are the union of SCCs reachable from C_s. Proof: reachability within an SCC and across the condensation are equivalent.
Theorem S2 (minimum unrestricted saturation budget): if every vertex is already reachable from s, budget is zero. Otherwise let U be the condensation components not reachable from C_s, and let q be the number of zero-indegree nodes in the DAG induced by U. Exactly q added edges suffice and are necessary to make all vertices reachable from s. Proof: each source of U needs an incoming added edge or it cannot be reached; connect s to one representative of each such source, and DAG reachability covers U.
Corollary S2a: P_k=|V\R(s)| for all k>=q.
Theorem S3 (one-edge weighted condensation): with unrestricted edges and fixed source, P_1 equals the maximum total weight of previously unreachable SCCs downstream of a single unreachable SCC, weights being SCC cardinalities. Proof: apply the single-edge reachability formula and SCC contraction.
Proposition S4 (coarse-signature separation): the two five-vertex examples in FOUNDATIONS.md share |V|, |E| and |R(s)| but differ in P_1. This does NOT distinguish complete SCC condensation, spectra or all graph invariants.

## What has NOT been proved
- A new theorem not already present in augmentation/reachability literature.
- Any impossibility of reducing this model to established graph theory.
- New computational complexity bounds.
- A well-defined curvature, dimension, or manifold geometry for generative natality.
- Superiority to SCC-based classical baselines.

## Research gates before paper
Gate A: exhaustively validate S2 and S3 on small graphs and independently audit proofs.
Gate B: compare against SCC condensation, degree sequence, spectra, transitive closure and budgeted augmentation.
Gate C: define a generative intervention calculus with composition and a nontrivial structural theorem.
Gate D: verify references and novelty through a targeted systematic literature search.
Gate E: run preregistered experiments with complete raw data, environments, tests and uncertainty.
