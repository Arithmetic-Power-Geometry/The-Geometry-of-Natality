"""Prompt 17: three-name shared-capacity GROOVE grammar and independent weighted oracles.

Closed fixed-node edge-only grammar. A live relay occupies one of two slots.
Relay 0 is initially live and unusable for target links; relays 1 and 2 each
serve their own terminal. The goal needs BOTH terminal links. Permanent
used-name history prevents re-creation. Costs are native edge-label metadata
(not GROOVE-native weighted rules): delete0=4, create1=2, create2=3,
link1=1, link2=2, unlink1=1, unlink2=1, delete1=1, delete2=1.
GROOVE validates UNWEIGHTED transitions; independent weighted shortest paths
on the matched transition systems validate costs. Do not conflate them.
"""
from __future__ import annotations
import heapq
import itertools
import json
from collections import deque
from pathlib import Path
from groove_minimal_fixture import write_graph
from groove_rule_equivalence_oracle import read_edges, rewrite

ROOT=Path("experiments/research_gate/gon_three_relay_capacity.gps")
NODES=("n0","n1","n2","t1","t2")
COSTS={"delete0":4,"create1":2,"create2":3,
       "link1":1,"link2":2,"unlink1":1,"unlink2":1,
       "delete1":1,"delete2":1}
TYPES=[(x,x,"Relay"+x[-1]) for x in ("n0","n1","n2")]+[
    ("t1","t1","Terminal1"),("t2","t2","Terminal2")]

def make_grammar():
    ROOT.mkdir(parents=True,exist_ok=True)
    start=TYPES+[("n0","n0","used"),("n0","n0","live")]
    write_graph(ROOT/"start.gst","start","graph",NODES,start)
    rules={}
    # A fixed-node NAC on *both* other live names implements capacity <=2.
    # To create relay i, require at least one of the other two names NOT live.
    # GROOVE NAC cannot express a disjunction directly; split each creation
    # into two named variants (first absent, second absent), allowing overlap.
    # This yields duplicated labelled arcs on states with both absent, which
    # are deduplicated after mapping variants to the same semantic action.
    for i in (1,2):
        for j in (0,1,2):
            if j==i:continue
            name=f"create{i}_absent{j}"
            edges=[("n"+str(i),"n"+str(i),"Relay"+str(i)),
                   ("n"+str(i),"n"+str(i),"not:used"),
                   ("n"+str(j),"n"+str(j),"Relay"+str(j)),
                   ("n"+str(j),"n"+str(j),"not:live"),
                   ("n"+str(i),"n"+str(i),"new:used"),
                   ("n"+str(i),"n"+str(i),"new:live")]
            rules[name]=edges
        edges=[("n"+str(i),"n"+str(i),"Relay"+str(i)),
               ("n"+str(i),"n"+str(i),"live"),
               ("t"+str(i),"t"+str(i),"Terminal"+str(i)),
               ("n"+str(i),"t"+str(i),"not:linked"),
               ("n"+str(i),"t"+str(i),"new:linked")]
        rules[f"link{i}"]=edges
        rules[f"unlink{i}"]=[("n"+str(i),"n"+str(i),"Relay"+str(i)),
                ("n"+str(i),"n"+str(i),"live"),
                ("t"+str(i),"t"+str(i),"Terminal"+str(i)),
                ("n"+str(i),"t"+str(i),"del:linked")]
        rules[f"delete{i}"]=[("n"+str(i),"n"+str(i),"Relay"+str(i)),
                ("n"+str(i),"n"+str(i),"del:live"),
                ("t"+str(i),"t"+str(i),"Terminal"+str(i)),
                ("n"+str(i),"t"+str(i),"not:linked")]
    rules["delete0"]=[("n0","n0","Relay0"),("n0","n0","del:live")]
    for name,edges in sorted(rules.items()):
        write_graph(ROOT/(name+".gpr"),name,"rule",NODES,edges)
    (ROOT/"system.properties").write_text(
        "startGraph=start\nenableControl=false\nuseStoredNodeIDs=true\n"
        "grammarVersion=3.10\ngrooveVersion=6.8.0\n"
        "remark=Three relays, two terminals, capacity two and action-time guards\n")
    return rules

def canonical_rule(name):
    return name.split("_absent")[0]

def native_successors(s):
    used,live,linked=s
    for i in (1,2):
        bit=1<<i
        if not used&bit and live.bit_count()<2:
            yield f"create{i}",(used|bit,live|bit,linked)
        if live&bit and not linked&bit:
            yield f"link{i}",(used,live,linked|bit)
        if linked&bit:
            yield f"unlink{i}",(used,live,linked&~bit)
        if live&bit and not linked&bit:
            yield f"delete{i}",(used,live&~bit,linked)
    if live&1:
        yield "delete0",(used,live&~1,linked)

def native_explore():
    start=(1,1,0)
    q=deque([start]);seen={start};arcs=set()
    while q:
        s=q.popleft()
        for label,t in native_successors(s):
            arcs.add((s,label,t))
            if t not in seen:seen.add(t);q.append(t)
    return start,seen,arcs

def project(graph):
    used=sum(1<<i for i in range(3) if (f"n{i}",f"n{i}","used") in graph)
    live=sum(1<<i for i in range(3) if (f"n{i}",f"n{i}","live") in graph)
    linked=sum(1<<i for i in (1,2) if (f"n{i}",f"t{i}","linked") in graph)
    return used,live,linked

def xml_explore():
    start=frozenset(read_edges(ROOT/"start.gst"))
    rules={p.stem:read_edges(p) for p in ROOT.glob("*.gpr")}
    q=deque([start]);seen={start};arcs=set()
    while q:
        s=q.popleft()
        for rule,edges in rules.items():
            t=rewrite(s,edges)
            if t is None:continue
            arcs.add((project(s),canonical_rule(rule),project(t)))
            if t not in seen:seen.add(t);q.append(t)
    return project(start),{project(s) for s in seen},arcs

def shortest(start,arcs):
    outgoing={}
    for s,label,t in arcs:
        outgoing.setdefault(s,[]).append((label,t))
    dist={start:0};plans={start:()};counter=itertools.count()
    q=[(0,next(counter),start)]
    while q:
        d,_,s=heapq.heappop(q)
        if d!=dist[s]:continue
        if s[2]&6==6:
            return d,plans[s]
        for label,t in outgoing.get(s,()):
            nd=d+COSTS[label]
            if nd<dist.get(t,10**10):
                dist[t]=nd;plans[t]=plans[s]+(label,)
                heapq.heappush(q,(nd,next(counter),t))
    return None,()

def bellman_ford(start,states,arcs):
    dist={s:float("inf") for s in states}
    dist[start]=0
    for _ in range(len(states)-1):
        changed=False
        for s,label,t in sorted(arcs):
            v=dist[s]+COSTS[label]
            if v<dist[t]:
                dist[t]=v;changed=True
        if not changed:break
    return min((dist[s] for s in states if s[2]&6==6),default=float("inf"))

def main():
    rules=make_grammar()
    n0,ns,na=native_explore()
    x0,xs,xa=xml_explore()
    assert n0==x0 and ns==xs,(len(ns),len(xs),ns^xs)
    assert na==xa,(len(na),len(xa),na^xa)
    assert all(s[1].bit_count()<=2 and s[2]&~s[1]==0 and s[1]&~s[0]==0 for s in ns)
    d1,p1=shortest(n0,na)
    d2,p2=shortest(x0,xa)
    d3=bellman_ford(n0,ns,na)
    assert d1==d2==d3==12,(d1,d2,d3)
    assert "delete0" in p1 and "create1" in p1 and "create2" in p1,p1
    summary={"grammar":ROOT.name,"rule_files":len(rules),"states":len(ns),
        "labelled_arcs":len(na),"independent_xml_oracle":"exact",
        "native_dijkstra_cost":d1,"xml_dijkstra_cost":d2,
        "independent_bellman_ford_cost":d3,"example_optimal_plan":p1,
        "goal":"both terminal links present","live_capacity":2,
        "costs":COSTS,"limitation":"GROOVE executes unweighted rules; weighted costs checked externally"}
    print(json.dumps(summary,indent=2))
if __name__=="__main__":main()
