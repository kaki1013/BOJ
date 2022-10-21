N = int(input())
step = [int(input()) for _ in range(N)]
 
if N == 1:
    ans = step[0]
else:
    dp = [(10001,step[0]), (step[1],step[0]+step[1])]
    # (i-2, 0), (i-2, 1) -> (i, 0) // (i-1,0) -> (i, 1)
    # dp[i][j] := i번째 계단까지 가는 경로에 있는 점수의 합의 최댓값 (단 연속된 계단은 J+1개)
    for i in range(N-2):
        temp = [step[i+2],step[i+2]]
        temp[0] += max(set(dp[-2]) - {10001})
        temp[1] = 10001 if dp[-1][0] == 10001 else temp[1] + dp[-1][0]
        dp.append(tuple(temp))
    ans = max(dp[-1])
print(ans)
