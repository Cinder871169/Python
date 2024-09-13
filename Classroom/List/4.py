def solve(a):
    res = set(a[0])
    for i in a[1:]:
        res.intersection_update(i)
    return list(res)


a = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
print(solve(a))
