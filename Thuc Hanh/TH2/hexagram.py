class Hexagram:
    SIZE = 12
    LINES = [
        [0, 2, 5, 7],  # Line #1
        [7, 8, 9, 10],  # Line #2
        [0, 3, 6, 10],  # Line #3
        [1, 2, 3, 4],  # Line #4
        [4, 6, 9, 11],  # Line #5
        [1, 5, 8, 11],  # Line #6
    ]

    def __init__(self):
        self.numbers = []

    def read_input(self):
        self.numbers = list(map(int, input().split()))
        if any(n == 0 for n in self.numbers):
            return None
        return self.numbers

    def get_permutations(self, index, permutation, used, magic_sum):
        if index == len(permutation):
            return 1

        stars = 0
        for i in range(len(permutation)):
            if not used[i]:
                valid_index = True

                for line in self.LINES:
                    if index == line[3]:
                        check_sum = self.numbers[i]

                        for j in range(len(line) - 1):
                            perm_index = permutation[line[j]]
                            check_sum += self.numbers[perm_index]

                            if check_sum > magic_sum:
                                valid_index = False
                                break

                        if check_sum != magic_sum:
                            valid_index = False

                if valid_index:
                    permutation[index] = i
                    used[i] = True
                    stars += self.get_permutations(
                        index + 1, permutation, used, magic_sum
                    )
                    used[i] = False
        return stars

    def main(self):
        test_cases = int(input())
        for _ in range(test_cases):
            numbers = self.read_input()
            if numbers is None:
                break

            magic_sum = sum(numbers)

            if magic_sum % 3 != 0:
                print(0)
                continue

            magic_sum //= 3
            permutation = [0] * self.SIZE
            used = [False] * self.SIZE
            result = self.get_permutations(0, permutation, used, magic_sum) // 12
            print(result)


if __name__ == "__main__":
    Hexagram().main()
