N = int(input())
A = set(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

for m in arr:
    print(int(m in A))

# sol2: 이분탐색/ https://chancoding.tistory.com/44
from sys import stdin
n = stdin.readline()
N = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
M = map(int, stdin.readline().split())


def binary(l, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l, N, start, m-1)
    else:
        return binary(l, N, m+1, end)

for l in M:
    start = 0
    end = len(N)-1
    print(binary(l, N, start, end))