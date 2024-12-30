# 11401 + 전처리
import sys


def exponential(a, x, mod):
    if x == 0 or x == 1:
        return a % mod if x else 1
    exp = exponential(a, x // 2, mod)
    if x % 2 == 0:
        return (exp * exp) % mod
    return (exp * exp * a) % mod


p = 1000000007
factorial_arr = [1]
for i in range(1, 4000001):
    factorial_arr.append((factorial_arr[-1] * i) % p)

M = int(sys.stdin.readline().rstrip())
for _ in range(M):
    N, K = map(int, sys.stdin.readline().rstrip().split())
    up = factorial_arr[N]
    down = exponential(factorial_arr[N-K] * factorial_arr[K], p - 2, p)
    print((up * down) % p)
