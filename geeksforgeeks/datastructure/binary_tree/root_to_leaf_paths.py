from geeksforgeeks.datastructure.binary_tree.binary_tree import Node, array_to_tree


def routes(stack, node):
    if not node:
        return
    stack.append(node.val)
    if not node.left and not node.right:
        print(stack)
    routes(stack, node.left)
    routes(stack, node.right)
    stack.pop()


print(routes([], array_to_tree([1, 2, 3, 4, 5])))
