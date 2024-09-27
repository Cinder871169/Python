ans = 0
a = int(input())
b = int(input())
for i in range(a, b + 1):
    res = 1
    for j in range(1, i + 1):
        res *= j
    ans += res
print(ans)
