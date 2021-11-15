#https://leetcode.com/discuss/interview-question/1519309/Amazon-phone-interview-passed.youch

class Solution:
        def wordBreak(self,s: str, wordDict: List[str])->bool:
                v=set()
                def check(p=0):
                        if p in v:
                                return False 

                        if p==len(s):
                                return True

                        v.add(p)

                        for w in wordDict:
                                if s[p:p+len(w)]==w:
                                        if check(p+len(w)):
                                                return True
                        return False
                return check()