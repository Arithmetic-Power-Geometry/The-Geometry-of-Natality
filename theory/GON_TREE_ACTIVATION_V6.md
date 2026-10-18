# Geometry of Natality (GoN) V6 — rooted generative activation trees
Status: mathematically derived restricted model; classical tree-knapsack structure; novelty not established.

## Model
Let T=(V,E) be a rooted out-tree with root s. Every nonroot vertex v represents a potential state with nonnegative integer activation cost c(v) and nonnegative integer realized value w(v). Activating v requires activating its parent (root is active at cost zero). Thus feasible activation sets are ancestor-closed and include s. A budget B limits total cost. Maximize total realized value of activated nonroot vertices. This is a restricted generative GoN model, not the full V5 action grammar.

## Axioms
T1 finite rooted out-tree; T2 nonnegative integer activation costs; T3 nonnegative integer vertex values; T4 ancestor-closed feasibility; T5 additive costs and realized values; T6 fixed budget B.

## Definitions
An activation ideal is an ancestor-closed subset containing s. Natality value N(F)=sum_{v in F\{s}} w(v). Budgeted tree potential Q_B=max N(F) over feasible ideals with cost<=B.

## Theorem 6.1 (exact tree dynamic programming)
For each vertex v, define DP_v[b] as the maximum value of an ancestor-closed activated subset of the subtree rooted at v that includes v and costs at most b; DP_v[b]=-infinity if b<c(v). Initialize DP_v[b]=w(v) for b>=c(v). For each child u, update:
DP_new[b]=max_{0<=j<=b}(DP_old[b-j]+max(0,DP_u[j])).
Here max(0,DP_u[j]) represents skipping child u, and -infinity states are ignored. The root has c(s)=w(s)=0. Then Q_B=DP_s[B].

Proof: In a rooted tree, after choosing v, activated vertices from distinct child subtrees are independent except for their budget allocation. Every feasible ideal uniquely decomposes into an optional feasible ideal for each child. The convolution considers all splits; induction on subtree size proves optimality.

## Corollary 6.2
Q_B is nondecreasing in B. The optimal value can exhibit threshold jumps, and marginal increments need not decrease.

## Proposition 6.3 (exhaustive search baseline)
Enumerating all subsets of n nonroot vertices and checking ancestor closure and cost is an exact baseline of O(2^n n). The dynamic program uses O(n B^2) time with naive convolution and O(n B) table storage; complexity is pseudo-polynomial in the binary-encoded budget.

## Counterexample 6.4
A chain s->a->b with c(a)=c(b)=1, w(a)=0, w(b)=5 has Q_0=Q_1=0, Q_2=5. Thus discrete budget response is not concave.

## Scope limitations
The DP assumes tree structure, additive values, integer budgets, and ancestor dependencies. It does not solve general graph activation or establish a new complexity result. Tree knapsack and precedence-constrained optimization are classical; independent prior-art analysis is mandatory.
