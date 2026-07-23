/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    sol = -Infinity;

    maxPathSum(root: TreeNode | null): number {
        const bruh = this.preorder(root);
        return this.sol;
    }

    preorder(node: TreeNode | null): number {
        if (!node) {
            return 0;
        }
        
        const left_max = Math.max(this.preorder(node.left), 0);
        const right_max = Math.max(this.preorder(node.right), 0);

        const curr_path = node.val + left_max + right_max;
        this.sol = Math.max(curr_path, this.sol);

        return node.val + Math.max(left_max, right_max);
    }
}
