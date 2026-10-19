# Reproducible compact independent-oracle regression for Prompt 3
from itertools import combinations,product
from collections import Counter
INF=10**8
def fw(n,es,caps):
 d=[[0 if i==j else INF for j in range(n)] for i in range(n)]
 for u,v,w,c in es:
  if not c or c in caps:d[u][v]=min(d[u][v],w)
 for k in range(n):
  for i in range(n):
   for j in range(n):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
 return d[0]
def bf(n,es,caps):
 d=[INF]*n;d[0]=0
 for _ in range(n-1):
  t=d[:]
  for u,v,w,c in es:
   if not c or c in caps:t[v]=min(t[v],d[u]+w)
  if t==d:break
  d=t
 return d
counts=Counter();total=0
for n in (2,3):
 arcs=[(u,v) for u in range(n) for v in range(n) if u!=v]
 for m in range(1,min(3,len(arcs))+1):
  for pairs in combinations(arcs,m):
   for spec in product(tuple(product((1,2),('', 'a','b'))),repeat=m):
    es=[(*uv,*wc) for uv,wc in zip(pairs,spec)]
    for obs in product((0,1),repeat=n):
     if obs[0]!=0:continue
     for B in range(5):
      vals=[]
      for caps in ((),('a',),('b',),('a','b')):
       d=fw(n,es,caps);assert d==bf(n,es,caps)
       vals.append(len({obs[i] for i in range(n) if d[i]<=B}))
      delta=vals[3]-vals[1]-vals[2]+vals[0]
      counts[(delta>0)-(delta<0)]+=1;total+=1
assert total==98400 and counts=={0:96950,-1:842,1:608}
print('PASS',total,'cases',4*total,'oracle comparisons',dict(counts))
