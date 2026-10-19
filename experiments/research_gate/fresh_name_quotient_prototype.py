"""Exact fresh-name orbit search for finite creation-enabled repair instances.

The initial identities and action labels are fixed. Fresh names are exchangeable
only when all constraints, goals, costs and future transitions are equivariant.
This module deliberately makes no claim of novelty over nominal symmetry reduction.
"""
from itertools import permutations
from heapq import heappush, heappop
import json

def canonical(state, fresh_names):
    """Exact minimum encoding over all permutations of allocated fresh identities."""
    active, edges, used = state
    fresh = sorted(set(active) & set(fresh_names))
    if len(fresh) > 8:
        raise ValueError("exact factorial canonicalization limited to 8 fresh names")
    best = None
    for perm in permutations(fresh):
        ren = dict(zip(fresh, perm))
        key = (tuple(sorted(ren.get(x,x) for x in active)),
               tuple(sorted((ren.get(a,a),ren.get(b,b)) for a,b in edges)),
               tuple(sorted(used)))
        if best is None or key < best: best = key
    return best

def solve(initial, actions, goal, fresh_names, quotient=False):
    """UCS with concrete predecessor chain; costs nonnegative, action labels unique."""
    def key(s): return canonical(s,fresh_names) if quotient else s
    q=[(0,0,initial,())]; distance={key(initial):0}
    serial=0; expansions=0
    while q:
        cost,_,s,path=heappop(q)
        if cost!=distance.get(key(s)): continue
        expansions+=1
        if goal(s):
            # Carry the concrete path in state-associated queue records instead of
            # orbit-level predecessor pointers, avoiding invalid representative lifts.
            return {"cost":cost,"expansions":expansions,"plan":list(path)}
        for name,weight,step in actions:
            if name in s[2]: continue
            nxt=step(s)
            if nxt is None: continue
            nxt=(nxt[0],nxt[1],frozenset(set(s[2])|{name}))
            new=cost+weight
            if new<distance.get(key(nxt),float("inf")):
                distance[key(nxt)]=new
                serial+=1;heappush(q,(new,serial,nxt,path+(name,)))
    return {"cost":None,"expansions":expansions}

def demo():
    # The two fresh identifiers can be created in either order. This model is
    # symmetric because the goal depends only on the number of active replicas.
    names=("replica_a","replica_b")
    initial=(frozenset(),frozenset(),frozenset())
    def create(name):
        def step(s):
            return (s[0]|{name},s[1])
        return step
    actions=[("create_a",1,create(names[0])),("create_b",1,create(names[1]))]
    goal=lambda s: len(s[0])==2
    plain=solve(initial,actions,goal,names)
    reduced=solve(initial,actions,goal,names,True)
    assert plain["cost"]==reduced["cost"]==2\n    assert sum(next(w for name,w,_ in actions if name==a) for a in reduced["plan"])==2
    return {"plain":plain,"quotient":reduced,
            "warning":"action labels are fixed, so the action-history-sensitive quotient is not expected to reduce states"}

if __name__=="__main__":
    print(json.dumps(demo(),indent=2))
