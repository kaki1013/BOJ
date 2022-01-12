import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]

def union(a, b):
    a, b = find(a), find(b)
    p[a] = b

N = int(input())
M = int(input())
p = [i for i in range(N)]
edges = []
for _ in range(M):
    a, b, cost = map(int, input().split())
    if a == b:
        continue
    edges.append((cost, a-1, b-1))
edges.sort()

mst, count = 0, 0
for w, u, v in edges:
    if count == N-1:
        break
    u, v = find(u), find(v)
    if u != v:
        union(u, v)
        mst += w
        count += 1
print(mst)