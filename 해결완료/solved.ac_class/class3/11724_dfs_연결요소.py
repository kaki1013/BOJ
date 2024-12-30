# PyPy3로 해야 시간초과 X
import sys
sys.setrecursionlimit(10**4)


def DFS(graph, visited, start):
    if visited[start]:
        return
    visited[start] = True
    for dest in graph[start]:
        DFS(graph, visited, dest)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False for _ in range(N + 1)]

ans = 0
for i in range(1, N+1):
    if not visited[i]:
        DFS(graph, visited, i)
        ans += 1
# https://velog.io/@devjuun_s/%EC%97%B0%EA%B2%B0-%EC%9A%94%EC%86%8C%EC%9D%98-%EA%B0%9C%EC%88%98-%EB%B0%B1%EC%A4%80-11724%EB%B2%88python
'''
while True:
    if visited[1:] == [True for _ in range(N)]:
        break
    DFS(graph, visited, s)
    for i in range(1, N+1):
        if not visited[i]:
            s = i
    ans += 1
'''

print(ans)
