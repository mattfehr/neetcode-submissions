"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
            
        # Maps original nodes to their cloned counterparts
        old_to_new = {node: Node(node.val)}
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            
            for neighbor in curr.neighbors:
                # If neighbor hasn't been cloned yet
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Link the clone's neighbor using the map
                old_to_new[curr].neighbors.append(old_to_new[neighbor])
                
        return old_to_new[node]
        
