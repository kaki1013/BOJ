# 1715 와 거의 동일
import heapq


T = int(input())
for _ in range(T):
    K = int(input())
    heap = list(map(int, input().split()))
    heapq.heapify(heap)

    ans = 0
    while len(heap) > 1:
        m1 = heapq.heappop(heap)
        m2 = heapq.heappop(heap)
        heapq.heappush(heap, m1+m2)
        ans += m1 + m2

    print(ans)
