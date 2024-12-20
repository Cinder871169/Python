def solve(n):
    s = 0
    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            s += (-1) ** ((i - 1) // 2) * (1 / i)
    else:
        for i in range(2, n + 1, 2):
            s += (-1) ** ((i // 2) - 1) * (1 / i)
    return f"{s:.5f}"


for t in range(int(input())):
    n = int(input())
    print(solve(n))
