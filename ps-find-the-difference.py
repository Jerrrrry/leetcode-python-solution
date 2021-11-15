class Solution:
        def findTheDifference(self,s:str,t:str)->str:
                data=0
                for c in t:
                        data+=ord(c)
                for c in s:
                        data-=ord(c)
                return chr(data)