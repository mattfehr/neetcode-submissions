#include <stack>

class Solution {
public:
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // Edge cases
        if (!subRoot) return true;  // Empty tree is always a subtree
        if (!root) return false;    // Non-empty tree cannot fit in empty tree

        // Correct stack initialization
        std::stack<TreeNode*> s;
        s.push(root);

        // Iterative Pre-order Traversal
        while (!s.empty()) {
            TreeNode* node = s.top();
            s.pop();

            // Match current node value with subRoot value
            if (node->val == subRoot->val) {
                if (isSameTree(node, subRoot)) {
                    return true;
                }
            }

            // Safe push: check for null before pushing to stack
            if (node->right) s.push(node->right);
            if (node->left) s.push(node->left);
        }

        return false;
    }

    bool isSameTree(TreeNode* p, TreeNode* q) {
        // Both empty nodes are structurally identical
        if (!p && !q) return true;
        
        // One empty and one populated means a mismatch
        if (!p || !q) return false;
        
        // Values match and structural recursion matches
        return (p->val == q->val) && 
               isSameTree(p->left, q->left) && 
               isSameTree(p->right, q->right);
    }
};
