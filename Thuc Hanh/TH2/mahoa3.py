class DRM:

    def process(self, source):
        length = len(source)
        half = length // 2
        sum1 = 0
        sum2 = 0

        for i in range(half):
            sum1 += ord(source[i]) - ord("A")
            sum2 += ord(source[i + half]) - ord("A")

        result = []
        for i in range(half):
            c1 = ord(source[i]) - ord("A")
            c2 = ord(source[i + half]) - ord("A")
            c = (c1 + sum1) % 26
            c = (c + c2 + sum2) % 26
            result.append(chr(c + ord("A")))

        return "".join(result)

    def solve(self):
        s = input().strip()
        print(self.process(s))

    def run(self):
        t = int(input().strip())
        for _ in range(t):
            self.solve()


if __name__ == "__main__":
    DRM().run()
