class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> diffs;
        for (int i=0; i < nums.size(); ++i) {
            int diff = target - nums[i];
            if (diffs.contains(diff)) return {diffs[diff], i};
            else diffs[nums[i]] = i;
        }
    }
};
