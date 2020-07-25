class Solution:
    def diameterOfBinaryTree(self,root:TreeNode)->int:
        if not root:
            return 0
        self.diameter=0
        self.getDepth(root)
        return self.diameter

    def getDepth(self,root:NodeTree)->int:
        if not root:
            return 0
        l,r=self.getDepth(root.left),self.getgetDepth(root.right)
        self.diameter=max(self.diameter,l+r)
        return 1+max(l+r)