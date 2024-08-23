p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    inp = input()
    if inp == "0":
        break
    k, s = inp.split()
    k = int(k)
    res = ""
    for i in s:
        pos = 0
        for j in p:
            if i == j:
                break
            pos += 1
        pos = (pos + k) % 28
        res = p[pos] + res
    print(res)
