"""Prompt 11: closed creation-to-terminal reachability grammar.

Each create action installs a new distinct relay with arcs root->relay and
relay->covered terminals, with nonnegative creation cost. Old graph has root
and isolated terminals; no other actions or guards. This is exactly weighted
set cover, NOT a novel reduction or a general GoN graph-rewriting solver.
"""
from dataclasses import dataclass
from heapq import heappush,heappop
from itertools import combinations,product
import json,hashlib

@dataclass(frozen=True)
class Template:
    covers: frozenset
    cost: int

@dataclass(frozen=True)
class Instance:
    terminals: int
    templates: tuple

def validate(p):
    if not isinstance(p,Instance) or type(p.terminals)!=int or not 1<=p.terminals<=12:
        raise ValueError("invalid terminal universe")
    if not 1<=len(p.templates)<=16:
        raise ValueError("invalid template count")
    for t in p.templates:
        if not isinstance(t,Template) or type(t.cost)!=int or t.cost<0:
            raise ValueError("invalid cost")
        if not t.covers or any(type(i)!=int or i<0 or i>=p.terminals for i in t.covers):
            raise ValueError("invalid cover")

def installed_graph(p,selected):
    """Independent graph materialization, with all created vertices explicit."""
    validate(p)
    verts={"root"}|{f"terminal:{i}" for i in range(p.terminals)}
    arcs=set()
    for i in selected:
        if not 0<=i<len(p.templates):raise ValueError("invalid template")
        relay=f"created:{i}"
        verts.add(relay);arcs.add(("root",relay))
        for j in p.templates[i].covers:arcs.add((relay,f"terminal:{j}"))
    return verts,arcs

def reached_by_graph(p,selected):
    verts,arcs=installed_graph(p,selected)
    seen={"root"};stack=["root"]
    while stack:
        u=stack.pop()
        for a,b in arcs:
            if a==u and b not in seen:
                seen.add(b);stack.append(b)
    return all(f"terminal:{i}" in seen for i in range(p.terminals))

def exhaustive_graph(p):
    """Independent exhaustive oracle over installed graphs, not bitmask DP."""
    validate(p)
    best=None;chosen=()
    for k in range(len(p.templates)+1):
        for sel in combinations(range(len(p.templates)),k):
            cost=sum(p.templates[i].cost for i in sel)
            if (best is None or cost<best) and reached_by_graph(p,sel):
                best=cost;chosen=sel
    return {"cost":best,"selected":chosen}

def subset_dp(p):
    """Exact subset-state Dijkstra baseline; distinct from graph enumeration."""
    validate(p)
    target=(1<<p.terminals)-1
    masks=[sum(1<<j for j in t.covers) for t in p.templates]
    q=[(0,0,())];dist={0:0};expanded=0
    while q:
        c,m,sel=heappop(q)
        if c!=dist[m]:continue
        expanded+=1
        if m==target:
            assert reached_by_graph(p,sel)
            return {"cost":c,"selected":sel,"expanded":expanded}
        for i,(t,mask) in enumerate(zip(p.templates,masks)):
            nxt=m|mask;nc=c+t.cost
            if nc<dist.get(nxt,float("inf")):
                dist[nxt]=nc;heappush(q,(nc,nxt,sel+(i,)))
    return {"cost":None,"selected":(),"expanded":expanded}

def greedy_newly_covered(p):
    """Falsifiable heuristic: cheapest raw creation cost first."""
    validate(p)
    remaining=set(range(p.terminals));chosen=[]
    for i in sorted(range(len(p.templates)),key=lambda i:(p.templates[i].cost,i)):
        if p.templates[i].covers & remaining:
            chosen.append(i);remaining-=p.templates[i].covers
        if not remaining:break
    return {"cost":sum(p.templates[i].cost for i in chosen) if not remaining else None,
            "selected":tuple(chosen)}

def ledger():
    # H1 false: local cheapest creation first always globally optimal.
    a=Instance(2,(Template(frozenset({0}),1),Template(frozenset({1}),1),
                  Template(frozenset({0,1}),1)))
    # H2 false: a zero-cost creation always improves the optimal objective.
    b=Instance(1,(Template(frozenset({0}),0),Template(frozenset({0}),0)))
    # H3: cover reachability equals union cover and optimum equals weighted set cover.
    assert greedy_newly_covered(a)["cost"]==2
    assert subset_dp(a)["cost"]==exhaustive_graph(a)["cost"]==1
    assert subset_dp(b)["cost"]==0
    return {"H1":{"status":"false","heuristic_cost":2,"optimal_cost":1},
            "H2":{"status":"false","counterexample":"adding a zero-cost relay covering an already reachable terminal to an instance already containing the same free relay leaves optimum unchanged"},
            "H3":{"status":"true_conditional_standard","claim":"weighted set-cover equivalence for the closed relay grammar"}}

def sweep():
    """Complete deterministic search of 3-terminal 3-template binary costs."""
    n=3;covers=[frozenset(j for j in range(n) if mask>>j&1) for mask in range(1,1<<n)]
    checked=0;unreachable=0
    for indices in product(range(len(covers)),repeat=3):
        for costs in product((0,1,2),repeat=3):
            p=Instance(n,tuple(Template(covers[j],costs[i]) for i,j in enumerate(indices)))
            a=exhaustive_graph(p);b=subset_dp(p)
            assert a["cost"]==b["cost"],(p,a,b)
            if a["cost"] is not None:
                assert reached_by_graph(p,a["selected"])
                assert reached_by_graph(p,b["selected"])
            else:unreachable+=1
            checked+=1
    return {"checked":checked,"unreachable":unreachable,"status":"exact_match"}

if __name__=="__main__":
    print(json.dumps({"counterexamples":ledger(),"exhaustive":sweep()},indent=2))
