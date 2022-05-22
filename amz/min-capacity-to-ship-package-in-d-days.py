class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minv=max(weights)
        maxv=sum(weights)
        
        def enough(c):
            t=1
            cap=c
            
            for w in weights:
                if w>cap:
                    t+=1
                    cap=c
                cap-=w
                
            return True if t<=days else False 
        
        while minv<maxv:
            m=(minv+maxv)//2
            
            if enough(m):
                maxv=m
            else:
                minv=m+1
                
        return minv