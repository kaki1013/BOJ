# UCPC 2019 예선 J
"""
가장 가까운 편의시설까지의 거리와 가장 먼 편의시설까지의 거리의 '평균' 이 최소
= 가장 가까운 편의시설까지의 거리와 가장 먼 편의시설까지의 거리의 '합' 이 최소
즉, 정답으로 가능한 집의 위치 중 하나에 대해
가장 가까운 편의시설 - 집 - 가장 먼 편의시설이 한 직선 위에 있도록 하는 직선이 존재한다 by 삼각부등식
이때 '가장 가까운 편의시설과는 더 가까워지고, 가장 먼 편의시설과는 더 멀어지는 것'은 답을 변화시키지 않으므로
집을 가장 가까운 편의시설 위로 이동시킬 수 있다.
다시 말해, 집은 편의시설 위에 존재해야 한다.
결국 집의 위치는 다음과 같이 구해진다.
1. 편의시설 i (1 <= i <= N) 에 대해 가장 먼 곳과의 거리를 d_i 라고 하면
2. d_i를 최소로 만드는 편의시설 i가 집의 위치이다.
"""
N = int(input())
utilities = [tuple(map(int, input().split())) for _ in range(N)]
candidate = [0] * N

for i in range(N):
    for j in range(N):
        compare = (utilities[j][0] - utilities[i][0])**2 + (utilities[j][1] - utilities[i][1])**2
        if compare > candidate[i]:
            candidate[i] = compare

"""
min_Dist, house_idx = candidate[0], 0
for i in range(N):
    if candidate[i] < min_Dist:
        min_Dist = candidate[i]
        house_idx = i
"""

house_idx = candidate.index(min(candidate))
print(*utilities[house_idx])
