# 2x 또는 10x+1, 단조증가
from collections import deque
A, B = map(int, input().split())
ans = -1
q = deque([(A, 1)])
while q:
    now, count = q.popleft()
    if now == B:
        ans = count
        break
    nxt1, nxt2 = 2*now, 10*now+1
    if nxt1 <= B:
        q.append((nxt1, count+1))
    if nxt2 <= B:
        q.append((nxt2, count+1))
print(ans)
