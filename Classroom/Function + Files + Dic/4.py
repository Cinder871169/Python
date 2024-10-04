import random


def check(x):
    if len(x) == len(set(x)):
        return 1
    return 0


def init(n, a, b):
    return [random.randint(a, b) for _ in range(n)]


print("Nhap so phan tu n:", end=" ")
n = int(input())
print("Nhap a: ", end="")
a = int(input())
print("Nhap b: ", end="")
b = int(input())
x = init(n, a, b)
print("Mang da tao: ", x)
if check(x) == 1:
    print("Yes")
else:
    print("No")
