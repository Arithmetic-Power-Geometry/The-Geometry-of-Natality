"""Prompt 13 bounded dynamic creation/rewrite/delete with action-time NAC.

Distinct from Prompt 12 static MILP: names are allocated at creation, links can
be rewired, and deleting a relay frees a slot. Finite closed grammar only.
"""
from dataclasses import dataclass
from itertools import product
from heapq import heappush,heappop
import json

@dataclass(frozen=True)
class Problem:
    names: int
    targets: int
    capacity: int
    create_cost: int=1
    link_cost: int=1
    delete_cost: int=1
    forbid_pair: tuple=(-1,-1)

@dataclass(frozen=True)
class State:
    active: frozenset=frozenset()
    links: frozenset=frozenset()
    used: frozenset=frozenset()

def valid(p):
    if not (1<=p.names<=4 and 1<=p.targets<=3 and 0<=p.capacity<=p.names):
        raise ValueError("bounded grammar")
    if min(p.create_cost,p.link_cost,p.delete_cost)<0:raise ValueError("negative cost")
    a,b=p.forbid_pair
    if (a,b)!=(-1,-1) and not (0<=a<b<p.names):raise ValueError("invalid NAC")

def legal(p,s):
    a,b=p.forbid_pair
    return (len(s.active)<=p.capacity and
        s.active<=set(range(p.names)) and
        s.used<=set(range(p.names)) and
        s.active<=s.used and
        all(i in s.active and 0<=t<p.targets for i,t in s.links) and
        (a<0 or not (a in s.active and b in s.active)))

def goal(p,s):
    return all(any(i in s.active and (i,t) in s.links for i in s.active)
               for t in range(p.targets))

def actions(p,s):
    # Unique name allocation: a name can be created only once, even after delete.
    for i in range(p.names):
        if i not in s.used and len(s.active)<p.capacity:
            ns=State(s.active|{i},s.links,s.used|{i})
            if legal(p,ns):yield ("create",i,-1),ns,p.create_cost
    for i in sorted(s.active):
        for t in range(p.targets):
            if (i,t) not in s.links:
                ns=State(s.active,s.links|{(i,t)},s.used)
                yield ("link",i,t),ns,p.link_cost
            else:
                ns=State(s.active,s.links-{(i,t)},s.used)
                yield ("unlink",i,t),ns,p.link_cost
        ns=State(s.active-{i},frozenset((j,t) for j,t in s.links if j!=i),s.used)
        yield ("delete",i,-1),ns,p.delete_cost

def dijkstra(p):
    valid(p);start=State();q=[(0,0,start,())];dist={start:0};counter=0
    while q:
        cost,_,s,plan=heappop(q)
        if cost!=dist[s]:continue
        if goal(p,s):return {"cost":cost,"plan":plan,"states":len(dist)}
        for act,ns,c in actions(p,s):
            if cost+c<dist.get(ns,float("inf")):
                dist[ns]=cost+c;counter+=1
                heappush(q,(cost+c,counter,ns,plan+(act,)))
    return {"cost":None,"plan":(),"states":len(dist)}

def independent_graph(p):
    """Independent state graph enumerator via explicit Cartesian state encoding.

    Does not call actions(), dijkstra() or goal(); constructs edges separately.
    """
    valid(p)
    import networkx as nx
    graph=nx.DiGraph();start=State();graph.add_node(start)
    frontier=[start];seen={start}
    while frontier:
        s=frontier.pop()
        if len(s.active)<p.capacity:
            for i in range(p.names):
                if i not in s.used:
                    ns=State(s.active|{i},s.links,s.used|{i})
                    if legal(p,ns):graph.add_edge(s,ns,weight=p.create_cost)
                    else:continue
                    if ns not in seen:seen.add(ns);frontier.append(ns)
        for i in s.active:
            for t in range(p.targets):
                if (i,t) in s.links:ns=State(s.active,s.links-{(i,t)},s.used)
                else:ns=State(s.active,s.links|{(i,t)},s.used)
                graph.add_edge(s,ns,weight=p.link_cost)
                if ns not in seen:seen.add(ns);frontier.append(ns)
            ns=State(s.active-{i},frozenset((j,t) for j,t in s.links if j!=i),s.used)
            graph.add_edge(s,ns,weight=p.delete_cost)
            if ns not in seen:seen.add(ns);frontier.append(ns)
    lengths=nx.single_source_dijkstra_path_length(graph,start,weight="weight")
    feasible=[c for s,c in lengths.items() if all(any((i,t) in s.links for i in s.active) for t in range(p.targets))]
    return {"cost":min(feasible) if feasible else None,"states":len(graph),"edges":graph.number_of_edges()}

def counterexamples():
    # H1 false: deleting then recreating same identity is forbidden by used history.
    p=Problem(1,1,1)
    s=State(frozenset(),frozenset(),frozenset({0}))
    assert list(actions(p,s))==[]
    # H2 false: a NAC can make two simultaneously created names impossible.
    q=Problem(2,1,2,forbid_pair=(0,1))
    a=State(frozenset({0}),frozenset(),frozenset({0}))
    assert not any(act[0]=="create" and act[1]==1 for act,_,_ in actions(q,a))
    # H3 true conditional: nonnegative unlink/delete never needed for minimum
    # cost in this *monotone goal, fixed-template* grammar. Proof in report.
    return {"H1":"identity reuse after deletion rejected by creation history",
            "H2":"NAC forbids second simultaneous relay",
            "H3":"delete and unlink can be eliminated from optimal plans in this restricted grammar"}

def sweep():
    checked=0;unreachable=0
    for n,t,cap,cc,lc,dc in product((1,2,3),(1,2),(0,1,2),(0,1,2),(0,1,2),(0,1)):
        if cap>n:continue
        for nac in ((-1,-1),((0,1) if n>=2 else (-1,-1))):
            p=Problem(n,t,cap,cc,lc,dc,nac)
            a=dijkstra(p);b=independent_graph(p)
            assert a["cost"]==b["cost"],(p,a,b)
            checked+=1
            if a["cost"] is None:unreachable+=1
    return {"checked":checked,"unreachable":unreachable,"matched":True,
            "external":"networkx single_source_dijkstra_path_length"}

if __name__=="__main__":print(json.dumps({"counterexamples":counterexamples(),"sweep":sweep()},indent=2))
