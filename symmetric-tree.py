class Solution:
    def isSymmeytic(self,root:TreeNode)->bool:


    def isMirror(self,t1:TreeNode,t2:TreeNode)->bool:
        if not t1 and not t2:return True
        if not t1 or not t2:return False
        return t1.val==t2.val and self.isMirror(t1.right,t2.left) and self.isMirror(t1.left,t2.right)
