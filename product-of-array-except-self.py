class Solution:
    def productExceptItself(self,nums:List[int])->List[int]:
        size=len(nums)
        left=1
        res=[1]*size

        for i in range(size-1):
            left*=nums[i]
            nums[i+1]*=left

        right=1
        n=size-1

        while n>0:
            right*=nums[n]
            nums[n-1]*=right
            n-=1

        return res