# 9299 응용
N = int(input())
ans = 0
for _ in range(N):
    C, K = map(int, input().split())
    ans += C*K
print(ans)

