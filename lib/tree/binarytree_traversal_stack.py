# https://en.wikipedia.org/wiki/Tree_traversal

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
def pre_order(root):
    stack = [root]
    while any(stack):
        node = stack.pop(0)
        print(node.val, end=" ")
        if node.right:
            stack.insert(0, node.right)
        if node.left:
            stack.insert(0, node.left)


# A B C D E F G H I
def in_order(root):
    node = root
    stack = []
    while True:
        if node:
            stack.append(node)
            node = node.left
        elif stack:
            node = stack.pop()
            print(node.val, end=" ")
            node = node.right
        else:
            break


# A C E D B H I G F
def post_order(root):
    s1 = [root]
    s2 = []
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    while s2:
        node = s2.pop()
        print(node.val, end=" ")


# F B G A D I C E H
def level_order(root):
    stack = [root]
    while any(stack):
        for i in range(len(stack)):
            node = stack.pop(0)
            print(node.val, end=" ")
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
