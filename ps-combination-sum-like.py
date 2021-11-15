# Question:
# Given an array of size n with unique positive integers and a positive integer K,
# check if there exists a combination of elements in the array satisfying below constraints.
# a. The sum of all such elements is K
# b. None of those elements are adjacent in the original array

# Ex:
# Input:
# arr = {1, 9, 8, 3, 6, 7, 5, 11, 12, 4}
# K = 14

# Output:
# [3, 7, 4]
from typing import List

class Solution:
        def __init__(self):
                self.res=[]
        
        def combinationSum(self,nums:List[int],target:int)->bool:
                self.dfs(nums,target,[])
                print(self.res)
                return True

        def dfs(self,data:List[int],target:int,path:List[int])->None:
                if target<0:return 
                if target==0 and sorted(path) not in self.res:
                        self.res.append(sorted(path))
                        return 
                for x in range(len(data)):
                        if target-data[x]>=0:
                                self.dfs(data[:x]+data[x+1:],target-data[x],path+[data[x]])

code=Solution()
nums=[2,4,6,7,23,55,66,44,22,10]
code.combinationSum(nums,20)