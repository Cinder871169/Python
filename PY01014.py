a, k, n = [int(x) for x in input().split()]
flag = 0
b = k - a % k + a
for i in range(b, n + 1, k):
    print(i - a, end=" ")
    flag = 1
if flag == 0:
    print(-1)
