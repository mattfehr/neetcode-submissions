# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.sol = float("-inf")
        
        def post_order(node):
            if not node:
                return 0
            
            # get max values from each subtree, if its negative ignore it
            left_sum = max(post_order(node.left), 0)
            right_sum = max(post_order(node.right), 0)

            # at every root, 3 options - combine, take left, take right
            curr_path = node.val + left_sum + right_sum # combine, deadend because for higher parents its a split
            self.sol = max(curr_path, self.sol)

            return node.val + max(left_sum, right_sum) # choose the max of the other two options
        
        post_order(root)
        return self.sol

            