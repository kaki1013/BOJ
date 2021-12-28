N = int(input())
arr = []
for _ in range(N):
    pair = list(map(int, input().split()))
    arr.append(pair)

arr.sort()


for a in arr:
    print(a[0], a[1])