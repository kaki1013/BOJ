# 시간 적게 걸리면 먼저, 오래 걸리면 나중에
N = int(input())
arr = list(map(int, input().split()))
arr.sort()
ans = 0

for i in range(N):
    ans += (N - i) * arr[i]

print(ans)