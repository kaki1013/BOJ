import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(node):
    if p[node] != node:
        p[node] = find(p[node])
    return p[node]

def union(u, v):
    p[find(u)] = find(v)

n = int(input())
stars = [tuple(map(float, input().split())) for _ in range(n)]
edges = []
for i in range(n):
    x1, y1 = stars[i]
    for j in range(i+1, n):
        x2, y2 = stars[j]
        dist = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
        edges.append((dist, i, j))
edges.sort()

p = [i for i in range(n)]
mst, count = 0, 0
for w, u, v in edges:
    if count == n-1:
        break
    if find(u) != find(v):
        union(u, v)
        mst += w
        count += 1
print(mst)