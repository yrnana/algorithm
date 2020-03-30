from geeksforgeeks.datastructure.binary_tree.binary_tree import Node


def replace_node(root):
    node = root
    stack = []
    arr = []
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            arr.append(node.val)
            node = node.right

    arr = [0] + arr + [0]
    s = 1
    node = root
    stack = []
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            node.val = arr[s - 1] + arr[s + 1]
            s += 1
            node = node.right


def inorder(node):
    if node:
        inorder(node.left)
        print(node.val, end=' ')
        inorder(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
inorder(root)
replace_node(root)
print()
inorder(root)
