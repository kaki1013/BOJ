"""
11443 참고
f(1) + f(3) + f(5) +  ... + f(2n-3) + f(2n-1)
= 1 + (f(1)+f(2)) + (f(3)+f(4)) + ... + (f(2n-5)+f(2n-4)) + (f(2n-3)+f((2n-2))
= 1 + S(2n-2)
= 1 + (f(2n) - 1 )  // sum(f(1) ~ f(n)) = f(n+2) - 1  // 2086 참고
= f(2n)
"""
def matrix_product(matrix1, matrix2, mod):
    a, b, c, d = matrix1[0][0], matrix1[0][1], matrix1[1][0], matrix1[1][1]
    e, f, g, h = matrix2[0][0], matrix2[0][1], matrix2[1][0], matrix2[1][1]
    return [[((a * e) % mod + (b * g) % mod) % mod, ((a * f) % mod + (b * h) % mod) % mod], [((c * e) % mod + (d * g) % mod) % mod, ((c * f) % mod + (d * h) % mod) % mod]]


def fibo_matrix(N, mod):
    if N == 1:
        return [[0, 1], [1, 1]]
    matrix = fibo_matrix(N // 2, mod)
    if N % 2 == 0:
        return matrix_product(matrix, matrix, mod)
    return matrix_product(matrix_product(matrix, matrix, mod), [[0, 1], [1, 1]], mod)


n = int(input())
mod = 10**9 + 7
if n % 2 == 1:
    n += 1
print(fibo_matrix(n, mod)[0][1])