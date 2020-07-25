class Solution:
    def checkSubarraySum(self,nums:List[int],k:int)->bool:
        if len(nums)<2:
            return False
        for i in range(len(nums)-1):
            if self.helper(i,nums,k):
                return True
        return False

    def helper(self,start:int,nums:List[int],k:int)->bool:
        end=start+1
        total=nums[start]
        while end<len(nums):
            total+=nums[end]
            if k!=0 and total%k==0:
                return True
            end+=1
        if total==0 and k==0:
            return True
        else:
            return False