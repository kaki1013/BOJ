# 1부터 N까지의 자연수 중에서 중복 없이 M개를 골라 오름차순으로 나열한 수열들을 사전 순으로 증가하는 순서로 출력
# sol1: bfs 응용
from collections import deque


def nCr(q, n, r):
    q = deque(q)
    while q[0][1] != r:
        curr, count = q.popleft()
        last = curr[-1]
        for i in range(last + 1, n - (r - (count + 1)) + 1):
            q.append([curr + [i], count+1])
    return q


N, M = map(int, input().split())

combination = nCr([[[i + 1], 1] for i in range(N - M + 1)], N, M)

for case in combination:
    for i in range(M):
        case[0][i] = str(case[0][i])
    print(' '.join(case[0]))


# sol2: 재귀 by 알림
def comb(n , m, start, selected):
    if len(selected) == m:
        print(*selected)
    elif start <= n:
        selected.append(start)
        comb(n, m, start + 1, selected)
        selected.pop()
        comb(n, m, start + 1, selected)


n, m = map(int, input().split())
comb(n, m, 1, [])

# sol3: 스택_dfs 응용
n, m = map(int, input().split())
stack = [[1, []]]
while stack:
    now, selected = stack.pop()
    if now > n+1:
        continue
    if len(selected) == m:
        print(*selected)
        continue
    stack.append([now + 1, selected])
    stack.append([now + 1, selected+[now]])


# sol4: 비트마스크
def bitCount(x):
    if x == 0:
        return 0
    return x % 2 + bitCount(x // 2)


N, M = map(int, input().split())

numbers = list(range(1, N+1))
masks = [1 << i for i in range(N)]
ans = []
for case in range(1 << N):
    if bitCount(case) == M:
        subset = [numbers[i] for i in range(N) if case & masks[i]]
        ans.append(subset)

for subset in sorted(ans):
    print(*subset)
