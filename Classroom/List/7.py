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


lst = [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 4, 6, 9, 1, 2]
print(solve(lst))
