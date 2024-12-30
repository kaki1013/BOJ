"""
https://kyunstudio.tistory.com/60
페르마의 소정리
p = 1000000007가 소수이고 a = N가 p의 배수가 아니면, a^(p-1)=1(mod p)
이때 a * a^(p-2) = 1 (mod p) 에서 a^(-1) = a ^ (p-2) (mod p)
즉,
nCr mod p = (n! / ((n-r)! * r!)) mod p = (n! mod p) * (((n-r)! * r!)^(p-2) mod p)
"""


def exponential(a, x, mod):
    if x == 0 or x == 1:
        return a % mod if x else 1
    exp = exponential(a, x // 2, mod)
    if x % 2 == 0:
        return (exp * exp) % mod
    return (exp * exp * a) % mod


N, K = map(int, input().split())
p = 1000000007

n_factorial, nk_factorial, k_factorial = 1, 1, 1
for num in range(1, N + 1):
    n_factorial = (n_factorial * num) % p
    if num <= N - K:
        nk_factorial = (nk_factorial * num) % p
    if num <= K:
        k_factorial = (k_factorial * num) % p

up = n_factorial
down = exponential(nk_factorial * k_factorial, p - 2, p)
print((up * down) % p)
