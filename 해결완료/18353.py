# 11722 참고
N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for now in range(N):
    for previous in range(now):
        if A[previous] > A[now]:
            dp[now] = max(dp[now], dp[previous] + 1)

print(N - max(dp))
