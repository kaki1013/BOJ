def power(x, y, mod):
    if y == 1:
        return x % mod
    if y % 2 == 0:
        return power(x, y // 2, mod) ** 2 % mod
    else:
        return ((power(x, y // 2, mod) ** 2 % mod) * (x % mod)) % mod


A, B, C = map(int, input().split())
print(power(A, B, C))
