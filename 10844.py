N = int(input())
# dp[i][j] := 길이가 i+1이고, 일의 자리가 j인 계단수의 개수
dp = [[0] * 10 for _ in range(N)]
# 초기화
for i in range(1, 10):
    dp[0][i] = 1
# 반복
for i in range(1, N):
    for j in range(10):
        for nxt in [j-1, j+1]:
            if 0 <= nxt < 10:
                dp[i][j] += dp[i-1][nxt]
print(sum(dp[-1]) % 1000000000)