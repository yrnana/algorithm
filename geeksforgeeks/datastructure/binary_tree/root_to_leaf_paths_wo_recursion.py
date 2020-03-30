from geeksforgeeks.datastructure.binary_tree.binary_tree import Node, array_to_tree


def print_path(node, parent):
    stack = []
    while node:
        stack.append(str(node.val))
        node = parent[node]
    print('->'.join(reversed(stack)))


def paths(root):
    if not root:
        return
    stack = [root]
    parent = {root: None}
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            print_path(node, parent)
            continue
        if node.right:
            parent[node.right] = node
            stack.append(node.right)
        if node.left:
            parent[node.left] = node
            stack.append(node.left)


paths(array_to_tree([6, 3, 5, 2, 5, None, 4, None, None, 7, 4]))
