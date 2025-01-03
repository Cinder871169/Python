import math


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % 2 == 0:
            return False
    return n > 1


def check(a, b):
    k = math.gcd(a, b)
    sum = 0
    for i in str(k):
        sum += int(i)
    if prime(sum):
        return "YES"
    return "NO"


for t in range(int(input())):
    a, b = [int(x) for x in input().split()]
    print(check(a, b))
