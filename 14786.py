import math


def check(a, b, c, x):
    return a * x + b * math.sin(x) - c >= 0


A, B, C = map(int, input().split())
error = 10 ** (-10)
left, right = (C - B) / A, (C + B) / A
m = (left + right) / 2

while True:
    P, Q = check(A, B, C, m - error), check(A, B, C, m + error)
    if P and not Q or not P and Q:
        break
    if check(A, B, C, m):
        right = m
    else:
        left = m
    m = (left + right) / 2

print(m)
