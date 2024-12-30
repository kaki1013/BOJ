# sol1: 내가 푼 풀이 / 6576 ms
def trans(char):
    return ord(char) - ord('A')


def dfs(r, c, score):
    global ans
    if ans == 26:       # 26이 존재하는 순간 이후의 탐색은 모두 불필요함
        return
    score += 1
    if score == 26:     # 최대 26까지 가능함을 이용하면 탐색을 크게 줄일 수 있음
        ans = 26
        return
    visited[r][c] = True
    chosen[board[r][c]] = True

    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        rr, cc = r + dr, c + dc
        if 0 <= rr < R and 0 <= cc < C:
            if not visited[rr][cc] and not chosen[board[rr][cc]]:
                dfs(rr, cc, score)
            else:
                ans = max(ans, score)

    visited[r][c] = False
    chosen[board[r][c]] = False


R, C = map(int, input().split())
board = [list(map(trans, list(input()))) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
chosen = [False] * 26

ans = 1
dfs(0, 0, 0)
print(ans)

# sol2: https://www.acmicpc.net/source/30256339 / 208ms
# stack을 명시적으로 사용한 dfs 라서 더 빠른가?
R, C = map(int,input().split())

arr = [list(input()) for _ in range(R)]
check = [['']*C for _ in range(R)]

stack = [(0,0,1,arr[0][0])]
result = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]
while stack:
    x,y,cnt,total = stack.pop()
    if result < cnt:
        result = cnt
    if result == 26:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < R and 0<= ny <C:
            if arr[nx][ny] not in total:
                temp = total + arr[nx][ny]
                if check[nx][ny] != temp:
                    check[nx][ny] = temp
                    stack.append((nx,ny,cnt+1,temp))
print(result)