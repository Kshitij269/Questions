from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        perimeter = 0
        visited = set()

        def bfs(r, c):
            perimeter = 0
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < columns:
                        if grid[nr][nc] == 1:
                            if (nr, nc) not in visited:
                                visited.add((nr, nc))
                                queue.append((nr, nc))
                        else:
                            perimeter += 1  # Increment perimeter if adjacent cell is water
                    else:
                        perimeter += 1  # Increment perimeter for out-of-bounds cells

            return perimeter

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1 and (r, c) not in visited:
                    perimeter += bfs(r, c)

        return perimeter
