def solve(lst, index):
    return [row[:index] + row[index + 1 :] for row in lst]


list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print("Nhap cot can xoa:")
n = int(input())
print(solve(list1, n - 1))

list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
print("Nhap cot can xoa:")
n = int(input())
print(solve(list2, n - 1))
