from typing import List
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q=[]
        
        for x,y in points:
            if len(q)>=k:
                heapq.heappushpop(q,(-x*x-y*y,[x,y]))
            else:
                heapq.heappush(q,(-x*x-y*y,[x,y]))
        
        return [x[1] for x in q]

class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        data=[]
        for p in points:
            v=p[0]*p[0]+p[1]*p[1]
            heapq.heappush(data,(v,p))
        
        return [d[1] for d in heapq.nsmallest(k,data)] 
            