class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # Map original node objects directly to their copies
        old_to_new = {None: None}
        
        # Pass 1: Create all new nodes and store them in the map
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Pass 2: Connect the next and random pointers
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next
            
        return old_to_new[head]
