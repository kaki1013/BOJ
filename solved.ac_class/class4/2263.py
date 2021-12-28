# 프리오더, 인오더, 포스트오더 (전위 순회, 중위 순회, 후위 순회)
# post[-1]은 해당 트리의 루트 노드 // in 에서 앞서 구한 루트 노드를 기준으로 좌우 서브트리 얻음
"""
sol1: 메모리 초과
import sys
sys.setrecursionlimit(10**5)


def get_idx(arr, goal):
    l = len(arr)
    for i in range(l):
        if arr[i] == goal:
            return i
    return -1


def get_tree(post_ord, in_ord, tree_adj, parent):
    root = post_ord.pop()
    tree_adj[parent].append(root)
    idx = get_idx(in_ord, root)  # 루트노드의 in_ord 인덱스 찾기
    in_left, in_right = in_ord[:idx], in_ord[idx + 1:]
    post_left, post_right = post_ord[:idx], post_ord[idx:]
    if len(post_left) > 0:
        get_tree(post_left, in_left, tree_adj, root)
    if len(post_right) > 0:
        get_tree(post_right, in_right, tree_adj, root)


def dfs(adj, visited, start, search):
    if visited[start]:
        return
    visited[start] = True
    search.append(start)
    for nxt in adj[start]:
        dfs(adj, visited, nxt, search)


n = int(input())
adj = [[] for _ in range(n+1)]
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

root = post_order[-1]
idx_root = get_idx(in_order, root)
in_order_left, in_order_right = in_order[:idx_root], in_order[idx_root + 1:]
post_order_left, post_order_right = post_order[:idx_root], post_order[idx_root:-1]

get_tree(post_order_left, in_order_left, adj, root)
get_tree(post_order_right, in_order_right, adj, root)

visited = [False] * (n+1)
pre_order = []
dfs(adj, visited, root, pre_order)
print(*pre_order)

# sol2: 메모리 초과
import sys
sys.setrecursionlimit(10**5)


def get_idx(arr, goal):
    l = len(arr)
    for i in range(l):
        if arr[i] == goal:
            return i
    return -1


def get_pre(in_ord, post_ord):  # index를 전달?
    rt = post_ord.pop()
    print(rt, end=' ')
    idx = get_idx(in_ord, rt)  # in_ord 에서 루트노드의 인덱스 찾기
    post_right = post_ord[idx:]
    if idx > 0:  # left 가 원소 1개 이상 존재
        get_pre(in_ord[:idx], post_ord[:idx])
    if post_right:  # right 가 원소 1개 이상 존재
        get_pre(in_ord[idx+1:], post_right)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

root = post_order[-1]
idx_root = get_idx(in_order, root)

print(root, end=' ')
get_pre(in_order[:idx_root], post_order[:idx_root])
get_pre(in_order[idx_root + 1:], post_order[idx_root:-1])
"""
# sol3: 메모리 초과 -> 맞았습니다 by 알림 iknoom1107
import sys

sys.setrecursionlimit(10 ** 9)


def get_pre(pre_ord, in_ord, in_l, in_r, post_ord, post_l, post_r):  # 살펴볼 범위의 양 끝 index 를 left 와 right 로 전달
    rt = post_ord[post_r]
    pre_ord.append(rt)
    idx = in_order_location[rt]  # in_ord 에서 루트노드의 인덱스 찾기
    if idx > in_l:  # left 에 원소 1개 이상 존재
        # in_ord의 범위: left는 유지, right는 루트 노드 이전이므로 idx - 1
        # post_ord의 범위: left는 유지, right는 in_ord의 구간 길이와 일치하도록 조정
        get_pre(pre_ord, in_ord, in_l, idx - 1, post_ord, post_l, (post_l - in_l) + idx - 1)
    if idx < in_r:  # right 에 원소 1개 이상 존재
        # in_ord의 범위: left는 루트 노드 다음이므로 idx + 1, right는 유지
        # post_ord의 범위: right는 루트 노드를 제외하고 post_r - 1, left는 in_ord의 구간 길이와 일치하도록 조정
        get_pre(pre_ord, in_ord, idx + 1, in_r, post_ord, (post_r - in_r) + idx, post_r - 1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

# 매번 한 원소의 중위순회(인오더)에서의 인덱스를 찾을 경우 O(n^2)의 시간복잡도를 가지게 됨
in_order_location = [-1] * (n + 1)
for i in range(n):
    # in_order_location[x] := in_order 에서 x의 index 를 반환
    in_order_location[in_order[i]] = i

root = post_order[-1]
idx_root = in_order_location[root]

pre_order = [root]
if idx_root > 0:  # 왼쪽에 남은 원소가 있는지 체크
    get_pre(pre_order, in_order,  0, idx_root - 1, post_order, 0, idx_root - 1)
if idx_root < n - 1:  # 오른쪽에 남은 원소가 있는지 체크
    get_pre(pre_order, in_order, idx_root + 1, n - 1, post_order, idx_root, (n - 1) - 1)

print(*pre_order)


# sol4
import sys

sys.setrecursionlimit(10 ** 9)


def get_pre(pre_ord, in_ord, in_l, in_r, post_ord, post_l, post_r):  # 살펴볼 범위의 양 끝 index 를 left 와 right 로 전달
    rt = post_ord[post_r]
    pre_ord.append(rt)
    idx = in_order_location[rt]  # in_ord 에서 루트노드의 인덱스 찾기
    if idx > in_l:  # left 에 원소 1개 이상 존재
        # in_ord의 범위: left는 유지, right는 루트 노드 이전이므로 idx - 1
        # post_ord의 범위: left는 유지, right는 in_ord의 구간 길이와 일치하도록 조정
        get_pre(pre_ord, in_ord, in_l, idx - 1, post_ord, post_l, (post_l - in_l) + idx - 1)
    if idx < in_r:  # right 에 원소 1개 이상 존재
        # in_ord의 범위: left는 루트 노드 다음이므로 idx + 1, right는 유지
        # post_ord의 범위: right는 루트 노드를 제외하고 post_r - 1, left는 in_ord의 구간 길이와 일치하도록 조정
        get_pre(pre_ord, in_ord, idx + 1, in_r, post_ord, (post_r - in_r) + idx, post_r - 1)


n = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

# 매번 한 원소의 중위순회(인오더)에서의 인덱스를 찾을 경우 O(n^2)의 시간복잡도를 가지게 됨
in_order_location = [-1] * (n + 1)
for i in range(n):
    # in_order_location[x] := in_order 에서 x의 index 를 반환
    in_order_location[in_order[i]] = i

pre_order = []
get_pre(pre_order, in_order,  0, n-1, post_order, 0, n - 1)
print(*pre_order)