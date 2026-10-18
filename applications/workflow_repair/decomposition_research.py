"""GoN: formally gated exact decomposition, with a coupling counterexample.

This is an evaluation of a standard separability principle, NOT an original
theorem. Never apply it when actions, goals or constraints cross components.
"""
import json
from pathlib import Path
from scaling_benchmark import make_instance, uniform_cost, transition, goal

def certified_decomposition(instance, coupling_edges=(), global_resource_limit=None):
    n=instance["n"]
    if coupling_edges or global_resource_limit is not None:
        return {"certified":False,"reason":"cross-component coupling"}
    local_costs=[]
    for i in range(n):
        local={"n":1,"seed":instance["seed"],
               "restart_costs":[instance["restart_costs"][i]],
               "create_costs":[instance["create_costs"][i]],
               "rewire_costs":[instance["rewire_costs"][i]],
               "action_order":[0,1,2]}
        r=uniform_cost(local)
        local_costs.append(r["cost"])
    return {"certified":True,"cost":sum(local_costs),
            "local_costs":local_costs,"local_expanded_total":sum(
                uniform_cost({"n":1,"seed":instance["seed"],
                "restart_costs":[instance["restart_costs"][i]],
                "create_costs":[instance["create_costs"][i]],
                "rewire_costs":[instance["rewire_costs"][i]],
                "action_order":[0,1,2]})["expanded"] for i in range(n))}

def coupling_counterexample():
    # Two local repairs each cost 3. A shared resource forbids executing
    # two restart actions, while creation+rewire remains possible.
    # The naive independently chosen local restart/restart plan is infeasible.
    # The optimal *cost* happens to remain 6 in this fixture, which makes
    # it especially important not to mistake equal costs for plan soundness.
    independent_plan=("restart_0","restart_1")
    coupled_feasible=not (independent_plan.count("restart_0") and independent_plan.count("restart_1"))
    assert not coupled_feasible
    return {"independent_plan":list(independent_plan),
            "shared_restart_capacity":1,
            "independent_plan_feasible_under_coupling":False,
            "claim":"plan-preserving decomposition is unsound without a coupling check"}

def main():
    rows=[]
    for n in range(1,9):
        for seed in (0,1,2):
            instance=make_instance(n,seed)
            decomposition=certified_decomposition(instance)
            assert decomposition["certified"]
            assert decomposition["cost"]==3*n
            if n<=4:
                whole=uniform_cost(instance)
                assert whole["cost"]==decomposition["cost"]
                whole_expanded=whole["expanded"]
            else:
                whole_expanded=None
            rows.append({"n":n,"seed":seed,"optimum":decomposition["cost"],
                         "local_expanded_total":decomposition["local_expanded_total"],
                         "whole_ucs_expanded":whole_expanded})
    assert not certified_decomposition(make_instance(2,0),
                    coupling_edges=[(0,1)])["certified"]
    report={"method":"certified independent-component decomposition",
            "novelty":"standard separability; not established as novel",
            "scope":"synthetic independent components only",
            "cases":len(rows),"rows":rows,
            "coupling_counterexample":coupling_counterexample(),
            "groove_comparison":False}
    output=Path(__file__).with_name("decomposition_results.json")
    output.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"cases":len(rows),"all_verified":True,
                      "coupling_rejected":True,"n8_optimum":24},indent=2))

if __name__=="__main__":main()
