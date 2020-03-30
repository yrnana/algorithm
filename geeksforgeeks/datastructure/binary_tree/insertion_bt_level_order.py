from geeksforgeeks.datastructure.binary_tree.binary_tree import Node


def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val, end=' ')
    inorder(node.right)


def insert(node, key):
    q = [node]
    while q:  # level order
        x = q.pop(0)
        if not x.left:
            x.left = Node(key)
            break
        else:
            q.append(x.left)
        if not x.right:
            x.right = Node(key)
            break
        else:
            q.append(x.right)


root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)
inorder(root)
insert(root, 12)
print()
inorder(root)
