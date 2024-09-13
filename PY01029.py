import math

for t in range(int(input())):
    s = input()
    n = ""
    for i in s:
        n = i + n
    if math.gcd(int(s), int(n)) == 1:
        print("YES")
    else:
        print("NO")
