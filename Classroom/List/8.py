def solve(lst, index):
    return [row[index] for row in lst]


lst = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
print("Nhap so cua cot can trich xuat:")
n = int(input())
print(solve(lst, n - 1))
