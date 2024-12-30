"""
맨 끝에 0이 생기기 위한 조건 : 곱해지는 과정에서 2와 5가 짝을 맞추며 추가
2는 수 2개에 1번 꼴로 추가되지만 5의 경우는 그렇지 않으므로
중간에 5가 몇개 들어갔는지가 관건
목표는 0!부터 n!까지 중에서 끝이 0이 짝수일 때를 세는 것

5 10 15 20 25 30 ... 125 130 ... 620 625 ...
1 1  1  1  2
짝수:
0~4, 10~14, 20~24
25~29, 35~39

홀수:
5~9, 15~19
30~34,
, ..., 95~99

"""
"""
while True:
    n = int(input())
    if n == -1:
        break
    q, r = n//10, n%10+1  # 0~4가 1~5에 대응
    print(5*q+r)
"""
from math import factorial
for i in range(101):
    f = str(factorial(i))
    count = 0
    while f[-1-count] == '0':
        count += 1
    print(i, count % 2 == 0, int(f))
