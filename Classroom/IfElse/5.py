a = float(input())
b = float(input())
c = float(input())
if a * b > b * c:
    if a * c > a * b:
        print(a * c)
    else:
        print(a * b)
else:
    print(b * c)
