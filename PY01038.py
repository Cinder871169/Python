for t in range(int(input())):
    n = int(input())
    while n % 7 != 0:
        n += int(str(n)[::-1])
    print(n)
