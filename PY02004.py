n = int(input())
s = [int(i) for i in input().split()]
cnt = 0
for i in range(1, n):
    if s[i] != s[i - 1]: cnt += 1
print(cnt)
