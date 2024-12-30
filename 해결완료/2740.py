def multi(mat1, mat2, i, j, common):
    ans = 0
    for k in range(common):
        ans += mat1[i][k] * mat2[k][j]
    return ans


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

ans = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        ans[i][j] = multi(A, B, i, j, M)
for line in ans:
    print(*line)