from typing import List
class Solution:
        def majorityElement(self,nums:List[int]):
                v=None
                c=0
                for n in nums:
                        if n==v:
                            c+=1
                        elif c<=1:
                                c=1
                                v=n
                        else:
                                c-=1
                return v