import math

n = int(input())
a = []
rows = [0] * n
cols = [0] * n
res = 0
for i in range(n):
    s = input()
    for j in range(len(s)):
        if s[j] == 'C':
            rows[i] += 1
            cols[j] += 1
for i in rows:
    if i >= 2: res += math.comb(i, 2)
for i in cols:
    if i >= 2: res += math.comb(i, 2)
print(res)
# 4
# CC..
# C..C
# .CC.
# .CC.
