import csv,random,time,statistics,json,collections
from pathlib import Path
OUT=Path(__file__).resolve().parent

def reach(adj,s):
    seen={s};q=collections.deque([s])
    while q:
        for v in adj[q.popleft()]:
            if v not in seen:seen.add(v);q.append(v)
    return seen

def make_graph(kind,n,seed):
    r=random.Random(seed);a=[set() for _ in range(n)]
    if kind=='erdos_renyi':
        p=2.0/n
        for u in range(n):
            for v in range(n):
                if u!=v and r.random()<p:a[u].add(v)
    elif kind=='dag':
        for u in range(n):
            for v in range(u+1,n):
                if r.random()<3/n:a[u].add(v)
    elif kind=='block':
        for u in range(n):
            for v in range(n):
                if u!=v and r.random()<(4/n if u//(n//4)==v//(n//4) else .15/n):a[u].add(v)
    elif kind=='chain':
        for u in range(n-1):a[u].add(u+1)
        for u in range(n):
            for v in range(n):
                if u!=v and v>u and r.random()<.4/n:a[u].add(v)
    elif kind=='scc_blocks':
        for start in range(0,n,5):
            vertices=list(range(start,min(n,start+5)))
            for j,v in enumerate(vertices):a[v].add(vertices[(j+1)%len(vertices)])
            if len(vertices)==1:a[v].discard(v)
        for u in range(n):
            for v in range(n):
                if u//5 !=v//5 and r.random()<.3/n:a[u].add(v)
    return a

def run_graph(kind,n,seed):
    a=make_graph(kind,n,seed);s=0;base=reach(a,s)
    candidates=[(u,v) for u in base for v in range(n) if v not in base and v not in a[u]]
    t=time.perf_counter()
    potentials={v:len(reach(a,v)-base) for v in range(n) if v not in base}
    fast_time=time.perf_counter()-t
    fast_best=max(potentials.values(),default=0)
    t=time.perf_counter();exact_best=0;exact_edge=None
    for u,v in candidates:
        a[u].add(v);gain=len(reach(a,s))-len(base);a[u].remove(v)
        if gain>exact_best:exact_best=gain;exact_edge=(u,v)
    exhaustive_time=time.perf_counter()-t
    assert fast_best==exact_best
    return dict(family=kind,n=n,seed=seed,edges=sum(map(len,a)),initial_reachable=len(base),candidates=len(candidates),optimal_gain=fast_best,final_reachable=len(base)+fast_best,fast_seconds=round(fast_time,8),exhaustive_seconds=round(exhaustive_time,8),speed_ratio=round(exhaustive_time/fast_time,3) if fast_time else None,optimal_edge=str(exact_edge),equivalent=True)

def main():
    rows=[];kinds=['erdos_renyi','dag','block','chain','scc_blocks'];sizes=[12,18,24,30]
    for kind in kinds:
        for n in sizes:
            for seed in range(50):
                rows.append(run_graph(kind,n,seed+100000))
    with (OUT/'results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    groups=[]
    for kind in kinds:
        subset=[x for x in rows if x['family']==kind]
        groups.append(dict(family=kind,graphs=len(subset),mean_gain=round(statistics.mean(x['optimal_gain'] for x in subset),3),mean_initial=round(statistics.mean(x['initial_reachable'] for x in subset),3),mean_final=round(statistics.mean(x['final_reachable'] for x in subset),3),mean_speed_ratio=round(statistics.mean(x['speed_ratio'] for x in subset),3),total_fast_seconds=round(sum(x['fast_seconds'] for x in subset),6),total_exhaustive_seconds=round(sum(x['exhaustive_seconds'] for x in subset),6)))
    summary=dict(count=len(rows),all_exact_matches=all(x['equivalent'] for x in rows),families=groups,nonzero_gain=sum(x['optimal_gain']>0 for x in rows),total_fast_seconds=round(sum(x['fast_seconds'] for x in rows),6),total_exhaustive_seconds=round(sum(x['exhaustive_seconds'] for x in rows),6),seed_range='100000..100049',python='stdlib only',note='Timings include Python BFS but exclude graph generation. Identical objective and optimum; algorithmic speedup is from grouping equivalent edge targets, not novel mathematics.')
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
