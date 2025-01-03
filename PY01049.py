import math


def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return n > 1


def check(s):
    if not prime(len(s)): return False
    cnt = 0
    for i in s:
        if prime(int(i)): cnt += 1
    if cnt * 2 < len(s): return False
    return True


for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
