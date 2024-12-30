# sol1: 대각선으로 이동
N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = maze[0][0]

for diag in range(N+M-1):
    for c in range(max(0, diag-N+1), min(M, diag+1)):
        r = diag - c
        for row, col in [(r + 1, c), (r, c + 1), (r + 1, c + 1)]:
            if 0 <= row < N and 0 <= col < M:
                dp[row][col] = max(dp[row][col], dp[r][c] + maze[row][col])

print(dp[-1][-1])
# (3, 4) 일 때의 이동 순서
"""
0
0 0

1
1 0
0 1

2
2 0
1 1
0 2

3
2 1
1 2
0 3

4
2 2
1 3

5
2 3
"""
# sol2: 출처 https://www.acmicpc.net/source/19587372
n, m = map(int, input().split())
pre = [0 for i in range(m)]

for i in range(n):
    new = list(map(int, input().split()))
    for j in range(m):
        # 근거: 사탕이 음수가 아니므로 직각으로 이동하는 것이 더 이득임을 이용
        if pre[j] > new[j - 1] or j == 0:
            new[j] += pre[j]
        else:
            new[j] += new[j - 1]

    pre = new[:]

print(pre[m-1])
