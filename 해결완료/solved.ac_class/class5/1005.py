# 2252 응용, dp
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    adj = [[] for _ in range(N)]
    in_degree = [0] * N
    for _ in range(K):
        X, Y = map(int, input().split())
        adj[X-1].append(Y-1)
        in_degree[Y-1] += 1

    q = deque([i for i in range(N) if in_degree[i] == 0])
    result = []
    while q:
        now = q.popleft()
        result.append(now)
        for nxt in adj[now]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                q.append(nxt)

    W = int(input())
    time = [0] * N
    for u in result:
        if time[u] == 0:
            time[u] = D[u]
        for v in adj[u]:
            time[v] = max(time[v], time[u] + D[v])
    print(time[W-1])
