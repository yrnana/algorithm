from .narytree import *


# tree = TreeNode('A', [])
# tree.children.append(TreeNode('B', []))
# tree.children.append(TreeNode('C', []))
# tree.children.append(TreeNode('D', []))
# tree.children[1].children.append(TreeNode('E', []))
# tree.children[1].children.append(TreeNode('F', []))
# tree.children[2].children.append(TreeNode('G', []))


# A B C E F D G
def pre_order(node) -> TreeNode:
	if node:
		print(node.val, end=" ")
		for x in node.children:
			pre_order(x)


# B E F C G D A
def post_order(node) -> TreeNode:
	if node:
		for x in node.children:
			post_order(x)
		print(node.val, end=" ")


def max_depth(root) -> int:
	if not root:
		return 0
	d = 0
	for node in root.children:
		d = max(d, max_depth(node))
	return d + 1
