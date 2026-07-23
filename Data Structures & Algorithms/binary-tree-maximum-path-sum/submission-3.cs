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
    private int sol = int.MinValue;

    public int MaxPathSum(TreeNode root) {
        int _ = Preorder(root);
        return sol;
    }

    private int Preorder(TreeNode node) {
        if (node is null) {
            return 0;
        }

        int left_sum = Math.Max(Preorder(node.left), 0);
        int right_sum = Math.Max(Preorder(node.right), 0);

        int curr_path = node.val + left_sum + right_sum;
        sol = Math.Max(sol, curr_path);

        return node.val + Math.Max(left_sum, right_sum);
    }
}
