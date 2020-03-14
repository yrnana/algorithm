class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        arr = [self.data]
        node = self.next
        while node:
            arr.append(node.data)
            node = node.next
        return '->'.join(list(map(str, arr)))


def list_to_linked(arr):
    head = Node(arr[0])
    node = head
    for x in arr[1:]:
        node.next = Node(x)
        node = node.next
    return head
