def Try(s, b, a):
    x = list(s)
    x.reverse()
    x = int(s + "".join(x))
    a.append(x)
    if len(s) != 3:
        for i in b:
            Try(s + i, b, a)


b = ["0", "2", "4", "6", "8"]
a = []

for i in range(1, 5):
    Try(b[i], b, a)
a.sort()
for _ in range(int(input())):
    n = int(input())
    result = [x for x in a if x < n]
    print(" ".join(map(str, result)))
