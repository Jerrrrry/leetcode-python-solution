import collections
class Solution:
        def getprint(self,nums:list):
                q=collections.deque()
                mv=-1
                for n in nums:
                        q.append(collections.deque(n))
                res=[]
                while q:
                        n=len(q)
                        while n:
                                l=q.popleft()
                                if len(l)>0:
                                        res.append(l.popleft())
                                        q.append(l)
                                n-=1
                                
                return res

c=Solution()
print(c.getprint([[1,2],[4],[6],[],[7,8,9]]))
                
                
