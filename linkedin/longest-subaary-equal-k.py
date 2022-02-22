#https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
        def sumequalsk(self,nums:list[int],k:int)->int:
                res=0
                data=collections.defaultdict(int)
                t=0
                data[0]=1
                for n in nums:
                        t+=n
                        if t-k in data:
                                res+=data[t-k]
                        data[t]=1
                return res
