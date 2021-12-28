from sys import stdin
input = stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

level = [2 * N] * (N + 1)
level[1] = 1

stack = [1]
while stack:
    now = stack.pop()
    for i in tree[now]:
        if level[i] == 2 * N:
            stack.append(i)
            level[i] = level[now] + 1

for i in range(2, N + 1):
    for adj in tree[i]:
        if level[adj] < level[i]:
            print(adj)