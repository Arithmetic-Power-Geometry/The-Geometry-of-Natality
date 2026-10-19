"""Independent Prompt 9 audit; does not import benchmark runner statistics."""
import argparse,collections,hashlib,json,math,random,statistics
from pathlib import Path
from experiments.research_gate.benchmark_v1 import manifest,verify

def qtile(values,q):
    v=sorted(values)
    if not v:return None
    z=q*(len(v)-1);lo=int(z);hi=min(lo+1,len(v)-1)
    if lo==hi:return v[lo]
    return v[lo]*(hi-z)+v[hi]*(z-lo)
def boot_ci(values,seed,draws=1000):
    if not values:return [None,None]
    rng=random.Random(seed)
    samples=[]
    for _ in range(draws):
        samples.append(statistics.median([values[rng.randrange(len(values))] for _ in values]))
    return [qtile(samples,.025),qtile(samples,.975)]
def audit(data,require_full=True):
    frozen=manifest();verify(frozen)
    if data["manifest_sha256"]!=frozen["manifest_sha256"]:
        raise AssertionError("frozen manifest mismatch")
    expected={r["instance_sha256"]:r for r in frozen["instances"]}
    cells=data["cells"];trials=data["trials"];neg=data["negative_controls"]
    if len(cells)!=36 or len(neg)!=36:raise AssertionError("cell count mismatch")
    for n in neg:
        if n["status"]!="correct_refusal" or n["instance_sha256"] not in expected:
            raise AssertionError("unsafe negative control")
    repetitions=data["repetitions"]
    expected_keys=set()
    for cell in cells:
        row=expected[cell["instance_sha256"]]
        if row["stratum"]!=cell["stratum"] or row["seed"]!=cell["seed"] or row["n"]!=cell["n"]:
            raise AssertionError("cell metadata mismatch")
        for alg in cell["algorithms"]:
            for rep in range(repetitions):
                expected_keys.add((cell["instance_sha256"],alg,rep))
    found={}
    for t in trials:
        key=(t["instance_sha256"],t["algorithm"],t["repetition"])
        if key not in expected_keys or key in found:
            raise AssertionError("duplicate or unexpected trial")
        found[key]=t
        if t["status"]=="success":
            if not math.isfinite(t["wall_seconds"]) or t["wall_seconds"]<0:
                raise AssertionError("invalid timing")
            c=next(c for c in cells if c["instance_sha256"]==t["instance_sha256"])
            if t["cost"]!=c["oracle_cost"]:raise AssertionError("cost disagreement")
    if require_full and set(found)!=expected_keys:
        raise AssertionError("missing trials")
    summaries=[]
    for c in cells:
        a,b=c["algorithms"];h=c["instance_sha256"]
        matched=[]
        for rep in range(repetitions):
            x=found.get((h,a,rep));y=found.get((h,b,rep))
            if x and y and x["status"]==y["status"]=="success":
                matched.append(x["wall_seconds"]-y["wall_seconds"])
        if require_full and len(matched)!=repetitions:
            raise AssertionError("missing successful paired trial")
        summaries.append({"stratum":c["stratum"],"n":c["n"],"seed":c["seed"],
                          "instance_sha256":h,"pairs":len(matched),
                          "median_difference_seconds":statistics.median(matched) if matched else None,
                          "iqr_difference_seconds":[qtile(matched,.25),qtile(matched,.75)],
                          "bootstrap95_median_difference_seconds":boot_ci(matched,c["seed"]*101+c["n"]),
                          "censored_pairs":repetitions-len(matched)})
    strata={}
    for s in sorted({c["stratum"] for c in cells}):
        values=[x["median_difference_seconds"] for x in summaries
                if x["stratum"]==s and x["median_difference_seconds"] is not None]
        strata[s]={"instances":len(values),"median_of_instance_medians_seconds":
                   statistics.median(values) if values else None}
    return {"manifest_sha256":frozen["manifest_sha256"],
            "audited_trials":len(trials),"expected_trials":len(expected_keys),
            "successes":sum(t["status"]=="success" for t in trials),
            "censored":sum(t["status"]!="success" for t in trials),
            "strata":strata,"comparisons":summaries,
            "audit_status":"complete" if set(found)==expected_keys else "incomplete"}
def figure(audit_result,path):
    """Dependency-free SVG, displaying instance-level median differences in ms."""
    rows=list(sorted(audit_result["strata"].items()))
    width,height=900,100+len(rows)*90
    scale=13000
    x0=450
    lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
           '<rect width="100%" height="100%" fill="white"/>',
           '<text x="20" y="28" font-family="sans-serif" font-size="17">Median paired runtime difference by stratum (ms)</text>',
           '<text x="20" y="49" font-family="sans-serif" font-size="12">First minus second algorithm; negative = second is slower. Synthetic CI-host data.</text>',
           f'<line x1="{x0}" y1="65" x2="{x0}" y2="{height-18}" stroke="#555" stroke-width="1"/>']
    for i,(name,val) in enumerate(rows):
        y=92+i*90
        delta=1000*val["median_of_instance_medians_seconds"] if val["median_of_instance_medians_seconds"] is not None else 0
        end=max(225,min(850,x0+delta*scale/1000))
        lines.append(f'<text x="20" y="{y+5}" font-family="sans-serif" font-size="15">{name}</text>')
        lines.append(f'<line x1="{min(x0,end):.1f}" y1="{y}" x2="{max(x0,end):.1f}" y2="{y}" stroke="#32659b" stroke-width="12"/>')
        lines.append(f'<text x="{end+8:.1f}" y="{y-10}" font-family="sans-serif" font-size="13">{delta:+.3f} ms</text>')
    lines.append('</svg>')
    Path(path).write_text("\n".join(lines),encoding="utf-8")
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True)
    p.add_argument("--output",required=True)
    p.add_argument("--figure",required=True)
    p.add_argument("--allow-censored",action="store_true")
    a=p.parse_args()
    data=json.loads(Path(a.input).read_text())
    result=audit(data,require_full=not a.allow_censored)
    Path(a.output).write_text(json.dumps(result,indent=2,sort_keys=True))
    figure(result,a.figure)
    print(json.dumps({"status":result["audit_status"],"strata":result["strata"],
                      "successes":result["successes"],"censored":result["censored"]}))
if __name__=="__main__":main()
