import math


def check(a, b):
    if math.gcd(a, b) == 1:
        return True
    return False


l, r = [int(x) for x in input().split()]
r += 1
for i in range(l, r):
    for j in range(i + 1, r):
        for k in range(j + 1, r):
            if check(i, j) and check(j, k) and check(i, k):
                print("(", end="")
                print(i, end=", ")
                print(j, end=", ")
                print(k, end=")\n")
