def unique(lst):
    res = set(lst)
    return len(res) == len(lst)


lst1 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
print(unique(lst1))

lst2 = [2, 4, 6, 8, 10, 12, 14]
print(unique(lst2))
