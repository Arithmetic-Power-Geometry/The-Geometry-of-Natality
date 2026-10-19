"""Finite declarative repair grammar and replayable plain/orbit UCS.

A deliberately narrow, closed grammar: every fresh name in one role pool is
interchangeable, actions enumerate names uniformly, and all costs are
role-level constants. This is NOT a general certification of user callbacks.
"""
from dataclasses import dataclass
from heapq import heappush, heappop
from itertools import count
from time import perf_counter
import tracemalloc

from experiments.research_gate.exact_orbit_key import (
    Ref, State, Certificate, UnsafeQuotient, canonical_key)

@dataclass(frozen=True)
class Grammar:
    names: tuple = ("replica_a", "replica_b")
    create_cost: int = 2
    rewire_cost: int = 1
    restore_cost: int = 3
    target: int = 1
    capacity: int = 8
    budget: int = 100
    # All identity-specific policies are forbidden in quotient mode.
    identity_costs: tuple = ()
    fixed_preferred: str = ""
    opaque_guards: bool = False

def validate(g, quotient=False):
    if not isinstance(g, Grammar):
        raise TypeError("Grammar required")
    if not 1 <= len(g.names) <= 8 or len(set(g.names)) != len(g.names):
        raise ValueError("1..8 distinct fresh names required")
    if any(type(n) is not str or not n for n in g.names):
        raise ValueError("names must be nonempty strings")
    if any(type(v) is not int or v < 0 for v in
           (g.create_cost,g.rewire_cost,g.restore_cost,g.target,g.capacity,g.budget)):
        raise ValueError("nonnegative integer costs and limits required")
    if g.target > len(g.names):
        raise ValueError("target exceeds pool size")
    if quotient and (g.identity_costs or g.fixed_preferred or g.opaque_guards):
        raise UnsafeQuotient("identity-sensitive or opaque grammar not certified")
    if g.identity_costs:
        d=dict(g.identity_costs)
        if set(d)-set(g.names) or any(type(v) is not int or v<0 for v in d.values()):
            raise ValueError("invalid identity-specific costs")

def cert(g):
    validate(g, quotient=True)
    return Certificate(pools=(tuple(sorted(g.names)),), fixed=("service",),
        equivariant_transitions=True, equivariant_goal=True,
        equivariant_costs=True, equivariant_constraints=True,
        equivariant_allocation=True, no_hidden_identity_data=True)

def start():
    return State(resources=(("restored",False),))

def _present(s, name):
    return Ref(name) in s.active

def _wired(s, name):
    return (Ref("service"),Ref(name)) in s.edges

def goal(s,g):
    return ("restored",True) in s.resources or len(s.edges) >= g.target

def actions(s,g):
    """Ordered action labels; history is identity-bearing, never dropped."""
    if ("restored",True) not in s.resources and ("restore",) not in s.used:
        yield ("restore",),g.restore_cost
    for n in sorted(g.names):
        if not _present(s,n) and len(s.active)<g.capacity:
            yield ("create",Ref(n)),dict(g.identity_costs).get(n,g.create_cost)
        if _present(s,n) and not _wired(s,n):
            if not g.fixed_preferred or g.fixed_preferred==n:
                yield ("rewire",Ref(n)),g.rewire_cost

def step(s,a,g):
    """Independent declarative interpreter; no user callbacks."""
    if a not in {label for label,_ in actions(s,g)}:
        raise ValueError("inapplicable action")
    if a[0]=="restore":
        return State(s.active,s.edges,s.used+(a,),s.attributes,s.forbidden,(("restored",True),))
    n=a[1]
    if a[0]=="create":
        return State(s.active+(n,),s.edges,s.used+(a,),s.attributes,s.forbidden,s.resources)
    if a[0]=="rewire":
        return State(s.active,s.edges+((Ref("service"),n),),s.used+(a,),
                     s.attributes,s.forbidden,s.resources)
    raise ValueError("unknown action")

def replay(g,plan,claimed_cost=None):
    validate(g)
    s=start();total=0
    for a in plan:
        options=dict(actions(s,g))
        if a not in options:
            raise AssertionError("inapplicable plan action")
        total+=options[a]
        if total>g.budget:
            raise AssertionError("budget exceeded")
        s=step(s,a,g)
    if not goal(s,g):
        raise AssertionError("plan does not reach goal")
    if claimed_cost is not None and total!=claimed_cost:
        raise AssertionError("incorrect claimed cost")
    return total,s

def search(g,quotient=False):
    validate(g,quotient)
    c=cert(g) if quotient else None
    calls=0;key_seconds=0.
    def key(s):
        nonlocal calls,key_seconds
        if not quotient:return s
        t=perf_counter()
        k=canonical_key(s,c)
        key_seconds+=perf_counter()-t
        calls+=1
        return k
    initial=start()
    dist={key(initial):0}
    queue=[(0,0,initial,())];seq=count(1)
    expanded=0;generated=0
    while queue:
        cost,_,s,path=heappop(queue)
        if dist.get(key(s))!=cost:continue
        expanded+=1
        if goal(s,g):
            replay(g,path,cost)
            return dict(cost=cost,plan=path,expanded=expanded,generated=generated,
                        distinct=len(dist),canonical_calls=calls,canonical_seconds=key_seconds)
        for a,w in actions(s,g):
            generated+=1
            newcost=cost+w
            if newcost>g.budget:continue
            t=step(s,a,g)
            k=key(t)
            if newcost<dist.get(k,float("inf")):
                dist[k]=newcost
                heappush(queue,(newcost,next(seq),t,path+(a,)))
    return dict(cost=None,plan=(),expanded=expanded,generated=generated,
                distinct=len(dist),canonical_calls=calls,canonical_seconds=key_seconds)

def exhaustive(g):
    """Independent full trace-tree enumeration for small grammars."""
    validate(g)
    best=None;best_plan=()
    stack=[(start(),0,())];visits=0
    while stack:
        s,c,p=stack.pop();visits+=1
        if goal(s,g):
            if best is None or c<best:
                best,best_plan=c,p
            continue
        for a,w in actions(s,g):
            if c+w<=g.budget:
                stack.append((step(s,a,g),c+w,p+(a,)))
    if best is not None:replay(g,best_plan,best)
    return dict(cost=best,plan=best_plan,visits=visits)

def measured(g,quotient):
    tracemalloc.start()
    t=perf_counter()
    result=search(g,quotient)
    elapsed=perf_counter()-t
    _,peak=tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return dict(result,wall_seconds=elapsed,peak_python_bytes=peak)

if __name__=="__main__":
    import json
    for n in (1,2,3,4):
        g=Grammar(names=tuple("r"+str(i) for i in range(n)),target=min(2,n))
        a=search(g);b=search(g,True);e=exhaustive(g)
        assert a["cost"]==b["cost"]==e["cost"]
        print(json.dumps({"n":n,"plain":a["expanded"],"quotient":b["expanded"],"cost":a["cost"]}))
