n = int(input())
dp = [0, 1]

for _ in range(n):
    dp.append(dp[-1]+dp[-2])

print(dp[n])