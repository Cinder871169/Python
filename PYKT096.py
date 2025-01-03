class Team:
    def __init__(self, id, name, schoolname):
        self.id = "Team{:02d}".format(id)
        self.name = name
        self.schoolname = schoolname


class Candidate:
    def __init__(self, id, name, team):
        self.id = "C{:03d}".format(id)
        self.name = name
        self.team = team

    def __str__(self):
        return f"{self.id} {self.name} {self.team.name} {self.team.schoolname}"


teams = []
candidates = []
for i in range(int(input())):
    teams.append(Team(i + 1, input(), input()))
for i in range(int(input())):
    name = input()
    x = input()
    for j in teams:
        if x == j.id:
            candidates.append(Candidate(i + 1, name, j))
            break
candidates.sort(key=lambda e: e.name)
print(*candidates, sep="\n")

# 2
# BAV_MIS
# Banking Academy of Vietnam
# FTU Knights1
# Foreign Trade University
# 6
# Le Trung Toan
# Team01
# Nguyen Trinh Quoc Long
# Team01
# Giang Minh Tung
# Team01
# Nguyen Hang Giang
# Team02
# Nguyen Thanh Nhan
# Team02
# Nguyen Viet Duc
# Team02
