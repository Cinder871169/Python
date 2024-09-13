def sum_range(nums, l, r):
    sub_list = nums[l : r + 1]
    res = sum(sub_list)
    return res


nums = [int(x) for x in input().split()]
l, r = [int(x) for x in input().split()]
print(sum_range(nums, l, r))
