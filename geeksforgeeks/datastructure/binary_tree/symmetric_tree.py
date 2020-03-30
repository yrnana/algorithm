from geeksforgeeks.datastructure.binary_tree.binary_tree import Node


def is_mirror(root1, root2):
    if not root1 and not root2:
        return True
    if root1 and root2:
        if root1.val == root2.val:
            return is_mirror(root1.left, root2.left) and is_mirror(root1.right, root1.right)
    return False


def is_symmetric(node):
    return is_mirror(node, node)


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print(is_symmetric(root))
