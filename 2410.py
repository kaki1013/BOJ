# 2293 응용
mod = 10**9
N = int(input())

coins = []
count = 0
while 2**count <= N:
    coins.append(2**count)
    count += 1
n, k = count, N
# dp[i;k] := k원을 만드는 경우의 수(반복문 i번 -> coins 0번부터 i-1번까지 사용) / 0원: 1가지
dp = [int(i % coins[0] == 0) for i in range(k+1)]   # 초기화

for i in range(1, n):                       # 동전 하나씩 사용
    now = coins[i]                          # 현재 사용 중인 금액
    for j in range(now, k+1):               # 금액 하나씩 갱신
        dp[j] = (dp[j] + dp[j-now]) % mod   # 현재 동전을 사용함
print(dp[k] % mod)