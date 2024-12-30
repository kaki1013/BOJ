# 유사 - 15712(자연수), 12987 (행렬)
def modular(matrix, n, mod):
    return [[matrix[i][j] % mod for j in range(n)] for i in range(n)]


def matrix_add(mat1, mat2, n, mod):
    return [[(mat1[i][j] + mat2[i][j]) % mod for j in range(n)] for i in range(n)]


def matrix_multi(mat1, mat2, n, mod):
    ans = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ans[i][j] += (mat1[i][k] * mat2[k][j]) % mod
    return ans


def Id_matrix(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def matrix_power(mat, x, n, mod):
    if x == 1:
        return modular(mat, n, mod)
    half = matrix_power(mat, x // 2, n, mod)
    ans = matrix_multi(half, half, n, mod)
    if x % 2 == 0:
        return ans
    return matrix_multi(mat, ans, n, mod)


def matrix_power_sum(a_matrix, r_matrix, x, n, mod):
    # A + AR + ... + AR^x-1
    if x == 1:
        return modular(a_matrix, n, mod)
    if x % 2 == 1:
        # a + (ar + ... + ar^x-1)
        start_matrix = matrix_multi(a_matrix, r_matrix, n, mod)
        ans = matrix_add(a_matrix, matrix_power_sum(start_matrix, r_matrix, x-1, n, mod), n, mod)
    else:
        # a + ar + ... + ar^k-1 + ar^k + ... + ar^2k-1 = (1 + r^k) * (a + ar + ... + ar^k-1)
        first = matrix_add(Id_matrix(n), matrix_power(r_matrix, x // 2, n, mod), n, mod)    # 1 + power(r, n // 2, mod)
        second = matrix_power_sum(a_matrix, r_matrix, x // 2, n, mod)     # power_sum(a, r, n // 2, mod)
        ans = matrix_multi(first, second, n, mod)
    return modular(ans, n, mod)


N, K = map(int, input().split())
M = 1000
A = [list(map(int, input().split())) for _ in range(N)]
ans = matrix_power_sum(A, A, K, N, M)

for line in ans:
    print(*line)