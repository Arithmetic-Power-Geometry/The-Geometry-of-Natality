"""GoN exact, independently checkable optimality certificate for the synthetic fixture.

Enumerates all 16 ordered subsets of three actions. Records every excluded
sequence with its reason and every feasible terminal state. This is a finite
certificate, not a scalability or novelty claim.
"""
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
data = json.loads((HERE / "fixture.json").read_text())
actions = {a["id"]: a for a in data["actions"]}
names = list(actions)

def evaluate(plan):
    alive = {s["id"] for s in data["services"] if s["alive"]}
    edges = {tuple(e) for e in data["dependencies"]}
    used = set()
    cost = 0
    for name in plan:
        a = actions[name]
        if not set(a["requires"]) <= used:
            return {"status": "invalid", "reason": "precondition"}
        cost += a["cost"]
        if cost > data["budget"]:
            return {"status": "invalid", "reason": "budget"}
        if name == "restart_auth":
            alive.add("auth")
        elif name == "create_auth_replacement":
            alive.add("auth_v2")
        elif name == "rewire_report":
            if "auth_v2" not in alive or ("report", "auth") not in edges:
                return {"status": "invalid", "reason": "rewire"}
            edges.remove(("report", "auth"))
            edges.add(("report", "auth_v2"))
        used.add(name)
    if edges.intersection(map(tuple, data["forbidden_dependencies"])):
        return {"status": "invalid", "reason": "forbidden_edge"}
    deps = [dst for src, dst in edges if src == "report"]
    goal = "report" in alive and all(dst in alive for dst in deps)
    return {"status": "feasible", "cost": cost, "goal": goal,
            "alive": sorted(alive), "edges": sorted([list(e) for e in edges])}

def main():
    records = []
    for k in range(len(names) + 1):
        for plan in itertools.permutations(names, k):
            records.append({"plan": list(plan), **evaluate(plan)})
    winners = [r for r in records if r["status"] == "feasible" and r["goal"]]
    minimum = min(r["cost"] for r in winners)
    optimal = [r["plan"] for r in winners if r["cost"] == minimum]
    expected = [["restart_auth"], ["create_auth_replacement", "rewire_report"]]
    assert len(records) == 16
    assert minimum == 3
    assert sorted(optimal) == sorted(expected), optimal
    assert len([r for r in records if r["status"] == "feasible"]) == 4
    report = {"scope": "synthetic fixture only", "enumerated_sequences": len(records),
              "feasible_sequences": 4, "minimum_cost": minimum,
              "optimal_plans": optimal, "records": records,
              "groove_matched": False, "q1_novelty_established": False}
    output = HERE / "optimality_certificate.json"
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k != "records"}, indent=2))

if __name__ == "__main__":
    main()
