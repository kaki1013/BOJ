N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
print(sum([A[i]*B[N-1-i] for i in range(N)]))
