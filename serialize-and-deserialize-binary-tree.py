class Codec:
    def serialize(self,root):
        data=[]
        def preorder(root):
            if not root:
                data.append("#")
            else:
                data.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return data
    def deserialize(self,data):
        data=collections.deque(data)
        def build():
            if data:
                val=data.popleft()
                if val=="#":
                    return None
                root=TreeNode(int(val))
                root.left=build()
                root.right=build()
                return root
        return build()