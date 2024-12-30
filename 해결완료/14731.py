def power(a, x, m):
    if x == 0:
        return 1
    half = power(a, x//2, m)
    if x % 2:
        return (a * half * half) % m
    return (half * half) % m


m = 10 ** 9 + 7
ans = 0
N = int(input())
for _ in range(N):
    C, K = map(int, input().split())
    if K == 0:
        continue
    ans = (ans + C * K * power(2, K-1, m)) % m
print(ans)