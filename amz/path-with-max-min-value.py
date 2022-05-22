class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        
        r=len(grid)
        c=len(grid[0])
        
        q=[]
        heapq.heappush(q,(-grid[0][0],0,0))
        v = [[0 for _ in range(c)] for _ in range(r)]
        
        while q:
            val,x,y=heapq.heappop(q)
            if x==r-1 and y==c-1:
                return -val
            for dir in dirs:
                nx,ny=x+dir[0],y+dir[1]
                if 0 <= nx < r and 0 <= ny < c and not v[nx][ny]:
                    v[nx][ny]=1
                    
                    heapq.heappush(q,(max(val,-grid[nx][ny]),nx,ny))
                    
        return -1
        