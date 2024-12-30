# 그리디: 가장 종료 시간이 빠른 회의(m)를 포함하는 최적해가 반드시 존재한다.
# 최적해 중에 m을 포함하지 않는 경우가 있다고 하면, 첫 번째로 개최되는 회의 대신 m을 넣을 수 있다
# 왜냐하면, m이 가장 일찍 끝나는 회의이므로 지워진 회의는 m보다 일찍 끝날 수 없고, 따라서 두번째 회의와 m은 겹치지 않는다.
# 즉 새로 만든 해도 최적해 중 하나이며, m을 포함하는 최적해는 항상 존재한다.
import sys
N = int(sys.stdin.readline().rstrip())
times = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

# 종료 시간을 기준으로 정렬하되, 종료 시간이 같은 경우 시작 시간이 빠른 것을 먼저
# 종료 시간의 우선 순위가 높으므로, 시작 시간을 기준으로 먼저 정렬
times = sorted(times, key=lambda time: time[0])
times = sorted(times, key=lambda time: time[1])

ans = 0
start = 0
for i in range(N):
    if times[i][0] >= start:  # 종료 시간과 이전의 시작 시간이 같을 수 있음
        ans += 1
        start = times[i][1]

print(ans)