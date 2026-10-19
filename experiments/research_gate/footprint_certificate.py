"""Conservative executable decomposition certificate for a CLOSED finite repair DSL.

This is a separate multi-component model, not an automatic extension of the
single-role quotient planner. Unknown guards/resources are rejected.
"""
from dataclasses import dataclass
from heapq import heappush, heappop
from itertools import count
from time import perf_counter

@dataclass(frozen=True)
class Component:
    restart: int = 3
    create: int = 2
    rewire: int = 1
    forbid_restart: bool = False
    forbid_create: bool = False
    require_create_history: bool = True

@dataclass(frozen=True)
class Problem:
    components: tuple
    budget: int = 100
    shared_restart_limit: object = None
    cross_edges: tuple = ()
    global_history_guard: bool = False
    shared_allocation: bool = False
    opaque_guard: bool = False
    global_negative_condition: bool = False

@dataclass(frozen=True)
class Footprint:
    reads: frozenset
    writes: frozenset
    guards: frozenset
    allocations: frozenset

def validate(p):
    if not isinstance(p,Problem) or not p.components:
        raise ValueError("nonempty typed Problem required")
    if type(p.budget) is not int or p.budget<0:
        raise ValueError("invalid budget")
    for c in p.components:
        if not isinstance(c,Component) or any(type(x) is not int or x<0 for x in
                                             (c.restart,c.create,c.rewire)):
            raise ValueError("invalid component costs")
    if p.shared_restart_limit is not None and (
        type(p.shared_restart_limit) is not int or p.shared_restart_limit<0):
        raise ValueError("invalid shared restart limit")

def footprint(p,i,kind):
    """Derived from the finite DSL action semantics, not caller declarations."""
    validate(p)
    if not 0<=i<len(p.components) or kind not in ("restart","create","rewire"):
        raise ValueError("unknown action")
    local=f"c:{i}"
    reads={local+":stage"}
    writes={local+":stage",local+":history"}
    guards={local+":stage",local+":history"}
    allocations=set()
    if kind=="create":
        allocations.add(local+":identity")
        writes.add(local+":identity")
        if p.shared_allocation:
            allocations.add("global:allocation")
            writes.add("global:allocation")
    if kind=="rewire":
        reads.add(local+":identity")
        guards.add(local+":history")
    if kind=="restart" and p.shared_restart_limit is not None:
        reads.add("global:restart_capacity")
        writes.add("global:restart_capacity")
        guards.add("global:restart_capacity")
    if p.global_history_guard:
        guards.add("global:history")
    if p.global_negative_condition:
        guards.add("global:negative")
    if p.opaque_guard:
        guards.add("unknown:opaque")
    return Footprint(frozenset(reads),frozenset(writes),
                     frozenset(guards),frozenset(allocations))

def certificate(p):
    validate(p)
    reasons=[]
    if p.cross_edges: reasons.append("cross-component edges")
    if p.opaque_guard: reasons.append("opaque guard")
    if p.global_history_guard: reasons.append("global history guard")
    if p.global_negative_condition: reasons.append("global negative application condition")
    if p.shared_allocation: reasons.append("shared fresh-name allocation")
    if p.shared_restart_limit is not None: reasons.append("shared restart capacity")
    footprints={(i,k):footprint(p,i,k)
                for i in range(len(p.components))
                for k in ("restart","create","rewire")}
    for (i,a),fa in footprints.items():
        for (j,b),fb in footprints.items():
            if i>=j: continue
            if fa.writes & (fb.reads|fb.writes|fb.guards|fb.allocations) or (
                fb.writes & (fa.reads|fa.guards|fa.allocations)):
                reasons.append(f"footprint conflict: {i}/{a} and {j}/{b}")
    return {"certified":not reasons,"reasons":tuple(dict.fromkeys(reasons)),
            "footprints":footprints,
            "budget_semantics":"external additive total-cost feasibility bound"}

def initial(p):
    return (tuple(0 for _ in p.components),tuple(() for _ in p.components),0)

def successors(p,s):
    stages,histories,restarts=s
    for i,c in enumerate(p.components):
        stage=stages[i];history=histories[i]
        opts=[]
        if stage==0:
            if not c.forbid_restart and (
                p.shared_restart_limit is None or restarts<p.shared_restart_limit):
                opts.append(("restart",c.restart,3))
            if not c.forbid_create:
                opts.append(("create",c.create,1))
        if stage==1 and (not c.require_create_history or "create" in history):
            opts.append(("rewire",c.rewire,2))
        for kind,cost,next_stage in opts:
            ns=list(stages);ns[i]=next_stage
            nh=list(histories);nh[i]=history+(kind,)
            nr=restarts+(kind=="restart")
            yield (i,kind),cost,(tuple(ns),tuple(nh),nr)

def finished(s):
    return all(x in (2,3) for x in s[0])

def full_ucs(p):
    validate(p)
    root=initial(p)
    queue=[(0,0,root,())];serial=count(1);dist={root:0}
    expanded=0;generated=0
    while queue:
        cost,_,state,plan=heappop(queue)
        if cost!=dist[state]:continue
        expanded+=1
        if finished(state):
            assert replay(p,plan)==cost
            return {"cost":cost,"plan":plan,"expanded":expanded,
                    "generated":generated,"distinct":len(dist)}
        for a,w,t in successors(p,state):
            generated+=1;nc=cost+w
            if nc<=p.budget and nc<dist.get(t,float("inf")):
                dist[t]=nc
                heappush(queue,(nc,next(serial),t,plan+(a,)))
    return {"cost":None,"plan":(),"expanded":expanded,
            "generated":generated,"distinct":len(dist)}

def replay(p,plan):
    s=initial(p);cost=0
    for a in plan:
        matches=[(w,t) for b,w,t in successors(p,s) if a==b]
        if len(matches)!=1:raise AssertionError("invalid or ambiguous plan")
        w,s=matches[0];cost+=w
        if cost>p.budget:raise AssertionError("budget exceeded")
    if not finished(s):raise AssertionError("goal not reached")
    return cost

def local_oracle(c):
    """Independent complete local trace enumeration; no full_ucs calls."""
    options=[]
    if not c.forbid_restart:
        options.append((c.restart,("restart",)))
    if not c.forbid_create and c.require_create_history:
        options.append((c.create+c.rewire,("create","rewire")))
    if not c.forbid_create and not c.require_create_history:
        options.append((c.create+c.rewire,("create","rewire")))
    if not options:return None,()
    return min(options,key=lambda v:(v[0],v[1]))

def decomposed(p):
    start_time=perf_counter()
    check=certificate(p)
    if not check["certified"]:
        return {"certified":False,"reasons":check["reasons"],
                "certificate_seconds":perf_counter()-start_time}
    local=[local_oracle(c) for c in p.components]
    if any(cost is None for cost,_ in local):
        return {"certified":True,"cost":None,"plan":(),
                "certificate_seconds":perf_counter()-start_time}
    total=sum(cost for cost,_ in local)
    plan=tuple((i,a) for i,(_,actions) in enumerate(local) for a in actions)
    if total>p.budget:
        return {"certified":True,"cost":None,"plan":(),
                "certificate_seconds":perf_counter()-start_time}
    assert replay(p,plan)==total
    return {"certified":True,"cost":total,"plan":plan,
            "local_costs":tuple(cost for cost,_ in local),
            "certificate_seconds":perf_counter()-start_time}

def exhaustive_global(p):
    """Independent trace-tree DFS; no UCS/distance map; bounded small DSL."""
    validate(p)
    stack=[(initial(p),0,())]
    best=None;best_plan=();visits=0
    while stack:
        state,cost,plan=stack.pop();visits+=1
        if finished(state):
            if best is None or cost<best:
                best,best_plan=cost,plan
            continue
        for a,w,t in successors(p,state):
            if cost+w<=p.budget:
                stack.append((t,cost+w,plan+(a,)))
    if best is not None:
        assert replay(p,best_plan)==best
    return {"cost":best,"plan":best_plan,"visits":visits}

def coupling_counterexample():
    p=Problem((Component(restart=1,create=2,rewire=1),
               Component(restart=1,create=2,rewire=1)),shared_restart_limit=1)
    unsafe=((0,"restart"),(1,"restart"))
    try:
        replay(p,unsafe)
    except AssertionError:
        rejected=True
    else:
        rejected=False
    assert rejected
    exact=full_ucs(p)
    assert exact["cost"]==4
    assert not certificate(p)["certified"]
    return {"minimal_components":2,"local_unconstrained_cost":2,
            "global_optimal_cost":exact["cost"],"unsafe_plan_rejected":rejected,
            "certificate_refused":True}

if __name__=="__main__":
    import json
    results=[]
    for n in range(1,5):
        p=Problem(tuple(Component(restart=2+i%3,create=1+i%2,rewire=2)
                        for i in range(n)))
        d=decomposed(p);f=full_ucs(p)
        assert d["cost"]==f["cost"]
        results.append({"n":n,"decomposed_cost":d["cost"],"full_cost":f["cost"],
                        "full_expanded":f["expanded"],
                        "certificate_seconds":d["certificate_seconds"]})
    print(json.dumps({"cases":results,"counterexample":coupling_counterexample(),
                      "status":"synthetic research-stage demonstration"},indent=2))
