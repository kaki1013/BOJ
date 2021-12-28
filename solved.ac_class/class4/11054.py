# 11053 참고
N = int(input())
A = list(map(int, input().split()))

dp_inc = [1] * N  # dp[k] := k에서 끝나는 최장 증가 부분 수열의 길이
dp_dec = [1] * N  # dp[k] := k에서 시작하는 최장 감소 부분 수열의 길이

for now in range(N):
    for previous in range(now):  # 이전까지의 수 중에서
        if A[previous] < A[now]:  # 수열의 값이 더 작고
            dp_inc[now] = max(dp_inc[now], dp_inc[previous] + 1)  # dp + 1(현재 값까지 할 때 수열의 길이가 1 증가) 가 더 크면 업데이트
for now in range(N-1, -1, -1):
    for later in range(N-1, now, -1):
        if A[later] < A[now]:  # 수열의 값이 더 크고
            dp_dec[now] = max(dp_dec[now], dp_dec[later] + 1)  # dp + 1(현재 값까지 할 때 수열의 길이가 1 증가) 가 더 크면 업데이트

ans = 1
for i in range(N):
    ans = max(ans, dp_inc[i]+dp_dec[i]-1)
print(ans)
