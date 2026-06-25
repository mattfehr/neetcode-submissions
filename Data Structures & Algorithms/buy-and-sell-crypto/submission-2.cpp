class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0, r = 1, sol = 0;
        while (r < prices.size()) {
            if (prices[l] < prices[r]) {
                int profit = prices[r]-prices[l];
                sol = max(sol, profit);
            } else {
                l = r;
            }
            r++;
        }
        return sol;
    }
};
