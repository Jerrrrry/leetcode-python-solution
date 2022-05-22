# Definition for a binary tree node.
from typing import List,Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:return []
        res=[]
        def p(node):
            if not node:
                res.append(None)
            else:
                res.append(node.val)
                if node.left:
                    p(node.left)
                if node.right:
                    p(node.right)
        p(root)
        return res

c=Solution()
root = [1,None,2,3]
print(c.preorderTraversal(root))