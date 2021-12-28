N, M = map(int, input().split())
array = list(map(int, input().split()))

made = array[0] + array[1] + array[2]
dif = M - array[0]

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            compare = array[i] + array[j] + array[k]
            if compare <= M and dif > M - compare:
                dif = M - compare
                made = compare
print(made)