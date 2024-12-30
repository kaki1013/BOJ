# 2252 응용, 불가능한 경우 판별 - > 정렬이 가능한 것과 결과가 N개인 것은 필요충분조건
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N)]
in_degree = [0] * N
for _ in range(M):
    n, *l = map(int, input().split())
    for i in range(n-1):
        A, B = l[i], l[i+1]
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

if len(result) == N:
    for i in result:
        print(i)
else:
    print(0)
