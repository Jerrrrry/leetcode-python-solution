class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0]!=0:
            return 0
        if len(nums)!=nums[-1]:
            return len(nums)
        
        x=0
        
        for i in range(1,len(nums)):
            x=nums[i-1]+1
            if x!=nums[i]:
                return x