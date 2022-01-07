# 유사 - 12987, 13246 (행렬)
def power(a, x, mod):
    if x == 1:
        return a % mod
    half = power(a, x // 2, mod)
    if x % 2 == 1:
        return (a * half * half) % mod
    return (half * half) % mod


def power_sum(a, r, n, mod):
    # a + ar + ... + ar^n-1
    if n == 1:
        return a % mod
    if n % 2 == 1:
        # a + (ar + ... + ar^n-1)
        return (a + power_sum(a * r, r, n - 1, mod)) % mod
    # a + ar + ... + ar^k-1 + ar^k + ... + ar^2k-1
    # = (a + ar + ... + ar^k-1) + r^k(a + ar + ... + ar^k-1)
    # = (1 + r^k) * (a + ar + ... + ar^k-1)
    return (1 + power(r, n // 2, mod)) * (power_sum(a, r, n // 2, mod)) % mod


a, r, n, mod = map(int, input().split())
print(power_sum(a, r, n, mod))