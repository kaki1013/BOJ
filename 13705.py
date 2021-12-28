# 14786 참고//틀림
# https://blog.naver.com/jinhan814/222076746452
# sin 함수도 구현해야 하는 듯
import math
from decimal import *
getcontext().prec = 300
D = Decimal


def check(a, b, c, x):
    return D(str(a)) * D(str(x)) + D(str(b)) * D(str(math.sin(D(str(x))))) - D(str(c)) >= 0


A, B, C = map(int, input().split())
error = str(10 ** (-9))  # 50%
left, right = D(str((D(str(C)) - D(str(B))))) / D(str(A)), D(str((D(str(C)) + D(str(B))))) / D(str(A))
m = D(str((D(str(left)) + D(str(right))))) / D(str(2))


while True:
    P, Q = check(A, B, C, m - D(error)), check(A, B, C, m + D(error))
    if P and not Q or not P and Q:
        break
    if check(A, B, C, m):
        right = m
    else:
        left = m
    m = D(str((D(str(left)) + D(str(right))))) / D(str(2))

print(round(m, 6))
