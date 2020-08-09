class Solution:
    def twoSum(self,nums:List[int],target:int)->List[int]:
        data=dict{}
        for i in range(len(nums)):
            if target-nums[i] in data:
                return [data[nums[target-nums[i]]],i]
            data[nums[i]]=i
        return []