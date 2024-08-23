def check(s):
    a = ""
    for pos in s:
        a = pos + a
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(a[i]) - ord(a[i - 1])):
            return False
    return True


for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
