from typing import List
import collections
class Solution:
        def twosum(self,nums:List[int],target:int)->List[int]:
                data=collections.defaultdict(int)
                for i in range(len(nums)):
                        if target-nums[i] in data:
                                return sorted([i,data[target-nums[i]]])
                        data[nums[i]]=i

                        