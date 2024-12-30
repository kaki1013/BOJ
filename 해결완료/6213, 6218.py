# 2357 응용, 6218 완전 동일
import sys
input = sys.stdin.readline


def initialize(index, start, end):
    if start == end:
        nodes[index] = (num[start], num[start])
        return nodes[index]
    mid = (start + end) // 2
    left = initialize(index * 2, start, mid)
    right = initialize(index * 2 + 1, mid + 1, end)
    nodes[index] = (min(left[0], right[0]), max(left[1], right[1]))
    return nodes[index]


def query(index, nodeStart, nodeEnd, reqStart, reqEnd):
    nodeMid = (nodeStart + nodeEnd) // 2
    if reqEnd < nodeStart or nodeEnd < reqStart:
        return 10 ** 9 + 1, 0
    elif reqStart <= nodeStart and nodeEnd <= reqEnd:
        return nodes[index]
    else:
        left = query(index * 2, nodeStart, nodeMid, reqStart, reqEnd)
        right = query(index * 2 + 1, nodeMid + 1, nodeEnd, reqStart, reqEnd)
        return min(left[0], right[0]), max(left[1], right[1])


N, Q = map(int, input().split())
num = [int(input()) for _ in range(N)]
nodes = [(0, 0) for _ in range(4*N)]
initialize(1, 0, N - 1)

for _ in range(Q):
    a, b = map(int, input().split())
    m, M = query(1, 0, N - 1, a - 1, b - 1)
    print(M - m)
