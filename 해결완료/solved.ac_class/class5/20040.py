import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)


def find(a):
    if p[a] != a:
        p[a] = find(p[a])
    return p[a]


def union(a, b):
    p[b] = a    # already find(x)


n, m = map(int, input().split())
p = [i for i in range(n)]
found = False
ans = 0
for i in range(m):
    a, b = map(int, input().split())
    if found:
        continue
    a, b = find(a), find(b)
    if a == b:
        ans = i+1
        found = True
    else:
        union(a, b)
print(ans)