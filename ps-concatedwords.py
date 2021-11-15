class Solution:
        def findAllCon(self,words:List[str])->List[str]:
                if not words:return words
                ans=[]
                seen=set()

                def dfs(word):
                        if not word:return []
                        if word in seen:return [word]

                        for i in range(1,len(word)):
                                li=dfs(word[i:])
                                if word[:i] in seen and li:
                                        return li+seen[word[:i]]
                        return []

                words.sort(key=lambda x:len(x))
                for word in words:
                        li=dfs(word)
                        if li:
                                res+=[li]
                        seen.add(word)
                return ans 
                