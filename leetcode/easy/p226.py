# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        self.recursive(root)
        return root

    def recursive(self, node: TreeNode):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.recursive(node.left)
        self.recursive(node.right)
