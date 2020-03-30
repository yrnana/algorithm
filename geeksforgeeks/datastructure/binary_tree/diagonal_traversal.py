from geeksforgeeks.datastructure.binary_tree.binary_tree import Node
from collections import defaultdict


def diagonal_traversal(root):
    diagonal_map = defaultdict(list)
    diagonal_util(root, 0, diagonal_map)
    for k, v in diagonal_map.items():
        print(k, v)


def diagonal_util(node, d, dmap):
    if not node:
        return
    dmap[d].append(node.val)
    diagonal_util(node.left, d + 1, dmap)
    diagonal_util(node.right, d, dmap)


tree = Node(8)
tree.left = Node(3)
tree.right = Node(10)
tree.left.left = Node(1)
tree.left.right = Node(6)
tree.right.right = Node(14)
tree.right.right.left = Node(13)
tree.left.right.left = Node(4)
tree.left.right.right = Node(7)
diagonal_traversal(tree)
