def solve(lst, index):
    return [row[:index] + row[index + 1 :] for row in lst]


lst = [list(map(int, s.strip().split())) for s in input().split(",")]
print("Nhap cot can xoa:")
n = int(input())
print(solve(lst, n - 1))
