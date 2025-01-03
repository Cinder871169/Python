import math


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1


for t in range(int(input())):
    s = input()
    if prime(int(s[-4:])):
        print("YES")
    else:
        print("NO")
