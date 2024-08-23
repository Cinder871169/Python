def check(s):
    for i in range(1, len(s)):
        if s[i - 1] > s[i]:
            return False
    return True


for i in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
