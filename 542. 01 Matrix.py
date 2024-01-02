import collections
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        visited = [[0 for i in range(m)] for j in range(n)]
        dist = [[0 for i in range(m)] for j in range(n)]
        q = collections.deque()

        for i in range(n):
            for j in range(m):
                if (mat[i][j] == 0):
                    q.append([[i, j], 0])
                    visited[i][j] = 1
                else:
                    visited[i][j] = 0

        delrow = [-1, 0, 1, 0]
        delcol = [0, 1, 0, -1]

        while (len(q) > 0):
            data = q.popleft()
            row = data[0][0]
            col = data[0][1]
            steps = data[1]

            dist[row][col] = steps

            for i in range(4):
                nrow = row + delrow[i]
                ncol = col + delcol[i]
                if (nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and visited[nrow][ncol] == 0):
                    visited[nrow][ncol] = 1
                    q.append([[nrow, ncol], steps + 1])

        return dist