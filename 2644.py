from collections import deque

n = int(input())
dist = [-1] * (n + 1)
visited = [False] * (n + 1)
start, goal = map(int, input().split())

m = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

q = deque([(start, 0)])
dist[start] = 0
while q and dist[goal] == -1:
    now, d = q.popleft()
    visited[now] = True
    dist[start] = d
    for nxt in adj[now]:
        if not visited[nxt]:
            q.append((nxt, d+1))
            visited[nxt] = True
            dist[nxt] = d+1

print(dist[goal])
