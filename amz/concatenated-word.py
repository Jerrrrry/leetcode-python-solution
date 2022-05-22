#https://leetcode.com/problems/concatenated-words/
from typing import List
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res=[]
        words=set(words)

        def check(w):
                for i in range(1,len(w)):
                        f=w[:i]
                        s=w[i:]

                        if f in words and (s in words or check(s)):
                                return True
                return False
        for word in words:
                if check(word):res.append(word)

        return res

class Another:
        def find(self, words: List[str]) -> List[str]:
                res=[]
                words=set(words)

                def check(w):
                        ans=[]
                        for i in range(1,len(w)):
                                f=w[:i]
                                s=w[i:]
                                t=check(s)
                                if f in words and s in words:
                                        ans.append([f,s])
                                elif f in words and len(t)>0:
                                        for x in t:
                                                ans.append([f]+x)

                        return ans

                for word in words:
                        t=check(word)
                        for x in t:
                                res.append(x)

                return res

a=Another()
data=["rockstar", "rock", "stars", "rocks", "tar", "star", "rockstars", "super", "highway", "high", "way", "superhighway"]
print(a.find(data))
                                

                