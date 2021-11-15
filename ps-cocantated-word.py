#https://leetcode.com/problems/concatenated-words/discuss/1463933/Python3-hash

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        seen = set(words)
        
        @cache
        def fn(word):
            """Return True if input is a concatenated word."""
            for i in range(1, len(word)): 
                prefix = word[:i]
                suffix = word[i:]
                if prefix in seen and (suffix in seen or fn(suffix)): return True 
            return False 
        
        ans = []
        for word in words: 
            if fn(word): ans.append(word)
        return ans
############################################################ 
class Trie: 
    
    def __init__(self): 
        self.root = {}
        
    def insert(self, word): 
        node = self.root
        for ch in reversed(word): 
            node = node.setdefault(ch, {})
        node["#"] = True
        
    def search(self, word): 
        """Return True if input is a concatenated word."""
        dp = [True] + [False] * len(word)
        for i in range(len(word)): 
            node = self.root
            for j in reversed(range(i+1)): 
                if word[j] not in node: break 
                node = node[word[j]]
                if dp[j] and node.get("#"):
                    dp[i+1] = True 
                    break 
        return dp[-1]


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        trie = Trie()
        for word in sorted(words, key=len): 
            if word: 
                if trie.search(word): ans.append(word)
                trie.insert(word)
        return ans