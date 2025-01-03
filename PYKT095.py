class Bill:
    def __init__(self, id, name, type, start, end):
        self.id = "KH{:02d}".format(id)
        self.name = self.chuan_hoa(name)
        self.factor = self.get_Factor(type)
        self.start = start
        self.end = end
        self.base = self.get_base()
        self.over = self.get_over()
        self.vat = self.get_vat()
        self.total = self.base + self.over + self.vat

    def chuan_hoa(self, name):
        return " ".join([i.title() for i in name.split()])

    def get_Factor(self, type):
        if type == "A":
            return 100
        if type == "B":
            return 500
        return 200

    def get_base(self):
        return min(self.end - self.start, self.factor) * 450

    def get_over(self):
        k = self.end - self.start - self.factor
        if k <= 0:
            return 0
        return k * 1000

    def get_vat(self):
        return self.over // 20

    def __str__(self):
        return f"{self.id} {self.name} {self.base} {self.over} {self.vat} {self.total}"


lst = []
for t in range(int(input())):
    name = input()
    a = input().split()
    lst.append(Bill(t + 1, name, a[0], int(a[1]), int(a[2])))
lst.sort(key=lambda e: -e.total)
print(*lst, sep="\n")

# 2
#  nGuyEn Hong Ngat
# C 200 278
#  Chu thi    minh
# A 120 160
