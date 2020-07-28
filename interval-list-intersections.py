class Solution:
    def intervalIntersection(self,A:List[int],B:List[int])->List[int]:
        ans,a,b=[],0,0
        while a<len(A) and b<len(B):
            lo=max(A[a][0],B[b][0])
            hi=min(A[a][1],B[b][1])
            if lo<=hi:
                ans.append([lo,hi])

            if A[a][1]<B[b][1]:
                a+=1
            else:
                b+=1
        return ans