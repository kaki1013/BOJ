# 1부터 N까지의 자연수 중에서 중복 없이 M개를 골라 오름차순으로 나열한 수열들을 사전 순으로 증가하는 순서로 출력
from collections import deque


def nPr(p, n, r):
    q = deque(p)
    while q[0][1] != r:
        curr, count = q.popleft()
        for i in range(n):
            if i not in curr:
                q.append([curr + [i], count+1])
    return q


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

permutation = nPr([[[i], 1] for i in range(N)], N, M)

for case in permutation:
    for i in case[0]:
        print(arr[i], end=' ')
    print()

# https://www.acmicpc.net/source/18163272
from itertools import permutations

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))

print("\n".join(map(" ".join, permutations(map(str, arr), m))))