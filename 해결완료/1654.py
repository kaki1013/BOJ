def solve(x, arr, N):
    tmp = 0
    for a in arr:
        tmp += a//x
    return tmp >= N


def binary_search(K, arr, l, r):
    # ... T T F F ...
    mid = (l+r)//2
    if solve(mid, arr, N) and not solve(mid+1, arr, N):
        return mid

    if solve(mid, arr, N):
        return binary_search(K, arr, mid+1, r)
    return binary_search(K, arr, l, mid-1)


K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
print(binary_search(K, arr, 0, 2**31-1))
