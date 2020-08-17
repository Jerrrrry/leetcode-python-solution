class Solution:
    def singleNonDuplicate(self,nums:List[int])->int:
        lo,hi=0,len(nums)-1
        while lo<hi:
            m=(lo+hi)//2
            half_even=(hi-m)%2==0
            if nums[m]==nums[m+1]:
                if half_even:
                    lo=m+2
                else:
                    hi=m-1
            elif nums[m-1]==nums[m]:
                if half_even:
                    hi=m-2
                else:
                    lo=m+1
            else:
                return nums[m]
        return nums[lo]