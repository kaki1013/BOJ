N, S = map(int, input().split())
A = list(map(int, input().split()))

# meet in the middle
m, n = N//2, N-N//2
A1, A2 = [A[i] for i in range(m)], [A[i] for i in range(m, N)]

# sum..
s1, s2 = {0:1}, {0:1}


def dfs(n, arr, d, idx, s):
    if idx == n:
        return
    tmp = s + arr[idx]

    if tmp in d:
        d[tmp] += 1
    else:
        d[tmp] = 1

    dfs(n, arr, d, idx+1, s)
    dfs(n, arr, d, idx+1, tmp)


dfs(m, A1, s1, 0, 0)
dfs(n, A2, s2, 0, 0)

# ans..
ans = 0
for x in s1.keys():
    if S-x in s2:
        ans += s1[x] * s2[S-x]
if S == 0:
    ans -= 1  # 0, 0 -> empty set
print(ans)
