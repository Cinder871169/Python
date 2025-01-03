import queue


def check(n, arr):
    g = {}
    in_deg = {}
    nodes = set()

    for a, op, b in arr:
        nodes.add(a)
        nodes.add(b)
        if a not in g:
            g[a] = []
        if b not in g:
            g[b] = []
        if a not in in_deg:
            in_deg[a] = 0
        if b not in in_deg:
            in_deg[b] = 0

        if op == ">":
            g[a].append(b)
            in_deg[b] += 1
        elif op == "<":
            g[b].append(a)
            in_deg[a] += 1

    queue = []
    for i in nodes:
        if in_deg[i] == 0:
            queue.append(i)

    cnt = 0
    while queue:
        cur = queue.pop()
        cnt += 1
        for v in g[cur]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                queue.append(v)

    if cnt == len(nodes):
        return "possible"
    else:
        return "impossible"


arr = []
n = int(input())
for i in range(n):
    arr.append(input().split())
print(check(n, arr))

# 3
# An > Binh
# Binh > Cong
# An < Cong

# 3
# An > Binh
# Binh > Cong
# An > Cong
