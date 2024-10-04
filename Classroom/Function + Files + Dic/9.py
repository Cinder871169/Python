data = {"c1": "Red", "c2": "Green", "c3": None}
res = {k: i for k, i in data.items() if i is not None}
print(res)
