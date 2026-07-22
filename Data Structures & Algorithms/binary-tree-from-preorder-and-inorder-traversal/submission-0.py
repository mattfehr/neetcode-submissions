# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_value = preorder[0]
        root = TreeNode(root_value)

        root_index = inorder.index(root_value)
        left_size = root_index

        root.left = self.buildTree(
            preorder[1 : left_size+1],
            inorder[ : root_index]
        )

        root.right = self.buildTree(
            preorder[1+left_size :],
            inorder[root_index+1 :]
        )

        return root
