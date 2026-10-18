# Natality V4: exact signature realizability under unrestricted extensions

## Scope
Finite directed graph G=(V,E), root s, original reachable set R, and horizon H=V\\R. An extension may (i) add arbitrary edges between original states and (ii) create exactly c fresh states and add arbitrary edges incident to any states. All original edges persist. We study signatures (a,g,c), where a counts newly reachable old vertices, g counts newly reachable new vertices, and c counts created vertices.

## Theorem V4.1 (exact realizability)
A triple (a,g,c) of nonnegative integers is realizable **if and only if**:
1. 0<=g<=c; and
2. there exists W subseteq H with |W|=a such that for every w in W, R_G(w) intersect H is contained in W.

Equivalently, W is a union of SCCs in the unreachable part of the condensation DAG and is successor-closed in that DAG.

**Necessity:** Let W=R_(G')(s) intersect H. If w in W and w reaches x in G, then x is reachable in G' because original edges persist. If x in H it belongs to W. Also newly reachable created states are among c new states.

**Sufficiency:** For every w in W add s->w (if absent). Add c fresh vertices b_1,...,b_c, and connect s->b_i for i<=g, leaving the other fresh vertices isolated. Since W is successor-closed in the original graph and the only added old-old edges target W, the newly reachable original states are exactly W. Precisely g fresh vertices are reachable. Therefore the signature is (|W|,g,c).

**Important:** The tempting condition 0<=a<=|H| alone is false. If H contains a strongly connected component of size 2 and no other unreachable states, a=1 is impossible under edge-preserving extensions.

## Corollary V4.2 (signature set)
Let Z_G={|W|: W subseteq H is successor-closed}. Then the attainable signatures are exactly {(a,g,c): a in Z_G, 0<=g<=c} when unrestricted additions and arbitrary finite creation are allowed.

## Corollary V4.3 (generative independence)
For fixed c, the attainable g values are {0,...,c}, independent of the attainable old-state gain values Z_G. This independence fails when actions or costs restrict how states and edges may be introduced.

## Proposition V4.4 (SCC-weighted description)
Let D be the SCC condensation DAG induced by SCCs outside R, with vertex weight equal to SCC size. Then Z_G is exactly the set of sums of weights of successor-closed vertex subsets of D.

## Algorithmic implication
Compute SCC condensation and enumerate successor-closed subsets; this is a classical finite-poset/closure enumeration problem. No new complexity classification or speedup is claimed.

## Test evidence
The companion exhaustive script checks every loop-free directed graph with n=2,3,4 (4+64+4096=4164 graphs), and verifies constructive realizability of every successor-closed W combined with c=0,1,2 and g=0,...,c. It is **not** a formal proof of the necessity direction; that is supplied above. Results are stored in experiments/v4.

## Comparison and limitations
- Classical SCC condensation and graph augmentation already imply much of this structure.
- This is a precise and falsifiable theorem, not a claim of priority.
- Performance comparisons need independent classical baselines and explicit cost/action grammars; this experiment tests correctness only.
- No Q1-readiness claim follows from this result alone.
