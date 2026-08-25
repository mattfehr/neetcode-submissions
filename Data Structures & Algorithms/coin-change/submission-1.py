class Solution:

  def coinChange(self, coins: List[int], amount: int) -> int:
    # Size amount + 1 to track indices from 0 up to amount
    dp = [-1 for i in range(amount + 1)]

    def dfs(curr):
      if curr > amount:
        return -1
      if curr == amount:
        return 0
      if dp[curr] != -1:
        return dp[curr]

      res = 1e9
      for denom in coins:
        subproblem = dfs(curr + denom)
        if subproblem != -1:
          res = min(res, 1 + subproblem)

      dp[curr] = res
      return res

    minCoins = dfs(0)
    return -1 if minCoins >= 1e9 else minCoins
