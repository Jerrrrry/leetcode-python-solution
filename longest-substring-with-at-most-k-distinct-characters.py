class Solution:
    def lengthOfLongestSubstringKDistinct(self,s:str,k:int)->int:
        seen={}
        j,res=0,0
        for i in range(len(s)):
            if s[i] not in seen:
                seen[s[i]]=1
            else:
                seen[s[i]]+=1
            while len(seen)>k:
                seen[s[j]]-=1
                if seen[s[j]]==0:
                    del seen[s[j]]
                j+=1
            res=max(res,i-j+1)
        return res