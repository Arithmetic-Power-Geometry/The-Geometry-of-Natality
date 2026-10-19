"""Independent finite graph-rule interpreter for the two committed GROOVE fixtures.

Reads .gst/.gpr XML as independent evidence of actual rule labels, applies
fixed-node edge additions/deletions/NACs, and compares *labelled* transitions
against a separately specified native finite-state oracle. This interpreter
covers only the restricted edge-only grammar; not general GROOVE matching.
"""
import json
from collections import deque
from pathlib import Path
from xml.etree import ElementTree as ET

BASE=Path("experiments/research_gate")
NS={"g":"http://www.gupro.de/GXL/gxl-1.0.dtd"}

def read_edges(path):
    root=ET.parse(path).getroot()
    edges=[]
    for e in root.findall(".//g:edge",NS):
        label=e.find("./g:attr[@name='label']/g:string",NS)
        assert label is not None,(path,ET.tostring(e))
        edges.append((e.attrib["from"],e.attrib["to"],label.text))
    return edges

def rewrite(state,rule_edges):
    required=set()
    forbidden=set()
    added=set()
    deleted=set()
    for a,b,label in rule_edges:
        if label.startswith("not:"): forbidden.add((a,b,label[4:]))
        elif label.startswith("new:"): added.add((a,b,label[4:]))
        elif label.startswith("del:"): deleted.add((a,b,label[4:]))
        else: required.add((a,b,label))
    if not required<=state or not deleted<=state or forbidden&state or added&state:
        return None
    return frozenset((state-deleted)|added)

def interpret(folder):
    start=frozenset(read_edges(folder/"start.gst"))
    rules={p.stem:read_edges(p) for p in sorted(folder.glob("*.gpr"))}
    queue=deque([start]);seen={start};arcs=set()
    while queue:
        state=queue.popleft()
        for label,edges in rules.items():
            target=rewrite(state,edges)
            if target is None:continue
            arcs.add((state,label,target))
            if target not in seen:
                seen.add(target);queue.append(target)
    return seen,arcs

def native_minimal():
    start=(0,0,0)
    queue=deque([start]);seen={start};arcs=set()
    while queue:
        s=queue.popleft()
        used,live,linked=s
        moves=[]
        if not used:moves.append(("create",(1,1,0)))
        if live and not linked:moves.append(("link",(used,live,1)))
        if live and linked:moves.append(("unlink",(used,live,0)))
        if live and not linked:moves.append(("delete",(used,0,0)))
        for label,t in moves:
            arcs.add((s,label,t))
            if t not in seen:seen.add(t);queue.append(t)
    return seen,arcs

def minimal_projection(graph):
    return (int(("n0","n0","used") in graph),
            int(("n0","n0","live") in graph),
            int(("n0","n1","linked") in graph))

def native_capacity():
    # (name0_live, name1_used, name1_live, name1_linked)
    start=(1,0,0,0)
    queue=deque([start]);seen={start};arcs=set()
    while queue:
        s=queue.popleft()
        l0,u1,l1,link=s
        moves=[]
        if l0:moves.append(("delete0",(0,u1,l1,link)))
        if not l0 and not u1:moves.append(("create1",(l0,1,1,0)))
        if l1 and not link:moves.append(("link1",(l0,u1,l1,1)))
        if l1 and link:moves.append(("unlink1",(l0,u1,l1,0)))
        for label,t in moves:
            arcs.add((s,label,t))
            if t not in seen:seen.add(t);queue.append(t)
    return seen,arcs

def capacity_projection(graph):
    assert ("n0","n0","used") in graph
    return (int(("n0","n0","live") in graph),
            int(("n1","n1","used") in graph),
            int(("n1","n1","live") in graph),
            int(("n1","n2","linked") in graph))

def check(folder,project,native):
    gs,ga=interpret(folder)
    ns,na=native()
    p_states={project(x) for x in gs}
    p_arcs={(project(s),label,project(t)) for s,label,t in ga}
    assert p_states==ns,("state mismatch",p_states^ns)
    assert p_arcs==na,("labelled transition mismatch",p_arcs^na)
    assert len(gs)==len(ns)==4 and len(ga)==len(na)==4
    return {"fixture":folder.name,"states":len(gs),"labelled_transitions":len(ga),
            "native_equivalence":"exact for fixed-node edge-only grammar"}

if __name__=="__main__":
    results=[
        check(BASE/"gon_minimal.gps",minimal_projection,native_minimal),
        check(BASE/"gon_capacity_counterexample.gps",capacity_projection,native_capacity)]
    print(json.dumps(results,indent=2))
