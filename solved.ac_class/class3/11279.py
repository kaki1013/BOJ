# 1927번 수정
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


N = int(sys.stdin.readline().rstrip())
arr = [0]
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0 and len(arr) == 1:
        print(0)
    elif x == 0:
        arr[1], arr[-1] = arr[-1], arr[1]
        data = arr.pop()
        maxHeapify(arr, 1)
        print(data)
    else:
        arr.append(x)
        i = len(arr) - 1  # 마지막 노드의 index
        while i > 1:
            if arr[i] > arr[(i // 2)]:  # 자식 > 부모
                arr[i], arr[(i // 2)] = arr[(i // 2)], arr[i]  # 자식, 부모 교체
                i = i // 2  # 부모 노드에 대해 동일하게 반복
            else:
                break

# 라이브러리/ https://it-garden.tistory.com/293?category=845077
import heapq
import sys

N = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(N)]
h = []
for i in arr:
    if i == 0:
        if h:
            print(-heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h, -i)
