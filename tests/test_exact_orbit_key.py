"""Exhaustive small-instance and adversarial orbit-key checks."""
import itertools
import unittest
from experiments.research_gate.exact_orbit_key import (
    Ref, State, Certificate, UnsafeQuotient, canonical_key,
    same_orbit_oracle, permutation_count)

def certified(pools=(("a", "b"),), **changes):
    fields = dict(pools=pools, fixed=("anchor",), equivariant_transitions=True,
                  equivariant_goal=True, equivariant_costs=True,
                  equivariant_constraints=True, equivariant_allocation=True,
                  no_hidden_identity_data=True)
    fields.update(changes)
    return Certificate(**fields)

class ExactOrbitTests(unittest.TestCase):
    def test_permutation_count(self):
        self.assertEqual(permutation_count(certified()), 2)

    def test_renaming_graph_history_guards_resources(self):
        c = certified()
        a = State(active=(Ref("a"),), edges=((Ref("anchor"),Ref("a")),),
                  used=(("create",Ref("a")),), attributes=(("role",Ref("a"),"replica"),),
                  forbidden=(("not_edge",Ref("b"),Ref("anchor")),),
                  resources=(("lock",Ref("a")),))
        b = State(active=(Ref("b"),), edges=((Ref("anchor"),Ref("b")),),
                  used=(("create",Ref("b")),), attributes=(("role",Ref("b"),"replica"),),
                  forbidden=(("not_edge",Ref("a"),Ref("anchor")),),
                  resources=(("lock",Ref("b")),))
        self.assertEqual(canonical_key(a,c), canonical_key(b,c))
        self.assertTrue(same_orbit_oracle(a,b,c))

    def test_exhaustive_iff_orbit(self):
        c=certified()
        states=[]
        for mask in range(4):
            for hist in range(4):
                for edge in range(4):
                    states.append(State(
                        active=tuple(Ref(n) for i,n in enumerate(("a","b")) if mask>>i&1),
                        used=tuple(("create",Ref(n)) for i,n in enumerate(("a","b")) if hist>>i&1),
                        edges=tuple((Ref("anchor"),Ref(n)) for i,n in enumerate(("a","b")) if edge>>i&1)))
        for a in states:
            self.assertEqual(canonical_key(a,c), canonical_key(a,c))
        for a,b in itertools.product(states,repeat=2):
            self.assertEqual(canonical_key(a,c)==canonical_key(b,c),
                             same_orbit_oracle(a,b,c))
        self.assertEqual(len(states),64)

    def test_equivalence_relation(self):
        c=certified()
        states=[State(active=(Ref("a"),)),State(active=(Ref("b"),)),
                State(active=(Ref("a"),Ref("b")))]
        for a in states:
            self.assertTrue(same_orbit_oracle(a,a,c))
        for a,b in itertools.product(states,repeat=2):
            self.assertEqual(same_orbit_oracle(a,b,c),same_orbit_oracle(b,a,c))
        for a,b,d in itertools.product(states,repeat=3):
            if same_orbit_oracle(a,b,c) and same_orbit_oracle(b,d,c):
                self.assertTrue(same_orbit_oracle(a,d,c))

    def test_history_sensitive_negative(self):
        c=certified()
        a=State(active=(Ref("a"),),used=(("create",Ref("a")),))
        b=State(active=(Ref("b"),),used=(("create",Ref("a")),))
        self.assertNotEqual(canonical_key(a,c),canonical_key(b,c))

    def test_fixed_name_negative(self):
        c=certified()
        self.assertNotEqual(canonical_key(State(active=(Ref("anchor"),)),c),
                            canonical_key(State(active=(Ref("a"),)),c))

    def test_role_negative(self):
        c=certified(pools=(("a",),("b",)))
        self.assertNotEqual(canonical_key(State(active=(Ref("a"),)),c),
                            canonical_key(State(active=(Ref("b"),)),c))

    def test_cost_and_guard_negative(self):
        c=certified()
        a=State(active=(Ref("a"),),attributes=(("cost",Ref("a"),1),),
                forbidden=(("blocked",Ref("a")),))
        b=State(active=(Ref("b"),),attributes=(("cost",Ref("b"),2),),
                forbidden=(("blocked",Ref("b")),))
        self.assertNotEqual(canonical_key(a,c),canonical_key(b,c))

    def test_shared_resource_negative(self):
        c=certified()
        a=State(resources=(("capacity",1),))
        b=State(resources=(("capacity",2),))
        self.assertNotEqual(canonical_key(a,c),canonical_key(b,c))

    def test_refuse_uncertified(self):
        with self.assertRaises(UnsafeQuotient):
            canonical_key(State(active=(Ref("a"),)),certified(equivariant_costs=False))
        with self.assertRaises(UnsafeQuotient):
            canonical_key(State(),certified(no_hidden_identity_data=False))
        with self.assertRaises(UnsafeQuotient):
            canonical_key(State(),certified(pools=(("a","b"),),fixed=("a",)))

    def test_refuse_opaque_and_large(self):
        with self.assertRaises(UnsafeQuotient):
            canonical_key(State(active=(object(),)),certified())
        with self.assertRaises(UnsafeQuotient):
            canonical_key(State(),certified(pools=(tuple("abcdefghi"),)))

if __name__=="__main__":
    unittest.main()
