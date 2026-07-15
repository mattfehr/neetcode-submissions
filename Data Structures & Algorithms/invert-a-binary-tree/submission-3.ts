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
     * @return {TreeNode}
     */
    invertTree(root: TreeNode | null): TreeNode {
        // Base case: if the node is null, stop recursion
        if (root === null) {
            return null;
        }

        // Swap using array destructuring (matches Python syntax)
        [root.left, root.right] = [root.right, root.left];

        // Recursively call on the subtrees
        this.invertTree(root.left);
        this.invertTree(root.right);

        return root;
    }
}
