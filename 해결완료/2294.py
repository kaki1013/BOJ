n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

# dp[i;k] := i원을 만드는 데 필요한 동전의 최소 개수(반복문 j번 -> coins 0번부터 j-1번까지 사용) / 0원: 0개
dp = [10**5 for i in range(k+1)]    # 초기화
dp[0] = 0
for i in range(n):                              # 동전 하나씩 사용
    for j in range(1, k+1):                     # 금액 하나씩 갱신
        now = coins[i]                          # 현재 사용 중인 금액
        if j >= now:                            # 현재 동전이 사용할 수 있다면
            dp[j] = min(dp[j], dp[j-now] + 1)   # 현재 동전을 사용함
print(-1 if dp[k] == 10**5 else dp[k])