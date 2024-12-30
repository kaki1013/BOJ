# 11500, 1492 참고, 1492 보다 k 범위가 큼 : 시간 초과
# 안보고 풀기 - 시간초과 해결 : https://edder773.tistory.com/159
from math import factorial
from math import gcd


def binomial_coefficient(n, k):
    return factorial(n)//(factorial(n-k)*factorial(k))


n, k = map(int, input().split())
k1_factorial = factorial(k+1)
dp = [[0 for _ in range((k+1)+1)] for _ in range(k+1)]  # k이하 == (k+1)미만 : dp[k] 접근하기 위함

# dp[0] initialization
dp[0][1] = k1_factorial  # dp[0] := [(0 + 1*n)*k1_factorial] 의 계수

for degree in range(1, k+1):
    # (1) dp[degree] = (n+1)^(degree+1)
    for term in range((degree+1)+1):
        dp[degree][term] += binomial_coefficient(degree+1, term)
    # (2) dp[degree][0] -= 1; dp[degree][1] -= 1;
    dp[degree][0] -= 1
    dp[degree][1] -= 1
    # (3) 이전 dp는 k1_factorial을 곱해서 관리되고 있으므로, 현재까지 구한 [(n+1)^(degree+1) - 1 - n]에 k1_factorial을 곱함
    for term in range((degree+1)+1):
        dp[degree][term] *= k1_factorial
    # (4) - C(degree+1, 2)*dp[degree-1] - ... - C(degree+1, t)*dp[degree-t+1] - ... - C(degree+1, degree)*dp[1] 를 수행
    for prev_degree in range(1, degree):
        for term in range((prev_degree+1)+1):
            dp[degree][term] -= binomial_coefficient(degree+1, prev_degree) * dp[prev_degree][term]
    # (5) (degree+1) 을 나눔
    for term in range((degree+1)+1):
        dp[degree][term] //= (degree+1)

# get answer
mod = 10 ** 9 + 7
ans = 0
for term in range(k+2):
    up = dp[k][term]
    down = k1_factorial

    GCD = gcd(abs(up), down)
    up //= GCD
    down //= GCD

    ans += pow(n, term, mod) * up * pow(down, -1, mod)
    ans %= mod

print(ans)
