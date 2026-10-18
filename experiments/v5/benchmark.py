"""GoN V5 exact baseline: disjoint birth–activation modules vs knapsack DP.
Python 3 standard library. Exhaustive subset search is limited to m<=16.
"""
import csv,json,random,time,itertools
from pathlib import Path
HERE=Path(__file__).resolve().parent
def brute(items,budget):
    best=0
    for mask in range(1<<len(items)):
        cost=reward=0
        for i,(w,r) in enumerate(items):
            if mask>>i&1:cost+=w;reward+=r
        if cost<=budget:best=max(best,reward)
    return best
def dp(items,budget):
    arr=[0]*(budget+1)
    for w,r in items:
        for b in range(budget,w-1,-1):
            arr[b]=max(arr[b],arr[b-w]+r)
    return arr[budget]
def run():
    rows=[]
    for m in (6,8,10,12,14,16):
        for seed in range(25):
            rng=random.Random(500000+m*1000+seed)
            items=[(rng.randint(2,12),rng.randint(1,8)) for _ in range(m)]
            budget=sum(w for w,_ in items)//3
            t=time.perf_counter();b=brute(items,budget);tb=time.perf_counter()-t
            t=time.perf_counter();d=dp(items,budget);td=time.perf_counter()-t
            assert b==d
            rows.append(dict(modules=m,seed=seed,budget=budget,optimal_natality=b,brute_seconds=round(tb,8),dp_seconds=round(td,8),match=b==d))
    with (HERE/'results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    summary=dict(instances=len(rows),all_exact_matches=all(r['match'] for r in rows),sizes=[6,8,10,12,14,16],seeds_per_size=25,comparison='classical 0-1 knapsack DP vs exhaustive module-subset enumeration',note='Timing is exploratory, not a novel performance claim')
    (HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':run()
