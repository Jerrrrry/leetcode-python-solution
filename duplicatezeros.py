from typing import List
import collections
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        c=collections.Counter(arr)
        if c[0]==0:
            return arr
        zeros=c[0]
        print(zeros)
        n=len(arr)
        for i in range(len(arr)-1,-1,-1):
            print(i)
            if i+zeros<n:
                arr[i+zeros]=arr[i]
            if arr[i]==0:
                zeros-=1
                if i+zeros<n:
                    arr[i+zeros]=0
        
##[1,0,2,3,0,4,5,0]
arr=[1,0,2,3,0,4,5,0]
solution=Solution()
solution.duplicateZeros(arr)
print(arr)