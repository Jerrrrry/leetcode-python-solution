from collection import Counter

class Solution:
    def findAnagrams(self,s:str,p:str)->List[int]:
        answer=[]
        m,n=len(s),len(p)

        if m<n:
            return answer
        sc=Counter(s[:n-1])
        pc=Counter(p)

        for index in range(n-1,m):
            sc[s[index]]+=1
            if sc==pc:
                answer.append(index+1-n)
            sc[s[index+1-n]]-=1
            if sc[s[index+1-n]]==0:
                del sc[s[index+1-n]]

        return answer