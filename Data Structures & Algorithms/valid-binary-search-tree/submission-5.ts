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
    isValidBST(root: TreeNode | null): boolean {
        // in order BST always produces increasing list
        let prev = -Infinity;
        const stack: TreeNode[] = [];
        let curr: TreeNode | null = root;

        while (stack.length > 0 || curr !== null) {
            // left
            while (curr !== null) {
                stack.push(curr);
                curr = curr.left;
            }

            // parent
            curr = stack.pop()!;
            if (curr.val <= prev) {
                return false;
            }

            // right
            prev = curr.val;
            curr = curr.right;
        }

        return true;
    }
}
