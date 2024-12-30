# 0-1 BFS
# https://justicehui.github.io/medium-algorithm/2018/08/30/01BFS/
"""
for all v in verticces:
    dist[v] = inf
dist[start] < - 0
deque
d
d.push_front(start)

while d.empty() == false:
    vertex = get
    front
    element and pop as in BFS
    for all edges e of form(vertex, u):
        if travelling e relaxes distance to u:
            relax
            dist[u]
            if e.weight = 1:
                d.push_back(u)
            else:
                d.push_front(u)
"""
# 1697 수정
# https://velog.io/@aonee/%EB%B0%B1%EC%A4%80-boj-13549-%EC%88%A8%EB%B0%94%EA%BC%AD%EC%A7%883-%ED%8C%8C%EC%9D%B4%EC%8D%AC
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
            location.appendleft([next3, count])

print(dp[K])