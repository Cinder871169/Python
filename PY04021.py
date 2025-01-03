from datetime import datetime


class Player:
    def __init__(self, id, name, start, end):
        self.id = id
        self.name = name
        self.start = start
        self.end = end
        self.time = self.get_time()

    def get_time(self):
        return (datetime.strptime(self.end, "%H:%M") - datetime.strptime(self.start, "%H:%M")).seconds

    def __str__(self):
        return self.id + " " + self.name + " " + "{} gio {} phut".format(self.time // 3600, self.time % 3600 // 60)


lst = []
for t in range(int(input())):
    lst.append(Player(input(), input(), input(), input()))
lst.sort(key=lambda e: -e.time)
print(*lst, sep="\n")

# 3
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00
