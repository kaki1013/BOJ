N, M = map(int, input().split())
board = [[0] * (M + 1)]
for _ in range(N):
    board.append([0] + list(map(int, input().split())))
# idea: p~q 구간합 = 0~q 구간합 - 0~p-1 구간합
# index 맞추기 위해 (N+1)행 * (M+1)열 로 확대  // "p~q 구간합 = 1~q 구간합 - 1~p-1 구간합" 이면 p=1일 때 등이 문제
for line in range(N+1):
    for i in range(M):
        board[line][i+1] += board[line][i]

K = int(input())
for _ in range(K):
    ans = 0
    i, j, x, y = map(int, input().split())
    for line in range(i, x + 1):
        ans += board[line][y] - board[line][j-1]
    print(ans)
