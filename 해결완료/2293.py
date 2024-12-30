# a1x1 + a2x2 + ... + anxn = k 의 해의 수를 구하는 문제 유형
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp[i;k] := k원을 만드는 경우의 수(반복문 i번 -> coins 0번부터 i-1번까지 사용) / 0원: 1가지
dp = [int(i % coins[0] == 0) for i in range(k+1)]   # 초기화

for i in range(1, n):           # 동전 하나씩 사용
    for j in range(1, k+1):     # 금액 하나씩 갱신
        now = coins[i]          # 현재 사용 중인 금액
        if j >= now:            # 현재 동전이 사용할 수 있다면
            dp[j] += dp[j-now]  # 현재 동전을 사용함
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