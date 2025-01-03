n = int(input())
a = [int(x) for x in input().split()]
cnt = 0
for i in range(n):
    for j in range(i):
        if a[i] < a[j]: cnt += 1
print(cnt)
