from typing import List
import collections
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        dirs=[[1,0],[-1,0],[0,1],[0,-1]]
        step=0
        q=collections.deque()
        m,n=len(grid),len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='#':
                    q.append([i,j])
                    
        while q:
            s=len(q)
            step+=1
            for _ in range(s):
                x,y=q.popleft()
                for dir in dirs:
                    nx,ny=x+dir[0],y+dir[1]
                    if 0<=nx<m and 0<=ny<n:
                        if grid[nx][ny]=='*':
                            return step
                        elif grid[nx][ny]=='O':
                            grid[nx][ny]='X'
                            q.append([nx,ny])
                            
        return -1
