import math


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutgon(self):
        k = math.gcd(self.tu, self.mau)
        self.tu = self.tu / k
        self.mau = self.mau / k

    def __str__(self):
        return "{}/{}".format(int(self.tu), int(self.mau))


x, y = map(int, input().split())
p = PhanSo(x, y)
p.rutgon()
print(p)
