for t in range(int(input())):
    s = input()
    n = len(s)
    if s[n - 1] == "6" and s[n - 2] == "8":
        print("YES")
    else:
        print("NO")
