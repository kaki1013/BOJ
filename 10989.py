"""
1. 메모리 초과
수의 개수 N은 최대 10^7인 반면, 수는 최대 10^4 이므로 각 수들은 평균적으로 1000번의 중복도를 가진다.
즉 실질적으로 정렬을 해야 하는 수들의 개수는 최대 10^4 = 10000 개 뿐이다.
2. Counting sort
입력 데이터에 특별한 조건 (입력으로 들어올 수 있는 데이터의 종류가 제한되어 있음) 이 있어야 사용할 수 있음
"""
import sys

N = int(sys.stdin.readline().rstrip())

count = [0 for _ in range(10001)]
for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    count[n] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)
