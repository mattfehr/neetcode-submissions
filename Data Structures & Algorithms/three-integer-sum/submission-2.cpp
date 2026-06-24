class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> sol = {};

        for (int i=0; i < nums.size()-2; ++i) {
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            if (nums[i] > 0) break;
            
            int target = -nums[i];
            int l = i+1, r = nums.size()-1;
            //binary search
            while (l < r) {
                int curr_sum = nums[l] + nums[r];
                if (curr_sum < target) {
                    l += 1;
                } else if (curr_sum > target) {
                    r -= 1;
                } else {
                    sol.push_back({nums[i], nums[l], nums[r]});

                    //find more for same i
                    l += 1;
                    r -= 1;
                    while (l < r && nums[l] == nums[l-1]) l++;
                    while (l < r && nums[r] == nums[r+1]) r--;
                }
            }
        }
        return sol;
    }
};
