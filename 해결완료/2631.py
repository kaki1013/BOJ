# 11053 참고
# 제대로 된 순서로 서있는 아이들을 제외한 아이들은 재배치가 필요, 즉 제대로 서있는 아이들의 수가 최대여야 함
N = int(input())
A = [int(input()) for _ in range(N)]

dp = [1] * N  # dp[k] := k에서 끝나는 최장 증가 부분 수열의 길이

for now in range(N):
    for previous in range(now):  # 이전까지의 수 중에서
        if A[previous] < A[now]:  # 수열의 값이 더 작고
            dp[now] = max(dp[now], dp[previous] + 1)  # dp + 1(현재 값까지 할 때 수열의 길이가 1 증가) 가 더 크면 업데이트

print(N - max(dp))
