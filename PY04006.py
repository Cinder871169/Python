import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, Point):
        d = math.sqrt((self.x - Point.x) ** 2 + (self.y - Point.y) ** 2)
        return d

    def Triangle(self, a, b):
        xy = self.distance(a)
        yz = a.distance(b)
        xz = self.distance(b)
        if xy + yz > xz and xz + yz > xy and xy + xz > yz:
            return "{:.2f}".format(math.sqrt((xy + yz + xz) * (xy + yz - xz) * (-xy + yz + xz) * (xy - yz + xz)) / 4)
        else:
            return "INVALID"


a = []
t = int(input())
for _ in range(t):
    a.extend(map(float, input().split()))

i = 0
for _ in range(t):
    p1 = Point(a[i], a[i + 1])
    p2 = Point(a[i + 2], a[i + 3])
    p3 = Point(a[i + 4], a[i + 5])
    print(p1.Triangle(p2, p3))
    i += 6
