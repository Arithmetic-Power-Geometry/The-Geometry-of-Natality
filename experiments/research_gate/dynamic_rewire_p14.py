"""Prompt 14: bounded dynamic directed relay rewiring with action-time NAC.
Independent shortest-path verification uses NetworkX on separately enumerated edges.
"""
from dataclasses import dataclass
from heapq import heappush,heappop
from itertools import product
import json
@dataclass(frozen=True)
class P:
    n:int=2
    capacity:int=2
    costs:tuple=(1,1,1,1)
    forbidden:tuple=()
    transient_forbid:bool=False
@dataclass(frozen=True)
class S:
    active:frozenset=frozenset()
    used:frozenset=frozenset()
    edges:frozenset=frozenset()
def legal(p,s):
    return len(s.active)<=p.capacity and s.active<=s.used and s.used<=set(range(p.n)) and all(
        u in s.active and (v=='t' or v in s.active) and u!=v for u,v in s.edges) and not (
        p.transient_forbid and {0,1}<=s.active)
def goal(p,s):
    if 0 not in s.active:return False
    seen={0}
    while True:
        nxt=seen|{v for u,v in s.edges if u in seen and v!='t'}
        if nxt==seen:break
        seen=nxt
    return any((u,'t') in s.edges for u in seen)
def successors(p,s):
    c,l,r,d=p.costs
    for i in range(p.n):
        if i not in s.used and len(s.active)<p.capacity:
            z=S(s.active|{i},s.used|{i},s.edges)
            if legal(p,z):yield ('create',i),z,c
    for u in s.active:
        for v in list(s.active)+['t']:
            if u==v:continue
            e=(u,v)
            if e not in s.edges and e not in p.forbidden:
                z=S(s.active,s.used,s.edges|{e})
                if legal(p,z):yield ('add',u,v),z,l
            if e in s.edges:yield ('remove',u,v),S(s.active,s.used,s.edges-{e}),r
        z=S(s.active-{u},s.used,frozenset((a,b) for a,b in s.edges if a!=u and b!=u))
        yield ('delete',u),z,d
def native(p):
    s0=S();dist={s0:0};q=[(0,0,s0)];counter=0
    while q:
        cost,_,s=heappop(q)
        if cost!=dist[s]:continue
        if goal(p,s):return cost,len(dist)
        for a,z,w in successors(p,s):
            if cost+w<dist.get(z,float('inf')):
                dist[z]=cost+w;counter+=1;heappush(q,(cost+w,counter,z))
    return None,len(dist)
def external(p):
    import networkx as nx
    g=nx.DiGraph();start=S();stack=[start];seen={start}
    while stack:
        s=stack.pop();g.add_node(s);candidates=[]
        for i in range(p.n):
            if i not in s.used and len(s.active)<p.capacity:
                z=S(s.active|{i},s.used|{i},s.edges)
                if legal(p,z):candidates.append((z,p.costs[0]))
        for u in s.active:
            for v in (*sorted(s.active),'t'):
                if u==v:continue
                e=(u,v)
                if e in s.edges:candidates.append((S(s.active,s.used,s.edges-{e}),p.costs[2]))
                elif e not in p.forbidden:candidates.append((S(s.active,s.used,s.edges|{e}),p.costs[1]))
            candidates.append((S(s.active-{u},s.used,frozenset((a,b) for a,b in s.edges if a!=u and b!=u)),p.costs[3]))
        for z,w in candidates:
            if g.has_edge(s,z):g[s][z]['weight']=min(w,g[s][z]['weight'])
            else:g.add_edge(s,z,weight=w)
            if z not in seen:seen.add(z);stack.append(z)
    distances=nx.single_source_dijkstra_path_length(g,start,weight='weight')
    values=[c for s,c in distances.items() if goal(p,s)]
    return (min(values) if values else None),len(g)
def run():
    p=P();s=S(frozenset(),frozenset({0}),frozenset())
    assert not any(a==('create',0) for a,_,_ in successors(p,s))
    q=P(forbidden=((0,1),));z=S(frozenset({0,1}),frozenset({0,1}),frozenset())
    assert not any(a==('add',0,1) for a,_,_ in successors(q,z))
    checked=0;unreachable=0
    for n,cap,cr,lk,rm,dl,forbid,liveguard in product((1,2),(0,1,2),(0,1),(0,1),(0,1),(0,1),(False,True),(False,True)):
        if cap>n:continue
        p=P(n,cap,(cr,lk,rm,dl),((0,'t'),) if forbid else (),liveguard)
        a=native(p);b=external(p)
        assert a[0]==b[0],(p,a,b)
        checked+=1
        if a[0] is None:unreachable+=1
    return {'checked':checked,'unreachable':unreachable,'matched':True,'external':'networkx','groove':False}
if __name__=='__main__':print(json.dumps(run(),indent=2))
