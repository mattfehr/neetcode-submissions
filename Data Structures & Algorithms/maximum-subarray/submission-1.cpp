class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = nums[0];
        int curr_sum = 0;

        for (int n : nums) {
            if (curr_sum < 0) {
                curr_sum = 0;
            }
            curr_sum += n;
            max_sum = max(max_sum, curr_sum);
        }
        return max_sum;
    }
};
