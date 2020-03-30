# 1. level 'l'의 노드 수는 최대 2^(l-1)
# 2. height 'h'의 노드 수는 최대 2^h-1
# 3. N 노드를 가지는 트리에서 최소 l or h = log_2(N+1)
# 4. l leaves를 가지는 트리는 최소 log_2(L) levels
# 5. Full Binary tree는 leaves = internal + 1


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        left = self.left.val if self.left else None
        right = self.right.val if self.right else None
        return 'val: {}, left: {}, right: {}'.format(self.val, left, right)


def array_to_tree(arr):
    root = None
    return build_tree(arr, root, 0)


def build_tree(arr, node, i):
    if i < len(arr):
        if not arr[i]:
            return None
        node = Node(arr[i])
        node.left = build_tree(arr, node.left, 2 * i + 1)
        node.right = build_tree(arr, node.right, 2 * i + 2)
    return node
