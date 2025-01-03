def check(s):
    if len(s) < 3: return False
    k = 1
    while k < len(s) and s[k] > s[k - 1]:
        k += 1
    while k < len(s) and s[k] < s[k - 1]:
        k += 1
    return k == len(s)


for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
