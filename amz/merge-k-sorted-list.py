# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q=[]
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q,(lists[i].val,i))
            
        ans=res=ListNode(0)
        while q:
            v,i=heapq.heappop(q)
            ans.next=ListNode(v)
            ans=ans.next
            lists[i]=lists[i].next
            if lists[i]:
                heapq.heappush(q,(lists[i].val,i))
                
        return res.next

##tc  nlogk 