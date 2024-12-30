# 힙에서 임의의 원소 제거하기
# https://blog.naver.com/PostView.naver?blogId=jh05013&logNo=221511441485&parentCategoryNo=&categoryNo=117&viewDate=&isShowPopularPosts=true&from=search
import sys


def maxHeapify(arr, i):
    left, right = 2 * i, 2 * i + 1
    largest = i  # 부모, 좌, 우 중에서 가장 큰 노드가 부모가 되도록 교체할 것

    # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 부모의 (키) 값보다 더 큰지를 판단
    if left < len(arr) and arr[largest] < arr[left]:
        # 조건이 만족하는 경우, largest 는 왼쪽 자식의 인덱스를 가집니다.
        largest = left

    # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 [왼쪽과 부모의 (키) 값 중 큰 값]보다 더 큰지를 판단
    if right < len(arr) and arr[largest] < arr[right]:
        # 조건이 만족하는 경우, largest 는 오른쪽 자식의 인덱스를 가집니다.
        largest = right

    if largest != i:
        # 현재 노드 (인덱스 i) 와 최솟값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
        arr[i], arr[largest] = arr[largest], arr[i]
        # 재귀적 호출을 이용하여 최대 힙의 성질을 만족할 때까지 트리를 정리합니다.
        maxHeapify(arr, largest)


def minHeapify(arr, i):
    left, right = 2 * i, 2 * i + 1
    smallest = i  # 부모, 좌, 우 중에서 가장 작은 노드가 부모가 되도록 교체할 것

    # 왼쪽 자식이 존재하는지, 그리고 왼쪽 자식의 (키) 값이 부모의 (키) 값보다 더 작은지를 판단
    if left < len(arr) and arr[smallest] > arr[left]:
        # 조건이 만족하는 경우, smallest 는 왼쪽 자식의 인덱스를 가집니다.
        smallest = left

    # 오른쪽 자식이 존재하는지, 그리고 오른쪽 자식의 (키) 값이 [왼쪽과 부모의 (키) 값 중 작은 값]보다 더 작은지를 판단
    if right < len(arr) and arr[smallest] > arr[right]:
        # 조건이 만족하는 경우, smallest 는 오른쪽 자식의 인덱스를 가집니다.
        smallest = right

    if smallest != i:
        # 현재 노드 (인덱스 i) 와 최솟값 노드 (왼쪽 아니면 오른쪽 자식) 를 교체합니다.
        arr[i], arr[smallest] = arr[smallest], arr[i]
        # 재귀적 호출을 이용하여 최소 힙의 성질을 만족할 때까지 트리를 정리합니다.
        minHeapify(arr, smallest)


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    k = int(sys.stdin.readline().rstrip())
    # 같은 원소를 여러번 제거할 수 있으므로 removes로 set 사용은 불가능
    max_arr, min_arr, max_removes, min_removes = [None], [None], [None], [None]
    for _ in range(k):
        cmd = sys.stdin.readline().rstrip().split()
        cmd, n = cmd[0], int(cmd[1])
        if cmd[0] == 'I':
            max_arr.append(n)
            min_arr.append(n)
            i = len(max_arr) - 1  # 마지막 노드의 index
            while i > 1:
                if max_arr[i] > max_arr[(i // 2)]:  # 자식 > 부모
                    max_arr[i], max_arr[(i // 2)] = max_arr[(i // 2)], max_arr[i]  # 자식, 부모 교체
                    i = i // 2  # 부모 노드에 대해 동일하게 반복
                else:
                    break
            i = len(min_arr) - 1  # 마지막 노드의 index
            while i > 1:
                if min_arr[i] < min_arr[(i // 2)]:  # 자식 < 부모
                    min_arr[i], min_arr[(i // 2)] = min_arr[(i // 2)], min_arr[i]  # 자식, 부모 교체
                    i = i // 2  # 부모 노드에 대해 동일하게 반복
                else:
                    break
        else:  # D
            if n == 1 and len(max_arr) != len(max_removes):
                if max_removes == [None]:
                    max_removes.append(max_arr[1])
                    min_removes.append(max_arr[1])
                else:
                    i = 1
                    max_arr_, max_removes_ = max_arr[:], max_removes[:]
                    while max_arr_[1] == max_removes_[1]:
                        max_arr_[1], max_arr_[-1] = max_arr_[-1], max_arr_[1]
                        max_arr_.pop()
                        maxHeapify(max_arr_, 1)
                        i += 1
                    max_removes.append(max_arr[i])  # 현재 값들(삭제되지 않은 값들) 중 최대값의 index 확인
                    min_removes.append(max_arr[i])

                    i = len(max_removes) - 1  # 마지막 노드의 index
                    while i > 1:
                        if max_removes[i] > max_removes[(i // 2)]:  # 자식 > 부모
                            max_removes[i], max_removes[(i // 2)] = max_removes[(i // 2)], max_removes[i]  # 자식, 부모 교체
                            i = i // 2  # 부모 노드에 대해 동일하게 반복
                        else:
                            break
                    i = len(min_removes) - 1  # 마지막 노드의 index
                    while i > 1:
                        if min_removes[i] < min_removes[(i // 2)]:  # 자식 < 부모
                                min_removes[i], min_removes[(i // 2)] = min_removes[(i // 2)], min_removes[i]  # 자식, 부모 교체
                                i = i // 2  # 부모 노드에 대해 동일하게 반복
                        else:
                            break
            elif n == -1 and len(min_arr) != len(min_removes):
                if min_removes == [None]:
                    max_removes.append(min_arr[1])
                    min_removes.append(min_arr[1])
                else:
                    i = 1
                    min_arr_, min_removes_ = min_arr[:], min_removes[:]
                    while min_arr_[1] == min_removes_[1]:
                        min_arr_[1], min_arr_[-1] = min_arr_[-1], min_arr_[1]
                        min_arr_.pop()
                        minHeapify(min_arr_, 1)
                        i += 1
                    max_removes.append(min_arr[i])
                    min_removes.append(min_arr[i])  # 현재 값들(삭제되지 않은 값들) 중 최소값의 index 확인

                    i = len(max_removes) - 1  # 마지막 노드의 index
                    while i > 1:
                        if max_removes[i] > max_removes[(i // 2)]:  # 자식 > 부모
                            max_removes[i], max_removes[(i // 2)] = max_removes[(i // 2)], max_removes[i]  # 자식, 부모 교체
                            i = i // 2  # 부모 노드에 대해 동일하게 반복
                        else:
                            break
                    i = len(min_removes) - 1  # 마지막 노드의 index
                    while i > 1:
                        if min_removes[i] < min_removes[(i // 2)]:  # 자식 < 부모
                            min_removes[i], min_removes[(i // 2)] = min_removes[(i // 2)], min_removes[i]  # 자식, 부모 교체
                            i = i // 2  # 부모 노드에 대해 동일하게 반복
                        else:
                            break
    if len(max_arr) == len(max_removes):
        print('EMPTY')
    else:
        while max_arr[1] == max_removes[1]:
            max_arr[1], max_arr[-1] = max_arr[-1], max_arr[1]
            max_arr.pop()
            maxHeapify(max_arr, 1)
        while min_arr[1] == min_removes[1]:
            min_arr[1], min_arr[-1] = min_arr[-1], min_arr[1]
            min_arr.pop()
            minHeapify(min_arr, 1)
        print(max_arr[1], min_arr[1])