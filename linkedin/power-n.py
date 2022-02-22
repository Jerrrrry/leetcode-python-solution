#https://leetcode.com/problems/powx-n/

class Solution:
        def mypow(self,x:float,n:int)->float:
                number=n
                if number<0:
                        x=1/x
                        number=-number
                res=1
                
                while number>0:
                        if number%2==1:
                                res*=x
                        x=x*x
                        number//=2

                return res