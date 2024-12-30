# A + (N - A) = N = 0 mod N
# Ax = 1 mod N이면 Ax = Ny + 1
# Ax - Ny = 1 인 x를 찾으면 됨
# Ax + Ny' = 1(A와 N이 서로소이면 존재)
from math import gcd

def e_gcd(a, b):
    # 초기화
    r1, r2 = a, b
    s1, s2 = 1, 0
    t1, t2 = 0, 1
    while r2 > 0:
        q = r1 // r2
        # r
        r = r1 - q * r2
        r1 = r2
        r2 = r
        # s
        s = s1 - q * s2
        s1 = s2
        s2 = s
        # t
        t = t1 - q * t2
        t1 = t2
        t2 = t
    return r1, s1, t1

N, A = map(int, input().split())
additive_inverse = N - A
multiplicative_inverse = -1
if gcd(A, N) == 1:
    multiplicative_inverse = e_gcd(N, A)[2] % N
print(additive_inverse, multiplicative_inverse)

# sol 2: https://www.acmicpc.net/source/19407239
n, a = map(int, input().split())
try:
    k = pow(a, -1, n)
except:
    k = -1
print(n - a, k)