rows = len(rowSum)
cols = len(colSum)

matrix = [[0] * cols for _ in range(rows)]

for i in range(rows):
    for j in range(cols):
        # Fill the cell with the minimum of the remaining rowSum and colSum
        matrix[i][j] = min(rowSum[i], colSum[j])

        # Update rowSum and colSum
        rowSum[i] -= matrix[i][j]
        colSum[j] -= matrix[i][j]

return matrix
