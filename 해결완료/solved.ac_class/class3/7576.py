# 처음 짠 코드
'''from collections import deque
import sys


def bfs(adj, vst, start_points):
    q = deque([[[row, column], 0] for row, column in start_points])
    for row, column in start_points:
        vst[row][column] = True

    while q:
        curr, dist = q.popleft()
        for nxt in adj[curr[0]][curr[1]]:
            if not vst[nxt[0]][nxt[1]]:
                q.append([nxt, dist + 1])
                vst[nxt[0]][nxt[1]] = True
    return dist


M, N = map(int, sys.stdin.readline().rstrip().split())  # 가로, 세로/ Column, Row
Tomato = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

start_points = []
for row in range(N):
    for column in range(M):
        if Tomato[row][column] == 1:
            start_points.append([row, column])

adj = [[[] for _ in range(M)] for _ in range(N)]
for row in range(N):
    for column in range(M):
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= row + dr < N and 0 <= column + dc < M and Tomato[row + dr][column + dc] != -1:
                adj[row][column].append([row + dr, column + dc])

visited = [[False for _ in range(M)] for _ in range(N)]
for row in range(N):
    for column in range(M):
        if Tomato[row][column] == -1:
            visited[row][column] = True

max_step = bfs(adj, visited, start_points)

all_visited = True
for row in range(N):
    if not all_visited:  # No_breaker = all_visited
        break
    for column in range(M):
        if not visited[row][column]:
            all_visited = False
            break

if all_visited:
    print(max_step)
else:
    print(-1)'''

# 중복되는 반복문 정리
"""from collections import deque
import sys


def bfs(adj, vst, start_points):
    q = deque([[[row, column], 0] for row, column in start_points])
    for row, column in start_points:
        vst[row][column] = True

    while q:
        curr, dist = q.popleft()
        for nxt in adj[curr[0]][curr[1]]:
            if not vst[nxt[0]][nxt[1]]:
                q.append([nxt, dist + 1])
                vst[nxt[0]][nxt[1]] = True
    return dist


M, N = map(int, sys.stdin.readline().rstrip().split())  # 가로, 세로/ Column, Row
Tomato = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

start_points = []
adj = [[[] for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
for row in range(N):
    for column in range(M):
        if Tomato[row][column] == -1:
            visited[row][column] = True
        elif Tomato[row][column] == 1:
            start_points.append([row, column])
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= row + dr < N and 0 <= column + dc < M and Tomato[row + dr][column + dc] != -1:
                adj[row][column].append([row + dr, column + dc])

max_step = bfs(adj, visited, start_points)

all_visited = True
for row in range(N):
    if not all_visited:  # No_breaker = all_visited
        break
    for column in range(M):
        if not visited[row][column]:
            all_visited = False
            break

if all_visited:
    print(max_step)
else:
    print(-1)"""

# 김정현(powergee) 보완해주심: https://www.acmicpc.net/source/share/96a2e18d76f1448a89340e1cd980834d
'''adj 배열이 메모리를 상당히 많이 사용합니다. 이론적으로 adj의 메모리 사용량을 계산해보면 약 1000^2*8 byte = 8 MB 밖에 되지 않지만, 내부적으로 리스트가 상당히 많이 겹쳐져 있으므로 
파이썬에서는 이 배열이 많은 메모리를 사용하게 됩니다. bfs 함수에서 UnboundLocalError가 발생할 수 있습니다. 함수의 마지막 줄에서 dist를 반환하고 있는데, dist는 while의 내부에서 
선언된 변수로, scope의 바깥에서 scope 안의 변수를 참조하므로 사실 illegal한 동작입니다. 대부분의 경우에는 while이 적어도 한번 실행되어 dist 변수가 할당되기 때문에 이 문제가 발생하지 
않지만, while이 단 한번도 실행되지 않는 예시(ex. 입력이 모두 -1인 경우)에는 이 문제가 발생합니다. '''
# 그 코드를 이해하고 정리해본 코드
from collections import deque
import sys


def bfs(M, N, Tomato, vst, start_points):
    q = deque([[[row, column], 0] for row, column in start_points])
    for row, column in start_points:
        vst[row][column] = True

    maxDist = -1  # q가 []이라면 while이 실행X(ex. 입력이 모두 -1)
    while q:
        curr, dist = q.popleft()
        maxDist = max(maxDist, dist)
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= curr[0] + dr < N and 0 <= curr[1] + dc < M and Tomato[curr[0] + dr][curr[1] + dc] != -1:
                nxt = [curr[0] + dr, curr[1] + dc]  # 매번 인접한 방향을 확인함으로써 adj의 메모리 과다 사용 문제 해결
                if not vst[nxt[0]][nxt[1]]:
                    q.append([nxt, dist + 1])
                    vst[nxt[0]][nxt[1]] = True
    return maxDist


M, N = map(int, sys.stdin.readline().rstrip().split())  # 가로, 세로/ Column, Row
Tomato = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

start_points = []
visited = [[False for _ in range(M)] for _ in range(N)]
for row in range(N):
    for column in range(M):
        if Tomato[row][column] == 1:
            start_points.append([row, column])
        elif Tomato[row][column] == -1:
            visited[row][column] = True

max_step = bfs(M, N, Tomato, visited, start_points)

all_visited = True
for row in range(N):
    if not all_visited:  # No_breaker = all_visited
        break
    for column in range(M):
        if not visited[row][column]:
            all_visited = False
            break

if all_visited:
    print(max_step)
else:
    print(-1)