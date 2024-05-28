class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_prices = float('inf')

        for i in range(0, len(prices)):
            if prices[i] < min_prices:
                min_prices = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_prices)
        return max_profit
