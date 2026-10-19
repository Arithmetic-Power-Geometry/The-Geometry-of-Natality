"""Prompt 6: falsifiable structural hypotheses in a finite repair-cost model.

Research sandbox: a service may be repaired by restart (cost r) or by
creation+rewiring (cost c+w). At most k restarts globally; independent
components otherwise. Does not establish publication novelty.
"""
from itertools import product,combinations
from math import inf
import json

def brute(components,k):
    """Independent 2^n strategy enumeration; each entry (restart,create,rewire)."""
    n=len(components)
    best=inf;choice=None
    for mask in product((0,1),repeat=n):
        if sum(mask)>k:continue
        cost=sum((r if use else c+w) for (r,c,w),use in zip(components,mask))
        if cost<best:best=cost;choice=mask
    return best,choice

def greedy(components,k):
    """Sort positive savings; valid only under unit restart capacity consumption."""
    baseline=sum(c+w for r,c,w in components)
    savings=sorted(((c+w-r,i) for i,(r,c,w) in enumerate(components)),reverse=True)
    chosen=[i for d,i in savings[:k] if d>0]
    return baseline-sum(d for d,i in savings[:k] if d>0),tuple(chosen)

def false_conjecture_one(components,k):
    """H1: independent optimum sum survives shared restart capacity."""
    return brute(components,k)[0]==sum(min(r,c+w) for r,c,w in components)

def false_conjecture_two(components,k):
    """H2: optimal restart selection uses cheapest restart action first."""
    indices=sorted(range(len(components)),key=lambda i:components[i][0])[:k]
    value=sum((r if i in indices else c+w) for i,(r,c,w) in enumerate(components))
    return value==brute(components,k)[0]

def theorem_three(components,k):
    """H3: select up to k positive savings, largest first."""
    return greedy(components,k)[0]==brute(components,k)[0]

def search_counterexamples():
    # Search by component count, then lexicographic costs; deterministic.
    candidates=list(product(range(3),repeat=3))
    failures={"H1":None,"H2":None,"H3":None}
    checked=0
    for n in (1,2,3):
        for entries in product(candidates,repeat=n):
            for k in range(n+1):
                checked+=1
                for name,pred in (("H1",false_conjecture_one),
                                  ("H2",false_conjecture_two),
                                  ("H3",theorem_three)):
                    if failures[name] is None and not pred(entries,k):
                        optimum,plan=brute(entries,k)
                        failures[name]={"components":[list(v) for v in entries],
                                        "capacity":k,"optimum":optimum,
                                        "optimal_restart_mask":plan}
    assert failures["H1"] is not None
    assert failures["H2"] is not None
    assert failures["H3"] is None
    return {"tested_parameter_instances":checked,"failures":failures,
            "theorem_status":"verified in finite domain only; separate proof required"}

def proof_witness(components,k):
    """Check exchange argument's numerical conclusion, including ties/zeros."""
    n=len(components)
    assert 0<=k<=n
    baseline=sum(c+w for r,c,w in components)
    discounts=[c+w-r for r,c,w in components]
    positive=sorted((d for d in discounts if d>0),reverse=True)
    predicted=baseline-sum(positive[:k])
    optimum,_=brute(components,k)
    assert predicted==optimum
    return predicted

if __name__=="__main__":
    print(json.dumps(search_counterexamples(),indent=2))
