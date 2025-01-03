def check(s):
    sum = 0
    mul = 1
    flag = 0
    for i in range(len(s)):
        if i % 2 == 1:
            sum += int(s[i])
        else:
            if s[i] != '0':
                flag = 1
                mul *= int(s[i])
    if flag == 0: mul = 0
    print(mul, sum)


for t in range(int(input())):
    s = input()
    check(s)
