def solve(mat):
    row_sum = [(sum(row), row) for row in mat]
    row_sum.sort()
    return [row for _, row in row_sum]


matrix = [list(map(int, s.strip().split())) for s in input().split(",")]
print(solve(matrix))
