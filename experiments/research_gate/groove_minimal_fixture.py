"""Generate an executable minimal GROOVE grammar and independently enumerate its states.

This is a *one-name*, *one-terminal*, unit-cost restriction of the dynamic
creation/rewriting grammar, NOT a full equivalence proof for Prompt 14.
"""
from __future__ import annotations
import json
import pathlib
from collections import deque
from xml.etree.ElementTree import Element, SubElement, ElementTree

OUT = pathlib.Path("experiments/research_gate/gon_minimal.gps")
NS = "http://www.gupro.de/GXL/gxl-1.0.dtd"

def write_graph(path, graph_id, role, nodes, edges):
    gxl = Element("gxl", {"xmlns": NS})
    graph = SubElement(gxl, "graph", {"role": role, "edgeids": "false",
                                      "edgemode": "directed", "id": graph_id})
    attr = SubElement(graph, "attr", {"name": "$version"})
    SubElement(attr, "string").text = "curly"
    for node in nodes:
        SubElement(graph, "node", {"id": node})
    for src, dst, label in edges:
        edge = SubElement(graph, "edge", {"from": src, "to": dst})
        attr = SubElement(edge, "attr", {"name": "label"})
        SubElement(attr, "string").text = label
    ElementTree(gxl).write(path, encoding="utf-8", xml_declaration=True)

def fixture():
    OUT.mkdir(parents=True, exist_ok=True)
    write_graph(OUT/"start.gst", "start", "graph", ("n0", "n1"),
                [("n0","n0","Name"),("n1","n1","Terminal")])
    # Name and terminal self loops are context edges; used/live/linked
    # represent persistent history, live allocation, and connectivity.
    rules = {
        "create": (("n0",), [
            ("n0","n0","Name"), ("n0","n0","not:used"),
            ("n0","n0","new:used"), ("n0","n0","new:live")]),
        "link": (("n0","n1"), [
            ("n0","n0","Name"), ("n1","n1","Terminal"),
            ("n0","n0","live"), ("n0","n1","not:linked"),
            ("n0","n1","new:linked")]),
        "unlink": (("n0","n1"), [
            ("n0","n0","Name"), ("n1","n1","Terminal"),
            ("n0","n0","live"), ("n0","n1","del:linked")]),
        "delete": (("n0","n1"), [
            ("n0","n0","Name"), ("n1","n1","Terminal"),
            ("n0","n1","not:linked"), ("n0","n0","del:live")]),
    }
    for name,(nodes,edges) in rules.items():
        write_graph(OUT/(name+".gpr"), name, "rule", nodes, edges)
    (OUT/"system.properties").write_text(
        "startGraph=start\n"
        "enableControl=false\n"
        "useStoredNodeIDs=true\n"
        "grammarVersion=3.10\n"
        "grooveVersion=6.8.0\n"
        "remark=Minimal one-name creation, link, unlink, delete test\n")
    return rules

def oracle():
    # (used, live, linked); one-time allocation; link requires live;
    # delete requires no link; used survives delete.
    start = (0,0,0)
    def succ(s):
        used,live,linked=s
        if not used: yield "create",(1,1,0)
        if live and not linked: yield "link",(used,live,1)
        if live and linked: yield "unlink",(used,live,0)
        if live and not linked: yield "delete",(used,0,0)
    seen={start}
    q=deque([start])
    arcs=[]
    while q:
        s=q.popleft()
        for name,t in succ(s):
            arcs.append((s,name,t))
            if t not in seen:
                seen.add(t);q.append(t)
    return sorted(seen), sorted(arcs)


def capacity_counterexample_grammar():
    """Two names; initially live name0; capacity one; only name1 can link."""
    dest=pathlib.Path("experiments/research_gate/gon_capacity_counterexample.gps")
    dest.mkdir(parents=True,exist_ok=True)
    write_graph(dest/"start.gst","start","graph",("n0","n1","n2"),[
        ("n0","n0","Name0"),("n0","n0","used"),("n0","n0","live"),
        ("n1","n1","Name1"),("n2","n2","Terminal")])
    rules={
        "delete0":(("n0",),[("n0","n0","Name0"),("n0","n0","del:live")]),
        "create1":(("n0","n1"),[("n0","n0","Name0"),("n0","n0","not:live"),
            ("n1","n1","Name1"),("n1","n1","not:used"),
            ("n1","n1","new:used"),("n1","n1","new:live")]),
        "link1":(("n1","n2"),[("n1","n1","Name1"),("n1","n1","live"),
            ("n2","n2","Terminal"),("n1","n2","not:linked"),("n1","n2","new:linked")]),
        "unlink1":(("n1","n2"),[("n1","n1","Name1"),("n1","n1","live"),
            ("n2","n2","Terminal"),("n1","n2","del:linked")])
    }
    for name,(nodes,edges) in rules.items():
        write_graph(dest/(name+".gpr"),name,"rule",nodes,edges)
    (dest/"system.properties").write_text(
        "startGraph=start\nenableControl=false\nuseStoredNodeIDs=true\n"
        "grammarVersion=3.10\ngrooveVersion=6.8.0\n"
        "remark=Capacity-one terminal-reachability deletion counterexample\n")
    return rules

if __name__=="__main__":
    rules=fixture()
    capacity_rules=capacity_counterexample_grammar()
    states,arcs=oracle()
    assert len(states)==4 and len(arcs)==4, (states,arcs)
    print(json.dumps({"states":states,"arcs":arcs,"rules":list(rules),"capacity_counterexample_rules":list(capacity_rules)},indent=2))
