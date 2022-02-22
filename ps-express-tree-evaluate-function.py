import abc 
from abc import ABC, abstractmethod 

class Node(ABC):
        @abstractmethod
        def evaluate(self):
                pass
class Num(Node):
        def __init__(self,value:int):
                self.value=value
        def evaluate(self)->int:
                return self.value
class BN(Node):
        def __init__(self,l,r):
                self.l=l
                self.r=r
        def evaluate(self)->int:
                pass

class Plus(BN):
        def evaluate(self):
                return self.l.evaluate()+self.r.evaluate()

class Minus(BN):
        def evaluate(self):
                return self.l.evaluate()-self.r.evaluate()

class Multi(BN):
        def evaluate(self):
                return self.l.evaluate()*self.r.evaluate()
class Divide(BN):
        def evaluate(self):
                return self.l.evaluate()/self.r.evaluate()

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        operators = {'+': Plus, '-': Minus, '*': Multi, '/': Divide}
        q=[]
        for token in postfix:
            if token in operators:
                r=q.pop()
                l=q.pop()
                q.append(operators[token](l,r))
            else:
                q.append(Num(int(token)))
            
        return q[0]