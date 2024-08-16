import math

for t in range(int(input())):
    n, x, m = [float(x) for x in input().split()]
    x /= 100
    res = math.log(m / n, 1 + x)
    if res != int(res):
        res += 1
    print(int(res))
