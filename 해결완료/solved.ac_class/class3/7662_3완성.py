# 참고: https://velog.io/@kyy00n/%EB%B0%B1%EC%A4%80-7662%EB%B2%88-%EC%9D%B4%EC%A4%91-%EC%9A%B0%EC%84%A0%EC%88%9C%EC%9C%84-%ED%81%90
import sys


def maxHeapify(arr, i, length):
    left, right = 2 * i + 1, 2 * i + 2
    largest = i
    if left < length and arr[largest] < arr[left]:
        largest = left
    if right < length and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest, length)


def minHeapify(arr, i, length):
    left, right = 2 * i + 1, 2 * i + 2
    smallest = i
    if left < length and arr[smallest] > arr[left]:
        smallest = left
    if right < length and arr[smallest] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(arr, smallest, length)


def maxHeapInsert(arr, x, length):
    arr.append(x)
    length += 1
    i = length - 1
    while i > 0:
        if arr[i][0] > arr[(i - 1) // 2][0]:
            arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
            i = (i - 1) // 2
        else:
            break
    return length


def minHeapInsert(arr, x, length):
    arr.append(x)
    length += 1
    i = length - 1
    while i > 0:
        if arr[i][0] < arr[(i - 1) // 2][0]:
            arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
            i = (i - 1) // 2
        else:
            break
    return length


def maxHeapRemove(arr, length):
    arr[0], arr[-1] = arr[-1], arr[0]
    arr.pop()
    length -= 1
    maxHeapify(arr, 0, length)
    return length


def minHeapRemove(arr, length):
    arr[0], arr[-1] = arr[-1], arr[0]
    arr.pop()
    length -= 1
    minHeapify(arr, 0, length)
    return length


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    max_arr, min_arr = [], []
    max_length, min_length = 0, 0
    popped = [False] * k
    for k_st in range(k):
        cmd = sys.stdin.readline().rstrip().split()
        cmd, n = cmd[0], int(cmd[1])
        if cmd[0] == 'I':
            max_length = maxHeapInsert(max_arr, (n, k_st), max_length)
            min_length = minHeapInsert(min_arr, (n, k_st), min_length)
        else:  # D
            if n == 1:
                while max_arr and popped[max_arr[0][1]]:
                    max_length = maxHeapRemove(max_arr, max_length)
                if max_arr:
                    popped[max_arr[0][1]] = True
                    max_length = maxHeapRemove(max_arr, max_length)
            elif n == -1:
                while min_arr and popped[min_arr[0][1]]:
                    min_length = minHeapRemove(min_arr, min_length)
                if min_arr:
                    popped[min_arr[0][1]] = True
                    min_length = minHeapRemove(min_arr, min_length)
    while min_arr and popped[min_arr[0][1]]:
        min_length = minHeapRemove(min_arr, min_length)
    while max_arr and popped[max_arr[0][1]]:
        max_length = maxHeapRemove(max_arr, max_length)

    if not min_arr:
        print('EMPTY')
    else:
        print(max_arr[0][0], min_arr[0][0])
