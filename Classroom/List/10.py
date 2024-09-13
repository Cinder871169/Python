def solve(mat):
    row_sum = [(sum(row), row) for row in mat]
    row_sum.sort()
    return [row for _, row in row_sum]


matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print(solve(matrix1))
print(solve(matrix2))
