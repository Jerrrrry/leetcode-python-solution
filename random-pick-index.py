class Solution:
    def __init__(self,nums):
        self.nums=nums
        self.dict1=dict()

        for i in range(len(self.nums)):
            self.dict1.setdefault(self.nums[i],[]).append(i)

    def pick(self,target):
        return random.choice(self.dict1[target])