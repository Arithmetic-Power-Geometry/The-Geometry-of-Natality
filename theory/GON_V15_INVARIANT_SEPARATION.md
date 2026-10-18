# Geometry of Natality (GoN) V15 — invariant separation at a fixed root

**Status:** explicit counterexample and independently checkable finite search. Not an original-priority claim.

## Graph pair
Let V={0,1,2,3}, with distinguished root s=0.
G has arcs (0,1),(1,3),(2,0).
H has arcs (0,3),(1,0),(2,1).
Both are simple loop-free directed acyclic graphs.

## Theorem 15.1
The labelled out-degree vectors of G and H are both (1,1,1,0), and the labelled in-degree vectors are both (1,1,0,1). Both have exactly three edges and four vertices. Because both are DAGs, their adjacency matrices are nilpotent and have characteristic polynomial lambda^4; hence they are adjacency-cospectral.

Nevertheless, Reach_G(0)={0,1,3} has size 3, while Reach_H(0)={0,3} has size 2.

Proof: compute the listed arcs, degrees and directed paths. Nilpotence follows by topologically ordering a DAG's adjacency matrix into strictly triangular form.

## Corollary 15.2
The tuple (n,m, labelled in-degree vector, labelled out-degree vector, adjacency characteristic polynomial) does not determine root accessibility, even for DAGs on four vertices.

## Scope
This does NOT establish that GoN is a stronger universal graph invariant, because root reachability is already a classical invariant. It does not establish cospectrality for arbitrary graph families or a computational advantage. Root-labelled isomorphism classes are different, and the pair is distinguishable by standard BFS.

## Verification
An exhaustive search over loop-free labelled digraphs with n=4 uses 2^(4*3)=4096 adjacency configurations. The committed verifier enumerates all and finds an explicit pair with identical labelled degree vectors but different root reachability; the reported pair is additionally verified to be acyclic and therefore cospectral. Search order is deterministic.

## Stronger next gate
Do not continue collecting easy separations alone. A Q1 candidate must prove an original characterization, nontrivial complexity/approximation bound, or deliver a reproducible practical improvement over classical reachability and graph-rewriting baselines.
