from datetime import datetime


class Data:
    def __init__(self, name, unit, finish):
        self.name = name
        self.unit = unit
        self.finish = finish
        self.id = self.get_id()
        self.speed = self.get_speed()

    def get_id(self):
        return "".join([i[:1].upper() for i in self.unit.split()]) + "".join([i[:1].upper() for i in self.name.split()])

    def get_speed(self):
        return 120 / (datetime.strptime(self.finish, "%H:%M") - datetime.strptime("6:00", "%H:%M")).seconds * 3600

    def __str__(self):
        return f"{self.id} {self.name} {self.unit} {round(self.speed)} Km/h"


lst = []
for t in range(int(input())):
    lst.append(Data(input(), input(), input()))
lst.sort(key=lambda e: -e.speed)
print(*lst, sep="\n")
# 3
# Tran Vu Minh
# Ha Noi
# 8:30
# Vu Ngoc Hoang
# Hoa Binh
# 8:20
# Pham Dinh Tan
# An Giang
# 8:45
