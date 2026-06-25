public class Solution {
    public int MaxProfit(int[] prices) {
        int l = 0, r = 1, max_profit = 0;
        while (r < prices.Length) {
            if (prices[l] < prices[r]) {
                int profit = prices[r]-prices[l];
                max_profit = Math.Max(profit, max_profit);
            } else {
                l = r;
            }
            r++;
        }
        return max_profit;
    }
}
