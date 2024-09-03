tlist = []
for i in range(int(input())):
    tlist.append(int(input()))
tlist.sort(reverse=True)
print("Silver = ", tlist[1])
