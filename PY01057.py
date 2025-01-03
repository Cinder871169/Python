import math


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def check(s):
    for i in range(len(s)):
        index_prime = is_prime(i + 1)
        digit_prime = is_prime(int(s[i]))
        if (index_prime and not digit_prime) or (not index_prime and digit_prime):
            return False
    return True


for _ in range(int(input())):
    print("YES" if check(input().strip()) else "NO")
