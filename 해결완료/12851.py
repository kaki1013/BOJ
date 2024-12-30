from collections import deque
size = 100001

N, K = map(int, input().split())
smallest = [-1] * size   # i에 도착하기 위한 최소 시간
way = [-1] * size        # i에 최소 시간으로 도착하는 방법의 수

# 초기화
smallest[N] = 0
way[N] = 1

# bfs
q = deque([N])
depth = 0
while smallest[K] == -1:
    depth += 1
    count = dict()  # 해당 depth에서 i에 도착하는 방법의 수 (최소 시간일 때만 기록)
    while q:
        now = q.popleft()
        nexts = [now-1, now+1, 2*now]
        for nxt in nexts:
            if 0 <= nxt < size:
                if smallest[nxt] == -1:  # 지금이 최소 시간
                    if nxt in count:
                        count[nxt] += way[now]
                    else:
                        count[nxt] = way[now]
    # 현재 depth에서 count에 저장한 최소시간과 방법의 수를, 전체에 대해(smallest, way) 저장
    temp = []
    for k in count.keys():
        temp.append(k)
        smallest[k] = depth
        way[k] = count[k]
    q = deque(temp)

print(smallest[K])
print(way[K])