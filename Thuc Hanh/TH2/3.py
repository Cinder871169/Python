class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX


q = int(input())
uf = UnionFind(100000)

for _ in range(q):
    x, y, z = map(int, input().split())
    if z == 1:
        uf.union(x, y)
    elif z == 2:
        if uf.find(x) == uf.find(y):
            print(1)
        else:
            print(0)
