"""GoN V15: exhaustive n=4 degree-signature non-identifiability.
No external packages required.
"""
import json
from pathlib import Path
N=4
ARCS=[(u,v) for u in range(N) for v in range(N) if u!=v]
G={(0,1),(1,3),(2,0)}
H={(0,3),(1,0),(2,1)}
def sig(edges):
    out=[0]*N;inn=[0]*N
    for u,v in edges:out[u]+=1;inn[v]+=1
    return tuple(out),tuple(inn)
def reachable(edges,root=0):
    q=[root];seen={root}
    for u in q:
        for a,b in edges:
            if a==u and b not in seen:seen.add(b);q.append(b)
    return seen
def dag(edges):
    indeg=[0]*N;adj=[[] for _ in range(N)]
    for u,v in edges:indeg[v]+=1;adj[u].append(v)
    q=[u for u in range(N) if indeg[u]==0];count=0
    for u in q:
        count+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    return count==N
def main():
    assert sig(G)==sig(H)==((1,1,1,0),(1,1,0,1))
    assert reachable(G)=={0,1,3} and reachable(H)=={0,3}
    assert dag(G) and dag(H)
    first={};pairs=0;graphs=0
    for mask in range(1<<len(ARCS)):
        edges={arc for j,arc in enumerate(ARCS) if mask>>j&1}
        key=sig(edges);r=len(reachable(edges));graphs+=1
        if key in first and first[key][0]!=r:pairs+=1
        elif key not in first:first[key]=(r,mask)
    assert graphs==4096 and pairs>0
    result={'graphs_enumerated':graphs,'signature_collisions_with_distinct_reachability':pairs,'witness_G':sorted(G),'witness_H':sorted(H),'root':0,'reach_G':3,'reach_H':2,'same_labelled_degrees':True,'both_DAG_cospectral':True,'failures':0,'novelty':'not established'}
    (Path(__file__).parent/'summary.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
