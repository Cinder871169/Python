def check(lst):
    return lst == sorted(lst)


list1 = [int(x) for x in input().split()]
print(check(list1))
