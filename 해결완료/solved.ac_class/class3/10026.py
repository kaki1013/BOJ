from collections import deque

N = int(input())
grid = [input() for _ in range(N)]
# 적녹색약이 아닌 사람
visited = [[False] * N for _ in range(N)]
diff = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            diff += 1
            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                now = grid[x][y]
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < N and 0 <= yy < N and grid[xx][yy] == now and not visited[xx][yy]:
                        visited[xx][yy] = True
                        q.append((xx, yy))
# 적녹색약인 사람
visited = [[False] * N for _ in range(N)]
same = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            same += 1
            q = deque([(i, j)])
            visited[i][j] = True
            while q:
                x, y = q.popleft()
                now = grid[x][y] in ('R', 'G')  # 1: RG, 0:B
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    xx, yy = x + dx, y + dy
                    if 0 <= xx < N and 0 <= yy < N and (grid[xx][yy] in ('R', 'G')) == now and not visited[xx][yy]:
                        visited[xx][yy] = True
                        q.append((xx, yy))
# 출력
print(diff, same)