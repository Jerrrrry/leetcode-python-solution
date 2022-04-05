class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
                l,r=0,0
                data=set()
                res=0
                n=len(s)
                while l<n and r<n:
                        if s[r] not in data:
                                data.add(s[r])
                                res=max(res,len(data))
                                r+=1
                        else:
                                data.remove(s[l])
                                l+=1
                return res
