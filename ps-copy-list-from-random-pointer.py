class Solution:
        def copyRandomList(self,head:'Node')->'Node':
                v={}
                def copy(head):
                        if not head:
                                return 
                        if head in v:
                                return v[head]
                        v[head]=n=Node(head.val)
                        n.next=copy(head.next)
                        n.random=copy(head.random)
                        return n
                return copy(head)