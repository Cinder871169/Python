def check(s):
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")
    return len(s) >= 3 and a * b * c > 0 and a <= b <= c


def solve(i, s, n, lst):
    if i > n: return
    if check(s):
        lst += [s]
    if i < n:
        solve(i + 1, s + "A", n, lst)
        solve(i + 1, s + "B", n, lst)
        solve(i + 1, s + "C", n, lst)


lst = []
solve(0, "", int(input()), lst)
lst.sort(key=lambda e: (len(e), e))
for i in lst:
    print(i)
