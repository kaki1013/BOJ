n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)])

dp = [0]*(k+1)  # dp[i;k] := k원을 만드는 경우의 수(반복문 i번 -> coins 0번부터 i-1번까지 사용) / 0원: 1가지

for i in range(k+1):
    first = coins[0]
    if i % first == 0:
        dp[i] = 1

for i in range(1, n):
    for j in range(1, k+1):
        now = coins[i]
        if j >= now:
            dp[j] += dp[j-now]
print(dp[k])

"""
1st try: 메모리 초과
dp = [[0]*(k+1) for i in range(n)]  # dp[i;n][j;k] := coins 0번부터 i번까지 사용하여 k원을 만드는 경우의 수 / 0원: 1가지

for j in range(k+1):
    first = coins[0]
    if j % first == 0:
        dp[0][j] = 1

for i in range(n):
    dp[i][0] = 1

for i in range(1, n):
    for j in range(1, k+1):
        dp[i][j] = dp[i-1][j]
        now = coins[i]
        if j >= now:
            dp[i][j] += dp[i][j-now]
print(dp[n-1][k])
"""