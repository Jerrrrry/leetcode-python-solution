class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wk='$'
        trie={}
        for word in words:
                node=trie
                for l in word:
                        node=node.setdefault(l,{})
                node[wk]=word
        r,c=len(board),len(board[0])
        
        res=[]
        def search(row,col,parent):
                letter=board[row][col]
                cur=parent[letter]
                wm=cur.pop(wk,False)
                if wm:
                        res.append(wm)
                board[row][col]='#'

                for (rd,cd) in dirs:
                        nr,nc=row+rd,col+cd
                        if nr<0 or nr>=r or nc<0 or nc>=c:
                                continue
                        if not board[nr][nc] in cur:
                                continue
                        search(nr,nc,cur)
                board[row][col]=letter

                if not cur:
                        parent.pop(letter)

        for i in range(r):
                for j in range(c):
                        if board[i][j] in trie:
                                search(i,j.trie)

        return res
