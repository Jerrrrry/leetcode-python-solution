class Solution:
    def reverserBits(self,n:int)->int:
        ret,power=0,31
        while n:
            ret+=(n&1)<<power
            n=n>>1
            power-=1
        return ret