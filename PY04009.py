class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def add(self, o):
        a = self.thuc + o.thuc
        b = self.ao + o.ao
        return SoPhuc(a, b)

    # a + bi , c + di
    def mul(self, o):
        a = self.thuc * o.thuc - self.ao * o.ao
        b = self.thuc * o.ao + self.ao * o.thuc
        return SoPhuc(a, b)

    def __str__(self):
        if self.ao > 0:
            return "{} + {}i".format(self.thuc, self.ao)
        else:
            return "{} - {}i".format(self.thuc, abs(self.ao))


for t in range(int(input())):
    a = [int(x) for x in input().split()]
    s1 = SoPhuc(a[0], a[1])
    s2 = SoPhuc(a[2], a[3])
    s3 = s1.add(s2)
    s4 = s3.mul(s1)
    s5 = s3.mul(s3)
    print(s4, ", ", s5, sep="")
