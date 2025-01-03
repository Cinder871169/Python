def check(s):
    sum = 0
    for i in s:
        sum += int(i)
    x = str(sum)
    if len(x) > 1 and x == x[::-1]: return True
    return False


for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
