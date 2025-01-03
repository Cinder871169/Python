a, k, n = [int(x) for x in input().split()]
b = k - a % k + a
flag = 0
for i in range(b, n + 1, k):
    print(i - a, end=" ")
    flag = 1
if flag == 0:
    print(-1)
