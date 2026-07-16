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
     * @param {TreeNode} subRoot
     * @return {boolean}
     */
    public isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
        // If the main root is null, it cannot contain any subtree
        if (!root) return false;
        
        const stack: TreeNode[] = [root];

        while (stack.length > 0) {
            const node = stack.pop()!;
            
            if (node.val === subRoot?.val) {
                if (this.isSameTree(node, subRoot)) return true;
            }

            if (node.left !== null) stack.push(node.left);
            if (node.right !== null) stack.push(node.right);
        }
        return false;
    }
    isSameTree(p: TreeNode | null, q: TreeNode | null): boolean {
        if (!p && !q) {
            return true;
        }
        if (p && q && p.val === q.val) {
            return this.isSameTree(p.left, q.left) && this.isSameTree(p.right,q.right);
        } else {
            return false;
        }
    }
}
