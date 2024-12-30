# 참고: https://copy-driven-dev.tistory.com/entry/%EB%B0%B1%EC%A4%80Python10942DP-%ED%8C%B0%EB%A6%B0%EB%93%9C%EB%A1%AC
import sys
N = int(sys.stdin.readline().rstrip())
arr = sys.stdin.readline().rstrip().split()
M = int(sys.stdin.readline().rstrip())
questions = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(M)]

# dp[i][j] := arr[i] 부터 arr[j] 까지가 팰린드롬이면 1, 아니면 0
# dp[i][j] = arr[i] == arr[j] & dp[i+1][j-1]
dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1

"""
dp표를 채우는 순서가 틀림
반례)
12
1 2 1 3 1 2 1 1 1 1 1 1
2
1 7
8 12

for i in range(N-2):
    for j in range(i+2, N):
        if arr[i] == arr[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1
"""
for length in range(2, N):
    for start in range(N - length):
        finish = start + length
        if arr[start] == arr[finish] and dp[start + 1][finish - 1] == 1:
            dp[start][finish] = 1

for question in questions:
    i, j = question
    print(dp[i-1][j-1])
