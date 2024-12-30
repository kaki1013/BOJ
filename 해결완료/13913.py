# 1697 응용
from collections import deque

N, K = map(int, input().split())
dp = [-1] * 100001
from_where = [-1] * 100001
from_where[N] = N
location = deque([(N, N, 0)])

while location:
    if dp[K] != -1:
        break
    pre, curr, count = location.popleft()
    if dp[curr] == -1:
        dp[curr] = count
        from_where[curr] = pre
        for nxt in [curr - 1, curr + 1, 2 * curr]:
            if 0 <= nxt <= 100000:
                location.append((curr, nxt, count+1))
print(dp[K])
way = deque([K])
while way[0] != N:
    way.appendleft(from_where[way[0]])
print(*way)