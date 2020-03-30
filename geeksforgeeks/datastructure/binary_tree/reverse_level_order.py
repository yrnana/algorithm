from geeksforgeeks.datastructure.binary_tree.binary_tree import Node


def reverse_level_order(root):
    h = height(root)
    for i in reversed(range(1, h + 1)):
        print_level(root, i)


def height(node):
    if not node:
        return 0
    l = height(node.left)
    r = height(node.right)
    return max(l, r) + 1


def print_level(node, lvl):
    if not node:
        return
    if lvl == 1:
        print(node.val, end=' ')
        return
    print_level(node.left, lvl - 1)
    print_level(node.right, lvl - 1)


def reverse_level_order_stack(root):
    s, q = [], [root]
    while q:
        node = q.pop(0)
        s.append(node)
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    while s:
        print(s.pop().val, end=' ')


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right.left = Node(6)
tree.right.right = Node(7)
reverse_level_order(tree)
print()
reverse_level_order_stack(tree)
