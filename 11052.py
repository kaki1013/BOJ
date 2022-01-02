N = int(input())
P = list(map(int, input().split()))
# dp[j] := 카드 j개를 사는 최대 금액 (i번 반복 -> 1개부터 i+1개짜리 카드팩)
dp = [0] *(N+1)
for i in range(N):
    number = i + 1  # 사용할 카드팩의 카드 개수
    price = P[i]    # 카드팩의 가격
    for j in range(number, N+1):
        dp[j] = max(dp[j], dp[j-number] + price)
print(dp[-1])