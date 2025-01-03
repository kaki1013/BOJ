def matrix_product(matrix1, matrix2, mod, n):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] = (ans[i][j] + matrix1[i][k] * matrix2[k][j]) % mod
    return ans


def matrix_power(matrix, b, mod, n):
    if b == 1:
        return matrix
    m = matrix_power(matrix, b // 2, mod, n)
    if b % 2 == 0:
        return matrix_product(m, m, mod, n)
    else:
        return matrix_product(matrix_product(m, m, mod, n), matrix, mod, n)


N, B = map(int, input().split())
mod = 1000
mtrx = [list(map(int, input().split())) for _ in range(N)]

ans = matrix_power(mtrx, B, mod, N)

for i in range(N):
    for j in range(N):
        ans[i][j] %= mod

for row in matrix_power(mtrx, B, mod, N):
    print(*row)
