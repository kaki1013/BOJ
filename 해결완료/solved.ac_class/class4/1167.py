# 1967 참고함
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # n이 100000까지 + 편향된 트리일 경우 깊이가 최대 100000까지 필요

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
for _ in range(n):
    information = list(map(int, input().split()))
    now = information[0]
    information.pop()
    while len(information) > 1:
        w = information.pop()
        adj = information.pop()
        tree[now].append([adj, w])
        tree[adj].append([now, w])

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
