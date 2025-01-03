def solve(n, A, B, C):
    if n == 1:
        print(A, "->", C)
        return
    solve(n - 1, A, C, B)
    solve(1, A, B, C)
    solve(n - 1, B, A, C)


solve(int(input()), 'A', 'B', 'C')
