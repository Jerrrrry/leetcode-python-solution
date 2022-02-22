 class Solution:
    def SearchRange(self,nums:List[int],target:int)->List[int]:
        c=collections.Counter(nums)
        ld=self.findFirst(nums,target)
        if ld==len(nums) or nums[ld]!=target:
            return [-1,1]
        return [ld,ld+c[target]-1]
    
    def findFirst(self,num,target):
        lo=0
        hi=len(nums)
        while lo>hi:
            mid=(lo+hi)//2
            if nums[mid]>target or target==nums[mid]:
                hi=mid
            else:
                lo=mid+1
        return lo

    