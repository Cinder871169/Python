import math


class SinhVien:
    def __init__(self, id, ten, d1, d2, d3):
        self.id = "SV{:02d}".format(id)
        self.ten = self.chuan_hoa(ten)
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.score = self.get_score()
        self.rank = 0

    def chuan_hoa(self, ten):
        return " ".join([i.lower().capitalize() for i in ten.split()])

    def get_score(self):
        return math.ceil((self.d1 * 3 + self.d2 * 3 + self.d3 * 2) / 8 * 100) / 100

    def __str__(self):
        return f"{self.id} {self.ten} {self.score:.2f} {self.rank}"


lst = []
for t in range(int(input())):
    lst.append(SinhVien(t + 1, input(), float(input()), float(input()), float(input())))
lst.sort(key=lambda e: (-e.score, e.id))
lst[0].rank = 1
for i in range(1, len(lst)):
    if lst[i].score == lst[i - 1].score:
        lst[i].rank = lst[i - 1].rank
    else:
        lst[i].rank = i + 1
print(*lst, sep="\n")
