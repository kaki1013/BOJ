# 11444, 2749 참고
def matrix_product(matrix1, matrix2, mod):
    a, b, c, d = matrix1[0][0], matrix1[0][1], matrix1[1][0], matrix1[1][1]
    e, f, g, h = matrix2[0][0], matrix2[0][1], matrix2[1][0], matrix2[1][1]
    return [[((a * e) % mod + (b * g) % mod) % mod, ((a * f) % mod + (b * h) % mod) % mod], [((c * e) % mod + (d * g) % mod) % mod, ((c * f) % mod + (d * h) % mod) % mod]]


def fibo_matrix(N, mod):
    if N == 0:
        return [[0, 0], [0, 0]]
    if N == 1:
        return [[0, 1], [1, 1]]
    if N % 2 == 0:
        matrix = fibo_matrix(N // 2, mod)  # matrix를 구하고 return 해야 함. 그렇지 않으면 중복해서 재귀가 발생하여 시간복잡도 증가
        return matrix_product(matrix, matrix, mod)
    else:
        matrix = fibo_matrix(N // 2, mod)
        return matrix_product(matrix_product(matrix, matrix, mod), [[0, 1], [1, 1]], mod)


n = int(input())
mod = 10000
print(fibo_matrix(n, mod)[0][1])
while True:
    n = int(input())
    if n == -1:
        break
    print(fibo_matrix(n, mod)[0][1])