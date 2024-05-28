class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(x, y, visited):

            gold_collected = grid[x][y]
            visited.add((x, y))

            max_gold = 0

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited and grid[nx][ny] > 0:
                    max_gold = max(max_gold, dfs(nx, ny, visited))

            visited.remove((x, y))
            return gold_collected + max_gold

        max_gold_collected = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    visited = set()
                    max_gold_collected = max(max_gold_collected, dfs(i, j, visited))

        return max_gold_collected
