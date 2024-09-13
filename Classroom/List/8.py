def solve(lst, index):
    return [row[index] for row in lst]


lst = [list(map(int, s.strip().split())) for s in input().split(",")]
print("Nhap so cua cot can trich xuat:")
n = int(input())
print(solve(lst, n - 1))
