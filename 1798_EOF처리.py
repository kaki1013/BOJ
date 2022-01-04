# 참고: https://has3ong.github.io/boj/boj-1798/
from math import cos, pi
import sys
input = sys.stdin.readline      # EOFError 피하려면 readline으로 해야 함

while True:
    arr = list(map(float, input().split()))     # ValueError 피하려면 arr로 따로받아서 처리
    if not arr:
        break
    r, h, d1, A1, d2, A2 = arr
    l = (r * r + h * h) ** 0.5
    A = abs(A1 - A2)
    if A > 180:
        A = 360 - A
    theta = (A * (2 * pi / 360)) * r / l

    dist = d1 ** 2 + d2 ** 2 - 2 * d1 * d2 * cos(theta)
    dist **= 0.5
    print('%.2f' % dist)