"""
N K
a1 a2 ... aN  (sort)

diff
a2-a2 ... aN-aN-1
d1 ... dN-1  (sort)

remove
k개의 max(diff)
"""
# 13164 동일
N = int(input())
K = int(input())
arr = sorted(list(map(int, input().split())))

diff = [arr[i+1] - arr[i] for i in range(N-1)]
diff.sort()

if K == 1:
    print(max(arr)-min(arr))
else:
    print(sum(diff[:-K+1]))
