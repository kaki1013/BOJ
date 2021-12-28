import sys
# https://www.acmicpc.net/board/view/66942
# 가장 큰 수가 뭔지 모름
while True:
    l = list(map(int, sys.stdin.readline().split()))
    l.sort()
    [a, b, c] = l
    if (a, b, c) == (0, 0, 0):
        break
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')