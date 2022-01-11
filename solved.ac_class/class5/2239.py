all_found = False


def is_correct(r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False
    rr, cc = r // 3, c // 3
    for row in range(3 * rr, 3 * (rr + 1)):
        for col in range(3 * cc, 3 * (cc + 1)):
            if board[row][col] == num:
                return False
    return True


def dfs(r, c, n, left):
    global all_found
    board[r][c] = n
    if left == 1:
        all_found = True
        return
    now = 9 * r + c
    for nxt in range(now + 1, 81):
        row, col = nxt // 9, nxt % 9
        if not board[row][col]:
            break
    for num in range(1, 10):
        if is_correct(row, col, num):
            dfs(row, col, num, left-1)
    if not all_found:
        board[r][c] = 0


board = [list(map(int, list(input()))) for _ in range(9)]
count = 0
for now in range(81):
    row, col = now // 9, now % 9
    if not board[row][col]:
        if not count:
            r, c = row, col
        count += 1

for n in range(1, 10):
    if is_correct(r, c, n):
        dfs(r, c, n, count)
for line in board:
    print(''.join(list(map(str, line))))