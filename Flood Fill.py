class Solution:
    def dfs(self, row, col, ans, image, newColor, delRow, delCol, ini):
        ans[row][col] = newColor
        n = len(image)
        m = len(image[0])

        for i in range(4):
            nrow = row + delRow[i]
            ncol = col + delCol[i]
            if (nrow >= 0 and nrow < n and ncol >= 0 and ncol < m and image[nrow][ncol] == ini and ans[nrow][
                ncol] != newColor):
                self.dfs(nrow, ncol, ans, image, newColor, delRow, delCol, ini)

    def floodFill(self, image, sr, sc, newColor):
        ini = image[sr][sc]
        ans = image
        delRow = [-1, 0, +1, 0]
        delCol = [0, +1, 0, -1]

    self.dfs(sr, sc, ans, image, newColor, delRow, delCol, ini)
    return ans
