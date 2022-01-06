board = [list(map(int, list(input()))) for _ in range(9)]
for line in board:
    print(*line)