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
    public bool IsValidBST(TreeNode root) {
        int prev = int.MinValue;
        Stack<TreeNode> stack = new();
        TreeNode curr = root;

        while (stack.Count > 0 || curr is not null) {
            while (curr is not null) {
                stack.Push(curr);
                curr = curr.left;
            }

            curr = stack.Pop();
            if (curr.val <= prev) {
                return false;
            }

            prev = curr.val;
            curr = curr.right;
        }

        return true;
    }
}
