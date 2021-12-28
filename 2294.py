# dp[n][k] := 동전을 0번부터 n-1번까지 사용하여 k원을 만드는 최소 동전 개수
# dp[0][x] = 0 으로 정의
# dp[n][k] := min(dp[n-1][k-coins[n]], dp[n][k-koins[n]]) + 1
# 10**6 초기화 후 -1로 치환
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1, n+1):
    coin = coins[i-1]
    for j in range(k+1):
        if j - coin == 0:
            dp[i][j] = 1
        elif j - coin > 0:
            if dp[i-1][j-coin] != 0 or dp[i][j-coin] != 0:
                dp[i][j] = min({dp[i-1][j-coin], dp[i][j-coin]} - {0}) + 1
        if dp[i-1][j] != 0:
            if dp[i][j] == 0:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j])

print(dp[n][k] if dp[n][k] else -1)
