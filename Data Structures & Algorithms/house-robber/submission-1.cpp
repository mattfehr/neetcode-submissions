class Solution {
public:
    int rob(vector<int>& nums) {
        const int n = nums.size();
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return nums[0];
        }

        // dp[i] stores the max money possible robbing up to house i
        vector<int> dp(n, 0); 

        //base cases
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]);

        //build table iteratively from bottom up
        for (int i=2; i < n; ++i) {
            dp[i] = max(nums[i] + dp[i-2], dp[i-1]);
        }

        return dp[n-1];
    }
};
