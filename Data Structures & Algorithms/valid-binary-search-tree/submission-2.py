# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # in order BST always produces increasing list
        prev = float('-inf')
        stack = []
        curr = root

        while stack or curr:
            # left
            while curr:
                stack.append(curr)
                curr = curr.left

            #parent
            curr = stack.pop()
            if curr.val <= prev:
                return False
            
            #right
            prev = curr.val
            curr = curr.right
        
        return True


        
    