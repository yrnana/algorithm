from geeksforgeeks.datastructure.binary_tree.binary_tree import Node, array_to_tree


def print_path(root, x):
    arr = []
    if has_path(root, arr, x):
        print(' -> '.join(list(map(str, arr))))


def has_path(node, arr, x):
    if not node:
        return False
    arr.append(node.val)
    if node.val == x:
        return True
    if has_path(node.left, arr, x) or has_path(node.right, arr, x):
        return True
    arr.pop()
    return False


tree = array_to_tree([1, 2, 3, 4, 5, 6, 7])
print_path(tree, 5)
