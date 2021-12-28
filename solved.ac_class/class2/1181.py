N = int(input())
arr = [[] for _ in range(50)]
m = 0
for _ in range(N):
    s = input()
    if s not in arr[len(s) - 1]:
        arr[len(s) - 1].append(s)
for a in arr:
    if len(a) not in [0, 1]:
        a.sort()
for a in arr:
    for s in a:
        print(s)