from random import choice
class RandomizeSet():
    def __init__(self):
        self.d={}
        self.data=[]

    def insert(self,val:int)->bool:
        if val in self.dict:
            return False
        self.dict[val]=len(self.data)
        self.data.append(val)
        return True

    def remove(self,val:int)->bool:
        if val in self.dict:
            ls,idx=self.data[-1],self,self.d[val]
            self.data[idx],self.d[ls]=ls,idx
            self.data.pop()
            del self.d[val]
            return True
        return False
    
    def getRandom(self)->int:
        return choice(self.data)