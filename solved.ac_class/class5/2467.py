def update(arr, now, update1, update2):
    if abs(arr[update1] + arr[update2]) < abs(sum(now)):
        now = (arr[update1], arr[update2])
    return now


N = int(input())  # 2 ~ 100,000
solutions = list(map(int, input().split()))  # sorted

minimum = (solutions[0], solutions[1])

for i in range(N):
    find = -solutions[i]
    left, right = 0, N - 1
    while True:
        left_sol, right_sol = solutions[left], solutions[right]
        if find <= left_sol:
            if i != left:
                minimum = update(solutions, minimum, i, left)
            else:
                minimum = update(solutions, minimum, i, left + 1)
            break
        elif find >= right_sol:
            if i != right:
                minimum = update(solutions, minimum, i, right)
            else:
                minimum = update(solutions, minimum, i, right - 1)
            break
        else:  # left_sol < find < right_sol
            if right - left == 1:
                if i != left:
                    minimum = update(solutions, minimum, i, left)
                if i != right:
                    minimum = update(solutions, minimum, i, right)
                break
            m = (left + right) // 2
            if solutions[m] < find:
                left = m
            elif find < solutions[m]:
                right = m
            else:  # find == solutions[m]
                minimum = update(solutions, minimum, i, m)
                break

print(*sorted(minimum))
