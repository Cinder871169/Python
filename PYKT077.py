from datetime import datetime


class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Schedule:
    def __init__(self, id, sub, date, time, group):
        self.id = "T{:03d}".format(id)
        self.sub = sub
        self.date = datetime.strptime(date, "%d/%m/%Y")
        self.time = time
        self.group = group

    def __str__(self):
        return f"{self.id} {self.sub.id} {self.sub.name} {self.date.strftime('%d/%m/%Y')} {self.time} {self.group}"


subjects = []
lst = []
n, m = map(int, input().split())
for i in range(n):
    subjects.append(Subject(input(), input()))
for i in range(m):
    id, date, time, group = input().split()
    for j in subjects:
        if id == j.id:
            lst.append(Schedule(i + 1, j, date, time, group))
lst.sort(key=lambda e: (e.date, e.time, e.sub.id))
print(*lst, sep="\n")

# 2 10
# INT1155
# Tin hoc co so 2
# INT1339
# Ngon ngu lap trinh C++
# INT1155 25/11/2021 08:00 01
# INT1155 04/12/2021 08:00 02
# INT1155 04/12/2021 13:30 03
# INT1155 25/11/2021 13:30 04
# INT1155 25/11/2021 15:00 05
# INT1339 25/11/2021 08:00 01
# INT1339 25/11/2021 08:00 02
# INT1339 04/12/2021 13:30 03
# INT1339 04/12/2021 13:30 04
# INT1339 04/12/2021 15:00 05
