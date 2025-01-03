from datetime import datetime


class Customer:
    def __init__(self, id, name, room, start, end, fee):
        self.id = "KH{:02d}".format(id)
        self.name = name
        self.room = room
        self.start = start
        self.end = end
        self.fee = fee
        self.time = (datetime.strptime(end, "%d/%m/%Y") - datetime.strptime(start, "%d/%m/%Y")).days + 1
        self.pay = self.get_pay()

    def get_pay(self):
        if self.room[0] == '1': return 25 * self.time + self.fee
        if self.room[0] == '2': return 34 * self.time + self.fee
        if self.room[0] == '3': return 50 * self.time + self.fee
        return 80 * self.time + self.fee

    def __str__(self):
        return f"{self.id} {self.name} {self.room} {self.time} {self.pay}"


lst = []
for t in range(int(input())):
    lst.append(
        Customer(t + 1, input().strip(), input().strip(), input().strip(), input().strip(), int(input().strip())))
lst.sort(key=lambda e: -e.pay)
print(*lst, sep="\n")

# 3
# Huynh Van Thanh
# 103
# 05/06/2010
# 05/06/2010
# 15
# Le Duc Cong
# 106
# 08/03/2010
# 01/05/2010
# 220
# Tran Thi Bich Tuyen
# 207
# 10/04/2010
# 21/04/2010
# 96
