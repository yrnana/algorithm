from geeksforgeeks.datastructure.binary_tree.binary_tree import Node, array_to_tree


def sum_of_parent_of_x(root, x):
    s = [0]
    helper(root, s, x)
    return s[0]


def helper(node, s, x):
    if not node:
        return
    if (node.left and node.left.val == x) or (node.right and node.right.val == x):
        s[0] += node.val
    helper(node.left, s, x)
    helper(node.right, s, x)


tree = array_to_tree([4, 2, 5, 7, 2, 2, 3])
print(sum_of_parent_of_x(tree, 2))
