class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList=set(wordList)
        wordList.discard(beginWord)
        
        def neis(word):
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nw=word[:i]+c+word[i+1:]
                    if nw in wordList:
                        yield nw
                        
        l={}
        l[beginWord]=[[beginWord]]
        
        res=[]
        
        while l:
            nl=collections.defaultdict(list)
            
            for key,paths in l.items():
                if key==endWord:
                    return paths
                for nei in neis(key):
                    for path in paths:
                        nl[nei].append(path+[nei])
                        
            wordList-=set(nl.keys())
            l=nl
        return []