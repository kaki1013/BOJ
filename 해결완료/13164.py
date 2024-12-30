"""
N K
a1 a2 ... aN  (sort)

diff
a2-a2 ... aN-aN-1
d1 ... dN-1  (sort)

remove
k개의 max(diff)
"""
# 2212 동일
m = map(int, input().split())
N, K = m
arr = sorted(list(map(int, input().split())))

diff = [arr[i+1] - arr[i] for i in range(N-1)]
diff.sort()

print(max(arr)-min(arr) if K == 1 else sum(diff[:-K+1]))
