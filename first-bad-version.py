## isBadVersion()  function is given to use 

class Solution:
    def firstBadVersion(self,n):
        l=1
        r=n
        while l<r:
            m=l+(r-l)//2
            if isBadVersion(m):
                r=m
            else:
                l=m+1
        return l 