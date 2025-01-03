from sys import flags


class NhanVien:
    def __init__(self, id, name, d1, d2):
        self.id = "TS0" + str(id)
        self.name = name
        self.d1 = d1
        self.d2 = d2
        self.score = self.get_score()
        self.status = self.get_status()

    def get_score(self):
        while self.d1 > 10:
            self.d1 /= 10
        while self.d2 > 10:
            self.d2 /= 10
        return (self.d1 + self.d2) / 2

    def get_status(self):
        if self.score < 5:
            return "TRUOT"
        if self.score < 8:
            return "CAN NHAC"
        if self.score <= 9.5:
            return "DAT"
        return "XUAT SAC"

    def __str__(self):
        return self.id + " " + self.name + " " + "{:.2f}".format(self.score) + " " + self.status


lst = []
for t in range(int(input())):
    lst.append(NhanVien(t + 1, input(), float(input()), float(input())))
lst.sort(key=lambda e: -e.score)
print(*lst, sep="\n")

# 3
# Nguyen Thai Binh
# 45
# 75
# Le Cong Hoa
# 4
# 4.5
# Phan Van Duc
# 56
# 56
