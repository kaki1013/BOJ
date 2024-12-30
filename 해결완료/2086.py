"""
f(3) - f(2) = f(1)
...
f(n+1) - f(n) = f(n-1)
f(n+2) - f(n+1) = f(n)
=> f(n+2) - f(2) = sum(f(1) ~ f(n))
sum(f(1) ~ f(n)) = f(n+2) - 1
"""
# 11444 참고
def matrix_product(matrix1, matrix2, mod):
    a, b, c, d = matrix1[0][0], matrix1[0][1], matrix1[1][0], matrix1[1][1]
    e, f, g, h = matrix2[0][0], matrix2[0][1], matrix2[1][0], matrix2[1][1]
    return [[((a * e) % mod + (b * g) % mod) % mod, ((a * f) % mod + (b * h) % mod) % mod], [((c * e) % mod + (d * g) % mod) % mod, ((c * f) % mod + (d * h) % mod) % mod]]


def fibo_matrix(N, mod):
    if N == 1:
        return [[0, 1], [1, 1]]
    matrix = fibo_matrix(N // 2, mod)  # matrix를 구하고 return 해야 함. 그렇지 않으면 중복해서 재귀가 발생하여 시간복잡도 증가
    if N % 2 == 0:
        return matrix_product(matrix, matrix, mod)
    return matrix_product(matrix_product(matrix, matrix, mod), [[0, 1], [1, 1]], mod)


a, b = map(int, input().split())
mod = 10**9
# f(a) + ... + f(b) = S(b) - S(a-1) = (f(b+2) - 1) - (f(a+1) - 1) = f(b+2) - f(a+1)
ans = (fibo_matrix(b+2, mod)[0][1] - fibo_matrix(a+1, mod)[0][1]) % mod
print(ans)
