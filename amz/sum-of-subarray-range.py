import operator
def subrange(nums):
        def getM(nums,m):
                if m==1:
                        c=operator.le
                else:
                        c=operator.ge
                q=[]
                at=0
                t=0
                for i,v in enumerate(nums):
                        while q and c(q[-1][-1],v):
                                r,lv=q.pop()
                                l=0 if not q else q[-1][0]+1
                                at-=(r-l+1)*lv
                        l=0 if not q else q[-1][0]+1
                        at+=(i-l+1)*v
                        t+=at
                        q.append([i,v])
                return t
        return getM(nums,1)-getM(nums,0)