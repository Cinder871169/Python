MAX_VAL = 100000
prime = [True] * (MAX_VAL + 1)


def sieve():
    prime[0], prime[1] = False, False
    i = 2
    while i * i <= MAX_VAL:
        if prime[i]:
            for j in range(i * i, MAX_VAL + 1, i):
                prime[j] = False
        i += 1


n, x = map(int, input().split())
sieve()
res = [x]
cnt, i = 0, 0
while cnt < n:
    if prime[i]:
        cnt += 1
        res.append(i + res[-1])
    i += 1
print(*res)
