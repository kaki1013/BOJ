# 1149 참고_미해결
from sys import stdin
input = stdin.readline

N = int(input())
RGBs = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0] for _ in range(N)]
dp[0][0], dp[0][1], dp[0][2] = RGBs[0][0], RGBs[0][1], RGBs[0][2]

for i in range(N-1):
    dp[i+1][0] = min(dp[i][1], dp[i][2]) + RGBs[i+1][0]
    dp[i+1][1] = min(dp[i][0], dp[i][2]) + RGBs[i+1][1]
    dp[i+1][2] = min(dp[i][0], dp[i][1]) + RGBs[i+1][2]
print(min(dp[-1]))