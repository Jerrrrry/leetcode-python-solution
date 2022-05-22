#https://leetcode.com/problems/word-break/
#word break ii is also necessary
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words=set(wordDict)
        res=[]

        def check(index,path):
                if index>len(s):return
                if index==len(s):
                        res.append(' '.join(path))
                        return 
                for word in words:
                        if s[index:index+len(word)]==word:
                                check(index+len(word),path+[word])
        check(0,[])
        return res
c=Solution()
wd=['bat','man','batman','batmans','ba','t','man','s']
s='batmans'
print(c.wordBreak(s,wd))