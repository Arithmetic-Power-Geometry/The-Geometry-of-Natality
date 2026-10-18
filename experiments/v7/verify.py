"""GoN V7: exact cyclic prerequisite optimization vs SCC condensation.
Standard library; exhaustive enumeration for small n.
"""
import csv,json,random
from pathlib import Path
HERE=Path(__file__).resolve().parent
def scc(n,edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v)
    reach=[]
    for v in range(n):
        seen={v};stack=[v]
        while stack:
            u=stack.pop()
            for z in adj[u]:
                if z not in seen:seen.add(z);stack.append(z)
        reach.append(seen)
    parts=[];used=set()
    for v in range(n):
        if v not in used:
            comp={u for u in range(n) if u in reach[v] and v in reach[u]}
            used|=comp;parts.append(comp)
    return parts
def optimum(n,edges,cost,reward,budget):
    best=0
    for mask in range(1<<n):
        if any((mask>>v&1) and not (mask>>u&1) for u,v in edges):continue
        if sum(cost[v] for v in range(n) if mask>>v&1)>budget:continue
        best=max(best,sum(reward[v] for v in range(n) if mask>>v&1))
    return best
def reduced(n,edges,cost,reward,budget):
    parts=scc(n,edges);idx={v:i for i,C in enumerate(parts) for v in C}
    ce={(idx[u],idx[v]) for u,v in edges if idx[u]!=idx[v]}
    cc=[sum(cost[v] for v in C) for C in parts]
    rr=[sum(reward[v] for v in C) for C in parts]
    return optimum(len(parts),ce,cc,rr,budget),len(parts)
def run():
    rows=[]
    for n in (4,6,8,10):
        for seed in range(50):
            r=random.Random(700000+n*1000+seed)
            edges={(u,v) for u in range(n) for v in range(n) if u!=v and r.random()<0.22}
            cost=[r.randint(1,5) for _ in range(n)]
            reward=[r.randint(0,8) for _ in range(n)]
            budget=sum(cost)//2
            baseline=optimum(n,edges,cost,reward,budget)
            contracted,q=reduced(n,edges,cost,reward,budget)
            assert baseline==contracted,(n,seed,baseline,contracted)
            rows.append(dict(n=n,seed=seed,edges=len(edges),scc_count=q,budget=budget,optimum=baseline,exact_match=True))
    with (HERE/'results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    summary=dict(instances=len(rows),exact_matches=len(rows),failures=0,sizes=[4,6,8,10],seeds_per_size=50,comparison='exhaustive original graph versus exhaustive SCC condensation',novelty='no new performance or priority claim')
    (HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':run()
