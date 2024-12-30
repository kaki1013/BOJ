# 11052 응용
N = int(input())
P = list(map(int, input().split()))
# dp[j] := 카드 j개를 사는 최소 금액 (i번 반복 -> 1개부터 i+1개짜리 카드팩)
dp = [10**8] *(N+1)
dp[0] = 0
for i in range(N):
    number = i + 1  # 사용할 카드팩의 카드 개수
    price = P[i]    # 카드팩의 가격
    for j in range(number, N+1):
        dp[j] = min(dp[j], dp[j-number] + price)
print(dp[-1])