from typing import List
class Solution:
        def peakIndexInMountainArray(self,nums:List[int])->int:
                l,r=0,len(nums)-1

                while l<r:
                        m=(l+r)//2
                        if nums[m]<nums[m+1]:
                                l=m+1
                        else:
                                r=m
                return l