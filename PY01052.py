import math


def check(s):
    sum = 0
    for i in s:
        sum += int(i)
    return prime(sum)


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1


for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
