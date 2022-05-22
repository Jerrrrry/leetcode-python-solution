class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wk="$"
        res=[]
        trie={}
        
        for word in words:
            node=trie
            for l in word:
                node=node.setdefault(l,{})
                
            node[wk]=word
         
        m,n=len(board),len(board[0])
        dirs=[[1,0],[0,1],[-1,0],[0,-1]]
            
        def search(x,y,p):
            l=board[x][y]
            cn=p[l]
            wm=cn.pop(wk,False)
            if wm:
                res.append(wm)
                
            board[x][y]='#'
            
            for dir in dirs:
                nx,ny=x+dir[0],y+dir[1]
                if nx<0 or nx>=m or ny<0 or ny>=n:
                    continue
                if board[nx][ny] not in cn:
                    continue
                search(nx,ny,cn)
                
            board[x][y]=l
            ##prune founded path in trie
            if not cn:
                p.pop(l)
                
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    search(i,j,trie)
                
        return res