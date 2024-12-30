T = int(input())
for _ in range(T):
    N = int(input())
    arr0 = [1, 0] + [-1] * 50
    arr1 = [0, 1] + [-1] * 50
    i = 2
    while True:
        if arr0[N] != -1 or arr1[N] != -1:
            break
        arr0[i] = arr0[i-1] + arr0[i-2]
        arr1[i] = arr1[i-1] + arr1[i-2]
        i += 1
    print(arr0[N], arr1[N])