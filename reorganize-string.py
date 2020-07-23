class Solution:
    def reorganzieString(self,S:str)->str:
        c=collection.Counter(S)
        ans="#"
        while c:
            stop=True
            for item,times in c.most_common():
                if ans[-1]!=item:
                    ans+=item
                    c[item]-=1
                    if not c[item]:
                        del c[item]
                    stop=False
                    break
            if stop:break
        return ans[1:] if len(ans)==len(S)+1 else ""
