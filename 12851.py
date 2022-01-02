from collections import deque
size = 100001

N, K = map(int, input().split())
smallest = [-1] * size   # i에 도착하기 위한 최소 시간
way = [-1] * size        # i에 최소 시간으로 도착하는 방법의 수
smallest[N] = 0
way[N] = 1

q = deque([N])
while q:
    print(q)
    now = q.popleft()
    nexts = [now-1, now+1, 2*now]
    for nxt in nexts:
        if 0 <= nxt <= size:
            if smallest[nxt] == -1:  # 첫 도착
                smallest[nxt] = smallest[now] + 1
                way[nxt] = 1
                q.append(nxt)
            else:  # 이전에 도착한 적 있음
                if smallest[now] + 1 == smallest[nxt]:  # 최소 횟수로 온 경우
                    way[nxt] += 1
                    q.append(nxt)
print(smallest[K])
print(way[K])

