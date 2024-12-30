idx = 0
while True:
    M, N, P, Q = map(int, input().split())
    if not M:
        break
    A = [list(map(int, input().split())) for _ in range(M)]
    B = [list(map(int, input().split())) for _ in range(P)]
    idx += 1
    print(f"Case #{idx}:")
    if N == P:
        ans = [[0 for _ in range(Q)] for _ in range(M)]
        for i in range(M):
            for j in range(Q):
                temp = 0
                for k in range(N):
                    temp += A[i][k] * B[k][j]
                ans[i][j] = temp
        for i in range(M):
            print("| ", end='')
            print(*ans[i], end='')
            print(" |")
    else:
        print("undefined")
