#include <vector>
#include <algorithm>

class Solution {
private:
    std::vector<std::vector<int>> sol;
    std::vector<int> combo;
    std::vector<int> nums_copy;
    int target_val;

    void dfs(int idx, int curr_sum) {
        if (curr_sum > target_val) return;
        if (curr_sum == target_val) {
            sol.push_back(combo);
            return;
        }
        for (int i = idx; i < nums_copy.size(); ++i) {
            combo.push_back(nums_copy[i]);
            dfs(i, curr_sum + nums_copy[i]);
            combo.pop_back();
        }
    }

public:
    std::vector<std::vector<int>> combinationSum(std::vector<int>& nums, int target) {
        sol.clear(); // Clear state in case the object is reused
        combo.clear();
        nums_copy = nums;
        target_val = target;
        
        std::sort(nums_copy.begin(), nums_copy.end());
        dfs(0, 0);
        return sol;
    }
};
