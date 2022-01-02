from collections import deque

M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]      # 1: 방문해야 하는 정점, 0: 방문한 정점

num = 0
for i in range(M):
    for j in range(N):
        if board[i][j]:     # 아직 방문 X
            num += 1
            board[i][j] = 0
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < M and 0 <= yy < N and board[xx][yy]:
                        board[xx][yy] = 0
                        q.append((xx, yy))
print(num)
