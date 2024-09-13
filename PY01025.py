s = input()
res = ""
x = -2
for i in range(len(s)):
    res = s[-i - 1] + res
    if x % 3 == 0:
        res = "," + res
    x += 1
print(res.strip(","))
