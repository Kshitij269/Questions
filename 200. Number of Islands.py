import collections

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


def bfs(r, c):
    q = collections.deque()
    visited.add((r, c))
    q.append((r, c))
    while q:
        row, col = q.popleft()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            if (row + dr) in range(rows) and (col + dc) in range(columns) and grid[row + dr][col + dc] == "1" \
                    and (row + dr, col + dc) not in visited:
                q.append((row + dr, col + dc))
                visited.add((row + dr, col + dc))


rows, columns = len(grid), len(grid[0])
visited = set()
islands = 0

for r in range(rows):
    for c in range(columns):
        if grid[r][c] == "1" and (r, c) not in visited:
            bfs(r, c)
            islands += 1
print(islands)
