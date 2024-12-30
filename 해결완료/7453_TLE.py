"""
https://www.acmicpc.net/board/view/65350

dict는 시간 복잡도만 평균 O(1)일 뿐, 숨어있는 상수가 매우 큽니다. 사실상 로그가 붙은 코드들과 비슷하거나 더 오래 걸린다고 생각하시면 됩니다.
"""
# c++로 해결
from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

s1, s2 = [], []
for a in A:
    for b in B:
        s1.append(a+b)

for c in C:
    for d in D:
        s2.append(c+d)

s1.sort()
s2.sort()

ans = 0
for x in s1:
    l = bisect_left(s2, -x)
    r = bisect_right(s2, -x)
    if s2[l] == -x:
        ans += r-l
print(ans)
