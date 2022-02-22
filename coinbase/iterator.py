from abc import ABC,abstractmethod
from re import T
from typing import List
class Iterator(ABC):
        @abstractmethod
        def hasNext(self)->bool:pass
        @abstractmethod
        def getNext(self)->int:pass

class NormalIterator(Iterator):
        def __init__(self,nums:list):
                self.data=[-1]+nums
                self.o=0
                self.e=len(nums)

        def hasNext(self)->bool:
                if self.o+1<=self.e:
                        return True
                else:
                        return False 
        def getNext(self)->int:
                if self.hasNext():
                        self.o+=1
                        return self.data[self.o]
                else:
                        return -1
class JumpIterator(Iterator):
        def __init__(self,nums:List[int],start:int,end:int,step:int):
                self.data=[-1]+nums

                if step<=0:
                        self.step=1
                else:
                        self.step=step
                if 1<=start<=len(nums)-self.step:
                        self.o=start-step
                else:
                        self.o=0
                

                if end>len(nums) or end<1:
                        self.end=len(nums)
                else:
                        self.end=end
                if (self.end-self.o)%self.step!=0:
                        self.end=(self.end-self.o)//self.step
                
        def hasNext(self)->bool:
                if self.o+self.step<=self.end:
                        return True
                else:
                        return False 

        def getNext(self)->int:
                if self.hasNext():
                        self.o+=self.step
                        return self.data[self.o]
                else:
                        return -1
class Solution:
        def __init__(self,nums:list):
                self.data=[-1]+nums
                self.o=0
                self.e=len(nums)

        def hasNext(self)->bool:
                if self.o+1<=self.e:
                        return True
                else:
                        return False 
        def getNext(self)->int:
                if self.hasNext():
                        self.o+=1
                        return self.data[self.o]
                else:
                        return -1

data=[1,2,4,5,6,7,8,98,100]
print('this is normal iterator')
c=NormalIterator(data)
while c.hasNext():
        print(c.getNext())

print('---------------')

j=JumpIterator(data,2,8,2)


while j.hasNext():
        print(j.getNext())
