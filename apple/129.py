import collections
from typing import List
class Solution:
        def maxSlidingWindow(self,nums: list[int],k:int)->list[int]:
                data=collections.deque()

                res=[]

                for i,n in enumerate(nums):
                        while data and nums[data[-1]]<n:
                                data.pop()

                        data.append(i)

                        if data[0]==i-k:
                                data.popleft()

                        if i>=k-1:
                                res.append(nums[data[0]])
                return res
c=Solution()

d=[4,3,2,6,77,88,0,8]

print(c.maxSlidingWindow(d,3))