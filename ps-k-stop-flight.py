class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        p=[math.inf]*n
        c=[math.inf]*n
        p[src]=0
        
        for i in range(1,k+2):
            c[src]=0
            for s,e,m in flights:
                if p[s]<math.inf:
                    c[e]=min(c[e],p[s]+m)
                
            p=c.copy()
        return -1 if c[dst]==math.inf else c[dst]