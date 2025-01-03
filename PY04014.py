class HocSinh:
    def __init__(self, id, name, a):
        self.id = "HS{:02d}".format(id)
        self.name = name
        self.a = a
        self.tb = self.get_tb()
        self.rank = self.get_rank()

    def get_tb(self):
        return round((sum(float(i) for i in self.a) + float(self.a[0]) + float(self.a[1])) / 10 / 1.2, 1)

    def get_rank(self):
        if self.tb >= 9:
            return "XUAT SAC"
        elif self.tb >= 8:
            return "GIOI"
        elif self.tb >= 7:
            return "KHA"
        elif self.tb >= 5:
            return "TB"
        return "YEU"

    def __str__(self):
        return self.id + " " + self.name + " " + str(self.tb) + " " + self.rank


lst = []
for t in range(int(input())):
    name = input()
    a = [float(x) for x in input().split()]
    lst.append(HocSinh(t + 1, name, a))
lst.sort(key=lambda e: (-e.tb, e.id))
print(*lst, sep="\n")

# 3
# Luu Thuy Nhi
# 9.3  9.0  7.1  6.5  6.2  6.0  8.2  6.7  4.8  5.5
# Le Van Tam
# 8.0  8.0  5.5  9.0  6.8  9.0  7.2  8.3  7.2  6.8
# Nguyen Thai Binh
# 9.0  6.4  6.0  7.5  6.7  5.5  5.0  6.0  6.0  6.0
