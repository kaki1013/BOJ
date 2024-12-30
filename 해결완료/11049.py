N = int(input())
d = [-1]
for i in range(N):
    r, c = map(int, input().split())
    d.pop()
    d.append(r)
    d.append(c)

dp = [[2**31]*N for _ in range(N)]

for i in range(N):
    dp[i][i] = 0

for diag in range(N-1):
    for row in range(N-1-diag):
        col = row + diag + 1

        for border in range(row, col):
            tmp = dp[row][border] + dp[border+1][col] + d[row-1]*d[border]*d[col]

            if dp[row][col] > tmp:
                dp[row][col] = tmp

print(dp[0][-1])
