# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        data=[]
        ans=ListNode(0)
        tmp=ans
        
        for l in lists:
            t=l
            while t:
                heapq.heappush(data,t.val)
                t=t.next
                
        while data:
            tmp.next=ListNode(heapq.heappop(data))
            tmp=tmp.next
            
        return ans.next
                