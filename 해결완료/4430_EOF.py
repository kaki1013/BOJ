# 14002 참고
# EOF 처리: https://pchild.tistory.com/2
# EOF 입력: ctrl + d
import sys
lines = sys.stdin.readlines()
elephants = []
N = len(lines)

for i in range(N):
    line = lines[i]
    w, iq = map(int, line.split())
    elephants.append((w, -iq, i+1))
elephants.sort()

dp = [1] * N
reverse_idx = list(range(N))
for now in range(N):
    for previous in range(now):
        if elephants[previous][1] < elephants[now][1] and elephants[previous][0] != elephants[now][0]:
            if dp[previous] + 1 > dp[now]:
                dp[now] = dp[previous] + 1
                reverse_idx[now] = previous

max_idx, max_length = 0, 1
for i in range(N):
    if dp[i] > max_length:
        max_length = dp[i]
        max_idx = i
print(max_length)

stack_value = [elephants[max_idx][2]]
stack_idx = [max_idx]
while stack_idx[-1] != reverse_idx[stack_idx[-1]]:  # self == inverse(self) 면 마지막 요소
    last = stack_idx[-1]
    nxt = reverse_idx[last]
    stack_idx.append(nxt)
    stack_value.append(elephants[nxt][2])

for idx in stack_value[::-1]:
    print(idx)
