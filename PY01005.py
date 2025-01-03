s = input()
cnt = 0
for i in s:
    if i == '4':
        cnt += 1
    elif i == '7':
        cnt += 1
if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")
