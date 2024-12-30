import heapq
import sys
input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x:
        # 절댓값, 양수인가, 홀수인가 -> 절댓값 작고, 음수이면 우선순위 높게
        # 음수는 -2x-1, 양수는 2x로 처리하면 수 하나로 가능 (https://www.acmicpc.net/source/18980840)
        heapq.heappush(heap, (abs(x), int(x > 0), int(x < 0)))
    else:
        ans = 0
        if len(heap):
            out = heapq.heappop(heap)
            ans = out[0] if out[1] else -out[0]
        print(ans)