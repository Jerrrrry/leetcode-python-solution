import heapq
from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q=[]

        for x,y in points:
                heapq.heappush(q,(x**2+y**2,[x,y]))

        res=[]
        while K>0 and q:
                res.append(heapq.heappop(q)[1])
        return res
        