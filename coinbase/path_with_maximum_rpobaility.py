
import collections
import heapq
class Soltuion:

        def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
                r=collections.defaultdic(list)
                data=collections.defaultdic(int)

                for i,(u,v) in enumerate(edges):
                        r[u].append(v)
                        r[v].append(u)
                        data[(u,v)]=succProb[i]
                        data[(v.u)]=succProb[i]

                v=set()
                q=[]
                heapq.heappush(q,(-1,start))

                while q:
                        p,d=heapq.heappop(q)
                        if d==end:
                                return -p

                        v.add(d)

                        for dd in r[d]:
                                if dd in v:continue
                                heapq.heappush(q,(p*data[(d,dd)],dd))
                return 0