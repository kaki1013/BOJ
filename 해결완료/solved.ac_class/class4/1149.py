"""
# sol1 : 시간 초과
from collections import deque
from sys import stdin
input = stdin.readline

N = int(input())
RGBs = [tuple(map(int, input().split())) for _ in range(N)]

# 지금까지_RGB_수/지금까지의_가격_p/현재_위치_i/현재_색_C
madeRGBs = {(1, 0, 0, RGBs[0][0], 1, 1), (0, 1, 0, RGBs[0][1], 1, 2), (0, 0, 1, RGBs[0][2], 1, 3)}
dp = deque([(1, 0, 0, RGBs[0][0], 1, 1), (0, 1, 0, RGBs[0][1], 1, 2), (0, 0, 1, RGBs[0][2], 1, 3)])
while dp[0][4] != N:
    curr = dp.popleft()
    R, G, B, price, location, color = curr[0], curr[1], curr[2], curr[3], curr[4], curr[5]
    next_location = location + 1
    next_colors = list({1, 2, 3} - {color})
    for next_color in next_colors:
        nextR, nextG, nextB = R, G, B
        if next_color == 1:
            nextR += 1
        elif next_color == 2:
            nextG += 1
        else:
            nextB += 1
        next_price = price + RGBs[next_location - 1][next_color - 1]
        RGBpiC = (nextR, nextG, nextB, next_price, next_location, next_color)
        dp.append(RGBpiC)

ans = 10 ** 6 + 1
for compare in dp:
    if ans > compare[3]:
        ans = compare[3]
print(ans)
"""
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