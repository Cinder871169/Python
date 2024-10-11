def solve(n, arr):
    res = set()
    se = set()
    for i in arr:
        x = set()
        for j in se:
            res.add(i | j)
            x.add(i | j)
        res.add(i)
        x.add(i)
        se = x
    return len(res)


n = int(input())
arr = list(map(int, input().split()))
res = solve(n, arr)
print(res)
