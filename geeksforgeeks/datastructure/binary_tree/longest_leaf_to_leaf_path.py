from geeksforgeeks.datastructure.binary_tree.binary_tree import Node, array_to_tree


class P:
    def __init__(self, x):
        self.v = x


def height(node, longest, lh, rh, curr):
    if not node:
        return 0
    left = height(node.left, longest, lh, rh, curr)
    right = height(node.right, longest, lh, rh, curr)
    if longest.v < 1 + left + right:
        longest.v = 1 + left + right  # longest path
        lh.v = left  # left height
        rh.v = right  # right height
        curr.v = node  # current root
    return max(left, right) + 1


def diameter(root):
    if not root:
        return
    longest, lh, rh, node = P(0), P(0), P(0), P(None)
    height(root, longest, lh, rh, node)
    node = node.v
    return longest_path(node.left)[::-1] + [node.val] + longest_path(node.right)


def longest_path(root):
    if root is None:
        return []
    left_path = [root.val] + longest_path(root.left)
    right_path = [root.val] + longest_path(root.right)
    return left_path if len(left_path) > len(right_path) else right_path


tree = array_to_tree([1, 2, 3, 4, 5, None, None, None, 8, 6, 7, None, None, None, None, None, None, 9])
print(diameter(tree))
