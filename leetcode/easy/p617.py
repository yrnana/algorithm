class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        left = str(self.left.val) if self.left else 'None'
        right = str(self.right.val) if self.right else 'None'
        return '{ val: ' + str(self.val) + ', left: ' + left + ', right: ' + right + ' }'


def traversal(node1, node2):
    if not node1:
        return node2
    if not node2:
        return node1
    result = TreeNode(node1.val + node2.val)
    result.left = traversal(node1.left, node2.left)
    result.right = traversal(node1.right, node2.right)
    return result


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.left.left = TreeNode(5)
    tree1.right = TreeNode(2)
    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.left.right = TreeNode(4)
    tree2.right = TreeNode(3)
    tree2.right.right = TreeNode(7)

    print(traversal(tree1, tree2))
