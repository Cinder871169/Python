def dfs(g, v, vs):
    vs[v] = True
    for i in g[v]:
        if not vs[i]:
            dfs(g, i, vs)


def tplt(n, e, x):
    g = [[] for _ in range(n + 1)]

    for u, v in e:
        g[u].append(v)
        g[v].append(u)

    vs = [False] * (n + 1)

    dfs(g, x, vs)

    res = [i for i in range(1, n + 1) if not vs[i]]

    return res


n, m, x = map(int, input().split())
e = [tuple(map(int, input().split())) for _ in range(m)]


ans = tplt(n, e, x)
for i in ans:
    print(i)
