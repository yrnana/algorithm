from geeksforgeeks.datastructure.binary_tree.binary_tree import array_to_tree


def all_leaves(node):
    if node:
        all_leaves(node.left)
        if not node.left and not node.right:
            print(node.val, end=' ')
        all_leaves(node.right)


all_leaves(array_to_tree([1, 2, 3, 4, None, 5, 8, None, None, None, None, 6, 7, 9, 10]))
