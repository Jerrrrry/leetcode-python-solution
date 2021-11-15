class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if sum([sum(g) for g in grid])==len(grid)*len(grid[0]) or sum([sum(g) for g in grid])==0:
                return -1
        q=collections.deque()
        for i in range(len(grid)):
                for j in range(len(grid[0])):
                        if grid[i][j]==1:
                                q.append((i,j))
        res=0
        dirs=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
                l=len(q)
                f=False
                for _ in range(l):
                        x,y=q.popleft()
                        for dir in dirs:
                                nx,ny=x+dir[0],y+dir[1]
                                if 0<=nx<len(grid) and 0<=ny<len(gird[0]) and grid[nx][ny]==0:
                                        f=True
                                        q.append((nx,ny))
                if f:
                        res+=1
        return res
         