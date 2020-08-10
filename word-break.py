class Solution:
    def wordBreak(self,s:str,wordDict:List[str])->bool:
        wordDict=set(wordDict)
        visited=set()
        def dfs(cur_ind=0):
            if cur_ind in visited:
                return False
            visited.add(cur_ind)
            if cur_ind==len(s):
                return True
            for word in wordDict:
                if s[cur_ind:cur_ind+len(word)]==word:
                    if dfs(cur_ind+len(word)):
                        return True
            return False
        return dfs()