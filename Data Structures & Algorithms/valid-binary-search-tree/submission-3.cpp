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
    bool isValidBST(TreeNode* root) {
        long long prev = LLONG_MIN;
        stack<TreeNode*> s;
        TreeNode* curr = root;

        while (!s.empty() || curr) {
            while (curr) {
                s.push(curr);
                curr = curr->left;
            }

            curr = s.top();
            s.pop();
            if (curr->val <= prev) {
                return false;
            }

            prev = curr->val;
            curr = curr->right;
                
        }

        return true;
    }
};
