import string 
import collections
class Solution:
        def ladderLength(self,beginWord:str,endWord:str,wordList:list[str])->int:
                words=set(wordList)
                if beginWord not in words and endWord not in words:
                        return 0
                letters=[x for x in string.ascii_lowercase]

                q=collections.deque()
                q.append([beginWord])
                v=set(beginWord)

                while q:
                        n=len(q)
                        for _ in range(n):
                                tmp=q.popleft()
                                ln=tmp[-1]

                                for i in range(len(ln)):
                                        for l in letters:
                                                nw=ln[:i]+l+ln[i+1:]
                                                if nw==endWord:
                                                        return len(tmp)+1

                                                if nw not in v and nw in words:
                                                        q.append(tmp+[nw])
                                                        v.add(nw)

                return 0 

