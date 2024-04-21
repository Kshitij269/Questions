from functools import lru_cache
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def helper(row, col, moves):

            if row < 0 or row >= m or col < 0 or col >= n:
                return 1
            if moves == 0:
                return 0

            paths = helper(row - 1, col, moves - 1)
            paths += helper(row + 1, col, moves - 1)
            paths += helper(row, col - 1, moves - 1)
            paths += helper(row, col + 1, moves - 1)

            return paths

        return helper(startRow, startColumn, maxMove) % MOD


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        dp = [[[None] * (maxMove + 1) for _ in range(n)] for _ in range(m)]
        self.m = m
        self.n = n
        self.mod = 10 ** 9 + 7
        return self.helper(maxMove, startRow, startColumn, dp)

    def helper(self, maxMove, x, y, dp):
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return 1

        if maxMove <= 0:
            return 0

        if dp[x][y][maxMove] is not None:
            return dp[x][y][maxMove]

        res = 0

        res = (res + self.helper(maxMove - 1, x + 1, y, dp)) % self.mod
        res = (res + self.helper(maxMove - 1, x, y - 1, dp)) % self.mod
        res = (res + self.helper(maxMove - 1, x - 1, y, dp)) % self.mod
        res = (res + self.helper(maxMove - 1, x, y + 1, dp)) % self.mod

        dp[x][y][maxMove] = res

        return res
