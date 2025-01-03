def check(s):
    sum = 0
    for i in s:
        sum += int(i)
    return sum % 3 == 0


for t in range(int(input())):
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")
