class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        left = str(self.left.val) if self.left else 'None'
        right = str(self.right.val) if self.right else 'None'
        return '{ val: ' + str(self.val) + ', left: ' + left + ', right: ' + right + ' }'


def traversal(node):
    result = None
    if node:
        if node.val == 2:
            return node
        result = traversal(node.left)
        if result and result.val == 2:
            return result
        result = traversal(node.right)
        if result and result.val == 2:
            return result
    return result


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right = TreeNode(7)
    print(traversal(tree))
