def gen(n):
    a = list(range(1, n + 1))
    v = []
    cnt = 0
    while True:
        s = "".join(map(str, a))
        v.append(s)
        cnt += 1
        check = False
        for i in range(n - 2, -1, -1):
            if a[i] < a[i + 1]:
                check = True
                a = a[: i + 1] + sorted(a[i + 1 :])
                for j in range(i + 1, n):
                    if a[j] > a[i]:
                        a[i], a[j] = a[j], a[i]
                        break
                break
        if not check:
            break
    print(cnt)
    for s in reversed(v):
        print(s, end=" ")
    print()


for t in range(int(input())):
    n = int(input())
    gen(n)
