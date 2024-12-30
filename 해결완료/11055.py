N = int(input())
A = list(map(int, input().split()))
# dp[i] := A[i] 로 끝나는 가장 큰 증가 부분 수열의 합
# dp[i] := A[i] 이전까지의 가장 큰 증가 부분 수열의 합으로 정의해도 가능??
# 초기값: A[i] 자기 자신만을 부분 수열로 가지는 경우
dp = A[:]

for i in range(N):  # dp[i] 결정
    for j in range(i):  # i < j 인 경우들에 대하여
        if A[j] < A[i] and dp[j] + A[i] > dp[i]:  # 수열이 증가하고, 기존보다 증가 부분 수열의 합이 더 커지는 경우
            dp[i] = dp[j] + A[i]  # dp[i] 를 갱신

print(max(dp))
