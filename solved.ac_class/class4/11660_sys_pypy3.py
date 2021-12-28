import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
board = [[0] * (N + 1)]
for _ in range(N):
    board.append([0] + list(map(int, sys.stdin.readline().rstrip().split())))
# idea: p~q 구간합 = 0~q 구간합 - 0~p-1 구간합
# index 맞추기 위해 (N+1) * (N+1)로 확대  // "p~q 구간합 = 1~q 구간합 - 1~p-1 구간합" 이면 p=1일 때 등이 문제
for line in range(N+1):
    for i in range(N):
        board[line][i+1] += board[line][i]

for _ in range(M):
    ans = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for line in range(x1, x2 + 1):
        ans += board[line][y2] - board[line][y1-1]
    print(ans)
