d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}

res = {}
for i in d1:
    res[i] = d1[i]

for j in d2:
    if j in res:
        res[j] += d2[j]
    else:
        res[j] = d2[j]

print(res)
