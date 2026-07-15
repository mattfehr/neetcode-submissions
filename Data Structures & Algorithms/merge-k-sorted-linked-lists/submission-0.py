# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointers = []
        for i, head in enumerate(lists):
            if head:
                # Format: (node value, index tie-breaker, node object)
                heapq.heappush(pointers, (head.val, i, head))

        dummy = ListNode()
        curr = dummy

        while pointers:
            val, i, node = heapq.heappop(pointers)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(pointers, (node.next.val, i, node.next))
        
        return dummy.next