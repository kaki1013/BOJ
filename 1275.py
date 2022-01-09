import sys
input = sys.stdin.readline


def initialize(index, start, end):
    if start == end:
        nodes[index] = num[start]
        return nodes[index]
    mid = (start + end) // 2
    left = initialize(index * 2, start, mid)
    right = initialize(index * 2 + 1, mid + 1, end)
    nodes[index] = left + right
    return nodes[index]


def query(index, nodeStart, nodeEnd, reqStart, reqEnd):
    nodeMid = (nodeStart + nodeEnd) // 2
    if reqEnd < nodeStart or nodeEnd < reqStart:
        return 0
    elif reqStart <= nodeStart and nodeEnd <= reqEnd:
        return nodes[index]
    else:
        left = query(index * 2, nodeStart, nodeMid, reqStart, reqEnd)
        right = query(index * 2 + 1, nodeMid + 1, nodeEnd, reqStart, reqEnd)
        return left + right


def update(index, nodeStart, nodeEnd, reqIndex, newVal):
    nodeMid = (nodeStart + nodeEnd) // 2
    if nodeStart == nodeEnd:
        nodes[index] = newVal
    else:
        if reqIndex <= nodeMid:
            update(index * 2, nodeStart, nodeMid, reqIndex, newVal)
        else:
            update(index * 2 + 1, nodeMid + 1, nodeEnd, reqIndex, newVal)
        nodes[index] = nodes[index * 2] + nodes[index * 2 + 1]


N, Q = map(int, input().split())
num = list(map(int, input().split()))
nodes = [0] * (4 * N)
initialize(1, 0, N - 1)
for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    print(query(1, 0, N - 1, x - 1, y - 1))
    update(1, 0, N - 1, a - 1, b)
