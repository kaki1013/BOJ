# 메모리 초과 : https://kimmessi.tistory.com/215
import heapq

K, N = map(int, input().split())
P = list(map(int, input().split()))

heap = P[:]
heapq.heapify(heap)
length = K

s = set(P)
max_ = max(P)
while N:
    min_ = heapq.heappop(heap)
    N -= 1
    length -= 1
    for p in P:
        tmp = min_ * p
        if (tmp not in s) and (length < N or (length >= N and tmp < max_)):
            s.add(tmp)
            heapq.heappush(heap, tmp)
            length += 1
            max_ = max(max_, tmp)
print(min_)

"""
4 2514
2 3 5 541
"""