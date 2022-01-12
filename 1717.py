import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]

def union(a, b):
    p[find(a)] = find(b)

n, m = map(int, input().split())
p = [i for i in range(n+1)]
for _ in range(m):
    q, a, b = map(int, input().split())
    if q == 0:
        union(a, b)
    if q == 1:
        print('YES' if find(a) == find(b) else 'NO')