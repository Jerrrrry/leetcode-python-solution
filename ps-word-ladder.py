import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wl=set(wordList)
        visited=set()
        q=collections.deque([(beginWord,1)])
        alpha=string.ascii_lowercase
        
        while q:
            word,l=q.popleft()
            if word==endWord:
                return l
            for i in range(len(word)):
                for c in alpha:
                    nw=word[:i]+c+word[i+1:]
                    if nw in wl and nw not in visited:
                        q.append((nw,l+1))
                        visited.add(nw)
                        
        return 0