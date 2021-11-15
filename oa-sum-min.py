import operator
from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        compare=operator.ge 
        at=0
        total=0
        q=[]
        for i in range(len(arr)):
            while q and compare(q[-1][1],arr[i]):
                r,on=q.pop()
                l=0 if not q else q[-1][0]+1
                at-=(r-l+1)*on
            l=0 if not q else q[-1][0]+1
            at+=(i-l+1)*arr[i]
            total+=at
            q.append((i,arr[i]))
        return total%(10**9+7)