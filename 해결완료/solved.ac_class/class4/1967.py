# 알림 2020 여름방학 정기스터디 6주차 참고함
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)  # n이 10000까지 + 편향된 트리일 경우 깊이가 최대 10000까지 필요

def DFS(gragh, visited, start, dist):
    if visited[start]:
        return
    visited[start] = True
    for adj, w in gragh[start]:
        if not visited[adj]:
            dist[adj] = dist[start] + w
            DFS(gragh, visited, adj, dist)


n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, weight = map(int, input().split())
    tree[x].append([y, weight])
    tree[y].append([x, weight])

visited = [False] * (n+1)
dist = [0] * (n+1)

# 임의의 노드(여기서는 루트 노드 선택)와 가장 먼 곳에 위치한 노드 찾기
DFS(tree, visited, 1, dist)
Max_where, Max_dist = 1, 0
for i in range(1, n+1):
    if dist[i] > Max_dist:
        Max_where = i
        Max_dist = dist[i]

# 바로 이전에 찾은 노드에 대해서, 가장 먼 곳에 위치한 노드와의 거리(트리의 지름) 찾기
visited = [False] * (n+1)
dist = [0] * (n+1)

DFS(tree, visited, Max_where, dist)
Max_where, Max_dist = 1, 0
for i in range(1, n+1):
    if dist[i] > Max_dist:
        Max_where = i
        Max_dist = dist[i]

print(Max_dist)
