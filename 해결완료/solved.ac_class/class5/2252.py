from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
in_degree = [0] * N
for _ in range(M):
    A, B = map(int, input().split())
    adj[A-1].append(B-1)
    in_degree[B-1] += 1

q = deque([i for i in range(N) if in_degree[i] == 0])
result = []
while q:
    now = q.popleft()
    result.append(now+1)
    for nxt in adj[now]:
        in_degree[nxt] -= 1
        if in_degree[nxt] == 0:
            q.append(nxt)
print(*result)