"""Matched, deterministic research-stage benchmark; no publication speedup claim."""
import json,platform,sys
from datetime import datetime,timezone
from pathlib import Path
from experiments.research_gate.certified_repair_ucs import Grammar,measured,exhaustive
from experiments.research_gate.independent_replay import verify

def run():
    rows=[]
    for n in range(1,5):
        for target in range(1,min(n,3)+1):
            g=Grammar(names=tuple("r"+str(i) for i in range(n)),
                      target=target,restore_cost=20,capacity=n,budget=20)
            oracle=exhaustive(g)
            plain=measured(g,False)
            orbit=measured(g,True)
            assert plain["cost"]==orbit["cost"]==oracle["cost"]
            for result in (plain,orbit):
                if result["cost"] is not None:
                    verify(g,result["plan"],result["cost"])
            def pack(result):
                return {k:v for k,v in result.items() if k!="plan"}
            rows.append(dict(n=n,target=target,oracle_cost=oracle["cost"],
                             oracle_visits=oracle["visits"],plain=pack(plain),
                             quotient=pack(orbit)))
    return {"status":"synthetic demonstration; no external baseline",
            "timestamp_utc":datetime.now(timezone.utc).isoformat(),
            "python":sys.version,"platform":platform.platform(),
            "cases":len(rows),"rows":rows,
            "warnings":["timings are single-run and lack uncertainty",
                        "tracemalloc captures Python allocations, not process RSS",
                        "canonicalization is factorial and may dominate runtime",
                        "not a matched GROOVE or realistic workload comparison"]}

if __name__=="__main__":
    result=run()
    path=Path("experiments/research_gate/prompt3_benchmark_results.json")
    path.write_text(json.dumps(result,indent=2,default=str)+"\n")
    print(json.dumps({"cases":result["cases"],"all_costs_agree":True,
                      "output":str(path)},indent=2))
