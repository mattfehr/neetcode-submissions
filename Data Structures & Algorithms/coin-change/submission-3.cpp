class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount+1, amount+1); //amount+1 is the unreachable upper bounnd
        dp[0] = 0;

        for (int a = 1; a < amount+1; ++a) {    //solve small amounts first
            for (int c : coins) {   //try every coin
                if (a-c >= 0) { //possible - coin is small enough to be used for amount
                    dp[a] = min(dp[a], 1 + dp[a-c]);  //if you take the coin, you need to know the min count for the remaining ammount
                }
            }
        } 
        return dp[amount] != amount + 1 ? dp[amount] : -1;  //if default value is still the upper bound, a solution cant be reached
    }
};
