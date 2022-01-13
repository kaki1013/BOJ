# 2467 응용
# 간략화 필요..
def update(now, v1, v2, v3):
    if abs(sol[v1] + sol[v2] + sol[v3]) < abs(sum(now)):
        now = (sol[v1], sol[v2], sol[v3])
    return now


N = int(input())  # 3 ~ 5,000
sol = sorted(list(map(int, input().split())))
minimum = (sol[0], sol[1], sol[2])

for i in range(N):
    for j in range(i + 1, N):
        find = -(sol[i] + sol[j])
        left, right = 0, N - 1
        if find <= sol[left]:
            check = left
            if i == left:
                check += 1
                if j == left + 1:
                    check += 1
            minimum = update(minimum, i, j, check)
            continue
        elif find >= sol[right]:
            check = right
            if j == right:
                check -= 1
                if i == right - 1:
                    check -= 1
            minimum = update(minimum, i, j, check)
            continue
        else:  # left_sol < find < right_sol
            while True:
                if right - left == 1:
                    if i != left:
                        if j != left:
                            minimum = update(minimum, i, j, left)
                        else:
                            minimum = update(minimum, i, j, right)
                    if i != right:
                        if j != right:
                            minimum = update(minimum, i, j, right)
                        else:
                            if i != left:
                                minimum = update(minimum, i, j, right - 1)
                            else:
                                if left - 1 >= 0:
                                    minimum = update(minimum, i, j, left - 1)
                                if right + 1 < N:
                                    minimum = update(minimum, i, j, right + 1)
                    break
                mid = (left + right) // 2
                if sol[mid] < find:
                    left = mid
                elif find < sol[mid]:
                    right = mid
                else:  # find == sol[mid]
                    if mid == i:
                        if i - 1 >= 0:
                            minimum = update(minimum, i, j, i - 1)
                        if i + 1 != j:
                            minimum = update(minimum, i, j, i + 1)
                        else:
                            if j + 1 < N:
                                minimum = update(minimum, i, j, j + 1)
                    else:
                        if mid == j:
                            if j + 1 < N:
                                minimum = update(minimum, i, j, j + 1)
                            if j - 1 != i:
                                minimum = update(minimum, i, j, j - 1)
                            else:
                                if i - 1 > 0:
                                    minimum = update(minimum, i, j, i - 1)
                        else:
                            minimum = update(minimum, i, j, mid)
                    break

print(*sorted(minimum))
