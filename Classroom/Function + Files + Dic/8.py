a = {"item1": 45.50, "item2": 35, "item3": 41.30, "item4": 55, "item5": 24}
data = dict(sorted(a.items(), key=lambda x: x[1], reverse=True))
res = dict(list(data.items())[:3])
for i, j in res.items():
    print(f"{i} {j}")
