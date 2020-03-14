class BinaryTree:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def print_tree(self):
		if self.left:
			self.left.print_tree()
		print(self.data, end=' ')
		if self.right:
			self.right.print_tree()


def solution(tree):
	new_tree = BinaryTree(-1)
	recursive(tree, new_tree)
	return new_tree


def recursive(node, new_tree):
	new_tree.data = node.data
	if node.right:
		new_tree.left = BinaryTree(-1)
		recursive(node.right, new_tree.left)
	if node.left:
		new_tree.right = BinaryTree(-1)
		recursive(node.left, new_tree.right)


root = BinaryTree(0)
root.left = BinaryTree(7)
root.left.left = BinaryTree(2)
root.left.right = BinaryTree(6)
root.left.right.left = BinaryTree(5)
root.left.right.right = BinaryTree(11)
root.right = BinaryTree(5)
root.right.right = BinaryTree(9)
root.right.right.left = BinaryTree(4)
root.print_tree()  # 2 7 5 6 11 0 5 4 9
print()
solution(root).print_tree()  # 9 4 5 0 11 6 5 7 2

# print()
# test = BinaryTree(0)
# test.left = BinaryTree(5)
# test.left.left = BinaryTree(9)
# test.left.left.right = BinaryTree(4)
# test.right = BinaryTree(7)
# test.right.left = BinaryTree(6)
# test.right.right = BinaryTree(2)
# test.right.left.left = BinaryTree(11)
# test.right.left.right = BinaryTree(5)
# test.print_tree()
