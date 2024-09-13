for t in range(int(input())):
    n = int(input())
    s = 0
    x = 2
    if n % 2 == 1:
        x = 1
    for i in range(x, n + 1, 2):
        s += 1 / i
    print("{:.6f}".format(s))
