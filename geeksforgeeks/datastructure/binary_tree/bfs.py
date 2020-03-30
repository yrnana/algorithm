# bfs = level order
from geeksforgeeks.datastructure.binary_tree.binary_tree import Node


def bfs(node):
    q = [node]
    while q:
        x = q.pop(0)
        print(x.val, end=' ')
        if x.left:
            q.append(x.left)
        if x.right:
            q.append(x.right)


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
bfs(root)
