for t in range(int(input())):
    s = input()
    k = 1
    n = len(s)
    for i in range(1, n):
        if s[i] != s[i - 1]:
            print(k, end="")
            print(s[i - 1], end="")
            k = 1
        else:
            k += 1
    print(k, end="")
    print(s[n - 1])
