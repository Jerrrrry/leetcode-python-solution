# Definition for a binary tree node.
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def scan(node):
                if not node:
                        return [0,0]
                left=scan(node.left)
                right=scan(node.right)
                r=node.val+left[1]+right[1]
                nr=max(left)+max(right)

                return [r,nr]

        return max(scan(root))

s=Solution()
print(s.rob([3,2,3,None,3,None,1]))