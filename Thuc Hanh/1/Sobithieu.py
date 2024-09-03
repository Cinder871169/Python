n = int(input())
sum = n * (n + 1) // 2
sum_input = 0
for i in range(n - 1):
    num = int(input())
    sum_input += num
print(sum - sum_input)
