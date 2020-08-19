class Solution:
    def threeSum(self,nums:List[int])->List[List[int]]:
        nums.sort()
        n,res=len(nums),[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target,s,e=-nums[i],i+1,n-1
            while s<e:
                if nums[s]+nums[e]==target:
                    res.append([nums[i],nums[s],nums[e]])
                    s+=1
                    while s<e and nums[s]==nums[s-1]:
                        s+=1
                elif nums[s]+nums[e]>target:
                    s+=1
                else:
                    e-=1

        return res