import heapq
import sys
input = sys.stdin.readline

N = int(input())
# 초기화: 처음에 pop 시킬 값들 (최소힙이기 때문에 입력보다 작은 값)
heap = [-10**9+1] * N
# 입력: 메모리 제한 -> 모든 수 저장할 필요 X
# N번째로 큰 값을 찾아야 하기 때문에 N번재 이하는 저장X
for _ in range(N):
    line = list(map(int, input().split()))
    for num in line:
        heapq.heappush(heap, num)
        heapq.heappop(heap)
# 남은 값 N개 중에서 가장 작은 값 = N번째로 큰 값
ans = heapq.heappop(heap)
print(ans)