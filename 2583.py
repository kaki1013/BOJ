from collections import deque

M, N, K = map(int, input().split())
rect = [list(map(int, input().split())) for _ in range(K)]
board = [[0]*M for _ in range(N)]
for x1, y1, x2, y2 in rect:
    for x in range(x1, x2):     # 꼭짓점으로 주어짐
        for y in range(y1, y2):
            board[x][y] = 1

num = 0
count = []
for i in range(N):
    for j in range(M):
        if not board[i][j]:     # 아직 방문 X
            num += 1
            board[i][j] = 1
            temp = 1
            q = deque([(i, j)])
            while q:
                x, y = q.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < N and 0 <= yy < M and not board[xx][yy]:
                        board[xx][yy] = 1
                        temp += 1
                        q.append((xx, yy))
            count.append(temp)
print(num)
print(*sorted(count))
