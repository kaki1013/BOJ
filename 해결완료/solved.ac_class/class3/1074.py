def Z(n, a, b):
    if n == 1:
        return 2 * a + b
    l = 2 ** (n - 1)
    unit_partial_square_end = 4 ** (n-1)
    return unit_partial_square_end * Z(1, a // l, b // l) + Z(n-1, a % l, b % l)


N, r, c = map(int, input().split())  # 1 <= N <= 15 / 0 <= r, c < 2^N
print(Z(N, r, c))
