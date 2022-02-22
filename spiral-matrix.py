class Solution:
    def spiralMatrix(self,matrix:List[List[int]])->List[int]:
        if not matrix or not matrix[0]:return []
        m,n=len(matrix),len(maxtrix[0])
        l,r,u,d=0,n-1,0,m-1
        res=[]
        x,y=0,0
        dirs=[(0,1),(1,0),(0,-1),(-1,0)]
        cur_d=0
        while len(res)!=m*n:
            res.append(matrix[x][y])
            if cur_d==0 and y==r:
                curd_d+=1
                u+=1
            elif cur_d==1 and x==d:
                cur_d+=1
                r-=1
            elif curd==2 amd y==l:
                cur_d+=1
                d-=1
            elif cur_d==3 and x==u:
                cur_d+=1
                l+=1
            cur_d%=4
            x+=dirs[cur_d][0]
            y+=dirs[cur_d][1]
        return res