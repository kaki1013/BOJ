# 11401 와 동일
def exponential(a, x, mod):
    if x == 0 or x == 1:
        return a % mod if x else 1
    exp = exponential(a, x // 2, mod)
    if x % 2 == 0:
        return (exp * exp) % mod
    return (exp * exp * a) % mod


N, R = map(int, input().split())
p = 1000000007

n_factorial, nr_factorial, r_factorial = 1, 1, 1
for num in range(1, N + 1):
    n_factorial = (n_factorial * num) % p
    if num <= N - R:
        nr_factorial = (nr_factorial * num) % p
    if num <= R:
        r_factorial = (r_factorial * num) % p

up = n_factorial
down = exponential(nr_factorial * r_factorial, p - 2, p)
print((up * down) % p)
