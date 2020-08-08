class Solution:
    def numIslands(self,grid:List[List[str]])->int:
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.dfs(grid,i,j)
                    res+=1
        return res

    def dfs(self,grid:List[List[str]],i:int,j:int)->None:
        dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        grid[i][j]="0"
        for dir in dirs:
            ni,nj=i+dir[0],j+dir[1]
            if ni>=0 and nj>=0 and ni<len(grid) and nj<len(grid[0]):
                if grid[ni][nj]=="1":
                    self.dfs(grid,ni,nj)