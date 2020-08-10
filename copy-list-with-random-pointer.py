class Solution:
    def copyRandomList(self,head:'Node')->'Node':
        memo={}
        def copy(n):
            if not n:
                return 
            if n in memo:
                return memo[n]
            memo[n]=new=Node(n.val)
            new.next=copy(n.next)
            new.random=copy(n.random)
            return new 
        return copy(head)