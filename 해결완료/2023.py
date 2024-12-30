from collections import deque


def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


N = int(input())
ans = deque([2, 3, 5, 7])
for i in range(2, N + 1):  # i자리 수 구하는 반복문
    temp = deque([])
    while ans:
        now = ans.popleft()
        for j in [1, 3, 5, 7, 9]:
            nxt = now * 10 + j
            if is_prime(nxt):
                temp.append(nxt)
    ans = temp

for num in ans:
    print(num)
