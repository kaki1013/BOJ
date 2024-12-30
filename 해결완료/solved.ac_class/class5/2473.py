# 2467 응용
# 기존: N^2logN (이중 반복문 + 이분 탐색)
# 새로운 풀이: N^2 (정렬 + 투 포인터)
# 반례 참고: https://www.acmicpc.net/board/view/59873, https://www.acmicpc.net/board/view/70893
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

# 다른 풀이(정렬, 투 카운터): https://zu-techlog.tistory.com/25
import sys

n = int(input())
array = list(map(int, input().split()))

array.sort()
minTake = sys.maxsize

for i in range(n - 2):
    start = i + 1
    end = n - 1
    while start < end:
        take = array[i] + array[start] + array[end]
        if abs(take) < minTake:
            minTake = abs(take)
            result = [array[i], array[start], array[end]]
        if take < 0:
            start += 1
        elif take > 0:
            end -= 1
        else:
            break

print(result[0], result[1], result[2])