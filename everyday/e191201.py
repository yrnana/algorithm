from lib.linkedlist import list_to_linked


def solution(head, N):
    tmp = []
    node = head
    while node:
        tmp.append(node)
        node = node.next
    i = len(tmp) - N
    if i == 0:
        return head.next
    tmp[i - 1].next = tmp[i].next
    return head


print(solution(list_to_linked([1, 2, 3, 4, 5]), 2))
print(solution(list_to_linked([1, 2, 3]), 3))
print(solution(list_to_linked([1]), 1))
