class Matrix:
    def __init__(self, rows, cols, a):
        self.rows = rows
        self.cols = cols
        self.a = a

    def mul(self):
        for i in range(self.rows):
            for j in range(self.rows):
                x = 0
                for k in range(self.cols):
                    x += (self.a[i][k] * self.a[j][k])
                print(x, end=" ")
            print()


for t in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    m = Matrix(n, m, a)
    m.mul()
