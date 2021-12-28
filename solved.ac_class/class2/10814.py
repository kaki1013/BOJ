# sol1: 시간 초과
import sys
N = int(input())
arr = [list(input().split())]
arr[0][0] = int(arr[0][0])
for element_count in range(N-1):
    data = sys.stdin.readline().rstrip().split()
    data[0] = int(data[0])
    i = 0
    while True:
        if i == len(arr):
            break
        if arr[i][0] > data[0]:
            break
        elif arr[i][0] == data[0]:
            i += 1
            continue
        elif arr[i][0] < data[0]:
            i += 1
            continue
    arr = arr[:i] + [data] + arr[i:]

for pair in arr:
    print(pair[0], pair[1])

# sol2: 이진탐색
N = int(input())
if N == 1:
    data = input().split()
    print(data[0], data[1])
else:
    arr = [list(input().split())]
    arr[0][0] = int(arr[0][0])

    data = list(input().split())
    data[0] = int(data[0])
    if data[0] < arr[0][0]:
        arr = [data] + arr
    else:
        arr = arr + [data]

    for element_count in range(2, N):  # m이 처음부터 0이 되는 것 방지
        data = list(input().split())
        data[0] = int(data[0])
        i, j = 0, element_count
        m = (i + j) // 2
        while True:
            if m == 0 or m == element_count:
                break
            elif arr[m][0] < data[0]:
                i = m
                m = (i + j) // 2
            elif arr[m][0] == data[0]:
                m = m + 1
            elif arr[m][0] > data[0]:
                j = m
                m = (i + j) // 2
        arr = arr[:m] + [data] + arr[m:]

    for pair in arr:
        print(pair[0], pair[1])


# sol3: 선입력 후정렬// 3s = 3*10^8번의 연산 & N은 10^5까지 => O(nlogn)짜리 정렬(병합 정렬)
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
        if arr1[i][0] <= arr2[j][0]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1
    if i != m:
        arr = arr + arr1[i:]
    elif j != n:
        arr = arr + arr2[j:]
    return arr


N = int(input())
arr = []
for _ in range(N):
    data = list(input().split())
    data[0] = int(data[0])
    arr.append(data)

arr = mergesort(arr)

for pair in arr:
    print(pair[0], pair[1])
