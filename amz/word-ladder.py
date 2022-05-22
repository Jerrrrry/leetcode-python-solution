from typing import List
import string
import collections
class Solution:
        def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
                words=set(wordList)
                v=set()
                ls=string.ascii_lowercases

                if beginWord not in words and endWord not in words:
                        return 0

                q=collections.deque()

                q.append([beginWord])
                v.add(beginWord)

                while q:
                        n=len(q)

                        for _ in range(n):
                                tmp=q.popleft()
                                ln=tmp[-1]
                                for i in range(len(ln)):
                                        for l in ls:
                                                nw=tmp[:i]+l+tmp[i+1:]
                                                if nw not in v and nw in words:
                                                        if nw==endWord:
                                                                return len(tmp)+1
                                                        else:
                                                                q.append(tmp+[nw])
                                                                v.add(nw)

                                return 0