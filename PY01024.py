def check(s):
    sum = 0
    n = len(s)
    for i in s:
        sum += int(i)
    for i in range(1, n):
        if abs(ord(s[i - 1]) - ord(s[i])) != 2:
            return False
    if sum % 10 != 0:
        return False
    return True


for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
