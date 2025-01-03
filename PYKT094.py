class PhongBan:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class NhanVien:
    def __init__(self, id, name, base_salary, days, phongban):
        self.id = id
        self.name = name
        self.base_salary = base_salary
        self.days = days
        self.phongban = phongban
        self.total = self.base_salary * self.days * self.get_Factor()

    def get_Factor(self):
        group, year = self.id[0], int(self.id[1:3])
        if group == "A":
            if year <= 3:
                return 10
            if year <= 8:
                return 12
            if year <= 15:
                return 14
            if year >= 16:
                return 20
        if group == "B":
            if year <= 3:
                return 10
            if year <= 8:
                return 11
            if year <= 15:
                return 13
            if year >= 16:
                return 16
        if group == "C":
            if year <= 3:
                return 9
            if year <= 8:
                return 10
            if year <= 15:
                return 12
            if year >= 16:
                return 14
        if group == "D":
            if year <= 3:
                return 8
            if year <= 8:
                return 9
            if year <= 15:
                return 11
            if year >= 16:
                return 13

    def __str__(self):
        return f"{self.id} {self.name} {self.phongban.name} {self.total * 1000}"


pb = []
nv = []
for i in range(int(input())):
    s = input()
    pb.append(PhongBan(s[:2], s[3:]))
for i in range(int(input())):
    s = input()
    for j in pb:
        if s[-2:] == j.id:
            nv.append(NhanVien(s, input(), int(input()), int(input()), j))
            break
print(*nv, sep="\n")
