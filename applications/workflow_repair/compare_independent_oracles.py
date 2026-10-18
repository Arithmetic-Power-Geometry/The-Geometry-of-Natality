"""GoN regression gate: independently enumerate all feasible repair traces.

Runs both existing solvers and compares their successful plan sets, not just
their minimum objective values. No GROOVE execution or novelty is implied.
"""
import importlib.util
import json
from itertools import permutations
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    fixture = json.loads((ROOT / "fixture.json").read_text())
    oracle = load("verify_fixture")
    independent = load("independent_audit")
    exact = {(tuple(path), cost) for cost, path in oracle.solve(fixture)}
    enumerated = set()
    for length in range(len(fixture["actions"]) + 1):
        for order in permutations([a["id"] for a in fixture["actions"]], length):
            result = independent.evaluate(order, fixture["budget"])
            if result is not None and result["usable"]:
                enumerated.add((order, result["cost"]))
    assert exact == enumerated, f"Oracle disagreement: exact={exact}; exhaustive={enumerated}"
    assert exact == {
        (("restart_auth",), 3),
        (("create_auth_replacement", "rewire_report"), 3),
    }, f"Unexpected plan set: {exact}"
    print(json.dumps({
        "fixture": fixture["name"], "kind": "synthetic",
        "independent_oracles_agree": True,
        "successful_plans": [
            {"actions": list(path), "cost": cost}
            for path, cost in sorted(exact)
        ],
        "groove_executed": False, "q1_ready": False
    }, indent=2))

if __name__ == "__main__":
    main()
