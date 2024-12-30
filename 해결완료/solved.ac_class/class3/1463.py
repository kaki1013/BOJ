# sol1
N = int(input())
dp = [-1, 0, 1, 1] + [-1] * N

i = 4
while True:
    if dp[N] != -1:
        break
    dp[i] = min(dp[i-1], int(i % 2 != 0) * 10**6 + int(i % 2 == 0) * dp[i//2], int(i % 3 != 0) * 10**6 + int(i % 3 == 0) * dp[i//3]) + 1
    i += 1

print(dp[N])

#for i in range(N):
#    print(f'{i+1}:{dp[i+1]}')

# sol2: 개선_dp 생성과 가독성 부분
N = int(input())
dp = [-1] * (N + 3)  # N = 1일 때 dp[3]을 할당하기 위해서
dp[1], dp[2], dp[3] = 0, 1, 1

if N > 3:
    for i in range(4, N + 1):
        if dp[N] != -1:
            break
        candidate = [dp[i-1]]
        if i % 2 == 0:
            candidate.append(dp[i // 2])
        if i % 3 == 0:
            candidate.append(dp[i // 3])
        dp[i] = min(candidate) + 1

print(dp[N])