class ThiSinh:
    def __init__(self, id, ten, diem, dantoc, kv):
        self.id = "TS{:02d}".format(id)
        self.ten = self.chuan_hoa(ten)
        self.diem = diem
        self.dantoc = dantoc
        self.kv = kv
        self.total = self.diem + self.get_bonus()
        self.status = self.get_status()

    def chuan_hoa(self, ten):
        a = ten.split()
        return " ".join([i.lower().capitalize() for i in a])

    def get_bonus(self):
        res = 0
        if self.kv == "1":
            res += 1.5
        elif self.kv == "2":
            res += 1
        if self.dantoc != "Kinh":
            res += 1.5
        return res

    def get_status(self):
        if self.total >= 20.5:
            return "Do"
        return "Truot"

    def __str__(self):
        return f"{self.id} {self.ten} {self.total:.1f} {self.status}"


lst = []
for t in range(int(input())):
    lst.append(ThiSinh(t + 1, input(), float(input()), input(), input()))
lst.sort(key=lambda e: (-e.total, e.id))
print(*lst, sep="\n")

# 2
# Nguyen  hong ngat
# 22
# Kinh
# 1
#   Chu thi MINh
# 14
# Dao
# 3
