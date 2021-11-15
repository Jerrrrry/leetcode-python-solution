class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
            n=len(nums)
            total=sum(nums)
            if total%k!=0:
                    return False
            target=total//k
            v=['0']*n
            memo={}

            def backtrack(i,c,t):

                if t>target:
                    return False
                if c==k-1:return True
                vs=''.join(v) 
                if vs in memo:
                        return memo[vs]
                if t==target:
                    memo[vs]=backtrack(0,c+1,0)
                    return memo[vs]
                for j in range(i,n):
                        if v[j]=='0':
                                v[j]='1'
                                if backtrack(j+1,c,t+nums[j]):
                                        return True
                                v[j]='0'
                memo[vs]=False
                return memo[vs]
        return backtrack(0,0,0)