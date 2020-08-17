class Solution:
    def generateParenthesis(self,n:int)->List[str]:
        res=[]
        self.dfs(res.n,n,'')
        return res
    def dfs(self,res:List[str],l:int,r:int,path:str)->None:
        if l==0 and r==0:
            res.append(path)
        if l>0:
            self.dfs(res,l-1,right,path+'(')
        if l<r:
            self.dfs(res,l,r-1,path+')')