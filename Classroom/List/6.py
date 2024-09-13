def check(lst):
    return lst == sorted(lst)


list1 = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
print(check(list1))
list2 = [1, 2, 4, 6, 8, 10, 12, 14, 17, 16]
print(check(list2))
