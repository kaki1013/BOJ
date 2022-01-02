from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    # 입력
    p = input()
    n = int(input())
    if n:
        x = list(map(int, input()[1:-2].split(',')))  # readline -> \n 고려
    else:
        __ = input()
        x = []
    x = deque(x)
    # 처리
    is_reversed = False
    error = False
    for q in p:
        if q == 'R':    # 뒤집기
            is_reversed = not is_reversed
        if q == 'D':    # 첫 번째 수 삭제
            if len(x) == 0:
                error = True
                break
            if is_reversed:
                x.pop()
            else:
                x.popleft()
    # 출력
    print('error' if error else str(list(x)[::-1] if is_reversed else list(x)).replace(" ", ""))
