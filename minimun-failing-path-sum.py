class Solution:
    def minFallingPathSum(self,A:List[List[int]])->int:
        m,n=len(A),len(A[0])
        dp=[ [0]*(n+2) for _ in range(m)]
        for i in range(m):
            dp[i][0]=dp[i][-1]=float('inf')
            for j in range(1,n+1):
                dp[i][j]=A[i][j-1]
        for i in range(1,m):
            for j in range(1,n+1):
                dp[i][j]=A[i][j-1]+min(dp[i-1][j],dp[i-1][j+1],dp[i-1][j-1])

        return min(dp[-1])




print(Solution.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))