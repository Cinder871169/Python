import math


def Prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1


for t in range(int(input())):
    a, b = [int(x) for x in input().split()]
    c = math.gcd(a, b)
    sum = 0
    while c > 0:
        sum += c % 10
        c = int(c / 10)
    if Prime(sum):
        print("YES")
    else:
        print("NO")
