def check(s):
    n = int(s)
    x = 0
    while n > 0:
        x += n % 10
        n = int(n / 10)
    if x % 10 != 0:
        return False
    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i - 1])) != 2:
            return False
    return True


for t in range(int(input())):
    s = input()
    if check(s) == True:
        print("YES")
    else:
        print("NO")
