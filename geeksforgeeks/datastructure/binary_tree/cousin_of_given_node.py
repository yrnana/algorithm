from geeksforgeeks.datastructure.binary_tree.binary_tree import Node, array_to_tree


def cousins(root, node):
    level = get_level(root, node, 1)
    level_node(root, node, level)


def get_level(root, node, level):
    if not root:
        return 0
    if root == node:
        return level
    down_level = get_level(root.left, node, level + 1)
    if down_level != 0:
        return down_level
    return get_level(root.right, node, level + 1)


def level_node(root, node, level):
    if not root or level < 2:
        return
    if level == 2:
        if root.left == node or root.right == node:
            return
        if root.left:
            print(root.left.val, end=' ')
        if root.right:
            print(root.right.val, end=' ')
    elif level > 2:
        level_node(root.left, node, level - 1)
        level_node(root.right, node, level - 1)


tree = array_to_tree([1, 2, 3, 4, 5, 6, 7])
cousins(tree, tree.left.right)
