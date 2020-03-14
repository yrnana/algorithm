class Node:
	def __init__(self, val, children):
		self.val = val
		self.children = children


root = Node(1, [])
root.children.append(Node(3, []))
root.children.append(Node(2, []))
root.children.append(Node(4, []))
root.children[0].children.append(Node(5, []))
root.children[0].children.append(Node(6, []))


stack = [root]
visited = []
while any(stack):
	node = stack.pop(0)
	visited.append(node.val)
	stack = node.children + stack
print(visited)

