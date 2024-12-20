def jaccard(a, b):
    if len(a) != len(b):
        return "INVALID"
    set1 = set(a)
    set2 = set(b)

    intersection = set1.intersection(set2)
    union = set1.union(set2)

    res = len(intersection) / len(union) if union else 0
    return f"{res:.5f}"


for t in range(int(input())):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(jaccard(a, b))
