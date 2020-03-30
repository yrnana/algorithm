from geeksforgeeks.datastructure.binary_tree.binary_tree import Node


def boundary_traversal(root):
    if root:
        print(root.val, end=' ')
        boundary_left(root.left)
        print_leaves(root.left)
        print_leaves(root.right)
        boundary_right(root.right)


def boundary_left(node):
    if not node:
        return
    if node.left:
        print(node.val, end=' ')
        boundary_left(node.left)
    elif node.right:
        print(node.val, end=' ')
        boundary_left(node.right)


def boundary_right(node):
    if not node:
        return
    if node.right:
        print(node.val, end=' ')
        boundary_right(node.right)
    elif node.left:
        print(node.val, end=' ')
        boundary_right(node.left)


def print_leaves(node):
    if node:
        print_leaves(node.left)
        if not node.left and not node.right:
            print(node.val, end=' ')
        print_leaves(node.right)


tree = Node(20)
tree.left = Node(8)
tree.left.left = Node(4)
tree.left.right = Node(12)
tree.left.right.left = Node(10)
tree.left.right.right = Node(14)
tree.right = Node(22)
tree.right.right = Node(25)
boundary_traversal(tree)
