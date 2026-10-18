# Geometry of Natality (GoN) V8 — complementarity and activation geometry

**Status:** exact formal analysis and falsifiable baseline, not an established novel result.

## 1. Birth–activation action systems
Fix a finite rooted directed graph (V,E,s). Each action a has a globally identified set of created vertices B_a and added arcs E_a, with a prerequisite set P_a. An action set F is feasible when every selected action's prerequisites are selected and every arc endpoint is in V union B_F. Original edges are preserved. Define D(F)=|Reach_(G[F])(s)|-|Reach_G(s)|. For actions with no prerequisites and no births, all subsets are feasible and the usual set-function definitions apply.

## 2. Pairwise GoN synergy
For a feasible context F and actions a,b with F, F+a, F+b and F+a+b feasible, define
sigma_F(a,b)=D(F+a+b)-D(F+a)-D(F+b)+D(F).
Positive values signify complementarity; negative values signify redundancy. The definition is a discrete mixed difference, standard in set-function analysis. It is not itself a novel mathematical invariant.

## 3. Theorem V8.1: path completion can produce unbounded positive synergy
For every integer m>=1 there is a rooted directed graph and two independent edge-addition actions a,b with sigma_empty(a,b)=m.
Construction: original vertices {s,u,v_1,...,v_m}; original edges u->v_i for every i. Action a adds s->u; action b adds s->v_1? This would yield negative interaction, so instead use an intermediate x and choose a:s->x, b:x->u, with original edges u->v_i. Then D(a)=1, D(b)=0, D(a+b)=m+2, so sigma=m+1. For exact m, use m-1 downstream vertices (m>=1), giving sigma=m. Proof by explicit reachability counts.
Consequence: a uniform submodularity or bounded-synergy assertion cannot hold for unrestricted edge actions.

## 4. Theorem V8.2: arbitrary negative synergy
For every m>=1, take m isolated original vertices v_1,...,v_m, with original arcs v_1->v_i for i>=2. Actions a and b are *distinct* admissible actions both adding s->v_1 (duplicate physical edge). Then D(a)=D(b)=D(a+b)=m, giving sigma=-m. If actions must add distinct edges, replace b by s->v_2 and add arcs v_2->v_i for i!=2; each independently reaches all m vertices, and sigma=-m. Thus redundancy can be arbitrarily large.

## 5. Theorem V8.3: synergy bounds
For any feasible context and independent actions, monotonicity gives D(F+a+b)>=max(D(F+a),D(F+b)). Therefore sigma_F(a,b)>=-min(delta_a,delta_b), where delta_a=D(F+a)-D(F) and delta_b likewise. Also sigma_F(a,b)<=D(F+a+b)-D(F). Proof: rearrange the mixed difference and use nonnegative marginals.

## 6. Counterexample: dependence matters
When b requires a, the set F+b may be infeasible and sigma_F(a,b) is undefined under the four-corner definition. Do not silently evaluate infeasible counterfactuals. For prerequisite models, either use feasible joint increments or an explicitly stated closure operator.

## 7. Computational implications
- A classical greedy algorithm for monotone submodular maximization cannot inherit its approximation guarantee without additional hypotheses.
- The same synergy can be computed by four ordinary reachability queries. This is not evidence of an algorithmic speedup.
- A future GoN-specific contribution needs a structural classification of sign/magnitude under constrained action grammars, a new provable guarantee, or an application in which the birth/activation distinction changes an actual decision.

## 8. Publication assessment
V8 demonstrates precisely where unrestricted reachability has complementarity and redundancy. These phenomena are known in network influence and combinatorial optimization. A targeted prior-art review and strong application baseline are still required before claiming novelty or Q1 readiness.
