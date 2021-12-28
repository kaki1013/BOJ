def tree_traversal(tree, root, mod):
    if root == '.':
        return ''
    if tree[root] == ['.', '.']:
        return root
    if mod == 1:  # 전위
        return root + tree_traversal(tree, tree[root][0], mod) + tree_traversal(tree, tree[root][1], mod)
    elif mod == 2:  # 중위
        return tree_traversal(tree, tree[root][0], mod) + root + tree_traversal(tree, tree[root][1], mod)
    else:  # 후위
        return tree_traversal(tree, tree[root][0], mod) + tree_traversal(tree, tree[root][1], mod) + root


N = int(input())
tree = dict()
for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = [left, right]

print(tree_traversal(tree, 'A', 1))
print(tree_traversal(tree, 'A', 2))
print(tree_traversal(tree, 'A', 3))
