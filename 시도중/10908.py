"""
1, p, 1+p=p^2, p+p^2=p(1+p)=p^3,...
즉, f(n) = phi^n

[f(n)]^k = phi^nk = a_nk * phi + b_nk (by divide and conquer)
f(k) = phi^k = a_k * phi + b_k

A = a_nk // a_k (if a_k | a_nk)
B = b_nk - b_k * A

"""
# 45%
# 모르겠으면 : https://www.acmicpc.net/board/view/70995
# 정답 있음 = 이거 보면 1달 금지 : https://hapby9921.tistory.com/entry/BOJ-10908-Phibonacci
mod = 10 ** 9 + 7


def mat_mult(m1, m2):
    [[a, b], [c, d]] = m1
    [[e, f], [g, h]] = m2
    i, j, k, l = a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h
    return [[i % mod, j % mod], [k % mod, l % mod]]


def mat_exp(m, e):
    if e == 0:
        return [[1, 0], [0, 1]]
    if e == 1:
        return m
    half = mat_exp(m, e // 2)
    full = mat_mult(half, half)
    if e % 2:
        full = mat_mult(full, m)
    return full


def phi(n):
    """
    :param n: integer
    :return: a, b where phi^n = a*phi+b
    """
    """
    [phi(n), phi(n-1)]^t = [[1, 1], [1, 0]] * [phi(n-1), phi(n-2)]^t = ... = [[1, 1], [1, 0]]^(n-1) * [phi(1), phi(0)]^t
    """
    if n == 0:
        return 0, 1
    if n == 1:
        return 1, 0
    [[a, b], [c, d]] = mat_exp([[1, 1], [1, 0]], n - 1)
    return a, b


n, k = map(int, input().split())

a_nk, b_nk = phi(n * k)
a_k, b_k = phi(k)

A = a_nk * pow(a_k, -1, mod)
B = b_nk - b_k * A
print(A % mod, B % mod)
