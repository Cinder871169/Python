class Rectangle:
    def __init__(self, x, y, mau):
        self.x = x
        self.y = y
        self.mau = mau

    def perimeter(self):
        return (self.x + self.y) * 2

    def area(self):
        return self.x * self.y

    def color(self):
        return self.mau.lower().capitalize()


arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
if int(arr[0]) <= 0 or int(arr[1]) <= 0:
    print("INVALID")
else:
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
