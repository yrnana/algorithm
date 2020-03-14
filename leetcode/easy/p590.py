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


s1 = [root]
s2 = []
while any(s1):
	node = s1.pop()
	s2.append(node)
	s1 += node.children
print(list(map(lambda x: x.val, reversed(s2))))
