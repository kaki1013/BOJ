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
    if find(u) != find(v):
        union(u, v)
        mst += w
        count += 1
    if count == V - 1:
        break
print(mst)
