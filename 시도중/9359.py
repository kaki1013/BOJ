primes = []
is_prime = [True] * 10**5
for i in range(2, 10**5):
    if is_prime[i]:
        primes.append(i)
        for j in range(2*i, 10**5, i):
            is_prime[j] = False


def get_prime_factor(n):
    if n == 1:
        return []

    factor = []
    for p in primes:
        if n % p == 0:
            factor.append(p)
            while n % p == 0:
                n //= p
    if n != 1:
        factor.append(n)
    return factor


T = int(input())
for t in range(T):
    A, B, N = map(int, input().split())
    prime_factors = get_prime_factor(N)
    print(prime_factors)

    a, b = A-1, B
    for p in prime_factors:
        a = a - a // p
        b = b - b // p
        print(p, a, b)
    print(a, b)
    print(f"Case #{t+1}: {b-a}")

# 반례
# 100000007 100000009 200000014 (1)
# 3 9 12 (2)
#