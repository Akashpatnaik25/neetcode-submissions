
class Solution:
    def solve(self, index: int, shouldBuy: int, prices: List[int], dp: List[List[int]]) -> int:
        if index >= len(prices):
            return 0

        if dp[index][shouldBuy] != -1:
            return dp[index][shouldBuy]

        profit = 0
        if shouldBuy:
            buy = -prices[index] + self.solve(index + 1, 0, prices, dp)
            dont_buy = 0 + self.solve(index + 1, 1, prices, dp)
            profit = max(buy, dont_buy)
        else:
            sell = prices[index] + self.solve(index + 1, 1, prices, dp)
            dont_sell = 0 + self.solve(index + 1, 0, prices, dp)
            profit = max(sell, dont_sell)

        dp[index][shouldBuy] = profit

        return dp[index][shouldBuy]


    def maxProfit(self, prices: List[int]) -> int:
        return self.solve(0, 1, prices, [[-1] * 2 for _ in range(len(prices) + 1)])

