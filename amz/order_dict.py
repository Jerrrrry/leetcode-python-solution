import collections
from typing import OrderedDict

d=OrderedDict()

d['a']=1
d['b']=2
d['c']=4
d['d']=6

n=3
if len(d)<n:
        print(d.keys())
else:
        q=collections.deque()
        while n>0:
                q.append(d.popitem())
                n-=1
        res=[x[0] for x in q]
        while q:
                k,v=q.pop()
                d[k]=v
        print(res)