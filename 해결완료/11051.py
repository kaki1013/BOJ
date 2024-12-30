# sol 1: 11401 참고
# a * a^(p-2) = 1 (mod p) 에서 a^(-1) = a ^ (p-2) (mod p)
# nCr mod p = (n! / ((n-r)! * r!)) mod p = (n! mod p) * (((n-r)! * r!)^(p-2) mod p)
def exponential(a, x, mod):
    if x == 0 or x == 1:
        return a % mod if x else 1
    exp = exponential(a, x // 2, mod)
    if x % 2 == 0:
        return (exp * exp) % mod
    return (exp * exp * a) % mod


N, K = map(int, input().split())
p = 10007

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

# sol2: dp
# nCr = n-1Cr + n-1Cr-1, nC0=1, nCn+a = 0(a>0)
N, K = map(int, input().split())
K = min(K, N-K)     # nCr = nCn-r
p = 10007
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1
for n in range(1, N+1):
    for k in range(1, K+1):
        dp[n][k] = (dp[n-1][k] + dp[n-1][k-1]) % p
print(dp[N][K])