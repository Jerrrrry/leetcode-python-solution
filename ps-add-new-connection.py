#https://leetcode.com/discuss/interview-question/344574/Amazon-or-Phone-Screen-or-Add-new-connection

#similar to lowest common anchestor 
from typing import TreeNode
import collections
class Solution:
        def __init__(self):
                self.parents=collections.defaultdict(TreeNode)
        def isValid(self,r1:TreeNode,r2:TreeNode)->bool:
                self.scan(r1)
                if r2 in self.parents:
                        return True
                else:
                        return False

        def scan(self,root:TreeNode)->None:
                if not root:return 
                for child in root.children:
                        if child:
                           self.parents[child]=root   
                           self.scan(child)  
                
