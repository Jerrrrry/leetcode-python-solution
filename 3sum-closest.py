class Solution:
    def def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            s,e=i+1,len(nums)-1
            while s<e:
                t=nums[i]+nums[s]+nums[e]
                if t==target:
                    return t
                if abs(t-target)<abs(res-target):
                    res=t
                if t<target:
                    s+=1
                else:
                    e-=1
        return res