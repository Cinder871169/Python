print("Nhap n:", end=" ")
n = int(input())
lst = [0]
for i in range(1, n):
    x = int(input())
    lst.append(x)
lst.sort()
for i in range(1, n + 1):
    if lst[i] != i:
        print("So con thieu la:", end=" ")
        print(i)
        break
