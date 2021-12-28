n = int(input())
if n == 1 or n == 2:
    print(n)
else:
    dp = [0, 1, 2]
    for i in range(n-2):
        dp.append((dp[-2] + dp[-1]) % 10007)
    print(dp[-1])