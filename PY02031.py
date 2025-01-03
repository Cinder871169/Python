import math


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1


n, m = map(int, input().split())
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
for i in range(n):
    for j in range(m):
        if prime(a[i][j]):
            a[i][j] = 1
        else:
            a[i][j] = 0
for i in a:
    print(*i, sep=" ")
