public class Solution {
    public int CoinChange(int[] coins, int amount) {
        List<int> dp = Enumerable.Repeat(amount + 1, amount + 1).ToList();
        dp[0] = 0;

        for (int a = 1; a < amount+1; ++a) {
            foreach (int c in coins) {
                if (a-c >= 0) {
                    dp[a] = Math.Min(dp[a], 1 + dp[a-c]);
                }
            }
        }
        return dp[amount] != amount + 1 ? dp[amount] : -1;
    }
}
