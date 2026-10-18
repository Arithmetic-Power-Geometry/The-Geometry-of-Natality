"""GoN V8 synergy constructions and exhaustive four-corner checks. Standard library."""
import json
from pathlib import Path
HERE=Path(__file__).resolve().parent
def reach(vertices,edges):
    seen={0};queue=[0]
    for u in queue:
        for a,b in edges:
            if a==u and b not in seen:seen.add(b);queue.append(b)
    return seen
def gain(n,base,added):
    return len(reach(range(n),base|added))-len(reach(range(n),base))
def synergy(n,base,a,b):
    return gain(n,base,a|b)-gain(n,base,a)-gain(n,base,b)
def run():
    positive=[];negative=[]
    for m in range(1,51):
        # s=0, x=1, u=2, downstream 3..m+1 (m-1 nodes)
        n=m+2;base={(2,i) for i in range(3,n)}
        a={(0,1)};b={(1,2)}
        got=synergy(n,base,a,b)
        assert got==m,(m,got)
        positive.append(got)
        # s=0, first hub=1, second hub=2; common leaves 3..m+1
        # each action reaches m nodes: hub 1 reaches hub 2 and leaves, and vice versa
        n=m+1
        if m==1:
            n=3;base={(2,1)}
        else:
            base={(1,2),(2,1)}|{(1,i) for i in range(3,n)}
        a={(0,1)};b={(0,2)}
        got=synergy(n,base,a,b)
        assert got==-m,(m,got)
        negative.append(got)
    out={'positive_constructions':len(positive),'negative_constructions':len(negative),'checks':100,'failures':0,'positive_range':[min(positive),max(positive)],'negative_range':[min(negative),max(negative)],'novelty':'no new priority claim'}
    (HERE/'summary.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':run()
