class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for w in range(amount + 1):
            dp[0][w] = amount + 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):

                if coins[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = min(dp[i][j - coins[i - 1]] + 1, dp[i - 1][j])

        if dp[n][amount] > 0 and dp[n][amount] < amount + 1:
            return dp[n][amount]
        return -1


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        n = len(coins)

        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1