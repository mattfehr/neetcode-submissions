/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    int sol = INT_MIN;

    int maxPathSum(TreeNode* root) {
        int bruh = post_order(root);
        return sol;
    }

    int post_order(TreeNode* node) {
        if (!node) {
            return 0;
        }

        int left_sum = max(post_order(node->left), 0);
        int right_sum = max(post_order(node->right), 0);

        int curr_path = node->val + left_sum + right_sum;
        sol = max(curr_path, sol);
        
        return node->val + max(left_sum, right_sum);
    }
};
