class SinhVien:
    def __init__(self, msv, ten, lop):
        self.msv = msv
        self.ten = ten
        self.lop = lop
        self.score = ""

    def get_score(self, s):
        res = 10 - s.count('v') * 2 - s.count('m')
        if res <= 0:
            self.score = "0 KDDK"
        else:
            self.score = res

    def __str__(self):
        return f"{self.msv} {self.ten} {self.lop} {self.score}"


n = int(input())
lst = []
for t in range(n):
    lst.append(SinhVien(input(), input(), input()))
for k in range(n):
    id, s = map(str, input().split())
    for i in lst:
        if id == i.msv:
            i.get_score(s)
            break
print(*lst, sep="\n")

# 3
# B19DCCN999
# Le Cong Minh
# D19CQAT02-B
# B19DCCN998
# Tran Truong Giang
# D19CQAT02-B
# B19DCCN997
# Nguyen Tuan Anh
# D19CQCN04-B
# B19DCCN998 xxxmxmmvmx
# B19DCCN997 xmxmxxxvxx
# B19DCCN999 xvxmxmmvvm
