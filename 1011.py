# d = y - x 애 대해 아래를 만족하는 최대 자연수 n을 잡을 수 있음
# d = 1 + 2 + 3 + ... + n-1 + n + n-1 + ... + 3 + 2 + 1 + r
# 1+2+...+n+..+2+1 = n^2 (항은 2n-1개) 이므로 0 <= r < 2n+1 (r=2n+1이면 n+1 선택하면 됨)
# r == 0일 때: 그대로, 1<=r<=n일 때: r만큼 한번 더 이동, n+1<=r<=2n: n만큼, r-n만큼 두번 더 이동
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y - x
    n = int(d ** 0.5)
    ans, r = 2 * n - 1, d - n ** 2
    if 1 <= r <= n:
        ans += 1
    elif n + 1 <= r <= 2 * n:
        ans += 2
    print(ans)

# short
for _ in range(int(input())):x,y=map(int,input().split());n=int((y-x)**0.5);print(2*n+(y-x-n*n-1)//n)