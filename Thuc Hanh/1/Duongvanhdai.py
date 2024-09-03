m = int(input())
v = int(input())
t = int(input())
d = input()
s = v * t
if d == "C":
    res = s % m
else:
    res = (m - s % m) % m
print(res)
