# sol1: 메모리 초과
"""
from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    dp = deque([[arr[0][0], 0, 1], [arr[1][0], 1, 1], [0, -1, 1]])
    while dp[0][2] != n:
        max_sum, last, curr = dp.popleft()
        if last == -1:
            dp.append([max_sum + arr[0][curr], 0, curr + 1])
            dp.append([max_sum + arr[1][curr], 1, curr + 1])
            dp.append([max_sum, -1, curr + 1])
        else:
            dp.append([max_sum + arr[1-last][curr], 1-last, curr + 1])
            dp.append([max_sum, -1, curr + 1])
    # dp 길이가 최소 2^100,000이 되어 메모리 초과
    ans = 0
    for info in dp:
        if info[0] > ans:
            ans = info[0]
    print(ans)
"""
# sol2
T = int(input())
for _ in range(T):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
    else:
        dp = [[0]*n for _ in range(2)]
        dp[0][0], dp[1][0], dp[0][1], dp[1][1] = arr[0][0], arr[1][0], arr[1][0] + arr[0][1], arr[0][0] + arr[1][1]
        i = 2
        while i < n:
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]
            i += 1
        print(max(dp[0][-1], dp[1][-1]))
