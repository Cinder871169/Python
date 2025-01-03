class Customer:
    def __init__(self, id, name, old, new):
        self.id = "KH{:02d}".format(id)
        self.name = name
        self.old = old
        self.new = new
        self.price = round(self.get_price())

    def get_price(self):
        x = self.new - self.old
        if x <= 50:
            return (x * 100) * 1.02
        elif x <= 100:
            return (50 * 100 + (x - 50) * 150) * 1.03
        return (50 * 100 + 50 * 150 + (x - 100) * 200) * 1.05

    def __str__(self):
        return self.id + " " + self.name + " " + str(int(self.price))


lst = []
for t in range(int(input())):
    lst.append(Customer(t + 1, input(), int(input()), int(input())))
lst.sort(key=lambda e: -e.price)
print(*lst, sep="\n")

# 3
# Le Thi Thanh
# 468
# 500
# Le Duc Cong
# 160
# 230
# Ha Hue Anh
# 410
# 612
