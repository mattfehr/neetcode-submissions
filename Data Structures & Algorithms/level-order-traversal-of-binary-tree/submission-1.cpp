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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> sol;
        if (!root) {
            return sol;
        }
        
        deque<TreeNode*> q;
        q.push_back(root);
        
        while (!q.empty()) {
            int levelSize = q.size(); // Lock the size of the current level
            vector<int> level;
            
            for (int i = 0; i < levelSize; ++i) {
                TreeNode* node = q.front();
                q.pop_front();
                
                level.push_back(node->val);
                
                // Fixed: Push to queue ONLY if the child node exists
                if (node->left) {
                    q.push_back(node->left);
                }
                if (node->right) {
                    q.push_back(node->right);
                }
            }
            sol.push_back(level);
        }
        return sol;
    }
};
