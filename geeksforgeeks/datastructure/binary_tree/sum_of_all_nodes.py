from geeksforgeeks.datastructure.binary_tree.binary_tree import Node


def sum_of_all_nodes(root):
    if not root:
        return 0
    return root.val + sum_of_all_nodes(root.left) + sum_of_all_nodes(root.right)


tree = Node(8)
tree.left = Node(3)
tree.right = Node(10)
tree.left.left = Node(1)
tree.left.right = Node(6)
tree.right.right = Node(14)
tree.right.right.left = Node(13)
tree.left.right.left = Node(4)
tree.left.right.right = Node(7)
print(sum_of_all_nodes(tree))
