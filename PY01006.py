def check(s):
    for i in s:
        if i != '4' and i != '7':
            return False
    return True


for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
