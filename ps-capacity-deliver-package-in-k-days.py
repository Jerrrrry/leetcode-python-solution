class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minv=max(weights)
        maxv=sum(weights)
        def isEnough(c):
            t=1
            cap=c
            for w in weights:
                if w>cap:
                    cap=c
                    t+=1
                cap-=w
            return True if t<=days else False 
        
        while minv<maxv:
            m=(minv+maxv)//2
            if isEnough(m):
                maxv=m
            else:
                minv=m+1
        return minv