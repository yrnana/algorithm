from lib.linkedlist import Node, list_to_linked


def solution(list1, list2):
	head = Node(-1)
	node = head
	node1 = list1
	node2 = list2
	while node1 and node2:
		if node1.data < node2.data:
			node.next = Node(node1.data)
			node = node.next
			node1 = node1.next
		elif node1.data == node2.data:
			node.next = Node(node1.data)
			node.next.next = Node(node2.data)
			node = node.next.next
			node1 = node1.next
			node2 = node2.next
		else:
			node.next = Node(node2.data)
			node = node.next
			node2 = node2.next
	if node1:
		node.next = node1
	elif node2:
		node.next = node2
	return head.next


print(solution(list_to_linked([1, 2, 3]), list_to_linked([1, 2, 3])))
print(solution(list_to_linked([1, 3, 5, 6]), list_to_linked([2, 4])))
