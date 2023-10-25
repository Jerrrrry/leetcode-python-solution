import abc 
from abc import ABC, abstractmethod 
"""
This is the interface for the expression tree Node.
You should not remove it, and you can define some classes to implement it.
"""

class Node(ABC):
    @abstractmethod
    # define your fields here
    def evaluate(self) -> int:
        pass
class Num(Node):
    def __init__(self,n:int):
        self.n=n
    def evaluate(self)->int:
        return self.n
    
class BN(Node):
    def __init__(self,l,r):
        self.l=l
        self.r=r
    def evaluate(self)->int:
        pass
    
class Plus(BN):
    def evaluate(self)->int:
        return self.l.evaluate()+self.r.evaluate()
    
class Minus(BN):
    def evaluate(self)->int:
        return self.l.evaluate()-self.r.evaluate()
    
class Muti(BN):
    def evaluate(self)->int:
        return self.l.evaluate()*self.r.evaluate()
    
class Divide(BN):
    def evaluate(self)->int:
        return self.l.evaluate()//self.r.evaluate()

"""    
This is the TreeBuilder class.
You can treat it as the driver code that takes the postinfix input
and returns the expression tree represnting it as a Node.
"""

class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':
        d={'+':Plus,'-':Minus,'*':Muti,'/':Divide}
        q=[]
        for token in postfix:
            if token not in d:
                q.append(Num(int(token)))
            else:
                r=q.pop()
                l=q.pop()
                q.append(d[token](l,r))
        return q[-1]
        
		
"""
Your TreeBuilder object will be instantiated and called as such:
obj = TreeBuilder();
expTree = obj.buildTree(postfix);
ans = expTree.evaluate();
"""