a = []
b = ["0", "2", "4", "6", "8"]


def Try(s):
    x = list(s)
    x.reverse()
    x = int(s + "".join(x))
    global a
    a = a + [x]
    if len(s) != 3:
        for i in b:
            Try(s + i)


for i in range(1, 5):
    Try(b[i])
a.sort()
for t in range(int(input())):
    n = int(input())
    for j in a:
        if j < n:
            print(j, end=" ")
        else:
            break
    print()
