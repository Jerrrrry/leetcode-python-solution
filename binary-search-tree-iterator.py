class BSTIterator:
    def __init__(self,root:TreeNode):
        self.stack=[]
        self.push_left(root)

    def next(self)->int:
        node=self.stack.pop()
        self.push_left(node.right)

    def hasNext(self)->bool:
        return self.stack

    def push_left(self,root):
        while root
            self.stack.append(root)
            root=root.left