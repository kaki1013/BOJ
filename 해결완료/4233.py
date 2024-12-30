# p: prime => a^p == a (mod p)
# reverse is not True.
# 아래의 2가지 check
# 1. 식을 만족하는지 2. p가 소수가 아닌지
def isprime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def power(base, exp, mod):
    if exp == 0 or exp == 1:
        return (base ** exp) % mod
    half_exp = power(base, exp//2, mod)
    if exp % 2 == 0:
        return (half_exp * half_exp) % mod
    return (base * (half_exp * half_exp)) % mod


while True:
    p, a = map(int, input().split())
    if p == a == 0:
        break
    print('yes' if (power(a, p, p) == (a % p)) and (not isprime(p)) else 'no')
