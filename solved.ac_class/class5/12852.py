# 1463 참고
N = int(input())

dp = [-1] * (N + 3)  # N = 1일 때 dp[3]을 할당하기 위해서
dp[1], dp[2], dp[3] = 0, 1, 1

reverse_idx = [-1] * (N + 3)
reverse_idx[1], reverse_idx[2], reverse_idx[3] = 1, 1, 1

if N > 3:
    for i in range(4, N + 1):
        candidate = [dp[i-1]]
        if i % 2 == 0:
            candidate.append(dp[i // 2])
        if i % 3 == 0:
            candidate.append(dp[i // 3])
        m = min(candidate)

        dp[i] = m + 1

        if m == dp[i-1]:
            reverse_idx[i] = i - 1
        elif i % 2 == 0 and m == dp[i // 2]:
            reverse_idx[i] = i // 2
        elif i % 3 == 0 and m == dp[i // 3]:
            reverse_idx[i] = i // 3

stack = [N]
while stack[-1] != 1:
    last = stack[-1]
    stack.append(reverse_idx[last])

print(dp[N])
print(*stack)
