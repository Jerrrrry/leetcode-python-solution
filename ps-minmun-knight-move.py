#simple bfs frorm (x,y)to (0,0) will lte , max(m,n)**2, we need bidirection bfs /2

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        
        dirs=[[2,1],[1,2],[2,-1],[-1,2],[-2,1],[-1,-2],[1,-2],[-2,-1]]
        oq=collections.deque([(0,0,0)])
        od={(0,0):0}
        
        tq=collections.deque([(x,y,0)])
        td={(x,y):0}
        
        while True:
            ox,oy,os=oq.popleft()
            
            if (ox,oy) in td:
                return os+td[(ox,oy)]
            tx,ty,ts=tq.popleft()
            if (tx,ty) in od:
                return ts+od[(tx,ty)]
            
            for i,j in dirs:
                nox,noy=ox+i,oy+j
                if (nox,noy) not in od:
                    oq.append((nox,noy,os+1))
                    od[(nox,noy)]=os+1
                ntx,nty=tx+i,ty+j
                
                if (ntx,nty) not in td:
                    tq.append((ntx,nty,ts+1))
                    td[(ntx,nty)]=ts+1      

class DFS:
    def minKnightMoves(self, x: int, y: int) -> int:

        @lru_cache(maxsize=None)
        def dfs(x, y):
            if x + y == 0:
                # base case: (0, 0)
                return 0
            elif x + y == 2:
                # base case: (1, 1), (0, 2), (2, 0)
                return 2
            else:
                return min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1

        return dfs(abs(x), abs(y))

#ts x*y  
                