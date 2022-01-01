from collections import deque

T = int(input())
for _ in range(T):
    n = int(input())
    wants = list(map(int, input().split()))
    wants = [i-1 for i in wants]

    queue_insert = [False] * n
    chosen = [False] * n

    q = deque([0])

    for _ in range(n):
        now = q.popleft()
        while not now in q:
            pass
