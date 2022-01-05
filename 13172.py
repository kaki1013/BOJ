mod = 10**9 + 7
M = int(input())
ans = 0
for _ in range(M):
    N, S = map(int, input().split())
    ans += S * pow(N, -1, mod)
    ans %= mod
print(ans)