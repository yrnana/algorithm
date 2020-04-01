from geeksforgeeks.datastructure.binary_tree.binary_tree import Node, array_to_tree


def solution(root, low, high):
    if not root:
        return
    level = 1
    marker = Node(None)
    queue = [root, marker]
    while queue:
        node = queue.pop(0)
        if node == marker:
            if level >= low:
                print()
            level += 1
            if not queue or level > high:
                break
            queue.append(marker)
            continue
        if level >= low:
            print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


solution(array_to_tree([20, 8, 22, 4, 12, None, None, None, None, 10, 14]), 2, 3)
