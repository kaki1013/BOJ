# dp[i] = min(dp[i-1], dp[i+1], dp[i*2]) + 1
# x-1 조건으로 인해 cycle이 생김(무한루프)
from collections import deque

N, K = map(int, input().split())
dp = [-1] * 100001
location = deque([[N, 0]])

while location:
    if dp[K] != -1:
        break
    [curr, count] = location.popleft()
    if dp[curr] == -1:
        dp[curr] = count
        next1, next2, next3 = curr - 1, curr + 1, 2 * curr
        if 0 <= next1 <= 100000:
            location.append([next1, count+1])
        if 0 <= next2 <= 100000:
            location.append([next2, count+1])
        if 0 <= next3 <= 100000:
            location.append([next3, count+1])

print(dp[K])