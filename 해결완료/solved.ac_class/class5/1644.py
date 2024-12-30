N = int(input())
p = [True] * (N + 1)
for i in range(2, int(N ** 0.5) + 1):
    if p[i]:
        for j in range(i + i, N + 1, i):
            p[j] = False
prime = [i for i in range(2, N + 1) if p[i]]

partial = [0]
for p in prime:
    partial.append(partial[-1] + p)

ans = 0
l, r = 0, 0
while True:
    if partial[r] == partial[-1]:
        if partial[l] == partial[-1]:
            break
        now = partial[r] - partial[l]
        if now == N:
            ans += 1
            break
        if now > N:
            l += 1
            continue
        if now < N:
            break
    now = partial[r] - partial[l]
    if now < N:
        r += 1
    if now > N:
        l += 1
    if now == N:
        ans += 1
        l += 1
        r += 1
print(ans)

# 누적합 쓸 필요 없음, 바로 투포인터 가능
# 참고: https://www.acmicpc.net/source/35563911
length = len(p)
start = end = 0
h = cnt = 0
while 1:
    if h >= N:
        if h == N:
            cnt += 1
        h -= p[start]
        start += 1
    elif end == length:
        break
    else:
        h += p[end]
        end += 1
print(cnt)
