# 1 2 3 ... n-1 n n-1... 3 2 1 + 나머지 r
# 1+2+...+n+..+2+1 = n^2 (term: 2n-1)
# 0 <= r < n^2
# 0 <= r <= n
#
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    d = y - x
    
