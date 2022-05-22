#https://leetcode.com/discuss/interview-question/1556048/Amazon-or-Phone-Screen-or-SDE-2-or-Seattle
#https://leetcode.com/problems/combinations/
from typing import List
import sys
class Combination:
        def combine(self,n:int,k:int)->List[List[int]]:
                res=[]
                def build(index,number,path):
                        if number==0:
                                res.append(sorted(path))
                                return 
                        for i in range(index+1,n+1):
                                if i==n and number>1:
                                        return 
                                build(i,number-1,path+[i])
                build(0,n,[])
                return res

class phonescreen:
        def combine(self,data:List[int],k:int)->List[int]:
                res=[]
                v=set()
                sys.setrecursionlimit(1000000)
                def build(number,path):
                        if number==0:
                                m=tuple(sorted(path))
                                if m not in v:
                                        v.add(m)
                                        res.append(path)
                                        return
                        else: 
                                for x in data:
                                        build(number-1,path+[x])
                build(k,[])
                return res
test=phonescreen()
print(test.combine([1,2,3,4,5,6,7],4))
