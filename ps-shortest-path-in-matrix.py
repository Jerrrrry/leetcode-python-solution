class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        q=collections.deque()
        q.append((0,0,1))
        v=set()
        dirs=[(1,-1),(1,0),(1,1),(-1,1),(-1,0),(-1,-1),(0,1),(0,-1)]
        while q:
            p=q.popleft()
            x,y,l=p[0],p[1],p[2]
            if x==len(grid)-1 and y==len(grid[0])-1:
                return l
            if (x,y) not in v:
                v.add((x,y))
                for d in dirs:
                    nx,ny=x+d[0],y+d[1]
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==0 and (nx,ny) not in v:
                        q.append((nx,ny,l+1))
        return -1