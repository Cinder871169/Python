def unique(lst):
    res = set(lst)
    return len(res) == len(lst)


lst = [int(x) for x in input().split()]
print(unique(lst))
