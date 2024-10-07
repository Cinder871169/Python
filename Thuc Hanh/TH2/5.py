def min_steps_to_equal(arr):
    min_steps = float("inf")
    best_value = -1
    for target in arr:
        steps = sum(abs(a - target) for a in arr)
        if steps < min_steps:
            min_steps = steps
            best_value = target

    return min_steps, best_value


n = int(input())
arr = list(map(int, input().split()))

result_steps, result_value = min_steps_to_equal(arr)
print(result_steps, result_value)
