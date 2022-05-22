import collections
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid)==0:
            return 0
        
        m,n=len(grid),len(grid[0])
        res=0
        dirs=[[1,0],[0,1],[-1,0],[0,-1]]
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    q=collections.deque()
                    
                    q.append([i,j])
                    res+=1
                    while q:
                        l=len(q)
                        for _ in range(l):
                            x,y=q.popleft()
                            grid[x][y]='0'

                            for dir in dirs:
                                nx,ny=x+dir[0],y+dir[1]

                                if 0<=nx<m and 0<=ny<n and grid[nx][ny]=='1':
                                    q.append([nx,ny])
                                
        return res


##dfs
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        r=len(grid)
        c=len(grid[0])
        def scan(x,y):
            grid[x][y]='0'
            
            for dir in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx,ny=x+dir[0],y+dir[1]
                
                if 0<=nx<r and 0<=ny<c and grid[nx][ny]=='1':
                    scan(nx,ny)
                    
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    scan(i,j)
                    res+=1
        return res