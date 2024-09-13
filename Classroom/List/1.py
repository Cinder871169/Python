def find(nums):
    a = "z"
    b = "z"
    for i in nums:
        if a == "z" and i % 2 == 0:
            a = i
        if b == "z" and i % 2 == 1:
            b = i
        if a != "z" and b != "z":
            break
    return a, b


nums = [1, 3, 5, 7, 4, 1, 6, 8]
even, odd = find(nums)
print(even, odd)
