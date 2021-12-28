n, E, W, S, N = map(int, input().split())

visited = [False for _ in range((2 * n + 1) ** 2)]
stack = [(2 * n * (n + 1), 0, 1, visited)]
ans = 0
while len(stack) > 0:
    now, distance, possibility, vst = stack.pop()

    if distance == n:
        ans += possibility
        continue
    if vst[now]:
        continue
    vst[now] = True

    east, west, south, north = now + 1, now - 1, now + (2 * n + 1), now - (2 * n + 1)
    if now % (2 * n + 1) != 2 * n and not vst[east] and possibility * E != 0:
        stack.append((east, distance + 1, possibility * E, vst[:]))
    if now % (2 * n + 1) != 0 and not vst[west] and possibility * W != 0:
        stack.append((west, distance + 1, possibility * W, vst[:]))
    if 0 <= south <= 4 * n * n + 4 * n and not vst[south] and possibility * S != 0:
        stack.append((south, distance + 1, possibility * S, vst[:]))
    if 0 <= south <= 4 * n * n + 4 * n and not vst[north] and possibility * N != 0:
        stack.append((north, distance + 1, possibility * N, vst[:]))

print(ans/100**n)


# https://www.acmicpc.net/source/10631138
def check_safe(x, y, level, prob):
    if level == num:
        return prob

    visited[x][y] = True
    ret_prob = 0

    if not visited[x + 1][y]:
        ret_prob += check_safe(x+1, y, level + 1, prob * e)
    if not visited[x - 1][y]:
        ret_prob += check_safe(x-1, y, level + 1, prob * w)
    if not visited[x][y + 1]:
        ret_prob += check_safe(x, y+1, level + 1, prob * s)
    if not visited[x][y - 1]:
        ret_prob += check_safe(x, y-1, level + 1, prob * n)

    visited[x][y] = False  # 2차원 배열에서 백트래킹 효율적으로 사용
    return ret_prob


num, e, w, s, n = list(map(int, input().split(' ')))

e /= 100
w /= 100
s /= 100
n /= 100

visited = [[False for x in range(30)] for y in range(30)]

print(check_safe(14, 14, 0, 1))
