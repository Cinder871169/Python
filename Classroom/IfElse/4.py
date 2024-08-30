n = int(input())
if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    if n % 3328 == 0:
        print("Multiple leap")
    else:
        print("Leap")
else:
    print("NO")
