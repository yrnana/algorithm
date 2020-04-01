from geeksforgeeks.datastructure.binary_tree.binary_tree import array_to_tree


def k_distance(root, k):
    if not root:
        return
    if k == 0:
        print(root.val)
    else:
        k_distance(root.left, k - 1)
        k_distance(root.right, k - 1)


k_distance(array_to_tree([1, 2, 3, 4, 5, 8]), 2)
