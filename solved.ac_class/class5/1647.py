# 1197 응용
import sys
input = sys.stdin.readline


def find(u):
    if parents[u] != u:
        parents[u] = find(parents[u])
    return parents[u]


def union(u, v):
    parents[find(u)] = find(v)


V, E = map(int, input().split())
parents = [i for i in range(V)]
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u-1, v-1))
edges.sort()

mst, count = 0, 0
for w, u, v in edges:
    if count == V - 2:  # v == 2 이면 바로 종료 & mst에서 가장 긴 1개 제외
        break
    if find(u) != find(v):
        union(u, v)
        mst += w
        count += 1
print(mst)
