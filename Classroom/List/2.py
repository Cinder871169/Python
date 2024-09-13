def sum_range(nums, l, r):
    sub_list = nums[l : r + 1]
    res = sum(sub_list)
    return res


nums = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
l, r = [int(x) for x in input().split()]
print(sum_range(nums, l, r))
