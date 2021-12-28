import heapq
import sys

N = int(sys.stdin.readline().rstrip())
min_heap, max_heap = [], []
heapq.heapify(min_heap)
heapq.heapify(max_heap)

m = int(sys.stdin.readline().rstrip())
print(m)
for have in range(1, N):
    compare = int(sys.stdin.readline().rstrip())
    if compare > m:
        if len(min_heap) == 0:
            heapq.heappush(min_heap, compare)
        elif compare <= min_heap[0]:
            if have % 2 == 0:
                heapq.heappush(max_heap, -m)
                m = compare
            else:
                heapq.heappush(min_heap, compare)
        else:
            if have % 2 == 0:
                heapq.heappush(max_heap, -m)
                m = heapq.heappop(min_heap)
                heapq.heappush(min_heap, compare)
            else:
                heapq.heappush(min_heap, compare)
    else:
        if len(max_heap) == 0:
            if have == 1:
                heapq.heappush(min_heap, m)
                m = compare
            elif have == 2:
                heapq.heappush(max_heap, -compare)
        elif compare >= -max_heap[0]:
            if have % 2 == 0:
                heapq.heappush(max_heap, -compare)
            else:
                heapq.heappush(min_heap, m)
                m = compare
        else:
            if have % 2 == 0:
                heapq.heappush(max_heap, -compare)
            else:
                heapq.heappush(min_heap, m)
                m = -heapq.heappop(max_heap)
                heapq.heappush(max_heap, -compare)
    print(m)

"""
# https://www.acmicpc.net/source/19323389
import sys
import heapq

n = int(sys.stdin.readline())
min_heap = []
max_heap = []

for _ in range(n):
    new_num = int(sys.stdin.readline())

    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, new_num*-1)
    else:
        heapq.heappush(min_heap, new_num)

    if min_heap and max_heap[0]*-1 > min_heap[0]:
        heapq.heappush(max_heap, heapq.heapreplace(min_heap, heapq.heappop(max_heap)*-1)*-1)

    print(max_heap[0]*-1)
"""