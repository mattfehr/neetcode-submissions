# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        curr = head
        while (curr):
            count += 1
            curr = curr.next

        target = count-n
        print(target)

        curr = ListNode(0, head)
        dummy = curr
        for i in range(target):
            curr = curr.next
        if curr.next and curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        return dummy.next
