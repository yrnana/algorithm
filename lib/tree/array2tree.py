from .binarytree import *


def array_to_tree_recursive(li, root, i, n):
    if i < n and li[i] is not None:
        temp = TreeNode(li[i])
        root = temp
        root.left = array_to_tree_recursive(li, root.left, 2 * i + 1, n)
        root.right = array_to_tree_recursive(li, root.right, 2 * i + 2, n)
    return root


def array_to_tree(li):
    return array_to_tree_recursive(li, None, 0, len(li))
