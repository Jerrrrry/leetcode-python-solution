class Solution(object):
    def uniquePathsWithObstacles(self, obs):
        m,n=len(obs),len(obs[0])
        data=[[0]*(n+1) for i in range(m+1)]
        for i in range(1,m+1):
                for j in range(1,n+1):
                        if obs[i-1][j-1]==1:
                                data[i][j]=0
                        else:
                                if i==1 and j==1:
                                        data[i][j]=1
                                else:
                                        data[i][j]=data[i-1][j]+data[i][j-1]
        return data[m][n]
s=Solution()
obs=[
        [0,0,0,0],
        [0,1,0,0],
        [0,0,1,0],
        [0,0,0,0]
]
print(s.uniquePathsWithObstacles(obs))
