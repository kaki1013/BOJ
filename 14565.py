"""
A + (N - A) = N = 0 mod N
Ax = 1 mod N이면 Ax = Ny + 1
Ax - Ny = 1 인 x를 찾으면 됨
Ax + Ny' = 1(A와 N이 서로소이면 존재)
"""
from math import gcd
N, A = map(int, input().split())
additive_inverse = N - A
multiplicative_inverse = -1
if gcd(A, N) == 1:
    a = A
    r = N % a
print(additive_inverse, multiplicative_inverse)
