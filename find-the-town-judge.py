class Solution:
    def findJudge(self,N:int.trust:List[List[int]])->int:
        g={i:[] for i in range(1,N+1)}
        for t in trust:
            g[t[0]].append(t[1])
        
        for k in g:
            if len(g[k])==0:
                for p in g:
                    if p!=k and k not in g[p]:
                        return -1
                return k
        return -1