"""Exact GoN tree-activation DP versus exhaustive enumeration. Python stdlib."""
import csv,json,random,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
def brute(parent,cost,value,B):
    n=len(parent);best=0
    for mask in range(1<<(n-1)):
        chosen={0}|{v for v in range(1,n) if mask>>(v-1)&1}
        if any(parent[v] not in chosen for v in chosen if v):continue
        if sum(cost[v] for v in chosen)<=B:best=max(best,sum(value[v] for v in chosen))
    return best
def solve(parent,cost,value,B):
    n=len(parent);children=[[] for _ in range(n)]
    for v in range(1,n):children[parent[v]].append(v)
    neg=-10**12
    def visit(v):
        d=[value[v] if b>=cost[v] else neg for b in range(B+1)]
        for u in children[v]:
            child=visit(u);new=[neg]*(B+1)
            for b in range(B+1):
                for j in range(b+1):
                    if d[b-j]!=neg:
                        new[b]=max(new[b],d[b-j]+max(0,child[j]))
            d=new
        return d
    return visit(0)[B]
def run():
    rows=[]
    for n in (6,8,10,12,14):
        for seed in range(30):
            r=random.Random(600000+n*1000+seed)
            parent=[-1]+[r.randrange(v) for v in range(1,n)]
            cost=[0]+[r.randint(1,5) for _ in range(1,n)]
            value=[0]+[r.randint(0,9) for _ in range(1,n)]
            B=sum(cost)//2
            t=time.perf_counter();b=brute(parent,cost,value,B);bt=time.perf_counter()-t
            t=time.perf_counter();d=solve(parent,cost,value,B);dt=time.perf_counter()-t
            assert b==d,(n,seed,b,d)
            rows.append(dict(vertices=n,seed=seed,budget=B,optimum=d,exact_match=True,brute_seconds=round(bt,8),dp_seconds=round(dt,8)))
    with (HERE/'results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    summary=dict(instances=len(rows),all_exact_matches=True,sizes=[6,8,10,12,14],seeds_per_size=30,method='tree DP versus exhaustive ancestor-closed subsets',note='one-run exploratory timing, not evidence of new algorithmic novelty')
    (HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':run()
