def reverse(strings):
    rev = []
    for s in strings:
        rev.append(s[::-1])
    return rev


strings = ["Red", "Green", "Blue", "White", "Black"]
print(reverse(strings))
