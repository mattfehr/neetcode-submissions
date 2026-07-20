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
    public int KthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new();
        TreeNode curr = root;
        int count = 0;

        while (stack.Count > 0 || curr is not null) {
            while (curr is not null) {
                stack.Push(curr);
                curr = curr.left;
            }

            curr = stack.Pop();
            if (count == k-1) {
                return curr.val;
            }
            count++;

            curr = curr.right;
        }
        return curr.val;
    }
}
