T = int(input())
for test in range(1, T+1):
    n, *arr = map(int, input().split())
    ans = []
    for i in range(n, 0, -1):
        ans.append(arr[n-i]*i)
    print(f"Case {test}: {n-1}", end=' ')
    print(*ans)
