def polynomial(a, n, x):
    res = a[0]
    for i in range(1, n + 1):
        res = res * x + a[i]
    return res


print("Nhap mang:")
a = list(map(int, input().split()))
print("Nhap x:")
x = float(input())
n = len(a) - 1
print(polynomial(a, n, x))

# P(x) = a0xn + a1xn-1+ . . . + an-1x + an = ((a0x + a1)x + a2)x + ... + an
