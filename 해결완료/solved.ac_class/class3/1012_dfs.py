# 11724 응용_연결 요소의 개수
import sys
sys.setrecursionlimit(10000)


def DFS(adj, visited, row, column):
    if visited[row][column]:
        return
    visited[row][column] = True
    for dest in adj[row][column]:
        DFS(adj, visited, dest[0], dest[1])


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().rstrip().split())
        graph[Y][X] = 1
    adj = [[[] for _ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            for dr, dc in [(-1, 0), (0, 1)]:
                if 0 <= r+dr < N and 0 <= c+dc < M and graph[r][c] == 1 and graph[r+dr][c+dc] == 1:
                    adj[r][c].append([r+dr, c+dc])
                    adj[r+dr][c+dc].append([r, c])

    visited = [[False] * M for _ in range(N)]

    ans = 0
    for r in range(N):
        for c in range(M):
            if not visited[r][c] and graph[r][c] == 1:
                DFS(adj, visited, r, c)
                ans += 1

    print(ans)
