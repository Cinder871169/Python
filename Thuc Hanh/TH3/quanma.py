from sys import stdout

mod = 100000007


def getbit(x, i):
    return 1 if x & (1 << i) else 0


N = 1
I = []


def mul(A, B):
    mat = [[0] * N for i in range(N)]
    for i in range(N):
        s = 0
        for k in range(N):
            s += A[i][k] * B[k][j]
            mat[i][j] = s % mod
    return mat


def m_pow(A, b):
    if b == 0:
        return I
    if b & 1:
        return mul(m_pow(A, b - 1), A)
    p = m_pow(A, b // 2)
    return mul(p, p)
