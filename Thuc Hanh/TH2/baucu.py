def cmp(a, b):
    if a[1] > b[1]:
        return -1
    if a[1] == b[1] and a[0] < b[0]:
        return -1
    return 1


n, m = map(int, input().split())
mp = {}
lst = list(map(int, input().split()))
for x in lst:
    if x in mp:
        mp[x] += 1
    else:
        mp[x] = 1
v = [(key, val) for key, val in mp.items()]
v.sort(key=lambda x: (x[1], -x[0]), reverse=True)
MAX_X = v[0][1]
i = 0
while i < len(v) and v[i][1] == MAX_X:
    i += 1
if i == len(v):
    print("NONE")
else:
    print(v[i][0])
