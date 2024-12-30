import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    if n in (1, 2, 3):
        print(n)
        continue
    dp = [1] * (n+1)    # dp[i] := i를 만드는 방법의 수
    for num in range(2, 3+1):
        for i in range(num, n+1):
            dp[i] += dp[i-num]
    print(dp[-1])