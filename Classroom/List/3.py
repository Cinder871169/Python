def reverse(strings):
    rev = []
    for s in strings:
        rev.append(s[::-1])
    return rev


strings = [s.strip() for s in input().split()]
print(reverse(strings))
