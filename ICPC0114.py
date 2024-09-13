import math


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1, 1):
        if n % i == 0:
            return False
    return n > 1


def check(n):
    if not prime(int(n)):
        return False
    s = sum(int(i) for i in n)
    if not prime(s):
        return False
    for i in n:
        if not prime(int(i)):
            return False
    return True


for t in range(int(input())):
    n = input()
    x = n[::-1]
    if check(n) and check(x):
        print("Yes")
    else:
        print("No")
