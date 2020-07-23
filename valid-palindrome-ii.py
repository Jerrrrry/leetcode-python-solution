class Solution:
    def validPalindrome(self,s:str)->bool:
        isPalindrome=lambda s:s==s[::-1]
        strPart=lambda s,x:s[:x]+s[x+1:]
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return isPalindrome(strPart(s,l)) or isPalindrome(strPart(s,r))
            l+=1
            r-=1
        return True