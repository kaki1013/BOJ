"""
sol1: 메모리 초과
from collections import deque

N = int(input())
possible = deque([([i], 1) for i in range(N)])
ans = 0

while possible:
    now, length = possible.popleft()
    if length == N:
        ans += 1
        continue
    for nxt_column in range(N):  # (length+1, nxt_column)
        if nxt_column in now:  # 같은 열
            continue

        failure = False
        for previous_row in range(length):
            if abs(length - previous_row) == abs(nxt_column - now[previous_row]):  # 대각선
                failure = True
                break
        if failure:
            continue
        possible.append((now + [nxt_column], length+1))  # 가능한 경우
print(ans)

# sol2: 시간초과
# https://claude-u.tistory.com/245 // https://wookcode.tistory.com/57
# 행과 열을 이중배열로 표현하지 않고, index가 행이고 row[index]가 열이 되게 함으로써 리스트 하나로 보드판을 표현
def adjacent(row, x):
    for i in range(x):  # i 값이 행, row[i] 값이 열
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:  # 내 윗줄에 나와 겹치는 열 또는 대각선에 퀸이 있는가?
            return False
    return True


# 한줄씩 재귀하며 DFS를 실행
def dfs(row, x, n):  # row, 살펴볼 행, 보드판의 사이즈 n
    global result

    if x == n:
        result += 1

    else:
        for i in range(n):  # 살펴볼 행의 각 열들에 대해 유망한 곳 찾기
            row[x] = i  # dfs 이므로 이전의 상태를 row로 유지 가능
            if adjacent(row, x):  # 유망한 경우라면 다음 행도 살펴봄
                dfs(row, x + 1, n)


N = int(input())
row = [0] * N  # 각 행들에서 퀸가 위치한 열의 값을 저장할 배열

result = 0
dfs(row, 0, N)
print(result)
"""
# sol3
# https://www.acmicpc.net/board/view/70799  //  https://developmentdiary.tistory.com/292
N = int(input())
row = [True] * N
dial_s = [True] * (2 * N - 1)  # 부대각선일 경우 x와 y 좌표의 합이 일정함을 이용 (ex) 0,1 과 1,0
dial_m = [True] * (2 * N - 1)  # 정대각선일 경우 x와 y 좌표의 차가 일정함을 이용 (ex) 0,1 과 1,2


def findNQueen(n):
    global row, dial_s, dial_m
    if n == N:
        global cnt
        cnt += 1
        return
    for j in range(N):
        if row[j] and dial_s[n + j] and dial_m[n - j + N - 1]:
            row[j], dial_s[n + j], dial_m[n - j + N - 1] = False, False, False
            findNQueen(n + 1)
            row[j], dial_s[n + j], dial_m[n - j + N - 1] = True, True, True


cnt = 0
findNQueen(0)
print(cnt)
