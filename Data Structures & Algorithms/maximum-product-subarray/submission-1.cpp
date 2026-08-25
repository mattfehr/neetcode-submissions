class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int sol = *max_element(nums.begin(), nums.end());
        int currMax = 1, currMin = 1;

        for (int n : nums) {
            if (n == 0) {
                currMax = 1, currMin = 1;
                continue;
            }
            int temp = currMax * n;
            currMax = max({currMax * n, currMin * n, n});
            currMin = min({temp, currMin * n, n});
            sol = max(sol, currMax);
        }

        return sol;
    }
};
