"""Frozen GoN benchmark v1: deterministic instances, semantic compatibility, hashes.

NO benchmark result, operational trace, or GROOVE equivalence is asserted here.
"""
from dataclasses import asdict,dataclass
import hashlib,json,random
from experiments.research_gate.certified_repair_ucs import Grammar
from experiments.research_gate.footprint_certificate import Component,Problem

VERSION="gon-benchmark-v1.0.0"
SEEDS=(17,29,43)
STRATA=("independent","shared_restart","graph_coupled","fresh_symmetric",
        "identity_cost","history_local","negative_local","opaque_guard")
FIELDS=("version","stratum","seed","n","instance","topology","topology_sha256",
        "instance_sha256","compatibility","provenance")
def canonical(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True)
def digest(x):
    return hashlib.sha256(canonical(x).encode("ascii")).hexdigest()
def topology(stratum,n):
    nodes=["service_"+str(i) for i in range(n)]
    edges=[[nodes[i],nodes[i+1]] for i in range(n-1)] if stratum=="graph_coupled" else []
    return {"nodes":nodes,"edges":edges,"directed":True}
def compatibility(stratum):
    if stratum=="fresh_symmetric":
        return {"plain_ucs":"supported","quotient_ucs":"supported",
                "decomposition":"incompatible_model","groove":"unverified"}
    if stratum=="identity_cost":
        return {"plain_ucs":"supported","quotient_ucs":"must_refuse",
                "decomposition":"incompatible_model","groove":"unverified"}
    if stratum=="opaque_guard":
        return {"plain_ucs":"supported_but_guard_not_enforced",
                "quotient_ucs":"must_refuse","decomposition":"must_refuse",
                "groove":"unverified"}
    if stratum in ("independent","history_local","negative_local"):
        return {"plain_ucs":"supported","quotient_ucs":"incompatible_model",
                "decomposition":"supported","groove":"unverified"}
    return {"plain_ucs":"supported_partial_semantics",
            "quotient_ucs":"incompatible_model","decomposition":"must_refuse",
            "groove":"unverified"}
def make(stratum,seed,n):
    if stratum not in STRATA or seed not in SEEDS or n not in (2,3,4):
        raise ValueError("not a frozen benchmark cell")
    rng=random.Random(seed*1000+n*97+STRATA.index(stratum))
    t=topology(stratum,n)
    if stratum in ("fresh_symmetric","identity_cost","opaque_guard"):
        names=tuple("replica_"+str(i) for i in range(n))
        costs=((names[0],0),) if stratum=="identity_cost" else ()
        g=Grammar(names=names,create_cost=rng.randint(1,4),
                  rewire_cost=rng.randint(0,3),restore_cost=rng.randint(4,12),
                  target=min(2,n),capacity=n,budget=40,
                  identity_costs=costs,opaque_guards=stratum=="opaque_guard")
        instance={"model":"single_pool","grammar":asdict(g)}
    else:
        cs=tuple(Component(restart=rng.randint(1,7),create=rng.randint(1,4),
                rewire=rng.randint(0,3),
                forbid_restart=(stratum=="negative_local" and i==0),
                require_create_history=True) for i in range(n))
        p=Problem(cs,budget=60,
                  shared_restart_limit=1 if stratum=="shared_restart" else None,
                  cross_edges=((0,1),) if stratum=="graph_coupled" else ())
        instance={"model":"multi_component","problem":asdict(p)}
    row={"version":VERSION,"stratum":stratum,"seed":seed,"n":n,
         "instance":instance,"topology":t,"topology_sha256":digest(t),
         "compatibility":compatibility(stratum),
         "provenance":"synthetic_deterministic_no_external_logs"}
    row["instance_sha256"]=digest(row)
    return row
def manifest():
    rows=[make(s,seed,n) for s in STRATA for seed in SEEDS for n in (2,3,4)]
    assert len(rows)==72 and len({x["instance_sha256"] for x in rows})==72
    payload={"version":VERSION,"frozen":True,"seed_list":list(SEEDS),
             "strata":list(STRATA),"cells":len(rows),
             "instances":rows}
    payload["manifest_sha256"]=digest(payload)
    return payload
def verify(payload):
    expected=manifest()
    if canonical(payload)!=canonical(expected):
        raise AssertionError("benchmark drift: instance or metadata changed")
    for row in payload["instances"]:
        assert set(row)==set(FIELDS)
        assert row["topology_sha256"]==digest(row["topology"])
        temp=dict(row);h=temp.pop("instance_sha256")
        assert digest(temp)==h
    return True
if __name__=="__main__":
    print(json.dumps(manifest(),sort_keys=True,indent=2))
