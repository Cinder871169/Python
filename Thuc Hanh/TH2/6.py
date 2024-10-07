def check(n, e):
    if len(e) != n - 1:
        return False

    deg = [0] * (n + 1)

    for u, v in e:
        deg[u] += 1
        deg[v] += 1

    center = 0
    leaf = 0

    for i in range(1, n + 1):
        if deg[i] == n - 1:
            center += 1
        elif deg[i] == 1:
            leaf += 1

    return center == 1 and leaf == n - 1


n = int(input())
e = [tuple(map(int, input().split())) for _ in range(n - 1)]

result = check(n, e)
print("Yes" if result else "No")
