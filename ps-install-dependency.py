from typing import List
import collections
class Solution:
        def install(self,A:int,dep:List[List[int]])->List[int]:
                r=collections.defaultdict(list)
                for u,v in dep:
                        r[u].append(v)
                if A not in r:
                        return []
                h=set()
                q=collections.deque()
                q.append(A)
                res=[]
                while q:
                        l=len(q)
                        while l>0:
                                l-=1
                                p=q.popleft()
                                if p not in h:
                                        h.add(p)
                                        res.append(p)
                                        for x in r[p]:
                                                q.append(x)
                return res[::-1]

code=Solution()
a=1
dep=[[1,3],[1,2],[2,4],[3,5],[3,6],[6,7],[8,9]]
res=code.install(a,dep)
print(res)
