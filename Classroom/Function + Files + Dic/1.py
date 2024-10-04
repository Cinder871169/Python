def fpower(a, n, p):
    res = 1
    a = a % p
    while n > 0:
        if n % 2 == 1:
            res = (res * a) % p
        a = (a * a) % p
        n = n // 2
    return res


a = int(input())
n = int(input())
p = int(input())
print(fpower(a, n, p))
