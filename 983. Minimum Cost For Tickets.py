class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_day = days[-1]

        dp = [float('inf')] * (max_day + 1)
        dp[0] = 0

        for day in range(1, max_day + 1):
            # If the current day is not a travel day, the cost is the same as the previous day
            if day not in days:
                dp[day] = dp[day - 1]
            else:
                cost_1day = dp[day - 1] + costs[0]
                cost_7day = dp[max(0, day - 7)] + costs[1]
                cost_30day = dp[max(0, day - 30)] + costs[2]
                dp[day] = min(cost_1day, cost_7day, cost_30day)
        return dp[max_day]
