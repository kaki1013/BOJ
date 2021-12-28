# N을 만들 수 없다면, 시작하는 수로 가능한 경우는 3가지. N보다 크면서 만들 수 있는 가장 작은 수, N보다 작으면서 만들 수 있는 가장 큰 수, 100(기존 수)
# 이때 각 수에 대해서 '해당 숫자의 자리수 + N과의 차' 와 'N과 100의 차이', 이 3가지 값들 중 최소인 수가 정답
N = input()
n = int(N)
M = int(input())
least = 0 if n == 100 else abs(n-100)  # N이 100이면 0, 100이 아니면 최대 N-100(+나 -로만)
if M != 0:
    impossible = set(input().split())

    makable = True
    for s in N:
        if s in impossible:
            makable = False
            break
    if makable:
        least = min(least, len(N))

    for i in range(n-1, -1, -1):
        makable = True
        for s in str(i):
            if s in impossible:
                makable = False
                break
        if makable:
            least = min(least, len(str(i))+(n-i))
            break

    if (not ((M == 9) and ('0' not in impossible))) and (M != 10):
        i = n+1
        while True:
            makable = True
            for s in str(i):
                if s in impossible:
                    makable = False
                    break
            if makable:
                least = min(least, len(str(i)) + (i-n))
                break
            i += 1
else:
    least = min(least, len(N))

print(least)

# 반례
# 123456
# 9
# 1 2 3 4 5 6 7 8 9

# 2
# 9
# 0 1 2 3 4 5 6 7 8

# 1
# 0