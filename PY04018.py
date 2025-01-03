class GV:
    def __init__(self, stt, name, id, d1, d2):
        self.stt = "GV{:02d}".format(stt)
        self.name = name
        self.id = id
        self.d1 = d1
        self.d2 = d2
        self.subject = self.get_subject()
        self.score = self.get_score()
        self.status = self.get_status()

    def get_subject(self):
        if self.id[0] == 'A':
            return "TOAN"
        if self.id[0] == 'B':
            return "LY"
        return "HOA"

    def get_score(self):
        res = self.d1 * 2 + self.d2
        if self.id[1] == '1':
            return res + 2
        if self.id[1] == '2':
            return res + 1.5
        if self.id[1] == '3':
            return res + 1
        return res

    def get_status(self):
        if self.score >= 18: return "TRUNG TUYEN"
        return "LOAI"

    def __str__(self):
        return f"{self.stt} {self.name} {self.subject} {self.score:.1f} {self.status}"


lst = []
for t in range(int(input())):
    lst.append(GV(t + 1, input(), input(), float(input()), float(input())))
lst.sort(key=lambda e: -e.score)
print(*lst, sep="\n")

# 3
# Le Van Binh
# A1
# 7.0
# 3.0
# Tran Van Toan
# B3
# 4.0
# 7.0
# Hoang Thi Tam
# C2
# 7.0
# 6.0
