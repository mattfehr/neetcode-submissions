# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        stack = [root]
        while stack:
            node = stack.pop()

            print(node.val)
            if node.val == subRoot.val:
                print('wtf')
                if self.isSameTree(node, subRoot):
                    return True
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


