class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) {
            return nums[0];
        }

        if (nums.size() == 0) {
            return 0;
        }
        int n = nums.size();

        // Scenario 1: Range [0, n-1) -> start=0, end=n-1
        // Scenario 2: Range [1, n)   -> start=1, end=n
        return max(robber(0, n - 1, nums), robber(1, n, nums)); //slice array to ignore last house
    }

    int robber(int start, int end, vector<int>& nums) {
        int prev_robbed = nums[start];  //max profit if previous house was robbed
        int prev_not_robbed = 0;        //max profit if previous was not robbed
        for (int i = start+1; i < end; ++i) {
            int rob = prev_not_robbed + nums[i];    //rob current house
            int not_rob = max(prev_robbed, prev_not_robbed);    //skip current house, take best outcome of previous house robbed or not
            prev_not_robbed = not_rob;
            prev_robbed = rob;
        }
        return max(prev_robbed, prev_not_robbed);
    }
};
