class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sol = nums.size();

        for (int i = 0; i < nums.size(); ++i) {
            sol ^= i ^ nums[i];
        }
        return sol;
    }
};
