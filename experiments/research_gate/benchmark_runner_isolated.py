"""Resource-limited Prompt 9 rerun of unchanged frozen GoN benchmark v1."""
import argparse,json,os,platform,random,resource,subprocess,sys,time
from datetime import datetime,timezone
from experiments.research_gate.benchmark_v1 import manifest,verify
from experiments.research_gate.benchmark_runner_v1 import (
    decode,independent_oracle,negative_control,PAIRS,stats)
from experiments.research_gate.certified_repair_ucs import search
from experiments.research_gate.footprint_certificate import full_ucs,decomposed,replay
from experiments.research_gate.independent_replay import verify as verify_replay

TIMEOUT=60
MEMORY=2*1024**3
def limits():
    resource.setrlimit(resource.RLIMIT_AS,(MEMORY,MEMORY))
def worker(cell,algorithm,timeout=TIMEOUT):
    cmd=[sys.executable,"-m","experiments.research_gate.benchmark_trial_worker",
         "--cell",str(cell),"--algorithm",algorithm]
    start=time.perf_counter()
    try:
        p=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                         text=True,timeout=timeout,preexec_fn=limits)
    except subprocess.TimeoutExpired:
        return {"algorithm":algorithm,"status":"timeout","exception":"per-trial timeout",
                "wall_seconds":time.perf_counter()-start,"censored":True}
    elapsed=time.perf_counter()-start
    if p.returncode:
        reason="memory_or_process_error" if p.returncode<0 else "process_error"
        return {"algorithm":algorithm,"status":reason,"exception":p.stderr[-500:],
                "exit_code":p.returncode,"wall_seconds":elapsed,"censored":True}
    try:
        r=json.loads(p.stdout)
    except Exception:
        return {"algorithm":algorithm,"status":"invalid_output",
                "exception":p.stdout[-500:],"wall_seconds":elapsed,"censored":True}
    r["process_wall_seconds"]=elapsed
    r["exit_code"]=p.returncode
    r["censored"]=False
    return r

def run(repetitions=20,warmup=3):
    if repetitions<1 or warmup<0:raise ValueError("invalid repetition count")
    frozen=manifest();verify(frozen)
    out={"schema":"gon-prompt9-isolated-v1","manifest_sha256":frozen["manifest_sha256"],
         "source_commit":os.getenv("GITHUB_SHA","unknown"),
         "utc":datetime.now(timezone.utc).isoformat(),
         "environment":{"python":sys.version,"platform":platform.platform(),
                        "cpu":platform.processor(),"machine":platform.machine()},
         "resource_policy":{"timeout_seconds":TIMEOUT,"address_space_bytes":MEMORY,
                            "enforcement":"subprocess.run timeout and Linux RLIMIT_AS",
                            "memory_metric":"tracemalloc peak is Python allocations, not RSS"},
         "repetitions":repetitions,"warmup":warmup,"cells":[],"trials":[],"negative_controls":[]}
    for index,row in enumerate(frozen["instances"]):
        s=row["stratum"];obj=decode(row)
        cell={"stratum":s,"seed":row["seed"],"n":row["n"],
              "instance_sha256":row["instance_sha256"],
              "topology_sha256":row["topology_sha256"]}
        if s not in PAIRS:
            outcome=negative_control(row)
            out["negative_controls"].append(dict(cell,**outcome))
            if outcome["status"]!="correct_refusal":
                raise AssertionError(("unsafe refusal",cell))
            continue
        a,b=PAIRS[s]
        oracle=independent_oracle(obj,row["instance"]["model"])
        cell.update({"algorithms":[a,b],"oracle_cost":oracle})
        for alg in (a,b):
            ans=(search(obj,alg=="quotient_ucs") if alg in ("plain_ucs","quotient_ucs")
                 else full_ucs(obj) if alg=="full_ucs" else decomposed(obj))
            assert ans["cost"]==oracle,("oracle mismatch",cell,alg)
            if oracle is not None:
                if s=="fresh_symmetric":verify_replay(obj,ans["plan"],oracle)
                else:assert replay(obj,ans["plan"])==oracle
        out["cells"].append(cell)
        for _ in range(warmup):
            for alg in (a,b):
                w=worker(index,alg)
                if w["status"]!="success" or w["cost"]!=oracle:
                    raise AssertionError(("warmup failure",cell,w))
        for rep in range(repetitions):
            order=[a,b]
            random.Random(row["seed"]*100000+row["n"]*1000+rep+len(s)*31).shuffle(order)
            for position,alg in enumerate(order):
                t=worker(index,alg)
                t.update({"stratum":s,"seed":row["seed"],"n":row["n"],
                          "instance_sha256":row["instance_sha256"],
                          "repetition":rep,"execution_order":position})
                if t["status"]=="success" and t.get("cost")!=oracle:
                    t["status"]="incorrect_cost";t["exception"]="independent oracle disagreement"
                out["trials"].append(t)
    out["comparisons"]=[]
    for cell in out["cells"]:
        rows=[t for t in out["trials"] if t["instance_sha256"]==cell["instance_sha256"]]
        a,b=cell["algorithms"]
        first={t["repetition"]:t["wall_seconds"] for t in rows if t["algorithm"]==a and t["status"]=="success"}
        second={t["repetition"]:t["wall_seconds"] for t in rows if t["algorithm"]==b and t["status"]=="success"}
        pairs=[(first[k],second[k]) for k in sorted(set(first)&set(second))]
        out["comparisons"].append(dict(cell,comparison=stats(pairs,cell["seed"]*101+cell["n"]),
                                       censored_pairs=repetitions-len(pairs)))
    out["counts"]={"matched_cells":len(out["cells"]),
                   "negative_control_cells":len(out["negative_controls"]),
                   "measured_trials":len(out["trials"]),
                   "censored_trials":sum(t["status"]!="success" for t in out["trials"])}
    return out
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--repetitions",type=int,default=20)
    p.add_argument("--warmup",type=int,default=3)
    p.add_argument("--output",default="prompt9_results.json")
    args=p.parse_args()
    out=run(args.repetitions,args.warmup)
    with open(args.output,"w") as f:json.dump(out,f,sort_keys=True,indent=2)
    print(json.dumps(out["counts"],sort_keys=True))
if __name__=="__main__":main()
