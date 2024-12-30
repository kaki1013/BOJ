P = int(input())
for _ in range(P):
    T, *arr = map(int, input().split())
    ans = 0
    for i in range(10):
        for j in range(i+2, 12):
            all_bigger = True
            for k in range(i+1, j):
                if arr[k] > arr[i] and arr[k] > arr[j]:
                    continue
                all_bigger = False
            ans += int(all_bigger)
    print(T, ans)