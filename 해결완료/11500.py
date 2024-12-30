from math import factorial as ftr
from math import gcd


def binomial_coefficient(n, k):
    return ftr(n)//(ftr(n-k)*ftr(k))


n = 25 + 1  # 25이하 == 26미만
nftr = ftr(n)  # 26!
dp = [[0 for _ in range(n+1)] for _ in range(n)]
dp[0][1], dp[1][1], dp[1][2] = nftr, nftr//2, nftr//2

for i in range(2, n):
    for j in range((i+1)+1):
        dp[i][j] += binomial_coefficient(i+1, j)
    dp[i][0] -= 1
    dp[i][1] -= 1
    for j in range((i+1)+1):
        dp[i][j] *= nftr
    for order in range(1, i):
        for term in range((order+1)+1):
            dp[i][term] -= binomial_coefficient(i+1, order) * dp[order][term]  # dp[order][term]은 nftr이 곱해진 상태
    for j in range((i+1)+1):
        dp[i][j] //= (i+1)

T = int(input())
for _ in range(T):
    t, *coefficients = map(int, input().split())

    S = [0 for _ in range(t+2)]
    S[0] = coefficients[0] * nftr
    for i in range(t+1):
        sum_of_i_th_power = dp[i]
        for term in range(i+2):
            S[term] += coefficients[i] * dp[i][term]

    ans = 0
    for i in range(t+2):
        ans += abs(S[i]//gcd(abs(S[i]), nftr))
    print(ans)
