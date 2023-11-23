import abc 
from abc import ABC, abstractmethod 

class Node(ABC):
        @abstractmethod
        def evaluate(self):
                pass

class Num(Node):
    def __init__(self,value:int):
        self.value=value

    def evaluate(self):
        return self.value

class BN(Node):
    def __init__(self,l,r):
        self.l=l
        self.r=r
    def evaluate(self):
        pass

class Plus(BN):
    def evaluate(self):
        return self.l.evaluate()+self.r.evaluate()

class Minus(BN):
    def evaluate(self):
        return self.l.evaluate()-self.r.evaluate()

class Mutiply(BN):
    def evaluate(self):
        return self.l.evaluate()*self.r.evaluate()
class Divide(BN):
    def evaluate(self):
        return self.l.evaluate()//self.r.evaluate()

def express(tokens):
    q=[]
    ops={'+':Plus,'-':Minus,'*':Mutiply,'/':Divide}
    for token in tokens:
        if token in ops:
            r=q.pop()
            l=q.pop()
            q.append(ops[token](l,r))
        else:
            q.append(Num(int(token)))

    return q[-1]