def mergesort(arr):
    n = len(arr)
    if n == 1:
        return arr
    m = n // 2
    left_arr = arr[:m]
    right_arr = arr[m:]
    return merge(left_arr, right_arr)


def merge(arr1, arr2):
    arr = []
    arr1 = mergesort(arr1)
    arr2 = mergesort(arr2)
    m, n = len(arr1), len(arr2)
    i, j = 0,0
    while True:
        if i == m or j == n:
            break
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    if i != m:
        for p in range(i, m):
            arr.append(arr1[p])
    elif j != n:
        for q in range(j, n):
            arr.append(arr2[q])
    return arr


N = int(input())
arr = []
for _ in range(N):
    data = int(input())
    arr.append(data)

arr = mergesort(arr)

for n in arr:
    print(n)
