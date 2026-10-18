# The Geometry of Natality: formal discrete foundation v1.0

Status: proposed terminology built on established finite directed-graph reachability. All claims below are mathematical deductions, **not priority/novelty claims**.

## 1. Objects and axioms
Let G=(V,E) be a finite simple directed graph (no loops), s in V, and R_G(s) the vertices reachable from s by paths of length >=0. Let A be a specified set of admissible absent edges, and F subseteq A. Write G+F=(V,E union F).

A1 (finite universe): V is finite and s belongs to V.
A2 (path semantics): reachability is the reflexive transitive closure of E.
A3 (admissible transformation): adding F preserves V and all existing edges.
A4 (budget): allowed additions satisfy |F|<=k, for k>=0.
A5 (observability): compare transformations using reachable sets and their cardinalities; this is a modelling choice, not a law of nature.
A6 (structural invariance): graph isomorphisms mapping s to s' and A to A' preserve all numerical natality quantities.

## 2. Definitions
D1. Natality gain: g_G,s(F)=|R_(G+F)(s) \ R_G(s)|.
D2. Natality potential: P_k(G,s;A)=max_{F subseteq A, |F|<=k} g(F).
D3. Natality profile: (P_0,...,P_|A|).
D4. Natality horizon: H_G(s)=V\R_G(s) (unreachable vertices).
D5. Natality saturation: P_k=|H_G(s)|.
D6. Natality synergy: S(F1,F2)=g(F1 union F2)-g(F1)-g(F2)+g(F1 intersect F2), for admissible F1,F2.
D7. Source-rooted natality equivalence under A: two systems are equivalent to budget K if their gain profiles agree for all 0<=k<=K. This is weaker than graph isomorphism.
D8. Unrestricted potential: A is all absent non-loop directed edges. Unless stated otherwise, this is the default.

## 3. Results with proofs
T1 (monotonicity). F subseteq F' implies R_(G+F)(s) subseteq R_(G+F')(s), hence g(F)<=g(F'). Proof: every old path remains a path after adding edges.

C1. 0=P_0<=P_1<=...<=|V|-|R_G(s)|. Proof: T1 and definition of P_k.

T2 (single-edge formula). If u in R_G(s), v not in R_G(s), then g({(u,v)})=|R_G(v)\R_G(s)|=|R_G(v)|. Proof: an augmented path first leaving R_G(s) must use the new edge (u,v); after that it follows old edges. No old path from v can reach R_G(s) and then escape to another previously unreachable vertex (otherwise that vertex would already be reachable from s). Thus the new vertices are exactly R_G(v).

C2. Under unrestricted additions, P_1=max_{v notin R_G(s)}|R_G(v)| when H is nonempty; P_1=0 otherwise. Proof: any useful new edge must leave the originally reachable set and enter its complement; edges elsewhere cannot enlarge reachability with one addition.

T3 (budget bound). 0<=P_k<=|H|, and P_k<=k P_1 for unrestricted additions. Proof: take an optimal F, and follow reachable vertices from s in G+F. Every newly reached vertex is reachable from the head of some added edge after a path containing its last added edge. Each such head has original reachability at most P_1, so the new vertices are contained in the union of at most k original reachability sets. (For restricted A this inequality need not hold relative to restricted P_1.)

T4 (saturation with unrestricted additions). If H is nonempty, P_|H|=|H|. Proof: add one edge from s to each initially unreachable vertex.

T5 (isomorphism invariance). A source-preserving digraph isomorphism that maps A bijectively to A' preserves the gain of each corresponding F and thus every P_k. Proof: the map carries directed paths bijectively to directed paths.

T6 (non-submodularity). g is not generally submodular. Counterexample: vertices {s,a,b}, no edges; additions e1=(s,a), e2=(a,b). Then g(empty)=0, g({e1})=1, g({e2})=0, g({e1,e2})=2. Thus the marginal contribution of e2 increases from 0 to 1 when e1 is present. This violates diminishing returns.

T7 (non-additivity). With the same example, g({e1,e2})=2>g({e1})+g({e2})=1. Therefore complementary transformations exist.

T8 (same reachability count and edge count, different natality potential). Let V={s,1,2,3,4}. G_A has edges 1->2, 2->3, 3->4. G_B has edges 1->2, 2->1, 3->4. In each graph s is isolated, |E|=3 and |R(s)|=1. But P_1(G_A,s)=4, whereas P_1(G_B,s)=2. Proof: T2 and enumeration of original reachability sets. This distinguishes these coarse statistics, **not full graph topology or all existing invariants**.

C3. The pair in T8 shows that (|V|,|E|,|R(s)|) is insufficient to determine P_1.

## 4. Cautions and open problems
- The unrestricted single-edge objective is a classical reachability quantity; T1-T8 should not be advertised as unprecedented results.
- T3's k*P1 bound depends on unrestricted edge additions and is intentionally stated with that condition.
- GoN cannot distinguish isomorphic graphs or graphs with identical full rooted reachability structures under identical action models merely by renaming an invariant.
- Open O1: characterize P_k using SCC condensation and derive nontrivial computational bounds.
- Open O2: find pairs matching increasingly strong baseline signatures (in/out-degree sequences, SCC-size multisets, spectra, etc.) but separated by P_k.
- Open O3: study restricted actions and intervention costs, where structural complementarity is strongest.
- Open O4: compare exact solvers and heuristics for k>1, avoiding false claims of novel algorithms.
- Open O5: define a genuinely new, operationally meaningful invariant not reducible to standard reachability augmentation.
