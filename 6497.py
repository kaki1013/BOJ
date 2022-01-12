# 1197 응용
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(u):
    if parents[u] != u:
        parents[u] = find(parents[u])
    return parents[u]


def union(u, v):
    parents[find(u)] = find(v)


while True:
    V, E = map(int, input().split())
    if V == 0:
        break
    parents = [i for i in range(V)]
    edges = []
    total = 0
    for _ in range(E):
        u, v, w = map(int, input().split())
        edges.append((w, u, v))
        total += w
    edges.sort()

    mst, count = 0, 0
    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst += w
            count += 1
        if count == V - 1:
            break
    print(total - mst)