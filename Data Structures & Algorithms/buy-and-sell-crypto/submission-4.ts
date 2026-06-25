class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices: number[]): number {
        let l = 0, r = 1, max_profit = 0;
        while (r < prices.length) {
            if (prices[l] < prices[r]) {
                const profit = prices[r]-prices[l];
                max_profit = Math.max(profit, max_profit);
            } else {
                l = r;
            }
            r++;
        }
        return max_profit;
    }
}
