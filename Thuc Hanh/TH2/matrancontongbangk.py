def solve(n, m, k, matrix):
    S = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            S[i][j] = S[i - 1][j] + S[i][j - 1] - S[i - 1][j - 1] + matrix[i - 1][j - 1]

    count = 0

    for start_row in range(1, n + 1):
        for start_col in range(1, m + 1):
            for end_row in range(start_row, n + 1):
                for end_col in range(start_col, m + 1):
                    total = (
                        S[end_row][end_col]
                        - S[start_row - 1][end_col]
                        - S[end_row][start_col - 1]
                        + S[start_row - 1][start_col - 1]
                    )

                    if total == k:
                        count += 1

    return count


for t in range(int(input())):
    n, m, k = map(int, input().split())
    matrix = [list(map(int, input().strip())) for _ in range(n)]
    res = solve(n, m, k, matrix)
    print(res)
