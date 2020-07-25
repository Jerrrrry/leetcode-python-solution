class Solution:
    def isNumber(self,s:str)->bool:
        try:
            _=float(s.strip())
        except:
            return False
        return True