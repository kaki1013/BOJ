# 11053(dp), 12852(역-인덱스 배열) 참고
N = int(input())
A = list(map(int, input().split()))

dp = [1] * N  # dp[k] := k에서 끝나는 최장 증가 부분 수열의 길이
reverse_idx = list(range(N))  # dp[k] 에 해당하는 부분 수열의 한 단계 전의 부분 수열의 인덱스, 없다면 자기 자신의 인덱스

for now in range(N):
    for previous in range(now):  # 이전까지의 수 중에서
        if A[previous] < A[now]:  # 수열의 값이 더 작고
            if dp[previous] + 1 > dp[now]:  # dp + 1(현재 값까지 할 때 수열의 길이가 1 증가) 가 더 크면
                dp[now] = dp[previous] + 1  # 그 값으로 업데이트하고
                reverse_idx[now] = previous  # 인덱스도 저장

# 최대 길이와 그때에 해당하는 k 값 구하기
max_idx, max_length = 0, 1
for i in range(N):
    if dp[i] > max_length:
        max_length = dp[i]
        max_idx = i
print(max_length)

# 위에서 구한 k를 시작으로 그 이전의 인덱스 역 추적
stack_value = [A[max_idx]]
stack_idx = [max_idx]
while stack_idx[-1] != reverse_idx[stack_idx[-1]]:
    last = stack_idx[-1]
    stack_idx.append(reverse_idx[last])
    stack_value.append(A[reverse_idx[last]])
print(*stack_value[::-1])
