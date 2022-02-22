#https://leetcode.com/problems/can-place-flowers/

class Solution:
        def insertFlower(self,f:list[int],n:int)->bool:
                data=[0]+f+[0]
                l=len(f)

                for i in range(1,l+1):
                        if data[i-1]==data[i]==data[i+1]==0:
                                n-=1
                                data[i]=1
                        if n<=0:
                                return True
                return False 