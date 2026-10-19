"""Independent bounded semantic audit of the closed GoN repair grammar.

The reference interpreter is deliberately independent of planner actions/step.
No arbitrary Python guards, multi-role coupling or name-dependent policies are
certified by this module.
"""
from collections import deque
from itertools import permutations, product
from experiments.research_gate.exact_orbit_key import Ref, State, canonical_key
from experiments.research_gate.certified_repair_ucs import (
    Grammar, actions, step, start, goal, cert, validate, search)

def ren_obj(v,mapping):
    if isinstance(v,Ref): return Ref(mapping.get(v.name,v.name))
    if isinstance(v,tuple): return tuple(ren_obj(x,mapping) for x in v)
    return v

def rename(s,mapping):
    return State(**{field:tuple(ren_obj(x,mapping) for x in getattr(s,field))
                    for field in ("active","edges","used","attributes","forbidden","resources")})

def rename_action(a,mapping):
    return ren_obj(a,mapping)

def reference_successors(s,g):
    """Separate interpreter: constructs operations directly from set semantics."""
    active={r.name for r in s.active}
    wired={v.name for u,v in s.edges if u==Ref("service")}
    used=set(s.used)
    restored=("restored",True) in s.resources
    out=[]
    if not restored and ("restore",) not in used:
        a=("restore",)
        t=State(s.active,s.edges,s.used+(a,),s.attributes,s.forbidden,(("restored",True),))
        out.append((a,g.restore_cost,t))
    for n in sorted(g.names):
        ref=Ref(n)
        if n not in active and len(active)<g.capacity:
            a=("create",ref)
            t=State(s.active+(ref,),s.edges,s.used+(a,),s.attributes,s.forbidden,s.resources)
            out.append((a,dict(g.identity_costs).get(n,g.create_cost),t))
        if n in active and n not in wired and (not g.fixed_preferred or g.fixed_preferred==n):
            a=("rewire",ref)
            t=State(s.active,s.edges+((Ref("service"),ref),),s.used+(a,),
                    s.attributes,s.forbidden,s.resources)
            out.append((a,g.rewire_cost,t))
    return out

def reachable(g,max_states=25000):
    validate(g)
    initial=start();seen={initial};queue=deque([initial]);edges=0
    while queue:
        s=queue.popleft()
        for a,w,t in reference_successors(s,g):
            edges+=1
            if t not in seen:
                seen.add(t)
                if len(seen)>max_states:raise RuntimeError("state audit bound exceeded")
                queue.append(t)
    return seen,edges

def audit(g,max_states=25000):
    validate(g,True)
    states,edges=reachable(g,max_states)
    keys={s:canonical_key(s,cert(g)) for s in states}
    group=list(permutations(g.names))
    checked=0
    for s in states:
        ref={(a,w,t) for a,w,t in reference_successors(s,g)}
        impl={(a,w,step(s,a,g)) for a,w in actions(s,g)}
        assert ref==impl,("reference mismatch",s)
        assert goal(s,g)==(("restored",True) in s.resources or len(s.edges)>=g.target)
        for perm in group:
            mapping=dict(zip(g.names,perm))
            transformed=rename(s,mapping)
            assert transformed in states,("not closed under renaming",s,mapping)
            assert keys[s]==keys[transformed],("orbit key mismatch",s,mapping)
            actual={(a,w,t) for a,w,t in reference_successors(transformed,g)}
            expected={(rename_action(a,mapping),w,rename(t,mapping)) for a,w,t in ref}
            assert actual==expected,("transition non-equivariance",s,mapping)
            assert goal(s,g)==goal(transformed,g),("goal non-equivariance",s,mapping)
            checked+=1
    p=search(g,False);q=search(g,True)
    assert p["cost"]==q["cost"],("optimality mismatch",g)
    return {"states":len(states),"edges":edges,"permutations":len(group),
            "state_permutation_checks":checked,"plain_cost":p["cost"],
            "quotient_cost":q["cost"],"plain_expanded":p["expanded"],
            "quotient_expanded":q["expanded"]}

def counterexample_non_equivariant():
    """Smallest witness for name-dependent creation costs if wrongly quotiented."""
    g=Grammar(names=("a","b"),identity_costs=(("a",0),("b",2)),
              restore_cost=9,target=1)
    s=start()
    a=next(t for label,w,t in reference_successors(s,g) if label==("create",Ref("a")))
    b=next(t for label,w,t in reference_successors(s,g) if label==("create",Ref("b")))
    assert canonical_key(a,cert(Grammar(names=("a","b"))))==canonical_key(
        b,cert(Grammar(names=("a","b"))))
    wa=next(w for label,w,t in reference_successors(s,g) if label==("create",Ref("a")))
    wb=next(w for label,w,t in reference_successors(s,g) if label==("create",Ref("b")))
    assert wa!=wb
    return {"names":2,"cost_a":wa,"cost_b":wb,
            "explanation":"graph orbit matches but transition costs differ; quotient must refuse"}

if __name__=="__main__":
    import json
    cases=[]
    for n in range(1,4):
        for capacity in range(0,n+1):
            g=Grammar(names=tuple("r"+str(i) for i in range(n)),
                      target=min(n,2),capacity=capacity,restore_cost=9,budget=10)
            cases.append({"n":n,"capacity":capacity,**audit(g)})
    print(json.dumps({"cases":len(cases),"results":cases,
                      "counterexample":counterexample_non_equivariant()},indent=2))
