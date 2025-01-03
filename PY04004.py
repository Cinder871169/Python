import math


def object(x, y):
    return PhanSo(x, y)


class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutgon(self):
        k = math.gcd(self.tu, self.mau)
        self.tu = self.tu / k
        self.mau = self.mau / k

    def add(self, PhanSo):
        x = self.tu * PhanSo.mau + PhanSo.tu * self.mau
        y = self.mau * PhanSo.mau
        return object(x, y)

    def __str__(self):
        return "{}/{}".format(int(self.tu), int(self.mau))


x1, y1, x2, y2 = map(int, input().split())
p = PhanSo(x1, y1)
q = PhanSo(x2, y2)
res = p.add(q)
res.rutgon()
print(res)
