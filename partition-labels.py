class Solution:
    def partitionLabels(self,S:str)->List[int]:
        index={c:i for i,c in enumerate(S)}
        j,anchor=0,0
        ans=[]
        for i,c in enumerate(S):
            j=max(j,index[c])
            if i==j:
                ans.append(i-anchor+1)
                anchor=j+1
        return ans 
