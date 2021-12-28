import sys

N = int(sys.stdin.readline().rstrip())
points = [tuple(map(float, sys.stdin.readline().rstrip().split())) for _ in range(N)]
dist_power = []
for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        dist_power.append((x1-x2)**2 + (y1-y2)**2)
dist_power.sort()
count = dict()
for power in dist_power:
    if power in count:
        count[power] += 1
    else:
        count[power] = 1

# {a_i} (최대 개수 1.125*10^4=11250, 약 10^4)에서 a + b = c인 경우의 수 찾기
ans = 0
l = len(count)
for i in range(l):
    pass

# 기울기 곱이 -1인 걸 이용해야 함!
