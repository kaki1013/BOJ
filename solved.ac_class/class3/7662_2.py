import sys


def maxHeapify(arr, i):
    left, right = 2 * i, 2 * i + 1
    largest = i
    if left < len(arr) and arr[largest] < arr[left]:
        largest = left
    if right < len(arr) and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, largest)


def minHeapify(arr, i):
    left, right = 2 * i, 2 * i + 1
    smallest = i
    if left < len(arr) and arr[smallest] > arr[left]:
        smallest = left
    if right < len(arr) and arr[smallest] > arr[right]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        minHeapify(arr, smallest)


def maxHeapInsert(arr, x):
    if arr == [None]:
        arr.append(x)
    else:
        arr.append(x)
        i = len(arr) - 1
        while i > 1:
            if arr[i] > arr[(i // 2)]:
                arr[i], arr[(i // 2)] = arr[(i // 2)], arr[i]
                i = i // 2
            else:
                break


def minHeapInsert(arr, x):
    if arr == [None]:
        arr.append(x)
    else:
        arr.append(x)
        i = len(arr) - 1
        while i > 1:
            if arr[i] < arr[(i // 2)]:
                arr[i], arr[(i // 2)] = arr[(i // 2)], arr[i]
                i = i // 2
            else:
                break


def maxHeapRemove(arr):
    arr[1], arr[-1] = arr[-1], arr[1]
    arr.pop()
    maxHeapify(arr, 1)


def minHeapRemove(arr):
    arr[1], arr[-1] = arr[-1], arr[1]
    arr.pop()
    minHeapify(arr, 1)


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    max_arr, min_arr, max_removes, min_removes = [None], [None], [None], [None]
    for _ in range(k):
        cmd = sys.stdin.readline().rstrip().split()
        cmd, n = cmd[0], int(cmd[1])
        if cmd[0] == 'I':
            maxHeapInsert(max_arr, n)
            minHeapInsert(min_arr, n)
        else:  # D
            if n == 1 and len(max_arr) != len(max_removes):
                if max_removes == [None]:
                    max_removes.append(max_arr[1])
                    min_removes.append(max_arr[1])
                else:
                    max_arr_, max_removes_ = max_arr[:], max_removes[:]
                    i = 1
                    while max_removes_ != [None] and max_arr_[1] == max_removes_[1]:
                        maxHeapRemove(max_arr_)
                        maxHeapRemove(max_removes_)
                        i += 1
                    maxHeapInsert(max_removes, max_arr[i])
                    maxHeapInsert(min_removes, max_arr[i])
            elif n == -1 and len(min_arr) != len(min_removes):
                if min_removes == [None]:
                    max_removes.append(min_arr[1])
                    min_removes.append(min_arr[1])
                else:
                    min_arr_, min_removes_ = min_arr[:], min_removes[:]
                    i = 1
                    while min_removes_ != [None] and min_arr_[1] == min_removes_[1]:
                        minHeapRemove(min_arr_)
                        minHeapRemove(min_removes_)
                        i += 1
                    maxHeapInsert(max_removes, min_arr[i])
                    minHeapInsert(min_removes, min_arr[i])
    if len(max_arr) == len(max_removes):
        print('EMPTY')
    else:
        while len(max_arr) > 2 and len(max_removes) > 2 and max_arr[1] == max_removes[1]:
            maxHeapRemove(max_arr)
            maxHeapRemove(max_removes)
        while len(min_arr) > 2 and len(min_removes) > 2 and min_arr[1] == min_removes[1]:
            minHeapRemove(min_arr)
            minHeapRemove(min_removes)
        print(max_arr[1], min_arr[1])
