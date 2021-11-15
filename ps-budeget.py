
from typing import List
class Solution:
        def minValue(self,prices:List[List[int]],target:int)->int:
                m=len(prices)
                n=len(prices[0])
                dp=[[False for _ in range(target+1)] for i in range(m)]
                for n in prices[0]:
                        if n<=target:
                                dp[0][n]=True

                for i in range(1,m):
                        for n in prices[i]:
                                for j in range(target+1):
                                        if dp[i-1][j] and n+j<= target :
                                                dp[i][j+n]=True
                for x in range(target,-1,-1):
                        if dp[m-1][x]:
                                print(x)
                                return x
                return 0

                

code=Solution()
data=[[3,4,5,7,9],[2,6,8,11,13],[10,12,17,21,24]]
code.minValue(data,45)