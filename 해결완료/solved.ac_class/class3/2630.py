def square(arr, white, blue):  # 이중리스트
    l = len(arr)
    if l == 1 and arr[0][0] == 0:
        return 1, 0
    elif l == 1 and arr[0][0] == 1:
        return 0, 1
    sample = arr[0][0]
    perpect, breaker = False, False
    for i in range(l):
        if breaker:
            break
        for j in range(l):
            if arr[i][j] != sample:
                breaker = True
                break
            elif i == j == l-1:
                perpect = True
    if perpect and sample == 0:
        return 1, 0
    elif perpect and sample == 1:
        return 0, 1
    else:
        a = square([arr[i][:l // 2] for i in range(l // 2)], 0, 0)
        b = square([arr[l // 2 + i][:l // 2] for i in range(l // 2)], 0, 0)
        c = square([arr[i][l // 2:] for i in range(l // 2)], 0, 0)
        d = square([arr[l // 2 + i][l // 2:] for i in range(l // 2)], 0, 0)
        return a[0] + b[0] + c[0] + d[0], a[1] + b[1] + c[1] + d[1]


N = int(input())  # 2, 4, 8, 16, 32, 64, 128
color_paper = []
for _ in range(N):
    line = list(map(int, input().split()))
    color_paper.append(line)

for ans in square(color_paper, 0, 0):
    print(ans)