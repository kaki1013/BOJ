def fibo(n):
    if n == 0 or n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)


#for i in range(10000):
#    print(f'{i}: {fibo(i)}')

dp = [-1] * 20000
dp[0], dp[1] = 1, 1
i = 2
while True:
    if dp[10001] != -1:
        break
    dp[i] = dp[i-1] + dp[i-2]
    i += 1

print(dp[10001])
