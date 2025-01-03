class ThiSinh:
    def __init__(self, name, dob, x, y, z):
        self.name = name
        self.dob = dob
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "{} {} {}".format(self.name, self.dob, "%.1f" % (self.x + self.y + self.z))


name = input()
dob = input()
x, y, z = float(input()), float(input()), float(input())
t = ThiSinh(name, dob, x, y, z)
print(t)
