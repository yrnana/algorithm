from geeksforgeeks.datastructure.binary_tree.binary_tree import Node


def preorder(node):
    if node:
        print(node.val, end=' ')
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=' ')
        inorder(node.right)


def inorder_wo_recursive(root):
    node = root
    stack = []
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            print(node.val, end=' ')
            node = node.right


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.val, end=' ')


tree = Node(1)
tree.left = Node(2)
tree.left.left = Node(4)
tree.left.right = Node(5)
tree.right = Node(3)
preorder(tree)
print()
inorder(tree)
print()
inorder_wo_recursive(tree)
print()
postorder(tree)
