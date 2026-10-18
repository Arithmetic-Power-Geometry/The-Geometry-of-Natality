"""Exhaustive check of exact natality signature realizability, n=2,3,4."""
import csv,json
from pathlib import Path
OUT=Path(__file__).resolve().parent
def reach(n,edges,start=0):
    seen={start};queue=[start]
    for u in queue:
        for a,b in edges:
            if a==u and b not in seen:seen.add(b);queue.append(b)
    return seen
def signature(n,base,c,added):
    old=reach(n,base);new=reach(n+c,base|added)
    return (len((new&set(range(n)))-old),len(new-set(range(n))),c)
def main():
    rows=[];checks=0
    for n in (2,3,4):
        arcs=[(u,v) for u in range(n) for v in range(n) if u!=v]
        for bits in range(1<<len(arcs)):
            base={e for i,e in enumerate(arcs) if bits>>i&1}
            old=reach(n,base)
            inaccessible=[v for v in range(n) if v not in old]
            h=len(inaccessible);closed=0
            for mask in range(1<<h):
                W={v for j,v in enumerate(inaccessible) if mask>>j&1}
                if any(not (reach(n,base,v)-old)<=W for v in W):continue
                closed+=1
                for c in range(3):
                    for g in range(c+1):
                        added={(0,v) for v in W}|{(0,n+j) for j in range(g)}
                        observed=signature(n,base,c,added)
                        assert observed==(len(W),g,c),(n,bits,W,g,c,observed)
                        checks+=1
            rows.append(dict(n=n,graph_mask=bits,edges=len(base),initial_reachable=len(old),horizon=h,closed_subsets=closed,constructive_checks=closed*6))
    with (OUT/'exhaustive_results.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
    summary=dict(graphs=len(rows),constructive_signatures_checked=checks,all_passed=True,n_counts={str(n):sum(x['n']==n for x in rows) for n in (2,3,4)},closed_subset_count=sum(x['closed_subsets'] for x in rows),scope='constructive sufficiency, not independent mathematical novelty')
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
