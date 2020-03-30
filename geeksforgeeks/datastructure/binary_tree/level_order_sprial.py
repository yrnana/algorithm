from geeksforgeeks.datastructure.binary_tree.binary_tree import Node


def spiral(root):
    h = height(root)
    ltr = False
    for i in range(1, h + 1):
        level(root, i, ltr)
        ltr = not ltr


def height(node):
    if not node:
        return 0
    left = height(node.left)
    right = height(node.right)
    return max(left, right) + 1


def level(root, lvl, ltr):
    if not root:
        return
    if lvl == 1:
        print(root.val, end=' ')
        return
    if ltr:
        level(root.left, lvl - 1, ltr)
        level(root.right, lvl - 1, ltr)
    else:
        level(root.right, lvl - 1, ltr)
        level(root.left, lvl - 1, ltr)


tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(7)
tree.left.right = Node(6)
tree.right.left = Node(5)
tree.right.right = Node(4)
spiral(tree)
