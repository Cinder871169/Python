def fmult(x, y, p):
    x = x % p
    y = y % p
    return (x * y) % p


x = int(input())
y = int(input())
p = int(input())
print(fmult(x, y, p))
