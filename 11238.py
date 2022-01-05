# 11778 동일
def matrix_product(matrix1, matrix2, mod):
    a, b, c, d = matrix1[0][0], matrix1[0][1], matrix1[1][0], matrix1[1][1]
    e, f, g, h = matrix2[0][0], matrix2[0][1], matrix2[1][0], matrix2[1][1]
    return [[((a * e) % mod + (b * g) % mod) % mod, ((a * f) % mod + (b * h) % mod) % mod],
            [((c * e) % mod + (d * g) % mod) % mod, ((c * f) % mod + (d * h) % mod) % mod]]


def fibo_matrix(N, mod):
    if N == 0:
        return [[0, 0], [0, 0]]
    if N == 1:
        return [[0, 1], [1, 1]]
    matrix = fibo_matrix(N // 2, mod)
    if N % 2 == 0:
        return matrix_product(matrix, matrix, mod)
    return matrix_product(matrix_product(matrix, matrix, mod), [[0, 1], [1, 1]], mod)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def solve(n, m, mod):
    return fibo_matrix(gcd(n, m), mod)[0][1]


for _ in range(int(input())):
    n, m = map(int, input().split())
    mod = 10 ** 9 + 7
    print(fibo_matrix(gcd(n, m), mod)[0][1])
