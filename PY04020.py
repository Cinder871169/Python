class Bill:
    def __init__(self, id, name, amount, price, discount):
        self.id = id
        self.name = name
        self.amount = amount
        self.price = price
        self.discount = discount

    def get_total(self):
        return self.price * self.amount - self.discount

    def __str__(self):
        return f"{self.id} {self.name} {self.amount} {self.price} {self.discount} {self.get_total()}"


lst = []
for t in range(int(input())):
    lst.append(Bill(input(), input(), int(input()), int(input()), int(input())))
lst.sort(key=lambda e: -e.get_total())
print(*lst, sep="\n")

# 3
# ML01
# May lanh SANYO
# 12
# 4000000
# 2400000
# ML02
# May lanh HITACHI
# 4
# 2550000000
# 0
# ML03
# May lanh NATIONAL
# 5
# 3000000
# 150000
