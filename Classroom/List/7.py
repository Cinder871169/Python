def solve(lst):
    cnt = {}
    for i in lst:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1

    max_count = max(cnt.values())
    res = []

    for item, count in cnt.items():
        if count == max_count:
            res.append(item)

    return " ".join(map(str, res))


lst = [int(x) for x in input().split()]
print(solve(lst))
