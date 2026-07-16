/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

public class Solution {    
    public bool IsSubtree(TreeNode root, TreeNode subRoot) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.Push(root);

        while (stack.Count != 0) {
            TreeNode node = stack.Pop();
            
            if (node.val == subRoot.val) {
                if (IsSameTree(node, subRoot)) return true;
            }

            if (node.left is not null) stack.Push(node.left);
            if (node.right is not null) stack.Push(node.right);
        }
        return false;
    }

    public bool IsSameTree(TreeNode p, TreeNode q) {
        if (p is null && q is null) {
            return true;
        }
        if (p is not null && q is not null && p.val == q.val) {
            return IsSameTree(p.left, q.left) && IsSameTree(p.right, q.right);
        } else {
            return false;
        }
    }
}
