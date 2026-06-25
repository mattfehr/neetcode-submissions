class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        sol = 0

        while r <= len(prices)-1:
            #print(f"l: {l}, r: {r}")
            if prices[l] > prices[r]:
                l = r
                r += 1
                #print(f"l: {l}, r: {r}")
                continue;

            profit = prices[r]-prices[l]
            sol = max(sol, profit)
            #print(profit, prices[l], prices[r])
            r += 1
        return sol

