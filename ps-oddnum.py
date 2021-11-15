import collections
from typing import List
class Solution:
        def oddnum(self,nums:List[int])->int:
                data=collections.Counter(nums)
                for n,v in data:
                        if v%2!=0:
                                return n