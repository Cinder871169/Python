def gcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y


def mod_calc(a, m):
    gcd_value, x, _ = gcd(a, m)
    if gcd_value != 1:
        raise Exception("Không tồn tại")
    return x % m


def solve(m):
    res = []
    for i in range(1, m):
        x = mod_calc(i, m)
        res.append(x)
    return res


with open("INPUT.TXT", "r") as file:
    m = int(file.readline().strip())

res = solve(m)

with open("OUTPUT.TXT", "w") as file:
    file.write(" ".join(map(str, res)))
