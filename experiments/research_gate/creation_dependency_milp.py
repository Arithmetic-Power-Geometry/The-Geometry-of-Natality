"""Closed creation-dependent relay grammar; scipy.optimize.milp external solver.
Not a general graph rewriting interpreter or GROOVE translation.
"""
from dataclasses import dataclass
from itertools import combinations,product
import json

@dataclass(frozen=True)
class Relay:
    covers: frozenset
    cost: int
    requires: frozenset = frozenset()

@dataclass(frozen=True)
class Model:
    terminals: int
    relays: tuple
    capacity: int
    forbidden_pairs: tuple = ()

def validate(p):
    n=len(p.relays)
    if not 1<=p.terminals<=8 or not 1<=n<=12 or not 0<=p.capacity<=n:
        raise ValueError("bounds")
    for i,r in enumerate(p.relays):
        if r.cost<0 or any(t not in range(p.terminals) for t in r.covers):
            raise ValueError("cost/cover")
        if any(j not in range(i) for j in r.requires):
            raise ValueError("prerequisite DAG must use earlier relays")
    for a,b in p.forbidden_pairs:
        if not 0<=a<b<n:raise ValueError("negative guard pair")

def legal(p,chosen):
    s=set(chosen)
    return len(s)<=p.capacity and all(p.relays[i].requires<=s for i in s) and all(
        not (a in s and b in s) for a,b in p.forbidden_pairs)

def graph_goal(p,chosen):
    """Actual root-to-terminal traversal; relay is connected through its prerequisites."""
    s=set(chosen)
    if not legal(p,s):return False
    edges={("root",f"relay:{i}") for i in s if not p.relays[i].requires}
    for i in s:
        for j in p.relays[i].requires:edges.add((f"relay:{j}",f"relay:{i}"))
        for t in p.relays[i].covers:edges.add((f"relay:{i}",f"terminal:{t}"))
    reached={"root"}
    while True:
        nxt=reached|{v for u,v in edges if u in reached}
        if nxt==reached:break
        reached=nxt
    return all(f"terminal:{t}" in reached for t in range(p.terminals))

def exhaustive(p):
    validate(p);best=None;arg=()
    for bits in product((0,1),repeat=len(p.relays)):
        selected=tuple(i for i,b in enumerate(bits) if b)
        if graph_goal(p,selected):
            c=sum(p.relays[i].cost for i in selected)
            if best is None or c<best:best,arg=c,selected
    return {"cost":best,"selected":arg}

def external_milp(p):
    """Genuinely third-party SciPy/HiGHS MILP, independently optimized.
    Valid because prerequisite indices are acyclic and legal selections make
    every selected relay reachable from root. Coverage is then linear union.
    """
    validate(p)
    import numpy as np
    from scipy.optimize import milp,LinearConstraint,Bounds
    n=len(p.relays);rows=[];lo=[];hi=[]
    for t in range(p.terminals):
        rows.append([int(t in r.covers) for r in p.relays]);lo.append(1);hi.append(np.inf)
    rows.append([1]*n);lo.append(-np.inf);hi.append(p.capacity)
    for i,r in enumerate(p.relays):
        for j in r.requires:
            row=[0]*n;row[i]=1;row[j]=-1
            rows.append(row);lo.append(-np.inf);hi.append(0)
    for a,b in p.forbidden_pairs:
        row=[0]*n;row[a]=1;row[b]=1
        rows.append(row);lo.append(-np.inf);hi.append(1)
    result=milp(c=np.array([r.cost for r in p.relays],dtype=float),
        integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.ones(n)),
        constraints=LinearConstraint(np.array(rows,dtype=float),np.array(lo),np.array(hi)),
        options={"time_limit":20.0,"mip_rel_gap":0.0})
    if result.status==2:return {"cost":None,"selected":(),"status":"infeasible"}
    if result.status!=0:raise RuntimeError(f"MILP not proven optimal: {result.message}")
    chosen=tuple(i for i,v in enumerate(result.x) if v>0.5)
    if not graph_goal(p,chosen):raise AssertionError("MILP produced invalid graph")
    cost=sum(p.relays[i].cost for i in chosen)
    assert abs(result.fun-cost)<1e-5
    return {"cost":cost,"selected":chosen,"status":"optimal"}

def counterexamples():
    # C1: cheapest immediate terminal-cover relay may be unavailable until prerequisite
    p=Model(1,(Relay(frozenset(),5),Relay(frozenset({0}),1,frozenset({0})),
               Relay(frozenset({0}),3)),2)
    assert exhaustive(p)["cost"]==3
    # C2: adding a relay cannot increase optimum when capacity counts chosen relays,
    # but can fail to improve it (duplicate expensive relay).
    q=Model(1,(Relay(frozenset({0}),1),Relay(frozenset({0}),4)),1)
    assert exhaustive(q)["cost"]==1
    # C3: feasibility is not monotone under adding selected relays because of NAC.
    z=Model(1,(Relay(frozenset({0}),1),Relay(frozenset(),0)),2,((0,1),))
    assert graph_goal(z,(0,)) and not graph_goal(z,(0,1))
    return {"C1":"cheapest raw relay cost 1 requires prerequisite cost 5; direct relay cost 3 is optimal",
            "C2":"additional template does not strictly improve optimal value",
            "C3":"negative application condition destroys monotonicity of feasible selected sets"}

def sweep():
    # 3 relays; terminal covers, acyclic prereqs, negative guard and capacity vary
    checked=0;infeasible=0
    for coverbits in product(range(4),repeat=3):
        for prereqbits in product((0,1),repeat=3): # edges 0->1, 0->2, 1->2
            req=(frozenset(),frozenset({0}) if prereqbits[0] else frozenset(),
                 frozenset(j for j,b in [(0,prereqbits[1]),(1,prereqbits[2])] if b))
            for cap in range(4):
                for forbidden in ((),((0,2),)):
                    p=Model(2,tuple(Relay(frozenset(t for t in range(2) if coverbits[i]>>t&1),i+1,req[i]) for i in range(3)),cap,forbidden)
                    a=exhaustive(p);b=external_milp(p)
                    assert a["cost"]==b["cost"],(p,a,b)
                    if a["cost"] is None:infeasible+=1
                    checked+=1
    return {"checked":checked,"infeasible":infeasible,"external_solver":"scipy.optimize.milp / HiGHS","all_costs_match":True}

if __name__=="__main__":
    print(json.dumps({"counterexamples":counterexamples(),"sweep":sweep()},indent=2))
