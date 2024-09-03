s = input().split()
res = ""
for i in s:
    if len(i) >= len(res):
        res = i
print(res, len(res))
