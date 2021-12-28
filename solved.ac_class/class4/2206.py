import sys
from collections import deque


def bfs(start, dist):
    q = deque([[start, dist]])
    visited = {start}
    while q:
        if q[0][0][0] == N-1 and q[0][0][1] == M-1:
            return q[0][1]
        (now_row, now_col, did_wall_pass), d = q.popleft()
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nxt_row, nxt_col = now_row + dr, now_col + dc
            if 0 <= nxt_row < N and 0 <= nxt_col < M and (nxt_row, nxt_col, did_wall_pass) not in visited:
                if did_wall_pass and board[nxt_row][nxt_col] == 0:
                    q.append([(nxt_row, nxt_col, True), d+1])
                    visited.add((nxt_row, nxt_col, True))
                elif not did_wall_pass:
                    q.append([(nxt_row, nxt_col, bool(board[nxt_row][nxt_col])), d+1])
                    visited.add((nxt_row, nxt_col, bool(board[nxt_row][nxt_col])))
    return -1


N, M = map(int, sys.stdin.readline().rstrip().split())  # N행 M열 크기의 맵
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(N)]
print(bfs((0, 0, False), 1))  # (0, 0)에서 (N-1, M-1)까지의 최단거리
