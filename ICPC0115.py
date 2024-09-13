def gt(n):
    s = 1
    for i in range(n):
        s *= i + 1
    return s


def check(n):
    s = 0
    x = n
    while n > 0:
        s += gt(n % 10)
        n = n // 10
    if s == x:
        return True
    else:
        return False


for t in range(int(input())):
    n = int(input())
    if check(n):
        print("Yes")
    else:
        print("No")
