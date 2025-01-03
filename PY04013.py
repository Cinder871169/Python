from datetime import datetime


class Data:
    def __init__(self, id, name, start, end, amount):
        self.id = "T{:02d}".format(id)
        self.name = name
        self.start = start
        self.end = end
        self.amount = amount
        self.time = datetime.strptime(self.end, "%H:%M") - datetime.strptime(self.start, "%H:%M")

    def __str__(self):
        return "{} {} {:.2f}".format(self.id, self.name, self.amount * 3600 / self.time.seconds)


lst = []

for t in range(int(input())):
    d = Data(t + 1, input(), input(), input(), int(input()))
    for i in lst:
        if i.name == d.name:
            i.amount += d.amount
            i.time += d.time
            break
    else:
        lst.append(d)

print(*lst, sep="\n")

# 10
# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35
