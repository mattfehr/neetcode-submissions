# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        prev = float('-inf')
        stack = []
        order = []
        curr = root

        while stack or curr:
            # left
            while curr:
                stack.append(curr)
                curr = curr.left

            #parent
            curr = stack.pop()
            order.append(curr.val)
            
            #right
            prev = curr.val
            curr = curr.right
        
        return order[k-1] 