class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(l,r,p):
            if l==0 and r==0:
                res.append(p)
            if l>0:
                dfs(l-1,r,p+'(')
            if l<r:
                dfs(l,r-1,p+')')
                
        dfs(n,n,'')
        return res