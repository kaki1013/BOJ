import sys
input = sys.stdin.readline

def prime_list(n):
    sieve = [True] * (n+1)

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i + i, n+1, i):
                sieve[j] = False

    return [i for i in range(2, n+1) if sieve[i]]

def coprime(n):
    ans = n

    p = []
    for pp in prime:
        if n % pp == 0:
            p.append(pp)
            while n % pp == 0:
                n //= pp
    if n != 1:
        p.append(n)

    for pp in p:
        ans = ans // pp * (pp-1)
    return ans

prime = prime_list(10000)
coprime_count = []
for i in range(1, 10001):
    coprime_count.append(coprime(i))
sum_coprime = [1]
for i in range(10000):
    sum_coprime.append(sum_coprime[-1]+coprime_count[i])

P = int(input())
for _ in range(P):
    K, n = map(int, input().split())
    print(K, sum_coprime[n])
