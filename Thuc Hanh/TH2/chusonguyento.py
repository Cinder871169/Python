from itertools import product


def gen(n):
    nums = ["2", "3", "5", "7"]
    res = []
    for l in range(4, n + 1):
        for i in product(nums, repeat=l):
            num_str = "".join(i)
            if (
                "2" in num_str
                and "3" in num_str
                and "5" in num_str
                and "7" in num_str
                and num_str[-1] in "357"
            ):
                res.append(num_str)
    return res


n = int(input())
ans = gen(n)
for i in ans:
    print(i)
