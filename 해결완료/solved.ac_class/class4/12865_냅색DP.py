"""
# sol1: TLE
N, K = map(int, input().split())  # 물건의 개수, 최대 가능 무게
stuff = [tuple(map(int, input().split())) for _ in range(N)]  # (무게 W, 가치 V)

possible = [(0, 0)]
ans = 0

for i in range(N):
    w, v = stuff[i]
    for weight, value in possible[:]:
        if w + weight <= K:
            possible.append((weight + w, value + v))
            ans = max(ans, value + v)

print(ans)
"""
# sol2 by 알림
N, K = map(int, input().split())  # 물건의 개수, 최대 가능 무게
w, v = [0], [0]  # 무게와 가치 리스트
for _ in range(N):  # 입력받기
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

# dp[i][j] := i번쩨 물건까지 고려했을 때, 무게가 k 이하인 조합 중 가치(v)가 최대인 경우
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

# 초기 조건: 1번째 물건을 골랐을 때, 각 무게에 대한 최대 가치
for j in range(K+1):  # 최대 무게를 0부터 K까지 늘려감
    if w[1] <= j:  # 넣을 공간이 있으면
        dp[1][j] = v[1]  # 넣음
    else:  # 없으면
        dp[1][j] = 0  # 넣지 않음

# 2번째 물건부터 N번째 물건까지 차례대로 넣음
for i in range(2, N+1):  # i번째 물건 넣음
    for j in range(K+1):  # 최대 무게를 0부터 K까지 늘려감
        if w[i] <= j:  # 넣을 공간이 있으면
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])  # 넣지 않는 경우와 넣는 경우 중 가치가 최대인 경우 선택
        else:  # 넣을 공간이 없으면
            dp[i][j] = dp[i-1][j]  # 넣지 않는 경우 선택

print(dp[N][K])
