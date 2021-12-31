# sol1: 시간초과 O(N^2)
N, S = map(int, input().split())
arr = list(map(int, input().split()))

cumulative_sum = [0]
for i in range(N):
    cumulative_sum.append(cumulative_sum[-1] + arr[i])

find = False
for length in range(1, N+1):
    if find:
        break
    for start in range(N - (length - 1)):
        if cumulative_sum[start+length] - cumulative_sum[start] >= S:
            print(length)
            find = True
            break

if not find:
    print(0)

# sol2: 투포인터
N, S = map(int, input().split())
arr = list(map(int, input().split()))

cumulative_sum = [0]
for i in range(N):
    cumulative_sum.append(cumulative_sum[-1] + arr[i])

min_length = N
left, right = 0, 0

while right < N - 1:
    if cumulative_sum[right + 1] - cumulative_sum[left] < S:  # left 부터 right 까지의 합
        right += 1
    else:
        min_length = min(min_length, right - left + 1)
        left += 1

for i in range(N, -1, -1):  # 5 15; 7 8 1 1 15
    if cumulative_sum[N] - cumulative_sum[i] >= S:
        min_length = min(min_length, N - i)
        break

if sum(arr) < S:
    print(0)
else:
    print(min_length)
