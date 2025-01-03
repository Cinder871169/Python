def check(a, b, n):
    for i in range(n):
        if a[i] > b[i]: return False
    return True


for t in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    a.sort()
    b.sort()
    if check(a, b, n):
        print("YES")
    else:
        print("NO")
