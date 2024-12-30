from sys import stdin
input = stdin.readline

N = int(input())
RGBs = [tuple(map(int, input().split())) for _ in range(N)]

ans = 10**6 + 1     # 10**3 * 10**3 + 1
# dp[i][j] := 1번부터 i+1번 집까지 칠할 때, 마지막 집이 j의 색일 때의 최소 비용
dp = [[0, 0, 0] for _ in range(N)]

# 1번 집과 N번 집의 색깔이 같을 때는 제외하고 탐색해야 함
# N번 집의 색깔 고정 -> 첫번째 집의 해당 색깔 dp에 INF 대입 -> 최소값 업데이트
for last_color in range(3):
    for init_color in range(3):
        if init_color == last_color:
            dp[0][init_color] = 10**3 + 1
        else:
            dp[0][init_color] = RGBs[0][init_color]
    for i in range(N-1):
        dp[i+1][0] = min(dp[i][1], dp[i][2]) + RGBs[i+1][0]
        dp[i+1][1] = min(dp[i][0], dp[i][2]) + RGBs[i+1][1]
        dp[i+1][2] = min(dp[i][0], dp[i][1]) + RGBs[i+1][2]
    ans = min(ans, dp[-1][last_color])
print(ans)