from collections import deque
def bfs(self, grid, visited, u, v):
    row = len(grid)
    col = len(grid[0])
    q = deque()
    q.append((u, v))
    visited[u][v] = True
    while q:
        u, v = q.popleft()
        for i in range(max(0, u - 1), min(row, u + 2)):
            for j in range(max(0, v - 1), min(col, v + 2)):
                if grid[u][v] == 1 and visited[i][j] == False:
                    q.append((i, j))
                    visited[i][j] = True
def numIslands(self, grid):
    row = len(grid)
    col = len(grid[0])
    res = 0
    visited = [[False] * col for i in range(row)]
    for u in range(row):
        for v in range(col):
            if grid[u][v] == 1 and visited[u][v] == False:
                res += 1
                self.bfs(grid, visited, u, v)
    return res
