# 2467 동일, 단 정렬되지 않은 입력
def update(arr, now, update1, update2):
    if abs(arr[update1] + arr[update2]) < abs(sum(now)):
        now = (arr[update1], arr[update2])
    return now


N = int(input())  # 2 ~ 100,000
A = sorted(list(map(int, input().split())))     # sorted

m = (A[0], A[1])

for i in range(N):
    find = -A[i]
    left, right = 0, N - 1
    while True:
        left_sol, right_sol = A[left], A[right]
        if find <= left_sol:
            if i != left:
                m = update(A, m, i, left)
            else:
                m = update(A, m, i, left + 1)
            break
        elif find >= right_sol:
            if i != right:
                m = update(A, m, i, right)
            else:
                m = update(A, m, i, right - 1)
            break
        else:  # left_sol < find < right_sol
            if right - left == 1:
                if i != left:
                    m = update(A, m, i, left)
                if i != right:
                    m = update(A, m, i, right)
                break
            mid = (left + right) // 2
            if A[mid] < find:
                left = mid
            elif find < A[mid]:
                right = mid
            else:  # find == solutions[m]
                m = update(A, m, i, mid)
                break

print(*sorted(m))
