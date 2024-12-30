N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

# dp[state][last] := 현재 방문한 노드의 bit string이 state(출발점 미포함)에 대응되면, last를 마지막으로 방문했을 때의 최소 비용
dp = [[float('INF')] * N for _ in range(1 << N)]

# dp[state][last] := min(dp[state_][])
# ex. 1,2,3 방문 & 2가 마지막 : dp[{1, 2, 3}][2] := min(dp[{1, 3}][1] + W[1][2], dp[{1, 3}][3] + W[3][2])

def dfs(state, last):
    return

for i in range(N):
    dfs((1<<N)-1, i)
