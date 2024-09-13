def solve(a):
    res = set(a[0])
    for i in a[1:]:
        res.intersection_update(i)
    return list(res)


a = [list(map(int, s.strip().split())) for s in input().split(",")]
print(solve(a))
