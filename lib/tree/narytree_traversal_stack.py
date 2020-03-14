# https://leetcode.com/articles/introduction-to-n-ary-trees/

# tree = TreeNode('A', [])
# tree.children.append(TreeNode('B', []))
# tree.children.append(TreeNode('C', []))
# tree.children.append(TreeNode('D', []))
# tree.children[1].children.append(TreeNode('E', []))
# tree.children[1].children.append(TreeNode('F', []))
# tree.children[2].children.append(TreeNode('G', []))


# A B C E F D G
def pre_order(root):
    stack = [root]
    while any(stack):
        node = stack.pop(0)
        print(node.val, end=" ")
        stack = node.children + stack


# B E F C G D A
def post_order(root):
    s1 = [root]
    s2 = []
    while any(s1):
        node = s1.pop()
        s2.append(node)
        s1 += node.children
    while s2:
        node = s2.pop()
        print(node.val, end=" ")


# A B C D E F G
def level_order(root):
    stack = [root]
    while any(stack):
        for i in range(len(stack)):
            node = stack.pop(0)
            print(node.val, end=" ")
            stack += node.children
