"""Deterministic tests of generative natality accounting. Python stdlib only."""
import unittest

def reachable(nodes,edges,source):
    seen={source};stack=[source]
    while stack:
        u=stack.pop()
        for a,b in edges:
            if a==u and b not in seen:seen.add(b);stack.append(b)
    return seen

def signature(old_nodes,old_edges,new_nodes,new_edges,source):
    assert old_nodes<=new_nodes and old_edges<=new_edges
    oldr=reachable(old_nodes,old_edges,source)
    newr=reachable(new_nodes,new_edges,source)
    a=len((newr & old_nodes)-oldr)
    g=len(newr-old_nodes)
    c=len(new_nodes-old_nodes)
    return a,g,c

class GenerativeCalculusTests(unittest.TestCase):
    def test_accessibility_only(self):
        self.assertEqual(signature({'s','a'},set(),{'s','a'},{('s','a')},'s'),(1,0,0))
    def test_latent_creation(self):
        self.assertEqual(signature({'s'},set(),{'s','b'},set(),'s'),(0,0,1))
    def test_realized_creation(self):
        self.assertEqual(signature({'s'},set(),{'s','b'},{('s','b')},'s'),(0,1,1))
    def test_generativity_not_additive(self):
        x0={'s'};x1={'s','b'}
        t0=set();t1=set();t2={('s','b')}
        self.assertEqual(signature(x0,t0,x1,t1,'s'),(0,0,1))
        self.assertEqual(signature(x1,t1,x1,t2,'s'),(1,0,0))
        self.assertEqual(signature(x0,t0,x1,t2,'s'),(0,1,1))
    def test_total_gain_and_creation_telescope(self):
        states=[({'s'},set()),({'s','b'},set()),({'s','b'},{('s','b')})]
        def total(x,y):
            a,g,c=signature(*x,*y,'s')
            return a+g,c
        first=total(states[0],states[1]);second=total(states[1],states[2]);whole=total(states[0],states[2])
        self.assertEqual(tuple(a+b for a,b in zip(first,second)),whole)
if __name__=='__main__':unittest.main()
