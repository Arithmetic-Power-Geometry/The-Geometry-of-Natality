"""Prompt 8: execute ONLY matched frozen GoN v1 benchmark comparisons.

The manifest generator is imported unchanged. All timing rows retain failures.
"""
import argparse,hashlib,json,os,platform,random,statistics,sys,time,tracemalloc
from dataclasses import fields
from datetime import datetime,timezone
from experiments.research_gate.benchmark_v1 import manifest,verify,canonical,digest
from experiments.research_gate.certified_repair_ucs import Grammar,search,exhaustive
from experiments.research_gate.footprint_certificate import (
    Component,Problem,full_ucs,decomposed,exhaustive_global,certificate,replay)
from experiments.research_gate.exact_orbit_key import UnsafeQuotient
from experiments.research_gate.independent_replay import verify as verify_replay

PAIRS={"fresh_symmetric":("plain_ucs","quotient_ucs"),
       "independent":("full_ucs","decomposition"),
       "history_local":("full_ucs","decomposition"),
       "negative_local":("full_ucs","decomposition")}
WARMUP=3
REPS=20
def decode(row):
    obj=row["instance"]
    if obj["model"]=="single_pool":
        g=dict(obj["grammar"])
        g["names"]=tuple(g["names"])
        g["identity_costs"]=tuple(tuple(x) for x in g["identity_costs"])
        return Grammar(**g)
    p=dict(obj["problem"])
    p["components"]=tuple(Component(**c) for c in p["components"])
    p["cross_edges"]=tuple(tuple(x) for x in p["cross_edges"])
    return Problem(**p)
def execute(obj,algorithm):
    if algorithm=="plain_ucs":return search(obj,False)
    if algorithm=="quotient_ucs":return search(obj,True)
    if algorithm=="full_ucs":return full_ucs(obj)
    if algorithm=="decomposition":return decomposed(obj)
    raise ValueError("unknown algorithm")
def independent_oracle(obj,model):
    if model=="single_pool":
        return exhaustive(obj)["cost"]
    return exhaustive_global(obj)["cost"]
def plan_identity(plan):
    return hashlib.sha256(repr(plan).encode("utf-8")).hexdigest()
def measured(obj,algorithm):
    tracemalloc.start()
    begin=time.perf_counter()
    try:
        result=execute(obj,algorithm)
        status="success";error=None
    except Exception as exc:
        result={};status="error";error=type(exc).__name__+": "+str(exc)
    seconds=time.perf_counter()-begin
    _,peak=tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return {"algorithm":algorithm,"status":status,"exception":error,
            "wall_seconds":seconds,"peak_tracemalloc_bytes":peak,
            "cost":result.get("cost"),"plan_sha256":plan_identity(result.get("plan",())),
            "expanded":result.get("expanded"),"generated":result.get("generated"),
            "distinct":result.get("distinct"),
            "canonical_calls":result.get("canonical_calls"),
            "canonical_seconds":result.get("canonical_seconds"),
            "certificate_seconds":result.get("certificate_seconds")}
def negative_control(row):
    obj=decode(row);stratum=row["stratum"]
    if stratum=="identity_cost":
        try:search(obj,True)
        except UnsafeQuotient:return {"status":"correct_refusal","algorithm":"quotient_ucs"}
        return {"status":"failure_not_refused","algorithm":"quotient_ucs"}
    if stratum=="opaque_guard":
        try:search(obj,True)
        except UnsafeQuotient:return {"status":"correct_refusal","algorithm":"quotient_ucs"}
        return {"status":"failure_not_refused","algorithm":"quotient_ucs"}
    if stratum in ("shared_restart","graph_coupled"):
        return {"status":"correct_refusal" if not certificate(obj)["certified"] else "failure_not_refused",
                "algorithm":"decomposition"}
    raise ValueError("not a refusal cell")
def percentile(xs,q):
    ys=sorted(xs)
    if not ys:return None
    v=(len(ys)-1)*q
    lo=int(v);hi=min(lo+1,len(ys)-1)
    return ys[lo]+(ys[hi]-ys[lo])*(v-lo)
def stats(pairs,seed):
    if not pairs:return None
    diffs=[a-b for a,b in pairs]
    rng=random.Random(seed)
    boots=[statistics.median([rng.choice(diffs) for _ in diffs]) for _ in range(1000)]
    return {"pairs":len(pairs),"median_difference_seconds":statistics.median(diffs),
            "iqr_difference_seconds":[percentile(diffs,.25),percentile(diffs,.75)],
            "bootstrap95_median_difference_seconds":[percentile(boots,.025),percentile(boots,.975)],
            "sign_convention":"first algorithm wall seconds minus second algorithm wall seconds"}
def run(repetitions=REPS,warmup=WARMUP):
    if repetitions<1 or warmup<0:raise ValueError("invalid repetition counts")
    frozen=manifest()
    verify(frozen)
    out={"schema":"gon-prompt8-v1","manifest_sha256":frozen["manifest_sha256"],
         "source_commit":os.getenv("GITHUB_SHA","unknown"),
         "utc":datetime.now(timezone.utc).isoformat(),
         "environment":{"python":sys.version,"platform":platform.platform(),
                        "cpu":platform.processor(),"machine":platform.machine(),
                        "github_runner":os.getenv("RUNNER_NAME","unknown")},
         "repetitions":repetitions,"warmup":warmup,
         "measurement_note":"tracemalloc Python allocations, not process RSS; no hard per-trial timeout enforcement",
         "cells":[],"trials":[],"negative_controls":[]}
    for row in frozen["instances"]:
        s=row["stratum"];obj=decode(row)
        cell={"stratum":s,"seed":row["seed"],"n":row["n"],
              "instance_sha256":row["instance_sha256"],
              "topology_sha256":row["topology_sha256"]}
        if s not in PAIRS:
            negative=negative_control(row)
            out["negative_controls"].append(dict(cell,**negative))
            if negative["status"]!="correct_refusal":raise AssertionError(("negative control",cell))
            continue
        a,b=PAIRS[s]
        oracle=independent_oracle(obj,row["instance"]["model"])
        cell.update({"algorithms":[a,b],"oracle_cost":oracle})
        for algorithm in (a,b):
            answer=execute(obj,algorithm)
            if answer.get("cost")!=oracle:
                raise AssertionError(("incorrect optimum",cell,algorithm,answer.get("cost"),oracle))
            if oracle is not None:
                if row["instance"]["model"]=="single_pool":
                    verify_replay(obj,answer["plan"],oracle)
                else:
                    assert replay(obj,answer["plan"])==oracle
        out["cells"].append(cell)
        for _ in range(warmup):
            execute(obj,a);execute(obj,b)
        for rep in range(repetitions):
            order=[a,b]
            random.Random(row["seed"]*100000+row["n"]*1000+rep+len(s)*31).shuffle(order)
            for algorithm in order:
                t=measured(obj,algorithm)
                t.update({"stratum":s,"seed":row["seed"],"n":row["n"],
                          "instance_sha256":row["instance_sha256"],"repetition":rep,
                          "execution_order":order.index(algorithm)})
                if t["status"]!="success" or t["cost"]!=oracle:
                    raise AssertionError(("trial failure",t))
                out["trials"].append(t)
    summaries=[]
    for cell in out["cells"]:
        rows=[x for x in out["trials"] if x["instance_sha256"]==cell["instance_sha256"]]
        a,b=cell["algorithms"]
        xa={x["repetition"]:x["wall_seconds"] for x in rows if x["algorithm"]==a}
        xb={x["repetition"]:x["wall_seconds"] for x in rows if x["algorithm"]==b}
        pairs=[(xa[i],xb[i]) for i in sorted(set(xa)&set(xb))]
        summaries.append(dict(cell,comparison=stats(pairs,seed=cell["seed"]*101+cell["n"])))
    out["comparisons"]=summaries
    out["counts"]={"matched_cells":len(out["cells"]),
                   "negative_control_cells":len(out["negative_controls"]),
                   "measured_trials":len(out["trials"])}
    return out
def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--repetitions",type=int,default=REPS)
    parser.add_argument("--warmup",type=int,default=WARMUP)
    parser.add_argument("--output",default="prompt8_results.json")
    args=parser.parse_args()
    result=run(args.repetitions,args.warmup)
    with open(args.output,"w",encoding="utf-8") as f:
        json.dump(result,f,indent=2,sort_keys=True)
    print(json.dumps({"output":args.output,"counts":result["counts"],
                      "manifest_sha256":result["manifest_sha256"]}))
if __name__=="__main__":main()
