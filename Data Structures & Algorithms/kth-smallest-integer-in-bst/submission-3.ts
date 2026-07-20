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
     * @param {number} k
     * @return {number}
     */
    kthSmallest(root: TreeNode | null, k: number): number {
        // in order BST always produces increasing list
        let count = 0;
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
            if (count == k-1) {
                return curr.val;
            }
            count++;

            // right
            curr = curr.right;
        }

        return curr.val;
    }
}
