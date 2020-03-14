from .binarytree import *


# tree = TreeNode('F')
# tree.left = TreeNode('B')
# tree.right = TreeNode('G')
# tree.left.left = TreeNode('A')
# tree.left.right = TreeNode('D')
# tree.left.right.left = TreeNode('C')
# tree.left.right.right = TreeNode('E')
# tree.right.right = TreeNode('I')
# tree.right.right.left = TreeNode('H')


# F B A D C E G I H
def pre_order(node) -> TreeNode:
    if node:
        print(node.val, end=" ")
        pre_order(node.left)
        pre_order(node.right)


# A B C D E F G H I
def in_order(node) -> TreeNode:
    if node:
        in_order(node.left)
        print(node.val, end=" ")
        in_order(node.right)


# A C E D B H I G F
def post_order(node) -> TreeNode:
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.val, end=" ")
