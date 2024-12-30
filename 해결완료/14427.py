# 14428 응용: 연산 2를 수열 전체에 대해서 수행
import sys
input = sys.stdin.readline


def initialize(index, start, end):
    if start == end:
        nodes[index] = start
        return nodes[index]
    mid = (start + end) // 2
    left = initialize(index * 2, start, mid)
    right = initialize(index * 2 + 1, mid + 1, end)
    nodes[index] = left if num[left] <= num[right] else right
    return nodes[index]


def query(index, nodeStart, nodeEnd, reqStart, reqEnd):
    nodeMid = (nodeStart + nodeEnd) // 2
    if reqEnd < nodeStart or nodeEnd < reqStart:
        return -1
    elif reqStart <= nodeStart and nodeEnd <= reqEnd:
        return nodes[index]
    else:
        left = query(index * 2, nodeStart, nodeMid, reqStart, reqEnd)
        right = query(index * 2 + 1, nodeMid + 1, nodeEnd, reqStart, reqEnd)
        if left == -1:
            return right
        elif right == -1:
            return left
        return left if num[left] <= num[right] else right


def update(index, nodeStart, nodeEnd, reqIndex, newVal):
    nodeMid = (nodeStart + nodeEnd) // 2
    if nodeStart == nodeEnd:
        num[reqIndex] = newVal
    else:
        if reqIndex <= nodeMid:
            update(index * 2, nodeStart, nodeMid, reqIndex, newVal)
        else:
            update(index * 2 + 1, nodeMid + 1, nodeEnd, reqIndex, newVal)
        left, right = nodes[index*2], nodes[index*2+1]
        nodes[index] = left if num[left] <= num[right] else right


N = int(input())
num = list(map(int, input().split()))
nodes = [0 for _ in range(4*N)]
initialize(1, 0, N - 1)

M = int(input())
for _ in range(M):
    Q = list(map(int, input().split()))
    if Q[0] == 1:
        update(1, 0, N - 1, Q[1] - 1, Q[2])
    if Q[0] == 2:
        print(query(1, 0, N - 1, 0, N - 1) + 1)
